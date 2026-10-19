# A sharp finite-size consensus gap between two mean-field-identical nonlinear voter rules

## Finding
Consider the binary nonlinear voter process on a complete network of \(N\ge3\) people. The two unanimity-panel sizes \(q=2\) and \(q=3\) have **the same infinite-population drift equation**, but their exact finite-population consensus probabilities differ. The difference is uniformly nonvanishing in the critical majority window as \(N\to\infty\).

Let \(\rho_q^{(N)}(k)\) be the probability that opinion A ultimately occupies all \(N\) people when initially exactly \(k\) people hold A. Put \(m=N-1\). For every integer \(0\le k\le N\), with empty sums equal to zero,
\[
\rho_2^{(N)}(k)=\frac{1}{2^m}\sum_{j=0}^{k-1}\binom mj,
\qquad
\rho_3^{(N)}(k)=\frac{1}{\binom{2m}{m}}\sum_{j=0}^{k-1}\binom mj^2.
\]
Thus the two consensus probabilities are respectively a symmetric binomial cumulative distribution and a symmetric hypergeometric cumulative distribution (with population size \(2m\), \(m\) marked units and sample size \(m\)).

Write \(\Delta_N(k)=\rho_3^{(N)}(k)-\rho_2^{(N)}(k)\). For every \(N\ge3\),
\[
\Delta_N(k)<0\quad(0<k<N/2),\qquad
\Delta_N(k)>0\quad(N/2<k<N).
\]
At an integer midpoint \(k=N/2\) the difference is exactly zero, as it is at the two absorbing endpoints. Accordingly, the larger panel **strictly amplifies whichever opinion initially has a strict majority**.

For every integer \(N\ge3\), the positive maximum \(D_N=\max_k\Delta_N(k)\) occurs at one or two adjacent integers in the upper-majority region. Its exact maximizing-index test is
\[
\binom m{k-1}\ge \frac{\binom{2m}{m}}{2^m}\ge\binom m{k}.
\]
If \(k_N\) is any maximizing index, then
\[
\frac{k_N-N/2}{\sqrt N}\longrightarrow\frac{\sqrt{\log2}}2,
\qquad
D_N\longrightarrow\Phi(\sqrt{2\log2})-\Phi(\sqrt{\log2})
=0.08303203749175645\ldots,
\]
where \(\Phi\) is the standard normal distribution function. In fact, for every fixed real \(s\), whenever \(k_N=N/2+s\sqrt N+o(\sqrt N)\) is an integer sequence,
\[
\rho_2^{(N)}(k_N)\longrightarrow\Phi(2s),\qquad
\rho_3^{(N)}(k_N)\longrightarrow\Phi(2\sqrt2\,s).
\]
Hence two rules with the same deterministic population limit can disagree by asymptotically **8.3032 percentage points** in their consensus predictions, even though at every fixed initial density other than one half both probabilities approach the same zero-or-one limit.

## Assumptions and scope
The population is well mixed; the contact graph is complete and has no self-neighbor. Every person has an independent rate-one exponential update clock. At an update, the focal person draws \(q\in\{2,3\}\) neighbors independently and uniformly **with replacement** from the other \(N-1\) people. The focal opinion changes only if all sampled neighbors hold the opposite opinion. There is no spontaneous flipping, mutation, external field, or influence from the focal person's own opinion beyond requiring that a unanimous opposite panel be seen. Both all-A and all-B configurations are absorbing. Population size and panel size are held fixed while the absorbing probability is computed. The large-population limit is taken subsequently.

An integer count \(k\) determines the full Markov state on the complete graph. When \(1\le k\le N-1\), the upward and downward continuous-time rates are exactly
\[
a_k^{(q)}=(N-k)\left(\frac{k}{N-1}\right)^q,
\qquad
b_k^{(q)}=k\left(\frac{N-k}{N-1}\right)^q.
\]
These rates are positive in the interior, so absorption in either endpoint occurs almost surely in finite time. The standard large-population density equation for either \(q=2\) or \(q=3\) is
\[
\dot x=(1-x)x^q-x(1-x)^q=x(1-x)(2x-1).
\]
These assertions do not compare transient trajectories at finite \(N\) or claim their absorption times are equal.

## Proof
**Step 1: exact harmonic increments.** Denote by \(u_k\) the probability of eventual all-A absorption. Its birth-death harmonicity equations, with \(u_0=0\) and \(u_N=1\), are
\[
a_k^{(q)}(u_{k+1}-u_k)=b_k^{(q)}(u_k-u_{k-1})\quad(1\le k\le N-1).
\]
For \(d_j=u_{j+1}-u_j\), the exact rate ratio is
\[
\frac{d_j}{d_{j-1}}=\left(\frac{N-j}{j}\right)^{q-1},
\qquad d_j=d_0\binom{N-1}{j}^{q-1}.
\]
The normalization \(\sum_{j=0}^{N-1}d_j=1\) gives the stated two formulas. The identities \(\sum_j\binom mj=2^m\) and \(\sum_j\binom mj^2=\binom{2m}m\) normalize them, with the second being Vandermonde's convolution. The displayed hypergeometric and binomial interpretations follow immediately.

**Step 2: strict majority comparison.** Define probability masses \(p_j=2^{-m}\binom mj\) and \(h_j=\binom mj^2/\binom{2m}m\) for \(0\le j\le m\). Both are strictly positive, symmetric about \(m/2\), and sum to one. Their ratio
\[
\frac{h_j}{p_j}=\frac{2^m\binom mj}{\binom{2m}m}
\]
is strictly increasing to the center and then strictly decreasing. As \(m\ge2\), the two masses are not identical, so the ratio is below one in both tails and above one centrally, with at most one sign change on each side. Partial summation on the left half, together with reflection \(j\mapsto m-j\), shows \(\sum_{j<k}(h_j-p_j)<0\) for \(0<k<N/2\) and strictly positive for \(N/2<k<N\). For even \(N\), the midpoint splits each symmetric distribution into equal halves, giving equality at \(k=N/2\).

**Step 3: exact maximum and location.** For all \(k\),
\[
\Delta_N(k+1)-\Delta_N(k)=h_k-p_k
=p_k\left(\frac{2^m\binom mk}{\binom{2m}m}-1\right).
\]
On the upper half \(\binom mk\) strictly decreases as \(k\) increases. Hence this increment changes from positive to negative once, with possibly one zero increment. Together with Step 2 this proves the exact maximizer criterion and the assertion of one or two adjacent maximizing indices.

**Step 4: Gaussian transition and sharp constant.** Put \(j=m/2+t\sqrt m\) with bounded \(t\). Stirling's formula gives the two normalized local mass asymptotics, uniformly for bounded \(t\):
\[
p_j\sim\sqrt{\frac2{\pi m}}e^{-2t^2},\qquad
h_j\sim\frac2{\sqrt{\pi m}}e^{-4t^2}.
\]
The corresponding distributions therefore have limiting centered variances \(1/4\) and \(1/8\) on the \(\sqrt m\) scale. Gaussian tail control follows, for example, from their exact variances \(m/4\) and \(m^2/[4(2m-1)]\), together with compact-uniform local approximation and Chebyshev truncation. This proves the two stated distribution-function limits, including moving thresholds with \(o(\sqrt N)\) perturbations.

For \(k=m/2+s\sqrt m+O(1)\), the threshold ratio in Step 3 obeys
\[
\frac{\binom mk}{\binom{2m}m/2^m}
\longrightarrow\sqrt2 e^{-2s^2}.
\]
Since the ratio is strictly decreasing to the right of the midpoint, every maximizing index satisfies \((k_N-N/2)/\sqrt N\to s_*\), where \(s_*^2=(\log2)/4\). Finally the limiting positive gap is \(g(s)=\Phi(2\sqrt2 s)-\Phi(2s)\). Its derivative vanishes on \(s>0\) exactly when \(\sqrt2 e^{-4s^2}=e^{-2s^2}\), i.e. \(s=s_*\); it is positive before and negative after. Substituting \(s_*\) gives the asserted sharp constant. This completes all finite and asymptotic statements.

## Verification
Run `python3 verify_exit.py` using only the Python standard library. It checks the exact harmonic equations as rational identities, Vandermonde's identity, symmetry, the majority sign and maximizing-index behavior for every \(3\le N\le39\). It separately calculates binomial and hypergeometric log-gamma masses for \(N\in\{101,401,1601,6401\}\), checks convergence toward the analytical maximum and its predicted location, and prints the limiting constant. The checked program passes 4305 assertions in the supplied environment. These finite numerical tests corroborate but do not replace the analytical infinite-population proof.

As a small exact example, for \(N=5\), the initial count \(k=3\) gives \(\rho_2^{(5)}(3)=11/16\) and \(\rho_3^{(5)}(3)=53/70\); the difference is \(39/560\), already favoring the three-neighbor panel after a majority of A is established.

## Relationship to prior work
Ramirez, Vazquez, San Miguel and Galla (arXiv:2310.20548v1, 2023) derive the underlying nonlinear voter model, finite-population jump rates and the equality of the \(q=2\) and \(q=3\) **deterministic** mean-field density equations. Those ingredients and the qualitative majority drift are established, not new here. Their analyzed quantities center on active-link decay, consensus times, multistate regimes and pair approximations; the exact pair of binomial/hypergeometric finite-size exit laws and the sharp maximum separation are not stated in the examined relevant full text.

Castellano, Muñoz and Pastor-Satorras (arXiv:0907.1775, 2009) formulate the original nonlinear \(q\)-voter process and use a backward diffusion approximation to analyze exit probabilities, including a special \(q=4\) example. Their approximate diffusion treatment does not give this exact finite-population comparison or its asymptotically maximized gap. Doniec et al. (arXiv:2502.10172, 2025) treat a different generalized biased rule and numerically solve finite-state Markov-chain exit probabilities for higher \(q\); their inspected analysis does not imply the present exact unforced two-rule comparison. The symmetric hypergeometric and binomial Gaussian approximations used in the last step are classical, with relevant rigorous work by Mattner and Schulz (arXiv:1404.7657); the standard probability tools are not claimed as innovations. A broader literature result explicitly joining these identities might still affect publication priority.

## Limitations
The finding concerns exactly two unanimous-neighbor panel sizes on finite complete graphs with independent draws with replacement, no noise and two opinions. It does not classify general influence networks, \(q\ge4\), heterogeneous updating, partial conformity or spontaneous flips. A statement of novelty is necessarily limited to the exact model-specific coupling of already standard birth-death and probability-distribution techniques; extensive future searches may identify unexamined equivalent or stronger published results. No independent scientific audit has been performed.

## References
1. L. S. Ramirez, F. Vazquez, M. San Miguel and T. Galla, *Ordering dynamics of nonlinear voter models*, first public arXiv version 31 October 2023, arXiv:2310.20548v1, https://arxiv.org/abs/2310.20548.
2. C. Castellano, M. A. Muñoz and R. Pastor-Satorras, *The non-linear q-voter model*, arXiv:0907.1775 (2009), https://arxiv.org/abs/0907.1775.
3. M. Doniec, P. Mullick, P. Sen and K. Sznajd-Weron, *Modeling biases in binary decision-making within the generalized nonlinear q-voter model*, arXiv:2502.10172 (2025), https://arxiv.org/abs/2502.10172.
4. L. Mattner and J. Schulz, *On normal approximations to symmetric hypergeometric laws*, arXiv:1404.7657 (2014), https://arxiv.org/abs/1404.7657.
5. P. Przybyła, K. Sznajd-Weron and M. Tabiszewski, *Exit probability in a one-dimensional nonlinear q-voter model*, arXiv:1107.0366 (2011), https://arxiv.org/abs/1107.0366.
