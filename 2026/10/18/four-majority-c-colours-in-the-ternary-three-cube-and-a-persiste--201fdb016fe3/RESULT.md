# Four majority C-colours in the ternary three-cube and a persistent odd-dimensional improvement

## Finding

Let \(H_d=K_3^{\square d}\), the Cartesian product of \(d\) copies of \(K_3\). A *majority C-colouring* partitions the vertices into nonempty colour classes so that every vertex has at least half its graph neighbours in its own class. Write \(\overline\chi_{\ge}(G)\) for the maximum number of classes in such a partition. Then

\[
\boxed{\overline\chi_{\ge}(H_3)=4.}
\]

Every subset of \(H_3\) of minimum induced degree at least \(3\) has at least six vertices. Moreover, the six-vertex sets with this property are exactly the \(54\) coordinate rectangles inducing \(K_3\square K_2\). In addition, for every integer \(r\ge0\),

\[
\boxed{\overline\chi_{\ge}(H_{2r+3})\ge 4\cdot3^r.}
\]

The latter bound exceeds the general \(3^{r+1}\) lower bound previously known for these ternary odd-dimensional Hamming graphs. The equality claim concerns only dimension three; no optimality is asserted for greater odd dimensions.

## Assumptions and scope

All graphs are finite, undirected, simple. The vertices of \(H_d\) are \(\{0,1,2\}^{d}\), with two vertices adjacent precisely when they differ in one coordinate. Each vertex has degree \(2d\). In dimension three, a colour class must induce minimum degree at least \(3\). The prescribed \(54\)-set classification concerns *subsets* inducing minimum degree three, not all colour classes of arbitrary cardinality. The established source first appeared publicly on 2026-08-27 (UTC); the revised version dated 2026-09-17 is cited for comparison.

## Proof

**Step 1: The local geometry.** Fix a vertex \(v\) of \(H_3\). Its six neighbours split into three two-vertex sets, one for each coordinate direction, and each set induces an edge. No edges join different sets. Thus \(H_3[N(v)]\) is a matching of size three, and every vertex in \(N(v)\) has at most one neighbour in \(N(v)\). For distinct vertices \(u,v\), their number of common neighbours is \(1\) if their Hamming distance is one, \(2\) if it is two, and \(0\) if it is three; in particular, it never exceeds two. Each triangle is a coordinate line: any three pairwise adjacent triples vary in precisely one coordinate.

**Step 2: Every admissible nonempty class has at least six vertices.** Let \(S\ne\varnothing\) and suppose \(\delta(H_3[S])\ge3\). If \(|S|\le3\), the degree requirement is impossible. If \(|S|=4\), every vertex would have the other three as neighbours; this would induce a \(K_4\), whereas \(H_3\) has clique number three. If \(|S|=5\), the degree sum is at least \(15\) and must be even, so some vertex \(v\) has all four other vertices of \(S\) as neighbours. Each of those four vertices has at most one neighbour among the other three, by Step 1, and therefore at most two neighbours inside \(S\), a contradiction. Hence \(|S|\ge6\).

Because \(|V(H_3)|=27\), a majority C-colouring with \(p\) colours has \(6p\le27\), hence \(p\le4\).

**Step 3: Every six-vertex admissible class is a coordinate rectangle.** Suppose \(|S|=6\) and \(\delta(H_3[S])\ge3\). No \(v\in S\) has induced degree five: its other five neighbours, all lying in \(N(v)\), then have induced degree at most two. Nor can \(v\) have degree four: the four members of \(S\cap N(v)\) each have at most one neighbour within \(N(v)\); to reach induced degree three, all four must also be adjacent to the unique sixth vertex \(w\in S\setminus N[v]\). This would make \(v\) and \(w\) share four common neighbours, contrary to Step 1. Therefore \(H_3[S]\) is a cubic graph on six vertices.

The complement of any six-vertex cubic graph is two-regular. A simple two-regular graph on six vertices is either a six-cycle or two disjoint triangles. Consequently the cubic graph is either a triangular prism \(K_3\square K_2\) or \(K_{3,3}\). The latter is impossible: two vertices in the same bipartition class of \(K_{3,3}\) would have three common neighbours in \(H_3\). Hence \(H_3[S]\) is a triangular prism.

Its two triangular faces lie on coordinate lines. If their directions differed, each vertex on one line could have at most one neighbour on the second line in total (for disjoint lines, a coordinate fixed on both must differ, while coincidence in every other coordinate determines at most one pair). A prism needs three disjoint edges between these lines, so they must be parallel. Parallel coordinate lines admit three cross edges exactly when they differ at exactly one of the other fixed coordinates. Thus \(S\) consists of every value in one coordinate, exactly two values in another coordinate, and a fixed value in the third: a \(K_3\square K_2\) coordinate rectangle. Conversely every such rectangle has internal degree \(2+1=3\). Selecting the three-coordinate full direction, the two-value direction, the remaining fixed coordinate's value, and the two chosen values gives exactly \(3\cdot2\cdot3\cdot\binom32=54\) distinct rectangles.

**Step 4: A four-colour construction.** Write vertices as \((x,y,z)\) and assign a colour depending only on \((x,y)\) according to the table

```text
         y=0  y=1  y=2
x=0       A    C    B
x=1       D    D    B
x=2       A    C    A
```

Every cell in the table shares a row or column with at least one other cell of its colour. Fixing a cell and varying \(z\) contributes exactly two same-colour neighbours, and the matching row/column companion contributes at least one more. Thus every vertex has at least three same-colour neighbours among its six neighbours. All four symbols occur, proving \(\overline\chi_{\ge}(H_3)\ge4\). Together with Step 2 this proves equality.

**Step 5: Product amplification.** For any \(r\ge0\), factor \(H_{2r+3}=H_3\square(H_2)^{\square r}\). Colour \(H_3\) by Step 4. For each copy of \(H_2=K_3\square K_3\), assign to \((a,b)\) its first coordinate \(a\), giving three colours and exactly two same-colour neighbours out of four. Give a vertex in the Cartesian product the tuple of its factor colours. Each vertex then has at least \(3+2r\) same-colour neighbours of its \(6+4r\) neighbours, precisely the required majority. All \(4\cdot3^r\) tuples occur. This proves the bound for all \(r\ge0\).

## Verification

Run `python3 verify.py` with Python 3.10 or later. The standalone script enumerates every \(\binom{27}{6}=296010\) labelled six-subset, checks the induced-degree condition, constructs the \(54\) coordinate rectangles independently, and verifies that the two collections coincide. It separately checks the explicit Cartesian-product colouring, vertex by vertex, for dimensions \(3,5,7,9\), including the exact claimed numbers of colours. These computations corroborate, but cannot replace, the arguments for all dimensions.

## Relationship to prior work

Bujtás–Dettlaff–Furmańczyk–Laskowska–Tuza, *Majority C-coloring in Cartesian products* (arXiv:2608.27669v2), introduce the relevant Cartesian-product analysis. Their Theorem 3 gives \(\overline\chi_{\ge}(K_m\square K_n)=\min\{m,n\}\); Theorem 4 evaluates even powers; Proposition 5(ii) yields \(\overline\chi_{\ge}(H_{2r+3})\ge3^{r+1}\). Their Theorem 7 gives stronger bounds for alphabet size \(5\) or at least \(7\), but does not cover size \(3\); Open Problem 3 asks for exact values for odd powers with alphabet size at least \(3\). This result settles the smallest ternary case and sharpens the lower bound for every higher odd ternary power. Its amplification follows the existing product-colouring principle; the new ingredient is the dimension-three construction and sharp class-size obstruction.

The earlier *Majority C-coloring of graphs* introduces the invariant. For a regular graph of degree \(6\), the condition is equivalent to the \(3\)-improper C-colouring of Bujtás and collaborators. Their older Cartesian-product inequalities and binary-hypercube results do not supply the ternary three-cube evaluation. The equivalence of terminology is acknowledged rather than offered as novelty.

## Limitations

The exact numerical result and all six-vertex-class classification apply only to \(H_3\). The general odd-dimensional statement is a constructive **lower** bound and may be nonoptimal. No classification of every optimal four-colouring of \(H_3\) is claimed; the theorem classifies minimum-size individual admissible colour classes. Finite enumerations do not establish the infinite-dimensional assertion. A matching result under an unindexed alias remains a bibliographic priority risk; no claim of independent external audit is made.

## References

1. Csilla Bujtás, Magda Dettlaff, Hanna Furmańczyk, Aleksandra Laskowska, Zsolt Tuza, *Majority C-coloring in Cartesian products*, arXiv:2608.27669v2 (2026), https://arxiv.org/pdf/2608.27669v2 (initial preprint 2026-08-27).
2. Csilla Bujtás, Magda Dettlaff, Hanna Furmańczyk, Aleksandra Laskowska, *Majority C-coloring of graphs*, arXiv:2604.20752 (2026), https://arxiv.org/abs/2604.20752.
3. Csilla Bujtás, E. Sampathkumar, Zsolt Tuza, L. Pushpalatha, R. C. Vasundhara, *Improper C-colorings of graphs*, Discrete Applied Mathematics **159** (2011), 174–186; https://doi.org/10.1016/j.dam.2010.11.004.
