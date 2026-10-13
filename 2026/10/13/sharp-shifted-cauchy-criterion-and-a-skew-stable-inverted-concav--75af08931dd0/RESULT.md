# Sharp shifted-Cauchy criterion and a skew-stable inverted-concavity region

## Finding

Write \(\mathcal H\) for the class of positive random variables \(X\) with essential infimum zero for which
\[
G_X(t):=\Pr(X>1/t),\qquad t>0,
\]
is concave. Let \(C\) be standard symmetric Cauchy, let \(T_\alpha\) be independent of \(C\), with \(\mathbb E[e^{-sT_\alpha}]=e^{-s^\alpha}\) for \(0<\alpha<1\), and set \(T_1=1\).

**Theorem (Cauchy gateway and stable region).** For every \(0<\alpha\le1\) and every real \(m\) satisfying \(|m|\le1/\sqrt3\),
\[
|T_\alpha(C+m)|\in\mathcal H.
\]
For \(\alpha=1\), this restriction is necessary as well as sufficient:
\[
|C+m|\in\mathcal H\quad\Longleftrightarrow\quad |m|\le1/\sqrt3.
\]
For \(0<\alpha<1\), denote by \(Z_{\alpha,\beta}\) any strictly \(\alpha\)-stable random variable having zero location, arbitrary positive scale, and skewness \(\beta\in[-1,1]\) in the parameterization
\[
\mathbb E[e^{itZ_{\alpha,\beta}}]=\exp\{-\sigma^\alpha|t|^\alpha[1-i\beta\tan(\pi\alpha/2)\operatorname{sgn}(t)]\}.
\]
Then the explicit, nonempty two-parameter region
\[
\boxed{\quad 0<\alpha<1,\qquad |\beta|\le b_\alpha:=\frac{\tan(\pi\alpha/6)}{\tan(\pi\alpha/2)}\quad}
\]
satisfies \(|Z_{\alpha,\beta}|\in\mathcal H\). In particular, **the magnitude of every centered symmetric strictly stable law with \(0<\alpha\le1\) is inverted concave** (including the Cauchy endpoint).

As an immediate application of the previously established stochastic-order theorem of Chen, Hu, Shneer and Zou, whenever \(X_1,\ldots,X_n\) are independent copies of any one of these positive magnitude laws and nonnegative vectors \(\theta\) and \(\eta\) satisfy \(\theta\preceq\eta\) in majorization order, then
\[
\sum_{j=1}^n\eta_jX_j\le_{\rm st}\sum_{j=1}^n\theta_jX_j.
\]
The new assertion is the class membership and its sharp Cauchy-shift gateway, not the general stochastic-order implication.

## Assumptions and scope

The Cauchy density is \(f_C(c)=1/[\pi(1+c^2)]\); all factors are independent as stated. For \(0<\alpha<1\), \(T_\alpha\) is the unit positive stable variable with the specified Laplace transform; at \(\alpha=1\) it is degenerate at one. The skewness definition fixes the strict-stable location convention for \(\alpha\ne1\); arbitrary positive scale does not change membership in \(\mathcal H\). No assertion is made about general nonzero location shifts of strictly stable laws for \(\alpha<1\), or about skewness beyond the displayed region. The ratio \(1/\sqrt3\) is the sharp boundary in the standardized shifted-Cauchy generator, *not* a proved sharp skewness boundary for the entire stable family.

For an absolutely continuous positive \(X\) with density \(f\), \(X\in\mathcal H\) is equivalent to \(x\mapsto x^2 f(x)\) being nondecreasing on \((0,\infty)\), by differentiation of \(G_X(t)\). This criterion is taken from the lead paper.

## Proof

**1. Exact shifted-Cauchy threshold.** By folding the location-shifted Cauchy density, for \(x>0\),
\[
f_{|C+m|}(x)=\frac1\pi\left[\frac1{1+(x-m)^2}+\frac1{1+(x+m)^2}\right].
\]
Put \(d_-(x)=1+(x-m)^2\) and \(d_+(x)=1+(x+m)^2\). Direct differentiation and collection of terms give the exact identity
\[
\frac{d}{dx}\bigl[x^2f_{|C+m|}(x)\bigr]
=\frac{4x}{\pi d_-(x)^2d_+(x)^2}\,P_m(x),
\]
where
\[
P_m(x)=(1-3m^2)x^4+2(1+m^2)^2x^2+(1+m^2)^3.
\]
If \(3m^2\le1\), each nonzero term of this polynomial is nonnegative and the constant term is positive, so the derivative is strictly positive for every \(x>0\). If \(3m^2>1\), the leading coefficient is negative and \(P_m(x)<0\) for all sufficiently large \(x\), contradicting inverted concavity. This proves the if-and-only-if statement at \(\alpha=1\), including the boundary.

**2. Independent positive scaling.** Let \(A\in\mathcal H\) and \(B>0\) be independent. For any \(t>0\), conditioning on \(B\) yields
\[
G_{AB}(t)=\mathbb E[G_A(tB)].
\]
Every map \(t\mapsto G_A(tb)\) is concave for fixed \(b>0\); averaging preserves concavity. The product retains essential infimum zero because \(A\) does and \(B\) is positive and finite almost surely. Thus \(AB\in\mathcal H\). This closure is an elementary consequence of the closure results of Chen et al. and is used as a lemma, not offered as an independent novel result. Taking \(A=|C+m|\), \(B=T_\alpha\), Step 1 proves the first statement for all \(0<\alpha\le1\).

**3. Exact stable skewness map.** For \(0<\alpha<1\), the Laplace transform of \(T_\alpha\) extends analytically to the open right half-plane. Conditioning on \(T_\alpha\) and using the Cauchy characteristic function gives for real \(t\)
\[
\begin{aligned}
\mathbb E[e^{itT_\alpha(C+m)}]
&=\mathbb E[e^{-(|t|-imt)T_\alpha}]\\
&=\exp\!\left[-(|t|-imt)^\alpha\right].
\end{aligned}
\]
Writing \(\vartheta=\arctan m\), this exponent is
\[
-|t|^\alpha(1+m^2)^{\alpha/2}\bigl[\cos(\alpha\vartheta)-i\operatorname{sgn}(t)\sin(\alpha\vartheta)\bigr].
\]
Since \(\cos(\alpha\vartheta)>0\), comparison with the displayed stable parameterization identifies positive scale through
\[
\sigma^\alpha=(1+m^2)^{\alpha/2}\cos(\alpha\vartheta)
\]
and skewness
\[
\beta_\alpha(m)=\frac{\tan(\alpha\arctan m)}{\tan(\pi\alpha/2)}.
\]
For each fixed \(0<\alpha<1\), this is continuous, odd and strictly increasing as \(m\) ranges over \([-1/\sqrt3,1/\sqrt3]\), with endpoints \(\pm b_\alpha\), because \(\arctan(1/\sqrt3)=\pi/6\). Thus every \(\beta\) in the claimed interval comes from a unique admissible \(m\). Positive scale changes preserve \(\mathcal H\), completing the skew-stable result. Set \(m=0\) to obtain all symmetric stable indices; \(\alpha=1\) follows directly from Step 1.

**4. Stochastic-order consequence.** Theorem 1 of Chen, Hu, Shneer and Zou states that independent identically distributed nonnegative inverted-concave losses satisfy the displayed majorization-reversed usual stochastic order. Each magnitude law established above meets its hypotheses, so the conclusion follows without an additional stochastic-order argument.

## Verification

The accompanying `verify.py` independently checks the folded-Cauchy derivative identity with exact rational arithmetic over a finite two-dimensional grid, checks the sign for interior rational shifts, and compares the two stable characteristic-function parameterizations at multiple parameter values. Running `python3 verify.py` produces a PASS line with 2,530 assertions. The checks are finite diagnostics; the proof for every real admissible parameter and every \(x>0\) is the polynomial sign argument, conditional-concavity argument and analytic characteristic-function identity above. The code requires only the Python standard library.

## Relationship to prior work

Chen, Hu, Shneer and Zou (arXiv:2505.01739; later journal article) introduce inverted concavity, prove its stochastic-order consequence, give closure results, and explicitly ask whether absolute stable laws with stability indices up to one and positive stable laws are inverted concave. They give the centered absolute Cauchy and Lévy cases but do **not** provide the skew-stable region or exact shifted-Cauchy threshold. Their general closure and stochastic-order theorems are credited rather than claimed as new. Mainardi, Pagnini and Gorenflo (arXiv:math/0702133) develop the classical Mellin/subordination representation of skew stable laws via skew Cauchy kernels; the probabilistic subordination identity is not itself new here. Bridaa, Jedidi and Sendov (DOI below) give an earlier exact monotonicity criterion for reciprocals of **positive one-sided** stable variables, a distinct and potentially stronger result on that different family; that result is not recast as a new theorem here. Chen and Shneer (2025/2026, ASTIN Bulletin) establish broader stochastic-dominance sufficient conditions but not this inverted-concavity classification of magnitudes.

The exact polynomial transition in the folded *shifted* Cauchy density and the resulting explicitly quantified asymmetric stable region are the additional mathematical statements. Published-results and record searches are evidence of an originality comparison, not a proof of global priority.

## Limitations

The skewness interval is sufficient, not claimed maximal; other methods might cover larger skewness or give nonmembership beyond it. The endpoint \(\alpha=1\) is treated as a shifted Cauchy law, not the general skew-stable parameterization (whose usual tangent form is singular there). These results are distributional population statements, not finite-sample estimation. The proof does not address absolute stable laws with \(\alpha>1\), or stable laws with nonzero location for \(\alpha<1\). Independent scientific audit has not been performed.

## References

1. Y. Chen, T. Hu, V. Shneer, Z. Zou, *Stochastic dominance for linear combinations of infinite-mean risks*, arXiv:2505.01739 (first posted 2025-05-03); *Journal of Applied Probability* (2026), DOI: 10.1017/jpr.2026.10138.
2. F. Mainardi, G. Pagnini, R. Gorenflo, *Mellin transform and subordination laws in fractional diffusion processes*, *Fractional Calculus and Applied Analysis* 6 (2003), 441–459; arXiv:math/0702133 (posted 2007).
3. S. Bridaa, W. Jedidi, H. Sendov, *Generalized unimodality and subordinators, with applications to stable laws and to the Mittag-Leffler function*, *Journal of Theoretical Probability* 37 (2024), 1–42, DOI: 10.1007/s10959-023-01242-z.
4. Y. Chen, V. Shneer, *Risk aggregation and stochastic dominance for a class of heavy-tailed distributions*, *ASTIN Bulletin* 56 (2026), 206–219; first publicly posted as arXiv:2408.15033 (2024-08-27), DOI: 10.1017/asb.2025.10053.
