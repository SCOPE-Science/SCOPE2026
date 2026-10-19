# Sharp coexistence and critical hub extinction under clique coarsening

## Finding
For a competitive Lotka–Volterra population on a graph consisting of a universal hub and a disjoint union of peripheral cliques of sizes \(q_1,\ldots,q_r\), where \(r\ge2\), the exact coexistence threshold \(\tau_c\in(0,1)\) is the unique root of
\[
 H_{\mathbf q}(\tau_c)=1,\qquad H_{\mathbf q}(\tau)=\tau\sum_{j=1}^r\frac{q_j}{1+\tau(q_j-1)}.
\]
Every strictly positive trajectory approaches the all-positive equilibrium for \(0<\tau<\tau_c\), and the hub-free, peripheral-positive equilibrium for \(\tau_c\le\tau<1\). At equality the hub goes extinct algebraically with the exact universal coefficient
\[
\lim_{t\to\infty}t h(t)=\frac{1}{1-\tau_c},
\]
and every peripheral vertex \(v\) in clique \(j\) obeys
\[
\lim_{t\to\infty}t\left[x_v(t)-\frac{1}{1+\tau_c(q_j-1)}\right]
=-\frac{\tau_c}{(1-\tau_c)[1+\tau_c(q_j-1)]}.
\]
Merging any two peripheral cliques strictly raises the coexistence threshold. These claims hold for arbitrary clique sizes and arbitrary strictly positive initial abundances in the physical unit cube.

## Assumptions and scope
Let \(r\ge2\), \(q_j\in\mathbb Z_{\ge1}\), and \(m=\sum_j q_j\). The graph has \(m+1\) vertices: one distinguished hub adjacent to all other vertices, and the remaining vertices divided into \(r\) disjoint complete graphs. Every edge is undirected and unweighted; there are no other edges. Fix the competitive pressure \(0<\tau<1\). On this graph study
\[
\dot x_v=x_v\left(1-x_v-\tau\sum_{u\sim v}x_u\right),\qquad x_v(0)\in(0,1].
\]
Write \(h\) for the hub abundance and \(y_{j,k}\), \(1\le k\le q_j\), for the peripheral abundances. Define \(d_j=1+\tau(q_j-1)>0\), \(H=\tau\sum_j q_j/d_j\). The state cube is forward invariant, and strictly positive coordinates stay strictly positive at finite times. An equilibrium with all positive coordinates is called full coexistence. The threshold here concerns full coexistence and its attracting outcome; it does not identify a finite-population stochastic threshold.

## Proof
**1. Threshold and equilibria.** Since
\[
 H'(\tau)=\sum_{j=1}^{r}\frac{q_j}{[1+\tau(q_j-1)]^2}>0,\quad H(0)=0,\quad\lim_{\tau\uparrow1}H(\tau)=r>1,
\]
there is a unique \(\tau_c\in(0,1)\) with \(H(\tau_c)=1\). At any equilibrium where every peripheral coordinate is positive, two vertices in the same clique obey identical equilibrium equations; subtracting them gives \((1-\tau)(y_{j,k}-y_{j,\ell})=0\). Thus the peripheral abundances in clique \(j\) all equal \(y_j\), with
\[
 y_j=\frac{1-\tau h}{d_j}.
\]
The hub equation, if \(h>0\), becomes \(h=1-\tau\sum_j q_jy_j=1-H+\tau Hh\). Therefore
\[
 h_*=\frac{1-H}{1-\tau H},\qquad y_{j,*}=\frac{1-\tau h_*}{d_j}.
\]
For \(H<1\), \(0<h_*<1\) and \(y_{j,*}>0\). For \(H=1\), the only candidate has \(h=0\). For \(H>1\), a formal root with positive \(h\) would require \(1-\tau H<0\), but it then satisfies \(h>1/\tau\), forcing \(y_j<0\). At \(1-\tau H=0\), the hub equation is inconsistent because \(1-H<0\). Hence the full-coexistence equilibrium exists exactly when \(\tau<\tau_c\). The peripheral-positive hub-free equilibrium always is
\[
 E_0:\quad h=0,\qquad y_{j,k}=d_j^{-1}.
\]

**2. Positive trajectories do not lose peripheral species.** Summing over clique \(j\), put \(S_j=\sum_k y_{j,k}\). Directly,
\[
\dot S_j=(1-\tau h)S_j-\tau S_j^2-(1-\tau)\sum_k y_{j,k}^2
\ge (1-\tau)S_j-S_j^2,
\]
using \(0\le h\le1\) and \(\sum y^2\le S_j^2\). Scalar comparison gives \(\liminf_{t\to\infty}S_j(t)\ge1-\tau>0\). For any two positive vertices of the same clique,
\[
\frac{d}{dt}\log\frac{y_{j,k}}{y_{j,\ell}}=-(1-\tau)(y_{j,k}-y_{j,\ell}).
\]
Consequently the maximum/minimum ratio within each clique is nonincreasing and finite; together with the lower bound on \(S_j\), this bounds every peripheral coordinate away from zero for sufficiently large time. The log ratio actually tends to zero: were its nonincreasing limit positive, the displayed derivative of the extreme log ratio, and the uniform lower coordinate bound, would force a persistent strictly negative derivative. Thus each omega-limit set has strictly positive and equal peripheral abundances inside each clique.

**3. Global convergence.** Put \(M=I+\tau A\) for the symmetric adjacency matrix \(A\), and define the smooth potential
\[
\Phi(x)=\sum_v x_v-\tfrac12x^{\mathsf T}Mx.
\]
Along every solution,
\[
\dot\Phi(x)=\sum_v x_v[1-(Mx)_v]^2\ge0.
\]
The invariant cube is compact. The omega-limit set lies among equilibria (LaSalle invariance), whose peripheral components are strictly positive by Step 2. Thus it is contained in the finite set \(\{E_0,E_+\}\) if \(\tau<\tau_c\), and in \(\{E_0\}\) otherwise. Because every trajectory's omega-limit set is connected, each converges to one equilibrium. When \(H<1\), \(E_0\) cannot attract a trajectory with \(h(0)>0\): near \(E_0\) the hub satisfies \(\dot h/h=1-h-\tau\sum y_{j,k}\to1-H>0\), contradicting \(h(t)\to0\). Hence \(E_+\) attracts every strictly positive trajectory below threshold; \(E_0\) attracts every strictly positive trajectory at and above it. Moreover, the leaf-leaf diagonal blocks of \(M\) are \(P_j=(1-\tau)I_{q_j}+\tau\mathbf 1\mathbf1^{\mathsf T}\), all positive definite. Their Schur complement on the hub is \(1-\tau H>0\) when \(H<1\). Hence \(M\) is positive definite there, and \(J(E_+)=-\operatorname{diag}(E_+)M\) has strictly negative eigenvalues, proving local asymptotic stability.

**4. Critical coefficients.** At \(\tau=\tau_c\), set \(d_j=1+\tau_c(q_j-1)\), \(u_{j,k}=d_j^{-1}\), \(z_{j,k}=y_{j,k}-u_{j,k}\), and regard \(z\) as the peripheral vector. Step 3 proves \((h,z)\to(0,0)\). The leaf equations have the expansion
\[
 \dot z=Lz+bh+R(z,h),\qquad L=-DP,\qquad b=-\tau_c D\mathbf1,
\]
where \(D=\operatorname{diag}(u)\), \(P\) is block diagonal with blocks \((1-\tau_c)I+\tau_c\mathbf1\mathbf1^{\mathsf T}\), and \(\|R(z,h)\|\le C(\|z\|+h)^2\) near zero. Every eigenvalue of \(L\) has negative real part because \(L\) is similar to the symmetric negative definite matrix \(-D^{1/2}PD^{1/2}\). The hub obeys
\[
\frac{\dot h}{h}=-h-\tau_c\sum z_{j,k}\longrightarrow0,
\]
since the constant part \(1-\tau_c\sum q_j/d_j\) is zero. Set \(w=z/h\), well-defined for all finite time. Dividing the leaf equation by \(h\) gives
\[
\dot w= Lw+b+E(t)w+e(t),\qquad\|E(t)\|+\|e(t)\|\to0.
\]
Indeed the quadratic remainder divided by \(h\) consists of coefficients bounded by \(C(\|z\|+h)\) times \(1+\|w\|\), and the term from differentiating \(1/h\) is \(-(\dot h/h)w\). Stability of \(L\), variation of constants, and a small-coefficient perturbation bound imply \(w\to-L^{-1}b=-P^{-1}\tau_c\mathbf1\), i.e.
\[
\lim_{t\to\infty}\frac{z_{j,k}(t)}{h(t)}=-\frac{\tau_c}{d_j}.
\]
Therefore
\[
 \lim_{t\to\infty}\frac{\dot h}{h^2}=-1-\tau_c\sum_{j,k}\lim\frac{z_{j,k}}h=-1+\tau_c H(\tau_c)=-(1-\tau_c).
\]
Integrate \(\frac{d}{dt}(1/h)=-\dot h/h^2\) and divide by \(t\), giving \(t h\to1/(1-\tau_c)\). Multiplication by the established leaf-to-hub ratios gives the asserted peripheral limits.

**5. Strict benefit of coarsening.** For integers \(p,q\ge1\) and \(0<\tau<1\), direct common-denominator subtraction gives
\[
\frac{p}{1+\tau(p-1)}+\frac{q}{1+\tau(q-1)}-\frac{p+q}{1+\tau(p+q-1)}
=\frac{pq\tau[2+(p+q-2)\tau]}{[1+\tau(p-1)][1+\tau(q-1)][1+\tau(p+q-1)]}>0.
\]
Replacing two cliques by their union strictly lowers \(H_{\mathbf q}(\tau)\) at each \(\tau\in(0,1)\). Since the old and new \(H\) are strictly increasing, and the new partition still has at least two cliques, its root \(\tau_c\) strictly increases. For the terminal partition with one clique, the graph is complete and full coexistence persists at every \(0<\tau<1\); the threshold is \(1\). In particular, for six peripheral vertices, the coarsening chain has exact thresholds
\[
 \tau_c(1,1,1,1,1,1)=\tfrac16<\tau_c(2,2,2)=\tfrac15<\tau_c(4,2)=\frac{2\sqrt2-1}{7}<\tau_c(6)=1.
\]

## Verification
The standalone program `verify.py` performs symbolic checks of the equilibrium identities, Schur-complement expression and critical eigenvector for seven partitions; independently derives the stated threshold examples and verifies the clique-merge sign. Numerical ODE integrations in the program corroborate the asymptotic coefficient and below/above-threshold equilibrium limits, but are not used as proof. Run `python verify.py` after installing the packages in `requirements.txt`. The continuous-time global and critical conclusions are established by Steps 2–4, not by finite-time computations.

## Relationship to prior work
Mooij, Baudena, von der Heydt, Miele and Kryven (2026) establish the identical-interaction competitive Lotka–Volterra model, the general \([1/\Delta,1]\) stability interval and star/complete extremizers, and provide a general equilibrium inversion method. They report clustering–robustness associations under **degree-preserving** network rewiring. The present exact clique-partition interpolation, hub-extinction outcome for arbitrary positive initial states, strict merger comparison and critical amplitudes concern a structured graph class; **clique mergers change peripheral degrees** and therefore are not an extension of the paper's degree-preserving empirical comparison. Mooij and Kryven (2025) investigate competition dynamics and independent-set selection through broader dynamical methods; the present threshold and center-direction coefficients are not stated in their inspected full text. General symmetric Lotka–Volterra Lyapunov methods and equilibrium inversion are established mathematics rather than claimed as new.

## Limitations
The classification assumes a single universal hub, disconnected clique subgraphs on the periphery, strictly equal symmetric competitive interactions, and \(0<\tau<1\). It does not assert monotonicity under arbitrary triangle addition, degree-preserving rewiring, heterogeneous coefficients, arbitrary graphs, or finite stochastic population dynamics. The coarsening comparison changes peripheral degrees. At \(\tau=1\) the system has additional degeneracies not covered by the theorem. The mathematical novelty assessment is subject to possible overlap with more general ecological equilibrium results; independent audit and independent historical-priority verification have not been performed.

## References
1. M. N. Mooij, M. Baudena, A. S. von der Heydt, L. Miele, I. Kryven, *A dynamic mechanism for prevalence of triangles in competitive networks* (2026), arXiv:2603.17584v1, https://arxiv.org/abs/2603.17584; *Bulletin of Mathematical Biology* **88**, article 156, https://doi.org/10.1007/s11538-026-01726-z.
2. M. N. Mooij and I. Kryven, *Finding large independent sets in networks using competitive dynamics* (2025), *Communications Physics*, https://doi.org/10.1038/s42005-025-02153-7.
3. M. N. Mooij et al., *Stable coexistence in indefinitely large systems of competing species* (2024), arXiv:2404.14031, https://arxiv.org/abs/2404.14031 (abstract-level background only).
