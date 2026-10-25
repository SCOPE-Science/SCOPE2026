# Equilibrium proliferation and sharp stability thresholds in pure-triad SIS contagion on friendship graphs

## Finding

Let \(F_m\), for any integer \(m\ge1\), be a friendship graph formed by \(m\) edge-disjoint triangles sharing exactly one hub. Its non-hub vertices occur in paired petals \((u_j,v_j)\). Under the deterministic, node-wise, pure-three-body SIS equations below, all equilibria in the physical cube can be explicitly classified, counted and assigned their local linear stability.

For each integer \(1\le k\le m\), let \(\lambda_k>1\) be the unique solution of
\[
4k(\lambda_k-1)^3=27\lambda_k.
\]
These thresholds are strictly decreasing: \(\lambda_1=4>\lambda_2>\cdots>\lambda_m\). The **exact number** of equilibria in \([0,1]^{2m+1}\), counting every distinctly labeled state once, is
\[
N_m(\lambda)=1+\sum_{k=1}^m\binom{m}{k}\left(2\mathbf1_{\lambda>\lambda_k}+\mathbf1_{\lambda=\lambda_k}\right).
\]
At \(\lambda>4\), this simplifies to \(N_m(\lambda)=2^{m+1}-1\); at \(\lambda=4\), it is \(2^{m+1}-m-1\). Every nonzero equilibrium supported on fewer than \(m\) petals is linearly unstable. For \(\lambda>\lambda_m\), the disease-free equilibrium and one fully active endemic equilibrium are the **only locally exponentially stable equilibria**; the second fully active endemic equilibrium is a saddle. At \(\lambda=\lambda_m\), the unique nonzero equilibrium is nonhyperbolic, while the disease-free equilibrium remains exponentially stable. The onset satisfies
\[
\lambda_m=1+\left(\frac{27}{4m}\right)^{1/3}+O(m^{-2/3}).
\]

## Assumptions and scope

Fix \(m\ge1\), a per-unordered-triangle infection rate \(\lambda>0\), and a unit individual recovery rate. No infection occurs across a single edge alone. The physical coordinate \(h\in[0,1]\) is the hub infection probability, and \(u_j,v_j\in[0,1]\) are the two non-hub infection probabilities in petal \(j\). The deterministic node-wise mean-field equations are, for every \(j=1,\ldots,m\),
\[
\begin{aligned}
\dot h&=-h+\lambda(1-h)\sum_{j=1}^m u_jv_j,\\
\dot u_j&=-u_j+\lambda(1-u_j)hv_j,\\
\dot v_j&=-v_j+\lambda(1-v_j)hu_j.
\end{aligned}
\]
Each unordered triangle contributes exactly one simultaneous two-infected-neighbor exposure term to each of its susceptible vertices. If an ordered interaction tensor is used instead, its coefficients must be normalized to reproduce these displayed equations. The cube is forward invariant: at each zero coordinate its derivative is nonnegative, and at each unit coordinate its derivative equals \(-1\). A steady state means all displayed derivatives vanish. Stability concerns the displayed continuous-time deterministic ODE, not an exact finite-population Markov chain.

## Proof

**1. Shape of every equilibrium.** If \(h=0\), the petal equations give \(u_j=v_j=0\) for all \(j\). Thus the all-zero state is an equilibrium. Any other equilibrium has \(0<h<1\): \(h=1\) is impossible because its derivative equals \(-1\). At any equilibrium the exact difference identity is
\[
\dot u_j-\dot v_j=-(1+\lambda h)(u_j-v_j).
\]
Consequently \(u_j=v_j\). Write this common value as \(y_j\). The petal steady-state equation becomes
\[
y_j[-1+\lambda h(1-y_j)]=0.
\]
Every positive \(y_j\) therefore equals the same common value
\[
y=1-\frac1{\lambda h},\qquad 0<y<1-\frac1\lambda;
\]
the other petals have \(y_j=0\). This also forces \(\lambda>1\). There is therefore a uniquely defined nonempty subset of \(k\) active petals. On this subset \(u_j=v_j=y\); on its complement both are zero.

**2. Scalar equation and root count.** The positive leaf equation yields \(h=[\lambda(1-y)]^{-1}\), while the hub equation yields \(h/(1-h)=k\lambda y^2\). Their exact combination is
\[
k\lambda y^2[\lambda(1-y)-1]=1,\qquad 0<y<1-\lambda^{-1}.
\tag{1}
\]
Conversely, every root of (1), combined with any choice of the \(k\) petals, produces a valid equilibrium. The left-hand side is zero at the two boundary points and attains its unique interior maximum at
\[
y_k^*=\frac{2(\lambda-1)}{3\lambda},\qquad
\max k\lambda y^2[\lambda(1-y)-1]
=\frac{4k(\lambda-1)^3}{27\lambda}.
\]
The function \((\lambda-1)^3/\lambda\) is strictly increasing on \((1,\infty)\), tends from zero to infinity, and hence each \(\lambda_k\) exists uniquely. Equation (1) has respectively zero, one double, or two distinct physical roots according as \(\lambda<\lambda_k\), \(\lambda=\lambda_k\), or \(\lambda>\lambda_k\). The roots are ordered \(y^-<y_k^*<y^+\) in the two-root case. Since distinct active-petal subsets give different labeled states, multiplication by \(\binom mk\) and addition of the all-zero state proves the displayed census. The threshold decreases with \(k\); at \(k=1\), direct substitution shows \(\lambda_1=4\). The exact large-\(m\) expansion follows by setting \(\lambda_m=1+\delta_m\) in \(4m\delta_m^3=27(1+\delta_m)\) and solving \(\delta_m=(27/(4m))^{1/3}+O(m^{-2/3})\).

**3. Linear instability of partially active petals.** Fix any positive equilibrium with \(k<m\). For each inactive petal the linearized subsystem on its two coordinates is exactly
\[
\begin{pmatrix}-1&\lambda h\\\lambda h&-1\end{pmatrix}.
\]
Its eigenvalues are \(-1-\lambda h\) and \(-1+\lambda h\). As \(\lambda h=(1-y)^{-1}>1\), the second eigenvalue is strictly positive. The inactive-petal block is isolated at first order from the active variables, so this is an eigenvalue of the full Jacobian. Every partially active equilibrium is thus unstable, including partially active folds.

**4. Full-activity stability.** Let \(k=m\), and let \(y\) be a positive physical root. The hub/petal-symmetric Jacobian block, on variables \((\delta h,\delta y)\), is
\[
J_{\rm sym}=\begin{pmatrix}
-1-m\lambda y^2&2m\lambda(1-h)y\\
\lambda y(1-y)&-y/(1-y)
\end{pmatrix}.
\]
Its trace is strictly negative. Substituting the equilibrium identity (1) in its determinant gives exactly
\[
\det J_{\rm sym}=m\lambda^2 y^3-2
=\frac{3\lambda y-2(\lambda-1)}{\lambda(1-y)-1}.
\]
The denominator is positive. Hence this determinant is negative for \(y^-<y_m^*\), zero at the fold and positive for \(y^+>y_m^*\). All other Jacobian modes are strictly negative: \(m\) within-petal antisymmetric modes have eigenvalue \(-(2-y)/(1-y)\), and \(m-1\) between-petal symmetric zero-sum modes have eigenvalue \(-y/(1-y)\). It follows that the lower full-activity branch is a saddle with exactly one unstable direction, while the upper branch has every eigenvalue in the open left half-plane and is locally exponentially stable. At its fold, one eigenvalue vanishes and the equilibrium is nonhyperbolic; no asymptotic-stability claim is made for that point.

At the disease-free equilibrium every infection term has degree at least two, hence its Jacobian is \(-I_{2m+1}\) for every \(\lambda>0\). This state is locally exponentially stable. Combining all cases proves the stability classification.

## Verification

The accompanying standalone program `verify.py` uses Python 3.10+ and SymPy. Run `python3 verify.py` after installing SymPy. It checks five symbolic identities (including the determinant reduction and threshold monotonicity), 34 exact-rational identities, and 88 numerical parameter combinations across \(1\le m\le8\). The latter evaluate 536 nonzero steady-state representatives directly in all \(2m+1\) original ODE equations and test the predicted Jacobian signs. Output from the included program was:

```text
PASS: 5 symbolic identities, 88 parameter cases, 536 evaluated nonzero endemic configurations, 34 exact-rational cases/identities.
```

For a small explicit check, take \(m=2\) and \(\lambda=4\). A fully active lower-branch equilibrium is \(h=1/3\), \(u_1=v_1=u_2=v_2=1/4\). Each single-petal active subset is at its fold, while the fully active subset has two roots, so there are exactly five equilibria including zero. Finite experiments confirm the algebra but do not establish universal root counts or stability without the proof above.

## Relationship to prior work

Iacopini, Petri, Barrat and Latora (2019; public preprint 2018) introduced the higher-order social-contagion mechanism, analytically deriving bistable behavior in a **scalar homogeneous-mixing** approximation. Their Eq. (1) averages simplicial degree; it does not represent hub–petal heterogeneity, classify boundary-supported steady states or provide the count \(N_m\). Their discussion explicitly points to heterogeneous simplicial degrees as further work. Thus bistability itself and the single-population fold are **not** new claims here.

Cisneros-Velarde and Bullo (public preprint 2020) analyze general multi-group simplicial SIS systems and provide sufficient conditions and iterative endemic-state computations. Their principal stability theorems involving pairwise irreducibility do not directly apply when all pairwise transmission is zero, and they do not enumerate the exponentially many partial-support equilibria of this graph. Kiss, Iacopini, Simon and Georgiou (public preprint 2023) derive an exact stochastic higher-order contagion formulation and a complete-connectivity mean-field bifurcation picture; their fully connected setting does not imply the present sparse windmill census. Burgio, Gómez and Arenas (public preprint 2023) address contact-overlap effects through a different triadic approximation; its accessible abstract gives no identical equilibrium classification. The graph-specific subset enumeration and transverse instability proof, not the generic occurrence of bistability, are the contributions assessed here.

## Limitations

This is an exact mathematical statement **about the stated deterministic node-wise mean-field ODE**, not a theorem on finite-population stochastic SIS fixation, probabilities of actual outbreak, or exact stochastic stationary distributions. There is no claim that all trajectories converge globally or that no non-equilibrium recurrent attractors exist. The number of locally exponentially stable equilibria does not determine their basin sizes. At a fold, linearization has a zero eigenvalue; its nonlinear stability is not classified here. Transmission normalization assumes one contribution per unordered triangle. The complete originality comparison is bounded by inspected primary literature and available research indices; an unknown equivalent result, especially under a hypergraph or chemical-reaction-network formulation, cannot be ruled out solely by unsuccessful searches.

## References

1. Iacopini, I., Petri, G., Barrat, A., and Latora, V., *Simplicial models of social contagion*, Nature Communications 10 (2019), 2485; public preprint arXiv:1810.07031v1 (2018-10-16), https://arxiv.org/abs/1810.07031. Open-access full article https://discovery.ucl.ac.uk/id/eprint/10076485/1/s41467-019-10431-6.pdf.
2. Cisneros-Velarde, P., and Bullo, F., *Multi-group SIS Epidemics with Simplicial and Higher-Order Interactions*, public preprint arXiv:2005.11404v1 (2020-05-22), https://arxiv.org/abs/2005.11404.
3. Burgio, G., Gómez, S., and Arenas, A., *A triadic approximation reveals the role of interaction overlap on the spread of complex contagions on higher-order networks*, arXiv:2306.11441v1 (2023-06-20), https://arxiv.org/abs/2306.11441.
4. Kiss, I. Z., Iacopini, I., Simon, P. L., and Georgiou, N., *Insights from exact social contagion dynamics on networks with higher-order structures*, public preprint arXiv:2309.12752v1 (2023-09-22), https://arxiv.org/abs/2309.12752; open manuscript https://nul.repository.guildhe.ac.uk/id/eprint/1505/1/higher_order_proofs%20(10).pdf.
