# Complete rational-base-point census of all-smooth plane-cubic pencils over \(\mathbf F_3\)

## Finding
Let \(V=\mathbf F_3[X,Y,Z]_3\), and call a two-dimensional vector subspace \(W\subset V\) **all-smooth** if its four projective members are geometrically smooth plane cubics. Set \(b(W)=\#\{P\in\mathbf P^2(\mathbf F_3): F(P)=0\ \text{for all }F\in W\}\). The complete census is

| \(b(W)\) | Number of all-smooth pencils |
|---:|---:|
| 0 | 2,577,744 |
| 1 | 2,651,454 |
| 2 | 1,493,856 |
| 3 | 499,824 |
| 4 | 56,160 |
| 5–9 | 0 |
| **Total** | **7,279,038** |

In particular, every all-smooth pencil has at most four rational base points, and this bound is attained. There are \(16{,}848\) projective geometrically smooth cubic forms, constituting ten projective-coordinate orbits.

## Assumptions and scope
All equations and projective coordinate transformations are defined over \(\mathbf F_3\). Smooth means geometrically smooth over an algebraic closure, not merely smooth at rational points. Different two-dimensional linear subspaces are counted separately, while different bases of one subspace define the same pencil. The base-point statistic counts distinct rational points only; it is not the length, multiplicity structure, or number of geometric points of the scheme-theoretic base locus. All four \(\mathbf F_3\)-rational members must be smooth; the infinitely many geometric members need not be.

## Proof
Write each homogeneous cubic uniquely as \(F=\sum_{i+j+k=3}c_{ijk}X^iY^jZ^k\). Normalize its coefficient vector so the first nonzero coefficient is 1. There are \((3^{10}-1)/2=29{,}524\) normalized forms. Elementary coordinate interchanges, the transvection \(X\mapsto X+Y\), and \(X\mapsto2X\) generate \(\operatorname{PGL}_3(\mathbf F_3)\). Explicit substitution partitions the normalized forms into exactly 25 orbits.

For each orbit representative, geometric smoothness is decided by testing whether the Jacobian ideal of \(F\) is the unit ideal on the three standard affine charts. An independent exact Gröbner-basis implementation confirms these decisions for all 25 representatives. Exactly ten orbits are smooth, and their sizes sum to \(16{,}848\); the remaining 15 orbits contain singular curves and sum to \(12{,}676\).

Let \(\mathcal S\) be this set of \(16{,}848\) normalized smooth forms. Two distinct projective forms \(F,G\in\mathcal S\) generate an all-smooth pencil if and only if their other projective members \(F+G\) and \(F+2G\) are both geometrically smooth. When implementing this condition, scalar multiples of each form are normalized, and both required additions are evaluated in \(\mathbf F_3\). Every pencil supplies exactly \(4\cdot3=12\) ordered pairs of distinct projective generators. For any valid pair, its number of rational base points is \(\#(Z(F)\cap Z(G)\cap\mathbf P^2(\mathbf F_3))\).

The first exhaustive enumeration fixes one representative from each smooth projective-coordinate orbit and weighs its partner count by that orbit's size. It obtains, for \(k=0,1,2,3,4\), respectively, the exact ordered-generator counts \(30{,}932{,}928\), \(31{,}817{,}448\), \(17{,}926{,}272\), \(5{,}997{,}888\), and \(673{,}920\); the count is zero for every \(5\le k\le9\). Dividing by 12 yields the table. The sum of ordered pairs is \(87{,}348{,}456\), also divisible by 12 with no remainder.

A second, separately coded algorithm evaluates all \(16{,}848\) possible first generators against all \(16{,}848\) possible second generators directly, without any orbit weights, using independent ternary-addition tables and projective rational-point masks. It recovers every bin and the same total exactly. The source programs and machine-readable outputs are included alongside this document.

To exhibit sharpness, set
\[
\begin{aligned}
 F&=Z^3+2YZ^2+Y^2Z+Y^3+X^2Z,\\
 G&=Y^2Z+XZ^2+2X^2Z+2X^3.
\end{aligned}
\]
Exact Jacobian-ideal calculations on all affine charts verify that each of \(F,G,F+G,F+2G\) is geometrically smooth. Their common rational points are exactly \([1:1:1]\), \([1:2:1]\), \([2:1:1]\), and \([2:2:1]\), establishing the bound's sharpness.

As an independent consistency restriction, every smooth plane cubic over \(\mathbf F_3\) has at most seven rational points by Hasse's bound. Summing rational point counts over all four members of an all-smooth pencil gives \(13+3b(W)\), because each of the thirteen rational points off the base lies on exactly one member, and each base point lies on all four. Hence \(13+3b(W)\le28\), implying \(b(W)\le5\). The exhaustive census sharpens this independent inequality by excluding five.

## Verification
Run `g++ -O3 -std=c++17 smooth_cubic_pencils_f3_v2.cpp -o census` and `./census smooth_ids.txt`, saving standard output and error to the embedded output files as desired. The polynomial encoding is base-three coefficient digits, in the order \((i,j,3-i-j)\) for \(0\le i\le3\) and \(0\le j\le3-i\). The C++ test searches for a common zero of \(F,F_X,F_Y,F_Z\) over extensions of degrees one, two, and three; for a singular plane cubic over \(\mathbf F_3\), a geometric singular point occurs over one of these extensions. A separately written SymPy Gröbner test verifies the geometric decisions without this extension-degree lemma: `python verify_geometric_smoothness.py`. Run `python verify_direct_tally.py` after regenerating `smooth_ids.txt` for the independent complete ordered-pair enumeration. The resulting saved outputs confirm all counts. Reproducibility requires a C++17 compiler, Python 3, SymPy and NumPy.

## Relationship to prior work
Kaplan and Matei (2020, Theorem 1) count rational common intersection points of **arbitrary** pairs of plane cubics without common geometric components. Their general polynomial formula does not distinguish whether all four members of the span are smooth, so it does not determine the smooth-restricted census or rule out five rational base points here. Asgarli and Ghioca (2022, Theorem 1.3) study the existence of pencils whose rational members are all smooth and give a large-field existence theorem; they do not classify plane-cubic pencils over \(\mathbf F_3\) by their rational bases. Moschetti, Pirola and Stoppino (2024 preprint) classify pencils over the complex numbers having a single *geometric* base point and smooth general member, a distinct question and field. The exact finite-field census is not asserted to be a consequence of any of these established results.

## Limitations
The result concerns the complete finite family over exactly \(\mathbf F_3\); it supplies no polynomial formula for general field size and makes no statement on smoothness of all geometric members of a pencil. The exact counts require computation, although all 25 geometric smoothness decisions have separate symbolic verification. The literature comparison cannot exclude unpublished or unindexed computations of the same finite census, and independent mathematical audit has not been performed.

## References
1. N. Kaplan and V. Matei, *Counting Plane Cubic Curves over Finite Fields with a Prescribed Number of Rational Intersection Points*, arXiv:2003.13944, first posted 2020-03-31, Theorem 1. https://arxiv.org/abs/2003.13944
2. S. Asgarli and D. Ghioca, *Smoothness in Pencils of Hypersurfaces over Finite Fields*, arXiv:2203.07169, first posted 2022-03-14, Theorem 1.3. https://arxiv.org/html/2203.07169v1
3. R. Moschetti, G. P. Pirola and L. Stoppino, *Pencils of Plane Cubics with One Base Point*, arXiv:2407.04569, first posted 2024-07-05, Theorem 1.3. https://arxiv.org/html/2407.04569v3
