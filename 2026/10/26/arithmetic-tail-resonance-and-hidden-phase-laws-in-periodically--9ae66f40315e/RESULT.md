# Arithmetic tail resonance and hidden-phase laws in periodically refreshed Cox walks

## Finding
Consider a symmetric nearest-neighbor continuous-time random walk whose jump intensity is held constant for intervals of length \(\tau>0\), with independent exponential intensity redraws of mean \(\bar\lambda>0\). Start the periodic rate environment in its stationary **uniform phase**, independently of all redrawn rates. Put \(B=\bar\lambda\tau\), and define
\[
 s=\operatorname{arcosh}(1+1/B),\qquad q=e^{-s},\qquad c=(1+2B)^{-1/2}.
\]
Let \(Z_T\) be the net integer displacement in an observation interval of length \(T\). All the following limits take \(m\to\infty\) through positive integers with \(B,\tau,T\) fixed.

**Exact refresh multiples.** At one period,
\[
 \Pr(Z_\tau=m)\sim \frac{2q^m}{m}.
\]
For every fixed integer \(n\ge2\),
\[
 \Pr(Z_{n\tau}=m)\sim
 \frac{2c^{n-1}}{(n-2)!}\,m^{n-2}(\log m)q^m.
\]
**Strictly noninteger multiples.** For every integer \(n\ge1\) and \(0<\alpha<1\),
\[
 \Pr(Z_{(n+\alpha)\tau}=m)\sim
 \frac{c^n}{(n-1)!}\frac{2\log(1/(1-\alpha))}{2-\alpha}\,
 m^{n-1}q^m.
\]
In particular, the polynomial and logarithmic prefactors depend discontinuously on whether the observation length is an exact refresh multiple; this is a fixed-parameter asymptotic statement, not an assertion of discontinuity of finite-displacement probabilities in observation time.

**Hidden refresh-phase inference.** Let \(U\in(0,1)\) be the stationary elapsed fraction of the current rate block at the observation start, and put \(V=\min(U,1-U)\). At one period, conditional on \(Z_\tau=m\),
\[
 mV\ \Longrightarrow\ \operatorname{Exp}(\text{rate }c).
\]
For every fixed integer \(n\ge2\), conditional on \(Z_{n\tau}=m\),
\[
 \frac{-\log V}{\log m}\ \Longrightarrow\ \operatorname{Uniform}(0,1).
\]
In both phase laws, the nearer endpoint (\(U\to0\) or \(U\to1\)) has limiting probability \(1/2\), independent of the displayed nondegenerate limiting variable. The same statements hold conditioned on \(Z_T=-m\) by spatial symmetry.

## Assumptions and scope
Let \(U\) be uniform on \([0,1)\). The rate redraw epochs are \(\{(j-U)\tau:j\in\mathbb Z\}\); the intensities on successive periods are independent \(\operatorname{Exp}\) variables with mean \(\bar\lambda\), independent of \(U\). Conditional on this rate path, the jump times form an inhomogeneous Poisson process and every jump is independently \(+1\) or \(-1\) with probability \(1/2\). No spatial resetting takes place. The origin of \(Z_T\) is the particle's position at the start of observation. The random-phase environment is stationary under continuous time shifts. All rates, the refresh period, and each integer \(n\) are fixed positive parameters. The one-sided laws concern exact lattice masses, not density values or first-passage times.

## Proof
**1. One block.** For a single constant rate of random amplitude used over a duration \(t\), conditioning on the exponential amplitude and then the Poisson number of jumps gives the bilateral probability-generating function
\[
 F_t(z)=\mathbb E[z^{Z_t}]
 =\frac{1}{1+\bar\lambda t(1-(z+z^{-1})/2)}.
\]
Writing \(b=\bar\lambda t\), its exact lattice law is
\[
 \Pr(Z_t=j)=\frac{q_t^{|j|}}{\sqrt{1+2b}},\qquad
 q_t=\frac{b}{1+b+\sqrt{1+2b}},
\]
including the limiting atom at zero when \(t=0\). At \(t=\tau\), \(q_\tau=q\) and \(\Pr(Z_\tau=j)=cq^{|j|}\). The outer singularity of \(F_\tau\) is the simple positive pole \(z_*=q^{-1}\); there are no other singularities of this modulus on the outer boundary of the bilateral generating-function annulus.

**2. Exact uniform-phase generating function.** Put
\[
 h(z)=1+B\bigl(1-(z+z^{-1})/2\bigr).
\]
For \(T=n\tau\) and \(0<U<1\), the observation covers a first partial block of length \((1-U)\tau\), then \(n-1\) complete blocks, then a last partial block of length \(U\tau\). The two partial blocks use independent exponential rates. Consequently,
\[
 \begin{aligned}
 \mathbb E[z^{Z_{n\tau}}]
 &=h(z)^{-(n-1)}\int_0^1
 \frac{du}{[1+(1-u)(h(z)-1)][1+u(h(z)-1)]}\\
 &=\frac{2\log h(z)}{h(z)^{n-1}(h(z)^2-1)}.
 \end{aligned}
\]
The logarithm denotes the branch continued analytically from \(z=1\), where the generating function equals one; the apparent singularity at \(h=1\) is removable.

**3. Sharp local masses at integer multiples.** At \(z=z_*\), \(h(z_*)=0\). Since \(F_\tau(z)=1/h(z)=c/(1-qz)+O(1)\) there,
\[
 h(z)=c^{-1}(1-qz)[1+O(1-qz)].
\]
The preceding exact generating function therefore has singular term
\[
 -2c^{n-1}(1-qz)^{-(n-1)}\log(1-qz)
\]
when \(n\ge2\), and \(-2\log(1-qz)\) when \(n=1\). Analytic coefficient extraction on the outer boundary of the bilateral Laurent annulus yields
\[
 [z^m](-(1-qz)^{-r}\log(1-qz)))
 \sim\frac{q^m m^{r-1}\log m}{(r-1)!}\quad(r\ge1),
\]
whereas \([z^m](-\log(1-qz))=q^m/m\). Terms analytic at \(z_*\), or of a lower singular order, are negligible. This proves both exact-multiple asymptotic coefficients. One can equivalently extract the coefficients by expanding the exact one-block bilateral geometric law; thus no continuum approximation is used.

**4. Noninteger multiples.** For \(T=(n+\alpha)\tau\), split the phase integral at \(U=1-\alpha\). On \(U\in(1-\alpha,1)\), precisely \(n\) complete refresh blocks occur and the two partial lengths, in units of \(\tau\), are \(1-U\) and \(\alpha+U-1\). Evaluating the two partial-block transforms at \(z_*\), where \(F_{t\tau}(z_*)=1/(1-t)\) for \(t<1\), gives the finite positive factor
\[
 J_\alpha=\int_{1-\alpha}^1\frac{du}{U(2-\alpha-U)}
 =\frac{2\log(1/(1-\alpha))}{2-\alpha}.
\]
This sector has a pole of order \(n\), with coefficient \(c^nJ_\alpha\). On the complementary sector there are only \(n-1\) complete blocks. Its partial-block integral has at worst an additional logarithmic singularity when a partial length approaches one, so its order is at most \((1-qz)^{-(n-1)}\log(1-qz)\), strictly lower than order \(n\). Standard coefficient extraction establishes the claimed \(c^nJ_\alpha m^{n-1}q^m/(n-1)!\).

**5. Conditional phase at a single period.** As \(U=u\downarrow0\), the first partial interval has duration \((1-u)\tau\), while the final interval has duration \(u\tau\). For \(u=w/m\) with bounded \(w\ge0\), the exact one-block lattice law and its exponential tilt imply, uniformly on compact \(w\)-sets,
\[
 \Pr(Z_\tau=m\mid U=w/m)
 \sim cq^m e^{-cw}.
\]
Indeed \(-\left.\frac{d}{du}\log q_{(1-u)\tau}\right|_{u=0}=c\). Contributions from phase values bounded away from both endpoints decay faster than \(q^m\), and geometric bounds control the intervening ranges. The two endpoint layers each integrate to \(q^m/m\); conditioning on their total proves the exponential limit with rate \(c\) and the fair independent endpoint label.

**6. Log-uniform conditional phase for all \(n\ge2\).** Write \(r=n-1\). For any fixed \(0<a<b<1\), uniformly when \(u\in[m^{-b},m^{-a}]\), the complete-block sum has the local mass
\[
 \Pr(S_r=k)\sim\frac{c^r}{(r-1)!}k^{r-1}q^k,
\]
while the two partial-block increments have exponential tilt at \(z_*\) of exact mean factor \(1/[u(1-u)]\). Under this tilt the near-complete partial block has displacement of order \(u^{-1}=o(m)\); its probability of reaching order \(m\) is exponentially small in \(mu\). Uniform convolution therefore gives
\[
 \Pr(Z_{n\tau}=m\mid U=u)
 \sim\frac{c^r}{(r-1)!}\frac{m^{r-1}q^m}{u(1-u)}.
\]
Integrating over \(u\in[m^{-b},m^{-a}]\) gives \((b-a)c^r m^{r-1}q^m\log m/(r-1)!\). The reflected interval near \(u=1\) contributes identically. Divide by the full mass from step 3, whose coefficient is twice this logarithmic scale. For each \(0<a<b<1\), both endpoint labels then have limiting joint probability \((b-a)/2\) with the logarithmic coordinate in \([a,b]\). These intervals determine the asserted uniform distribution on \([0,1]\) and independence of the fair endpoint label; the total-mass asymptotic excludes escaped boundary mass.

## Verification
Run `python3 check.py` (Python standard library only). It checks the exact integrated phase transform against numerical phase quadrature for three independent mean intensities, algebraic relations among \(q,c,s\), the exact single-period lattice convolution against its \(2q^m/m\) asymptotic, the noninteger prefactor integral, and probability normalization. The recorded run passed 64 deterministic assertions. Additional independent numerical calculations of the two-period convolution for \(B=1\) gave ratios of exact mass to \(2c q^m\log(m)\) of approximately 1.0194, 1.0109, and 1.0058 at \(m=10,40,200\), respectively. Infinite-size assertions are proved by the preceding analytic calculations, not inferred from finite tests.

## Relationship to prior work
Arutkin and Reuveni (first publicly available February 14, 2023) introduced the doubly stochastic continuous-time random walk and the exponentially refreshed-rate example, and derived a generating function at refresh-aligned observation starts. Their article and supplement concern transport crossover, moments, and first-exit laws. Those models and their aligned generating functions are antecedents, not new results here. The new object is the continuously stationary, *uniformly phase-randomized* refresh environment; the new conclusions concern sharp integer-versus-noninteger extreme-displacement prefactors and the conditional latent phase laws. Pacheco-Pozo and Sokolov's CTRW large-deviation framework concerns ordinary renewal waiting times and leading rate functions rather than this stationary phase mixture, lattice prefactors, or posterior phase. Classical analytic-combinatorial transfer theorems are used as proof machinery rather than claimed as discoveries.

## Limitations
This theorem addresses independent exponentially distributed rates, symmetric unit jumps, deterministic refresh intervals, and a stationary uniform phase. It does not assert the same constants for other intensity priors, nonlattice jumps, nonperiodic redraw times, or nonstationary aligned initialization. All asymptotics fix the observation time before sending the integer displacement to infinity; uniform crossover results when a noninteger observation time approaches an integer multiple jointly with displacement are not established. The conditional labels are mathematical consequences of the model, not finite-data inference guarantees. No independent audit or exhaustive priority certification has been carried out.

## References
1. M. Arutkin and S. Reuveni, *Doubly stochastic continuous time random walk*, arXiv:2302.07041 (initial submission 2023-02-14), especially the exactly solvable model and its supplemental discussion of deterministic refreshes. https://arxiv.org/abs/2302.07041
2. A. Pacheco-Pozo and I. M. Sokolov, *Large Deviations in Continuous Time Random Walks*, arXiv:2012.09656 (2020). https://arxiv.org/abs/2012.09656
3. D. R. Cox, *Some Statistical Methods Connected with Series of Events*, Journal of the Royal Statistical Society, Series B **17** (1955), 129–164 (background on stochastic intensities).
4. P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009), singularity-transfer methods (proof technique).
