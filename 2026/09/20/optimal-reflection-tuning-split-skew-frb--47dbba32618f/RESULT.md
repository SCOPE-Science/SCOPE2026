# Optimal reflection tuning against split-skew FRB obstructions

## Statement

Consider the constant-reflection one-call forward-reflected-backward family
\[
x_{k+1}=J_{\lambda A}\!\left(x_k-\lambda Bx_k-\theta\lambda(Bx_k-Bx_{k-1})\right),
\qquad \theta\ge 0,
\]
for a maximally monotone operator \(A\) and a monotone \(L\)-Lipschitz operator \(B\).  Standard FRB is \(\theta=1\).

On the planar split-skew family
\[
A=\gamma L J,\qquad B=LJ,\qquad \gamma\ge0,
\]
where \(J(u,v)=(-v,u)\), put \(\tau=\lambda L\).  For every \(\theta>1/2\), the iteration is Schur stable exactly when
\[
0<\tau<\tau_\theta^\star(\gamma),
\]
where
\[
(\tau_\theta^\star(\gamma))^2
=\frac{\gamma+2\theta-1}{(\gamma+\theta)^2(2\theta+1-\gamma)},
\qquad 0\le\gamma<2\theta+1,
\]
and \(\tau_\theta^\star(\gamma)=\infty\) for \(\gamma\ge2\theta+1\).  At a finite threshold one characteristic root lies on the unit circle and the other lies strictly inside; above the threshold the spectral radius exceeds one.

The exact worst split-skew ceiling for a fixed reflection coefficient is
\[
c(\theta)=\inf_{\gamma\ge0}\tau_\theta^\star(\gamma).
\]
Among all constant reflection coefficients, its maximum is attained at
\[
\boxed{\theta_\star=\frac{1+\sqrt3}{4}=0.683012701892\ldots}
\]
and equals
\[
\boxed{
 c_\star=\sqrt{\frac83(7\sqrt3-12)}
 =0.575860290886\ldots .
}
\]
At \(\theta_\star\), the two global worst split-skew placements are exactly
\[
\gamma=0\quad\text{and}\quad\gamma=\frac12,
\]
and both give \(\tau_\theta^\star=c_\star\).  Thus the optimal robust reflection coefficient is an equioscillating choice: it balances the pure forward skew obstruction against a nonzero resolvent-skew obstruction.

For comparison, \(\theta=1\) gives
\[
(\tau_1^\star(\gamma))^2=\frac1{(1+\gamma)(3-\gamma)},\qquad 0\le\gamma<3,
\]
so the standard FRB worst split-skew ceiling is \(1/2\), attained at \(\gamma=1\).  Retuning the reflection coefficient therefore raises this exact split-skew ceiling by
\[
\frac{c_\star}{1/2}-1=15.172058\ldots\%.
\]
This is a sharp obstruction result for the split-skew test family, not a universal convergence theorem: a general monotone inclusion outside this family may impose a smaller step-size ceiling.

## Proof of the split-skew phase diagram

Identify \(\mathbb R^2\) with \(\mathbb C\), so that \(J\) is multiplication by \(i\).  The resolvent equation becomes
\[
(1+i\gamma\tau)z_{k+1}
=(1-i(1+\theta)\tau)z_k+i\theta\tau z_{k-1}.
\]
Hence the characteristic polynomial is
\[
(1+i\gamma\tau)r^2-(1-i(1+\theta)\tau)r-i\theta\tau=0.
\]
After division by \(1+i\gamma\tau\), write it as
\[
r^2-ar-b=0,
\]
with
\[
a=\frac{1-i(1+\theta)\tau}{1+i\gamma\tau},
\qquad
b=\frac{i\theta\tau}{1+i\gamma\tau}.
\]
For a quadratic \(r^2-ar-b\), Schur--Cohn gives the necessary and sufficient conditions
\[
|b|<1,
\qquad
|a+\overline a b|<1-|b|^2.
\]
Direct simplification gives
\[
|b|^2=\frac{\tau^2\theta^2}{1+\gamma^2\tau^2},
\]
\[
a+\overline a b
=
\frac{1-\tau^2(1+\theta)(\gamma+\theta)-i\tau(\gamma+1)}
{1+\gamma^2\tau^2},
\]
and
\[
(1-|b|^2)^2-|a+\overline a b|^2
=
\frac{\tau^2(\gamma+1)}{(1+\gamma^2\tau^2)^2}
\Bigl[
\gamma+2\theta-1
+\tau^2(\gamma+\theta)^2(\gamma-2\theta-1)
\Bigr].
\]
When \(\theta>1/2\), the bracket is positive for all finite \(\tau>0\) if \(\gamma\ge2\theta+1\).  If \(0\le\gamma<2\theta+1\), positivity is exactly
\[
\tau^2<
\frac{\gamma+2\theta-1}
{(\gamma+\theta)^2(2\theta+1-\gamma)}.
\]
The first Schur inequality is redundant on this range.  Indeed, if \(\gamma\ge\theta\) it is automatic.  If \(\gamma<\theta\), its separate bound is \(\tau^2<1/(\theta^2-\gamma^2)\), and
\[
\frac1{\theta^2-\gamma^2}-(\tau_\theta^\star)^2
=
\frac{2\theta(\gamma+1)}
{(\gamma-\theta)(\gamma+\theta)^2(\gamma-2\theta-1)}>0.
\]
This proves the phase diagram.  For \(\theta\le1/2\), the pure forward-skew slice \(\gamma=0\) has no positive robust small-step interval; the coefficient threshold \(\theta>1/2\) is already covered by recent work and is not claimed here as new.

## Proof of the robust optimum

Let
\[
h_\theta(\gamma)=(\tau_\theta^\star(\gamma))^2.
\]
For \(0\le\gamma<2\theta+1\),
\[
\partial_\gamma h_\theta
=
\frac{2\left[\gamma^2+2(\theta-1)\gamma+1-2\theta^2\right]}
{(\gamma+\theta)^3(\gamma-2\theta-1)^2}.
\]
Two useful test values are
\[
h_0(\theta):=h_\theta(0)
=\frac{2\theta-1}{\theta^2(2\theta+1)},
\]
\[
h_{1/2}(\theta):=h_\theta(1/2)
=4\frac{4\theta-1}{(2\theta+1)^2(4\theta+1)}.
\]
Their difference is
\[
h_0(\theta)-h_{1/2}(\theta)
=
\frac{8\theta^2-4\theta-1}
{\theta^2(2\theta+1)^2(4\theta+1)}.
\]
Thus their unique relevant crossing is
\[
\theta_\star=\frac{1+\sqrt3}{4}.
\]
At this value, the two roots of the numerator in \(\partial_\gamma h\) are
\[
\gamma_-=1-\frac{\sqrt3}{2},
\qquad
\gamma_+=\frac12.
\]
The derivative is positive on \([0,\gamma_-)\), negative on \((\gamma_-,1/2)\), and positive on \((1/2,2\theta_\star+1)\).  Since \(h\to\infty\) at the right endpoint and \(h(0)=h(1/2)\), the two tied global minima are \(\gamma=0\) and \(\gamma=1/2\).

It remains to show global optimality over \(\theta\).  If \(1/2<\theta\le\theta_\star\), then
\[
c(\theta)^2\le h_0(\theta),
\]
and
\[
h_0'(\theta)
=-\frac{2(4\theta^2-2\theta-1)}{\theta^3(2\theta+1)^2}>0
\]
through this interval, so \(c(\theta)^2\le h_0(\theta_\star)\).  If \(\theta\ge\theta_\star\), then
\[
c(\theta)^2\le h_{1/2}(\theta),
\]
and
\[
h_{1/2}'(\theta)
=-\frac{16(16\theta^2-4\theta-3)}{(2\theta+1)^3(4\theta+1)^2}<0,
\]
so again \(c(\theta)^2\le h_{1/2}(\theta_\star)\).  Evaluating the common value gives
\[
c_\star^2
=\frac83(7\sqrt3-12).
\]

## Relation to prior work

Shehu (arXiv:2609.18373) proved that the classical \(\theta=1\) FRB universal step-size constant \(1/(2L)\) is sharp, using the matched-skew example \(A=LJ,B=LJ\), and derived the exact \(\theta=1\) split-skew threshold.  The formula above recovers that result exactly when \(\theta=1\).

Ou, Themelis, and Latafat (arXiv:2609.15936) consider the same idea of replacing the unit FRB reflection coefficient by a constant coefficient and state in the abstract that the tight admissible coefficient range is all values greater than \(1/2\), for sufficiently small step size.  The parameterized algorithm and the \(\theta>1/2\) range are therefore not novelty claims here.

The slice \(A=0\) is also closely related to generalized optimistic gradient methods for bilinear zero-sum games, where exact linear convergence conditions and parameter tuning have long been analyzed; see Zhang and Yu (arXiv:1908.05699).  Accordingly, no novelty is claimed for the pure-forward rotation slice by itself.  Soe, Vetrivel, and Yao (arXiv:2509.02005) study a different generalized FRB involving an additional older operator value and different inertial parameters.

The new claim is deliberately narrower: to the best of our knowledge, the exact two-parameter \((\theta,\gamma)\) phase diagram above for the nonzero split-skew resolvent family, and especially its exact max--min tuning
\[
\theta_\star=(1+\sqrt3)/4,
\qquad
c_\star=\sqrt{\tfrac83(7\sqrt3-12)},
\]
have not been stated in the checked literature.

A material originality uncertainty remains: only the abstract of arXiv:2609.15936 was available for inspection.  Because that paper directly studies constant reflection coefficients, its full theorem/proof sections are the source most plausibly capable of already containing a related split-skew or constant-step sharpness formula.  Its abstract establishes overlap with the coefficient range but does not state the split-skew phase diagram or the robust max--min coefficient above.  If the inaccessible full text contains an equivalent formula, the corresponding originality claim here would have to be withdrawn.

## Numerical verification

`artifacts/verify_split_skew_reflection.py` independently evaluates the characteristic roots and the closed-form threshold.  It checks representative finite-threshold and unconditional regimes, verifies the \(\theta=1\) reduction, and performs a dense scan of the robust ceiling.

At \(\tau=0.55\), standard FRB on the matched-skew case has
\[
\rho=1.095410295993205>1,
\]
whereas the tuned coefficient gives
\[
\rho(\gamma=0)=0.985723085481399,
\quad
\rho(\gamma=1/2)=0.962583280829179,
\quad
\rho(\gamma=1)=0.940653812106153.
\]
A scan over \(0\le\gamma\le10\) found the largest tuned spectral radius at \(\gamma=0\), still below one.  At \(\tau=c_\star\), both \(\gamma=0\) and \(\gamma=1/2\) have one root of modulus one, as predicted.

## Limitations

This result is exact for the planar linear family \(A=\gamma LJ, B=LJ\).  It supplies sharp divergence/stability certificates inside that family and hence necessary upper ceilings for any universal theorem about the fixed-\(\theta\) algorithm.  It does **not** prove convergence for arbitrary maximally monotone \(A\) and monotone Lipschitz \(B\) up to \(c(\theta)/L\), nor that \(\theta_\star\) is universally optimal outside the split-skew family.  The result is an exact-arithmetic spectral statement; finite-precision behavior is not analyzed.

## References

- Y. Shehu, *The sharp step-size constant for one-call reflection splittings on monotone inclusions*, arXiv:2609.18373 (2026), https://arxiv.org/abs/2609.18373.
- H. Ou, A. Themelis, P. Latafat, *An Adaptive Linesearch-free Method for Monotone Variational Inequalities under Local Lipschitz Continuity*, arXiv:2609.15936 (2026), https://arxiv.org/abs/2609.15936.
- G. Zhang, Y. Yu, *Convergence of Gradient Methods on Bilinear Zero-Sum Games*, arXiv:1908.05699 (2019), https://arxiv.org/abs/1908.05699.
- S. Soe, V. Vetrivel, J.-C. Yao, *On Generalized Forward-Reflected-Backward Method for Monotone Inclusion Problems*, arXiv:2509.02005 (2025), https://arxiv.org/abs/2509.02005.
