# An infinite Young-graph isomorphism conjecture for reverse multiples

## Finding
For every integer \(m\ge3\), put \(g=m^2-1\) and \(k=m^2-m-1\). The Young graph of base-\(g\), multiplier-\(k\) reverse multiples, including its distinguished start vertex and its even- and odd-pivot markings, is isomorphic to the Young graph \(Y(8,5)\):
\[
Y(m^2-1,m^2-m-1)\cong Y(8,5)\qquad(m\ge3).
\]
This proves the isomorphism asserted in Conjecture 39 of Kendrick (2015). The isomorphism concerns the carry-pair graph and pivot markings; edge digit labels depend on \(m\) and are not claimed to be identical.

## Assumptions and scope
A base-\(g\) reverse multiple is an integer whose base-\(g\) digits are reversed by multiplication by \(k\), with \(2\le k<g\). The carry-pair graph \(H(g,k)\) has a distinguished starting vertex \(\star\), and ordinary vertices \((R,L)\) with \(0\le R,L<k\). A directed edge labeled \((h,\ell)\), with digits \(0\le h,\ell<g\), from \((R,L)\) to \((V,U)\) exists precisely when
\[
k\ell+L=h+gU,\qquad kh+V=\ell+gR,\qquad 0\le U,V<k.
\]
At \(\star\), use \((R,L)=(0,0)\) but require \(h,\ell>0\). Even pivot vertices have equal coordinates. Odd pivot vertices have an edge to their coordinate reversal; the two pivot classes may overlap. The Young graph \(Y(g,k)\) deletes precisely those nonpivot vertices that cannot reach a pivot, retaining \(\star\) if it can reach a pivot. These are the definitions of Young and Sloane used by Kendrick.

Set \(a=m-2\), \(b=m(m-2)\), and \(c=k-1\). Note \(0<a<b<c<k\) for every \(m\ge3\). Denote the eight ordinary vertices by
\[
A=(0,0),\ B=(0,b),\ C=(a,a),\ D=(a,c),\ E=(b,0),\ F=(b,b),\ G=(c,a),\ H=(c,c).
\]

## Proof
**Step 1 (an exhaustive digit filter).** Since \(k=g-m\), the first carry equation gives \(m\ell\equiv L-h\pmod g\). As \(m^2\equiv1\pmod g\), the *unique* admissible low digit for a chosen high digit \(h\) is
\[
\ell=[m(L-h)]_g,
\]
where \([\cdot]_g\) is the least nonnegative residue. The second equation gives \(V=\ell+gR-kh\). The inequalities \(0\le\ell\le g-1\) and \(0\le V\le k-1\) force
\[
\max\!\left(0,\left\lceil\frac{gR-(k-1)}{k}\right\rceil\right)
\le h\le
\min\!\left(g-1,\left\lfloor\frac{gR+g-1}{k}\right\rfloor\right).
\]
For \(R=0,a,b,c\), direct substitution of \(g=m^2-1\), \(k=m^2-m-1\) gives, respectively, the exhaustive candidate sets
\[
\{0,1\},\quad\{a,a+1,a+2\},\quad\{c,k,k+1\},\quad\{g-2,g-1\}.
\]
The candidate \(h=a+2\) produces \(V=1-2m\) when \(L=a\) and \(V=-m-1\) when \(L=c\), both negative. The candidate \(h=c\) produces \(V=g\) when \(L=0\) and \(V=g+m-2\) when \(L=b\), both at least \(k\). For the other candidate digits, the resulting \(\ell,U,V\) have the required bounds, as is verified by substitution in the following table. Thus there are **no additional outgoing edges** from any of the eight vertices.

**Step 2 (the complete transition table).** Entries give successor and edge label \((h,\ell)\). They are identities in the integer parameter \(m\), not a finite numerical search.

| Vertex | First successor and label | Second successor and label |
|---|---|---|
| \(A\) | \(A:(0,0)\) | \(B:(1,k)\) |
| \(B\) | \(C:(0,a)\) | \(D:(1,g-2)\) |
| \(C\) | \(E:(a,0)\) | \(F:(a+1,k)\) |
| \(D\) | \(G:(a,a)\) | \(H:(a+1,g-2)\) |
| \(E\) | \(A:(k,1)\) | \(B:(k+1,k+1)\) |
| \(F\) | \(C:(k,m-1)\) | \(D:(k+1,g-1)\) |
| \(G\) | \(E:(g-2,1)\) | \(F:(g-1,k+1)\) |
| \(H\) | \(G:(g-2,m-1)\) | \(H:(g-1,g-1)\) |

At the distinguished starting vertex, the only nonzero-digit edge is \(\star\to B\), labeled \((1,k)\): the otherwise possible transition to \(A\) carries the forbidden label \((0,0)\). The table is closed under successors, so induction on graph distance proves that the full reachable carry-pair graph has exactly these eight ordinary vertices and one starting vertex. Conversely all eight vertices are reachable from \(\star\) by the displayed edges, so none are redundant.

**Step 3 (pivots and pruning).** The even pivot vertices are exactly \(A,C,F,H\). The odd pivot vertices, found by checking whether an edge leads to the coordinate reversal, are exactly \(A,D,E,H\). Every reachable vertex can reach \(A\): for example \(A\) has its loop, \(B\to C\to E\to A\), \(D\to G\to E\to A\), and \(H\to G\to E\to A\); the remaining cases follow immediately. Hence no vertex is removed in forming the Young graph.

**Step 4 (uniform isomorphism).** The complete nine-vertex transition pattern, distinguished start, and both pivot markings are independent of \(m\). At \(m=3\), one has \((g,k,a,b,c)=(8,5,1,3,4)\), and the construction is precisely \(Y(8,5)\). The map matching \(\star,A,B,C,D,E,F,G,H\) across values of \(m\) is therefore the claimed graph isomorphism. \(\square\)

## Verification
Run the attached standalone \`verify.py\` with Python 3. It constructs all digit-pair transitions independently from the two carry equations, starting only at \(\star\), rather than assuming the eight-vertex answer. It checks every integer \(3\le m\le100\), including edge labels, the even- and odd-pivot markings, and reachability of a pivot from each state. These finite checks corroborate—but do not replace—the symbolic exhaustive interval argument and transition table above.

## Relationship to prior work
Kendrick, *Young Graphs: 1089 et al.* (arXiv:1410.0106, earliest public version 2014-10-01; Journal of Integer Sequences 18 (2015)), Section 6.1, **Conjecture 39**, states the isomorphism for all \(m\ge3\) without proof; Section 2 supplies the definitions used here. Sloane's *2178 and All That* (arXiv:1307.0453; Fibonacci Quarterly 52 (2014)) establishes the Young-graph framework, transfer-matrix enumerations, and previously proved graph classes. The present carry-coordinate enumeration settles this specific isomorphism family; it is not the broader isomorphism conjectures in Kendrick's neighboring Conjectures 38, 40–43. Searches for equivalent carry-graph descriptions and algebraic parametrizations found no stronger theorem implying this exact infinite graph family.

## Limitations
The result does not classify other pairs \((g,k)\), establish digit-label-preserving isomorphism, or settle other conjectured Young-graph families. Later unindexed or differently phrased equivalences remain a literature risk. The proof's infinite scope depends on the displayed integer inequalities and identities, not on extrapolating the finite verification range.

## References
1. L. H. Kendrick, *Young Graphs: 1089 et al.*, arXiv:1410.0106 (2014 first version, 2015 revision and journal publication). https://arxiv.org/abs/1410.0106 ; https://www.maths.tcd.ie/EMIS/journals/JIS/VOL18/Kendrick/ken1.pdf
2. N. J. A. Sloane, *2178 and All That*, arXiv:1307.0453 (2013 first version), Fibonacci Quarterly **52** (2014), 99–120. https://arxiv.org/abs/1307.0453
