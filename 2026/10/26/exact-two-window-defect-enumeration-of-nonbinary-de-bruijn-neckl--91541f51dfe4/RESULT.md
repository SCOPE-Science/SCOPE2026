# Exact two-window-defect enumeration of nonbinary de Bruijn necklaces

## Finding

For every labeled alphabet of cardinality \(q\ge3\) and every \(n\ge2\), let \(T_{q,n}\) count rotation classes of cyclic words of length \(q^n-2\) in which all cyclic length-\(n\) factors are distinct. Put
\[
B_{q,n}=\frac{(q!)^{q^{n-1}}}{q^n},
\]
the classical count of ordinary de Bruijn necklaces. Then
\[
\boxed{T_{q,n}=B_{q,n}\frac{q^2+(-1)^{n-1}q^{2-n}}{q^2-1}.}
\]

Exactly two length-\(n\) words are absent. They are necessarily either two **distinct constant words**, or the two **alternating words on two distinct letters**, of length \(n\). For each fixed unordered alphabet pair \(\{a,b\}\), the numbers of necklaces with respectively missing \(a^n,b^n\), or missing both \(abab\cdots\) and \(baba\cdots\), are
\[
\boxed{L_{q,n}=\frac{B_{q,n}}{(q-1)^2},\qquad
A_{q,n}=\frac{B_{q,n}}{(q-1)^2}\frac{q-1+2(-1/q)^{n-1}}{q+1}.}
\]
Here the alternating words are truncated to length \(n\). Both pair types occur for every \(q\ge3,n\ge2\). Consequently \(T_{q,n}=\binom q2(L_{q,n}+A_{q,n})\). Such necklaces are **exactly** the balanced arbitrary-length de Bruijn analogs \(P^{(q)}_{q^n-2}\) of Nellore and Ward.

This is a nonbinary enumeration result: the binary specialization is reproduced for comparison but is not presented as new (see Relationship to prior work). For illustration, \(T_{3,2}=24\), \(T_{3,3}=435456\), and \(T_{4,2}=20736\). As \(n\to\infty\) for fixed \(q\), the proportions of the two missing-pair types approach \((q+1)/(2q)\) and \((q-1)/(2q)\), respectively.

## Assumptions and scope

A cyclic word (necklace) is identified only under cyclic rotation, not under alphabet relabeling or reversal. Each cyclic length-\(j\) factor is taken with indices modulo its total length. Thus, for a word of length \(M\), there are exactly \(M\) indexed factors of each positive length. Two words of the same length with identical symbols but starting at different cyclic positions represent one necklace. The alphabet symbols are distinct labeled objects. All counts are exact integers, even though their displayed expressions use rational factors. The theorem covers all integers \(q\ge3\), \(n\ge2\); it does not enumerate shorter deficits \(q^n-d\) for arbitrary \(d\ge3\).

## Proof

**1. The only balanced missing pairs.** Let \(m=n-1\), and consider the directed de Bruijn graph \(G\) whose vertices are the \(q^m\) length-\(m\) words. Each length-\(n\) word labels one directed edge from its length-\(m\) prefix to its length-\(m\) suffix. Each vertex has in-degree and out-degree \(q\), including loops. A cyclic word with mutually distinct length-\(n\) windows traces a single edge-simple closed Euler tour in \(G\) with exactly two edges deleted. Conversely such a tour spells precisely one necklace. Since every edge label is distinct, these tours have no nontrivial cyclic period.

The remaining graph must have equal in- and out-degrees at every vertex. Therefore the two deleted edges themselves constitute a balanced directed multigraph. A balanced directed graph with two distinct edges is either two loops at distinct vertices or a directed two-cycle. The only loops in \(G\) correspond to constant words \(a^n\). A directed two-cycle is necessarily based at the two alternating length-\(m\) words on distinct letters \(a,b\), and its edge labels are the two alternating length-\(n\) words. Conversely, precisely these missing-edge pairs are balanced.

**2. Euler-tour normalization.** Write \(V=q^m\) and \(F=((q-1)!)^V\). The directed BEST theorem counts cyclic Euler tours of an Eulerian graph with distinguished edge labels by the number of in-arborescences rooted at any fixed vertex, multiplied by \(\prod_v(d_v^+-1)!\). The familiar de Bruijn enumeration implies the rooted arborescence count of \(G\) is
\[
t_0=\frac{B_{q,n}}{F}=q^{V-n}.
\]
For every admissible deleted pair, two distinct vertices have new out-degree \(q-1\); every other vertex remains at degree \(q\). Consequently the BEST factorial product is \(F/(q-1)^2\). The only variable factor is the spanning in-arborescence count after edge removal. A zero arborescence count correctly signals disconnectedness; for \(q\ge3\) all the ratios below are positive and an Euler tour exists.

**3. Two removed loops.** Loops belong to no directed arborescence and cancel in the out-Laplacian. Thus removing loops at \(a^m\) and \(b^m\) does not change the arborescence count, which stays \(t_0\). Applying BEST gives \(t_0F/(q-1)^2=L_{q,n}\).

**4. An alternating two-cycle.** Let \(u\) and \(v\) be the two alternating length-\(m\) vertices. Denote the transition matrix of the uniform edge-following random walk on \(G\) by \(P\), and the out-Laplacian by \(L=q(I-P)\). Put \(J=\mathbf1\mathbf1^\top/V\) and \(w=e_u-e_v\). Removing the two edges between \(u\) and \(v\) replaces \(L\) by \(L'=L-ww^\top\). Since the original graph is Eulerian and \(L+J\) is invertible, the matrix determinant lemma and the directed matrix-tree theorem give
\[
\frac{t(G')}{t(G)}=\frac{\det(L'+J)}{\det(L+J)}=1-w^\top(L+J)^{-1}w.
\]
The random walk forgets its entire starting vertex after \(m\) steps: \(P^m=J\). Therefore, on vectors orthogonal to \(\mathbf1\),
\[
(L+J)^{-1}=\frac1q\sum_{k=0}^{m-1}(P^k-J).
\]
Indeed multiplication by \(L\) telescopes to \(I-P^m=I-J\); both sides vanish on constants after accounting for the inverse of \(J\). For \(0\le k<m\), shifting an alternating length-\(m\) word by \(k\) places retains the same vertex when \(k\) is even and gives the opposite vertex when \(k\) is odd, provided the \(k\) newly appended letters match; that event has probability \(q^{-k}\). Thus
\[
w^\top P^kw=2(-1/q)^k,
\qquad
\frac{t(G')}{t(G)}=1-\frac2q\sum_{k=0}^{m-1}(-1/q)^k
=\frac{q-1+2(-1/q)^m}{q+1}=:R_{q,m}.
\]
For \(q\ge3\), \(R_{q,m}>0\), proving all alternating cases admit tours. BEST now gives \(t_0R_{q,m}F/(q-1)^2=A_{q,n}\).

**5. The closed form.** There are exactly \(\binom q2\) choices of each missing-pair type, and different missing pairs cannot produce the same necklace. Adding yields
\[
T_{q,n}=\binom q2\frac{B_{q,n}}{(q-1)^2}(1+R_{q,n-1})
=B_{q,n}\frac{q^2+(-1)^{n-1}q^{2-n}}{q^2-1}.
\]
The stated limiting proportions follow by sending \(n\to\infty\) in \(R_{q,n-1}\).

**6. Equivalence to balanced necklaces.** In the above classification the two missing length-\(n\) words start with distinct symbols. For each \(1\le j<n\), every \(j\)-word \(x\) is the prefix of precisely \(q^{n-j}\) possible length-\(n\) words, and at most one of these is missing, so its cyclic occurrence count is \(q^{n-j}\) or \(q^{n-j}-1\). These are exactly \(\lfloor(q^n-2)/q^j\rfloor\) and \(\lceil(q^n-2)/q^j\rceil\), because \(q^j\ge3\). For \(j=n\), all counts are \(0\) or \(1\); for \(n<j\le q^n-2\), every longer cyclic window is uniquely determined by its first length-\(n\) symbols and therefore also has multiplicity \(0\) or \(1\). Hence the word satisfies all balanced-necklace conditions. Conversely, balance at length \(n\) forces each length-\(n\) word to occur at most once, so the two notions coincide.

## Verification

The companion standalone Python program `verify.py` uses arbitrary-precision integer arithmetic and no dependencies. It computes directed Laplacian cofactors with fraction-free Bareiss elimination for nine alphabet/order cases: \((q,n)\in\{(2,2),(2,3),(2,4),(2,5),(2,6),(3,2),(3,3),(4,2),(4,3)\}\). It compares the resulting BEST counts, independently of the closed-form calculation, against both missing-pair formulas. It also enumerates every possible word and reduces by rotation for \((2,2),(2,3),(2,4),(3,2)\), checking every missing pair and all balanced occurrence counts. The actual completed run ended with `VERIFY_OK tree_cases=9 exhaustive_cases=4 total_checks=13`. Examples: ternary order three has \(93312\) necklaces per fixed constant pair and \(51840\) per fixed alternating pair, giving \(435456\) altogether. These finite checks are not substitutes for the unrestricted proof above.

## Relationship to prior work

Gabric, Holub and Shallit (first public preprint March 13, 2019) define generalized de Bruijn words and explicitly identify near-power enumeration as a difficult open direction; their binary tables include \(20\), \(2816\), and \(88080384\) at lengths \(14\), \(30\), and \(62\). Nellore and Ward (2021 preprint; 2022 conference version) define the stronger balanced \(P_L^{(q)}\) necklaces and expressly ask for counts over all parameters. Cameron, Gündoğan and Sawada (2022) give constructive cut-down algorithms, not an all-parameter enumeration. Alhakim (2022) provides nonbinary constructions with prescribed missing constant windows, not the two-defect census or the full count.

**Binary precedent is acknowledged, not claimed:** Fredricksen's 1982 survey reports an older proposed binary count; later work documents a problem in the printed expression. A MathOverflow answer dated October 19, 2026 gives the corrected **binary** \(2^n-2\) count and a related Laplacian-rank-one argument. The present scope and originality claim concern \(q\ge3\), including complete counts and type-resolved missing-pair distributions for all nonbinary alphabet sizes. The binary formula arises from the same algebra by substitution but is prior coverage, not a newly obtained special case.

## Limitations

The result counts rotation classes only, with alphabet symbols labeled. It does not quotient by reversal or symbol permutations, does not classify arbitrary larger defects, and does not yield the full enumeration for every length in the cited open problem. Existing binary work is excluded from the claimed novelty. The originally published 1982 source could not be inspected in full despite searches for publicly accessible copies and institutional retrieval; its binary-only formula was compared through later primary research and the accessible scholarly discussion. An unindexed nonbinary enumeration remains an originality risk. The proof of the infinite theorem is mathematical; finite code checks do not establish independent validation or publication priority.

## References

1. Daniel Gabric, Štěpán Holub, Jeffrey Shallit, *Maximal State Complexity and Generalized de Bruijn Words*, first public 2019-03-13, arXiv:1903.05442, especially Sections 2 and 4. https://arxiv.org/abs/1903.05442
2. Abhinav Nellore, Rachel Ward, *Arbitrary-Length Analogs to de Bruijn Sequences*, first public 2021-08-17, arXiv:2108.07759; CPM 2022, Definition 1 and Discussion Question 1. https://arxiv.org/abs/2108.07759
3. Ben Cameron, Aysu Gündoğan, Joe Sawada, *Cut-Down de Bruijn Sequences*, first public 2022-05-05, arXiv:2205.02815. https://arxiv.org/abs/2205.02815
4. Abbas Alhakim, *Nonbinary Counterparts of the Prefer-Same and Prefer-Opposite de Bruijn Sequences*, first public 2022-06-09, arXiv:2206.04408. https://arxiv.org/abs/2206.04408
5. Harold Fredricksen, *A Survey of Full Length Nonlinear Shift Register Cycle Algorithms*, SIAM Review 24 (1982), pp. 195–221, especially Section 2c; historical binary claim, full original not inspected. DOI:10.1137/1024041.
6. Timothy Chow, *Cycles of length \(2^n-2\) in the De Bruijn graph*, MathOverflow question 2016-01-04 and answer 2026-10-19 (binary case). https://mathoverflow.net/questions/227666/cycles-of-length-2n-2-in-the-de-bruijn-graph/516176
