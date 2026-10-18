# Tangent-filling plane cubics over \(\mathbb F_3\): three projective classes and the degree threshold

## Finding
Let \(k=\mathbb F_3\). A nonzero homogeneous ternary form is *tangent-filling* if the union of tangent lines at its smooth \(k\)-rational projective zeroes contains every point of \(\mathbb P^2(k)\). There are exactly \(3744\) tangent-filling cubic forms up to scalar in \(k^\times\). These forms are all geometrically smooth and split into exactly three projective-equivalence classes under \(\operatorname{PGL}_3(k)\):

| Representative polynomial | \(\#C(k)\) | Distinct rational tangents | Orbit size | Stabilizer order |
|---|---:|---:|---:|---:|
| \(X^2Z+Y^3-YZ^2\) | \(4\) | \(4\) | \(936\) | \(6\) |
| \(X^2Z+XY^2-Y^2Z+YZ^2\) | \(6\) | \(6\) | \(1872\) | \(3\) |
| \(X^2Z+Y^3-YZ^2-Z^3\) | \(7\) | \(7\) | \(936\) | \(6\) |

No nonzero ternary form of degree one or two is tangent-filling. Hence the minimum degree of an irreducible tangent-filling plane curve over \(k\) is exactly \(3\). The lower-degree nonexistence statement holds even without irreducibility or reducedness.

## Assumptions and scope
All coefficients, projective points, and rational tangent lines are over \(k=\mathbb F_3\); geometric smoothness means smoothness after extension to an algebraic closure. A tangent is counted only at a \(k\)-point where the gradient is nonzero. Forms are identified under scalar multiplication, while the three classes in the table are under the larger \(\operatorname{PGL}_3(k)\) action by coordinate changes. The result classifies *all* cubic forms, not merely a specified family of smooth or absolutely irreducible cubics.

## Proof
There are exactly \((3^3-1)/(3-1)=13\) projective rational points. To exhaust the degree-\(d\) forms, order the monomials as \(X^aY^bZ^{d-a-b}\), with \(a\) decreasing and then \(b\) decreasing. Represent each projective coefficient vector uniquely by requiring its first nonzero coefficient to be \(1\); all its subsequent coefficients vary freely over \(\{0,1,2\}\). This gives exactly \((3^{\binom{d+2}{2}}-1)/2\) possibilities. In particular the totals are \(13\), \(364\), and \(29524\) for degrees \(1,2,3\).

Normalize each projective point \(P\in\mathbb P^2(k)\) by requiring its first nonzero coordinate to equal \(1\). At every rational point with \(f(P)=0\), evaluate the three formal partial derivatives modulo three. If the gradient is nonzero, normalize it to the coefficient triple of the line \(T_PC\). Represent a line by a thirteen-bit mask: bit \(i\) is set precisely when the \(i\)-th normalized point lies on that line. Taking the bitwise union over smooth rational points decides tangent-filling exactly: all thirteen bits must be set. The supplied `verify.py` contains the complete finite enumeration and asserts its totals; its loops visit every coefficient vector and every projective point once, with no random sampling.

The degree-one and degree-two enumerations have respectively \(0\) and \(0\) tangent-filling forms. Of the \(29524\) cubic forms, exactly \(3744\) are tangent-filling, with the complete profile
\[
(\#C(k),\#\{\text{distinct rational tangents}\}):\quad
(4,4)\mapsto936,\qquad(6,6)\mapsto1872,\qquad(7,7)\mapsto936.
\]
The three displayed cubics have coefficient vectors, in the stated monomial order,
\[
(0,0,1,0,0,0,1,0,2,0),\quad
(0,0,1,1,0,0,0,2,1,0),\quad
(0,0,1,0,0,0,1,0,2,2).
\]
The verifier calculates their orbits by breadth-first search under substitutions \(X\mapsto X+Y\), \(Y\mapsto X+Y\), \(Y\mapsto Y+Z\), the interchanges \(X\leftrightarrow Y\), \(Y\leftrightarrow Z\), and \(X\mapsto-X\). Elementary row operations, permutations, and a nontrivial diagonal scaling generate all of \(\operatorname{GL}_3(k)\). Thus these substitutions generate all projective coordinate changes. The resulting three orbits have exactly \(936\), \(1872\), and \(936\) elements; they are disjoint, their members satisfy the tangent-filling test, and their union has the same \(3744\) elements as the complete enumeration. This proves both exhaustion and equivalence classification. As \(\#\operatorname{PGL}_3(k)=5616\), the stated stabilizer orders follow. The three classes are inequivalent because their rational-point counts differ.

For independent geometric smoothness checks, write the first and third representatives as \(X^2Z+Y^3-YZ^2-cZ^3\) with \(c\in\{0,1\}\). Their \(Y\)-derivative is \(-Z^2\); at a geometric singular point this forces \(Z=0\), and the equation forces \(Y=0\). At \([1:0:0]\), however, the \(Z\)-derivative is \(1\), a contradiction. For the middle representative \(G=X^2Z+XY^2-Y^2Z+YZ^2\), on \(Z=0\) its possible zeroes \([1:0:0]\) and \([0:1:0]\) are smooth by direct differentiation. On \(Z=1\), the equations \(G_X=0\) and \(G_Y=0\) give \(X=Y^2\) and \(Y^3=Y+1\), respectively. Substitution into \(G\) gives \(G=Y^2\), hence \(Y=0\), incompatible with \(Y^3=Y+1\). Thus all three representatives are geometrically smooth; their coordinate transforms are geometrically smooth too.

For the first representative the four rational tangent lines form the complete pencil through \([1:0:0]\), a transparent geometric witness to its covering property. The second and third representatives have six and seven distinct rational tangents and their unions also cover all thirteen rational points, as directly verified by the same incidence masks.

## Verification
Run `python verify.py` in an environment with Python \(\ge3.10\) and SymPy \(1.14.0\) (see `requirements.txt`). The code independently enumerates normalized degree-one, degree-two, and degree-three forms; computes gradients and incidence bitmasks; checks the exact counts; generates all three projective orbits; and uses Gröbner unit ideals in every affine chart to recheck geometric smoothness. It prints the totals and ends with `PASS: three disjoint PGL3(F3) orbits cover all tangent-filling cubics` only if every assertion succeeds.

## Relationship to prior work
Asgarli and Ghioca [1] introduce and study tangent-filling plane curves, construct a family for \(q\ge11\), and explicitly ask in Question 1.5 for the minimum possible degree over \(\mathbb F_q\). Their theorems and the characteristic-three remark do not classify all cubics over \(\mathbb F_3\). The present result answers that degree question at the first odd prime field and completely enumerates its cubic minimizers. Asgarli, Ghioca, and Yip [2] investigate the different condition that rational *points of the curve* form a blocking set; this does not imply a classification of tangent lines covering the ambient plane. The precise comparison is by invariant and mathematical implication, not by paper title.

## Limitations
This is a complete finite-field result only for \(\mathbb F_3\); it does not determine the minimum degree or cubic equivalence classes over other fields. The exhaustive classification is computationally certified by a self-contained finite algorithm, not by a closed-form orbit-count theorem. A matching unindexed classification in older finite-geometry literature remains a bibliographic possibility.

## References
[1] Shamil Asgarli and Dragos Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420v1 (public 2023-02-26), https://arxiv.org/abs/2302.13420 ; especially Question 1.5, Theorem 1.3 and Remark 1.4.

[2] Shamil Asgarli, Dragos Ghioca, and Chi Hoi Yip, *Plane curves giving rise to blocking sets over finite fields*, arXiv:2208.13299v1 (public 2022-08-28), https://arxiv.org/abs/2208.13299 .
