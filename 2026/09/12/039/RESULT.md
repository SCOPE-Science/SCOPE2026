# Dependent non-torsion node extensions in a two-node genus-three degeneration

## Finding

For the smooth projective hyperelliptic family
\[
C_t:\quad y^2=x(x-t)(x-1)(x-1-t)(x-2)(x-3)(x-4),
\qquad 0<|t|<1/2,
\]
the monodromy logarithm \(N\) has rank two and \(N^2=0\). The monodromy weight filtration shifted to weight one has graded dimensions \((2,2,2)\). The two node extension classes in the Jacobian of the normalization satisfy
\[
e_1=-e_2=e,\qquad e\ne0,
\]
and \(e\) has infinite order. Thus individually non-torsion node extensions need not be independent. The conclusion here is a relation between extension classes, not an assertion about every choice of unreduced analytic period representatives.

## Assumptions and scope

At \(t=0\) the normalization is the elliptic curve
\[
E:\quad Y^2=X^3-X,
\quad X=x-3,
\quad y=x(x-1)Y.
\]
Put \(K=\mathbb Q(s)\), \(s^2=-6\), and choose the preimages
\[
P_1^\pm=(-3,\pm2s),\qquad P_2^\pm=(-2,\pm s).
\]
The origin is the point at infinity and
\(e_i=[P_i^+-P_i^-]=2P_i^+\) in \(E(K)\). Statements about rational splitting refer to these classes tensored with \(\mathbb Q\). No general claim about all two-node degenerations or Ceresa height pairings is made.

## Proof

The seven finite roots are distinct in the stated punctured disc. Hence the smooth fiber has genus three. The central fiber has exactly two ordinary nodes, at \(x=0,1\), and its normalization has genus one.

The two disjoint vanishing cycles \(\delta_1,\delta_2\) have zero mutual intersection. For this particular parameterization, the local smoothing parameters have order two in \(t\): after dividing by a holomorphic square root of the nonvanishing factor, each local equation is equivalent to \(z^2=x(x-t)\), and completing the square gives smoothing proportional to \(t^2\). A loop in \(t\) therefore induces the square of each local Picard–Lefschetz twist. Consequently
\[
T_i(v)=v+2\langle v,\delta_i\rangle\delta_i,
\qquad N=N_1+N_2.
\]
Both cycles are independent and nonseparating; the normalization has genus one and the dual graph has two loops. In a symplectic basis extending them, \(N\) maps two dual basis elements to nonzero multiples of \(\delta_1,\delta_2\) and kills the other four. Thus its rank is two, its square vanishes, and
\[
W_0=\operatorname{im}N,\quad W_1=\ker N,\quad W_2=H^1,
\quad \dim\operatorname{Gr}^W=(2,2,2).
\]
The middle graded piece is the cohomology of the normalization. The harmless orientation sign in the Picard–Lefschetz formula does not affect these conclusions.

Let \(T_0=(-1,0)\). The line \(Y+sX+s=0\) meets the cubic at \(P_1^+,P_2^+,T_0\), as follows from
\[
(-sX-s)^2-(X^3-X)=-(X+1)(X+2)(X+3).
\]
The chord law gives \(P_1^++P_2^++T_0=0\). Since \(2T_0=0\), doubling gives \(e_1+e_2=0\). Direct duplication yields
\[
e_1=\left(-\frac{25}{24},\frac{35s}{288}\right).
\]

To establish infinite order without the invalid reduction-at-three argument, use the quadratic twist
\[
E':\quad v^2=u^3-36u,
\qquad u=-6X,\quad v=6sY.
\]
This is an isomorphism over \(K\), and it sends \(e_1\) to the rational point
\[
\left(\frac{25}{4},-\frac{35}{8}\right)\in E'(\mathbb Q).
\]
The integral short Weierstrass equation has nonzero discriminant. The Nagell–Lutz theorem says that any rational torsion point on such a curve has integral coordinates. The displayed coordinates are nonintegral, so this point, and therefore \(e_1\), is non-torsion. Since \(e_2=-e_1\), both rational extension classes are nonzero and linearly dependent.

## Verification

The exact arithmetic in `artifacts/verify_maintenance.py` checks the duplication coordinate, twist point, elliptic equation and rank-two square-zero matrix. The line divisor identity and local smoothing calculation are explicit above. Finite arithmetic supports those calculations; the infinite-order conclusion uses the stated Nagell–Lutz theorem. Earlier numerical quadrature and the old reduction-at-three argument are not used as proof.

## Relationship to prior work

The generalized Jacobian of a nodal curve identifies a node extension with the difference of its two preimages in the normalization. This standard description supplies the framework, not the particular dependent non-torsion pair above. Goswami–Spelta's main theorem in arXiv:2604.01842 concerns either one irreducible node with a torsion preimage difference or a separating node between genus-one and genus-two components. Neither hypothesis describes this two-node, genus-one-normalization example. The retained contribution is the explicit boundary example of non-torsion but dependent node extensions, not new general mixed-Hodge machinery.

## Limitations

No numerical biextension-height determinant, generic independence theorem or full Ceresa-cycle limit is computed. A class relation does not imply a literal zero determinant for arbitrary period lifts differing by lattice elements. The weight dimensions are over \(\mathbb Q\); integral monodromy has the factor two explained above.

## References

- S. Goswami and I. Spelta, *Degeneration of genus three Ceresa cycles and limit of archimedean height*, arXiv:2604.01842v1, main theorem and nodal-Jacobian discussion. https://arxiv.org/html/2604.01842v1
- J. H. Silverman, *The Arithmetic of Elliptic Curves*, rational torsion and the Nagell–Lutz theorem.
- Standard Picard–Lefschetz monodromy and generalized-Jacobian descriptions for nodal curves, as used in the cited nodal-degeneration framework.
