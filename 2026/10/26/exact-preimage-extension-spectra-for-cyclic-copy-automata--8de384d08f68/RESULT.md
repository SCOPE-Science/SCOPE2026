# Exact preimage-extension spectra for cyclic copy automata

## Finding
Fix integers \(n\geq2\) and \(1\leq d<n\). On \(Q=\mathbb Z/n\mathbb Z\), consider the two-letter deterministic automaton
\[
 a:i\mapsto i+1\pmod n,\qquad
 b:i\mapsto\begin{cases}d,&i=0,\\i,&i\ne0.\end{cases}
\]
For every proper nonempty \(S\subset Q\), let \(\operatorname{minext}(S)\) be the minimum length of a word \(w\) such that \(|w^{-1}(S)|>|S|\), or \(\infty\) if no such word exists. Define the directed crossing set
\[
 E_d(S)=\{i\in\{0,\ldots,n-1\}:i\notin S,\;i+d\pmod n\in S\}.
\]
**Exact extension theorem.** For every \(n,d,S\) above,
\[
 \operatorname{minext}(S)=\begin{cases}1+\min E_d(S),&E_d(S)\ne\varnothing,\\
 \infty,&E_d(S)=\varnothing.\end{cases}
\]
When finite, the word \(ba^r\), with \(r=\min E_d(S)\), attains the minimum (letters act on states from left to right).

**Complete spectrum for coprime displacement.** Suppose \(\gcd(n,d)=1\). For \(0\leq t<n\), draw on \(Q\) the directed edges \(i\to i+d\pmod n\) for \(0\leq i<t\). They form vertex-disjoint directed paths, including singleton vertices; let their respective numbers of vertices be \(v_{t,1},\dots,v_{t,c_t}\). Put
\[
 A_t=\prod_{j=1}^{c_t}(v_{t,j}+1),\qquad A_n=2.
\]
Then, for every \(1\leq\ell\leq n\), the **exact number of proper nonempty subsets** satisfying \(\operatorname{minext}(S)=\ell\) is
\[
 \boxed{N_{n,d}(\ell)=A_{\ell-1}-A_\ell.}
\]
In particular \(\boxed{N_{n,d}(n)=n-1}\); there is **exactly one** subset of each cardinality \(s=1,\ldots,n-1\) whose shortest extending word has length \(n\), namely
\[
 S_s=\{(n-1)+jd\pmod n:1\leq j\leq s\}.
\]
Thus exactly \(n-1\) of the \(2^n-2\) nontrivial subsets fail to extend within \(n-1\) letters. In the classical displacement-one case the entire spectrum simplifies to
\[
 N_{n,1}(\ell)=\ell\,2^{n-\ell-1}\quad(1\leq\ell<n),
 \qquad N_{n,1}(n)=n-1.
\]
The intermediate spectra can genuinely depend on displacement. For \(n=7\), the counts at lengths \(1,\ldots,7\) are \((32,32,24,16,10,6,6)\) for \(d=1\), but \((32,24,24,16,12,12,6)\) for \(d=2\).

## Assumptions and scope
An inverse image \(w^{-1}(S)\) is the set of states \(q\) whose forward image under \(w\) belongs to \(S\). We count every subset of \(Q\) as labeled, and words have unit cost per letter. The definition of \(E_d\) uses the standard integer representatives \(0,\ldots,n-1\) to order crossings. The first theorem holds regardless of coprimality; the forest product and finite length spectrum assume coprimality. The special case \(d=1\) is a cyclic relabeling of the usual Černý family. In the noncoprime case the formula \(\operatorname{minext}(S)=\infty\) precisely characterizes the nonextensible subsets.

## Proof
Write \(T\ell^{-1}\) for the inverse action of a letter \(\ell\). From the displayed transition maps one has
\[
 Ta^{-1}=T-1\pmod n,
 \qquad Tb^{-1}=(T\setminus\{0\})\cup
 \begin{cases}\{0\},&d\in T,\\\varnothing,&d\notin T.\end{cases}
\]
Consequently, an inverse \(b\)-step grows a set by one exactly when \(0\notin T\) and \(d\in T\), equivalently \(0\in E_d(T)\). It decreases cardinality by one exactly when \(0\in T\) and \(d\notin T\). In the latter case \(E_d(Tb^{-1})\subseteq E_d(T)\): changing occupancy at vertex \(0\) from one to zero cannot create a crossing, because the outgoing edge \(0\to d\) still ends at an unoccupied vertex, and the incoming crossing into \(0\) can only disappear. Every other inverse \(b\)-step leaves \(T\) unchanged. Meanwhile inverse \(a\) rotates every crossing index down by one modulo \(n\).

Let \(r=\min E_d(S)\), if the crossing set is nonempty. After \(r\) inverse \(a\)-steps, the original crossing at \(r\) lies at index zero. The inverse \(b\)-step then adds vertex zero and increases cardinality, so \(ba^r\) is an extending word of length \(r+1\). For the converse consider an arbitrary inverse-letter path from \(S\) to a strictly larger set and stop at its first cardinality-increasing step. This step must be an inverse \(b\). Prior inverse \(b\)-steps either do nothing or shrink and cannot create crossing indices; inverse \(a\)-steps merely rotate the original surviving crossings. If fewer than \(r\) inverse \(a\)-steps have occurred, no original crossing index can yet rotate to zero (the rotation count is less than \(r\leq n-1\)). Therefore at least \(r\) inverse \(a\)-steps and the growing inverse \(b\)-step are necessary. Any preceding shrinking steps also contribute nonnegative length. The minimum is exactly \(r+1\).

If \(E_d(S)\) is empty, it stays empty after inverse rotations. For any set with no crossings, the inverse \(b\)-step cannot grow; moreover it cannot shrink either: if \(0\in T\) and \(d\notin T\), then the edge \(d\to2d\) is irrelevant, but the no-crossing condition on the finite \(d\)-orbit forces \(d\in T\) whenever \(0\in T\), contradiction. Indeed, no \(0\to1\) crossing on a finite directed \(d\)-cycle forces every vertex on that cycle to have equal occupancy. Thus inverse \(b\) fixes such a set, and no extension is ever possible.

For the spectrum assume \(\gcd(n,d)=1\), so the edges \(i\to i+d\) form one directed \(n\)-cycle. A proper nonempty subset must have at least one unoccupied-to-occupied crossing and is therefore extensible. The condition \(\min E_d(S)\geq t\) says precisely that none of the edges starting at indices \(0,\ldots,t-1\) has occupancy pattern \(0\to1\). When \(t<n\), deleting the other edges of the single directed cycle leaves a forest of directed paths. On a path of \(v\) vertices the admissible zero-one occupation strings are exactly \(1^j0^{v-j}\) for \(0\leq j\leq v\), giving \(v+1\) choices. Independent paths give \(A_t\) choices, including the all-empty and all-full sets. At \(t=n\), absence of any crossings forces exactly these two constant sets, giving \(A_n=2\). Taking successive differences yields the stated \(N_{n,d}(\ell)\).

For \(t=n-1\), removing one edge from an \(n\)-cycle leaves one path on \(n\) vertices. Thus \(A_{n-1}=n+1\) and \(N_{n,d}(n)=n-1\). These extreme subsets have their **sole** crossing at index \(n-1\); along the directed cycle they consist of a nonempty proper contiguous block following that edge, exactly \(S_s\), one for each \(s\). Finally when \(d=1\) and \(t<n\), the first \(t\) edges form one path on \(t+1\) vertices and \(n-t-1\) isolated vertices. Hence \(A_t=(t+2)2^{n-t-1}\), and subtraction gives the simplified length formula.

## Verification
The accompanying executable `artifacts/verify_general.py` independently breadth-first searches the inverse-subset automaton for each nonempty proper subset of each cyclic-copy automaton with \(2\leq n\leq10\) and \(1\leq d<n\), including noncoprime cases. For coprime displacement it also independently computes the path-component product and checks every length multiplicity, the unique longest subset of each size, and the closed displacement-one formula. It tested all \(45\) automata and \(16{,}298\) subset instances and returned `PASS`. This finite exhaustive check is supplementary; all unbounded quantifiers are proved above.

## Relationship to prior work
Miccinesi (2026) studies exactly the invariant \(\operatorname{minext}(S)\), proves certificate-based sufficient conditions for extending within \(n-1\), and notes that Černý automata contain subsets exceeding this threshold (Section 8.1). The present exact per-subset formula, all-length distribution, and enumeration of exceptional subsets are not stated there. Berlinkov, Ferens and Szykuła (2018/2020) develop the general preimage-extension decision and complexity framework, without the cyclic-copy spectrum. Don (2016), especially Lemma 13 and Proposition 15, gives extension existence and complete reachability under a coprimality condition, but does not provide *shortest* extension lengths or their multiplicities. The public works titled *Exact k-avoiding thresholds of the Černý automata* and *Exact early deficiency profile of the Černý automata* respectively optimize **total** avoidance of specified sets and initial **image-rank** loss, not the one-step preimage growth of a prescribed subset. *Two-defect reachability in cyclic defect-one automata* treats two-letter-copy image codimension-two targets, not the present inverse-extension distribution. The distinctions are between different quantifiers and extremization problems, not merely different parameter choices.

## Limitations
The exact distribution \(N_{n,d}(\ell)\) is formulated through finite path sizes, rather than a single closed expression for every displacement. It holds for this explicitly defined cyclic-copy automaton family and does not apply to an arbitrary rank-\((n-1)\) transformation with the same excluded/duplicated states. The statement is about first enlargement of a prescribed inverse image, not shortest reset words or complete reachability of prescribed image sets. The source comparison supports originality to the best of inspected work; differently phrased equivalent results in unindexed transformation-semigroup literature remain possible.

## References
1. M. Miccinesi, *Certificates for short extending words in a finite automaton*, arXiv:2609.21603, first public 2026-09-18. https://arxiv.org/abs/2609.21603
2. M. V. Berlinkov, R. Ferens and M. Szykuła, *Preimage Problems for Deterministic Finite Automata*, arXiv:1704.08233. https://arxiv.org/html/1704.08233v4
3. H. Don, *The Černý Conjecture and 1-Contracting Automata*, Electronic Journal of Combinatorics 23(3) (2016), P3.12. https://doi.org/10.37236/5616
4. *Exact k-avoiding thresholds of the Černý automata*, public research result (2026), https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE-cerny-k-avoiding-thresholds--5cdbaf373a0f
5. *Exact early deficiency profile of the Černý automata*, public research result (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-early-deficiency-profile-of-the-ern-automata--766d362d36d3
6. *Two-defect reachability in cyclic defect-one automata*, public research result (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-two-defect-reachability-in-cyclic-defect-one-automata--3d0ad329ab1e
