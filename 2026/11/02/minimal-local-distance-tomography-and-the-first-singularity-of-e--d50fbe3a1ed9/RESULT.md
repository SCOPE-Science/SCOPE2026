# Minimal local-distance tomography and the first singularity of Euclidean orthotopes

## Finding

Fix an integer \(d\ge3\), and let \(B\subset\mathbb R^d\) be any Euclidean orthotope (a rectangular box, in arbitrary position) with positive side lengths \(a_1,\ldots,a_d\). Choose \(X,Y\) independently and uniformly from \(B\), and put \(F_B(r)=\mathbb P\{\|X-Y\|_2\le r\}\), \(V=\prod_i a_i\), and \(a=\min_i a_i\). Write \(e_k\) for the degree-\(k\) elementary symmetric polynomial, with \(e_0=1\). For every \(0\le r\le a\), the exact, not merely asymptotic, identity is
\[
F_B(r)=\sum_{k=0}^d c_k r^{d+k},\qquad
c_k=\frac{(-1)^k\pi^{(d-k)/2}}{V\,\Gamma((d+k)/2+1)}\,e_k(a_1^{-1},\ldots,a_d^{-1}).
\tag{1}
\]
The first \(d\) coefficients \(c_0,\ldots,c_{d-1}\) uniquely recover the unordered side lengths, including repeated lengths. For an orthotope with pairwise distinct side lengths, the first \(d-1\) coefficients do **not** suffice: arbitrarily close noncongruent orthotopes have the same values of all of them. Thus \(d\) is the sharp generic prefix length for exact local-distance recovery. In particular the last coefficient in (1) is redundant:
\[
c_d=\frac{(-1)^d}{d!\,V^2},\qquad c_0=\frac{\kappa_d}{V},\quad \kappa_d=\frac{\pi^{d/2}}{\Gamma(d/2+1)}.
\tag{2}
\]

The domain \(0\le r\le a\) is maximal for identity (1). More precisely, let \(t=\#\{i:a_i=a\}\), and denote the right-hand polynomial in (1) by \(P_B(r)\). As \(h\downarrow0\),
\[
\boxed{\displaystyle
F_B(a+h)-P_B(a+h)
=\frac{t\,8\kappa_{d-1}(2a)^{(d-1)/2}}{V\,a(d+1)(d+3)}\,h^{(d+3)/2}
+O_B\bigl(h^{(d+4)/2}\bigr).}
\tag{3}
\]
Consequently the first departure radius identifies the shortest side length, and its leading amplitude additionally identifies how many side lengths attain that minimum (once \(V\), already determined by \(c_0\), is known). The order of vanishing of \(F_B\) at zero also determines \(d\) if the ambient dimension was not supplied.

## Assumptions and scope

The body is a full-dimensional Euclidean orthotope in integer dimension \(d\ge3\). The two points are independent and uniform with respect to \(d\)-dimensional volume; distance is ordinary Euclidean distance. Rotations and translations do not affect the probability. Side lengths are positive but need not be distinct except in the sharp generic lower bound. The local coefficients are defined with unnormalized physical distance \(r\), not relative distance. Equality at \(r=a\) follows by continuity. The remainder constant in (3) depends on the fixed orthotope; no dimension-uniform or degenerating-side bound is claimed.

## Proof

**1. Exact displacement density.** Rotate and translate so that \(B=\prod_{i=1}^d[0,a_i]\). For \(Z=X-Y\), independence gives
\[
f_Z(z)=\frac1V\prod_{i=1}^d\left(1-\frac{|z_i|}{a_i}\right)_+,
\quad (u)_+=\max\{u,0\}.
\tag{4}
\]
Indeed the one-coordinate difference density is \((a_i-|z_i|)_+/a_i^2\). Since \(F_B(r)=\int_{\|z\|_2\le r}f_Z(z)\,dz\), when \(r\le a\) all factors in (4) can be expanded without clipping. Integrate each term of the product over the radius-\(r\) ball. For every \(0\le k\le d\), the required monomial integral is
\[
\int_{\|z\|_2\le r}|z_1\cdots z_k|\,dz
=r^{d+k}\frac{\Gamma(1)^k\Gamma(1/2)^{d-k}}{\Gamma((d+k)/2+1)}.
\tag{5}
\]
This follows by substituting squared coordinates, or by the beta-gamma integral in each orthant. Summing over the \(\binom dk\) coordinate subsets gives (1); the terms for \(k=0,d\) yield (2). These are exact equalities, not truncated Taylor approximations.

**2. Reconstruction and its generic minimality.** Since \(c_0=\kappa_d/V>0\), obtain \(V=\kappa_d/c_0\). For each \(1\le k\le d-1\), solve (1) for
\[
e_k(a_1^{-1},\ldots,a_d^{-1})
=\frac{(-1)^k V\,\Gamma((d+k)/2+1)}{\pi^{(d-k)/2}}c_k.
\tag{6}
\]
Moreover \(e_d(a_1^{-1},\ldots,a_d^{-1})=1/V\). All reciprocal lengths, with multiplicity, are therefore the roots of the explicitly determined monic polynomial
\[
T^d-e_1T^{d-1}+e_2T^{d-2}-\cdots+(-1)^de_d=0.
\tag{7}
\]
This recovers every side length, without any simple-root assumption.

For optimality, start with \(d\) *distinct* positive reciprocal lengths \(b_1,\ldots,b_d\). Their monic polynomial has \(d\) simple positive real roots. Perturb only the coefficient \(e_{d-1}\) by a sufficiently small nonzero real amount, while holding \(e_1,\ldots,e_{d-2},e_d\) fixed. By the implicit-function theorem at the simple real roots (or disjoint intervals and sign persistence), all roots remain distinct, real, and positive; they vary continuously and define a noncongruent orthotope. By (1), both boxes have identical \(c_0,\ldots,c_{d-2}\), because \(c_0\) determines \(e_d\) and the other listed coefficients determine only \(e_1,\ldots,e_{d-2}\). The perturbation can be arbitrarily small. Thus fewer than \(d\) leading coefficients cannot give generic local injectivity.

**3. First breakpoint and multiplicity.** Extend the unclipped integrand of (4) polynomially, replacing every \((1-|z_i|/a_i)_+\) by \(1-|z_i|/a_i\). Its ball integral at any \(r\) is exactly \(P_B(r)\) by (5). For \(r=a+h\) with sufficiently small \(h>0\), only coordinates whose side length equals \(a\) can exceed their support interval. Also, no two such coordinates can simultaneously satisfy \(|z_i|>a\) in the ball: this would require \(r\ge\sqrt2\,a\). Therefore the correction \(F_B(r)-P_B(r)\) is the sum of \(t\) *disjoint*, positive, two-sided cap integrals.

For any one shortest coordinate, denote it by \(s=|z_i|\). The correction from both caps is
\[
\frac2{Va}\int_a^{a+h}(s-a)
\left[\int_{\|y\|\le\sqrt{(a+h)^2-s^2}}\ \prod_{j\ne i}\left(1-\frac{|y_j|}{a_j}\right)dy\right]ds.
\tag{8}
\]
Uniformly for \(s\in[a,a+h]\), the bracket is
\[
\kappa_{d-1}\bigl((a+h)^2-s^2\bigr)^{(d-1)/2}
+O_B\bigl(((a+h)^2-s^2)^{d/2}\bigr),
\tag{9}
\]
because the omitted factors differ from one by \(O_B(\|y\|)\). Substitute \(s=a+hu\); then
\[
(a+h)^2-s^2=2ah(1-u)+h^2(1-u^2).
\]
The leading cap term becomes
\[
\frac{2\kappa_{d-1}}{Va}(2a)^{(d-1)/2}
 h^{(d+3)/2}\int_0^1u(1-u)^{(d-1)/2}du.
\]
The beta integral equals \(4/((d+1)(d+3))\). Error (9) integrates to \(O_B(h^{(d+4)/2})\), while the quadratic correction inside the square-root contributes a smaller \(O_B(h^{(d+5)/2})\) term. Multiplying by \(t\) proves (3). Its coefficient is strictly positive, so the local polynomial cannot agree with \(F_B\) on any right-neighborhood of \(a\). Conversely it agrees on all \([0,a]\), establishing the exact maximal validity range and the asserted recovery of \(a,t\).

## Verification

The separate program `verify.py` computes the coefficients in (1), reconstructs three distinct-length orthotopes in dimensions three through five, and independently integrates planar disks through the three-dimensional box with lengths \((1,2,3)\). It compares the resulting exact-slicing distance probability with (1) strictly below the shortest side and verifies numerical convergence toward the cap coefficient in (3) above it. Running `python3 verify.py` prints `ALL_CHECKS_PASSED`. These checks test normalization, inverse formulas and the singularity constant; the general statements follow from the preceding analytic proof, not finite numerical tests.

For \((a_1,a_2,a_3)=(1,2,3)\) one has \(V=6\), \(t=1\), and (3) predicts
\[
F_B(1+h)-P_B(1+h)=\frac\pi9h^3+O(h^{7/2}).
\]

## Relationship to prior work

Bonnet, Gusakova, Thäle and Zaporozhets [1] treat mean distances of random points in arbitrary convex bodies and their sharp comparison with mean width, not local distance jets identifying high-dimensional box parameters. Pure, Durrani, Tong and Pan [2] derive a general *planar* polygon-distance integration framework. Wang [3] gives a convex-body covariogram formulation and its first short-distance correction. These general identities are acknowledged ingredients and could be used to derive the local direct polynomial after specializing to product boxes, but none of the inspected statements supplies the sharp all-dimensional local inverse prefix or the first-cap multiplicity law (3). Holmin, Kurlberg and Månsson [4] reconstruct rectangular boxes from a different random-billiard free-path distribution; this does not imply recovery from pairwise uniform-point Euclidean distances. The full planar coefficient expansion and a sharp planar angle inequality are known in [5]; this result therefore restricts its novelty claim to dimensions at least three, with a different, orthotope-specific inverse and breakpoint question. The classical two-dimensional rectangle-distance papers [6,7] are not claimed as new here.

## Limitations

The result concerns Euclidean orthotopes only, not arbitrary affine parallelotopes or convex bodies. It assumes exact population probabilities; extracting high-order local coefficients from finite noisy samples can be unstable, and no quantitative statistical error bound is proved. The reconstruction does not recover location or orientation and necessarily treats permutations of lengths as identical. The expansion at the first threshold does not classify later thresholds, which can involve simultaneous coordinate contacts. The full text of the older rectangle-distance article [6] was not available through the checked open sources, though that article explicitly concerns planar rectangles, outside the claimed dimensions. Historical priority for equivalent higher-dimensional inverse formulations is not exhaustively established.

## References

1. Gilles Bonnet, Anna Gusakova, Christoph Thäle, Dmitry Zaporozhets, *Sharp inequalities for the mean distance of random points in convex bodies*, arXiv:2010.03351v1, first public 7 October 2020, https://arxiv.org/abs/2010.03351 (primary MSC2020 52A22).
2. Ross Pure, Salman Durrani, Fei Tong, Jianping Pan, *Distance Distribution Between Two Random Nodes in Arbitrary Polygons*, arXiv:1903.07757v1, 18 March 2019, https://arxiv.org/abs/1903.07757.
3. Sinan Wang, *A Brunn–Minkowski Theory for the Distribution of Random Pairs of Points in Convex Bodies*, arXiv:2610.01916v1, 1 October 2026, https://arxiv.org/html/2610.01916v1.
4. Samuel Holmin, Pär Kurlberg, Daniel Månsson, *On the free path length distribution for linear motion in an n-dimensional box*, arXiv:1702.08096v1, 26 February 2017, https://arxiv.org/abs/1702.08096.
5. *Sharp uniform angular stability for the short-pair distance coefficient of convex polygons*, https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-sharp-uniform-angular-stability-for-the-short-pair-distance-coef--24e8bcd8655b/RESULT.md (2026).
6. George Marsaglia, B. Narasimhan, Arif Zaman, *The distance between random points in rectangles*, Communications in Statistics—Theory and Methods 19 (1990), 4199–4212, DOI 10.1080/03610929008830437.
7. A. M. Mathai, P. G. Moschopoulos, G. Pederzoli, *Random points associated with rectangles*, Rendiconti del Circolo Matematico di Palermo 48 (1999), 163–190, DOI 10.1007/BF02844387.
