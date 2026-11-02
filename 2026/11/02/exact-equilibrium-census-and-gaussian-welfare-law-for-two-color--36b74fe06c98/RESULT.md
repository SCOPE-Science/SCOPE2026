# Exact equilibrium census and Gaussian welfare law for two-color swap Schelling games on cycles

## Finding
For every labeled cycle with \(n\ge3\) vertices, color each vertex red or blue. A **swap equilibrium** means that no two differently colored occupants can exchange their sites and both strictly raise their fractions of same-colored neighbors. A coloring is an equilibrium **exactly** when it has at most two bichromatic edges or when no cyclic monochromatic run is a singleton. Consequently, fixing the two population sizes \(a,b\ge1\), with \(a+b=n\), the number of equilibrium colorings is
\[
N_{n;a,b}=n+\sum_{r=2}^{\min(\lfloor a/2\rfloor,\lfloor b/2\rfloor)}\frac nr\binom{a-r-1}{r-1}\binom{b-r-1}{r-1}.
\]
For \(a=0\) or \(b=0\), exactly one coloring exists and is stable.

Let \(J\) count bichromatic cycle edges and let \(W\) be total utility. The exact welfare generating polynomial across all stable two-color assignments is
\[
Z_n(z)=\sum_{\sigma:\,\mathrm{stable}} z^{J(\sigma)}
=\operatorname{tr}(T(z)^n)+2nz^2,\qquad
T(z)=\begin{pmatrix}1&z&0&0\\0&0&0&1\\1&0&0&0\\0&0&z&1\end{pmatrix}.
\]
In particular, setting \(\phi=(1+\sqrt5)/2\),
\[
Z_n(1)=\phi^n+(1-\phi)^n+2\cos(n\pi/3)+2n.
\]
A uniformly selected equilibrium coloring among all \(Z_n(1)\) stable labeled colorings satisfies
\[
\frac{W}{n}\xrightarrow{\mathsf P}\frac{5+\sqrt5}{10},\qquad
\frac{W-n(5+\sqrt5)/10}{\sqrt n}
\xrightarrow{\mathsf d}\mathcal N\!\left(0,\frac{\sqrt5}{25}\right).
\]
Thus the count grows as \(\phi^n\), whereas typical equilibrium welfare has a definite nonoptimal limiting fraction. The two agent colors are distinguished and no quotient by rotations or color interchange is taken.

## Assumptions and scope
The graph is the simple cycle \(C_n\) with fixed labeled vertices \(0,\ldots,n-1\), for all integers \(n\ge3\). Every site is occupied by one strategic agent with a binary type; agents sharing a type have identical utility. At a site \(v\), utility is \(u_v=(\mathbf1_{\sigma_{v-1}=\sigma_v}+\mathbf1_{\sigma_{v+1}=\sigma_v})/2\), with cyclic indices. Only simultaneous exchanges of the occupants of two sites are allowed, and an exchange is improving only if **both** agents strictly improve. The count regards colorings as arrangements of type classes, not distinct permutations among individually labeled same-type agents. A run means a maximal nonempty cyclic interval of consecutive sites of one type; \(J\) is the even number of boundaries between runs (or zero for monochromatic colorings). Each monochromatic edge contributes one unit of total welfare, while a bichromatic edge contributes zero, so \(W=n-J\).

## Proof
**1. Exact equilibrium criterion.** For a nonadjacent pair of differently colored sites \(i,j\), let \(s_i,s_j\in\{0,1,2\}\) be their original counts of same-colored neighbors. At the opposite site each agent would have \(2-s_j\) or \(2-s_i\) same-colored neighbors, respectively. Thus the pair strictly benefits **if and only if** \(s_i+s_j<2\). For adjacent sites with opposite colors, the swapped agents each retain their mutual opposite-color adjacency. Both strictly benefit exactly when the two outside neighbors have colors opposite to the original occupant at their respective boundary sites: the four-site pattern around the edge alternates. This is precisely a pair of adjacent singleton runs. The simple triangle case causes no exception: there cannot be four distinct sites, and direct inspection shows every two-run coloring is stable.

If every run has length at least two, each same-neighbor count is at least one, so no nonadjacent improving pair exists, and there is no adjacent pair of singleton runs. If there are precisely two runs, a possible singleton of either color is the only agent with zero same-type neighbors; all nonadjacent opposite-color occupants have two same-type neighbors, and adjacent improvements cannot occur. Monochromatic assignments are plainly stable. Conversely, suppose there are at least four runs and a singleton of, say, type red. Following it clockwise, the immediately following blue run either has length one, in which case the first four positions spanning the previous red singleton and the next red run produce a profitable adjacent swap, or has length at least two, in which case the last blue site of this run is nonadjacent to the red singleton and has at most one same-type neighbor; their swap strictly benefits both. Therefore the stated condition is necessary and sufficient.

**2. Composition count.** A two-run coloring with \(a,b\ge1\) is specified uniquely by the clockwise starting position of the red run and has \(n\) possibilities. Otherwise write the number of red runs and blue runs as \(r\ge2\), with each of their lengths at least two. Choosing an ordered red length composition of \(a\) into \(r\) pieces at least two gives \(\binom{a-r-1}{r-1}\), and likewise the blue lengths give \(\binom{b-r-1}{r-1}\). Choose a labeled starting vertex of a marked red run in \(n\) ways. Each coloring is counted once per its \(r\) red runs, so divide by \(r\), giving the asserted formula. The upper bound on \(r\) comes from the minimum run length.

**3. Exact generating polynomial.** Let the transfer states be consecutive color pairs \(00,01,10,11\). A directed transition from \((x,y)\) to \((y,z)\) is allowed unless \(x=z\ne y\), the forbidden isolated site. Assign weight \(z\) for a color change \(y\ne z\); to avoid reusing the formal variable, denote that weight \(\xi\) while constructing the transfer matrix. In the stated ordered basis, the matrix is
\[
T(\xi)=\begin{pmatrix}1&\xi&0&0\\0&0&0&1\\1&0&0&0\\0&0&\xi&1\end{pmatrix}.
\]
Its trace to power \(n\) counts exactly the cyclic colorings with no singleton runs, with exponent equal to their number of bichromatic edges. The stable two-run colorings excluded by this constraint are those containing a singleton run. For each of the two possible singleton colors, and each of the \(n\) possible singleton sites, one coloring occurs, so the correction is \(2n\xi^2\). This includes the case \(n=3\), where every nonmonochromatic coloring has such a singleton. Thus the generating polynomial formula holds for all \(n\ge3\).

The matrix has characteristic polynomial \((\lambda^2-\lambda-\xi)(\lambda^2-\lambda+\xi)\). At \(\xi=1\), its eigenvalues are \(\phi,1-\phi,e^{i\pi/3},e^{-i\pi/3}\). Taking powers and traces proves the closed counting identity. This also gives the fraction of all binary colorings that are equilibria as asymptotic to \((\phi/2)^n\).

**4. Typical welfare.** In a complex neighborhood of \(\xi=1\), \(T(\xi)\) has a unique simple eigenvalue of maximal modulus, \(\lambda_+(\xi)=(1+\sqrt{1+4\xi})/2\); the other eigenvalues have strictly smaller modulus there. The additive correction \(2n\xi^2\) is exponentially negligible in this neighborhood relative to \(\lambda_+(\xi)^n\). For a uniform random stable coloring, the moment-generating function of \(J\) therefore satisfies
\[
\log\mathbb E[e^{tJ}]=n\bigl[\log\lambda_+(e^t)-\log\phi\bigr]+O(nq^n)
\]
uniformly for complex \(t\) close to zero, for some \(0<q<1\). Direct differentiation gives
\[
\left.\frac{d}{dt}\log\lambda_+(e^t)\right|_{t=0}=\frac{5-\sqrt5}{10},\qquad
\left.\frac{d^2}{dt^2}\log\lambda_+(e^t)\right|_{t=0}=\frac{\sqrt5}{25}.
\]
Expanding the logarithm at \(t=i s/\sqrt n\) and applying the continuity theorem for characteristic functions yields a Gaussian limit for \(J\), centered at \(n(5-\sqrt5)/10\) and scaled by \(\sqrt n\). Since \(W=n-J\), the asserted normal welfare law follows; its law of large numbers also follows from this estimate.

## Verification
The accompanying `cyclic_swap_verifier.py` enumerates every binary coloring of every labeled cycle of sizes \(3\) through \(14\), computes the original and post-swap utilities for every differently colored pair, tests the exact structural characterization, independently totals the fixed-composition equilibrium counts, and compares the resulting welfare polynomial with integer transfer-matrix multiplication. There are \(32{,}760\) directly tested binary colorings. Further integer recurrence comparisons of the generating polynomial, full count, and run-length enumeration cover cycle sizes \(3\) through \(33\). These are checks of the definitions and formulas, not a substitute for the proof for arbitrary \(n\) or the asymptotic limit.

Reproduce with `python3 cyclic_swap_verifier.py` (Python 3 standard library only). Exact arithmetic is used throughout. The matrix eigenvalue calculation and the analytic-limit argument are proved above and are not claimed to follow from finite testing.

## Relationship to prior work
Agarwal, Elkind, Gan and Voudouris introduced and analyzed this all-sites-occupied swap model, studying equilibrium existence and welfare. Bilò, Bilò, Lenzner and Molitor established sharp price-of-anarchy bounds for two-color swap Schelling games on cycles (Theorem 12 of the 2022 journal version, preprint from May 2020), and their proof already establishes that when each color has at least two agents, an equilibrium cannot contain a singleton monochromatic run. That observation, its welfare bounds, and the model itself are **prior work**, not newly claimed here. The full count by both population sizes, the all-compositions welfare generating polynomial, and the limiting typical-equilibrium welfare law are the additions assessed here. Later research on robustness of cycle equilibria addresses swap resilience rather than this distribution over all stable colorings. Classically known Fibonacci/Lucas and binary run-counting identities are used as enumerative tools, not claimed as new identities in isolation.

## Limitations
The result is specific to a fully occupied simple cycle, two identical-type utility classes, degree-normalized monotone homophily, and bilateral strictly profitable swaps. It does not apply to vacant sites, one-sided moves, more types, nonmonotone preferences, or a uniform distribution conditional on a *fixed* color proportion for the Gaussian law (the exact fixed-composition count is provided separately). The asymptotic law samples uniformly among all stable colorings with unrestricted proportions. It does not describe the distribution induced by any strategic improvement process, and uniqueness of the mathematical result in all unindexed or inaccessible literature is not asserted. The evidence is self-review and reproducibility, not an independent external audit.

## References
1. A. Agarwal, E. Elkind, J. Gan, A. A. Voudouris, *Swap Stability in Schelling Games on Graphs*, AAAI 2020. https://arxiv.org/abs/1909.02421 ; https://doi.org/10.1609/AAAI.V34I02.5541.
2. D. Bilò, V. Bilò, P. Lenzner, L. Molitor, *Topological Influence and Locality in Swap Schelling Games*, arXiv:2005.02752v1, first public May 6, 2020; *Autonomous Agents and Multi-Agent Systems* 36, 47 (2022). https://arxiv.org/abs/2005.02752 ; https://doi.org/10.1007/s10458-022-09573-7.
3. Kreisel et al., *Equilibria in Schelling games: computational hardness and robustness*, *Autonomous Agents and Multi-Agent Systems*. https://doi.org/10.1007/s10458-023-09632-7.
