# Universal half-log oracle regret for empirical and fixed-mass MDP bounded-mean betting
## Finding
{claim}

The result supplies a second-order rate for the empirical and mixture-DP-style predictive rules used in bounded-mean betting. The leading constant \(1/2\) is distribution-free within the stated interior regime even though the local curvature \(J\) depends on \(P\), \(\mu\), and \(c\).

## Assumptions and scope
The observations \(X_1,X_2,\ldots\) are i.i.d. from a nondegenerate probability law \(P\) supported on \([0,1]\). A candidate mean \(\mu\in(0,1)\) and truncation constant \(c\in(0,1)\) are fixed. Define
\[
I_{\mu,c}=\left[-\frac{c}{1-\mu},\frac{c}{\mu}\right],
\qquad
f_\lambda(x)=\log\{1+\lambda(x-\mu)\},
\qquad
M(\lambda)=P f_\lambda.
\]
The oracle maximizer \(\lambda^\star\) is assumed to lie in \(\operatorname{int}(I_{\mu,c})\). This is automatic at the null \(\mu=\mathbb E_P X\), where \(\lambda^\star=0\), and can fail for sufficiently distant false candidates because of coefficient truncation.

For \(n\ge1\), let \(P_n\) be the empirical law of \(X_1,\ldots,X_n\). The empirical rule maximizes \(P_n f_\lambda\). The fixed-mass MDP rule maximizes \(Q_{n+1\mid n} f_\lambda\), where
\[
Q_{n+1\mid n}=\frac{n}{n+\kappa}P_n+\frac{\kappa}{n+\kappa}H_{n+1\mid n},
\]
\(\kappa\ge0\) is fixed, and \(H_{n+1\mid n}\) is any predictable probability law supported on \([0,1]\). This includes the mixture-DP-style predictive in Kilian, Cortinovis, and Caron when \(H_{n+1\mid n}\) is their parametric posterior predictive.

## Proof
Set
\[
h_\lambda(x)=\frac{x-\mu}{1+\lambda(x-\mu)}.
\]
Because \(1+\lambda(x-\mu)\ge1-c\) throughout \(I_{\mu,c}\times[0,1]\), the score \(h_\lambda\) and its first two derivatives in \(\lambda\) are uniformly bounded. Differentiation under the integral gives
\[
M'(\lambda)=P h_\lambda,
\qquad
-M''(\lambda)=P h_\lambda^2.
\]
At the interior maximizer, \(P h_{\lambda^\star}=0\). Hence the score variance and the negative curvature coincide:
\[
\operatorname{Var}_P(h_{\lambda^\star})=P h_{\lambda^\star}^2
=J=-M''(\lambda^\star)>0.
\]
This identity is the source of the universal constant.

For the empirical optimizer, strict concavity and the interior assumption imply that, with probability tending to one exponentially fast, the optimizer is interior and satisfies the score equation \(P_n h_{\widehat\lambda_{n+1}}=0\). Indeed, choose a fixed neighborhood strictly inside \(I_{\mu,c}\); the population score has opposite strict signs at its two endpoints, while bounded Hoeffding deviations preserve both signs except on an exponentially small event. On the interior event, the mean-value theorem yields
\[
\widehat\lambda_{n+1}-\lambda^\star
=
\frac{P_n h_{\lambda^\star}}
     {P_n h_{\widetilde\lambda_n}^2}
\]
for an intermediate \(\widetilde\lambda_n\). Uniform boundedness and the law of large numbers give \(P_n h_{\widetilde\lambda_n}^2\to J\), while the central limit theorem gives \(\sqrt n P_n h_{\lambda^\star}\Rightarrow N(0,J)\). Thus
\[
\sqrt n(\widehat\lambda_{n+1}-\lambda^\star)
\Rightarrow N(0,J^{-1}).
\]
The same sign argument plus bounded-score concentration makes the exceptional boundary event exponentially small. On its complement the displayed representation bounds the estimation error by a constant times \(|P_n h_{\lambda^\star}|+n^{-1}\). Standard bounded-summand moment bounds then give uniform integrability at second order and \(n\,\mathbb E[(\widehat\lambda_{n+1}-\lambda^\star)^2]\to J^{-1}\), while \(n\,\mathbb E|\widehat\lambda_{n+1}-\lambda^\star|^3\to0\).

For the fixed-mass MDP rule, its score equation is
\[
0=nP_n h_{\widehat\lambda_{n+1}}+\kappa H_{n+1\mid n}h_{\widehat\lambda_{n+1}}.
\]
The second term is uniformly \(O(1)\) because \(H_{n+1\mid n}\) is a probability law on \([0,1]\) and the score is uniformly bounded. After division by \(n\), it perturbs the empirical score by only \(O(n^{-1})\), uniformly over all predictable choices of \(H_{n+1\mid n}\). Repeating the preceding local mean-value argument therefore gives the same central limit law and the same second- and third-moment limits.

Finally, a third-order Taylor expansion of \(M\) around its interior maximizer, whose third derivative is uniformly bounded on \(I_{\mu,c}\), gives
\[
M(\lambda^\star)-M(\widehat\lambda_{n+1})
=
\frac{J}{2}(\widehat\lambda_{n+1}-\lambda^\star)^2
+O(|\widehat\lambda_{n+1}-\lambda^\star|^3).
\]
Taking expectations and using the moment limits proves
\[
n\,\mathbb E[M(\lambda^\star)-M(\widehat\lambda_{n+1})]\longrightarrow\frac12.
\]
Because the next observation is independent of the past, its expected log-wealth increment is \(\mathbb E[M(\widehat\lambda_n)]\). Summing the one-step deficits and using the harmonic-series asymptotic yields
\[
N M(\lambda^\star)-\mathbb E[\log W_N]
=
\frac12\log N+o(\log N).
\]
At \(\mu=\mathbb E_P X\), the oracle is \(\lambda^\star=0\) and \(M(0)=0\), giving the stated null corollary.

## Verification
The proof is analytic. The accompanying deterministic script `verify_half_log.py` checks an exactly reducible Bernoulli case in which the population regret is a Bernoulli Kullback--Leibler divergence. For \(P=\operatorname{Bernoulli}(0.6)\), \(\mu=0.5\), and \(c=0.9\), it evaluates the finite-sample expectation by summing the full binomial law, with no simulation. It checks both the empirical rule and fixed prior masses \(\kappa=2\) and \(\kappa=10\); in each case \(n\) times the one-step expected regret approaches \(1/2\).

The script is a finite numerical cross-check only. The general theorem for arbitrary nondegenerate \(P\) and arbitrary predictable bounded-support \(H_{n+1\mid n}\) follows from the analytic concentration, score expansion, moment control, and Taylor argument above.

## Relationship to prior work
Kilian, Cortinovis, and Caron (arXiv:2605.07964v1) define the predictive-assisted coefficient, prove first-order oracle log-optimality under Wasserstein consistency, and for their MDP predictive prove expected Wasserstein error \(O(n^{-1/2})\). Combining their finite-sample Wasserstein comparison with that rate gives only an \(O(\sqrt N)\) cumulative oracle-gap bound. Their paper does not state a second-order \(\tfrac12\log N\) law.

Grünwald's discussion of Waudby-Smith and Ramdas explicitly conjectures that GRAPA should have regret similar to the parametric prequential plug-in benchmark, namely \(\tfrac12\log N+O(1)\), and calls for further theoretical analysis of GRAPA and regret. The present result proves the leading \(1/2\) coefficient in the bounded-mean growth objective under the interior-oracle condition and shows that the same coefficient survives every fixed-mass MDP prior perturbation.

Orabona and Jun obtain confidence sequences from universal-portfolio regret relative to the best fixed bet in hindsight; this is a different algorithm and comparator from the empirical/MDP predictive oracle gap here. Classical prequential maximum-likelihood results establish half-logarithmic redundancy in regular parametric likelihood models, but the inspected statements do not directly cover the distribution-free bounded-mean growth objective or an arbitrary predictable MDP component. Wang, Agrawal, and Ramdas prove almost-sure null bankruptcy for GRAPA and other betting strategies; the inspected abstract establishes bankruptcy rather than the expected \(-\tfrac12\log N\) log-wealth rate proved here.

## Limitations
The interior-oracle condition is essential to this statement. Boundary maximizers can have different local geometry and are not covered. The theorem assumes a fixed prior mass \(\kappa\); growing prior mass is not analyzed. It concerns expected oracle log-growth regret, not a pathwise regret expansion, a confidence-sequence width expansion, or an \(O(1)\) remainder. The originality comparison leaves a residual possibility that a sufficiently general sequential M-estimation theorem implies the empirical \(\kappa=0\) case under different terminology; no such direct implication was found in the inspected sources, and the arbitrary predictable fixed-mass MDP extension is not present in those inspected formulations.

## References
1. Valentin Kilian, Stefano Cortinovis, François Caron. *Asymptotically Log-Optimal Bayes-Assisted Confidence Sequences for Bounded Means*. arXiv:2605.07964v1, 2026.
2. Peter Grünwald. *Proposer of the vote of thanks to Waudy-Smith and Ramdas and contribution to the Discussion of ‘Estimating means of bounded random variables by betting’*. Journal of the Royal Statistical Society Series B 86(1), 28--30, 2024. DOI: 10.1093/jrsssb/qkad128.
3. Ian Waudby-Smith, Aaditya Ramdas. *Estimating means of bounded random variables by betting*. Journal of the Royal Statistical Society Series B 86(1), 1--27, 2024. DOI: 10.1093/jrsssb/qkad009.
4. Francesco Orabona, Kwang Sung Jun. *Tight Concentrations and Confidence Sequences From the Regret of Universal Portfolio*. IEEE Transactions on Information Theory 70(1), 436--455, 2024. DOI: 10.1109/TIT.2023.3330187.
5. Hongjian Wang, Shubhada Agrawal, Aaditya Ramdas. *Almost sure null bankruptcy of testing-by-betting strategies*. arXiv:2602.08888v1, 2026.
