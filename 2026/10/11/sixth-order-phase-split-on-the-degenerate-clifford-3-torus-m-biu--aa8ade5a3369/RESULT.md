# Sixth-order phase split on the degenerate Clifford 3-torus Möbius boundary

## Finding

Let
\[
f:T^3\longrightarrow\mathbb S^5\subset\mathbb R^6
\]
be the Clifford three-torus, and let
\[
v\in\mathbb S^5
\]
be a unit direction for the Möbius deformation used by Ni, Wang, and Xie. Write
\[
w_i=v_{2i-1}^2+v_{2i}^2,
\qquad i=1,2,3,
\]
so that
\[
w_1+w_2+w_3=1.
\]
Define
\[
\Sigma_2=w_1^2+w_2^2+w_3^2,
\qquad
\Pi=w_1w_2w_3.
\]
Let \(F_v(t)\) denote the total mean curvature of the corresponding Möbius image, with the source parameter
\[
t=\frac{2\varepsilon}{1+\varepsilon^2},
\]
and let
\[
V_0=\operatorname{Vol}(f).
\]

Then the exact small-\(t\) expansion through eighth order is
\[
\boxed{
\frac{F_v(t)}{V_0}
=
1
+\frac{2\Sigma_2-1}{16}t^4
+\frac{105\Sigma_2-41-690\Pi}{1728}t^6
+\frac{-382+1440\Sigma_2-555\Sigma_2^2-11400\Pi}{27648}t^8
+O(t^{10}).
}
\]

The source proves the fourth-order coefficient and explicitly notes that it gives no information on the boundary
\[
\Sigma_2=\frac12.
\]
On exactly that boundary, the expansion becomes
\[
\boxed{
\frac{F_v(t)}{V_0}
=
1+\frac{23-1380\Pi}{3456}t^6+O(t^8).
}
\]
Consequently, for sufficiently small nonzero \(t\), a quartically degenerate direction is strictly decreasing if and only if
\[
\boxed{\Pi>\frac1{60}.}
\]
It is strictly increasing when
\[
\Pi<\frac1{60}.
\]

There is one secondary degeneracy. If
\[
\Sigma_2=\frac12,
\qquad
\Pi=\frac1{60},
\]
then the sixth-order coefficient vanishes, but the eighth-order coefficient is positive:
\[
\boxed{
\frac{F_v(t)}{V_0}
=
1+\frac{37}{110592}t^8+O(t^{10}).
}
\]
Thus these directions are also strictly increasing for sufficiently small nonzero \(t\).

The threshold is nonvacuous. On
\[
\Sigma_2=\frac12,
\]
the feasible product range is exactly
\[
0\le\Pi\le\frac1{54}.
\]
For example,
\[
(w_1,w_2,w_3)=\left(\frac12,\frac12,0\right)
\]
has \(\Pi=0\) and lies in the increasing phase, whereas
\[
(w_1,w_2,w_3)=\left(\frac23,\frac16,\frac16\right)
\]
has \(\Pi=1/54\) and lies in the decreasing phase. The secondary value \(\Pi=1/60\) is attained by the three positive roots of
\[
z^3-z^2+\frac14z-\frac1{60}=0,
\]
which are approximately
\[
0.6590276224,
\qquad
0.2319333686,
\qquad
0.1090390091.
\]

## Assumptions and scope

The Clifford torus is parametrized in the source by
\[
f=\frac1{\sqrt3}(\alpha_1+\alpha_2+\alpha_3),
\]
with orthonormal tangent vectors \(\beta_i\). A torus translation rotates each coordinate two-plane independently, so the phase of each pair
\[
(v_{2i-1},v_{2i})
\]
may be absorbed into the torus coordinates. Hence the functional depends on the direction only through the three block weights \(w_i\).

The theorem is local in the Möbius parameter near \(t=0\). It does not assert global monotonicity along the full Möbius orbit, nor does it determine the global infimum discussed in the source.

## Proof

After absorbing the three block phases by torus translations, write
\[
v=(\sqrt{w_1},0,\sqrt{w_2},0,\sqrt{w_3},0).
\]
Let
\[
\gamma_i=\cos\theta_i,
\qquad
\eta_i=\sin\theta_i,
\]
where the three angles are independent uniform phase variables on the Clifford torus. The source's frame formulas give
\[
s:=\langle f,v\rangle
=
\frac1{\sqrt3}\sum_{i=1}^3\sqrt{w_i}\,\gamma_i
\]
and
\[
|v^\top|^2
=
\sum_{i=1}^3w_i\eta_i^2.
\]
Set
\[
P=|v^\top|^2+s^2.
\]
The exact Möbius formula of the source therefore becomes
\[
\frac{F_v(t)}{V_0}
=
\mathbb E\left[(1-t^2P)^{3/2}(1+ts)^{-3}\right],
\]
where \(\mathbb E\) denotes normalized integration over the three phase variables.

Simultaneously shifting all three phases by \(\pi\) sends \(s\) to \(-s\) and leaves \(P\) unchanged. Thus the functional is even in \(t\), so only even powers occur.

The two factors expand as
\[
(1-t^2P)^{3/2}
=
1-\frac32Pt^2+\frac38P^2t^4+\frac1{16}P^3t^6+\frac3{128}P^4t^8+O(t^{10})
\]
and
\[
(1+ts)^{-3}
=
1-3ts+6t^2s^2-10t^3s^3+15t^4s^4-21t^5s^5+28t^6s^6-36t^7s^7+45t^8s^8+O(t^9).
\]
The phase averages are exact because
\[
\mathbb E[\gamma_i^{2m}]
=
\frac{\binom{2m}{m}}{4^m},
\qquad
\mathbb E[\gamma_i^{2m+1}]=0,
\]
and the three phase variables are independent.

Carrying out these averages and using
\[
w_1+w_2+w_3=1
\]
gives vanishing quadratic coefficient and
\[
c_4=\frac{2\Sigma_2-1}{16},
\]
\[
c_6=\frac{105\Sigma_2-41-690\Pi}{1728},
\]
\[
c_8=\frac{-382+1440\Sigma_2-555\Sigma_2^2-11400\Pi}{27648}.
\]
This proves the displayed eighth-order expansion. The fourth-order term agrees exactly with the source formula for \(n=3\).

Now impose the source's degenerate condition
\[
\Sigma_2=\frac12.
\]
Then
\[
c_6
=
\frac{23-1380\Pi}{3456}.
\]
Hence the sixth-order sign changes at
\[
\Pi=\frac1{60}.
\]
At that value, direct substitution into \(c_8\) gives
\[
c_8=\frac{37}{110592}>0,
\]
which resolves the secondary degeneracy.

It remains to verify that all three regimes can occur. From
\[
(w_1+w_2+w_3)^2
=
\Sigma_2+2\sum_{i<j}w_iw_j,
\]
the condition \(\Sigma_2=1/2\) is equivalent to
\[
w_1w_2+w_1w_3+w_2w_3=\frac14.
\]
On this compact set, \(\Pi\ge0\). An interior extremum of \(\Pi\) has at least two equal weights. Setting
\[
w_2=w_3=x,
\qquad
w_1=1-2x,
\]
and imposing the pair-sum condition gives
\[
12x^2-8x+1=0.
\]
The positive interior solution is
\[
x=\frac16,
\]
which yields
\[
\Pi_{\max}=\frac1{54}.
\]
The boundary point \((1/2,1/2,0)\) gives \(\Pi=0\). Finally, the polynomial
\[
z^3-z^2+\frac14z-\frac1{60}
\]
has discriminant \(1/1200>0\) and one root in each of
\[
\left(\frac1{10},\frac19\right),
\qquad
\left(\frac15,\frac14\right),
\qquad
\left(\frac{13}{20},\frac23\right).
\]
Its roots are therefore positive and have elementary symmetric functions \(1\), \(1/4\), and \(1/60\), giving an actual secondary-degenerate direction.

## Verification

The bundled symbolic checker reconstructs the exact phase averages from the source integrand. It independently verifies that the coefficients of \(t^2,t^4,t^6,t^8\) are respectively
\[
0,
\qquad
\frac{2\Sigma_2-1}{16},
\qquad
\frac{105\Sigma_2-41-690\Pi}{1728},
\qquad
\frac{-382+1440\Sigma_2-555\Sigma_2^2-11400\Pi}{27648}.
\]
It also verifies the secondary value
\[
c_8=\frac{37}{110592}
\]
at \(\Sigma_2=1/2\), \(\Pi=1/60\), and the exact product extrema used in the phase classification.

No finite sampling is used to infer the Taylor coefficients or their signs. Numerical root values are included only to display one secondary-degenerate weight triple; their existence is proved by exact sign intervals and the cubic discriminant.

## Relationship to prior work

Ni, Wang, and Xie derive an exact Möbius-transformation formula for the total mean curvature of a minimal submanifold of a sphere. For the Clifford \(n\)-torus they prove
\[
\frac{F_v(t)}{V_0}
=
1+\frac{n-2}{32}\bigl((n+1)S_v-2\bigr)t^4+O(t^5),
\]
where
\[
S_v=\sum_i(v_{2i-1}^2+v_{2i}^2)^2.
\]
They explicitly state that when
\[
S_v=\frac{2}{n+1},
\]
the fourth-order coefficient vanishes and their expansion does not determine the behavior of the functional. They then choose the balanced direction \(v^\sharp\), for which the fourth-order coefficient is negative, and separately prove global monotonicity of that one-parameter family when \(n=4\).

The present result addresses the unresolved quartically degenerate locus in the first counterexample dimension \(n=3\). It shows that this locus is not behaviorally uniform: it contains both locally decreasing and locally increasing Möbius directions, separated at sixth order by the block product \(\Pi=1/60\), with the equality case decided positively at eighth order.

Targeted searches using the source identifier, the degenerate condition \(S_v=1/2\), sixth-order and eighth-order terminology, block-weight formulations, and the constant \(1/60\) did not locate a prior statement of this phase split.

## Limitations

The theorem resolves the source's fourth-order degeneracy only for the Clifford three-torus. It does not classify the analogous degenerate directions for all dimensions \(n\ge4\).

The conclusion is local for sufficiently small nonzero Möbius parameter. A direction that initially increases or decreases could change monotonicity farther along its Möbius orbit.

The result concerns total mean curvature, not the conformally invariant Willmore functional. The source explains that these functionals agree up to a constant on flat tori but behave differently under Möbius transformations once the deformed torus is no longer flat.

## References

1. Ruijie Ni, Peng Wang, and Zhenxiao Xie, *On the Willmore energy of flat \(n\)-tori in \(\mathbb R^N\) and Chen's conjecture for \(n\)-tori*, arXiv:2609.36491v1, first submitted 29 September 2026.
