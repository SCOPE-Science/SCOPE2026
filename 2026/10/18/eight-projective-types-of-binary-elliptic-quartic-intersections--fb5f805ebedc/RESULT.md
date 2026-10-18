# Eight projective types of binary elliptic quartic intersections

## Finding
Let \(k=\mathbf F_2\). Among the \(174251\) two-dimensional \(k\)-subspaces of the ten-dimensional vector space of homogeneous quadrics on \(\mathbf P^3_k\), exactly \(40320\) have geometrically smooth common zero scheme. Each such common zero scheme is a degree-four genus-one curve. Under \(\operatorname{PGL}_4(k)\), these smooth pencils form **eight orbits**. Their full distribution by \(N=\#C(k)\) and by the point counts of the three nonzero quadrics is as follows.

| Representative masks | Orbit size | \(N\) | Three quadric point counts | Rational order-four osculating planes | Four rational points coplanar |
|---|---:|---:|---|---:|---|
| `20,555` | 5040 | 1 | \((5,5,7)\) | 1 | not applicable |
| `40,205` | 5040 | 2 | \((5,5,9)\) | 0 | not applicable |
| `20,613` | 5040 | 2 | \((5,7,7)\) | 2 | not applicable |
| `20,552` | 10080 | 3 | \((5,7,9)\) | 1 | not applicable |
| `40,206` | 5040 | 4 | \((5,9,9)\) | 0 | no |
| `20,609` | 2520 | 4 | \((7,7,9)\) | 4 | no |
| `20,842` | 2520 | 4 | \((7,7,9)\) | 0 | yes |
| `20,554` | 5040 | 5 | \((7,9,9)\) | 1 | not applicable |

A smooth quadric with five rational points is nonsplit; one with nine is split. Every seven-point quadric in this table is a cone with one rational vertex. Thus exactly \(10080\), \(20160\), and \(10080\) smooth base curves have respectively three, two, and one smooth quadric among their defining pencil's rational members.

The three classes with \(N=4\) are geometrically distinguished: one admits four rational hyperplanes whose intersection with the curve is \(4P\) for a rational point \(P\), one has its four rational points coplanar, and the third has neither property. In particular, the two \((7,7,9)\)-profile classes are genuinely distinct despite having the same rational-point and quadric-profile data.

## Assumptions and scope
A *quadric pencil* means a two-dimensional subspace \(W\subset H^0(\mathbf P^3_k,\mathcal O(2))\), not an ordered pair and not a pencil with a prescribed ambient smooth quadric. It has exactly three nonzero equations. The *base curve* is the scheme-theoretic common zero locus of any basis of \(W\). Geometric smoothness refers to smoothness after extension to an algebraic closure, not just regularity at rational points. The group is the full \(\operatorname{PGL}_4(\mathbf F_2)=\operatorname{GL}_4(\mathbf F_2)\). An order-four osculating plane is a rational hyperplane whose scheme-theoretic intersection divisor with \(C\) equals \(4P\) at some \(P\in C(\mathbf F_2)\).

Masks use the bit order
\[
(x_0^2,x_0x_1,x_0x_2,x_0x_3,x_1^2,x_1x_2,x_1x_3,x_2^2,x_2x_3,x_3^2).
\]
The two decimal masks determine a pair of forms by taking the coefficient of each monomial modulo two; the third nonzero form is their bitwise exclusive-or. There are no scalar ambiguities over \(\mathbf F_2\).

## Proof
**Finite parameter domain.** The vector space of quadratic forms has dimension ten. The number of two-dimensional subspaces is the Gaussian binomial
\[
{10\brack 2}_2=\frac{(2^{10}-1)(2^{10}-2)}{(2^2-1)(2^2-2)}=174251.
\]
Each is represented uniquely by the first two entries \((a,b)\) in the increasing ordering of its three nonzero bit masks \(a,b,a\mathbin{\oplus}b\).

**Projective orbits.** The adjacent coordinate transpositions together with the elementary substitution \(x_0\mapsto x_0+x_1\) generate \(\operatorname{GL}_4(\mathbf F_2)\) (conjugation gives every elementary transvection). Their induced actions on all ten quadratic monomials are computed by exact binary expansion. Orbit traversal partitions all \(174251\) pencils into exactly \(54\) orbits, with total size \(174251\). Exactly eight orbit representatives pass the geometric Jacobian test below. Their orbit sizes are listed in the table; they sum to \(40320\).

**Geometric smoothness test.** For every representative \((Q_a,Q_b)\), form the six two-by-two minors of the two-by-four homogeneous Jacobian matrix. A geometric singularity of \(V(Q_a,Q_b)\) is precisely a common zero of these eight homogeneous polynomials. On each of the four affine charts \(x_i=1\), the Gröbner basis of the resulting ideal is computed over \(\mathbf F_2\); the ideal contains \(1\) if and only if that chart has no geometric singular point, by the Nullstellensatz. All four chart ideals contain \(1\) for exactly eight of the \(54\) orbit representatives. This criterion detects nonrational geometric singularities and is not a bounded-extension heuristic. Because the intersection of two quadrics in \(\mathbf P^3\) is a smooth codimension-two complete intersection, it is a connected genus-one curve of degree four by adjunction: \(\omega_C\cong\mathcal O_C(-4+2+2)\cong\mathcal O_C\).

**Arithmetic and quadric profiles.** There are \(15\) rational points in \(\mathbf P^3(\mathbf F_2)\), represented by nonzero binary coordinate vectors. Testing the two equations yields each stated value of \(N\). Testing each of the three pencil members yields the sorted quadric-point triple, with values \(5,7,9\). For these representatives the five- and nine-point quadrics are nonsingular and respectively nonsplit and split. Direct differentiation of the seven-point forms gives a unique rational singular vertex. Since rational point counts, geometric smoothness, and the unordered triple of quadrics are invariant under projective substitution, the table covers every pencil in the orbit.

**The two hidden four-point types.** The representatives \((20,609)\) and \((20,842)\) both give \(N=4\) and quadric profile \((7,7,9)\). In the first case the four rational points are not coplanar. At \(P=[0:0:1:0]\) the plane \(x_0=0\) has the following local intersection ideal on \(x_2=1\):
\[
(x_1+x_3^3+x_3^2,\ x_3^4).
\]
There are no points of this intersection on \(x_2=0\). Its length is four and its support consists only of \(P\), proving a rational contact divisor \(4P\). A truncated local parameter calculation through order three shows one such osculating plane at each of the four rational points. For \((20,842)\), its four rational points all lie on \(x_1=0\), and no rational order-four osculating plane exists. For \((40,206)\), its four rational points are not coplanar and there is no such osculating plane. The latter two nonexistence assertions are checked using the exact local series algorithm described below; only expansions through order three are required, because any plane intersection has total degree four.

## Verification
The standalone `verify.py` script reconstructs all \(174251\) binary pencils and all \(54\) projective orbits, computes geometric smoothness by Gröbner bases on the four charts, and reproduces every row, including contact and coplanarity tests. The script uses Python 3 and SymPy with exact characteristic-two arithmetic. It prints `VERIFY_OK` only after checking the totals, all eight orbit sizes, the rational-point multiplicities, and the three four-point osculation/coplanarity strata.

The separate standard-library `verify_orbits.py` enumerates all \(20160\) invertible four-by-four binary coordinate matrices, independently computes the eight projective orbit sizes directly, and checks the rational coplanarity properties. It also records the local-algebra contact certificate displayed above. Its successful output ends in `VERIFY_INDEPENDENT_OK`. Captured outputs are supplied in `verify_output.txt` and `verify_orbits_output.txt`. Both included programs can be extracted and rerun from the embedded source files; the supplied outputs record the exact checks.

## Relationship to prior work
The classical identification of a degree-four genus-one model with a pair of quadrics is established in work of Fisher and presented in Manh Hung Tran's 2019 preprint on invariants of genus-one models. In particular, the literature describes generic invariants and the map to the Jacobian, not this exact characteristic-two projective census, three-quadric point-profile distribution, or rational osculation/coplanarity distinction. Fisher's 2010 Hessian treatment explicitly assumes characteristic not dividing \(6n\), so its characteristic-zero Hesse formulas do not directly establish this binary classification. Levine's 2017 work refines enumerative formulas for quadratic forms but assumes characteristic different from two for the results examined; its quadric Euler characteristics do not imply the eight embedded types here.

A projective normal elliptic quartic is a natural first codimension-two genus-one model. The jointly recorded invariants answer how arithmetic point spectra coexist with split, nonsplit and conical rational members of its defining quadric pencil. The two same-profile, same-point-count four-point classes show that these coarse data do not alone determine the embedded model.

## Limitations
This is a complete classification only over \(\mathbf F_2\) for scheme-theoretic intersections of two independent quadrics in \(\mathbf P^3\). It does not classify singular base curves, larger finite fields, or models with extra marked structure. The exhaustive verification is finite and exact, not a general theorem about all fields. The literature search did not reveal an equivalent earlier binary table, but no search can certify universal priority; obscure prior enumerations or a non-obvious specialization of broader invariant theory remain possible. The stated classification has no independent publication-priority certification; the possibility of an earlier unindexed equivalent table remains a literature risk.

## References
1. M. H. Tran, *Invariants of models of genus one curves and modular forms*, arXiv:1911.01350v1 (first submitted 2019-11-04), sections 1, 2.4, 2.6 and 3 (HTML version v2 consulted).
2. T. Fisher, *The Hessian of a genus one curve*, 2010, definition 2.1 and discussion of degree-four models; original PDF at `https://www.dpmms.cam.ac.uk/~taf1000/papers/g1hessians.pdf`.
3. M. Levine, *Aspects of enumerative geometry with quadratic forms*, arXiv:1703.03049v1 (first submitted 2017-03-08), introduction and quadratic-form comparison (HTML v7 consulted).
