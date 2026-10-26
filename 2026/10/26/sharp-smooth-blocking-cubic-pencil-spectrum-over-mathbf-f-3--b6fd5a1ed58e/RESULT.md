# Sharp smooth blocking-cubic pencil spectrum over \(\mathbf F_3\)

## Finding
Let \(V=H^0(\mathbf P^2_{\mathbf F_3},\mathcal O(3))\). A *pencil* means a two-dimensional \(\mathbf F_3\)-linear subspace \(W\subset V\), with four rational projective members. Call it *admissible* if its two generating cubics have no common \(\mathbf F_3\)-point and **all four** rational members are geometrically smooth. A member is *blocking* if its \(\mathbf F_3\)-points meet each of the thirteen rational lines.

**Theorem.** Every admissible pencil has at least three nonblocking members. The bound is sharp: exactly \(292032\) coordinate-fixed admissible pencils have one blocking member. Their three nonblocking members have the following unordered \(\mathbf F_3\)-point-count distributions:

| Counts of the three other members | Number of pencils |
|---|---:|
| \((1,1,5)\) | \(22464\) |
| \((1,2,4)\) | \(123552\) |
| \((1,3,3)\) | \(39312\) |
| \((2,2,3)\) | \(106704\) |

These are **linear subspaces in fixed coordinates**, not projective-isomorphism classes. Equivalently, exactly \(312\) admissible pencils contain a *fixed* smooth blocking cubic. No admissible pencil has two blocking members.

## Assumptions and scope
All curves, equations, pencil parameters, lines and rational points are defined over \(\mathbf F_3\), unless geometric smoothness is explicitly invoked; smoothness always means smooth over the algebraic closure. The base-locus hypothesis excludes **rational** base points, not the nine geometric intersection points counted by Bézout. No claims are made about larger finite fields, singular members, non-rational pencil parameters, or geometric equivalence classes of pencils.

## Proof
**1. A structural at-most-one statement.** The rational point sets of the four members of an admissible pencil partition \(\mathbf P^2(\mathbf F_3)\), which has thirteen points, because the base locus has no rational point. A geometrically smooth blocking cubic cannot contain four collinear rational points: four distinct intersections with one line would force that line to be a component. The standard lower bound for nontrivial blocking sets in the prime-order plane implies that such a cubic has at least six rational points. Every smooth plane cubic over \(\mathbf F_3\) is genus one and has at least one rational point by Hasse–Weil: \(4-2\sqrt3>0\). If two distinct members were blocking, at least \(6+6+1+1=14\) rational points would be required. Hence there is at most one blocking member and at least three nonblocking members.

**2. Exhaustive classification of the possible distinguished cubic.** Fix monomials in the order
\[
(x^3,x^2y,x^2z,xy^2,xyz,xz^2,y^3,y^2z,yz^2,z^3).
\]
A nonzero ternary cubic is represented by exactly one vector whose first nonzero coefficient is one. This covers all \((3^{10}-1)/2=29524\) projective cubic equations. Evaluate at the thirteen rational points, test intersection with each of the thirteen rational lines, and test geometric smoothness by the projective Jacobian criterion. Exact enumeration yields \(4940\) blocking projective cubic equations, of which \(936\) are geometrically smooth. All \(936\) have six rational points.

Take
\[
F=Y^2Z-X^3-X^2Z+XZ^2.
\]
Enumerating the invertible \(3\times3\) matrices over \(\mathbf F_3\), modulo scalar matrices, gives a projective orbit of \(936\) equations for \(F\). Since the whole smooth blocking population is \(936\), this is its unique projective equivalence class. In this orbit calculation, homogeneous cubic evaluations transform by the cube of the scalar used to normalize each projective point. The evaluation map on cubic forms is injective: a cubic vanishing at all thirteen rational points would vanish identically on each rational line (four roots on a degree-three restriction), hence would be divisible by all thirteen line equations, which is impossible for a nonzero cubic.

**3. Canonical parameterization through \(F\).** The point \(P_0=[0:0:1]\) lies on \(F\); the coefficient of \(X^3\) in \(F\) is nonzero. Any pencil \(\langle F,G\rangle\) with no rational base point has a unique second generator \(G\) characterized by \(G(P_0)=1\) and vanishing \(X^3\)-coefficient. Indeed, scale \(G\) to make its evaluation at \(P_0\) one, then add a unique multiple of \(F\) to eliminate its \(X^3\)-coefficient. These operations do not change the pencil. The remaining eight coefficients are arbitrary elements of \(\mathbf F_3\), giving exactly \(3^8=6561\) candidates and no duplicates.

The base-point condition is \(G(P)\ne0\) at each of the six rational points of \(F\). Exactly \(864\) canonical generators satisfy it. Among those, exactly \(576\) give a geometrically smooth \(G\), and exactly \(312\) have all of \(G\), \(G+F\), and \(G-F\) geometrically smooth. Counting the three other curves' rational points gives the *local* profiles
\[
(1,1,5):24,\quad (1,2,4):132,\quad
(1,3,3):42,\quad (2,2,3):114.
\]
Since \(F\) is the unique blocking member, each admissible pencil with a blocking member is counted once in the total \(936\cdot312=292032\). The four global multiplicities in the theorem are the corresponding local counts multiplied by \(936\).

**4. Explicit sharpness witness.** One normalized generator is
\[
G=2X^2Y+2X^2Z+2XY^2+Y^3+Z^3.
\]
The pencil generated by \(F\) and \(G\) has no rational base point. Its members \(F,G,F+G,F-G\) are all geometrically smooth and have respectively \(6,4,1,2\) rational points. Thus exactly one is blocking.

**5. Why the enumeration proves geometric claims.** The attached independently written Gröbner-based programs test each chart \(X=1\), \(Y=1\), \(Z=1\). In a chart with affine equation \(f\), geometric smoothness is equivalent to the ideal generated by \(f\) and both affine partial derivatives being the unit ideal over \(\mathbf F_3\). Lexicographic Gröbner bases over \(\mathbf F_3\) test this exactly, without a field-extension cutoff. The full-projective-cubic census and the normalized-pencil census separately implement these tests. A second implementation, in C++, uses exact \(\mathbf F_3\), \(\mathbf F_9\), and \(\mathbf F_{27}\) arithmetic; the two approaches agree on all \(312\) normalized coefficient vectors and all relevant populations. Finite checks alone are sufficient here because the parameter spaces being claimed are explicitly finite and exhaustively traversed; no inference from sampled examples is made.

## Verification
From a working directory containing the companion files, run:

```
g++ -O3 -std=c++17 verify_census.cpp -o verify_census
./verify_census
python3 verify_pencils_groebner.py
python3 verify_global_groebner.py
```

Python requires SymPy. Compare standard output to the three files ending in `.expected.txt` and compare the sorted `pencils_recomputed.txt` with `accepted_pencils_reference.txt` and `pencils_groebner_recomputed.txt`. The reference list has exactly \(312\) distinct coefficient vectors in the monomial order displayed above. All three programs were executed successfully from these files. The Python projective census independently checked \(4940\) blocking cubic equations, \(936\) smooth ones, and their \(234\) six-point supports (four smooth equations per support). The C++ projective orbit and the two independent smooth-pencil lists were checked against these totals.

## Relationship to prior work
Asgarli–Ghioca (2022) studies the existence of pencils with all rational members smooth and proves a large-field existence result, with small-field constructions for conics. Asgarli–Ghioca–Yip (2022) studies blocking plane curves and gives smooth cubic examples over the smallest fields. Asgarli–Ghioca–Yip (2023) analyzes the proportion of blocking curves in base-point-free pencils and proves a general lower bound of at least \((q+1)/3\) nonblocking members when \(q\) is prime. At \(q=3\), that yields at least two; the present exact result gives the sharp count of three **under the additional smoothness hypothesis**, and counts every equality pencil with its point profile. None of these cited results states the \(292032\) mass or the four equality profiles. The projective uniqueness of the individual smooth blocking cubic is a prerequisite reproduced here, not the primary novelty claim.

## Limitations
The statement is restricted to the first odd field with smooth blocking cubics. It is a finite exact computation backed by complete enumeration, not a uniform formula over all fields. Some historical finite-geometry tables or unindexed computational catalogues may implicitly encode the same pencil counts; priority therefore requires independent literature review. No external or independent scientific audit has been performed.

## References
1. S. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169, first posted 2022-03-14, https://arxiv.org/abs/2203.07169.
2. S. Asgarli, D. Ghioca and C. H. Yip, *Plane curves giving rise to blocking sets over finite fields*, arXiv:2208.13299, first posted 2022-08-28, https://arxiv.org/abs/2208.13299.
3. S. Asgarli, D. Ghioca and C. H. Yip, *Proportion of blocking curves in a pencil*, arXiv:2301.06019, first posted 2023-01-15, https://arxiv.org/abs/2301.06019.
