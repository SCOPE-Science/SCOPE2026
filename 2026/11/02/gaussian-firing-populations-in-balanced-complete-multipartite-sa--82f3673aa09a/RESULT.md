# Gaussian firing populations in balanced complete multipartite sandpiles

## Finding

Fix an integer \(r\ge3\). On the labelled graph \(G_{r,n}=K_{n,\ldots,n}\) with \(r\) distinguished shores of size \(n\ge1\), use synchronous ordinary degree-threshold chip firing: at every update, each vertex containing at least its degree in chips sends one chip to each neighbor; every other vertex waits. Let \(N_{r,n}\) count distinct *primitive two-cycles* of nonnegative integer chip configurations, one per two-state temporal orbit. Write \(d=(r-1)n\), \(k=(k_1,\ldots,k_r)\), and \(s_i=\sum_{j\ne i}k_j\). With \(0^0=1\), the exact count is

\[
N_{r,n}=\frac12\sum_{k_1=0}^{n}\cdots\sum_{k_r=0}^{n}
\prod_{i=1}^{r}\binom{n}{k_i}(d-s_i)^{k_i}s_i^{n-k_i}.
\]

For every *fixed* \(r\ge3\), as \(n\to\infty\),

\[
\boxed{N_{r,n}\sim \frac14\left(\frac{r-1}{r-2}\right)^{r-1}((r-1)n)^{rn}.}
\]

Choose one primitive two-cycle uniformly and then choose one of its two phases uniformly. Let \(K_{i,n}\) be the number of firing vertices on shore \(i\) in the selected phase. The vector of centered, square-root-scaled firing populations converges jointly in distribution:

\[
\left(\frac{K_{i,n}-n/2}{\sqrt n}\right)_{i=1}^{r}
\xrightarrow{\mathrm d}\mathcal N_r(0,\Sigma_r),
\quad
\Sigma_r=\frac{(r-1)^2}{4(r-2)^2}\left(I_r-\frac{J_r}{r}\right)
+\frac{J_r}{16r},
\]

where \(I_r\) is the identity matrix and \(J_r\) is the all-ones matrix. In particular, \(\Sigma_3\) has diagonal entries \(11/16\) and off-diagonal entries \(-5/16\), while \(N_{3,n}\sim(2n)^{3n}\). This fixed-shore-number Gaussian regime is structurally different from the two-shore case: at \(r=2\), the entropy maximizers form a full interval rather than a unique nondegenerate point.

## Assumptions and scope

Every shore has exactly \(n\) labelled vertices, \(r\) is held fixed when taking \(n\to\infty\), chips are nonnegative integers, the graph has no loops, and all firings are simultaneous. The probability law is uniform on primitive two-cycle *orbits* with a uniform phase, **not** uniform over all chip configurations at a fixed chip total. The theorem makes no assertion about attraction basins, other primitive periods, or joint limits where \(r\) grows with \(n\).

## Proof

**1. Alternating firing is necessary and sufficient.** For a connected graph, write \(f_t(v)\in\{0,1\}\) for whether vertex \(v\) fires on update \(t\). A state returning after two steps satisfies \(L(f_0+f_1)=0\), where \(L\) is the ordinary graph Laplacian. Its kernel on a connected graph consists of constant vectors, so \(f_0(v)+f_1(v)=q\) for every vertex, with \(q\in\{0,1,2\}\). If \(q=0\) or \(q=2\), all vertices make the same decision in each phase, and one update leaves the state unchanged; hence a primitive two-cycle requires \(q=1\). Thus every vertex alternates firing and waiting. Conversely, if every vertex switches firing status on the next update, \(f_1=\mathbf1-f_0\) and the two-step chip displacement is \(-L(f_0+f_1)=0\), giving a primitive two-cycle (the status vector changes).

Fix the time-zero firing set \(S\). Let \(t_v=|N(v)\cap S|\) and \(d_v=\deg(v)\). For \(v\in S\), the inequalities \(\sigma(v)\ge d_v\) and \(\sigma(v)-d_v+t_v<d_v\) give precisely \(d_v-t_v\) choices \(\sigma(v)\in\{d_v,\ldots,2d_v-t_v-1\}\). For \(v\notin S\), the inequalities \(\sigma(v)<d_v\) and \(\sigma(v)+t_v\ge d_v\) give precisely \(t_v\) choices \(\sigma(v)\in\{d_v-t_v,\ldots,d_v-1\}\). All intervals are nonnegative, and the choices are independent vertex by vertex. Therefore the number of phase states with firing set \(S\) is

\[
\prod_{v\in S}(d_v-t_v)\prod_{v\notin S}t_v.
\]

On \(G_{r,n}\), if shore \(i\) contains \(k_i\) firing vertices, each vertex there has \(d=(r-1)n\) and \(t_v=s_i\). There are \(\prod_i\binom n{k_i}\) choices of labelled firing sets. Summing the preceding product counts all primitive period-two states, each orbit exactly twice, and proves the finite formula.

**2. A unique entropy maximizer appears when \(r\ge3\).** Set \(x_i=k_i/n\), \(y_i=\sum_{j\ne i}x_j/(r-1)\), and \(D(p\Vert q)=p\log(p/q)+(1-p)\log((1-p)/(1-q))\), using the usual endpoint conventions. Divide the summand by \(d^{rn}\). The normalized weight is

\[
W_n(k)=\prod_{i=1}^{r}\binom n{k_i}(1-y_i)^{k_i}y_i^{n-k_i}.
\]

The elementary entropy bound \(\binom nk\le\exp(nH(k/n))\) implies

\[
W_n(k)\le\exp(n\Phi(x)),\qquad
\Phi(x)=-\sum_{i=1}^{r}D(x_i\Vert1-y_i)\le0.
\]

Equality holds exactly when \(x_i=1-y_i\) for all \(i\). Equivalently \((r-2)x_i+\sum_jx_j=r-1\). Since \(r\ge3\), subtracting two equations forces all coordinates equal; their only common value is \(1/2\). Hence \(x_*=(1/2,\ldots,1/2)\) is the unique global maximizer on the whole closed unit cube. This uniqueness fails for \(r=2\), when equality holds along \(x_1+x_2=1\).

**3. Gaussian expansion and uniform tails.** Write \(x=x_*+\delta\) and put

\[
M_r=\frac{(r-2)I_r+J_r}{r-1},\qquad H_r=4M_r^2.
\]

Since \(x_i-(1-y_i)=(M_r\delta)_i\), Taylor expansion of binary relative entropy at equal half-probabilities gives

\[
\Phi(x_*+\delta)=-2\lVert M_r\delta\rVert^2+O_r(\lVert\delta\rVert^3)
=-\frac12\delta^{\mathsf T}H_r\delta+O_r(\lVert\delta\rVert^3).
\]

The eigenvalues of \(M_r\) are \(2\) along the constant vector and \(\alpha_r=(r-2)/(r-1)>0\) on its orthogonal complement. Pinsker's binary inequality gives \(\Phi(x)\le-2\lVert M_r(x-x_*)\rVert^2\le-2\alpha_r^2\lVert x-x_*\rVert^2\) everywhere, including endpoints by limits. This supplies global exponential control of all weights away from the central window. On the window \(\lVert x-x_*\rVert\le n^{-1/3}\), uniform Stirling asymptotics imply

\[
W_n(k)=\left(\frac{2}{\pi n}\right)^{r/2}
\exp\!\left[-\frac12u^{\mathsf T}H_ru+o_r(1)\right],
\quad u_i=\frac{k_i-n/2}{\sqrt n},
\]

with the error uniform on every bounded \(u\)-set. The Pinsker bound combined with uniform local Stirling factors controls the rescaled Gaussian tails; outside the \(n^{-1/3}\) window the total weight is exponentially small even after summing at most \((n+1)^r\) lattice points. Riemann-sum convergence with mesh \(n^{-1/2}\) yields both the multivariate central limit theorem and the normalization

\[
\frac{2N_{r,n}}{d^{rn}}\longrightarrow
\left(\frac2\pi\right)^{r/2}\int_{\mathbb R^r}e^{-u^{\mathsf T}H_ru/2}\,du
=\frac{2^r}{\sqrt{\det H_r}}.
\]

Because \(H_r\) has eigenvalues \(16\) once and \(4\alpha_r^2\) with multiplicity \(r-1\), its determinant is \(16(4\alpha_r^2)^{r-1}\). Thus \(2^r/\sqrt{\det H_r}=1/(2\alpha_r^{r-1})\), proving the asserted orbit asymptotic after dividing by two. Finally \(H_r^{-1}\) acts by \(1/16\) along the constant vector and \(1/(4\alpha_r^2)\) transversely, which is the stated \(\Sigma_r\).

## Verification

The standalone `verify.py` enumerates all confined labelled chip states on the four finite graphs \(G_{3,1}\), \(G_{3,2}\), \(G_{4,1}\), and \(G_{5,1}\), testing exactly which have primitive period two by explicitly applying the update twice. Across these cases it tests \(296{,}272\) states and compares the exact orbit counts to the independent firing-set formula. It additionally computes six finite-\(n\) exact enumerations and second moments for fixed part numbers \(3,4,5\), comparing to the stated limiting constants; these numerical comparisons illustrate convergence, rather than prove the asymptotic theorem. Run `python3 verify.py` with Python's standard library. The recording `verification_output.txt` accompanies the source.

## Relationship to prior work

Jiang (2010, arXiv:1003.0943) established possible periods for bipartite chip-firing and constructed periods on higher complete multipartite graphs; his Proposition 2.5 gives the equal-firing-count criterion used above. Scully, Zhang, and Jiang (2011, *Total Chip Numbers and Motors in the Parallel Chip-Firing Game*, Lemma 4.1) already characterized two-periodic states on arbitrary connected graphs by a local chip inequality. The present exact finite sum is a specialized enumeration of that known characterization, **not** a claim to discover the two-cycle criterion. The additional asymptotic orbit constant and a nondegenerate \(r\)-variate Gaussian law for every fixed \(r\ge3\), together with the singular two-shore entropy ridge, are the asserted new mathematical content. Jung (2026, arXiv:2608.01350) proves a chip-total condition forcing eventual period two on complete bipartite graphs; it does not address uniformly sampled multipartite primitive-orbit firing populations.

## Limitations

The novelty assessment is based on accessible indexed literature and mathematical-record searches, not an exhaustive proof of priority. In particular, the general two-cycle characterization is previously known and the finite summation follows readily from it; the distinct contribution is the analytic limit theorem. The proof does not treat varying numbers of shores, unequal shore sizes, higher periods, or basins. The Gaussian limit is asymptotic for fixed \(r\), and numerical finite checks are not its proof. No independent mathematical audit is claimed.

## References

1. Tian-Yi Jiang, *On the Period Lengths of the Parallel Chip-Firing Game* (first arXiv posting 2010-03-04), arXiv:1003.0943, https://arxiv.org/abs/1003.0943 ; full HTML https://ar5iv.labs.arxiv.org/html/1003.0943 .
2. Ziv Scully, Yan Zhang, and Damien Jiang, *Total Chip Numbers and Motors in the Parallel Chip-Firing Game* (2011 document), https://math.mit.edu/research/highschool/primes/materials/2011/Scully-Zhang-Jiang.pdf , particularly Section 4, Lemma 4.1.
3. Minkyu Jung, *The Middle Stair for Complete Bipartite Parallel Chip-Firing* (first arXiv posting 2026-08-02), arXiv:2608.01350, https://arxiv.org/abs/2608.01350 .
