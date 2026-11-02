# A smallest-prime-factor law for Crank–Nicolson positivity on budgeted multipartite networks

## Finding
Fix an integer \(N\ge3\) and a total conductance budget \(B>0\). Choose any connected complete multipartite graph \(G=K_{n_1,\ldots,n_k}\), where \(k\ge2\), each \(n_i\ge1\), and \(\sum_i n_i=N\). Allocate the budget **equally to every existing edge**, so its conductance is \(w=B/|E(G)|\). Write \(L_G\) for the *unit-conductance combinatorial* Laplacian, and evolve diffusion \(\dot u=-wL_Gu\) with the Crank–Nicolson end-step
\[
C_G(h)=(I+hwL_G/2)^{-1}(I-hwL_G/2),\qquad h\ge0.
\]
Let \(a=\min_i n_i\), and set
\[
\sigma_N(a)=\frac{a+\sqrt{a^2+4(N-2)(N-a)}}{2(N-2)(N-a)}.
\]
Then the **exact positivity radius** for this network is
\[
C_G(h)\text{ is entrywise nonnegative}
\quad\Longleftrightarrow\quad 0\le h\le H_G,
\qquad H_G=\frac{2|E(G)|}{B}\,\sigma_N(a).
\]
At the positive endpoint, precisely the diagonal entries corresponding to vertices in the smallest parts vanish; every off-diagonal entry remains strictly positive. After the endpoint, these diagonal entries are negative.

Let \(p\) be the smallest prime divisor of \(N\), and let \(d=N/p\), its largest proper divisor (for prime \(N\), this means \(p=N\), \(d=1\)). **Among every eligible complete multipartite topology**, the unique maximizing graph up to isomorphism is
\[
G_*=K_{\underbrace{d,\ldots,d}_{p\text{ parts}}}.
\]
Its exact maximum admissible physical time step is
\[
\boxed{\ H_*(N,B)=\frac{N}{2B(N-2)}
\left[d+\sqrt{d^2+4(N-2)(N-d)}\right].\ }
\]
Thus even order selects a balanced complete bipartite graph; odd orders divisible by three select three equal parts unless the order is even; prime orders select the complete graph. More generally the number of equal parts is exactly the smallest prime factor. If the smallest prime divisor \(p\) is held fixed along growing orders, then
\[
H_*(N,B)=\frac NB+\frac{2}{B(2-1/p)}+O\!\left(\frac1{BN}\right).
\]

## Assumptions and scope
All vertices have unit mass, all existing edges are undirected and have the **same** strictly positive conductance \(B/|E(G)|\); nonedges carry no flux. The budget is the **sum of edge conductances**, not a cost assigned independently to vertices. The number of vertices \(N\), the budget \(B\), and the Crank–Nicolson scheme are fixed. The optimization variable is the integer multipartition, with no restriction on its number of parts beyond connectivity. The assertion is not an optimization over arbitrary connected graphs, nonuniform edge allocations, normalized Laplacians, or nonlinear time integrations. The operator is the combinatorial graph Laplacian, with no exterior Dirichlet boundary.

## Proof
**1. Resolvent decomposition.** Write \(s=hw/2\) and \(R_s=(I+sL_G)^{-1}\), so \(C_G(h)=2R_s-I\). The inverse is strictly positive entrywise for \(s>0\) because \(I+sL_G\) is an irreducible nonsingular \(M\)-matrix. Thus only its diagonal may obstruct positivity.

For a vertex in a part of size \(a\), the orthogonal Laplacian decomposition consists of the constant eigenvalue-zero subspace, the dimension-\(k-1\) part-constant subspace of eigenvalue \(N\), and the within-part sum-zero subspace of eigenvalue \(N-a\). The corresponding diagonal projector weights at that vertex are \(1/N\), \(1/a-1/N\), and \(1-1/a\), respectively. Consequently its diagonal resolvent entry is exactly
\[
R_a(s)=\frac1N+\frac{N-a}{aN(1+Ns)}
          +\frac{a-1}{a[1+(N-a)s]}.
\]
A direct common-denominator calculation gives
\[
R_a(s)-\frac12=
\frac{1+as-(N-2)(N-a)s^2}
{2(1+Ns)[1+(N-a)s]}.
\]
For \(N\ge3\), the quadratic numerator has exactly one positive zero, namely \(\sigma_N(a)\), and is positive below it and negative above it. Moreover, for \(a>b>0\),
\[
R_a(s)-R_b(s)=
\frac{s(a-b)[1+(N-1)s]}
{(1+Ns)[1+(N-a)s][1+(N-b)s]}>0
\qquad(s>0).
\]
Thus the smallest part gives exactly the first zero diagonal. Setting \(s=hw/2=hB/(2|E|)\) proves the claimed graph-specific radius and endpoint statements. The same ordering and the strict decrease of \(R_a(s)\) in \(s\) show that \(\sigma_N(a)\) is strictly increasing in \(a\).

**2. A continuous comparison lemma.** For real \(1\le x\le N/2\) put
\[
D(x)=\sqrt{x^2+4(N-2)(N-x)},\qquad
F(x)=\frac{N(N-x)}2\,\sigma_N(x)
     =\frac{N[x+D(x)]}{4(N-2)}.
\]
Then \(F'(x)>0\), and, more sharply,
\[
0<F'(x)\le\frac{\sigma_N(x)}2.
\]
Here is a direct verification of the nonstandard inequality. Differentiating the identity
\(1+x\sigma_N(x)=(N-2)(N-x)\sigma_N(x)^2\) gives
\[
\frac{\sigma_N'(x)}{\sigma_N(x)}=
\frac{1+(N-2)\sigma_N(x)}
{2(N-2)(N-x)\sigma_N(x)-x}.
\]
The denominator is \(D(x)>0\). Substitution into \(F'=N[-\sigma_N+(N-x)\sigma_N']/2\) shows that \(F'\le\sigma_N/2\) is equivalent to
\[
\frac{D(x)}{2N-x}\ge\frac{N}{N+2}.
\]
Indeed,
\[
\frac{d}{dx}\frac{D(x)^2}{(2N-x)^2}
=\frac{8x}{(2N-x)^3}>0,
\]
and at \(x=1\) the left-hand ratio is
\((2N-3)/(2N-1)\ge N/(N+2)\), the last inequality being exactly \(2(N-3)\ge0\). This proves the upper derivative bound. Separately, \(D(x)^2-[2(N-2)-x]^2=8(N-2)>0\), which proves \(F'(x)>0\) from its explicit derivative.

**3. Integer-partition comparison.** Let \(a=\min_i n_i\) and put
\[
\delta=\frac12\sum_i n_i(n_i-a)\ge0.
\]
The edge count satisfies \(|E|=[N^2-\sum_i n_i^2]/2=N(N-a)/2-\delta\), and hence
\[
\frac B2 H_G=|E|\sigma_N(a)=F(a)-\delta\sigma_N(a).
\]
Let \(d=N/p\) be the largest proper divisor. The equal-part graph \(G_*\) exists and has \(\delta=0\), so \(BH_{G_*}/2=F(d)\).

If \(a\le d\), monotonicity gives \(F(a)-\delta\sigma_N(a)\le F(a)\le F(d)\). Equality forces \(a=d\), \(\delta=0\), and therefore every part has size \(d\).

If \(a>d\), the partition cannot be uniform: otherwise \(a\) would be a proper divisor larger than \(d\). A part of size at least \(a+1\) forces \(2\delta=\sum_i n_i(n_i-a)\ge a+1\). By the derivative bound and monotonicity of \(\sigma_N\),
\[
F(a)-F(d)\le\frac12\int_d^a\sigma_N(x)\,dx
\le\frac{a-d}{2}\sigma_N(a)
<\frac{a+1}{2}\sigma_N(a)
\le\delta\sigma_N(a).
\]
Thus \(F(a)-\delta\sigma_N(a)<F(d)\) in this case. This proves **global optimality and uniqueness** among all eligible integer partitions, with no unproved convexity assumption.

**4. Exact maximum and asymptotics.** Substituting \(d=N/p\), \(|E(G_*)|=N(N-d)/2\) into the graph-specific formula gives the boxed result. For fixed \(p\), write \(\alpha=1/p\); then
\(D(\alpha N)=N(2-\alpha)-4(1-\alpha)/(2-\alpha)+O(N^{-1})\). Expanding \(2F(\alpha N)/B\) proves the displayed limiting correction.

## Verification
The standalone `verify.py` uses only the Python standard library. It independently constructs dense graph Laplacians and performs exact-fraction Gaussian elimination, checks the diagonal return formula and strict off-diagonal positivity, brackets each quadratic crossing with exact rational signs, and checks matrix nonnegativity on both sides of the predicted boundary under the equal-edge budget. It also exhausts **every multipartition for each order through eighteen** and compares all balanced fixed-part-count competitors through order one thousand. Executing `python verify.py` produced `VERIFY_OK 503211`. The numerical partition census is a diagnostic, **not** the proof of the all-order optimization, which is Step 3 above.

## Relationship to prior work
Faragó and Horváth (2006) develop discrete maximum-principle and nonnegativity conditions for parabolic discretizations; this work motivates sharp end-step positivity. The published resolvent-return law for reversible Markov chains (2026) already gives the identity \(C=2R-I\), the diagonal positivity criterion, and general single-crossing theory. None of those general facts is claimed as new here. Horváth (1998) also treats positivity radii for Runge–Kutta methods in a broad problem-class setting.

The new claim is the **closed multipartite size-dependent threshold together with the complete fixed-budget topology extremum and its smallest-prime-divisor equality classification**. Generic return-resolvent criteria do not specify an optimal partition; knowing the Laplacian eigenvalues alone also does not determine this integer optimum without the vertexwise projector calculation and comparison lemma. Delorme (2012) studies adjacency eigenvalues of complete multipartite graphs rather than this Crank–Nicolson end-step objective.

## Limitations
The conclusion requires equal rates over all installed cross-part edges. Allowing independently optimized edge conductances or arbitrary connected graphs changes the optimization problem. A larger positivity-permitted time step does **not** by itself mean faster mixing, smaller approximation error, or better accuracy. The comparison addresses exact arithmetic and does not estimate roundoff near a vanishing diagonal. The 2006 Faragó–Horváth article and several older specialized positivity sources were not available in full text for this review; an unlocated implication-equivalent statement in specialist literature remains a residual publication-priority risk. No independent mathematical audit has been performed.

## References
1. I. Faragó and R. Horváth, *Discrete Maximum Principle and Adequate Discretizations of Linear Parabolic Problems*, SIAM Journal on Scientific Computing **28** (2006), 2313–2336, DOI: 10.1137/050627241. Online publication verified as 2006-12-21. https://doi.org/10.1137/050627241
2. Z. Horváth, *Positivity of Runge–Kutta and Diagonally Split Runge–Kutta Methods*, Applied Numerical Mathematics **28** (1998), 309–326, DOI: 10.1016/S0168-9274(98)00050-6. https://doi.org/10.1016/S0168-9274(98)00050-6
3. *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains* (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a
4. C. Delorme, *Eigenvalues of Complete Multipartite Graphs*, Discrete Mathematics **312** (2012), 2532–2535, DOI: 10.1016/j.disc.2011.07.018. https://doi.org/10.1016/j.disc.2011.07.018
5. R. Horváth, I. Faragó and J. Karátson, *Qualitative properties of discrete nonlinear parabolic operators*, Numerische Mathematik **143** (2019), 529–554. https://doi.org/10.1007/s00211-019-01062-6
