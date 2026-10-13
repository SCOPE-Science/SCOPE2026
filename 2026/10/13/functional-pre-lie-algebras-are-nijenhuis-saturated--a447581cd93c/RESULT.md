# Functional pre-Lie algebras are Nijenhuis-saturated

## Finding

Let \(K\) be a field, let \(V\) be an \(n\)-dimensional vector space with
\[
n\ge1,
\]
and fix a nonzero functional
\[
\varphi\in V^*.
\]
Define
\[
x\cdot_\varphi y=\varphi(x)y.
\]

This multiplication is associative:
\[
(x\cdot_\varphi y)\cdot_\varphi z
=
\varphi(x)\varphi(y)z
=
x\cdot_\varphi(y\cdot_\varphi z),
\]
so it is in particular pre-Lie.

Choose a basis with
\[
\varphi(e_1)=1,
\qquad
\varphi(e_i)=0
\quad(2\le i\le n).
\]
Then
\[
L_{e_1}=I,
\qquad
L_{e_i}=0
\quad(i\ge2),
\]
which is exactly the arbitrary-dimensional family in Example 5.3(1) of Wang, Bai, Liu, and Sheng.

The stronger structural fact is:
\[
\boxed{
\text{every }N\in\operatorname{End}(V)\text{ is a Nijenhuis operator on }A_\varphi.
}
\]

For every such \(N\), the induced Nijenhuis product is
\[
\boxed{
x\cdot_N y=(\varphi\circ N)(x)y.
}
\]
Thus the entire Nijenhuis deformation theory of this family closes inside the same functional class.

If
\[
\varphi\circ N=0,
\]
the induced product is zero. If
\[
\varphi\circ N\ne0,
\]
then the induced pre-Lie algebra is isomorphic to \(A_\varphi\). Hence there are only two induced algebra isomorphism types: the zero algebra and the original nonzero functional type.

Over a finite field \(\mathbf F_q\),
\[
\boxed{
|\operatorname{Nij}(A_\varphi)|=q^{n^2}.
}
\]
The linear map
\[
\Theta:\operatorname{End}(V)\longrightarrow V^*,
\qquad
\Theta(N)=\varphi\circ N,
\]
is surjective and has kernel dimension
\[
n(n-1).
\]
Therefore every target functional has exactly
\[
q^{n(n-1)}
\]
preimages. In particular,
\[
\boxed{
\#\{N:(\cdot_\varphi)_N=0\}=q^{n(n-1)},
}
\]
and
\[
\boxed{
\#\{N:(\cdot_\varphi)_N\cong(\cdot_\varphi)\}
=
q^{n^2}-q^{n(n-1)}.
}
\]

Every matrix rank occurs. The exact number of rank-\(r\) Nijenhuis operators is
\[
\boxed{
M_{n,r}(q)
=
\frac{\displaystyle\prod_{i=0}^{r-1}(q^n-q^i)^2}
{\displaystyle\prod_{i=0}^{r-1}(q^r-q^i)}
}
\]
for
\[
0\le r\le n.
\]

The weight-zero Rota–Baxter locus singled out in the source is a strict sublocus. For this functional algebra, direct substitution gives
\[
R\text{ is weight-zero Rota–Baxter}
\iff
R^2=0.
\]
Its rank-\(r\) stratum has
\[
\boxed{
\binom{n}{r}_q
\binom{n-r}{r}_q
|\operatorname{GL}_r(\mathbf F_q)|
}
\]
points, where
\[
0\le r\le\left\lfloor\frac n2\right\rfloor.
\]
Thus the source's square-zero examples occupy a sharply smaller, rank-bounded part of the full Nijenhuis space.

For fixed \(n\), over every extension field
\[
\mathbf F_{q^m},
\]
the Nijenhuis point count is
\[
q^{mn^2}.
\]
Consequently
\[
\boxed{
Z(T)=\frac{1}{1-q^{n^2}T}.
}
\]

## Assumptions and scope

Wang, Bai, Liu, and Sheng introduced Nijenhuis operators on pre-Lie algebras. Their Example 5.3(1) treats precisely the family
\[
L_{e_1}=I,
\qquad
L_{e_i}=0
\quad(i\ge2),
\]
and states that on this family a map is a weight-zero Rota–Baxter operator exactly when its square is zero; every such operator is then Nijenhuis.

The result here retains exactly that family but solves the complete Nijenhuis problem in arbitrary dimension and over an arbitrary field.

The later complete classification of Nijenhuis operators on two-dimensional complex pre-Lie algebras and three-dimensional complex associative algebras necessarily contains the corresponding low-dimensional complex members. The accepted claim is the uniform arbitrary-dimensional structural theorem and its finite-field deformation fibers, not novelty for those low-dimensional specializations.

The finite-field Gaussian-binomial formula is ordinary linear algebra applied after the Nijenhuis-saturation theorem; it is included to quantify how small the square-zero Rota–Baxter locus is inside the full Nijenhuis space.

## Proof

The Nijenhuis identity on a pre-Lie algebra is
\[
N(x)\cdot N(y)
=
N\!\left(
N(x)\cdot y
+
x\cdot N(y)
-
N(x\cdot y)
\right).
\]

For the functional product,
\[
N(x)\cdot_\varphi N(y)
=
\varphi(Nx)N(y).
\]
Inside the right-hand side,
\[
\begin{aligned}
N(x)\cdot_\varphi y
+
x\cdot_\varphi N(y)
-
N(x\cdot_\varphi y)
&=
\varphi(Nx)y
+
\varphi(x)N(y)
-
N(\varphi(x)y)\\
&=
\varphi(Nx)y.
\end{aligned}
\]
Applying \(N\) gives
\[
\varphi(Nx)N(y),
\]
which equals the left-hand side. There is no condition on \(N\).

The induced product is the expression inside the outer \(N\):
\[
x\cdot_N y
=
N(x)\cdot_\varphi y
+
x\cdot_\varphi N(y)
-
N(x\cdot_\varphi y)
=
(\varphi\circ N)(x)y.
\]

If
\[
\psi\ne0
\]
is another functional, then \(A_\varphi\cong A_\psi\). Indeed, choose an invertible linear map \(g\) with
\[
\psi\circ g=\varphi.
\]
Then
\[
g(x\cdot_\varphi y)
=
\varphi(x)g(y)
=
\psi(gx)g(y)
=
g(x)\cdot_\psi g(y).
\]
This proves the two induced isomorphism types.

Now let
\[
K=\mathbf F_q.
\]
After choosing coordinates with
\[
\varphi=(1,0,\ldots,0),
\]
the functional
\[
\varphi\circ N
\]
is the first row of the matrix of \(N\). Hence
\[
\Theta:N\mapsto\varphi\circ N
\]
is visibly onto, and its kernel consists of matrices with zero first row. It therefore has dimension
\[
n^2-n=n(n-1).
\]
This gives all deformation-fiber counts.

The rank formula is the standard count of rank-\(r\) matrices: choose an \(r\)-dimensional image and an \(r\)-dimensional quotient map, or equivalently use the classical factorization
\[
M_{n,r}(q)
=
\frac{\prod_{i=0}^{r-1}(q^n-q^i)^2}
{\prod_{i=0}^{r-1}(q^r-q^i)}.
\]

For the weight-zero Rota–Baxter identity,
\[
R(x)\cdot R(y)
=
R\!\left(
R(x)\cdot y
+
x\cdot R(y)
\right),
\]
the same substitution yields
\[
\varphi(Rx)R(y)
=
\varphi(Rx)R(y)
+
\varphi(x)R^2(y).
\]
Since \(\varphi\ne0\),
\[
R^2=0.
\]

For a square-zero map of rank \(r\), choose
\[
U=\operatorname{im}R
\]
of dimension \(r\), then choose
\[
\ker R
\]
of dimension \(n-r\) containing \(U\), and finally choose the induced isomorphism
\[
V/\ker R\longrightarrow U.
\]
These choices give
\[
\binom{n}{r}_q
\binom{n-r}{r}_q
|\operatorname{GL}_r(\mathbf F_q)|.
\]

Finally, the Nijenhuis variety is all of
\[
\operatorname{End}(V)\cong\mathbf A^{n^2},
\]
so its extension-field count and zeta function are immediate.

## Verification

The included `artifacts/verify.py` performs finite-field replay checks for
\[
(n,q)=(1,2),(2,2),(2,3),(3,2),(3,3).
\]

For every matrix in those test spaces it checks the Nijenhuis identity directly on all ordered basis pairs and confirms that every endomorphism passes.

It groups the operators by the induced functional
\[
\varphi\circ N
\]
and confirms that every one of the \(q^n\) target functionals has exactly
\[
q^{n(n-1)}
\]
preimages.

It checks the full matrix-rank distribution against the displayed closed formula.

It also tests the weight-zero Rota–Baxter identity directly and verifies that it is equivalent to
\[
R^2=0,
\]
with each square-zero rank stratum matching
\[
\binom{n}{r}_q
\binom{n-r}{r}_q
|\operatorname{GL}_r(\mathbf F_q)|.
\]

The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence only. The arbitrary-field theorem is the cancellation proof above.

## Relationship to prior work

Wang, Bai, Liu, and Sheng define pre-Lie Nijenhuis operators and, in Example 5.3, revisit an arbitrary-dimensional family with
\[
L_{e_1}=I,\qquad L_{e_i}=0\ (i\ge2).
\]
For this family they state the weight-zero Rota–Baxter criterion
\[
R^2=0
\]
and note that those Rota–Baxter operators are Nijenhuis. Their statement gives a sufficient square-zero subclass, not the complete Nijenhuis locus.

Li, Hou, and Bai had previously studied weight-zero Rota–Baxter operators on pre-Lie algebras and supplied higher-dimensional examples. That work predates the pre-Lie Nijenhuis definition and does not state Nijenhuis saturation.

Zou, Gao, Kang, and Lü later classify every Nijenhuis operator on all two-dimensional complex pre-Lie algebras and all three-dimensional complex associative algebras. Their result covers the corresponding low-dimensional complex specializations of this functional family, but it does not state the uniform arbitrary-dimensional identity
\[
\operatorname{Nij}(A_\varphi)=\operatorname{End}(V)
\]
or the general deformation-fiber formula
\[
N\mapsto\varphi\circ N.
\]

Targeted semantic searches for all-endomorphism Nijenhuis saturation, the functional form
\[
x\cdot y=\varphi(x)y,
\]
the source's Example 5.3, and the deformation map
\[
\varphi\circ N
\]
did not locate the arbitrary-dimensional theorem.

## Limitations

The theorem treats the one-sided functional associative family
\[
x\cdot y=\varphi(x)y
\]
with \(\varphi\ne0\).

It does not classify automorphism-conjugacy orbits of all endomorphisms.

Low-dimensional complex members are covered by later complete classification work; the new scope is the uniform arbitrary-dimensional theorem and its arithmetic consequences.

The square-zero Rota–Baxter rank formula is standard finite linear algebra and is not itself claimed as the main novelty.

Failed searches do not prove absolute novelty.

## References

1. Q. Wang, C. Bai, J. Liu, and Y. Sheng, “Nijenhuis operators on pre-Lie algebras,” arXiv:1710.03749v1, first public 9 October 2017; *Communications in Contemporary Mathematics* 21 (2019), 1850050, DOI `10.1142/S0219199718500505`.
2. X. Li, D. Hou, and C. Bai, “Rota-Baxter operators on pre-Lie algebras,” *Journal of Nonlinear Mathematical Physics* 14 (2007), 269–289, DOI `10.2991/jnmp.2007.14.2.9`.
3. X. Zou, X. Gao, C. Kang, and J. Lü, “Nijenhuis Operators on 2D Pre-Lie Algebras and 3D Associative Algebras,” *Axioms* 15 (2026), 80, DOI `10.3390/axioms15010080`.
