# Extremal genus-two curves of bidegree \((2,3)\) over \(\mathbf F_3\): fifteen embedded types and three branch spectra

## Finding
Let \(k=\mathbf F_3\), let \(S=\mathbf P^1_k\times\mathbf P^1_k\), and let \(V=H^0(S,\mathcal O_S(2,3))\). Consider the projectivized nonzero sections \(\mathbf P(V)(k)\), and call a section smooth when its zero divisor is geometrically smooth. The action of \(G=\operatorname{PGL}_2(k)\times\operatorname{PGL}_2(k)\) preserves this family. Let \(N_1(C)=\#C(k)\).

**Classification.** Of the \(265720\) projective sections, exactly \(139392\) are smooth, forming \(286\) \(G\)-orbits. Exactly \(6096\) smooth sections have \(N_1(C)=8\), forming \(15\) \(G\)-orbits. They have the following exhaustive distribution by Frobenius cycle lengths on the six geometric ramification points of the degree-two ruling map, together with the number \(N_2(C)=\#C(\mathbf F_9)\):

| Ramification Frobenius partition | Sections | \(G\)-orbits | \(N_2(C)\) | Middle coefficient of \(P_C(T)\) |
| --- | ---: | ---: | ---: | ---: |
| \((6)\) | 3888 | 9 | 12 | 9 |
| \((4,2)\) | 1872 | 4 | 10 | 8 |
| \((2,2,2)\) | 336 | 2 | 14 | 10 |
| **Total** | **6096** | **15** | | |

In particular, there is no such maximal-point embedded curve with the ramification partition \((3,3)\). For these curves the zeta numerator is
\[
P_C(T)=1+4T+a_2T^2+12T^3+9T^4,
\]
with \(a_2\) respectively \(9,8,10\) in the rows above. The upper bound \(N_1(C)\leq8\) and its attainability are *prior known results*; the claimed classification is the embedded-model orbit count and the joint branch/zeta refinement.

Representatives of the three rows are obtained from the coefficient integers \(8868,9864,9372\), respectively, using the encoding defined below. Their precise equations are
\[
\begin{aligned}
F_{(6)}={}&U^2S^2T+U^2ST^2+U^2T^3+UVS^3+UVT^3+V^2S^3,\\
F_{(4,2)}={}&U^2ST^2+2U^2T^3+UVS^3+UVS^2T+UVST^2+UVT^3+V^2S^3,\\
F_{(2,2,2)}={}&U^2S^2T+2U^2T^3+UVS^3+2UVS^2T+UVT^3+V^2S^3.
\end{aligned}
\]

## Assumptions and scope
All fields, forms, smoothness assertions, and equivalences above are as stated, with no extension to other prime powers. An equation is counted up to a single nonzero scalar; two equations in distinct \(G\)-orbits may still define abstractly isomorphic curves. The ordered two ruling factors are fixed. A section has unique expansion
\[
F(U,V;S,T)=U^2A(S,T)+UVB(S,T)+V^2C(S,T),
\]
where \(A,B,C\) are homogeneous cubics. Put \(v=(v_0,\ldots,v_{11})\), with each successive block of four coordinates representing coefficients of \(S^3,S^2T,ST^2,T^3\) in \(A,B,C\). Encode a normalized \(v\) as \(n=\sum_{j=0}^{11}v_j3^j\), with its first nonzero \(v_j\) equal to one. Thus each section has one integer \(n\) in the census.

The degree-two map is projection to \([S:T]\). By adjunction, any smooth divisor in \(\mathcal O_S(2,3)\) has genus \((2-1)(3-1)=2\); its other projection has degree three. The ramification points of the degree-two map are precisely the six Weierstrass points over the algebraic closure.

## Proof
**Exact smoothness criterion.** Define the binary sextic
\[
\Delta(S,T)=B(S,T)^2-4A(S,T)C(S,T).
\]
A section is geometrically smooth if and only if \(\Delta\) is squarefree as a homogeneous binary sextic. Indeed, if \(A,B,C\) vanish simultaneously at a base point, \(\Delta\) has a multiple zero there. Otherwise the projection is finite flat of degree two, and, since the characteristic is not two, its local equations have the form \(w^2=\Delta\) times a unit. Smoothness is equivalent to simple branching at every root of \(\Delta\). A squarefree sextic gives six geometric branch points and a geometrically connected smooth genus-two curve by Riemann--Hurwitz.

The homogeneous squarefree test is exact: for \(f(X)=\Delta(X,1)\), require \(\gcd(f,f')=1\) in \(\mathbf F_3[X]\) and require that the coefficients of \(S^6\) and \(S^5T\) not vanish simultaneously (to rule out a double root at infinity). In `census.cpp`, every normalized twelve-vector is enumerated. There are exactly \((3^{12}-1)/2=265720\) such vectors; exactly \(139392\) pass this test. As cross-checks on all candidates accepted by the full sieve, `orbits.py` produces \(286\) smooth orbits and `symbolic_orbit_check.py` independently recomputes polynomial gcds on their representatives; their orbit weights sum to \(139392\). These orbit checks do not independently test the excluded coefficients; completeness of the smooth total rests on the full coefficient sieve and its exact squarefreeness criterion.

**Maximal-point models.** The degree-two map gives \(N_1(C)\leq2\#\mathbf P^1(\mathbf F_3)=8\). A smooth curve attains eight exactly when all four rational fibers split into two distinct rational points. On each fiber there are \(\binom42(3-1)=12\) nonzero split quadratic equations; moreover evaluation of homogeneous binary cubics at the four rational points of the base is a bijection from their four-dimensional coefficient space to \(\mathbf F_3^4\). Consequently there are exactly \(12^4/2=10368\) projective equations with fully split rational fibers, before imposing smoothness. The independent `interpolation_check.py` enumerates these \(10368\) sections *from their fiber quadratics*, reconstructs their coefficient cubics by inverting the evaluation matrix, and uses a different polynomial Euclidean algorithm to show that \(6096\) are smooth.

**Orbits.** Each factor \(\operatorname{PGL}_2(\mathbf F_3)\) has \(24\) elements, hence \(\#G=576\). `orbits.py` explicitly constructs each projective matrix, its symmetric-square or symmetric-cube coefficient action, and the \(576\) Kronecker-product actions on \(V\). For each still-unseen smooth section it computes all transformed normalized coefficients and marks its orbit; transformed sections are checked to belong to the original smooth set. Exactly \(286\) disjoint orbits cover all \(139392\) smooth models, and exactly \(15\) of them have eight rational points. Their representatives and sizes are given in `orbit_reps.csv`; in the maximal stratum the orbit sizes sum to \(6096\).

**Ramification and zeta refinement.** For each maximal representative, `extremal_checks.py` factors \(\Delta\) over \(\mathbf F_3\) and enumerates points directly over \(\mathbf F_9=\mathbf F_3[i]/(i^2+1)\). The Frobenius splitting types and extension-field counts are constant on each rational projective orbit. Independent `interpolation_check.py` computes the factor degrees for *all* \(6096\) maximal equations, without reliance on orbits: the counts are \(3888,1872,336\) for splitting \((6),(4,2),(2,2,2)\) and zero for \((3,3)\). For genus two, the usual zeta identity and \(N_1=8\) give the displayed numerator with \(a_2=(N_2+6)/2\). This proves the table.

## Verification
Reproduction requires a C++17 compiler, Python 3 with NumPy and SymPy, and the files bundled alongside this document. Execute the precise commands in `REPRODUCE.md` from the containing directory. The cross-checks use two distinct coefficient parametrizations (full coefficient enumeration and rational-fiber interpolation), an explicit full group action, symbolic checks on every smooth orbit representative, and direct \(\mathbf F_9\)-point enumeration for every maximal orbit representative. Expected outputs are embedded in `census_results.txt`, `orbit_results.txt`, `interpolation_results.txt`, `extremal_results.txt`, and `symbolic_orbit_results.txt`. The complete \(139392\)-line normalized smooth-model list is `smooth_models.csv`. All statements concern these finite, exhaustively enumerable spaces; no inference from incomplete extension-degree sampling is made.

## Relationship to prior work
Faber--Grantham, *Ternary and Quaternary Curves of Small Fixed Genus and Gonality with Many Rational Points* (first arXiv version 2020-10-15), Section 2, Theorem 2.4, already proves that the maximal point count of a genus-two curve over \(\mathbf F_3\) is eight. The point bound and existence therefore are **not** originality claims here. This paper does not state the number of smooth bidegree-\((2,3)\) embeddings with eight points, their orbits under the ruling-preserving group, or their joint ramification and second-extension point distribution.

Vermeulen, *Curves of fixed gonality with many rational points* (first arXiv version 2021-02-01), studies maximum rational-point constructions via toric surfaces and squarefree discriminants for sufficiently large genera, rather than the finite low-genus orbit decomposition here. Rains--Sam, *Invariant theory of \(\bigwedge^3(9)\) and genus 2 curves* (arXiv 2017), studies a different parametrization involving a marked rational Weierstrass point and 3-covering data, not the specified pair of ruling maps. The related published results found in semantic research-record searches concern other moduli objects and do not imply this classification. Absence of an indexed matching statement is not a proof of global priority; unpublished or unindexed small-field computations remain a residual risk.

## Limitations
The group equivalence is ambient \(G\)-equivalence, not abstract curve isomorphism; the \(15\) classes need not yield \(15\) abstractly nonisomorphic curves. No corresponding counts for other fields, genus-two models outside this bidegree, or all choices of trigonal maps are asserted. The established universal \(\mathbf F_3\) genus-two point bound is excluded from the novelty claim. This package has undergone a self-review only, not independent mathematical validation. Python package availability and compiler versions may affect execution convenience but not the specified exact finite tests.

## References
1. X. Faber and J. Grantham, *Ternary and Quaternary Curves of Small Fixed Genus and Gonality with Many Rational Points*, arXiv:2010.07992, initially public 2020-10-15; especially Section 2 and Theorem 2.4. https://arxiv.org/abs/2010.07992
2. F. Vermeulen, *Curves of fixed gonality with many rational points*, arXiv:2102.00900, initially public 2021-02-01; especially Sections 1, 2, and 4. https://arxiv.org/abs/2102.00900
3. E. M. Rains and S. V. Sam, *Invariant theory of \(\bigwedge^3(9)\) and genus 2 curves*, arXiv:1702.04840, initially public 2017-02; especially Introduction and Section 2. https://arxiv.org/abs/1702.04840
