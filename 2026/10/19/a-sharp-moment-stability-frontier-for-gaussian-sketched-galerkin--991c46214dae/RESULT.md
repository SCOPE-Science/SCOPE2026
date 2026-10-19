# A sharp moment-stability frontier for Gaussian-sketched Galerkin decay

## Finding

**Theorem (Gaussian-sketched one-mode decay and sketch-reuse dichotomy).** Fix an integer \(d\ge2\), a real symmetric positive-definite matrix \(A\in\mathbb R^{d\times d}\), and a deterministic unit trial vector \(u\in\mathbb R^d\). Write
\[
\mu=u^{\mathsf T}Au>0,\qquad
\beta=\|(I-uu^{\mathsf T})Au\|_2.
\]
Assume \(\beta>0\), so the trial line is not invariant under \(A\). For any finite integer sketch size \(\ell\ge1\), draw \(S\in\mathbb R^{\ell\times d}\) with independent standard real Gaussian entries. The **sketched Galerkin** approximation \(y(t)=a(t)u\) to the dissipative equation \(y'(t)=-Ay(t)\) enforces the one-dimensional sketched inner-product condition
\[
(Su)^{\mathsf T}S\bigl(u a'(t)+Au\,a(t)\bigr)=0.
\]
Almost surely \(Su\ne0\); the random reduced rate is therefore
\[
\Lambda_\ell=\frac{(Su)^{\mathsf T}S Au}{\|Su\|_2^2}
\ \overset{\mathrm d}=\ \mu+\frac{\beta}{\sqrt\ell}\,T_\ell,
\]
where \(T_\ell\) has the standard real Student distribution with \(\ell\) degrees of freedom.

For every deterministic \(a_0\ne0\) and every \(t>0\), the **exact-in-time, frozen-sketch** Galerkin solution satisfies
\[
\boxed{\ \mathbb E\|a_0e^{-t\Lambda_\ell}u\|_2^2=+\infty\quad\text{for every finite }\ell\ge1.\ }
\]
In fact, every positive moment of the norm is infinite at every positive time. Nevertheless, \(\Lambda_\ell\to\mu\) in probability as \(\ell\to\infty\).

For explicit Euler with any fixed \(h>0\) and integer step count \(k\ge1\), distinguish two sampling conventions:

1. **One frozen sketch:** \(a_k=a_0(1-h\Lambda_\ell)^k\). Its squared moment is finite **if and only if** \(\ell>2k\); at \(\ell=2k\) it already diverges logarithmically. Consequently a fixed finite sketch cannot give finite mean-square error for arbitrarily many Euler steps, however small \(h\) is.
2. **An independent fresh sketch on each Euler step:** \(a_{j+1}=(1-h\Lambda_{\ell,j})a_j\), with independent copies of the rate. If \(\ell\le2\), \(\mathbb E|a_k|^2=+\infty\) for every \(k\ge1\). If \(\ell>2\), then for every \(k\ge0\)
\[
\boxed{\quad \mathbb E|a_k|^2=|a_0|^2\biggl[(1-h\mu)^2+\frac{h^2\beta^2}{\ell-2}\biggr]^k.\quad}
\]
Thus fresh-sketch Euler is **strictly mean-square stable** (\(\mathbb E|a_k|^2\to0\)) precisely when
\[
\boxed{\quad \ell>2,\qquad 0<h<\frac{2\mu}{\mu^2+\beta^2/(\ell-2)}.\quad}
\]
This is a sharp sketch-size and stepsize boundary, not merely a sufficient condition. The orthogonal (unsketched) Galerkin method has deterministic rate \(\mu\) and the larger Euler stability interval \(0<h<2/\mu\).

The formula for the exact negative-rate probability, which is a **supporting known fixed-vector sign-loss law** rather than the novel part of this result, is
\[
\Pr(\Lambda_\ell<0)=\frac12 I_{\beta^2/(\mu^2+\beta^2)}\left(\frac\ell2,\frac12\right)>0,
\]
with \(I_z\) the regularized incomplete beta integral. The genuinely dynamical conclusions above show why the vanishing of this probability with increasing \(\ell\) cannot be interchanged with positive-time mean-square averaging.

## Assumptions and scope

All matrices and vectors are real, the parent generator is \(-A\) with \(A\) symmetric positive-definite, and arithmetic and time propagation are exact except for the deliberately specified explicit-Euler discretization. The trial space \(\operatorname{span}\{u\}\) and \(A\) are fixed independently of all Gaussian sketches. The sketch is used **inside the Galerkin inner product**; merely using a random sketch to orthogonalize a basis while retaining ordinary orthogonal Galerkin projection is a different method. No Gaussian truncation, screening, rejection, or conditioning on a successful subspace embedding is imposed. Reused versus refreshed sketches refer only to the random reduced rates, not to a changing trial space.

The degenerate case \(\beta=0\) is an exact exception: \(Au=\mu u\), so the random rate is identically \(\mu\), every positive-time norm moment is finite, and both Euler conventions reduce to deterministic Euler with the usual interval \(0<h<2/\mu\). All infinite-moment claims require \(a_0\ne0\), \(\beta>0\), and strictly positive time or step size as stated.

## Proof

**1. Random reduced generator.** Set \(v=(Au-\mu u)/\beta\), so \(\|v\|_2=1\) and \(v^{\mathsf T}u=0\). The independent standard-normal vectors \(g=Su\) and \(z=Sv\) in \(\mathbb R^\ell\) have independent entries and are independent of one another, by rotational invariance of the Gaussian rows. Consequently
\[
\Lambda_\ell=\mu+\beta\frac{g^{\mathsf T}z}{g^{\mathsf T}g}.
\]
Conditionally on \(g\ne0\), \(Z=g^{\mathsf T}z/\|g\|_2\) is standard normal with a law independent of \(g\); hence \(Z\) is independent of \(V=\|g\|_2^2\sim\chi^2_\ell\). It follows that
\[
\Lambda_\ell=\mu+\beta Z/\sqrt V,
\qquad T_\ell=Z/\sqrt{V/\ell}.
\]
This proves the asserted distribution exactly. The standard Student tail formula yields the incomplete-beta expression above. Since \(V/\ell\to1\) in probability and \(Z/\sqrt\ell\to0\), the rate converges in probability to \(\mu\).

**2. Frozen exact-time propagation.** The sketched Galerkin condition is the scalar ODE \(a'=-\Lambda_\ell a\) and has the pathwise solution \(a(t)=a_0e^{-t\Lambda_\ell}\). For arbitrary \(p,t>0\), restrict to the positive-probability event \(Z\le-1\); on it
\[
|a(t)|^p\ge |a_0|^p e^{-pt\mu}e^{pt\beta/\sqrt V}.
\]
As \(v\downarrow0\), the \(\chi^2_\ell\) density is a positive constant times \(v^{\ell/2-1}e^{-v/2}\), and
\[
\int_0^1 e^{pt\beta/\sqrt v}\,v^{\ell/2-1}e^{-v/2}\,dv=+\infty.
\]
Independence of \(Z,V\) proves \(\mathbb E|a(t)|^p=+\infty\). In particular take \(p=2\). Every realized rate is finite almost surely; the divergence is solely an averaging/tail phenomenon, not finite-time blow-up of an individual scalar ODE.

**3. Frozen Euler threshold.** For integer \(k\ge1\), \(|1-h\Lambda_\ell|^{2k}\) is a nonnegative polynomial of exact degree \(2k\) in \(Z/\sqrt V\), with positive leading coefficient \((h\beta)^{2k}\). Student tails have positive polynomial density asymptotic to a constant times \(|x|^{-(\ell+1)}\), so the moment exists exactly if \(2k<\ell\). At equality the tail integral behaves as \(\int^\infty dx/x\). Equivalently, the same threshold follows from
\[
\mathbb E V^{-k}=2^{-k}\frac{\Gamma(\ell/2-k)}{\Gamma(\ell/2)}\quad\text{when }\ell>2k,
\]
with an infinite integral otherwise. There is no cancellation because the integrand is nonnegative and grows as a fixed positive multiple of \(|Z/\sqrt V|^{2k}\) on either far tail.

**4. Refreshed Euler threshold.** If \(\ell>2\), symmetry and the same inverse-chi-square identity give
\[
\mathbb E\Lambda_\ell=\mu,\qquad
\operatorname{Var}(\Lambda_\ell)=\beta^2\mathbb EV^{-1}=\frac{\beta^2}{\ell-2}.
\]
Thus the conditional one-step squared amplitude multiplier has expectation \((1-h\mu)^2+h^2\beta^2/(\ell-2)\). Fresh independence yields the geometric identity by conditional expectation and induction. The multiplier is below one exactly in the stated open interval; at its right endpoint it is one, and outside it is greater than one. For \(\ell\le2\), the first-step second moment is infinite, and independence gives the same result at every later step. This proves all cases.

## Verification

A standalone program, `check.py`, tests the reduced-rate formula on a symmetric positive-definite two-mode example; matches the Student and incomplete-beta tail probabilities at six sketch sizes; checks 18 simulated quantiles and four finite-second-moment estimates; and validates the rational three-row Euler threshold. Its random seeds and parameters are embedded in the file. It is run with `python check.py` (requires NumPy and SciPy). Numerical sampling **cannot** verify an infinite expectation or an all-dimension theorem; those follow from the displayed integral and inverse-chi-square arguments.

As a concrete diagnostic, take \(A=\operatorname{diag}(1,9)\) and \(u=(1,1)^{\mathsf T}/\sqrt2\). Then \(\mu=5\), \(\beta=4\). With three Gaussian sketch rows and Euler step \(h=1/5\), independently refreshed sketches give the exact mean-square factor \(16/25\) per step, whereas a single reused sketch already gives an **infinite second moment at the second Euler step**. The sharp fresh-sketch Euler stability ceiling is \(10/41\), versus \(2/5\) without sketching. These are exact expressions, not fitted simulation constants.

## Relationship to prior work

Carrel and Grigori, *Sketch low-rank dynamics: orthogonal vs. oblique projections* (arXiv:2607.03402v1, first public July 3, 2026), analyze the distinction between orthogonal and sketched Galerkin dynamics in matrix dynamical low-rank approximation, with deterministic embedding conditions and numerical demonstrations of oblique energy drift. Their Section 4 and Section 6 explicitly distinguish the analytic resampling convention from experiments using frozen sketches. The theorem here concerns a fixed one-dimensional Galerkin trial space for a dissipative linear ODE, **not** the full matrix dynamical low-rank integrators; it contributes a distributional and moment-stability analysis absent from the material examined there.

Krieger and Schweitzer, *A general framework for Krylov ODE residuals with applications to randomized Krylov methods* (arXiv:2510.17538v1, October 20, 2025), Section 4, derive sketched-inner-product Galerkin equations for ODE approximation and investigate residual-based estimates and restarts. Their projected ODE identity is consistent with the reduction used here. Their analysis does not establish the Student law, infinite positive-time moment, or frozen-versus-fresh Euler threshold stated above.

Balabanov and Nouy, *Randomized linear algebra for model reduction. Part I: Galerkin methods and error estimation* (arXiv:1803.02602, first public March 7, 2018), develop high-probability sketch-embedding conditions for accurate Galerkin reduction. Such conditioned or high-probability guarantees do not entail unconditional expectation bounds; the distinction is central here. Fixed-vector Gaussian sign-loss formulas and basic Student-distribution tail and inverse-chi-square facts are pre-existing ingredients, not asserted as new independent contributions.

## Limitations

The theorem is exact for a fixed rank-one trial space with Gaussian sketches and a symmetric positive-definite generator. It makes no claim about all higher-rank sketch Galerkin matrices, adaptive trial spaces, finite-precision implementations, or the named source papers' production algorithms. Its infinite-moment conclusions are unconditional over the full Gaussian distribution; conditioning sketches on an embedding event, regularizing small \(\|Su\|_2\), resampling continuously in time under a separately specified stochastic process, or imposing finite-precision cutoffs changes the model. An infinite expectation is not a claim of almost-sure divergence: every realized frozen-sketched exponential trajectory is finite at finite times. The mean-square stability threshold is not an assertion of optimal total computational cost.

## References

1. B. Carrel and L. Grigori, *Sketch low-rank dynamics: orthogonal vs. oblique projections*, arXiv:2607.03402v1 (2026-07-03), https://arxiv.org/abs/2607.03402.
2. E. Krieger and M. Schweitzer, *A general framework for Krylov ODE residuals with applications to randomized Krylov methods*, arXiv:2510.17538v1 (2025-10-20), https://arxiv.org/abs/2510.17538.
3. O. Balabanov and A. Nouy, *Randomized linear algebra for model reduction. Part I: Galerkin methods and error estimation*, arXiv:1803.02602 (2018-03-07), https://arxiv.org/abs/1803.02602.
