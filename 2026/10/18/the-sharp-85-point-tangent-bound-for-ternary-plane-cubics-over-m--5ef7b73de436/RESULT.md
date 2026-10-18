# The sharp 85-point tangent bound for plane cubics over \(\mathbf F_9\)

## Finding
Let \(k=\mathbf F_9\), and, for any homogeneous cubic \(G\in k[X,Y,Z]\), let \(T(G)\) be the union of the \(k\)-points on all tangent lines to \(G=0\) at its **smooth** \(k\)-rational points. This definition applies to reducible and singular cubics as well. Then
\[
\boxed{\max_{G\ne0}|T(G)|=85<|\mathbf P^2(k)|=91.}
\]
Equality is attained by the geometrically smooth cubic
\[
 C:\quad X^2Y+Y^2Z+Z^3=0,
\]
which has 16 rational points and 16 distinct rational tangents, covering 85 points and missing exactly six. In the field \(k=\mathbf F_3[\iota]/(\iota^2+1)\), the uncovered points are \([0:u:1]\) for the six \(u\in k\setminus\{0,\iota,-\iota\}\). The number of tangent lines through each point has histogram
\[
(0:6,\ 1:41,\ 2:24,\ 3:12,\ 4:5,\ 5:3).
\]
Consequently the least degree of a tangent-filling plane curve over \(k\) is exactly four, even if singular or reducible curves are allowed. The degree-four upper bound is supplied by the already-known Hermitian curve \(X^4+Y^4+Z^4=0\).

## Assumptions and scope
All rational points and tangent lines are over \(k\). A point on a plane curve is smooth if its homogeneous gradient is nonzero there; singular points contribute no tangents. The result concerns equations up to arbitrary projective changes of coordinates and nonzero scalar multiples, not the number of geometric isomorphism classes. The complete cubic bound is proved by finite exhaustive exact arithmetic after a projective normal-form reduction. The Hermitian quartic construction is prior work, not a new construction.

## Proof
**Normal form and exhaustiveness.** Any cubic with at least one smooth \(k\)-point has a rational incident point--tangent-line flag. Since \(\mathrm{PGL}_3(k)\) is transitive on such flags, take that point to \([0:1:0]\) and its tangent line to \(Z=0\). The cubic equation has no \(Y^3\) or \(XY^2\) terms, while its \(Y^2Z\) coefficient is nonzero. Scale to make that coefficient one. Hence **every** cubic with at least one smooth rational point is projectively equivalent to exactly some member (not necessarily uniquely) of the seven-parameter family
\[
G=A X^3+B X^2Y+C X^2Z+D XYZ+E XZ^2+F YZ^2+H Z^3+Y^2Z,
\qquad A,B,C,D,E,F,H\in k.
\]
A cubic with no smooth rational point has empty \(T(G)\) and cannot improve the bound. Thus enumerating this family is exhaustive for the maximum, with no irreducibility or geometric smoothness assumption.

**Exact finite certificate.** The complete program `verify_cubic.cpp` enumerates **all \(9^7=4{,}782{,}969\) coefficient septuples** using the field representation \(a+b\iota\mapsto a+3b\), where \(a,b\in\{0,1,2\}\) and \(\iota^2=2\). It generates all 91 normalized rational projective points and, independently, all 91 normalized line coefficients. For every cubic and rational projective point it evaluates \(G\), tests the three partial derivatives and, at each smooth zero, adds the 10 points of the projective tangent line to a two-word exact bitset. The search reports `TOTAL_NORMAL_FORMS 4782969`, `FULL_COVERAGE 0`, `MAX_COVER 85`, and the maximizing septuple `(0,1,0,0,0,0,1)`. Since these are all coefficients in the complete normal form, this proves the universal 85-point bound, not merely a sampled or partial search.

**Explicit maximizer.** For \(C=X^2Y+Y^2Z+Z^3\), the gradient is \((2XY,X^2+2YZ,Y^2)\). If \(Y=0\), the equation and the second derivative force \(X=Z=0\), impossible projectively; if \(Y\ne0\), the last derivative is nonzero. Thus the cubic is geometrically smooth. The independent verifier `verify_examples.py` obtains 16 rational zeros, all 16 distinct tangent lines, the claimed incidence histogram, and exactly the six stated uncovered points.

**Lower degrees and degree-four witness.** A line has one rational tangent line and covers ten points. A nonsingular conic has ten rational tangents, with no three concurrent because its dual is again a conic; their union covers exactly \(10\cdot10-\binom{10}{2}=55\) points. Any singular or reducible conic contributes at most two distinct rational tangent lines from its linear components, hence at most 19 points (or none if nonreduced or nonsplit). Thus no curve of degree below four is tangent-filling. The smooth Hermitian quartic \(X^4+Y^4+Z^4=0\) is tangent-filling by Asgarli--Ghioca, Example 3.1. Its 28 rational points and full 91-point tangent cover are also reproduced by `verify_examples.py`. Therefore the minimum degree is four.

## Verification
Compile and run `g++ -O3 -std=c++17 verify_cubic.cpp -o verify_cubic && ./verify_cubic`, and run `python3 verify_examples.py`; both scripts are complete standalone artifacts included with this document. C++ confirms the **full 4,782,969-element** normal-form census, not a random search. Python independently checks the single maximizing cubic and known Hermitian quartic. The exhaustive census requires a C++17 compiler and is an exact finite computational proof; no claim that finite sampling proves statements over infinite fields is made.

## Relationship to prior work
Asgarli and Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420, ask for the minimum degree in Question 1.5 and prove in Example 3.1 that the Hermitian curve gives degree \(\sqrt q+1\) for square \(q\). That supplies the already-known degree-four upper bound here. Their nonexistence Theorems 1.1--1.2 do not apply to cubics over \(\mathbf F_9\), because their stated field and characteristic bounds fail. The novel claim is the **sharp cubic 85-point upper bound**, which gives the missing degree-three obstruction and thus the sharp minimum. Asgarli--Ghioca--Yip, *Plane curves giving rise to blocking sets over finite fields*, arXiv:2208.13299, study incidence of rational points of curves with lines; that problem is different from covering the plane by rational tangent lines to the curve. Nearby small-field examples over other fields do not imply the asserted maximum over \(\mathbf F_9\).

## Limitations
This establishes no count of isomorphism classes or classification of **all** maximizing cubics. The finite census is exact but its correctness still depends on the displayed normal-form argument, finite-field implementation, and code execution; no independent mathematical audit has been performed. Existing unindexed equivalent computations cannot be excluded solely from targeted literature searches. The Hermitian upper-bound construction is not asserted to be original.

## References
1. S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420 (first public 2023-02-26), especially Theorems 1.1--1.2, Question 1.5, and Example 3.1. https://arxiv.org/pdf/2302.13420
2. S. Asgarli, D. Ghioca, and C. H. Yip, *Plane curves giving rise to blocking sets over finite fields*, arXiv:2208.13299. https://arxiv.org/pdf/2208.13299
