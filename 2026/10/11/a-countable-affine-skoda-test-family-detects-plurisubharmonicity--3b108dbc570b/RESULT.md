# A countable affine Skoda test family detects plurisubharmonicity

## Finding

Let
\[
D\subset\mathbb C^n
\]
be a bounded domain, let
\[
\varphi\in C^2(D)
\]
be real-valued, and fix a nonzero
\[
f\in A^2(D,\varphi).
\]
Write
\[
K=\mathbb Q(i).
\]

For
\[
q\in D\cap K^n,
\qquad
A\in\operatorname{GL}(n,K),
\qquad
M,\ell\in\mathbb N,
\]
consider the \((n+1)\)-tuple
\[
g_{q,A,M}(z)
=
\bigl(A(z-q),M\bigr).
\]
For these tuples,
\[
p=n,
\]
and define
\[
\psi_{g,\ell}
=
n(1+\ell)\log|g|^2
\]
and
\[
J_{\varphi,g,\ell}(f)
=
\int_D
\frac{|f|^2}{|g|^2}
e^{-\varphi-\psi_{g,\ell}}\,dV.
\]

Assume that, for every such
\[
(q,A,M,\ell),
\]
there exists
\[
h\in\mathcal O(D)^{\oplus(n+1)}
\]
with
\[
g_{q,A,M}\cdot h=f
\]
and
\[
\int_D
|h|^2e^{-\varphi-\psi_{g,\ell}}\,dV
\le
\left(1+\frac1\ell\right)
J_{\varphi,g,\ell}(f).
\]
Then
\[
\varphi
\]
is plurisubharmonic on
\[
D.
\]

If
\[
D
\]
is pseudoconvex, the converse also holds. Thus, for a fixed nonzero weighted Bergman function, plurisubharmonicity is characterized by one explicit **countable** family of affine-radial Skoda tests. It is unnecessary to test all holomorphic tuples or a continuum of centers, matrices, radial parameters, and Skoda exponents.

## Assumptions and scope

The weighted Bergman space is
\[
A^2(D,\varphi)
=
\left\{
f\in\mathcal O(D):
\int_D|f|^2e^{-\varphi}\,dV<\infty
\right\}.
\]

The Gaussian-rational field is
\[
K=\mathbb Q(i),
\]
so the permitted centers and matrices form countable dense subsets of
\[
\mathbb C^n
\]
and
\[
\operatorname{GL}(n,\mathbb C),
\]
respectively.

Only \((n+1)\)-generator tuples are used. The recent source explains why the same concentration proof does not simply descend to fewer generators: fewer coordinate components localize the Skoda weight along a positive-dimensional slice rather than at a point.

The converse implication from plurisubharmonicity to the test estimates requires pseudoconvexity, exactly as in the classical Skoda theorem. The forward implication proved here does not.

## Proof

Assume, toward a contradiction, that
\[
\varphi
\]
is not plurisubharmonic. Then there are
\[
z_*\in D
\]
and
\[
v\in\mathbb C^n\setminus\{0\}
\]
such that
\[
\left\langle
H_\varphi(z_*)v,v
\right\rangle
<0,
\]
where
\[
H_\varphi(z)
=
\left[
\frac{\partial^2\varphi}
{\partial z_j\partial\bar z_k}(z)
\right]_{j,k}.
\]

Choose
\[
\delta>0
\]
small enough that
\[
P_\delta
=
vv^*+\delta I
\]
satisfies
\[
\operatorname{tr}
\left(
H_\varphi(z_*)P_\delta
\right)
<0.
\]
The source's affine argument shows that every positive definite Hermitian matrix is of the form
\[
P
=
\overline{A^{-1}}
(A^{-1})^{\mathsf T}
\]
for some
\[
A\in\operatorname{GL}(n,\mathbb C).
\]

Now consider
\[
\mathcal T(z,A)
=
\operatorname{tr}
\left(
H_\varphi(z)
\overline{A^{-1}}
(A^{-1})^{\mathsf T}
\right).
\]
This is continuous in
\[
(z,A).
\]
Hence strict negativity persists in a product neighborhood of some
\[
(z_*,A_*).
\]

Because
\[
f
\]
is a nonzero holomorphic function on the domain, its zero set has empty interior. The negative neighborhood therefore contains a point at which
\[
f\ne0.
\]
Gaussian-rational points are dense, so one can choose
\[
q\in D\cap K^n
\]
inside that neighborhood with
\[
f(q)\ne0.
\]
Likewise,
\[
\operatorname{GL}(n,K)
\]
is dense in
\[
\operatorname{GL}(n,\mathbb C),
\]
so after an arbitrarily small matrix perturbation one can choose
\[
A\in\operatorname{GL}(n,K)
\]
such that
\[
\mathcal T(q,A)<0.
\]

Set
\[
w=A(z-q),
\qquad
\widetilde D=A(D-q),
\]
and
\[
\widetilde\varphi
=
\varphi\circ T^{-1},
\qquad
\widetilde f
=
f\circ T^{-1}.
\]
By the chain rule,
\[
\operatorname{tr}
i\partial\bar\partial
\widetilde\varphi(0)
=
\mathcal T(q,A)
<0.
\]

For each integer
\[
M\ge1
\]
and
\[
\ell\ge1,
\]
the original tuple
\[
g_{q,A,M}(z)
=
\bigl(A(z-q),M\bigr)
\]
becomes, in the \(w\)-coordinate,
\[
(w_1,\ldots,w_n,M).
\]
The Jacobian factor from the affine coordinate change appears on both sides of the Skoda estimate and cancels. Hence the assumed estimate transfers exactly to
\[
\widetilde f
\]
for this special tuple and every positive integer
\[
\ell.
\]

The key source proof for the special tuple fixes
\[
M>0
\]
and lets the Skoda exponent
\[
\varepsilon\to\infty.
\]
It proves
\[
\operatorname{tr}
i\partial\bar\partial
\widetilde\varphi(0)
\ge
-\frac{n^2}{M^2}.
\]
Its concentration and curvature limits are ordinary limits as
\[
\varepsilon\to\infty,
\]
so the same argument applies unchanged along the integer subsequence
\[
\varepsilon=\ell\to\infty.
\]
Therefore our restricted hypothesis yields, for every integer
\[
M\ge1,
\]
\[
\operatorname{tr}
i\partial\bar\partial
\widetilde\varphi(0)
\ge
-\frac{n^2}{M^2}.
\]
Letting integer
\[
M\to\infty
\]
gives
\[
\operatorname{tr}
i\partial\bar\partial
\widetilde\varphi(0)
\ge0,
\]
contradicting
\[
\mathcal T(q,A)<0.
\]
Thus
\[
\varphi
\]
is plurisubharmonic.

Conversely, assume
\[
D
\]
is pseudoconvex and
\[
\varphi
\]
is plurisubharmonic. The classical Skoda theorem supplies the division estimate for every zero-free holomorphic tuple and every positive real exponent for which the source integral is finite. It therefore supplies all members of the displayed countable test family.

## Verification

The recent primary preprint was inspected in full at its definition of Skoda divisibility, the classical forward theorem, affine invariance, the special \((n+1)\)-generator tuple, the concentration lemma, Proposition 3.8, the proof of Theorem 1.3, and the final equivalence theorem.

For
\[
g=(z_1,\ldots,z_n,M),
\]
the source proves concentration at the origin as
\[
\varepsilon\to\infty
\]
and obtains
\[
\operatorname{tr}
i\partial\bar\partial\varphi(0)
\ge
-\frac{n^2}{M^2}.
\]
Only the behavior along an unbounded sequence of exponents is needed for this limiting conclusion, so restricting
\[
\varepsilon
\]
to positive integers preserves the proof.

Likewise, the last step requires only an unbounded sequence of
\[
M
\]
values. Positive integers therefore suffice.

The Gaussian-rational discretization is justified by strictness and continuity. A negative Levi direction gives a strictly negative trace against some positive definite Hermitian matrix. Both the point and the matrix may then be approximated inside a strict negative neighborhood, while the nonzero set of
\[
f
\]
is dense.

No finite experiment or numerical approximation is used to infer positivity. Density is used only to select a member of the fixed countable test family inside an open strict-negativity set.

## Relationship to prior work

Li, Meng, Ning, and Zhou's 2026 sequel proves that the original Skoda division estimate for one nonzero weighted Bergman function characterizes plurisubharmonicity. Its formal definition asks for all generator counts, all zero-free holomorphic tuples, and every positive real Skoda exponent.

Their proof already reveals that \((n+1)\)-generator affine-radial tuples are the localizing mechanism. It uses arbitrary affine coordinate changes, arbitrary centers, arbitrary positive \(M\), and the limit \(\varepsilon\to\infty\), but it does not state a fixed countable test family.

The authors' 2024 precursor concerns a formally stronger division estimate and therefore does not imply the countable characterization for the original Skoda estimate.

Targeted searches for countable Skoda test families, Gaussian-rational centers, rational affine matrices, and restricted integer parameter tests did not locate an implication-equivalent published statement.

The present result isolates a separable test set: a single countable collection of rigid affine-radial division problems determines a differential positivity property on the whole domain.

## Limitations

The weight is assumed
\[
C^2,
\]
as in the principal converse theorem whose local Hessian proof is discretized here. The source develops additional continuity-level consequences using extension theory, but the present countable characterization does not claim that lower regularity.

The result does not reduce the generator count below
\[
n+1.
\]
Indeed, the source identifies a genuine localization obstruction in its proof when fewer generators are used.

The countable test family is not claimed to be minimal. Other countable dense choices of centers, affine matrices, and unbounded positive parameter sequences would work by the same argument.

## References

1. Z. Li, X. Meng, J. Ning, and X. Zhou, *A Converse to the Skoda \(L^2\) division theorem II*, arXiv:2609.33300v1, 2026.
2. Z. Li, X. Meng, J. Ning, and X. Zhou, *A Converse to the Skoda \(L^2\) Division Theorem*, arXiv:2405.18713, first posted 2024.
3. H. Skoda, *Application des techniques \(L^2\) à la théorie des idéaux d'une algèbre de fonctions holomorphes avec poids*, Annales Scientifiques de l'École Normale Supérieure 5 (1972), 545–579.
4. H. Skoda, *Morphismes surjectifs de fibrés vectoriels semi-positifs*, Annales Scientifiques de l'École Normale Supérieure 11 (1978), 577–611.
