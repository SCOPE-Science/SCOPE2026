# Two-defect bound-state threshold and separation scaling on a finite cycle

## Finding

Let \(C_N\) be the cycle with \(N\ge3\) vertices, let \(H_0\) be its nearest-neighbour adjacency operator with unit hopping, and define
\[
H_N=H_0+V\bigl(|0\rangle\langle0|+|d\rangle\langle d|\bigr),
\qquad V>0,
\]
where \(d\in\{1,\ldots,N-1\}\). The unperturbed band is \([-2,2]\). There is exactly one eigenvalue strictly above \(2\) for every \(V>0\), and a second eigenvalue strictly above \(2\) if and only if
\[
V>V_c(N,d):=\frac{2N}{d(N-d)}.
\]
At equality, the second branch is at \(E=2\). No eigenvalue is pushed below \(-2\) by this positive perturbation.

If \(d_N/N\to\rho\in(0,1/2]\) and \(V_N=\lambda/N\), then for fixed \(\lambda>0\) away from the critical value the number of eigenvalues above \(2\) is two when
\[
\lambda>\lambda_c(\rho):=\frac{2}{\rho(1-\rho)},
\]
and one when \(\lambda<\lambda_c(\rho)\). At equality, the limiting scaling alone does not determine the finite-size count. For every branch that exists above \(2\), its scaled energy has a limit
\[
N^2(E_{\pm,N}-2)\longrightarrow y_\pm^2,
\]
where \(y_+>0\) is the unique solution of \(\lambda=\Psi_+(y;\rho)\), and \(y_->0\) is the unique solution of \(\lambda=\Psi_-(y;\rho)\) when \(\lambda>\lambda_c(\rho)\), with
\[
\Psi_\pm(y;\rho)=\frac{2y\sinh(y/2)}{\cosh(y/2)\pm\cosh((1/2-\rho)y)}.
\]
The plus and minus signs correspond respectively to symmetric and antisymmetric defect channels. For antipodal defects, \(\rho=1/2\), the limiting equations reduce to \(\lambda=2y_+\tanh(y_+/4)\) and \(\lambda=2y_-\coth(y_-/4)\), and the second-mode threshold is \(\lambda_c=8\).

## Assumptions and scope

The operator acts on \(\mathbb C^N\), with \((H_0\psi)_j=\psi_{j-1}+\psi_{j+1}\) and indices modulo \(N\). The two defects are distinct, have the same positive on-site potential \(V\), and the hopping amplitude is normalized to one. By cycle symmetry, the separation can be replaced by \(\min(d,N-d)\), so the scaling parameter may be taken in \(\rho\in(0,1/2]\). The result concerns eigenvalues above the infinite-chain band edge \(2\); it does not classify resonances inside the finite-cycle band, negative defects, unequal defect strengths, disorder, or interacting particles.

## Proof

For \(E=2\cosh\kappa>2\), \(\kappa>0\), the resolvent kernel of the unperturbed cycle is
\[
G_{0j}(E)=\langle0|(E-H_0)^{-1}|j\rangle
=\frac{\cosh((N/2-j)\kappa)}{2\sinh\kappa\,\sinh(N\kappa/2)},
\qquad 0\le j\le N.
\]
This follows by periodizing the infinite-line kernel \(e^{-\kappa|j|}/(2\sinh\kappa)\). Write \(g_0=G_{00}(E)\) and \(g_d=G_{0d}(E)\). The finite-rank determinant identity reduces the eigenvalue equation outside the band to
\[
(1-V(g_0+g_d))(1-V(g_0-g_d))=0.
\]
The two factors are the resolvent quadratic forms for the normalized symmetric and antisymmetric vectors supported at \(0,d\). Each is positive and strictly decreasing as a function of \(E>2\), because the derivative of \((E-H_0)^{-1}\) is \(-(E-H_0)^{-2}\).

As \(E\downarrow2\), equivalently \(\kappa\downarrow0\), the symmetric form diverges. The antisymmetric form has the finite limit
\[
\begin{aligned}
\lim_{\kappa\downarrow0}(g_0-g_d)
&=\lim_{\kappa\downarrow0}
\frac{\cosh(N\kappa/2)-\cosh((N/2-d)\kappa)}
{2\sinh\kappa\,\sinh(N\kappa/2)}\\
&=\frac{d(N-d)}{2N}.
\end{aligned}
\]
Both forms tend to zero as \(E\to\infty\). Therefore the symmetric equation has exactly one root above \(2\) for every \(V>0\), while the antisymmetric equation has exactly one such root precisely when \(Vd(N-d)/(2N)>1\). At equality the antisymmetric branch reaches \(E=2\). Since the perturbation is positive semidefinite and has rank two, there are no eigenvalues below \(-2\) and at most two above \(2\); this proves the exact count and threshold.

For the scaling limit, put \(d=d_N\), \(V_N=\lambda/N\), and \(\kappa_N=y_N/N\). Substituting the kernel into the two secular equations gives the finite-size relations
\[
\lambda=\frac{2N\sinh(y_N/N)\sinh(y_N/2)}
{\cosh(y_N/2)\pm\cosh((1/2-d_N/N)y_N)}.
\]
On every compact positive \(y\)-interval, the right-hand side converges uniformly to \(\Psi_\pm(y;\rho)\). The symmetric limiting branch increases from \(0\) to infinity. The antisymmetric branch increases from \(2/[\rho(1-\rho)]\) to infinity. Monotonicity follows from the resolvent quadratic-form monotonicity above and analyticity of the limiting expressions. Hence the stated roots are unique whenever they exist, and the finite-size roots converge to them for fixed \(\lambda\) strictly away from the threshold. Finally, \(E_{\pm,N}=2\cosh(y_{\pm,N}/N)\), so \(N^2(E_{\pm,N}-2)\to y_\pm^2\). The exact finite-size threshold satisfies \(NV_c(N,d_N)=2N^2/[d_N(N-d_N)]\to\lambda_c(\rho)\), giving the mode-count statement away from equality.

## Verification

The analytic proof establishes the count, exact threshold, and scaling equations. The standalone checker `CHECKER.py` verifies the resolvent kernel against its Fourier sum for several finite cycles, checks the antisymmetric threshold limit using a cancellation-stable identity, and checks convergence of both scaled branches for increasing cycle sizes. It reports 40 passing numerical checks. These finite checks corroborate the algebra but are not used as a proof of the all-\(N\) theorem or the limiting statements.

## Relationship to prior work

Joglekar, Scott, Babbey, and Saxena study two parity-time-symmetric *imaginary* impurities on an *open* tight-binding chain and report a separation-dependent critical scale proportional to \(1/N\). Their Hamiltonian, boundary conditions, and transition are different: they concern complex eigenvalue formation, not the number of real eigenvalues above the band for two equal positive defects on a periodic cycle. Bierman studies a dilute many-impurity crystal and impurity-band formation, but the accessible abstract does not state the finite-cycle threshold or the separation-fraction scaling function proved here. The literature search found no directly matching formula; this is a best-knowledge assessment, not proof that no equivalent result exists.

## Limitations

The claim assumes equal positive defects, a cycle, nearest-neighbour hopping, and one-particle dynamics. The limiting count at exactly \(\lambda=\lambda_c(\rho)\) depends on the finite-size approach of \(d_N/N\) and is intentionally left unclassified. The finite-size formula is exact, while the scaling statement assumes \(d_N/N\to\rho\in(0,1/2]\) and fixed \(\lambda\); it does not cover a separation that remains bounded as \(N\to\infty\). The numerical checker is not an independent proof or an exhaustive computational certification.

## References

1. Y. N. Joglekar, D. Scott, M. Babbey, and A. Saxena, “Robust and fragile PT-symmetric phases in a tight-binding chain,” *Physical Review A* **82** (2010), 030103; arXiv:1008.2968. The full text was inspected for its model, secular equation, and stated \(1/N\) critical scaling.
2. A. Bierman, “Statistical Theory of Localized States of a Many-Impurity Crystal,” *Physical Review B* **1** (1970), 3402–3408, DOI: 10.1103/PhysRevB.1.3402. The accessible abstract describes impurity-band formation in a dilute many-impurity model; the full text was not available in this run.
