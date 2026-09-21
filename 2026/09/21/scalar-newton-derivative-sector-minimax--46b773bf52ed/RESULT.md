# Sharp minimax relaxation frontier for scalar Newton under derivative-sector bounds

## Setting

Let \(f:\mathbb R\to\mathbb R\) be continuously differentiable, let \(x_*\) be a root, and assume the global derivative-sector bounds
\[
0<m\le f'(x)\le L<\infty\qquad(x\in\mathbb R).
\]
Then the root is unique. Write \(\kappa=L/m\ge1\). Consider the constant-relaxation Newton step
\[
x_+=x-\gamma\frac{f(x)}{f'(x)},\qquad \gamma>0.
\]
The norm is absolute value and arithmetic is exact.

## Exact one-step error envelope

For every nonroot state \(x\), define the secant slope to the root
\[
a(x)=\frac{f(x)-f(x_*)}{x-x_*}.
\]
The fundamental theorem of calculus gives \(a(x)\in[m,L]\). With \(d=f'(x)\in[m,L]\),
\[
\frac{x_+-x_*}{x-x_*}=1-\gamma\frac{a(x)}{d}.
\]
Consequently
\[
\boxed{
\sup_{f,x\ne x_*}\frac{|x_+-x_*|}{|x-x_*|}
=
W_\gamma(\kappa)
:=\max\left\{\left|1-\frac{\gamma}{\kappa}\right|,\left|1-\gamma\kappa\right|\right\}.
}
\]
The supremum ranges over all continuously differentiable functions satisfying the derivative-sector bounds and possessing a root.

### Sharpness

The two endpoint ratios are attainable in the closure of this class. After translating and scaling, take \(x_*=0\), \(x=1\), and \(m=1\). To approach \(a/d=\kappa\), let \(f'\) equal \(L\) on \([0,1-\varepsilon]\), decrease linearly from \(L\) to \(m\) on \([1-\varepsilon,1]\), and extend continuously while preserving \([m,L]\). Then
\[
a=L-\frac{L-m}{2}\varepsilon,\qquad d=m,
\]
so \(a/d\to\kappa\). Reversing \(m\) and \(L\) gives \(a/d\to1/\kappa\). Thus no smaller uniform factor is possible.

## Optimal constant damping

Minimizing the exact envelope over \(\gamma>0\) gives the unique minimizer
\[
\boxed{\gamma_* = \frac{2\kappa}{\kappa^2+1}}
\]
and the exact minimax factor
\[
\boxed{
W_*(\kappa)=\frac{\kappa^2-1}{\kappa^2+1}.
}
\]
Equioscillation occurs between the two limiting sector ratios \(1/\kappa\) and \(\kappa\). Since \(\gamma_*\le1\), this optimum lies within the usual under-relaxed Newton range.

For a fixed constant \(\gamma\), a uniform linear contraction over the whole class holds exactly when
\[
0<\gamma<\frac{2}{\kappa}.
\]
The sufficient part is immediate from the exact envelope. Sharpness follows from the boundary-layer witnesses above.

## The undamped Newton threshold is sharp, including the boundary

For \(\gamma=1\),
\[
\boxed{W_1(\kappa)=\kappa-1.}
\]
Hence \(\kappa<2\) gives a uniform global linear contraction. The strict condition \(\gamma<2m/L\) is consistent with existing global convergence theorems for damped Newton methods on strongly monotone Lipschitz operator equations; the new point here is the exact scalar error envelope and its sharp boundary behavior.

At the boundary \(\kappa=2\), the supremum is one but every individual nonroot Newton step still strictly decreases the root error. Indeed, equality \(a/d=2\) would require simultaneously \(a=L\) and \(d=m\). Since \(f'\) is continuous and bounded above by \(L=2m\), the equality \(a=L\) forces \(f'\equiv L\) on the segment joining \(x_*\) to \(x\), contradicting \(d=m\). Therefore
\[
|x_+-x_*|<|x-x_*|\quad\text{for every }x\ne x_*.
\]
The errors decrease monotonically. If their limit were positive, compactness and continuity of the Newton map would produce a nonroot limit point with equality of successive error magnitudes, a contradiction. Thus undamped Newton converges globally for every start also at \(\kappa=2\), although no uniform linear factor below one exists.

For every \(\kappa>2\), this boundary is sharp even for a smooth monotone geometry in the following strong sense: there exists a continuously differentiable odd \(f\) with \(m\le f'\le L\) whose Newton map has the exact two-cycle \(1\leftrightarrow-1\).

Set \(m=1\) by scaling. Choose
\[
0<\varepsilon<\min\left\{1,\frac{2(\kappa-2)}{\kappa-1}\right\},
\qquad
C=\frac{4-\varepsilon}{2-\varepsilon}<\kappa.
\]
Define an even continuous derivative \(h\) by \(h(t)=C\) for \(|t|\le1-\varepsilon\), linearly decrease it to \(1\) on \([1-\varepsilon,1]\), reflect evenly, and set \(h(t)=1\) for \(|t|\ge1\). Let
\[
f(x)=\int_0^x h(t)\,dt.
\]
Then \(1\le f'\le C<L\), while
\[
\int_0^1h(t)\,dt
=C\left(1-\frac\varepsilon2\right)+\frac\varepsilon2=2.
\]
Hence \(f(1)=2\), \(f'(1)=1\), and oddness gives
\[
N(1)=-1,\qquad N(-1)=1.
\]
Thus no global-convergence theorem for undamped Newton can hold over the entire derivative-sector class once \(\kappa>2\).

## A stronger minimax statement: local derivative information can be useless

Consider the larger one-step family
\[
x_+=x-\Gamma(f'(x))\frac{f(x)}{f'(x)},
\]
where the scalar relaxation rule \(\Gamma:[m,L]\to\mathbb R\) may use the current derivative and the known sector endpoints, but no additional information about the function away from the current point.

For any endpoint derivative \(d\in[m,L]\), continuous derivative profiles can make the root secant slope \(a\) approach any value in \([m,L]\). Hence the exact minimax problem is
\[
\inf_\Gamma\sup_{d\in[m,L]}\sup_{a\in[m,L]}
\left|1-\Gamma(d)\frac{a}{d}\right|.
\]
For fixed \(d\), writing \(s=\Gamma(d)/d\) reduces this to the classical two-endpoint Chebyshev problem
\[
\min_s\max\{|1-sm|,|1-sL|\},
\]
whose unique minimizer is \(s=2/(m+L)\). Therefore
\[
\boxed{
\inf_\Gamma\sup_{f,x\ne x_*}
\frac{|x_+-x_*|}{|x-x_*|}
=\frac{L-m}{L+m}
=\frac{\kappa-1}{\kappa+1}.
}
\]
The unique pointwise minimax rule is
\[
\boxed{\Gamma_*(d)=\frac{2d}{m+L}.}
\]
It cancels the Newton denominator exactly:
\[
x_+=x-\frac{2}{m+L}f(x).
\]
Thus, under derivative-sector information alone, allowing a relaxation parameter to depend on the exact local derivative provides no minimax advantage over the standard optimally tuned fixed-slope iteration; the robust optimum discards the local derivative. In contrast, restricting to a single constant Newton damping incurs the larger exact factor
\[
\frac{\kappa^2-1}{\kappa^2+1}>\frac{\kappa-1}{\kappa+1}
\qquad(\kappa>1).
\]

## Relation to prior work

Ortega and Rheinboldt's classical monograph surveys Newton, relaxed iterative processes, contraction arguments, and convergence theory for nonlinear equations. The Newton--Kantorovich literature, including sharp majorant/error-bound work of Gragg--Tapia and Potra--Ptak, treats substantially different semilocal hypotheses involving derivative variation relative to a starting point.

Heid (2023) studies damped Newton methods for strongly monotone and Lipschitz continuous operator equations. Under additional structural assumptions, its Theorem 2.1 guarantees convergence when the damping is bounded above by a constant strictly below \(2\alpha_{F'}/L\). In the present scalar derivative-sector class this becomes \(\gamma<2m/L=2/\kappa\). Accordingly, the sufficient global-convergence inequality itself is prior coverage and is not claimed as new here. The contribution is the exact scalar root-error envelope, its sharp limiting constructions, the \(\kappa=2\) boundary behavior and \(\kappa>2\) exact two-cycle, the optimal constant factor, and the derivative-aware minimax collapse to the fixed-slope iteration.

Polyak and Tremba (2020) develop Newton/damped-Newton hybrids with adaptive step-size choices and global convergence domains, including one-dimensional specializations. Their objectives and assumptions differ from the derivative-sector minimax problem above; no checked theorem states the exact formulas here.

## Reproducibility and limitations

The proof is analytic. A compact deterministic script checks the closed-form factors, boundary-layer sharpness, explicit two-cycle construction, and derivative-aware minimax formula on representative parameter values.

Limitations:

- Scalar real equations only; no vector or Banach-space minimax claim is made.
- Global \(C^1\) derivative-sector bounds and existence of a root are assumed.
- The factors concern root error in absolute value, not residual decrease or floating-point behavior.
- The derivative-aware minimax statement is for memoryless multiplicative relaxation depending on the current derivative and known \(m,L\); richer history-dependent or line-search algorithms are outside the claim.
- The exact formulas are elementary enough that an equivalent statement may exist in older nonlinear-equation or relaxation literature under different terminology; the classical monographs and pre-digital literature remain the principal originality risk.

## References

1. J. M. Ortega and W. C. Rheinboldt, *Iterative Solution of Nonlinear Equations in Several Variables*, Academic Press, 1970; SIAM Classics reprint, 2000. https://doi.org/10.1137/1.9780898719468
2. W. B. Gragg and R. A. Tapia, "Optimal Error Bounds for the Newton--Kantorovich Theorem," *SIAM Journal on Numerical Analysis* 11 (1974), 10--13. https://doi.org/10.1137/0711002
3. F. A. Potra and V. Ptak, "Sharp error bounds for Newton's process," *Numerische Mathematik* 34 (1980), 63--72. https://doi.org/10.1007/BF01463998
4. B. Polyak and A. Tremba, "New versions of Newton method: step-size choice, convergence domain and under-determined equations," *Optimization Methods and Software* 35 (2020), 1272--1303. https://doi.org/10.1080/10556788.2019.1669154
5. P. Heid, "A short note on an adaptive damped Newton method for strongly monotone and Lipschitz continuous operator equations," *Archiv der Mathematik* 121 (2023), 55--65. https://doi.org/10.1007/s00013-023-01858-x
