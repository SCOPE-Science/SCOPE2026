# Exact binomial phase diagram for zero observed relative utility under perfect risk probabilities
## Finding
Fix a treatment threshold \(t\in(0,1)\). Let \(Y_1,\ldots,Y_n\) be independent Bernoulli\((q)\) outcomes, with \(q\in(0,1)\), and suppose the prediction supplied for every individual is the true constant risk, \(p_i=q\). Treatment is assigned when \(p_i\ge t\). Write \(S_n=\sum_{i=1}^nY_i\), and let
\[
A_n=\{1\le S_n\le n-1\},
\]
which is exactly the event on which observed relative utility is defined under the net-benefit normalization used in Hoessly (2026).

Define
\[
z_n(q,t)=\Pr\{\mathrm{RU}(t)=0\mid A_n\}.
\]
Then \(z_n(q,t)\) is given exactly by a binomial tail. If \(q\ge t\),
\[
z_n(q,t)=
\frac{\displaystyle\sum_{s=\max(1,\lceil nt\rceil)}^{n-1}\binom ns q^s(1-q)^{n-s}}
{1-q^n-(1-q)^n}.
\]
If \(q<t\),
\[
z_n(q,t)=
\frac{\displaystyle\sum_{s=1}^{\min(n-1,\lfloor nt\rfloor)}\binom ns q^s(1-q)^{n-s}}
{1-q^n-(1-q)^n}.
\]
The numerators are also the corresponding unconditional probabilities that relative utility is both defined and equal to zero.

For every fixed \(q\ne t\), the exceptional conditional probability has the sharp logarithmic rate
\[
-\frac1n\log(1-z_n(q,t))\longrightarrow D(t\|q),
\]
where
\[
D(t\|q)=t\log\frac tq+(1-t)\log\frac{1-t}{1-q}.
\]
At the critical point \(q=t\),
\[
z_n(t,t)\longrightarrow \frac12.
\]
More generally, if \(q_n=t+c/\sqrt n\) for a fixed real \(c\) and \(q_n\in(0,1)\), then
\[
z_n(q_n,t)\longrightarrow
\Phi\!\left(\frac{|c|}{\sqrt{t(1-t)}}\right),
\]
where \(\Phi\) is the standard normal distribution function.

Thus the probability-one degeneration identified by Hoessly away from the threshold has a sharp finite-sample formula and an exponential rate, while the threshold itself is a genuine root-\(n\) transition layer.

## Assumptions and scope
The result concerns the observed, sample-normalized relative utility in Hoessly's threshold-specific net-benefit representation. Outcomes are independent with common event probability \(q\); predictions are perfect in the probabilistic sense \(p_i=q\); and the classification convention is treatment when \(p_i\ge t\). The conditioning event \(A_n\) is not an extra statistical assumption: observed relative utility is undefined at the all-zero and all-one samples because its denominator vanishes there.

The result does not address heterogeneous risks, estimated probabilities, dependence among outcomes, uncertainty in the threshold, or population-level expected utility. Its purpose is to resolve exactly the constant-risk example used to expose the distinction between perfect probabilities and perfect outcome information.

## Proof
For a realized event rate \(\bar Y=S_n/n\), Hoessly's observed relative utility uses the better default net benefit
\[
\max\left\{0,\frac{\bar Y-t}{1-t}\right\},
\]
and is defined exactly when \(0<\bar Y<1\).

Suppose first that \(q\ge t\). Perfect constant-risk prediction treats everyone, so the model net benefit is the treat-all value
\[
\frac{\bar Y-t}{1-t}.
\]
On \(A_n\), the observed relative utility is zero exactly when treat-all is itself the better default, equivalently when \(\bar Y\ge t\). Since \(S_n\) is integer, this is \(S_n\ge\lceil nt\rceil\). Intersecting with \(1\le S_n\le n-1\) gives the first exact sum.

If \(q<t\), perfect constant-risk prediction treats nobody, so the model net benefit is zero. On \(A_n\), observed relative utility is zero exactly when treat-none is the better default, equivalently when \(\bar Y\le t\). This is \(S_n\le\lfloor nt\rfloor\), giving the second exact sum. In either branch,
\[
\Pr(A_n)=1-q^n-(1-q)^n.
\]

For fixed \(q>t\), the event contributing to \(1-z_n(q,t)\) is the lower binomial tail immediately below \(nt\), apart from the excluded endpoint \(S_n=0\). A Chernoff upper bound gives exponential rate at least \(D(t\|q)\), while a single lattice mass at an integer \(s_n\) with \(s_n/n\to t\), together with Stirling's formula, gives the matching lower exponential rate. Excluding \(S_n=0\) does not alter the rate because the rate function is strictly larger at zero than at \(t\). The argument for fixed \(q<t\) is symmetric, using the upper tail immediately above \(nt\); excluding \(S_n=n\) again does not change the rate. Since \(\Pr(A_n)\to1\), conditioning on \(A_n\) does not change the logarithmic limit.

When \(q=t\), the convention \(p_i\ge t\) puts the rule in the treat-all branch, and \(z_n(t,t)\) is the conditional probability that \(S_n\ge\lceil nt\rceil\). The threshold differs from the mean \(nt\) by less than one. The binomial central limit theorem and \(\Pr(A_n)\to1\) therefore give the limit \(1/2\).

Finally let \(q_n=t+c/\sqrt n\). Since \(q_n\to t\),
\[
\frac{nt-nq_n}{\sqrt{nq_n(1-q_n)}}
\longrightarrow
-\frac c{\sqrt{t(1-t)}}.
\]
For \(c\ge0\), the perfect predictor treats all and the zero-relative-utility event is the upper side \(S_n/n\ge t\); for \(c<0\), it treats none and the event is the lower side \(S_n/n\le t\). The triangular-array binomial central limit theorem gives the common limit \(\Phi(|c|/\sqrt{t(1-t)})\). Endpoint conditioning is asymptotically negligible because \(q_n\) stays bounded away from zero and one.

## Verification
The standalone script `verify.py` reconstructs observed relative utility from its net-benefit definition for every attainable count \(S_n\) in several rational test cases, and checks that the resulting exact rational probability agrees with the two closed-form binomial sums. The cases cover \(q>t\), \(q<t\), and \(q=t\). It also reports deterministic finite-\(n\) numerical checks of the predicted large-deviation and root-\(n\) limits. Running the finalized script returns `VERIFY_OK`.

The asymptotic statements are proofs from binomial large-deviation and central-limit estimates, not extrapolations from the numerical checks.

## Relationship to prior work
Hoessly (2026) proves the motivating phenomenon for the branch \(t<q<1\): under perfect constant-risk predictions, the probability that observed relative utility is defined and equals zero tends to one by the law of large numbers. The present result retains that phenomenon but determines its exact finite-sample probability, adds the symmetric \(q<t\) branch, identifies the binary-divergence exponent away from the threshold, and resolves the critical and local root-\(n\) threshold regimes.

The earlier relative-utility literature of Baker and coauthors develops the decision-analytic normalization and interprets its endpoints. The inspected formulations do not supply the constant-risk binomial phase diagram above. The new result is not a new definition of relative utility; it is a finite-sample and local-asymptotic characterization of the pathology highlighted in the 2026 paper.

## Limitations
The finding is deliberately narrow. It uses independent identically distributed Bernoulli outcomes and a common known risk. It does not imply that the same binomial formulas hold under heterogeneous conditional risks or dependent outcomes. It also does not claim that observed relative utility is unsuitable as a decision metric; it quantifies one specific interpretation issue when perfect probability forecasts induce a default action for everyone.

The originality search found no statement of the exact two-sided formula, the \(D(t\|q)\) exception rate, or the root-\(n\) profile in the inspected relative-utility sources or indexed mathematical findings. An equivalent observation under different terminology remains a residual literature risk.

## References
1. L. Hoessly, “Interpreting relative utility for probabilistic predictions,” arXiv:2609.29133v1, 24 September 2026.
2. S. G. Baker, N. R. Cook, A. Vickers, and B. S. Kramer, “Using Relative Utility Curves to Evaluate Risk Prediction,” Journal of the Royal Statistical Society Series A, 172(4):729–748, 2009, DOI: 10.1111/j.1467-985X.2009.00592.x.
3. S. G. Baker, “Decision Curves and Relative Utility Curves,” Medical Decision Making, 39(5), 2019, DOI: 10.1177/0272989X19850762.
