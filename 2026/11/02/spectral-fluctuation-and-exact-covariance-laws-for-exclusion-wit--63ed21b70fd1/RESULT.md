# Spectral fluctuation and exact covariance laws for exclusion with sitewise reservoirs

## Finding

Consider symmetric exclusion on a finite connected undirected graph \(G=(V,E)\), \(|V|=n\ge 2\), with positive symmetric exchange rates \(w_{uv}>0\). Independently, at each vertex \(i\) a clock of common rate \(\xi>0\) replaces the occupancy by an independent \(\operatorname{Bernoulli}(h_i)\) variable, with \(h_i\in[0,1]\). Write \(\eta_i\in\{0,1\}\) for stationarity occupancies, \(N=\sum_i\eta_i\), \(\mu_i=\mathbb E\eta_i\), and \(C_{ij}=\operatorname{Cov}(\eta_i,\eta_j)\) for distinct vertices. Let \(L\) be the weighted graph Laplacian, \(\bar h=n^{-1}\sum_i h_i\), \(\delta_i=h_i-\bar h\), and \(R=(\xi I+L)^{-1}\).

**The spectral fluctuation and edge-response identities are**
\[
\mu=\xi Rh,\qquad
\operatorname{Var}(N)=n\bar h(1-\bar h)-\xi\,\delta^{\mathsf T}R\delta.
\]
For any edge \(e=\{u,v\}\), or a proposed additional edge, let \(b_e=e_u-e_v\). Increasing its exchange rate by \(s\ge0\), with all reservoirs and other edges unchanged, changes the stationary total-number variance by the exact amount
\[
\boxed{\operatorname{Var}_{w+s e}(N)-\operatorname{Var}_{w}(N)
=\frac{s(\mu_u-\mu_v)^2}{\xi\,[1+s\,b_e^{\mathsf T}R b_e]}.}
\]
In particular, the derivative with respect to an existing edge conductance is \((\mu_u-\mu_v)^2/\xi\). Thus adding or strengthening edges cannot decrease stationary total-number variance; equality for a specified increase occurs exactly when the two original stationary means coincide.

**The complete pair-covariance law** uses the generator \(Q^{(2)}\) of two *unlabelled* exclusion walkers on distinct vertices, each crossing an edge of rate \(w_{uv}\) when its opposite endpoint is unoccupied. Regard \(C\) and \(g\) as functions on unordered pairs, with
\[
 g_{ij}=w_{ij}(\mu_i-\mu_j)^2
 \quad (w_{ij}=0\text{ for nonedges}).
\]
Then
\[
\boxed{C=-(2\xi I-Q^{(2)})^{-1}g,
\qquad \sum_{i<j}C_{ij}=-\frac1{2\xi}\sum_{\{i,j\}\in E}w_{ij}(\mu_i-\mu_j)^2.}
\]
Every off-diagonal covariance is strictly negative if the bath densities are not all equal, and is zero if they are all equal. The sign assertion is a consequence of the exact Green representation, not a claim that negative association itself is newly discovered.

**A closed-form solution on the complete graph.** Suppose \(n\ge3\) and all edges of \(K_n\) have the same exchange rate \(w>0\). Put
\[
 a=\frac\xi{\xi+n w},\quad
 S_2=\sum_i\delta_i^2,\quad
 d_0=\frac{2S_2}{n-1},\quad
 u_i=\frac{n\delta_i^2-S_2}{n-2},\quad
 d^{(2)}_{ij}=(\delta_i-\delta_j)^2-d_0-u_i-u_j.
\]
Then, simultaneously for all unordered pairs,
\[
\boxed{C_{ij}=-w a^2\left[\frac{d_0}{2\xi}+
\frac{u_i+u_j}{2\xi+n w}+
\frac{d^{(2)}_{ij}}{2\xi+2(n-1)w}\right].}
\]
The three denominators are the eigenvalues of the killed two-particle Johnson-graph Laplacian on the constant, additive, and row-sum-zero modes; when \(n=3\), the third mode is identically zero. Consequently,
\[
\boxed{\operatorname{Var}(N)=n\bar h(1-\bar h)-\frac\xi{\xi+n w}\sum_i(h_i-\bar h)^2.}
\]
If \(n,w,\xi\) and the stationary mean and variance of total occupancy are observed, the last identity determines the *exact quadratic heterogeneity* \(\sum_i(h_i-\bar h)^2\) without observing any local occupation variables.

## Assumptions and scope

All graph orders are finite and at least two, exchange rates on present edges are positive, the underlying graph is connected, and the common bath rate is strictly positive. Bath probabilities may equal zero or one. All expectations and covariances are for the unique stationary distribution. An edge-rate increment may be zero and may apply to a previously absent edge. The complete-graph harmonic formula requires \(n\ge3\), \(w>0\), and a common exchange rate on every edge; the graph-general identities do not require uniform edge rates.

For an explicit generator, if \(\eta^{uv}\) swaps the occupancies at \(u,v\), and \(\eta^{i\leftarrow x}\) replaces occupancy at \(i\) by \(x\in\{0,1\}\), then
\[
\mathcal Lf(\eta)=\sum_{\{u,v\}\in E}w_{uv}[f(\eta^{uv})-f(\eta)]
+\xi\sum_i\left[h_i f(\eta^{i\leftarrow1})+(1-h_i)f(\eta^{i\leftarrow0})-f(\eta)\right].
\]
The stationary distribution is unique: if at least one bath allows creating particles and at least one allows destroying them, irreducibility follows from connectedness, exchange, and reservoir updates; if neither is possible, the corresponding all-empty or all-full state is the unique absorbing stationary state.

## Proof

**1. First moments.** For the coordinate function \(f(\eta)=\eta_i\), the generator gives
\[
\mathcal L\eta_i=\sum_{j:\{i,j\}\in E}w_{ij}(\eta_j-\eta_i)+\xi(h_i-\eta_i).
\]
Stationarity yields \((\xi I+L)\mu=\xi h\). The matrix is positive definite because \(\xi>0\) and \(L\succeq0\), giving \(\mu=\xi Rh\). Since \(L\mathbf1=0\), summing the equations gives \(\sum_i\mu_i=\sum_i h_i=n\bar h\).

**2. Total-number variance.** Exchanges do not change \(N\). A bath update at \(i\) changes \(N\) to \(N-\eta_i+B_i\), where \(B_i\) is independent \(\operatorname{Bernoulli}(h_i)\). Its expected square increment, conditional on the current configuration, is
\[
2(N-\eta_i)(h_i-\eta_i)+(h_i-\eta_i).
\]
Sum the identity over vertices, apply stationarity to \(N^2\), and use \(\mathbb EN=\sum_i h_i\). This gives the *exact* balance
\[
\operatorname{Var}(N)=\sum_i h_i(1-\mu_i).
\]
Write \(h=\bar h\mathbf1+\delta\) and \(\mu=\bar h\mathbf1+\xi R\delta\); the asserted spectral identity follows. If \((\lambda_k,v_k)\), \(0\le k<n\), is an orthonormal eigenbasis of \(L\) with \(v_0=n^{-1/2}\mathbf1\), the equivalent explicit form is
\[
\operatorname{Var}(N)=n\bar h(1-\bar h)-\sum_{k=1}^{n-1}\frac\xi{\xi+\lambda_k}\langle\delta,v_k\rangle^2.
\]

**3. Finite edge-response formula.** For \(b=e_u-e_v\) the new Laplacian is \(L+sbb^{\mathsf T}\). The rank-one inverse identity gives
\[
R_s=R-\frac{sRbb^{\mathsf T}R}{1+s b^{\mathsf T}Rb}.
\]
Substitute this into the variance formula, noting that \(\mu_u-\mu_v=\xi b^{\mathsf T}R\delta\), to obtain
\[
\operatorname{Var}_s(N)-\operatorname{Var}_0(N)=
\frac{s\xi(b^{\mathsf T}R\delta)^2}{1+s b^{\mathsf T}Rb}
=\frac{s(\mu_u-\mu_v)^2}{\xi(1+s b^{\mathsf T}Rb)}.
\]
The denominator is positive. Differentiation at zero proves the stated derivative. If all positive edge rates are strengthened together on a connected graph with nonconstant \(h\), at least one \(\mu_u\ne\mu_v\), so the variance increases strictly.

**4. Pair Green function and strict negativity.** Apply \(\mathcal L\) to \(\eta_i\eta_j\) for \(i\ne j\), subtract the first-moment stationarity equations multiplied by the opposite means, and group covariances. The exchange directly between \(i,j\) does not alter \(\eta_i\eta_j\), while the corresponding two mean equations contribute \(+w_{ij}(\mu_i-\mu_j)^2\). The exact resulting relation is
\[
0=(Q^{(2)}C)_{ij}-2\xi C_{ij}-w_{ij}(\mu_i-\mu_j)^2.
\]
Thus \((2\xi I-Q^{(2)})C=-g\). The inverse is the nonnegative Green operator
\[
(2\xi I-Q^{(2)})^{-1}=\int_0^\infty e^{-2\xi t}\exp(tQ^{(2)})\,dt,
\]
which is entrywise strictly positive because the two-particle exclusion chain on a connected graph is irreducible (for \(n=2\), the one-state transition kernel is one). Nonconstant \(h\) gives nonconstant \(\mu\) and hence a positive \(g\) on at least one graph edge, proving \(C_{ij}<0\) for *every* distinct pair. If all bath values coincide, the invariant product Bernoulli law has \(C_{ij}=0\). Finally, summing the pair equation over all unordered pairs eliminates \(Q^{(2)}C\) by symmetry of the pair exchange rates, yielding the exact covariance-sum identity.

**5. Complete-graph harmonic evaluation.** For \(K_n\), first moments give \(\mu_i=\bar h+a\delta_i\) with \(a=\xi/(\xi+n w)\). On unordered pairs, \(Q^{(2)}=w[A-2(n-2)I]\), where \(A\) is adjacency on the Johnson graph \(J(n,2)\). The forcing is \(g_{ij}=w a^2(\delta_i-\delta_j)^2\). Put \(D_{ij}=(\delta_i-\delta_j)^2\). Its average over pairs is \(d_0=2S_2/(n-1)\), and its row sum at \(i\) is \(n\delta_i^2+S_2\). Therefore
\[
D_{ij}=d_0+u_i+u_j+d^{(2)}_{ij},\quad
\sum_i u_i=0,\quad
\sum_{j\ne i}d^{(2)}_{ij}=0.
\]
The adjacency operator \(A\) acts by the scalars \(2(n-2)\), \(n-4\), and \(-2\), respectively, on these three orthogonal invariant subspaces. Inverting \(2\xi I-Q^{(2)}\) modewise gives the displayed covariance formula (the third subspace is zero when \(n=3\)). The complete-graph variance is the graph-general spectral formula with \(L=w(nI-\mathbf1\mathbf1^{\mathsf T})\); its nonconstant eigenvalue is \(nw\). This proves the stated heterogeneity reconstruction formula without any unproved limiting argument.

## Verification

The separately implemented finite-state calculation implemented in `check_stationary_covariances.py` solves exact rational stationary master equations on graphs of orders two through five. Its comparison includes heterogeneous positive edge rates, rational bath probabilities including boundary values, and the predicted means, variance, killed-two-particle Green covariance, strict sign, covariance-sum identity, and exact finite edge-response. For complete graphs it also compares all pair covariances against the three-mode closed form. Additional exact rational complete-graph tests cover orders three through seven. The saved `check-output.txt` records 1,291 passing exact-rational assertions across 64 full master-equation regimes. These finite tests are consistency checks and are *not* offered as proof for arbitrary graph order or real parameters; the general result is proved in the preceding section.

## Relationship to prior work

Schulman and Sinclair, arXiv:2607.22991v1 (first posted July 25, 2026), study the same edge-exchange and heat-bath dynamics on general graphs, prove mixing and spectral results and provide an algorithm for small-set steady-state probabilities. Their Section 4 highlights the lack of useful explicit pair-correlation formulas outside particularly tractable geometries. Their general numerical algorithm is not the explicit all-graph total-number response law or the symbolic complete-graph pair kernel derived here. Floreani and González Casanova, arXiv:2307.02481v1, give a general stochastic-duality/mixed-product representation for open exclusion with reservoirs, with explicit correlations on a path. That broad representation motivates the two-particle method, but is not presented as the three-harmonic evaluation for heterogeneous sitewise reservoirs on \(K_n\). Established negative-dependence results for exclusion already motivate the sign of pair covariances; negative correlation *in isolation* is not asserted as new. The precise contribution is the connected package of global spectral variance, exact finite edge-response, Green forcing, and closed-form complete-graph covariance for heterogeneous bath parameters.

## Limitations

The rate of bath refresh is common to all vertices. The spectral formula and response law need not retain their present form for unequal refresh rates; such an extension is not claimed. The closed three-mode formula assumes complete-graph uniform exchange rates. The result characterizes first and second stationary moments, not the full joint distribution, its mixing time, or temporal correlations. A generic duality theorem gives implicit access to finite-dimensional moments and may support alternative derivations; historical priority of all formulas is not independently certified. The full generality of possible classical network fluctuation identities has not been exhaustively catalogued.

## References

- L. J. Schulman and A. Sinclair, *Mixing times and spectra of non-equilibrium symmetric exclusion processes on general graphs*, arXiv:2607.22991v1 (first public July 25, 2026). https://arxiv.org/abs/2607.22991
- S. Floreani and A. González Casanova, *Non-equilibrium steady state of the symmetric exclusion process with reservoirs*, arXiv:2307.02481v1 (2023). https://arxiv.org/abs/2307.02481
- A. Vandenberg-Rodes, *A limit theorem for particle current in the symmetric exclusion process*, Electronic Communications in Probability 15 (2010), 240–252. https://doi.org/10.1214/ECP.v15-1550
- F. Casini, C. Giardinà, and F. Redig, *Density Fluctuations for the Multi-Species Stirring Process*, Journal of Theoretical Probability 37 (2024), 3317–3354. https://arxiv.org/abs/2307.05111
