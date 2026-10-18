# Quenched Brownian independence for time-frozen elliptic Pascal bootstrap walks

## Finding

In the inclusion-induced, one-factor Markov bootstrap random walk with one *time-frozen* independent Bernoulli coefficient per subset cardinality, every uniformly elliptic choice of the coefficient probabilities admits a quenched two-coordinate invariance principle. No equality, convergence, or stationarity of those probabilities is required. Almost every realized coefficient environment gives a pair of **independent standard Brownian motions** under diffusive functional scaling.

Quantitatively, for each \(0<\varepsilon<1/2\), there is \(C_\varepsilon<\infty\) such that, for every \(N\ge2\),
\[
\mathbb E\left[\left(\frac1N\sum_{j=0}^{N-1}\zeta_j\right)^2\right]
\le C_\varepsilon N^{-\delta},\qquad
\delta=\frac{1}{32\log 2}.
\]
The expectation is over both environments and fair-walk increments. More strongly, for almost every environment \(\beta\), the predictable cross-variation satisfies
\[
\mathbb P^\beta\left(\lim_{N\to\infty}\frac1N\sum_{j=0}^{N-1}\zeta_j=0\right)=1.
\]

## Assumptions and scope

Fix \(0<\varepsilon<1/2\). Let \((p_k)_{k\ge0}\) be **any deterministic sequence** with \(p_k\in[\varepsilon,1-\varepsilon]\), and let \((\beta_k)_{k\ge0}\) be independent, \(\beta_k\sim\operatorname{Bernoulli}(p_k)\). Independently let \((\xi_j)_{j\ge1}\) be i.i.d. symmetric \(\{-1,+1\}\)-valued increments, and write
\[
S_j=\sum_{i=1}^{j}\frac{1-\xi_i}{2},\quad S_0=0,\quad
\mathcal C(s)=\{0\le k\le s:\tbinom{s}{k}\text{ is odd}\}.
\]
Define \(\zeta_0=1\) and, for \(j\ge1\),
\[
\zeta_j=(-1)^{\sum_{k\in\mathcal C(S_j)}\beta_k},\qquad
X_n=\sum_{j=1}^{n}\xi_j,\qquad
Y_n=\sum_{j=1}^{n}\zeta_{j-1}\xi_j.
\]
The environment \(\beta\) is sampled once and then held fixed for all times. The quenched law \(\mathbb P^\beta\) averages only over \(\xi\), never over \(\beta\). For almost every \(\beta\), in the Skorokhod space \(D([0,1],\mathbb R^2)\),
\[
\left(\frac{X_{\lfloor Nt\rfloor}}{\sqrt N},
      \frac{Y_{\lfloor Nt\rfloor}}{\sqrt N}\right)_{0\le t\le1}
\Longrightarrow (B_t^{(1)},B_t^{(2)})_{0\le t\le1},
\]
where \(B^{(1)}\) and \(B^{(2)}\) are independent standard Brownian motions. The analogous assertion holds on every fixed compact time interval.

## Proof

**1. A deterministic Pascal-support separation bound.** Write \(\nu(t)\) for the number of ones in the binary expansion of the nonnegative integer \(t\). Lucas' parity theorem yields
\[
\mathcal C(t)=\{k:\text{every set binary digit of }k\text{ is also set in }t\},
\qquad |\mathcal C(t)|=2^{\nu(t)}.
\]
For integers \(0\le s<t\), let \(r\) be the highest binary digit on which they differ. That digit is one in \(t\) and zero in \(s\). Exactly \(2^{\nu(t)-1}\) members of \(\mathcal C(t)\) have digit \(r\) set, and none belongs to \(\mathcal C(s)\). Therefore
\[
|\mathcal C(s)\mathbin\triangle\mathcal C(t)|\ge 2^{\nu(t)-1}.
\tag{1}
\]
This exact combinatorial lower bound is independent of the coefficient probabilities.

**2. Joint-environment two-time decorrelation.** Set \(\rho=1-2\varepsilon\in(0,1)\). For \(1\le m<n\), condition on \(S_m=s\) and \(S_n=t\). Independence of the environment coefficients gives
\[
\mathbb E_\beta[\zeta_m\zeta_n\mid S_m=s,S_n=t]
=\prod_{k\in\mathcal C(s)\triangle\mathcal C(t)}(1-2p_k).
\]
The counting process \(S_n\) is nondecreasing; its equality event has probability \(\mathbb P(S_m=S_n)=2^{-(n-m)}\). On its strict-increase event, (1) applies. Hence
\[
\big|\mathbb E_{\beta,\xi}[\zeta_m\zeta_n]\big|
\le 2^{-(n-m)}+a_n,\qquad
a_n:=\mathbb E_\xi\left[
\rho^{2^{\nu(S_n)-1}}\mathbf1_{\{S_n>0\}}\right].
\tag{2}
\]
This also covers the possibility \(p_k>1/2\), because absolute values were taken before bounding the Bernoulli character products.

**3. A polynomial bound on the exceptional binary-bit counts.** For \(n\ge16\), set \(\ell_n=\lfloor(\log_2 n)/4\rfloor\) and \(M_n=2^{\ell_n}\). Fourier inversion for a fair Bernoulli sum modulo \(M_n\), followed by \(|\cos u|\le e^{-u^2/2}\) for \(0\le u\le\pi/2\), yields
\[
\begin{aligned}
d_{\mathrm{TV}}\big(\mathcal L(S_n\bmod M_n),\operatorname{Unif}\{0,\dots,M_n-1\}\big)
&\le \frac{M_n-1}{2}\exp\left(-\frac{\pi^2 n}{2M_n^2}\right)\\
&\le \frac{n^{1/4}}2\exp(-\pi^2\sqrt n/2).
\end{aligned}
\tag{3}
\]
A uniform residue has \(\operatorname{Binomial}(\ell_n,1/2)\) set bits. Hoeffding's inequality bounds the probability of fewer than \(\ell_n/4\) ones by \(e^{-\ell_n/8}\). Coupling the two residue laws in (3), and noting that the full binary expansion has at least as many ones as its lowest \(\ell_n\) digits, gives
\[
a_n\le \frac{n^{1/4}}2e^{-\pi^2\sqrt n/2}
       +e^{-\ell_n/8}
       +\rho^{2^{\ell_n/4-1}}
       =O_\varepsilon(n^{-\delta}),\qquad \delta=\frac1{32\log2}.
\tag{4}
\]
The last term decreases stretched-exponentially; the middle term determines the displayed (deliberately conservative) polynomial exponent.

**4. Almost-sure cross-variation.** Define \(Q_N=\sum_{j=0}^{N-1}\zeta_j\). Expanding the square, using \(|\zeta_j|=1\), treating \(\zeta_0=1\) separately, and summing (2) and (4), yields
\[
\mathbb E_{\beta,\xi}[Q_N^2]
\le N+2(N-1)+2\sum_{1\le m<n<N}\big(2^{-(n-m)}+C_\varepsilon n^{-\delta}\big)
=O_\varepsilon(N^{2-\delta}).
\tag{5}
\]
Take \(N_j=\lceil j^{32}\rceil\), since \(32\delta=1/\log2>1\). By (5),
\(\sum_j\mathbb E[(Q_{N_j}/N_j)^2]<\infty\), so \(Q_{N_j}/N_j\to0\) almost surely. For \(N_j\le N\le N_{j+1}\), \(|Q_N-Q_{N_j}|\le N_{j+1}-N_j\) and \((N_{j+1}-N_j)/N_j\to0\); hence \(Q_N/N\to0\) along **all** integers. Fubini's theorem transfers this joint-almost-sure statement to almost every fixed \(\beta\), with conditional probability one over the increments.

**5. Quenched functional limit.** For each such fixed \(\beta\), the vectors \((\xi_j,\zeta_{j-1}\xi_j)\) are bounded martingale differences with predictable covariance matrix
\[
\begin{pmatrix}1&\zeta_{j-1}\\\zeta_{j-1}&1\end{pmatrix}.
\]
Their rescaled predictable bracket at time \(t\) has diagonal entries \(\lfloor Nt\rfloor/N\) and off-diagonal entry \(Q_{\lfloor Nt\rfloor}/N\). The almost-sure convergence \(Q_M/M\to0\), together with \(|Q_M|\le M\), gives uniform convergence of the bracket to \(tI_2\) on each compact time interval. Bounded jumps ensure the conditional Lindeberg condition. The martingale functional central limit theorem then yields two independent standard Brownian coordinates under \(\mathbb P^\beta\).

## Verification

The standalone program `verify_pascal.py` makes 65,904 exact finite assertions: Lucas-parity membership and the separation bound for all \(0\le s<t<256\); rational-environment checks of (2) for heterogeneous and nonfair probabilities; and an independent exact enumeration of \(\mathbb E[Q_N^2]\) for small \(N\) against the pair-covariance expansion. Execute it with `python3 verify_pascal.py` from the directory holding the file. The program uses only the Python standard library. Finite assertions are consistency evidence, not a substitute for the infinite proof above. The Fourier, Hoeffding, Borel--Cantelli, and martingale limit steps were separately proved in the displayed argument.

## Relationship to prior work

Hamza and Tournier [1], Section 4.3, Proposition 11 and Corollary 12, prove **annealed** Brownian independence for precisely the time-invariant one-factor Markov elliptic coefficient setup, and explicitly identify the corresponding quenched assertion as open. Their Lucas-based parity separation and modular-uniformity lemma motivate the quantitative estimate (2)--(4); those ingredients are not claimed as new. The present theorem supplies the stronger almost-every-environment conclusion, via a summable-square subsequence and interpolation.

Collevecchio, Hamza, Shi and Williams [2], Theorem 6, supply the general deterministic necessary/sufficient predictable-covariation criterion. That criterion alone does not verify its hypotheses for almost every randomly sampled time-frozen nonidentical coefficient sequence; (5) and the subsequent almost-sure argument establish the missing step.

The independent-by-time coefficient model and the time-frozen all-fair model are different comparisons: timewise resampling does not cover reused cardinality coefficients, and an all-fair instance does not cover arbitrarily varying elliptic probabilities. Lucas' theorem [3] and the martingale invariance principle [4] are used as established tools.

## Limitations

Uniform ellipticity and independence across coefficient cardinalities are essential assumptions of this proof. No assertion is made for probabilities tending to zero or one, for correlated coefficient environments, or for quenched fluctuation limits of the unnormalized cross-variation beyond its almost-sure vanishing. The exponent \(\delta\) is a valid nonoptimized bound, not a sharp decay rate. Priority remains subject to independent review; no independent audit has been performed.

## References

1. K. Hamza and L. Tournier, *Are random random walks normal?*, arXiv:2610.01658v1 (first public October 1, 2026), especially Introduction, Section 4.3 and Appendix B. https://arxiv.org/html/2610.01658v1
2. A. Collevecchio, K. Hamza, M. Shi and R. J. Williams, *Limit theorems and ergodicity for general bootstrap random walks*, Electronic Journal of Probability 27 (2022), article 92, DOI:10.1214/22-EJP818; arXiv:2010.16000. https://arxiv.org/abs/2010.16000
3. É. Lucas, *Théorie des fonctions numériques simplement périodiques*, American Journal of Mathematics 1 (1878), 197--240.
4. J. Jacod and A. N. Shiryaev, *Limit Theorems for Stochastic Processes*, Theorem VIII.3.11, cited here for the standard martingale functional central limit criterion.
