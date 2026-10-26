# A multiplicity-driven depth–restart phase diagram for two Gaussian eigenvector probes

## Finding

A fixed budget of two matrix–vector products can either deepen one Gaussian eigenvector probe or test two independent Gaussian probes. For the precisely defined policies below, their relative success probabilities admit exact, **multiplicity-sensitive** classifications. In two dimensions the deeper policy has a reentrant success advantage at intermediate tolerances, although two fresh probes win at both small and large tolerances; in three dimensions the same comparison has a single explicit accuracy threshold rather than a reentrant window.

Fix \(m\in\{1,2\}\), \(\lambda>0\), \(\kappa>1\), and an orthogonal \((m+1)\times(m+1)\) matrix \(Q\). Let
\[
A=\lambda Q\operatorname{diag}(\kappa,1,\ldots,1)Q^{\mathsf T},\qquad
v_*=Qe_1.
\]
For an approximate nonzero eigenvector \(v\), measure angular error by
\[
T(v)=\frac{\|(I-v_*v_*^{\mathsf T})v\|_2}{|v_*^{\mathsf T}v|}\in[0,\infty],
\]
with value \(\infty\) if the denominator vanishes. At tolerance \(\varepsilon>0\), call the output successful when \(T(v)\le\varepsilon\).

The **depth policy**, denoted \(D\), draws one standard Gaussian \(g\in\mathbb R^{m+1}\) and returns the ray spanned by \(A^2g\). The **restart policy**, denoted \(R\), draws independent standard Gaussian \(g^{(1)},g^{(2)}\), forms \(Ag^{(1)},Ag^{(2)}\), and returns the ray spanned by whichever image maximizes the *observable normalized gain* \(\|Ag^{(j)}\|_2/\|g^{(j)}\|_2\). Each policy uses exactly two matrix–vector products; no spectral eigenvectors are used by the selection rule.

For \(m=1\), their exact success probabilities are
\[
\mathbb P_D(\varepsilon)=\frac2\pi\arctan(\kappa^2\varepsilon),\qquad
\mathbb P_R(\varepsilon)=1-\left(1-\frac2\pi\arctan(\kappa\varepsilon)\right)^2.
\]
Define the continuous contrast function and its exact minimum by
\[
H(u)=\frac{\tan(2u-2u^2/\pi)}{\tan u},\qquad
\kappa_*=\min_{0<u<\pi/2}H(u),\qquad 1<\kappa_*<2.
\]
Numerical minimization gives \(\kappa_*\approx1.93910347\); the exact definition is the minimum above, not its numerical approximation. With \(u=\arctan(\kappa\varepsilon)\), the complete pointwise comparison is
\[
\mathbb P_D(\varepsilon)\begin{cases}
>\mathbb P_R(\varepsilon),&\kappa>H(u),\\
=\mathbb P_R(\varepsilon),&\kappa=H(u),\\
<\mathbb P_R(\varepsilon),&\kappa<H(u).
\end{cases}
\]
Thus \(1<\kappa<\kappa_*\) makes restarts strictly better at **every** positive tolerance; at \(\kappa=\kappa_*\) restarts weakly dominate with equality at an interior tolerance. If \(\kappa_*<\kappa<2\), restarts win at sufficiently small and sufficiently large tolerances, while depth wins on a nonempty intermediate interval (there are at least two success-curve crossings). If \(\kappa\ge2\), depth wins for sufficiently small positive tolerances and restarts win for sufficiently large tolerances. For instance, at \(\kappa=39/20\), the two-dimensional comparisons at \(\varepsilon=1/100,1/10,1\) have signs respectively \(D<R,D>R,D<R\).

For \(m=2\), the exact probabilities instead simplify to
\[
\mathbb P_D(\varepsilon)=1-\frac1{\sqrt{1+\kappa^4\varepsilon^2}},\qquad
\mathbb P_R(\varepsilon)=1-\frac1{1+\kappa^2\varepsilon^2}.
\]
If \(1<\kappa\le\sqrt2\), the restart policy is strictly better at every positive tolerance. If \(\kappa>\sqrt2\), then
\[
\begin{aligned}
\mathbb P_D(\varepsilon)&>\mathbb P_R(\varepsilon)
&&\Longleftrightarrow\quad 0<\varepsilon<\sqrt{1-2/\kappa^2},\\
\mathbb P_D(\varepsilon)&=\mathbb P_R(\varepsilon)
&&\Longleftrightarrow\quad \varepsilon=\sqrt{1-2/\kappa^2},\\
\mathbb P_D(\varepsilon)&<\mathbb P_R(\varepsilon)
&&\Longleftrightarrow\quad \varepsilon>\sqrt{1-2/\kappa^2}.
\end{aligned}
\]
In particular, this three-dimensional setting has **one** positive crossing when \(\kappa>\sqrt2\), not the two-or-more crossing phenomenon from the two-dimensional reentrant regime.

## Assumptions and scope

All Gaussian entries are real, independent, centered, and have variance one. Both policies share the same positive-definite input matrix but otherwise independent experiments; selection by normalized gain is a specified algorithmic rule. The target is the unique dominant eigenray, not an eigenvalue estimate or optimal rank-one matrix approximation. The angular tangent is defined with the full Euclidean norm of the trailing eigenspace. All probabilities are exact and all inequalities are strict except on explicitly stated equality boundaries. No restriction is placed on the orthogonal orientation \(Q\) or overall scale \(\lambda\).

## Proof

**Reduction to a Gaussian ratio.** Orthogonal invariance allows us to work in the eigenbasis of \(A\). Write a standard Gaussian as \(g=(Z,Y)\), with \(Z\sim N(0,1)\), \(Y\sim N(0,I_m)\) independent. Almost surely \(Z\ne0\). Put \(S=\|Y\|_2/|Z|\). The two-step depth output has angular tangent \(S/\kappa^2\). For any one-step probe, the tangent is \(S/\kappa\). Its normalized gain squared equals
\[
\lambda^2\frac{\kappa^2Z^2+\|Y\|_2^2}{Z^2+\|Y\|_2^2}
=\lambda^2\frac{\kappa^2+S^2}{1+S^2},
\]
which is strictly decreasing in \(S\) for \(\kappa>1\). Hence the restart rule selects the smaller of two independent copies of \(S\). If \(F_m(s)=\Pr\{S\le s\}\), then
\[
\mathbb P_D(\varepsilon)=F_m(\kappa^2\varepsilon),\qquad
\mathbb P_R(\varepsilon)=1-\bigl(1-F_m(\kappa\varepsilon)\bigr)^2.
\]

**Ratio distributions.** For \(m=1\), the ratio of two independent real Gaussians has a Cauchy distribution, so \(F_1(s)=2\arctan(s)/\pi\) for \(s\ge0\). For \(m=2\), conditional on \(Z\), the squared norm \(\|Y\|_2^2\) is chi-squared with two degrees of freedom, giving
\[
\Pr\{S>s\}=\mathbb E\left[e^{-s^2Z^2/2}\right]=\frac1{\sqrt{1+s^2}}.
\]
Substitution gives all four probability formulas above.

**Two-dimensional comparison and its sharp contrast frontier.** Set \(u=\arctan(\kappa\varepsilon)\in(0,\pi/2)\). The equality \(\mathbb P_D=\mathbb P_R\) is equivalent to
\[
\arctan(\kappa\tan u)=2u-2u^2/\pi.
\]
The right side lies strictly between \(u\) and \(\pi/2\), so monotonicity of the arctangent proves the pointwise sign criterion via \(H(u)\). In the interior, \(H(u)>1\). As \(u\downarrow0\),
\[
H(u)=2-\frac{2u}{\pi}+O(u^2),
\]
while, putting \(\delta=\pi/2-u\downarrow0\),
\[
H(u)\sim\frac{\pi}{2\delta}\longrightarrow\infty.
\]
Thus some interior values are strictly below \(2\), the positive continuous function attains its global minimum at an interior point, and \(1<\kappa_*<2\). These properties and the exact sign criterion imply all stated regimes by continuity, without assuming or needing uniqueness of the minimizer or of the reentrant crossing pair. In particular, if \(\kappa_*<\kappa<2\), then \(H(u)>\kappa\) near both endpoints and \(H(u)<\kappa\) on some interior interval.

**Three-dimensional single crossing.** For \(m=2\), subtract the two exact expressions. Since all denominators are positive, the inequality \(\mathbb P_D>\mathbb P_R\) is equivalent to
\[
\sqrt{1+\kappa^4\varepsilon^2}>1+\kappa^2\varepsilon^2.
\]
Squaring both positive sides and dividing by \(\kappa^2\varepsilon^2>0\) yields \(\kappa^2(1-\varepsilon^2)>2\). This is impossible for \(\kappa\le\sqrt2\) and defines precisely one positive boundary when \(\kappa>\sqrt2\), as claimed.

## Verification

The self-contained `verify.py` uses no nonstandard packages. Running `python verify.py` checks the exact two-dimensional equality transformation at 399 interior angles, the three-dimensional sign condition at 30 parameter pairs, the explicit reentrant three-tolerance example, and the analytic probability formulas against eight reproducible direct Gaussian experiments. Its expected terminal line is:

`VERIFY_OK: 399 exact-angle identities, 30 dimension-three sign checks, 8 seeded simulations`

The checker is a finite consistency test; the mathematical proof above establishes the statements for all allowed inputs. Numerical minimization of \(H\) supplies the displayed approximation to \(\kappa_*\), but the exact minimum definition and strict bounds are proved analytically and do not depend on floating-point optimization.

## Relationship to prior work

Tropp and Webber, *Randomized Algorithms for Low-Rank Matrix Approximation: Design, Analysis, and Applications* (first publicly available June 21, 2023), explicitly contrast Gaussian-probe breadth, power/subspace iteration depth, and computational resources. Their main theorems quantify rank-approximation errors and Krylov-type guarantees; the present result instead compares two specific equal-two-product, one-ray selection policies through full angular success distributions. Del Corso's earlier random-start power-method analysis already explains dependence on eigenvalue ratios and multiplicities. Kuczyński and Woźniakowski and Wang et al. analyze random-start power/Krylov-type eigenproblems, rather than the stated two-policy exact success frontier. Accordingly, neither the Cauchy starting-ratio law nor generic spectral filtering is claimed as original. The assessed contribution is the *exact comparative phase diagram*, especially the two-dimensional reentrant region and its disappearance for a trailing eigenspace of dimension two.

## Limitations

The result compares only the explicitly stated depth and normalized-gain restart policies with **two** products, and only the two indicated trailing multiplicities. It is not an oracle-complexity lower bound, a claim of optimality among all two-product procedures, or a convergence statement in large dimensions. In very small dimensions, algorithms combining all available Krylov information can outperform either deliberately restricted policy; knowing the full eigenspectrum permits still stronger spectral filtering. The overall scale of the matrix is immaterial, but Gaussianity, independence, a two-level positive spectrum, and the normalized-gain selection rule are essential to the displayed exact probabilities. Potential equivalent analyses under multistart order statistics remain an originality risk.

## References

1. J. A. Tropp and R. J. Webber, *Randomized Algorithms for Low-Rank Matrix Approximation: Design, Analysis, and Applications*, arXiv:2306.12418, first version June 21, 2023. https://arxiv.org/abs/2306.12418
2. G. M. Del Corso, *Estimating an Eigenvector by the Power Method with a Random Start*, SIAM Journal on Matrix Analysis and Applications 18(4), 913–937 (1997), DOI:10.1137/S0895479895296689. An openly accessible manuscript is https://arpi.unipi.it/retrieve/e0d6c928-17b1-fcf8-e053-d805fe0aa794/SML000913.pdf
3. J. Kuczyński and H. Woźniakowski, *Estimating the Largest Eigenvalue by the Power and Lanczos Algorithms with a Random Start*, SIAM Journal on Matrix Analysis and Applications 13(4), 1094–1122 (1992), DOI:10.1137/0613066.
4. S. Wang, Z. Zhang, and T. Zhang, *Improved Analyses of the Randomized Power Method and Block Lanczos Method*, arXiv:1508.06429 (2015). https://arxiv.org/abs/1508.06429
