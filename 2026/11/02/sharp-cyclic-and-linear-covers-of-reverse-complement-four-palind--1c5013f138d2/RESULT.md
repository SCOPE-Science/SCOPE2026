# Sharp cyclic and linear covers of reverse-complement four-palindromes

## Finding

Let \(\Sigma\) be a labeled alphabet of even cardinality \(q\ge 2\), equipped with a fixed-point-free involution \(a\mapsto\bar a\). Consider the \(q^2\) length-four reverse-complement palindromes
\[
\mathcal P_q=\{T_{a,b}=a b\bar b\bar a:a,b\in\Sigma\}.
\]
Every member must appear as an **oriented contiguous factor**; reversal or complementation of a factor does not substitute for literal appearance. The exact minimum lengths of a circular cover and a linear cover are
\[
\boxed{L_{\rm cyc}(q)=\frac{5q^2-q}{2}},\qquad
\boxed{L_{\rm lin}(q)=\frac{5q^2-q+2}{2}}.
\]
In particular, with the Watson–Crick pairing \(A\leftrightarrow T\), \(C\leftrightarrow G\), the minima are \(38\) and \(39\). A circular witness is

`AATTAATATACGTACCGGCCGCGCATGCAGCTAGATCG`

and a linear witness is

`ATATACGTACCGGCCGCGCATGCAGCTAGATCGAATTAA`.

Every optimum can be ordered by one selected occurrence of each required factor so that each of the \(q^2/2\) two-target modules described below is traversed internally by its unique cheapest overlap, and consecutive modules overlap in exactly one symbol. This is a necessary structure for selected target occurrences, not a uniqueness assertion about the covering word.

## Assumptions and scope

Lengths count symbols, not the number of distinct factors. A circular word of length \(L\) is indexed modulo \(L\), including boundary-crossing factors; a linear word admits only ordinary nonwrapping factors. There are no restrictions on factors outside \(\mathcal P_q\), and extra occurrences of target factors are allowed. The involution has no fixed letters, so \(q\) is necessarily even. The result applies to every such involution, up to renaming the alphabet.

For distinct target words \(X,Y\) of length four, let \(c(X,Y)\) be four minus the length of their longest proper suffix-prefix overlap. This value belongs to \(\{1,2,3,4\}\). Any gap between the starting positions of two consecutive selected target occurrences is at least \(c(X,Y)\). In a circular cover these gaps sum to its length; in a linear cover their sum plus four is at most its length. Thus minimizing total target-transition cost gives rigorous lower bounds even when a cover contains other, unselected occurrences.

## Proof

**1. Exact cheap overlaps and module partition.** Write \(X=T_{a,b}=ab\bar b\bar a\). A distinct next target has three-letter overlap with \(X\) if and only if \(b=\bar a\); in that case the unique successor is \(T_{\bar a,a}\) and costs one. These are the \(q\) *special* alternating targets \(T_{a,\bar a}\), partitioned into \(q/2\) two-target modules
\[
\{T_{a,\bar a},T_{\bar a,a}\}.
\]
If \(b\ne\bar a\), there is no three-letter overlap. The unique two-letter-overlap successor is \(T_{\bar b,\bar a}\), a distinct *ordinary* target. The \(q^2-q\) ordinary targets partition into \(q(q-1)/2\) two-target modules
\[
\{T_{a,b},T_{\bar b,\bar a}\},\qquad b\ne\bar a.
\]
Each ordinary module is a reciprocal pair of cost-two transitions; each special module is a reciprocal pair of cost-one transitions. All other transitions leaving an ordinary target cost at least three, as do all other transitions leaving a special target.

**2. Circular lower bound.** Choose one occurrence of each of the \(q^2\) different targets in cyclic order. Their successor relation is a single directed Hamiltonian cycle. Since the two cheapest transitions of each module form an isolated directed two-cycle, at least one target from every module must use a transition to a different module. Begin with the sum of individual minimum outgoing costs,
\[
B=2(q^2-q)+q=2q^2-q.
\]
An ordinary module must incur at least one excess cost of one; a special module incurs at least one excess cost of two. The chosen tour therefore has cost at least
\[
B+\frac{q(q-1)}2+2\frac q2=\frac{5q^2-q}{2}.
\]
The length of every circular cover is at least this cost.

**3. Linear lower bound.** Choose one occurrence of each target in their linear order. The last target contributes its full four symbols and has no outgoing transition. All modules other than the terminal module still require an outgoing transition costing at least three. If the terminal target is ordinary, the minimum outgoing-cost sum of all selected targets except the last is \(B-2\), and only \(q(q-1)/2-1\) ordinary modules need an excess cost of one. If the terminal target is special, the corresponding baseline is \(B-1\), and only \(q/2-1\) special modules need an excess cost of two. Either calculation gives
\[
L_{\rm lin}(q)\ge 4+B+\frac{q(q-1)}2+q-3
=\frac{5q^2-q}{2}+1.
\]

**4. Constructing sharp circular covers.** Orient an ordinary module by writing \(T_{a,b}\) before \(T_{\bar b,\bar a}\); its internal transition costs two. Regard this oriented module as a directed arc \(a\to b\), since the first target starts with \(a\) and the second ends with \(b\). The reverse orientation represents \(\bar b\to\bar a\). Orient the special module starting with \(T_{a,\bar a}\); its internal transition costs one, and it represents the loop \(a\to a\).

Write the complementary letter pairs as \(\{u_i,v_i\}\), \(v_i=\bar u_i\), for \(1\le i\le q/2\). For each \(i\), orient both within-pair modules as loops \(u_i\to u_i\). For each pair \(i<j\), orient the four ordinary modules between these two complement pairs to represent
\[
u_i\to u_j,\quad u_j\to u_i,\quad
u_i\to v_j,\quad v_j\to u_i.
\]
These are all the modules exactly once: the four indicated arcs represent four different reciprocal-complement pairs, and within each complement pair the two loops represent its two remaining modules. The resulting directed multigraph is balanced and connected on its nonisolated vertices, because every cross-pair arc occurs with its reverse and each later pair is connected to \(u_1\). Consequently it has an Euler circuit. Traverse its modules in Euler order, traversing their internal cheap target pairs. Between successive modules, the last letter of the departing second target equals the first letter of the arriving first target by the arc incidence condition. These two targets belong to different modules, so they have no overlap of length two or three; their overlap is exactly one letter, of cost three.

The Euler traversal contains \(q(q-1)/2\) ordinary internal transitions of cost two, \(q/2\) special internal transitions of cost one, and \(q^2/2\) intermodule transitions of cost three. Thus its circular overlap word has length
\[
2\frac{q(q-1)}2+\frac q2+3\frac{q^2}{2}
=\frac{5q^2-q}{2}.
\]
All \(q^2\) targets occur, proving sharpness. Cut the circular word at any cost-three intermodule transition. All chosen targets then fit in a linear word after adjoining just the first symbol at the far end, so the linear length is \(L_{\rm cyc}(q)+1\), meeting the linear lower bound.

**5. Equality structure.** Equality in either bound forces exactly one transition leaving each nonterminal module (and each module in a circle) to have the minimum possible noncheap cost three, and every remaining intramodule transition to be the unique cost-one or cost-two partner transition. All chosen-occurrence gaps must equal their overlap costs. Thus optimal target orders consist of the modules linked by single-symbol overlaps; for a linear optimum exactly one module forms the terminal pair.

## Verification

`verify.py` implements the construction using a directed Euler circuit, checks that every module occurs exactly once, and directly scans each resulting circular and linear word for all \(q^2\) target factors. It tests every even alphabet size from \(2\) through \(30\). Independently, Held–Karp dynamic programming minimizes the complete directed target-overlap tour and path for \(q=2\) and \(q=4\), recovering \((9,10)\) and \((38,39)\) without assuming the module construction. Run `python verify.py`; the expected terminal marker is `VERIFY_OK`.

The finite checks do not establish the all-alphabet result by themselves. The exhaustive lower-bound and Euler-circuit arguments above are the proof for all even \(q\). The verifier uses only Python's standard library.

## Relationship to prior work

Gabric and Sawada (2018, arXiv:1803.09009) develop concatenation of universal cycles, principally for complete de Bruijn factor families. Chen, Kitaev and Sun (2019, arXiv:1908.01116) study exact-once universal cycles/words after deleting elements from a full factor language. Neither analyzed this all-complement-palindrome shortest *cover*, which permits repeated non-target words and has strictly positive overlap penalties. General approximation results for shortest superstrings with reverse complements (Yamano and Shibuya, 2026) concern arbitrary input sets and approximation ratios; the present target words are individually self-reverse-complementary, so the exact optimum of this special instance is not supplied by those results.

An ordinary length-four palindrome has form \(abba\), in contrast with the present \(ab\bar b\bar a\). The ordinary-palindrome cover lengths do not imply the present lengths: for \(q=4\), this theorem gives \(38\) cyclic symbols, whereas a separate ordinary-palindrome covering theorem gives \(44\). Alternately complementing letters by their absolute positions maps each encountered reverse-complement palindrome to an ordinary palindrome, but it does not give a fixed bijection of the two complete required factor sets across both starting parities, so it is not a transfer of optimal lengths.

## Limitations

The theorem is only about length-four targets and fixed-point-free involutions; it does not give exact shortest covers for longer reverse-complement palindromes or complement maps with fixed points. No claim is made about uniqueness of shortest words or about the exact number of *additional* target occurrences in an optimum. Earlier indexed or unindexed results phrased as restricted superstring, anti-palindrome, involutive universal-cover or Eulerian augmentation questions might be equivalent; this residual literature risk remains for independent review.

## References

1. D. Gabric and J. Sawada, *Constructing de Bruijn sequences by concatenating smaller universal cycles*, arXiv:1803.09009 (first public version 2018-03-23). https://arxiv.org/abs/1803.09009
2. H. Z. Q. Chen, S. Kitaev and B. Y. Sun, *On the probability of existence of a universal cycle or a universal word for a set of words*, arXiv:1908.01116 (first public version 2019-08-03). https://arxiv.org/abs/1908.01116
3. R. Yamano and T. Shibuya, *Improved Approximation Ratios for the Shortest Common Superstring Problem with Reverse Complements*, LIPIcs CPM 2026, Article 15, DOI:10.4230/LIPIcs.CPM.2026.15. https://doi.org/10.4230/LIPIcs.CPM.2026.15
