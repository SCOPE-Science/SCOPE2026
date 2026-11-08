# A global deficit identity for conjugate Brownian target distributions

## Finding

A target is drawn once at an unknown signed location; only its distance \(R>0\) matters. A Brownian searcher starts at the origin, diffuses with generator \(D\partial_{xx}\) for fixed \(D>0\), and is instantaneously returned to the origin at independent identically distributed positive waiting times, until absorption at the target. The target is **not** redrawn after a reset.

Fix any reference positive waiting-time law \(\mu_0\) with finite mean. For any probability law \(\mu\) on \((0,\infty)\), set
\[
f_\mu(x)=\mathbb E_\mu\!\left[\operatorname{erfc}\!\left(\frac{x}{\sqrt{4D\tau}}\right)\right],\qquad
Z=\int_0^\infty f_{\mu_0}(x)^2\,dx,
\qquad p_0(x)=\frac{f_{\mu_0}(x)^2}{Z}.
\]
Write \(\mathcal T_\mu\) for the expected first-detection time averaged over this **fixed-once** target-distance law \(p_0\), and \(h(x)=f_\mu(x)/f_{\mu_0}(x)\). Then, with both sides interpreted in the extended nonnegative sense when necessary,
\[
\boxed{\;
\mathcal T_\mu-\mathcal T_{\mu_0}
=\frac1{2DZ}\int_0^\infty\!\int_0^\infty
\min(x,y)f_{\mu_0}(x)f_{\mu_0}(y)
\frac{(h(x)-h(y))^2}{h(x)h(y)}\,dx\,dy\;\ge0.
\;}
\]
**Equality holds if and only if \(\mu=\mu_0\)**. Consequently the reference renewal resetting law is the unique *global* minimizer among all proper independent identically distributed positive reset-interval laws, not merely a stationary point or a minimizer in a parameterized family. In particular, non-Poisson laws may be uniquely optimal for their corresponding conjugate targets.

## Assumptions and scope

The diffusion coefficient \(D>0\) is fixed. Reset intervals are iid with proper Borel law on \((0,\infty)\), independent of Brownian motion and of the once-drawn target. The reference law satisfies \(0<\mathbb E_{\mu_0}\tau<\infty\). Competing laws need not have a finite moment; if their averaged mean time diverges, the displayed gap is \(+\infty\). Search and resetting are instantaneous and incur no relocation delay. Only one-dimensional Brownian motion, absorption upon first touching the target, and the class of iid renewal clocks are asserted. The radial target law \(p_0\) is normalized over positive distances; it may be assigned either sign, independently of distance.

## Proof

**1. Renewal mean.** Let \(Q(x,t)=\operatorname{erf}(x/\sqrt{4Dt})\) be the no-reset survival probability for \(x,t>0\), and define
\[
g_\mu(x)=\mathbb E_\mu\left[\int_0^\tau Q(x,s)\,ds\right].
\]
In a single attempt, the success probability equals \(f_\mu(x)=\mathbb E[1-Q(x,\tau)]>0\), and its expected duration is \(g_\mu(x)\). The elementary first-attempt renewal equation therefore gives the exact (possibly infinite) conditional mean \(T_\mu(x)=g_\mu(x)/f_\mu(x)\). This identity also holds for deterministic clocks.

**2. Positive Green kernel.** For each deterministic \(t>0\), let \(g_t(x)=\int_0^tQ(x,s)\,ds\) and \(f_t(x)=1-Q(x,t)\). The backward heat equation gives \(Dg_t''(x)=Q(x,t)-1=-f_t(x)\). The conditions \(g_t(0)=0\) and \(g_t'(x)\to0\) as \(x\to\infty\) yield
\[
g_t(x)=\frac1D\int_0^\infty\min(x,y)f_t(y)\,dy.
\]
All integrands are nonnegative, so Tonelli's theorem extends this identity to every positive reset law:
\[
g_\mu(x)=\frac1D\int_0^\infty\min(x,y)f_\mu(y)\,dy.
\tag{1}
\]
In particular \(f_\mu(x)\) is continuous, strictly positive for finite \(x>0\), and tends to one as \(x\downarrow0\).

**3. The reference average is finite.** Tonelli's theorem and direct Gaussian integration give
\[
\int_0^\infty f_{\mu_0}(y)\,dy=
2\sqrt{D/\pi}\,\mathbb E_{\mu_0}\sqrt\tau<\infty,
\qquad
\int_0^\infty y f_{\mu_0}(y)\,dy=D\,\mathbb E_{\mu_0}\tau<\infty.
\]
Thus \(0<Z<\infty\) and, since \(\min(x,y)\le y\),
\[
0<\mathcal T_{\mu_0}=\frac1{DZ}\iint\min(x,y)f_{\mu_0}(x)f_{\mu_0}(y)\,dx\,dy<\infty.
\]
The double integrals here and below range over \((0,\infty)^2\).

**4. Exact global gap.** Using (1), the target law and \(h=f_\mu/f_{\mu_0}\), one obtains
\[
\mathcal T_\mu=\frac1{DZ}\iint\min(x,y)f_{\mu_0}(x)f_{\mu_0}(y)\frac{h(y)}{h(x)}\,dx\,dy.
\]
The symmetric nonnegative kernel is \(K(x,y)=\min(x,y)f_{\mu_0}(x)f_{\mu_0}(y)\). Exchanging the variables and averaging gives
\[
\mathcal T_\mu=\frac1{2DZ}\iint K(x,y)
\left(\frac{h(y)}{h(x)}+\frac{h(x)}{h(y)}\right)\,dx\,dy.
\]
Subtract the finite reference mean, using the algebraic identity \(u/u'+u'/u-2=(u-u')^2/(uu')\). This yields the asserted nonnegative gap, also when the left-hand mean is infinite.

**5. Sharp uniqueness.** If the gap is zero, strict positivity of \(K(x,y)\) on \((0,\infty)^2\) forces \(h(x)=h(y)\) for almost every pair. By continuity, \(h\) is constant; because both \(f\)'s tend to one as \(x\downarrow0\), the constant equals one. Thus \(f_\mu=f_{\mu_0}\). But \(f_\mu(x)=\Pr(|B_\tau|\ge x)\) for a Brownian variable at the independent reset time; the entire law of \(|B_\tau|\) and hence its symmetric signed version is determined. Its characteristic function is \(\mathbb E_\mu[e^{-Dk^2\tau}]\). Uniqueness of Laplace transforms on positive probability laws gives \(\mu=\mu_0\). The converse is immediate.

## Verification

A standalone numerical checker, \(\texttt{verify_conjugate.py}\), tests 16 direct Green-kernel identities, seven exact Poisson-target rate formulas (two assertions each), a non-exponential mixture with the same target law, its independently integrated positive double-kernel deficit, and five contrasts against a deterministic-clock conjugate target: **37 passed assertions**. This checks normalization and integration constants; the theorem for all reset laws follows from the analytic proof, not those finite tests.

For an exponential reference clock with rate \(r_0>0\), let \(\lambda=\sqrt{r_0/D}\). Then \(f_{\mu_0}(x)=e^{-\lambda x}\), the conjugate target is \(p_0(x)=2\lambda e^{-2\lambda x}\), and \(\mathcal T_{\mu_0}=1/r_0\). For a competing exponential rate \(s>0\), \(k=\sqrt{s/D}\), the averaged time equals \(1/[Dk(2\lambda-k)]\) for \(k<2\lambda\), and is infinite for \(k\ge2\lambda\), giving a sharp illustrative uniqueness case.

## Relationship to prior work

Evans and Ray (arXiv:2410.01941, first public 2024-10-02) derive the **conjugate target law** proportional to \(f_0^2\) and the renewal mean as known premises. Their main text explicitly distinguishes the vanishing first variation from a proof that the candidate is a true minimum; it reports numerical minimization in two selected clock families. The present assertion is strictly the global, exact, nonnegative deficit identity and uniqueness over all iid reset-time laws, including heavy-tailed and singular clocks. Neither the conjugate law itself nor the renewal expression is new here.

Pal and Reuveni (arXiv:1607.06048) prove general restart identities and sharp-restart optimality for a specified underlying completion law, which is not the fixed-once random target average in the theorem. Evans and Majumdar (arXiv:1107.4225) examine optimized *spatial* resetting distributions with a Poisson reset mechanism; they do not optimize arbitrary renewal clocks in this class. García-Valladares and collaborators (arXiv:2505.16626) optimize position-dependent bulk resetting rates in a bounded search domain, and explicitly distinguish their setup from the renewal waiting-time optimization of Evans and Ray.

## Limitations

This does not prove optimality against protocols that adapt the reset interval to particle position, current search history, or elapsed absolute time; nor does it cover a target redrawn after every reset, multivariate diffusion, costly or delayed relocation, or a reference law without finite first moment. It makes no claim of novelty for the conjugate target distribution, Brownian survival formula, or renewal quotient. The exact global deficit formula may potentially be implicit in more general positive-kernel optimization results not found in the inspected sources. Independent scientific assessment has not been performed.

## References

- M. R. Evans and S. Ray, *Stochastic resetting prevails over sharp restart for broad target distributions*, arXiv:2410.01941, version 1 first public 2024-10-02. https://arxiv.org/abs/2410.01941
- A. Pal and S. Reuveni, *First Passage Under Restart*, arXiv:1607.06048 (2016). https://arxiv.org/abs/1607.06048
- M. R. Evans and S. N. Majumdar, *Diffusion with Optimal Resetting*, arXiv:1107.4225 (2011). https://arxiv.org/abs/1107.4225
- G. García-Valladares, A. Prados, A. Manacorda and C. A. Plata, *How target distributions shape optimal stochastic resetting*, arXiv:2505.16626 (2025). https://arxiv.org/abs/2505.16626
