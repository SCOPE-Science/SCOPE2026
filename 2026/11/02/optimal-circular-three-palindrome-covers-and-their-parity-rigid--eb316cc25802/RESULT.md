# Optimal circular three-palindrome covers and their parity-rigid adjacency profiles

## Finding

For every alphabet size \(q\ge 2\), let \(\mathcal P_q=\{aba:a,b\in\{0,\ldots,q-1\}\}\) be the \(q^2\) three-letter palindromes, including the constant words. A cyclic word \(W=(w_i)_{i\in\mathbb Z/L\mathbb Z}\) **covers** \(\mathcal P_q\) when every member occurs as \(w_iw_{i+1}w_{i+2}\) for some cyclic starting position \(i\). Additional factors are permitted.

**Theorem (exact minimum and rigid optimum profiles).** The minimum possible cyclic length is
\[
L_q=\frac{3q^2+q}{2}+\begin{cases}0,&q\text{ odd},\\q/2,&q\text{ even}.\end{cases}
\]
Write \(m_{ab}(W)\) for the number of cyclic adjacent pairs whose *unordered* symbols are \(\{a,b\}\), with \(m_{aa}\) counting loops. A covering word is length-optimal if and only if its unordered adjacency multiplicities obey the following conditions:

* If \(q\) is odd, every \(m_{aa}=2\) and every \(m_{ab}=3\) for \(a\ne b\).
* If \(q\) is even, every \(m_{aa}=2\), and the pairs with \(m_{ab}=4\) form a perfect matching on the alphabet; all other distinct-symbol pairs have \(m_{ab}=3\).

Here the converse is stated **among covering words**; the multiplicity conditions by themselves do not imply the required palindrome coverage. All the optimal multiplicity profiles listed above are realized. In particular, the optimum lengths for \(q=2,3,4,5,6\) are \(8,15,28,40,60\).

## Assumptions and scope

All alphabet symbols are distinct labels; \(q\) is an arbitrary integer at least two. A cyclic word of length \(L\) has exactly \(L\) length-three windows, including windows crossing the boundary. Coverage means at least one occurrence per required palindrome, without restriction on unwanted windows. The theorem does not concern non-cyclic shortest superstrings, maximum distinct palindromic factors, or universal cycles that forbid extra windows. The alphabet has no adjacency restrictions.

The symbols in \(\mathcal P_q\) are *ordered* (so \(aba\) and \(bab\) are both required when \(a\ne b\)), whereas \(m_{ab}\) records **unordered** adjacent pairs. This distinction is essential to the lower bound.

## Proof

**1. Mandatory adjacent-pair multiplicities.** Regard \(W\) as a closed walk, with the step from \(w_i\) to \(w_{i+1}\) carrying unordered edge label \(\{w_i,w_{i+1}\}\). Let \(m_{ab}\) be the frequency of this label. Each constant palindrome \(aaa\) requires two consecutive loop steps at \(a\), hence \(m_{aa}\ge2\).

For distinct \(a,b\), each of \(aba\) and \(bab\) uses two consecutive steps both labeled \(\{a,b\}\). These are two **different** cyclic adjacencies in the step-label sequence (their middle vertex is different). The step-label sequence is not identically \(\{a,b\}\), since \(aaa\) and \(bbb\) are also required. In any nonconstant cyclic label sequence, if a given label appears \(t\) times, there can be at most \(t-1\) cyclic adjacencies between two consecutive occurrences of that label: decompose its occurrences into maximal proper cyclic runs. Thus at least two such adjacencies require \(t\ge3\). Consequently \(m_{ab}\ge3\) for every distinct pair.

Since each cyclic step contributes once to exactly one unordered pair count,
\[
L=\sum_a m_{aa}+\sum_{a<b}m_{ab}
\ge 2q+3\binom q2=\frac{3q^2+q}{2}=:L_0.
\]

**2. Even-alphabet obstruction.** In any closed walk, each vertex has even degree in the undirected edge multigraph, where loops contribute two to degree. Put \(x_{aa}=m_{aa}-2\) and \(x_{ab}=m_{ab}-3\) for \(a<b\). Every \(x\) is nonnegative by the preceding step, and the degree at vertex \(a\) is
\[
2m_{aa}+\sum_{b\ne a}m_{ab}
=4+3(q-1)+2x_{aa}+\sum_{b\ne a}x_{ab}.
\]
If \(q\) is even, the baseline \(4+3(q-1)\) is odd. Therefore \(\sum_{b\ne a}x_{ab}\) must be odd, in particular at least one, at every vertex. Summing over vertices yields \(2\sum_{a<b}x_{ab}\ge q\); hence \(L\ge L_0+q/2\). If \(q\) is odd, the baseline is even and the previous \(L\ge L_0\) is the relevant bound.

**3. Sharp construction.** Begin with the connected undirected multigraph on \(q\) vertices having one loop at each vertex and one edge between each pair of distinct vertices. Its degree is \(q+1\) at every vertex (a loop contributes two). For odd \(q\), all degrees are even, so the graph has a closed Euler tour. For even \(q\), add one more copy of each edge in any perfect matching; the resulting degree is \(q+2\) at every vertex, again even, and a closed Euler tour exists.

Follow such a tour with a chosen orientation on every traversal. Replace the first traversal \(a\to b\) of each nonloop unordered pair by the three-step path \(a\to b\to a\to b\). On a repeated matching edge, leave its second traversal unchanged as a single step. Replace each loop traversal \(a\to a\) by the two-step path \(a\to a\to a\). Each replacement has the same endpoints as the original step, so the replacements concatenate into a closed walk. Every expanded nonloop first traversal exhibits both windows \(aba\) and \(bab\), and every expanded loop exhibits \(aaa\). Hence the cyclic vertex list, with its final repeated initial vertex omitted, is a cover.

The constructed cyclic word uses exactly two loop steps per symbol, three steps per unordered distinct pair, and, only for even \(q\), one extra step per matching pair. Its length is exactly \(L_0\) or \(L_0+q/2\), attaining the lower bounds.

**4. Every optimum has the stated multiplicity profile.** For odd \(q\), attaining \(L_0\) forces every lower bound in Step 1 to be an equality: \(m_{aa}=2\) and \(m_{ab}=3\). For even \(q\), attaining \(L_0+q/2\) forces the total excess to be exactly \(q/2\). The degree-parity argument forces each vertex to meet at least one extra nonloop edge. Since the \(q/2\) extra nonloop edges have exactly \(q\) endpoints counted with multiplicity, each vertex has exactly one extra edge endpoint, there are no extra loop steps, and the extra edges form a perfect matching with multiplicity one each. The construction realizes every chosen perfect matching because the initial graph and expansion are invariant under alphabet relabeling. This completes the proof.

## Verification

The complete standalone standard-library script `verify.py` implements Hierholzer Euler tours for the looped complete graph (with matching augmentation when needed), expands every step, and directly checks the length and occurrence of each of the \(q^2\) prescribed palindromes for every alphabet size from \(2\) through \(30\). It additionally checks the full unordered-adjacency multiplicity profile, including the perfect-matching condition.

As an independently formulated finite check, a breadth-first search tracks the set of length-three palindromes seen, the last two letters, and the first two fixed letters. Rotating to the compulsory factor \(000\) makes the chosen initial two letters \(00\) without loss. Exhaustive BFS recovers exact minimum lengths \(8,15,28\) at alphabet sizes \(2,3,4\), respectively. These finite tests are corroboration only; Steps 1–4 prove the all-alphabet theorem. A cyclic witness at \(q=2\) is `01011100`; its cyclic triples include `000`, `010`, `101`, and `111`.

Reproduce by running `python3 verify.py`; no external packages or network access are required.

## Relationship to prior work

Chen, Kitaev, and Sun (initially public August 3, 2019; subsequently published 2020) study existence probabilities for **exact** universal cycles and universal words after deleting members of a full fixed-length language. Their u-cycle uses every allowed factor exactly once and allows no additional factors. The present problem instead requires a fixed, sparse palindrome family to appear **at least once**, and optimality necessitates many non-palindromic filler windows. The proofs in that article concern removed de Bruijn-graph cycles and do not give this all-alphabet minimum or the matching-rigid optimal profiles; these are materially different statements, not a mere change in terminology.

General shortest-superstring methods, as studied for example by Mucha, provide general algorithmic formulations but do not themselves imply the closed parity-sensitive minimum for this exact cyclic language. Orientable sequences studied by Gabrić and Sawada avoid reversed-window repetitions and address a different extremal objective. The Euler-tour existence theorem and degree parity are classical ingredients; this result does not claim either as new. Related-but-different cyclic covering results for adjacency-restricted binary languages likewise do not imply coverage of all three-palindromes over unrestricted alphabets.

## Limitations

The result treats only length-three palindromes, unrestricted alphabets of size at least two, and cyclic covers. It neither determines the total number of non-isomorphic shortest covers nor claims a minimum for linear words or longer palindromes. The lower bound depends on simultaneous inclusion of **both** \(aba\) and \(bab\) and all constant palindromes. The novelty assessment is based on accessible searches and inspected full-text sources; an equivalent characterization in older shortest-superstring or graph-postman literature might still exist and requires external independent validation.

## References

1. H. Z. Q. Chen, S. Kitaev, B. Y. Sun, *On the probability of existence of a universal cycle or a universal word for a set of words*, arXiv:1908.01116, initially submitted August 3, 2019, https://arxiv.org/abs/1908.01116. Revised version published as *Lower Bounds, and Exact Enumeration in Particular Cases, for the Probability of Existence of a Universal Cycle or a Universal Word for a Set of Words*, Mathematics 8 (2020), 778, https://doi.org/10.3390/math8050778.
2. M. Mucha, *Lyndon Words and Short Superstrings*, arXiv:1205.6787 (2012), https://arxiv.org/abs/1205.6787.
3. D. Gabrić, J. Sawada, *Efficient Construction of Long Orientable Sequences*, CPM 2024, https://doi.org/10.4230/LIPIcs.CPM.2024.15.
