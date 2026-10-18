# Nine rational flexes are optimal for smooth plane-filling sextics over \(\mathbf F_3\)

## Finding
Let \(C\subset\mathbf P^2_{\mathbf F_3}\) be a geometrically smooth plane sextic satisfying \(C(\mathbf F_3)=\mathbf P^2(\mathbf F_3)\). A rational flex is a rational point \(P\) at which the tangent line has intersection multiplicity at least three. Then \(C\) has **at most nine rational flexes**, and this bound is attained.

Precisely **16,848 distinct projective sextic equations** attain nine rational flexes. Under \(\operatorname{PGL}_3(\mathbf F_3)\), they form exactly **three orbits, each of size 5,616**, so all three have trivial projective stabilizer. If both nonzero scalar multiples are counted as separate equations, the number is **33,696**. This is a classification of embedded equations up to rational projective coordinates, not of abstract curve isomorphism classes.

For explicit extremizers, use the monomial order and basis in `verify/make_jets.py`. Their fifteen-coefficient vectors are `001000101102020`, `001000101102022`, and `001001001121012`, in increasing order of the monomial-compatible nullspace basis. For example, the first vector defines
\[
-X^5Z-X^4YZ+X^3Y^3+X^3Y^2Z+X^3Z^3+X^2YZ^3-XY^5-XY^2Z^3+Y^5Z-YZ^5=0.
\]
The coefficient signs are interpreted in \(\mathbf F_3\).

## Assumptions and scope
All fields of definition and projective equivalences are over \(\mathbf F_3\). All geometric smoothness assertions mean smooth after base change to an algebraic closure. The 13 rational plane points are the entire rational point set of a plane-filling curve. Its genus is \((6-1)(6-2)/2=10\).

At a rational point of a geometrically smooth plane-filling sextic, the tangent line contains three further distinct rational points of the curve. Bezout implies that the tangent contact at the chosen point is exactly two or three. Thus "flex" here means contact exactly three; higher contact cannot occur on these smooth curves. This makes nine a natural extremal value among 13 prescribed rational points, rather than a chosen coefficient slice.

## Proof
Write \(V\) for the 15-dimensional \(\mathbf F_3\)-vector space of homogeneous ternary sextics vanishing at all 13 rational projective points. The 28 monomials of total degree six give an evaluation matrix of rank 13. Exact row reduction provides the nullspace basis used throughout the verification. Thus all \(3^{15}-1=14,348,906\) nonzero equations are covered, without sampling or numerical approximation.

For every rational point \(P\), choose an affine chart containing it and write the local equation through quadratic order as
\[
F_P(u,v)=a u+b v+c u^2+d uv+e v^2+\text{terms of degree at least three}.
\]
The point is smooth iff \((a,b)\ne(0,0)\). The tangent direction is \((b,-a)\), and the rational-flex condition is exactly
\[
cb^2-dab+ea^2=0\quad\text{in }\mathbf F_3.
\]
The formula uses the actual quadratic Taylor coefficients (not a Hessian divided by two), and is valid in characteristic three. All 13 local first and second jets are linear functions of the 15 coefficients; their exact matrices are supplied in `verify/jet_data.json`.

Exhausting the coefficients gives 3,122,496 rationally nonsingular nonzero equations, with rational-flex frequencies for \(1,3,5,7,9,11\) respectively
\[
213408,\quad1044576,\quad1095120,\quad527904,\quad202176,\quad39312.
\]
No rationally nonsingular equation has twelve or thirteen flexes; the maximum is eleven. For eleven flexes the 39,312 equations give 19,656 projective points after dividing by \(\mathbf F_3^\times\). Under coordinate swaps, a coordinate sign change and one transvection (which generate the full projective linear group of order 5,616), these points form four orbits of sizes \(2808,5616,5616,5616\). Each representative has a nontrivial geometric Jacobian ideal on the chart \(Y=1\), so **every eleven-flex equation is geometrically singular**. Explicit Groebner bases appear in `verify/groebner_report.txt`.

Similarly, the 202,176 rationally nonsingular nine-flex equations give 101,088 projective points. Their projective-linear action has twenty orbits. Exact Groebner-basis computation of the ideals \((F,\partial F/\partial u,\partial F/\partial v)\) in all three standard affine charts finds exactly three geometrically smooth orbits, all of size 5,616. The remaining seventeen orbits are geometrically singular. Consequently, every geometrically smooth curve has at most nine rational flexes, and exactly three projective orbits attain nine. The construction displays an explicit equation in each orbit, establishing sharpness.

## Verification
The accompanying package contains executable sources and reference output. `verify/make_jets.py` independently constructs the nullspace basis and jets. `verify/enumerate.cpp` enumerates the complete coefficient space, with `verify/jet_data.h` containing exact jet constants. `verify/orbits.py` checks orbit closure and partitions the nine- and eleven-flex cases under four explicit projective generators. `verify/check_orbits.py` calculates Groebner bases on each representative. `verify/independent_contact.py` independently computes actual tangent-line contact orders by direct univariate substitution and repeats the geometric chart checks. The 24 representative certificates, including non-flex rational points, are in `verify/independent_report.json`.

The complete source programs were replayed with their generated inputs, and all count and geometric-smoothness checks agreed. A full geometric curve is not inferred from rational-point regularity alone: each surviving representative has unit Jacobian ideal on every projective chart. The exact scope is all sextic equations through all rational plane points, not all sextics over other fields.

## Relationship to prior work
Homma and Kim (2009) established the minimum possible degree \(q+2\) for smooth plane-filling curves and classified degree-\(q+2\) examples. Asgarli and Ghioca (arXiv:2307.03072, first posted July 6, 2023) study degree-\(q+3\) plane-filling curves, including smoothness conditions and explicit families. Their full accessible text does not state a nine-rational-flex bound or the three projective extremal orbits. An earlier result for the special Asgarli--Ghioca one-parameter family expresses its rational-flex count via a dual quartic but does not classify all smooth degree-six equations. Homma and Kim's Hermitian-relative curves have degree \(\sqrt q+1\) over square-order fields, a different geometric class. These are comparisons of stated implications, not a claim that lack of a search hit proves novelty.

## Limitations
Originality remains subject to an unindexed or differently named exact finite-field enumeration or classical inflection classification; independent human priority verification has not occurred. The projective-orbit counts are not absolute isomorphism counts. No assertion is made for \(q\ne3\), for singular curves, or for all rationally nonsingular but geometrically singular equations.

## References
1. S. Asgarli and D. Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072 (initial submission 2023-07-06), https://arxiv.org/html/2307.03072v1 .
2. M. Homma and S. J. Kim, *Nonsingular plane filling curves of minimum degree over a finite field and their automorphism groups*, arXiv:0903.1918 (2009), https://arxiv.org/abs/0903.1918 .
3. M. Homma and S. J. Kim, *Relatives of the Hermitian curve*, arXiv:2402.14192 (2024), https://arxiv.org/abs/2402.14192 .
