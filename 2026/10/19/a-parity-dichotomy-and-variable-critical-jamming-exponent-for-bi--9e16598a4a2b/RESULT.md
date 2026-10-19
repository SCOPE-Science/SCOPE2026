# A parity dichotomy and variable critical jamming exponent for bipartite path adsorption

## Finding
Consider the complete bipartite graph \(K_{a_N,b_N}\), with \(a_N+b_N=N\). An object is an undirected embedded copy of the path \(P_\ell\) on \(\ell\) distinct vertices, with copies identified under reversal but not required to be induced subgraphs. Assign every object an independent continuously distributed priority and accept it in increasing order exactly when none of its vertices was previously occupied. Let \(U_N^{(\ell)}\) be the number of vertices remaining vacant when no further object can be accepted.

**Even paths.** For every integer \(r\ge2\) and every \(a_N,b_N\ge0\), the terminal vacancy count for \(\ell=2r\) is nonrandom:
\[
U_N^{(2r)}=|a_N-b_N|+2\bigl(\min\{a_N,b_N\}\bmod r\bigr).
\]
In particular, balanced substrates have at most \(2r-2\) vacancies, regardless of their order of deposition.

**Odd paths.** Fix an integer \(r\ge2\) and put \(k=2r+1\). If \((a_N-b_N)/N\to\delta\in(-1,1)\setminus\{0\}\), then
\[
\frac{U_N^{(k)}}{N}\xrightarrow{\mathbb P}|\delta|^{k/(k-1)},
\qquad
\frac{\mathbb E U_N^{(k)}}N\longrightarrow |\delta|^{k/(k-1)}.
\]
In the critical imbalance window \((a_N-b_N)/\sqrt N\to u\in\mathbb R\), define
\[\theta_k=\frac{k-2}{2(k-1)}.\]
Then
\[
\boxed{\frac{U_N^{(k)}}{N^{\theta_k}}\ \Longrightarrow\ 
\left|u+\frac{G}{\sqrt{k-2}}\right|^{k/(k-1)},\qquad G\sim N(0,1).}
\]
In particular, adsorption of five-vertex paths has critical vacancy scale \(N^{3/8}\), while six-vertex paths on a balanced substrate leave only a bounded number of vacant vertices. The exponent increases with odd path length and tends to \(1/2\), whereas every fixed even path length gives a deterministic bounded balanced remainder.

The full odd-path result is not merely a law for a specially chosen initial imbalance: it identifies the noncentral-Gaussian crossover at order \(\sqrt N\) for every fixed length \(k\ge5\).

## Assumptions and scope
The number of path vertices \(\ell\) is fixed as \(N\to\infty\). The substrate is the *complete* bipartite graph with vertices distinguishable by labels. A path copy means an embedded edge set and its vertex set; paths with distinct orderings are distinct eligible objects even when their vertex sets coincide. The arrival order is a uniform random permutation of all such objects, equivalent to independent identical continuous clocks. Every accepted object occupies all of its vertices permanently. No edge is deleted except by occupation of its endpoints. The limiting statements concern the number of unoccupied vertices, not the distribution of deposition times. All limits are along sequences of integer class sizes satisfying the stated assumptions.

## Proof
**1. Even-length stoichiometry.** An alternating path of \(2r\) vertices uses exactly \(r\) vertices of each class. Whenever both classes have at least \(r\) vacant vertices, at least one eligible path exists. Every accepted path removes \(r\) vertices from each class. The number accepted is therefore exactly \(\lfloor\min(a_N,b_N)/r\rfloor\), independently of priorities. Subtracting twice the occupied count proves the even-path formula.

**2. Exact odd-path reduction.** For an odd path with \(k=2r+1\) vertices, an eligible object uses either \((r+1,r)\) or \((r,r+1)\) vertices of the two classes. For every fixed admissible vertex set of either type, the number of undirected alternating path orderings is the same, namely \((r+1)!r!/2\). Thus at any state with \(a\ge r\), \(b\ge r\), \(a+b>2r\), the probability that the next accepted path uses \(r+1\) vertices in the first class is exactly
\[
\frac{\binom a{r+1}\binom b r}{\binom a{r+1}\binom b r+\binom a r\binom b{r+1}}
=\frac{a-r}{a+b-2r}.
\]
Put \(S=a+b\), \(D=a-b\). At each successful deposition, \(S\) decreases deterministically by \(k\), while \(D\) decreases by one with probability \((S-k+1+D)/(2(S-k+1))\), and increases by one otherwise. Therefore
\[
\mathbb E[D_{j+1}\mid\mathcal F_j]
=\frac{S_j-k}{S_j-k+1}D_j,
\qquad S_j=N-kj.
\]
The process stops if either class contains fewer than \(r\) vacant vertices, or both contain exactly \(r\). Its terminal state satisfies the uniform boundary estimate
\[
0\le S_\tau-|D_\tau|\le2r.
\]

**3. An exact multiplicative martingale.** For \(S_j>0\) define
\[
h_j=\prod_{i=1}^j\frac{N-ki}{N-ki+1}
=\frac{\Gamma(N/k)\Gamma((S_j+1)/k)}
{\Gamma((N+1)/k)\Gamma(S_j/k)},\qquad h_0=1.
\]
Then \(M_j=D_j/h_j\), stopped at the terminal deposition, is a martingale. If the last deposition takes \(S=k\) to \(S=0\), the final move is deterministic and \(M\) is defined by continuity to equal its value immediately before that move. For every nondegenerate step,
\[
\mathbb E[(M_{j+1}-M_j)^2\mid\mathcal F_j]
=\frac{1-(D_j/(S_j-k+1))^2}{h_{j+1}^2}.
\]
The gamma-ratio estimate gives
\[
h_j=(S_j/N)^{1/k}\bigl(1+O_k(S_j^{-1}+N^{-1})\bigr)
\]
whenever \(S_j\to\infty\), and fixed positive constants bound \(h_j/(S_j/N)^{1/k}\) above and below for all \(S_j\ge1\).

**4. Macroscopic imbalance.** As long as \(S_j\ge\varepsilon N\), the stopped martingale has variance at most \(C_{k,\varepsilon}N\). Doob's inequality consequently gives \(\sup_{S_j\ge\varepsilon N}|M_j-D_0|/N\to0\) in probability. If \(D_0/N\to\delta\ne0\), it follows uniformly on that range that
\[
D_j/N=\bigl(\delta+o_{\mathbb P}(1)\bigr)(S_j/N)^{1/k}.
\]
Together with \(|D_j|\le S_j\) and the terminal estimate of step 2, this traps the terminal fraction between arbitrarily close bounds around the unique positive solution \(s=|\delta|s^{1/k}\), namely \(s=|\delta|^{k/(k-1)}\). The claimed convergence in probability follows. Boundedness of \(U_N/N\) implies convergence in expectation.

**5. Critical martingale central limit theorem.** Assume \(D_0/\sqrt N\to u\). Up to the terminal move, the normalized predictable quadratic variation is
\[
\frac1N\sum_{j<\tau,\,S_{j+1}>0}
\frac{1-(D_j/(S_j-k+1))^2}{h_{j+1}^2}.
\]
For fixed \(\varepsilon>0\), Doob's inequality yields \(\sup_{S_j\ge\varepsilon N}|D_j|/N\to0\) in probability, so the contribution from \(S_j\ge\varepsilon N\) converges to
\[
\frac1k\int_\varepsilon^1 t^{-2/k}\,dt
=\frac{1-\varepsilon^{1-2/k}}{k-2}.
\]
The remaining contribution is bounded, uniformly in the realized process, by \(C_k\varepsilon^{1-2/k}+o(1)\) after division by \(N\): this follows by summing \(h_j^{-2}\le C_k(N/S_j)^{2/k}\) over the arithmetic progression of positive remaining sizes. Because \(k>2\), the late contribution vanishes as \(\varepsilon\downarrow0\). The chance of terminating while \(S_j\ge\varepsilon N\) is itself \(o(1)\), since termination requires \(|D_j|\ge S_j-2r\).

Moreover every normalized martingale increment is bounded by \(C_k N^{1/k-1/2}\to0\), including the deterministic-last-move convention. The conditional-variance limit and this infinitesimal-increment bound give the martingale central limit theorem (equivalently by conditional characteristic-function expansion):
\[
M_\tau/\sqrt N\ \Longrightarrow\ u+G/\sqrt{k-2}.
\]
A normal law has no atom at zero. For any fixed \(L\), the event \(S_\tau\le L\) forces \(|M_\tau|/\sqrt N\le C_{k,L}N^{1/k-1/2}\); hence \(S_\tau\to\infty\) in probability. The macroscopic bound above also implies \(S_\tau/N\to0\). Thus the gamma-ratio estimate and the terminal boundary estimate apply at the random stopping size:
\[
\frac{|M_\tau|}{\sqrt N}
=\left(\frac{S_\tau}{N^{(k-2)/(2(k-1))}}\right)^{(k-1)/k}(1+o_{\mathbb P}(1)).
\]
The continuous-mapping theorem proves the asserted powered noncentral-Gaussian limit. The case of a zero-remaining-vertex final move is already negligible by the preceding no-atom argument.

**6. A perfect-packing substrate with positive stochastic waste.** For \(r=2\), the substrate \(K_{11m,9m}\) has a full covering by \(3m\) paths using three vertices in the first class and two in the second, and \(m\) paths of the reverse type. Nevertheless the random greedy process leaves a limiting vacant fraction \(10^{-5/4}=0.0562341325\ldots\), by the macroscopic odd-path formula. Thus the jamming is kinetic rather than a deterministic packing obstruction.

## Verification
The included standard-library program `verify.py` constructs labelled alternating path embeddings independently of the reduced transition formula and compares the exact distributions of terminal vacancies from exhaustive labelled-state recursion with those from the two-count Markov chain. It checks eleven small bipartite substrates at path lengths five and seven, 564 further rational drift identities, 6,300 even-path stoichiometric identities, and the exponent normalization for six odd lengths. All stated finite checks pass. These finite checks do not constitute proofs of the infinite-size limit; that limit is established by the martingale arguments above.

Separate Monte Carlo sampling of the reduced five-vertex-path chain at \(N=12000\) gave empirical vacancy fractions \(0.05624\), \(0.13377\), and \(0.42065\) for imbalances \(0.1\), \(0.2\), and \(0.5\), versus predictions \(0.056234\), \(0.133748\), and \(0.420448\). Simulations serve only as sanity checks.

## Relationship to prior work
Classical random sequential adsorption and its reaction-kinetic motivation are reviewed by Evans (1993). General random greedy hypergraph packing theorems of Spencer (1995) and Rödl–Thoma (1996) address asymptotically almost-perfect packing under regularity and small-codegree conditions; these do not furnish the terminal power-law fluctuation distribution for the present bipartite odd-path family. Flajolet–Dumas–Puyhaubert (2006) provide a general urn-theory framework, but the fully sacrificial family discussed in their Section 6 has *positive* total urn balance; the present decreasing two-color process has balance \(-k\) and terminates at an absorbing boundary. An earlier result for three-vertex-path adsorption is not claimed anew: the new odd-path theorem begins with five vertices, and the simultaneous all-length parity comparison isolates a different structural question.

## Limitations
All theorems require complete bipartite substrates, uniform priorities over *embedded* path copies, and a fixed path length. No quantitative rate of weak convergence or uniformity in growing path length is asserted. The critical limit is weak convergence, not a claim of convergence of every unbounded moment. The martingale proof does not determine the limiting distribution of deposition times or the microscopic spatial correlations of accepted paths. Literature not available in full may contain related decreasing-urn stopping laws, so independent bibliographic verification remains desirable.

## References
1. J. W. Evans, “Random and cooperative sequential adsorption,” *Reviews of Modern Physics* **65** (1993), 1281–1329, DOI: 10.1103/RevModPhys.65.1281. Published 1993-10-01.
2. J. Spencer, “Asymptotic packing via a branching process,” *Random Structures & Algorithms* **7** (1995), 167–172, DOI: 10.1002/rsa.3240070206.
3. V. Rödl and L. Thoma, “Asymptotic packing and the random greedy algorithm,” *Random Structures & Algorithms* **8** (1996), 161–177, DOI: 10.1002/(SICI)1098-2418(199605)8:3<161::AID-RSA1>3.0.CO;2-W.
4. P. Flajolet, P. Dumas, and V. Puyhaubert, “Some exactly solvable models of urn process theory,” *DMTCS Proceedings* AG (2006), 59–118, https://algo.inria.fr/flajolet/Publications/FlDuPu06.pdf.
