# Sharp anomalous Fourier-mode averaging in a finite exclusion process with power-law resetting

## Finding

For each even integer \(L\ge4\), consider the symmetric simple exclusion process on a periodic ring of \(L\) sites containing exactly \(L/2\) particles. Each bond exchanges unequal occupations at rate one. At independent renewal times the *entire configuration* is reset to the deterministic half-filled step \(\eta_x^*=\mathbf 1_{\{0\le x<L/2\}}\). Successive reset waiting times are independent, with density
\[
\psi(u)=\alpha t_0^\alpha u^{-\alpha-1}\mathbf 1_{\{u\ge t_0\}},\qquad \alpha>1,\quad t_0>0.
\]
The process is observed under its stationary equilibrium-renewal law, rather than started at a fresh reset. Define its first sine density mode,
\[
F(\eta)=\sum_{x=0}^{L-1}\sin\!\left(\frac{2\pi(x+1/2)}L\right)\eta_x,
\]
and its centered time-integral \(S_T=\int_0^T(F(\eta_t)-\bar F)\,dt\). Put
\[
\lambda_L=4\sin^2(\pi/L),\quad F_*=\csc(\pi/L),\quad
\mu=\frac{\alpha t_0}{\alpha-1},\quad
f(u)=\Pr(\tau>u)=\min\{1,(t_0/u)^\alpha\},
\]
with \(f(0)=1\), and \(H(s)=\int_0^\infty e^{-su}f(u)\,du\). The stationary mean is strictly positive and exactly
\[
\bar F=\frac{F_*H(\lambda_L)}\mu.
\]
For fixed \(L,t_0\), as \(T\to\infty\), the **sharp three-regime variance law** is
\[
\boxed{\operatorname{Var}(S_T)\sim
\begin{cases}
\displaystyle\frac{2\bar F^2t_0^{\alpha-1}}{\alpha(2-\alpha)(3-\alpha)}T^{3-\alpha}, &1<\alpha<2,\\[6pt]
\displaystyle\bar F^2t_0\,T\log(T/t_0),&\alpha=2,\\[6pt]
\displaystyle\sigma_F^2T,&\alpha>2.
\end{cases}}
\]
In the last case the finite, strictly positive coefficient has the exact regenerative representation
\[
\sigma_F^2=\frac{1}{\mu}\mathbb E\left[\left(\int_0^\tau F(\eta_u^{\mathrm{SEP}})\,du-\bar F\tau\right)^2\right],
\]
where each unreset SEP segment begins from \(\eta^*\), and \(\tau\) is independent of that segment. In particular, for \(1<\alpha\le2\) the variance of the time average \(S_T/T\) decays *strictly more slowly than the ordinary inverse-time law*, despite the finite ring's exponentially mixing internal exclusion dynamics.

## Assumptions and scope

Time is continuous. At an unordered bond \(\{x,x+1\}\) (indices modulo \(L\)) particles and holes exchange at rate one; bonds at unequal occupations contribute the jump. A common renewal clock replaces the complete configuration by \(\eta^*\), independently of all future exclusion randomness. Clock interarrival durations are continuously distributed on \([t_0,\infty)\) as above, independently of SEP. The age at time zero in the stationary two-sided construction has density \(f(a)/\mu\). For the same stationary clock, the joint density of age and forward residual lifetime is \(\psi(a+r)/\mu\) for \(a,r>0\). This construction exists exactly because \(\alpha>1\). The system size remains fixed as the observation duration diverges. The modes and normalization are specified explicitly; resetting does not leave the configuration intact. No statement is made about the thermodynamic limit, or \(\alpha\le1\), or finite-time Gaussianity.

## Proof

**1. A nonvanishing exact density eigenmode.** For the generator \(\mathcal L_0\) of the unreset SEP, the one-site occupation evolves by the discrete Laplacian, and therefore
\[
\mathcal L_0F=-\lambda_LF,\qquad
\mathbb E[F(\eta_u^{\mathrm{SEP}})\mid\eta_0]=e^{-\lambda_Lu}F(\eta_0).
\]
The finite sine-sum over the initially occupied half ring gives \(F(\eta^*)=1/\sin(\pi/L)=F_*>0\). If \(A_t\) is the elapsed time since the latest reset and \(Y_t=e^{-\lambda_L A_t}\), conditioning on the entire reset clock thus gives
\[
\mathbb E[F(\eta_t)\mid\text{clock}]=F_*Y_t,
\qquad m:=\mathbb E Y_0=\frac{H(\lambda_L)}\mu.
\]
In particular \(\bar F=F_*m\).

**2. Isolate the reset-clock correlations exactly.** For \(t>0\), the law of total covariance yields
\[
C_F(t):=\operatorname{Cov}(F(\eta_0),F(\eta_t))
=F_*^2\operatorname{Cov}(Y_0,Y_t)+E_t,
\]
where \(E_t\) is the conditional SEP covariance averaged over reset histories. If a reset occurs inside \((0,t)\), independence of distinct exclusion segments makes this conditional covariance zero. Otherwise, the eigenmode property gives
\[
\operatorname{Cov}(F(\eta_0),F(\eta_t)\mid\text{clock})
=e^{-\lambda_Lt}\operatorname{Var}(F(\eta_0)\mid\text{clock}).
\]
As \(F\) is bounded on a fixed finite ring, \(0\le E_t\le B_Le^{-\lambda_Lt}\) for a finite constant \(B_L\). Hence its integrated contribution is bounded uniformly in \(T\). The divergent contribution when \(\alpha\le2\) is therefore **entirely** the stationary renewal-age covariance.

**3. Exact renewal decomposition.** Write \(g(t)=\mathbb E(e^{-\lambda_LA_t}\mid\text{a reset occurs at time zero})\). With \(k(u)=e^{-\lambda_Lu}f(u)\) and the renewal measure \(U(du)=\sum_{j\ge0}\Pr(\tau_1+\cdots+\tau_j\in du)\), the renewal equation is
\[
g=k*U,\qquad \int_0^\infty k(u)\,du=H(\lambda_L).
\]
The contribution to \(\mathbb E[Y_0Y_t]\) from having no reset in \((0,t)\) is
\[
n(t)=\frac{e^{-\lambda_Lt}}\mu\int_0^\infty e^{-2\lambda_La}f(a+t)\,da.
\]
The contribution with a first reset at residual time \(r<t\) is \((b*g)(t)\), where
\[
b(r)=\frac1\mu\int_0^\infty e^{-\lambda_La}\psi(a+r)\,da.
\]
Thus the **exact stationary identity** is
\[
h(t):=\mathbb E[Y_0Y_t]=n(t)+(b*g)(t),\qquad
\int_0^\infty b(r)\,dr=m.
\]
The function \(n\) is integrable because of its exponential factor. The first moment \(\int rb(r)\,dr\) is finite for \(\alpha>1\), by the Pareto tail \(b(r)=O(r^{-1-\alpha})\).

**4. The renewal-function asymptotic with its sharp constant.** A standard second-order finite-mean renewal theorem (in the form recalled in Doney, reference [4], equation (3)) states for \(1<\alpha\le2\) that
\[
U([0,T])=\frac T\mu+
\frac1{\mu^2}\int_0^T du\int_u^\infty f(v)\,dv
+o\!\left(\int_0^Tdu\int_u^\infty f(v)\,dv\right).
\]
For the specified *exact* Pareto tail, its second term equals
\[
K_\alpha T^{2-\alpha}(1+o(1)),\qquad
K_\alpha=\frac{t_0^\alpha}{\mu^2(\alpha-1)(2-\alpha)}
\quad(1<\alpha<2),
\]
or \(K_2\log(T/t_0)+o(\log T)\), where \(K_2=t_0^2/\mu^2\). The additive constant from the lower cutoff is negligible. Because \(k\) is exponentially integrable, Tonelli's theorem and the renewal expansion imply
\[
\int_0^T(g(t)-m)\,dt
\sim H(\lambda_L) K_\alpha T^{2-\alpha}
\]
in the power-law case, and the analogous \(H(\lambda_L)K_2\log(T/t_0)\) at the boundary. Explicitly,
\(\int_0^Tg(t)dt=\int_0^T k(u)U([0,T-u])du\); the linear term yields \(mT+O(1)\), while the second-order term yields the displayed asymptotic. Exponential decay of \(k\) justifies discarding the large-\(u\) endpoint and the theorem's little-oh remainder.

Applying the same argument to \(h=n+b*g\), now using \(\int b=m\), its finite first moment, and integrability of \(n\), gives
\[
\int_0^T\operatorname{Cov}(Y_0,Y_t)\,dt
\sim mH(\lambda_L)K_\alpha T^{2-\alpha}
\]
for \(1<\alpha<2\), with the corresponding logarithm at \(\alpha=2\). Substituting \(H(\lambda_L)=\mu m\), \(\mu=\alpha t_0/(\alpha-1)\), produces
\[
\int_0^T C_F(t)dt\sim
\begin{cases}
\displaystyle\frac{\bar F^2t_0^{\alpha-1}}{\alpha(2-\alpha)}T^{2-\alpha},&1<\alpha<2,\\[5pt]
\displaystyle\frac{\bar F^2t_0}{2}\log(T/t_0),&\alpha=2.
\end{cases}
\]
The SEP conditional term \(E_t\) contributes only \(O(1)\) to this primitive.

**5. Integrated variance and the finite-second-moment regime.** Stationarity, bounded observables and Fubini yield
\[
\operatorname{Var}(S_T)=2\int_0^T(T-t)C_F(t)\,dt
=2\int_0^Tdu\int_0^u C_F(t)\,dt.
\]
Integrating the asymptotics in Step 4 establishes both constants and powers for \(1<\alpha\le2\); integration of the logarithm has leading term \(T\log(T/t_0)\).

For \(\alpha>2\), each independent reset-to-reset cycle has finite duration second moment. Put \(R=\int_0^\tau F(\eta_u^{\mathrm{SEP}})du\). Its mean obeys \(\mathbb ER=F_*H(\lambda_L)\), so \(\mathbb ER/\mu=\bar F\). The renewal-reward variance theorem for iid pairs \((\tau,R)\) gives
\[
\lim_{T\to\infty}T^{-1}\operatorname{Var}(S_T)
=\mu^{-1}\mathbb E(R-\bar F\tau)^2.
\]
This also holds for the stationary rather than fresh-reset initialization: the forward recurrence lifetime has tail \(O(T^{1-\alpha})\), and the bounded partial-cycle reward has squared second moment \(O(T^{3-\alpha})\) for \(2<\alpha<3\), \(O(\log T)\) for \(\alpha=3\), and \(O(1)\) for \(\alpha>3\), all \(o(T)\); Cauchy–Schwarz controls its cross-term with the bulk reward. Finally \(\sigma_F^2>0\): if \(R-\bar F\tau\) vanished almost surely, boundedness of \(\mathbb E(R\mid\tau)\le F_*/\lambda_L\) would contradict \(\bar F\tau\to\infty\) along the unbounded support of \(\tau\). Finiteness follows from \(|R|\le\|F\|_\infty\tau\), completing the proof.

## Verification

The standalone script `check.py` uses arbitrary-precision `mpmath` and no external data. Running `python check.py` with the `requirements.txt` dependency produces `PASS 1329 independent assertions`. It enumerates all half-filled configurations on rings of sizes \(4,6,8,10,12\) to check the exact finite-state eigenmode identity and initial sine amplitude. It also computes two independently derived Laplace-domain expressions for stationary renewal-age correlations and checks the predicted nonanalytic small-frequency amplitudes for several Pareto exponents and timescales, the logarithmic boundary, and finiteness above the boundary. These numerical checks are finite, not a substitute for the renewal theorem, the stationary decomposition, or the infinite-time limit proof.

## Relationship to prior work

Mishra and Basu [1] establish the same power-law-reset SSEP model, the finite-ring stationary density profile, and the diffusive/total-current statistics. The mode's stationary **mean** follows from their renewal density formula. They do not, in the inspected full text, establish the present stationary **time-integrated Fourier-density-mode variance** or its sharp \(T^{3-\alpha}\)/\(T\log T\)/\(T\) trichotomy with constants. Sadekar and Basu [2] analyze density correlations under **two-state Poisson resetting**, not the present non-Poisson clock. Basu, Kundu and Pal [3] study SEP with exponential resetting. Doney [4] reviews/proves second-order renewal-function asymptotics, an acknowledged mathematical ingredient, not the evaluated exclusion-process fluctuation law. Generic renewal-reward theory could yield alternate derivations, and independent priority assessment is still needed.

## Limitations

The size \(L\) is finite and fixed while \(T\to\infty\); none of the displayed constants is asserted uniformly in \(L\). The exact Pareto law, deterministic full-configuration reset state, stationary two-sided renewal preparation, fixed particle count and sine-mode observable are essential assumptions. For \(\alpha\le1\), no finite-mean stationary renewal clock exists in this construction. The result determines variance growth, not an entire fluctuation distribution, a central limit law for \(\alpha>2\), or thermodynamic hydrodynamic limits. Previous broad renewal literature may contain a stronger theorem whose specialization implies this statement.

## References

1. S. Mishra and U. Basu, “Symmetric Exclusion Process under Stochastic Power-law Resetting,” arXiv:2211.14120, first submitted 2022-11-25, https://arxiv.org/abs/2211.14120 (model, density, current, renewal sections).
2. O. Sadekar and U. Basu, “Zero-current Nonequilibrium State in Symmetric Exclusion Process with Dichotomous Stochastic Resetting,” arXiv:2004.00951, https://arxiv.org/abs/2004.00951 (temporal density correlations under Poisson resetting).
3. U. Basu, S. Kundu and A. Pal, “Symmetric Exclusion Process under Stochastic Resetting,” arXiv:1906.11801, https://arxiv.org/abs/1906.11801 (exponential resetting).
4. R. Doney, “The remainder in the Renewal Theorem,” arXiv:1909.11458, https://arxiv.org/abs/1909.11458 (equation (3), second-order renewal expansion).
