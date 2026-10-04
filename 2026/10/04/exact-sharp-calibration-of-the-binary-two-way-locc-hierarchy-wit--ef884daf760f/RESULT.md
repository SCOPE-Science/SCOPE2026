# Exact sharp calibration of the binary two-way LOCC hierarchy witness

## Finding

Chitambar and Hsieh exhibit an equiprobable binary two-qubit ensemble for which two-way classical communication strictly improves minimum-error discrimination over optimal one-way LOCC. Their explicit two-way protocol has a measurement-strength parameter
\[
p\in[0,1]
\]
and total error probability
\[
E(p)
=
\frac{1}{16}
\left(
6-\sqrt{4-3p}-\sqrt{4+5p}
\right).
\]

The exact unique optimum of this published protocol family is
\[
\boxed{
p_*=\frac{8}{15}
}.
\]
At that point,
\[
\boxed{
E_*=
\frac{3}{8}-\frac{\sqrt{15}}{15}
}
=
0.1168011102528\ldots .
\]

The source proves that the optimal one-way LOCC error for the same ensemble is
\[
E_{\to}=\frac18.
\]
Therefore the largest advantage attained inside the displayed two-way protocol family is exactly
\[
E_{\to}-E_*
=
\frac{\sqrt{15}}{15}-\frac14
=
\frac{4\sqrt{15}-15}{60}
=
0.00819888974716\ldots>0.
\]

For comparison, the separable-operation optimum quoted by the source is
\[
E_{\mathrm{SEP}}
=
\frac{3-\sqrt5}{8}.
\]
The optimized explicit LOCC protocol does not attain that lower value:
\[
E_*-E_{\mathrm{SEP}}
=
\frac{\sqrt5}{8}-\frac{\sqrt{15}}{15}
=
0.0213096074403\ldots>0.
\]

Thus the two-way communication advantage furnished by the source's concrete witness can be calibrated exactly rather than only read qualitatively from its plotted error curve.

## Assumptions and scope

The theorem concerns exactly the one-parameter two-way LOCC protocol of Chitambar and Hsieh for their equiprobable binary two-qubit ensemble. Alice uses their parameterized first weak measurement, Bob performs the conditional computational-basis measurement, and Alice performs the source's final optimal discrimination step.

The parameter range is
\[
0\le p\le1.
\]
The theorem optimizes the error of this explicit protocol family only. It does not prove the globally optimal finite-round or unrestricted two-way LOCC error for the ensemble. It also does not change the source's proofs of the optimal one-way error or the separable-operation benchmark.

## Proof

Write
\[
F(p)=\sqrt{4-3p}+\sqrt{4+5p}.
\]
Since
\[
E(p)=\frac{6-F(p)}{16},
\]
minimizing \(E\) is equivalent to maximizing \(F\).

For \(0\le p\le1\),
\[
F'(p)
=
-\frac{3}{2\sqrt{4-3p}}
+
\frac{5}{2\sqrt{4+5p}},
\]
and
\[
F''(p)
=
-\frac{9}{4(4-3p)^{3/2}}
-
\frac{25}{4(4+5p)^{3/2}}
<0.
\]
Thus \(F\) is strictly concave and has at most one stationary point.

The equation \(F'(p)=0\) is equivalent to
\[
\frac{5}{\sqrt{4+5p}}
=
\frac{3}{\sqrt{4-3p}}.
\]
Both sides are positive, so squaring is reversible. Hence
\[
25(4-3p)=9(4+5p),
\]
which gives
\[
p_*=\frac8{15}.
\]
Because
\[
F'(0)=\frac12>0
\]
and
\[
F'(1)=-\frac23<0,
\]
the stationary point lies in the interval and is the unique global maximizer of \(F\). Therefore it is the unique global minimizer of \(E\).

At \(p=8/15\),
\[
4-3p=\frac{12}{5},
\qquad
4+5p=\frac{20}{3}.
\]
Consequently,
\[
\sqrt{4-3p_*}
=
\frac{2\sqrt{15}}5,
\qquad
\sqrt{4+5p_*}
=
\frac{2\sqrt{15}}3,
\]
and hence
\[
F(p_*)=\frac{16\sqrt{15}}{15}.
\]
Substitution gives
\[
E_*
=
\frac{1}{16}
\left(
6-\frac{16\sqrt{15}}{15}
\right)
=
\frac38-\frac{\sqrt{15}}{15}.
\]

The exact one-way advantage follows by subtracting from
\[
E_{\to}=\frac18.
\]
Its positivity follows from
\[
4\sqrt{15}>15,
\]
because squaring gives \(240>225\).

Finally,
\[
E_*-E_{\mathrm{SEP}}
=
\left(
\frac38-\frac{\sqrt{15}}{15}
\right)
-
\frac{3-\sqrt5}{8}
=
\frac{\sqrt5}{8}-\frac{\sqrt{15}}{15}.
\]
This is positive because
\[
15\sqrt5>8\sqrt{15},
\]
equivalently \(1125>960\) after squaring.

## Verification

`verify_binary_two_way_optimum.py` independently reconstructs the exact rational optimizer and evaluates all radical constants with high-precision decimal arithmetic. It checks the reversible stationary equation, the endpoint derivative signs, the exact one-way and separable gaps, and the closed-form value of the minimum.

As a supplementary stress test, the script evaluates the protocol error on a uniform grid of \(200001\) points in \([0,1]\) and verifies that the best grid point lies within one grid spacing of \(8/15\), with error no smaller than the proven exact minimum.

The finite grid is not used to establish global optimality. Uniqueness follows from the strictly negative second derivative of \(F\).

## Relationship to prior work

Chitambar and Hsieh derive the one-way optimum
\[
E_{\to}=\frac18
\]
for their binary ensemble and then construct the one-parameter two-way protocol. Their equation for its total error is
\[
\frac{1}{16}
\left(
6-\sqrt{4-3p}-\sqrt{4+5p}
\right).
\]
The source plots this expression and states that the endpoints \(p=0\) and \(p=1\) reproduce the one-way value while every interior value improves on it. It also quotes the smaller separable-operation error
\[
\frac{3-\sqrt5}{8}.
\]
The inspected source does not state the exact minimizing value \(p=8/15\), the exact protocol minimum, or the exact maximal gap to one-way LOCC.

The separable benchmark comes from earlier two-qubit state-discrimination work by Chitambar, Duan, and Hsieh. That broader work concerns optimality under LOCC and separable measurements, not this scalar optimization of the later explicit feedback protocol.

Targeted searches using the source title, the two square-root terms, the exact value \(8/15\), and the radical value \(3/8-\sqrt{15}/15\) did not locate an equivalent published optimization. The present statement is therefore deliberately limited to the sharp calibration of the already-published witness protocol.

## Limitations

The result does not determine the unrestricted two-way LOCC optimum. A different protocol with more rounds or a different measurement architecture could attain a smaller error.

The exact optimization is one-dimensional because the source has already fixed the state ensemble and the rest of the adaptive measurement architecture. The mathematical contribution is the sharp closed-form calibration of this natural operational witness, not a new discrimination protocol.

An equivalent simplification may exist in unindexed notes, lecture material, or later work using a different parameter convention. The literature comparison therefore supports only the narrow originality claim stated above.

## References

1. E. Chitambar and M.-H. Hsieh, “Asymptotic State Discrimination and a Strict Hierarchy in Distinguishability Norms,” arXiv:1311.1536, first submitted 6 November 2013; *Journal of Mathematical Physics* 55, 112204 (2014), DOI: 10.1063/1.4902027.
2. E. Chitambar, R. Duan, and M.-H. Hsieh, “When Do Local Operations and Classical Communication Suffice for Two-Qubit State Discrimination?,” arXiv:1308.1737; *IEEE Transactions on Information Theory* 60, 1549–1561 (2014), DOI: 10.1109/TIT.2013.2295356.
