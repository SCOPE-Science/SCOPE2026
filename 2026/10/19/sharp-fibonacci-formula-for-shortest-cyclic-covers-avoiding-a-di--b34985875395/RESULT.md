# Sharp Fibonacci formula for shortest cyclic covers avoiding a directed binary triple

## Finding
Let \(k\ge3\) be an integer, and let \(\mathcal L_k\) consist of all length-\(k\) binary words with no occurrence of the contiguous factor `110`. A cyclic covering word means any nonempty cyclic binary word in which every member of \(\mathcal L_k\) occurs as a circular factor of length \(k\); neither the host word nor its additional factors are constrained to avoid `110`. If \(C_k\) denotes the smallest length of such a host and \(F_0=0\), \(F_1=1\), \(F_{j+2}=F_{j+1}+F_j\), then
\[
|\mathcal L_k|=F_{k+3}-1,\qquad
C_k=F_{k+3}-1+(k-2)F_{k-1}.
\]
Equivalently, the unavoidable additional number of cyclic windows is exactly \((k-2)F_{k-1}\). The same formula holds when the forbidden triple is `011`, `001`, or `100`, by word reversal and bit complementation. Moreover
\[
\frac{C_k-|\mathcal L_k|}{|\mathcal L_k|}\sim\frac{k}{\varphi^4},\qquad
\varphi=\frac{1+\sqrt5}{2}.
\]

## Assumptions and scope
Words, including cyclic host words, use the alphabet \(\{0,1\}\). A cyclic factor of length \(k\) can wrap around the host and can revisit a position if the host is shorter than \(k\); the optimum constructed below is always at least \(k\). Distinct required words need only occur at least once. Additional windows are allowed and counted with multiplicity. The claim is for every integer \(k\ge3\), not for an unproved range or an alphabet of arbitrary size.

## Proof
**Step 1: count required words.** Binary words of length \(k\) avoiding `11` are counted by \(F_{k+2}\). If a word avoids `110` but contains `11`, then after its first consecutive `11` no zero may occur: it has a unique final block of at least two ones, preceded by either the empty word or a word avoiding `11` and ending in zero. For a prefix of length \(\ell\), with \(0\le\ell\le k-2\), the number of such prefixes is \(F_{\ell+1}\), including the empty case. Hence this second family has \(\sum_{\ell=0}^{k-2}F_{\ell+1}=F_{k+1}-1\) members, giving \(|\mathcal L_k|=F_{k+3}-1\).

**Step 2: calculate compulsory imbalances.** Use the binary de Bruijn directed graph with length-\((k-1)\) words as vertices and length-\(k\) words as edges, joining their length-\((k-1)\) prefix to their length-\((k-1)\) suffix. Retain just the required edges avoiding `110`, and their incident vertices. For every vertex \(v\) avoiding `110`, the mandatory outdegree and indegree are respectively
\[
d^+(v)=2-\mathbf1_{\{v\text{ ends in }11\}},\qquad
d^-(v)=2-\mathbf1_{\{v\text{ begins with }10\}}.
\]
Thus \(d^+(v)-d^-(v)=\mathbf1_{\{v\text{ begins with }10\}}-\mathbf1_{\{v\text{ ends with }11\}}\). A positive-imbalance vertex begins with `10` and does not end with `11`. Since an internal `11` in a `110`-avoiding word forces all subsequent symbols to be ones, this vertex contains no `11` at all. Conversely every word `10` followed by a length-\((k-3)\) word avoiding `11` is such a vertex. Its number is \(F_{k-1}\). Every nonzero degree difference is \(1\) or \(-1\), and the total negative deficit count is also \(F_{k-1}\). Every negative vertex ends in `11`, every positive vertex begins in `10`.

**Step 3: unrestricted lower bound.** A cyclic host induces a closed walk in the full de Bruijn graph; each compulsory edge is used at least once. Removing one copy of each compulsory edge leaves a directed edge multiset whose net out-minus-in at vertex \(v\) is \(-(d^+(v)-d^-(v))\). It decomposes into directed paths from the \(F_{k-1}\) negative vertices to positive vertices, together with directed cycles. Any directed walk from a state ending in `11` to one beginning in `10` requires at least \(k-2\) edges: a shorter walk would force agreement of an overlapping pair of symbols, simultaneously `11` and `10`. Therefore every covering host has at least \((k-2)F_{k-1}\) excess edges beyond the distinct required edges.

**Step 4: attain the bound.** Choose any bijection from negative to positive vertices. If \(s\) is negative and \(t=t_1t_2\cdots t_{k-1}\) is positive, then the last symbol of \(s\) equals \(t_1=1\). Appending \(t_2,\ldots,t_{k-1}\) yields a de Bruijn walk of exactly \(k-2\) edges from \(s\) to \(t\). Duplicate these paths in the compulsory edge graph. Every vertex is now balanced. The underlying undirected support of the required graph is connected: beginning with the all-zero state, sequentially appending the symbols of any state avoiding `110` reaches that state along required edges, since the initial leading zeros cannot introduce `110`. Consequently the augmented balanced multigraph admits an Eulerian circuit; spelling its last symbol on each edge yields a cyclic host of exactly \(|\mathcal L_k|+(k-2)F_{k-1}\) positions. The lower bound is attained.

**Step 5: symmetry and asymptotics.** Reversal and bit complementation preserve the cyclic-cover optimum and map `110` to the stated four triples. Binet's formula gives \(F_{k-1}/F_{k+3}\to\varphi^{-4}\), proving the asymptotic relation.

## Verification
The standalone standard-library program `verify.py` independently builds the required de Bruijn graph, balances its imbalances using explicit walks, computes an Euler circuit, constructs its cyclic host and checks all required cyclic windows. It covers every length \(3\le k\le16\). Its expected outcome is `VERIFY_OK cyclic_hosts_k=3..16 exact_coverage_and_length`. This is a finite consistency check, while Steps 1–5 prove the quantified theorem for all \(k\ge3\).

## Relationship to prior work
Classical universal cycles and de Bruijn graph constructions supply the general Eulerian framework. Burstein and Kitaev [1] investigate unavoidable word-pattern families, not the shortest repetition-allowing cover for this particular forbidden-factor language. Moreno and Matamala [2] investigate the *lexicographically minimum* de Bruijn sequence in a language with forbidden substrings; their minimization criterion and hypotheses differ from the present unrestricted shortest-cover problem. Chen, Kitaev and Sun [3] investigate existence and enumeration of universal cycles using each required word once, rather than an optimal repetition overhead when many words are forbidden. The integer overhead sequence agrees after index shift with a Fibonacci product recorded at OEIS [4]; numerical sequence agreement does not establish the present combinatorial optimization or construction. A related result for avoidance of `111` addresses a different language with Tribonacci growth and does not imply the present Fibonacci formula.

## Limitations
The classification concerns one forbidden directed length-three pattern and its three reversal/complement images. It does not determine optimal covers for arbitrary forbidden sets or higher alphabets, and does not enumerate optimal covering hosts. The bibliography search and comparable theorems reduce but cannot eliminate originality risk from unindexed or inaccessible treatments of forbidden-factor universal covers. No independent scientific audit has been performed.

## References
[1] A. Burstein and S. Kitaev, *On unavoidable sets of word patterns*, arXiv:math/0311399 (public 2003-11-23).
[2] E. Moreno and M. Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings*, arXiv:0711.1695 (public 2007-11-12).
[3] H. Z. Q. Chen, S. Kitaev, and B. Y. Sun, *Lower Bounds, and Exact Enumeration in Particular Cases, for the Probability of Existence of a Universal Cycle or a Universal Word for a Set of Words*, arXiv:2005.00165 (2020).
[4] OEIS A023607, Fibonacci-product integer sequence (numerical comparison only).
