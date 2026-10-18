# A one-interval positivity theorem for every finite Markov theta step

## Finding
Let \(Q\in\mathbb R^{N\times N}\), \(N\ge1\), be any finite continuous-time Markov generator in row convention: \(q_{ij}\ge0\) for \(i\ne j\) and \(Q\mathbf1=0\). Irreducibility, reversibility, and diagonalizability are **not** assumed. For \(h\ge0\) and \(0\le\theta\le1\), set
\[
M_{\theta,h}=(I-\theta hQ)^{-1}(I+(1-\theta)hQ),\qquad
R(s)=(I-sQ)^{-1}.
\]
For each state \(i\), put \(r_i=-q_{ii}\). If \(r_i>0\), let \(T_i\in(0,\infty]\) be the first time of returning to \(i\) **after its initial departure** (measured from that departure), with \(T_i=\infty\) on nonreturn. Define
\[
\rho_i=\begin{cases}
1,&r_i=0,\\
(1+r_i\mathbb E T_i)^{-1},&r_i>0,
\end{cases}
\]
where an infinite mean gives \(\rho_i=0\), and write \(\rho_* =\min_i\rho_i\).

**Universal no-reentry law.** For every such \(Q\) and \(\theta\), the complete positivity-preserving timestep set \(\{h\ge0:M_{\theta,h}\ge0\text{ entrywise}\}\) is **exactly** \([0,H_\theta]\), with \(H_\theta\in(0,\infty]\). It never has a disconnected component. The sharp boundary is as follows.

* At \(\theta=0\), \(H_0=1/\max_i r_i\), taking \(H_0=\infty\) when \(Q=0\).
* At \(0<\theta\le1\), \(H_\theta=\infty\) **if and only if** \(\theta\ge1-\rho_*\). Otherwise, for each \(i\) with \(\rho_i<1-\theta\), there is a unique \(s_i>0\) satisfying \(R(s_i)_{ii}=1-\theta\), and
\[
H_\theta=\frac1\theta\min_{\{i:\rho_i<1-\theta\}}s_i.
\]
These are exact scalar root conditions, with no spectral reality requirement.

**Recurrence and time-reversal consequences.** If \(i\) belongs to a closed irreducible class with stationary probability \(\pi_i^{(C)}\) within that class, then \(\rho_i=\pi_i^{(C)}\). Every transient state has \(\rho_i=0\). Thus a single transient state forces \(H_\theta<\infty\) for every \(\theta<1\); a finite irreducible chain has unconditional positivity precisely for \(\theta\ge1-\min_i\pi_i\). For an irreducible chain, the stationary time reversal \(Q^*=D^{-1}Q^{\mathsf T}D\), where \(D=\operatorname{diag}(\pi)\), has **the same** sharp \(H_\theta\) for every \(\theta\in[0,1]\).

## Assumptions and scope
The generator is finite, conservative, and has finite nonnegative off-diagonal jump rates. The update acts on row probability distributions on the right. An absorbing state has \(r_i=0\), and contributes the constant resolvent diagonal \(R(s)_{ii}=1\). The result concerns the completed theta step, not internal stages of a particular implementation. Positivity means nonnegativity of every matrix entry, which is equivalent to preserving every nonnegative initial row vector. The state space may have any number of communicating classes and transient states. The parameter \(s>0\) in the scalar condition is \(s=\theta h\).

## Proof
**1. Reduction to return resolvents.** The finite generator produces a nonnegative Markov semigroup. For every \(s>0\),
\[
R(s)=\int_0^\infty e^{-u}e^{suQ}\,du\ge0,
\qquad R(s)\mathbf1=\mathbf1.
\]
For \(\theta>0\), a direct rearrangement gives
\[
M_{\theta,h}=\theta^{-1}R(\theta h)
-\frac{1-\theta}{\theta}I.
\]
All off-diagonal entries of \(M_{\theta,h}\) are nonnegative, and
\[
M_{\theta,h}\ge0\ \Longleftrightarrow\
R(\theta h)_{ii}\ge1-\theta\quad\text{for every }i.
\]
The formula extends continuously to \(h=0\). At \(\theta=0\), \(M_{0,h}=I+hQ\) has nonnegative off-diagonal entries and diagonal \(1-hr_i\), yielding the stated \(H_0\).

**2. A return-time formula valid without detailed balance.** Fix \(i\) with \(r_i>0\). Let \(G_{ii}(\alpha)=\int_0^\infty e^{-\alpha t}(e^{tQ})_{ii}\,dt\), \(\alpha>0\), and \(\phi_i(\alpha)=\mathbb E[e^{-\alpha T_i}]\), with \(e^{-\alpha\infty}=0\). Starting at \(i\), the initial holding time is exponential with rate \(r_i\). Its expected discounted occupation of \(i\) is \((\alpha+r_i)^{-1}\); the discounted probability of completing the initial holding time and returning to \(i\) is \(r_i(\alpha+r_i)^{-1}\phi_i(\alpha)\). By the strong Markov property at the return time,
\[
G_{ii}(\alpha)=\frac1{\alpha+r_i}
+\frac{r_i\phi_i(\alpha)}{\alpha+r_i}G_{ii}(\alpha)
=\frac1{\alpha+r_i(1-\phi_i(\alpha))}.
\]
Since \(R(s)_{ii}=s^{-1}G_{ii}(s^{-1})\), this proves
\[
\boxed{R(s)_{ii}=\bigl(1+r_i\mathbb E[s(1-e^{-T_i/s})]\bigr)^{-1}.}
\]
For each \(t\in(0,\infty)\), the function \(g_t(s)=s(1-e^{-t/s})\) has derivative
\[
g_t'(s)=1-(1+t/s)e^{-t/s}>0\qquad(s>0)
\]
by \(e^x>1+x\) for \(x>0\). For \(t=\infty\), \(g_t(s)=s\), also strictly increasing. As \(T_i>0\) almost surely, its expectation is strictly increasing, so \(s\mapsto R(s)_{ii}\) is continuous and strictly decreasing on \((0,\infty)\). It tends to \(1\) as \(s\downarrow0\), by \(0\le g_t(s)\le s\). By monotone convergence, \(g_t(s)\uparrow t\) (including the extended value \(\infty\)) as \(s\to\infty\); hence \(R(s)_{ii}\downarrow\rho_i\). For \(r_i=0\), \(R(s)_{ii}\equiv1\).

**3. Exact positivity interval.** If \(\theta=1\), then \(M_{1,h}=R(h)\ge0\) for every \(h\). Suppose \(0<\theta<1\). Each nonconstant resolvent diagonal starts at \(1\), strictly decreases to \(\rho_i\), and therefore either never falls below \(1-\theta\) (if \(\rho_i\ge1-\theta\)) or crosses that level exactly once, at \(s_i>0\) (if \(\rho_i<1-\theta\)). Intersecting these statewise initial intervals proves the exact formula for \(H_\theta\), endpoint inclusion, unconditional criterion, and impossibility of any later positivity recovery. No claim relies on a sample-grid search.

**4. Recurrence interpretation.** If \(i\) is transient, its probability of ever returning after departure is strictly less than one in a finite chain, so \(\mathbb P(T_i=\infty)>0\), and \(\rho_i=0\). If \(i\) lies in a finite closed irreducible class, successive visits to \(i\) are renewal cycles with mean occupation time \(1/r_i\) at \(i\) per cycle and mean cycle time \(1/r_i+\mathbb E T_i\). The stationary occupation fraction in its class is therefore
\[
\pi_i^{(C)}=\frac{1/r_i}{1/r_i+\mathbb E T_i}=\rho_i.
\]
An absorbing singleton has stationary mass one and is already handled. This establishes both structural consequences.

**5. Invariance under time reversal.** For an irreducible generator with positive stationary row \(\pi\), define \(Q^*=D^{-1}Q^{\mathsf T}D\). Then \((I-sQ^*)^{-1}=D^{-1}R(s)^{\mathsf T}D\). Diagonal similarity and transposition preserve every diagonal entry, so the scalar positivity tests coincide for every \(s\). The \(\theta=0\) endpoint coincides too, because \(q^*_{ii}=q_{ii}\). Thus all sharp horizons are invariant.

## Verification
The standalone standard-library program `verify.py` evaluates inverse matrices by exact rational Gaussian elimination. It compares the two algebraic definitions of \(M_{\theta,h}\), checks stochasticity and off-diagonal nonnegativity, and confirms the diagonal threshold criterion across 197 explicit directed generators (including reducible cases), six theta parameters, and five test timesteps each. It also checks strict diagonal-resolvent ordering at five strictly increasing rational parameters whenever a state has positive exit rate, the exact positive-step threshold for a three-state absorbing pure-birth chain, and time-reversal equality for a nonreversible four-state chain. Run `python3 verify.py` with Python 3 and no additional packages. This finite replay checks algebra and examples; the universal theorem follows from the renewal proof.

For the pure-birth example with transitions \(1\to2\) at rate \(1\), \(2\to3\) at rate \(2\), and absorbing state \(3\), the sharp horizon is \(H_\theta=1/[2(1-\theta)]\) for every \(0\le\theta<1\), and \(H_1=\infty\). This exhibits the transient-state obstruction explicitly.

## Relationship to prior work
Horváth (1998) proves positivity-radius criteria for Runge–Kutta methods on classes of positive dissipative problems; these give general problem-class step guarantees, not a generator-specific no-reentry theorem with recurrence classification. Fallat and Tsatsomeros (2002) derive matrix Cayley identities and properties for \(M\)-matrix classes; the resolvent algebra in Step 1 is already implicit in their Lemma 2.2. Doyle (2009) reviews the Markov return-time/resolvent connection, without the theta positivity classification. The public result *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains* gives the exact diagonal criterion for all finite generators but derives the one-interval result **only in the reversible case** using a positive spectral representation; its limitations explicitly leave nonreversible positivity windows unclassified. The new step is the non-spectral return-time monotonicity for all finite generators, including reducible chains and arbitrary \(\theta\), and its transient-state and time-reversal consequences.

## Limitations
The theorem does not assert a closed elementary formula for \(H_\theta\) for arbitrary \(Q\); it gives an exact scalar crossing characterization computable from resolvents. The chain must have finitely many states and finite jump rates. The claim makes no statement about nonlinear systems, nonconservative generators, higher-order Gauss or Radau methods, internal-stage positivity, or infinite-state chains. The root may be ill-conditioned near the critical \(\theta\), so numerical root finding must guard interval endpoints. Literature searches cannot exclude every unindexed equivalent statement; the classical first-return identity alone should not be mistaken for the new integrator-level conclusion.

## References
1. Z. Horváth, *Positivity of Runge–Kutta and Diagonally Split Runge–Kutta Methods*, Applied Numerical Mathematics 28 (1998), 309–326, DOI: 10.1016/S0168-9274(98)00050-6.
2. S. M. Fallat and M. J. Tsatsomeros, *On the Cayley Transform of Positivity Classes of Matrices*, Electronic Journal of Linear Algebra 9 (2002), 190–196, DOI: 10.13001/1081-3810.1086.
3. P. G. Doyle, *The Kemeny Constant of a Markov Chain*, arXiv:0909.2636, first version 14 September 2009.
4. *A Resolvent-Return Law for Crank–Nicolson Positivity on Reversible Markov Chains*, public research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a .
