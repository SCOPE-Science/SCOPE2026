# All-budget threshold vaccination in an equal-susceptibility SIR model

## Finding

In an age-structured susceptible–infectious–removed epidemic with a common force of infection and heterogeneous infectiousness and removal rates, the exact optimal **perfect pre-epidemic vaccination policy** is to vaccinate in decreasing order of infectiousness divided by removal rate, for **every vaccine budget**. In particular, no small-budget or supercriticality restriction is needed, and ties in the priority index are permitted. The complete optimal survivor curve is given by one scalar final-size equation. This fills the large-budget regime left outside Theorem 4 of Almeida, Ducasse and Paparelli [1].

Here is the precise theorem. Let \(X=[0,A]\) with \(A>0\). Assume \(S_0, I_0,\beta,\mu\) are continuous on \(X\), \(S_0>0\), \(I_0\geq0\) and not identically zero, and \(\beta,\mu>0\). Transmission from an infectious individual of age \(y\) to a susceptible of any age \(x\) is \(\beta(x,y)=\beta(y)\). Vaccination before transmission begins removes an arbitrary measurable density \(v\) satisfying \(0\leq v\leq S_0\); its total mass is at most \(K\), where \(0\leq K\leq S:=\int_X S_0\). Define

\[
r(y)=\frac{\beta(y)}{\mu(y)},\qquad B=\int_Xr(y)I_0(y)\,dy>0,\qquad T(v)=\int_Xr(y)(S_0(y)-v(y))\,dy.
\]

For every such \(v\) there is exactly one positive number \(H(v)\) satisfying

\[
\boxed{H(v)=B+T(v)\bigl(1-e^{-H(v)}\bigr)}.
\]

The total mass initially vaccinated or never infected is exactly

\[
\boxed{N(v)=\int_Xv+\left(S-\int_Xv\right)e^{-H(v)}}.
\]

**All-budget optimization.** Every maximizing allocation uses precisely \(K\) doses. For \(0<K<S\), all maximizing allocations (up to null sets) have a threshold form

\[
\boxed{
v_K(y)=S_0(y)\mathbf 1_{\{r(y)>c\}}+\theta(y)S_0(y)\mathbf 1_{\{r(y)=c\}},
}\qquad 0\leq\theta\leq1,
\]

where \(c\) and \(\theta\) are chosen so that \(\int_Xv_K=K\). No doses are assigned where \(r<c\). For \(K=0\), the unique allocation is zero; for \(K=S\), it is \(S_0\). Ties at \(r=c\) permit arbitrary distribution of the requisite dose mass within that level set. When the priority index has no positive-measure level sets, the optimal allocation is unique almost everywhere.

For an exact expression valid for all budgets, let \(R:[0,S]\to(0,\infty)\) be the nonincreasing rearrangement of \(r\) with respect to the measure \(S_0(y)\,dy\). Write

\[
T_*(K)=\int_K^S R(u)\,du,\qquad H_K=B+T_*(K)(1-e^{-H_K}).
\]

The defining equation has a unique positive solution, and the maximum surviving mass is

\[
\boxed{N_*(K)=K+(S-K)e^{-H_K}},\qquad 0\leq K\leq S.
\]

The curve is strictly increasing. At every interior budget where \(R\) is continuous, its derivative exists and is

\[
\boxed{N_*'(K)=(1-e^{-H_K})\left[1+\frac{(S-K)R(K)e^{-H_K}}{1-T_*(K)e^{-H_K}}\right]>0.}
\]

At jumps of \(R\), the corresponding one-sided versions hold. In particular, **the formula remains regular when the post-vaccination reproduction parameter \(T_*(K)\) passes through one**. The denominator in these formulas is always strictly positive because the initial infectious mass is nonzero.

As a direct consequence of the equivalence of the dynamic and initial vaccination suprema established in [1, Theorem 3], the same \(N_*(K)\) is the supremum for the source's admissible time-dependent vaccination controls. The source allows approximating the initial mass vaccination arbitrarily early; it does **not** assert that an impulsive initial allocation is attained by a time-dependent control.

## Assumptions and scope

The unvaccinated evolution after the initial allocation is

\[
\partial_t S(t,x)=-\lambda(t)S(t,x),\quad
\partial_t I(t,x)=\lambda(t)S(t,x)-\mu(x)I(t,x),\quad
\lambda(t)=\int_X\beta(y)I(t,y)\,dy,
\]

with \(S(0,x)=S_0(x)-v(x)\) and \(I(0,x)=I_0(x)\). In the mathematical model of [1], an infected individual eventually leaves the infectious class, and its removal is counted as a casualty; the objective counts the vaccinated and the never-infected rather than recovered people. Vaccine doses grant immediate perfect protection, are assigned only to initially susceptible individuals, and have equal cost. The result does not rely on weak seeding or any restriction on the ratio of transmission to removal. The analogous finite-group model with nonnegative susceptible and positive initial infectious masses satisfies the same formulas with sums instead of integrals.

## Proof

**1. Exact scalar final size.** Since \(\lambda\geq0\), define \(H(t)=\int_0^t\lambda(s)\,ds\). The susceptible equation integrates to \(S(t,x)=(S_0(x)-v(x))e^{-H(t)}\). Nonnegative incidence and removal imply

\[
\int_0^\infty\int_X\mu(x)I(t,x)\,dx\,dt\leq\int_X(I_0+S_0-v)<\infty.
\]

As \(\beta/\mu\) is bounded, \(H(\infty)<\infty\). Moreover, each infectious class tends to zero (the standard positive SIR convergence argument in [1, Theorem 2]; alternatively solve its stable scalar inhomogeneous equation, noting the integrable incidence). Integrating the infectious equation over time and multiplying by \(r(x)\), then integrating over \(X\), gives

\[
\begin{aligned}
H(\infty)
&=\int_X \frac{\beta(x)}{\mu(x)}\left[I_0(x)+S_0(x)-v(x)-S(\infty,x)\right]dx\\
&=B+T(v)(1-e^{-H(\infty)}).
\end{aligned}
\]

Consequently \(N(v)=\int v+(S-\int v)e^{-H}\).

**2. Physical root and its strict response.** For \(T\geq0\), consider \(g_T(h)=h-B-T(1-e^{-h})\). It satisfies \(g_T(0)=-B<0\), tends to infinity, and has \(g_T''(h)=Te^{-h}\geq0\). Thus it has exactly one zero \(H(T)>0\); for \(T=0\), the root is \(B\). At every root, \(H\geq B>0\), and

\[
Te^{-H}=\frac{H-B}{e^H-1}<1.
\]

The strict inequality uses \(e^H-1>H\). Implicit differentiation is therefore valid even for \(T\leq1\), yielding

\[
H'(T)=\frac{1-e^{-H(T)}}{1-Te^{-H(T)}}>0,
\qquad
\frac{d(e^{-H(T)})}{dT}=-\frac{e^{-H(T)}(1-e^{-H(T)})}{1-Te^{-H(T)}}<0.
\]

Thus, for fixed used dose mass \(m\), maximizing the surviving mass \(m+(S-m)e^{-H(T)}\) is equivalent to minimizing \(T(v)\).

**3. The priority exchange argument.** With \(m\) fixed, \(T(v)=\int_XrS_0-\int_Xrv\). Choose \(c\) so that the mass \(m\) can be allocated among \(r>c\) and the required portion of \(r=c\). This exists by the distribution function of \(r\) under the finite nonatomic measure \(S_0(x)dx\). For any competitor \(v\) of the same mass, the threshold allocation \(v_m\) satisfies

\[
\int_X r(v_m-v)=\int_X (r-c)(v_m-v)\geq0.
\]

On \(r>c\), the first factor is positive and \(v_m-v\geq0\); on \(r<c\), both factors are negative or zero; on \(r=c\), the integrand is zero. Equality is possible only through reallocations within tied priority levels, except at trivial endpoints. Therefore the threshold allocation exactly minimizes \(T\) for every \(m\in[0,S]\) and hence maximizes \(N\) at that \(m\).

**4. Every dose is used.** Suppose \(m<K\). Since \(K\leq S\), choose nonnegative \(\delta\leq S_0-v\) of positive mass \(d\leq K-m\), and put \(w=v+\delta\). Then \(T(w)<T(v)\), so \(q_w:=e^{-H(w)}>q_v:=e^{-H(v)}\). Therefore

\[
N(w)-N(v)=d(1-q_w)+(S-m)(q_w-q_v)>0.
\]

This excludes any maximizer using fewer than \(K\) doses, including beyond the low-budget range. At \(K=S\) everyone initially susceptible may be vaccinated and \(N_*(S)=S\).

**5. Exact full frontier and its derivative.** The decreasing rearrangement identity gives \(\min_{\int v=K}T(v)=\int_K^S R(u)du\). Applying steps 1–4 yields the boxed all-budget formula. At a point of continuity of \(R\), \(T_*'(K)=-R(K)\), so implicit differentiation yields

\[
H_K'=-\frac{R(K)(1-e^{-H_K})}{1-T_*(K)e^{-H_K}}.
\]

Differentiating \(K+(S-K)e^{-H_K}\) proves the displayed positive marginal benefit. Every denominator is positive by step 2, regardless of whether \(T_*(K)\) is above, equal to or below one. This completes the proof.

## Verification

The accompanying standalone Python program `verify.py` enumerates all \(5^3=125\) allocations on a three-group rational quarter-dose grid. It proves the exact weighted-exposure inequalities on that grid using rational arithmetic, then checks the numerical survivor ordering through a bisection solution of the scalar final-size equation. It also verifies a tied-index example, parameter values on both sides of \(T=1\), and two independent direct Runge–Kutta integrations of the SIR equations. These finite tests **do not prove** the continuum theorem; the unrestricted proof is above.

An example deliberately exceeds the budget cap in [1, Theorem 4]. In a two-group version with \(S_0=(1,1)\), \(\mu=(1,1)\), \(\beta=(4,1)\), \(I_0=(0.05,0)\), and \(K=1.5\), the source's small-budget condition would require \(K<1.25\). The threshold choice \(v=(1,0.5)\) has \(T=0.5\) and gives \(N\approx1.853622849292\). The reversed choice \(v=(0.5,1)\) has \(T=2\) and gives \(N\approx1.574692330951\). This is a finite-group illustration, not an extra assumption in the general theorem.

## Relationship to prior work

Almeida, Ducasse and Paparelli [1, Theorem 4] establish the same priority index and threshold allocation subject to a small-budget restriction and, in their displayed theorem, a no-positive-measure-ties hypothesis. Remark 1.4 explicitly suggests that the budget restriction could be removed. Their proof uses a monotonicity comparison in a regime ensured by that restriction [1, Section 2.5]. The present argument instead uses the unique positive integrated-force root, its derivative for every nonnegative remaining exposure, and a separate full-budget saturation argument. The new statement is therefore the **all-budget theorem and complete survivor frontier**, not a claim to the original priority ordering, the final-size equations, or the bathtub principle themselves. The possibility of tied priority classes is also acknowledged in [1].

Duijzer and colleagues [2, Sections 2.4 and 5.1] establish a related greedy order in separable mixing for maximizing the unbudgeted herd effect, equivalently finding the *minimum supply required to reach the critical reproduction threshold*. That optimization has a constraint on the reproduction ratio instead of a fixed arbitrary budget and does not yield the entire finite-seed optimal total-survivor curve above and below criticality. Penn and Donnelly [3] analyze small-supply asymptotics for a more general multi-group model, while Gavish and Katriel [4] examine imperfect leaky vaccines and a susceptibility-induced policy reversal; neither is the present perfect-vaccine, common-susceptibility all-budget theorem. The possibility that a broader, specialized allocation theorem elsewhere implies this particular conclusion remains a literature risk rather than a claim of absolute uniqueness.

## Limitations

The proof assumes a common infection hazard across susceptible age classes, perfect instantaneous vaccination of susceptible individuals, common per-dose cost, a finite initial infectious seed \(B>0\), and the deterministic SIR dynamics of [1]. It is not a theorem about distinct age-dependent susceptibility, imperfect or waning vaccines, hard delivery-rate constraints, differential disease fatality weights, or nonlinear feedback from control capacity. If the initial infectious seed is identically zero, a zero-force equilibrium becomes a distinct root-selection problem; that case is excluded. The result establishes an abstract optimal allocation, not an ethically or operationally justified public-health policy. The all-time control conclusion is about the supremum inherited from [1], not attainment by an admissible impulsive control.

## References

[1] L. Almeida, R. Ducasse, E. Paparelli, *Optimizing vaccine allocation in an age-structured SIR model*, arXiv:2605.18256v1, first public 18 May 2026. https://arxiv.org/abs/2605.18256 ; especially Theorems 3–4, Remark 1.4, and Section 2.5.

[2] E. Duijzer, W. van Jaarsveld, J. Wallinga, R. Dekker, *The most efficient critical vaccination coverage and its equivalence with maximizing the herd effect*, Mathematical Biosciences 282 (2016), 68–81. Full lawful institutional preprint https://repub.eur.nl/pub/79912/EI2016-06.pdf ; DOI:10.1016/j.mbs.2016.09.017.

[3] M. J. Penn, C. A. Donnelly, *Asymptotic Analysis of Optimal Vaccination Policies*, Bulletin of Mathematical Biology 85 (2023), article 15. https://doi.org/10.1007/s11538-022-01114-3 .

[4] N. Gavish, G. Katriel, *Optimal vaccination at high reproductive numbers: sharp transitions and counter-intuitive allocations*, arXiv:2202.03909v1 (2022). https://arxiv.org/abs/2202.03909 .
