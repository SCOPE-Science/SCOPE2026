# A sharp mortality threshold for overexploration on star-shaped metapopulations

## Finding

For the fast-explorer metapopulation model on a connected, undirected, unweighted habitat graph, intrinsic mortality of explorers can cause the invasion-capacity benefit of exploration to reverse. The effect is governed at high exploration by a graph-Laplacian degree-heterogeneity energy. On a star with one hub and \(m\geq2\) leaves, the condition for **some finite exploration rate to yield strictly greater metapopulation capacity than infinite exploration** is exactly
\[
1+g>\frac{4m(m+1)}{(m-1)^2},
\]
where \(g\geq0\) is explorer mortality divided by its colonization-attempt rate. Whenever this inequality holds, the entire interval of exploration rates above the limiting capacity is explicit and begins at a unique positive crossing. Otherwise, *every* finite rate has capacity strictly below the infinite-rate limit.

More precisely, let \(a=1+g\), \(f>0\) be the exploration-to-colonization rate ratio, and \(\xi>0\) the maximal explorability. For the star, the effective kernel has capacity
\[
\Lambda_m(f)=\frac{\xi f\bigl(mf+\sqrt{m^2f^2+ma(a+(m+1)f)}\bigr)}{a(1+f)(a+(m+1)f)},\qquad
\Lambda_m(\infty)=\frac{2\xi m}{a(m+1)}.
\]
Put \(\delta=a(m-1)^2-4m(m+1)\) and \(B=4m(2a+m+1)\). For \(\delta>0\), define
\[
f_*=\frac{B+\sqrt{B^2+16am\delta}}{2\delta}.
\]
Then \(\Lambda_m(f)>\Lambda_m(\infty)\) holds exactly when \(f>f_*\); at \(f=f_*\) the values agree, and at \(0<f<f_*\) the finite-rate capacity is smaller. For \(\delta\leq0\), the finite-rate capacity is smaller for every finite \(f>0\). In the \(\delta>0\) regime, \(\Lambda_m\) attains a maximum at a finite rate and eventually decreases toward its infinite-rate limit.

An explicit threshold reversal uses 21 habitat patches (a star with \(m=20\) leaves), \(g=9\), \(\xi=1\), and \(f=5\). Its capacity is strictly greater than \(1/5\), while the infinite-exploration capacity is \(4/21<1/5\). Consequently, for uniform colonization coefficient \(c=1\) and local extinction \(e=1/5\), the positive state can establish at the finite rate, but sufficiently large exploration rates force extinction from all initial occupancies.

## Assumptions and scope

Let \(G\) be any fixed finite, connected, simple undirected graph of order \(n\geq3\), with symmetric adjacency matrix \(A\), degree vector \(d=A\mathbf1\), and Laplacian \(L=\operatorname{diag}(d)-A\). Patches have equal capacities and uniform local demographic coefficients. Explorers diffuse along each oriented edge at rate \(D\), attempt colonization at rate \(\lambda>0\), and die independently at rate \(\gamma\geq0\). Write \(f=D/\lambda>0\), \(g=\gamma/\lambda\), and \(a=1+g\). The feasibility-of-exploration matrix is the saturating Monod choice \(C=\xi f/(1+f)\,A\) with \(\xi>0\).

The fast-explorer, quasi-stationary reduction gives exactly
\[
K(f)=\frac{\xi f}{1+f}(aI+fL)^{-1}A,\qquad \Lambda_G(f)=\rho(K(f)).
\]
This is an effective deterministic model. No stochastic finite-carrying-capacity survival-time assertion, nonuniform patch-size assertion, or directed-graph assertion is included. The invasion statement uses \(\dot p_i=-ep_i+c(1-p_i)\sum_jK_{ij}(f)p_j\) on \([0,1]^n\) with \(c,e>0\).

The general-graph mechanism is also exact at first order. Let \(\bar d=n^{-1}\sum_i d_i>0\), \(h=d-\bar d\mathbf1\), and \(L^+\) be the Moore–Penrose inverse of \(L\). With \(S=h^TL^+h\),
\[
\Lambda_G(f)=\xi\left[\frac{\bar d}{a}+\frac1f\left(\frac{S}{n\bar d}-\frac{\bar d}{a}\right)+O(f^{-2})\right]
\quad(f\to\infty).
\]
Thus the sign of the first high-exploration correction is positive precisely if \(aS>n\bar d^2\), and negative if \(aS<n\bar d^2\); at equality this first-order test is inconclusive. For the star, \(S=m(m-1)^2/(m+1)^2\), giving the displayed sharp condition. The exact star formula, not the first-order expansion, resolves equality and all finite rates.

## Proof

**Kernel and Perron reduction.** The source model's fast-explorer matrix is \(F=(1+g)I+fL\) for equal patch sizes and undirected dispersal. Substituting the symmetric feasibility matrix \(C=\xi f/(1+f)A\) gives the stated \(K(f)\). For any \(f>0\), \(F\) is a symmetric positive-definite irreducible nonsingular \(M\)-matrix; consequently \(F^{-1}\) is entrywise positive. As every vertex has positive degree, \(F^{-1}A\) is entrywise positive. Its spectral radius \(\mu(f)\) is a simple positive eigenvalue with a positive right eigenvector. It equals the largest real generalized eigenvalue in
\[
Av=\mu(aI+fL)v.
\]
The capacity is \(\Lambda_G(f)=\xi f\mu(f)/(1+f)\).

**High-exploration degree energy.** Since \(G\) is connected, \(\ker L=\operatorname{span}\{\mathbf1\}\), and the inverse \((aI+fL)^{-1}\) converges to \(\mathbf1\mathbf1^T/(an)\). Thus \((aI+fL)^{-1}A\) converges to the rank-one nonnegative matrix \(\mathbf1 d^T/(an)\). Its sole nonzero eigenvalue is \(\mu_0=\bar d/a>0\), simple, so standard finite-matrix perturbation yields a positive eigenvector normalized by \(\mathbf1^Tv=n\) of the form \(v=\mathbf1+f^{-1}u+O(f^{-2})\), with \(\mathbf1^Tu=0\), and an expansion \(\mu=\mu_0+f^{-1}\mu_1+O(f^{-2})\). The constant-order generalized eigen-equation is
\[
d=\mu_0(a\mathbf1+Lu),\quad Lu=(a/\bar d)h,\quad u=(a/\bar d)L^+h.
\]
Multiplying the *exact* generalized eigen-equation by \(\mathbf1^T\) gives \(d^Tv=an\mu\). Therefore \(\mu_1=d^Tu/(an)=S/(n\bar d)\). Multiplication by \(\xi f/(1+f)=\xi(1-f^{-1}+O(f^{-2}))\) proves the general expansion, including its coefficient and its stipulated equality limitation.

**Exact star spectrum.** Suppose the graph is the star with one hub and \(m\) leaves. On the two-dimensional invariant subspace in which all leaves have the same coordinate, adjacency and Laplacian act by
\[
A_R=\begin{pmatrix}0&m\\1&0\end{pmatrix},\qquad
L_R=\begin{pmatrix}m&-m\\-1&1\end{pmatrix}.
\]
On the complementary leaf-difference subspace, \(A\) vanishes. Hence all remaining eigenvalues of \((aI+fL)^{-1}A\) are zero. Its positive Perron eigenvalue is the positive root of
\[
P(\mu)=a(a+(m+1)f)\mu^2-2mf\mu-m=0.
\]
The positive root is
\[
\mu_+(f)=\frac{mf+\sqrt{m^2f^2+ma(a+(m+1)f)}}{a(a+(m+1)f)},
\]
which gives \(\Lambda_m(f)\) and its limit as asserted. The negative second root and the zero leaf-difference roots cannot exceed this positive Perron root.

**Sharp crossing.** The comparison \(\Lambda_m(f)>\Lambda_m(\infty)\) is equivalent to \(\mu_+(f)>u\), where \(u=2m(1+f)/(a(m+1)f)>0\). Since \(P(0)=-m<0\) and \(P\) has exactly one positive root, \(\mu_+>u\) is equivalent to \(P(u)<0\). Exact substitution yields
\[
\frac{af^2(m+1)^2}{m}P(u)
=-\delta f^2+Bf+4am.
\]
For \(\delta\le0\), the right side is strictly positive at all \(f>0\). For \(\delta>0\), it is strictly positive until its unique positive root \(f_*\), zero there, and strictly negative afterwards. This proves the complete finite-rate comparison. Because \(\Lambda_m(f)\to0\) at \(f\downarrow0\), approaches \(\Lambda_m(\infty)\) at infinity, and is strictly above that limiting value somewhere when \(\delta>0\), a finite global maximizer exists. The positive first-order correction shown above also implies eventual strict decrease through its differentiable asymptotic expansion.

**Rational survival-threshold example.** Set \(m=20\), \(a=10\), \(f=5\), and \(\xi=1\). For an invasion threshold of \(e/c=1/5\), the corresponding positive-root comparison value is \(u=(1/5)(1+f)/f=6/25\). Direct substitution gives \(P(6/25)=-44/25<0\); hence \(\Lambda_{20}(5)>1/5\). At infinite exploration, \(\Lambda_{20}(\infty)=4/21<1/5\), so \(\Lambda_{20}(f)<1/5\) for all sufficiently large finite \(f\). When \(c\Lambda_G(f)<e\), multiplying the population equation by a positive left Perron vector of \(K\) yields exponential decay to extinction. When \(c\Lambda_G(f)>e\), a sufficiently small positive multiple of the right Perron vector is a strict subsolution, and \(\mathbf1\) is a strict supersolution. Cooperativity, boundedness, and monotone comparison give a positive equilibrium between them, establishing the stated persistence possibility.

## Verification

The standalone `verify.py` uses Python's exact rational arithmetic to check the two-dimensional star matrix identities and the full finite-rate crossing-polynomial identity in 1,302 parameter triples; it additionally tests floating-point spectral comparison signs on the same grid. It also solves exact Laplacian equations to verify the star degree energy for 20 star sizes, checks an additional non-star connected graph, verifies \(P(6/25)=-44/25\), and compares several numerical large-rate values against the proved asymptotic expansion. On replay it prints four PASS lines. The proof above is analytic; exhaustive testing over a finite parameter grid is not a proof of the all-parameter statements.

## Relationship to prior work

Bernardi et al. (2026) derive the fast-explorer kernel, admit explorer death and nonuniform habitat extinction, and identify the leading eigenvalue as a metapopulation survival threshold. The present result analyzes how that eigenvalue depends on the exploration parameter, obtains the previously unstated first-order Laplacian-energy correction, and gives an exact mortality-dependent finite-overmixing boundary for star networks. The earlier Nicoletti et al. (2023) framework analyzes the zero-intrinsic-mortality kernel and gives the infinite-exploration degree limit; that limit alone does not determine whether a finite exploration rate can do better. The explicit star boundary requires positive intrinsic explorer mortality, and hence cannot be recovered as an instance of the earlier zero-mortality star case. Jorba-Cuscó et al. (2024) optimize equilibrium total population in a distinct direct-diffusion, two-patch logistic model; neither the observable nor the evolution equation is the same. See the associated review for comparison details and residual priority risk.

## Limitations

The finding uses one particular saturating explorability law; changing that law can change the threshold. It assumes a connected undirected graph, equal patch capacities and uniform local vital rates, independent explorer mortality, and fast-explorer quasi-stationarity. No result about finite carrying capacity, stochastic lifetime, globally optimal finite exploration rate in closed form, or arbitrary directed or nonuniform networks is asserted. The general degree-energy expansion determines only the first-order high-rate comparison, not all-rate monotonicity. Historical priority is not independently certified.

## References

1. D. Bernardi, A. Doimo, G. Nicoletti, P. Padmanabha, A. Rinaldo, S. Suweis, S. Azaele, and A. Maritan, *Habitat heterogeneity and dispersal network structure as drivers of metacommunity dynamics*, arXiv:2602.06640, first posted 2026-02-06. https://arxiv.org/abs/2602.06640
2. G. Nicoletti, P. Padmanabha, S. Azaele, S. Suweis, A. Rinaldo, and A. Maritan, *Emergent encoding of dispersal network topologies in spatial metapopulation models*, PNAS 120 (2023), e2311548120. https://doi.org/10.1073/pnas.2311548120
3. M. Jorba-Cuscó, R. I. Oliva-Zúniga, J. Sardanyés, and D. Pérez-Palau, *Optimal dispersal and diffusion-enhanced robustness in two-patch metapopulations: origin's saddle-source nature matters*, Theory in Biosciences 143 (2024), 79–95. https://doi.org/10.1007/s12064-023-00411-2
