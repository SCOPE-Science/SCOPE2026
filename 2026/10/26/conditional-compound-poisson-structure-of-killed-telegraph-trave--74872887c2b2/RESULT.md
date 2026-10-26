# Conditional compound-Poisson structure of killed telegraph travel time

## Finding
Consider the symmetric one-dimensional telegraph motion with initial velocity \(+c\) or \(-c\), each with probability \(1/2\), switches at rate \(\alpha>0\), and an independent exponential killing time \(T\) of rate \(\gamma>0\). Write \(Z=X(T)\). In the original killing-at-an-event model of Orsingher--Marchione, \(\alpha=\lambda(1-p)\) and \(\gamma=\lambda p\), where \(\lambda>0\) and \(0<p<1\).

For every \(x\in\mathbb R\) there is a continuous version of the conditional law of \(T\) given \(Z=x\) with the **independent compound-Poisson representation**
\[
T\mid\{Z=x\}\ \overset{d}{=}\ \frac{|x|}{c}+U+V_{|x|}.
\]
Here \(U\) is a compound-Poisson sum with finite Lévy measure
\[
\nu_0(dt)=\frac{e^{-\gamma t}-e^{-(\gamma+2\alpha)t}}{2t}\,dt,
\]
and, independently, \(\{V_y:y\ge0\}\) is a compound-Poisson subordinator with time-per-distance Lévy measure
\[
\nu_1(dt)=\frac{\alpha}{c}\frac{e^{-(\gamma+\alpha)t}I_1(\alpha t)}{t}\,dt,
\]
where \(I_1\) is the usual modified Bessel function of the first kind. Their jump rates are exactly
\[
\rho_0=\frac12\log\frac{\gamma+2\alpha}{\gamma},\qquad
\rho_1=\frac{\gamma+\alpha-\sqrt{\gamma(\gamma+2\alpha)}}{c}.
\]
In particular, each conditional law is compound Poisson shifted by the ballistic time; these laws admit a common coupling increasing with \(|x|\). The boundary atom is
\[
\Pr\!\left(T=\frac{|x|}{c}\,\middle|\, Z=x\right)
=\sqrt{\frac{\gamma}{\gamma+2\alpha}}\,
\exp\!\left[-\frac{|x|}{c}\bigl(\gamma+\alpha-\sqrt{\gamma(\gamma+2\alpha)}\bigr)\right]>0.
\]
The conditional first two moments have affine dependence on endpoint distance:
\[
\mathbb E[T\mid Z=x]=\frac{\alpha}{\gamma(\gamma+2\alpha)}
+\frac{(\gamma+\alpha)|x|}{c\sqrt{\gamma(\gamma+2\alpha)}},
\]
\[
\operatorname{Var}(T\mid Z=x)=\frac12\left(\frac1{\gamma^2}-\frac1{(\gamma+2\alpha)^2}\right)
+\frac{\alpha^2|x|}{c[\gamma(\gamma+2\alpha)]^{3/2}}.
\]
These compound-Poisson and coupling identities, rather than the already known joint density of \((Z,T)\), are the subject of the finding.

## Assumptions and scope
The particle starts at the origin, chooses its initial velocity symmetrically and independently, and subsequently reverses sign after independent exponential waiting times of rate \(\alpha\). An independent \(\operatorname{Exp}(\gamma)\) clock kills the particle. All parameters \(c,\alpha,\gamma\) are strictly positive and fixed. The identification with kill-at-switching events uses independent thinning of a rate-\(\lambda\) Poisson process. The conditional assertions specify the continuous regular conditional distribution obtained below, including its value at the measure-zero conditioning point \(x=0\).

The Poisson jump measures above have no atoms at zero and are finite; the jump variables are positive. Conditional distributions for opposite terminal positions are identical. The theorem does not concern planar motions, deterministic observation horizons, or asymmetric velocities.

## Proof
**1. Joint Fourier--Laplace resolvent.** Let \(f_t(k)=\mathbb E e^{ikX(t)}\) for the un-killed symmetric telegraph motion. Its two-state velocity generator gives
\[
f_t''(k)+2\alpha f_t'(k)+c^2k^2f_t(k)=0,\qquad f_0(k)=1,\quad f'_0(k)=0,
\]
where primes here denote derivatives in time. Consequently, for \(s>0\),
\[
\int_0^\infty e^{-st}f_t(k)\,dt
=\frac{s+2\alpha}{s(s+2\alpha)+c^2k^2}.
\]
Since \(T\sim\operatorname{Exp}(\gamma)\) is independent, putting \(s=\gamma+u\) for \(u\ge0\) gives
\[
\mathbb E[e^{-uT+ikZ}]
=\frac{\gamma(s+2\alpha)}{s(s+2\alpha)+c^2k^2}.
\]
The elementary inverse Fourier integral of \((c^2k^2+s(s+2\alpha))^{-1}\) yields the \(x\)-density of \(\mathbb E[e^{-uT};Z\in dx]\):
\[
g_u(x)=\frac{\gamma(s+2\alpha)}{2c\sqrt{s(s+2\alpha)}}
\exp\!\left(-\frac{|x|}{c}\sqrt{s(s+2\alpha)}\right).
\]
At \(u=0\), this becomes the already known Laplace endpoint density \(g_0(x)=\kappa e^{-\kappa|x|}/2\) with \(\kappa=\sqrt{\gamma(\gamma+2\alpha)}/c\). Therefore \(g_u(x)/g_0(x)\) gives a continuous version of the conditional Laplace transform, namely
\[
L_x(u)=\sqrt{\frac{\gamma(\gamma+u+2\alpha)}{(\gamma+u)(\gamma+2\alpha)}}
\exp\!\left[-\frac{|x|}{c}\left(\sqrt{(\gamma+u)(\gamma+u+2\alpha)}-\sqrt{\gamma(\gamma+2\alpha)}\right)\right].
\]

**2. Fixed-delay Lévy measure.** Direct differentiation and integration of \(\log(1+u/a)\) give the identity
\[
\log\sqrt{\frac{\gamma(\gamma+u+2\alpha)}{(\gamma+u)(\gamma+2\alpha)}}
=-\int_0^\infty(1-e^{-ut})\,\frac{e^{-\gamma t}-e^{-(\gamma+2\alpha)t}}{2t}\,dt.
\]
The kernel is positive, integrable at zero and infinity, and integrates to \(\rho_0\) by Frullani's integral.

**3. Distance-indexed Lévy measure.** Let \(a=\gamma+\alpha>\alpha\) and \(h(u)=\sqrt{(u+a)^2-\alpha^2}\). The special-function identity
\[
\int_0^\infty e^{-st}I_0(\alpha t)\,dt=(s^2-\alpha^2)^{-1/2},\qquad s>\alpha,
\]
combined with \(\frac{d}{dt}I_0(\alpha t)=\alpha I_1(\alpha t)\) and integration by parts proves
\[
\frac{s}{\sqrt{s^2-\alpha^2}}-1
=\alpha\int_0^\infty e^{-st}I_1(\alpha t)\,dt.
\]
It follows by integrating \(h'(u)\) over \([0,u]\) that
\[
\frac{h(u)-h(0)}{c}
=\frac{u}{c}+\int_0^\infty(1-e^{-ut})
\frac{\alpha e^{-at}I_1(\alpha t)}{ct}\,dt.
\]
Positivity of \(I_1\) follows from its power series. Near zero, the latter density tends to \(\alpha^2/(2c)\); at infinity, its exponential factor and \(a>\alpha\) ensure integrability. The total mass is
\[
\rho_1=\lim_{u\to\infty}\left(\frac{h(u)-h(0)}c-\frac uc\right)
=\frac{a-h(0)}c.
\]

**4. Probability-law identification and consequences.** Combining Steps 2 and 3 gives
\[
L_x(u)=\exp\!\left[-\frac{u|x|}c-\int_0^\infty(1-e^{-ut})\,\nu_0(dt)
-|x|\int_0^\infty(1-e^{-ut})\,\nu_1(dt)\right].
\]
For a finite nonnegative measure \(\nu\), the transform \(\exp[-\int(1-e^{-ut})\nu(dt)]\) is the Laplace transform of a compound-Poisson sum with intensity \(\nu((0,\infty))\) and jump law \(\nu/\nu((0,\infty))\). Uniqueness of Laplace transforms proves the stated independent decomposition for every \(x\). Taking one common \(U\) and one independent compound-Poisson subordinator \(V_y\) couples the entire family monotonically in \(y=|x|\). The event of no jump in either component has probability \(e^{-\rho_0-y\rho_1}\) and produces exactly the ballistic atom; positivity of both jump laws makes this the entire atom at the boundary.

Finally, taking the first and second cumulants of the two Lévy measures gives the displayed affine mean and variance. Specifically,
\[
\int_0^\infty t\,\nu_0(dt)=\frac{\alpha}{\gamma(\gamma+2\alpha)},\quad
\int_0^\infty t^2\,\nu_0(dt)=\frac12\bigl(\gamma^{-2}-(\gamma+2\alpha)^{-2}\bigr),
\]
\[
\int_0^\infty t\,\nu_1(dt)=\frac{\gamma+\alpha}{c\sqrt{\gamma(\gamma+2\alpha)}}-\frac1c,\quad
\int_0^\infty t^2\,\nu_1(dt)=\frac{\alpha^2}{c[\gamma(\gamma+2\alpha)]^{3/2}}.
\]
The extra deterministic \(|x|/c\) completes the mean formula and has no variance. The same calculation shows that the endpoint-averaged mean is \(1/\gamma\), as it must be for the independent killing clock.

## Verification
A standalone SciPy-based checker is included as `telegraph_posterior_check.py`. It integrates independently the previously published joint space-time density, including its ballistic boundary singularity, and compares the resulting conditional Laplace transform with the closed transform and two independently integrated Lévy exponents. It also integrates the measures' masses and first two moments, tests the unconditional mean, and independently checks the boundary-atom formula. Executing the packaged script completed **72 numerical comparisons** without assertion errors. These computations are finite consistency checks, not a substitute for the transform proof, Frullani identity, or Bessel Laplace identity above.

## Relationship to prior work
Orsingher and Marchione, *Killing random motions with finite velocity* (arXiv:2610.15094v1, publicly submitted 2026-10-10), established the Laplace distribution of \(Z\) (their Theorem 4, equation (28)) and the complete joint distribution of \((Z,T)\), including its ballistic component (equations (45)--(48)). Those important formulas **are prior work**. The present result does **not** claim a new joint density or a new marginal. Its additional structural assertion is the explicit **finite** Lévy--Khintchine factorization of the posterior time distribution into two independent compound-Poisson delays, with positive explicit jump kernels, endpoint-distance semigroup and exact posterior sampling/coupling consequences. The cited joint density determines these conditional distributions abstractly but does not state this factorization. Deriving finite Lévy positivity and its Bessel jump measure requires the separate analysis in Steps 2--4.

Cinque, *A Note on the Conditional Probabilities of the Telegraph Process* (arXiv:2202.01904), studies conditioning on velocities, reversal counts, and earlier fixed-time positions. Ratanov and Kolesnik's *Symmetric Telegraph Process on the Line* (2022) supplies background resolvent transforms. The first-passage work on generalized telegraph motions studies a different first-crossing observable and its compound-Poisson representation. The exact posterior decomposition could conceivably be implicit in earlier resolvent/telegraph literature, which remains the main originality qualification.

## Limitations
The decomposition applies to symmetric one-dimensional telegraph motion under independent exponential killing (or independent thinning at switches), not to general non-Markov velocity renewal laws or position-dependent killing. It describes regular conditional laws defined via a continuous density ratio; conditioning at an exact endpoint is interpreted in that sense. Source equation (48) already gives the full joint law, so the incremental contribution is a stochastic factorization and its consequences, not information unavailable from that joint law in principle. Independent review of the originality comparison has not been performed.

## References
1. E. Orsingher and M. M. Marchione, *Killing random motions with finite velocity*, arXiv:2610.15094v1 (2026), Sections 2--4, particularly equations (28), (45)--(48). https://arxiv.org/html/2610.15094v1
2. F. Cinque, *A Note on the Conditional Probabilities of the Telegraph Process*, arXiv:2202.01904 (2022). https://arxiv.org/abs/2202.01904
3. N. Ratanov and A. D. Kolesnik, *Symmetric Telegraph Process on the Line*, in *Telegraph Processes and Option Pricing*, Springer (2022), pp. 31--64, DOI:10.1007/978-3-662-65827-7_2.
4. M. M. Marchione and E. Orsingher, *Dirichlet problems and exit distributions for the telegraph process and its planar extensions*, arXiv:2605.05430v1 (2026). https://arxiv.org/abs/2605.05430
