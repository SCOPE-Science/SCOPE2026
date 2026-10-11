# Exact fixed-turning phase diagram for the slab Santaló path problem

## Finding

Fix an integer \(n\ge2\). For a causal curve
\[
\gamma(u)=(t(u),s(u))\in[-1,1]^2
\]
with nondecreasing coordinates and endpoints \((-1,-1)\) and \((1,1)\), define
\[
a(\gamma)=\max\left\{0,-\min_u t(u)s(u)\right\}
\]
and
\[
I_n(\gamma)=\int (1-ts)^{n/2}\sqrt{t's'}\,du.
\]
For a prescribed turning parameter \(a\), set
\[
H_n(a)=\sup\{I_n(\gamma):a(\gamma)=a\}.
\]

Let \(a_n\in(0,1)\) be the unique closing parameter from the sharp slab Santaló theorem, and put
\[
p_a=\frac12\sqrt{a(1+a)^n}.
\]
For
\[
0<a<1,\qquad p\ge p_a,
\]
define
\[
F_n(a,p)
=
2p\log\frac1a
+
\int_{-a}^{1}
\frac{(1-w)^n}
{\sqrt{4p^2+w(1-w)^n}+2p}\,dw
\]
and
\[
\Psi_n(a,p)
=
\log\frac1a
-
\int_{-a}^{1}
\frac{(1-w)^n}
{\sqrt{4p^2+w(1-w)^n}
\left(\sqrt{4p^2+w(1-w)^n}+2p\right)}
\,dw.
\]

Then
\[
\boxed{\partial_pF_n(a,p)=2\Psi_n(a,p)}
\]
and \(p\mapsto F_n(a,p)\) is strictly convex on \([p_a,\infty)\).

The exact fixed-turning phase diagram is
\[
\boxed{
H_n(a)=
\begin{cases}
\Sigma_n(a),&0\le a\le a_n,\\[1mm]
F_n(a,p_n^*(a)),&a_n<a<1,\\[1mm]
0,&a=1,
\end{cases}
}
\]
where, for every \(a_n<a<1\), \(p_n^*(a)\) is the unique solution of
\[
\boxed{\Psi_n(a,p_n^*(a))=0,\qquad p_n^*(a)>p_a.}
\]

For \(a_n<a<1\), the maximizing curve is obtained by joining the incoming and outgoing calibrated characteristics of momentum \(p_n^*(a)\). They meet at
\[
(\sqrt a,-\sqrt a)
\]
with a genuine corner.

There is also a sharp boundary law:
\[
\boxed{
p_n^*(a)\sqrt{1-a}
\longrightarrow
\frac{2^{(n-2)/2}}{\sqrt{n+1}}
}
\]
and
\[
\boxed{
\frac{H_n(a)}{\sqrt{1-a}}
\longrightarrow
\frac{2^{(n+2)/2}}{\sqrt{n+1}}
}
\qquad(a\uparrow1).
\]
Thus the exact fixed-turning optimum collapses to zero at the boundary with square-root order, even though the nonoptimized \(p_a\)-calibration bound is not the sharp fixed-\(a\) value in this regime.

## Assumptions and scope

The notation is that of the causal-curve reduction in the cited slab Santaló paper. The horizontal-section dimension is \(n\ge2\).

The theorem solves the auxiliary variational problem in which the turning parameter \(a(\gamma)\) is prescribed. It does not alter the global sharp constant of the slab Santaló inequality, whose optimizer occurs at \(a=a_n\).

The result uses the source's established fact that
\[
\Psi_n(a,p_a)>0\quad(0<a<a_n),
\qquad
\Psi_n(a_n,p_{a_n})=0,
\qquad
\Psi_n(a,p_a)<0\quad(a_n<a<1).
\]
All additional claims about variable momentum, uniqueness, exact fixed-\(a\) values, and the \(a\uparrow1\) asymptotics are proved below.

## Proof

For \(p\ge p_a\), set
\[
S_p(w)=\sqrt{4p^2+w(1-w)^n}.
\]
The condition \(p\ge p_a\) is exactly what makes \(S_p\) real on the full interval \([-a,1]\).

Define
\[
W_{a,p}(w)
=
p\log\frac{|w|}{a}
+
\frac12
\int_{-a}^{w}
\frac{(1-v)^n}{S_p(v)+2p}\,dv.
\]
Then \(W_{a,p}(-a)=0\), and the two separated Hamilton--Jacobi potentials
\[
\Phi_{a,p,\pm}(t,s)
=
p\log\left|\frac ts\right|
\pm W_{a,p}(ts)
\]
satisfy
\[
4(\Phi_{a,p,\pm})_t(\Phi_{a,p,\pm})_s=(1-ts)^n
\]
on their respective domains. The same sign check as in the source works for every \(p\ge p_a\): when \(ts\ge0\), one has \(S_p\ge2p\), while when \(-a\le ts\le0\), one has \(S_p\le2p\). Hence the relevant partial derivatives are nonnegative.

Split any causal curve with turning parameter \(a\) at a point where \(ts=-a\). Before the split use the minus potential, and after the split use the plus potential. Since \(W_{a,p}(-a)=0\), the two potentials agree at the switching point. The calibration inequality therefore gives
\[
I_n(\gamma)\le
\Phi_{a,p,+}(1,1)-\Phi_{a,p,-}(-1,-1)
=
2W_{a,p}(1)
=
F_n(a,p).
\]
Consequently
\[
H_n(a)\le\inf_{p\ge p_a}F_n(a,p).
\]

Differentiate under the integral sign. Since
\[
\frac{\partial}{\partial p}
\frac{1}{S_p(w)+2p}
=
-\frac{2}{S_p(w)(S_p(w)+2p)},
\]
we obtain
\[
\partial_pF_n(a,p)
=
2\log\frac1a
-
2\int_{-a}^{1}
\frac{(1-w)^n}{S_p(w)(S_p(w)+2p)}\,dw
=
2\Psi_n(a,p).
\]
For fixed \(a\), the integrand in the last integral is strictly decreasing in \(p\) on a set of positive measure. Hence \(\Psi_n(a,p)\) is strictly increasing in \(p\), and therefore
\[
\partial_p^2F_n(a,p)>0.
\]

When \(0<a<a_n\), the source gives
\[
\Psi_n(a,p_a)>0.
\]
Strict increase of \(\Psi_n(a,p)\) shows that \(F_n(a,p)\) is minimized at the boundary \(p=p_a\). The source constructs an equality curve from the two \(p_a\)-characteristics joined by a segment of the turning hyperbola, so
\[
H_n(a)=F_n(a,p_a)=\Sigma_n(a).
\]
At \(a=a_n\), the same conclusion holds, with the two characteristics meeting smoothly. The case \(a=0\) is the diagonal equality curve from the source.

Now let
\[
a_n<a<1.
\]
Then
\[
\Psi_n(a,p_a)<0.
\]
For fixed \(a<1\),
\[
\lim_{p\to\infty}\Psi_n(a,p)=\log\frac1a>0.
\]
Strict monotonicity therefore gives a unique
\[
p_n^*(a)>p_a
\]
with
\[
\Psi_n(a,p_n^*(a))=0.
\]
By strict convexity this is the unique minimizer of \(F_n(a,\cdot)\).

It remains to show that the optimized calibration bound is attained. The incoming momentum-\(p\) characteristic from \((-1,-1)\) can be parametrized by \(w=ts\) as
\[
s_-(w)
=
-\exp\left[
-\frac12
\int_w^1
\frac{(1-v)^n}{S_p(v)(S_p(v)+2p)}\,dv
\right],
\qquad
t_-(w)=\frac{w}{s_-(w)}.
\]
Its contact point with \(ts=-a\) has hyperbolic coordinate
\[
\rho(P_-)
=
-\frac12\Psi_n(a,p).
\]
The outgoing characteristic is its reflected counterpart and has
\[
\rho(P_+)
=
\frac12\Psi_n(a,p).
\]
At \(p=p_n^*(a)\), both contact points therefore coincide at \(\rho=0\), namely at
\[
P=(\sqrt a,-\sqrt a).
\]
Both arcs have increasing coordinates and hence remain inside the square. Their union is a causal curve with turning parameter exactly \(a\). Each arc is calibrated, and the two potentials agree at \(P\), so its action is exactly
\[
F_n(a,p_n^*(a)).
\]
Thus the upper bound is sharp.

For \(a=1\), a causal curve with minimum product \(-1\) must pass through one of the two corners
\[
(1,-1),\qquad(-1,1).
\]
Coordinate monotonicity then forces it to consist of one horizontal and one vertical boundary segment. Along each segment one of \(t'\) and \(s'\) vanishes, so
\[
H_n(1)=0.
\]

Finally consider \(a\uparrow1\). Write
\[
L_a=\log\frac1a,
\qquad
C_a=\int_{-a}^{1}(1-w)^n\,dw
=
\frac{(1+a)^{n+1}}{n+1}.
\]
The root \(p_n^*(a)\) tends to infinity: otherwise the positive integral in \(\Psi_n\) would stay bounded away from zero while \(L_a\to0\).

Because \(w(1-w)^n\) is uniformly bounded on \([-1,1]\), the large-\(p\) expansions are uniform for \(a\) near \(1\):
\[
\frac{1}{S_p(w)(S_p(w)+2p)}
=
\frac{1}{8p^2}+O(p^{-4}),
\]
and
\[
\frac{1}{S_p(w)+2p}
=
\frac{1}{4p}+O(p^{-3}).
\]
The equation \(\Psi_n(a,p_n^*(a))=0\) gives
\[
L_a
=
\frac{C_a}{8(p_n^*(a))^2}
+
O((p_n^*(a))^{-4}).
\]
Since
\[
C_a\to\frac{2^{n+1}}{n+1},
\qquad
L_a\sim1-a,
\]
we obtain
\[
p_n^*(a)\sqrt{1-a}
\longrightarrow
\sqrt{\frac{2^{n+1}}{8(n+1)}}
=
\frac{2^{(n-2)/2}}{\sqrt{n+1}}.
\]

At the minimizing momentum,
\[
H_n(a)
=
2p_n^*(a)L_a
+
\frac{C_a}{4p_n^*(a)}
+
O((p_n^*(a))^{-3}).
\]
The root equation shows that the first two displayed contributions are asymptotically equal. Therefore
\[
H_n(a)
=
4p_n^*(a)L_a
+
o(\sqrt{L_a}),
\]
and hence
\[
\frac{H_n(a)}{\sqrt{1-a}}
\longrightarrow
\sqrt{\frac{2^{n+2}}{n+1}}
=
\frac{2^{(n+2)/2}}{\sqrt{n+1}}.
\]

## Verification

The bundled checker numerically reconstructs the unique optimized momentum for several dimensions and values of \(a\) near \(1\), checks strict increase of \(\Psi_n(a,p)\), verifies
\[
\partial_pF_n=2\Psi_n
\]
by centered finite differences, and confirms convergence to both analytic endpoint constants.

These computations are supplementary. The infinite-dimensional-in-parameter conclusions are established by the calibration argument, strict monotonicity of the integral kernel, and the uniform large-\(p\) expansion in the proof.

## Relationship to prior work

The primary source constructs the sharp global slab Santaló inequality and, in Remark 6.5, observes that the auxiliary fixed-\(a\) problem can be handled by allowing momentum \(p\ge p_a\). It states qualitatively that minimizing the resulting calibration bounds gives the exact fixed-\(a\) value, that the minimizing momentum equals \(p_a\) in the closing regime, and that it is strictly larger after the closing threshold. The paper explicitly leaves this fixed-parameter problem undeveloped.

The result here carries that observation to a complete scalar phase diagram. It writes the variable-momentum objective and closing equation explicitly, proves strict convexity and uniqueness of the minimizing momentum, proves attainment by the cornered characteristic pair, treats the endpoint \(a=1\), and determines the sharp square-root boundary asymptotics of both the optimal momentum and the optimal action.

Searches for the source identifier together with fixed-turning, variable-momentum, closing-mismatch, and endpoint-asymptotic terminology did not locate a separate public result containing this phase diagram or the constants above.

## Limitations

The theorem concerns the relaxed causal-curve problem with prescribed turning parameter. It does not assert a new global Santaló constant or a new global extremizer.

The source already contains the key qualitative insight that variable momentum solves the post-closing fixed-\(a\) problem. Accordingly, the new content is the explicit one-variable optimization, uniqueness, exact characteristic realization, and boundary law rather than the general idea of varying momentum.

A very recent or unindexed follow-up could independently spell out the auxiliary calculation; no such source was found in the targeted searches.

## References

1. Shiri Artstein-Avidan, *A sharp Santaló inequality in a slab with centrally symmetric sections*, arXiv:2609.38041v1, 29 September 2026.
