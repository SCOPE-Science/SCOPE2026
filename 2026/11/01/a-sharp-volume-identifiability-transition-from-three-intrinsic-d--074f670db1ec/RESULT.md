# A sharp volume-identifiability transition from three intrinsic distance moments of rectangular flat three-tori

## Finding
Let \(T(a,b,c)=\mathbb R^3/(a\mathbb Z\oplus b\mathbb Z\oplus c\mathbb Z)\), with \(a,b,c>0\), carry its quotient Euclidean geodesic metric. Choose two independent Haar-uniform points \(X,Y\), put \(D=d_T(X,Y)\), and write \(\mu=\mathbb E[D^2]\), \(\nu=\mathbb E[D^4]\), \(\omega=\mathbb E[D^6]\). Define
\[
S=12\mu,\quad Q=180(\nu-\mu^2),\quad R=3780(\omega-3\mu\nu+2\mu^3),\quad T_0=Q-S^2/3.
\]
The following are exact.

**(i) Two-moment feasibility and volume bounds.** A pair \((\mu,\nu)\) comes from such a torus if and only if
\[
\mu>0,\qquad \frac{19}{15}\mu^2\le\nu<\frac95\mu^2.
\]
Equivalently \(S>0\) and \(S^2/3\le Q<S^2\). Put
\[
B=\frac{5S^3-9SQ}{54},\qquad E=\frac{T_0^{3/2}}{3\sqrt6}.
\]
For fixed feasible \((\mu,\nu)\), every squared Riemannian volume \(V^2=(abc)^2\) in the following set occurs, and no other value does:
\[
\begin{cases}
\{S^3/27\},&Q=S^2/3,\\
[B-E,B+E],&S^2/3<Q<S^2/2,\\
(0,B+E],&S^2/2\le Q<S^2.
\end{cases}
\]
For \(Q>S^2/3\) the upper bound is attained only by the torus with two equal *shorter* circle lengths. When \(Q<S^2/2\), the lower bound is attained only by the torus with two equal *longer* lengths. At and beyond \(Q=S^2/2\), arbitrarily small positive volume is possible at fixed \(\mu,\nu\), but zero volume is not attained. The sharp collapse transition is
\[
Q=S^2/2\quad\Longleftrightarrow\quad \nu/\mu^2=7/5.
\]

**(ii) Three-moment rigidity.** The three values \(\mu,\nu,\omega\) determine the unordered multiset of side lengths \(\{a,b,c\}\) and hence the Riemannian isometry class. Explicitly \(a^2,b^2,c^2\) are the positive roots, counted with multiplicities, of
\[
p(z)=z^3-Sz^2+\frac{S^2-Q}{2}z-\frac{S^3-3SQ+2R}{6}.
\]
In particular \(V^2=(S^3-3SQ+2R)/6\).

**(iii) Sharp finite-data stability and cutoff.** On every compact family of such tori with \(0<\alpha\le a,b,c\le\beta\), there is a constant \(C_{\alpha,\beta}\) such that, for any two members,
\[
\min_{\sigma\in S_3}\max_i|a_i-b_{\sigma(i)}|
\le C_{\alpha,\beta}\left(|\mu-\mu'|+|\nu-\nu'|+|\omega-\omega'|\right)^{1/3}.
\]
The exponent \(1/3\) is optimal uniformly near a cubic torus. Two moments fail to determine the side lengths, or even volume, except at their unique cubic equality point; therefore three moments are the minimal universal cutoff.

## Assumptions and scope
All tori are three-dimensional, flat, orthogonal products of three metric circles with strictly positive circumferences. Distances are *intrinsic quotient geodesic distances*, not extrinsic chord distances under any embedding. The Haar probability is normalized Riemannian volume; \(\mathbb E[D^{2j}]\) means a two-independent-point expectation. Side permutations define congruent products. Every finite positive triple is admissible, but zero side lengths are excluded. There is no assertion for skew flat three-tori or nonuniform sampling.

## Proof
**1. Reduction to three independent squared uniform coordinates.** By translation invariance, \(X-Y\) is Haar-uniform. In the coordinatewise Voronoi cell of the rectangular lattice, its coordinates are independent uniform variables \(U_i\in[-1/2,1/2]\). Consequently, with \(x_1=a^2\), \(x_2=b^2\), \(x_3=c^2\),
\[
D^2=x_1U_1^2+x_2U_2^2+x_3U_3^2.
\]
Direct integration gives \(\mathbb E[U_i^{2k}]=1/(4^k(2k+1))\), and the first three cumulants of \(U_i^2\) are \(1/12\), \(1/180\), \(1/3780\). Independence and cumulant additivity therefore give \(S=\sum x_i\), \(Q=\sum x_i^2\), \(R=\sum x_i^3\). This proves the moment formulas for all positive \(a,b,c\).

**2. Feasible two-moment data.** The Cauchy inequality gives \(Q\ge S^2/3\), with equality only when all three \(x_i=S/3\). Strict positivity of the three \(x_i\) implies \(Q<S^2\). Conversely, for every \(S^2/3\le Q<S^2\), the positive triple
\[
x_1=S/3+A,\qquad x_2=x_3=S/3-A/2,\qquad A=\sqrt{2(Q-S^2/3)/3}
\]
realizes the desired \(S,Q\): positivity of the two smaller terms follows from \(Q<S^2\). Replacing \(S,Q\) by the measured moments gives the displayed feasible region.

**3. Complete volume fiber and sharp phase transition.** For fixed \(S,Q\) with \(T_0>0\), the triples with these two symmetric power sums can be parameterized, modulo permutation, by
\[
x_j=S/3+A\cos(\theta+2\pi(j-1)/3),\qquad 0\le\theta\le\pi/3.
\]
The two equal smaller entries occur at \(\theta=0\) and the two equal larger entries at \(\theta=\pi/3\). Along this sorted arc the smallest entry decreases from \(S/3-A/2>0\) to \(S/3-A\). Thus the complete arc is positive precisely when \(Q<S^2/2\); at equality its endpoint \(\theta=\pi/3\) has a zero entry and is excluded, and for larger \(Q\) the positive arc stops at the first zero coordinate. The identity \(\sum_{j=1}^3\cos^3(\theta+2\pi(j-1)/3)=(3/4)\cos(3\theta)\) yields
\[
R=S^3/9+ST_0+T_0^{3/2}\cos(3\theta)/\sqrt6.
\]
Newton's identity \(x_1x_2x_3=(S^3-3SQ+2R)/6\) then yields
\[
V^2=B+E\cos(3\theta).
\]
Because \(\cos(3\theta)\) decreases strictly from one to minus one along this arc, the set of positive volume values is exactly the claimed interval (or half-open interval). The end configurations and uniqueness statements follow from the same strict monotonicity. At \(T_0=0\), the sole triple is cubic with \(V^2=(S/3)^3\).

**4. Three-moment uniqueness and minimality.** Newton's formulas give the elementary symmetric functions \(e_1=S\), \(e_2=(S^2-Q)/2\), and \(e_3=(S^3-3SQ+2R)/6\). Hence the displayed cubic has precisely the three positive squared lengths as its roots, proving uniqueness up to permutation. For explicit two-moment collisions take \(0<\delta<1/2\) and the distinct squared-length triples
\[
(1+2\delta,1-\delta,1-\delta),\qquad (1-2\delta,1+\delta,1+\delta).
\]
Their \(S\) and \(Q\) agree, while their products differ by \(4\delta^3\) and their third power sums differ by \(12\delta^3\). Thus their first two distance moments agree but their volume and third distance moment differ. The first moment alone plainly cannot distinguish the positive triples with a given sum.

**5. Hölder stability.** On a bounded positive length range, the coefficients of the displayed monic cubic vary at most \(C\varepsilon\), where \(\varepsilon\) is the sum of the three absolute moment errors. All its roots lie in a common bounded interval. Put \(r=(C'\varepsilon)^{1/3}\), with \(C'\) sufficiently large. On the boundary of the union of closed complex discs of radius \(r\) centered at the roots of the first polynomial (counting repeated roots only once for the union), the original polynomial has modulus at least \(r^3\), while the coefficient perturbation has modulus at most \(C\varepsilon<r^3\). Rouché's theorem on each connected union component gives equal root counts for the two cubics inside that component. Each such component has diameter at most \(6r\), so the roots, with multiplicities, can be bijectively matched within \(6r\). Taking positive square roots is uniformly Lipschitz because all squared side lengths are bounded away from zero. This proves the stated \(1/3\)-Hölder bound. For the preceding collision family, the squared-length multisets (and hence the length multisets) are separated by order \(\delta\), whereas their first two moments coincide and their third moments differ by exactly \(\delta^3/315\). Hence no exponent strictly larger than \(1/3\) can hold uniformly near a cube.

## Verification
Run `python3 verify_torus.py` in the same directory as this file. The verifier independently expands the first three even-distance moments using exact rational coordinate integrals for hundreds of randomly chosen rational squared-length triples. It checks the Newton product formula, the full positive-volume fiber and both sharp endpoints against the trigonometric parameterization, and verifies the cubic-order two-moment collision exactly. The analytical proof, not finite tests, establishes the results for all admissible side lengths. No outside data, numerical optimization package, or external mathematical certificate is needed.

## Relationship to prior work
Silverman (1978) studies empirical distance-distribution processes on circles, tori and spheres; the accessible abstract emphasizes their limit theory, not recovery of a rectangular three-torus from the first three intrinsic even-distance moments. Agaronyan (2012) investigates mean distance between two uniform points in convex planar domains, a different non-quotient sampling problem. An elementary 2014 torus-distance calculation notes the coordinatewise Voronoi reduction, which is used here as standard background. Glorieux and Yarmola (2020), inspected in its arXiv full text, determine the probability of a homotopically trivial *three-point triangle* on a two-dimensional flat torus. Zhou (2026), inspected in its arXiv full text, studies energy maximization over *variable sampling measures* and negative type on flat tori; its rectangular-case Theorem 5.1 does not give moment-based shape recovery for fixed Haar sampling. A separate established reconstruction from the *full* two-point distance distribution in dimension two does not imply any finite three-moment cutoff in dimension three. No general method of moments or elementary Newton identity is claimed as new; the retained claim is the sharp inverse and volume-fiber classification for this intrinsic geometric model.

## Limitations
Historical novelty is provisional, not independently certified. The full Silverman (1978) paper was not obtainable in this run; its archival abstract is not evidence for a full-text absence claim. The result is restricted to orthogonal three-dimensional flat tori and exact idealized moments. It does not supply statistical error bounds for finite noisy samples; the Hölder estimate compares exact population moments. A volume zero is a limiting degeneration only and is never a three-torus. The 1978 literature source has a verified month and year but no independently verified day, so no specific day is assigned to that item. The dated 2012 supporting article used in the metadata has a source-listed first-publication date of 2012-12-01, not a date inferred from the 1978 article.

## References
- B. W. Silverman, “Distances on circles, toruses and spheres,” *Journal of Applied Probability* **15** (1978), 136–143, DOI: 10.2307/3213243 (print issue March 1978; full text inaccessible for direct comparison).
- N. Agaronyan, “Mean Distance between Two Points in a Domain,” *Proceedings of YSU A* **46** (2012), 3–8, DOI: 10.46991/PYSUA.2012.46.3.003 (source records 2012-12-01).
- R. Israel, “Random Distance on Torus,” Mathematics Stack Exchange answer, 2014-10-28, https://math.stackexchange.com/a/995574 (background elementary coordinate reduction).
- O. Glorieux and A. Yarmola, “Random triangles on flat tori,” arXiv:2003.08190v1 (2020-03-18; relevant sections read).
- Y. Zhou, “Distance Energies and Negative Type of Flat Tori,” arXiv:2609.05622v1 (2026-09-04; Sections 1 and 5 read).
