# The exact first breakpoint of finite metric emergence
## Finding
Let \(X\) be a compact metric space, let \(f:X\to X\) be measurable, and let \(\mu\) be a probability measure. Use the Kantorovich-Wasserstein distance \(d_W\) on \(\mathcal M(X)\), and let \(\mathscr E_\mu(f)\) and \(\mathscr E'_\mu(f)\) denote Berger's metric and second metric emergences, with the strict error convention in Definition 1.1 and Definition 1.2 of arXiv:2609.28264v1.

Assume
\[
N:=\limsup_{\varepsilon\downarrow0}\mathscr E'_\mu(f)(\varepsilon)\in\{2,3,\ldots\}.
\]
Berger's Theorem 1.4 yields distinct measures \(\nu_1,\ldots,\nu_N\) whose basins cover \(\mu\)-almost every point. Write
\[
B(\nu_i):=\{x:\mathsf e_n^f(x)\to\nu_i\},\qquad p_i:=\mu(B(\nu_i)).
\]
Then every \(p_i>0\). Define
\[
\Delta:=\min_{1\le i<j\le N}\min\{p_i,p_j\}d_W(\nu_i,\nu_j).
\]
The number \(\Delta\) is positive and is exactly the first small-scale breakpoint of metric emergence:
\[
\mathscr E_\mu(f)(\varepsilon)=\mathscr E'_\mu(f)(\varepsilon)=N
\quad\text{for every }0<\varepsilon\le\Delta,
\]
whereas
\[
\mathscr E_\mu(f)(\varepsilon)=\mathscr E'_\mu(f)(\varepsilon)\le N-1
\quad\text{for every }\varepsilon>\Delta.
\]
Equivalently, if \(D_k\) denotes the optimal average \(k\)-prototype distortion of the empirical-limit law, then
\[
D_{N-1}=\Delta.
\]
This gives an exact finite-resolution margin, rather than only the qualitative statement that finitely many basins cover almost every point.

## Assumptions and scope
The phase space \(X\) is compact and metric. The map \(f\) is only required to be measurable. No invariance of \(\mu\) is assumed. The hypothesis is precisely finite second metric emergence in the sense of Berger's Theorem 1.4, with finite value \(N\ge2\). The claim concerns the \(1\)-Wasserstein/Kantorovich version used in arXiv:2609.28264v1.

The basin measures \(p_i\) are not additional assumptions. Berger's theorem gives almost-everywhere convergence to one of the \(N\) limits. If some \(p_i=0\), then the empirical-limit law would be supported on at most \(N-1\) points, so \(N-1\) prototypes would give zero limiting average distortion, contradicting the definition of the finite small-scale value \(N\). Thus all \(p_i\) are positive. Distinctness of the \(\nu_i\) and finiteness then imply \(\Delta>0\).

## Proof
By Berger's Theorem 1.4, \(\mathsf e_n^f(x)\) converges for \(\mu\)-almost every \(x\) to one of \(\nu_1,\ldots,\nu_N\). Hence the system is empirical. Proposition 1.3 of the same paper therefore gives
\[
\mathscr E_\mu(f)=\mathscr E'_\mu(f).
\]
Let \(\eta=(\mathsf e^f)_*\mu\) be the empirical-limit law. The basin decomposition gives
\[
\eta=\sum_{i=1}^N p_i\,\delta_{\nu_i}.
\]
For a finite set \(F\subset\mathcal M(X)\), define its average distortion
\[
C_\eta(F):=\int d_W(\nu,F)\,d\eta(\nu)
=\sum_{i=1}^N p_i d_W(\nu_i,F).
\]
Berger's Theorem 1.12, equivalently Berger-Bochi Proposition 3.2 applied to \(\eta\), identifies metric emergence with the least cardinality of \(F\) for which \(C_\eta(F)<\varepsilon\). Put
\[
D_{N-1}:=\inf_{1\le |F|\le N-1}C_\eta(F).
\]
We prove \(D_{N-1}=\Delta\).

For the lower bound, fix any \(F\) with at most \(N-1\) points. Assign each \(\nu_i\) to a nearest point of \(F\). By the pigeonhole principle, two distinct atoms, say \(\nu_i\) and \(\nu_j\), are assigned to the same center \(c\in F\). If \(p_i\le p_j\), then the contribution of these two atoms satisfies
\[
p_i d_W(\nu_i,c)+p_j d_W(\nu_j,c)
\ge p_i\bigl(d_W(\nu_i,c)+d_W(\nu_j,c)\bigr)
\ge p_i d_W(\nu_i,\nu_j)
\ge\Delta.
\]
The first inequality uses \(p_j\ge p_i\); the second is the triangle inequality. The case \(p_j\le p_i\) is symmetric. Since every remaining contribution is nonnegative, \(C_\eta(F)\ge\Delta\), and therefore \(D_{N-1}\ge\Delta\).

For the upper bound, choose a pair \(r\ne s\) attaining \(\Delta\), and suppose \(p_r\le p_s\). Take
\[
F=\{\nu_i: i\ne r\}.
\]
This set has \(N-1\) points. Every atom except \(\nu_r\) has zero distance to \(F\), while \(\nu_s\in F\), so
\[
C_\eta(F)=p_r d_W(\nu_r,F)
\le p_r d_W(\nu_r,\nu_s)=\Delta.
\]
Together with the lower bound this proves \(D_{N-1}=\Delta\).

If \(0<\varepsilon\le\Delta\), no family of at most \(N-1\) prototypes has distortion strictly below \(\varepsilon\), whereas the \(N\) points \(\nu_1,\ldots,\nu_N\) give distortion zero. Thus the emergence is exactly \(N\). If \(\varepsilon>\Delta\), the preceding \(N-1\)-point set has distortion \(\Delta<\varepsilon\), so the emergence is at most \(N-1\). This proves the claim.

## Verification
The proof uses only four ingredients: Berger's finite-second-emergence theorem to obtain finitely many almost-everywhere empirical limits; equality of the two metric emergences for empirical systems; the quantization characterization of metric emergence; and the triangle inequality in \(\mathcal M(X)\).

The key new finite-metric calculation was checked independently in both directions. The lower bound does not assume that optimal centers are empirical-limit atoms: the pigeonhole argument allows arbitrary centers in \(\mathcal M(X)\). The upper bound uses an explicit \(N-1\)-point family. The strict inequality in Berger's emergence definition is retained, which is why the value is still \(N\) at the endpoint \(\varepsilon=\Delta\).

No finite experiment, numerical approximation, or unproved exhaustion is used.

## Relationship to prior work
Berger's 2026 survey proves that finite second metric emergence forces finitely many almost-everywhere basins (Theorem 1.4), proves equality of the two metric emergences for empirical systems (Proposition 1.3), and recalls the quantization characterization (Theorem 1.12). Those statements do not evaluate the first nonzero finite-resolution breakpoint after the basin decomposition is known.

Berger and Bochi's earlier quantization framework gives the general identity between emergence and quantization of an ergodic decomposition, and Proposition 3.2 rewrites \(1\)-Wasserstein quantization as minimizing average distance to a finite set. The present result computes the \(N-1\)-prototype distortion for an arbitrary finite atomic empirical-limit law in an arbitrary metric space: it is exactly the minimum weighted pair separation \(\Delta\). This explicit value is not stated in the inspected emergence sources. This converts the qualitative finite-emergence conclusion into an exact resolution margin.

General quantization literature contains extensive results on optimal codebooks, including finite and discrete distributions. A targeted search did not locate this arbitrary-metric \(L^1\), \(N-1\)-center formula stated as an emergence breakpoint. Because the finite-metric argument is elementary, an implicit or folklore occurrence in the broader facility-location or quantization literature remains a residual originality risk.

## Limitations
The formula is specific to the first drop from \(N\) to fewer than \(N\) prototypes. For \(k\le N-2\), several atoms may have to share centers, and the exact distortion is a genuine weighted \(k\)-median problem; no closed formula is claimed here. The result also uses the average-distance, \(1\)-Wasserstein form of emergence. Analogues for higher Wasserstein powers have different pair costs and are not asserted.

The result does not prove that the emergence equals exactly \(N-1\) for every \(\varepsilon>\Delta\); at larger resolutions it may drop by more than one. What is proved is that \(\Delta\) is the exact first threshold at which the value becomes strictly smaller than \(N\).

## References
1. Pierre Berger, *Emergence in dynamical systems*, arXiv:2609.28264v1, 23 September 2026. Relevant items: Proposition 1.3, Theorem 1.4, Theorem 1.12, and Section 4.1.
2. Pierre Berger and Jairo Bochi, *On Emergence and Complexity of Ergodic Decompositions*, arXiv:1901.03300; *Advances in Mathematics* 390 (2021), 107904. Relevant items: Proposition 3.2 and Proposition 3.12.
3. Siegfried Graf and Harald Luschgy, *Foundations of Quantization for Probability Distributions*, Lecture Notes in Mathematics 1730, Springer, 2000. General quantization background.
