"""Finite independent verification of a Frobenius-adjoint Heyting-algebra census."""
from itertools import product


def height_two(a,b):
    u=(1<<b)-1
    top=(1<<(a+b))-1
    vals=list(range(1<<b))+[u|(v<<b) for v in range(1,1<<a)]
    def imp(x,y):
        d=x & ~y
        return (u & ~d) if (d & u) else (top & ~d)
    return vals,imp


def bell(n):
    r=[1]
    for i in range(1,n+1):
        r.append(sum(__import__('math').comb(i-1,k)*r[k] for k in range(i)))
    return r[n]


def check_axioms(vals,imp,f,g):
    for x in vals:
        if f[x] & x != f[x]:
            return False
        for y in vals:
            if ((g[x]&y)==g[x]) != ((x&f[y])==x):
                return False
            if f[imp(g[x],y)] != imp(g[x],f[y]):
                return False
            if f[g[x]|y] != (g[x]|f[y]):
                return False
            if g[x & g[y]] != (g[x]&g[y]):
                return False
    return True


def subalgebras_count(a,b):
    vals,imp=height_two(a,b)
    count=0
    for mask in range(1<<(len(vals)-2)):
        image=[vals[0],vals[-1]]+[v for j,v in enumerate(vals[1:-1]) if mask>>j&1]
        ss=set(image)
        if any((x|y) not in ss or (x&y) not in ss for x in image for y in image):
            continue
        f={x:max((s for s in image if (s&x)==s),key=int.bit_count) for x in vals}
        g={x:min((s for s in image if (s|x)==s),key=int.bit_count) for x in vals}
        if check_axioms(vals,imp,f,g):
            count+=1
    return count


def direct_f_count(a,b):
    vals,imp=height_two(a,b)
    bottom,top=vals[0],vals[-1]
    domain=[v for v in vals if v!=top]
    choices=[[s for s in vals if (s&x)==s] for x in domain]
    count=0
    candidates=0
    for values in product(*choices):
        f=dict(zip(domain,values));f[top]=top
        if any(f[x&y] != (f[x]&f[y]) for x in vals for y in vals):
            continue
        candidates+=1
        g={x: min((y for y in vals if (x&f[y])==x),key=int.bit_count) for x in vals}
        if check_axioms(vals,imp,f,g):
            count+=1
    return candidates,count


def main():
    for a,b in [(1,1),(1,2),(2,1),(1,3),(3,1),(2,2),(2,3),(3,2),(3,3)]:
        expect=1+bell(a)*bell(b)
        observed=subalgebras_count(a,b)
        assert observed==expect,(a,b,observed,expect)
        print('image enumeration',a,b,observed)
    for a,b in [(1,1),(1,2),(2,1),(2,2),(2,3)]:
        candidates,observed=direct_f_count(a,b)
        expect=1+bell(a)*bell(b)
        assert observed==expect,(a,b,candidates,observed,expect)
        print('independent unary-function enumeration',a,b,candidates,observed)
    print('ALL_CHECKS_OK')


if __name__=='__main__':
    main()
