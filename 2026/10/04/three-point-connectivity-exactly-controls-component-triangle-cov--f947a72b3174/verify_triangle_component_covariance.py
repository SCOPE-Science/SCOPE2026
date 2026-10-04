#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, product

def components(n, edges):
    adj=[[] for _ in range(n)]
    for a,b in edges:
        adj[a].append(b)
        adj[b].append(a)
    seen=[False]*n
    c=0
    labels=[None]*n
    for i in range(n):
        if not seen[i]:
            stack=[i]
            seen[i]=True
            labels[i]=c
            while stack:
                x=stack.pop()
                for y in adj[x]:
                    if not seen[y]:
                        seen[y]=True
                        labels[y]=c
                        stack.append(y)
            c+=1
    return c,labels

def triangles(n,E):
    E=set(tuple(sorted(e)) for e in E)
    out=[]
    for t in combinations(range(n),3):
        if all(tuple(sorted(e)) in E for e in combinations(t,2)):
            out.append(t)
    return out

def exact_law(n,E,p):
    E=[tuple(sorted(e)) for e in E]
    tri=triangles(n,E)
    m=len(E)
    EK=ET=ER=EKT=ERT=Fraction(0)
    state_count=0
    for bits in product((0,1), repeat=m):
        k=sum(bits)
        pr=(p**k)*((1-p)**(m-k))
        A=[E[i] for i,b in enumerate(bits) if b]
        Aset=set(A)
        K,_=components(n,A)
        T=sum(
            int(all(tuple(sorted(e)) in Aset for e in combinations(t,2)))
            for t in tri
        )
        R=k-n+K
        EK+=pr*K
        ET+=pr*T
        ER+=pr*R
        EKT+=pr*K*T
        ERT+=pr*R*T
        state_count+=1
    return tri,EKT-EK*ET,ERT-ER*ET,state_count

def connectivity_probabilities(n,E,t,p):
    tri_edges=set(tuple(sorted(e)) for e in combinations(t,2))
    rest=[tuple(sorted(e)) for e in E if tuple(sorted(e)) not in tri_edges]
    p2=p3=Fraction(0)
    states=0
    for bits in product((0,1), repeat=len(rest)):
        k=sum(bits)
        pr=(p**k)*((1-p)**(len(rest)-k))
        A=[rest[i] for i,b in enumerate(bits) if b]
        _,lab=components(n,A)
        c=len({lab[x] for x in t})
        if c==2:
            p2+=pr
        elif c==3:
            p3+=pr
        states+=1
    return p2,p3,states

def check_graph(n,E,p):
    tri,covK,covR,states=exact_law(n,E,p)
    rhsK=Fraction(0)
    rhsR=Fraction(0)
    connectivity_states=0
    for t in tri:
        p2,p3,s=connectivity_probabilities(n,E,t,p)
        connectivity_states+=s
        rhsK += -(p**3)*((1-p)**2)*(p2+(p+2)*p3)
        rhsR += (p**3)*(1-p)*(3-(1-p)*p2-(1-p)*(p+2)*p3)

    assert covK==rhsK
    assert covR==rhsR

    if tri:
        assert covK<0
        lo=len(tri)*(p**3)*(1-p)*(1+p+p*p)
        hi=3*len(tri)*(p**3)*(1-p)
        assert lo<=covR<=hi
        assert covR>0
    else:
        assert covK==0
        assert covR==0

    return len(tri),states,connectivity_states

def run():
    graphs=[]

    # Single triangle with a tail.
    graphs.append((4,[(0,1),(1,2),(0,2),(2,3)]))

    # Two triangles sharing an edge.
    graphs.append((4,[(0,1),(1,2),(0,2),(0,3),(1,3)]))

    # Two triangles sharing one vertex plus a cross edge.
    graphs.append((5,[(0,1),(1,2),(0,2),(0,3),(3,4),(0,4),(2,3)]))

    # Complete graphs.
    graphs.append((4,list(combinations(range(4),2))))
    graphs.append((5,list(combinations(range(5),2))))

    # Triangle-free control.
    graphs.append((5,[(0,1),(1,2),(2,3),(3,4),(4,0)]))

    ps=[Fraction(1,4),Fraction(2,5),Fraction(3,5)]
    graph_parameter_checks=0
    percolation_states=0
    connectivity_states=0
    triangle_instances=0

    for n,E in graphs:
        for p in ps:
            nt,s,cs=check_graph(n,E,p)
            graph_parameter_checks+=1
            percolation_states+=s
            connectivity_states+=cs
            triangle_instances+=nt

    print(
        "VERIFY_OK "
        f"graph_parameter_checks={graph_parameter_checks} "
        f"percolation_states={percolation_states} "
        f"connectivity_states={connectivity_states} "
        f"triangle_instances={triangle_instances}"
    )

if __name__=="__main__":
    run()
