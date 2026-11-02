# Universal critical extinction profile in density-dependent metapopulations

## Finding

For a positive, density-suppressed, finite-patch Kolmogorov population map at the exact invasion threshold, every nonzero nonnegative population approaches extinction at the same algebraic rate and with the same spatial profile. This holds regardless of the initial distribution or total density. More precisely, if the zero-population Jacobian has Perron root \(1\), then

\[
\lim_{t\to\infty}t\,x_i(t)=\frac{v_i}{\kappa}\quad (i=1,\ldots,n),
\]

where \(v\) is the positive Perron right eigenvector normalized by \(\sum_jv_j=1\), and \(\kappa\) is an explicit positive weighted curvature including both local recruitment and density-dependent dispersal. Thus an invasion-neutral population can still become extinct globally, but its relaxation is polynomial rather than exponentially fast.

## Assumptions and scope

Let \(n\ge 2\) be any fixed integer, and let \(x(t)\in[0,\infty)^n\). The update for each patch \(i\) is

\[
x_i(t+1)=F_i(x(t))=\sum_{j=1}^n d_{ij}(x_j(t))g_j(x_j(t))x_j(t).
\]

All functions \(g_j:[0,\infty)\to(0,\infty)\) and \(d_{ij}:[0,\infty)\to(0,1)\) are \(C^2\) (with one-sided derivatives at zero); \(g_j\) is strictly decreasing with \(g_j'(0)<0\); \(d_{ij}\) is nonincreasing; \(\sum_i d_{ij}(u)<1\) for every \(u\ge0\); and each local recruitment map \(u\mapsto u g_j(u)\) is bounded. No monotonicity of the full population update \(F\) is assumed.

Define the strictly positive matrix \(M_{ij}=d_{ij}(0)g_j(0)\) and assume \(\rho(M)=1\). Fix strictly positive Perron eigenvectors \(Mv=v\), \(w^{\mathsf T}M=w^{\mathsf T}\) with \(\sum_jv_j=1\), \(w^{\mathsf T}v=1\). Set

\[
B_{ij}=d_{ij}(0)g'_j(0)+d'_{ij}(0)g_j(0),\qquad
\kappa=-\sum_{i,j}w_i B_{ij}v_j^2>0.
\]

The stated limit holds for every \(x(0)\in[0,\infty)^n\setminus\{0\}\), with no smallness requirement on the starting population. The equilibrium at extinction is globally attracting and Lyapunov stable on the nonnegative cone. The theorem pertains to deterministic finite-dimensional patch populations, not demographic stochasticity or time-varying environments.

## Proof

**Strict global drift.** Since each local \(g_j\) is strictly decreasing and each \(d_{ij}\) is nonincreasing, for any \(u>0\),
\(0<d_{ij}(u)g_j(u)<d_{ij}(0)g_j(0)=M_{ij}\). Therefore \(0<F(x)\le Mx\) for any \(x\ne0\), and the inequality is strict componentwise whenever \(x\ne0\), because some active column contributes strictly to every row. Define \(s_t=w^{\mathsf T}x(t)>0\). Positivity and \(w^{\mathsf T}M=w^{\mathsf T}\) imply \(0<s_{t+1}<s_t\). Since \(w\gg0\), all components of every orbit are uniformly bounded by \(s_0/\min_iw_i\). If \(s_t\to L>0\), compactness supplies a nonzero limit point \(x_*\) of a subsequence. The continuous strict decrement \(w^{\mathsf T}(Mx_*-F(x_*))>0\) contradicts \(s_t-s_{t+1}\to0\). Hence \(s_t\to0\), and therefore \(x(t)\to0\). The monotone positive functional also gives Lyapunov stability.

**Quadratic expansion.** A second-order Taylor expansion, uniformly as \(x\to0\) in the cone, gives
\[
F_i(x)=\sum_jM_{ij}x_j+\sum_jB_{ij}x_j^2+o(\|x\|^2).
\]
Strictly negative \(g'_j(0)\), nonpositive \(d'_{ij}(0)\), and positivity of \(d_{ij}(0),g_j(0),w,v\) ensure \(B_{ij}<0\) and \(\kappa>0\). Since \(x(t)\to0\) and its coordinates are bounded by constants times \(s_t\), the nonlinear remainder \(H(x):=F(x)-Mx\) satisfies \(\|H(x(t))\|=O(s_t^2)\). Thus \(s_{t+1}=s_t+O(s_t^2)\) and \(s_{t+1}/s_t\to1\).

**Perron direction.** Write \(x(t)=s_tv+z_t\) with \(w^{\mathsf T}z_t=0\). The spectral radius of \(M\) restricted to the invariant space \(E=\{z:w^{\mathsf T}z=0\}\) is strictly below one because \(M\) is a positive primitive matrix. Hence there is an equivalent norm on \(E\) and \(\lambda<1\) for which \(\|Mz\|_*\le\lambda\|z\|_*\). Applying the projection \(I-vw^{\mathsf T}\) to the update yields
\[
\|z_{t+1}\|_*\le \lambda\|z_t\|_*+Cs_t^2.
\]
Divide by \(s_{t+1}\); the ratio \(s_t/s_{t+1}\to1\) and \(s_t\to0\) give, for sufficiently large \(t\),
\(\|z_{t+1}\|_*/s_{t+1}\le\lambda'\|z_t\|_*/s_t+o(1)\) for some \(\lambda'<1\). The elementary contractive-recursion lemma now implies \(\|z_t\|_*/s_t\to0\), i.e. \(x(t)=s_tv+o(s_t)\).

**Sharp amplitude.** Substitute this direction asymptotic into the quadratic expansion and apply \(w^{\mathsf T}\):
\[
s_{t+1}-s_t=\sum_{i,j}w_iB_{ij}x_j(t)^2+o(s_t^2)
=-\kappa s_t^2+o(s_t^2).
\]
Thus \(s_{t+1}^{-1}-s_t^{-1}\to\kappa\), because \(s_{t+1}/s_t\to1\). Summing the reciprocal differences and dividing by \(t\) proves \(t s_t\to1/\kappa\). Combining this with \(x(t)/s_t\to v\) gives the claimed coordinatewise limit for every initial population. \(\square\)

## Verification

An explicit density-dependent two-patch example has
\[
M=\begin{pmatrix}3/4&1/3\\1/4&2/3\end{pmatrix},\qquad
g_j(u)=\frac{2}{1+2u},\qquad
d_{ij}(u)=\frac{M_{ij}}{2(1+u)}.
\]
Both dispersal-column sums are \(1/[2(1+u)]<1\), and each recruitment map \(ug_j(u)\) is bounded by \(1\). The Perron vectors are \(v=(4/7,3/7)^{\mathsf T}\) and \(w=(1,1)^{\mathsf T}\). Because \(B_{ij}=-3M_{ij}\),
\[
\kappa=3\bigl[(4/7)^2+(3/7)^2\bigr]=75/49,
\quad \lim_{t\to\infty}t x(t)=\bigl(28/75,7/25\bigr)^{\mathsf T}.
\]
For comparison, keeping the same local recruitment and the same zero-density dispersal matrix but making dispersal constant produces \(B_{ij}=-2M_{ij}\), \(\kappa=50/49\), so the extra dispersal density dependence raises the decay curvature by exactly \(50\%\). The embedded standalone Python program `verify_critical_metapopulation.py` verifies these rational identities and provides a 200,000-step numerical diagnostic, not a substitute for the global proof.

## Relationship to prior work

McGrane-Corrigan, Mason and de Andrade Moral (2024), Section 4, introduce this exact class of nonlinear, costly, density-dependent dispersal and bounded Kolmogorov recruitment. Their Proposition 2 establishes global extinction under additional monotonicity and the strict linear threshold \(\rho(M)<1\); their Theorem 5.1 treats positive equilibria for \(\rho(M)>1\). The present theorem addresses the excluded equality \(\rho(M)=1\) and obtains a sharp amplitude that separately records recruitment and dispersal derivatives. Their main result does not imply this critical-rate limit.

Jin, Smith and Thieme (2015) establish extinction/persistence criteria for a broader class of structured discrete-time positive systems; that broader threshold context is relevant, but the accessible abstract does not state the exact global critical profile here. Thieme (2020) studies spectral thresholds for population turnover maps on measure spaces, also without an accessible statement of the specific coefficient in this model. Perron–Frobenius spectral decomposition and reciprocal quadratic-drift asymptotics are classical mathematical ingredients; no claim of inventing either ingredient is made.

## Limitations

All dispersal entries must be strictly positive at every density and nonincreasing; each recruitment factor must decrease strictly with a negative derivative at zero. The result need not hold if the local recruitment curves are Allee-enhancing at low densities, if nonlinear dispersal increases sufficiently strongly, if the Perron root is multiple, or if quadratic curvature vanishes. The rate is not an extinction-time statement for finite stochastic populations. The coefficient is an asymptotic statement, not an exact finite-time formula. Bibliographic originality requires independent confirmation against additional generic nonlinear Perron-limit literature and any inaccessible full texts; the self-review is not an independent audit.

## References

1. B. McGrane-Corrigan, O. Mason and R. de Andrade Moral, *A density-dependent metapopulation model: Extinction, persistence and source-sink dynamics*, arXiv:2405.04505v1 (first posted 2024-05-07), https://arxiv.org/html/2405.04505v1 , esp. Sections 3–5.
2. W. Jin, H. L. Smith and H. R. Thieme, *Persistence versus extinction for a class of discrete-time structured population models*, Journal of Mathematical Biology 72 (2016), 821–850, https://doi.org/10.1007/s00285-015-0898-8 (first online in 2015).
3. H. R. Thieme, *Discrete-time population dynamics on the state space of measures*, Mathematical Biosciences and Engineering 17 (2020), 1168–1217, https://doi.org/10.3934/mbe.2020061 .
