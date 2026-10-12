# The Klein quartic two-torsion is the hyperbolic \(V\oplus V^\vee\) module
## Finding
Let \(C:x^3y+y^3z+z^3x=0\) be Klein’s quartic over \(\mathbb C\), let \(H=\operatorname{Aut}(C)\cong\operatorname{PSL}(2,7)\cong\operatorname{GL}(3,2)\), and put \(J=\operatorname{Jac}(C)\). From the period lattice of Markushevich–Moreau,
\[
\Lambda=\mathcal Oe_1\oplus\mathcal Oe_2\oplus\mathcal Oe_3,
\qquad \mathcal O=\mathbb Z[\alpha],\qquad \alpha^2-\alpha+2=0,
\]
one obtains, after reduction modulo \(2\), an \(H\)-stable decomposition
\[
J[2]=\Lambda/2\Lambda\cong V\oplus V^\vee,
\qquad V\cong\mathbb F_2^3,
\]
natural up to swapping the two summands. Under this identification the Weil pairing is the hyperbolic evaluation pairing and the unique \(H\)-invariant quadratic refinement is
\[
q(v,\varphi)=\varphi(v).
\]
Hence the four nonzero \(H\)-orbits are characterized intrinsically as
\[
\begin{aligned}
A&=(V\setminus\{0\})\times\{0\}, &|A|&=7,\\
B&=\{0\}\times(V^\vee\setminus\{0\}), &|B|&=7,\\
C_0&=\{(v,\varphi):v,\varphi\ne0,\ \varphi(v)=0\}, &|C_0|&=21,\\
C_1&=\{(v,\varphi):v,\varphi\ne0,\ \varphi(v)=1\}, &|C_1|&=28.
\end{aligned}
\]
The already-known orbit sizes \(7,7,21,28\) therefore arise from the two coordinate summands and the zero/nonzero evaluation dichotomy, rather than as an unexplained finite orbit census. The quadratic form has \(36\) zeros and \(28\) ones, so it is even; relative to the known unique invariant even theta characteristic, it is the associated parity form.

There is also a complete orbit-addition law. Write \(0\) for the zero orbit and, for \(X,Y,Z\in\{0,A,B,C_0,C_1\}\), let \(n_{XY}^Z\) be the number of \(y\in Y\) such that \(x+y\in Z\), for a fixed \(x\in X\). Transitivity makes the number independent of the choice of \(x\). The nontrivial rows are:

| \(X\) | \(Y\) | nonzero \(n_{XY}^Z\) |
|---|---|---|
| \(A\) | \(A\) | \(n^0=1,\ n^A=6\) |
| \(A\) | \(B\) | \(n^{C_0}=3,\ n^{C_1}=4\) |
| \(A\) | \(C_0\) | \(n^B=3,\ n^{C_0}=6,\ n^{C_1}=12\) |
| \(A\) | \(C_1\) | \(n^B=4,\ n^{C_0}=12,\ n^{C_1}=12\) |
| \(B\) | \(A\) | \(n^{C_0}=3,\ n^{C_1}=4\) |
| \(B\) | \(B\) | \(n^0=1,\ n^B=6\) |
| \(B\) | \(C_0\) | \(n^A=3,\ n^{C_0}=6,\ n^{C_1}=12\) |
| \(B\) | \(C_1\) | \(n^A=4,\ n^{C_0}=12,\ n^{C_1}=12\) |
| \(C_0\) | \(A\) | \(n^B=1,\ n^{C_0}=2,\ n^{C_1}=4\) |
| \(C_0\) | \(B\) | \(n^A=1,\ n^{C_0}=2,\ n^{C_1}=4\) |
| \(C_0\) | \(C_0\) | \(n^0=1,\ n^A=2,\ n^B=2,\ n^{C_0}=8,\ n^{C_1}=8\) |
| \(C_0\) | \(C_1\) | \(n^A=4,\ n^B=4,\ n^{C_0}=8,\ n^{C_1}=12\) |
| \(C_1\) | \(A\) | \(n^B=1,\ n^{C_0}=3,\ n^{C_1}=3\) |
| \(C_1\) | \(B\) | \(n^A=1,\ n^{C_0}=3,\ n^{C_1}=3\) |
| \(C_1\) | \(C_0\) | \(n^A=3,\ n^B=3,\ n^{C_0}=6,\ n^{C_1}=9\) |
| \(C_1\) | \(C_1\) | \(n^0=1,\ n^A=3,\ n^B=3,\ n^{C_0}=9,\ n^{C_1}=12\) |

## Assumptions and scope
The statement concerns the complex Klein quartic and the natural action of its full curve automorphism group \(H\) on the two-torsion of its principally polarized Jacobian. The two three-dimensional summands are individually determined by the two idempotent factors of \(\mathcal O/2\mathcal O\); complex conjugation swaps those factors, so the decomposition is asserted only up to that swap. The result does not claim that the orbit sizes \(7,7,21,28\), the existence of the unique invariant even theta characteristic, or the corresponding \(1+7+7+21\) decomposition of even theta characteristics are new.

## Proof
Because \(\alpha^2-\alpha+2=0\), reduction modulo \(2\) gives
\[
\mathcal O/2\mathcal O\cong\mathbb F_2[\alpha]/(\alpha(\alpha-1))\cong\mathbb F_2\times\mathbb F_2.
\]
Since the source proves that \(\Lambda\) is a free rank-three \(\mathcal O\)-module, this immediately yields two \(H\)-stable three-dimensional summands in \(\Lambda/2\Lambda\).

Using the source roots
\[
e_1=(0,\alpha,\alpha),\qquad e_2=(0,0,2),\qquad e_3=(1,1,\bar\alpha)
\]
and the anti-reflections \(\rho_i=-r_{e_i}\), direct substitution into the Hermitian reflection formula gives the following matrices in the \(\mathcal O\)-basis \((e_1,e_2,e_3)\):
\[
M_1=\begin{pmatrix}1&1-\alpha&-\alpha\\0&-1&0\\0&0&-1\end{pmatrix},\quad
M_2=\begin{pmatrix}-1&0&0\\\alpha&1&1-\alpha\\0&0&-1\end{pmatrix},\quad
M_3=\begin{pmatrix}-1&0&0\\0&-1&0\\\alpha-1&\alpha&1\end{pmatrix}.
\]
Evaluation at \(\alpha=0\) and \(\alpha=1\) modulo \(2\) gives two three-dimensional representations. Their paired closure has order \(168\). Solving the intertwining equations
\[
A_{0,i}^{\mathsf T}PA_{1,i}=P
\]
for all three generators gives a one-dimensional solution space, whose unique nonzero matrix is
\[
P=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}.
\]
It is invertible. Thus the second summand is the dual of the first.

On \(V\oplus V^\vee\), the alternating form
\[
\langle(v,\varphi),(w,\psi)\rangle=\psi(v)+\varphi(w)
\]
is \(H\)-invariant and nondegenerate. Exact linear algebra over \(\mathbb F_2\) shows that the space of invariant alternating forms is one-dimensional. The Weil pairing is itself nonzero, nondegenerate, and \(H\)-invariant because automorphisms of \(C\) preserve the canonical principal polarization, so it is this form.

The function \(q(v,\varphi)=\varphi(v)\) has this alternating form as its polarization. It is \(H\)-invariant. Exact computation shows that there is no nonzero invariant linear functional on \(V\oplus V^\vee\); since two quadratic refinements of the same alternating form differ by a linear functional, \(q\) is the unique invariant refinement. Counting gives \(36\) zeros and \(28\) ones. The four orbit descriptions and sizes follow immediately: each nonzero vector in \(V\) has exactly three nonzero annihilating covectors and four nonzero covectors evaluating to one. Exhaustive group action confirms that each of these four sets is a single orbit. The same finite enumeration gives the displayed addition table.

## Verification
Run `python3 verify.py`. The verifier uses exact arithmetic in \(\mathbb F_2\). It checks that the paired generator group has order \(168\), that the perfect intertwining pairing is unique, that the invariant alternating-form space is one-dimensional, that \(q\) has \(36\) zeros and \(28\) ones, that the orbit decomposition is \(1+7+7+21+28\), and that every entry of the orbit-addition table is correct. Its success line is:

`VERIFY_OK group=168 module=V+Vdual pairing_space_dim=1 invariant_alt_dim=1 q_zero=36 q_one=28 orbits=1+7+7+21+28 fusion=verified`

## Relationship to prior work
Markushevich–Moreau give the period lattice, the explicit action of the Klein group, and the fixed-point/orbit data on the Jacobian. Classical accounts already record that the \(63\) nonzero two-torsion classes, equivalently Steiner complexes, split into orbits of sizes \(28,21,7,7\). They also record the unique invariant even theta characteristic and the corresponding decomposition of the \(36\) even theta characteristics as \(1+7+7+21\). Those statements are used as external checks and are not part of the originality claim here.

The refinement proved here is the explicit characteristic-two module structure \(J[2]\cong V\oplus V^\vee\), the identification of the Weil and parity forms with evaluation, the intrinsic support/evaluation description of the four orbits, and the complete orbit-addition fusion law. Focused searches for this module formulation, for an equivalent dual-module description, and for an addition/fusion table did not find an implication-equivalent statement.

## Limitations
The decomposition is natural only up to interchanging the two factors of \(\mathcal O/2\mathcal O\). No claim is made about torsion of odd order, the full endomorphism algebra of \(J\), or orbit fusion outside \(J[2]\). Literature searches cannot prove absence from all unpublished or unindexed sources; older representation-theoretic treatments of the Klein group are the main residual originality risk.

## References
1. Dimitri Markushevich and Anne Moreau, *Action of the automorphism group on the Jacobian of Klein’s quartic curve*, arXiv:2107.03745, first posted 2021-07-08.
2. Igor Dolgachev, *Classical Algebraic Geometry: A Modern View*, discussion of the Klein quartic, theta characteristics, and Steiner complexes.
3. H. Abban, I. Cheltsov, J. Park, and C. Shramov, *Double Veronese cones with 28 nodes*, Example 7.21, for the invariant even theta characteristic and the \(1+7+7+21\) even-theta orbit decomposition.
