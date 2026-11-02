"""Independent GF(2) checks for single-corner feedback on square grids.

Run: python3 corner_grid_verify.py
Uses Python's arbitrary-precision bit vectors, no external packages.
"""
from itertools import product


def construct(side, feedback):
    masks = []
    for i in range(side):
        for j in range(side):
            nbr = []
            if i: nbr.append((i-1)*side+j)
            if i+1<side: nbr.append((i+1)*side+j)
            if j: nbr.append(i*side+j-1)
            if j+1<side: nbr.append(i*side+j+1)
            if feedback and i==0 and j==0: nbr.append(0)
            masks.append(sum(1 << v for v in nbr))
    return masks


def step(x,masks):
    y=0
    for i,mask in enumerate(masks):
        y |= ((x & mask).bit_count() & 1) << i
    return y


def rank_gf2(columns):
    pivots={}
    for value in columns:
        while value:
            leading=value.bit_length()-1
            if leading in pivots:
                value ^= pivots[leading]
            else:
                pivots[leading]=value
                break
    return len(pivots)


def predicted_rank(a,k,feedback):
    L=1<<a
    dim=(L-1)**2
    if k==0:return dim
    if not feedback:return (L-2)*max(L-k,0)
    if k<=L:return (L-2)*(L-k)+k
    return max(2*L-k,1)


def ranks_check(a):
    L=1<<a
    side=L-1
    dim=side**2
    for feedback in [False,True]:
        masks=construct(side,feedback)
        columns=[1 << i for i in range(dim)]
        for k in range(2*L+2):
            got=rank_gf2(columns)
            want=predicted_rank(a,k,feedback)
            assert got==want,(a,k,feedback,got,want)
            columns=[step(v,masks) for v in columns]
    return dim


def exhaustive_three_by_three():
    a=2; L=4; side=3; dim=9
    masks=construct(side,True)
    observed=[0]*(2*L)
    for initial in range(1<<dim):
        state=initial
        history={}
        trajectory=[]
        while state not in history:
            history[state]=len(trajectory)
            trajectory.append(state)
            state=step(state,masks)
        first=history[state]
        period=len(trajectory)-first
        assert period==1,(initial,period)
        observed[first]+=1
    cumulative=0
    for t,count in enumerate(observed):
        cumulative+=count
        rank=predicted_rank(a,t,True)
        expected=1 << (dim+1-rank)
        assert cumulative==expected,(t,cumulative,expected)
    assert observed==[2,6,8,16,32,64,128,256]
    return observed


def randomized_trajectory_check():
    a=3; L=8; side=7
    masks=construct(side,True)
    dim=side**2
    state=0x123456789abcdef
    mask=(1<<dim)-1
    for sample in range(4000):
        state=(1103515245*state+12345)&mask
        initial=state
        value=initial
        for t in range(2*L-1):
            value=step(value,masks)
        assert step(value,masks)==value,(sample,value)
        if sample<1000:
            assert step(step(value,masks),masks)==value
    return 4000


def main():
    sizes=[]
    for a in (2,3,4,5):
        sizes.append((a,ranks_check(a)))
    observed=exhaustive_three_by_three()
    trials=randomized_trajectory_check()
    print('RANK_CASES_OK',sizes)
    print('EXHAUSTIVE_3x3_ENTRY_COUNTS_OK',observed)
    print('RANDOMIZED_7x7_TERMINAL_TRAJECTORIES_OK',trials)
    print('CORNER_GRID_FEEDBACK_VERIFY_OK')


if __name__=='__main__':
    main()
