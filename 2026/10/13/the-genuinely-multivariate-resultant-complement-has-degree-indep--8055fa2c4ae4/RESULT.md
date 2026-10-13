# The genuinely multivariate resultant complement has degree-independent Euler characteristic
## Finding
Let
\[
n\ge3,
\qquad
d_1,\ldots,d_n\ge1,
\]
and set
\[
N_i=\binom{n+d_i-1}{n-1}.
\]
Consider the product of projective coefficient spaces
\[
A_{\mathbf d}
=
\prod_{i=1}^n
\mathbb P\!\left(\operatorname{Sym}^{d_i}\mathbb C^n\right).
\]
Let
\[
R_{\mathbf d}\subset A_{\mathbf d}
\]
be the Macaulay resultant locus: the set of ordered systems
\[
([f_1],\ldots,[f_n])
\]
of homogeneous forms of degrees
\[
d_1,\ldots,d_n
\]
that have a common zero in
\[
\mathbb P^{n-1}.
\]
Write
\[
U_{\mathbf d}
=
A_{\mathbf d}\setminus R_{\mathbf d}.
\]

Then
\[
\boxed{
\chi_c(U_{\mathbf d})=n!.
}
\]
Consequently,
\[
\boxed{
\chi_{\mathrm{top}}(R_{\mathbf d})
=
\prod_{i=1}^n\binom{n+d_i-1}{n-1}-n!.
}
\]

Thus the compactly supported Euler characteristic of the genuinely multivariate non-resultant locus is independent of every degree.

For example, three linear forms in three variables give
\[
\chi_c(U_{(1,1,1)})=6,
\qquad
\chi_{\mathrm{top}}(R_{(1,1,1)})=27-6=21,
\]
while three quadrics in three variables give
\[
\chi_c(U_{(2,2,2)})=6,
\qquad
\chi_{\mathrm{top}}(R_{(2,2,2)})=216-6=210.
\]

## Assumptions and scope
The ground field is
\[
\mathbb C.
\]
The integer
\[
n\ge3
\]
is the number of variables and also the number of homogeneous equations, so the Macaulay resultant is defined for a square homogeneous system.

The coefficient of an individual form is projectivized independently. This is the natural multiprojective parameter space because the Macaulay resultant is multihomogeneous in the coefficient blocks.

The restriction
\[
n\ge3
\]
is the genuinely multivariate regime. Binary-variable resultant spaces have additional factorization and symmetric-product descriptions and are not part of the statement here.

## Proof
Choose an integer
\[
B>\max_i d_i
\]
and let
\[
\mathbb C^*
\]
act diagonally on the variables by
\[
t\cdot x_j=t^{B^{j-1}}x_j,
\qquad
1\le j\le n.
\]
This induces an algebraic action on every coefficient projective space and hence on
\[
A_{\mathbf d}.
\]
The common-zero condition is invariant under change of variables, so both
\[
R_{\mathbf d}
\quad\text{and}\quad
U_{\mathbf d}
\]
are invariant.

Fix a degree
\[
d<B.
\]
A monomial
\[
x_1^{a_1}\cdots x_n^{a_n},
\qquad
\sum_j a_j=d,
\]
has weight
\[
\sum_{j=1}^n a_jB^{j-1}.
\]
Because
\[
0\le a_j<B,
\]
base-\(B\) expansion shows that two distinct degree-\(d\) monomials have distinct weights. Therefore the fixed points of each projective coefficient factor are exactly its monomial coordinate points, and the fixed points of
\[
A_{\mathbf d}
\]
are exactly ordered tuples of monomials
\[
(m_1,\ldots,m_n),
\qquad
\deg m_i=d_i.
\]

We now classify which such tuples lie in
\[
U_{\mathbf d}.
\]
For a monomial
\[
m,
\]
write
\[
\operatorname{supp}(m)
\]
for the set of variables occurring with positive exponent.

Suppose first that the monomials
\[
m_1,\ldots,m_n
\]
have no common projective zero. Fix a variable
\[
x_j.
\]
At the coordinate point
\[
[0:\cdots:0:1:0:\cdots:0]
\]
with only the \(j\)-th coordinate nonzero, at least one monomial must be nonzero. The only degree-\(d_i\) monomial nonzero there is
\[
x_j^{d_i}.
\]
Hence, for every
\[
j=1,\ldots,n,
\]
one of the \(n\) monomials is a pure power of \(x_j\).

There are exactly \(n\) monomials and \(n\) variables. Therefore every monomial is a pure power and the variables occur exactly once. Thus there is a unique permutation
\[
\sigma\in S_n
\]
such that
\[
m_i=x_{\sigma(i)}^{d_i}
\qquad
\text{for all }i.
\]

Conversely, for every permutation
\[
\sigma\in S_n,
\]
the system
\[
x_{\sigma(1)}^{d_1},\ldots,x_{\sigma(n)}^{d_n}
\]
has no common projective zero: at any nonzero projective point at least one coordinate \(x_j\) is nonzero, and the unique pure power assigned to \(x_j\) does not vanish there.

Hence
\[
U_{\mathbf d}^{\mathbb C^*}
=
\left\{
([x_{\sigma(1)}^{d_1}],\ldots,[x_{\sigma(n)}^{d_n}]):
\sigma\in S_n
\right\},
\]
a finite set of exactly
\[
n!
\]
points.

For any complex algebraic variety
\[
Y
\]
with an algebraic
\[
\mathbb C^*
\]
action,
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}).
\]
One direct proof removes the fixed locus and uses a finite Rosenlicht stratification; after refining by stabilizer type, each nonfixed stratum is a locally trivial bundle with fiber a finite quotient of
\[
\mathbb C^*,
\]
whose compactly supported Euler characteristic is zero.

Applying this to
\[
U_{\mathbf d}
\]
gives
\[
\chi_c(U_{\mathbf d})=n!.
\]

Finally,
\[
\chi_{\mathrm{top}}(A_{\mathbf d})
=
\prod_{i=1}^n N_i
=
\prod_{i=1}^n\binom{n+d_i-1}{n-1}.
\]
Since
\[
A_{\mathbf d}=R_{\mathbf d}\sqcup U_{\mathbf d}
\]
and
\[
R_{\mathbf d}
\]
is projective, constructible additivity yields
\[
\chi_{\mathrm{top}}(R_{\mathbf d})
=
\prod_{i=1}^n\binom{n+d_i-1}{n-1}-n!.
\]

## Verification
The bundled checker performs a direct monomial census in two genuinely multivariate regression ranges:
\[
n=3,
\qquad
1\le d_i\le3,
\]
and
\[
n=4,
\qquad
1\le d_i\le2.
\]

For every parameter tuple it constructs all monomials explicitly. It tests common projective zeros without using the pure-power classification: for every nonempty coordinate support it asks whether all selected monomials vanish on points with exactly that support.

Across
\[
43
\]
parameter tuples, it checks
\[
45275
\]
monomial fixed-point systems and finds exactly
\[
546
\]
non-resultant fixed points in total, namely
\[
27\cdot3!+16\cdot4!.
\]
It also performs
\[
961
\]
direct weight-separation checks for the base-weight construction.

These finite computations are regression evidence only. The all-degree theorem follows from the symbolic fixed-point classification.

## Relationship to prior work
D'Andrea and Dickenstein treat the Macaulay resultant of
\[
n
\]
homogeneous forms in
\[
n
\]
variables and develop explicit determinantal formulas for it. Their full text gives the exact square-system object used here and places it in algebraic geometry, but does not discuss Euler characteristic or topology.

Vassiliev studies topology of spaces of non-resultant homogeneous polynomial systems in two variables and computes rational cohomology in the complex case. That work is confined to the binary-variable regime and an affine coefficient-space formulation; it does not state the genuinely multivariate multiprojective formula above.

Earlier and later topology papers on resultants largely treat monic univariate systems, binary homogeneous systems, real systems, bounded multiplicity, or stable homotopy. Targeted searches did not locate the degree-independent value
\[
\chi_c(U_{\mathbf d})=n!
\]
for square systems in at least three variables, nor the equivalent Euler formula for the multiprojective resultant locus.

## Limitations
Euler characteristic is coarse. The formula does not determine the homotopy type, individual Betti numbers, mixed Hodge structure, singular locus, or degree of the resultant hypersurface.

The theorem concerns the product of independently projectivized coefficient spaces. A single common projectivization of the direct sum is a different compactification and has a different fixed-point geometry.

The proof is short once the torus action is chosen, so an older unindexed or folklore observation remains a residual originality risk.

## References
Carlos D'Andrea and Alicia Dickenstein, *Explicit formulas for the multivariate resultant*, arXiv:math/0007036, first submitted 6 July 2000; *Journal of Pure and Applied Algebra* 164 (2001), 59--86, DOI 10.1016/S0022-4049(00)00145-6.

V. A. Vassiliev, *Homology of spaces of non-resultant polynomial systems in \(\mathbb R^2\) and \(\mathbb C^2\)*, arXiv:1409.6005, first submitted 21 September 2014; *Arnold Mathematical Journal* 1 (2015), 233--242, DOI 10.1007/s40598-015-0018-2.
