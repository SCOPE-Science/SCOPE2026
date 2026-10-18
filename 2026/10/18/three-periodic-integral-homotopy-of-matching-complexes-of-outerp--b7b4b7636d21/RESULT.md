# Three-periodic integral homotopy of matching complexes of outerplanar fan graphs

## Finding
For every integer \(n\ge 2\), let \(F_n=K_1\vee P_n\) be the fan on one apex and \(n\) path vertices, and let \(\mathcal M(F_n)\) be its ordinary matching complex (faces are collections of pairwise vertex-disjoint graph edges). Its **integral homotopy type** is
\[
\mathcal M(F_n)\simeq
\begin{cases}
\displaystyle\bigvee^{k+1}S^{k-1},&n=3k,\ k\ge1,\\
\displaystyle\bigvee^{k}S^{k},&n=3k+1,\ k\ge1,\\
\displaystyle\bigvee^{2k+2}S^{k},&n=3k+2,\ k\ge0.
\end{cases}
\]
All reduced integral homology vanishes outside the displayed sphere degree; in that degree it is free abelian with the displayed multiplicity. The exceptional one-path-vertex fan \(F_1=K_2\) has contractible matching complex. This is the full parametric homotopy classification, not merely a Betti-number formula.

## Assumptions and scope
\(P_m\) denotes the path with \(m\) vertices (not \(m\) edges); in particular, \(F_n\) has \(n+1\) graph vertices and \(2n-1\) graph edges. The symbol \(\vee\) in \(K_1\vee P_n\) denotes **graph join**, whereas \(\bigvee\) in the conclusion denotes a **topological wedge**. Every simplicial complex is finite; topological homotopy refers to geometric realization. The two empty-edge path graphs \(P_0,P_1\) contribute the augmented join unit \(\{\varnothing\}\), interpreted combinatorially as a formal sphere of dimension \(-1\), never as an ordinary nonempty geometric space. The cases \(n=2,3\) are checked separately.

## Proof
**Step 1: the path building block.** Let \(I_t=\operatorname{Ind}(P_t)\), the independence complex on a path of \(t\) vertices. For \(t\ge3\), split by the second path vertex. Its deletion has the first vertex isolated, hence a contractible independence complex; its link is \(I_{t-3}\). The star of the second vertex is a cone, so this simplicial pushout gives \(I_t\simeq\Sigma I_{t-3}\), using the augmented suspension convention when the link has no vertices. The initial complexes \(I_0\), \(I_1\), \(I_2\) have, respectively, the formal \((-1)\)-sphere, a point, and \(S^0\). Inductively, since \(\mathcal M(P_m)=I_{m-1}\), for \(m\ge2\):
\[
\mathcal M(P_m)\simeq
\begin{cases}
S^{q-1},&m=3q\text{ or }m=3q+1,\ q\ge1,\\
\text{point},&m\equiv2\pmod3.
\end{cases}
\]
Both \(\mathcal M(P_0)\) and \(\mathcal M(P_1)\) are the augmented join unit.

**Step 2: separate the apex edges.** Denote the path vertices by \(1,\ldots,n\) and the apex edges by \(s_i\). Put \(B=\mathcal M(P_n)\). No matching contains two apex edges. When it contains \(s_i\), its other edges form a matching in the two disjoint paths obtained by deleting path vertex \(i\). Accordingly, with simplicial joins,
\[
\mathcal M(F_n)=B\cup\bigcup_{i=1}^{n}(s_i*A_i),\qquad
A_i=\mathcal M(P_{i-1})*\mathcal M(P_{n-i})\subseteq B.
\]
The cones meet one another only in their common base subcomplex \(B\); thus their attachments are homotopy cofibers of the inclusions \(A_i\hookrightarrow B\). By the path classification and the join formula \(S^a*S^b\simeq S^{a+b+1}\), a **noncontractible** \(A_i\) appears precisely as follows (write \(t=i-1\)):

- For \(n=3k\), exactly \(t\equiv1\pmod3\), giving \(k\) links of type \(S^{k-2}\).
- For \(n=3k+1\), exactly \(t\equiv0\pmod3\), giving \(k+1\) links of type \(S^{k-1}\).
- For \(n=3k+2\), exactly \(t\equiv0,1\pmod3\), giving \(2k+2\) links of type \(S^{k-1}\).

Every other link contains a contractible path factor and is contractible. Here the asserted link types are ordinary spaces for \(n\ge4\); the small cases are treated below. Attaching a cone along a contractible subcomplex leaves the homotopy type unchanged.

**Step 3: three congruence classes.** Suppose \(n=3k\), \(k\ge2\). The base \(B\simeq S^{k-1}\), while each of the \(k\) relevant links has homotopy type \(S^{k-2}\). Every map \(S^{k-2}\to S^{k-1}\) is nullhomotopic; therefore all cone attachments split, and \(\mathcal M(F_{3k})\simeq\bigvee^{k+1}S^{k-1}\).

Suppose \(n=3k+1\), \(k\ge1\). Now \(B\simeq S^{k-1}\). The first link is \(A_1=\mathcal M(P_{3k})\). Its inclusion in \(B=\mathcal M(P_{3k+1})\) is a homotopy equivalence: identifying these complexes with the independence complexes of paths on \(3k-1\) and \(3k\) vertices, the latter is obtained from the former by coning off the link \(\operatorname{Ind}(P_{3k-2})\), which is contractible by Step 1. Attaching the cone on \(A_1\) therefore makes the base contractible. Each of the other \(k\) noncontractible links is homotopy equivalent to \(S^{k-1}\), and its cone attaches by a now-null map, contributing \(S^k\). Hence \(\mathcal M(F_{3k+1})\simeq\bigvee^k S^k\).

Suppose \(n=3k+2\), \(k\ge1\). In this case \(B\simeq\text{point}\); all cone attaching maps are nullhomotopic. The \(2k+2\) sphere-bearing links each contribute \(S^k\), giving \(\mathcal M(F_{3k+2})\simeq\bigvee^{2k+2}S^k\).

For \(n=2\), the fan is a triangle; its matching complex is three isolated points, or \(\bigvee^2S^0\). For \(n=3\), its matching complex consists of two disjoint edges and an isolated point, hence has three components and homotopy type \(\bigvee^2S^0\). These supply all missing low-dimensional boundary cases. This finishes the all-integers proof.

## Verification
The dependency-free file `verify_fan_matching.py` reconstructs all path and apex graph edges, enumerates every matching and its simplicial boundary, and reduces integer bitset boundary columns over \(\mathbf F_2\) for every \(2\le n\le15\). Independently, it computes the matching face polynomial via the path recurrence and the decomposition in Step 2, and compares every coefficient and the reduced Euler characteristic. All finite checks agree with the formula, including all three congruence classes. Run `python3 verify_fan_matching.py`; recorded output is in `verification_output.txt`. The **infinite** homotopy statement follows from Steps 1–3 and not from finite extrapolation.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega, *Matching Complexes of Outerplanar Graphs* (first public version November 7, 2024; arXiv:2411.04601), prove that every outerplanar graph has contractible or sphere-wedge matching complex (Theorem 2). This covers the **qualitative** wedge property of fans but does not specify their integral sphere dimensions or multiplicities. The same authors' *General polygonal line tilings and their matching complexes* (arXiv:2211.12559; 2023), Theorem 15, classifies a **zigzag triangular line** defined on alternating upper/lower path vertices. It can agree with the first few small fans but, for arbitrarily long lengths, is not the cone-over-path family: the triangular-line graphs have bounded maximum degree, while the fan apex has degree \(n\). Neither inspected result entails the formula for all fans. Related independence-complex formulas for fan graphs themselves do not address the matching complex, which is the independence complex of the **line graph**. The path and cofibration techniques themselves are classical and are not claimed as new.

## Limitations
The classification is restricted to a **single apex adjacent to every vertex of a path**. It makes no assertion about arbitrary maximal outerplanar graphs, graph automorphism actions, or equivariant homotopy. The first small fan cases overlap known triangular-line examples; the new assertion is the complete infinite parametric fan formula. Originality is supported by the inspected published literature and relevant indexed searches, not by a proof that no other report exists. The field-valued verification alone cannot detect integral torsion or certify infinite homotopy; the supplied symbolic cofibration proof is the basis for the integral conclusion.

## References
1. Margaret Bayer, Marija Jelić Milutinović, Julianne Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601, first posted 2024-11-07, revision 2026-09-23. https://arxiv.org/pdf/2411.04601
2. Margaret Bayer, Marija Jelić Milutinović, Julianne Vega, *General polygonal line tilings and their matching complexes*, arXiv:2211.12559, first posted 2022-11-22; Discrete Mathematics 346 (2023), 113428. https://arxiv.org/pdf/2211.12559
3. Dmitry N. Kozlov, *Complexes of directed trees*, Journal of Combinatorial Theory Series A 88 (1999), 112–122 (standard path independence/matching topology).
