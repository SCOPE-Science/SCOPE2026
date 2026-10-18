# A sharp particle-number crossover for jump-activity noise in the two-site inclusion process

## Finding

For the stationary two-site symmetric inclusion process with \(N\ge 1\) conserved particles, attraction parameter \(d>0\), and unit interaction-clock normalization specified below, let \(A_t\) count **all successful jumps between the two sites** up to time \(t\), in either direction. Its mean activity rate and variance rate are exactly
\[
\mu_N(d)=\lim_{t\to\infty}\frac{\mathbb E A_t}{t}=\frac{Nd(N+2d)}{2d+1},\qquad
\nu_N(d)=\lim_{t\to\infty}\frac{\operatorname{Var}(A_t)}t=\mu_N(d)F_N(d),
\]
with the stationary activity Fano factor
\[
\boxed{F_N(d)=1+\frac{(N-1)(N+2d+1)}{(2d+1)^2(2d+3)}.}
\]
This equals one for \(N=1\) and is strictly greater than one for every \(N\ge2\). For any positive sequence \(d_N\), there is a sharp number-dependent crossover:
\[
\begin{aligned}
 d_N/N^{2/3}\to0&\quad\Longrightarrow\quad F_N(d_N)\to\infty,\\
 d_N/N^{2/3}\to c\in(0,\infty)&\quad\Longrightarrow\quad F_N(d_N)\to1+\frac1{8c^3},\\
 d_N/N^{2/3}\to\infty&\quad\Longrightarrow\quad F_N(d_N)\to1.
\end{aligned}
\]
In particular, fixed attraction parameter gives \(F_N(d)\sim N^2/[(2d+1)^2(2d+3)]\). The crossover concerns second-cumulant-to-first-cumulant ratios, not convergence of the full jump-count distribution to a Poisson law.

## Assumptions and scope

The occupied-left-site count \(K_t\) takes values \(k\in\{0,\ldots,N\}\). Each left-to-right transfer occurs at rate
\[
 a_k=k(d+N-k),
\]
and each right-to-left transfer at rate
\[
 b_k=(N-k)(d+k).
\]
The finite chain starts from its unique stationary law. The above rates fix the units of time: in the convention of Giardinà, Redig and Vafayi's \(\mathrm{SIP}(m)\) generator, the same dynamics results from \(m=2d\) after multiplying their generator by one quarter when the two-site transition kernel equals one. All rates are strictly positive when the corresponding jump is permitted, so the finite-state chain is irreducible. Its invariant distribution is the symmetric beta-binomial law
\[
 \pi_k=\binom Nk\frac{(d)_k(d)_{N-k}}{(2d)_N},\qquad 0\le k\le N,
\]
where \((u)_j=u(u+1)\cdots(u+j-1)\) and \((u)_0=1\). The activity \(A_t\) counts jumps of the occupation chain, not attempted events, self-transitions, or a signed current. Long-time limits are taken for fixed \(N,d\) before number-dependent asymptotics.

## Proof

**Stationarity and moments.** The detailed-balance relation \(\pi_k b_k=\pi_{k+1}a_{k+1}\) gives the stated beta-binomial distribution. Its factorial moments are
\[
 \mathbb E_\pi[(K)_{\underline r}]
 =\frac{(N)_{\underline r}(d)_r}{(2d)_r},\qquad 0\le r\le N,
\]
where \((K)_{\underline r}\) denotes the falling factorial. Put \(X=K-N/2\). Expansion through degree four gives
\[
 \begin{split}
 \mathbb E_\pi[X^2]&=\frac{N(N+2d)}{4(2d+1)},\\
 \operatorname{Var}_\pi(X^2)&=\frac{Nd(N-1)(N+2d)(N+2d+1)}{4(2d+1)^2(2d+3)}.
 \end{split}
\]
These identities include \(N=1\): then \(X^2\) is constant.

**A single degree-two relaxation mode.** The escape intensity (successful jumps per unit time conditional on state) is
\[
 q(k)=a_k+b_k=dN+\frac{N^2}{2}-2X^2.
\]
For the backward generator \(L\) of \(K_t\), direct evaluation of its action on the quadratic polynomial gives
\[
 L X^2=dN+\frac{N^2}{2}-(4d+2)X^2
       =-(4d+2)(X^2-\mathbb E_\pi X^2).
\]
Stationarity therefore yields
\[
 \mu_N(d)=\mathbb E_\pi q=\frac{Nd(N+2d)}{2d+1}.
\]
The centered Poisson equation \(Lh=\mu_N-q\), \(\mathbb E_\pi h=0\), has the exact solution
\[
 h(k)=-\frac{X^2-\mathbb E_\pi X^2}{2d+1}.
\]

**Counting cumulant calculation.** Let \(B\) be the off-diagonal jump-rate operator, so \((Bf)(k)=a_kf(k-1)+b_kf(k+1)\), with nonexistent endpoint terms absent. The tilted generator for activity is \(L_s=L+(e^s-1)B\). For the unique eigenvalue \(\lambda(s)\) near zero with \(\lambda(0)=0\), finite irreducibility and analyticity give
\[
 \lim_{t\to\infty}\frac{\mathbb E A_t}{t}=\lambda'(0),\qquad
 \lim_{t\to\infty}\frac{\operatorname{Var}(A_t)}{t}=\lambda''(0).
\]
Differentiation of the normalized right eigenvector at zero gives the Poisson solution \(h\), and consequently
\[
 \lambda'(0)=\mu_N,\qquad \lambda''(0)=\mu_N+2\mathbb E_\pi[Bh].
\]
Since \(B=q+L\) as operators, \(\mathbb E_\pi Lh=0\), and \(q-\mu_N=-2(X^2-\mathbb E_\pi X^2)\), we find
\[
 \mathbb E_\pi Bh=\mathbb E_\pi[qh]=\frac{2\operatorname{Var}_\pi(X^2)}{2d+1}.
\]
Thus \(\nu_N=\mu_N+4\operatorname{Var}_\pi(X^2)/(2d+1)\), which simplifies to the boxed Fano factor. This calculation counts actual jumps; the diagonal holding-time contribution \(\mu_N\) is essential.

**Sharp crossover.** In the exact excess factor, the numerator is \((N-1)(N+2d+1)\), and the denominator is \((2d+1)^2(2d+3)\). If \(d\sim cN^{2/3}\), the ratio tends to \(1/(8c^3)\). For \(d=o(N^{2/3})\), the numerator is asymptotic to \(N^2\) while the denominator is \(o(N^2)\), hence divergence. For \(d\gg N^{2/3}\), use \((N-1)(N+2d+1)=O(N^2+Nd)\) and a lower bound of order \(d^3\) on the denominator to obtain vanishing excess. This proves all stated regimes.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It independently builds the full \((N+1)\)-state generator, computes the reversible stationary probabilities, solves a rational linear Poisson system, and reconstructs the tilted-generator activity variance. It checks 54 combinations (\(1\le N\le9\) and six positive rational choices of \(d\)) using exact fractions, with generator and second-moment identities. Run `python verify.py` in the same directory. These finite tests supplement, but do not replace, the symbolic proof for all \(N,d\).

## Relationship to prior work

Giardinà, Redig and Vafayi (2009) introduced and analyzed the symmetric inclusion process, its duality, and stationary product measures; conditioning their product invariant measure on particle number gives the known beta-binomial law used here. Grosskinsky, Redig and Vafayi (2012 preprint) treated finite-graph condensate motion, including the two-site case, in a weak-diffusion scaling. Huillet (2013) studied finite birth-death and Moran chains with mutations, including spectral and invariant-measure information. Pizzoferrato's thesis (2018, §7.2) studied activity fluctuations in reservoir-driven inclusion systems, with the counting field on boundary events. The present claim is different from stationary correlations, condensate motion, Moran occupation fluctuation spectra, and open-boundary activity: it evaluates the **closed, fixed-particle, two-site total-jump variance** exactly and identifies the sharp \(N^{2/3}\) Fano-ratio crossover. This comparison does not establish global novelty; broader exact tilted-generator identities could imply the result and warrant further bibliographic scrutiny.

## Limitations

The theorem assumes exactly two sites, symmetric attractive transfers, constant \(d>0\), and stationary initial conditions. It treats only the mean and asymptotic variance of the total *unsigned* successful-jump count; it does not determine higher cumulants, finite-time count distributions, nonequilibrium boundary reservoirs, or interacting lattices with more than two sites. Poissonian Fano factor is not a Poisson limit theorem. A common rescaling of all rates rescales both cumulant rates, but not their ratio. The proof and originality assessment have not undergone independent validation.

## References

1. C. Giardinà, F. Redig and K. Vafayi, *The inclusion process: duality and correlation inequalities*, arXiv:0906.4664 (first posted 2009-06-25), especially §§2 and 4. https://arxiv.org/abs/0906.4664
2. S. Grosskinsky, F. Redig and K. Vafayi, *Dynamics of condensation in the symmetric inclusion process*, arXiv:1210.3827 (first posted 2012-10-14), especially §§2–3. https://arxiv.org/abs/1210.3827
3. T. E. Huillet, *Fluctuations Analysis of Finite Discrete Birth and Death Chains with Emphasis on Moran Models with Mutations*, International Scholarly Research Notices (2013), DOI:10.1155/2013/939308. https://doi.org/10.1155/2013/939308
4. A. Pizzoferrato, *Large Scale Dynamics and Fluctuations in Non-Equilibrium Stochastic Particle Systems*, PhD thesis, University of Warwick (2018), §7.2. https://wrap.warwick.ac.uk/104849/1/WRAP_Theses_Pizzoferrato_2018.pdf
