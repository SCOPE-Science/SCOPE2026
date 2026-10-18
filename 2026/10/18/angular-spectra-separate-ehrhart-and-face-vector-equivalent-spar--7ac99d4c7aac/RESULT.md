# Angular spectra separate Ehrhart- and face-vector-equivalent sparse-paving polytopes

## Finding
For integers \(n\ge5\) and \(2\le r\le n-2\), let \(\mathcal D\) be a set of \(r\)-subsets of \([n]\) such that distinct members have intersection of size at most \(r-2\). The remaining \(r\)-subsets are the bases of a sparse-paving matroid, and its base polytope is
\[
P_{\mathcal D}=\operatorname{conv}\{\mathbf{1}_{B}:|B|=r,\ B\notin\mathcal D\}\subseteq\{x\in\mathbb R^n:\sum_i x_i=r\}.
\]
Put \(N=\binom nr\), \(d=r(n-r)\), and \(t(B)=|\{H\in\mathcal D:|B\cap H|=r-1\}|\) for every remaining basis \(B\). The intrinsic Euclidean Gaussian solid angle of the normal cone at \(\mathbf{1}_{B}\), equivalently the probability that a uniform spherical direction exposes that vertex, is exactly
\[
\alpha_B=\frac1N\left(1+\frac{t(B)}d\right).
\]
If \(m=|\mathcal D|\) and \(q\) counts unordered pairs of deleted bases with intersection size \(r-2\), then the two-direction vertex collision probability is
\[
C_2(P_{\mathcal D})=\sum_{B\notin\mathcal D}\alpha_B^2
=\frac1{N^2}\left(N+m+\frac m d+\frac{8q}{d^2}\right).
\]

The angular spectrum, unlike this collision probability, is not determined even by the complete face vector together with the Tutte and Ehrhart polynomials. For every \(n\ge7\), use rank \(r=3\) and the two deleted families
\[
\mathcal D_{\mathrm s}=\{123,145,167\},\qquad
\mathcal D_{\mathrm t}=\{123,145,246\},
\]
where, for instance, \(123\) denotes \(\{1,2,3\}\); all remaining ground-set elements are permitted. Let \(P_{\mathrm s}(n)\) and \(P_{\mathrm t}(n)\) be their base polytopes. Their Tutte polynomials, Ehrhart polynomials, entire face vectors, and two-direction collision probabilities coincide, but their angular spectra do not. For every real \(s>2\), put \(C_s(P)=\sum_v\alpha_v^s\). Then
\[
C_s(P_{\mathrm t}(n))-C_s(P_{\mathrm s}(n))
=\frac{(d+3)^s-3(d+2)^s+3(d+1)^s-d^s}{(Nd)^s}>0,
\quad N=\binom n3,\ d=3(n-3).
\]
In particular, three independent isotropic directions expose the same vertex with probabilities differing by exactly
\[
C_3(P_{\mathrm t}(n))-C_3(P_{\mathrm s}(n))=\frac6{N^3d^3}.
\]
For \(n=7\), the difference is \(1/12348000\). This supplies an infinite family with a sharp first separation at the third angular power sum.

## Assumptions and scope
All vertex coordinates are the canonical zero-one basis incidence vectors and all Euclidean measurements use the induced metric on the affine hull. For any finite polytope \(P\), \(\alpha_v\) is the probability that the maximum of a standard Gaussian linear functional is attained at vertex \(v\); this equals the normalized intrinsic spherical measure of its normal cone. A generic Gaussian functional has an almost-surely unique maximizing vertex. The notation \(C_j\) for integer \(j\ge1\) is the probability that \(j\) independent directions select the same vertex. The rank-three pair is valid for every integer \(n\ge7\), with no bound on \(n\).

## Proof
**1. Basis system and affine span.** Two deleted \(r\)-subsets are never adjacent in the Johnson graph \(J(n,r)\). If \(B_1,B_2\) survive and \(i\in B_1\setminus B_2\), then the exchange sets \(B_1-i+j\), for \(j\in B_2\setminus B_1\), cannot all be deleted: with two or more choices they would form adjacent deleted vertices, while with one choice the exchange set is \(B_2\). Thus the surviving sets obey basis exchange. This is the usual stable-set characterization of sparse-paving matroids. For the displayed rank-three pair, every coordinate difference \(e_i-e_j\) lies in the linear span of vertex differences: among the \(\binom{n-2}{2}\ge10\) ways to choose a common two-element subset outside \(i,j\), at most three are forbidden by the deleted sets. Hence both base polytopes have intrinsic dimension \(n-1\) and are connected matroid base polytopes.

**2. The exact normal-cone law.** Let \(G_1,\dots,G_n\) be independent continuous identically distributed scores, in particular standard Gaussians. The set \(H\) of the top \(r\) coordinates is uniformly distributed among the \(N\) subsets. If \(H\notin\mathcal D\), its vertex is exposed. If \(H\in\mathcal D\), the largest-scoring \(r\)-subset other than \(H\) is obtained by exchanging the lowest-scoring coordinate of \(H\) for the highest-scoring coordinate of its complement. Indeed, each additional exchange loses a strictly positive amount, because every score in \(H\) exceeds every score outside \(H\). That one-exchange subset is a permitted basis: no neighbor of a deleted set is deleted. Conditional on the top set \(H\), the internal ranking of the \(r\) elements and the internal ranking of the other \(n-r\) elements are independent uniform permutations. Every one of the \(d=r(n-r)\) neighbors therefore receives equal probability \(1/(Nd)\) from \(H\). Summing its own top-set mass \(1/N\) and contributions from its \(t(B)\) deleted neighbors yields the displayed \(\alpha_B\). Projecting the Gaussian to the zero-sum subspace leaves all optimizing orders and normal-cone probabilities unchanged; rotational invariance makes these intrinsic Euclidean solid angles.

**3. The second collision moment.** There are \(N-m\) surviving bases, and \(\sum_Bt(B)=md\). Two Johnson vertices at distance exactly two have exactly four common neighbors (choose one of two removed and one of two inserted elements); at greater distance they have none. Stability excludes distance one. Thus \(\sum_B\binom{t(B)}2=4q\), so \(\sum_Bt(B)^2=md+8q\). Expanding \(\sum_B(1+t(B)/d)^2/N^2\) proves the formula for \(C_2\).

**4. Two families and their angular spectra.** Every pair of deleted triples within each displayed family intersects in exactly one element. Hence both have \(m=3\) and \(q=3\). The three Johnson neighbor sets of \(\mathcal D_{\mathrm s}\) have no common neighbor: such a triple would need the element \(1\) and at least one element from each of three disjoint pairs. The three neighbor sets of \(\mathcal D_{\mathrm t}\) have exactly one common neighbor, \(124\). Write \(a_j\) for the number of surviving bases having \(t(B)=j\). Since \(\sum_j a_j=N-3\), \(\sum_jja_j=3d\), \(\sum_j\binom j2 a_j=12\), and \(a_3\) is respectively \(0\) or \(1\), the complete spectra are
\[
(a_0,a_1,a_2,a_3)_{\mathrm s}=(N-3d+9,\,3d-24,\,12,\,0),
\]
\[
(a_0,a_1,a_2,a_3)_{\mathrm t}=(N-3d+8,\,3d-21,\,9,\,1).
\]
A basis in class \(j\) has angle \((d+j)/(Nd)\). The difference of the two power sums is therefore the third forward difference in the Finding. It is zero for powers \(1\) and \(2\), positive for every real power \(s>2\), because the third derivative of \(x\mapsto x^s\) is strictly positive on the positive real axis. For \(s=3\), the numerator is exactly \(6\).

**5. Equality of established invariants.** The Tutte polynomial of a sparse-paving matroid depends on \(n,r,m\): its rank function agrees with that of the uniform matroid except that the \(m\) deleted \(r\)-subsets have rank \(r-1\). Explicitly, the difference from the uniform Tutte polynomial is \(m((x-1)(y-1)-1)\). The same \(n,r,m\) also give identical Ehrhart polynomials, as established in the cited sparse-paving Ehrhart theory. Directly, the polytope is the hypersimplex intersected with \(x(H)\le r-1\) for each deleted \(H\). No point of a dilated hypersimplex can violate two such cuts: if \(|H\cap H'|\le r-2\), then \(x(H)+x(H')\le x([n])+x(H\cap H')\le 2(r-1)t\) in its \(t\)-dilation. Symmetry makes each single removed lattice-point cap identical, so only \(m\) matters. Finally, Ferroni--Schröter's face-enumeration theorem for connected sparse-paving matroids states that the entire face vector depends only on \(n,r,m,q\) (their circuit-hyperplane modular-pair count is exactly \(q\)). Since these parameters coincide, the full face vectors coincide. Thus the new angular spectra and every collision moment of order at least three separate polytopes that all those invariants fail to distinguish.

## Verification
The accompanying standalone `verify.py` uses only Python's standard library. For dimensions \(n=7,8\) it exhaustively evaluates every strict coordinate ranking (respectively \(5040\) and \(40320\) orders) with distinct power-of-two scores, finding the maximizing surviving basis by direct exhaustive maximization. It checks each exact predicted Gaussian angular mass, the stable-set and exchange properties, the complete neighbor multiplicity distributions, and equality of rank-based Tutte-polynomial counts. It also verifies exact collision formulas and histogram identities through \(n=11\). All arithmetic for the claimed moments is rational. These finite tests corroborate, but do not replace, the universal analytic argument.

## Relationship to prior work
Hanely, Martin, McGinnis, Miyata, Nasr, Vindas-Meléndez and Yin describe paving-matroid base polytopes as hypersimplex truncations and recover the known Ehrhart formula for sparse paving matroids. Ferroni and Schröter prove that the face vector of a connected sparse-paving matroid is determined by the number of circuit-hyperplanes and their distance-two pair count. Those results are used here, not claimed as original. The general greedy maximization of matroid weights and the uniformity of Gaussian coordinate rankings are standard facts. The result here adds the explicit normal-cone angle law and identifies an infinite pair with identical Tutte, Ehrhart, face-vector, and second-collision data but different full angular spectra and third/higher collisions. The pair-count component of the second-collision law is not advertised as a face-vector-independent invariant.

## Limitations
The angles concern canonical zero-one embeddings and isotropic Euclidean directions, not arbitrary affine realizations or anisotropic Gaussian objectives. The comparison addresses exact probabilities, not geometric congruence classification or reconstruction from the full normal fan. The finding does not settle any conjecture on Ehrhart positivity or matroid enumeration. Although primary literature and indexed mathematical records were checked for equivalent angular claims, bibliographic completeness and independent mathematical validation remain outstanding.

## References
1. D. Hanely, J. L. Martin, D. McGinnis, D. Miyata, G. D. Nasr, A. R. Vindas-Meléndez and M. Yin, *Ehrhart Theory of Paving and Panhandle Matroids*, arXiv:2201.12442, first posted 2022-01-28; especially Sections 1, 2 and Remark 5.12. https://arxiv.org/abs/2201.12442
2. L. Ferroni and B. Schröter, *Face enumeration for split matroid polytopes*, arXiv:2310.05487, first posted 2023-10-09; especially Corollary 2.10 and examples. https://arxiv.org/abs/2310.05487 ; Combinatorics, Probability and Computing 34 (2025), 528–544, doi:10.1017/S0963548325000021.
