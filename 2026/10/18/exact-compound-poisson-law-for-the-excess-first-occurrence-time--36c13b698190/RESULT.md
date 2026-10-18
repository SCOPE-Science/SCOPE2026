# Exact compound-Poisson law for the excess first-occurrence time of every iid word

## Finding
Let \(w\) be any nonempty finite word of length \(m\) over a finite alphabet, with positive probability \(p_w\) under an iid letter source. If \(T_w\) is the completion time of its first appearance, then the **excess waiting time** \(Y_w=T_w-m\) is compound Poisson, even when \(w\) has self-overlap or the letters have unequal probabilities. Let \(A\) be the substochastic prefix-matching transition matrix defined below. For \(k\ge1\), put
\[
\nu_k=\frac{\operatorname{tr}(A^k)}{k}\ge0.
\]
Then the full law is
\[
\mathbb E[z^{Y_w}]=\frac{p_w}{\det(I-zA)}
=\exp\!\left(\sum_{k\ge1}\nu_k(z^k-1)\right),\qquad |z|\le1.
\]
The total jump intensity satisfies \(\sum_{k\ge1}\nu_k=-\log p_w\). For \(0<p_w<1\), take a Poisson number \(N\) of jumps with mean \(-\log p_w\) and iid positive-integer jump sizes \(J\) with \(\Pr(J=k)=\nu_k/(-\log p_w)\); then \(Y_w\overset d=\sum_{i=1}^{N}J_i\). For \(p_w=1\), \(Y_w=0\) almost surely and the jump intensity is zero. In particular, the excess waiting-time law is infinitely divisible on the nonnegative integers; all of its ordinary cumulants are \(\kappa_r=\sum_{k\ge1}k^r\nu_k\ge0\) for \(r\ge1\).

## Assumptions and scope
Fix a finite alphabet \(\Sigma\), an arbitrary probability vector \((\pi_a)_{a\in\Sigma}\), and iid letters \(X_1,X_2,\ldots\). Fix a word \(w=(w_1,\ldots,w_m)\in\Sigma^m\), with \(m\ge1\) and \(p_w=\prod_{i=1}^m\pi_{w_i}>0\). Define \(T_w=\min\{t\ge m:(X_{t-m+1},\ldots,X_t)=w\}\). Only the letters appearing in \(w\) must have positive probability; others can have zero probability. Overlaps are unrestricted.

The prefix-matching automaton has transient states \(0,1,\ldots,m-1\): after processing observations without a completed occurrence, state \(i\) is the length of the longest prefix of \(w\) matching the observed suffix. On reading letter \(a\), update to the longest prefix of \(w\) that is a suffix of the extended observations, or absorb upon completing \(w\). Define \(A_{ij}\) as the total \(\pi\)-probability of transitions \(i\to j\) without absorption. The matrix \(A\) is a nonnegative \(m\times m\) substochastic matrix. Its entries are computable by finite prefix/suffix comparisons and do not involve an infinite search.

## Proof
**Step 1 (upper-Hessenberg structure).** Appending one letter can extend the current longest matched prefix by at most one. Hence \(A_{ij}=0\) if \(j>i+1\). Moreover, for \(0\le i<m-1\), a transition from \(i\) to \(i+1\) occurs exactly when the next letter is \(w_{i+1}\); thus \(A_{i,i+1}=\pi_{w_{i+1}}\). Absorption requires state \(m-1\) and next letter \(w_m\), with probability \(\pi_{w_m}\). These statements hold for words with borders, because the automaton records the longest matching prefix.

**Step 2 (rational generating function).** For \(|z|<1\), the first-occurrence generating function is
\[
\mathbb E[z^{T_w}]=z\pi_{w_m}\,e_0^{\mathsf T}(I-zA)^{-1}e_{m-1}.
\]
By the adjugate formula, the indicated inverse entry is the signed minor obtained by deleting row \(m-1\) and column \(0\) of \(I-zA\), divided by \(\det(I-zA)\). This minor is lower triangular: its diagonal consists of \(-z\pi_{w_1},\ldots,-z\pi_{w_{m-1}}\). The cofactor sign cancels those minus signs, giving
\[
 e_0^{\mathsf T}(I-zA)^{-1}e_{m-1}
=\frac{z^{m-1}\prod_{i=1}^{m-1}\pi_{w_i}}{\det(I-zA)}.
\]
The empty product convention makes the same identity valid for \(m=1\). Consequently \(\mathbb E[z^{T_w-m}]=p_w/\det(I-zA)\).

**Step 3 (transience and normalization).** Whatever the current nonabsorbing prefix state, the next \(m\) iid letters equal \(w\) with probability \(p_w\), which forces absorption no later than those \(m\) letters. Thus \(\|A^{m}\|_{\infty}\le1-p_w<1\), whence \(\rho(A)<1\). Absorption occurs almost surely; letting \(z\uparrow1\) in the preceding probability-generating function proves \(\det(I-A)=p_w>0\).

**Step 4 (exact nonnegative Lévy masses).** Because \(\rho(A)<1\), the matrix logarithm/determinant power-series identity converges absolutely for \(|z|\le1\):
\[
-\log\det(I-zA)=\sum_{k\ge1}\frac{\operatorname{tr}(A^k)}{k}z^k.
\]
Every diagonal entry of \(A^k\) is nonnegative, so \(\nu_k=\operatorname{tr}(A^k)/k\ge0\). At \(z=1\), the preceding identity and \(\det(I-A)=p_w\) give \(\sum_{k\ge1}\nu_k=-\log p_w<\infty\). Subtracting this finite constant from the logarithmic generating function yields the displayed compound-Poisson representation. The limiting deterministic case \(p_w=1\) has \(A\) nilpotent with zero traces and no jumps. For any \(r\ge1\), exponential decay of \(A^k\) justifies termwise differentiation of the cumulant generating function at zero and gives \(\kappa_r=\sum_{k\ge1}k^r\nu_k\).

## Verification
The supplied standalone Python checker uses exact rational arithmetic and no external packages. Run `python3 word_wait_checker.py`. It constructs independent prefix automata for \(498\) words (including overlapping patterns and unequal three-letter frequencies), checks \(7968\) determinant-coefficient identities, \(7470\) finite nonnegative matrix-trace calculations, and \(365\) independently brute-enumerated first-occurrence probabilities. Example: for the pattern `HTH`, with \(\Pr(H)=2/5\), the first six positive jump masses are \(1,13/50,89/375,457/2500,397/3125,1757/18750\). These tests corroborate, but do not replace, the proof for all finite alphabets, positive pattern probabilities and finite word lengths.

## Relationship to prior work
Oh, Park and Kim (2022, arXiv:2210.08797), especially their independent-Bernoulli probability-generating-function section, derive recurrences and rational generating functions for repeated-success runs; those words form a restricted subfamily of the present theorem. Johnson and Fu (2014) use finite Markov-chain embeddings to study distributions and compound-Poisson **approximations for counts of pattern occurrences**; their stated theorems do not assert an exact compound-Poisson decomposition of the excess first-occurrence waiting time for every fixed word. Sankaran and Midhu (2010) develop a full pattern-waiting-time Markov embedding, including its one-superdiagonal structure and exact first-hit calculations; the author-uploaded full-text sections 2–4 and Appendix give numerical algorithms and expectations but no exact compound-Poisson representation or nonnegative logarithmic trace statement. The automaton embedding is standard; the contribution here is the universal exact jump-mass and infinite-divisibility theorem obtained from its special upper-Hessenberg structure.

## Limitations
The theorem concerns first completion of one specified word under an iid **finite-alphabet** source. It does not claim the corresponding theorem for a union of words, Markov-dependent letters, an arbitrary absorbing finite-state chain, or a count of occurrences. The discrete Lévy masses are given implicitly but exactly by matrix traces and are not claimed to have a closed form for every pattern. The prior-work survey may miss older terminology for the same all-word compound-Poisson representation, including unexamined historical pattern-generating-function papers; human literature assessment remains desirable. Self-review does not constitute independent validation.

## References
1. Jungtaek Oh, Chongjin Park and Sungsu Kim, *Recurrence algorithms of waiting time for the success run of length k in relation to generalized Fibonacci sequences*, arXiv:2210.08797 (first posted 2022-10-17), https://arxiv.org/abs/2210.08797.
2. Brad C. Johnson and James C. Fu, *Approximating the distributions of runs and patterns*, Journal of Statistical Distributions and Applications **1**, 5 (2014), DOI:10.1186/2195-5832-1-5, https://doi.org/10.1186/2195-5832-1-5.
3. P. G. Sankaran and N. N. Midhu, *On waiting time distributions for patterns in a sequence of multistate trials*, Statistics & Probability Letters **80** (2010), 1798–1805, DOI:10.1016/j.spl.2010.08.004, https://doi.org/10.1016/j.spl.2010.08.004.
