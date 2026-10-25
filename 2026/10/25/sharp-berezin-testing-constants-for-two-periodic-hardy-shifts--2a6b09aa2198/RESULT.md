# Sharp Berezin-testing constants for two-periodic Hardy shifts

## Finding

Let \(H^2(\mathbb D)\) be classical complex Hardy space with orthonormal monomials. For \(a,b\in\mathbb C\), not both zero, define the two-periodic unilateral weighted shift \(T=T_{a,b}\) by
\[
Tz^{2j}=az^{2j+1},\qquad Tz^{2j+1}=bz^{2j+2}\qquad(j=0,1,\ldots).
\]
Let \(\widehat k_z(\lambda)=\sqrt{1-|z|^2}/(1-\overline z\lambda)\) be the normalized Szegő kernel, and let
\[
\operatorname{ber}(T)=\sup_{z\in\mathbb D}|\langle T\widehat k_z,\widehat k_z\rangle|,\qquad
\omega(T)=\sup_{\|f\|=1}|\langle Tf,f\rangle|.
\]
Then the following two sharp inequalities hold **simultaneously**:
\[
\boxed{\operatorname{ber}(T)\ge(3-2\sqrt2)\|T\|},\qquad
\boxed{\operatorname{ber}(T)\ge\frac{\sqrt2-1}{2}\,\omega(T)}.
\]
For either inequality, equality holds if and only if \(b\ne0\) and \(a=-(4\sqrt2-5)b\). Thus exactly the same complex one-parameter family optimizes both independent comparisons. Its Berezin range is the closed disk of radius \((3-2\sqrt2)|b|\); the outer circle is achieved at every kernel parameter with modulus \(\sqrt2-1\).

## Assumptions and scope

The coefficients \(a,b\) are arbitrary complex numbers with \((a,b)\ne(0,0)\); zero coefficients are allowed individually. No positivity or normality is assumed. The norms and Berezin transforms use the standard Hardy Hilbert-space normalization and the inner product linear in the first variable. All suprema are taken over the infinite-dimensional spaces indicated, not finite sections. The result is about classical \(q=1\) Berezin testing, not the full family of \(q\)-Berezin quantities.

## Proof

Write \(z=re^{i\theta}\), where \(0\le r<1\). Summing the even and odd monomial coefficients gives the exact transform
\[
\langle T\widehat k_z,\widehat k_z\rangle
=(1-r^2)z\sum_{j\ge0}(ar^{4j}+br^{4j+2})
=z\frac{a+br^2}{1+r^2}.
\]
Consequently,
\[
\operatorname{ber}(T)=\sup_{0\le r<1}\frac{r|a+br^2|}{1+r^2},
\qquad \|T\|=\max\{|a|,|b|\}.
\tag{1}
\]
The numerical-radius identity is
\[
\omega(T)=\frac{|a|+|b|}{2}.
\tag{2}
\]
Indeed, a diagonal unitary gauges all weights to their moduli. The resulting real-part Jacobi matrix has off-diagonal entries alternating between \(|a|/2\) and \(|b|/2\). Its norm is at most the largest row sum, \((|a|+|b|)/2\). Constant-amplitude vectors on long consecutive blocks force the matching lower bound. Multiplication of the weighted shift by a complex phase is also implemented by a diagonal unitary, so the numerical radius is exactly this Jacobi norm.

Put \(h=\sqrt2-1\), \(c=h^2=3-2\sqrt2\), and \(t_*=1-2c=4\sqrt2-5\). The identities
\[
h^2+2h=1,\qquad
\frac{1-t_*}{2}=c,\qquad
\frac{h(t_*-c)}{1+c}=c,\qquad
\frac{2c}{1+t_*}=\frac h2
\tag{3}
\]
will be used repeatedly. Note \(0<c<t_*<1\).

**First case: \(|a|\ge|b|\).** Evaluating (1) at \(r=1/2\) and using the reverse triangle inequality,
\[
\operatorname{ber}(T)\ge\frac25|a+b/4|
\ge\frac25\left(|a|-\frac{|b|}{4}\right)
\ge\frac3{10}|a|.
\]
Here \(\|T\|=|a|\) and \(\omega(T)\le |a|\), while \(3/10>c\) and \(3/10>h/2\). Both desired bounds are therefore strict.

**Second case: \(|b|\ge|a|\).** Write \(t=|a|/|b|\in[0,1]\). The reverse triangle inequality in (1), evaluated at \(r=h\) and in the boundary limit \(r\uparrow1\), yields
\[
\frac{\operatorname{ber}(T)}{|b|}\ge
\max\left\{\frac{1-t}{2},\frac{h|t-c|}{1+c}\right\}.
\tag{4}
\]
For \(t\le t_*\), the first term of (4) is at least \(c\); for \(t\ge t_*\), the second term (with \(t>c\)) is at least \(c\). Thus the first bound follows, with equality possible only at \(t=t_*\). For the numerical-radius comparison, use (2). When \(t\le t_*\),
\[
\frac{\operatorname{ber}(T)}{\omega(T)}\ge\frac{1-t}{1+t}
\ge\frac{1-t_*}{1+t_*}=\frac h2.
\]
When \(t\ge t_*\),
\[
\frac{\operatorname{ber}(T)}{\omega(T)}
\ge\frac{2h(t-c)}{(1+c)(1+t)}
\ge\frac{2h(t_*-c)}{(1+c)(1+t_*)}=\frac h2,
\]
because \((t-c)/(1+t)\) is strictly increasing. Equality in either comparison forces \(t=t_*\). Equality in the boundary reverse-triangle estimate then forces \(a/b\) to be real and negative, hence \(a=-t_*b\).

**Sharpness and attainment.** Conversely set \(a=-t_*b\) with \(b\ne0\). The radial response in (1), divided by \(|b|\), is
\[
F(r)=\frac{r|r^2-t_*|}{1+r^2}.
\]
On \(0\le r\le\sqrt{t_*}\), the signed branch \(r(t_*-r^2)/(1+r^2)\) has derivative with numerator \(t_*-(t_*+3)r^2-r^4\), strictly decreasing from positive to negative, and its unique maximum occurs at \(r=h\) by (3). The value is \(c\). On \(\sqrt{t_*}\le r<1\), the other branch has derivative numerator \(-t_*+(t_*+3)r^2+r^4>0\), and it increases to \((1-t_*)/2=c\). Hence \(\operatorname{ber}(T)=c|b|\), attained precisely at \(|z|=h\) on the outer Berezin circle. From (2), \(\omega(T)=(1+t_*)|b|/2\), giving the second equality as well. Rotational invariance of the transform and continuity in \(r\) show that the range is the entire closed centered disk in this case. This completes the proof.

## Verification

The accompanying `verify.py` performs exact arithmetic in \(\mathbb Q(\sqrt2)\), independently checks the algebraic identities and critical point, and runs 4,588 supplementary finite computations covering complex coefficient grids, random phase pairs, and the extremal radial profile. Execute `python verify.py` with standard Python 3. These checks are not used in place of the analytic inequalities or the uniqueness argument. No external dataset or third-party package is required.

## Relationship to prior work

Bhattacharya and Patra, *\(q\)-Berezin Range of Operators in Hardy Space* (arXiv:2601.02334), study geometric and convexity properties of \(q\)-Berezin ranges and prove a centered-disk assertion for real weighted shifts. Their Section 3.3 does not establish the present optimal testing constants or complex equality class. Augustine, Garayev, and Shankar (arXiv:2411.10771) study finite-rank Berezin range geometry and general inequalities, not this infinite-rank periodic family. Wang and Wu (2011) treat ordinary numerical ranges of periodic shifts; equation (2) is included only as a proof input and is not claimed to be novel. The new point is the joint sharp comparison between kernel testing, the full numerical radius, and operator norm, together with simultaneous rigidity of extremizers.

## Limitations

The result is restricted to exactly two-periodic unilateral weights in the standard Hardy space and to classical \(q=1\) Berezin testing. It does not give sharp constants for arbitrary bounded weights, higher periods, Bergman kernels, or \(q<1\). No claim of independently certified publication priority is made; an equivalent estimate in unindexed or older literature remains possible. The analytic argument proves the infinite-dimensional result; finite tests serve only as auxiliary checks.

## References

1. D. Bhattacharya and A. Patra, *\(q\)-Berezin Range of Operators in Hardy Space*, arXiv:2601.02334, first posted 2026-01-05, revised 2026-05-05. https://arxiv.org/abs/2601.02334
2. A. Augustine, M. Garayev and P. Shankar, *Convexity of the Berezin range of finite rank operators*, arXiv:2411.10771, first posted 2024-11-16. https://arxiv.org/abs/2411.10771
3. K.-Z. Wang and P. Y. Wu, *Numerical ranges of weighted shifts*, J. Math. Anal. Appl. 381 (2011), 897–909, DOI:10.1016/j.jmaa.2011.04.010.
