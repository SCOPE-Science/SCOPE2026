# Rational Eckardt-point spectrum of smooth cubic surfaces over \(\mathbf F_2\)

## Finding
Let \(S\subset\mathbf P^3_{\mathbf F_2}\) be any geometrically smooth cubic surface, and let \(e(S)\) be the number of \(\mathbf F_2\)-rational Eckardt points, i.e. rational points at which **three distinct geometric lines on the surface** concur. Among the \(322560\) smooth homogeneous cubic equations in fixed coordinates, the complete spectrum is:

| \(e(S)\) | Equations |
| ---: | ---: |
| 0 | 189952 |
| 1 | 115920 |
| 2 | 10080 |
| 3 | 2800 |
| 4 | 3360 |
| 7 | 420 |
| 15 | 28 |

Thus \(e(S)\in\{0,1,2,3,4,7,15\}\), each possibility occurs, and among geometrically smooth cubic surfaces with at most three rational points every surface has a rational Eckardt point. The smooth equations form exactly \(36\) orbits under \(\operatorname{PGL}_4(\mathbf F_2)\).

More precisely, partition the rational Eckardt points into counts \(E_0,E_1,E_3\), indexed by the number \(0,1,3\) of rational lines among the three geometric concurrent lines. For \(N=\#S(\mathbf F_2)\), and \(L\) the number of rational lines contained in \(S\), the full joint distribution is:

| \(N\) | \(L\) | \(E_0\) | \(E_1\) | \(E_3\) | Equations |
|---:|---:|---:|---:|---:|---:|
| 1 | 0 | 1 | 0 | 0 | 840 |
| 3 | 0 | 1 | 0 | 0 | 10080 |
| 3 | 0 | 3 | 0 | 0 | 1120 |
| 3 | 1 | 0 | 3 | 0 | 420 |
| 5 | 0 | 0 | 0 | 0 | 44352 |
| 5 | 0 | 1 | 0 | 0 | 25200 |
| 5 | 1 | 0 | 1 | 0 | 10080 |
| 5 | 1 | 0 | 2 | 0 | 5040 |
| 7 | 0 | 0 | 0 | 0 | 40320 |
| 7 | 0 | 1 | 0 | 0 | 13440 |
| 7 | 1 | 0 | 0 | 0 | 40320 |
| 7 | 1 | 0 | 1 | 0 | 35280 |
| 7 | 3 | 0 | 6 | 1 | 420 |
| 9 | 0 | 1 | 0 | 0 | 840 |
| 9 | 1 | 0 | 0 | 0 | 23520 |
| 9 | 2 | 0 | 0 | 0 | 40320 |
| 9 | 3 | 0 | 0 | 0 | 1120 |
| 9 | 3 | 0 | 1 | 0 | 10080 |
| 9 | 3 | 0 | 1 | 1 | 5040 |
| 9 | 3 | 0 | 3 | 1 | 1680 |
| 11 | 5 | 0 | 0 | 1 | 10080 |
| 11 | 5 | 0 | 1 | 2 | 1260 |
| 13 | 9 | 0 | 0 | 4 | 1680 |
| 15 | 15 | 0 | 0 | 15 | 28 |

All counts refer to distinct coefficient vectors (in characteristic two, there is no nontrivial scalar rescaling), not to arithmetic isomorphism classes unless expressly stated.

## Assumptions and scope
The base field is exactly \(\mathbf F_2\). The ambient is \(\mathbf P^3\) with fixed homogeneous coordinates. The classification exhausts all \(2^{20}\) binary coefficient vectors of homogeneous degree-three polynomials in four variables, including the zero vector only for bookkeeping. Geometric smoothness means no singular geometric point over the algebraic closure. The word 'Eckardt' requires three *distinct geometric lines*, not merely a rational tangent plane with multiplicity. A rational Eckardt point need not lie on any rational line: its three lines can be permuted as one Frobenius orbit.

## Proof
**Exact smoothness criterion.** Write \(F\) for a homogeneous cubic and \(J_F\) for the ideal of its four homogeneous quadratic partial derivatives. Euler's formula in characteristic two gives \(F=\sum_i X_i(\partial F/\partial X_i)\). Thus the projective cubic is geometrically smooth exactly when the four partial derivatives have no common projective zero. Equivalently, \(J_F\) is irrelevant-primary, so the four quadrics are a homogeneous regular sequence. Their quotient then has Hilbert series \((1+t)^4\), in particular zero degree-five part. Conversely, if \((J_F)_5\) spans all \(56\) degree-five monomials, the projective common zero set is empty (a homogeneous ideal with a projective zero cannot contain every form of degree five). Thus geometric smoothness is **equivalent** to a \(56\)-rank test over \(\mathbf F_2\) on the matrix of \(X^\alpha\partial F/\partial X_i\), with \(|\alpha|=3\). The equivalence is algebraic, not a bounded extension-field experiment.

**Exact Eckardt criterion.** Fix a rational smooth point \(P\) and its tangent plane \(H_P\). Choose independent \(\mathbf F_2\)-vectors \(P,A,B\) spanning that plane and restrict the cubic to its coordinates \([t:u:v]\), where \(P=[1:0:0]\). Because \(P\in S\) and \(H_P\) is tangent, the restriction uniquely has the form \(tQ(u,v)+B_3(u,v)\), where \(Q\) is quadratic and \(B_3\) is homogeneous cubic. Three geometric lines on \(S\) through \(P\) occur precisely if \(Q=0\) and \(B_3\) has three distinct geometric roots. Writing \(B_3=a u^3+b u^2v+c uv^2+d v^3\), squarefreeness over \(\overline{\mathbf F}_2\) is equivalent to \(ad+bc=1\). Count its roots in \(\mathbf P^1(\mathbf F_2)\): Frobenius invariance forces \(0,1\), or \(3\), which yield \(E_0,E_1,E_3\). Independently, one may check vanishing of the polar derivative \(D_PF\) on the tangent plane and count rational contained lines through \(P\) directly. The two implementations use these two tests respectively.

**Completeness.** Enumerate all \(2^{20}\) coefficients, use the rank criterion for geometric smoothness, test the fifteen rational projective points, and test all thirty-five rational lines. The direct exhaustive program independently obtains exactly \(322560\) smooth coefficient vectors and the \(24\) rows in the table. A second program enumerates all orbits of the full group generated by twelve elementary transvections in \(\mathrm{GL}_4(\mathbf F_2)\), obtaining \(142\) total equation orbits, \(36\) smooth ones, and \(322560\) smooth equations. On the latter representatives the tangent-plane binary-cubic criterion supplies \(E_0,E_1,E_3\); weighting by the computed orbit sizes reproduces the direct exhaustive table. Two independent methods also check smoothness for the \(36\) representatives: the degree-five rank criterion and exact affine-chart Gröbner bases of the gradient ideal.

The 24-row joint table implies the displayed marginal and the three-point consequence. It also shows that every value listed in the marginal occurs. No inference about the geometric Frobenius action on all twenty-seven lines beyond the stated triple splitting is made.

## Verification
Source code and outputs are embedded in the accompanying package, with the monomial order fixed by the coefficient encodings. Using C++17 and Python 3 with SymPy installed, run from the directory containing the package files:

```
g++ -O3 -std=c++17 cubic_enum.cpp -o cubic_enum
./cubic_enum > summary.txt
python3 eckardt.py > eckardt_summary.txt
g++ -O3 -std=c++17 direct_enum.cpp -o direct_enum
./direct_enum > direct_summary.txt
python3 check_groebner.py > groebner_summary.txt
```

The first command generates `orbit_cubic.tsv`; the second uses its 36 smooth representatives and writes `eckardt_orbits.tsv`. The direct enumerator uses the independently encoded quadratic-polar test, not orbit weights. `direct_summary.txt` contains the 24-row census; `eckardt_summary.txt` contains the same profiles grouped into 36 orbits and the Eckardt marginal. `groebner_summary.txt` reports 36 checked representatives and zero failures. Machine-generated tables and code are included for exact replay. The full exhaustive domain is finite and specified; each program terminates by explicit bounded loops.

## Relationship to prior work
Das, *Arithmetic statistics on cubic surfaces* (first publicly posted 2020-02-25, arXiv:2002.11183), describes Frobenius arithmetic statistics for cubic surfaces and tabulates distributions of rational points and lines. Its Remark 2.2 flags Eckardt configurations as a genuine subtlety; the present joint rational Eckardt incidence distribution is not its point/line marginal. McKean, *Rational lines on smooth cubic surfaces* (arXiv:2101.08217), studies rational-line possibilities, not this refined spectrum. Kadyrsizova and collaborators, *Cubic Surfaces of Characteristic Two* (arXiv:2007.12018), analyze geometric automorphisms and Eckardt phenomena in characteristic two, rather than a census of arithmetic Eckardt counts across all forms. Brosowsky and collaborators, *Geometry of Smooth Extremal Surfaces* (arXiv:2110.15908), describe large Eckardt configurations of exceptional Fermat/extremal surfaces; those are not asserted new here. Vikulova, *The most symmetric smooth cubic surface over a finite field of characteristic 2* (arXiv:2312.17032), characterizes maximally symmetric cases, not the full joint incidence distribution. Existence and standard 27-line properties are background, not claimed discoveries.

## Limitations
This is an exact \(\mathbf F_2\) classification, not a formula for arbitrary finite fields; it is about coefficient vectors and a finite number of projective orbits, not an asserted count of abstract surfaces with markings forgotten. Some distributions could be derivable indirectly from historical classification tables or unindexed computational catalogues; exhaustive search and failure to locate them do not establish priority. All computational statements are finite and independently reproduced but have not undergone outside validation. No independent audit has been performed.

## References
- R. Das, *Arithmetic statistics on cubic surfaces*, arXiv:2002.11183 (first public preprint, 2020-02-25), https://arxiv.org/abs/2002.11183.
- N. Kadyrsizova et al., *Cubic Surfaces of Characteristic Two*, arXiv:2007.12018, https://arxiv.org/abs/2007.12018.
- S. McKean, *Rational lines on smooth cubic surfaces*, arXiv:2101.08217, https://arxiv.org/abs/2101.08217.
- J. Brosowsky et al., *Geometry of Smooth Extremal Surfaces*, arXiv:2110.15908, https://arxiv.org/abs/2110.15908.
- A. Vikulova, *The most symmetric smooth cubic surface over a finite field of characteristic 2*, arXiv:2312.17032, https://arxiv.org/abs/2312.17032.
