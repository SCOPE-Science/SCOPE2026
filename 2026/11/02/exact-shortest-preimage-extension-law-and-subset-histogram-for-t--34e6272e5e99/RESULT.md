# Exact shortest preimage-extension law and subset histogram for the Černý automata

## Finding

For every integer \(n\ge 2\), every nonempty proper subset of the standard \(n\)-state Černý automaton has **exactly one shortest extending word**. Its length is the index of the first cyclic zero-to-one boundary in the subset's membership vector, plus one. The complete distribution of these minimum lengths is

\[
H_n(t)=\#\{S\subsetneq Q: S\ne\varnothing,\ \operatorname{minext}(S)=t\}
=\begin{cases}
t\,2^{n-t-1},&1\le t<n,\\
n-1,&t=n.
\end{cases}
\]

The \(n-1\) subsets that cannot be extended in \(n-1\) or fewer letters are **exactly** \(\{0,1,\ldots,k-1\}\) for \(1\le k<n\). In particular, among all \(2^n-2\) nonempty proper subsets, the obstructed proportion is \((n-1)/(2^n-2)\). Under uniform sampling of these subsets,

\[
\mathbb E[\operatorname{minext}(S)]
=\frac{3\cdot 2^n-3n-3}{2^n-2}\longrightarrow 3.
\]

For each fixed positive integer \(t\), the fraction having minimum extension length \(t\) tends to \(t/2^{t+1}\).

## Assumptions and scope

Let \(Q=\{0,1,\ldots,n-1\}\) and let the complete deterministic automaton have alphabet \(\{a,b\}\) with \(\delta(q,a)=q+1\pmod n\), \(\delta(0,b)=1\), and \(\delta(q,b)=q\) for \(1\le q<n\). A word acts left to right, so \(\delta(q,ba^j)=\delta(\delta(q,b),a^j)\). For any word \(u\) and subset \(S\), write

\[
S\cdot u^{-1}=\{q\in Q:\delta(q,u)\in S\},\qquad
\operatorname{minext}(S)=\min\{|u|:|S\cdot u^{-1}|>|S|\}.
\]

Only \(\varnothing\ne S\subsetneq Q\) is considered. Write \(s_i=1\) for \(i\in S\), otherwise \(s_i=0\), and read indices modulo \(n\). Define

\[
j(S)=\min\{j\in\{0,\ldots,n-1\}:s_j=0,\ s_{j+1\bmod n}=1\}.
\]

Such a boundary exists because \(S\) is nonempty and proper. The individual formula is

\[
\operatorname{minext}(S)=j(S)+1,
\qquad\text{and the unique shortest extending word is }ba^{j(S)}.
\]

The automaton's state labels and alphabet labels are fixed; no quotient under relabeling is used.

## Proof

**1. Inverse actions.** Let \(A(U)=U\cdot a^{-1}\) and \(B(U)=U\cdot b^{-1}\). The map \(A\) shifts the membership vector one place cyclically and preserves cardinality. Directly from \(b(0)=1\) and the other fixed points,

\[
B(U)=\begin{cases}
U\cup\{0\},&1\in U,\ 0\notin U,\\
U\setminus\{0\},&0\in U,\ 1\notin U,\\
U,&\text{otherwise}.
\end{cases}
\]

In particular, \(B(U)\) either contains \(U\), equals \(U\), or is contained in \(U\). Every inverse-letter map is inclusion-monotone: \(U\subseteq V\) implies \(A(U)\subseteq A(V)\) and \(B(U)\subseteq B(V)\).

**2. A shortest extension has just one final growth step.** Read the inverse images for a candidate word from **last letter to first letter**. Let the sequence of inverse letters for a shortest extending word start with \(j\) applications of \(A\) followed by its first \(B\). If that \(B\) does not increase the current set, its output is a subset of the current set. Removing this inverse \(B\) and applying the remaining inverse operations produces a final superset by inclusion-monotonicity, hence still an extension with fewer letters. This contradicts shortestness. Thus this first \(B\) increases the set. Since all preceding \(A\)'s preserve size, the shortest sequence must terminate at this \(B\); otherwise its initial segment already extends \(S\). Every shortest extending word therefore has the form \(ba^j\), with \(j\ge0\). Inverse rotation has period \(n\), so a shortest such word has \(0\le j<n\).

**3. Boundary and uniqueness.** The set \(A^j(S)\) contains state 1 but not state 0 precisely when \(s_{j+1\bmod n}=1\) and \(s_j=0\). By step 1 this is exactly when \(B\) increases its size. Therefore the least eligible \(j\) is \(j(S)\), the shortest length is \(j(S)+1\), and the preceding argument forces the single word \(ba^{j(S)}\). This proves both the individual formula and uniqueness.

**4. Histogram.** For \(0\le j<n-1\), the first zero-to-one boundary occurs at \(j\) exactly when \(s_{j+1}=1\), \(s_j=0\), and the prefix \(s_0s_1\cdots s_j\) has no earlier zero-to-one transition. Such a prefix is \(1^k0^{j+1-k}\) for exactly \(j+1\) choices \(k=0,1,\ldots,j\), with \(n-j-2\) completely free subsequent bits. Thus

\[
\#\{S:j(S)=j\}=(j+1)2^{n-j-2}.
\]

The remaining case \(j=n-1\) has no zero-to-one transition in the linear string \(s_0\cdots s_{n-1}\), but has the closing cyclic boundary \(s_{n-1}=0,s_0=1\). Its members are exactly \(1^k0^{n-k}\) for \(1\le k<n\), giving \(n-1\) subsets and the stated obstruction classification. Substituting \(t=j+1\) proves \(H_n(t)\).

**5. Mean and limiting distribution.** The histogram has total \(2^n-2\), and finite geometric summation gives

\[
\sum_{t=1}^{n-1}t^2 2^{n-t-1}+n(n-1)
=3\cdot 2^n-3n-3.
\]

Division by \(2^n-2\) gives the mean. For fixed \(t<n\), dividing \(t2^{n-t-1}\) by \(2^n-2\) and letting \(n\) grow gives \(t/2^{t+1}\). This completes the proof for all \(n\ge2\).

## Verification

The self-contained standard-library program `verify.py` checks three separate finite encodings. For every \(2\le n\le13\), it runs shortest-path breadth-first search on all nontrivial inverse-subset states and checks each individual boundary formula, the entire histogram and the precise stuck subsets. For \(2\le n\le8\), it also enumerates forward action maps of every word through length \(n\), independently reconstructs each shortest expanding word and verifies **uniqueness**. The saved `verification_output.txt` ends with `VERIFY_OK`. These finite checks corroborate the separate all-parameter proof; they are not used to infer the infinite statement.

## Relationship to prior work

Miccinesi's 2026 work [1] defines \(\operatorname{minext}\), supplies general per-subset sufficient extension certificates, explicitly identifies the two stuck subsets of the three-state Černý automaton in Example 1, and notes in Section 8.1 that some such subsets obstruct the \(n-1\) extension bound for all \(n\). The present result goes beyond these statements by deriving **the exact shortest word for every subset**, the complete all-size histogram, and a classification of all obstructions. Its argument does not follow from the sign of that certificate without a separate analysis of the subset transitions.

Berlinkov, Ferens and Szykuła [2,3] study the general computational complexity of extending a subset and illustrate the four-state Černý automaton. Their preimage-decision and complexity results do not assert the present all-parameter Černý histogram or unique-word rule. Previously described Černý rank-compression and avoiding-set thresholds likewise concern different quantifiers: total-image rank or avoidance of prescribed states, rather than growing the preimage of **every** prescribed subset.

## Limitations

The result applies only to the stated labeled binary Černý automata, not arbitrary synchronizing automata, arbitrary rank-one perturbations of permutations, or weighted words. It concerns the **first** increase in inverse-image cardinality; it does not bound the length of a whole chain of extensions or improve general reset thresholds. A covering unindexed earlier computation or different presentation of the same cyclic-boundary rule remains a publication-priority risk. The proof and checks are not an independent mathematical audit.

## References

1. M. Miccinesi, *Certificates for short extending words in a finite automaton*, arXiv:2609.21603, first posted 2026-09-18. https://arxiv.org/abs/2609.21603
2. M. V. Berlinkov, R. Ferens and M. Szykuła, *Preimage problems for deterministic finite automata*, arXiv:1704.08233, first posted 2017-04-26, version 4 (2020). https://arxiv.org/html/1704.08233v4
3. M. V. Berlinkov, R. Ferens and M. Szykuła, *Complexity of Preimage Problems for Deterministic Finite Automata*, MFCS 2018, LIPIcs 117, article 32. https://doi.org/10.4230/LIPIcs.MFCS.2018.32
