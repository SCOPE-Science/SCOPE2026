# Poisson micropaint islands in a weakly diffusive run-and-tumble trajectory

## Finding

Consider the one-dimensional run-and-tumble process
\[
 X_t=v\int_0^t\sigma_s\,ds+\sqrt{2D}\,B_t,
\]
where \(v>0\), \(D>0\), \(B\) is standard Brownian motion, and the independent orientation \(\sigma\in\{+1,-1\}\) flips at rate \(q>0\). Initially \(X_0=0\) and \(\sigma_0=+1\). At every spatial level \(x\geq0\), color the level by its orientation at first arrival: \(S_x=\sigma_{\tau_x}\), where \(\tau_x=\inf\{t\geq0:X_t=x\}\). All levels are eventually reached almost surely. Spatial transition-point conventions are immaterial for colored lengths; the field has a right-continuous modification.

**Theorem.** Set \(s_D=\sqrt{v^2+2Dq}\). For each \(D>0\), the positive-half-line first-arrival color field is a two-state continuous-time Markov chain in the *spatial* variable, with generator (rows and columns ordered \(+,-\))
\[
 K_D=\begin{pmatrix}-a_D&a_D\\b_D&-b_D\end{pmatrix},\qquad
 a_D=\frac{q}{s_D+v},\qquad b_D=\frac{s_D+v}{2D}.
\]
This fixed-parameter Markov-ladder fact is an explicit specialization of established Markov-additive first-passage theory, not the asserted novelty. The new singular-limit conclusion concerns entire counter-oriented color islands, rather than one-point first-passage probabilities.

For a fixed \(R>0\), let \((u_j^{(D)},\ell_j^{(D)})\) be the starting level and full length of each maximal negative-color interval with start in \((0,R)\). As \(D\downarrow0\), the random marked point measure
\[
 \sum_{j:u_j^{(D)}\in(0,R)}
  \delta_{(u_j^{(D)},\,\ell_j^{(D)}/D)}
 \ \Longrightarrow\ \operatorname{PPP}\!\left(
 \frac{q}{2v}\,du\otimes v e^{-vz}\,dz\right)
\]
on \((0,R)\times(0,\infty)\). Thus the microscopic negative-color islands have limiting spatial start intensity \(q/(2v)\), and their lengths divided by \(D\) have independent exponential marks of rate \(v\).

In particular, for the negative-colored length \(M_D(R)=\int_0^R\mathbf 1_{\{S_x=-1\}}\,dx\),
\[
 \frac{M_D(R)}D\Longrightarrow Y_R=\sum_{j=1}^{N_R} Z_j,
 \quad N_R\sim\operatorname{Poisson}\!\left(\frac{qR}{2v}\right),
 \quad Z_j\overset{\mathrm{iid}}\sim\operatorname{Exp}(v),
\]
with independence of the count and marks and convergence of every positive integer moment. In particular,
\[
 \mathbb E[e^{-\theta Y_R}]
  =\exp\left[-\frac{qR}{2v}\frac{\theta}{v+\theta}\right],\quad \theta\geq0,
 \qquad
 \mathbb E[Y_R]=\frac{qR}{2v^2},\quad
 \operatorname{Var}(Y_R)=\frac{qR}{v^3}.
\]
Already for fixed \(D>0\), the probability of no counter-oriented paint on \((0,R)\) is exactly
\[
 \Pr(M_D(R)=0)=e^{-a_D R}\ \longrightarrow\ e^{-qR/(2v)}.
\]
Hence the minority-colored area vanishes as \(D\downarrow0\), but the chance that at least one minority island occurs in a fixed interval stays strictly positive.

## Assumptions and scope

The parameters \(v,q,R\) remain fixed and positive while \(D\) decreases to zero. The orientation flip process is a genuine two-state continuous-time Markov chain of flip rate \(q\), independent of the Brownian noise. The coloring records first arrival at each *positive* spatial level after an indefinitely long physical observation; this is not a finite-time painting claim. The initial orientation is \(+1\); another initial orientation produces an additional possible microscopic initial interval. In the convention of Sezik and collaborators, the reported tumbling parameter is \(\alpha=2q\), with physical diffusivity \(D_x=D\) and speed \(\nu_0=v\).

## Proof

**1. Almost-sure arrival and spatial Markov property.** Observe the particle after pairs of successive orientation flips. The displacement over each complete pair is the sum of a positive run, a negative run, and an independent Brownian increment. These paired increments are iid, symmetric, nondegenerate, have mean zero, and have finite positive variance. Their random walk is unbounded above and below almost surely, implying that the continuous process reaches every prescribed finite level in each direction. For \(0\leq x<y\), the strong Markov property at \(\tau_x\) and spatial translation invariance give
\[
 \Pr(S_y=j\mid S_x=i,\{S_z:0\leq z\leq x\})
 =\Pr_{0,i}(\sigma_{\tau_{y-x}}=j).
\]
Here a regular conditional version of the displayed identity suffices; it follows first for finitely many record levels and then for the generated sigma-field. The transition matrices therefore form a conservative homogeneous semigroup in the level variable.

**2. Exact spatial generator.** For each terminal orientation, form the column vector of its hitting probabilities as a function of the remaining distance \(h\geq0\). The backward equations are
\[
 D f''(h)-v\operatorname{diag}(1,-1)f'(h)+Qf(h)=0,
 \quad Q=\begin{pmatrix}-q&q\\q&-q\end{pmatrix},
\]
with the corresponding identity boundary data at \(h=0\) and boundedness as \(h\to\infty\). The characteristic polynomial has roots \(0\) (twice) and \(\pm s_D/D\). Removing the linearly growing and exponentially increasing solutions leaves exactly a constant and one decaying mode, uniquely fixed by the two boundary values. Direct substitution gives the stochastic transition matrix \(P_D(h)=e^{hK_D}\), where the stated \(K_D\) satisfies
\[
 D K_D^2-v\operatorname{diag}(1,-1)K_D+Q=0,
 \quad K_D\mathbf 1=0,
 \quad a_D,b_D>0.
\]
The uniqueness just established identifies this matrix with the first-arrival orientation semigroup. On a compact level interval, only finitely many physical orientation flips occur before its last hitting time. Thus the color field has finitely many spatial switches; assigning one-sided values at these random boundaries yields a standard right-continuous version without changing integrals or complete interval lengths.

**3. Exact color-interval structure.** A two-state spatial Markov chain alternates independent positive-color run lengths with \(\operatorname{Exp}(a_D)\) laws and negative-color run lengths with \(\operatorname{Exp}(b_D)\) laws. Since the initial color is positive, the first interval is positive. The identities
\[
 a_D=\frac{q}{\sqrt{v^2+2Dq}+v}\ \longrightarrow\ \frac{q}{2v},
 \qquad
 D b_D=\frac{\sqrt{v^2+2Dq}+v}{2}\ \longrightarrow\ v
\]
show that positive intervals have nondegenerate limiting lengths, while negative intervals shrink linearly in \(D\).

**4. Marked point-process limit, including boundary control.** Use independent unit exponential variables \(E_j,F_j\) for every \(D\), representing successive positive intervals by \(E_j/a_D\) and negative intervals by \(F_j/b_D\). For each fixed index, the start of the corresponding negative interval converges almost surely to \(\sum_{k\leq j}E_k/(q/(2v))\), and its width divided by \(D\) converges almost surely to \(F_j/v\). These limiting start locations are arrival times of a Poisson process of rate \(q/(2v)\). On \((0,R)\) the limiting number of arrivals is finite almost surely, and no arrival coincides with \(R\). The coupling therefore proves convergence of the finite marked point configurations, including the stated intensity and exponential mark law. If the final negative interval straddles \(R\), its truncated length differs from its full width, but this event has probability tending to zero: on any fixed window the start intensity is bounded uniformly and the negative width tends to zero in probability. Hence integrating the actual colored subset of \((0,R)\) gives the stated compound-Poisson limit. Starting in the positive color also proves the exact empty-window probability \(e^{-a_D R}\).

**5. Transform and moments.** For every \(\theta\geq0\), the finite-\(D\) Feynman–Kac formula is
\[
 \mathbb E_+[e^{-\theta M_D(R)/D}]
 = (1,0)\exp\!\left(R\left[K_D-
 \frac{\theta}{D}\operatorname{diag}(0,1)\right]\right)\binom{1}{1}.
\]
The characteristic polynomial of the tilted matrix is
\[
 \lambda^2+\left(a_D+b_D+\frac\theta D\right)\lambda+
 \frac{a_D\theta}{D}=0.
\]
Its slow eigenvalue tends to \(-q\theta/(2v(v+\theta))\), its fast eigenvalue tends to negative infinity, and the slow-mode coefficient in the initial-positive expectation tends to one. This independently yields the limiting Laplace transform. For a fixed sufficiently small \(z\in(0,v)\), the same two-eigenvalue calculation with \(\theta=-z\) shows that the moment generating functions are uniformly bounded for all sufficiently small \(D\), with limit \(\exp[(qR/(2v))z/(v-z)]\). Uniform exponential integrability then gives convergence of all positive integer moments. Differentiating the compound-Poisson transform gives the stated mean and variance.

## Verification

The independent standard-library program `checker.py` tests the generator's backward-equation identities, stochastic-rate positivity, agreement of the limiting color fraction with the published long-time half-line volume ratio, finite-window Feynman–Kac transforms and their singular limit, and two seeded Monte Carlo comparisons. It passed 202 numerical assertions plus 50,000 simulated finite-window samples. The proof of the spatial point-process limit relies on the explicit exponential coupling, not on finite simulations.

One further exact finite-diffusivity cross-check follows from the color-chain semigroup: \(\Pr(S_x=-1)=\frac{a_D}{a_D+b_D}(1-e^{-(a_D+b_D)x})\) and consequently
\[
 \mathbb E[M_D(R)]
 =\frac{a_D}{a_D+b_D}\left(R-\frac{1-e^{-(a_D+b_D)R}}{a_D+b_D}\right).
\]
Dividing by \(D\) and taking \(D\downarrow0\) gives \(qR/(2v^2)\), agreeing with the limiting compound-Poisson mean. The stationary negative-color fraction \(a_D/(a_D+b_D)=(s_D-v)/(2s_D)\) also agrees with the color fraction implicit in the previously published long-time positive-half-line volume coefficients.

## Relationship to prior work

Sezik, Britton, Touma and Pruessner (2026) define the same first-arrival color/paint observable, derive time-dependent orientation-resolved visit probabilities and long-time expected painted volumes, and note minority islands of order \(D/v\) separated by longer majority-color stretches. These facts and the one-point color fraction are prior work. Their inspected model, results, discussion and appendices do not state the marked spatial island process, its exact nonzero small-noise intensity, the compound-Poisson rescaled minority area, or the empty-window limit.

The fact that first-passage phases of a Markov-modulated Brownian motion form a spatial Markov ladder chain is long established, notably by D'Auria, Ivanovs, Kella and Mandjes (2009/2010). Their matrix-exponent approach is the general theory underlying the explicit two-state generator above. The 2026 Latouche chapter also advertises this general ladder property; its complete text was not available for comparison. The assessed mathematical addition is specifically the weak-diffusivity *marked Poisson limit for the first-arrival paint geometry* and the associated rescaled area/empty-window laws, not the general Markov-ladder theorem or standard Poisson/exponential formulas in isolation.

## Limitations

The theorem is strictly for one-dimensional, freely moving, two-state run-and-tumble dynamics with independent constant diffusivity and flip rate. It does not cover sticky boundaries, confining forces, interactions with deposited paint, finite physical observation time, correlations between the painted positive and negative half-lines, or a simultaneous growing-window limit. Its singular limit excludes zero propulsion speed and zero flip rate. General Markov-additive theory may allow other derivations of the exact finite-parameter ladder generator; publication-priority uncertainty remains for the specialized microscopic island limit. An independent audit has not been performed.

## References

- E. Sezik, C. Britton, A. Touma and G. Pruessner, *Run, Tumble and Paint*, first public preprint 25 March 2026, arXiv:2603.24277, https://arxiv.org/abs/2603.24277. In particular Sections II, IV, V and the appendices.
- B. D'Auria, J. Ivanovs, O. Kella and M. Mandjes, *First passage process of a Markov additive process, with applications to reflection problems*, originally circulated 2009, arXiv:1006.2965, https://arxiv.org/abs/1006.2965. In particular the first-passage phase semigroup and matrix exponent.
- G. Latouche, *Markov-Modulated Brownian Motion: The Matrix-Analytic Perspective*, Chapter 2, *First Passage Across a Level*, 2026, https://doi.org/10.1007/978-3-031-98576-8_2 (abstract accessible; chapter text not verified).
