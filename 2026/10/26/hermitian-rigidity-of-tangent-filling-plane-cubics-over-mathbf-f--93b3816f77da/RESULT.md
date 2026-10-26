# Hermitian rigidity of tangent-filling plane cubics over \(\mathbf F_4\)

## Finding
Let \(k=\mathbf F_4\). A nonzero homogeneous cubic \(F\in k[X,Y,Z]\) is **tangent-filling** if the union of the projective tangent lines at its smooth \(k\)-rational curve points covers all of \(\mathbf P^2(k)\). Then **every tangent-filling cubic with no \(k\)-rational line component is projectively equivalent over \(k\)** to the smooth Hermitian cubic
\[
H:X^3+Y^3+Z^3=0.
\]
Equivalently, every geometrically integral tangent-filling plane cubic over \(\mathbf F_4\) is Hermitian, and the statement continues to hold for any cubic lacking a rational linear factor, without assuming geometric integrality. The exact enumeration is:

| Cubic equations up to nonzero scalar | Count |
|---|---:|
| All nonzero ternary cubics | 349,525 |
| Tangent-filling | 11,368 |
| Tangent-filling with a rational linear factor | 11,088 |
| Tangent-filling without a rational linear factor | **280** |
| Geometrically smooth and tangent-filling | **280** |

The last 280 equations comprise one orbit under \(\operatorname{PGL}_3(\mathbf F_4)\), with stabilizer order \(216\).

## Assumptions and scope
Use \(k=\mathbf F_2[\alpha]/(\alpha^2+\alpha+1)\), represented by the integers \(0,1,2,3\) with XOR addition and polynomial-remainder multiplication. Only ordinary projective plane cubics over the specified field are covered, and projective equivalence is over \(k\). A tangent at a rational point is included only if the gradient is nonzero there. No assertion is made about tangent lines based at nonrational points. A \(k\)-rational linear factor is equivalent to a \(k\)-line component, including when the curve is nonreduced.

The scalar normalization used in the exact count takes the coefficient of the **last nonzero monomial** to be \(1\), where the ten degree-three monomials are ordered
\[
X^3, X^2Y, X^2Z, XY^2, XYZ, XZ^2, Y^3, Y^2Z, YZ^2, Z^3.
\]
It gives one representative per nonzero scalar class, hence \((4^{10}-1)/3=349525\) possibilities.

## Proof
**Incidence certificate.** Enumerate the 21 rational projective points with normalizations \((1,u,v)\) for \(u,v\in k\), \((0,1,v)\) for \(v\in k\), and \((0,0,1)\). Use the same normalizations for the 21 rational lines. For every normalized cubic and rational point \(P\), compute \(F(P)\) and the three partial derivatives. When \(F(P)=0\) and \(\nabla F(P)\ne0\), mark the line with normal vector \(\nabla F(P)\). Its points are those satisfying \(\nabla F(P)\cdot Q=0\). Test whether the union of the marked lines contains all 21 points. Exhausting every one of the 349,525 normalized forms returns exactly 11,368 tangent-filling forms, comprising 5,320 with nine rational curve points and 6,048 with ten.

**Detecting rational components.** A homogeneous cubic restricts to a binary cubic on a rational line \(L\). Such a binary form vanishing at all five points of \(L(k)\) must vanish identically, since its degree is three. Therefore \(L\) divides \(F\) if and only if all five rational points on \(L\) lie on the cubic. The incidence search examines all 21 lines using this exact criterion. Among the 11,368 tangent-filling forms, precisely 11,088 have a rational linear factor. The remaining 280 have none. Independent Python/Numpy and C++ implementations return identical lists of the 280 coefficient vectors.

**Identifying the remaining forms.** The Hermitian cubic \(H\) is smooth because its three partial derivatives are \(X^2,Y^2,Z^2\). It is tangent-filling: its nine rational points have tangent lines whose union, checked directly in the 21-point plane, is the whole plane (also the standard Hermitian-unital polar-line property). Enumerating all \(181440\) invertible \(3\times3\) matrices over \(k\), substituting the corresponding linear forms into \(H\), and normalizing the resulting cubic gives exactly 280 distinct equations. There are 648 matrices preserving \(H\) up to scalar, corresponding to 216 projective stabilizer elements. The 280 distinct orbit equations agree **exactly** with the 280 tangent-filling equations without a rational line component. This proves the theorem, including the irreducible case.

**Independent geometric-smoothness certificate.** The three first derivatives of a cubic are homogeneous quadrics. Since the characteristic is two, Euler's identity gives \(F=X F_X+Y F_Y+Z F_Z\). Thus projective singularities are exactly the common projective zeros of these three quadrics. They have no common geometric projective zero if and only if they form a regular sequence in the three-variable polynomial ring. Its Artinian quotient then has Hilbert series \((1+t)^3\), hence vanishing degree-four component. Conversely, if their degree-four multiples span every quartic, they cannot have a common projective zero. Accordingly, geometric smoothness is **equivalent** to rank 15 of the 18-by-15 coefficient matrix of the three Jacobian quadrics multiplied by all six quadratic monomials. Exact row reduction over \(k\) on all 11,368 tangent-filling forms yields ranks 11, 13, 15 with respective counts 5,040, 6,048, 280. The rank-15 forms agree with the 280-member Hermitian orbit. This second certificate checks geometric smoothness over the algebraic closure, not only rational nonsingularity.

## Verification
In a writable directory, with C++17 compiler and Python with NumPy installed, run `sh scripts/verify.sh` from the package root. The runner compiles three independent-purpose C++ programs and invokes a separate vectorized Python incidence implementation. It recreates the raw classification lists, proves coefficient-by-coefficient agreement between implementations, recomputes the Jacobian-rank distribution, enumerates the full projective orbit, and checks that the orbit equals both the no-rational-line and smooth tangent-filling sets. `verification_output.txt` records the exact output. `tangent_noline_codes.txt` is the 280-element independent result and can be regenerated. Integer coefficient codes are base-four encodings in the specified monomial order, with digit zero the coefficient of \(X^3\).

The finite enumeration is exhaustive because every nonzero scalar class is normalized exactly once; all 21 projective points and lines are listed exactly once; all cubic tangent lines are calculated via the homogeneous gradient; and every invertible matrix is enumerated. Each script uses exact finite-field arithmetic, not floating-point approximations.

## Relationship to prior work
Asgarli and Ghioca introduced the tangent-filling condition and exhibited Hermitian curves as examples in *Tangent-filling plane curves over finite fields* (arXiv:2302.13420, first public 2023-02-26; later published in 2024). Their stated theorems give large-field nonexistence bounds and examples, rather than this small-field, all-cubics rigidity and rational-component dichotomy. Their general large-field hypotheses do not apply to degree three in characteristic two. The classical Hermitian unital and its unitary stabilizer are known: neither the example nor its stabilizer alone implies that **every** tangent-filling cubic without a rational line component is Hermitian. The extra implication follows from the complete incidence calculation here. Work on maximal-point curves gives related Hermitian characterizations conditional on attaining a point bound; the present hypothesis is instead coverage by tangent lines.

## Limitations
This is a finite-field classification confined to degree three and \(\mathbf F_4\). It is not a general theorem for arbitrary degree, arbitrary square fields, or higher-dimensional projective spaces. The proof is a computer-assisted exhaustive finite argument with the supplied source and raw coefficient certificate, not a short characteristic-free structural classification. Classification of schemes with rational line components is not asserted; only their exact total among tangent-filling cubics is given. Publication priority against inaccessible or unindexed small-field catalogues remains an open bibliographic risk. A formal independent audit has not been performed.

## References
1. S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420 (first posted 2023-02-26), DOI: 10.1017/S0004972723000382.
2. J. W. P. Hirschfeld and G. Korchmáros, *Arcs and Curves over a Finite Field*, Finite Fields and Their Applications 5 (1999), DOI: 10.1006/ffta.1999.0260.
3. S. Barwick and G. Ebert, *Unitals in Projective Planes*, Springer (2008), for classical Hermitian-unitals background.
