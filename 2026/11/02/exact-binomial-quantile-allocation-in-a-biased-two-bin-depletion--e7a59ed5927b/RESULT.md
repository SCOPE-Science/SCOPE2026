# Exact binomial-quantile allocation in a biased two-bin depletion race

## Finding
For each integer \(n\ge2\), each probability \(p\in(0,1)\), and each integer allocation \(0\le a\le n\), put \(q=1-p\). Initially, bin 1 contains \(a\) balls and bin 2 contains \(n-a\) balls. While both bins are nonempty, remove one ball from bin 1 with probability \(p\), and from bin 2 with probability \(q\), independently from round to round. Stop as soon as at most one bin remains nonempty. Let \(R_{n,p}(a)\) be the number of balls left, and set \(f_{n,p}(a)=\mathbb E R_{n,p}(a)\).

For \(B\sim\operatorname{Bin}(n,p)\), the following finite-size identities hold, including allocations with one initially empty bin:
\[
f_{n,p}(a)=\frac{\mathbb E(a-B)_+}{q}+\frac{\mathbb E(B-a)_+}{p},
\qquad 0\le a\le n,
\]
\[
f_{n,p}(a+1)-f_{n,p}(a)
=\frac{\Pr(B\le a)-q}{pq},\qquad 0\le a<n.
\]
Here \(x_+=\max(x,0)\). The finite objective is strictly discretely convex: its consecutive slopes increase by \(\Pr(B=a+1)/(pq)>0\).

Let \(a_n=\min\{a:\Pr(B\le a)\ge q\}\). This integer is always between \(1\) and \(n-1\), and it is a global minimizer. It is the only minimizer unless \(\Pr(B\le a_n)=q\), in which case exactly \(a_n\) and \(a_n+1\) minimize the expected remainder.

For every fixed \(p\in(0,1)\), let \(z_p=\Phi^{-1}(q)\), where \(\Phi\) and \(\phi\) denote the standard normal distribution function and density. Then
\[
a_n=np+\sqrt{npq}\,z_p+O_p(1),
\qquad
\min_{0\le a\le n}f_{n,p}(a)
\sim\phi(z_p)\sqrt{\frac{n}{pq}}.
\]
In particular, for \(p>1/2\), the optimal bin-1 allocation is asymptotically **below** the proportional allocation \(np\) by an order-\(\sqrt n\) amount.

## Assumptions and scope
The probabilities are constant throughout the removal race and do not depend on the current occupancies, except that the process terminates when one bin empties. The draws are independent. The total initial inventory \(n\) is an integer at least two. The exact optimization result allows arbitrary \(p\in(0,1)\) and all integer splits, including degenerate endpoints. The asymptotic formula fixes \(p\) as \(n\to\infty\); no uniform assertion is made as \(p\) approaches zero or one with \(n\).

## Proof
**1. A stopped-sequence identity.** Generate an infinite independent sequence of bin labels, with label 1 having probability \(p\), and consider its first \(n\) terms. For a given allocation let \(T\) be the first time a bin empties (take \(T=0\) for an already empty bin), and let \(R=n-T\). Up to time \(T\), every selection removes exactly one ball, so \(R\) is the terminal remainder. Set \(B\) equal to the number of label-1 selections among the first \(n\) terms; thus \(B\sim\operatorname{Bin}(n,p)\).

On the event that bin 1 survives, its first \(T\) selections number \(a-R\), while bin 2 has received exactly \(n-a\) selections. Therefore \((a-B)_+\) equals the number of label-2 selections between \(T+1\) and \(n\), and \((B-a)_+=0\). Conditional on the stopped history, the expected number of those label-2 selections is \(qR\). Conversely, on the event that bin 2 survives, \((B-a)_+\) equals the number of label-1 selections from \(T+1\) through \(n\), of conditional expectation \(pR\), and \((a-B)_+=0\). These assertions also apply when a bin is empty initially. The strong Markov property for the independent label sequence, with bounded \(T\), gives
\[
\mathbb E(a-B)_+=q\,\mathbb E[R\mathbf1_{\{\text{bin 1 survives}\}}],\qquad
\mathbb E(B-a)_+=p\,\mathbb E[R\mathbf1_{\{\text{bin 2 survives}\}}].
\]
The survival events partition the outcomes. Adding the corresponding expectations after dividing by \(q\) and \(p\) proves the first identity.

**2. Exact optimizer.** Increasing \(a\) by one changes \((a-B)_+\) by \(\mathbf1_{\{B\le a\}}\), and changes \((B-a)_+\) by \(-\mathbf1_{\{B\ge a+1\}}\). Taking expectations yields
\[
\Delta f_{n,p}(a)
=\frac{\Pr(B\le a)}q-\frac{1-\Pr(B\le a)}p
=\frac{\Pr(B\le a)-q}{pq}.
\]
Every binomial atom is positive because \(0<p<1\). Hence the slopes are strictly increasing. Their sign changes at the first integer \(a_n\) with \(\Pr(B\le a_n)\ge q\). Moreover, \(\Pr(B=0)=q^n<q\) and \(\Pr(B\le n-1)=1-p^n>q\), proving \(1\le a_n\le n-1\) and the claimed characterization of all minimizers, including the possible adjacent tie.

**3. Asymptotic allocation and remainder.** Write \(\sigma_n=\sqrt{npq}\) and \(Z_n=(B-np)/\sigma_n\). The Berry–Esseen inequality for the fixed-parameter binomial law gives a uniform CDF error of order \(n^{-1/2}\) from \(\Phi\). Because \(\phi(z_p)>0\) and the binomial CDF crosses \(q\) at \(a_n\), comparing the CDF at the integers nearest \(np+\sigma_n z_p\pm K\), with fixed sufficiently large \(K\), gives \(a_n=np+\sigma_n z_p+O_p(1)\).

Consequently \(z_n=(a_n-np)/\sigma_n\to z_p\). The central limit theorem gives \(Z_n\Rightarrow Z\sim N(0,1)\). Since \(\mathbb EZ_n^2=1\) and \((z_n)\) is bounded, the two positive-part families are uniformly integrable. Divide the exact remainder identity by \(\sigma_n\) and pass to the limit:
\[
\frac{f_{n,p}(a_n)}{\sigma_n}
\longrightarrow
\frac{\mathbb E(z_p-Z)_+}{q}+
\frac{\mathbb E(Z-z_p)_+}{p}.
\]
The Gaussian truncated-moment formulas give \(\mathbb E(z_p-Z)_+=z_p\Phi(z_p)+\phi(z_p)\) and \(\mathbb E(Z-z_p)_+=\phi(z_p)-z_p[1-\Phi(z_p)]\). Since \(\Phi(z_p)=q\), the \(z_p\) terms cancel and the remaining value is \(\phi(z_p)/(pq)\). Multiplying by \(\sigma_n\) gives the announced asymptotic minimal remainder.

## Verification
The standalone standard-library script `verify.py` evaluates the exact two-bin Markov recurrence in rational arithmetic and independently compares it with the binomial positive-part identity, its finite differences, and every candidate minimizer. It reports 7,074 passed exact-rational assertions across eight rational selection probabilities and inventories from two through 27. The published example with \(n=6\) and \(p=5/6\) is recovered: the optimal split is \((4,2)\), with expected remainder \(139/81\), whereas split \((5,1)\) yields \(3125/1296\). These finite checks corroborate, but do not constitute, the proof for all \(n\) and all real \(p\).

## Relationship to prior work
Correa, Kiwi, Livanos, E. Solan and R. Solan, *About a ball removal process on bins* (arXiv:2602.12523, first posted 13 February 2026), prove balanced allocation under equal selection probabilities for any number of bins. Their section on nonuniform selection provides the particular \(n=6\), \(p=5/6\) counterexample; it does not give an all-size, all-bias optimizer characterization. Zhou, Wang and Zhang, *Optimal Inventory Allocation for Indifferent Goods Under Dynamic Substitution* (Operations Research 74, 2026), treat the symmetric terminating inventory problem and related multinomial-logit variants. Their publicly accessible abstract does not assert the biased two-bin stopping-time identity or its binomial-quantile optimizer; their full paper was not inspected and remains a historical-priority uncertainty. The critical-fractile rule for asymmetric absolute loss is classical; the contribution here is the exact representation of the stopped deletion process as that loss, followed by its finite and asymptotic consequences.

## Limitations
The result concerns exactly two competing bins with fixed probabilities, not an arbitrary number of bins or state-dependent selection probabilities. The asymptotic expansion assumes \(p\) stays fixed strictly between zero and one. The proof is self-contained apart from standard binomial central-limit and Berry–Esseen estimates. Exhaustive checks are finite and do not replace the proof. The historical relation to a related publisher article is limited by inaccessible full text.

## References
- J. Correa, M. Kiwi, V. Livanos, E. Solan, R. Solan, *About a ball removal process on bins*, arXiv:2602.12523v2 (2026), https://arxiv.org/html/2602.12523v2; initial public version 13 February 2026, https://arxiv.org/abs/2602.12523.
- Z. Zhou, T. Wang, J. Zhang, *Optimal Inventory Allocation for Indifferent Goods Under Dynamic Substitution*, Operations Research 74(4), 2001–2012 (2026), https://doi.org/10.1287/opre.2025.2228.
- Classical binomial central limit theorem, Berry–Esseen inequality, and asymmetric absolute-loss (newsvendor critical-fractile) quantile principle; used only as standard probability tools after the exact reduction.
