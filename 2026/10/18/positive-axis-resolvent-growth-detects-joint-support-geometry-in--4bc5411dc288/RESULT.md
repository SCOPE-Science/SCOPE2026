# Positive-axis resolvent growth detects joint support geometry in tensor Volterra operators

## Finding

For each fixed integer \(d\ge2\), define the Volterra integration operator \(V\) on \(L^2([0,1])\) and its Hilbert tensor power \(T_d\) by
\[
(Vg)(x)=\int_0^x g(t)\,dt,\qquad
(T_df)(x)=\int_0^{x_1}\cdots\int_0^{x_d}f(t)\,dt_d\cdots dt_1.
\]
For nonzero, almost-everywhere nonnegative real \(f\in L^2([0,1]^d)\), put
\[
\rho_f=\operatorname*{ess\,sup}_{\{t:f(t)>0\}}\prod_{j=1}^d(1-t_j).
\]
This lies in \((0,1]\). Let \(R_\lambda=(\lambda I-T_d)^{-1}\) for positive **real** \(\lambda\). Then both ordinary limits exist and are
\[
\boxed{\lim_{\lambda\downarrow0}\lambda^{1/d}\log\|R_\lambda f\|_2
=d\rho_f^{1/d},\qquad
\lim_{\lambda\downarrow0}\lambda^{1/d}\log\|R_\lambda\|_{2\to2}=d.}
\]
In particular, the positive-axis relative logarithmic growth invariant is
\[
\boxed{\lim_{\lambda\downarrow0}\frac{\log\|R_\lambda f\|_2}{\log\|R_\lambda\|_{2\to2}}=\rho_f^{1/d}.}
\]
It depends on the **joint** essential support, not just the individual coordinate-marginal supports.

## Assumptions and scope

All spaces are complex Hilbert spaces, while the measured input \(f\) is real-valued and nonnegative almost everywhere. The dimension \(d\) is any fixed integer at least two. The expression for \(\rho_f\) takes the essential supremum on the measurable set where \(f\) is strictly positive. The parameter approaches zero through positive real numbers only. No assertion is made about arbitrary complex parameter directions or signed/complex-valued \(f\).

For \(0<\varepsilon<1/2\), let \(\mathbf1_E\) denote the indicator of a measurable set and define, in two dimensions,
\[
E_{\rm cross}=([0,\varepsilon]\times[1-\varepsilon,1])\cup([1-\varepsilon,1]\times[0,\varepsilon]),
\]
\[
E_{\rm diag}=([0,\varepsilon]\times[0,\varepsilon])\cup([1-\varepsilon,1]\times[1-\varepsilon]).
\]
Both sets project onto exactly the same coordinate supports in either direction, yet
\[
\rho_{\mathbf1_{E_{\rm cross}}}=\varepsilon,\qquad
\rho_{\mathbf1_{E_{\rm diag}}}=1.
\]
Thus their normalized positive-axis local resolvent indicators are \(\sqrt\varepsilon\) and \(1\), respectively. This distinction cannot be inferred from separate one-variable support left endpoints.

## Proof

**1. Power bounds, quasinilpotence, and the entire scalar kernel.** For \(n\ge1\), the kernel of \(V^n\) is
\[
K_n(x,t)=\frac{(x-t)^{n-1}}{(n-1)!}\mathbf1_{0\le t\le x}.
\]
Its row and column integrals do not exceed \(1/n!\), so Schur's test gives \(\|V^n\|_{2\to2}\le1/n!\). Since \(T_d^n=(V^n)^{\otimes d}\),
\[
\|T_d^n\|_{2\to2}\le (n!)^{-d}.
\]
Therefore \(T_d\) is quasinilpotent, and the norm-convergent Neumann resolvent expansion is valid at every nonzero \(\lambda\). Introduce
\[
E_d(z)=\sum_{n=0}^{\infty}\frac{z^n}{(n!)^d}\quad(z\ge0).
\]
For \(z\ge0\), compare the diagonal terms of the product of \(d\) exponential series to obtain
\[
E_d(z)\le\exp(dz^{1/d}).
\]
For \(z\ge1\), taking the single term at \(n=\lfloor z^{1/d}\rfloor\) and applying elementary Stirling bounds yields
\[
\log E_d(z)\ge dz^{1/d}-O_d(\log(z+2)).
\]
Consequently \(\log E_d(z)/z^{1/d}\to d\) as \(z\to\infty\).

**2. A positive resolvent kernel.** Summing the integral kernels of the powers with nonnegative coefficients gives, for almost every \(x\in[0,1]^d\),
\[
(R_\lambda f)(x)=\lambda^{-1}f(x)+\lambda^{-2}
\int_{\{0\le t_j\le x_j\ \forall j\}}
E_d\left(\frac{\prod_{j=1}^d(x_j-t_j)}{\lambda}\right)f(t)\,dt.
\]
Indeed, the coefficient of the \(n\)-th Volterra power has product kernel \(\prod_j(x_j-t_j)^{n-1}/((n-1)!)^d\). The formula is justified by norm convergence and monotone convergence for nonnegative \(f\). It also extends by absolute convergence to general \(L^2\) inputs, although positivity will be used in what follows.

**3. Exact operator growth.** The power bounds imply
\[
\|R_\lambda\|\le\lambda^{-1}E_d(1/\lambda),
\]
so the upper rate is at most \(d\). Let \(\mathbf1\) be the constant function on the unit cube, whose norm is one. The power identity \(T_d^n\mathbf1(x)=\prod_jx_j^n/(n!)^d\) yields
\[
R_\lambda\mathbf1(x)=\lambda^{-1}E_d\left(\frac{\prod_jx_j}{\lambda}\right).
\]
For every \(\delta\in(0,1)\), its \(L^2\) norm on \([1-\delta,1]^d\) is at least
\[
\delta^{d/2}\lambda^{-1}E_d((1-\delta)^d/\lambda).
\]
The resulting lower rate is \(d(1-\delta)\); letting \(\delta\downarrow0\) proves the operator formula.

**4. Exact local growth for positive vectors.** By the definition of \(\rho_f\), for almost every \(t\) with \(f(t)>0\) and each \(t_j\le x_j\le1\),
\[
\prod_j(x_j-t_j)\le\prod_j(1-t_j)\le\rho_f.
\]
Since \(\|f\|_1\le\|f\|_2\) on the unit cube, the kernel formula and scalar monotonicity give the pointwise bound on the integral term \(\lambda^{-2}E_d(\rho_f/\lambda)\|f\|_1\). Together with the explicit \(\lambda^{-1}f\) term, this proves
\[
\limsup_{\lambda\downarrow0}\lambda^{1/d}\log\|R_\lambda f\|_2\le d\rho_f^{1/d}.
\]
For the reverse estimate fix \(\eta\in(0,\rho_f/3)\). By the essential-supremum definition and \(f\ge0\), there are \(c>0\) and a measurable set \(F\) of positive measure with
\[
f(t)\ge c,\qquad\prod_j(1-t_j)>\rho_f-\eta\quad(t\in F),
\]
up to null sets. Since every factor is at most one, the product condition implies \(1-t_j>\rho_f-\eta\) for each coordinate. Select a fixed \(\delta>0\) such that \(\delta<\rho_f-\eta\) and \(d\delta<\eta\). For every \(x\in[1-\delta,1]^d\) and \(t\in F\), we have \(t_j\le x_j\), and telescoping products of factors in \([0,1]\) yields
\[
\prod_j(x_j-t_j)\ge\prod_j(1-t_j)-d\delta>\rho_f-2\eta.
\]
The positive kernel therefore satisfies on that output cube
\[
(R_\lambda f)(x)\ge c|F|\lambda^{-2}E_d((\rho_f-2\eta)/\lambda).
\]
Taking the \(L^2\) norm over the output cube, then the positive-axis exponential rate, shows the lower bound \(d(\rho_f-2\eta)^{1/d}\). Let \(\eta\downarrow0\). This proves the first claimed limit. Division by the operator limit proves the relative indicator formula.

**5. Marginal indistinguishability.** For the cross-rectangle input, the maximum of the product \(\prod_j(1-t_j)\) on its support is \(\varepsilon\). For the diagonal-rectangle input, one component touches the origin and the essential supremum is one. Both coordinate projections coincide, so the claimed difference follows from step 4.

## Verification

The analytic certificate consists of the explicit power kernels, Schur's test, the two-sided exponential-type estimate for \(E_d\), and the matching support-localized resolvent bounds. Their inequalities are valid for all \(d\ge2\), all admissible positive inputs, and all sufficiently small positive \(\lambda\); no finite test is substituted for these quantifiers.

A standalone standard-library checker, `check_resolvent.py`, verifies finite scalar-kernel inequalities and evaluates exact rectangle-power series for a cross/diagonal comparison. It reports 42 finite diagnostics. Its outputs are illustrative convergence checks, not infinite proofs.

## Relationship to prior work

Ji and Zhang [2] compute the full complex-plane resolvent power set of the **one-variable** Volterra operator and analyze support-interval witnesses. Hu, Ji, and Liang [1] prove a universal power-set inclusion and give operator realizations of prescribed right-closed sets. Neither cited source states the positive-real-axis exponential-type formula for \(V^{\otimes d}\) on arbitrary nonnegative multivariate inputs, nor its dependence on joint rather than marginal support. The present formula is a different invariant from the full complex-plane limsup defining the classical power set; it does not purport to calculate that full invariant.

The proof relies on standard Schur estimates, Stirling bounds, and positivity. Its specialized contribution is the exact support-geometric classification of the positive cone for every tensor dimension, including correlated inputs not reducible to elementary tensors.

## Limitations

The positive-input hypothesis is essential to the lower-bound argument; cancellation for signed or complex inputs has not been analyzed. The positive-axis formula alone does not classify the ordinary complex-plane power set, establish norm rates on arbitrary rays, or imply new invariant-subspace results. The tensor dimension is fixed and finite. No claim is made about a full operator asymptotic equivalent beyond its leading exponential type. The literature comparison does not exclude all possible earlier formulations in general positive-kernel Laplace principles; publication priority requires independent assessment.

## References

[1] C. L. Hu, Y. Q. Ji, D. H. Liang, *On the Power Set of Quasinilpotent Operators in Banach Spaces*, arXiv:2607.01614v1, first public July 2, 2026; Theorems 1.4 and 1.6.

[2] Y. Ji, Y. Zhang, *On the power set of quasinilpotent operators*, arXiv:2305.09963v1, first public May 17, 2023; Theorem C and Proposition 4.14.
