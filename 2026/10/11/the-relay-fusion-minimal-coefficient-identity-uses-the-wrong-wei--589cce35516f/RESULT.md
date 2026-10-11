# The relay-fusion minimal-coefficient identity uses the wrong weight geometry

## Finding
Theorem 3.14 of Hong--Li states a Pythagorean identity intended to show that the canonical dual relay-fusion frame gives expansion coefficients of minimal norm. The identity is false when the relay weights are not all normalized to \(1\).

The defect is a mismatch between two coefficient geometries. The relay analysis and synthesis operators use one factor of \(v_{ij}\), whereas Theorem 3.14 imposes a reconstruction constraint with \(v_{ij}^2\) but measures the auxiliary coefficients with an unweighted norm.

A one-block example suffices. Let
\[
H=K_1=V_{11}=W_1=\mathbb C,\qquad
\Lambda_1=I,\qquad
v_{11}=2.
\]
Then
\[
S_{\mathcal R}=4I,
\qquad
\widehat\Lambda_1=\frac14I.
\]
For \(f=1\), the theorem requires
\[
1=4g_{11},
\]
so
\[
g_{11}=\frac14.
\]
Its claimed identity has left side
\[
\frac1{16},
\]
but its right side is
\[
4\left|\frac14\right|^2+
\left|\frac14-4\frac14\right|^2
=
\frac14+\frac9{16}
=
\frac{13}{16}.
\]
Hence the theorem fails.

The exact repair is to use the coefficient norm naturally induced by the relay weights. If
\[
A_{ij}=\tau_{V_{ij}}\Lambda_i\pi_{W_i}
\]
and
\[
a_{ij}(f)=A_{ij}S_{\mathcal R}^{-1}f,
\]
then every coefficient family satisfying
\[
f=\sum_{i,j}v_{ij}^2A_{ij}^*g_{ij}
\]
obeys
\[
\sum_{i,j}v_{ij}^2\|g_{ij}\|^2
=
\sum_{i,j}v_{ij}^2\|a_{ij}(f)\|^2
+
\sum_{i,j}v_{ij}^2\|g_{ij}-a_{ij}(f)\|^2.
\]
Therefore \(a(f)\) is the minimum-norm coefficient family in the weighted coefficient Hilbert space.

## Assumptions and scope
A relay fusion frame consists of closed relay subspaces, local relay subspaces, bounded analysis maps, and positive relay weights. Its analysis operator has coordinates
\[
v_{ij}A_{ij}f,
\]
and its synthesis operator is
\[
(c_{ij})\longmapsto
\sum_{i,j}v_{ij}A_{ij}^*c_{ij}.
\]
Consequently,
\[
S_{\mathcal R}
=
\sum_{i,j}v_{ij}^2A_{ij}^*A_{ij}.
\]

The counterexample is finite-dimensional and one-block. There are no convergence or closure issues.

The correction concerns the minimal-coefficient identity in Theorem 3.14. It does not challenge the reconstruction formula of Theorem 3.13.

## Proof
For the one-block example,
\[
\sum_{i,j}v_{ij}^2\|A_{ij}f\|^2
=
4|f|^2,
\]
so the family is a tight relay fusion frame and
\[
S_{\mathcal R}=4I.
\]
The canonical-dual analysis map is
\[
\widehat\Lambda_1
=
\Lambda_1S_{\mathcal R}^{-1}
=
\frac14I.
\]

At \(f=1\), the constraint in Theorem 3.14 gives
\[
g_{11}=\frac14.
\]
Substitution into the theorem's displayed equality gives
\[
\frac1{16}
\stackrel{\text{claimed}}{=}
\frac14+\frac9{16},
\]
which is impossible.

For the repaired identity, write
\[
a_{ij}=A_{ij}S_{\mathcal R}^{-1}f.
\]
The reconstruction hypothesis gives
\[
f=\sum_{i,j}v_{ij}^2A_{ij}^*g_{ij}.
\]
Taking the inner product with \(S_{\mathcal R}^{-1}f\) yields
\[
\langle f,S_{\mathcal R}^{-1}f\rangle
=
\sum_{i,j}v_{ij}^2
\langle g_{ij},a_{ij}\rangle.
\]
On the other hand,
\[
\langle f,S_{\mathcal R}^{-1}f\rangle
=
\left\langle
S_{\mathcal R}S_{\mathcal R}^{-1}f,
S_{\mathcal R}^{-1}f
\right\rangle
=
\sum_{i,j}v_{ij}^2\|a_{ij}\|^2.
\]
Thus
\[
\sum_{i,j}v_{ij}^2
\langle g_{ij}-a_{ij},a_{ij}\rangle
=
0.
\]
This is orthogonality in the weighted direct-sum inner product
\[
\langle x,y\rangle_v
=
\sum_{i,j}v_{ij}^2\langle x_{ij},y_{ij}\rangle.
\]
Pythagoras now gives
\[
\|g\|_v^2
=
\|a(f)\|_v^2+
\|g-a(f)\|_v^2,
\]
which is precisely the corrected formula.

Equivalently, if
\[
h_{ij}=v_{ij}g_{ij},
\]
then the reconstruction constraint becomes the ordinary relay synthesis equation
\[
f=T_{\mathcal R}^*h.
\]
The canonical minimum-norm solution is
\[
h=T_{\mathcal R}S_{\mathcal R}^{-1}f,
\]
whose coordinates are
\[
v_{ij}a_{ij}(f).
\]
This is the standard Hilbert-space least-norm geometry expressed in the variables used by the relay reconstruction.

## Verification
The open publisher full text was inspected at the relay representation space, the analysis and synthesis operators, the frame operator, Theorems 3.13 and 3.14, and the complete proof of Theorem 3.14.

The source defines the coefficient Hilbert space with the ordinary direct-sum inner product. Its analysis and synthesis maps contain one factor of \(v_{ij}\), while Theorem 3.14 asks for coefficients \(g_{ij}\) satisfying a reconstruction equation with \(v_{ij}^2\).

The last calculation in the source proof establishes
\[
\sum_{i,j}v_{ij}^2\|a_{ij}(f)\|^2
=
\sum_{i,j}v_{ij}^2\langle g_{ij},a_{ij}(f)\rangle.
\]
That is exactly the orthogonality relation needed for the corrected weighted identity. It does not imply the printed identity, whose residual is centered at \(v_{ij}^2a_{ij}(f)\).

All computations in the counterexample and repair are exact. No numerical experiment is used.

## Relationship to prior work
Classical frame and \(g\)-frame minimum-coefficient theorems apply the ordinary Hilbert direct-sum norm to coefficients entering the synthesis operator itself. The relay synthesis operator in the source uses one factor of \(v_{ij}\). After the change of variables
\[
h_{ij}=v_{ij}g_{ij},
\]
the corrected weighted formula is exactly that standard minimum-norm principle.

A later paper by Hong and Li develops relay fusion frames and bridging results for fusion frames, but the checked full-text material did not supply this Theorem 3.14 correction.

A separate previously identified issue in the same 2019 article concerns the local relay-dual construction and missing uniform bounds on a family of local frame operators. That statement has different hypotheses and conclusion and does not imply the weight-geometry failure of Theorem 3.14.

Targeted searches for the exact theorem number, minimal-coefficient identity, relay weights, squared-weight reconstruction, and correction terminology did not locate an indexed erratum or an equivalent correction.

## Limitations
The result corrects Theorem 3.14 and identifies the coefficient norm for which its underlying orthogonality calculation is valid.

It does not claim that all weights must equal \(1\) for every special coefficient family to satisfy the printed equality; cancellation among several blocks can occur. In the one-block scalar model, however, the printed identity holds for all \(f\) exactly when the positive weight is \(1\).

No claim is made about unrelated duality or stability theorems in the article.

## References
1. G. Hong and P. Li, *Relay fusion frames for Hilbert spaces*, Journal of Inequalities and Applications 2019, Article 226, DOI 10.1186/s13660-019-2181-9.
2. G. Hong and P. Li, *Relay fusion frames and bridging results for fusion frames*, Journal of Mathematical Analysis and Applications 489 (2020), Article 124124, DOI 10.1016/j.jmaa.2020.124124.
3. Z.-Q. Xiang, *Some Properties of Canonical Dual \(K\)-Bessel Sequences for Parseval \(K\)-Frames*, Journal of Function Spaces 2019, Article 9862369, DOI 10.1155/2019/9862369.
