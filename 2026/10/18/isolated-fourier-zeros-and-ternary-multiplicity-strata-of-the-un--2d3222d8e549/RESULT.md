# Isolated Fourier zeros and ternary multiplicity strata of the uniform Sierpiński carpet measure

## Finding
Let \(\mu\) be the canonical equal-weight probability measure on the standard planar Sierpiński carpet: its digit set is
\[
D=\{0,1,2\}^2\setminus\{(1,1)\},\qquad
\mu=\frac18\sum_{d\in D}(x\mapsto(x+d)/3)_\#\mu.
\]
Use \(\widehat\mu(\xi)=\int e^{-2\pi i\xi\cdot x}\,d\mu(x)\) for \(\xi\in\mathbb R^2\). Let \(\mathcal Z\) be its real-frequency zero set and let \(\mathcal Z_{\rm iso}\) be the zeros isolated in \(\mathcal Z\). Then:

**(1) Exact mixed-dimensional zero locus.** Define on the unit torus
\[
\Gamma=\left\{(s,t)\bmod\mathbb Z^2:
(1+2\cos(2\pi s))(1+2\cos(2\pi t))=1,\ 
1+2\cos(2\pi s)>0\right\}.
\]
The set \(\Gamma\) is a single nonsingular closed real-analytic oval around the torus origin. All Fourier zeros are exactly
\[
\boxed{\mathcal Z=3(\mathbb Z+\tfrac12)^2\ \cup\
\bigcup_{j\ge1}3^j(\Gamma+\mathbb Z^2),}
\]
where the first set is disjoint from every analytic oval in the union. In particular,
\[
\boxed{\mathcal Z_{\rm iso}=3(\mathbb Z+\tfrac12)^2.}
\]
Every zero outside this shifted lattice lies on at least one smooth real-analytic curve (different scaled curves may intersect).

**(2) Complete multiplicities at isolated zeros.** Every isolated zero has the unique form \(\xi=\frac32(u,v)\), with \(u,v\) odd integers. Define \(\nu_3(w)\) as the exponent of \(3\) in a nonzero integer \(w\), and
\[
r=1+\min\{\nu_3(u),\nu_3(v)\}.
\]
Then the exact real-analytic Taylor order of \(\widehat\mu\) at \(\xi\) is \(2r\). More precisely, for \(h\in\mathbb R^2\) approaching zero,
\[
\boxed{\widehat\mu(\xi+h)=C_\xi(h_1^2+h_2^2)^r
+O_\xi(|h|^{2r+1}),\qquad C_\xi\ne0.}
\]
Consequently, its complex-phase winding index around a sufficiently small counterclockwise real circle about \(\xi\) is \(0\), despite the occurrence of arbitrarily large even vanishing orders.

**(3) Exact multiplicity census and asymptotic density.** Let
\(N_{\rm iso}(R)=\#\{\xi\in\mathcal Z_{\rm iso}:|\xi|\le R\}\),
let \(N_{2r}(R)\) count isolated zeros of exact order \(2r\) in that disk, and let
\(M(R)=\sum_{\xi\in\mathcal Z_{\rm iso},\,|\xi|\le R}\operatorname{ord}_\xi\widehat\mu\). Then for all \(R\ge0\) and integers \(r\ge1\),
\[
\boxed{N_{2r}(R)=N_{\rm iso}(R/3^{r-1})-N_{\rm iso}(R/3^r).}
\]
As \(R\to\infty\),
\[
\boxed{N_{\rm iso}(R)=\frac{\pi}{9}R^2+O(R+1),\qquad
M(R)=\frac\pi4 R^2+O(R+1),}
\]
and for each fixed \(r\ge1\),
\[
\boxed{\lim_{R\to\infty}\frac{N_{2r}(R)}{N_{\rm iso}(R)}=\frac8{9^r}.}
\]
The order-distribution assertion is specifically about isolated zeros, not all zeros: the other zeros include continuous real-analytic curves and cannot be counted as discrete points.

## Assumptions and scope
The eight affine contractions have common scalar ratio \(1/3\), all eight weights are exactly \(1/8\), and the Fourier convention includes \(2\pi\) in the exponent. The claim concerns *real* frequency vectors in \(\mathbb R^2\), Taylor order in two real variables, and the local winding of the associated complex-valued transform. No assertion is made about its complex-frequency zero variety. The Fourier-zero set need not be a disjoint union of closed curves: different scaled ovals may meet, but no such oval meets the isolated lattice.

## Proof
**A. Infinite product and single-mask geometry.** By invariance, with
\[
P(s,t)=\frac18\sum_{(a,b)\in D}e^{-2\pi i(as+bt)},
\]
we have an absolutely locally uniformly convergent product
\[
\widehat\mu(\xi)=\prod_{j=1}^\infty P(\xi/3^j).
\]
Indeed \(P(0)=1\), and for every compact set \(K\subset\mathbb C^2\) there is a constant \(C_K\) with \(|P(\xi/3^j)-1|\le C_K3^{-j}\); a tail consisting of nonzero factors therefore has nonzero product. Thus a real Fourier zero occurs if and only if at least one finite mask factor vanishes.

Set \(A(s)=1+2\cos(2\pi s)\), with \(-1\le A\le3\). The elementary eight-digit factorization gives
\[
\boxed{P(s,t)=\tfrac18e^{-2\pi i(s+t)}\big(A(s)A(t)-1\big).}
\]
If \(A(s)A(t)=1\) and one of the factors is negative, both are negative, and each has absolute value at most \(1\); equality forces \(A(s)=A(t)=-1\), or \((s,t)\equiv(1/2,1/2)\pmod{\mathbb Z^2}\). Otherwise both are positive and the zero belongs to \(\Gamma\). Along the positive level curve, \(\nabla(A(s)A(t))\ne0\): the only simultaneous critical points of \(A\) in the torus have coordinates \(0\) or \(1/2\), and their products are \(9,-3,1\), with the sole level-one critical point belonging to the negative branch. To see that \(\Gamma\) is one oval, the positive component forces \(A(s)\in[1/3,3]\); for each allowable \(s\) the two choices of \(t\) are the opposite continuous branches of \(\arccos((1/A(s)-1)/2)/(2\pi)\), meeting smoothly at their two endpoints. This gives one simple analytic closed curve.

At the isolated mask zero put \(s=k+1/2+\sigma\), \(t=l+1/2+\tau\). Then
\[
P(s,t)=-\frac{\pi^2}{2}(\sigma^2+\tau^2)
+O\big((|\sigma|+|\tau|)^3\big).
\]
In particular its Taylor order is exactly two and its leading real quadratic form is definite.

**B. Cyclotomic separation lemma (critical step).** For every integer \(k\ge0\) and odd integers \(u,v\), put \(\alpha=e^{\pi i u/3^k}\), \(\beta=e^{\pi i v/3^k}\). The identity
\[
(1+\alpha+\alpha^{-1})(1+\beta+\beta^{-1})=1
\]
holds **only if** \(\alpha=\beta=-1\). To prove it, if \(\alpha=-1\), its first factor is \(-1\), and the real second factor is at least \(-1\), with equality only for \(\beta=-1\). The same applies with the variables interchanged. Otherwise \(\alpha,\beta\) have respective exact orders \(2\cdot3^h\) and \(2\cdot3^{h'}\), with \(h,h'\ge1\). Let \(B(z)=1+z+z^{-1}\). The real algebraic number \(B(\alpha)\) generates the maximal real cyclotomic subfield of conductor \(2\cdot3^h\), of degree \(3^{h-1}\); similarly \(B(\beta)\) has degree \(3^{h'-1}\). Since the proposed identity gives \(B(\beta)=B(\alpha)^{-1}\), the two fields coincide and their degrees force \(h=h'\). Therefore \(\beta=\alpha^a\) for some \(a\) coprime to \(2\cdot3^h\). The Galois automorphism \(\sigma\) of the real cyclotomic field taking \(\alpha+\alpha^{-1}\) to \(\alpha^a+\alpha^{-a}\) has **odd** order, because that Galois group has order \(3^{h-1}\). Applying its iterates to \(B(\alpha)\,\sigma(B(\alpha))=1\) alternates between \(B(\alpha)\) and its reciprocal. An odd-length orbit forces \(B(\alpha)^2=1\). But \(B(\alpha)=1\) would force \(\alpha=\pm i\), of order four, and \(B(\alpha)=-1\) would force \(\alpha=-1\), of order two. Both contradict its order \(2\cdot3^h\). This proves the lemma, including \(h=1\).

**C. Exhaustion of isolated zeros and Taylor order.** The single mask has one periodic lattice of isolated zeros \((\mathbb Z+1/2)^2\); its level-\(j\) dilate is \(3^j(\mathbb Z+1/2)^2\). Because \(3\) is odd, these dilates are nested and their union equals \(\mathcal L=3(\mathbb Z+1/2)^2\). Every point on a scaled copy of \(\Gamma\) is nonisolated in the full zero set. Conversely, every point \(\xi\in\mathcal L\) has \(\xi=\tfrac32(u,v)\) with \(u,v\) odd. At level \(j\), its coordinates are \(u/(2\cdot3^{j-1})\) and \(v/(2\cdot3^{j-1})\). By the cyclotomic separation lemma these coordinates never lie on \(\Gamma\); a level-\(j\) zero exists precisely when they are *both* half-integers, which is equivalent to \(j\le r\). Thus there are exactly \(r\) zero factors, all having the same nondegenerate quadratic leading form; every remaining factor is nonzero, as is their product. Indeed
\[
C_\xi=\left(-\frac{\pi^2}{2}\right)^r
3^{-r(r+1)}\prod_{j>r}P(\xi/3^j)\ne0.
\]
This proves the leading Taylor polynomial and shows that the transform has no zero in a sufficiently small punctured disk around \(\xi\). Since that leading polynomial maps each sufficiently small circle into a disk excluding the origin and concentrated around the nonzero constant \(C_\xi\rho^{2r}\), its winding index is zero. All other zeros belong to the analytic ovals, proving the exact decomposition.

**D. Counting.** The isolated lattice has covolume \(9\), hence the disk lattice-point estimate
\[
N_{\rm iso}(R)=\frac\pi9R^2+O(R+1).
\]
Its level-\(r\) sublattice \(3^r(\mathbb Z+1/2)^2\) is exactly the subset with Taylor order at least \(2r\). Subtracting the nested counts yields the exact formula for \(N_{2r}\), then the geometric limit \((1-3^{-2})3^{-2(r-1)}=8/9^r\). Furthermore \(\operatorname{ord}_\xi\widehat\mu=2\sum_{r\ge1}\mathbf1_{\xi\in3^r(\mathbb Z+1/2)^2}\), so
\[
M(R)=2\sum_{k\ge0}N_{\rm iso}(R/3^k)
=2\frac\pi9\frac1{1-1/9}R^2+O(R+1)
=\frac\pi4R^2+O(R+1).
\]
The sum is finite for each fixed disk, because the smallest norm of a point of \(3^r(\mathbb Z+1/2)^2\) tends to infinity. All three conclusions follow.

## Verification
Run `python checker.py` with Python 3, `sympy`, and `mpmath`. Exact polynomial greatest-common-divisor checks exclude any nontrivial root-of-unity intersection of the mask oval for primitive conductors \(2\cdot3^h\) with \(1\le h\le4\) (80 checks). High-precision product evaluations verify the predicted vanishing orders and zero winding on eight isolated lattice nodes; direct lattice enumeration verifies exact multiplicity-shell identities for radii \(20,100,300\). The exact counts at radius \(300\) are \(27{,}948,3{,}088,348,40,4\) for orders \(2,4,6,8,10\), totaling \(31{,}428\) isolated zeros. These are finite cross-checks only; the cyclotomic and counting arguments above prove the claims for all relevant integers.

## Relationship to prior work
Dutkay and Jorgensen's *Fourier frequencies in affine iterated function systems* (first arXiv posting 2006-04-25, arXiv:math/0604547) provides the general invariant-measure and Fourier-mask framework and develops Fourier bases and invariant sets. Its full text was inspected, especially the IFS definitions, Fourier-weight relation, and examples; it does not classify the canonical eight-digit carpet's real Fourier-zero geometry or its isolated-zero orders. Chen and Yan's *Spectral properties of a class of Sierpinski-type Moran measures on* \(\mathbb R^n\) (arXiv:2505.09360, first posted 2025) treats spectrality and explicit mask zeros for other, prime-cardinality digit families, including five-digit examples; it does not imply this eight-digit continuous-oval/isolated-point classification. The standard ternary carpet's digit geometry is classical, and the infinite-product identity is established background, not claimed as new. The new claim is the **complete isolated-zero and nodal-curve dichotomy**, requiring the cyclotomic separation lemma, and its all-order exact count. Related dyadic three-digit Sierpiński gasket results have discrete mask zeros rather than the present nonisolated oval components, and do not imply this theorem.

## Limitations
The theorem does not classify pairwise intersections, tangencies, or topology of the different scaled nodal ovals, nor does it count the uncountably many nonisolated zeros. All multiplicity and phase statements apply **only to isolated** real zeros. The analysis is for uniform weights and scalar ternary contraction, not arbitrary carpets. The literature comparison excludes the named inspected theorems but does not establish absolute publication priority; older diffraction, cyclotomic-unit, or unpublished carpet studies might contain equivalent observations.

## References
1. D. E. Dutkay and P. E. T. Jorgensen, *Fourier frequencies in affine iterated function systems*, arXiv:math/0604547 (first submitted 2006-04-25); https://arxiv.org/abs/math/0604547.
2. J.-L. Chen and X.-Y. Yan, *Spectral properties of a class of Sierpinski-type Moran measures on* \(\mathbb R^n\), arXiv:2505.09360 (first posted 2025-05-14); https://arxiv.org/abs/2505.09360.
