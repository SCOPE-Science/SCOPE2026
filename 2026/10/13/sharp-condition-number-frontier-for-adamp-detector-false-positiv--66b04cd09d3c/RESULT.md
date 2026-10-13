# Sharp condition-number frontier for AdamP detector false positives
## Finding

AdamP automatically decides whether a parameter group is scale invariant by comparing the cosine between the parameter vector and its gradient with a dimension-normalized threshold. On an ordinary strictly convex quadratic, the same cosine can become small for a completely different reason: ill-conditioning.

Let
\[
f(w)=\frac12 w^\top H w,
\qquad
H\succ0,
\]
on a detector group of dimension
\[
d.
\]
Write
\[
\mu=\lambda_{\min}(H),
\qquad
L=\lambda_{\max}(H),
\qquad
\kappa=\frac{L}{\mu}.
\]
AdamP's source detector projects when
\[
\cos(w,\nabla f(w))
<
\frac{\delta}{\sqrt d},
\]
where
\[
\cos(a,b)
=
\frac{|a^\top b|}{\|a\|\,\|b\|}.
\]
For the SPD quadratic,
\[
\nabla f(w)=Hw,
\]
and therefore
\[
\cos(w,Hw)>0.
\]

The exact minimum over all nonzero states is
\[
\boxed{
\min_{w\ne0}
\cos(w,Hw)
=
\frac{2\sqrt{\mu L}}{\mu+L}
=
\frac{2\sqrt{\kappa}}{\kappa+1}
}.
\]

Let
\[
\tau=\frac{\delta}{\sqrt d},
\qquad
0<\tau<1.
\]
Because AdamP uses the strict test
\[
\cos(w,Hw)<\tau,
\]
the detector is guaranteed never to activate anywhere on the quadratic if and only if
\[
\frac{2\sqrt{\kappa}}{\kappa+1}\ge\tau.
\]
Solving the equality gives the sharp frontier
\[
\boxed{
\kappa_\star(d,\delta)
=
\left(
\frac{\sqrt d+\sqrt{d-\delta^2}}{\delta}
\right)^2
}.
\]

Hence
\[
\kappa\le\kappa_\star(d,\delta)
\]
is exactly the regime in which curvature alone cannot make AdamP declare this scale-variant quadratic group scale invariant.

If
\[
\kappa>\kappa_\star(d,\delta),
\]
then false-positive directions exist for every SPD \(H\) with that condition number. Let \(u_\mu\) and \(u_L\) be unit eigenvectors for the smallest and largest eigenvalues. A minimizer of the cosine is
\[
w_\star
=
\sqrt{\frac{L}{\mu+L}}\,u_\mu
+
\sqrt{\frac{\mu}{\mu+L}}\,u_L.
\]
Thus
\[
\frac{
|\langle w_\star,u_L\rangle|^2
}{
|\langle w_\star,u_\mu\rangle|^2
}
=
\frac{\mu}{L}
=
\frac1\kappa.
\]
At this point the cosine equals the displayed minimum. If the minimum is strictly below AdamP's threshold, continuity gives an open cone of nearby false-positive states.

For the source-recommended
\[
\delta=0.1,
\]
the sharp frontiers are
\[
\begin{array}{c|c}
d & \kappa_\star(d,0.1)\\
\hline
1 & 397.997487421\ldots\\
2 & 797.998746865\ldots\\
64 & 25597.999960934\ldots\\
256 & 102397.999990234\ldots
\end{array}
\]
and, for large \(d\),
\[
\kappa_\star(d,0.1)
=
400d-2+O(d^{-1}).
\]

The quadratic is genuinely scale variant:
\[
f(cw)=c^2f(w),
\]
so any activation of the detector on a nonzero state is a false positive with respect to exact scale invariance. The theorem therefore separates two causes of near orthogonality: true scale invariance and extreme curvature anisotropy.

## Assumptions and scope

The detector is the cosine test in the defining AdamP update:
\[
\cos(w,\nabla f(w))
<
\delta/\sqrt{\dim(w)}.
\]
The paper applies the test channel-wise or layer-wise in practice; here \(d\) is the vector dimension of one such detector group.

The objective is an SPD quadratic and therefore strictly convex and scale variant.

The theorem concerns only the automatic scale-invariance detector and whether projection is invoked. It does not claim that the subsequent projected AdamP trajectory diverges or converges.

The threshold is assumed to satisfy
\[
0<\delta<\sqrt d,
\]
which includes the source recommendation
\[
\delta=0.1.
\]

## Proof

Diagonalize
\[
H=U\Lambda U^\top
\]
and write
\[
z=U^\top w.
\]
Define probability weights
\[
p_i=\frac{z_i^2}{\|z\|^2}
\]
and eigenvalues
\[
\lambda_i\in[\mu,L].
\]
Then
\[
\cos(w,Hw)^2
=
\frac{
\left(\sum_i p_i\lambda_i\right)^2
}{
\sum_i p_i\lambda_i^2
}.
\]
Set
\[
m=\sum_i p_i\lambda_i.
\]

For every
\[
\lambda\in[\mu,L],
\]
\[
(\lambda-\mu)(L-\lambda)\ge0,
\]
so
\[
\lambda^2
\le
(\mu+L)\lambda-\mu L.
\]
Averaging with the \(p_i\) gives
\[
\sum_i p_i\lambda_i^2
\le
(\mu+L)m-\mu L.
\]
Therefore
\[
\cos(w,Hw)^2
\ge
\frac{m^2}{(\mu+L)m-\mu L}.
\]

The right-hand side is minimized over
\[
m\in[\mu,L]
\]
at
\[
m_\star
=
\frac{2\mu L}{\mu+L}.
\]
Its minimum value is
\[
\frac{4\mu L}{(\mu+L)^2}.
\]
Taking square roots proves
\[
\cos(w,Hw)
\ge
\frac{2\sqrt{\mu L}}{\mu+L}.
\]

The bound is attained using only the extremal eigenspaces. Give the \(L\)-eigenvector total squared weight
\[
\frac{\mu}{\mu+L}
\]
and the \(\mu\)-eigenvector total squared weight
\[
\frac{L}{\mu+L}.
\]
Then both inequalities above are equalities, proving sharpness.

Now put
\[
\tau=\delta/\sqrt d
\]
and
\[
y=\sqrt{\kappa}\ge1.
\]
The boundary equation
\[
\frac{2y}{y^2+1}=\tau
\]
is
\[
\tau y^2-2y+\tau=0.
\]
The relevant root is
\[
y_\star
=
\frac{1+\sqrt{1-\tau^2}}{\tau}.
\]
Hence
\[
\kappa_\star
=
y_\star^2
=
\left(
\frac{\sqrt d+\sqrt{d-\delta^2}}{\delta}
\right)^2.
\]

The minimum cosine decreases strictly with \(\kappa\ge1\). Because AdamP's detector uses a strict inequality, no state triggers at or below the boundary, while above it the extremal-eigenspace witness triggers. Continuity then gives a nonempty open cone of triggering states.

For fixed \(\delta\), expansion of the square root gives
\[
\kappa_\star(d,\delta)
=
\frac{4d}{\delta^2}
-
2
+
O(d^{-1}).
\]
Substituting
\[
\delta=0.1
\]
gives the displayed numerical values.

## Verification

The accompanying `verify.py` independently checks the analytic lower bound on randomized SPD spectra and states, the exact two-eigenvector equality witness, the inversion of the cosine threshold, and the source-default numerical frontiers.

The finite computations are transcription guards. The universal minimum and sharp frontier are proved algebraically above.

## Relationship to prior work

Heo and coauthors introduced AdamP to remove radial update components on scale-invariant parameters. Their defining update automatically declares a parameter group scale invariant when the absolute cosine between the current weight and gradient is smaller than
\[
\delta/\sqrt{\dim(w)}.
\]
They recommend
\[
\delta=0.1.
\]

The source appendix empirically compares this detector on scale-invariant and scale-variant neural-network weights. It reports a clear empirical separation and high detection accuracy over a broad range of \(\delta\), but does not give a worst-case condition-number analysis for ordinary scale-variant objectives.

The present result supplies that missing deterministic boundary on the canonical SPD quadratic class. It shows that small cosine does not logically imply scale invariance: sufficiently strong curvature anisotropy can produce the same detector signal, with an exact condition-number threshold.

Focused published-record searches for AdamP detector false positives, condition-number thresholds, quadratic cosine bounds in the AdamP setting, and equivalent projection-activation conditions did not locate an implication-equivalent result.

## Limitations

The theorem is a worst-case geometric statement. It does not estimate how often training trajectories visit the false-positive cone.

The detector group dimension \(d\) depends on whether AdamP is applied channel-wise or layer-wise.

The result does not challenge the source paper's empirical detector accuracy on its tested networks.

The subsequent projected optimizer dynamics are outside the claim.

## References

1. Byeongho Heo, Sanghyuk Chun, Seong Joon Oh, Dongyoon Han, Sangdoo Yun, Gyuwan Kim, Youngjung Uh, and Jung-Woo Ha, “AdamP: Slowing Down the Slowdown for Momentum Optimizers on Scale-invariant Weights,” arXiv:2006.08217v1, 2020; ICLR 2021.
