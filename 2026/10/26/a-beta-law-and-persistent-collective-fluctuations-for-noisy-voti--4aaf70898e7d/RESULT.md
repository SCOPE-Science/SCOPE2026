# A beta law and persistent collective fluctuations for noisy voting on growing stars

## Finding
Fix any \(a>0\). On a star with hub \(0\) and \(m\ge1\) leaves, assign spins \(\sigma_i\in\{-1,+1\}\). Independently at each vertex, at rate one replace its spin by that of a uniformly chosen neighbor; also flip that spin at rate \(a\). The finite continuous-time chain is irreducible, so it has a unique stationary law. Let \(H_m=\sigma_0\) and \(X_m=m^{-1}\sum_{i=1}^{m}\sigma_i\). Put
\[
b=1+2a>1,\qquad \nu=\frac{b^2-1}{2b^2}\in(0,1/2).
\]
Then the stationary joint laws converge as \(m\to\infty\):
\[
(X_m,H_m)\Rightarrow(X,H),\qquad \frac{1+bX}{2}\sim\operatorname{Beta}(\nu,\nu),\qquad
\Pr(H=+1\mid X=x)=\frac{1+bx}{2}.
\]
In particular, the limiting marginal density of \(X\) is
\[
f_b(x)=\frac{b}{B(1/2,\nu)}(1-b^2x^2)^{\nu-1}\mathbf1_{\{|x|<1/b\}}.
\]
Here \(B\) is the Euler beta integral. The limit has no endpoint atoms, and every positive noise rate has a nondegenerate macroscopic leaf magnetization:
\[
\lim_{m\to\infty}\operatorname{Var}(X_m)=\frac1{2b^2-1}>0.
\]
The hub–leaf and distinct-leaf correlations are **exactly**, for every \(m\ge2\),
\[
\mathbb E(H_m\sigma_i)=\frac{b(m+1)}{m(2b^2-1)+1},\qquad
\mathbb E(\sigma_i\sigma_j)=\frac{m+1}{m(2b^2-1)+1}\quad (i\ne j).
\]
Thus the whole joint stationary limit, not merely its variance, is identified.

## Assumptions and scope
The graph is the unweighted star with \(m\) leaves; every vertex has **total** copying rate one (a hub chooses one leaf uniformly, whereas each leaf has only the hub as neighbor). Noise is an independent spontaneous **flip** at rate \(a>0\), rather than a rerandomization at that rate. Rerandomization at rate \(2a\) is equivalent to this flipping convention for binary spins. All claims concern equilibrium, and \(a\) is fixed as \(m\to\infty\). With \(a=0\), the finite chain is not irreducible and the theorem is not asserted.

## Proof
**1. Exact finite correlations.** Global spin-flip symmetry gives \(\mathbb E H_m=\mathbb E\sigma_i=0\). Permutation symmetry of leaves makes \(u=\mathbb E(H_m\sigma_i)\) independent of \(i\), and \(v=\mathbb E(\sigma_i\sigma_j)\) independent of distinct \(i,j\). Apply the finite generator to a hub–leaf product and a distinct leaf–leaf product. The noise terms contribute \(-4a\) times the corresponding correlation, and the copying terms give
\[
0=1+\frac1m+\frac{m-1}{m}v-2(1+2a)u,\qquad
0=2u-(2+4a)v.
\]
Hence \(u=bv\), \(v=(m+1)/[m(2b^2-1)+1]\), as claimed. In particular, since distinct leaves have correlation \(v\),
\[
\operatorname{Var}(X_m)=\frac1m+\frac{m-1}{m}\frac{m+1}{m(2b^2-1)+1}
\longrightarrow\frac1{2b^2-1}.
\]

**2. Exact reduced generator and limit.** Let \(h\in\{-1,+1\}\), \(x=(2k-m)/m\) when \(k\) leaves have spin \(+1\), and denote by \(F(x,h)\) a smooth function. Put \(\Delta=2/m\). The exact reduced generator is
\[
\begin{aligned}
\mathcal L_mF(x,h)={}&\frac{m(1-x)}2\left(a+\frac{1+h}2\right)[F(x+\Delta,h)-F(x,h)]\\
&+\frac{m(1+x)}2\left(a+\frac{1-h}2\right)[F(x-\Delta,h)-F(x,h)]\\
&+\frac{b-hx}{2}[F(x,-h)-F(x,h)].
\end{aligned}
\]
At inaccessible boundary lattice points the associated rate is zero, so the displayed expression is well defined. Uniform Taylor expansion on the compact state space gives, for every polynomial \(F\),
\[
\mathcal L_mF\longrightarrow\mathcal LF
=(h-bx)\,\partial_xF+\frac{b-hx}{2}[F(x,-h)-F(x,h)]
\]
uniformly on admissible grid points, with an \(O_F(m^{-1})\) remainder. The limiting operator describes a piecewise-deterministic process; only its stationary identities are required.

**3. Stationary moment determination.** Let \(\pi_m\) be the reduced stationary distribution, a measure on the compact space \([-1,1]\times\{-1,+1\}\). Along any weakly convergent subsequence, \(\pi_m\Rightarrow\pi\); stationarity and the preceding uniform convergence show \(\int\mathcal L F\,d\pi=0\) for every polynomial \(F\). Write \(M_j=\mathbb E_\pi X^j\). Applying \(\mathcal L\) to \(x\) and \(h\) gives \(\mathbb E H=bM_1\) and \(M_1=b\mathbb E H\); since \(b>1\), \(M_1=\mathbb E H=0\). For every integer \(k\ge0\), applying the operator to \(x^{k+1}\) yields
\[
\mathbb E(HX^k)=bM_{k+1}.
\]
For \(k\ge1\), apply it also to \(hx^k\):
\[
0=kM_{k-1}-(k+1)b\mathbb E(HX^k)+M_{k+1},
\quad\Longrightarrow\quad
M_{k+1}=\frac{k}{(k+1)b^2-1}M_{k-1}.
\]
Thus all odd moments vanish and, for every integer \(j\ge1\),
\[
M_{2j}=\prod_{r=1}^{j}\frac{2r-1}{2rb^2-1}.
\]

**4. Identification of the entire joint law.** If \(Y\sim\operatorname{Beta}(\nu,\nu)\), then \(X=(2Y-1)/b\) has the above even moments because \(2\nu=1-b^{-2}\), and has zero odd moments. Conditional on this \(X\), choose \(H=+1\) with probability \((1+bX)/2\), so \(\mathbb E(H\mid X)=bX\). This construction matches **every** mixed monomial moment \(\mathbb E(H^rX^k)\), using \(H^2=1\) and the relation in step 3. Polynomials in \(x\), separately for the two hub signs, determine measures on the compact product space (e.g., by Weierstrass approximation). Hence every subsequential \(\pi\) is this same joint law, proving full convergence. The beta transform gives the density in the finding and its positive variance. No unproved diffusion approximation, independence assumption among leaves, or finite-enumeration extrapolation is used.

## Verification
The standalone `verify.py` builds the exact \(2(m+1)\)-state hub/count generator, solves its stationary linear system for several \(m\) and \(a\), and checks normalization, stationarity residuals, exact hub–leaf and leaf–leaf second moments, and convergence of second, fourth and sixth magnetization moments toward the beta values. Run `python verify.py` with the versions specified in `requirements.txt`. An observed pass verifies only those finite instances; the argument in the Proof establishes the infinite-volume statements.

## Relationship to prior work
Cox, Peres and Steif (arXiv:1408.5122, originally public on 21 August 2014) studied noisy voter dynamics on a star and derived the **same reduced finite Markov chain** at rerandomization rate one (our \(a=1/2\)); their Theorem 2 and Section 4 concern mixing and nonstandard initial-state effects. The current finding concerns a fixed-noise **stationary joint beta limit** and closed finite second correlations; it neither claims discovery of the star reduction nor extends their mixing theorem. Carro, Toral and San Miguel (arXiv:1602.06935) studied the impact of network heterogeneity using an annealed approximation for uncorrelated random networks, rather than this exact singular-hub stationary limit. Pymar and Rivera (arXiv:2112.01478) studied asymptotic stationary noisy-voter densities on other graph families and noted that a star violates one Gaussian-convergence condition. Beta-binomial laws on a complete interaction graph are also known, but those have different fixed-noise large-population behavior and do not state this star's compact-support beta law. These comparisons support the stated scope, not a claim of exhaustive priority.

## Limitations
The graph must be a star, the total copying rate at every vertex must equal one, and the spontaneous-flip rate \(a\) must remain fixed and positive. The theorem does not establish a convergence rate for the full joint law, time-dependent mixing, a fluctuating-noise scaling, or an analogous beta law for other hub geometries. Prior-art uncertainty remains for general stochastic hybrid-process transformations and less accessible exact star stationary calculations.

## References
1. J. T. Cox, Y. Peres, J. E. Steif, *Cutoff for the noisy voter model*, arXiv:1408.5122 (first public 2014-08-21); *Annals of Applied Probability* 26 (2016), 917–932; doi:10.1214/15-AAP1108.
2. A. Carro, R. Toral, M. San Miguel, *The noisy voter model on complex networks*, arXiv:1602.06935 (first public 2016-02-22); *Scientific Reports* 6 (2016), 24775; doi:10.1038/srep24775.
3. R. Pymar, N. Rivera, *Asymptotic behaviour of the noisy voter model density process*, arXiv:2112.01478 (first public 2021-12-02).
4. B. L. Granovsky, N. Madras, *The noisy voter model*, *Stochastic Processes and their Applications* 55 (1995), 23–43 (historical model reference, not inspected in full).
