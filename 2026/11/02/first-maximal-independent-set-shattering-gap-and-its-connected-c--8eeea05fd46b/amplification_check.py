#!/usr/bin/env python3
"""Check the connected cograph amplification at its first two orders."""
from verify import maximal_stable_sets,vc_dimension,littlestone_dimension,has_induced_p4
F=((0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3))

def G(m):
    u=5*m
    e=[]
    for i in range(m):
        e += [(5*i+a,5*i+b) for a,b in F]
    e += [(x,u) for x in range(u)]
    return 5*m+1,tuple(e)

def main():
    for m in (1,2):
        n,edges=G(m)
        H=maximal_stable_sets(n,edges)
        assert len(H)==4**m+1
        assert not has_induced_p4(n,edges)
        v=vc_dimension(n,H);l=littlestone_dimension(n,H)
        assert (v,l)==(m,2*m)
        print('AMPLIFICATION',m,'VERTICES',n,'CONCEPTS',len(H),'VC',v,'LD',l)
    print('CONNECTED_COGRAPH_AMPLIFICATION_PASS')

if __name__=='__main__':main()
