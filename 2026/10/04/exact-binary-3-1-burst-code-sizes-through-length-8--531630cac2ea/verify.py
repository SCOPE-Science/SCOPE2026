from itertools import product

EXPECTED={3:1,4:1,5:2,6:2,7:4,8:8}
WITNESSES={
3:['111'],
4:['1111'],
5:['11111','00100'],
6:['111111','100100'],
7:['1111111','1010100','0110010','0011001'],
8:['11111111','11010100','10101010','10000001','01110010','01011001','00111000','00010011'],
}

def ball_slice(w):
    n=len(w)
    return {w[:i]+b+w[i+3:] for i in range(n-2) for b in '01'}

def ball_loop(w):
    n=len(w); out=set()
    for i in range(n-2):
        for b in '01':
            z=[]
            for j in range(n-2):
                if j<i: z.append(w[j])
                elif j==i: z.append(b)
                else: z.append(w[j+2])
            out.add(''.join(z))
    return out

def graph(n):
    words=[''.join(p) for p in product('01',repeat=n)]
    balls=[]
    for w in words:
        a=ball_slice(w); b=ball_loop(w)
        assert a==b,(n,w,a,b)
        assert len(a)==n-1,(n,w,len(a))
        balls.append(a)
    N=len(words); adj=[0]*N
    for i in range(N):
        for j in range(i+1,N):
            if balls[i].isdisjoint(balls[j]):
                adj[i]|=1<<j; adj[j]|=1<<i
    return words,balls,adj

def color_sort(P,adj):
    # Greedily partition the candidate subgraph into independent color classes.
    # The number of classes is therefore an upper bound on any clique.
    order=[]; colors=[]; rem=P; color=0
    while rem:
        color += 1
        avail=rem
        while avail:
            lsb=avail & -avail
            v=lsb.bit_length()-1
            order.append(v); colors.append(color)
            rem &= ~lsb
            avail &= ~lsb
            avail &= ~adj[v]
    return order,colors

def maximum_clique(adj):
    N=len(adj); best=[]; nodes=0
    def expand(R,P):
        nonlocal best,nodes
        nodes+=1
        if not P:
            if len(R)>len(best): best=R[:]
            return
        order,colors=color_sort(P,adj)
        for k in range(len(order)-1,-1,-1):
            if len(R)+colors[k] <= len(best):
                return
            v=order[k]
            bit=1<<v
            if not (P&bit):
                continue
            expand(R+[v], P & adj[v])
            P &= ~bit
    expand([], (1<<N)-1)
    return best,nodes

def check_witness(ws):
    bs=[ball_loop(w) for w in ws]
    return all(bs[i].isdisjoint(bs[j]) for i in range(len(bs)) for j in range(i+1,len(bs)))

def main():
    vals=[]
    for n in range(3,9):
        words,balls,adj=graph(n)
        best,nodes=maximum_clique(adj)
        m=len(best); vals.append(m)
        assert m==EXPECTED[n],(n,m,best)
        assert check_witness(WITNESSES[n]),n
        assert len(WITNESSES[n])==m
        sphere=(2**(n-2))//(n-1)
        assert m<=sphere
        print(f'n={n} max={m} nodes={nodes} sphere={sphere} witness={",".join(WITNESSES[n])}')
    print('VERIFY_OK profile='+','.join(map(str,vals)))

if __name__=='__main__': main()
