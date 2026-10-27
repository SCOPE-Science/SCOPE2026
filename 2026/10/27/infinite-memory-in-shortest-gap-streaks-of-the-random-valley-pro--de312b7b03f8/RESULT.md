# Infinite memory in shortest-gap streaks of the random-valley process

## Finding

Let \((U_i)_{i\in\mathbb Z}\) be independent random variables with a common atomless distribution. Declare \(i\) a **valley** if \(U_i<U_{i-1}\) and \(U_i<U_{i+1}\). Condition on the event that 0 is a valley, and let \(G_1,G_2,\ldots\) be the successive positive spacings between valleys, starting at 0. Each spacing is an integer at least 2.

For every integer \(k\ge0\), define
\[
p_k=\Pr(G_1=\cdots=G_k=2\mid 0\text{ is a valley}),\qquad p_0=1,
\]
and the conditional continuation probability \(r_k=p_{k+1}/p_k\). Write \(E_n\) for the number of alternating permutations on \(n\) labels (the Euler zigzag number), and \(S_s=\sum_{j\ge0}(2j+1)^{-s}\) for \(s>1\).

Then the entire shortest-spacing streak law and its conditional continuation probabilities are
\[
\boxed{\quad p_k=\frac{3E_{2k+3}}{(2k+3)!}=6\left(\frac2\pi\right)^{2k+4}S_{2k+4},\qquad
r_k=\frac4{\pi^2}\frac{S_{2k+6}}{S_{2k+4}}.\quad}
\]
The continuation probabilities are **strictly increasing** for every \(k\ge0\) and satisfy
\[
\frac25=r_0<r_1=\frac{17}{42}<r_2=\frac{62}{153}<\cdots<\frac4{\pi^2}.
\]
In particular the sequence of consecutive valley gaps in its stationary valley-index law **is not a Markov chain of any finite order**. The tail of a shortest-gap streak has the exact sharp asymptotic
\[
p_k\sim 6\left(\frac2\pi\right)^{2k+4}\quad(k\to\infty).
\]

## Assumptions and scope

The index set is the two-sided integer line. The priorities are independent and identically distributed and have an atomless common law; the probability integral transform reduces the problem to independent uniform priorities. A valley has probability \(1/3\); almost surely there are infinitely many valleys in both directions (for example, disjoint blocks of three sites contain a valley with fixed positive probability). All displayed conditional probabilities are therefore defined. Distances count lattice edges, not non-valley sites.

The valley-index process means the bi-infinite sequence of gaps viewed from a typical valley. Its law is invariant under shifting the marked origin from a valley to its next valley: by the translation-invariant mass-transport identity, the total expected mass sent from valleys to their successors equals the total expected mass received at valleys. Conditioning on a valley at the origin is the resulting stationary Palm version. The claimed non-Markov property concerns finite-order **homogeneous** Markov models for this stationary gap sequence.

## Proof

**1. Exact cylinder probabilities.** A sequence of \(k\) consecutive gaps of size 2 occurs exactly when positions \(0,2,\ldots,2k\) are valleys. The event, together with the requirement that 0 is a valley, is equivalent to strict alternating comparisons on the \(2k+3\) consecutive priorities with indices \(-1,0,1,\ldots,2k+1\):
\[
U_{-1}>U_0<U_1>U_2<\cdots>U_{2k}<U_{2k+1}.
\]
The displayed orientation has exactly \(E_{2k+3}\) of the \((2k+3)!\) equally likely relative orders; reflection or complementation shows its count is the classical alternating-permutation number. As \(\Pr(0\text{ is a valley})=1/3\), dividing gives \(p_k=3E_{2k+3}/(2k+3)!\). This also handles \(k=0\) since \(E_3=2\).

**2. Analytic representation.** The standard Euler enumeration gives
\[
\tan z=\sum_{m\ge0}\frac{E_{2m+1}}{(2m+1)!}z^{2m+1}.
\]
Differentiating the Euler product for \(\cos z\) yields the absolutely convergent partial fraction expansion, for \(|z|<\pi/2\),
\[
\tan z=\sum_{j\ge0}\frac{8z}{(2j+1)^2\pi^2-4z^2}.
\]
Expansion in a geometric series gives, for odd \(n\ge1\),
\[
\frac{E_n}{n!}=2\left(\frac2\pi\right)^{n+1}S_{n+1}.
\]
Substitute \(n=2k+3\) into the first part and divide consecutive probabilities to obtain the stated formulas for \(p_k\) and \(r_k\).

**3. Strict increasing continuation.** For every \(s>1\), the strict Cauchy–Schwarz inequality applied to the two nonproportional positive sequences \(((2j+1)^{-s/2})_j\) and \(((2j+1)^{-(s+4)/2})_j\) gives
\[
S_{s+2}^2<S_sS_{s+4}.
\]
Thus the ratios \(S_{s+2}/S_s\) are strictly increasing along increments of 2. Since \(S_s> S_{s+2}>1\) and \(S_s\to1\) as \(s\to\infty\), these ratios are strictly below 1 and converge to 1. Taking \(s=2k+4\) proves \(r_k\nearrow4/\pi^2\). Substituting \(E_3=2\), \(E_5=16\), \(E_7=272\), and \(E_9=7936\) gives the first three conditional probabilities. The same limit for \(S_{2k+4}\) yields the streak-tail asymptotic.

**4. Exclusion of finite Markov order.** Suppose the stationary gap process were an order-\(m\) homogeneous Markov chain, for some finite \(m\ge1\). Conditional on \(G_1=\cdots=G_k=2\), with \(k\ge m\), the conditional probability of \(G_{k+1}=2\) would depend only on the last \(m\) gaps (all equal to 2), and by stationarity could not depend on \(k\). It would therefore equal one common transition probability for every \(k\ge m\). But the exact \(r_k\) is strictly increasing for all \(k\), a contradiction. The order-zero (independent) case is excluded by \(r_0\ne r_1\).

## Verification

The accompanying standalone `verify_valley_streak.py` uses an independent exact-integer recurrence for the Euler numbers, enumerates all permutations of lengths 3, 5, 7 and 9, and checks 108 exact-rational/computational assertions. Among the checks are \(p_0=1\), \(p_1=2/5\), \(p_2=17/105\), \(p_3=62/945\), the corresponding conditional probabilities, 31 strict successive inequalities, and upper bounds against \(4/\pi^2\) using a high-precision Machin-series computation. Its actual output is stored in `verification_output.txt`. Finite arithmetic does **not** establish the for-all-\(k\) theorem; the strict inequality and Markov exclusion are analytical.

## Relationship to prior work

Matijasevick, *Gaps between roots in ballistic deposition on a strip* (first posted 15 October 2026, arXiv:2610.21094v1), identifies deposition roots with valleys of an iid priority sequence and develops one-gap means, two-gap joint laws \(u_{ij}\), and certain three-gap events \(v_{ij}\), together with fluctuations and limiting count laws. In particular the first few shortest-gap streak probabilities, through three consecutive gaps, are **already implicit** in that paper's joint-event formulas and are not asserted as independent novelties here. The contribution under review is the entire all-orders sequence of shortest-gap continuation probabilities, its strict monotone dependence on the full streak age, and the consequent obstruction to every finite-order Markov description of root spacings.

Stanley's *A Survey of Alternating Permutations* (arXiv:0912.4240, first posted 2009) records the classical Euler enumeration \(\sec z+\tan z\). That generating function gives the enumerative foundation; it is not new here. Applying the classical coefficients to stationary valley-gap run conditioning, then using strict Dirichlet-series log-convexity to obtain infinite stochastic memory, is the substantive synthesis. The exact cylinder coefficients are directly derivable from the classical enumeration, so this is an explicitly acknowledged novelty/priority limitation.

## Limitations

The statement is for iid continuous priorities on the integer line, equivalently the infinite-volume local limit of uniformly ranked cyclic deposition roots. It does not establish a finite-cycle all-length identity when the run approaches the circumference, nor a classification of all possible gap histories or non-iid priority laws. The asymptotic concerns streaks of **minimum length 2 only**, not all types of runs. A broad earlier theorem on Markov order of random-permutation local-extremum spacings could subsume the conclusion, and independent historical-priority review remains outstanding. No external independent audit has been performed.

## References

1. Mateo Matijasevick, *Gaps between roots in ballistic deposition on a strip: linear variance, Gaussian limits and a Poisson regime*, arXiv:2610.21094v1 (first public 2026-10-15). https://arxiv.org/html/2610.21094v1
2. Richard P. Stanley, *A Survey of Alternating Permutations*, arXiv:0912.4240 (2009), author manuscript https://math.mit.edu/~rstan/papers/altperm.pdf
3. Classical Euler product for the cosine and the alternating-permutation generating function; the precise formulas used are reproduced in the proof.
