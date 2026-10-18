# Exact colour-refinement depth of corner-marked rectangular grids

## Finding
For all integers \(2\le m\le n\), let \(G=P_m\square P_n\) be the simple grid with vertex set \(\{0,\ldots,m-1\}\times\{0,\ldots,n-1\}\), edges between points differing by one in a single coordinate, and initial colouring distinguishing only \((0,0)\). In ordinary synchronous counting colour refinement, round \(t+1\) records the previous colour and the multiset of neighbour colours. Define the stabilization depth as the smallest \(t\) for which rounds \(t\) and \(t+1\) induce the same vertex partition. Then
\[
R(m,n)=n+\left\lfloor\frac m2\right\rfloor-2.
\]
For \(m<n\), the stable partition is discrete, with \(mn\) classes. For \(m=n\), its classes are precisely the coordinate-swap orbits \(\{(i,j),(j,i)\}\), numbering \(m(m+1)/2\). The formula is exact for every parameter pair.

## Assumptions and scope
All graphs are finite and simple, \(2\le m\le n\), with no precolours other than the distinguished corner. One refinement round is one synchronous application of the counting multiset rule. This result concerns within-graph vertex partitions, not discrimination against arbitrary nonisomorphic graphs. A colour at round \(t\) determines all preceding-round colours and their neighbour-colour multiplicities.

## Proof
**(1) Boundary moments are refinement invariants.** Let \(A\) be the adjacency matrix, \(D\) the degree matrix, and \(L=D-A\) the combinatorial Laplacian. The local degree deficit \(f=4-\deg\) is known after round one, and inductively a round-\(t\) colour determines \(L^k f\) for all \(0\le k\le t-1\): given the previous colour, vertex degree, and multiset of earlier colours, both \(A\) and \(D\) acting on an earlier-colour-measurable scalar are determined. Write \(L=L_m\otimes I+I\otimes L_n\), where \(L_q\) is the path Laplacian. Let \(b_q(i)={\bf1}_{i=0}+{\bf1}_{i=q-1}\), including multiplicity two only if the endpoints coincide (excluded here). Then \(f(i,j)=b_m(i)+b_n(j)\). As \(L_q\mathbf1=0\),
\[
(L^k f)(i,j)=(L_m^k b_m)(i)+(L_n^k b_n)(j),\qquad k\ge0.
\]

**(2) A resolvent identity.** Define the formal power series \(F_{q,i}(z)=\sum_{k\ge0}(L_q^k b_q)(i)z^k\). There is a unique \(r=-z+O(z^2)\) satisfying \(z=-r/(1-r)^2\), and
\[
F_{q,i}(z)=(1-r)\,\frac{r^i+r^{q-1-i}}{1-r^q}.
\]
Indeed, \(F-zL_qF=b_q\) is the path's tridiagonal resolvent equation. Substitution of the displayed expression solves the interior recurrence, since \(1-2z+z(r+r^{-1})=0\), and the two endpoint equations; the solution in formal power series is unique because the operator has constant term \(I\). This also checks \(q=2\), when \(F\equiv1\).

Suppose vertices \((i,j)\) and \((i',j')\) have the same round-\(T\) colour, with \(T\ge1\). Put \(p_q(r)=r^a+r^{q-1-a}-r^{a'}-r^{q-1-a'}\), using \((a,a')=(i,i')\) for \(q=m\) and \((j,j')\) for \(q=n\). Equality of the first \(T\) moments and substitution of a formal parameter of order one implies that
\[
N(r)=p_m(r)(1-r^n)+p_n(r)(1-r^m)
\]
has zero coefficients at degrees \(0,\ldots,T-1\). Moreover, with \(H=m+n-1\), direct reversal gives \(r^HN(1/r)=-N(r)\). Thus vanishing through degree \(\lfloor H/2\rfloor\) implies \(N\equiv0\), by antisymmetry of the coefficient array. For \(T=R\), the inequality \(R-1\ge\lfloor H/2\rfloor\) holds for all \(2\le m\le n\) apart from \((2,2),(2,3),(3,3),(3,4)\), handled below.

**(3) Boundary moments determine unmarked grid orbits.** The rational function \((r^a+r^{q-1-a})/(1-r^q)\) is the generating function of a periodic integer sequence of period \(q\), with two unit masses at positions \(a\) and \(q-1-a\) modulo \(q\). Distinct unordered endpoint-reflection classes have differences of *least* period \(q\): for a primitive \(q\)-th root of unity \(\zeta\), their Fourier amplitudes are \(2\zeta^{(q-1)/2}\cos((2a-q+1)\pi/q)\) and its counterpart for \(a'\), which are unequal when \(0\le a<a'\le\lfloor(q-1)/2\rfloor\); equivalently the periodic difference has a nonzero primitive Fourier coefficient. (For \(q=2\) there is only one reflection class.) If \(N=0\) and \(m<n\), the two periodic difference sequences are negatives of one another, so any nonzero one would have periods \(m\) and \(n\). A nonzero sequence of least period \(n\) cannot also have the smaller period \(m\); hence both vanish. Their endpoints therefore agree up to reflection, so the vertices lie in the same orbit under independent coordinate reflections of the unmarked rectangle. If \(m=n\), \(N=0\) says the sum of two reflected endpoint-pair indicator polynomials agrees; the nonnegative coefficient multiset determines the unordered pair of reflected coordinate types. These are exactly the unmarked square-grid orbits, allowing coordinate interchange.

**(4) Rooted walk signatures distinguish within unmarked orbits.** Round \(T\) additionally determines the root-walk counts \(w_k(v)=(A^k\mathbf1_{\{(0,0)\}})(v)\) for \(k\le T\), by induction from the unique root colour and neighbour multisets. For \(v=(i,j)\) at root distance \(d=i+j\), these vanish for \(k<d\), while \(w_d(v)=\binom di\). Consequently, when at least one of two vertices has \(d\le R\), the two round-\(R\) colours can agree only when their root distances are equal and the binomial coefficients \(\binom di\) agree. Strict increase of binomial coefficients up to the middle of a row shows that the coordinates then agree as an ordered pair or are interchanged. The interchange is a root-preserving grid automorphism exactly for square grids; for non-square grids, distinct interchanges are separated by the unmarked-orbit information from (3).

If both root distances exceed \(R\), use the unmarked orbits from (3). Represent each reflection pair by a near index \(0\le a\le\lfloor(m-1)/2\rfloor\), \(0\le b\le\lfloor(n-1)/2\rfloor\). The near-near point has distance \(a+b\le R\). A singly reflected point \((m-1-a,b)\) with its first coordinate not fixed by reflection has distance at most \(m-1+\lfloor(n-2)/2\rfloor\le R\). Similarly, \((a,n-1-b)\), when distinct, has distance at most \(n-1+\lfloor(m-2)/2\rfloor=R\). Hence in each unmarked orbit the only point with distance exceeding \(R\) is the far-far point, or its coordinate swap when \(m=n\). Those are rooted-automorphic. Thus all same-coloured pairs at round \(R\) are rooted-automorphic, and round \(R\) has the stable orbit partition.

The four small exceptions \((m,n)=(2,2),(2,3),(3,3),(3,4)\) follow directly by one, two, two, and three rounds respectively, for example from the direct verification program supplied below.

**(5) Sharpness.** Write \(a=\lfloor m/2\rfloor\) and take the two vertices in the final column \(u=(a-1,n-1)\) and \(v=(a,n-1)\) if \(m\) is even, or \(v=(a+1,n-1)\) if \(m\) is odd. They are exchanged by an automorphism of the unmarked grid reflecting its first coordinate. Their root distances satisfy \(d(u)=R\) and \(d(v)>R\). For every round \(t<R\), neither vertex's radius-\(t\) coloured unfolding contains the uniquely marked corner, and therefore their colours agree by this unmarked reflection. At round \(R\), the root-walk invariant separates them. Thus stabilization is impossible before round \(R\), proving equality in the formula.

## Verification
Two standalone, dependency-free Python checkers accompany this result. `verify_direct.py` constructs each marked graph and iterates colour refinement to stabilization for \(345\) dimension pairs (\(2\le m\le16\), \(m\le n\le31\)), confirming the exact depth and stable rooted orbits. `verify_algebra.py` separately computes boundary-series coefficients, antipolynomial degree thresholds, geodesic binomial certificates, and the distant sharpness witness for \(912\) parameter pairs (\(2\le m\le33\), \(m\le n\le45\)). Both complete successfully. Numerical checks are corroboration, not a replacement for the infinite-parameter proof.

## Relationship to prior work
Arvind–Köbler–Rattan–Verbitsky (arXiv:1502.01255, first public 2015-02-04) establish the general colour-refinement and graph-isomorphism framework. Kiefer–McKay (arXiv:2005.10182) study extremal iteration numbers across general graphs. These sources do not, in the material inspected, supply the sharp corner-marked rectangular-grid depth formula or the boundary-moment argument. Related earlier work determines stable partitions for pointed rectangular grids, but determination of a final partition does not by itself determine the *first* stabilization round. A specialized earlier proof of this exact formula remains possible; the literature comparison is not a proof of publication priority.

## Limitations
Only a single distinguished corner with no other initial markings is treated; no assertion is made about arbitrary base colours, arbitrary competitors in graph identification, unmarked grids, or more general Cartesian products. Finite checkers do not independently certify the all-parameter theorem. The proof depends on the nontrivial path-resolvent and primitive-period lemmas supplied above; independent mathematical review is still outstanding.

## References
1. V. Arvind, J. Köbler, G. Rattan, and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (public 2015-02-04), https://arxiv.org/abs/1502.01255.
2. S. Kiefer and B. D. McKay, *The Iteration Number of Colour Refinement*, arXiv:2005.10182 (2020), https://arxiv.org/abs/2005.10182.
