# Frozen optimal injective colorings of \(K_b\times C_{2b+3}\)

## Finding

For every integer \(b\ge3\), put \(n=2b+3\), \(q=2b+1\), and let \(G_b=K_b\times C_n\) be the direct (categorical) product of a labeled \(b\)-clique with a labeled \(n\)-cycle. The injective chromatic number is \(\chi_i(G_b)=q\). Consider the reconfiguration graph whose vertices are all injective colorings \(V(G_b)\to\{1,\ldots,q\}\), with an edge for a change at exactly one graph vertex. Its **complete degree distribution** is

\[
\begin{array}{c|c}
\text{reconfiguration degree}&\text{number of optimal injective colorings}\\\hline
0 & \dfrac{n(b-1)(b-2)}{6}\,q!\,(b!)^n\\
b & n(b-1)\,q!\,(b!)^n\\
2b & n\,q!\,(b!)^n.
\end{array}
\]

Thus precisely the degree-zero colorings are frozen under single-vertex recoloring. The fraction of all optimal injective colorings that are frozen is
\[
\frac{(b-1)(b-2)}{(b+1)(b+2)}\longrightarrow1.
\]
Every optimal coloring is also classified by one independent \(b\)-set on a cycle, as described in the proof. The total number of optimal colorings is \(\dfrac{n(b+1)(b+2)}{6}\,q!\,(b!)^n\).

## Assumptions and scope

All graphs are finite, loopless, undirected, and their vertices are distinguished. The vertices of \(K_b\) are \(\{1,\dots,b\}\); the vertices of \(C_n\) are \(\mathbb Z/n\mathbb Z\), with edges between consecutive residues. An injective coloring assigns different colors to every pair of **distinct** vertices with a common neighbor; it need not be proper on edges. The product \(G_b\) joins \((a,i)\) to \((a',j)\) exactly when \(a\ne a'\) and \(i-j\equiv\pm1\pmod n\). The palette \(\{1,\ldots,q\}\) consists of named colors, not colors identified up to permutation. A recoloring changes exactly one vertex's color, leaving every other vertex fixed and preserving the injective condition with the same palette. The theorem concerns \(b\ge3\) and this optimal palette only.

## Proof

**Step 1: reduction and optimality.** For \(b\ge3\), two distinct vertices of \(G_b\) have a common neighbor precisely when their cycle coordinates are equal or differ by \(\pm2\pmod n\). Indeed, in the clique coordinate a third vertex different from any two chosen coordinates exists, while a common neighbor in the cycle coordinate requires equal or two-step positions. Consequently each fiber \(K_b\times\{i\}\) must use \(b\) distinct colors, and two fibers distance two around \(C_n\) must have disjoint color sets. Since multiplication by \(2\) permutes \(\mathbb Z/n\mathbb Z\), put
\[
P_t=\{f(a,2t):1\le a\le b\}.
\]
Then \(f\) is injective exactly when \(|P_t|=b\) and \(P_t\cap P_{t+1}=\varnothing\) for every \(t\in\mathbb Z/n\mathbb Z\). For each color \(c\), the support \(S_c=\{t:c\in P_t\}\) is independent in \(C_n\), hence \(|S_c|\le b+1\). A palette with \(r\) colors can cover at most \(r(b+1)\) of the \(bn=q(b+1)-1\) colored positions. Thus \(r\ge q\). We construct such colorings below, proving \(\chi_i(G_b)=q\).

**Step 2: the one-defect classification.** In an injective \(q\)-coloring, the sum of the \(q\) support sizes is \(bn=q(b+1)-1\). Therefore precisely one color (the *deficient color*) has support size \(b\), and every other color has support size \(b+1\). No color is unused. Write \(D\) for the deficient color's independent \(b\)-vertex support. Denote by \(e_t=\{t,t+1\}\) the \(n\) edges of the reindexed cycle. For any independent support \(S\), call \(e_t\) *uncovered* if neither endpoint belongs to \(S\). A size-\(b+1\) support leaves exactly one uncovered edge, and there is exactly one such maximum independent set \(M_t\) whose uncovered edge is \(e_t\) (alternate around the remaining cycle). The support \(D\) leaves exactly three uncovered edges; call their set \(U(D)\).

At each edge \(e_t\), the disjoint palettes at its endpoints use \(2b=q-1\) different colors. Thus exactly one color is absent from both endpoints. This absent color is precisely a color whose support leaves \(e_t\) uncovered. Since the deficient support already leaves the three edges in \(U(D)\), no maximum support can leave any of those edges uncovered. Each other edge must be the unique missing edge of one maximum support; because all maximum supports have distinct uncovered edges, the complete support multiset is exactly
\[
\{D\}\ \cup\ \{M_t:e_t\notin U(D)\}.
\]
Conversely, choose any independent \(b\)-set \(D\) and these \(2b\) maximum independent supports. Exactly one of the resulting \(q\) supports misses any edge \(e_t\), so its endpoints together belong to exactly \(q-1=2b\) supports. Supports are independent, hence the palette sizes satisfy \(|P_t|+|P_{t+1}|=2b\). As the cycle has odd order, these equations force \(|P_t|=b\) for every \(t\). Thus this construction always produces a valid palette profile. Naming the \(q\) supports as distinct colors takes \(q!\) choices; independently assigning the \(b\) colors of each fiber to its \(b\) labeled vertices takes \((b!)^n\) choices. These operations are reversible and do not overcount.

**Step 3: exact recoloring-degree criterion.** Let \(s_t\) denote the sole color absent from \(P_t\cup P_{t+1}\). A vertex in fiber \(t\) may receive a new color if and only if that color belongs to
\[
\{1,\ldots,q\}\setminus(P_{t-1}\cup P_t\cup P_{t+1}).
\]
Since \(s_{t-1}\) and \(s_t\) are respectively the unique missing colors for the two incident cycle edges, the allowed set has one element exactly when \(s_{t-1}=s_t\), and is empty otherwise. Every maximum support misses exactly one edge, so equality of these two consecutive spare colors can occur only when both edges are missed by the deficient support \(D\). In other words, the vertex \(t\) and both its immediate cycle neighbors lie outside \(D\). If this occurs, each of the \(b\) separately labeled vertices in that fiber admits precisely one nontrivial recoloring. Thus
\[
\deg_{\mathrm{rec}}(f)=b\sum_{j=1}^{b}\max\{0,g_j-3\},
\]
where \(g_1,\ldots,g_b\ge2\) are the successive clockwise distances between consecutive elements of \(D\) on \(C_n\), and \(\sum_jg_j=n=2b+3\).

**Step 4: gap types and exact counts.** Put \(h_j=g_j-2\ge0\). The positive excesses sum to \(3\); the only types, up to their positions among the \(b\) gaps, are \((3)\), \((2,1)\), and \((1,1,1)\). In the first type one gap has length \(5\), hence the degree is \(2b\); in the second a length-\(4\) gap and a length-\(3\) gap give degree \(b\); in the third three length-\(3\) gaps give degree \(0\). Choosing an oriented starting member of \(D\), then dividing by its \(b\) choices of starting member, yields respectively
\[
\frac nb\,b=n,\qquad
\frac nb\,b(b-1)=n(b-1),\qquad
\frac nb\,{b\choose3}=\frac{n(b-1)(b-2)}6
\]
independent supports \(D\) of these types. Multiply by \(q!(b!)^n\) using Step 2. These are all possibilities, so the degree distribution and frozen fraction follow. In particular \(\sum_D1=n(b+1)(b+2)/6\), as also follows from \(\frac nb{b+2\choose3}\).

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It independently enumerates every independent deficient support for \(3\le b\le8\), reconstructs every claimed maximum support, verifies the cycle-palette conditions, computes every permitted one-vertex recoloring directly from the palettes, and compares all degree histograms to the stated formulas. It also constructs literal neighborhoods in \(K_b\times C_n\) for \(b=3,4\) to check the two-step reduction, and independently counts all valid labeled palette profiles by a closed-walk transfer computation for \(b=3,4\). Run `python3 verify.py` to reproduce the finite checks. These finite checks corroborate but do not replace Steps 1–4, which prove every \(b\ge3\) case.

## Relationship to prior work

Samadi–Soltankhah–Yero (2023) study injective colorings of graph products through two-step graphs and determine the injective chromatic number for products of two cycles; that work supplies the motivating framework, but does not state this optimal-coloring recoloring-degree distribution on \(K_b\times C_n\). Dong–Royle–Wagner (2011) study chromatic polynomials of rings of four cliques. The graph of color conflicts here is a longer ring of \(n=2b+3\) cliques; chromatic-polynomial evaluations count colorings, but do not by themselves determine which colorings are isolated under single-vertex recoloring. Brewster–Lee–Moore–Noel–Siggers (2017) investigate general frozen graph-homomorphism colorings and decision complexity, not the exact families and counts here. Bonamy–Bousquet–Perarnau (2018) bound the frozen fraction at the \((\Delta+1)\)-color regime; our conflict graph has degree \(3b-1\) but uses the smaller optimal palette \(2b+1\), so their theorem neither yields nor contradicts the limiting frozen fraction here.

## Limitations

The proof does not describe recoloring component sizes, reachability among non-frozen colorings, non-optimal palettes, or the cases \(b=1,2\). The estimates are exact for a fixed named palette and labeled graph vertices; quotienting by graph automorphisms or color permutations changes counts. No independent external scientific audit is claimed. The literature comparison concerns inspected primary sources and recorded searches, and cannot exclude every unpublished or unindexed equivalence.

## References

1. B. Samadi, N. Soltankhah, I. G. Yero, *Injective coloring of product graphs*, arXiv:2306.01488v1 (first public 2023-06-02), https://arxiv.org/abs/2306.01488.
2. F. M. Dong, G. Royle, D. Wagner, *Chromatic Roots of a Ring of Four Cliques*, Electronic Journal of Combinatorics **18** (2011), P151, https://doi.org/10.37236/638.
3. R. C. Brewster, J.-B. Lee, B. Moore, J. A. Noel, M. Siggers, *Graph Homomorphism Reconfiguration and Frozen H-Colourings*, arXiv:1712.00200v1 (2017), https://arxiv.org/abs/1712.00200.
4. M. Bonamy, N. Bousquet, G. Perarnau, *Frozen \((\Delta+1)\)-colourings of bounded degree graphs*, arXiv:1811.12650v1 (2018), https://arxiv.org/abs/1811.12650.
