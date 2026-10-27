# Exact nineteen-value spatial image entropy spectrum of elementary cellular automata

## Finding
For each Wolfram elementary binary rule \(r\in\{0,1,\ldots,255\}\), let \(F_r\) act on bilateral binary configurations and let \(Y_r=F_r(\{0,1\}^{\mathbb Z})\) be its **one-step spatial image**. For \(n\geq0\), let \(a_r(n)\) be the number of length-\(n\) words appearing in \(Y_r\), with \(a_r(0)=1\). Define \(\lambda_r=\lim_{n\to\infty}a_r(n)^{1/n}\) and \(h_r=\log\lambda_r\). These limits exist.

**The exact spectrum consists of nineteen distinct logarithms of algebraic Perron roots.** The table below records their order from largest to smallest, the number of rules realizing each value, an example, and a rational isolating interval for \(\lambda_r\). The interval column is displayed decimally only for readability; the two integer endpoints over \(10^9\) are in `entropy_spectrum.csv`. Each value is uniquely determined as the root in its interval of the displayed irreducible polynomial in that CSV. The companion `rule_catalog.csv` gives the full assignment for every rule.

| Class | Number of rules | Example rule | Root \(\lambda\), approximate |
|:--:|--:|--:|--:|
| 0 | 30 | 15 | 2.000000000 |
| 1 | 4 | 22 | 1.917168419 |
| 2 | 4 | 37 | 1.915259447 |
| 3 | 8 | 62 | 1.897179401 |
| 4 | 8 | 25 | 1.891598683 |
| 5 | 4 | 57 | 1.890385778 |
| 6 | 8 | 41 | 1.889697432 |
| 7 | 8 | 26 | 1.886527045 |
| 8 | 4 | 73 | 1.886499639 |
| 9 | 4 | 94 | 1.882618724 |
| 10 | 28 | 7 | 1.866760399 |
| 11 | 44 | 14 | 1.839286755 |
| 12 | 16 | 13 | 1.784598933 |
| 13 | 8 | 6 | 1.772330223 |
| 14 | 8 | 9 | 1.764131372 |
| 15 | 32 | 3 | 1.754877666 |
| 16 | 28 | 1 | 1.618033989 |
| 17 | 8 | 2 | 1.465571232 |
| 18 | 2 | 0 | 1.000000000 |

Exactly 30 rules have the full spatial-image entropy \(\log 2\), hence are surjective. Exactly two rules (0 and 255) have zero spatial-image entropy. Among the remaining 224 rules, the **largest proper-image entropy** is achieved precisely by

\[
\boxed{r\in\{22,104,151,233\}}.
\]

For these four rules, \(h_r=\log\lambda_*\), where \(\lambda_*=1.9171684191613876\ldots\) is the largest real root of

\[
\begin{aligned}
P_*(z)={}&z^{13}-3z^{12}+2z^{11}-2z^{10}+6z^9-3z^8\\
&-5z^7+10z^6-5z^5-3z^4+6z^3-2z^2+2.
\end{aligned}
\]

In particular, \(h_r\approx0.650849315792010\) for these extremizers. The **second-highest** proper-image entropy occurs precisely for rules \(37,91,164,218\), with Perron root \(1.915259446764830\ldots\). All remaining proper images have strictly smaller entropy; thus the extremizer classification is sharp. The full-shift-versus-proper-image entropy gap is \(\log(2/\lambda_*)\approx0.042297864767936\).

## Assumptions and scope
An elementary rule uses the usual Wolfram convention: for three input bits \((u,v,w)\), set \(j=4u+2v+w\); the output is the binary digit of \(r\) at position \(j\) (least significant position numbered zero). Thus \((F_rx)_i=f_r(x_{i-1},x_i,x_{i+1})\). The source is the **entire** two-sided binary full shift, with no periodic boundary restriction and no stochastic assumptions. The entropy is that of spatial translation restricted to the **single-step image** \(Y_r\), not the entropy of the temporal map \(F_r\). The logarithm is natural. All class assignments, rule counts, and isolating intervals are exact.

## Proof
**Step 1: A right-resolving presentation of the image language.** Use four input-pair states \(s\in\{0,1,2,3\}\). Appending \(b\in\{0,1\}\) to the pair \(s\) gives the input triple indexed by \(j=2s+b\), the new pair state \(j\bmod4\), and output label \(f_r(j)\). A length-\(n\) output word is realized on the full bilateral shift if and only if it labels a path of length \(n\) in this four-state graph: the forward implication is local, and a finite input block of length \(n+2\) generating that word extends arbitrarily in both directions.

**Step 2: Determinization and exact counting.** Represent a subset of the four pair states by its four-bit mask \(S\). For output label \(a\), let

\[
\Delta_r(S,a)=\{(2s+b)\bmod4:\ s\in S,\ b\in\{0,1\},\ f_r(2s+b)=a\}.
\]

Start from the full mask \(15\) and retain exactly the reachable **nonempty** masks; there are at most 15. The deterministic transition on output symbol \(a\) goes to \(\Delta_r(S,a)\) when nonempty. Every retained state is accepting. Let \(A_r\) be the nonnegative integer adjacency matrix on these masks, where the entry from \(S\) to \(T\) counts the output letters \(a\in\{0,1\}\) for which \(\Delta_r(S,a)=T\). Writing \(e_0\) for the initial-state unit vector and \(\boldsymbol1\) for the all-ones vector yields the **exact identity**

\[
 a_r(n)=e_0^{\mathsf T}A_r^n\boldsymbol1\qquad(n\ge0).
\]

Every state of \(A_r\) is reachable from the start and accepting. Consequently, each recurrent component contributing the maximal spectral radius contributes nontrivially to the word-growth rate; Perron–Frobenius theory yields \(\lambda_r=\rho(A_r)\). In particular \(h_r=\log\rho(A_r)\). Every row sum is at most two, hence \(\rho(A_r)\le2\).

**Step 3: Exhaustive finite exact certificate.** The finite input consists of all 256 integers \(r\). For each, construct \(A_r\) by the preceding formula and compute \(p_r(z)=\det(zI-A_r)\) **exactly over the integers**. Apply exact Sturm real-root counting to certify that \(p_r\) has a positive real zero in exactly one of the nineteen disjoint rational intervals of `entropy_spectrum.csv`, and has **no positive real zero** between that interval's upper endpoint and 3. The Perron–Frobenius eigenvalue is real and positive and at most 2, so the isolated zero is necessarily \(\rho(A_r)\). Verify that the irreducible polynomial \(P_k\) displayed for the assigned class divides \(p_r\) over \(\mathbb Q[z]\) and has exactly one zero in that interval. Counting the members gives exactly the table above; all 19 intervals are disjoint, so there are exactly 19 values, not merely at most 19. The class-1 members are exactly \(22,104,151,233\), and class 2 contains exactly \(37,91,164,218\). These steps are implemented in the complete standalone `verify.py` and produce the two included CSV tables, with no floating-point decisions.

**Step 4: Equality with full entropy.** If the image is the full binary shift then every word appears and \(h_r=\log2\). Conversely, if the image omits a binary word of length \(m\), then the \(\lfloor n/m\rfloor\) disjoint blocks of length \(m\) within a length-\(n\) admissible word each have at most \(2^m-1\) possibilities, yielding \(h_r\le \log(2^m-1)/m<\log2\). Thus class 0 consists precisely of the surjective rules. The exact ordering of the remaining classes establishes the sharp extremal statement.

## Verification
Run `python3 verify.py` in the directory containing `verify.py`, `entropy_spectrum.csv`, and `rule_catalog.csv` (requires SymPy). It recomputes all 256 reachable subset matrices, their exact characteristic polynomials, exact Sturm root isolations, and polynomial divisibility for every class. It also independently enumerates **all** \(2^{n+2}\) input blocks and compares the resulting sets of output words with the matrix formula for each rule and all \(0\le n\le8\), totaling 2,304 direct count comparisons. Finally, it regenerates and byte-compares both included CSV files. This exhaustive finite computation certifies the classification of the complete 256-rule family; the infinite-word entropy step uses the general matrix-growth argument and is not inferred from the finite block tests.

## Relationship to prior work
Li and Packard (1990) classify structural and mean-field properties of the elementary rule space, rather than the exact entropy spectrum of the one-step image subshifts. Schüle and Stoop (2011 preprint, 2012 journal) classify topological-dynamical properties including sensitivity, surjectivity and chaoticity; this does not supply the nineteen exact proper-image entropy values or their extremizers. The general entropy-preservation and Garden-of-Eden theorems reviewed by Kari and Taati (2015) explain the full-entropy case, but not the proper-image values. Martínez and collaborators (2019 journal, 2020 preprint) develop the de Bruijn/subset diagrams for Rule 22 and list forbidden patterns, providing directly relevant graph methodology; their inspected Garden-of-Eden section does not evaluate the all-rule image entropy spectrum or establish Rule 22's sharp cross-rule entropy extremality. The novelty claim is **the evaluated exact spectrum, complete assignment, and extremal ordering**, not the general finite-automaton technique.

## Limitations
This theorem does not classify time-iterated images, limit sets, temporal dynamical entropy, invariant measures, or finite-ring orbit entropies. The class polynomials and root intervals are certified by the included exact finite computation, which requires an installation of SymPy for replay. The fact that an inspected collection of relevant papers does not contain the same evaluated classification does not establish exhaustive historical priority; an unindexed earlier table or equivalent computation remains possible. The work has undergone self-review only; independent audit has not been performed.

## References
1. W. Li and N. Packard, "The Structure of the Elementary Cellular Automata Rule Space," *Complex Systems* 4 (1990), 281–297. https://content.wolfram.com/sites/13/2018/02/04-3-3.pdf
2. M. Schüle and R. Stoop, "A Full Computation-relevant Topological Dynamics Classification of Elementary Cellular Automata," arXiv:1107.2080, first posted 2011-07-11; *Chaos* 22 (2012), 043143. https://arxiv.org/abs/1107.2080
3. J. Kari and S. Taati, "Statistical Mechanics of Surjective Cellular Automata," *Journal of Statistical Physics* (2015), doi:10.1007/s10955-015-1281-2. https://link.springer.com/article/10.1007/s10955-015-1281-2
4. G. J. Martínez, A. Adamatzky, R. Hoffmann, D. Désérable, and I. Zelinka, "On Patterns and Dynamics of Rule 22 Cellular Automaton," *Complex Systems* 28 (2019), 125–174; arXiv:2005.01480 (2020). https://arxiv.org/html/2005.01480v1
