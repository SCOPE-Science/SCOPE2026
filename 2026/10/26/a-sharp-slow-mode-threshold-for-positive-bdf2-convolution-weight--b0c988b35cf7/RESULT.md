# A sharp slow-mode threshold for positive BDF2 convolution weights of finite exponential mixtures

## Finding

Let \(0\le a<b<\infty\), let \(h>0\), and consider the positive relaxation-window memory kernel
\[
 k_{a,b}(t)=\int_a^b e^{-st}\,ds=\frac{e^{-at}-e^{-bt}}{t}\qquad(t>0),
\]
with Laplace symbol \(F_{a,b}(z)=\log((z+b)/(z+a))\) for \(\operatorname{Re}z>0\). Define the **uncorrected BDF2 convolution-quadrature weights** \((w_n(h))_{n\ge0}\) by the Taylor series at zero
\[
 \sum_{n\ge0}w_n(h)\zeta^n
 =F_{a,b}\!\left(\frac{3/2-2\zeta+\zeta^2/2}{h}\right).
\]
The exact coefficientwise-positivity criterion is
\[
 \boxed{\bigl(\forall n\ge0:\ w_n(h)>0\bigr)
 \quad\Longleftrightarrow\quad ha\le\tfrac12.}
\]
For \(ha>1/2\), \(w_0(h)>0\) but infinitely many positive-index weights are strictly negative and infinitely many are strictly positive. The upper rate \(b\) does not alter the threshold, provided \(b>a\). In particular, \(a=0\) yields strictly positive weights for every \(h>0\), even when the interval includes high relaxation rates whose individual exponential-mode BDF2 weights oscillate in sign.

## Assumptions and scope

All parameters are real, \(0\le a<b<\infty\) and \(h>0\); no asymptotic small-step assumption is made. All coefficients are from the standard BDF2 generating symbol \(\delta(\zeta)=3/2-2\zeta+\zeta^2/2\), without starting corrections. The logarithm denotes the analytic germ chosen real at \(\zeta=0\); equivalently use the integral of resolvents \(\int_a^b h/(\delta(\zeta)+hs)\,ds\). This fixes its branch unambiguously. The kernel has a strictly positive continuous-time value at every \(t>0\). Coefficientwise weight positivity is equivalent to positivity preservation of every finite causal discrete convolution on arbitrary entrywise nonnegative sampled inputs (including impulses); this is not the weaker positive-definiteness property of a convolution quadratic form.

## Proof

**Step 1: an exact coefficient representation.** Put \(c_s=3/2+s\) and, for \(s\ge0\), define
\[
 q_s=\frac{\sqrt{1-2s}}2,\qquad
 \lambda_\pm(s)=\frac{1}{2(1\mp q_s)},\qquad
 p_n(s)=\lambda_+(s)^n+\lambda_-(s)^n.
\]
Here the square root is real nonnegative if \(s\le1/2\) and purely imaginary with positive imaginary part if \(s>1/2\). Direct multiplication gives
\[
 \delta(\zeta)+s=c_s(1-\lambda_+(s)\zeta)
 (1-\lambda_-(s)\zeta).
\]
Indeed, \(\lambda_++\lambda_-=2/c_s\) and \(\lambda_+\lambda_-=1/(2c_s)\). Taking the analytic logarithms of the factors around zero shows that, for every integer \(n\ge1\),
\[
 \boxed{w_n(h)=\frac{p_n(ha)-p_n(hb)}{n}},\qquad
 w_0(h)=\log\frac{3/2+hb}{3/2+ha}>0.
\]
These identities also hold at \(s=1/2\), where the two factors coincide.

**Step 2: the nonoscillatory regime.** For \(0\le s\le1/2\), \(q_s\in[0,1/2]\) and
\[
 p_n(s)=2^{-n}\big[(1-q_s)^{-n}+(1+q_s)^{-n}\big].
\]
For every \(n\ge1\), the expression in square brackets increases strictly in \(q_s>0\): its derivative is \(n[(1-q_s)^{-n-1}-(1+q_s)^{-n-1}]>0\). Thus \(p_n(s)\) decreases strictly with \(s\) on \([0,1/2]\) and \(p_n(1/2)=2^{1-n}\).

For \(s>1/2\), the two \(\lambda\)'s are complex conjugates of modulus \((3+2s)^{-1/2}<1/2\), hence
\[
 |p_n(s)|\le2(3+2s)^{-n/2}<2^{1-n}.
\]
If \(ha\le1/2\), either \(hb\le1/2\) and strict monotonicity applies, or \(hb>1/2\) and \(p_n(ha)\ge2^{1-n}>p_n(hb)\). Consequently \(w_n(h)>0\) for every \(n\ge1\), together with the already positive zeroth weight.

**Step 3: sharpness and infinitely many signs.** If \(ha>1/2\), define for \(s>1/2\)
\[
 r_s=(3+2s)^{-1/2},\qquad
 \theta_s=\arctan\frac{\sqrt{2s-1}}2\in(0,\pi/2).
\]
Then \(p_n(s)=2r_s^n\cos(n\theta_s)\). Since \(ha<hb\), one has \(0<r_{hb}/r_{ha}<1\), and thus
\[
 w_n(h)=\frac{2r_{ha}^n}{n}
 \left[\cos(n\theta_{ha})-
 \left(\frac{r_{hb}}{r_{ha}}\right)^n\cos(n\theta_{hb})\right].
\]
For any fixed \(\theta\in(0,\pi/2)\), let \(n_k=\lfloor2\pi k/\theta\rfloor\) and \(m_k=\lfloor(2k+1)\pi/\theta\rfloor\). Then \(\cos(n_k\theta)\ge\cos\theta>0\) and \(\cos(m_k\theta)\le-\cos\theta<0\), for all positive integers \(k\). These indices tend to infinity. The second cosine term in the displayed weight formula is bounded in absolute value by \((r_{hb}/r_{ha})^n\to0\). Thus the weights have infinitely many strictly positive terms and infinitely many strictly negative terms. This proves both necessity and the stronger sign-oscillation conclusion.

## Verification

The accompanying standalone \(\texttt{checks/verify.py}\) uses exact rational arithmetic to generate \(p_n\) through its two-root recurrence and independently computes Taylor coefficients by polynomial division of the logarithmic derivative. Six rational parameter triples agree coefficient by coefficient through order 45, including cases below, at, and above the threshold. Five additional cases compare the complex factorization through 150 coefficients. For \((a,b,h)=(1,2,1)\), the first negative weight occurs at index \(5\); for \((a,b,h)=(1/4,4,1)\), every checked weight is positive. These finite checks are diagnostics only: Step 3 gives the infinite sign conclusion without numerical extrapolation. Run with \(\texttt{python3 checks/verify.py}\) using only the Python standard library.

## Relationship to prior work

The classical Lubich convolution-quadrature construction fixes the generating-symbol framework; the 2026 analysis by Ren and Su derives radial-symbol weight bounds and consistency/error estimates, rather than a coefficientwise sign classification. Karaa's 2024 BDF2 positivity work concerns positive definiteness of convolution quadratic forms, which is logically weaker and distinct from sign of each causal coefficient. Work on completely monotonicity-preserving fractional methods concerns other symbols and/or discretization families. The result here is the exact all-order sign classification for a finite uniform interval of positive exponential relaxation rates, including the unexpectedly independent upper-bandwidth parameter and the sharp transition from positivity to infinitely recurrent sign changes.

## Limitations

This result does not address general nonuniform positive relaxation measures, finite time-window truncations, variable steps, starting corrections, other multistep symbols, or roundoff-induced sign changes. The proof is specialized to the uniform-density spectral interval, for which the Laplace symbol is an elementary logarithmic ratio. No claim of novelty is made for BDF2 convolution quadrature itself, the resolvent formula, or positive-definiteness estimates. Inaccessible older sources may contain an implicit equivalent of this specialized coefficient result.

## References

1. Jingchuang Ren and Haibin Su, *Stability and Error Estimates for Convolution Quadrature under Radial Symbol Bounds*, arXiv:2610.23163v1 (public October 16, 2026). https://arxiv.org/html/2610.23163v1
2. C. Lubich, *Convolution quadrature and discretized operational calculus. I*, Numerische Mathematik 52 (1988), 129–145. https://doi.org/10.1007/BF01398686
3. Samir Karaa, *Positivity of convolution quadratures generated by nonconvex sequences*, Comptes Rendus Mathématique 362 (2024), 1627–1634. https://doi.org/10.5802/crmath.669
4. Lei Li and Dongling Wang, *Complete monotonicity-preserving numerical methods for time fractional ODEs*, arXiv:1909.13060 (2019). https://arxiv.org/abs/1909.13060
