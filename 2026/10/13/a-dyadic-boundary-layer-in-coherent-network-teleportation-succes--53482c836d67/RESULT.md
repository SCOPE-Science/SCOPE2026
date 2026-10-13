# A dyadic boundary layer in coherent-network teleportation success probability

## Finding

El Allati, Hassouni, and Metwally give the success probability for their entangled coherent quantum network as a function of the number of network participants and the coherent-state intensity. Put
\[
x=|\alpha|^2\ge0,\qquad a=2^{m-1},\qquad m\ge2.
\]
Starting from their Eq. (18), the probability has the exact form
\[
P_m(x)=\frac12\frac{1+e^{-2(2a-1)x}}{1+e^{-2ax}},
\]
with the continuous extension \(P_m(0)=1/2\).

For every \(m\ge2\), \(P_m\) has a unique global minimum. If
\[
q_m=e^{-2x_m},
\]
then \(q_m\in(0,1)\) is the unique solution of
\[
(2a-1)q_m^{a-1}+(a-1)q_m^{2a-1}=a.
\]
The minimum lies in a dyadically shrinking low-intensity layer. Precisely,
\[
2^m x_m\longrightarrow \log(1+\sqrt2)
\]
and
\[
P_m(x_m)\longrightarrow \sqrt2-1.
\]
For every fixed \(t\ge0\), the full boundary-layer profile is
\[
P_m\!\left(\frac{t}{2^m}\right)
\longrightarrow
\frac12\frac{1+e^{-2t}}{1+e^{-t}}.
\]
The limiting profile has its unique minimum at
\[
t=\log(1+\sqrt2)
\]
with value \(\sqrt2-1\).

For each fixed \(x\ge0\), one nevertheless has
\[
P_m(x)\longrightarrow\frac12.
\]
The convergence is therefore pointwise but not uniform on the full intensity half-line. In fact,
\[
\sup_{x\ge0}\left|P_m(x)-\frac12\right|
=\frac12-\min_{x\ge0}P_m(x)
\longrightarrow
\frac32-\sqrt2.
\]
Numerically, the limiting worst-case deficit is about \(0.0857864\).

## Assumptions and scope

The result concerns the analytic success-probability expression printed as Eq. (18) in the cited coherent-network teleportation paper. The parameter \(m\) is an integer with \(m\ge2\), and \(x=|\alpha|^2\) is nonnegative. The statement does not rederive the optical protocol or the state-preparation assumptions that lead to Eq. (18); it analyzes that published probability formula exactly.

The boundary-layer limit is a joint scaling limit in which the coherent-state intensity decreases as \(x=t/2^m\). The pointwise statement keeps \(x\) fixed while \(m\) tends to infinity. Distinguishing those two limits is essential.

## Proof

The source formula can be written as
\[
P_m(x)=
\frac{e^{-(a-1)x}}{2\sinh(2ax)}
\left(\sinh((3a-1)x)-\sinh((a-1)x)\right).
\]
Using
\[
\sinh u-\sinh v
=2\cosh\!\left(\frac{u+v}{2}\right)
 \sinh\!\left(\frac{u-v}{2}\right),
\]
the difference of hyperbolic sines equals
\[
2\cosh((2a-1)x)\sinh(ax).
\]
Since \(\sinh(2ax)=2\sinh(ax)\cosh(ax)\), cancellation for \(x>0\) gives
\[
P_m(x)=\frac{e^{-(a-1)x}\cosh((2a-1)x)}{2\cosh(ax)}
=\frac12\frac{1+e^{-2(2a-1)x}}{1+e^{-2ax}}.
\]
The right-hand side extends continuously to \(x=0\) with value \(1/2\).

Set
\[
q=e^{-2x}\in(0,1].
\]
Then
\[
P_m=\frac12\frac{1+q^{2a-1}}{1+q^a}.
\]
Differentiating with respect to \(q\) shows that the sign of the derivative is the sign of
\[
q^{a-1}F_a(q),
\]
where
\[
F_a(q)=(2a-1)q^{a-1}+(a-1)q^{2a-1}-a.
\]
For \(a\ge2\),
\[
F_a(0)=-a<0,
\qquad
F_a(1)=2a-2>0,
\]
and
\[
F_a'(q)=(a-1)(2a-1)\left(q^{a-2}+q^{2a-2}\right)>0
\]
for \(0<q<1\). Hence \(F_a\) has exactly one root \(q_m\in(0,1)\). Because \(q=e^{-2x}\) decreases strictly with \(x\), this root gives the unique global minimum of \(P_m\).

Let
\[
u_m=q_m^a=e^{-2ax_m}.
\]
The critical equation becomes
\[
\left(2-\frac1a\right)u_m^{1-1/a}
+\left(1-\frac1a\right)u_m^{2-1/a}=1.
\]
The left side is strictly increasing in \(u_m\in(0,1)\). Passing to the limit gives
\[
2u+u^2=1,
\]
whose unique solution in \((0,1)\) is
\[
u=\sqrt2-1.
\]
Therefore
\[
2^m x_m=2ax_m=-\log u_m
\longrightarrow -\log(\sqrt2-1)=\log(1+\sqrt2).
\]
At the minimizing point,
\[
q_m^a=u_m\to u,
\qquad
q_m^{2a-1}=u_m^{2-1/a}\to u^2.
\]
Thus
\[
P_m(x_m)
\longrightarrow
\frac12\frac{1+u^2}{1+u}
=\sqrt2-1.
\]

For the boundary layer, put \(x=t/2^m=t/(2a)\). Then
\[
e^{-2ax}=e^{-t},
\qquad
e^{-2(2a-1)x}=e^{-(2-1/a)t},
\]
so for every fixed \(t\ge0\),
\[
P_m(t/2^m)
\longrightarrow
\frac12\frac{1+e^{-2t}}{1+e^{-t}}.
\]
For fixed \(x>0\), both exponential corrections instead tend to zero, giving \(P_m(x)\to1/2\); at \(x=0\), equality with \(1/2\) holds identically.

Finally, because \(2a-1\ge a\) and \(0\le q\le1\),
\[
q^{2a-1}\le q^a,
\]
so \(P_m(x)\le1/2\) for all \(x\ge0\). Consequently the uniform error equals the depth of the unique minimum:
\[
\sup_{x\ge0}\left|P_m(x)-\frac12\right|
=\frac12-P_m(x_m)
\longrightarrow
\frac32-\sqrt2.
\]

## Verification

A deterministic checker reconstructs both the source hyperbolic expression and the simplified exponential quotient at multiple parameter values, verifies the unique derivative sign change for several integer network sizes, and tracks the scaled minimizer and minimum toward their analytic limits. It returns `VERIFY_OK`.

The checker is supplementary. The uniqueness and asymptotic statements are proved above from monotonicity and exact limiting equations; finite numerical sampling is not used as a proof of the infinite claims.

## Relationship to prior work

The source paper supplies Eq. (18), plots the finite-size success probability, and states qualitatively that increasing the number of participants makes the probability independent of the coherent-state intensity, with probability approaching \(1/2\) at low intensity. The exact quotient form, the unique-minimum equation, the dyadic boundary-layer profile, the limiting minimum \(\sqrt2-1\), and the resulting failure of uniform convergence are not stated in the inspected source text.

A later paper on bidirectional teleportation through an entangled coherent quantum network studies a different bidirectional protocol and reports dependence on coherent-state amplitude, decoherence, and user number. It does not supply an implication covering the one-way Eq. (18) boundary-layer theorem stated here.

Targeted searches for the source identifier, the exact probability formula, boundary-layer terminology, the constant \(\sqrt2-1\), and nonuniform large-network convergence did not locate a source stating the same theorem. The comparison is therefore limited by indexing and terminology: an unindexed or differently phrased follow-up could contain equivalent algebra or asymptotics.

## Limitations

The result is conditional on the correctness and intended parameterization of the published Eq. (18). It does not independently certify the complete teleportation protocol, experimental implementation, or every approximation used earlier in the source.

The theorem concerns the success probability only. It does not optimize fidelity, resource cost, decoherence robustness, or a different network architecture. The asymptotic nonuniformity is specifically with respect to the full intensity range \(x\ge0\).

No independent audit has been performed.

## References

1. A. El Allati, Y. Hassouni, and N. Metwally, “Communication via entangled coherent quantum network,” arXiv:1011.3915v1, first public 17 November 2010; *Physica Scripta* 83 (2011), 065002, DOI: 10.1088/0031-8949/83/06/065002.
2. “Bidirectional teleportation through an entangled coherent quantum network,” *Journal of the Optical Society of America B* 38 (2021), DOI: 10.1364/JOSAB.425157.
