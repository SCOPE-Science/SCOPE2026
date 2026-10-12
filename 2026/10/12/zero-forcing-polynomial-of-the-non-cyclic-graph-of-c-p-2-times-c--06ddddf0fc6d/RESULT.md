# Zero forcing polynomial of the non-cyclic graph of \(C_{p^2}\times C_p\)

## Finding

Let \(p\) be a prime, let \(G=C_{p^2}\times C_p\), and let \(\Gamma_G\) be the non-cyclic graph on \(G\setminus\operatorname{Cyc}(G)\). For \(p\ge3\), put \(N=p^3-1\). Then \[\mathcal Z(\Gamma_G;u)=\frac{p^4(p-1)^5}{2}u^{N-4}+\frac{p^3(p-1)^3(p^2+1)}{2}u^{N-3}+\frac{p(p-1)^2(p^3+p^2+3p+1)}{2}u^{N-2}+Nu^{N-1}+u^N.\] Hence \(Z(\Gamma_G)=p^3-5\). Every minimum zero forcing set is exactly the complement of four vertices consisting of one nonidentity element of \(pC_{p^2}\times\{0\}\), one element from each of two distinct maximal cyclic subgroups of order \(p^2\) outside their common order-\(p\) subgroup, and one element from an order-\(p\) subgroup not equal to that common subgroup. There are \(p^4(p-1)^5/2\) such minimum sets. For \(p=2\), \(\mathcal Z(\Gamma_G;u)=20u^4+18u^5+7u^6+u^7\), so \(Z(\Gamma_G)=4\).

For odd \(p\), the polynomial has exactly five nonzero terms although the graph has \(p^3-1\) vertices. The minimum zero forcing sets have a rigid group-theoretic description by the unique common order-\(p\) subgroup of the maximal cyclic order-\(p^2\) subgroups.

## Assumptions and scope

Write the group additively as
\[
G=\mathbb Z/(p^2)\times\mathbb Z/p.
\]
The non-cyclic graph \(\Gamma_G\) has vertex set
\[
G\setminus\operatorname{Cyc}(G),
\]
and distinct vertices are adjacent exactly when they generate a noncyclic subgroup.

For this group, \(\operatorname{Cyc}(G)=\{0\}\). Indeed, the foundational non-cyclic-graph paper records that a finite \(p\)-group has nontrivial cyclicizer only when it is cyclic or generalized quaternion; \(G\) is neither.

Put
\[
P=(p\mathbb Z/(p^2)\times\{0\})\setminus\{0\},
\qquad |P|=s=p-1.
\]
There are exactly \(p\) maximal cyclic subgroups \(H_1,\ldots,H_p\) of order \(p^2\). They all have the same unique subgroup of order \(p\), namely \(P\cup\{0\}\). Define
\[
A_i=H_i\setminus(P\cup\{0\}),
\qquad |A_i|=a=p(p-1).
\]
The \(p\)-torsion subgroup \(G[p]\cong C_p^2\) has \(p+1\) subgroups of order \(p\). Besides \(P\cup\{0\}\), write the remaining \(p\) lines as \(L_1,\ldots,L_p\), and put
\[
B_j=L_j\setminus\{0\},
\qquad |B_j|=s.
\]
These \(2p+1\) sets partition \(G\setminus\{0\}\).

## Proof

If one of two elements has order \(p^2\), the subgroup they generate is cyclic exactly when the other element lies in the same maximal cyclic order-\(p^2\) subgroup. If both have order \(p\), they generate a cyclic subgroup exactly when they lie on the same one-dimensional subspace of \(G[p]\).

Consequently every class \(P,A_i,B_j\) is independent, and the complete adjacency pattern between classes is:

- \(P\) is adjacent to every \(B_j\) and to no \(A_i\);
- distinct \(A_i,A_k\) are completely adjacent;
- distinct \(B_j,B_k\) are completely adjacent;
- every \(A_i\) is completely adjacent to every \(B_j\).

Thus vertices inside each of the \(2p+1\) classes are false twins.

A zero forcing set cannot leave two vertices white in one false-twin class. If two such vertices were white, every vertex outside the class would be adjacent to both or neither, and vertices inside the class are mutually nonadjacent; neither white twin could ever become the unique white neighbor of a blue vertex.

Assume now \(p\ge3\). Every class has at least two vertices, so when exactly one vertex of a class is white there is still a blue vertex in that same class. Hence the forcing process reduces exactly to a class-level peeling process.

For a current white-class set, let \(\varepsilon\in\{0,1\}\) record whether \(P\) is white, let \(r\) be the number of white \(A\)-classes, and let \(t\) be the number of white \(B\)-classes. A blue vertex from the \(P\)-class has \(t\) white neighbors. A blue vertex in a white \(A\)-class has \(r-1+t\) white neighbors, while a blue vertex in a fully blue \(A\)-class has \(r+t\). Likewise a blue vertex in a white \(B\)-class has \(\varepsilon+r+t-1\) white neighbors, and one in a fully blue \(B\)-class has \(\varepsilon+r+t\).

These counts give the complete peeling criterion:
\[
(\varepsilon,r,t)\text{ is peelable}
\quad\Longleftrightarrow\quad
\bigl(t\le1\text{ and }r\le2\bigr)
\text{ or }
(\varepsilon,r,t)=(0,0,2).
\tag{1}
\]
To see this, if \(t=1\), a blue vertex in \(P\) first forces the unique white \(B\)-vertex. With \(t=0\), two white \(A\)-classes can be peeled by a blue mate in one of them, one white \(A\)-class can be peeled by a fully blue \(A\)-class, and a final white \(P\)-vertex can be forced by a blue \(B\)-vertex. If \(t\ge2\) and at least three classes are white, every possible blue source has at least two white neighbors. The exceptional two-white configuration with two \(B\)-classes peels because a blue mate in either class sees the other white \(B\)-vertex uniquely.

Criterion (1) shows immediately that at most four vertices may be white in a forcing coloring. The unique four-class profile is
\[
(\varepsilon,r,t)=(1,2,1).
\]
Therefore
\[
Z(\Gamma_G)=N-4=p^3-5.
\]
The number of minimum zero forcing sets is the number of choices of the four omitted vertices:
\[
|P|\binom p2 a^2\,p|B_1|
=
\frac{p^4(p-1)^5}{2}.
\]
This also proves the asserted classification of all minimum sets.

For the remaining coefficients, weight every peelable class profile by the product of its class sizes. Every two-class subset is peelable, giving
\[
z(\Gamma_G;N-2)
=
\frac{p(p-1)^2(p^3+p^2+3p+1)}{2}.
\]
The peelable three-class profiles are
\[
(1,1,1),\qquad(0,2,1),\qquad(1,2,0),
\]
which give
\[
z(\Gamma_G;N-3)
=
\frac{p^3(p-1)^3(p^2+1)}{2}.
\]
Finally every single omitted vertex is forceable and the all-blue set is forcing, so
\[
z(\Gamma_G;N-1)=N,
\qquad
z(\Gamma_G;N)=1.
\]
No other coefficients are nonzero.

When \(p=2\), the class sizes are
\[
1,2,2,1,1.
\]
The graph has seven vertices, so the boundary can be checked exactly. Minimum forcing sets have four blue vertices. Their three omitted vertices are precisely either one vertex from each \(A\)-class together with one of \(P,B_1,B_2\), or \(P\) together with one \(B\)-vertex and one vertex from one \(A\)-class. These give \(12+8=20\) minimum sets. A direct complete subset census gives
\[
\mathcal Z(\Gamma_G;u)=20u^4+18u^5+7u^6+u^7.
\]

## Verification

The accompanying `verify.py` constructs \(C_{p^2}\times C_p\) directly for \(p=2,3,5\), forms every cyclic subgroup, and declares two nonidentity elements adjacent exactly when neither cyclic subgroup contains the other. It independently recovers the classes \(P,A_i,B_j\), checks their sizes, verifies every quotient adjacency, and checks the false-twin property.

It then enumerates all admissible white-class subsets, replays zero forcing on the full graph, weights each profile by the number of choices of representatives, and compares the complete polynomial with the closed formulas. For \(p=2\), all \(2^7\) vertex subsets are exhaustively tested independently. The class-profile formula is additionally checked for \(p=3,5,7,11\).

Exact replay output:

```text
p=2: N=7, class_sizes=P:1, A:2x2, B:1x2, polynomial={7: 1, 6: 7, 5: 18, 4: 20}
p=3: N=26, class_sizes=P:2, A:6x3, B:2x3, polynomial={26: 1, 25: 26, 24: 276, 23: 1080, 22: 1296}
p=5: N=124, class_sizes=P:4, A:20x5, B:4x5, polynomial={124: 1, 123: 124, 122: 6640, 121: 104000, 120: 320000}
p=2 exhaustive_all_subsets={4: 20, 5: 18, 6: 7, 7: 1}
p=3: profile_formula_OK min_omitted=4 min_sets=1296
p=5: profile_formula_OK min_omitted=4 min_sets=320000
p=7: profile_formula_OK min_omitted=4 min_sets=9335088
p=11: profile_formula_OK min_omitted=4 min_sets=732050000
VERIFY_OK
```

The computations are finite corroboration. The arbitrary-prime theorem follows from the subgroup partition and the class-peeling criterion (1).

## Relationship to prior work

Abdollahi and Mohammadi Hassanabadi introduced the non-cyclic graph and established its basic group-theoretic structure. Their full paper gives the exact graph definition, records the finite \(p\)-group cyclicizer criterion used above, and studies connectivity, regularity, degree patterns, and graph reconstruction questions. It does not discuss zero forcing or the zero forcing polynomial. The official publication record reports online publication on 11 June 2007 and primary Mathematics Subject Classification \(20D60\).

Boyer and collaborators introduced the zero forcing polynomial and characterize several generic coefficients and graph families. Their full text defines complete multipartite graphs and graph joins and discusses recognizability, but contains no occurrence of “non-cyclic” and no specialization to group-associated non-cyclic graphs. The present formula requires the mixed-exponent subgroup geometry of \(C_{p^2}\times C_p\) and the complete class-peeling analysis above.

The foundational non-cyclic-graph paper already uses \(C_2\oplus C_4\) as an example when discussing cyclicizers. That example does not give its zero forcing polynomial; the \(p=2\) formula here is therefore treated as a boundary case of the uniform group family rather than as evidence of prior zero-forcing coverage.

## Limitations

The theorem treats only the rank-two mixed-exponent abelian \(p\)-group \(C_{p^2}\times C_p\). It does not claim the same five-term polynomial for other abelian types such as \(C_{p^a}\times C_{p^b}\) with larger exponents.

No minimum-rank or maximum-nullity formula is claimed here.

For \(p=2\), three of the false-twin classes are singletons, so the odd-prime class-peeling proof does not apply verbatim; the seven-vertex boundary is handled exactly and separately.

The graph order alone determines \(p\) inside this one-parameter family, so the value of the polynomial is not presented as a new group-reconstruction invariant. The mathematical content is the complete forcing enumeration and the classification of every minimum forcing set.

## References

1. A. Abdollahi and A. Mohammadi Hassanabadi, “Noncyclic Graph of a Group,” *Communications in Algebra* 35 (2007), 2057–2081. DOI: 10.1080/00927870701302081. Published online 11 June 2007.
2. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” *Discrete Applied Mathematics* 258 (2019), 35–48. DOI: 10.1016/j.dam.2018.11.033; arXiv:1801.08910.
