# Sharp Gaussian-dilution transition for optimal sub-gamma scales of Gamma-jump compound Poisson laws

## Finding

Let \(Z\sim N(0,1)\), \(N\sim\operatorname{Poisson}(\lambda)\), and let \(J_i\) be independent \(\operatorname{Gamma}(\alpha,\text{scale }\beta)\) variables; all inputs are independent, with \(\alpha,\beta,\lambda>0\). For \(\sigma^2\ge0\) put
\[
X=\sigma Z+\sum_{i=1}^{N}J_i-\lambda\alpha\beta,
\qquad V=\operatorname{Var}(X)=\sigma^2+\lambda\alpha(\alpha+1)\beta^2,
\qquad w=\frac{\lambda\alpha(\alpha+1)\beta^2}{V}\in(0,1].
\]
The *variance-exact right sub-gamma scale* \(c_*(X)\) is the smallest \(c\ge0\) for which
\[
\log\mathbb E e^{tX}\le\frac{Vt^2}{2(1-ct)}
\quad\text{for every }0\le t<1/c,
\]
interpreting \(1/0=\infty\) and requiring the moment-generating function to be finite at the arguments used. Then:

1. For \(0<\alpha\le1\), \(c_*(X)=\beta\) for every \(0<w\le1\). For each \(\alpha>1\), \(c_*(X)>\beta\) for every \(0<w\le1\).
2. For each fixed \(\alpha>1\), as \(w\downarrow0\),
\[
\frac{c_*(X)}{\beta}=1+\frac{\alpha-1}{\alpha}
\left(\frac{2w}{\alpha^2(\alpha+1)}\right)^{1/(\alpha-1)}
+o_\alpha\!\left(w^{1/(\alpha-1)}\right).
\]
Every maximizing positive dimensionless transform argument \(x_*=\beta t_*\), for sufficiently small \(w\), obeys
\[
1-x_*\sim\left(\frac{2w}{\alpha^2(\alpha+1)}\right)^{1/(\alpha-1)}.
\]
3. For the natural Erlang-2 jump case \(\alpha=2\), write \(r=\sqrt{1-w}\). The optimal scale has the exact global phase diagram
\[
\boxed{\frac{c_*(X)}{\beta}=\begin{cases}
\displaystyle\frac{3(1+r)}{2(1+2r)},&0<w<15/16,\\[3pt]
\displaystyle\frac{4w}{3},&15/16\le w\le1.
\end{cases}}
\]
In the first regime the unique maximizing positive argument is
\[
x_*=\frac{4r-1}{3r};
\]
in the second regime the supremum is attained only as \(x\downarrow0\). In particular \(c_*(X)/\beta=1+w/12+O(w^2)\) as \(w\downarrow0\). The transition from an interior optimum to a cumulant-controlled optimum occurs at exactly \(w=15/16\).

## Assumptions and scope

All Gamma variables use the shape–scale convention \(\mathbb E e^{tJ}=(1-\beta t)^{-\alpha}\) for \(t<1/\beta\). The independent Gaussian variance \(\sigma^2\) may vanish; \(w=0\) is excluded because the compound-Poisson part then vanishes, leaving the Gaussian optimal scale zero. The small-\(w\) limit holds with \(\alpha\) fixed; no uniformity near \(\alpha=1\) is asserted. All optimizations use the true quadratic variance proxy, not an adjustable upper bound.

## Proof

**Reduction to a scalar optimization.** For \(0\le x=\beta t<1\), independence and the compound-Poisson MGF yield
\[
K(t)=\log\mathbb E e^{tX}=\frac{\sigma^2t^2}{2}
+\lambda\big[(1-x)^{-\alpha}-1-\alpha x\big]
=\frac{Vt^2}{2}F_w(x),
\]
with
\[
F_w(x)=1-w+wH_\alpha(x),\qquad
H_\alpha(x)=\frac{2\big[(1-x)^{-\alpha}-1-\alpha x\big]}{\alpha(\alpha+1)x^2},\quad H_\alpha(0)=1.
\]
For \(x\in(0,1)\) define
\[
\Psi_w(x)=\frac{1-F_w(x)^{-1}}x.
\]
The exact scale satisfies \(c_*/\beta=\sup_{0<x<1}\Psi_w(x)\), with the left endpoint limit allowed. Indeed, a candidate \(c\) can be feasible only if \(c\ge\beta\), because the MGF diverges at \(t=1/\beta\). For every \(0<t<1/c\), rearranging the sub-gamma inequality is equivalent to \(\beta\Psi_w(\beta t)\le c\). For \(t\ge1/c\), the bound \(0\le(1-F_w^{-1})/t\le1/t\le c\) is automatic, including at or beyond the MGF boundary with the convention \(F_w^{-1}=0\). Thus the unrestricted supremum gives precisely the feasible optimum. The MGF divergence also gives \(\lim_{x\uparrow1}\Psi_w(x)=1\).

**The shape-one threshold.** Write \(H_\alpha(x)=\sum_{j\ge0}a_jx^j\), where \(a_0=1\) and
\[
\frac{a_{j+1}}{a_j}=\frac{\alpha+j+2}{j+3}.
\]
If \(\alpha\le1\), then \(a_j\le1\) and \(H_\alpha(x)\le(1-x)^{-1}\). Since \(F_w=(1-w)+wH_\alpha\le(1-x)^{-1}\), it follows that \(\Psi_w(x)\le1\). The positive MGF boundary then gives equality \(c_*=\beta\). If \(\alpha>1\), with \(\delta=1-x\downarrow0\),
\[
H_\alpha(1-\delta)\sim C_\alpha\delta^{-\alpha},
\quad C_\alpha=\frac{2}{\alpha(\alpha+1)},
\quad F_w(1-\delta)^{-1}\sim\frac{\delta^\alpha}{wC_\alpha}=o(\delta).
\]
Hence \(\Psi_w(1-\delta)=(1-o(\delta))/(1-\delta)>1\) for all sufficiently small positive \(\delta\). This proves strict inequality for every fixed \(w>0\).

**Small-jump-variance singular layer.** Fix \(\alpha>1\), let \(\epsilon=(wC_\alpha/\alpha)^{1/(\alpha-1)}\), and put \(\delta=\epsilon u\). On compact subsets \(0<u<\infty\), as \(w\downarrow0\),
\[
F_w(1-\epsilon u)^{-1}=\frac{\epsilon u^\alpha}{\alpha}(1+o(1)),\qquad
\frac{\Psi_w(1-\epsilon u)-1}{\epsilon}
=u-\frac{u^\alpha}{\alpha}+o(1).
\]
The limiting function has the unique maximum at \(u=1\), of height \((\alpha-1)/\alpha\). This is the *global* scale: if a competing sequence has \(\delta\) bounded away from zero, then \(\Psi_w\to0\); if \(\delta/\epsilon\to0\), then \(\Psi_w-1\le\delta/(1-\delta)=o(\epsilon)\). Finally, if \(\delta\downarrow0\) and \(\delta/\epsilon\to\infty\), the estimate \(H_\alpha(1-\delta)\le2C_\alpha\delta^{-\alpha}\) applies eventually. Whenever \(w(H_\alpha-1)\le1\), one has \(F_w^{-1}\ge1/2>\delta\); otherwise \(F_w\le1+2wC_\alpha\delta^{-\alpha}\le4wC_\alpha\delta^{-\alpha}\) and
\[
F_w^{-1}\ge\frac{\delta^\alpha}{4wC_\alpha}>\delta
\]
for \(\delta/\epsilon\) large enough. In either case \(\Psi_w\le1\). Therefore all maximizing sequences lie in a compact positive \(u\)-range, and the limiting unique maximizer forces \(u\to1\) and the claimed constant. (In the latter estimate, if \(wH_\alpha\) is the quantity compared to one, the same dichotomy applies with harmless universal constants.)

**Exact Erlang-2 maximization.** At \(\alpha=2\), an exact cancellation gives
\[
H_2(x)=\frac{3-2x}{3(1-x)^2},\qquad
\Psi_w(x)=\frac{w(4-3x)}{3(1-x)^2+wx(4-3x)}.
\]
Writing \(\delta=1-x\), the derivative of the final expression with respect to \(\delta\) has the sign of
\[
\Theta_w(\delta)=w-(1-w)(6\delta+9\delta^2).
\]
This is strictly decreasing on \([0,1]\) for \(w<1\), with \(\Theta_w(0)=w>0\) and \(\Theta_w(1)=16w-15\). If \(w<15/16\), the unique maximizer is \(\delta_*=(1-r)/(3r)\in(0,1)\), yielding \(\Psi_w(1-\delta_*)=3(1+r)/[2(1+2r)]\). For \(w\ge15/16\), \(\Psi_w\) increases through \(\delta\in[0,1)\), and its supremum is its \(\delta=1\) limit \(4w/3\). The endpoint \(w=1\) follows by direct substitution. Expanding the first branch at \(w=0\) gives \(1+w/12+O(w^2)\), agreeing with the general boundary layer. This completes all claims.

## Verification

The standalone script `check_gamma_gaussian.py` uses exact rational arithmetic to compare two independently written expressions for the Erlang-2 objective across 3,969 rational input pairs, and numerical arithmetic to compare the closed-form maximum against 99,900 grid values across weight parameters, as well as the shape threshold, moment transform, and small-weight coefficient. Run `python check_gamma_gaussian.py` from the package directory. Its recorded output is in `verification_output.txt`. These tests are finite sanity checks, not proofs of the quantifiers above.

## Relationship to prior work

Y. Chen (2026), arXiv:2610.00032v1, Theorem 3.1 and Proposition 7.1, proves the general variational characterization and the optimal *unmixed* compound-Poisson Gamma-jump scale \(\beta\max\{1,(\alpha+2)/3\}\); Section 5 establishes general convolution monotonicity. The present result starts from those known mathematical structures but optimizes the Gaussian–jump mixture, determining a new sharp weight-dependent phase diagram and singular small-weight boundary layer. Chen and Wang (2026), arXiv:2609.02590v1, develops directional generalizations and related Skellam transitions; its signed-jump setting and stated examples do not give this Gaussian-diluted Gamma-jump calculation. No historical-priority certification is claimed.

## Limitations

The jump distribution must be Gamma with common shape and scale and the added perturbation Gaussian; the result does not classify arbitrary jump laws or non-Gaussian smoothing. The small-weight expansion is fixed-shape rather than uniform as \(\alpha\downarrow1\). The source variational formula already implies an abstract optimization; the contribution is its explicit solution and singular asymptotic in the stated natural family. The non-Gaussian parameter region \(w>0\) is essential: at \(w=0\) the optimal scale drops discontinuously to zero.

## References

1. Y. Chen, *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws*, arXiv:2610.00032v1 (first public 2026-09-02), https://arxiv.org/html/2610.00032v1.
2. Y. Chen and X. Wang, *Directional Optimal Sub-Gamma Scales for Infinitely Divisible Laws*, arXiv:2609.02590v1 (first public 2026-09-02), https://arxiv.org/abs/2609.02590.
