# Exact 109-level four-simplex volume spectrum of the regular 600-cell

## Finding

Let \(P\subset\mathbb R^4\) be the centered regular 600-cell with circumradius \(1\), and let \(\varphi=(1+\sqrt5)/2\). Among all \(\binom{120}{5}=190{,}578{,}024\) five-element subsets of its vertices, the absolute oriented four-simplex determinant has exactly **109 distinct values**, including zero. The complete exact frequency distribution is `spectrum.csv` (one row per determinant value in ascending numerical order). In particular, exactly \(16{,}493{,}784\) subsets are affinely dependent.

The largest volume of **any** four-simplex contained in \(P\), without a vertex-support restriction, is
\[
\boxed{\max_{T\subseteq P}\operatorname{Vol}_4(T)=\frac{1+2\varphi}{32}=\frac{2+\sqrt5}{32}.}
\]
Exactly \(2{,}400\) five-vertex subsets attain this volume. The second-largest *vertex-supported* volume is \((4+5\varphi)/96=(13+5\sqrt5)/192\), attained by exactly \(10{,}800\) five-vertex subsets. Thus the gap between the two highest vertex-supported levels is \((\sqrt5-1)/192\).

All \(2{,}400\) maximizing five-vertex subsets have the same multiset of ten squared edge lengths: six \(\varphi^2\), three \(2\), and one \(3\). There are also nonvertex maximizing simplices; therefore the number \(2{,}400\) does **not** classify every equality configuration for the continuous optimization problem.

## Assumptions and scope

A four-simplex is the convex hull of five affinely independent points of \(\mathbb R^4\); its volume is the absolute four-by-four difference determinant divided by \(4!=24\). The body \(P\) is precisely the convex hull of the following \(120\) vectors:

1. The eight permutations of \((\pm1,0,0,0)\).
2. The sixteen vectors \(\tfrac12(\pm1,\pm1,\pm1,\pm1)\).
3. The ninety-six vectors given by **even permutations** of \(\tfrac12(0,\pm1,\pm\varphi,\pm\varphi^{-1})\), with the three nonzero signs chosen independently.

The displayed coordinates are the standard unit-circumradius icosian coordinates for the regular 600-cell. Each has Euclidean norm one. The first motivating source in the specified literature time cohort is Bao et al. (initial public arXiv posting 30 May 2010). The problem concerns an exact extremal metric invariant of the \(H_4\) polytope, not the combinatorial matroid alone.

## Proof

**1. Reduction to vertex quintuples.** For fixed four points of \(P\), the oriented affine determinant is affine in the fifth point, and its absolute value is convex. Its maximum over the compact polytope therefore occurs at a vertex. Repeating for the other four points proves that the global maximum over \(P^5\) equals the maximum over vertex quintuples. This establishes the unrestricted-volume assertion once the discrete bound below is proved; it does not imply that all equality configurations are vertex-supported.

**2. Exact normalization.** Write \(W=2V\), where \(V\) is the stated 120-element vertex set. All four coordinates of the vectors of \(W\) lie in \(\mathbb Z[\varphi]\). A determinant formed from differences of the scaled vertices is \(16\) times the determinant of the corresponding unit-radius simplex. Thus a scaled absolute determinant \(d\) represents volume \(d/384\).

**3. Exhaustive exact ring calculation.** The 600-cell's geometric symmetry group is transitive on its 120 vertices (see Denney et al., Fact 4). Fix one vertex \(w_0\). There are exactly \(\binom{119}{4}=7{,}940{,}751\) remaining unordered four-tuples. Every five-vertex set is counted five times when all 120 anchors are used; by transitivity, its total frequency is exactly \(120/5=24\) times the frequency for a fixed anchor.

The standalone file `verify_spectrum.cpp` constructs the complete vertex set, checks cardinality, distinctness and Euclidean squared norm \(4\) for the scaled vectors, and evaluates every fixed-anchor determinant **exactly**, not as a floating-point approximation. It represents \(a+b\varphi\) by the integer pair \((a,b)\), multiplies using \(\varphi^2=\varphi+1\), and compares elements with exact integer inequalities. For two displacement pairs of vectors, it uses six two-by-two minors and the exterior-product formula
\[
\begin{aligned}
\det(a,b,c,d)={}&(a\wedge b)_{01}(c\wedge d)_{23}
 -(a\wedge b)_{02}(c\wedge d)_{13}\\
&+(a\wedge b)_{03}(c\wedge d)_{12}
 +(a\wedge b)_{12}(c\wedge d)_{03}\\
&-(a\wedge b)_{13}(c\wedge d)_{02}
 +(a\wedge b)_{23}(c\wedge d)_{01}.
\end{aligned}
\]
The full deterministic loop uses only \(i<j<k<l\) over the 119 differences from the anchor; no random sample or unverified numerical bound enters the enumeration. All resulting coefficients are ordinary, safely bounded machine integers; the checker also completed with signed-integer-overflow and undefined-behavior checks enabled.

The exact enumeration yields 109 values, with largest scaled determinants \(12+24\varphi\) (100 anchored quintuples) and \(16+20\varphi\) (450 anchored quintuples), and 687,241 zero determinants for the anchor. Multiplying the frequencies by 24 gives 2,400, 10,800 and 16,493,784, respectively. This proves all discrete claims and the unrestricted sharp upper bound. The checker repeats the entire enumeration anchored at representatives of the other two coordinate classes and confirms identical spectra.

**4. Equality beyond vertices.** In scaled coordinates, fix
\[
\begin{split}
 u_0&=(-2,0,0,0),\\
 u_1&=(\varphi-1,0,\varphi,1),\\
 u_2&=(\varphi-1,0,-\varphi,1),\\
 u_3&=(\varphi-1,1,0,-\varphi).
\end{split}
\]
Both \(p=(0,-2,0,0)\) and \(q=(0,-\varphi,\varphi-1,-1)\) are scaled vertices of \(P\). Direct symbolic expansion gives
\[
\det(u_1-u_0,u_2-u_0,u_3-u_0,p-u_0)
=\det(u_1-u_0,u_2-u_0,u_3-u_0,q-u_0)
=-(12+24\varphi).
\]
Consequently, replacing the fifth vertex by any point \((1-t)p+tq\), \(0\le t\le1\), preserves the maximum. This explicitly demonstrates continuous equality configurations, without purporting to classify all of them.

## Verification

Compile with `c++ -std=c++17 -O2 verify_spectrum.cpp -o verify_spectrum` and run `./verify_spectrum --check spectrum.csv`. On success it reports 120 distinct vertices, 7,940,751 anchored quintuples, 190,578,024 total quintuples, 109 exact levels, 16,493,784 degeneracies, the two highest scaled determinants and their frequencies. The `--emit spectrum.csv` variant regenerates the distribution from scratch; `--check` compares the entire byte-for-byte table, not only headline statistics.

The supplementary `verify_examples.py` (SymPy required) independently expands both displayed extremal determinants and their midpoint determinant; it checks the exact table's total counts. These checks were run on the actual packaged source files. Direct verification of the ring inequalities and of all three full anchor enumerations does not rely on any earlier results or cached calculation.

## Relationship to prior work

Bao et al. (2010) analyze the rank-four matroid, dependence flats and automorphisms of \(H_4\); their matroid-incidence tables distinguish dependence from independence, but they do not encode absolute 4-simplex determinants. Dechant (2013) constructs the 600-cell and other root systems via spinors, rather than solving an inscribed-simplex optimization. Denney et al. (2019) analyze the 600-cell's embedded 24-cells, symmetry and icosian coordinates; their central counts concern subpolytopes, not this 109-level affine volume distribution.

An exact maximal-four-simplex result for the **regular 24-cell** is relevant but does not imply this theorem: a 24-cell embedded in the 600-cell supplies a *lower bound* on the larger body's optimum, not a covering upper bound, and it cannot classify determinants involving vertices outside that 24-cell. General circumscribed-sphere simplex bounds provide an upper bound but do not attain equality at a 600-cell five-vertex set. The examined material did not establish the volume spectrum or the 2,400 optimizers reported here.

## Limitations

The complete exact 109-level table concerns **vertex-supported** simplices only. The maximum-volume assertion extends to arbitrary contained simplices by coordinatewise convexity, but their full equality locus is **not** classified. Likewise the second-largest statement is only about vertex-supported simplices; the continuous problem has arbitrarily near-maximal volumes. Although exact enumeration constitutes a finite proof given the checker and symmetry reduction, it is not a formal proof-assistant certificate. Absence from inspected literature and database results does not establish global historical priority; unindexed specialized \(H_4\) metric tables remain a potential overlap risk. Independent audit has not been performed.

## References

- C. Bao, C. Freidman-Gerlicz, G. Gordon, P. McGrath and J. Vega, *Matroid automorphisms of the root system \(H_4\)* (initial public arXiv posting 2010-05-30), https://arxiv.org/abs/1005.5492.
- P.-P. Dechant, *Platonic solids generate their four-dimensional analogues* (initial public arXiv posting 2013-07-25), https://arxiv.org/abs/1307.6768.
- T. Denney, D. Hooker, D. Johnson, T. Robinson, M. Butler and S. Claiborne, *The Geometry of \(H_4\) Polytopes* (arXiv preprint, 2019), https://arxiv.org/abs/1912.06156.
