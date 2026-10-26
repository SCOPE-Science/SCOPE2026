# Geometric accumulation of fold-phase returns in a same-chirality Bykov transition map

## Finding

Consider the local transition map
\[
\eta(x,y)=\bigl(x-K\log y,\ y^\delta\bigr),
\qquad K>0,\quad \delta>1,
\]
in the normalized coordinates used for a same-chirality Bykov cycle. Let \(h_\lambda\) be a positive \(C^2\) graph family, for \(\lambda\downarrow0\), satisfying
\[
h_\lambda(x)=\lambda g(x)+O_{C^2}(\lambda^2)
\]
near \(x_*\), where \(g(x_*)>0\),
\[
g(x_*)=K g'(x_*),\qquad (g-Kg')'(x_*)\ne0.
\]
The image curve has a unique nearby fold in its angular projection. Its lifted angular phase satisfies
\[
\theta_f(\lambda)=K\log(1/\lambda)+C+O(\lambda),
\qquad C=x_*-K\log g(x_*).
\]
For any fixed phase \(\theta_0\), define \(\lambda_n\downarrow0\) by
\[
\theta_f(\lambda_n)=\theta_0+2\pi n
\]
for all sufficiently large integers \(n\). Then
\[
\lambda_n=\exp\!\left(\frac{C-\theta_0}{K}\right)
e^{-2\pi n/K}\bigl(1+O(\lambda_n)\bigr),
\qquad
\lim_{n\to\infty}\frac{\lambda_{n+1}}{\lambda_n}=e^{-2\pi/K}.
\]
Thus the leading geometric ratio is determined by the logarithmic winding coefficient \(K\), independently of the first-order graph profile \(g\), the fold location \(x_*\), and the exponent \(\delta\).

## Assumptions and scope

The map is the leading local transition map for a same-chirality Bykov cycle in the normalization where the angular frequencies at the two saddle-foci are set to one. In the notation of Labouriau and Rodrigues, the coefficient is
\[
K=\frac{C_v+E_w}{E_vE_w}>0,
\]
and \(\delta=\delta_v\delta_w>1\). The graph expansion is an additional nondegeneracy assumption on the symmetry-breaking family; it is not claimed for every smooth unfolding without verification.

The phase \(\theta_f\) is lifted to the real line rather than reduced modulo \(2\pi\). The theorem concerns successive returns of the fold to a fixed angular phase. It does not, by itself, identify every such return with a heteroclinic tangency of the full vector field.

## Proof

Write the image of the graph as
\[
\theta_\lambda(x)=x-K\log h_\lambda(x),\qquad
z_\lambda(x)=h_\lambda(x)^\delta.
\]
A fold of the angular projection satisfies
\[
\theta_\lambda'(x)=1-K\frac{h_\lambda'(x)}{h_\lambda(x)}=0,
\]
equivalently \(F_\lambda(x)=0\), where
\[
F_\lambda(x)=h_\lambda(x)-K h_\lambda'(x).
\]
The assumed \(C^2\) expansion gives
\[
\frac{F_\lambda(x)}{\lambda}
=g(x)-K g'(x)+O_{C^1}(\lambda).
\]
At \(x_*\), the leading term vanishes and its derivative is nonzero. The implicit function theorem therefore gives a unique nearby root
\[
x_f(\lambda)=x_*+O(\lambda).
\]
Since \(g(x_*)>0\),
\[
h_\lambda(x_f(\lambda))
=\lambda g(x_*)+O(\lambda^2),
\]
and hence
\[
\log h_\lambda(x_f(\lambda))
=\log\lambda+\log g(x_*)+O(\lambda).
\]
Substitution into the angular coordinate yields
\[
\theta_f(\lambda)
=x_f(\lambda)-K\log h_\lambda(x_f(\lambda))
=K\log(1/\lambda)+C+O(\lambda),
\]
with \(C=x_*-K\log g(x_*)\). Differentiating the expansion gives
\[
\theta_f'(\lambda)=-K/\lambda+O(1)<0
\]
for sufficiently small positive \(\lambda\), while \(\theta_f(\lambda)\to+\infty\) as \(\lambda\downarrow0\). Thus each sufficiently large target phase \(\theta_0+2\pi n\) is attained at exactly one small \(\lambda_n\).

Solving the phase equation gives
\[
\log(1/\lambda_n)
=\frac{\theta_0+2\pi n-C}{K}+O(\lambda_n),
\]
so
\[
\lambda_n=
\exp\!\left(\frac{C-\theta_0}{K}\right)e^{-2\pi n/K}
\bigl(1+O(\lambda_n)\bigr).
\]
Taking the ratio at consecutive indices proves
\[
\frac{\lambda_{n+1}}{\lambda_n}\longrightarrow e^{-2\pi/K}.
\]
The conclusion is an asymptotic statement, not a finite-index exact geometric progression.

## Verification

The fold equation, implicit-function step, logarithmic expansion, monotonicity, and ratio limit are derived explicitly above. No numerical experiment is used as a proof. The result is conditional on the stated \(C^2\) graph expansion and simple-fold condition. For a full vector-field application, one must also verify that the higher-order transition-map terms preserve the lifted phase asymptotic with an \(o(1)\) error.

## Relationship to prior work

Labouriau and Rodrigues, *Global bifurcations close to symmetry* (arXiv:1504.01659v1), derive the same-chirality local map with first coordinate \(x-K\log y\) and prove that the fold winds around the cylinder infinitely often, producing a sequence of heteroclinic tangencies. Their stated result is qualitative and does not give the geometric ratio for phase-locked fold returns. The present statement adds that quantitative rate under an explicit first-order graph expansion and simple-fold hypothesis.

Labouriau and Rodrigues, *Global generic dynamics close to symmetry* (2012), establish related \(n\)-pulse connections and suspended horseshoes in a symmetry-breaking setting, but the inspected statements do not give this fold-phase spacing law. Their paper and the 2015 analysis motivate the same local geometry but do not imply the ratio merely from existence of infinitely many turns.

Labouriau and Rodrigues, *Dense heteroclinic tangencies near a Bykov cycle* (arXiv:1402.5455v1), concerns different chirality and tangencies accumulating near the cycle. Its mechanism is distinct from the same-chirality fold-return model here.

## Limitations

The ratio applies to phase-locked returns of the fold in the stated leading transition model. It is not a universal ratio for all heteroclinic tangencies, all parameterizations, or all Bykov cycles. Transfer to a specific full flow requires checking the higher-order transition terms, the first-order graph expansion, and any additional condition that relates a fold-phase return to a tangency. The asymptotic estimate does not supply a useful error bound for small finite indices without further coefficient information.

## References

1. I. S. Labouriau and A. A. P. Rodrigues, “Global bifurcations close to symmetry,” arXiv:1504.01659v1 (first public version 2015-04-07); published in *Journal of Mathematical Analysis and Applications* 444 (2016), 648–671.
2. I. S. Labouriau and A. A. P. Rodrigues, “Global generic dynamics close to symmetry,” *Journal of Differential Equations* 253 (2012), 2527–2557, DOI: 10.1016/j.jde.2012.06.009.
3. I. S. Labouriau and A. A. P. Rodrigues, “Dense heteroclinic tangencies near a Bykov cycle,” arXiv:1402.5455v1 (first public version 2014-02-22); published in *Journal of Differential Equations* 259 (2015), 5875–5902.
