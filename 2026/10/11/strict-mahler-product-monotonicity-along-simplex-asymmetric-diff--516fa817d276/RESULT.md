# Strict Mahler-product monotonicity along simplex asymmetric difference bodies

## Finding

Fix an integer \(d\ge2\) and a nondegenerate Euclidean \(d\)-simplex \(\Delta\) with centroid \(c\). Write \(\Delta_0=\Delta-c\) and let
\[
K_t=\Delta_0+t(-\Delta_0),\qquad 0\le t<\infty.
\]
The Santaló point of every \(K_t\) is the origin. The affine-invariant volume product \(\mathcal M_d(t)=\operatorname{vol}_d(K_t)\operatorname{vol}_d(K_t^\circ)\) satisfies, with \(n=d+1\),
\[
\boxed{\quad \mathcal M_d(t)=\frac{n^n}{d!}\frac{\displaystyle\sum_{k=0}^d\binom{d}{k}^{\!2}t^k}{\displaystyle\prod_{j=1}^d\bigl(j+(n-j)t\bigr)}.\quad}
\]
Moreover, \(\mathcal M_d(t)\) is strictly increasing for \(0<t<1\), strictly decreasing for \(t>1\), and \(\mathcal M_d(t)=\mathcal M_d(1/t)\) for \(t>0\). Consequently its **unique global maximum** for finite \(t\ge0\) occurs at the symmetric difference body \(K_1=\Delta-\Delta\), with
\[
\mathcal M_d(1)=\frac{d+1}{d!}\binom{2d}{d},\qquad
\mathcal M_d(0)=\frac{(d+1)^{d+1}}{(d!)^2}.
\]
The maximum has an exact second-order stability coefficient. Writing \(t=e^u\),
\[
\boxed{\ \log\frac{\mathcal M_d(e^u)}{\mathcal M_d(1)}
=-\frac{d(d-1)(d+4)}{24(2d-1)(d+1)}u^2+O_d(u^4)\quad(u\to0).\ }
\]

## Assumptions and scope

All volumes are ordinary Lebesgue volumes. For a body \(K\) containing the origin in its interior, \(K^\circ=\{y:\langle y,x\rangle\le1\text{ for every }x\in K\}\). The Santaló point minimizes the polar volume among translations of \(K\); it is unique. There are no regularity or angle assumptions on \(\Delta\). The affine-invariance of the product permits replacing \(\Delta\) by the standard simplex \(\operatorname{conv}(0,e_1,\ldots,e_d)\). The monotonicity assertion is restricted to these reflected-simplex Minkowski sums and is not asserted for arbitrary convex bodies.

## Proof

**1. Center and primal volume.** For the standard simplex \(S=\operatorname{conv}(0,e_1,\ldots,e_d)\), its centroid is \(m=(1,\ldots,1)/(d+1)\). The centered family is \((S-m)+t(m-S)\), which differs from \(S-tS\) only by translation and therefore has the same volume. In an orthant having \(k\) nonnegative coordinates, a point \(x\) belongs to \(S-tS\) exactly when
\[
\sum_{i:x_i\ge0}x_i\le1,\qquad
\sum_{i:x_i<0}(-x_i)\le t.
\]
(The conditions are necessary by writing \(x=y-tz\), \(y,z\in S\), and sufficient using \(y_i=\max(x_i,0)\) and \(tz_i=\max(-x_i,0)\).) That orthant contributes \(t^{d-k}/(k!(d-k)!)\). Summing over its \(\binom dk\) possible sign patterns and exchanging \(k\) with \(d-k\) gives
\[
\operatorname{vol}_d(K_t)=\frac1{d!}\sum_{k=0}^d\binom dk^2t^k=\frac{S_d(t)}{d!}.
\]

**2. Why the polar is taken at the Santaló point.** The \(d+1\) centered simplex vertices, including \(v_0=-m\) and \(v_i=e_i-m\), are permuted by linear automorphisms. These symmetries preserve \(K_t\) and fix only the origin, since the \(v_i\) span the \(d\)-space and sum to zero. The unique Santaló point is fixed by all automorphisms and hence is the origin.

**3. Polar-volume product formula.** For \(u\in\mathbb R^d\), set \(a_i=\langle u,v_i\rangle\), so \(\sum_{i=0}^d a_i=0\). The support function is
\[
h_{K_t}(u)=\max_i a_i-t\min_i a_i.
\]
On a chamber in which the \(n=d+1\) values are ordered, let \(g_j=a_{(j+1)}-a_{(j)}\ge0\) for \(1\le j\le d\). The zero-sum identity gives
\[
h_{K_t}(u)=\frac1n\sum_{j=1}^d\bigl(j+(n-j)t\bigr)g_j.
\]
The linear map from \(u\) to the \(d\) gaps is invertible on each chamber and has an absolute Jacobian independent of \(t\). Consequently the part of the polar \(\{u:h_{K_t}(u)\le1\}\) in that chamber is the image of a \(d\)-simplex with volume proportional to \(\prod_j\bigl(j+(n-j)t\bigr)^{-1}\). All \(n!\) chambers share that dependence; thus
\[
\frac{\operatorname{vol}_d(K_t^\circ)}{\operatorname{vol}_d(K_0^\circ)}=\frac{d!}{P_d(t)}.
\]
At \(t=0\) the polar of \(S-m\) has vertices \(n(1,\ldots,1)\) and \(-n e_i\) for \(1\le i\le d\). Its edge-determinant has absolute value \(n^{d+1}\), giving \(\operatorname{vol}_d(K_0^\circ)=n^{d+1}/d!\). We obtain \(\operatorname{vol}_d(K_t^\circ)=n^n/P_d(t)\), proving the displayed product formula.

**4. Root comparison and strict global monotonicity.** The elementary Legendre-polynomial identity
\[
S_d(t)=(1-t)^d\,\mathrm P_d\!\left(\frac{1+t}{1-t}\right)
\]
holds by the classical binomial expansion of the Legendre polynomial \(\mathrm P_d\). The two sides are understood polynomially, including at \(t=1\). For a positive Legendre root \(\beta_j\), the corresponding negative zero of \(S_d\) is \(-r_j\), where \(r_j=(1-\beta_j)/(1+\beta_j)\); the opposite Legendre root gives \(-1/r_j\). Denominator zeros form analogous reciprocal pairs from \(y_j=(n-2j)/n\), for \(1\le j\le\lfloor d/2\rfloor\); when \(d\) is odd, the shared zero at \(-1\) cancels.

The classical strict Stieltjes zero-comparison theorem states that the positive roots \(\beta_j\) of the degree-\(d\) Legendre polynomial exceed the correspondingly ordered positive roots \(\cos(j\pi/n)\) of the Chebyshev polynomial of the second kind. The elementary concavity-of-cosine inequality \(\cos(j\pi/n)\ge1-2j/n=y_j\) gives
\[
\beta_j>y_j>0\quad(1\le j\le\lfloor d/2\rfloor).
\]
Put \(z(r)=r+1/r\). Since \(r=(1-x)/(1+x)\) is in \((0,1)\) for \(x\in(0,1)\), \(z(r)=2(1+x^2)/(1-x^2)\) strictly increases with \(x\). Therefore the quadratic factor \((t+r_j)(t+1/r_j)=t^2+z_jt+1\) of the numerator has a strictly larger \(z_j\) than its paired denominator factor.

For all \(t>0\) and \(z>2\),
\[
\frac{\partial}{\partial z}\left(\frac{d}{dt}\log(t^2+zt+1)\right)
=\frac{1-t^2}{(t^2+zt+1)^2}.
\]
Thus for \(0<t<1\) every paired numerator-minus-denominator logarithmic-derivative contribution is strictly positive, and for \(t>1\) it is strictly negative. There is at least one pair because \(d\ge2\). Leading polynomial constants are independent of \(t\) and the unmatched factor for odd \(d\) cancels. It follows that \(\mathcal M_d\) strictly increases then strictly decreases, including continuity at \(t=1\). Both \(S_d\) and \(P_d\) have palindromic coefficient sequences of degree \(d\), establishing \(\mathcal M_d(t)=\mathcal M_d(1/t)\). Evaluation at \(t=0\) and \(t=1\) completes the extremal formula.

**5. Exact curvature.** Set \(t=e^u\). The second derivative of \(\log S_d(e^u)\) at \(u=0\) is the variance of \(k\) under weights \(\binom dk^2/\binom{2d}d\), namely \(d^2/[4(2d-1)]\). The corresponding derivative of \(\log P_d(e^u)\) is
\[
\sum_{j=1}^d\frac{j(n-j)}{n^2}=\frac{d(d+2)}{6(d+1)}.
\]
Their difference is \(-d(d-1)(d+4)/[12(2d-1)(d+1)]\). Palindromicity makes \(\log\mathcal M_d(e^u)\) even in \(u\), so its Taylor series has no odd-order terms, proving the sharp quadratic expansion with an \(O_d(u^4)\) remainder.

## Verification

The complete proof is analytic and applies to every integer \(d\ge2\), not only tested dimensions. The standalone `verify.py` executes using Python 3 with SymPy, NumPy and SciPy. It checks exact polynomial identities and positive derivative-factor coefficients for dimensions \(2\) through \(12\), the exact logarithmic curvature for those dimensions, strict Legendre/Chebyshev root separation through dimension \(64\), and independent convex-hull primal and halfspace polar volume calculations through dimension \(4\). Running `python3 verify.py` returns `VERIFY_OK 2292` on the included test suite. Finite diagnostics are not treated as a universal proof.

## Relationship to prior work

Kim and Reisner (2010) prove that the simplex is a strict *local minimum* of the Santaló volume product among all convex bodies. Their theorem neither identifies the polar volume of \(\Delta+t(-\Delta)\) nor proves a global increasing/decreasing profile along this specific one-parameter family. Alonso-Gutiérrez, González and Jiménez (2013) study convolution/difference-body volume inequalities, not this complete Santaló product. Artstein-Avidan and Putterman (2024) study pointwise volumes of *unbalanced difference bodies*; those primal-volume statements cannot determine the opposite-moving polar-volume factor. Marcus, Spielman and Srivastava (2022, Theorem 4.22) explicitly quote the classical Stieltjes zero comparison used in step 4, which is a **known ingredient**, not part of the claimed novelty. A publicly available geometric result on a higher-order unbalanced simplex-volume profile likewise optimizes the primal volume alone and does not imply the present product theorem. A general lower bound for simplex-symmetric bodies by Barthe and Fradelizi, reported in Makai's 2015 survey, establishes a different, lower comparison; its full primary article was not materially accessible and is an originality risk.

## Limitations

The strict monotonicity is proved only for sums of one simplex and its reflection; no universal statement for arbitrary convex bodies is claimed. The polar is taken at the Santaló point, and replacing it with an arbitrary origin would change the product. The precise second-order expansion is local, while the maximum assertion is global. The originality assessment compares the inspected primary results and published-record searches by implication, but cannot exclude a differently named older equivalent result. The Barthe–Fradelizi article is a notable unresolved full-text comparison. Independent validation has not been performed.

## References

1. Jaegil Kim and Shlomo Reisner, *Local minimality of the volume-product at the simplex*, arXiv:1001.0217, first publicly available 2010-01-01. Primary MSC2020 52A40. https://arxiv.org/abs/1001.0217
2. David Alonso-Gutiérrez, Bernardo González and Carlos Hugo Jiménez, *Volume inequalities for the i-th-Convolution bodies*, arXiv:1312.6005, first publicly available 2013-12-20. https://arxiv.org/abs/1312.6005
3. Shiri Artstein-Avidan and Eli Putterman, *On unbalanced difference bodies and Godbersen's conjecture*, arXiv:2412.05308, first publicly available 2024-11-27. https://arxiv.org/abs/2412.05308
4. Adam W. Marcus, Daniel A. Spielman and Nikhil Srivastava, *Finite free convolutions of polynomials*, Probability Theory and Related Fields 182 (2022), Theorem 4.22 (Stieltjes root comparison). https://doi.org/10.1007/s00440-021-01105-w
5. F. Barthe and M. Fradelizi, *The volume product of convex bodies with many hyperplane symmetries*, American Journal of Mathematics 135 (2013); comparison through the theorem summarized in E. Makai Jr., *The recent status of the volume product problem*, arXiv:1507.01473. https://arxiv.org/abs/1507.01473
