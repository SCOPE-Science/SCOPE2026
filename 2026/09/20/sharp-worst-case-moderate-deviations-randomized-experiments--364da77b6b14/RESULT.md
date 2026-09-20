# Sharp worst-case moderate deviations for bounded-outcome randomized experiments

## Result

Consider a finite population of size \(n\) with potential outcomes
\[
Y_i(0),Y_i(1)\in[a,b],\qquad R=b-a>0.
\]
Under complete randomization, exactly \(n_1\) units are treated and \(n_0=n-n_1\) are controls. Write \(\pi_n=n_1/n\) and let
\[
\widehat\tau_n=\frac1{n_1}\sum_i Z_iY_i(1)-\frac1{n_0}\sum_i(1-Z_i)Y_i(0),
\qquad
\tau_n=\frac1n\sum_i\{Y_i(1)-Y_i(0)\}.
\]

There is a finite-sample concentration inequality with the correct uniform moderate-deviation exponent. Put
\[
m_n=\min(n_0,n_1),\qquad M_n=\max(n_0,n_1).
\]
Then, for every \(t>0\),
\[
\boxed{
\Pr\{|\widehat\tau_n-\tau_n|\ge t\}
\le
2\exp\!\left\{-\frac{2m_nM_n^2}{n(M_n+1)R^2}t^2\right\}.
}
\tag{1}
\]
Consequently,
\[
\boxed{
\widehat\tau_n\ \pm\
R\sqrt{\frac{n(M_n+1)}{2m_nM_n^2}\log\frac2\alpha}
}
\tag{2}
\]
is a finite-sample \((1-\alpha)\)-confidence interval for the SATE.

More importantly, (1) is asymptotically sharp uniformly over all bounded potential-outcome arrays. Suppose
\[
\pi_n\to\pi\in(0,1),\qquad t_n\downarrow0,
\qquad \frac{nt_n^2}{\log n}\to\infty.
\]
Let \(\mathcal Y_n=[a,b]^{2n}\). Then
\[
\boxed{
\lim_{n\to\infty}
\frac{R^2}{nt_n^2}
\log\sup_{Y(\cdot)\in\mathcal Y_n}
\Pr\{|\widehat\tau_n-\tau_n|\ge t_n\}
=-2\pi(1-\pi).
}
\tag{3}
\]
The same exponent holds for either one-sided tail. Thus the exact bounded-outcome effective sample size on the moderate-deviation scale is \(n\pi(1-\pi)\), with sharp quadratic exponent \(2\pi(1-\pi)/R^2\).

The lower bound in (3) already occurs on a sharp-null family: take approximately half the units with
\(Y_i(1)=Y_i(0)=a\) and the remainder with \(Y_i(1)=Y_i(0)=b\). Hence treatment-effect heterogeneity is not needed to attain the worst-case exponent.

## Sampling-without-replacement representation

Define the finite-population score
\[
A_i=(1-\pi_n)Y_i(1)+\pi_nY_i(0).
\tag{4}
\]
It remains in \([a,b]\). A direct identity gives
\[
\widehat\tau_n-\tau_n
=\frac{n}{n_0}(\bar A_T-\bar A)
=-\frac{n}{n_1}(\bar A_C-\bar A),
\tag{5}
\]
where \(\bar A_T\), \(\bar A_C\), and \(\bar A\) denote the treated, control, and population means of \(A_i\). Under complete randomization either treatment arm is a simple random sample without replacement. Choosing the smaller arm gives sample size \(m_n\), complement size \(M_n\), and multiplicative factor \(n/M_n\).

Serfling's finite-population Hoeffding inequality states that for a sample of size \(m\) from a population of size \(n\) with range \(R\),
\[
\Pr\{|\bar X_m-\mu|\ge s\}
\le 2\exp\left\{-\frac{2ms^2}{(1-(m-1)/n)R^2}\right\}.
\]
Substituting \(m=m_n\), \(1-(m_n-1)/n=(M_n+1)/n\), and
\(s=(M_n/n)t\) proves (1).

The representation (5) is closely related to the without-replacement representation used in the appendix of Freidling (2026). Therefore the representation itself, and the use of Serfling's inequality as a generic sampling theorem, are treated here as prior machinery rather than as new contributions.

## Sharpness proof for complete randomization

It remains to prove that no uniformly better quadratic exponent is possible over the bounded potential-outcome class.

For clarity first take \(n\) even and set
\[
Y_i(1)=Y_i(0)=
\begin{cases}
 b,&1\le i\le n/2,\\
 a,&n/2<i\le n.
\end{cases}
\tag{6}
\]
Then \(\tau_n=0\). If \(H_n\) is the number of \(b\)-units assigned to treatment, then
\[
H_n\sim\operatorname{Hypergeom}(n,n/2,n_1)
\]
and
\[
\widehat\tau_n
=\frac{R}{1-\pi_n}\left(\frac{H_n}{n_1}-\frac12\right).
\tag{7}
\]
Let
\[
\delta_n=\frac{(1-\pi_n)t_n}{R},
\qquad
h_n=n_1(1/2+\delta_n)+O(1)
\]
be an admissible integer. Its hypergeometric point probability is
\[
\Pr(H_n=h_n)
=
\frac{\binom{n/2}{h_n}\binom{n/2}{n_1-h_n}}
{\binom n{n_1}}.
\tag{8}
\]
Writing \(h(x)=-x\log x-(1-x)\log(1-x)\), Stirling's formula gives
\[
\log\Pr(H_n=h_n)
=
\frac n2 h(\pi_n+2\pi_n\delta_n)
+
\frac n2 h(\pi_n-2\pi_n\delta_n)
-
nh(\pi_n)
+O(\log n).
\tag{9}
\]
Since \(h''(x)=-1/[x(1-x)]\), symmetry cancels the cubic term and \(\delta_n\to0\) yields
\[
\log\Pr(H_n=h_n)
=
-\frac{2n\pi_n}{1-\pi_n}\delta_n^2\{1+o(1)\}
+O(\log n)
=
-\frac{2n\pi_n(1-\pi_n)}{R^2}t_n^2\{1+o(1)\}.
\tag{10}
\]
The assumption \(nt_n^2/\log n\to\infty\) makes the Stirling and integer-rounding terms negligible. Equation (8) is already a lower bound on the relevant one-sided tail, while (1) supplies the matching upper bound. Odd \(n\) is handled by replacing \(n/2\) with either nearest integer, which changes only lower-order terms. This proves (3).

## Stratified randomization

Now partition the population into a fixed number \(J\) of independent randomization strata. Stratum \(j\) has size \(N_j\), treated count \(n_{j1}\), control count \(n_{j0}\), and
\[
m_j=\min(n_{j0},n_{j1}),\qquad
M_j=\max(n_{j0},n_{j1}).
\]
Let \(n=\sum_jN_j\), and estimate the overall SATE by the usual weighted difference in means
\[
\widehat\tau=\sum_{j=1}^J\frac{N_j}{n}\widehat\tau_j.
\]
Applying the Serfling moment-generating-function bound to the minority arm in each stratum and multiplying the independent stratum mgfs gives
\[
\boxed{
\Pr\{|\widehat\tau-\tau|\ge t\}
\le
2\exp\left\{
-\frac{2n^2t^2}
{R^2\displaystyle\sum_{j=1}^J
\frac{N_j^3(M_j+1)}{m_jM_j^2}}
\right\}.
}
\tag{11}
\]
Hence a finite-sample confidence half-width is
\[
\boxed{
W_{\rm strat}
=R\sqrt{
\frac{\log(2/\alpha)}{2n^2}
\sum_{j=1}^J\frac{N_j^3(M_j+1)}{m_jM_j^2}}
.}
\tag{12}
\]

There is again a sharp uniform moderate-deviation law. Assume
\[
\frac{N_j}{n}\to w_j>0,
\qquad
\frac{n_{j1}}{N_j}\to p_j\in(0,1),
\qquad j=1,\ldots,J,
\]
and define
\[
\Gamma=\sum_{j=1}^J\frac{w_j}{p_j(1-p_j)}.
\tag{13}
\]
For the same conditions \(t_n\downarrow0\) and \(nt_n^2/\log n\to\infty\),
\[
\boxed{
\lim_{n\to\infty}
\frac{R^2}{nt_n^2}
\log\sup_{Y(\cdot)\in\mathcal Y_n}
\Pr\{|\widehat\tau-\tau|\ge t_n\}
=-\frac2\Gamma.
}
\tag{14}
\]

For the upper bound, the denominator in (11) satisfies
\[
\frac1n\sum_j
\frac{N_j^3(M_j+1)}{m_jM_j^2}
\longrightarrow
\sum_j\frac{w_j}{p_j(1-p_j)}=\Gamma.
\]
For the lower bound, use the binary sharp-null population (6) separately within every stratum. If the stratum error is forced to be \(e_j=o(1)\), its hypergeometric point probability has logarithmic cost
\[
\frac{2N_jp_j(1-p_j)}{R^2}e_j^2\{1+o(1)\}.
\tag{15}
\]
The least expensive way to create total error \(\sum_jw_je_j=t\) is the quadratic program
\[
\min\left\{
\sum_jw_jp_j(1-p_j)e_j^2:
\sum_jw_je_j=t
\right\}.
\]
Its optimizer is
\[
e_j^*=\frac{t}{\Gamma p_j(1-p_j)},
\]
and its minimum is \(t^2/\Gamma\). Taking admissible nearby hypergeometric counts in each stratum, and using independence across strata, yields the lower exponent \(2/(R^2\Gamma)\). The condition \(nt_n^2/\log n\to\infty\) again absorbs all polynomial Stirling factors and rounding errors.

Equation (14) gives a simple design consequence. If the overall treated fraction is fixed at
\[
\bar p=\sum_jw_jp_j,
\]
then strict convexity of \(p\mapsto1/[p(1-p)]\) gives
\[
\Gamma\ge\frac1{\bar p(1-\bar p)},
\tag{16}
\]
with equality exactly when all stratum treatment fractions are equal. Thus heterogeneous allocation fractions across strata worsen the sharp worst-case bounded-outcome moderate-deviation exponent, even though stratification can improve variance for particular outcome arrays.

## Comparison with recent finite-sample Hoeffding bounds

Freidling (2026), Proposition 4.1, gives for complete randomization a Hoeffding half-width
\[
W_F
=\frac R2\frac1{\pi_n(1-\pi_n)}
\sqrt{\frac{(1+\epsilon_n')\log(2/\alpha)}{2n}},
\qquad
\epsilon_n'=\frac{H_n-1}{n-H_n},
\]
where \(H_n=\sum_{k=1}^n1/k\). Comparing with (2) gives the exact ratio
\[
\frac{W_S^2}{W_F^2}
=
\frac{4m_n(M_n+1)}{(1+\epsilon_n')n^2}
\le1.
\tag{17}
\]
One way to see the last inequality is that \(\epsilon_n'\ge2/n\) for \(n\ge2\), while
\(4m_nM_n/n^2\le1\) and \(M_n\ge n/2\). Asymptotically,
\[
\frac{W_S}{W_F}\to2\sqrt{\pi(1-\pi)}.
\tag{18}
\]
Thus the two bounds agree at balanced allocation to first order, whereas the finite-population correction gives a strict asymptotic constant improvement away from balance.

The same termwise comparison applies to Freidling's stratified Hoeffding formula: replacing its exchangeable-weight term by the minority-arm Serfling term yields (12), and each stratum's squared contribution is no larger.

Sandoval, Balakrishnan, Feller, Jordan and Waudby-Smith (2026) established nonasymptotic intervals with the optimal \(1/\sqrt{n\pi}\) order and design-based minimax lower bounds for squared-error risk up to constants. Sudijono, Dobriban and Tchetgen Tchetgen (2026) subsequently obtained sharp minimax mean-squared-risk results for binary potential outcomes when design and estimator can vary. Equations (3) and (14) concern a different object: the exact logarithmic worst-case tail exponent for the standard difference-in-means estimator under fixed complete or stratified randomization.

## Verification

The accompanying verification script performs three checks using only elementary log-gamma calculations:

1. it enumerates all complete-randomization allocations for \(2\le n\le500\) and confirms that the squared half-width ratio in (17) never exceeds one;
2. for the binary sharp-null construction with \(\pi=0.3\), exact hypergeometric point probabilities converge after normalization to the predicted constant \(2\pi(1-\pi)=0.42\);
3. for a two-stratum example with \((w_1,w_2)=(0.4,0.6)\) and \((p_1,p_2)=(0.25,0.60)\), the normalized product of exact hypergeometric point probabilities converges to \(2/\Gamma=0.431654676259\).

These computations illustrate the asymptotic constants; the proofs above do not depend on numerical evidence.

## Prior literature and originality boundary

The following components are prior art and are not claimed as new:

- Serfling's finite-population Hoeffding inequality and subsequent refinements for sampling without replacement, including Bardenet and Maillard;
- finite-population Cramér/moderate-deviation theory, including Hu, Robinson and Wang;
- the completely randomized SATE representation as a without-replacement sample of a potential-outcome combination, which appears in recent randomization-inference work and is closely related to standard survey-sampling algebra;
- recent nonasymptotic SATE confidence intervals and minimax rate results of Sandoval et al.;
- recent sharp mean-squared minimax theory for randomized experiments of Sudijono, Dobriban and Tchetgen Tchetgen;
- recent concentration-based complete and stratified randomization intervals of Freidling.

To the best of our knowledge, the literature search did not locate the treatment-effect statements (3) and (14): an exact worst-case bounded-outcome moderate-deviation exponent for the standard SATE estimator, attained by a sharp-null endpoint population, together with the stratified harmonic allocation constant \(\Gamma\). The finite Serfling intervals (2) and (12) are short consequences of known sampling-without-replacement theory; their role here is to provide matching nonasymptotic upper bounds, not to support a claim that Serfling's method itself is new.

The principal residual originality risk is the older survey-sampling and permutation-test literature: a theorem equivalent to (3) or (14) may exist in finite-population language without causal-inference terminology. Hu, Robinson and Wang give powerful general finite-population tail approximations, but the sources inspected did not formulate the worst-case bounded potential-outcome optimization or the stratified constant (13). This record therefore limits its originality claim to the randomized-experiment worst-case matching theorem and its stratified allocation law.

## Limitations

The sharp asymptotics assume a fixed positive allocation fraction in every relevant stratum, a fixed number of strata, bounded outcomes, and a moderate-deviation sequence satisfying \(t_n\downarrow0\) and \(nt_n^2/\log n\to\infty\). No uniform crossover result is proved when treatment fractions approach zero, when the number of strata diverges, or for studentized/variance-adaptive estimators. The result fixes the usual difference-in-means estimator and assignment design; it is not a claim of minimax optimality over all estimators or all experimental designs. No independent audit has been performed.

## References

- R. J. Serfling (1974), *Probability Inequalities for the Sum in Sampling without Replacement*, Annals of Statistics 2(1), 39–48. DOI: 10.1214/aos/1176342611.
- R. Bardenet and O.-A. Maillard (2015), *Concentration inequalities for sampling without replacement*, Bernoulli 21(3), 1361–1385. arXiv:1309.4029; DOI: 10.3150/14-BEJ605.
- Z. Hu, J. Robinson and Q. Wang (2007), *Cramér-type large deviations for samples from a finite population*, Annals of Statistics 35(2), 673–696. arXiv:0708.1880.
- Z. Hu, J. Robinson and Q. Wang (2012), *Tail approximations for samples from a finite population with applications to permutation tests*, ESAIM: Probability and Statistics 16, 425–435. DOI: 10.1051/ps/2010027.
- R. J. Sandoval, S. Balakrishnan, A. Feller, M. I. Jordan and I. Waudby-Smith (2026), *On Nonasymptotic Confidence Intervals for Treatment Effects in Randomized Experiments*, arXiv:2601.11744.
- T. Sudijono, E. Dobriban and E. Tchetgen Tchetgen (2026), *Sharp Minimax Theory for Randomized Experiments*, arXiv:2608.13822.
- T. Freidling (2026), *Randomization Inference with Concentration Inequalities*, arXiv:2609.18586.
