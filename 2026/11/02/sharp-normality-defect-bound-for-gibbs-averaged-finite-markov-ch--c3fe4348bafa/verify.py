"""Exact-rational sanity checks for weighted normal-chain Gibbs averaging.

Run with Python 3 standard library; finite checks support, but do not replace,
the operator-theoretic proof for arbitrary finite state spaces and all times.
"""
from fractions import Fraction as F

CHECKS = 0

def check(cond, label):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(label)

def zero(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]

def ident(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]

def trans(a):
    return list(map(list, zip(*a)))

def mul(a, b):
    bt = trans(b)
    return [[sum((x*y for x,y in zip(row,col)), F(0)) for col in bt] for row in a]

def power(a, t):
    n=len(a)
    x=ident(n)
    for _ in range(t):
        x=mul(x,a)
    return x

def sub(a,b):
    return [[v-w for v,w in zip(x,y)] for x,y in zip(a,b)]

def pi_kernel(pi):
    return [pi[:] for _ in pi]

def adj(a,pi):
    n=len(pi)
    return [[pi[j]*a[j][i]/pi[i] for j in range(n)] for i in range(n)]

def norm_sq(a,pi):
    return sum((pi[i]*a[i][j]**2/pi[j] for i in range(len(pi)) for j in range(len(pi))),F(0))

def gibbs(pi, groups):
    n=len(pi)
    out=zero(n)
    for group in groups:
        total=sum((pi[i] for i in group),F(0))
        for i in group:
            for j in group:
                out[i][j]=pi[j]/total
    return out

def circ(weights):
    n=len(weights)
    total=sum(weights)
    row=[F(w,total) for w in weights]
    return [[row[(j-i)%n] for j in range(n)] for i in range(n)]

def kron(a,b):
    return [[a[i//len(b)][j//len(b)]*b[i%len(b)][j%len(b)] for j in range(len(a)*len(b))] for i in range(len(a)*len(b))]

def partitions(n):
    # Every unlabeled set partition exactly once, through restricted growth labels.
    def walk(labels, top):
        if len(labels)==n:
            yield [[i for i,x in enumerate(labels) if x==j] for j in range(top+1)]
        else:
            for lab in range(top+2):
                yield from walk(labels+[lab],max(top,lab))
    yield from walk([0],0)

def validate_chain(P, pi, families, max_t=7):
    n=len(pi)
    I=ident(n)
    Pi=pi_kernel(pi)
    check(sum(pi)==1,'pi normalized')
    check(all(v>0 for v in pi),'positive pi')
    check(all(sum(row)==1 for row in P),'stochastic')
    check(all(all(x>=0 for x in row) for row in P),'positive entries')
    check(all(sum((pi[i]*P[i][j] for i in range(n)),F(0))==pi[j] for j in range(n)), 'stationarity')
    check(mul(P,adj(P,pi))==mul(adj(P,pi),P), 'weighted normality')
    for blocks in families:
        G=gibbs(pi,blocks)
        Q=mul(mul(G,P),G)
        check(mul(G,G)==G,'G projection')
        check(adj(G,pi)==G,'G self-adjoint')
        check(mul(G,Pi)==Pi and mul(Pi,G)==Pi,'G fixes stationary constants')
        check(all(sum(row)==1 for row in Q),'Q stochastic')
        check(all(sum((pi[i]*Q[i][j] for i in range(n)),F(0))==pi[j] for j in range(n)), 'Q stationary')
        check(norm_sq(sub(P,Pi),pi)==norm_sq(sub(Q,Pi),pi)+norm_sq(sub(P,Q),pi), 'Pythagorean equality')
        for t in range(1,max_t+1):
            err_P=norm_sq(sub(power(P,t),Pi),pi)
            err_Q=norm_sq(sub(power(Q,t),Pi),pi)
            check(err_Q<=err_P,'all-time improvement')
            check((err_Q==err_P)==(P==Q),'strict equality characterization')
            improvement=norm_sq(sub(P,Q),pi)**t/F((n-1)**(t-1))
            check(err_Q+improvement<=err_P,'quantitative all-time gap')


def main():
    # Directed circulants include nonreversible normal chains.
    for n in (3,4,5):
        pi=[F(1,n)]*n
        for base in (1,2,3):
            weights=[base+i*(i+1) for i in range(n)]
            P=circ(weights)
            validate_chain(P,pi,partitions(n),max_t=6)

    # The explicitly described nonreversible three-state chain.
    P=circ([3,2,1]); pi=[F(1,3)]*3
    G=gibbs(pi,[[0,1],[2]])
    Q=mul(mul(G,P),G)
    check(P!=trans(P),'3-state chain nonreversible')
    for t in range(1,13):
        check(norm_sq(sub(power(P,t),pi_kernel(pi)),pi)==2*F(1,12)**t, 'three-state exact baseline formula')
        check(norm_sq(sub(power(Q,t),pi_kernel(pi)),pi)==F(1,16)**t, 'three-state exact compressed formula')

    # A normal directed four-cycle becomes nonnormal after Gibbs averaging.
    P=[[F(1,2) if i==j or j==(i+1)%4 else F(0) for j in range(4)] for i in range(4)]
    pi=[F(1,4)]*4
    G=gibbs(pi,[[0,1],[2],[3]])
    Q=mul(mul(G,P),G)
    check(P!=trans(P),'four-state directed chain')
    check(mul(P,trans(P))==mul(trans(P),P),'four-state normality')
    check(mul(Q,trans(Q))!=mul(trans(Q),Q),'compressed chain nonnormal')
    comm=sub(mul(Q,trans(Q)),mul(trans(Q),Q))
    check(comm[0][2]==-F(1,16),'nonnormal commutator entry')
    # The single example has structural zero entries, but is primitive.
    for t in range(1,9):
        check(norm_sq(sub(power(P,t),pi_kernel(pi)),pi)==2*F(1,2)**t,'four-state exact baseline')
        check(norm_sq(sub(power(Q,t),pi_kernel(pi)),pi)<2*F(1,2)**t,'four-state strict comparison')

    # A nonuniform invariant distribution and a nonreversible normal product chain.
    R=[[F(3,4),F(1,4)],[F(1,2),F(1,2)]]
    C=circ([3,2,1])
    P=kron(R,C)
    pi=[F(2,9)]*3+[F(1,9)]*3
    check(P!=adj(P,pi),'six-state product is nonreversible')
    blocks_list=[[[0,1,3],[2,4,5]], [[0,3],[1,4],[2,5]], [[0,1],[2,3,4,5]], [[0],[1,2,3],[4,5]],[[0,1,2],[3,4,5]]]
    validate_chain(P,pi,blocks_list,max_t=10)
    # Explicit general, nonnormal second-time commutator budget.
    for n in (3,4):
        I=ident(n)
        S=[[F(j==(i+1)%n) for j in range(n)] for i in range(n)]
        H=ident(n)
        H[0],H[1]=H[1],H[0]
        Pi=[[F(1,n)]*n for _ in range(n)]
        P=[[F(1,10)*I[i][j]+F(3,10)*H[i][j]+F(1,2)*S[i][j]+F(1,10)*Pi[i][j]
            for j in range(n)] for i in range(n)]
        pi=[F(1,n)]*n
        check(P!=adj(P,pi),'nonreversible nonnormal witness')
        check(mul(P,adj(P,pi))!=mul(adj(P,pi),P),'witness nonnormal')
        for blocks in partitions(n):
            G=gibbs(pi,blocks)
            Q=mul(mul(G,P),G)
            comm=sub(mul(adj(P,pi),P),mul(P,adj(P,pi)))
            second_defect=F(1,2)*norm_sq(comm,pi)
            gap=norm_sq(sub(P,Q),pi)**2/(n-1)
            lhs=norm_sq(sub(power(Q,2),Pi),pi)
            rhs=norm_sq(sub(power(P,2),Pi),pi)+second_defect-gap
            check(lhs<=rhs,'universal nonnormal second-time bound')

    # The factor (N-1)^(t-1) is sharp for full averaging.
    for n in range(2,8):
        pi=[F(1,n)]*n
        Pi=pi_kernel(pi)
        for r in (F(1,3),F(2,3)):
            I=ident(n)
            P=[[r*I[i][j]+(1-r)*Pi[i][j] for j in range(n)] for i in range(n)]
            Q=Pi
            for t in range(1,10):
                original=norm_sq(sub(power(P,t),Pi),pi)
                gap=norm_sq(sub(P,Q),pi)**t/F((n-1)**(t-1))
                check(original==gap,'sharp quantitative-gap coefficient')

    print('OK: %d exact-rational assertions passed.'%CHECKS)
    print('Finite verifications are not a proof of the all-size, all-time theorem.')

if __name__=='__main__':
    main()
