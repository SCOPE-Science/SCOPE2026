# Exact paired busy-period detection law and sharp covert constant

## Finding
Fix a service rate \(\mu>0\), an arrival rate \(0<\lambda<\mu\), an alternative \(\lambda_1=\lambda+\eta<\mu\) with \(\eta>0\), and an integer \(k\ge1\). Independently observe \(k\) complete, unlabeled busy periods of a stable \(M/M/1\) queue, each initialized with exactly one customer. Let \(N_i\ge1\) denote the total number of completed services and \(T_i>0\) the duration of busy period \(i\); put \(S=\sum_{i=1}^k(N_i-1)\), \(U=\sum_{i=1}^kT_i\).

**The paired record \((N_i,T_i)_{i=1}^k\) is statistically equivalent, for inference on the arrival rate with known \(\mu\), to all event types and times within those busy periods.** For the two simple arrival-rate hypotheses, the likelihood ratio of either record is exactly
\[
L=\frac{dP_{\lambda_1}}{dP_{\lambda}}=
\left(\frac{\lambda_1}{\lambda}\right)^S e^{-\eta U}.
\]
Set \(q=\log(\lambda_1/\lambda)/\eta\). With equal testing costs, the Neyman--Pearson decision rule chooses the higher arrival rate precisely when \(U<qS\). The infimum of the sum of type-I and type-II errors equals \(\alpha_k+\beta_k\), where
\[
\begin{aligned}
\alpha_k&=\sum_{s=1}^{\infty}w_{\lambda,k}(s)G_{2s+k}((\mu+\lambda)qs),\\
\beta_k&=\sum_{s=0}^{\infty}w_{\lambda_1,k}(s)
 [1-G_{2s+k}((\mu+\lambda_1)qs)],\\
w_{\theta,k}(s)&=\frac{k}{2s+k}\binom{2s+k}{s}
 \frac{\mu^{s+k}\theta^s}{(\mu+\theta)^{2s+k}},\qquad s\ge0,
\end{aligned}
\]
and \(G_a(t)\) is the unit-rate Gamma CDF with shape \(a\), with \(G_a(0)=0\). Each sum converges absolutely. For every \(\eta>0\) and every \(k\ge1\), the paired experiment has **strictly greater total-variation detection power** than observing all counts alone or all durations alone.

The one-period relative entropy, in the direction of the baseline versus the alternative, is exactly
\[
D_{\rm pair}(\lambda\Vert\lambda+\eta)
 =\frac{\eta-\lambda\log(1+\eta/\lambda)}{\mu-\lambda}.
\]
Writing \(D_{\rm count}\) for the count-only divergence gives the **strict exact information gap**
\[
D_{\rm pair}-D_{\rm count}
=\frac{\mu+\lambda}{\mu-\lambda}
\left[\frac{\eta}{\mu+\lambda}-\log\left(1+\frac{\eta}{\mu+\lambda}\right)\right]>0.
\]
The paired Fisher information per busy period is \(I_{\rm pair}=1/[\lambda(\mu-\lambda)]\); the count-only information is \(I_{\rm count}=\mu/[\lambda(\mu^2-\lambda^2)]\). Under a fixed \(\delta>0\) constraint \(\limsup_{k\to\infty}kD_{\rm pair}(\lambda\Vert\lambda+\eta_k)\le\delta\), the sharp asymptotic supremum of the expected number of additional jobs, normalized by \(\sqrt{k\delta}\), is
\[
K_{\rm pair}=\mu\sqrt{\frac{2}{\lambda(\mu-\lambda)}}
=K_{\rm count}\sqrt{\frac{\mu}{\mu+\lambda}}<K_{\rm count}.
\]
Under a local alternative \(\eta_k=h/\sqrt{k}\) for any fixed \(h>0\), the optimal total testing error converges to
\[
2\Phi\left(-\frac{h}{2\sqrt{\lambda(\mu-\lambda)}}\right).
\]
These claims form one detection theorem: full-path sufficiency, its exact finite testing law, and its sharp weak-insertion limit.

## Assumptions and scope
Each busy period starts at queue state one immediately after the initiating arrival and ends at its first return to zero. During a positive queue size, arrivals form a Poisson process with constant rate \(\theta\in(0,\mu)\), and completions occur at exponential rate \(\mu\), independent of arrivals. Each new busy period is sampled from a fresh regeneration cycle. The within-busy *full path* comprises unlabelled jump directions and their occurrence times. It excludes preceding idle intervals, source identities/marks of arrivals, and service information unavailable from the queue-size path. The server is work conserving, with known fixed \(\mu\). All formulas are for finite \(k\ge1\), \(0<\lambda<\lambda_1<\mu\), and the indicated asymptotic sequences.

## Proof
**1. The bivariate busy-period law.** On a path with \(N=j\), there are exactly \(j-1\) upward jumps and \(j\) downward jumps before the first return from one to zero. There are \(C_{j-1}=\binom{2j-2}{j-1}/j\) admissible direction sequences (the Catalan paths). Until absorption, all holding times are independent \(\operatorname{Exp}(\theta+\mu)\), independent of jump directions. Multiplying the path weights and integrating the jump-time simplex yields the mixed mass-density
\[
f_{\theta}(j,t)=\frac{\theta^{j-1}\mu^j}{j!(j-1)!}
 t^{2j-2}e^{-(\theta+\mu)t},\qquad j\ge1,\ t>0.
\]
In particular, \(T\mid N=j\sim\operatorname{Gamma}(2j-1,\theta+\mu)\) in shape--rate notation. For \(j=1\), this is \(\operatorname{Exp}(\theta+\mu)\): the duration conditioned on a single completion **depends on the arrival rate**. The classical joint-transform calculation gives the same density and is not being claimed as new.

**2. Full-path equivalence and finite sufficiency.** For a fixed \(j,t\), every admissible direction sequence has equal conditional probability \(1/C_{j-1}\), independently of \(\theta\). Conditional on this sequence and \(T=t\), the \(2j-1\) successive holding-time proportions have a uniform Dirichlet distribution on the simplex, also independently of \(\theta\). Hence a \(\theta\)-independent randomization reconstructs the full within-busy path from the pair \((N,T)\). Conversely, the pair is a measurable function of that path. The two experiments are exactly Blackwell equivalent. Cancellation of the \(\theta\)-free factors in \(f_\theta\) gives the stated likelihood ratio, proving that \((S,U)\) is sufficient for all \(k\) pairs and all within-busy full paths.

**3. Count--duration joint distribution for \(k\) periods.** The convolution of \(k\) Catalan count series, equivalently the generalized ballot count for a walk from height \(k\) to zero with \(s\) upward steps, is \(k\binom{2s+k}{s}/(2s+k)\). This gives \(\Pr_\theta(S=s)=w_{\theta,k}(s)\) as displayed. Given every individual count, the independent durations are Gamma with a common rate \(\mu+\theta\), whose shapes sum to \(2S+k\). Thus \(U\mid S=s\sim\operatorname{Gamma}(2s+k,\mu+\theta)\). The likelihood threshold \(\log L=S\log(\lambda_1/\lambda)-\eta U>0\) gives the \(\alpha_k,\beta_k\) series. Since \(\theta<\mu\), \(4\theta\mu/(\mu+\theta)^2<1\), guaranteeing geometric-tail convergence of these sums.

**4. Strict power over both marginal records.** The paired likelihood is not almost surely of one sign around one conditional on the count record: on the positive-probability event \(S=1\), \(U\) has a Gamma density with full positive support and \(L-1\) changes sign at \(U=q\). Conditional on any duration vector with positive entries, every nonnegative count-excess vector has positive conditional probability. Taking all count excesses zero yields \(L<1\), while sufficiently many gives \(L>1\). Thus conditional Jensen for \(|L-1|\) is strict under *either* marginal observation, and total variation for the pair is strictly larger. Full-path total variation equals paired total variation by the common conditional reconstruction kernel.

**5. Exact entropy and sharp information gap.** Differentiating the classical busy-period branching equation, or using first-step equations, gives \(\mathbb E_\lambda(N-1)=\lambda/(\mu-\lambda)\) and \(\mathbb E_\lambda T=1/(\mu-\lambda)\). The expectation of \(-\log L\) gives \(D_{\rm pair}\). By the count likelihood from \(w_{\theta,1}\),
\[
D_{\rm count}=\frac{(\mu+\lambda)\log\left(1+\frac\eta{\mu+\lambda}\right)-\lambda\log\left(1+\frac\eta\lambda\right)}{\mu-\lambda}.
\]
The difference is the conditional Gamma relative entropy, averaged over counts, and is strictly positive because \(z-\log(1+z)>0\) for \(z>0\). The conditional count distribution given \(T=t\) depends strictly on \(\theta\) for all \(t>0\), so the duration-only KL divergence is also strictly smaller. The negative expectation of the second derivative of \(\log f_{\theta}\) gives \(I_{\rm pair}=\mathbb E_\theta(N-1)/\theta^2\); differentiating \(D_{\rm count}\) twice gives \(I_{\rm count}\).

**6. Local detection and the covert constant.** A Taylor expansion of \(S\log(1+\eta/\lambda)-\eta U\), combined with the i.i.d. central limit theorem for the finite-variance score \((N-1)/\lambda-T\), yields under the baseline the normal log-likelihood limit of mean \(-h^2I_{\rm pair}/2\) and variance \(h^2I_{\rm pair}\) for \(\eta=h/\sqrt{k}\). Under the alternative, the corresponding mean is positive with the same limiting variance (by triangular-array moments, or the standard likelihood third lemma). The sign test therefore has limiting total error \(2\Phi(-h\sqrt{I_{\rm pair}}/2)\). The exact relative entropy has the expansion \(D_{\rm pair}=\eta^2/[2\lambda(\mu-\lambda)]+O(\eta^3)\). Under the alternative, the expected number of additional Poisson-source customers served across \(k\) busy periods is exactly
\[
E_b(k,\eta)=\frac{k\mu\eta}{(\lambda+\eta)(\mu-\lambda-\eta)}.
\]
The divergence is strictly increasing in \(\eta>0\), so an asymptotic \(\delta\)-KL constraint forces \(\limsup\sqrt{k}\eta_k\le\sqrt{2\delta\lambda(\mu-\lambda)}\). Choosing rates approaching this bound attains the stated \(K_{\rm pair}\). The count-only constant is obtained from its separate second-order entropy coefficient, giving the exact ratio displayed.

## Verification
The standalone `verification.py` (Python 3 with SciPy) reconstructs Catalan path counts independently, tests generalized ballot coefficients by integer convolution, checks count normalizations and moments, verifies finite relative-entropy decomposition and Fisher information by separate moment sums, and checks the exact Neyman--Pearson series against direct numerical integration of the minimum of two joint densities. Executing `python verification.py` produced the included `verification_output.txt`, with 125 passing assertions. An illustrative instance \((\lambda,\lambda_1,\mu,k)=(1,1.25,3,2)\) has optimal type-I error \(0.28658175846030864\), type-II error \(0.6328878067411836\), and total \(0.9194695652014923\). The calculations corroborate finite identities; the infinite sums, strict inequalities and limit statements are proved analytically above, not by finite enumeration.

## Relationship to prior work
Sahithi, Yardi and Ravi (2026) analyze covert detection from busy-period job counts **or** durations separately and compute the respective square-root constants, but not the joint paired experiment or its optimal finite-sample error law. The underlying busy-period count law is classical; Takács (1961) and Prabhu's earlier queueing analysis treat joint count--length distributions. Chaudhry and Goswami (2019) provide broad service-count formulas. **General full-trajectory likelihood sufficiency is older work**: Asanjarani, Nazarathy and Taylor (2020/2021), surveying Clarke's 1957 stopping scheme, explicitly explain how an observed \(M/M/1\) trajectory has likelihood depending only on arrival/departure counts and exposure time. Thus the bare sufficiency assertion is not claimed as a discovery. The claimed new addition in the 2026 *paired-monitoring* formulation is the explicit Gamma--ballot optimal finite testing error, strict simultaneous-report power relative to each marginal, the exact relative-entropy/information gap, and the corresponding sharp covert constant. The conditional Gamma law shows that the paired experiment cannot be reconstructed from counts alone. Standard likelihood-ratio testing and exponential-family theory are used rather than claimed as new.

## Limitations
These statements exclude idle-period waiting times, origin labels, unobserved queue dynamics outside the busy interval, unknown service rate, non-Poisson insertion, and general service-time distributions. The closed testing error is an absolutely convergent infinite series, not a finite elementary formula; its numerical truncation requires a tail assessment, particularly near heavy traffic. The local alternative conclusion assumes fixed strictly subcritical baseline parameters. Although the primary recent and 2019 open-access manuscripts were read, original historical joint-law and earlier covert-queueing manuscripts could not all be inspected in full; equivalent specialized inference results remain a priority risk. No claim of independent proof validation is made.

## References
1. A. V. S. S. Sahithi, A. Yardi, J. Ravi, *Fundamental Limits of Covert queueing under Busy-Period Observations*, arXiv:2610.13911v1 (first submitted 2026-10-09), https://arxiv.org/abs/2610.13911.
2. L. Takács, *The Probability Law of the Busy Period for Two Types of Queuing Processes*, Operations Research 9 (1961), 402--407, https://doi.org/10.1287/opre.9.3.402.
3. M. L. Chaudhry, V. Goswami, *Analytically Explicit Results for the Distribution of the Number of Customers Served during a Busy Period for Special Cases of the M/G/1 Queue*, Journal of Probability and Statistics (2019), article 7398658, https://doi.org/10.1155/2019/7398658.
4. A. Yardi, T. Bodas, *A Covert Queueing Problem With Busy Period Statistic*, IEEE Communications Letters 25 (2021), 726--729, https://doi.org/10.1109/LCOMM.2020.3038191.
5. A. Asanjarani, Y. Nazarathy, P. Taylor, *A Survey of Parameter and State Estimation in Queues*, arXiv:2012.14614v1 (2020; Queueing Systems 97, 2021, 39--80), https://arxiv.org/abs/2012.14614.
