# Quadratic log-distortion stability of the harmonic quasiregular Bloch coefficient

## Finding

For locally univalent harmonic \(K\)-quasiregular Bloch-type mappings, Theorem 1.5 of the recent source gives a pseudo-hyperbolic Lipschitz estimate with an explicit coefficient \(C(K)\). The source proves only that
\[
C(K)\longrightarrow C_0
\qquad(K\to1^+),
\]
where
\[
C_0=(4+2\sqrt5)e^{-(1+\sqrt5)/2}
\]
is the sharp locally univalent harmonic Bloch constant.

The coefficient has a stronger exact structure. Put
\[
q=\log K,
\qquad
c=\cosh(q/2).
\]
Then
\[
C(K)
=
C_0c
+
(c-1)
\left[
\frac{3\sqrt3}{2}
+
\coth\!\left(\frac{2c}{1+c}\right)
\right].
\]

It follows that \(C(K)\) is strictly increasing for
\[
K\ge1,
\]
with unique minimum
\[
C(1)=C_0.
\]
More importantly, the loss from the analytic endpoint is quadratic in the natural logarithmic distortion:
\[
C(K)
=
C_0
+
\alpha(\log K)^2
+
O\!\left((\log K)^4\right),
\]
where
\[
\alpha
=
\frac18
\left(
C_0+\frac{3\sqrt3}{2}+\coth1
\right)
=
0.6988794607708748\ldots.
\]
Equivalently,
\[
C(K)-C_0
=
\alpha(K-1)^2+O((K-1)^3).
\]

Thus the specialized \(K\)-quasiregular estimate has no first-order small-distortion penalty.

## Assumptions and scope

The coefficient is exactly the \(C(K)\) appearing in Theorem 1.5 of arXiv:2609.33140v1:
\[
C(K)
=
C_0\frac{K+1}{2\sqrt K}
+
\frac{kL(K)}2
\left(
\frac{3\sqrt3}{2}+\coth L(K)
\right)
\frac{K-1}{2\sqrt K},
\]
with
\[
k=\frac{K-1}{K+1},
\qquad
L(K)=\frac{2}{1+\sqrt{1-k^2}}.
\]

The theorem applies for
\[
K\ge1
\]
to locally univalent harmonic \(K\)-quasiregular mappings in the harmonic Bloch-type class used by the source.

The result concerns the explicit coefficient proved in that theorem. It does not claim that this coefficient is the optimal constant for every fixed \(K>1\).

## Proof

Set
\[
q=\log K,
\qquad
c=\cosh(q/2),
\qquad
s=\sinh(q/2).
\]
Then
\[
\frac{K+1}{2\sqrt K}=c,
\qquad
\frac{K-1}{2\sqrt K}=s,
\qquad
k=\tanh(q/2)=\frac{s}{c}.
\]
Moreover,
\[
\sqrt{1-k^2}
=
\operatorname{sech}(q/2)
=
\frac1c,
\]
so
\[
L(K)
=
\frac{2}{1+1/c}
=
\frac{2c}{1+c}.
\]

The product multiplying the second bracket simplifies exactly:
\[
\frac{kL(K)}2
\frac{K-1}{2\sqrt K}
=
\frac{s}{c}
\frac{c}{1+c}
s
=
\frac{s^2}{1+c}
=
c-1.
\]
Therefore
\[
C(K)
=
C_0c
+
(c-1)
\left[
\frac{3\sqrt3}{2}
+
\coth\!\left(\frac{2c}{1+c}\right)
\right].
\]

Write
\[
A=\frac{3\sqrt3}{2},
\qquad
\ell(c)=\frac{2c}{1+c},
\]
and
\[
\mathcal C(c)=C_0c+(c-1)(A+\coth\ell(c)).
\]
Differentiation gives
\[
\mathcal C'(c)
=
C_0+A+\coth\ell(c)
-
\frac{2(c-1)}{(c+1)^2}\csch^2\ell(c).
\]

For
\[
c\ge1,
\]
one has
\[
0\le
\frac{2(c-1)}{(c+1)^2}
\le
\frac14.
\]
Also
\[
\ell(c)\ge1,
\]
hence
\[
\csch^2\ell(c)<1
\]
and
\[
\coth\ell(c)>1.
\]
Since \(C_0>0\) and \(A>0\),
\[
\mathcal C'(c)
>
1-\frac14
=
\frac34.
\]
Thus \(\mathcal C\) is strictly increasing for \(c\ge1\). Since
\[
c=\cosh((\log K)/2)
\]
is strictly increasing for \(K>1\), the same is true of \(C(K)\).

For the endpoint expansion,
\[
c
=
1+\frac{q^2}{8}+O(q^4).
\]
Putting
\[
u=c-1,
\]
one gets
\[
\ell(c)
=
\frac{2(1+u)}{2+u}
=
1+\frac{u}{2}+O(u^2)
=
1+\frac{q^2}{16}+O(q^4).
\]
Therefore
\[
\coth\ell(c)
=
\coth1+O(q^2).
\]
Substitution in the exact formula gives
\[
C(K)
=
C_0+
\frac{q^2}{8}
\left(
C_0+\frac{3\sqrt3}{2}+\coth1
\right)
+
O(q^4).
\]
Since
\[
q=\log K=(K-1)+O((K-1)^2),
\]
the equivalent expansion in powers of \(K-1\) follows.

## Verification

The fresh primary source was inspected at its definition of harmonic \((K,K_0)\)-quasiregularity, Theorems 1.3--1.5, Lemma 2.6, and the proof of Theorem 1.5. In particular, the exact formula for \(C(K)\), the definitions of \(k\) and \(L(K)\), and the statement
\[
\lim_{K\to1^+}C(K)=C_0
\]
were checked directly in the primary full text.

The algebraic reduction to the \(q=\log K\) variable was reconstructed from that formula. The monotonicity proof uses only elementary hyperbolic identities and the displayed derivative. The endpoint coefficient follows from the ordinary Taylor expansions of \(\cosh\) and the smooth function \(\coth\) near \(1\).

The 2022 Huang--Rasila--Zhu predecessor was also checked at its theorem-level formulation: it proves a Lipschitz estimate for harmonic quasiregular Bloch-type mappings with a coefficient linear in \(K+1\), and it poses the optimal-constant problem later addressed by the fresh source.

No numerical experiment is needed for the proof. The decimal value of \(\alpha\) is only an evaluation of the exact expression.

## Relationship to prior work

Huang, Rasila, and Zhu proved the earlier estimate
\[
2.8587(K+1)
\]
for harmonic \(K\)-quasiregular Bloch-type mappings and asked for the optimal constant.

The 2026 source substantially improves that bound. Its Theorem 1.5 gives the explicit coefficient \(C(K)\) above and proves asymptotic sharpness in the sense that
\[
C(K)\to C_0
\]
as
\[
K\to1^+.
\]

The present result resolves the next perturbative question for that explicit coefficient. It shows that the convergence is not merely qualitative: the first variation in logarithmic distortion vanishes and the first nonzero term is exactly quadratic.

This also exposes a strong difference between the specialized \(K\)-quasiregular estimate and the coefficient obtained by simply setting
\[
K_0=0
\]
in the source's more general \((K,K_0)\)-quasiregular theorem. The latter displayed coefficient contains a term proportional to
\[
\sqrt{K-1},
\]
whereas the specialized coefficient satisfies
\[
C(K)-C_0=O((K-1)^2).
\]

Targeted searches for a quadratic small-distortion expansion, a logarithmic-distortion form, and reciprocal-dilatation symmetry of this coefficient did not locate a prior statement of the result.

## Limitations

The coefficient \(C(K)\) is the explicit asymptotically sharp upper bound proved by the source. The result does not prove that \(C(K)\) is the exact optimal constant for each fixed \(K>1\).

The quadratic law is an endpoint expansion near
\[
K=1.
\]
It does not by itself give a globally optimal replacement for the full coefficient.

The strict monotonicity proved here is monotonicity of the source's explicit coefficient, not of an independently defined unknown optimal constant.

## References

1. S. Chen, H. Hamada, M. Huang, and L. Jin, *The sharp Lipschitz continuity problem with respect to the pseudo hyperbolic metric*, arXiv:2609.33140v1, 2026.
2. J. Huang, A. Rasila, and J.-F. Zhu, *Lipschitz property of harmonic mappings with respect to the pseudo-hyperbolic metric*, Analysis Mathematica 48 (2022), 1069--1080; arXiv:2104.05976.
3. S. Chen, H. Hamada, and J.-F. Zhu, *Composition operators on Bloch and Hardy type spaces*, Mathematische Zeitschrift 301 (2022), 3939--3957.
