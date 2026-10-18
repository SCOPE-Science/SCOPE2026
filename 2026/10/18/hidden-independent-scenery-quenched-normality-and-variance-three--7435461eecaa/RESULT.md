# Hidden independent scenery: quenched normality and variance-three cross-variation

## Finding

Let \((\xi_j)_{j\geq1}\) be independent fair signs, and independently let \((b_k)_{k\geq0}\) be independent Bernoulli\((1/2)\) coefficients. For \(j\geq0\), put
\[
S_j=\sum_{i=1}^{j}{\mathbf{1}}_{\{\xi_i=-1\}},\qquad
f_s=(-1)^{\sum_{k=0}^{s}\binom{s}{k}b_k}\quad(s\geq0).
\]
Set \(q_0=1\), \(q_j=f_{S_j}\) for \(j\geq1\), and define the bootstrap pair
\[
X_n=\sum_{j=1}^{n}\xi_j,\qquad
Y_n=\sum_{j=1}^{n}q_{j-1}\xi_j.
\]
Then the following results hold.

**Quenched normality.** For almost every fixed coefficient sequence \(b\), conditional on that sequence, the processes
\[
\left(n^{-1/2}X_{\lfloor nt\rfloor},\;n^{-1/2}Y_{\lfloor nt\rfloor}\right)_{t\geq0}
\]
converge in the Skorokhod \(J_1\) topology to two *independent* standard Brownian motions. More precisely, for almost every \(b\),
\[
\frac1n\sum_{j=0}^{n-1}q_j\longrightarrow0
\quad\text{almost surely under the conditional walk law.}
\]

**Annealed fluctuations of the predictive cross-variation.** Write
\[
C_n=\sum_{j=0}^{n-1}f_{S_j},\qquad C_0=0.
\]
For every integer \(n\geq1\), under the joint coefficient-and-walk law,
\[
\mathbb E C_n=0,\qquad
\operatorname{Var}(C_n)=3n-4+2^{2-n}.
\]
Furthermore,
\[
\left(n^{-1/2}X_{\lfloor nt\rfloor},\;n^{-1/2}C_{\lfloor nt\rfloor}\right)_{t\geq0}
\Longrightarrow (B_t,\sqrt3\,\widetilde B_t)_{t\geq0},
\]
where \(B\) and \(\widetilde B\) are independent standard Brownian motions. The actual predictable cross-variation \(Q_n=\sum_{j=0}^{n-1}q_j\) differs from \(C_n\) by at most two, so has the same functional limit. Precisely, \(\mathbb E Q_n=1\) and \(\operatorname{Var}(Q_n)=3n-7+2^{3-n}\) for \(n\geq2\) (and \(Q_1=1\)).

The environmental coefficients are *frozen across all times*: the single \(b_k\) is reused whenever a cardinality \(k\) is encountered. The theorem does not assume independent coefficient resampling at successive times.

## Assumptions and scope

The coefficient law is precisely independent fair Bernoulli, the base increments are independent fair signs, and the two families are independent. The random environment is the complete infinite sequence \(b=(b_k)_{k\geq0}\); "quenched" means its realization is fixed before sampling the walk increments. There is no claim for biased coefficient probabilities, asymmetric base steps, or non-cardinality coefficient arrays. All functional convergence statements are on every bounded time interval, hence in \(D([0,\infty),\mathbb R^2)\).

## Proof

**1. A binary Pascal map is an exact scenery isomorphism.** Set
\[
t_s=\sum_{k=0}^{s}\binom{s}{k}b_k\pmod2.
\]
For every \(m\geq0\), the map sending \((b_0,\ldots,b_m)\) to \((t_0,\ldots,t_m)\) is linear over \(\mathbb F_2\), with a lower-triangular matrix having all diagonal entries equal to one. Hence it is bijective. Since the input is uniform on the binary cube, its image is also uniform. Compatibility as \(m\) grows shows that \((t_s)_{s\geq0}\) is an independent sequence of fair bits. Therefore \((f_s)_{s\geq0}\) is an independent fair-sign scenery, independent of \((\xi_j)\). This independence is an *annealed* fact about the random environment; it does not assert randomness of the scenery after freezing it.

**2. Regenerative decomposition.** Let \(\tau_0=0\) and \(\tau_{s+1}=\inf\{j>\tau_s:S_j=s+1\}\). Then
\[
G_s=\tau_{s+1}-\tau_s
\]
are independent geometric\((1/2)\) random variables on \(\{1,2,\ldots\}\), independent of the scenery. Each visit to level \(s\) contributes \(f_s\) for exactly \(G_s\) successive time indices. Thus for every \(m\geq1\), exactly,
\[
\tau_m=\sum_{s=0}^{m-1}G_s,\quad
C_{\tau_m}=\sum_{s=0}^{m-1}G_sf_s,\quad
X_{\tau_m}=\sum_{s=0}^{m-1}(G_s-2).
\]
Because \(\mathbb EG_s=2\), \(\mathbb E(G_sf_s)=0\), and \(\mathbb E|G_sf_s|<\infty\), the strong law gives
\[
\frac{C_{\tau_m}}{\tau_m}\longrightarrow0
\quad\text{almost surely under the joint law.}
\]
For \(\tau_m\leq n<\tau_{m+1}\), the omitted partial-block contribution to \(C_n\) is bounded by \(G_m\). Geometric tails and Borel--Cantelli give \(G_m/m\to0\) almost surely. Since \(\tau_m/m\to2\), it follows that \(C_n/n\to0\) almost surely along *all* integers. The difference between \(C_n\) and \(\sum_{j=0}^{n-1}q_j\) is \(f_0-1\), of absolute value at most two. Fubini's theorem converts the joint almost-sure limit into the stated conditional almost-sure limit for almost every fixed environment.

**3. Quenched functional limit.** For each fixed environment the two-dimensional process \((X_n,Y_n)\) is a martingale in the base-walk filtration. Its increment at time \(j\) is \((\xi_j,q_{j-1}\xi_j)\), with conditional covariance
\[
\begin{pmatrix}1&q_{j-1}\\q_{j-1}&1\end{pmatrix}.
\]
By Step 2, for almost every environment the off-diagonal predictable bracket is \(o(n)\) almost surely under the conditional walk law. This also holds uniformly over compact rescaled times: if \(A_m/m\to0\), then \(n^{-1}\max_{m\leq nT}|A_m|\to0\) for each fixed \(T\). The diagonal brackets are exactly the step count. The increments have bounded Euclidean norm, so the conditional Lindeberg condition holds. The standard multidimensional martingale functional central limit theorem yields two independent Brownian coordinates.

**4. Exact finite variance.** Independence and centering of the scenery imply, for \(0\leq i<j\),
\[
\mathbb E[f_{S_i}f_{S_j}]
=\mathbb P(S_i=S_j)=2^{-(j-i)}.
\]
Consequently
\[
\operatorname{Var}(C_n)
=n+2\sum_{h=1}^{n-1}(n-h)2^{-h}
=3n-4+2^{2-n},
\]
including \(n=1\). Removing the random first scenery term and replacing it by the deterministic \(q_0=1\) gives \(\operatorname{Var}(Q_n)=3n-7+2^{3-n}\) for \(n\geq2\).

**5. Annealed functional fluctuation limit.** The pairs
\[
\bigl(G_s-2,\,G_sf_s\bigr),\qquad s\geq0,
\]
are independent and identically distributed, centered, with covariance matrix \(\operatorname{diag}(2,6)\). Their renewal clock has mean increment two. The multivariate iid functional central limit theorem, combined with \(\tau_{\lfloor nt\rfloor}/n\to2t\) uniformly on compact intervals and the random-time-change theorem, gives Brownian covariance matrix \(\operatorname{diag}(1,3)\) per unit physical time. To pass from complete blocks to arbitrary times, note that on \([0,nT]\) the leftover fluctuation in either coordinate is at most a constant times \(\max_{s\leq nT+1}G_s\). For every \(\delta>0\),
\[
\mathbb P\!\left(\max_{s\leq nT+1}G_s>\delta\sqrt n\right)
\leq(nT+2)\,2^{-\lfloor\delta\sqrt n\rfloor+1}\longrightarrow0.
\]
Thus the partial blocks vanish on the diffusion scale, proving the claimed functional limit. Since the limiting covariance matrix is diagonal, its Brownian coordinates are independent.

## Verification

The standalone `checker.py` exhaustively checks that the finite binary Pascal map permutes binary cubes through ten coefficients, verifies the exact variance by independent enumeration of coefficient vectors and sign paths through seven steps, and checks conditional invertibility of the bootstrap increment map for all coefficient vectors through seven steps. It uses exact integers and rational numbers, not simulation. The script reports 302 passing assertions. None of these finite checks substitutes for the strong laws, Borel--Cantelli argument, or functional limit theorems used above.

To reproduce, run `python checker.py` with Python 3.11 or later; no external dependencies are required.

## Relationship to prior work

Hamza and Tournier, *Are random random walks normal?* (arXiv:2610.01658, first submitted October 1, 2026), Section 4.3, Proposition 11 and Corollary 12, study the same inclusion-induced model with time-invariant cardinality coefficients \(b_k\). They establish **annealed** two-dimensional Brownian convergence for coefficients bounded away from deterministic values, and explicitly identify the corresponding quenched statement as unresolved. The current theorem proves that quenched statement for the distinguished fair-coefficient case, using a binary Pascal transform to iid scenery, and additionally provides the exact finite cross-variation variance and a variance-three functional fluctuation theorem.

Collevecchio, Hamza, Shi and Williams, *Limit theorems and ergodicity for general bootstrap random walks* (Electronic Journal of Probability 27 (2022), article 92; arXiv:2010.16000), give a general criterion for Brownian limits of deterministic predictable-sign recycles. That criterion is compatible with Step 3 but does not itself establish almost-sure typicality of the particular frozen random environment or the variance-three fluctuation law.

The elementary Pascal bijection, iid regenerative central limit theorem, and martingale functional central limit theorem are standard proof tools and are not claimed as newly discovered general principles. The claim is their exact application to this frozen-cardinality model and its resulting pair of limit laws.

## Limitations

The quenched theorem is proved only for fair coefficients, not the full elliptic parameter range of the motivating paper. The variance-three functional limit is **annealed**, not a quenched central limit theorem for the uncentered cross-variation. The conclusion concerns weak functional convergence, not an almost-sure invariance coupling, a convergence rate, or independence of the finite-time random walks. Independent priority verification against more general bootstrap-walk and random-scenery results remains outstanding.

## References

1. K. Hamza and L. Tournier, *Are random random walks normal?*, arXiv:2610.01658v1 (2026), https://arxiv.org/abs/2610.01658 . Relevant material: Sections 1, 2, and 4.3, especially Proposition 11 and Corollary 12.
2. A. Collevecchio, K. Hamza, M. Shi and R. J. Williams, *Limit theorems and ergodicity for general bootstrap random walks*, Electronic Journal of Probability **27** (2022), article 92, https://doi.org/10.1214/22-EJP818 ; arXiv:2010.16000.
3. Standard results invoked: strong law for iid integrable variables, Borel--Cantelli lemma, iid and martingale functional central limit theorems, and continuity of deterministic-limit random time changes.
