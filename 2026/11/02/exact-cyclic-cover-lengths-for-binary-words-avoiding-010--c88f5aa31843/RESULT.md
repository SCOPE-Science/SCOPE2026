# Exact cyclic-cover lengths for binary words avoiding `010`

## Finding

For each integer \(n\ge3\), let \(\mathcal A_n\) be the set of all binary words of length \(n\) containing no consecutive factor `010`. A circular word of length \(L\ge1\) covers \(\mathcal A_n\) when all members occur among its cyclic length-\(n\) windows, with symbols interpreted periodically even if \(L<n\). Additional and repeated windows are permitted. Let \(L_n\) denote the least possible \(L\).

Define \(a_0=1\), \(a_1=2\), \(a_2=4\), and, for \(j\ge3\),
\[
a_j=2a_{j-1}-a_{j-2}+a_{j-3}.
\]
Then \(a_n=|\mathcal A_n|\) and
\[
\boxed{L_3=8,\qquad L_4=14,\qquad
L_n=a_n+a_{n-2}+a_{n-5}-(n-1)\quad(n\ge5).}
\]
The minimum unavoidable number of supplementary cyclic windows is therefore \(1\), \(2\), and \(a_{n-2}+a_{n-5}-(n-1)\), respectively. In particular, for orders \(3\) through \(16\), the exact lengths are
\[
8,14,25,46,84,151,269,477,843,1486,2615,4597,8076,14182.
\]
The theorem covers the entire infinite family, not just these checked examples.

## Assumptions and scope

All words are over \(\{0,1\}\); forbidden factor means an ordinary contiguous substring, not avoidance in an infinite periodic extension. A cyclic cover is **one** circular word, not an arbitrary collection of circular words. Every required length-\(n\) word must occur at least once; repetitions and length-\(n\) windows containing `010` are allowed in the covering word. Both lower and upper bounds apply for every integer \(n\ge3\), with no assumption that a candidate cover itself avoids `010`.

Write \(m=n-1\). The binary de Bruijn digraph has vertices \(\{0,1\}^m\) and one directed arc \(w_0\cdots w_{m-1}\to w_1\cdots w_m\) for each binary \((m+1)\)-word \(w\); this arc is labelled by its final bit. The **required** multigraph consists of the arcs whose length-\(n\) words avoid `010`. Every circular cover corresponds to a closed walk using each required arc at least once, and conversely such a closed walk yields a cover of the same length. Additional traversals may use any binary de Bruijn arc.

## Proof

**1. The required graph and its defects.** Every allowed length-\(m\) vertex has required outdegree two except when it ends `01`, when its required outdegree is one; it has required indegree two except when it starts `10`, when its indegree is one. Vertices containing `010` have no required incident arc. Consequently the nonzero required outdegree-minus-indegree defects are
\[
S=\{u\in\{0,1\}^m:\ u\text{ avoids `010`, starts `10`, does not end `01`}\},
\]
with defect \(+1\), and
\[
T=\{v\in\{0,1\}^m:\ v\text{ avoids `010`, ends `01`, does not start `10`}\},
\]
with defect \(-1\). All other defects vanish. The required graph is strongly connected on its incident vertices: from any allowed vertex, successively append ones to reach \(1^m\); from \(1^m\), append the desired allowed vertex. Neither operation creates `010` at a join.

**2. Lower bound using the first `10`.** For \(v\in T\), define \(k(v)\) to be the least \(i\in\{1,\ldots,m-2\}\) for which the consecutive internal pair \(v_i v_{i+1}\) is `10`, or set \(k(v)=m-1\) when no such index exists (indices start at zero). This last case occurs exactly for \(v=0^{m-1}1\). Since the first two symbols of a vertex reached after \(t\le m-2\) de Bruijn shifts from \(v\) are \(v_t v_{t+1}\), no directed walk from \(v\) to any member of \(S\) can have fewer than \(k(v)\) arcs.

Given any cyclic cover, remove one copy of every required arc from its closed-walk multiset. The remaining arcs form a nonnegative integral flow with one unit of net supply at each \(v\in T\), one unit of net demand at each \(u\in S\), and zero at all other vertices. Such a flow decomposes into directed sink-to-source paths (one per sink) and directed cycles. The preceding distance bound therefore gives
\[
L_n\ \ge\ a_n+\sum_{v\in T}k(v).
\]
This holds regardless of which forbidden windows are used as supplementary arcs.

**3. A matching of sinks to sources.** For every \(v\in T\), split \(v=PQ\), where \(|P|=k(v)\), and set
\[
f(v)=Q\,\operatorname{rev}(P).
\]
For the unique special sink \(v=0^{m-1}1\), this gives \(f(v)=10^{m-1}\in S\). For any other sink, its first internal `10` determines a unique factorization \(v=0^a1^bQ\), with \(a\ge0\), \(b\ge2\), and \(Q\) beginning `10` and ending `01`. Thus \(P=0^a1^{b-1}\), and \(f(v)=Q1^{b-1}0^a\) starts `10`, avoids `010`, and does not end `01`: it is a source.

This map is a bijection. Indeed, a source with no internal `01` is necessarily \(10^{m-1}\), the image of the special sink. Otherwise split the source as \(u=QR\), where \(Q\) ends at the **last** `01` and \(R\) is the nonempty remaining suffix. The absence of `010` forces \(R\) to begin with one, and the absence of another `01` forces \(R=1^c0^a\) for some \(c\ge1\), \(a\ge0\). Then \(v=\operatorname{rev}(R)Q\) lies in \(T\), its first internal `10` is at position \(|R|\), and \(f(v)=u\). The preimage is unique.

From each sink \(v=PQ\), append the bits of \(\operatorname{rev}(P)\) to perform exactly \(k(v)\) de Bruijn transitions, reaching its matched source \(f(v)\). Adding these walks balances all vertices. Since the original required graph is strongly connected and the added arcs only enlarge it, the resulting balanced graph is Eulerian. Its Eulerian cycle is a cyclic cover of length \(a_n+\sum_{v\in T}k(v)\), proving equality in the lower bound.

**4. Exact enumeration.** Write \(E_n=\sum_{v\in T}k(v)\). Besides the special sink \(0^{m-1}1\), of cost \(m-1\), every sink is uniquely \(0^a1^bt\) with \(a\ge0\), \(b\ge2\), and \(t\) beginning `0`, ending `01`, and avoiding `010`; its cost is \(a+b-1\). The length-generating series for such \(t\) is
\[
T(z)=\frac{z^2(1-z)}{1-2z+z^2-z^3},
\]
obtained, for example, by the three-state prefix automaton with states empty, `0`, `01`. The weighted length series for the initial factor is
\[
\sum_{a\ge0,b\ge2}(a+b-1)z^{a+b}=\frac{z^2(1+z)}{(1-z)^3}.
\]
Consequently,
\[
\sum_{n\ge3}E_nz^n
=z\left(\frac{z^2}{(1-z)^2}+\frac{z^2(1+z)}{(1-z)^3}T(z)\right)
=\frac{z^3(1-2z+2z^2)}{(1-z)^2(1-2z+z^2-z^3)}.
\]
The automaton also gives
\[
\sum_{j\ge0}a_jz^j=\frac{1+z^2}{1-2z+z^2-z^3}.
\]
Comparison of these rational series yields \(E_3=1\), \(E_4=2\), and \(E_n=a_{n-2}+a_{n-5}-(n-1)\) for every \(n\ge5\), completing the proof.

## Verification

The accompanying `verify.py` is self-contained Python 3 code using only the standard library. Running `python3 verify.py` constructs the required de Bruijn multigraph and sink-to-source augmentation at each order \(3\le n\le16\); checks that every required word occurs in a circular Euler tour of the claimed length; checks bijectivity of the matching; tests the coefficient identity for the rational generating series through degree fifty; and exhaustively excludes shorter circular words for orders three and four. The program prints `VERIFY_OK` on success.

An independent general min-cost-flow formulation on the **full** binary de Bruijn graph (not restricted to allowed states) was also solved for orders three through sixteen, with exact integer costs matching the formula. This second test is finite corroboration, not an infinite proof. All infinite lower and upper bounds follow from the explicit arguments above.

## Relationship to prior work

Moreno and Matamala's *Minimal de Bruijn Sequence in a Language with Forbidden Substrings* (WG 2004) considers Eulerian, exactly-once de Bruijn sequences for the **periodically admissible** language \(W_F(n)\): a word belongs when its infinite repetition avoids the forbidden set. The present theorem instead covers **every finite** `010`-avoiding word and permits auxiliary edges; transient words in this larger language prevent the same Eulerian exactly-once argument. Their 2007 preprint further describes the restricted-language framework.

Cazaux and Rivals study the Shortest Cyclic Cover of Strings problem, where the output is a **collection** of cyclic strings minimizing total length. That is not the same optimization objective as the connected single-circle problem. The accessible abstract and introductory manuscript material do not establish the formula above; a complete specialized-example check of their full paper remains a priority limitation. Universal-cycle results for restricted words likewise address exact-once cycles under different hypotheses.

Earlier computations for forbidden `000` and `001` concern different forbidden-word equivalence classes. Under word reversal and bit complementation, binary forbidden factors of length three fall into three classes represented by `000`, `001`, and `010`. This result handles the remaining `010` class; the numerical values and all-order bound are not implied by those previous cases. Search and priority checking cannot rule out every unindexed source, and the theorem is offered with that qualification.

## Limitations

The result concerns precisely one forbidden binary length-three substring (and its reversal/complement equivalent `101`), a single circular cover, and exact cyclic windows. It does not give a complete classification of all minimizing cycles, nor claim corresponding formulas for other finite languages or larger alphabets. Finite program checks do not replace the all-order proof. The earliest individually dated public record of the cited WG 2004 paper is its print proceedings publication on December 21, 2004; the work was presented at the June 21–23, 2004 workshop, whose individual presentation date is not established here.

## References

1. E. Moreno and M. Matamala, *Minimal de Bruijn Sequence in a Language with Forbidden Substrings*, WG 2004, LNCS 3353, pp. 168–176. DOI: https://doi.org/10.1007/978-3-540-30559-0_14. Authors' preprint: https://www.dim.uchile.cl/~emoreno/publicaciones/PREPRINTS/preprint-LNCS04-Minimal_de_Bruijn_sequence_in_a_language_with_forbidden_substrings.pdf .
2. E. Moreno and M. Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings*, arXiv:0711.1695, publicly submitted 2007-11-12. https://arxiv.org/abs/0711.1695 .
3. B. Cazaux and E. Rivals, *A Linear Time Algorithm for Shortest Cyclic Cover of Strings*, Journal of Discrete Algorithms 2016, DOI: https://doi.org/10.1016/j.jda.2016.05.001 .
4. G. Gardner and A. Godbole, *Universal Cycles of Restricted Words*, arXiv:1711.07029. https://arxiv.org/abs/1711.07029 .
