# Majority-stable-set polynomial and colouring phases for directed cycle blow-ups

## Finding

For all integers \(d\ge3\) and \(m\ge1\), let \(D_{d,m}\) be the directed cycle with each vertex replaced by an independent layer of \(m\) labelled vertices, with every possible arc directed from each layer into the succeeding layer. A subset is *majority-stable* when every vertex it contains has at most half of its outneighbours also in the subset. Write \(F_{d,m}(z)=\sum_{S}z^{|S|}\), summing over majority-stable subsets of \(D_{d,m}\).

Set
\[
t=\lfloor m/2\rfloor,\qquad A(z)=(1+z)^m,\qquad B(z)=\sum_{j=0}^{t}\binom mj z^j.
\]
Then the complete counting polynomial is
\[
\boxed{F_{d,m}(z)=\operatorname{tr}\!\left(\begin{pmatrix}1&A(z)-1\\1&B(z)-1\end{pmatrix}^{d}\right).}
\]
Equivalently, the polynomial sequence with fixed \(m\) obeys \(F_{0,m}=2\), \(F_{1,m}=B\), and \(F_{d,m}=BF_{d-1,m}+(A-B)F_{d-2,m}\) for \(d\ge2\). Only the \(d\ge3\) terms describe the cycle blow-ups.

The maximum size is \(\alpha_{\mathrm{maj}}(D_{d,m})=\lfloor dm/2\rfloor\). Its coefficient in the polynomial is precisely
\[
[z^{\lfloor dm/2\rfloor}]F_{d,m}(z)=
\begin{cases}
2,&m\text{ odd},\ d\text{ even};\\
d\binom{m}{(m-1)/2},&m\text{ odd},\ d\text{ odd};\\
\displaystyle\sum_{k=0}^{\lfloor d/2\rfloor}\frac{d}{d-k}\binom{d-k}{k}\binom{m}{m/2}^{d-2k},&m\text{ even}.
\end{cases}
\]
In particular, the optimum fractional majority colouring is
\[
\boxed{\chi^*_{\mathrm{maj}}(D_{d,m})=\frac{dm}{\lfloor dm/2\rfloor}=\begin{cases}2,&dm\text{ even};\\2dm/(dm-1),&dm\text{ odd},\end{cases}}
\]
and the integral majority chromatic number is \(3\) exactly when \(d,m\) are both odd, and otherwise \(2\). For named colours red and blue, the exact number of valid two-colourings is \(\binom m{m/2}^{d}+2\mathbf1_{\{d\text{ even}\}}\) when \(m\) is even, \(2\) when \(m\) is odd and \(d\) even, and zero otherwise.

## Assumptions and scope

The graph is a finite simple directed graph without loops. Its vertices are partitioned into \(L_i\) for \(i\in\mathbb Z/d\mathbb Z\), each \(L_i\) containing exactly \(m\) distinct, labelled vertices. For every \(u\in L_i\) and \(v\in L_{i+1}\) there is exactly the arc \(u\to v\), and no other arcs. Thus each vertex has outdegree \(m\). The term majority-stable means \(|N^+(v)\cap S|\le\lfloor m/2\rfloor\) for **each \(v\in S\)**; vertices outside \(S\) are unrestricted. A majority colouring partitions vertices into such sets. A fractional majority colouring is a nonnegative weighted family of majority-stable sets covering every vertex to weight at least one, with cost the sum of weights. The polynomial counts the empty subset, and every nonempty subset only once, by its labelled vertices.

## Proof

**1. Layer admissibility and full generating polynomial.** Put \(x_i=|S\cap L_i|\). Every selected vertex in \(L_i\) sees all \(x_{i+1}\) selected vertices in the next layer. Hence
\[
S\text{ is majority-stable}\quad\Longleftrightarrow\quad
\text{for every }i,\quad x_i=0\text{ or }x_{i+1}\le t.
\]
A nonempty layer has weight \(A(z)-1\) if its preceding layer is empty, and weight \(B(z)-1\) if its preceding layer is nonempty; an empty layer always has weight one. Using states empty/nonempty gives the transition matrix
\[
M(z)=\begin{pmatrix}1&A(z)-1\\1&B(z)-1\end{pmatrix}.
\]
A cyclic sequence of \(d\) states contributes the product of its transition weights. The trace of \(M(z)^d\) sums these products over all cyclic state sequences with a fixed first layer; each selection of labelled vertices contributes exactly one monomial. This proves the matrix identity. Because \(\operatorname{tr}(M)=B\) and \(\det M=B-A\), Cayley--Hamilton yields the recurrence with initial traces \(2,B\). All identities hold as polynomial identities with integer coefficients, so no numerical diagonalization or formal division is needed.

**2. Upper bound and extremal structure.** Call a layer *heavy* when it contains more than \(t\) selected vertices. Every heavy layer has an empty predecessor by the preceding admissibility criterion. Two heavy layers cannot be consecutive, so the preceding-empty/heavy pairs are vertex-disjoint edges of the cyclic layer graph. If there are \(k\) such pairs, then \(0\le k\le\lfloor d/2\rfloor\). Each pair contains at most \(m\) selected vertices, whereas each of the remaining \(d-2k\) layers has at most \(t\). Consequently
\[
|S|\le km+(d-2k)t=dt+k(m-2t)\le\lfloor dm/2\rfloor.
\]
For even \(m\), selecting \(m/2\) vertices in every layer attains the bound. For odd \(m\) and even \(d\), alternating full and empty layers attains it. When both are odd, take \((d-1)/2\) disjoint empty/full adjacent pairs and select exactly \(t\) vertices in the sole remaining layer. Each construction is admissible, so the maximum is sharp.

Equality also classifies all extremizers. In any preceding-empty/heavy pair, equality requires that the heavy layer be full. Every unpaired layer must have exactly \(t\) selected vertices. When \(m\) is even, \(m-2t=0\), so an arbitrary matching of \(k\) edges of the \(d\)-cycle specifies the full/empty pairs and every uncovered layer is half-filled. Conversely every such configuration attains equality, with no duplicate representation because precisely the heavy layers identify the pairs. The number of \(k\)-edge matchings of \(C_d\) is
\[
\frac{d}{d-k}\binom{d-k}{k}
\]
for \(0\le k\le\lfloor d/2\rfloor\). This standard identity follows by counting a cyclically marked first unmatched vertex or, equivalently, counting \(k\) distinct nonconsecutive positions on a \(d\)-cycle. Every uncovered layer admits \(\binom m{m/2}\) labelled half-fills, proving the even-\(m\) count.

For odd \(m\), \(m-2t=1\), so equality forces the maximum possible number of pairs. If \(d\) is even, the two alternating perfect matchings are the only possibilities. If \(d\) is odd, there are exactly \(d\) matchings with \((d-1)/2\) edges, each leaving one layer unpaired; this layer has \(\binom m{(m-1)/2}\) choices. These yield the remaining leading-coefficient formulas.

**3. Exact fractional optimum.** For any fractional majority colouring of total weight \(w\), summing the vertex coverage inequalities gives \(dm\le\alpha_{\mathrm{maj}}w\). Conversely, the cyclic layer rotation and independent within-layer permutations act transitively on all \(dm\) vertices and preserve the majority-stable family. Choose a maximum-size set \(S\) and average its images under this finite transitive automorphism group. Every vertex occurs in the same fraction \(\alpha_{\mathrm{maj}}/(dm)\) of those images, so multiplying the associated probability distribution of stable sets by \(dm/\alpha_{\mathrm{maj}}\) is a fractional majority colouring achieving the lower bound. This proves the exact fractional value.

**4. Integral phase and two-colouring census.** In any two-colouring, record the number \(r_i\) of red vertices in layer \(L_i\). If a layer contains both colours, then each colour occurs in the preceding layer, forcing the next layer to have at most \(t\) red and at most \(t\) blue vertices. Thus \(m\le2t\), which requires even \(m\); the next layer is then exactly balanced. Inducting around the cycle shows that every layer is balanced. These choices give \(\binom m{m/2}^d\) distinct named two-colourings when \(m\) is even. Otherwise, all layers are monochromatic, and the majority rule forces adjacent layers to have opposite colours. This is possible if and only if \(d\) is even, with exactly two alternating patterns. These patterns are disjoint from the balanced family. This gives the complete two-colouring census and the sharp obstruction when both \(d,m\) are odd. A proper colouring of the underlying cycle with three colours, assigning each layer its cycle colour, is always a majority colouring, so the integral minimum is three precisely in the obstructed case. A single colour never satisfies the majority rule because every vertex has positive outdegree.

## Verification

The accompanying pure-Python program `verify.py` independently computes the polynomial by three methods: the claimed matrix-trace recurrence; a weighted enumeration of every layer-occupancy vector; and, for \(dm\le14\), exhaustive enumeration of every labelled vertex subset. It checks the leading coefficient against the matching formulas and independently counts all named two-colourings by their red occupancies. Execution returned `VERIFY_OK`: 72 recurrence/leading-coefficient/two-colouring comparisons across 24 parameter pairs \(3\le d\le8,1\le m\le4\), and 14 exhaustive labelled-subset comparisons. These finite experiments corroborate the proof but do not replace its unrestricted argument.

Run from the package directory with `python3 verify.py`; no external packages or network are required.

## Relationship to prior work

Ben-Ameur and Maddaloni (arXiv:2610.11997v1, first public October 8, 2026) formalize fractional majority colouring and improve general upper bounds, including for digraphs with a directed cycle factor. Their bounds imply no exact value or enumerator for the full cyclic-layer family. Anastos, Lamaison, Steiner and Szabó (arXiv:1911.01954, later *Electronic Journal of Combinatorics* 28(2), P2.31) prove general sparse-digraph majority-colouring and fractional bounds; their result that a digraph with no odd directed cycle is majority two-colourable already gives a two-colour existence statement for the even-\(d\) subfamily. That special existence implication is not claimed as new here. The present result gives the complete majority-stable-set polynomial, all maximum-set counts, a vertex-transitivity-derived fractional optimum, and an exact ordinary-colouring and two-colouring census throughout all \(d,m\). The matrix enumeration is closely related to standard transfer-matrix and cyclic-matching methods; no originality is claimed for those techniques in general.

## Limitations

The theorem is restricted to **equal** independent layer sizes and complete arcs between successive layers. It makes no assertion for unequal layers, additional arcs, weighted outneighbours, list colouring, or a classification of all optimal fractional-colouring weight vectors. The leading-coefficient census counts labelled vertex subsets, while the two-colouring census treats red and blue as named colours. A similar evaluation might exist in unindexed prior work; a literature search is evidence of comparison rather than proof of historical uniqueness. Independent scientific validation has not yet been performed.

## References

1. W. Ben-Ameur and A. Maddaloni, *Fractional majority coloring of digraphs: bounds and inapproximability*, arXiv:2610.11997v1 (first submitted 2026-10-08), https://arxiv.org/abs/2610.11997.
2. M. Anastos, A. Lamaison, R. Steiner and T. Szabó, *Majority Colorings of Sparse Digraphs*, arXiv:1911.01954; *Electronic Journal of Combinatorics* 28(2), P2.31 (2021), https://arxiv.org/abs/1911.01954.
