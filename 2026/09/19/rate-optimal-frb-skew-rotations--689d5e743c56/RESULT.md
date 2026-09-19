# Exact rate-optimal steps for FRB/RFB on the skew-rotation family

## Statement

Let \(J(x_1,x_2)=(-x_2,x_1)\), let \(L>0\), and consider the monotone inclusion
\[
0\in (A+B)x,\qquad A=\gamma L J,\qquad B=LJ,
\]
with a fixed forward-reflected-backward (FRB) step \(\lambda>0\). Since \(B\) is linear, the reflected-forward-backward (RFB) iteration is identical on this family. Put
\[
h=\lambda L.
\]

For \(\gamma\neq-1\), the solution is uniquely \(x_\star=0\). Identifying \(\mathbb R^2\) with \(\mathbb C\), the scalar recurrence has characteristic polynomial
\[
p_{\gamma,h}(r)
=(1+i\gamma h)r^2-(1-2ih)r-ih.
\]
Let \(\rho_\gamma(h)\) denote the spectral radius of its two roots.

### Theorem 1: finite rate optimum for \(\gamma>-1\)

For every \(\gamma>-1\), \(\rho_\gamma(h)\) has a unique global minimum over \(h>0\), attained at
\[
\boxed{
h_{\rm opt}=\frac{1}{2\sqrt{1+\gamma}}
}
\]
with
\[
\boxed{
\rho_{\rm opt}=\frac{1}{\sqrt{\gamma+2}}.
}
\]
Equivalently,
\[
\boxed{
\lambda_{\rm opt}
=\frac{1}{2L\sqrt{1+\gamma}}.
}
\]

The optimum occurs exactly where the characteristic discriminant vanishes. Thus the two characteristic roots coalesce at the fastest asymptotic step.

More explicitly, for
\[
0<h\le h_{\rm opt},\qquad
u=\sqrt{1-4(1+\gamma)h^2},
\]
one has
\[
\boxed{
\rho_\gamma(h)^2
=
\frac{1+u}{\gamma+2-\gamma u}.
}
\]
For \(h\ge h_{\rm opt}\), define
\[
w=
\frac{\sqrt{4(1+\gamma)h^2-1}}
{2\sqrt{1+\gamma}\,h}\in[0,1).
\]
Then
\[
\boxed{
\rho_\gamma(h)^2
=
\frac{1}
{\gamma+2-2\sqrt{\gamma+1}\,w}.
}
\]
The first expression is strictly decreasing in \(h\), and the second is strictly increasing in \(h\).

### Theorem 2: the remaining pure-skew line

At \(\gamma=-1\), \(A+B\equiv0\). One root is \(r=1\) for every \(h>0\), while the other has modulus \(h/\sqrt{1+h^2}<1\); hence
\[
\rho_{-1}(h)=1.
\]

For every \(\gamma<-1\),
\[
u=\sqrt{1+4(-1-\gamma)h^2}>1
\]
and
\[
\boxed{
\rho_\gamma(h)^2
=
\frac{1+u}{\gamma+2-\gamma u}.
}
\]
This is strictly decreasing in \(h\), with
\[
\boxed{
\inf_{h>0}\rho_\gamma(h)
=
\lim_{h\to\infty}\rho_\gamma(h)
=
\frac{1}{\sqrt{-\gamma}}.
}
\]
Thus \(\gamma=-1\) is a rate-phase boundary: for \(\gamma>-1\) the fastest fixed step is finite, whereas for \(\gamma<-1\) the spectral radius decreases monotonically toward a nonzero limiting infimum.

## Proof

The recent sharp-stability analysis for this family gives
\[
p_{\gamma,h}(r)
=(1+i\gamma h)r^2-(1-2ih)r-ih.
\]
Its discriminant simplifies unusually strongly:
\[
\Delta
=(1-2ih)^2+4ih(1+i\gamma h)
=
1-4(1+\gamma)h^2.
\]

Assume first \(\gamma>-1\).

When \(\Delta\ge0\), put
\[
u=\sqrt{\Delta}.
\]
The roots are
\[
r_\pm=
\frac{1-2ih\pm u}{2(1+i\gamma h)}.
\]
The \(+\) root has the larger modulus. Since
\[
4(1+\gamma)h^2=1-u^2,
\]
direct cancellation gives
\[
|r_+|^2
=
\frac{1+u}{\gamma+2-\gamma u}.
\]
Differentiating with respect to \(u\),
\[
\frac{d}{du}|r_+|^2
=
\frac{2(\gamma+1)}
{(\gamma+2-\gamma u)^2}>0.
\]
Because \(u\) strictly decreases with \(h\), the spectral radius strictly decreases until \(\Delta=0\).

When \(\Delta<0\), write
\[
\sqrt{\Delta}=it,\qquad
t=\sqrt{4(1+\gamma)h^2-1},
\]
and
\[
w=\frac{t}{\sqrt{1+t^2}}
=
\frac{\sqrt{4(1+\gamma)h^2-1}}
{2\sqrt{1+\gamma}\,h}.
\]
The root with imaginary numerator \(-2h-t\) is dominant. Simplifying its squared modulus gives
\[
\rho_\gamma(h)^2
=
\frac{1}
{\gamma+2-2\sqrt{\gamma+1}\,w}.
\]
Here \(w\) strictly increases from \(0\) to \(1\), so this expression strictly increases with \(h\). The unique global minimum is therefore at
\[
\Delta=0,\qquad
h=\frac1{2\sqrt{1+\gamma}},
\]
and substitution yields
\[
\rho_\gamma(h)^2=\frac1{\gamma+2}.
\]

At the minimizing step the characteristic polynomial has a repeated root
\[
r_c=
\frac{1-2ih_{\rm opt}}
{2(1+i\gamma h_{\rm opt})}.
\]
The associated two-step companion matrix is not a scalar matrix, so the repeated eigenvalue is defective. Generic scalarized iterates therefore have the form
\[
z_k=(c_1+c_2 k)r_c^k.
\]
Thus \(1/\sqrt{\gamma+2}\) is the asymptotic root factor, but the exactly optimal step carries the usual polynomial \(k\) transient of a \(2\times2\) Jordan block.

For \(\gamma=-1\), the factor \(r=1\) can be checked directly. For \(\gamma<-1\), the discriminant is positive for every \(h\) and
\[
u=\sqrt{1+4(-1-\gamma)h^2}.
\]
The same algebra gives
\[
\rho_\gamma(h)^2
=
\frac{1+u}{\gamma+2-\gamma u}.
\]
Now
\[
\frac{d}{du}\rho_\gamma(h)^2
=
\frac{2(\gamma+1)}
{(\gamma+2-\gamma u)^2}<0,
\]
while \(u\) increases with \(h\), proving strict decrease. Finally \(u\sim2\sqrt{-1-\gamma}\,h\), so
\[
\rho_\gamma(h)^2\to-\frac1\gamma.
\]

## Consequences for the sharp stability family

For \(0\le\gamma<3\), the recent sharp stability threshold is
\[
h_{\rm stab}
=
\frac1{\sqrt{(1+\gamma)(3-\gamma)}}.
\]
The rate-optimal step satisfies
\[
\boxed{
\frac{h_{\rm opt}}{h_{\rm stab}}
=
\frac{\sqrt{3-\gamma}}2.
}
\]
Hence maximizing the stable step and minimizing the asymptotic contraction factor are distinct objectives.

For the matched-skew instance \(\gamma=1\),
\[
h_{\rm stab}=\frac12,\qquad
h_{\rm opt}=\frac1{2\sqrt2},\qquad
\rho_{\rm opt}=\frac1{\sqrt3}.
\]
The sharp stability boundary itself is nonconvergent. Just below it the spectral radius tends to \(1\), so a step close to the largest stable value can be arbitrarily slower asymptotically than the rate-optimal step.

For \(\gamma\ge3\), the same recent stability analysis shows convergence for every finite \(h>0\), but the fastest step is still finite:
\[
h_{\rm opt}
=
\frac1{2\sqrt{1+\gamma}}.
\]
For \(\gamma>0\),
\[
\lim_{h\to\infty}\rho_\gamma(h)
=
\frac1{\sqrt{\gamma+1}-1},
\]
which is strictly larger than \(1/\sqrt{\gamma+2}\). Unbounded stability therefore does not imply that arbitrarily large steps improve the asymptotic rate.

## Relation to prior work and originality boundary

Shehu, arXiv:2609.18373v1, derives the exact stability threshold for the skew family and a broader normal-operator phase diagram. Its displayed spectral-radius curves motivate the rate question, but the paper's stated results concern stability boundaries. It explicitly notes that earlier tight rate results concern the \(A=0\) case.

The \(\gamma=0\) specialization
\[
h_{\rm opt}=\frac12,\qquad
\rho_{\rm opt}=\frac1{\sqrt2}
\]
is prior work: Malitsky--Tam's FRB rotation example is cited for that rate, and Soe--Vetrivel--Yao, arXiv:2509.02005, use it as the tight FRB benchmark for generalized FRB. No novelty is claimed for that special case.

The contribution claimed here is the exact \(\gamma\)-dependent rate phase diagram for the pure-skew family: the closed spectral-radius formulas, the unique finite optimum for every \(\gamma>-1\), the defective critical-discriminant characterization, the finite-optimum versus unbounded-stability separation, and the monotone infinite-step regime for \(\gamma<-1\). To the best of our knowledge, these statements are not given in the inspected prior sources.

## Computational model and limitations

The result concerns exact arithmetic and fixed scalar step sizes for the two-dimensional linear family \(A=\gamma LJ\), \(B=LJ\). The objective is the asymptotic spectral radius of the induced two-step linear recurrence. It does not assert that the same step is rate-optimal for general monotone inclusions, nonlinear operators, variable-step methods, finite-horizon error, or finite-precision implementations.

At \(h_{\rm opt}\) for \(\gamma>-1\), the repeated root is defective. Consequently, although the spectral radius is minimal, generic trajectories have a polynomial \(k\) prefactor. A slightly off-critical step can therefore outperform the exact minimizer over a prescribed short horizon even while having a larger asymptotic root factor.

## Reproducibility

`artifacts/verify_frb_skew_rate.py` evaluates the characteristic roots directly in complex arithmetic and compares them with the closed formulas for representative \(\gamma\). It also checks the matched-skew instance and the \(\gamma<-1\) limiting regime. `artifacts/verification_output.txt` contains the corresponding output.

## References

1. Y. Shehu, *The sharp step-size constant for one-call reflection splittings on monotone inclusions*, arXiv:2609.18373v1, 2026. https://arxiv.org/abs/2609.18373
2. S. Soe, V. Vetrivel, J.-C. Yao, *On Generalized Forward-Reflected-Backward Method for Monotone Inclusion Problems*, arXiv:2509.02005, 2025. https://arxiv.org/abs/2509.02005
3. Y. Malitsky, M. K. Tam, *A forward-backward splitting method for monotone inclusions without cocoercivity*, SIAM Journal on Optimization 30(2), 1451--1472, 2020.
4. V. Cevher, B. C. Vũ, *A reflected forward-backward splitting method for monotone inclusions involving Lipschitzian operators*, Set-Valued and Variational Analysis 29(1), 163--174, 2021.
