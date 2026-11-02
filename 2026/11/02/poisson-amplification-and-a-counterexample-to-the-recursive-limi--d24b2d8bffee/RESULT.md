# Poisson amplification and a counterexample to the recursive-limit conjecture for counting modal logic

## Finding
Fix integers \(k\ge 1\) and \(t\ge 1\). On a complete rooted \(n\)-ary tree of depth two, give each vertex an independent uniform valuation of the \(2k\) propositional letters \(p_1,q_1,\ldots,p_k,q_k\). Let
\[
\psi_k := \bigwedge_{i=1}^{k}(\#p_i=\#q_i),\qquad
\varphi_{k,t}:=(\#\psi_k\ge t),\qquad
c_n:=\frac{\binom{2n}{n}}{4^n}.
\]
Here \(\#\chi\) counts the accessible children satisfying \(\chi\). Equality abbreviates the conjunction of both corresponding linear inequalities, so these are formulas in the counting-modal language \(K^{\#}\).

The **exact truth proportion** of \(\varphi_{k,t}\) is
\[
\mu_n^{\mathcal T}(\varphi_{k,t})=
\sum_{j=t}^{n}\binom{n}{j}c_n^{kj}(1-c_n^k)^{n-j}.
\]
For fixed \(k,t\), its limit is
\[
\lim_{n\to\infty}\mu_n^{\mathcal T}(\varphi_{k,t})=
\begin{cases}
1,&k=1,\\[2pt]
1-e^{-1/\pi}\displaystyle\sum_{j=0}^{t-1}\frac{(1/\pi)^j}{j!},&k=2,\\[6pt]
0,&k\ge3.
\end{cases}
\]
By contrast, the recursive limit obtained by first replacing each direct subformula probability by its limiting value (Definition 26 of Ghosh--Schwarzentruber) is
\[
\mu'_{\infty}(\varphi_{k,t})=0
\qquad\text{for every fixed }k,t\ge1.
\]
Consequently \(\varphi_{1,1}\) has an ordinary **convergent** truth proportion with limit \(1\), whereas its recursive limit equals \(0\). In the full-branching tree interpretation used in the paper's Section 6.1, this refutes its Conjecture 38, which says that the recursive limit must be an accumulation point of the ordinary proportions. The \(k=2\) regime is a nontrivial critical Poisson limit, with \(\Pr(\operatorname{Poi}(1/\pi)\ge1)=1-e^{-1/\pi}\approx0.272622650705\).

## Assumptions and scope
For each \(n\ge1\), the underlying directed Kripke frame is the complete rooted tree of height exactly two, each nonleaf having exactly \(n\) outgoing edges and each leaf none. The root is designated. The only randomly chosen objects are the valuations of the \(2k\) letters; at every vertex each letter is true with probability \(1/2\), independently across all letters and vertices. Fixed \(k\) and \(t\) do not vary with \(n\). The \(n\)-ary tree is not a random graph, nor is an ensemble of variable-degree trees being sampled.

The formulas are well formed in the syntax of arXiv:2610.26187v1: \(\#p_i=\#q_i\) means both \(\#p_i-\#q_i\ge0\) and \(\#q_i-\#p_i\ge0\), and \(\#\psi_k\ge t\) means \(\#\psi_k-t\ge0\). Boolean conjunction is a standard abbreviation. There are no independence assumptions between the truth values of \(p_i\) and \(q_i\) at different logical depths beyond the independent uniform valuation just specified.

## Proof
For a fixed child of the root and one pair of letters \((p_i,q_i)\), there are four equally likely truth assignments at each of the \(n\) grandchildren. The difference between the number of \(p_i\)-grandchildren and the number of \(q_i\)-grandchildren has probability generating Laurent polynomial
\[
\left(\frac{z^{-1}+2+z}{4}\right)^n
=4^{-n}z^{-n}(1+z)^{2n}.
\]
Its constant coefficient is exactly \(c_n=4^{-n}\binom{2n}{n}\). The \(k\) pairs have disjoint letters and are therefore independent, so a fixed child satisfies \(\psi_k\) with probability \(c_n^k\).

Distinct children depend on disjoint sets of grandchild valuations. Consequently the root's \(\psi_k\)-child count is exactly \(\operatorname{Bin}(n,c_n^k)\), proving the finite formula, including the empty tail when \(t>n\). Truth values at the root and at intermediate children do not affect this event, so their uniform valuation choices cancel from the proportion.

Stirling's formula gives
\[
c_n=\frac1{\sqrt{\pi n}}\left(1+O(n^{-1})\right),
\qquad nc_n^k=\pi^{-k/2}n^{1-k/2}(1+O(n^{-1})).
\]
For \(k=1\), the mean of the root count diverges and its variance is at most its mean; Chebyshev's inequality shows that the probability of fewer than any fixed \(t\) successes tends to zero. For \(k=2\), the success probability tends to zero and \(nc_n^2\to 1/\pi\); the ordinary binomial-to-Poisson theorem gives the asserted Poisson tail. For \(k\ge3\), the mean tends to zero, so Markov's inequality gives a vanishing upper tail. These establish every stated infinite-size limit.

At modal depth one, \(\mu_n^{\mathcal T}(\psi_k)=c_n^k\to0\). Definition 26's recursive limit first substitutes precisely this limiting probability into the distribution of the root's individual successors. Each successor then satisfies \(\psi_k\) with probability zero, so \(\mu'_n(\varphi_{k,t})=0\) for every \(n\ge1\) and \(t\ge1\), whence \(\mu'_{\infty}(\varphi_{k,t})=0\). At \(k=t=1\) the ordinary proportions converge to \(1\) and have only that accumulation point. Thus the recursive limit \(0\) is not an accumulation point, as claimed.

## Verification
The accompanying `checker.py` directly enumerates all four assignments of each propositional pair across \(n\le8\) grandchildren to reconstruct the central-binomial coefficient; it separately enumerates multiple disjoint pairs for specified \(k\le3,n\le4\), forms the root distribution by a separate child-by-child integer dynamic program, and directly enumerates all relevant leaves of several complete depth-two trees (through \(n=3,k=1\) and \(n=2,k=2\)). Exact rational threshold probabilities agree throughout. The script reports `ALL_CHECKS_OK`. This finite check is not the proof of the infinite asymptotic limits; their justification is the preceding Stirling/Poisson/Chebyshev/Markov argument.

To rerun: `python3 checker.py`. No nonstandard packages, external data, or hidden files are required.

## Relationship to prior work
Ghosh and Schwarzentruber (arXiv:2610.26187v1, October 19, 2026) introduce the counting-modal truth-proportion problem, provide a parity-dependent **nonconvergent** example in Section 6.1, and define the recursive alternative in Section 6.2. Conjecture 38 in Section 6.3 specifically asserts the accumulation-point relationship now contradicted by the present **convergent** example. Their Appendix A calculates the one-step central-binomial comparison count; that elementary ingredient is expressly credited here. The new statement is the iterated modal amplification law, its three regimes, and the negative comparison with Conjecture 38. General binomial-to-Poisson convergence is classical; the novelty claim is not the limit theorem alone.

Adam-Day, Benedikt, Ceylan, and Finkelshtein study asymptotically constant neural architectures on random graph models, not this exact fixed-degree complete-tree counting language or the recursive-limit conjecture. Related results on rare Bernoulli weak limits concern probability arrays without the nested modal formula or Conjecture 38. Searches did not establish a prior identical counterexample; they are not proof of historical uniqueness.

## Limitations
The theorem is scoped to complete \(n\)-ary depth-two trees with independent fair Boolean valuations, matching the fixed-branching experiment of the motivating paper's Section 6.1. Its results are not asserted for arbitrary random graph ensembles, variable-degree tree sampling conventions, dependent valuations, or a different meaning of the recursive-limit operation. The original paper's description of tree counting also discusses at-most-branching conventions elsewhere; this possible convention ambiguity is an explicit interpretation risk when applying the counterexample to the wording of Conjecture 38. The original formulas of Section 6.1 already feature rare balanced counts, so the degree of historical originality of the resulting amplification construction should receive independent scrutiny. No independent mathematical audit has been performed.

## References
1. A. Ghosh and F. Schwarzentruber, *On Counting Graphs for Modal Logic with Counting*, arXiv:2610.26187v1 (first posted October 19, 2026), especially Sections 3, 4, 6.1--6.3, 7 and Appendix A. https://arxiv.org/abs/2610.26187
2. S. Adam-Day, M. Benedikt, I. I. Ceylan and B. Finkelshtein, *Almost Surely Asymptotically Constant Graph Neural Networks*, arXiv:2403.03880 (2024), especially Sections 1, 2 and 5. https://arxiv.org/abs/2403.03880
3. The classical central-binomial Stirling asymptotic and binomial-to-Poisson limit, as standard probability results; no priority is claimed for them.
