# Two-barrier strong-selection law for threshold-funded cooperation

## Finding

Consider the finite-population Fermi imitation process in the individual-based institutional-reward model of Duong, Durbac, and Han [1]. For every integer population size \(N\ge4\), every *partial* reward cutoff \(2\le t\le N-2\), every baseline disadvantage \(d>0\), every incentive \(\theta>0\), and every initial mixed state \(i\in\{1,\dots,N-1\}\), define \(E_i(\beta,\theta)\) to be the expected cumulative expense up to absorption, at selection intensity \(\beta>0\). Under the transition and expenditure conventions below, the following hold.

**Strong-reward regime.** If \(\theta>d\), write
\[
A=t(\theta-d),\qquad B=(N-1-t)d.
\]
For any compact \(K\subset(d,\infty)\), uniformly for \(\theta\in K\) and all initial mixed states \(i\),
\[
\boxed{E_i(\beta,\theta)=\frac{\theta N^2}{N-t}\frac{e^{\beta B}}{1+e^{\beta(B-A)}}\left[1+O_K(e^{-\beta\rho})\right],\quad \rho=\min\{d,\inf_{\theta\in K}(\theta-d)\}>0.}
\]
Thus its sharp exponential growth exponent is \(\min\{A,B\}\), not merely the statement that expected expenditure diverges. At \(A=B\), the leading coefficient is exactly half the off-crossover coefficient. The equal-barrier incentive is \(\theta_c=d(N-1)/t\). For each fixed real \(s\), putting \(\theta_\beta=\theta_c+s/(\beta t)\) yields the *crossover law*
\[
\boxed{\lim_{\beta\to\infty}\frac{E_i(\beta,\theta_\beta)}{\theta_\beta N^2 e^{\beta B}/(N-t)}=\frac{1}{1+e^{-s}}.}
\]
Both laws hold with the same leading term for every initial mixed state.

**The two finite-cost regimes.** If \(0<\theta<d\), then
\[
\boxed{\lim_{\beta\to\infty}E_i(\beta,\theta)=\theta N^2\sum_{j=1}^{\min(i,t)}\frac1{N-j}.}
\]
At the boundary \(\theta=d\), the limit is instead
\[
\boxed{\lim_{\beta\to\infty}E_i(\beta,d)=2dN^2\sum_{j=1}^{t}\frac{\min(i,j)}{N-j}.}
\]
For contrast, when the reward is paid at *all* nonabsorbing states (\(t=N-1\)) and \(\theta>d\), its strong-selection cost is finite:
\[
\lim_{\beta\to\infty}E_i^{\mathrm{full}}(\beta,\theta)=\theta N^2\sum_{j=i}^{N-1}\frac1{N-j}.
\]
In particular, omitting rewards at even one high-cooperation state can change the strong-selection scaling from finite to exponentially large.

## Assumptions and scope

There are \(N\) agents, and the Markov state \(X_n=j\) records the number of cooperators. States \(0\) and \(N\) are absorbing. Define \(u_j=j(N-j)/N^2\) for \(1\le j\le N-1\), and let the game payoff difference without subsidy be the state-independent number \(-d<0\), as in the donation and linear public-goods games of [1]. At nonabsorbing state \(j\), the transitions are
\[
\begin{aligned}
P(j,j+1)&=u_jp_j,\\
P(j,j-1)&=u_j(1-p_j),\\
P(j,j)&=1-u_j,
\end{aligned}\qquad
p_j=\begin{cases}
[1+e^{-\beta(\theta-d)}]^{-1},&1\le j\le t,\\
[1+e^{\beta d}]^{-1},&t<j\le N-1.
\end{cases}
\]
The institution pays \(\theta j\) per update at state \(j\le t\), and zero at other states. With \(\tau=\inf\{n\ge0:X_n\in\{0,N\}\}\), the exact object is
\[
E_i(\beta,\theta)=\mathbb E_i\left[\sum_{n=0}^{\tau-1}\theta X_n\mathbf1_{\{X_n\le t\}}\right].
\]
For finite \(\beta\) all nonabsorbing transition directions have strictly positive probability, so \(\tau\) and this expectation are finite. Results take \(\beta\to\infty\) with \(N,t,d\) fixed. The uniform law allows \(\theta\) to move within a fixed compact subset strictly above \(d\). No assertion is made about a simultaneous growing-population limit, mutation during the fixation episode, or state-dependent base game payoffs.

## Proof

**1. Exact Green kernel.** Write \(q_j=1-p_j\), \(r_j=q_j/p_j\), \(R_0=1\), and \(R_k=\prod_{m=1}^{k}r_m\) for \(1\le k\le N-1\). Let \(s_i=\sum_{k=0}^{i-1}R_k\), \(S=s_N\). The expected number of discrete update steps in state \(j\) starting from \(i\) is
\[
G(i,j)=\frac{s_{\min(i,j)}(S-s_{\max(i,j)})}{S\,u_jp_jR_j}.
\]
Indeed \(G(0,j)=G(N,j)=0\). Away from \(i=j\), the right-hand side is harmonic for the birth-death transition because \(p_iR_i=q_iR_{i-1}\). At \(i=j\), its jump satisfies
\[
u_j\{G(j,j)-p_jG(j+1,j)-q_jG(j-1,j)\}=1.
\]
These are exactly the transient occupation equations \((I-P_T)G=I\). The unique solution exists because every transient state can reach an absorbing boundary with positive probability. Hence
\[
E_i=\theta\sum_{j=1}^{t}jG(i,j).
\]
This expression provides an independent finite-\(\beta\) identity and fixes the normalization of *update steps*, as opposed to a continuous-time embedded jump chain.

**2. End-point competition for \(\theta>d\).** Put \(h=\theta-d>0\), \(y=e^{-\beta h}\), and \(z=e^{\beta d}\). Then
\[
R_k=\begin{cases}y^k,&k\le t,\\ y^t z^{k-t},&k>t.\end{cases}
\]
In particular \(R_t=e^{-\beta A}\) and \(R_{N-1}=e^{\beta(B-A)}\). All interior terms of \(S=\sum_{k=0}^{N-1}R_k\) are exponentially smaller than at least one of the two endpoint terms \(R_0=1\) and \(R_{N-1}\). Uniformly when \(h\ge h_0>0\),
\[
S=(1+e^{\beta(B-A)})\bigl[1+O(e^{-\beta\min(h_0,d)})\bigr].
\]
For the funded boundary state \(j=t\), the exact Green formula gives, for every \(i\ge1\),
\[
s_{\min(i,t)}=1+O(e^{-\beta h_0}),\quad
S-s_{\max(i,t)}=R_{N-1}[1+O(e^{-\beta d})],\quad
p_t=1+O(e^{-\beta h_0}).
\]
Consequently
\[
\theta tG(i,t)=\frac{\theta t}{u_t}\frac{e^{\beta B}}{S}\bigl[1+O(e^{-\beta\min(h_0,d)})\bigr]
=\frac{\theta N^2}{N-t}\frac{e^{\beta B}}{S}\bigl[1+O(e^{-\beta\min(h_0,d)})\bigr].
\]
For each \(j<t\), split the tail \(S-s_{\max(i,j)}\) into the funded-side terms (up to \(t\)) and the unfunded-side terms (above \(t\)). Relative to the displayed \(j=t\) contribution, the former is at most \(O(e^{-\beta B})\) and the latter at most \(O(e^{-\beta(t-j)h_0})\). Since \(B\ge d\), summing over finitely many \(j<t\) retains the stated error. Substituting the two-endpoint estimate for \(S\) proves the uniform formula and hence all three fixed-incentive exponential asymptotics.

**3. The crossover.** The equality \(A=B\) has the unique solution \(\theta_c=d(N-1)/t>d\). For \(\theta_\beta=\theta_c+s/(\beta t)\), one has \(\beta(B-A)=-s\) and \(\theta_\beta\to\theta_c\). Substitution in the *uniform* estimate gives the stated logistic crossover, with no unproved interchange of limits.

**4. The finite regimes.** If \(0<\theta<d\), both \(r_j=e^{\beta(d-\theta)}\) on the funded states and \(r_j=e^{\beta d}\) on the unfunded states diverge. In the exact Green kernel, \(S\sim R_{N-1}\); for \(j\le i\), \(G(i,j)\to1/u_j\), and for \(j>i\), \(G(i,j)\to0\). Multiplying by the costs proves the first finite-limit formula. At \(\theta=d\), the funded-state ratios are exactly \(r_j=1\), hence \(s_{\min(i,j)}=\min(i,j)\) for every funded \(j\); the unfunded ratios diverge, so \((S-s_{\max(i,j)})/S\to1\), and \(p_j=1/2\). Therefore \(G(i,j)\to2\min(i,j)/u_j\), proving the second finite-limit formula. Under full investment with \(\theta>d\), all up-step probabilities tend to one, so the exact occupation Green kernel tends to \(1/u_j\) for \(j\ge i\) and zero below \(i\). This gives the displayed full-invest contrast.

## Verification

The accompanying `verify.py` uses Python's standard library only. It builds absorbing transition equations and solves them by exact rational Gaussian elimination independently of the scale-function Green identity, covering \(N=4,\ldots,8\), every partial cutoff, multiple rational up/down odds, and every mixed initial state. It then uses high-precision decimal arithmetic to compare the exact Green formula against all three strong-reward barrier regimes, both finite-cost regimes, the logistic crossover, and full investment. Run `python verify.py` from the extracted package directory. The computations check finite identities and representative asymptotic accuracy; the estimates for arbitrary \(\beta\), sizes, and parameters follow from the proof, not from finite tests.

For a concrete example, take \(N=7\), \(t=3\), \(d=1\). The crossover is \(\theta_c=2\), with \(A=B=3\) and
\[
E_i(\beta,2)\sim\frac{49}{4}e^{3\beta}\qquad\text{for each }1\le i\le6.
\]
At \(\theta=3/2\), the exponent is \(3/2\), and at \(\theta=5/2\) it is \(3\). Under the full-invest cutoff \(t=6\), strong-selection expenditure instead has a finite limit.

## Relationship to prior work

Duong, Durbac, and Han [1, Sect. 2 and Sect. 3] define the individual-based cutoff incentive and derive the finite-state fundamental-matrix cost. Their theorems and strong-selection limiting statements cover cutoff \(t=1\); their cutoff \(t=2\) treatment gives matrix entries but not a sharp large-selection exponential law or crossover. The journal text and appendix were inspected, including the small-size numerical studies and the discussion of general cutoff thresholds. Thus the present statement does **not** claim the Markov model, the Green-function principle, finite-\(\beta\) resolvent representation, or the qualitative \(t=1\) divergence as new. It derives a uniform, all-cutoff, all-initial-state exponential law with its exact barrier competition and logistic transition.

Duong and Han [2] and Duong, Durbac, and Han [3] study full-invest and hybrid incentives; neither uses the partial-reward interface in the present theorem. Their strong-selection limits remain finite in the full-invest setting and do not imply the partial-funding barrier law as a stated result. Classical birth-death scale functions and potential theory [4] provide the proof mechanism; the novelty claim is the model-specific global asymptotic classification and prefactor, not the Green-kernel method itself.

## Limitations

This is an asymptotic theorem with \(N\) fixed, not a uniform assertion as population size grows. It does not quantify the expenditure under recurrent mutation, continuous-time rescaling, arbitrary game-dependent payoff gaps, or imperfect institutional information. The barrier formula assumes strictly partial funding and \(\theta>d\); finite boundary cases are treated separately. The exact model-specific priority claim remains subject to a specialist literature review because general birth-death metastability frameworks could encode equivalent formulas, even if not indexed with this incentive language. No independent validation has been carried out.

## References

1. M. H. Duong, C. M. Durbac, T. A. Han, *Cost Optimisation of Individual-Based Institutional Reward Incentives for Promoting Cooperation in Finite Populations*, Bulletin of Mathematical Biology 86, 115 (2024), DOI: 10.1007/s11538-024-01344-7; arXiv:2402.07663 (first publicly posted 2024-02-12).
2. M. H. Duong and T. A. Han, *Cost efficiency of institutional incentives for promoting cooperation in finite populations*, 2021 (full-invest reward and punishment, cited in [1]).
3. M. H. Duong, C. M. Durbac, T. A. Han, *Cost optimisation of hybrid institutional incentives for promoting cooperation in finite populations*, Journal of Mathematical Biology 87, 77 (2023), DOI: 10.1007/s00285-023-02011-6; arXiv:2212.08823.
4. Standard absorbing birth-death chain scale-function and Green-kernel construction (proved directly here; no priority claimed for this method).
