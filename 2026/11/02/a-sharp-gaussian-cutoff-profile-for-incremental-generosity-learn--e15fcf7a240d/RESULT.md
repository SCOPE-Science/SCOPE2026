# A sharp Gaussian cutoff profile for incremental-generosity learning

## Finding

For every fixed number \(k\ge2\) of ordered generosity levels, the incremental-generosity-tuning count chain has an exact leading total-variation mixing threshold, an \(O(m)\) cutoff window, and a Gaussian transition profile for homogeneous endpoint initial conditions. Its sharp rate depends on the exact first nonzero eigenvalue

\[
\gamma=a+b-2\sqrt{ab}\cos(\pi/k)>0.
\]

Let \(d_m(t)\) denote the maximum total-variation distance to stationarity over all count-vector initial states and put \(t_m=m\log m/(2\gamma)\). Then

\[
\lim_{c\to+\infty}\limsup_{m\to\infty}d_m(\lfloor t_m+cm\rfloor)=0,\qquad
\lim_{c\to-\infty}\liminf_{m\to\infty}d_m(\lfloor t_m+cm\rfloor)=1.
\]

For the count vector with all \(m\) adaptive agents initially at generosity level \(i\in\{1,k\}\), a stronger fixed-window profile holds:

\[
\lim_{m\to\infty}\left\|P_m^{\lfloor t_m+cm\rfloor}(me_i,\cdot)-\Pi_m\right\|_{\rm TV}
=2\Phi\!\left(\frac{|\psi(i)|e^{-\gamma c}}2\right)-1,
\quad c\in\mathbb R.
\]

Here \(\Phi\) is the standard normal cumulative distribution function and \(\psi\) is defined explicitly in the next section. The result is a specialization to strategy-learning dynamics; it is not a claim of a new general product-chain cutoff principle.

For the originating \(k\)-IGT repeated-game model, write \(n\) for the total population, \(\alpha\) for its unconditional-cooperator fraction, \(\beta\) for its unconditional-defector fraction, and \(m=(1-\alpha-\beta)n\) for the number of adapting players. At fixed \(\alpha,\beta,k\), with \(\beta\in(0,1)\), \(\alpha\ge0\), \(\alpha+\beta<1\), and \(m\) integer, the leading cutoff location in *total pair interactions* is

\[
\boxed{\frac{n\log m}{2[1-2\sqrt{\beta(1-\beta)}\cos(\pi/k)]}},
\]

and the window is \(O(n)\). In particular its leading \(n\log n\) coefficient has no \(\alpha\)-dependence.

## Assumptions and scope

Fix \(k\ge2\), \(a,b>0\), \(a+b\le1\), and an integer \(m\ge2\). The state space is

\[
\Delta_{k,m}=\{z\in\mathbb Z_{\ge0}^k:\sum_{j=1}^k z_j=m\}.
\]

At each discrete step, \(z\mapsto z-e_j+e_{j+1}\) with probability \(az_j/m\) for \(1\le j<k\), and \(z\mapsto z+e_{j+1}-e_j\) with probability \(bz_{j+1}/m\). All remaining probability is assigned to staying at \(z\). These are precisely the source's normalized birth--death count transitions. Reversibility gives the multinomial equilibrium

\[
\Pi_m(z)=\frac{m!}{\prod_j z_j!}\prod_{j=1}^k\pi_j^{z_j},\qquad
\pi_j=\frac{(a/b)^{j-1}}{\sum_{r=0}^{k-1}(a/b)^r}.
\]

Set \(q=\sqrt{b/a}\) and \(\vartheta=\pi/k\). An explicit eigenfunction with eigenvalue \(-\gamma\) for the one-agent continuous-time generator is

\[
u_j=q^{j-1}[\sin(j\vartheta)-q\sin((j-1)\vartheta)],\quad 1\le j\le k.
\]

Normalize it by \(\psi_j=u_j/(\sum_{r=1}^k\pi_r u_r^2)^{1/2}\). Thus \(\sum_j\pi_j\psi_j=0\) and \(\sum_j\pi_j\psi_j^2=1\); both endpoint values are nonzero. In the unbiased three-level example \(k=3\), \(a=b=1/4\), this gives \(\gamma=1/4\), \(\psi=(\sqrt{3/2},0,-\sqrt{3/2})\) and

\[
\lim_{m\to\infty}\left\|P_m^{\lfloor2m\log m+cm\rfloor}(me_1,\cdot)-\Pi_m\right\|_{\rm TV}
=2\Phi\!\left(\sqrt{3/2}\,e^{-c/4}/2\right)-1.
\]

All limits in this finding hold with fixed \(k,a,b\) or fixed game-population fractions, not with \(k\) growing with \(m\).

## Proof

**1. One-agent spectrum.** Let \(Q\) be the generator on \(\{1,\ldots,k\}\) whose forward moves have rate \(a\) and backward moves rate \(b\), with suppressed moves at the two endpoints. The detailed-balance equations \(\pi_j a=\pi_{j+1}b\) hold. Conjugating \(Q\) by \(\operatorname{diag}(\sqrt\pi)\) gives a real symmetric tridiagonal matrix with off-diagonal \(\sqrt{ab}\). In the interior, the eigenvector substitution \(f_j=q^{j-1}g_j\) reduces the eigenvalue equation to

\[
 g_{j+1}+g_{j-1}=2\cos\vartheta\,g_j.
\]

The left reflecting boundary gives \(g_j=\sin(j\vartheta)-q\sin((j-1)\vartheta)\). The right boundary becomes

\[
[2\cos\vartheta-q-q^{-1}]\sin(k\vartheta)=0.
\]

The nonstationary solutions \(\vartheta=r\pi/k\), \(r=1,\ldots,k-1\), give distinct eigenvalues

\[
\gamma_r=a+b-2\sqrt{ab}\cos(r\pi/k).
\]

Together with the eigenvalue zero, these are the complete spectrum. The first nonzero eigenvalue \(\gamma_1=\gamma\) is simple and strictly less than all others. The displayed \(u\) gives the corresponding eigenfunction; \(u_1=\sin\vartheta\) and \(u_k=-q^k\sin\vartheta\), so no endpoint projection vanishes.

**2. Independent-coordinate continuous-time chain.** Label the \(m\) adaptive agents and let each independently evolve under \(Q\) for time \(s\). The count vector has continuous-time generator \(m(P_m-I)\). The labeled stationary distribution is \(\pi^{\otimes m}\), and its count pushforward is \(\Pi_m\). If all agents initially occupy level \(i\), their common one-agent law is \(p_i(s)=e_i e^{sQ}\). Orthogonal spectral expansion yields

\[
\frac{p_i(s)_j}{\pi_j}=1+e^{-\gamma s}\psi(i)\psi(j)
+\sum_{r=2}^{k-1}e^{-\gamma_r s}\psi_r(i)\psi_r(j).
\]

Set \(s=(\log m)/(2\gamma)+c\). Because every \(\gamma_r>\gamma\) when \(r\ge2\), uniformly over the finite level set,

\[
\frac{p_i(s)_j}{\pi_j}=1+m^{-1/2}e^{-\gamma c}\psi(i)\psi(j)+o(m^{-1/2}).
\]

For \(m\) independent observations under \(\pi\), a Taylor expansion of the log likelihood ratio and the central limit theorem give a Gaussian limiting log-likelihood with mean \(-v^2/2\) and variance \(v^2\), where \(v=|\psi(i)|e^{-\gamma c}\). The corresponding tilted law has mean \(+v^2/2\). Uniform integrability follows from the exact second-moment product bound. Therefore the total-variation distance tends to \(2\Phi(v/2)-1\). Crucially, the product likelihood ratio depends only on the counts \(z_j\), so passing from labeled configurations to count vectors loses **no** total variation in this homogeneous initial condition.

**3. Universal upper bound.** For an arbitrary labeled initial configuration, each one-agent density has squared \(L^2(\pi)\) distance bounded by \(C e^{-2\gamma s}\), where \(C=\max_i\sum_{r=1}^{k-1}\psi_r(i)^2\) is finite because \(k\) is fixed. Multiplication of independent-coordinate chi-squared factors gives

\[
\chi^2(\mathcal L(X(s))\|\pi^{\otimes m})
\le(1+C e^{-2\gamma s})^m-1
\le \exp(Ce^{-2\gamma c})-1.
\]

The bound descends to count vectors. Consequently the maximum continuous-time total-variation distance tends to zero as \(c\to+\infty\), whereas the endpoint Gaussian limit tends to one as \(c\to-\infty\).

**4. Exact transfer to discrete interactions.** The discrete labeled chain has transition operator \(\mathsf P=I+m^{-1}\sum_{h=1}^m Q_h\), where \(Q_h\) acts on only the \(h\)-th coordinate. Tensor products of the one-agent orthonormal eigenfunctions diagonalize both the discrete transition and the independent-coordinate continuous semigroup. If a tensor eigenmode has \(H\) nonconstant coordinates and total decay rate \(L=\sum_{h=1}^m\gamma_{r_h}\), its discrete multiplier after \(t\) interactions is \((1-L/m)^t\), versus \(e^{-Lt/m}\) in continuous time. At \(t=\lfloor m\log m/(2\gamma)+cm\rfloor\), modes with fixed \(H\) have vanishing squared \(L^2(\pi^{\otimes m})\) multiplier difference, even after their \(O(m^H)\) multiplicity is included, since \(e^{-2Lt/m}\le O(m^{-H})\) and \(\log(1-L/m)=-L/m+O(H^2/m^2)\).

The remaining modes are controlled uniformly: for \(L\le m\), their squared difference is at most \(4e^{-2Lt/m}\), so the sum over \(H>M\) is bounded by a Poisson-series tail \(4\sum_{H>M} A_c^H/H!\) for a finite constant \(A_c\). For \(L>m\), the largest one-agent rate satisfies \(\gamma_{k-1}<2\), so \(|1-L/m|\le\rho<1\) uniformly over this range, and its contribution is at most \(O(k^m B^m\rho^{2t})=o(1)\) for a fixed \(B\). First letting \(m\to\infty\), then \(M\to\infty\), establishes convergence to zero of the squared \(L^2\) difference between discrete- and continuous-time labeled laws at the matched times, uniformly over initial configurations. Total-variation contraction under the count map transfers the bounds and the endpoint Gaussian profile to the discrete count chain.

**5. Original game parameters.** The population protocol has

\[
 a=(1-\alpha-\beta)(1-\beta),\quad b=(1-\alpha-\beta)\beta,
 \quad m=(1-\alpha-\beta)n.
\]

Substituting in \(m\log m/(2\gamma)\) cancels the common factor \(1-\alpha-\beta\), producing exactly the claimed \(n\log m\) center. The model-specific interpretation concerns time to approach the *stationary distribution of generosity levels*, not convergence of the repeated-game payoffs to a Nash equilibrium.

## Verification

The standalone file `verify.py` reconstructs the one-agent matrices for \(k=2,\ldots,9\) under four positive rate pairs. It checks detailed balance, the exact trigonometric eigenvalue formula and the first nonconstant eigenvector against independent matrix eigensolvers. It then builds the \(k=3\) count transition matrices at five population sizes and verifies their probability rows and the multinomial stationarity equations. Finally it iterates finite count chains at three centered times for each of \(m=20,40,80\), in both unbiased and asymmetric cases, and compares the distances with the Gaussian limit.

For \(k=3\), \(a=b=1/4\), the computed center-window distances at \(c=0\) for \(m=20,40,80\) were respectively \(0.465601\), \(0.463397\), \(0.461712\), while the limiting expression is \(0.459709\). These finite experiments corroborate but do not replace the preceding proof. Run `python verify.py` after installing the two packages named in `requirements.txt`.

## Relationship to prior work

Alistarh, Chatterjee, Karrabi and Lazarsfeld derive the \((k,a,b,m)\) chain from incremental generosity tuning, give its multinomial equilibrium and mixing-time order estimates, and explicitly identify obtaining cutoff constants as future work (arXiv:2307.07297, Sections 2.2.2--2.2.3). Their results do not contain the Gaussian fixed-window limit.

Chen and Kumagai (arXiv:1701.06665) establish broad product-chain cutoff criteria and provide two-state examples. Such general theory anticipates the existence and scale of cutoff once a one-agent spectrum is known; neither its broad criteria nor the inspected examples supply the reflecting, asymmetric \(k\)-level Gaussian endpoint profile or the game-fraction cancellation in this theorem. The general framework is acknowledged, not claimed as newly discovered.

Classical multi-urn Hamming-graph cutoff profiles (e.g. Hora 1997) use a different one-agent transition graph. Chen, Fang and Sheu (2012) give general results titled *The cutoff phenomenon for Ehrenfest chains*; only accessible bibliographic and abstract material was available for that particular source, so unobserved specialization is a residual originality risk.

## Limitations

The total-variation profile is proved for both homogeneous endpoint initial states, **not** for arbitrary initial empirical mixtures. The maximum-distance theorem identifies its cutoff center and order of window, but makes no assertion that its exact window profile equals one of the endpoint curves. All parameters other than population size are fixed; the bounds do not imply uniformity in growing \(k\), vanishing transition probabilities, or varying population fractions. General Markov product-chain cutoff machinery partly anticipates the cutoff phenomenon, and mathematical novelty is claimed for this model's explicit spectrum-dependent constant, endpoint profiles and associated strategic-population cancellation, not for product-chain cutoff as an abstract concept. Independent verification has not been performed.

## References

1. D. Alistarh, K. Chatterjee, M. Karrabi, J. Lazarsfeld, *Game Dynamics and Equilibrium Computation in the Population Protocol Model*, first arXiv version 14 July 2023, https://arxiv.org/abs/2307.07297 ; published in PODC 2024, DOI 10.1145/3662158.3662768.
2. G.-Y. Chen and T. Kumagai, *Cutoffs for product chains*, arXiv:1701.06665, 2017; Stochastic Processes and Their Applications 128 (2018), 3840--3879, DOI 10.1016/j.spa.2018.01.002.
3. G.-Y. Chen, Y.-J. Fang and Y.-C. Sheu, *The cutoff phenomenon for Ehrenfest chains*, Stochastic Processes and Their Applications 122 (2012), 2830--2853, DOI 10.1016/j.spa.2012.05.003.
4. A. Hora, *The Cut-Off Phenomenon for Random Walks on Hamming Graphs with Variable Growth Conditions*, Publications of the Research Institute for Mathematical Sciences 33 (1997), 695--710, DOI 10.2977/prims/1195145152.
