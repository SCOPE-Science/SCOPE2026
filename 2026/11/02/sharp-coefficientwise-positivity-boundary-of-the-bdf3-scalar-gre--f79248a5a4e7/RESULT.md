# Sharp coefficientwise positivity boundary of the BDF3 scalar Green sequence

## Finding
Let \(\mu>0\), set \(x=(11+6\mu)^{-1}\), and define the causal BDF3 Green sequence by
\[
G_0=1,\quad G_1=18x,\quad G_2=324x^2-9x,\qquad
G_n=18xG_{n-1}-9xG_{n-2}+2xG_{n-3}\quad(n\ge3).
\]
Write
\[
H(x)=34012224x^4-4723920x^3+204120x^2-2673x+4.
\]
There is a unique zero \(x_*\) of \(H\) in \((1/16,76/1215)\), namely \(x_*=0.0625485340197980\ldots\). Define
\[
\mu_* = \frac{x_*^{-1}-11}{6}=0.831264155297064\ldots.
\]
Then the following condition is **necessary and sufficient**, over the entire half-line \(\mu>0\):
\[
\boxed{G_n(\mu)\ge0\text{ for all integers }n\ge0\quad\Longleftrightarrow\quad0<\mu\le\mu_*.}
\]
At \(\mu=\mu_*\), \(G_6=0\) and the remaining coefficients are strictly positive. For \(\mu_*<\mu\le5/6\), already \(G_6<0\); for \(\mu>5/6\), infinitely many Green coefficients are strictly positive and infinitely many are strictly negative. In particular, the scalar causal convolution gain
\[
\Lambda_3(\mu)=(1-11x)\sum_{n\ge0}|G_n(\mu)|
\]
is exactly \(1\) precisely for \(0<\mu\le\mu_*\), and strictly greater than \(1\) otherwise.

## Assumptions and scope
The exact-arithmetic statement concerns the **zero-prehistory impulse response** of the constant-step third-order backward differentiation (BDF3) scalar difference operator, with positive real spectral parameter \(\mu=k\lambda\) and \(x=(11+6\mu)^{-1}\in(0,1/11)\). The generating function is
\[
\sum_{n\ge0}G_nz^n=\bigl(1-18xz+9xz^2-2xz^3\bigr)^{-1}.
\]
This is a coefficientwise positivity classification, not a claim that the entire multistep evolution with arbitrary starting values is positive, or that its PDE discretization obeys a maximum principle.

## Proof
**1. First negative coefficient and isolation of the boundary.** Expanding the defining recurrence gives
\[
G_6(x)=x^2H(x).
\]
Put \(\ell=1/16\), \(t=76/1215\), and \(u=256/3915\). Rational arithmetic yields
\[
\ell<t<u<1/11,\qquad H(\ell)=-35/1024<0,\qquad H(t)=8464/4100625>0.
\]
The degree-three polynomial \(H'\) has all-positive exact Bernstein coefficients on \([\ell,u]\), the minimum being \(5589/8>0\). Thus \(H\) is strictly increasing on this interval, proving the unique root \(x_*\in(\ell,t)\). It also proves \(G_6<0\) throughout \(x\in[\ell,x_*)\), corresponding to \(\mu_*<\mu\le5/6\).

**2. A positive order-eight recurrence on the narrow boundary interval.** Define
\[
P(x)=104976x^3-11664x^2+351x-2,\qquad
W(x)=66339x^2-3888x-16.
\]
The following identity holds for **every integer** \(n\ge0\):
\[
G_{n+8}=\frac{H(x)}{18P(x)}G_{n+7}
+\frac{x^2W(x)}{18P(x)}G_{n+1}
+\frac{x^3(76-1215x)}{P(x)}G_n.
\tag{1}
\]
Indeed, the polynomial \(z^8-\frac{H}{18P}z^7-\frac{x^2W}{18P}z-\frac{x^3(76-1215x)}P\) is divisible by \(z^3-18xz^2+9xz-2x\); equivalently, cross-multiplying (1) and using the original order-three recurrence verifies the relation for three consecutive indices, after which it follows inductively for all indices.

On \([x_*,t]\), one has \(P>0\), \(W>0\), \(H\ge0\), and \(76-1215x\ge0\). The initial eight terms are nonnegative, because \(G_0,G_1>0\), \(G_6=x^2H\ge0\), and the remaining \(G_2,G_3,G_4,G_5,G_7\) are strictly positive on the larger rational interval \([\ell,u]\). Therefore the **infinite** sequence is nonnegative on \([x_*,t]\), by (1). At \(x=x_*\), the last two coefficients of (1) are strictly positive and the positive seeds force \(G_n>0\) for every \(n\ne6\).

**3. A second positive recurrence on the next interval.** On \([t,u]\), the independent identity
\[
G_{n+7}=\frac{2916x^2-117x-4}{2(81x-1)}G_{n+6}
+\frac{x(1215x-76)}{2(81x-1)}G_{n+4}
+\frac{8x^2}{81x-1}G_n
\tag{2}
\]
holds for all \(n\ge0\). Its generating polynomial is likewise divisible by the original cubic characteristic polynomial. Every coefficient in (2) is nonnegative on \([t,u]\) and the initial seven terms \(G_0,\ldots,G_6\) are nonnegative; consequently every later coefficient is nonnegative.

For completeness, the exact positivity certificates for steps 1–3 are as follows. The minimum Bernstein coefficients over the indicated rational intervals are:

| Polynomial | Interval | Minimum Bernstein coefficient |
|---|---|---|
| \(H'\) | \([\ell,u]\) | \(5589/8\) |
| \(P\) | \([\ell,u]\) | \(1/256\) |
| \(W\) | \([\ell,t]\) | \(35/256\) |
| \(2916x^2-117x-4\) | \([t,u]\) | \(184/2025\) |
| \(G_2/x\), \(G_3/x\) | \([\ell,u]\) | \(45/4\), \(145/32\) |
| \(G_4/x^2\), \(G_5/x^2\) | \([\ell,u]\) | \(261/16\), \(9/128\) |
| \(G_7/x^3\) | \([\ell,u]\) | \(16065/512\) |

All these entries are **strictly positive exact rationals**, not floating-point samples. If \(f(x)=\sum_{j=0}^df_jx^j\), each certificate follows by expanding \(f(a+(b-a)v)\) in the Bernstein basis \(\binom{d}{j}v^j(1-v)^{d-j}\), whose terms are nonnegative and sum to one. The included standalone checker reconstructs the certificates and both recurrence identities using integer and rational arithmetic.

**4. Positivity above the source's previously sufficient rational endpoint.** For \(u\le x<1/11\), set \(d=1/x\) and let \(r\) be the unique positive real root of \(d r^3-18r^2+9r-2=0\). Put \(D(r)=18r^2-9r+2\), \(E(r)=3r^2-3r+1\). The relation \(d=D(r)/r^3\) is strictly decreasing in \(r>0\), and \(x=u\) corresponds to \(r=8/15\). Hence \(r\ge8/15\). The other characteristic roots form a nonreal conjugate pair of modulus \(\rho\), with \(\rho^2=2r^2/D(r)\le r^2\). In the partial fractions
\[
G_n=A_0r^n+B_0z^n+\overline{B_0}\,\overline z^n,
\qquad A_0=\frac{D(r)}{6E(r)}>0,
\]
one has \(A_0^2-4|B_0|^2=D(r)T(r)/[12E(r)^2(21r^2-12r+4)]\), where
\[
T(r)=126r^4-135r^3+42r^2+12r-8.
\]
The inequalities \(T(8/15)=344/5625>0\), \(T'(8/15)>0\), \(T''(r)>0\) for \(r\ge8/15\) imply \(A_0\ge2|B_0|\). Thus \(G_n\ge(A_0-2|B_0|)r^n\ge0\). This reproduces the source's rational sufficient range, now joined to the extended intervals in steps 2–3.

**5. Sign oscillation above \(\mu=5/6\).** The characteristic cubic's discriminant is \(-108(d^2-27d+189)<0\), so its roots consist of the single real \(r\in(0,1)\) and a nonreal conjugate pair \(z=\rho e^{i\theta},\overline z\), with nonzero residue \(B_0\). For \(\mu>5/6\), \(d>16\), which is equivalent to \(r<1/2\). Therefore \(D(r)<2\) and \(\rho^2=2r^2/D(r)>r^2\). The leading term of \(G_n\) is \(2\rho^n\operatorname{Re}(B_0e^{in\theta})\), with an exponentially smaller \(A_0r^n\) correction. If \(\theta/(2\pi)\) is irrational, its phase visits positive and negative cosine arcs infinitely often by density. If it is rational, the corresponding finite phase orbit has order at least three and cosine values of both signs, hence each sign occurs infinitely often. This proves persistent signed coefficients for \(\mu>5/6\), completing necessity.

**6. Gain equivalence.** All three characteristic roots have modulus below one for \(\mu>0\): the real \(r\) is below one, and \(\rho^2=2r^2/D(r)<1\) because \(D(r)-2r^2=16r^2-9r+2>0\). Evaluating the absolutely convergent generating function at \(z=1\) gives \((1-11x)\sum_nG_n=1\). Consequently
\[
\Lambda_3(\mu)=1+2(1-11x)\sum_{\{n:G_n<0\}}|G_n|.
\]
It equals one exactly in the classified positivity interval, and exceeds one outside it.

## Verification
Run `python3 bdf3_green_verify.py` with Python 3.9+ and no third-party packages. It reconstructs all \(G_0,\ldots,G_{17}\) as integer polynomials, verifies (1) and (2) after denominator clearing for five consecutive indices (hence, by the original recurrence, identically for all indices), checks all displayed rational Bernstein coefficients, establishes existence and uniqueness of \(x_*\) in its rational bracket, and computes a non-probative numerical approximation. The decisive infinite-sequence arguments are the two positive-coefficient recurrences and the characteristic-root comparison, not finite sampling.

## Relationship to prior work
W. Qiu, *Long-time stability and convergence of a BDF3 method for a parabolic equation with fading memory*, arXiv:2610.32364v1 (first public release 23 October 2026), Section 4.2 and Appendix B.1, defines precisely this Green sequence and proves the sufficient coefficientwise positivity range \(x\ge256/3915\), equivalently \(\mu\le1099/1536\). The present result gives the **necessary-and-sufficient** positivity interval and a first-sign-loss mechanism, extending that sufficient interval to \(\mu_*=0.831264\ldots\). The source's global upper bound for \(\Lambda_3\) is not challenged. General BDF3 absolute stability, coefficientwise positivity and positivity of full multistep solutions are distinct propositions. Thomée–Wahlbin's 1994 lower-order fading-memory analysis treats backward Euler and BDF2, not this BDF3 sharp boundary.

## Limitations
This theorem concerns scalar, constant-stepsize, zero-prehistory Green weights only. It does not assert positivity for arbitrary initial histories, discrete PDE states or quadrature-coupled memory trajectories. The numerical digits for \(\mu_*\) are approximations; exact root isolation and the all-index proof are algebraic. Historical priority beyond the inspected literature is not independently certified. An independent audit has not been performed.

## References
- W. Qiu, *Long-time stability and convergence of a BDF3 method for a parabolic equation with fading memory*, arXiv:2610.32364v1, 23 October 2026. https://arxiv.org/html/2610.32364v1
- V. Thomée and L. Wahlbin, work on long-time BDF1/BDF2 stability of parabolic equations with memory, *Mathematics of Computation* **62** (1994), 477–496; discussed in Qiu's introduction and references.
- Z. Li and H. L. Liao, *Stability of variable-step BDF2 and BDF3 methods*, arXiv:2201.00527 (2022). https://arxiv.org/abs/2201.00527
