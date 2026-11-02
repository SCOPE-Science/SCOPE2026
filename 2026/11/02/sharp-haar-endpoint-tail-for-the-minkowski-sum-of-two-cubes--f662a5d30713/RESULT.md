# Sharp Haar endpoint tail for the Minkowski sum of two cubes

## Finding

Let \(C=[-1,1]^3\) and let \(R\) be Haar-uniform in \(SO(3)\). Define \(V(R)=\operatorname{Vol}_3(C+RC)\), with ordinary Euclidean three-volume. Then
\[
V(R)=16\left(1+\sum_{i,j=1}^{3}|R_{ij}|\right),\qquad 64\le V(R)\le96,
\qquad \mathbb EV(R)=88.
\]
The maximum is attained at exactly \(96\) distinct proper rotations, all nondegenerate quadratic maxima. The sharp upper-endpoint probability is
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon^{-3/2}
\Pr\{V(R)>96-\varepsilon\}=\frac{1}{6\sqrt2\,\pi}.}
\]
Equivalently, setting \(L(R)=\sum_{i,j}|R_{ij}|\), as real \(k\to+\infty\),
\[
\boxed{\mathbb E[L(R)^k]\sim20\sqrt{\frac{10}{\pi}}\frac{5^k}{k^{3/2}}.}
\]
The endpoint \(96\) and the maximum \(L=5\) follow from previously established matrix-norm optimization; **the claims of interest here are the sharp Haar endpoint coefficient and high-moment prefactor**, not those known endpoints.

## Assumptions and scope

The cubes are full three-dimensional Euclidean unit-coordinate cubes of side length \(2\), centered at the origin. The sum is the Minkowski sum \(C+RC=\{x+Ry:x,y\in C\}\). The rotation is distributed according to the unique normalized Haar probability on \(SO(3)\). All limits are for positive \(\varepsilon\downarrow0\) or positive real \(k\to\infty\), respectively. The probability uses the strict inequality; changing it to a non-strict inequality has no asymptotic effect. No claim about generic polytopes, higher-dimensional cubes, or non-Haar orientation laws is made.

## Proof

**1. Exact volume.** The sum is the three-dimensional zonotope with six half-generators \(e_1,e_2,e_3,Re_1,Re_2,Re_3\). For a three-dimensional zonotope with half-generators \(g_1,\dots,g_6\), its volume is \(8\sum_{i<j<\ell}|\det(g_i,g_j,g_\ell)|\). Among these \(20\) triples, two wholly belong to one orthonormal basis and contribute \(1\) each. The nine with two original and one rotated vector contribute \(\sum_{i,j}|R_{ij}|\); the nine with one original and two rotated vectors contribute the same sum by cofactor orthogonality. Therefore \(V(R)=16(1+L(R))\). Every rotation entry is marginally uniform on \([-1,1]\), giving \(\mathbb E L=9/2\) and \(\mathbb EV=88\). Also \(L\ge3\) since each unit row has \(\ell^1\)-norm at least \(1\), with equality exactly for signed permutation matrices.

**2. Every maximizer and its count.** For each sign matrix \(S\in\{-1,1\}^{3\times3}\), its nuclear norm gives
\[
L(Q)=\max_S\operatorname{tr}(S^TQ)\le\max_S\|S\|_*,\qquad Q\in O(3).
\]
If two rows of \(S\) are proportional, then \(\operatorname{rank}S\le2\), hence \(\|S\|_*\le\sqrt{2\operatorname{tr}(SS^T)}=\sqrt{18}<5\). Otherwise every two distinct row lines have dot product \(\pm1\), with the three off-diagonal dot products having negative product. Thus a sign vector \(t\in\{-1,1\}^3\) exists with \(SS^T=4I-tt^T\), whose eigenvalues are \(4,4,1\); consequently \(\|S\|_*=5\). The unique orthogonal polar optimizer for the trace is
\[
Q_S=(SS^T)^{-1/2}S=\left(\frac12 I+\frac16tt^T\right)S.
\]
Direct substitution gives \(\operatorname{sgn}(Q_S)=S\) entrywise, with one entry of absolute value \(1/3\) and two of absolute value \(2/3\) in each row; hence \(L(Q_S)=5\). There are \(2^{3-1}=4\) row-sign lines, of which \(\binom{4}{3}=4\) sets of three distinct lines and \(2^3\cdot3!=48\) label/sign arrangements each, giving \(4\cdot48=192\) admissible sign matrices. (More directly, select three of the four row-sign lines, order them, and independently choose a sign for each row.) The map \(S\mapsto Q_S\) is injective since the entrywise sign is \(S\). Replacing one row's signs changes \(\det Q_S\), so exactly \(96\) of these maximizers lie in \(SO(3)\). This recovers the previously known maximum \(L=5\) while supplying an explicit count needed for the probability calculation.

**3. The common nondegenerate Hessian.** At the explicit maximizer \(Q_0=\frac23J-I\), where \(J\) denotes the all-ones matrix, write \(S_0=J-2I\), so \(H=Q_0^TS_0=2I-J/3\). Its eigenvalues are \(2,2,1\), with the last eigendirection \(u=(1,1,1)/\sqrt3\). In exponential rotation coordinates \(Q=Q_0\exp([\omega]_\times)\), where \([\omega]_\times v=\omega\times v\), all nine signs remain unchanged for small \(\omega\). Since \(\operatorname{tr}(H[\omega]_\times)=0\) and \([\omega]_\times^2=\omega\omega^T-\|\omega\|^2I\),
\[
5-L(Q)=\frac12\big(3\|\omega\|^2+(\omega\cdot u)^2\big)+O(\|\omega\|^3).
\]
Therefore the volume deficit has quadratic part
\[
96-V(Q)=24(\omega_1^2+\omega_2^2)+32\omega_3^2+O(\|\omega\|^3)
\]
in an orthonormal basis whose third vector is \(u\). The same form holds at every maximizer: its positive polar factor has eigenvalues \(2,2,1\). In particular, all \(96\) maxima are isolated and nondegenerate.

**4. Sharp Haar coefficient.** Normalized Haar measure in these infinitesimal exponential coordinates has density \((8\pi^2)^{-1}(1+O(\|\omega\|^2))\); this follows, for instance, from the angle-axis Haar volume of \(SO(3)\). The ellipsoid \(24(\omega_1^2+\omega_2^2)+32\omega_3^2<\varepsilon\) has Euclidean volume
\[
\frac{4\pi}{3\sqrt{24\cdot24\cdot32}}\,\varepsilon^{3/2}
=\frac{\pi}{72\sqrt2}\,\varepsilon^{3/2}.
\]
The contribution from one maximizer is therefore \(\varepsilon^{3/2}/(576\sqrt2\,\pi)+o(\varepsilon^{3/2})\). Since the maximizing set is finite and \(SO(3)\) is compact, outside disjoint small neighborhoods of these maxima the volume is uniformly bounded below \(96\). Adding \(96\) contributions proves the claimed coefficient \(1/(6\sqrt2\,\pi)\).

**5. High moments.** For \(Y=5-L(R)\), the preceding result and \(96-V=16Y\) give
\[
\Pr\{Y<y\}\sim\frac{16\sqrt2}{3\pi}y^{3/2}.
\]
The tail-integration identity \(\mathbb E[L^k]=k\int_0^5 t^{k-1}\Pr(L>t)\,dt\), combined with the change of variables \(t=5(1-s/k)\), localization near \(t=5\), and dominated convergence yields
\[
\mathbb E[L^k]\sim5^k\,\frac{16\sqrt2}{3\pi}\,\Gamma(5/2)\,5^{3/2}\,k^{-3/2}
=20\sqrt{10/\pi}\,5^k k^{-3/2}.
\]
No finite simulation is used to justify this limiting passage.

## Verification

Run `python3 verify.py` in the directory containing the accompanying verifier. It enumerates all \(512\) sign matrices with exact rational polar factors, confirms \(192\) full-rank sign matrices and \(96\) proper-rotation maxima, verifies the common positive polar factor, and independently compares the 20-minor zonotope formula against the nine-entry formula for 250 deterministic pseudorandom rotations. It also checks the second-order deficit at decreasing scales. The maximum direct-volume discrepancy in these numerical comparisons was \(2.85\times10^{-14}\); all assertions passed. These finite computations are consistency checks; the infinite asymptotics are justified by the analytic steps above.

## Relationship to prior work

Banica, Collins and Schlenker (arXiv:0901.2923, first public 2009-01-19) already established the maximal entrywise \(\ell^1\)-norm \(5\) for \(3\times3\) real orthogonal matrices and analyzed their optimization. Their paper explicitly formulates the asymptotics of high moments as a motivating problem. Thus neither the norm maximum, the sign-matrix technique in general, nor elementary local Hessian analysis is asserted to be novel here. The present claim isolates the sharp **normalized-Haar geometric probability prefactor**, including the correct multiplicity and local measure, and its quantitative moment consequence for three dimensions. Lien's SCG 2008 paper treats efficient construction of Minkowski sums under rotations, but not this probability law. The determinant volume formula is standard zonotope theory. Relevant independently published geometric measurements of cube shadows concern projection/section statistics rather than this two-body Minkowski-sum endpoint.

## Limitations

The conclusion is specific to two congruent three-dimensional cubes, exact Haar orientation, and the maximal-volume endpoint. It does not give the interior density of \(V\), lower-endpoint rare-event asymptotics, or analogous higher-dimensional laws. Previously known maximal-norm results supply important components of the proof. Although the most relevant accessible primary work was inspected, an equivalent unlocated endpoint asymptotic might exist; independent historical-priority assessment has not been performed.

## References

1. J.-M. Lien, *Minkowski Sums of Rotating Convex Polyhedra*, Proceedings of the 24th Annual Symposium on Computational Geometry, June 9–11, 2008, DOI `10.1145/1377676.1377716` (author-hosted two-page paper inspected).
2. T. Banica, B. Collins, J.-M. Schlenker, *On orthogonal matrices maximizing the 1-norm*, arXiv:0901.2923v1, public January 19, 2009 (complete 17-page paper inspected; published 2010).
3. E. Gover and N. Krikorian, *Determinants and the Volumes of Parallelotopes and Zonotopes*, *Linear Algebra and its Applications* (2010); general determinant-volume background (full text not inspected).
