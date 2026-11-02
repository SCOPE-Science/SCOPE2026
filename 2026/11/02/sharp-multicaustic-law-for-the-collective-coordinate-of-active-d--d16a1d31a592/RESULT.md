# Sharp multicaustic law for the collective coordinate of active Dyson particles

## Finding

In the zero-temperature harmonic active Dyson model with \(N\ge3\) independent, symmetrically flipping propulsion signs, the stationary center of mass has a distribution *independent of the pair-repulsion strengths*. Its density exhibits a sharp, exactly calculable \(N+1\)-site caustic transition at the flip-to-trap ratio \(\alpha=1/N\). Below the transition, all \(N+1\) sites carry divergent power-law peaks with explicit and generally unequal left and right coefficients. At the transition, all \(N-1\) interior peaks become logarithmic, whereas the two endpoints retain finite one-sided nonzero density. Above it, the density is bounded and continuous and vanishes at the edges.

Here is a precise version. Set
\[
\alpha=\frac{\gamma}{\mu},\qquad b_\alpha=\frac{2^{\alpha-1}\Gamma(\alpha+1/2)}{\sqrt\pi},\qquad c_k=2k-N\quad(0\le k\le N).
\]
Write \(M=N^{-1}\sum_{i=1}^N X_i\) for the stationary center and let \(g_N\) be the density of \(S=\mu NM/v\). For \(0<\alpha<1/N\), its right- and left-hand local expansions at each interior \(c_k\), \(1\le k\le N-1\), are
\[
 g_N(c_k+q)\sim A_{k,+}q^{N\alpha-1},\quad
 g_N(c_k-q)\sim A_{k,-}q^{N\alpha-1}\quad(q\downarrow0),
\]
where
\[
 A_{k,+}={N\choose k}\frac{b_\alpha^N\Gamma(1-N\alpha)}{\Gamma((N-k)\alpha)\Gamma(1-(N-k)\alpha)},\qquad
 A_{k,-}={N\choose k}\frac{b_\alpha^N\Gamma(1-N\alpha)}{\Gamma(k\alpha)\Gamma(1-k\alpha)}.
\]
At the two endpoints, from inside the support,
\[
 g_N(-N+q)\sim g_N(N-q)\sim\frac{b_\alpha^N}{\Gamma(N\alpha)}q^{N\alpha-1}.
\]
All coefficients are positive, and \(g_N\) is locally smooth away from the displayed caustic sites. The physical density of \(M\) is \((\mu N/v)g_N(\mu Nm/v)\).

At \(\alpha=1/N\), for every interior \(k\),
\[
 g_N(c_k+q)\sim g_N(c_k-q)\sim {N\choose k}\frac{b_{1/N}^{N}}{\Gamma(k/N)\Gamma((N-k)/N)}\log\frac1q,
\]
while \(\lim_{s\downarrow-N}g_N(s)=\lim_{s\uparrow N}g_N(s)=b_{1/N}^N\) and the density is zero outside \([-N,N]\). For \(\alpha>1/N\), \(g_N\) extends continuously to the whole real line with \(g_N(-N)=g_N(N)=0\).

## Assumptions and scope

Fix an integer \(N\ge3\), trap relaxation \(\mu>0\), propulsion speed \(v>0\), and flip rate \(\gamma>0\). The zero-temperature equations are
\[
 \dot X_i=-\mu X_i+v\sigma_i+\sum_{j\ne i}F_{ij},\qquad \sigma_i\in\{-1,+1\},
\]
with independent stationary telegraph processes whose individual signs flip at rate \(\gamma\). Assume pair forces cancel exactly, \(F_{ij}=-F_{ji}\), and a stationary joint regime exists. The active Dyson models I and II of Touzo, Le Doussal, and Schehr satisfy these force conditions, including repulsive logarithmic forces; the result also applies to any symmetric translation-invariant pair potential for which the dynamics is well posed. The statement concerns the center of mass, **not** the single-particle spatial density, nor finite-temperature noise.

The caustic conclusions describe the density on \([-N,N]\). At a transition endpoint the density's value at the single endpoint itself is immaterial, whereas its one-sided limit is fixed.

## Proof

**1. Cancellation and independent stationary filters.** Sum all equations over particles. The antisymmetry of the forces gives
\[
 \dot M=-\mu M+\frac vN\sum_{i=1}^N\sigma_i.
\]
The unique stationary solution of this stable scalar equation is
\[
 \frac{\mu NM(t)}v=\sum_{i=1}^NZ_i(t),\qquad
 Z_i(t)=\mu\int_{-\infty}^t e^{-\mu(t-s)}\sigma_i(s)\,ds.
\]
The \(Z_i\) are independent and identically distributed since the telegraph processes are independent. This identity is pathwise and holds irrespective of the spatial interactions.

**2. Exact one-filter density.** Let \(p_\pm(z)\) denote the stationary joint densities of \(Z\in(-1,1)\) and its current sign. Their stationary transport equations have velocities \(\mu(\pm1-z)\) and flip terms \(\gamma(p_\mp-p_\pm)\). The summed zero-current condition gives \(p_+-p_-=z(p_++p_-)\). Substitution into either equation yields
\[
 \frac{d}{dz}\big((1-z^2)f_\alpha(z)\big)=-2\alpha zf_\alpha(z),
\]
with the equivalent logarithmic derivative \(f_\alpha'(z)/f_\alpha(z)=-2(\alpha-1)z/(1-z^2)\). Hence normalization gives
\[
 f_\alpha(z)=\frac{\Gamma(\alpha+1/2)}{\sqrt\pi\Gamma(\alpha)}(1-z^2)^{\alpha-1}\mathbf1_{\{|z|<1\}}.
\]
The normalized stationary density of \(S\) is exactly the ordinary \(N\)-fold convolution \(g_N=f_\alpha^{*N}\). As \(u\downarrow0\),
\[
 f_\alpha(1-u)\sim f_\alpha(-1+u)\sim\frac{b_\alpha}{\Gamma(\alpha)}u^{\alpha-1}.
\]

**3. Exact endpoint peaks.** For \(S=-N+q\), every constituent must lie near its lower endpoint. Each endpoint deficit is positive with leading density \(b_\alpha u^{\alpha-1}/\Gamma(\alpha)\). Repeated beta integrals for their sum give \(b_\alpha^Nq^{N\alpha-1}/\Gamma(N\alpha)\). Reflection gives the upper endpoint.

**4. Interior peaks and both unequal amplitudes.** Partition each factor into smooth interior mass and narrow lower/upper endpoint pieces. Any convolution containing a smooth interior factor is locally smooth. For a site \(c_k\), the only singular terms consist of precisely \(k\) upper and \(N-k\) lower pieces; there are \({N\choose k}\) such choices. If \(U\) is the sum of upper deficits and \(V\) the sum of lower deficits, then \(S-c_k=V-U\). Their leading respective densities are \(b_\alpha^ku^{k\alpha-1}/\Gamma(k\alpha)\) and \(b_\alpha^{N-k}v^{(N-k)\alpha-1}/\Gamma((N-k)\alpha)\). On the right, the local convolution is asymptotic to
\[
 {N\choose k}\frac{b_\alpha^N}{\Gamma(k\alpha)\Gamma((N-k)\alpha)}
 \int_0^\delta u^{k\alpha-1}(u+q)^{(N-k)\alpha-1}\,du.
\]
For \(N\alpha<1\), replacing \(u=qt\), extending the scaled upper limit to infinity, and using
\[
 \int_0^\infty t^{k\alpha-1}(1+t)^{(N-k)\alpha-1}\,dt
 =\frac{\Gamma(k\alpha)\Gamma(1-N\alpha)}{\Gamma(1-(N-k)\alpha)}
\]
gives \(A_{k,+}\). Interchanging the upper and lower groups yields \(A_{k,-}\). The substitution and dominated passage follow from \(0<k\alpha<N\alpha<1\). Terms from the next-order endpoint expansion are smaller; nonsingular terms are bounded. This establishes the claimed positive leading coefficients and the absence of any other divergent sites.

**5. Transition and regular regime.** At \(N\alpha=1\), the same local integral has integrand asymptotic to \(u^{-1}\) for \(q\ll u\ll\delta\); its coefficient is exactly the stated logarithmic coefficient on both sides. At the endpoints the step-3 convolution exponent is zero, giving the finite positive one-sided constant. If \(\alpha>1/N\), then \(f_\alpha\in L^{N/(N-1)}(\mathbb R)\), since the edge integrability condition is \((\alpha-1)N/(N-1)>-1\). Generalized Young convolution and continuity under \(L^p\) translations show that \(g_N\) is continuous and bounded. Its support is \([-N,N]\), forcing zero boundary values.

## Verification

The accompanying `verify.py` computes single-filter cell probabilities from the exact symmetric beta cumulative distribution, forms discrete convolutions, and checks normalization and both unequal \(N=3\) interior amplitudes in the \(N\alpha<1\) regime. It also compares two-point formulas and the critical logarithmic coefficient against independent numerical integration. These finite tests corroborate the analytic formulas; the all-parameter theorem follows from the preceding beta-integral and \(L^p\)-convolution proof, not from sampling.

Run with `python verify.py` after installing `numpy` and `scipy` as specified in `requirements.txt`. The code computes only finite approximations and does not certify publication novelty.

## Relationship to prior work

Touzo, Le Doussal and Schehr (2023), arXiv:2302.02937, introduced active Dyson models I and II. Their main text and supplementary material identify the center-of-mass equation and analyze singularities of the **single-particle spatial density**, including the general exponent \(N\gamma/\mu-1\) and a heuristic logarithmic critical case. These established statements are not new here. The present result instead determines the stationary law of the collective mean, establishes interaction independence, locates precisely its \(N+1\) caustics, and computes **their exact two-sided amplitudes and critical endpoint values** for every \(N\ge3\). Thus sharing an exponent does not make the two observables or their amplitude classifications identical.

Basu, Majumdar, Rosso, Sabhapandit and Schehr (2019), arXiv:1910.10083, obtained power/logarithmic transitions for a related three-internal-state harmonic run-and-tumble particle. Accordingly the analogous three-site \(N=2\) phenomenon is **excluded from the novelty claim**. The exact multidimensional \(N\ge3\) collection of coefficients and pair-interaction-independent collective-coordinate interpretation are the claimed contribution. General theorems on convolutions of algebraic endpoint densities may supply reusable proof principles, and the result is not asserted to invent those principles.

## Limitations

The result requires independent telegraph signs, a common harmonic relaxation rate, zero thermal diffusion, and cancellation of pair forces. Correlated flips, heterogeneous trap rates, nonharmonic traps and finite-temperature forcing are not addressed. Even when repulsion changes individual particle distributions dramatically, only the center-of-mass marginal has the stated interaction independence. The caustic exponent and generic logarithmic singularity were already anticipated for different observables in the 2023 paper. Publication priority for the precise \(N\ge3\) amplitudes has not been exhaustively established, and independent scientific review has not been performed.

## References

1. L. Touzo, P. Le Doussal and G. Schehr, *Interacting, running and tumbling: the active Dyson Brownian motion*, arXiv:2302.02937 (first public 2023-02-06), https://arxiv.org/html/2302.02937v2 ; EPL 142, 61004 (2023).
2. U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit and G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083 (2019), https://arxiv.org/html/1910.10083v1 .
3. D. Frydel, *Positing the problem of stationary distributions of active particles as third-order differential equation*, Phys. Rev. E 106, 024121 (2022), https://doi.org/10.1103/PhysRevE.106.024121 .
