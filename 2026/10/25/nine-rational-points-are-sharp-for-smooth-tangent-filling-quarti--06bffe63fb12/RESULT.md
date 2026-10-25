# Nine rational points are sharp for smooth tangent-filling quartics over \(\mathbf F_5\)

## Finding

Let \(C\subset\mathbf P^2_{\mathbf F_5}\) be a geometrically smooth plane quartic. Suppose that every point of \(\mathbf P^2(\mathbf F_5)\) lies on the tangent line at some point of \(C(\mathbf F_5)\). Then
\[
\#C(\mathbf F_5)\ge 9.
\]
This bound is attained in two geometrically distinct dual-incidence modes: there exist such smooth quartics with exactly nine rational points whose nine distinct rational tangent lines (a) contain the full pencil of six lines through one rational point, and (b) contain no full rational pencil. The two curves are not asserted to represent all extremal projective classes.

Write \(X,Y,Z\) for the coordinates, and interpret coefficients in \(\mathbf F_5\). Explicit equations for the two cases are
\[
\begin{aligned}
F_{\mathrm{pencil}}={}&X^4+X^3Y+4X^3Z+X^2Y^2+X^2YZ+X^2Z^2\\
&+XY^3+2XY^2Z+3XYZ^2+2YZ^3,\\[2pt]
F_{\mathrm{nontrivial}}={}&4X^3Y+2X^3Z+2X^2Y^2+4X^2YZ+3X^2Z^2\\
&+2XY^3+XY^2Z+4XYZ^2+4XZ^3\\
&+2Y^3Z+3Y^2Z^2+2YZ^3+Z^4.
\end{aligned}
\]
Each zero locus has exactly nine \(\mathbf F_5\)-rational points, whose nine tangent lines cover all 31 rational points of the plane. Their genera are three.

## Assumptions and scope

Throughout, the base field is exactly \(\mathbf F_5\). A plane quartic is *geometrically smooth* if the three homogeneous first partial derivatives have no simultaneous projective zero over an algebraic closure. By Euler's relation in characteristic five, this implies smoothness of its projective zero locus. A tangent-filling curve is one whose tangent lines at its smooth rational points cover all rational points of the projective plane. The quantity minimized is the number of rational **curve points**, not the number of tangent lines. A full pencil means the six \(\mathbf F_5\)-lines through a single rational point.

## Proof

**Dual-cover reduction.** For each rational curve point \(Q\), its tangent line is a rational line. The set \(B\) of distinct tangent lines is a blocking set in the *dual* projective plane: it meets every dual line because the union of the corresponding ordinary lines covers \(\mathbf P^2(\mathbf F_5)\). Moreover \(|B|\le\#C(\mathbf F_5)\). Exact finite-incidence enumeration in `verify_dual_blocking.cpp` examines all \(\binom{31}{8}=7,888,725\) eight-element sets of rational lines. Among 9,300 whose union covers all 31 rational points, **every one contains the six lines through some rational point**. Any covering set of fewer than eight lines can be enlarged to eight lines; therefore any dual blocking set of at most eight points contains an entire dual line. This also follows from Blokhuis's lower bound \(3(p+1)/2=9\) for a nontrivial blocking set in \(\mathrm{PG}(2,p)\).

**Elimination of an eight-point full-pencil curve.** It remains to exclude a geometrically smooth quartic with at most eight rational points and with all six lines through a rational point \(P\) tangent at rational curve points. Change rational coordinates to \(P=[0:0:1]\). The six lines through \(P\) are indexed by \((x,y)=(1,t)\) for \(t\in\mathbf F_5\), and \((x,y)=(0,1)\). A rational tangency point on a chosen line other than \(P\) has the form \([x:y:z]\), with \(z\in\mathbf F_5\). Its tangency conditions are the two **linear** equations \(F(x,y,z)=F_Z(x,y,z)=0\). The second condition, together with Euler's formula, makes the line through \(P\) tangent whenever the rational gradient is nonzero. If the contact point is \(P\), the two linear conditions are \(F(P)=0\) and \(xF_X(P)+yF_Y(P)=0\). A nonsingular \(P\) can be the contact point for at most one of the six lines.

Consequently there are exactly \(5^6+6\cdot5^5=34,375\) possible patterns specifying one contact point on each line, with either no contact at \(P\) or exactly one. For each pattern, form the indicated 12-by-15 linear system in the coefficients of the fifteen quartic monomials. Row-reduce over \(\mathbf F_5\), enumerate every nonzero vector in the kernel, and discard vectors that have a rational projective point at which all first derivatives vanish. The complete enumeration in `verify_pencil_lower.cpp` finds coefficient-matrix ranks nine for 25 patterns, eleven for 750 patterns, and twelve for 33,600 patterns. Across all patterns it finds **no rationally nonsingular equation with fewer than nine rational curve points**. This search need not determine geometric smoothness: every geometrically smooth quartic is necessarily nonsingular at all its rational points and so belongs to the tested superset. Any full rational pencil is equivalent to the one fixed above, so the conclusion is coordinate-independent. Together with the dual-cover reduction, this proves the lower bound.

**Sharpness and the two modes.** For each displayed polynomial, `verify_examples.py` evaluates the form and first partial derivatives at all 31 normalized rational projective points, records the nine rational curve points, and checks that their nine distinct tangent lines cover all 31 points. In the first example, six tangent lines pass through \([0:0:1]\); in the second example no rational point lies on six of the distinct tangent lines. Finally, on each of the three affine charts \(X=1\), \(Y=1\), and \(Z=1\), the Gröbner basis of the ideal generated by the three first derivatives of each form is \([1]\) over \(\mathbf F_5\). Thus neither quartic has any geometric singular point, not merely any rational singular point. A smooth plane quartic is geometrically integral and has genus \((4-1)(4-2)/2=3\).

## Verification

The following three commands reproduce the complete finite certificates from the **standalone source files included here**:

```sh
g++ -O3 -std=c++17 verify_dual_blocking.cpp -o verify_dual_blocking
./verify_dual_blocking

g++ -O3 -std=c++17 verify_pencil_lower.cpp -o verify_pencil_lower
./verify_pencil_lower

python3 verify_examples.py
```

The first reports exactly 7,888,725 eight-line subsets, 9,300 covering subsets and zero covering subsets lacking a full pencil. The second reports 34,375 contact patterns with rank distribution \(25,750,33,600\), and smallest rational-point count nine among its rationally nonsingular solutions. The third reports two nine-point curves, two nine-line coverings, their respective pencil distinctions, and three unit Jacobian ideals for each example. `verify_examples.py` needs SymPy; the two C++ programs need only a standard C++17 compiler. Reference outputs are included as `dual_blocking_output.txt`, `pencil_lower_output.txt`, and `examples_output.txt`.

## Relationship to prior work

Asgarli and Ghioca, *Tangent-filling plane curves over finite fields* (arXiv:2302.13420, first posted 2023-02-26), introduce the tangent-filling condition, relate it to blocking sets in the dual plane, prove large-field exclusion results, and provide Hermitian and other constructions. Their full accessible text discusses the failure of their general degree-\(q-1\) family to be tangent-filling when \(q=5\); it does not state the sharp **minimum rational-point count nine among smooth degree-four tangent-filling curves over \(\mathbf F_5\)**, nor the two explicit dual-incidence modes above. Blokhuis's 1994 blocking-set inequality supplies the general nontrivial-dual lower bound but by itself does not exclude the full-pencil case or produce smooth curves attaining nine. Previously computed bounds for tangent coverage of ternary cubics over \(\mathbf F_5\) concern degree three and do not imply this degree-four cardinality theorem. General point-count tables for genus-three curves do not, by mere point counts, certify the tangent-covering condition.

## Limitations

The minimum and examples concern \(\mathbf F_5\) and geometrically smooth plane quartics only, not arbitrary singular quartics, higher degrees, or fields of other orders. The calculation is a finite complete exact search for the potential full-pencil case, but is not a classification of all nine-point quartics. The two displayed curves demonstrate two distinct line-incidence types, not complete projective-orbit classifications. No independent external validation or publication-priority certification is claimed; earlier unindexed small-field enumerations could in principle contain the same sharp bound.

## References

1. S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420, version 1 dated 2023-02-26; *Bulletin of the Australian Mathematical Society* 109 (2024), 301–315, DOI:10.1017/S0004972723000382.
2. A. Blokhuis, *On the size of a blocking set in PG(2,p)*, *Combinatorica* 14 (1994), 111–114, DOI:10.1007/BF01305953.
