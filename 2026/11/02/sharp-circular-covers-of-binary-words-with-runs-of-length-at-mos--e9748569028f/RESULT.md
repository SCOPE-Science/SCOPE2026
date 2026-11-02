# Sharp circular covers of binary words with runs of length at most two

## Finding

For every integer \(k\ge 3\), let \(\mathcal W_k\subset\{0,1\}^k\) consist of all length-\(k\) binary words with no contiguous factor `000` or `111`. A *circular cover* is a nonempty indexed cyclic binary word \(c\) in which every member of \(\mathcal W_k\) occurs as at least one cyclic factor of length \(k\). No restriction is placed on additional factors in the definition of a cover. Let \(M_k\) be the minimum length of a circular cover. Then, writing \(F_0=0,F_1=1\) and \(F_{j+2}=F_{j+1}+F_j\),

\[
M_k=2(F_{k+1}+F_{k-1})-2.
\]

Moreover, one optimal cover has **only** permissible cyclic factors. In it every member of \(\mathcal W_k\) appears once, except that every word in
\[
\mathcal S_k=\{w\in\mathcal W_k:w_1\ne w_2,\ w_{k-1}\ne w_k,\ \text{and }w_i=w_{i+1}\text{ for some }i\}
\]
appears *twice*. There are exactly \(2F_{k-1}-2\) such doubled words. The minimum is also \(2L_k-2\), where \(L_k=F_{k-1}+F_{k+1}\) is a Lucas number; this is an identity, not a claimed novel integer sequence.

## Assumptions and scope

All words are finite binary words. The prohibited triples are only `000` and `111`; a word in \(\mathcal W_k\) may begin or end in either symbol and its first and last symbols need not be compatible when the word is repeated. A circular cover's length counts cyclic starting positions, including repeated copies of a length-\(k\) factor. Its length is not the length after appending the usual \(k-1\) linear wraparound symbols. The lower bound applies even to hosts with forbidden triples; the constructed optimum itself avoids both triples cyclically. No assertion is made about uniqueness of optimal covers or about larger alphabets.

## Proof

**1. Mandatory edge multiset.** Use the ordinary binary order-\((k-1)\) de Bruijn digraph: an edge labeled \(w_1\dots w_k\) leaves \(p=w_1\dots w_{k-1}\) and enters \(s=w_2\dots w_k\). Cyclic length-\(k\) windows of any host are precisely a closed walk in this graph. Take one obligatory copy of each \(w\in\mathcal W_k\), forming edge multiset \(E\). For a vertex \(v\) occurring in this subgraph, the outdegree of \(E\) is \(1\) if its final two bits agree and \(2\) otherwise; the indegree is \(1\) if its first two bits agree and \(2\) otherwise. Define \(b(v)=\deg_E^+(v)-\deg_E^-(v)\). Thus
\[
b(v)={\bf1}_{\{v_1=v_2\}}-{\bf1}_{\{v_{k-2}=v_{k-1}\}}.
\]
This holds for \(k=3\), where the two indicated pairs coincide and \(b=0\).

**2. Balancing with precisely the stated doubles.** Add one further copy of each edge in \(\mathcal S_k\), producing multiset \(E'\). A vertex \(v\) that contains an equal adjacent pair has one outgoing edge in \(\mathcal S_k\) exactly when its *first* two bits differ, and one incoming edge in \(\mathcal S_k\) exactly when its *last* two bits differ. Indeed, for the outgoing edge there is just one appendable last bit that makes the final pair unequal; the already-present equal pair ensures the resulting edge is not entirely alternating. The incoming assertion is symmetric. At a fully alternating vertex neither an incoming nor outgoing \(\mathcal S_k\)-edge exists: demanding unequal first and last pairs would make the entire edge alternating. Therefore
\[
\deg_{\mathcal S_k}^+(v)-\deg_{\mathcal S_k}^-(v)=-b(v)
\]
for all target vertices. Hence \(E'\) is balanced.

The digraph consisting of target edges is strongly connected on its nonisolated vertices: between any two allowed \((k-1)\)-bit vertices \(u,v\), append a sufficiently long alternating bridge beginning with the bit opposite the final bit of \(u\), chosen to end opposite the first bit of \(v\), then append \(v\). Every sliding triple stays permissible, so this produces a directed path from \(u\) to \(v\). Consequently \(E'\) is strongly connected and balanced, and the directed Euler theorem yields a closed tour visiting each \(E'\)-edge once. The corresponding cyclic binary word realizes every target once and every specified extra edge once more, with no forbidden triple.

**3. A global lower bound, including hosts with forbidden windows.** For any binary vertex \(v\) of length \(m=k-1\), let \(j(v)\) be the one-based position of its first equal adjacent pair, or \(m\) if no such pair exists. Put \(\phi(v)=-j(v)\). Every binary length-\(k\) edge \(p\to s\), even a forbidden one, satisfies
\[
\phi(s)-\phi(p)\le 1.
\]
Indeed, deleting the first bit shifts an existing first equal pair left by exactly one when it survives; if it disappears, or if the prefix was alternating, the new first pair cannot occur earlier than that bound. For any circular cover, let \(x_e\ge0\) be the multiplicity of each edge in its closed tour minus one copy of each target edge (and minus zero copies of every nontarget edge). Since the tour is closed,
\[
\deg_x^+(v)-\deg_x^-(v)=-b(v).
\]
Using the potential inequality on *all* full-graph edges yields
\[
\sum_e x_e\ge\sum_e x_e(\phi(\mathrm{head}(e))-\phi(\mathrm{tail}(e)))
=\sum_v b(v)\phi(v).
\]
Every edge in \(\mathcal S_k\) is tight in the potential inequality: its first two bits differ, it has an equal adjacent pair somewhere, and removing the first bit moves the first equal pair exactly one position earlier. Applying the last equality to the balancing multiset \(\mathcal S_k\) proves
\[
\sum_v b(v)\phi(v)=\lvert\mathcal S_k\rvert.
\]
Thus every circular cover needs at least \(\lvert\mathcal S_k\rvert\) windows beyond its \(\lvert\mathcal W_k\rvert\) mandatory windows. The constructed tour meets this bound.

**4. Exact counts.** Every word in \(\mathcal W_k\) is uniquely specified by its initial bit (two choices) and a composition of \(k\) into run lengths \(1\) and \(2\). There are \(F_{k+1}\) such compositions, giving \(\lvert\mathcal W_k\rvert=2F_{k+1}\). The first and last bits of a word each form a singleton run precisely when both its first and last adjacent bit pairs are unequal. Removing these singleton runs leaves a run-length composition of \(k-2\), with \(F_{k-1}\) choices, and two initial-bit choices. Exactly two words in this family are fully alternating; discarding them gives \(\lvert\mathcal S_k\rvert=2F_{k-1}-2\). Adding the two cardinalities proves the theorem for all \(k\ge3\).

## Verification

The independent optimization check modeled the full binary de Bruijn graph (including forbidden edges), required each admissible edge once and minimized extra circulation cost by integer minimum-cost flow; the computed optima for \(3\le k\le13\) equal the theorem. The included self-contained `VERIFY.py` separately constructs Eulerian tours for \(3\le k\le18\), verifies all target multiplicities and cyclic forbidden-factor avoidance, checks all edge-potential inequalities for \(3\le k\le14\), and confirms each construction meets the dual lower bound. Run `python3 VERIFY.py`; success terminates with `VERIFY_OK`. These finite tests check implementation and examples; the proof above supplies the infinite-domain result.

## Relationship to prior work

Chee, Etzion, Nguyen, Ta, Tran and Vu (arXiv:2403.01454v1, first available March 3, 2024) study longest run-length-limited sequences in a de Bruijn graph, emphasizing restrictions on long runs of zeros and distinct windows. The present problem instead requires *all* finite length-\(k\) words avoiding *both* constant triples and minimizes cyclic host length, explicitly allowing factor repetition. Moreno and Matamala (arXiv:0711.1695) investigate lexicographically minimal de Bruijn cycles for **periodically admissible** forbidden-substring languages; their target language and exactly-once formulation are not identical to all finite admissible factors treated here. Chen, Kitaev and Sun (arXiv:1908.01116) study exactly-once universal cycles after removal of target words, not the shortest repeated cover here. The numerical sequence of minima equals OEIS A168674 beginning at index three; that sequence is therefore **not** asserted to be new. The novel scientific claim sought is its shortest-cover interpretation, uniform optimality proof, and factor-multiplicity construction. These comparisons do not constitute a proof of historical priority.

## Limitations

The statement concerns binary alphabet, a pair of forbidden triples, and all integer lengths \(k\ge3\) only. It neither classifies every optimal cyclic word nor extends to different run bounds. Equivalent earlier work under constrained de Bruijn, Eulerian augmentation, or universal-cycle terminology could exist outside the inspected literature. The source comparison is a documented novelty assessment, not an independent audit or priority guarantee.

## References

- Y. M. Chee, T. Etzion, T. L. Nguyen, D. H. Ta, V. D. Tran, and V. K. Vu, *Maximum Length RLL Sequences in de Bruijn Graph*, arXiv:2403.01454v1 (2024), https://arxiv.org/html/2403.01454v1 .
- E. Moreno and M. Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings*, arXiv:0711.1695 (2007), https://arxiv.org/pdf/0711.1695 .
- Y. Chen, S. Kitaev, and B. Y. Sun, *On the probability of existence of a universal cycle or a universal word for a set of words*, arXiv:1908.01116 (2019), https://arxiv.org/abs/1908.01116 . [Comparison limited to the source's universal-cycle coverage framework; this work is not cited for the stated formula.]
- OEIS Foundation, A168674, https://oeis.org/A168674 (numerical identity, not a cover interpretation).

- R. D. Bryant and H. Fredricksen, *Covering the de Bruijn graph*, Discrete Mathematics 89 (1991), 133–148; bibliographic citation only, full text not inspected, https://dblp.org/rec/journals/dm/BryantF91 .
