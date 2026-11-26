# Exact stationary rank diagram for two-level small-sample quantile Kaczmarz

## Finding

Consider a scalar system with all row coefficients equal to 1: there are \(g\) rows with observed right-hand side \(0\) and \(c\) rows with observed right-hand side \(h>0\), where \(1\le c<g\). At each step take a fresh batch of \(s\) rows, order their absolute residuals, and project exactly onto the row at a fixed order rank \(1\le j\le s\) **in that same batch**. The uncorrupted solution is \(0\). Let \(R_j\) be the stationary mean squared error for rank \(j\).

* **Without replacement:** The batch is a uniform \(s\)-element subset and \(1\le s\le g\). Put \(\ell=\max(0,s-c)\). Precisely the ranks \(1\le j\le\ell\) have \(R_j=0\); the risks at ranks \(\ell+1,\ldots,s\) are positive and strictly increasing. If \(s\le c\), rank one is the unique minimizer and
  \[
  \min_j R_j=h^2\frac{\binom{c}{s}}{\binom{c}{s}+\binom{g}{s}}.
  \]
  If \(s>c\), the minimizing ranks are exactly \(1,\ldots,s-c\) and each reaches and permanently retains \(0\) almost surely. Thus \(s=c+1\) is the smallest batch size allowing exact absorption at some rank.
* **With replacement:** The batch consists of \(s\) independent uniform row draws, for any positive integer \(s\); multiplicities are counted when ordering the residuals. Then \(0<R_1<R_2<\cdots<R_s\) (with just one rank when \(s=1\)), and
  \[
  R_1=h^2\frac{c^s}{c^s+g^s}.
  \]
  No fixed rank at a finite batch size gives exact absorption.

The contribution is the stationary risk ordering and optimization. The two-state law and odd-median independence for subset sampling are prior results [1]. They are not asserted as new here.

## Assumptions and scope

Batches are independent across updates. Projection is unrelaxed; even an arbitrary real starting point lands at \(0\) or \(h\) on its first update. The particular state selected on that first update may depend on the tie convention if the two residual levels coincide. In either projected state, ties are only within one right-hand-side type and do not affect the update. No conclusion is asserted for independent update rows, nonidentical coefficients, noise in the clean rows, or more than two right-hand-side levels.

## Proof

**Transition law used in the optimization.** Write \(m=g+c\) and let \(w_u\) be the probability a sampled batch contains \(u\) corrupt rows or draws. For subset sampling,
\[
w_u=\frac{\binom{c}{u}\binom{g}{s-u}}{\binom{m}{s}},
\]
with out-of-range binomial coefficients interpreted as zero; for independent draws, \(w_u=\binom{s}{u}(c/m)^u(g/m)^{s-u}\). Starting at \(0\), the selected row is corrupt iff there are fewer than \(j\) clean draws, equivalently \(u\ge s-j+1\). Starting at \(h\), the selected row is clean iff \(u<j\). Let
\[
A_j=\sum_{u=0}^{j-1}w_{s-u},\qquad B_j=\sum_{u=0}^{j-1}w_u.
\]
These are the respective probabilities of \(0\to h\) and \(h\to0\). In both sampling schemes \(w_0>0\), hence \(B_j>0\) and \(A_j<1\). Every invariant law is supported on \(\{0,h\}\) by the one-step projection. Balancing flux between the states gives the unique invariant mass \(\pi_j=A_j/(A_j+B_j)\) at \(h\). Thus \(R_j=h^2\pi_j\), and risk increases strictly when the odds \(A_j/B_j\) increase strictly.

**Ordering for subset sampling.** The assumption \(s\le g\) gives \(w_u>0\) exactly for \(0\le u\le q=\min(c,s)\). The first positive reflected weight \(w_{s-u}\) occurs at \(u=s-q=\ell\). For indices with \(w_u>0\), let \(\rho_u=w_{s-u}/w_u\). It is zero up to but not including \(u=\ell\). Whenever \(\ell\le u<q\), cancellation gives
\[
\frac{\rho_{u+1}}{\rho_u}
=\frac{(g-u)(g-s+u+1)}{(c-u)(c-s+u+1)}>1.
\]
The denominator factors are positive in that range, and the corresponding numerator factors are strictly larger because \(g>c\). For \(j\le q+1\), the odds \(A_j/B_j\) are the weighted mean of \(\rho_0,\ldots,\rho_{j-1}\) with the respective weights \(w_u\). In any step from rank \(j\) to \(j+1\) with \(\ell\le j\le q\), the newly inserted positive ratio \(\rho_j\) is greater than each previous ratio, so the odds strictly increase. If a rank increment adds index \(j>q\), the denominator is unchanged and the numerator increases strictly exactly when \(j\ge\ell\), because then \(w_{s-j}>0\). This also covers \(\ell>q\), in which case all positive risks occur after the denominator has saturated. Therefore the odds are zero exactly at ranks \(1,\ldots,\ell\) and strictly increasing on the positive range. When \(s\le c\), substituting \(j=1\) leaves only the all-corrupt and all-clean batch probabilities, giving the stated optimum. When \(s>c\) the zero-risk ranks have \(A_j=0\) and \(B_j>0\), so starting from \(h\) the number of steps to reach the absorbing state is geometric. At any positive-risk rank, \(A_j>0\) prevents permanent retention of \(0\) almost surely, by independence of fresh batches.

**Ordering for independent draws.** All weights are positive; every reflected ratio \(\rho_u=w_{s-u}/w_u\) is defined and satisfies \(\rho_{u+1}/\rho_u=(g/c)^2>1\). Hence every rank increment strictly raises the running weighted mean. Rank one has \(A_1=(c/m)^s\), \(B_1=(g/m)^s\); these give its positive risk and rule out absorption at every finite size.

## Verification

Run `python3 verify_rank.py` in this directory. The standard-library checker directly enumerates batches, sorts the actual scalar residuals in both states, and checks the exact rational risk ordering and optimal values. It tests subset sizes \(1\le s\le g\) for \(2\le g\le6\), \(1\le c<g\); it also tests independent draws up to \(s=5\) for \(2\le g\le4\), \(1\le c<g\). These finite checks supplement the proof and do not establish its universal conclusions.

## Relationship to prior work

The same one-coordinate, same-batch subset model and its exact two-state transition probabilities, invariant law, eigenvalue, covariance, and independence at the odd-batch median appear in [1]. The existence cutoff for an absorbing rank follows already from the support of that transition law. The distinctive calculation here is the strict ordering of the full positive part of the stationary risk profile, including when some ranks are absorbing, and the optimized comparison with independent draws in the batch. The same-batch row-selection algorithm itself is due to [2, §V-D, Algorithm 2]. By contrast [3, Algorithm 1.1] estimates the quantile from a sample but independently selects a tentative update row from the full system; its sample-size bounds apply to a different mechanism.

## References

1. *Exact two-state dynamics and a sharp rare-corruption horizon for small-sample quantile Kaczmarz*, Resultary record `2639ecb81dd1`, [statement and proof](https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-exact-two-state-dynamics-and-a-sharp-rare-corruption-horizon-for--2639ecb81dd1/RESULT.md).
2. J. Haddock, A. Ma, and E. Rebrova, *On Subsampled Quantile Randomized Kaczmarz*, [arXiv:2308.07987](https://arxiv.org/abs/2308.07987), §V-D, Algorithm 2.
3. J.-F. Cai, J. Chen, A. Ma, and T. Wu, *On the Subsample Size of Quantile-Based Randomized Kaczmarz*, [arXiv:2507.15185](https://arxiv.org/abs/2507.15185), Algorithm 1.1 and discussion.
