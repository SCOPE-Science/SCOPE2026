# A sharp M-class phase boundary and quadratic onset for compound-Poisson Beta jumps

## Finding

Let \(N\sim\operatorname{Poisson}(\lambda)\) with \(\lambda>0\), independently of i.i.d. jumps \(J_i=LZ_i\), where \(L>0\) and \(Z_i\sim\operatorname{Beta}(\alpha,\beta)\), with both shape parameters strictly positive. Define the centered compound sum \(X=\sum_{i=1}^{N}J_i-\lambda\mathbb EJ\) and fix its true variance \(V=\lambda\mathbb EJ^2>0\). Write \(c_*\) for the least nonnegative \(c\) satisfying the right sub-gamma inequality
\[
\log\mathbb E e^{tX}\leq\frac{Vt^2}{2(1-ct)},\qquad 0\leq t<1/c.
\]
The inequality at \(c=0\) uses the entire nonnegative half-line. Put
\[
a=\alpha+2,\quad b=\alpha+\beta+2,\quad m=\frac{La}{3b},\quad
\beta_{\mathrm{crit}}(\alpha)=\frac{(\alpha+2)(\alpha+3)}{1-\alpha}\quad (0<\alpha<1).
\]
**Theorem.** The exact phase classification is
\[
\boxed{c_*=m\quad\Longleftrightarrow\quad
\alpha\geq1\ \text{or}\ [0<\alpha<1\ \text{and}\ \beta\leq\beta_{\mathrm{crit}}(\alpha)].}
\]
For \(0<\alpha<1\) and \(\beta>\beta_{\mathrm{crit}}(\alpha)\), one has \(c_*>m\); the variational supremum defining \(c_*\) is attained at a positive finite argument. At and below the critical line, the optimal value equals the local third-cumulant bound, although the sharp bound is strict at every admissible positive transform argument.

The onset at the critical line is quadratic. For fixed \(0<\alpha<1\), set \(a=\alpha+2\) and \(\delta=\beta-\beta_{\mathrm{crit}}(\alpha)\downarrow0\). For sufficiently small \(\delta>0\), the variational maximizer \(t_*(\beta)\) is unique and
\[
\boxed{t_*(\beta)=\frac{5(a+3)}{2a(a+1)}\frac{\delta}{L}
+O\!\left(\frac{\delta^2}{L}\right).}
\]
Moreover,
\[
\boxed{c_*(\beta)-\frac{La}{3(a+\beta)}
=\frac{5(3-a)^4(a+3)}{6912a^2(a+1)^2}L\delta^2+O(L\delta^3).}
\]
These values are independent of the Poisson intensity \(\lambda\). As a concrete benchmark, uniform jumps \(\alpha=\beta=1\) have the exact optimal scale \(c_*=L/4\), improving the generic jump-range Bernstein scale \(L/3\).

## Assumptions and scope

The model is one-dimensional and right-sided, with finite, strictly positive intensity and bounded positive jumps of the stated Beta shape. The normalization fixes the quadratic proxy to the true variance \(V\), not to an adjustable variance factor. The classification concerns the *least feasible pole scale*, not equality of the cumulant generating function and its rational upper envelope. The statements hold for every real \(\alpha,\beta,\lambda,L>0\), with the critical expansion taken at fixed \(\alpha\in(0,1)\) and fixed \(L>0\). No global uniqueness of the interior optimizer is asserted away from the critical regime.

For reproducibility the dimensionless transform variable is \(s=Lt\). Define the rising factorial \((z)_n=\prod_{j=0}^{n-1}(z+j)\), with \((z)_0=1\), and the entire function
\[
F_{a,b}(s)=\sum_{n=0}^{\infty}\frac{2(a)_n}{(n+2)!(b)_n}s^n.
\]
The exact optimal scale is equivalently
\[
\boxed{c_*=L\sup_{s>0}\frac{1-F_{a,b}(s)^{-1}}{s}.}
\]
The series has strictly positive coefficients and converges for all complex \(s\).

## Proof

**1. Canonical remainder identity.** Since \(N\) is Poisson,
\[
K_X(t)=\lambda(\mathbb E e^{tJ}-1-t\mathbb EJ),\qquad V=\lambda\mathbb EJ^2.
\]
Let \(Y\) have the squared-size-biased jump law \(\Pr(Y\in dy)=y^2\Pr(J\in dy)/\mathbb EJ^2\). Let \(U\sim\operatorname{Beta}(1,2)\) independently and put \(R=UY\). Integrating the Beta density gives, for every real \(z\),
\[
\mathbb Ee^{zU}=2\frac{e^z-1-z}{z^2},
\]
with the continuous value one at zero. Conditioning on \(Y\) yields
\[
K_X(t)=\frac{Vt^2}{2}\mathbb Ee^{tR}.
\]
Squaring the Beta jump density shifts its first shape parameter by two. Thus \(Y/L\sim\operatorname{Beta}(a,\beta)\), and for every integer \(n\geq0\),
\[
\mathbb E(R/L)^n=\frac{2(a)_n}{(n+1)(n+2)(b)_n}.
\]
Consequently \(M_R(t)=F_{a,b}(Lt)\) and \(\mathbb ER=La/(3b)=m\). In particular, \(\kappa_3(X)/(3V)=m\).

**2. Reduction to a one-dimensional optimal scale.** For \(c>0\), the target sub-gamma inequality is equivalent, for \(0<t<1/c\), to \(M_R(t)\leq(1-ct)^{-1}\), which in turn is equivalent to \((1-M_R(t)^{-1})/t\leq c\). For \(t\geq1/c\), this last inequality is automatic because \(0<M_R(t)^{-1}\leq1\). Thus the least feasible scale is precisely the supremum in the Finding. The limit at the origin is \(m\), so \(c_*\geq m>0\).

**3. Exact phase boundary.** Write \(F_{a,b}(s)=\sum_{n\geq0}A_ns^n\). Then \(A_0=1\) and
\[
\frac{A_{n+1}}{A_n}=\frac{a+n}{(b+n)(n+3)}.
\]
Its difference from \(m_0=a/(3b)\) is exactly
\[
\frac{A_{n+1}}{A_n}-m_0
=\frac{n[b(3-a)-a(n+3)]}{3b(b+n)(n+3)},\qquad n\geq0.
\]
For \(n\geq1\), the numerator is nonpositive for every \(n\) if and only if \(b(3-a)\leq4a\). This holds for all \(b>a\) when \(a\geq3\) (equivalently \(\alpha\geq1\)); for \(2<a<3\), it is equivalent to \(\beta\leq a(a+1)/(3-a)=\beta_{\mathrm{crit}}\). In that entire region, \(A_n\leq m_0^n\) for every \(n\geq0\). Summing nonnegative coefficients proves
\[
F_{a,b}(s)\leq\frac{1}{1-m_0s},\qquad0\leq s<1/m_0.
\]
Therefore \(c_*\leq Lm_0=m\); combined with the lower bound, this gives equality. For all \(s>0\) the corresponding \(\Psi(s)=(1-F_{a,b}(s)^{-1})/s\) is strictly less than \(m_0\): within \(0<s<1/m_0\) there is a strict coefficient inequality for some degree \(n\geq2\), and at \(s\geq1/m_0\), \(\Psi(s)<1/s\leq m_0\).

Conversely, if \(2<a<3\) and \(b(3-a)>4a\), then \(A_2>A_1^2\). The expansion \(\Psi(s)=m_0+(A_2-m_0^2)s+O(s^2)\) makes \(\Psi(s)>m_0\) at small positive \(s\). Hence \(c_*>m\). Because \(R/L\in(0,1)\), \(F_{a,b}(s)\) is continuous and finite, \(0<\Psi(s)<1/s\), and \(\Psi(s)\to0\) as \(s\to\infty\); a global positive maximizer exists.

**4. Sharp onset and uniqueness close to the boundary.** Fix \(a\in(2,3)\), let \(b_0=4a/(3-a)\), and write \(b=b_0+\delta\). Expand
\[
\Psi_b(s)=m_0(b)+u(b)s+v(b)s^2+O(s^3),
\]
where \(m_0(b)=a/(3b)\), \(u(b)=A_2(b)-m_0(b)^2\), and \(v(b)=A_3(b)-2m_0(b)A_2(b)+m_0(b)^3\). Substituting the coefficient formula gives
\[
u(b)=\frac{a[b(3-a)-4a]}{36b^2(b+1)},\qquad
u(b_0)=0,
\]
\[
u'(b_0)=\frac{(3-a)^4}{1728a(a+1)}>0,\qquad
v(b_0)=-\frac{(3-a)^4}{8640(a+3)}<0.
\]


At \(b=b_0\), Step 3 gives \(\Psi_{b_0}(s)<m_0(b_0)\) for every \(s>0\), while \(\Psi_{b_0}(s)\to0\) at infinity. By continuity on compact sets, the bound \(\Psi_b(s)\leq1/s\), and \(m_0(b)>0\), any global maximizer for \(\delta\downarrow0\) must approach zero. On a fixed small neighborhood of zero the analytic expansion has uniformly negative second derivative for \(b\) near \(b_0\), because \(2v(b_0)<0\). The derivative at zero is positive for \(\delta>0\), so strict concavity supplies a unique critical point there; it is necessarily the unique global maximizer for sufficiently small \(\delta>0\).

The implicit-function expansion of \(\partial_s\Psi_b=0\) yields
\[
s_*(b)=-\frac{u'(b_0)}{2v(b_0)}\delta+O(\delta^2)
=\frac{5(a+3)}{2a(a+1)}\delta+O(\delta^2).
\]
Substituting this into \(\Psi_b(s_*)\) gives
\[
\Psi_b(s_*)-m_0(b)
=-\frac{u'(b_0)^2}{4v(b_0)}\delta^2+O(\delta^3)
=\frac{5(3-a)^4(a+3)}{6912a^2(a+1)^2}\delta^2+O(\delta^3).
\]
Since \(s=Lt\) and \(c_*=L\Psi_b(s_*)\), the claimed dimensional expansions follow.

## Verification

The standalone file `verify_beta_subgamma.py` implements the stated Beta moments with exact rational arithmetic, tests the coefficient ratio and sign identity across positive shape parameters, verifies the exact critical Taylor coefficients, and compares dimensionless transform scales numerically. Execute it using Python 3 without external dependencies:

`python verify_beta_subgamma.py`

It produces `PASS: 2746 exact rational / numerical consistency assertions`. The algebraic identities were also independently simplified symbolically. These finite tests check the algebra and representative parameter values; the global classification, uniqueness close to the critical line, and all real-parameter assertions follow from the preceding analytical proof, not from those finite tests.

## Relationship to prior work

Chen (2026) established the canonical remainder transform, the exact sub-gamma variational characterization, and its M-class criterion for positive-jump infinitely divisible laws, including compound Poisson laws; those general results are used and not claimed as new. The examples in that paper calculate Gamma-jump and two-point-jump scales, not the two-parameter Beta-jump phase boundary derived here. Chen and Wang (2026) developed the directional extension and Skellam transition; its signed-jump and Skellam results do not specialize to a Beta-distributed positive jump. Klar and Müller (2003) introduced the M-class and general MGF-comparison criteria; they do not state the present squared-size-biased Beta phase classification.

The assessed contribution is the explicit necessary-and-sufficient phase boundary for positive Beta jumps, the interior-versus-local optimizer distinction throughout its full two-shape parameter range, and the quadratic critical onset with explicit constants. The presence of a Beta(1,2) *transform multiplier* in prior work is not a result about Beta-distributed *jump amplitudes*. A general enough unlocated special-function or stochastic-order theorem might subsume the computation; independent priority assessment has not been performed.

## Limitations

The location and value of a global interior optimum away from the critical line are characterized variationally, not by elementary closed form. Global uniqueness of an interior optimizer is not asserted away from sufficiently near criticality. The result is for right-sided variance-matched sub-gamma bounds on positive compound Poisson Beta jumps, not for direct Beta random variables, bilateral jumps, adjustable variance proxies, or arbitrary bounded-jump distributions. Independent priority verification remains an unresolved provenance limitation.

## References

1. Y. Chen (2026), *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws*, arXiv:2610.00032v1, first posted 2026-09-02. https://arxiv.org/html/2610.00032v1
2. Y. Chen and X. Wang (2026), *Directional Optimal Sub-Gamma Scales for Infinitely Divisible Laws*, arXiv:2609.02590v1, first posted 2026-09-02. https://arxiv.org/html/2609.02590v1
3. B. Klar and R. Müller (2003), *Characterizations of classes of lifetime distributions generalizing the NBUE class*, Journal of Applied Probability 40, 20–35. https://doi.org/10.1239/jap/1044476825
