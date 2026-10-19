# Exact absorption-time law for fixed-increment limited-precision stochastic summation

## Finding

A fixed, positive representable increment is eventually **lost forever** under a common limited-precision stochastic-rounding rule, even though the calculation initially makes random upward progress. The absorbing value and the **entire time-to-absorption distribution** are explicit. In the parameter range below the accumulator traverses at most the \(r\) subsequent binary binades, whereas ideal stochastic rounding traverses every binade almost surely. This supplies a quantitative, infinite-horizon qualification to finite-precision summation error bounds.

For the precise setup below let \(T\) be the first time the accumulator reaches the terminal power of two. Its probability generating function is

\[
\mathbb E[z^T]=\prod_{k=E}^{L-1}
\left(\frac{q_k z}{1-(1-q_k)z}\right)^{2^{p-1}},
\qquad q_k=2^{-r}\left\lfloor\frac{a}{2^{k-p-r+1}}\right\rfloor.
\]

Thus its distribution is a finite convolution of standard negative-binomial laws, with exact mean and variance

\[
\mathbb E T=2^{p-1}\sum_{k=E}^{L-1}\frac1{q_k},\qquad
\operatorname{Var}(T)=2^{p-1}\sum_{k=E}^{L-1}\frac{1-q_k}{q_k^2}.
\]

## Assumptions and scope

Fix integers \(p\ge2\), \(r\ge1\), and \(E\in\mathbb Z\). The floating-point set consists of **positive normalized binary values with unbounded integral exponents** and \(p\) significand bits. Independent fresh rounding randomness is used at every addition; there is no overflow, underflow, subnormal region, shared randomness, or sticky-bit correction.

For \(k\in\mathbb Z\), the adjacent precision-\(p\) spacing inside the binade \([2^k,2^{k+1})\) is \(u_k=2^{k-p+1}\); the \(p+r\)-bit spacing is \(v_k=2^{k-p-r+1}=u_k/2^r\). The operator \(\mathrm{SR}_{p,r}(x)\) first truncates the exact positive argument \(x\) toward zero to a precision-\(p+r\) value, then rounds it to one of the two enclosing precision-\(p\) values with probabilities yielding the truncated value in expectation. This is the specific truncated-guard operator of El Arar et al.; other few-bit rounding rules need not behave this way.

Choose a constant positive \(p\)-representable operand \(a\) such that

\[
v_E\le a<u_E.
\]

Set \(S_0=2^E\), and for every integer \(t\ge0\) set \(S_{t+1}=\mathrm{SR}_{p,r}(S_t+a)\). Define

\[
L=\min\{k\in\mathbb Z:k\ge E,\ v_k>a\}
=E+1+\left\lfloor\log_2(a/v_E)\right\rfloor,
\quad N=2^{p-1},\quad
q_k=\frac{\lfloor a/v_k\rfloor}{2^r}\quad(E\le k<L).
\]

The logarithm expression is exact, including equality cases when the increment is an integer power of two times \(v_E\). It follows from \(v_E\le a<2^rv_E\) that \(1\le L-E\le r\).

For \(0<q\le1\), \(\mathrm{NegBin}(N,q)\) means the number of independent Bernoulli trials needed to accumulate \(N\) successes, with support \(N,N+1,\dots\). Let \(T=\inf\{t\ge0:S_t=2^L\}\).

## Proof

**1. Exact one-step transition.** Consider a precision-\(p\) grid point \(s=2^k+j u_k\), with \(E\le k<L\) and \(0\le j<N\). Since \(0<a<u_E\le u_k\), the exact sum \(s+a\) lies strictly inside the *same* binade and below \(s+u_k\), even for \(j=N-1\). Because \(s\) itself lies on the \(p+r\) grid,

\[
\operatorname{trunc}_{p+r}(s+a)
=s+v_k\lfloor a/v_k\rfloor.
\]

Therefore the next state is \(s+u_k\) with probability \(q_k=v_k\lfloor a/v_k\rfloor/u_k\) and remains at \(s\) otherwise. For \(k<L\), the definition of \(L\) gives \(a\ge v_k\), whence \(q_k\ge 2^{-r}>0\); the strict bound \(a<u_k\) gives \(q_k<1\). At the terminal boundary \(s=2^L\), the inequality \(0<a<v_L\) gives \(\operatorname{trunc}_{p+r}(s+a)=s\), so this state is *fully absorbing*.

**2. Passage times.** Each binade contains exactly \(N=2^{p-1}\) successive \(p\)-grid increments. By step 1, at every one of these states the passage to the next grid point occurs after an independent geometric waiting time with success parameter \(q_k\). Consequently the time \(T_k\) to traverse binade \(k\) is \(\operatorname{NegBin}(N,q_k)\). The fresh randomness and disjoint sets of trial times make the \(T_k\) independent. There are \(L-E\le r\) binades, each with strictly positive success probability, so \(T=\sum_{k=E}^{L-1}T_k<\infty\) almost surely. The generating function and moment formulas in the Finding section follow from geometric probability generating functions and independence. The accumulator is then identically \(2^L\) forever.

**3. Comparison with ideal stochastic rounding.** For the ideal (untruncated) stochastic-rounding operator, at any precision-\(p\) grid point \(s\ge2^E\) the next step increases to the following grid point with probability \(a/u_k>0\), provided \(a<u_k\), which holds for every \(k\ge E\). Every one-state geometric waiting time is finite almost surely. By countable intersection, all countably many grid levels are eventually traversed, so the ideal process tends to \(+\infty\) almost surely. For the truncated rule, the true exact sum \(2^E+ta\) tends to infinity whereas \(S_t\to2^L\). Hence \(1-S_t/(2^E+ta)\to1\) almost surely.

**4. Illustrative sharp guard-bit scale.** Choosing \(a=v_E\) gives \(L=E+1\), \(q_E=2^{-r}\) and the exact distribution \(T\sim\mathrm{NegBin}(2^{p-1},2^{-r})\). In particular \(\mathbb ET=2^{p+r-1}\) and \(\operatorname{Var}(T)=2^{p-1}(1-2^{-r})2^{2r}\). This is an exact absorption-time law, not an asymptotic estimate.

## Verification

The included standalone standard-library `verify.py` tests the truncation definition directly using rational arithmetic, without calling the derived formulas to construct its transition probabilities. It checked 62,496 intermediate grid states over exponent shifts, several significand widths and guard-bit budgets; for every state it compared the independently implemented \(p+r\)-bit truncation probabilities with \(q_k\). It also checked that the predicted terminal boundary is absorbing, and independently summed first two moments from backward state equations. All assertions passed. At \(E=0,p=5,r=3,a=1/128\), it obtains \(S_T=2\), \(\mathbb ET=128\) and \(\operatorname{Var}(T)=896\). These finite checks support, but do not replace, the proof for all parameter values.

To reproduce: from this document's directory run `python3 verify.py`; no external packages are required.

## Relationship to prior work

El Arar, Fasi, Filip and Mikaitis first defined this truncated-guard limited-precision rounding operator and analyzed its bias and finite-\(n\) recursive-summation error bounds [1]. Their 2026 sequel develops finite-depth error bounds for Horner evaluation and pairwise summation [2]. Both the rounding definition and the fact that truncation can discard small contributions are **prior knowledge**. The contribution claimed here is the *global fixed-increment Markov classification*: the exact maximum number of traversed binades, eventual deterministic absorbing power, full negative-binomial convolution law for absorption time, moments, and contrast with ideal stochastic rounding on the same infinite-exponent model. The 2025 few-random-bit comparison [3] concerns multiple alternative implementations and their biases; a 2025 neuromorphic study [4] explicitly observes loss of guard bits for small addends and uses stochastic sticky bits to overcome this issue. The absorption mechanism itself should therefore not be claimed as newly discovered.

## Limitations

The theorem is for one *fixed*, positive, \(p\)-representable addend satisfying \(v_E\le a<u_E\), positive normal inputs, independent truncation-based stochastic rounding, and unbounded exponents. It is not a finite-format overflow statement and does not cover varying/random addends, hardware-specific extra sticky bits, rounding of the intermediate value by a different rule, or the behavior of implementations with correlated random bits. The specific exact distribution is established analytically, but wider hardware generality and uniqueness in the full stochastic-rounding literature have not been certified. The finite program cannot independently prove the infinite-horizon almost-sure conclusion.

## References

[1] E. M. El Arar, M. Fasi, S.-I. Filip and M. Mikaitis, *Probabilistic error analysis of limited-precision stochastic rounding*, arXiv:2408.03069, first publicly posted 2024-08-06. https://arxiv.org/html/2408.03069v3

[2] E. M. El Arar, M. Fasi, S.-I. Filip and M. Mikaitis, *Probabilistic Error Analysis of Limited-Precision Stochastic Rounding: Horner's Algorithm and Pairwise Summation*, arXiv:2603.24161, first publicly posted 2026-03-25. https://arxiv.org/html/2603.24161v1

[3] A. Fitzgibbon and S. Felix, *On Stochastic Rounding with Few Random Bits*, arXiv:2504.20634, first publicly posted 2025-04-29. https://arxiv.org/html/2504.20634v1

[4] *Stochastic rounding for memory-efficient digital simulation of synaptic plasticity using 8-bit floating-point*, 2025. DOI:10.1088/2634-4386/ae01d2. https://doi.org/10.1088/2634-4386/ae01d2
