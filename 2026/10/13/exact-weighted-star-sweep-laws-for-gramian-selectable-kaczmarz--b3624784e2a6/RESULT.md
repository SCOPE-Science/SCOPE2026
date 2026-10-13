# Exact weighted-star sweep laws for Gramian-selectable Kaczmarz

## Finding

Fix an integer \(m\ge2\) and \(w>0\). For a star-Gramian system described below, Gramian-selectable randomized Kaczmarz (GSSRK), started immediately after selecting its central equation, has the following *structural sweep-certificate* mean:

\[
\mathbb E T_G=\binom{m+w}{m-1}+\binom{m+w-1}{m-1}-1. \tag{1}
\]

The corresponding certificate time for ordinary independently sampled norm-weighted randomized Kaczmarz (RK), started at the same post-center state, has mean

\[
\mathbb E T_R=\frac{m+w}{w}\left[\frac{\Gamma(m+w+1)}{\Gamma(m+1)\Gamma(w+1)}-1\right]. \tag{2}
\]

In both algorithms the certificate guarantees that the current iterate equals the exact solution, regardless of the starting iterate. It is not claimed to be the *first actual solution-hitting time*: accidental or structurally untracked earlier exact convergence is not excluded. Conditional upon starting immediately after a center, both certificate times are almost surely finite.

For fixed \(w>0\),

\[
\mathbb E T_G\sim\frac{m^{w+1}}{\Gamma(w+2)},\qquad
\mathbb E T_R\sim\frac{m^{w+1}}{w\Gamma(w+1)},\qquad
\frac{\mathbb E T_R}{\mathbb E T_G}\longrightarrow\frac{w+1}{w}. \tag{3}
\]

At equal row weights \(w=1\), these are exactly \(\mathbb E T_G=(m^2+3m-2)/2\) and \(\mathbb E T_R=m(m+1)\). In the one-sided limit \(w\downarrow0\) at fixed \(m\), the means become \(m\) and \(mH_m\), respectively; the model itself assumes strictly positive \(w\).

## Assumptions and scope

Let \(A\) be an \((m+1)\)-by-\(m\) real matrix. Its leaf rows are \(a_i=e_i^\top\) for \(1\le i\le m\), and its center row is \(a_0=\sqrt{w/m}\,\mathbf1^\top\). The right-hand side is \(b=Ax^\star\) for an arbitrary \(x^\star\in\mathbb R^m\), so the system is consistent and has a unique solution. Kaczmarz uses the orthogonal hyperplane projection

\[
 x^+=x-\frac{a_i x-b_i}{\|a_i\|_2^2}a_i^\top.
\]

For GSSRK, draw only from the current selectable set \(S\), with conditional probabilities proportional to the fixed squared row norms: weight \(1\) per leaf and \(w\) for the center. After projecting row \(i\), update exactly by \(S^+=(S\cup N(i))\setminus\{i\}\), where \(N(i)=\{j\ne i: a_i a_j^\top\ne0\}\). The starting state is the state *immediately after a center projection*, namely \(S=\{1,\ldots,m\}\). This is an admissible state of the published algorithm (including after its first central draw).

Define the certificate event as selection of all \(m\) distinct leaves *after the latest center draw*, with no intervening center draw. Let \(T_G\) count all performed projections after the starting center up to the first certificate. Ordinary RK uses the same original norm-squared weights at each independent selection, including repetitions, and its certificate time \(T_R\) is defined identically from the initial post-center state. This definition compares a common verifiable terminal condition, not equal-cost implementations or their earliest exact solutions.

Throughout, the generalized binomial coefficient means \(\binom{u}{k}=\Gamma(u+1)/[\Gamma(k+1)\Gamma(u-k+1)]\) when \(u>k-1\), with integer \(k\ge0\).

## Proof

**Star transition and certificate.** Distinct leaves have zero Gramian inner product, while each leaf has nonzero inner product \(\sqrt{w/m}\) with the center. Therefore the nonorthogonality graph is exactly a star. Immediately after projecting the center, every leaf and no center is selectable. After \(j\) different leaves have been selected, for \(1\le j<m\), the selectable set contains exactly the \(m-j\) unselected leaves plus the center. The next action is an unselected leaf with probability \((m-j)/(m-j+w)\), otherwise the center is selected and the selectable state resets to all leaves. The first leaf after any center is forced.

Selecting any leaf sets its coordinate to the correct value, and subsequent distinct leaf selections do not alter previously fixed leaf coordinates. Hence a complete leaf sweep without a center sets all coordinates to \(x^\star\). This establishes the certificate property for every starting iterate.

**GSSRK renewal equation.** Call the random sequence from all leaves selectable until the next center (failure) or completion of all leaves (success) an episode. Since the selector resets after each center, episodes are identically distributed with independent selection randomness. The probability of reaching the \(j\)-th distinct leaf before a center is

\[
 \pi_j=\prod_{r=m-j+1}^{m-1}\frac{r}{r+w}\quad (1\le j\le m).
\]

In particular, the probability that an episode succeeds is

\[
 p_G=\pi_m=\prod_{r=1}^{m-1}\frac r{r+w}
 =\frac{\Gamma(m)\Gamma(w+1)}{\Gamma(m+w)}>0.
\]

Counting one projection for each leaf actually reached and one for a center that terminates a failed episode, the expected episode length is \(\mathbb E L_G=\sum_{j=1}^m\pi_j+1-p_G\). Renewal at failure yields \(\mathbb E T_G=\mathbb E L_G/p_G\). Moreover,

\[
 \frac{\pi_j}{p_G}
 =\binom{w+m-j}{m-j},\qquad
 \frac{1}{p_G}=\binom{w+m-1}{m-1}.
\]

The generalized hockey-stick identity \(\sum_{r=0}^{m-1}\binom{w+r}{r}=\binom{w+m}{m-1}\), valid by generalized Pascal recursion, now gives equation (1).

**Independent RK comparison.** In an ordinary RK episode, independently draw from \(m\) equally weighted leaves and a center of weight \(w\). A successful episode has all leaf labels observed before the first center. Equivalently use independent exponential first-appearance clocks of rates \(1\) for the leaves and \(w\) for the center. This event has probability

\[
 p_R=\prod_{r=1}^{m}\frac r{r+w}
 =\frac{\Gamma(m+1)\Gamma(w+1)}{\Gamma(m+w+1)}>0.
\]

The number of center draws before the certificate is the number of failed episodes, with mean \(p_R^{-1}-1\). On the other hand, conditional on every past row history, the next ordinary RK draw is the center with fixed probability \(w/(m+w)\). Wald's count identity gives \(\mathbb E[\#\text{centers before completion}]=[w/(m+w)]\mathbb E T_R\). All means are finite because every episode has strictly positive success probability and its length is bounded above by the waiting time to the next center, which has finite expectation. Solving this identity proves equation (2).

**Growth and scaling.** At fixed \(w>0\), the ratio asymptotic \(\Gamma(m+a)/\Gamma(m+b)\sim m^{a-b}\) in (1) and (2) yields equation (3). The \(w=1\) identities follow by factorial cancellation. At \(w\downarrow0\) with fixed \(m\), \(p_R^{-1}=\prod_{r=1}^m(1+w/r)=1+wH_m+O(w^2)\), while equation (1) tends to \(m\). Rescaling the center row alters its norm-squared sampling weight but does not alter its Kaczmarz projection hyperplane or the set of nonzero Gramian off-diagonal entries, proving the stated weight sensitivity.

## Verification

The accompanying `verify.py` performs exact-rational checks of the closed forms against separately derived finite-state first-step recurrences for \(m=2,\ldots,10\) and the six weights \(1/4,1/2,1,3/2,2,5\). It additionally checks the star selectable-set transitions and two equal-weight identities. Run `python3 verify.py`; the expected start of output is `PASS 126 exact closed-form/recurrence equalities`. These tests are finite consistency checks; the argument above proves the statements for every integer \(m\ge2\) and real \(w>0\).

## Relationship to prior work

Yaniv, Moorman, Swartworth, Tu, Landis, and Needell describe GSSRK and its exact selectable-set update in Algorithm 3, prove expected squared-error contraction estimates, and discuss graph-theoretic bounds on selectable-set size in Section 4 [1]. Their bounds do not state this probability law for completing a leaf sweep or the exact norm-weighted IID certificate comparison. Nutini, Schmidt, Laradji, Friedlander, and Koepke introduced sampling accelerated by the orthogonality graph and discuss graph-aware selection and data structures [2]. Their published convergence rates and Appendix L are algorithmic precedents, not this stopping-certificate formula. The reduction of the independent baseline to coupon collection is standard; the exact structural-selector renewal and its dependence on a rescalable row weight are the points of the present statement. Unindexed derivations of this specialized relation may exist.

## Limitations

The results concern a deliberately structured redundant system and a *sufficient structural certificate*, not the generally unknown first actual exact-convergence time or time to reach a numerical tolerance. Row-selection overhead and practical wall-clock speed are excluded. The center row is a linear combination of leaf equations; the result does not extend automatically to nonorthogonal leaves, noisy systems, inconsistent equations, other selectable-set updates, or a generic Gramian. The fixed-\(w\) asymptotics do not assert uniformity when \(w\) scales with \(m\).

## References

[1] Y. Yaniv, J. D. Moorman, W. Swartworth, T. Tu, D. Landis, and D. Needell, *Selectable Set Randomized Kaczmarz*, arXiv:2110.04703, first publicly submitted 2021-10-10, especially Algorithm 3 and Section 4, https://arxiv.org/html/2110.04703v2 .

[2] J. Nutini, M. Schmidt, I. Laradji, M. P. Friedlander, and H. Koepke, *Convergence Rates for Greedy Kaczmarz Algorithms, and Faster Randomized Kaczmarz Rules Using the Orthogonality Graph*, arXiv:1612.07838, especially Section 9 and Appendix L, https://arxiv.org/html/1612.07838v1 .
