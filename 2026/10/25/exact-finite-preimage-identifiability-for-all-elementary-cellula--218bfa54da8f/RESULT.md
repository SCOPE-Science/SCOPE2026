# Exact finite-preimage identifiability for all elementary cellular automata

## Finding
For every Wolfram elementary binary radius-one cellular-automaton rule \(r\in\{0,\ldots,255\}\), define \(u_r\) as the smallest positive length of a one-step output word with **exactly one unrestricted finite predecessor block**, and set \(u_r=\infty\) if there is no such word. The complete spectrum is:

| \(u_r\) | Number of rules |
| --- | ---: |
| \(1\) | 16 |
| \(2\) | 52 |
| \(3\) | 56 |
| \(4\) | 28 |
| \(5\) | 4 |
| \(6\) | 8 |
| \(\infty\) | 92 |

Consequently, **six is a sharp universal finite-identifiability cutoff**. Every rule with any uniquely reconstructible finite output word has one with at most six symbols. Exactly Rules 37, 57, 91, 99, 156, 164, 198, and 218 require all six; lexicographically first shortest output witnesses, in that order, are `100101`, `000100`, `010010`, `001000`, `000100`, `100101`, `001000`, and `010010`.

The distinction from merely recovering the rightmost predecessor pair is strict: 42 rules admit a finite output word forcing that pair but admit **no output word of any length** with a unique entire finite predecessor block. Of the 164 rules that admit full uniqueness, the difference between shortest full-uniqueness length and shortest right-boundary-synchronization length is \(0,1,2,3\) for 132, 20, 8, and 4 rules respectively. The accompanying `classification.csv` gives each rule, both optimal lengths, exact shortest witnesses, and a finite-state closure size.

## Assumptions and scope
Write \(f_r(a,b,c)=\lfloor r/2^{4a+2b+c}\rfloor\bmod 2\) for \(a,b,c\in\{0,1\}\). For every output word \(w=(w_0,\ldots,w_{n-1})\in\{0,1\}^n\), \(n\ge1\), its unrestricted finite predecessor set is
\[
\operatorname{Pre}_r(w)=\bigl\{(a_0,\ldots,a_{n+1})\in\{0,1\}^{n+2}:f_r(a_j,a_{j+1},a_{j+2})=w_j\text{ for all }0\le j<n\bigr\}.
\]
Define \(u_r=\min\{n\ge1: \exists w\in\{0,1\}^n,\ |\operatorname{Pre}_r(w)|=1\}\), with \(\infty\) for the empty minimum. This is a **finite-open-boundary** observation problem: no periodic input condition is imposed. The right-boundary synchronization length \(b_r\) uses the same output words but asks only for a singleton set of final input pairs \((a_n,a_{n+1})\). An inadmissible output with no predecessor does not synchronize. The counts concern one update, not temporal iterates or entire bi-infinite predecessor uniqueness.

## Proof
There are four overlap states, each representing an ordered binary pair. Label a directed edge from state \(s=2a+b\) to \(t=2b+c\) by \(f_r(a,b,c)\). For every length-\(n\) output word, paths of length \(n\) in this graph are in bijection with its \(n+2\)-bit finite predecessors, because the successive two-bit overlaps uniquely determine each input bit.

Let \(A_0,A_1\) be the \(4\)-by-\(4\) adjacency matrices for the corresponding labels. Initialize \(v^{(0)}=(1,1,1,1)\), counting one empty path at every initial overlap. After reading the next output bit \(d\), update every terminal coordinate by
\[
 v^{(k+1)}_t=\min\left(2,\sum_{s=0}^{3}v^{(k)}_s A_d(s,t)\right).
\]
Inductively, \(v^{(k)}_t\) is the true count of finite predecessor paths terminating at \(t\), capped at two. Capping at two before future additions does not affect whether the total count is zero, one, or at least two. Thus an output word has exactly one finite predecessor if and only if \(\sum_t v^{(n)}_t=1\). There are at most \(3^4=81\) possible capped-count states, so complete breadth-first reachability with both output labels decides the existence of an identifiable word **at every positive length**. Breadth-first order also certifies the shortest length and the lexicographically first shortest witness.

The accompanying exact verifier enumerates this entire reachable transition closure for each integer rule from 0 through 255, with at most 66 states reached for any rule. The generated `classification.csv` is the complete rule-by-rule certificate, not a list of unexplained sampled observations. Tallying its lengths yields the first table; its eight maximal cases attain length six; for each rule labeled `never`, no reachable capped-count state has total one, proving impossibility at arbitrarily large output lengths.

For the right boundary, replace every positive coordinate of \(v\) by its support bit and update supports under the same labeled graph. This has at most \(2^4=16\) states, and admissible singleton supports are precisely right-boundary-synchronizing outputs. Complete reachability gives 50 rules with no singleton right boundary and 206 with one. Because a unique finite predecessor necessarily has one final pair, the rules lacking complete uniqueness but admitting boundary synchronization are precisely 42. The shortest-length comparisons yield the stated \(132,20,8,4\) gap distribution.

## Verification
Run `python3 verify.py classification.csv` using only the Python standard library. It reconstructs all 256 complete capped-count reachability graphs, the independent support-only right-boundary machines, the per-rule lexicographically first shortest witnesses and lengths, and **32,256 independent finite-output-word checks**. For these independent checks, it directly enumerates every \((n+2)\)-bit input block for every rule and for each \(1\le n\le6\), computes its output and final input pair, and compares the resulting exact counts and support sets with both finite-state predictions. It also regenerates and byte-compares the complete CSV, checks the stated class counts and all eight six-symbol extremizers, and verifies the 42-rule distinction. Direct enumeration is a cross-check only: the unbounded assertion is certified by complete finite-state closure.

## Relationship to prior work
Seck Tuoh Mora, Juárez Martínez and McIntosh developed subset-diagram ancestor calculations; Jeras and Dobnikar developed exact count-and-list methods for predecessor configurations, illustrating their methods chiefly with Rule 110. Such general counting machinery is foundational here, but the inspected works do not state the all-256 least **full-preimage-uniqueness** classification, the sharp six-symbol cutoff, or the 42-rule separation from one-sided synchronization. Salo's studies of split epicness and von Neumann regularity concern existence of continuous generalized inverses rather than a unique predecessor for a particular finite open-boundary output. Specific isolated unique-preimage words, including Rule 18 output `11`, have been documented in work on limit dynamics and are not claimed as new. These distinctions are mathematical statement comparisons, not assertions of historical priority from absent search hits.

## Limitations
The finding proves only this finite-block invariant and its exact classification; it does not imply global reversibility or injectivity of any rule on the bilateral full shift. The six-symbol theorem is specific to the 256 binary radius-one rules, not a universal bound for arbitrary local rules or alphabet sizes. The predecessor computations are exhaustive finite-state certificates, with independent finite-length cross-checks; no external independent audit has been performed. Unindexed earlier calculations or tabulations could contain the same all-rule distribution.

## References
1. J. C. Seck Tuoh Mora, G. Juárez Martínez, and H. V. McIntosh, “Calculating Ancestors in One-Dimensional Cellular Automata,” *International Journal of Modern Physics C* 15 (2004), 1151–1169. DOI: 10.1142/S0129183104006625.
2. I. Jeras and A. Dobnikar, “Cellular Automata Preimages: Count and List Algorithm,” *Computational Science—ICCS 2006*, LNCS 3993 (2006), 345–352. DOI: 10.1007/11758532_47. Accessible manuscript: https://rattus.info/al/files/conference.pdf.
3. I. Jeras and A. Dobnikar, “Algorithms for computing preimages of cellular automata configurations,” *Physica D* 233 (2007), 95–111. Manuscript: https://rattus.info/al/files/preimages.pdf.
4. Y. Kayama, “Complex networks derived from cellular automata,” arXiv:1009.4509v1 (first posted 2010-09-23), https://arxiv.org/abs/1009.4509.
5. V. Salo, “On von Neumann regularity of cellular automata,” arXiv:2209.13373 (2022), https://arxiv.org/abs/2209.13373.
6. “Limit dynamics of elementary cellular automaton 18,” *Ergodic Theory and Dynamical Systems* (2026), https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/limit-dynamics-of-elementary-cellular-automaton-18/8D236BAA96D6BB0F894ABCFEF3C1312B.
