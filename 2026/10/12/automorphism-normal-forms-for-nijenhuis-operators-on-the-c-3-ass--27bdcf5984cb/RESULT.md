# Automorphism normal forms for Nijenhuis operators on the \(C_3\) associative algebra

## Finding

Let \(C_3\) be the three-dimensional complex commutative associative algebra with basis
\[
\{e_1,e_2,e_3\}
\]
and nonzero products
\[
e_2^2=e_1,\qquad e_3^2=e_1.
\]

Introduce the isotropic basis
\[
z=2e_1,\qquad u=e_2+i e_3,\qquad v=e_2-i e_3.
\]
Then
\[
uv=vu=z
\]
and every other basis product is zero.

A linear map \(N:C_3\to C_3\) is Nijenhuis when
\[
N(x)N(y)
=
N\!\left(N(x)y+xN(y)-N(xy)\right)
\]
for all \(x,y\in C_3\).

Using matrices whose columns are the coordinates of images in the ordered basis
\[
(z,u,v),
\]
every Nijenhuis operator is conjugate by an algebra automorphism to exactly one matrix in the following seven families:
\[
\boxed{
Z_a^0=aI_3,\qquad
Z_a^1=aI_3+E_{12},\qquad
Z_a^2=aI_3+E_{12}+E_{13},
}
\]
\[
\boxed{
P_{a,t}^0=aI_3+tE_{22},\qquad
P_{a,t}^1=aI_3+tE_{22}+E_{13},
\qquad
a\in\mathbb C,\quad t\in\mathbb C^\times,
}
\]
and
\[
\boxed{
R_{a,t}^0=aI_3+tE_{22}+E_{23},\qquad
R_{a,t}^1=aI_3+E_{12}+tE_{22}+E_{23},
\qquad
a,t\in\mathbb C.
}
\]

Here \(E_{ij}\) denotes the matrix unit with its \(1\) in row \(i\), column \(j\).

The quotient has a simple intrinsic description. If
\[
V=\operatorname{span}\{u,v\},
\qquad
J=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\]
then every Nijenhuis operator has a unique block form
\[
N
=
aI_3+
\begin{pmatrix}
0&\ell\\
0&K
\end{pmatrix}
\]
with
\[
\boxed{K^TJK=0.}
\]
For nonzero \(K\), this says that \(\operatorname{im}K\) is an isotropic line. After an automorphism sends that line to \(\mathbb Cu\),
\[
K=
\begin{pmatrix}
t&s\\
0&0
\end{pmatrix}.
\]
If \(s=0\), then \(t\ne0\) and the \(P\)-families occur. If \(s\ne0\), scaling normalizes \(s=1\) and the \(R\)-families occur. The remaining covector \(\ell\), modulo the row space of \(K\), is either zero or nonzero; this binary invariant gives the superscripts \(0\) and \(1\).

When \(K=0\), the automorphism group has exactly three orbits on \(\ell\): zero, nonzero isotropic support, and nonisotropic support. These give \(Z_a^0,Z_a^1,Z_a^2\).

Thus the five coordinate families in the published raw \(C_3\) list collapse to a complete, nonredundant automorphism quotient organized by rank, isotropic geometry, trace, and one residual covector flag.

## Assumptions and scope

The field is \(\mathbb C\), matching the primary classification source. The use of
\[
i^2=-1
\]
is essential to the displayed isotropic basis.

The equivalence relation is conjugacy by automorphisms of the fixed associative algebra:
\[
N\sim \phi N\phi^{-1},
\qquad
\phi\in\operatorname{Aut}(C_3).
\]

The result treats only the algebra \(C_3\) from the published three-dimensional commutative associative list. It does not claim orbit classifications for the other algebras in that paper.

## Proof

In the basis \((z,u,v)\), multiplication is encoded on
\[
V=\operatorname{span}\{u,v\}
\]
by the symmetric form
\[
B(x,y)=x^TJy,
\qquad
J=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\]
through
\[
xy=B(x,y)z.
\]

Start with a completely general \(3\times3\) matrix for \(N\). Applying the Nijenhuis identity to basis pairs first forces
\[
N(z)=az.
\]
Writing
\[
N=
\begin{pmatrix}
a&\alpha&\beta\\
0&b&c\\
0&d&e
\end{pmatrix},
\]
the remaining equations are
\[
c(a-e)=0,\qquad
d(a-b)=0,
\]
and
\[
(a-b)(a-e)+cd=0.
\]

Set
\[
K=
\begin{pmatrix}
b-a&c\\
d&e-a
\end{pmatrix},
\qquad
\ell=(\alpha,\beta).
\]
The three scalar equations are exactly the entries of
\[
K^TJK=0.
\]
Consequently
\[
N
=
aI_3+
\begin{pmatrix}
0&\ell\\
0&K
\end{pmatrix},
\qquad
K^TJK=0.
\]

If \(K\ne0\), then \(K\) has rank one and every vector in its image is isotropic for \(B\). Over \(\mathbb C\), the two isotropic lines are
\[
\mathbb Cu,\qquad \mathbb Cv.
\]

The automorphism group can also be read directly from the multiplication. Since
\[
\operatorname{Ann}(C_3)=\mathbb Cz,
\]
an automorphism sends
\[
z\longmapsto \lambda z.
\]
Its induced map \(F\) on \(V\) satisfies
\[
F^TJF=\lambda J.
\]
Hence, up to the component interchanging \(u\) and \(v\), every automorphism has matrix
\[
\Phi_{p,q,\rho,\sigma}
=
\begin{pmatrix}
pq&\rho&\sigma\\
0&p&0\\
0&0&q
\end{pmatrix},
\qquad
p,q\in\mathbb C^\times.
\]

For
\[
Q=N-aI_3=
\begin{pmatrix}
0&\ell\\
0&K
\end{pmatrix},
\]
conjugation gives
\[
K\longmapsto F K F^{-1},
\]
and
\[
\ell\longmapsto
(\lambda\ell+rK)F^{-1},
\qquad
r=(\rho,\sigma).
\]

Assume \(K\ne0\). Interchanging \(u\) and \(v\) if necessary puts
\[
\operatorname{im}K=\mathbb Cu,
\]
so
\[
K=
\begin{pmatrix}
t&s\\
0&0
\end{pmatrix}.
\]
For diagonal
\[
F=\operatorname{diag}(p,q),
\]
one gets
\[
K\longmapsto
\begin{pmatrix}
t&(p/q)s\\
0&0
\end{pmatrix}.
\]
Thus \(t=\operatorname{tr}K\) is invariant.

If \(s=0\), then \(t\ne0\), giving
\[
K=tE_{11}.
\]
The translation \(rK\) removes the first component of \(\ell\); the second component is either zero or can be scaled to \(1\). This gives
\[
P_{a,t}^0,\qquad P_{a,t}^1.
\]

If \(s\ne0\), choose \(p/q=s^{-1}\) and normalize
\[
K=
\begin{pmatrix}
t&1\\
0&0
\end{pmatrix}.
\]
Again \(rK\) changes \(\ell\) by the row space of \(K\). The quotient
\[
V^*/\operatorname{row}(K)
\]
is one-dimensional, so it has two orbits: zero and nonzero. The nonzero class can be normalized to the class of \((1,0)\). This gives
\[
R_{a,t}^0,\qquad R_{a,t}^1.
\]

These two kinds cannot merge. In the \(P\)-case the kernel of \(K\) is an isotropic line. In the \(R\)-case with \(t\ne0\), the kernel is nonisotropic; for \(t=0\), \(K\) is nonzero nilpotent and has trace zero, while the \(P\)-case requires \(t\ne0\).

Finally let \(K=0\). Then translations do not affect \(\ell\), while diagonal automorphisms act by
\[
(\alpha,\beta)\longmapsto(q\alpha,p\beta)
\]
and the second automorphism component interchanges the two coordinates. Therefore there are exactly three orbits:
\[
(0,0),\qquad(1,0),\qquad(1,1),
\]
giving
\[
Z_a^0,\qquad Z_a^1,\qquad Z_a^2.
\]

The scalar \(a\), the trace \(t\), the kernel-isotropy type, and the zero/nonzero class of \(\ell\) in the indicated quotient prove uniqueness of the representatives.

## Verification

The included script `artifacts/verify.py` reconstructs the Nijenhuis equations from the multiplication
\[
uv=vu=z
\]
using a completely general \(3\times3\) matrix.

It verifies that the first column must be
\[
(a,0,0)^T
\]
and that the remaining equations are exactly equivalent to
\[
K^TJK=0.
\]

It independently checks the full connected-component automorphism matrix, the component interchanging \(u\) and \(v\), and the block conjugation formula for \(K\) and \(\ell\).

Finally, it substitutes every displayed normal-form family into all nine ordered basis-pair Nijenhuis equations and confirms that every defect vanishes identically. It also symbolically verifies the transformations used to normalize \(s\) and the residual covector class.

The script returns `VERIFY_OK`.

No finite sample is used in place of the complex-field proof.

## Relationship to prior work

Gao, Kang, Lü, and Yu first made public the low-dimensional Nijenhuis classification in August 2023. The later expanded version by Zou, Gao, Kang, and Lü gives the \(C_3\) multiplication
\[
e_2^2=e_1,\qquad e_3^2=e_1
\]
and lists five parametric families containing every Nijenhuis operator on \(C_3\).

The expanded paper explicitly states that its families are parametrically complete but that it does not perform a full orbit analysis under \(\operatorname{Aut}(A)\), leaving conjugacy classification as a future direction. Its Remark 4.4 illustrates an orbit reduction only for the two-dimensional algebra \(A_5\), not for \(C_3\).

The published 2026 journal version retains the same scope and the same statement that a full automorphism-orbit analysis is not performed.

Targeted searches for \(C_3\), its multiplication table, Nijenhuis conjugacy, automorphism normal forms, and equivalent isotropic-basis descriptions did not locate a source giving the seven-family quotient above.

## Limitations

The theorem is specific to the complex algebra \(C_3\).

Over non-algebraically closed fields, the isotropic-line geometry of the form \(J\) can change and the orbit list need not remain the same.

The result does not re-audit the correctness of the other operator tables in the source.

An unindexed or differently phrased conjugacy calculation could exist. Failed searches do not prove novelty.

## References

1. X. Gao, C. Kang, J. Lü, and S. Yu, “Nijenhuis operators on low dimensional pre-Lie algebras and solutions of CYBE,” arXiv:2308.12121v1, first public 23 August 2023.
2. X. Zou, X. Gao, C. Kang, and J. Lü, “Nijenhuis Operators on 2D Pre-Lie Algebras and 3D Associative Algebras,” arXiv:2308.12121v3.
3. X. Zou, X. Gao, C. Kang, and J. Lü, “Nijenhuis Operators on 2D Pre-Lie Algebras and 3D Associative Algebras,” *Axioms* 15 (2026), 80, DOI `10.3390/axioms15010080`.
