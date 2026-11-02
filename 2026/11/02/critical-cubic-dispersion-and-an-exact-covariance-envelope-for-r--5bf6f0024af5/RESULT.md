# Critical cubic dispersion and an exact covariance envelope for repulsive delayed diffusion

## Finding

For the critical *linear* Langevin delay equation
\[
dX_t=\tau^{-1}(X_t-X_{t-\tau})\,dt+\sqrt{2D}\,dW_t,
\qquad X_t=0\ ( -\tau\le t\le0),
\]
with any \(\tau,D>0\), the causal deterministic impulse response \(R\) obeys the **global sharp envelope**
\[
\frac{2t}{\tau}\le R(t)\le\frac{2t}{\tau}+1\qquad(t\ge0).
\]
The additive upper constant 1 is the smallest constant valid simultaneously for all \(t\ge0\). In particular, \(R(t)/t\to2/\tau\).

For every \(0\le s\le t\), define the integrated-Brownian covariance
\[
G(s,t)=\frac{8D}{\tau^2}\int_0^s(s-u)(t-u)\,du.
\]
The exact position covariance has the **two-time, all-lag quantitative comparison**
\[
0\le\operatorname{Cov}(X_s,X_t)-G(s,t)
\le \frac{4Dst}{\tau}+2Ds.
\]
In particular, for every \(t\ge0\),
\[
\frac{8D}{3\tau^2}t^3\le\operatorname{Var}(X_t)
\le\frac{8D}{3\tau^2}t^3+\frac{4D}{\tau}t^2+2Dt,
\qquad \lim_{t\to\infty}\frac{\operatorname{Var}(X_t)}{t^3}=\frac{8D}{3\tau^2}.
\]

The known second-order uniform-renewal asymptotic \(R(t)=2t/\tau+2/3+o(1)\) also sharpens this to
\[
\operatorname{Var}(X_t)=\frac{8D}{3\tau^2}t^3+\frac{8D}{3\tau}t^2+o(t^2).
\]

Moreover, for every \(H>0\), the rescaled continuous process \((T^{-3/2}X_{Tt})_{0\le t\le H}\) converges in distribution in \(C([0,H])\) as \(T\to\infty\) to the integrated Brownian motion
\[
Z_t=\frac{2\sqrt{2D}}{\tau}\int_0^t(t-u)\,dB_u.
\]
There is a canonical coupling (using the same Brownian motion for the rescaled process and \(Z\)) with the **finite-scale pointwise \(L^2\) bound**
\[
\mathbb E\bigl|Z_T(t)-Z_t\bigr|^2\le\frac{2Dt}{T^2}\qquad(0\le t\le H),
\]
where \(Z_T\) has the same path law as \(T^{-3/2}X_{T\cdot}\). The bound is uniform over the feedback delay and requires no small-delay limit. In this specific coupling the rate has the exact leading constant
\[
\lim_{T\to\infty} T^2\mathbb E|Z_T(t)-Z(t)|^2=\frac{8Dt}{9}\qquad(t>0),
\]
so the quadratic mean error rate is sharp as an order of approximation.

## Assumptions and scope

Here \(W\) and \(B\) are standard one-dimensional Brownian motions and \(D>0\) is the diffusion coefficient in the conventional \(\sqrt{2D}\) noise normalization. The history is deterministic and identically zero. The time delay \(\tau>0\) is fixed; the feedback coefficient is exactly \(1/\tau\). The causal response is defined by \(R(t)=0\) for \(t<0\), \(R(0)=1\), and \(R'(t)=\tau^{-1}[R(t)-R(t-\tau)]\) between switching times. The stochastic solution is the continuous variation-of-constants process \(X_t=\sqrt{2D}\int_0^t R(t-u)dW_u\). Equal claims hold componentwise for isotropic vector-valued Brownian forcing.

This equation is the small-displacement *linearization* of the repulsive Gaussian delayed-feedback force analyzed by Kopp and Klapp, with the physical parameter ratio \(A\tau/(\gamma b^2)=1\). No claim is made that the linear approximation remains accurate for arbitrarily large displacements in their *nonlinear* model.

## Proof

**1. Renewal representation and a sharp deterministic barrier.** Integrating the causal response equation, or taking its Laplace transform, gives
\[
R(t)=1+\frac1\tau\int_0^{\min(t,\tau)}R(t-u)\,du\qquad(t\ge0).
\]
To check the transform, for \(z>0\) the right side yields \(\widehat R(z)=[z-\tau^{-1}(1-e^{-\tau z})]^{-1}\). Uniqueness follows by the method of steps (or standard Volterra iteration).

Write \((\mathcal K f)(t)=1+\tau^{-1}\int_0^{\min(t,\tau)} f(t-u)du\), and set \(L(t)=2t/\tau\), \(U(t)=2t/\tau+1\). Direct integration for \(0\le t\le\tau\) gives
\[
(\mathcal KL)(t)-L(t)=(1-t/\tau)^2\ge0,\qquad
U(t)-(\mathcal KU)(t)=(t/\tau)(1-t/\tau)\ge0.
\]
For \(t\ge\tau\), both differences vanish identically. Since the integral kernel is nonnegative, its finite Picard iterations preserve these order inequalities. Iterating from either barrier converges locally uniformly to the unique Volterra solution: indeed, on each bounded time interval, differences between iterates are controlled by the usual factorial bound for successive Volterra convolution powers. Thus \(L\le R\le U\). Because \(R(0)=1\), the upper additive constant cannot be below 1, and division by \(t\) gives the exact asymptotic slope.

**2. The two-time covariance envelope.** The stochastic convolution and the Itô isometry imply
\[
\operatorname{Cov}(X_s,X_t)=2D\int_0^s R(s-u)R(t-u)\,du\qquad(0\le s\le t).
\]
By the nonnegative pointwise barrier, the product exceeds \(4(s-u)(t-u)/\tau^2\). It exceeds it by no more than \(2(s-u)/\tau+2(t-u)/\tau+1\), since \(R(v)\le2v/\tau+1\) for both arguments. Integration therefore bounds the difference by
\[
2D\int_0^s\left[\frac{2(s-u)}\tau+\frac{2(t-u)}\tau+1\right]du
=\frac{4Dst}{\tau}+2Ds.
\]
Setting \(s=t\) proves the variance inequalities and the cubic limit. The bound is global in time, not a fit to late-time data. For the second-order variance coefficient, apply the known nonarithmetic renewal expansion for uniform waiting times, \(R(v)=2v/\tau+2/3+o(1)\). Write \(e(v)=R(v)-2v/\tau\); it is uniformly bounded between zero and one. Expanding \(R(v)^2\), the cross term is \(4v e(v)/\tau\). The weighted Cesàro limit \(t^{-2}\int_0^t v e(v)dv\to1/3\) yields the displayed coefficient \(8D/(3\tau)\); the bounded-square contribution is at most linear in \(t\).

**3. Quantitative integrated-Brownian limit.** Brownian scaling shows that \(T^{-3/2}X_{Tt}\) has the law of
\[
Z_T(t)=\sqrt{2D}\int_0^t k_T(t-u)\,dB_u,\qquad
k_T(v)=T^{-1}R(Tv).
\]
The response barrier gives \(0\le k_T(v)-2v/\tau\le T^{-1}\). The Itô isometry on this coupling yields
\[
\mathbb E|Z_T(t)-Z(t)|^2
=2D\int_0^t[k_T(v)-2v/\tau]^2\,dv\le2Dt/T^2.
\]
Moreover, the known limit \(e(v)\to2/3\) for fixed \(v\to\infty\), together with \(0\le e\le1\), gives by dominated convergence
\[
T^2\mathbb E|Z_T(t)-Z(t)|^2
=2D\int_0^t e(Tv)^2dv\longrightarrow2Dt\cdot(2/3)^2=8Dt/9.
\]
Thus all finite-dimensional marginals converge to those of \(Z\).

For path-level tightness, \(R\) is globally Lipschitz with constant \(e/\tau\). Indeed on \([0,\tau)\), \(R'(v)=e^{v/\tau}/\tau\). For almost every \(v>\tau\),
\[
R'(v)=\frac1\tau\int_{v-\tau}^{v}R'(z)\,dz,
\]
so the derivative is a moving average of previously bounded derivatives and stays between zero and \(e/\tau\) by induction (the isolated switching points do not affect absolute continuity). Consequently the \(k_T\) are uniformly \(e/\tau\)-Lipschitz and bounded on each \([0,H]\). By splitting each stochastic convolution increment into the old-noise interval and the newly added interval, the Itô isometry gives \(\mathbb E|Z_T(t)-Z_T(s)|^2\le C_H|t-s|\) for \(0\le s,t\le H\) and \(T\ge1\). These centered Gaussian increments have fourth moments at most \(3C_H^2|t-s|^2\). Kolmogorov tightness in continuous-path space, together with finite-dimensional convergence, proves convergence in \(C([0,H])\).

## Verification

A standalone, standard-library-only checker is included at `checks/verify.py`. It independently evaluates the exact method-of-steps expression
\[
R(t)=\sum_{j=0}^{\lfloor t/\tau\rfloor}
\frac{(-1/\tau)^j}{j!}(t-j\tau)^j e^{(t-j\tau)/\tau},
\]
with the \(j=0\) term interpreted as 1 even at zero argument; it checks the response barriers over several delays, the delayed differential identity away from switching instants, and deterministic quadrature of the variance bound. It does **not** certify inequalities over uncountably many times, the process limit, or the originality claim: those require the proof and literature assessment above.

Run `python checks/verify.py` using the Python standard library. The numeric calculations use high-precision decimal arithmetic to avoid cancellation in the finite method-of-steps sum.

## Relationship to prior work

Kopp and Klapp (arXiv:2210.03182, 2022) introduce the Gaussian delayed-feedback model, its deterministic threshold, and numerical mean-squared displacement of the full nonlinear particle; their deterministic linear analysis supplies the relevant critical parameter. Kopp and Klapp (arXiv:2408.03316v1, August 6, 2024), Section III.1, examine steady-state heat and linearized delayed dynamics and explicitly discuss the nonstationarity of the position and the threshold. The results here are the separate all-time **critical stochastic positional covariance envelope**, cubic variance coefficient, and functional integrated-Brownian limit with an explicit coupling rate and its sharp asymptotic error constant. No general nonlinear long-time scaling is inferred.

The renewal-equation formulation, exact finite-sum uniform renewal function, and its asymptotic offset are *known*, not claimed as new: a 2021 Mathematics Stack Exchange discussion explicitly gives the same finite-sum expression and the asymptotic \(R(t)=2t/\tau+2/3+o(1)\) (after setting \(\tau=1\)), while Lototsky’s renewal notes state the basic renewal equation and asymptotic renewal law. The claim assessed here is the resulting physical critical **all-time stochastic covariance inequality and quantitative functional coupling**, not the underlying renewal representation or asymptotic response slope. Classical stochastic delay analysis and renewal equations provide relevant general tools. Lingala and Namachchivaya (arXiv:1311.4532, 2013) study small-noise averaging near oscillatory critical eigenspaces, rather than the present double-zero feedback threshold and global finite-time covariance barriers. Mackey and Nechaeva (Phys. Rev. E 52, 3366, 1995) study moment stability in a broader linear delay class, with full-text comparison remaining an originality risk. No blanket absence or priority claim is made about all stochastic-delay literature.

## Limitations

The theorem is exact only for the additive-noise linear critical delay equation with deterministic zero history. In the original nonlinear repulsive Gaussian model, growing displacements invalidate the global use of its linearization; cubic dispersion there is **not** proved. The coupling estimate is pointwise in rescaled time, not a proved \(L^2\) supremum estimate. The moment diagnostics are finite and cannot establish the analytical limit. General renewal-theoretic or delay-equation results already contain the underlying response representation and asymptotic and might implicitly contain the whole quantitative stochastic statement, and independent publication-priority review remains outstanding.

## References

- R. A. Kopp and S. H. L. Klapp, *Heat production in a stochastic system with nonlinear time-delayed feedback*, arXiv:2408.03316v1, 2024-08-06, https://arxiv.org/html/2408.03316v1 (Sections II, III and appendices inspected).
- R. A. Kopp and S. H. L. Klapp, *Persistent motion of a Brownian particle subject to repulsive feedback with time delay*, arXiv:2210.03182v1, 2022-10-06, https://arxiv.org/abs/2210.03182 (Sections III and IV inspected).
- N. Lingala and N. S. Namachchivaya, *Nonlinear and additive white noise perturbations of linear delay differential equations at the verge of instability: an averaging approach*, arXiv:1311.4532, 2013, https://arxiv.org/abs/1311.4532 (Introduction and scope compared).
- M. C. Mackey and I. G. Nechaeva, *Solution moment stability in stochastic differential delay equations*, Phys. Rev. E 52, 3366 (1995), https://doi.org/10.1103/PhysRevE.52.3366 (abstract compared; full text not materially inspected).
- *First principles proof of the limit of the expected excess of the uniform renewal function*, Mathematics Stack Exchange, 2021-04-18, https://math.stackexchange.com/questions/4106814 (known exact uniform renewal formula and offset).
- S. Lototsky, *A Summary of Renewal Theory*, https://dornsife.usc.edu/sergey-lototsky/wp-content/uploads/sites/211/2023/06/RenewalTheory-summary.pdf (pp. 1–2 inspected; general renewal equation and renewal theorems).
