# Exact sink allocation and a chi-square persistence window in balanced bipartite habitats

## Finding

Consider the complete bipartite habitat \(K_{n,n}\), with \(n\ge2\), and designate exactly \(2m\) vertices as lethal sinks, where \(1\le m<n\). A viable vertex obeys logistic growth of rate \(r>0\) and graph diffusion of rate \(D>0\), while sink density is fixed to zero. Let \(s\) be the number of sinks in the first part and put \(j=s-m\), \(q=n-m\). The principal Dirichlet eigenvalue of the original graph Laplacian restricted to viable vertices is exactly

\[
\lambda_{n,m,j}=n-\sqrt{q^2-j^2},\qquad |j|\le\min\{m,q\}.
\]

Consequently, the unique optimal *allocation count* for persistence is \(m\) sinks in each part, yielding \(\lambda_{\min}=m\). The most hostile allocations put as many sinks as feasible into a single part, yielding

\[
\lambda_{\max}=n-\sqrt{(n-m)^2-\min\{m,n-m\}^2}.
\]

These extrema are over all sink subsets of cardinality \(2m\); choices within each part are equivalent by graph symmetry. More particularly, for independent uniformly sampled sink *sets* of that fixed cardinality, \(J=s-m\) has the exact distribution

\[
\Pr(J=j)=\frac{\binom n{m+j}\binom n{m-j}}{\binom{2n}{2m}},\qquad |j|\le\min\{m,n-m\}.
\]

For any integer sequence \(m=m_n\) with \(m_n/n\to\rho\in(0,1)\), the excess critical growth-to-diffusion ratio has the **non-Gaussian**, order-one limit

\[
\boxed{\lambda_{n,m_n,J}-m_n\ \Longrightarrow\ \frac{\rho}{4}\chi^2_1.}
\]

Its mean converges to \(\rho/4\) and variance to \(\rho^2/8\). If the ecological reaction-to-diffusion ratio is tuned to \(r_n/D_n=m_n+c\) for fixed \(c>0\), then the exact probability of persistence converges to

\[
\boxed{\Pr(\text{persistence})\longrightarrow
\operatorname{erf}\!\left(\sqrt{2c/\rho}\right).}
\]

For \(c\le0\) persistence has probability zero at every finite size. Thus optimal placement, random placement and worst-case placement differ sharply even at the same number of lethal sites: random allocation incurs an order-one chi-square threshold penalty; adversarial allocation can incur an order-\(n\) penalty.

## Assumptions and scope

The graph has two disjoint parts \(U,V\), each of size \(n\), and every edge between the two parts is present. Let \(S\subset U\cup V\) contain exactly \(2m\) sinks. Write \(F=(U\cup V)\setminus S\) for the viable sites. For each \(i\in F\), with the density at every sink fixed to zero, the model is

\[
\dot u_i=r u_i(1-u_i)-D\sum_{k\in F}L_{ik}^{(S)}u_k,\qquad u_i(0)>0,
\]

where \(L^{(S)}\) is the principal submatrix of the *original* combinatorial Laplacian \(L(K_{n,n})\), not the Laplacian of the induced viable subgraph. All parameters are homogeneous, edges are unweighted, and all initially viable sites have strictly positive densities. The strict persistence criterion is \(r/D>\lambda_{\min}(L^{(S)})\); at equality every solution becomes extinct. The randomness in the theorem concerns the sink set only, not demographic noise or random edges. The asymptotic regime has a positive limiting fraction of sinks strictly less than the whole graph and permits \(r_n/D_n\) to scale with \(n\).

## Proof

**1. Complete finite-dimensional spectrum.** If \(s=m+j\), the viable part sizes are \(a=n-s=q-j\) and \(b=n-(2m-s)=q+j\). Every original vertex has degree \(n\); hence, in the viable-vertex ordering,

\[
L^{(S)}=\begin{pmatrix}nI_a&-\mathbf1_a\mathbf1_b^{\mathsf T}\\-\mathbf1_b\mathbf1_a^{\mathsf T}&nI_b\end{pmatrix}.
\]

If both \(a,b>0\), this matrix has eigenvalues \(n-\sqrt{ab}\), \(n+\sqrt{ab}\), and \(n\) repeated \(a+b-2\) times. Indeed, on the two-dimensional subspace of vectors constant within either part, its quotient matrix is \(\left(\begin{smallmatrix}n&-b\\-a&n\end{smallmatrix}\right)\), while every within-part zero-sum vector has eigenvalue \(n\). If one part has no viable vertices, the matrix is \(nI\), and the same principal-eigenvalue formula holds because \(ab=0\). Since \(ab=q^2-j^2\), the asserted formula follows including all boundary allocations.

**2. Sharp placement extremes.** Because \(q-\sqrt{q^2-j^2}\) is strictly increasing in \(|j|\) throughout \([0,q]\), the principal eigenvalue is uniquely minimized at \(j=0\), or \(s=m\). The legal integer range is \(|j|\le\min\{m,q\}\), so its maximum occurs precisely at the two boundary allocation counts, giving the stated formula. For fixed \(m/n\to\rho\), the optimal threshold is \(\rho n+o(n)\), whereas the worst-case threshold divided by \(n\) approaches \(1-\sqrt{1-2\rho}\) if \(\rho\le1/2\), and \(1\) if \(\rho\ge1/2\). Both exceed \(\rho\) for \(0<\rho<1\).

**3. Exact random-allocation law.** With \(2m\) sinks drawn uniformly without replacement from \(2n\) vertices, the number \(s\) in the first part is hypergeometric. Choosing \(m+j\) sinks from the first part and \(m-j\) from the second gives the stated exact formula. The exact mean and variance are

\[
\mathbb E J=0,\qquad \operatorname{Var}(J)=\frac{m(n-m)}{2n-1}.
\]

Consequently the finite persistence probability for \(\theta=r/D\) can be computed without simulation as

\[
\Pr(\text{persistence})=\frac{1}{\binom{2n}{2m}}
\sum_{j=-h}^{h}\binom n{m+j}\binom n{m-j}
\mathbf1\!\left\{n-\sqrt{(n-m)^2-j^2}<\theta\right\},
\quad h=\min\{m,n-m\}.
\]

**4. Non-Gaussian critical window.** The finite-population central limit theorem for the symmetric hypergeometric distribution (also obtainable by Stirling's formula applied to the displayed probabilities) yields

\[
\frac{J}{\sqrt{m(n-m)/(2n-1)}}\Longrightarrow Z,
\qquad Z\sim N(0,1),
\]

when \(m/n\to\rho\in(0,1)\). In particular \(J=O_{\mathbb P}(\sqrt n)\). Rationalization gives the *exact* identity

\[
\lambda_{n,m,J}-m=
\frac{J^2}{(n-m)+\sqrt{(n-m)^2-J^2}}.
\]

Because \((n-m)/n\to1-\rho>0\), the denominator divided by \(2(n-m)\) converges in probability to one. Therefore

\[
\lambda_{n,m,J}-m
=\frac{J^2}{2(n-m)}(1+o_{\mathbb P}(1))
\Longrightarrow\frac{\rho}{4}Z^2.
\]

Sampling without replacement has sub-Gaussian tails \(\Pr(|J|>t)\le2\exp(-C t^2/n)\) for a fixed positive constant \(C\), and the exact identity bounds the excess by \(J^2/(n-m)\). Thus its first two powers are uniformly integrable for \(m/n\) bounded away from \(0\) and \(1\), proving convergence of the mean and variance to those of \((\rho/4)Z^2\). By continuity of the chi-square distribution at each positive \(c\),

\[
\Pr(\lambda_{n,m,J}<m+c)\to\Pr(Z^2<4c/\rho)
=\operatorname{erf}\!\left(\sqrt{2c/\rho}\right).
\]

For \(c\le0\), the strict inequality is impossible because \(\lambda\ge m\).

**5. Connection to nonlinear ecological persistence.** Let \(\varphi\) be a strictly positive principal eigenvector of \(L^{(S)}\). Such a vector exists when both viable parts are nonempty by Perron–Frobenius, and if a whole part is removed then \(L^{(S)}=nI\) and a strictly positive eigenvector may be chosen. Taking the weighted total \(H(t)=\sum_i\varphi_i u_i(t)\) gives

\[
\dot H=(r-D\lambda)H-r\sum_i\varphi_i u_i^2.
\]

If \(r\le D\lambda\), this and weighted Cauchy–Schwarz force \(H(t)\to0\), hence extinction at all viable vertices, including exact equality. If \(r>D\lambda\), a sufficiently small positive multiple of \(\varphi\) is a strict subsolution, and a sufficiently large constant is a supersolution. Monotone comparison yields a positive equilibrium. Its uniqueness follows from the strict subhomogeneity of the logistic reaction: two distinct positive equilibria scaled to first touch would violate the negative off-diagonal comparison at that coordinate. The same ordered sub-/supersolution bounds imply attraction from all strictly positive initial states. Therefore persistence is equivalent to \(r/D>\lambda\), completing the ecological interpretation.

## Verification

Run `python check.py` from the directory containing this document. It constructs the actual principal submatrix after every feasible allocation count for all \(2\le n\le16\) and \(1\le m<n\), and compares its numerically computed smallest eigenvalue with the closed-form expression. It also verifies hypergeometric probability normalization, exact centering, exact variance, and both sharp placement extrema, using rational arithmetic for the probability identities. This constitutes 864 separate matrix comparisons and 120 exact probability-law checks. The checker additionally compares exact finite-size survival probabilities against the analytically proved limiting prediction for three network sizes.

## Relationship to prior work

The Dirichlet-Laplacian persistence criterion and large-random-graph law are prior results, not claimed here. Apollonio, Tora and Vergni (arXiv:2604.00624v1, submitted 2026-04-01) prove a large-network concentration law for Erdős–Rényi habitats with sink sets and explicitly identify structured-network extensions as a direction for further investigation. Their full-text results concern random edges and a leading-order law; neither the exact fixed balanced-bipartite sink-allocation spectrum nor the order-one chi-square threshold window is stated there. Pirani and Sundaram (arXiv:1406.2271v2) give general grounded-Laplacian spectral bounds and random-graph asymptotics; those general inequalities do not determine the specific hypergeometric fluctuation law. The graph model is motivated as a controlled two-community habitat benchmark, not proposed as a representation of all real habitats. The usual hypergeometric central limit theorem and the rank-two eigenvalue reduction are standard ingredients; originality is asserted only for their combined sharp ecological allocation and finite-size persistence-window classification, subject to the literature limits below.

## Limitations

The conclusion concerns symmetric complete bipartite graphs with hard absorbing sink vertices, homogeneous logistic growth and diffusion, and exactly \(2m\) sinks. It does not extend automatically to irregular ecological networks, heterogeneous growth, stochastic epidemic dynamics, or demographic extinction. The chi-square result requires \(m/n\to\rho\in(0,1)\) and a tuned reaction-to-diffusion ratio \(m+c\). The limiting formula is not a finite-\(n\) equality. No independent external scientific audit is asserted. A potentially related general network study by Tora and Vergni (2026, doi:10.1016/j.mbs.2026.109749) could be compared only using its accessible abstract because full text could not be retrieved; it is a residual literature risk rather than evidence of novelty.

## References

1. N. Apollonio, V. Tora, D. Vergni, *The Critical Patch Size Problem in Random Graphs*, arXiv:2604.00624v1 (first public 2026-04-01), https://arxiv.org/html/2604.00624v1.
2. M. Pirani, S. Sundaram, *On the Smallest Eigenvalue of Grounded Laplacian Matrices*, arXiv:1406.2271v2 (2014), https://arxiv.org/html/1406.2271v2.
3. V. Tora, D. Vergni, *The critical patch size problem on networks*, Mathematical Biosciences 399 (2026), 109749, https://doi.org/10.1016/j.mbs.2026.109749 (abstract accessible; full text not inspected).
4. Classical hypergeometric sampling without replacement: the central limit theorem, Stirling asymptotics, and concentration inequalities; used as standard probability facts rather than claimed new results.
