# Strict all-horizon mutation delay of pure-state entrance in neutral Moran dynamics

## Finding

Let \(n\geq 3\), let \(K_0=k\in\{1,\ldots,n-1\}\), and let \(\tau_{\mu}=\inf\{t\geq0:K_t\in\{0,n\}\}\) be the *first entrance* into either pure state of the neutral two-allele Moran chain with symmetric per-birth mutation probability \(\mu\in[0,1]\). Put \(r=\min(k,n-k)\). For every pair \(0\leq\mu_1<\mu_2\leq1\) and every integer \(t\geq0\),

\[
\mathbb P_k(\tau_{\mu_2}>t)=\mathbb P_k(\tau_{\mu_1}>t)=1\quad(t<r),
\]
\[
\mathbb P_k(\tau_{\mu_2}>t)>\mathbb P_k(\tau_{\mu_1}>t)\quad(t\geq r).
\]

Consequently, the complete first-purity hitting-time distribution is strictly ordered by mutation intensity at every horizon when purity is reachable. Its expectation is strictly increasing. If \(Q_{n,\mu}\) denotes the transient transition matrix of the reflected minority-count process, its Perron root \(\lambda_n(\mu)\) satisfies \(0<\lambda_n(\mu)<1\) and \(\lambda_n'(\mu)>0\), including one-sided endpoint derivatives. In particular, the exact exponential survival-tail base increases strictly with mutation. The population-size condition is sharp: for \(n=2\) the stopping-time law is independent of mutation, with \(\mathbb P(\tau_{\mu}>t)=2^{-t}\). For \(n=3\), the complete law is explicitly \(\mathbb P(\tau_{\mu}>t)=((7+\mu)/9)^t\).

## Assumptions and scope

The population contains exactly \(n\) haploid individuals of two possible alleles and has no fitness differences. At each discrete step, one individual is uniformly chosen as parent. Independently, the offspring inherits the parent's allele with probability \(1-\mu\) and flips to the other allele with probability \(\mu\). Another uniform draw from the *pre-existing* \(n\) individuals determines which individual is removed; the parent may be removed. The offspring replaces the removed individual. The draws are independent conditional on the current allele count. The chain is stopped at its **first** visit to either homogeneous state, even when later mutations could reverse homogeneity in the unstopped model. No diffusion, continuous-time, large-population or weak-mutation limit is assumed.

## Proof

**1. Exact kernel and reflection.** Write \(x=k/n\). A direct parent/offspring/removal calculation gives the ordinary allele-count transition probabilities

\[
p_k(\mu)=(1-x)\,[x+\mu(1-2x)],\qquad
q_k(\mu)=x\,[1-x-\mu(1-2x)],
\]

for \(k\to k+1\) and \(k\to k-1\) respectively, with stay probability \(1-p_k-q_k\). Symmetry under interchange of alleles makes \(R_t=\min(K_t,n-K_t)\) a Markov chain on \(\{0,1,\ldots,m\}\), where \(m=\lfloor n/2\rfloor\); \(0\) is made absorbing. Let \(Q=Q_{n,\mu}\) be its restriction to \(\{1,\ldots,m\}\). For \(1\leq r<m\), its up/down probabilities are

\[
a_r=(1-r/n)[r/n+\mu(1-2r/n)],\quad
b_r=(r/n)[1-r/n-\mu(1-2r/n)].
\]

At \(r=m\) and even \(n\), both ordinary allele-count changes lower \(R\), with combined probability \(1/2\) independent of \(\mu\). At \(r=m\) and odd \(n\), the upward allele-count change reflects back into \(R=m\); only the downward change, of probability \(b_m\), lowers \(R\). In all cases, \(Q\) is a nonnegative substochastic matrix with positive diagonal and nearest-neighbor communicating entries (where applicable). The probability of survival through time \(t\) from minority count \(r\) is

\[
u_t^{\mu}(r)=\mathbb P_r(\tau_{\mu}>t)
=(Q^t\mathbf 1)_r,\qquad u_t^{\mu}(0)=0.
\]

**2. Monotonicity in starting minority count.** For fixed \(\mu\) and any \(1\leq r<m\), a path from \(r+1\) to \(0\) must first visit \(r\), since the chain is skip-free. Its first passage \(\sigma\) from \(r+1\) to \(r\) is almost surely finite: from every state above \(r\) there is a positive-probability descending route, and the state space is finite. By the strong Markov property, the hitting time from \(r+1\) has the law \(\sigma+\tau'_r\), where \(\tau'_r\) is independent of \(\sigma\) and has the law of the hitting time from \(r\). Therefore

\[
u_t^{\mu}(0)\leq u_t^{\mu}(1)\leq\cdots\leq u_t^{\mu}(m)
\]

for every \(t\). This argument requires neither a coupling at distinct mutation rates nor a large-population approximation.

**3. Mutation derivative and strict finite-horizon order.** Let \(D=\partial_{\mu}Q\). For any nondecreasing vector \(f(0)=0\leq f(1)\leq\cdots\leq f(m)\), for \(r<m\),

\[
(Df)_r=(1-r/n)(1-2r/n)[f(r+1)-f(r)]
- (r/n)(1-2r/n)[f(r-1)-f(r)]\geq0.
\]

For even \(n\), the top row of \(D\) is zero. For odd \(n\), its top row gives \((Df)_m=b'_m[f(m-1)-f(m)]\geq0\). Thus \(D\) maps every nondecreasing nonnegative survival vector to a nonnegative vector. By differentiating the finite matrix power,

\[
\partial_{\mu}u_t^{\mu}
=\sum_{j=0}^{t-1}Q^{\,t-1-j}D u_j^{\mu}\geq0.
\]

Moreover, for every \(n\geq3\), direct differentiation of the one-step boundary-loss probability gives

\[
(D\mathbf1)_1=-b'_1=\frac1n\left(1-\frac2n\right)>0.
\]

The \(j=0\) term in the sum is therefore **strictly** positive in coordinate \(r\) whenever \(t-1\geq r-1\): the matrix entry \((Q^{t-1})_{r1}\) is positive, since \(r-1\) downward steps reach state \(1\) and additional steps can be spent holding there with positive probability. Therefore \(\partial_{\mu}u_t^{\mu}(r)>0\) for all \(t\geq r\). When \(t<r\), skip-free movement makes first entrance into \(0\) impossible, hence \(u_t^{\mu}(r)=1\). Integrating the strict derivative from \(\mu_1\) to \(\mu_2\) proves the asserted comparison, including the endpoints. Summing the survival probabilities establishes strict increase of the finite mean \(\mathbb E\tau_{\mu}\).

**4. The tail exponent.** The matrix \(Q\) is primitive: it has positive diagonal and, if \(m>1\), positive nearest-neighbor transitions between all transient states. Its chance of eventual absorption is one, since every transient state has a uniformly positive-probability route to \(0\) within finitely many steps; hence its Perron root \(\lambda\) lies strictly between zero and one. Let \(v\) and \(w\) be positive right/left Perron eigenvectors. Perron convergence of \(\lambda^{-t}Q^t\mathbf1\) to a positive multiple of \(v\), together with step 2, shows \(0=v_0\leq v_1\leq\cdots\leq v_m\). The simple-eigenvalue derivative identity and step 3 give

\[
\lambda'(\mu)=\frac{w^{\mathsf T}Dv}{w^{\mathsf T}v}>0,
\]

because \(Dv\geq0\), and its first component satisfies \((Dv)_1\geq -b'_1 v_1>0\). Primitive Perron asymptotics further yield \(\mathbb P_r(\tau_{\mu}>t)=c_r(\mu)\lambda(\mu)^t(1+o(1))\) with \(c_r(\mu)>0\).

**5. Sharp size boundary.** If \(n=2\), the sole minority state is \(1\). Whichever allele is born, it replaces the other allele with probability \(1/2\), so \(Q=(1/2)\) for all \(\mu\). If \(n=3\), there is likewise only one transient minority state and the one-step probability of reaching purity is \((2-\mu)/9\); thus \(Q=((7+\mu)/9)\), proving the explicit formula.

As a nontrivial diagnostic, away from the central allele count the ordinary probability of *any* allele-count change is \(2x(1-x)+\mu(1-2x)^2\), which increases with mutation; the strict delay of entrance into purity is therefore not a consequence of simply suppressing all transitions.

## Verification

Run `python3 verify.py` using the attached standalone standard-library program. Exact rational matrix recursions for \(3\leq n\leq16\), \(\mu\in\{0,1/4,1/2,3/4,1\}\), and \(0\leq t\leq20\) check 5,292 strict/equal cross-mutation survival comparisons, 6,615 strict/zero mutation-derivative comparisons, and 5,145 monotone-in-state comparisons. It also verifies the \(n=2\) exception and the \(n=3\) closed form. These are finite tests; the unbounded population-size, time-horizon and parameter conclusions follow from steps 1–5, not from enumeration.

## Relationship to prior work

Gaeta (2024), Sections 3 and 7–8, studies **exactly this symmetric-mutation complete Moran process** and first-pure-state entrance. It derives hitting-probability and mean-time recursions and reports that the mean increases with mutation, but does not state the pointwise **entire hitting-time survival law** ordered strictly at all reachable horizons, nor strict monotonicity of the killed-chain Perron rate. Thus the mean comparison alone is not claimed as novel here. Huillet (2013), Sections 2–5, develops spectral, hitting-time and Siegmund-duality analyses of Moran birth–death chains with mutation; its *stochastic monotonicity* compares the chain over initial states or concerns associated dual chains, not the parameter ordering of the first-purity hitting law at all time horizons. Díaz, Goldberg, Richerby and Serna (2013), Sections 1 and 3–4, obtain stochastic dominations for graph Moran absorption under selection without recurrent mutation; their comparison does not supply the stated symmetric-mutation parameter theorem. DeVille and Galiardi (2015), Sections 2 and 4, analyze a two-strategy Moran game with fitness-dependent reproduction and metastable passage between evolutionary-stability basins; their large-population passage-time asymptotics do not assert finite-horizon first-purity mutation order. The proof here exploits the minor-allele reflection and the order-preserving mutation derivative specifically for the two-sided first-entrance problem.

## Limitations

The result assumes exactly two alleles, equal mutation probabilities in the two directions, neutrality, constant population size, and independent uniform birth/death draws. It makes **no** assertion about selection, asymmetric mutation, spatial graph replacement, continuous time, or later visits after the first homogeneous state. Stopping at temporary homogeneity is not biological fixation when \(\mu>0\). The \(n=2\) case shows strict ordering genuinely fails for the smallest population. Literature comparisons cannot establish absolute uniqueness; further specialized first-passage coupling literature may contain equivalent formulations. Independent external validation has not been performed.

## References

1. Giuseppe Gaeta, “On some dynamical features of the complete Moran model for neutral evolution in the presence of mutations,” arXiv:2402.12943, first publicly posted 2024-02-20, https://arxiv.org/abs/2402.12943 (Sections 3 and 7–8).
2. Thierry E. Huillet, “Fluctuations Analysis of Finite Discrete Birth and Death Chains with Emphasis on Moran Models with Mutations,” *International Scholarly Research Notices* (2013), https://doi.org/10.1155/2013/939308 (Sections 2–5).
3. Josep Díaz, Leslie Ann Goldberg, David Richerby, and Maria Serna, “Absorption Time of the Moran Process,” arXiv:1311.7631 (2013), https://arxiv.org/abs/1311.7631 (Sections 1 and 3–4).
4. Lee DeVille and Meghan Galiardi, “Finite-size effects and switching times for Moran dynamics with mutation,” arXiv:1512.06886 (2015), https://arxiv.org/abs/1512.06886 (Sections 2 and 4; frequency-dependent fitness and metastable switching, not exact neutral first-purity entrance).
