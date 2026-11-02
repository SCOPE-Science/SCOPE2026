# Exact star-exclusion evacuation law and a Gaussian–Gumbel crossover

## Finding

**Theorem.** Fix positive rates \(a,\gamma\), an integer \(N\ge1\), and an outward per-edge rate \(b\ge0\). On the star \(K_{1,N}\), put at most one particle at each site. Every occupied leaf sends its particle to the vacant hub at rate \(a\); the occupied hub sends its particle to each vacant leaf at rate \(b\); and a particle at the hub is removed irreversibly at rate \(\gamma\). All event clocks are independent conditional on the current configuration; moves to occupied sites are forbidden. Initially the hub is vacant and exactly \(m\) leaves are occupied, where \(1\le m\le N\). Let \(T_{N,m}\) be the time until no particles remain.

For all \(s\ge0\), the complete evacuation-time law has the transform

\[
\mathbb E[e^{-sT_{N,m}}]
=\prod_{k=1}^{m}\frac{ka\gamma}{s^2+s[\gamma+ka+(N-k+1)b]+ka\gamma}.
\]

Equivalently, \(T_{N,m}\) is distributed as a sum of \(2m\) independent exponential variables with the positive rates \(\alpha_k,\beta_k\), \(1\le k\le m\), defined by

\[
\alpha_k+\beta_k=\gamma+ka+(N-k+1)b,\qquad
\alpha_k\beta_k=ka\gamma.
\]

Write \(H_m=\sum_{k=1}^{m}1/k\), \(H_m^{(2)}=\sum_{k=1}^{m}1/k^2\), \(C_N=\gamma+(N+1)b\), and \(D_N=a-b\). Then

\[
\begin{aligned}
\mathbb E T_{N,m}&=\frac{C_N H_m+D_Nm}{a\gamma},\\
\operatorname{Var}(T_{N,m})&=\frac{C_N^2H_m^{(2)}+2C_ND_NH_m+D_N^2m}{a^2\gamma^2}-\frac{2H_m}{a\gamma}.
\end{aligned}
\]

There is also a **sharp fluctuation crossover** for the fully occupied leaves, \(m=N\). Allow the outward rate \(b=b_N\ge0\) to vary with \(N\); keep \(a,\gamma\) fixed. Let \(Z\) be standard normal and \(G\) an independent standard Gumbel variable, \(\Pr(G\le x)=e^{-e^{-x}}\), with Euler constant \(\gamma_{\rm E}=\mathbb EG\). If

\[
\frac{b_N\sqrt N}{a}\longrightarrow\theta\in[0,\infty),
\]

then

\[
\frac{\gamma(T_{N,N}-\mathbb ET_{N,N})}{\sqrt N}
\ \xrightarrow{\ d\ }\ Z+\theta(G-\gamma_{\rm E}).
\]

In contrast, if \(b_N\sqrt N/a\to\infty\) and \(R_N=C_N/(a\gamma)\), then

\[
\frac{T_{N,N}-\mathbb ET_{N,N}}{R_N}
\ \xrightarrow{\ d\ }\ G-\gamma_{\rm E}.
\]

Thus the inward-only model \(b_N=0\) has Gaussian emptying-time fluctuations, any fixed \(b>0\) has Gumbel fluctuations, and the physical weak-backscatter window \(b_N\asymp a/\sqrt N\) has a nontrivial convolution of the two, not a simple change of variance.

## Assumptions and scope

The graph is the ordinary \(N\)-leaf star with identical rates on all leaves. The dynamics are continuous-time, classical, single-species, hard-core exclusion. The initially vacant hub is essential; exactly \(m\) leaves are initially occupied but their labels do not affect the law. The finite-\(N\) transform holds for arbitrary \(a,\gamma>0\) and \(b\ge0\). The asymptotic results apply only to \(m=N\) and fixed positive \(a,\gamma\); \(b_N\) may depend on system size. All limiting statements are in distribution as \(N\to\infty\).

## Proof

**1. Two-state renewal at each remaining particle count.** Immediately after an absorption the hub is empty, and the number of occupied leaves has decreased by one. If that number is \(k\), an occupied leaf first moves to the hub after an exponential wait of rate \(ka\). The resulting occupied hub has \(k-1\) occupied leaves and \(N-k+1\) vacant leaves. It is next removed at rate \(\gamma\), or returns to one of those vacant leaves at total rate \((N-k+1)b\), restarting the same \(k\)-leaf state. By first-event conditioning, the Laplace transform \(f_k(s)\) of the waiting time for one successful removal from this empty-hub state satisfies

\[
f_k(s)=\frac{ka}{ka+s}\left[
\frac{\gamma}{\gamma+(N-k+1)b+s}
+\frac{(N-k+1)b}{\gamma+(N-k+1)b+s}f_k(s)
\right].
\]

Solving gives precisely the \(k\)-th rational factor in the stated product. The strong Markov property at successive removals makes all stage durations independent and shows that their laws depend only on the current \(k\), never on which leaves are occupied. Every stage is absorbed almost surely since the success probability at a hub visit is positive.

**2. Spectral factorization and moments.** The two denominator roots in the variable \(-s\) have positive rates \(\alpha_k,\beta_k\), because their sum and product are positive and

\[
[\gamma+ka+(N-k+1)b]^2-4ka\gamma\ge(\gamma-ka)^2\ge0.
\]

The \(k\)-th transform factors as \(\alpha_k/(s+\alpha_k)\) times \(\beta_k/(s+\beta_k)\). This proves the independent-exponential representation, including equal-rate cases. For its mean, use \(1/\alpha_k+1/\beta_k=(C_N+D_Nk)/(ka\gamma)\). For its variance, use \(1/\alpha_k^2+1/\beta_k^2=(C_N+D_Nk)^2/(k^2a^2\gamma^2)-2/(ka\gamma)\). Summing over \(k\) proves both displayed moment expressions.

**3. Exact Gamma-product identity.** In a complex neighborhood of \(s=0\), define \(v_N(s)=s(s+C_N)/(a\gamma+D_Ns)\). The finite transform for \(m=N\) can be rewritten as

\[
\mathbb E e^{-sT_{N,N}}
=\left(1+\frac{D_Ns}{a\gamma}\right)^{-N}
\frac{\Gamma(N+1)\Gamma(1+v_N(s))}{\Gamma(N+1+v_N(s))}.
\]

This follows from extracting \(1+D_Ns/(a\gamma)\) in each product factor and applying the finite Gamma identity. The rational product, not this locally factored expression, defines the transform globally if a factorized denominator vanishes outside the neighborhood.

**4. Weak-backscatter crossover.** Suppose \(b_N\sqrt N/a\to\theta<\infty\). For each real \(t\), set \(s=-it\gamma/\sqrt N\), \(c_N=C_N/(a\sqrt N)\to\theta\), and \(d_N=D_N/a\to1\). Then

\[
\frac{D_Ns}{a\gamma}=-\frac{itd_N}{\sqrt N},\qquad
v_N(s)=-itc_N+O_t(N^{-1/2}).
\]

Stirling's formula, uniformly for bounded complex \(v\), yields \(\Gamma(N+1)/\Gamma(N+1+v)=N^{-v}(1+o(1))\). Also \(\mathbb ET_{N,N}\,\gamma/\sqrt N=c_NH_N+d_N\sqrt N\). Consequently the characteristic function of the centered, normalized time tends to

\[
\exp(-t^2/2)\,\Gamma(1-it\theta)\,
\exp(-it\theta\gamma_{\rm E}),
\]

since \(H_N-\log N\to\gamma_{\rm E}\). This is the characteristic function of \(Z+\theta(G-\gamma_{\rm E})\). Lévy's continuity theorem completes this regime, including \(\theta=0\).

**5. Gumbel regime.** Suppose \(b_N\sqrt N/a\to\infty\). Then \(C_N\to\infty\), \(|D_N|/C_N\to0\), \(N(D_N/C_N)^2\to0\), and \((|D_N|/C_N+C_N^{-2})\log N\to0\). For fixed real \(t\), take \(s=-it/R_N=-ita\gamma/C_N\). The Gamma argument satisfies \(v_N(s)=-it+o(1/\log N)\), and

\[
\left(1+\frac{D_Ns}{a\gamma}\right)^{-N}
=\exp\!\left(itN\frac{D_N}{C_N}+o(1)\right).
\]

Since \(\mathbb ET_{N,N}/R_N=H_N+ND_N/C_N\), the centered transform converges to \(\Gamma(1-it)e^{-it\gamma_{\rm E}}\), proving the standard centered-Gumbel limit. No simultaneous scaling of \(a\) or \(\gamma\) is assumed.

## Verification

The standalone `check_star.py` constructs the full \(2m\)-state transient Markov generator directly, without using the renewal formula, and solves the independent backward Laplace and moment equations. It compares these values against the theorem for \(1\le m\le N\le9\), four parameter sets (including zero and nonzero outward rates), and four Laplace points: 720 transform comparisons and 180 mean/variance comparisons. It separately evaluates the exact finite product characteristic function for \(N=1000,5000,20000\) against the Gaussian–Gumbel characteristic function at four crossover parameters, and against the Gumbel characteristic function for three fixed outward rates. Run `python check_star.py` with NumPy and SciPy. The actual output is supplied in `check_output.txt`.

Finite calculations are consistency checks only. The all-\(N\) and asymptotic assertions follow from the exact renewal equations, Gamma identity, and limiting characteristic functions above.

## Relationship to prior work

Mottishaw, Waclaw and Evans (2013, arXiv:1306.0360) analyze steady-state correlations and currents of a **directed** exclusion process on rooted trees, including the two-level star. The present model instead has an irreversible *hub* trap and bidirectional rates, starts with a fixed finite particle population, and studies the complete time to remove all particles. Their steady-state star solution does not state the present finite-time transform or crossover.

Meerson, Vilenkin and Krapivsky (2014, arXiv:1406.3502) analyze the survival of an external target in a gas of diffusing exclusion particles by macroscopic fluctuation theory, not finite-star full evacuation. Hathcock and Strogatz (2021, arXiv:2103.08522) establish broad Gaussian and Gumbel absorption-time universality for birth-death processes and related models. This background explains why those two limits are natural; it does not state the present star-specific, exactly solvable two-phase renewal law or the \(b_N\sim a/\sqrt N\) normal–Gumbel convolution. The ordinary coupon-collector limit and general extreme-value distribution are antecedents, not originality claims.

## Limitations

The geometry is a star and the rates are homogeneous on each direction. The result assumes memoryless exponential hopping and absorption, hard-core exclusion, a vacant hub initially, and no particle injection. It does not extend without further proof to heterogeneous leaves, arbitrary trees, hubs with several occupancies, reaction rates depending on local density, or finite-time particle-count correlations. No independent scientific audit has been conducted, and specialized prior-work coverage remains a historical-priority risk.

## References

- P. Mottishaw, B. Waclaw and M. R. Evans, *An exclusion process on a tree with constant aggregate hopping rate*, arXiv:1306.0360 (first public 2013-06-03), https://arxiv.org/html/1306.0360v4.
- B. Meerson, A. Vilenkin and P. L. Krapivsky, *Survival of a static target in a gas of diffusing particles with exclusion*, arXiv:1406.3502 (first public 2014-06-13), https://arxiv.org/abs/1406.3502.
- D. Hathcock and S. H. Strogatz, *Asymptotic absorption-time distributions in extinction-prone Markov processes*, arXiv:2103.08522 (first public 2021-03-15), https://arxiv.org/abs/2103.08522.
- J. E. Santos and G. M. Schütz, *Exact time-dependent correlation functions for the symmetric exclusion process with open boundary*, Phys. Rev. E 64, 036107 (2001), https://doi.org/10.1103/PhysRevE.64.036107.
