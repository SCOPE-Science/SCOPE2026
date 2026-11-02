# A universal optimal-tumbling crossover at the double-well active barrier

## Finding
For the single run-and-tumble particle in the quartic potential \(U_a(x)=(x^2-a^2)^2/4\), with fixed propulsion speed \(v>0\) and orientation-flip rate \(\gamma>0\), the stationary-density barrier-crossing **proxy** \(\tau_a(\gamma)=1/[vP_{a,\gamma}(0)]\), as defined by Basu, Majumdar and Rosso, has **exactly one** global minimizer for every \(0<a<a_c\), where
\[
a_c=\left(\frac{3\sqrt3 v}{2}\right)^{1/3}.
\]
For \(\varepsilon=a_c-a\downarrow0\), let \(z_*=1+W_0(-1/(2e))=0.7680390470\ldots\), where \(W_0\) is the real principal Lambert function. The unique optimal flip rate and optimal barrier proxy satisfy
\[
\boxed{\displaystyle
\gamma_*(a)\sim\frac{a_c\sqrt{2a_c\varepsilon}}{\pi}\,z_*,\qquad
\min_{\gamma>0}\tau_a(\gamma)\sim
\frac{\pi}{a_c\sqrt{2a_c\varepsilon}}\frac{2e^{z_*}-1}{z_*}.}
\]
In particular, tuning the flip rate to the vanishing square-root scale avoids the stretched-exponential/Vogel--Fulcher--Tammann growth of this stationary-density proxy at every fixed positive flip rate. This is a claim about the precise stationary-density proxy, **not** an identity with an exact first-passage mean.

More strongly, with \(\delta_\varepsilon=\sqrt{2a_c\varepsilon/3}\), for every fixed \(z>0\), uniformly on compact \(z\)-sets,
\[
\boxed{\displaystyle
\lim_{\varepsilon\downarrow0}
\left[\frac{z\sqrt3a_c\delta_\varepsilon}{\pi}\;
\tau_{a_c-\varepsilon}\!\left(\frac{z\sqrt3a_c\delta_\varepsilon}{\pi}\right)\right]
=2e^z-1.}
\]
The two terms \(e^z-1\) and \(e^z\) arise from different singular spatial regions: a nearly blocked inner barrier and the remote turning-point boundary, respectively.

## Assumptions and scope
Fix \(v>0\) and \(0<a<a_c\). The orientation \(\sigma_t\in\{-1,+1\}\) flips at constant Poisson rate \(\gamma>0\); position evolves by \(\dot X_t=f_a(X_t)+v\sigma_t\), with \(f_a(x)=a^2x-x^3\). There is no added Brownian noise or reset. The uniquely accessible connected stationary support is \([-\ell_a,\ell_a]\), where \(\ell_a>a\) is the unique positive solution of \(f_a(\ell_a)=-v\). The relevant stationary density \(P_{a,\gamma}\) is the normalized marginal density on this support; the observable is \(\tau_a(\gamma)=1/(vP_{a,\gamma}(0))\), not the mean of any explicitly killed process. The run-and-tumble convention has separate \(+\to-\) and \(-\to+\) flip rates both equal to \(\gamma\).

## Proof
**1. Exact integral and strict convexity.** The known zero-current stationary formula (Basu--Majumdar--Rosso, Eqs. (4), (5) and (14)) gives, writing \(B_a(x)=v^2-f_a(x)^2\) and \(G_a(x)=\int_0^x f_a(u)/B_a(u)\,du\),
\[
\tau_a(\gamma)=2v\int_0^{\ell_a}\frac{\exp(2\gamma G_a(x))}{B_a(x)}\,dx.
\tag{1}
\]
On \([0,\ell_a)\), \(B_a>0\). Let \(s_a=-f'_a(\ell_a)>0\). Taylor expansion as \(h\downarrow0\) gives \(B_a(\ell_a-h)=2vs_ah+O(h^2)\) and \(G_a(\ell_a-h)=(2s_a)^{-1}\log h+C_a+O(h)\). Thus (1), and its first two derivatives in \(\gamma\), converge for each \(\gamma>0\). In particular,
\[
\tau_a''(\gamma)=8v\int_0^{\ell_a}\frac{G_a(x)^2\exp(2\gamma G_a(x))}{B_a(x)}\,dx>0.
\tag{2}
\]
The turning-point contribution gives \(\tau_a(\gamma)\to\infty\) as \(\gamma\downarrow0\). Also \(G_a(x)>0\) for \(0<x<a\), since \(f_a(x)>0\) there, so \(\tau_a(\gamma)\to\infty\) as \(\gamma\to\infty\). Continuity and (2) show there is exactly one positive, nondegenerate global minimizer.

**2. Coalescing inner barrier.** The positive maximum of \(f_a\) is at \(m_a=a/\sqrt3\), with \(f_a(m_a)=2a^3/(3\sqrt3)\uparrow v\). As \(\varepsilon=a_c-a\downarrow0\) and \(\delta=\delta_\varepsilon\), uniformly for bounded \(t\),
\[
B_a(m_a+\delta t)=\frac{4a_c^4}{3}\delta^2(1+t^2+o(1)),
\qquad
2\gamma G_a(m_a+\delta t)=\frac{\gamma}{\sqrt3a_c\delta}\left(\arctan t+\frac\pi2\right)+o(1),
\tag{3}
\]
provided \(\gamma/\delta\) remains in a fixed compact subset of \((0,\infty)\). Indeed, the Taylor expansion of \(f_a\) around \(m_a\) is \(f_a(m_a+y)=f_a(m_a)-\sqrt3ay^2-y^3\); the first denominator expansion in (3) follows from \(v^2-f_a(m_a)^2=(4a_c^4/3)\delta^2+O(\delta^4)\). The integral of the leading reciprocal quadratic in \(G_a\) is an arctangent. Away from a fixed small neighborhood of \(m_a\) its contribution to \(2\gamma G_a\) is \(O(\gamma)\). Local comparison bounds \(c(\delta^2+y^2)\le B_a(m_a+y)\le C(\delta^2+y^2)\) on a fixed neighborhood justify dominated convergence after the blow-up.

Put \(q=\gamma/(\sqrt3a_c\delta)\) and \(z=\pi q\). The contribution of the neighborhood of \(m_a\), multiplied by \(\gamma\), tends to
\[
q\int_{-\infty}^{\infty}
\frac{\exp[q(\arctan t+\pi/2)]}{1+t^2}\,dt=e^{\pi q}-1=e^z-1.
\tag{4}
\]
The compact portion of the domain separated from \(m_a\) and \(\ell_a\) contributes \(O(\gamma)\) after multiplication by \(\gamma\).

**3. Remote turning-point layer.** On an interval \((\ell_a-\eta,\ell_a)\), chosen a fixed positive distance from \(m_a\), use \(h=\ell_a-x\) and the expansions in step 1. Matching from the right side of the inner layer, equation (3) implies \(2\gamma G_a(\ell_a-\eta)\to z\); the bounded outer regular part only changes this exponent by \(o(1)\). The singular layer is therefore asymptotic, after multiplication by \(\gamma\), to
\[
\gamma\,2v\int_0^\eta
\frac{e^z}{2vs_ah}h^{\gamma/s_a}\,dh
=e^z\eta^{\gamma/s_a}\longrightarrow e^z.
\tag{5}
\]
This is an **integrated boundary layer**, not a pointwise approximation: the \(1/\gamma\) divergence must be retained before sending \(\gamma\downarrow0\). Standard upper and lower comparison of \(B_a\) and \(G_a\) by their leading endpoint expansions yields (5) uniformly for \(q\) in compact positive intervals. Adding (4) and (5) proves \(\gamma\tau_a(\gamma)\to 2e^z-1\) and the displayed crossover, uniformly on compact \(z\)-sets.

**4. Global location of the optimizer.** For a fixed trial \(\gamma=\sqrt3a_c\delta z/\pi\) the crossover gives a finite limiting \(\delta\tau_a\). If a minimizing sequence had \(\gamma/\delta\to0\), the endpoint lower comparison in step 3 would give \(\tau_a\ge c/\gamma\) and hence \(\delta\tau_a\to\infty\), contradiction. If it had \(\gamma/\delta\to\infty\), restricting (1) to \(x=m_a+\delta t\) with \(1\le t\le2\) yields \(\tau_a\ge c\delta^{-1}\exp(c'\gamma/\delta)\), also a contradiction. Thus the optimizers stay in a compact positive range of \(z=\pi\gamma/(\sqrt3a_c\delta)\). Uniform convergence shows any subsequential limit minimizes \(F(z)=(2e^z-1)/z\) on \((0,\infty)\). Its derivative has numerator \(2e^z(z-1)+1\), which increases strictly from \(-1\) at \(z=0\) to infinity and has exactly one positive zero \(z_*=1+W_0(-1/(2e))\). Hence all optimizers converge to \(z_*\), yielding both sharp asymptotics.

## Verification
An independently implemented quadrature-of-ODE calculation of the original stationary-density formula evaluates \(\tau_a\) at four \(\varepsilon\)-values. Its computed scaled optimizer \(z\) decreases toward \(0.768039\ldots\) and its optimized proxy divided by the leading prediction increases toward one. The bundled `verify.py` prints the actual values and checks endpoint-cutoff stability and nearby strict minimization. These finite checks cannot certify the limiting theorem; the matched singular analysis and convexity argument above establish it.

## Relationship to prior work
Basu, Majumdar and Rosso (2025 preprint; 2026 journal) derive the exact stationary density and the proxy (1), demonstrate a numerically optimal flip rate, and find a Vogel--Fulcher--Tammann-type divergence at **fixed** positive flip rate. Their discussion states that the optimum moves downward near threshold, but neither derives the unique optimizer for every subcritical barrier nor analyzes the joint limit with flip rate of order square-root distance to threshold. Those are the contributions proved here. Guéneau, Majumdar and Schehr (2024 preprint, 2025 journal) give general mean-first-passage expressions, distinct from the stationary-density proxy used here, including double-well examples and weak-noise asymptotics; they do not provide this two-layer optimized proxy limit. The proof uses the established stationary integral and elementary analytic consequences, without claiming that general stationarity formulas or ordinary convexity are new.

## Limitations
This finding is **only** about the stationary-density barrier proxy \(1/(vP(0))\), not an exact killed-particle mean first-passage time. It applies to the specified symmetric quartic potential, one-dimensional noiseless telegraph propulsion, and \(0<a<a_c\) at fixed \(v>0\). The limiting formulas require \(a\uparrow a_c\) and a jointly tuned flip rate. Uniformity under thermal noise, interactions, other potentials, or a simultaneous changing propulsion speed is not established. The numerical verifier is illustrative and uses finite cutoffs; analytic uniform estimates are the mathematical basis.

## References
1. U. Basu, S. N. Majumdar, A. Rosso, *Ergodicity Breaking in Active Run-and-Tumble Particles in a Double-Well Potential*, arXiv:2512.23641v1 (first publicly posted 2025-12-29); *APS Open Science* **1**, 000021 (2026), DOI:10.1103/jysw-w2mb. Relevant Eqs. (1)--(5), (14)--(16) and Appendix B.
2. M. Guéneau, S. N. Majumdar, G. Schehr, *Run-and-tumble particle in one-dimensional potentials: mean first-passage time and applications*, arXiv:2409.16951v1 (2024), *Physical Review E* **111**, 014144 (2025); relevant Secs. II, III and V.A.
