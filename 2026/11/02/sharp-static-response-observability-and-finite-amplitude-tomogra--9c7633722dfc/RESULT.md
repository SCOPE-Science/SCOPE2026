# Sharp static-response observability and finite-amplitude tomography of equiaccessible jump networks

## Finding

For an irreducible finite continuous-time Markov jump process whose embedded transition matrix is **doubly stochastic**, changing one outgoing transition probability at the expense of another moves its stationary jump-visit distribution along a fixed line, at **every admissible finite perturbation strength**. The span of all such experimentally admissible single-row responses has an exact graph-theoretic dimension. Specifically, if the *common-target graph* has \(c\) connected components on \(n\) states, then

\[
\boxed{\dim\operatorname{span}\{u^{(i;j\to k)}_\varepsilon-u_0\}=n-c.}
\]

When the common-target graph is connected, \(n-1\) controlled finite-amplitude experiments, one for each edge of any spanning tree, determine **the entire unknown embedded transition matrix exactly** from stationary occupations alone, provided the escape rates and allowed transition support are known. Connectivity and aperiodicity of the original jump chain alone do not ensure full observability: an explicit irreducible, aperiodic, doubly stochastic six-state example has response rank \(4\), rather than \(5\).

## Assumptions and scope

Fix \(n\ge3\) labeled states, known positive escape rates \(v_i>0\), and a possibly unknown real transition matrix \(P\) satisfying \(P_{ii}=0\), \(P_{ij}\ge0\), \(P\mathbf1=P^{\mathsf T}\mathbf1=\mathbf1\), and irreducibility. Its continuous-time generator is \(Q=V(P-I)\), with \(V=\operatorname{diag}(v_1,\ldots,v_n)\). The stationary time-occupation column vector is \(\pi\), while the stationary jump-visit column vector is \(u\), related by

\[
\pi=\frac{V^{-1}u}{\mathbf1^{\mathsf T}V^{-1}u},\qquad
u=\frac{V\pi}{\mathbf1^{\mathsf T}V\pi}.
\]

Thus at the unperturbed equiaccessible point \(u_0=\mathbf1/n\). A *controlled row-transfer probe* specifies source \(i\) and distinct outgoing destinations \(j,k\) with \(P_{ij},P_{ik}>0\); it replaces \(P\) by \(P_\varepsilon=P+\varepsilon e_i(e_k-e_j)^{\mathsf T}\). Choose nonzero \(\varepsilon\) sufficiently small so that all originally positive entries remain positive. This preserves escape rates, row sums, support, and irreducibility, though the perturbed matrix need not remain doubly stochastic. The measured data are the stationary \(\pi_\varepsilon\) for each chosen probe, along with the known \(v\), \(i,j,k,\varepsilon\). No trajectories, currents, or mean first-passage times are assumed observable.

Define the *common-target graph* \(\Gamma(P)\): vertices are destinations \(1,\ldots,n\), and an undirected edge \(\{j,k\}\) exists when at least one source row has both \(P_{ij}>0\) and \(P_{ik}>0\). Its connected components are \(C_1,\ldots,C_c\). Let \(H=\{z\in\mathbb R^n:\mathbf1^{\mathsf T}z=0\}\) and \(A=(I-P^{\mathsf T})|_H:H\to H\). Irreducibility makes \(A\) invertible even for periodic \(P\).

## Proof

**1. Exact response line.** For any admissible row-transfer, put \(d=e_k-e_j\in H\) and \(w=A^{-1}d\). Stationarity of the perturbed jump chain and of the unperturbed uniform distribution gives

\[
(I-P^{\mathsf T})(u_\varepsilon-u_0)
=\varepsilon d(e_i^{\mathsf T}u_\varepsilon).
\]

Because \(u_\varepsilon-u_0\in H\), inversion on \(H\) yields \(u_\varepsilon-u_0=\varepsilon (u_\varepsilon)_i w\). Looking at its \(i\)-th coordinate gives

\[
(u_\varepsilon)_i=\frac{1}{n(1-\varepsilon w_i)},\qquad
\boxed{u_\varepsilon=\frac{\mathbf1}{n}+\frac{\varepsilon}{n(1-\varepsilon w_i)}w.}
\]

The denominator is positive because \(u_\varepsilon\) is positive. In particular, the **exact** response direction depends only on the destination pair \(\{j,k\}\), not which row supplied that pair. Its scale can depend on the row and perturbation size. From one nonzero finite-strength stationary measurement, \(w\) is recovered without estimating a derivative:

\[
\boxed{w=\frac{u_\varepsilon-u_0}{\varepsilon (u_\varepsilon)_i}}.
\]

The small-perturbation derivative \(u'_0=w/n\) follows as a corollary, not as an assumption. All formulas are exact for every \(\varepsilon\) retaining irreducibility and nonnegative probabilities, with the stated support-preserving range ensuring this.

**2. Complete rank criterion.** Let \(D\subset H\) be the span of all admissible differences \(e_k-e_j\). These differences are exactly the oriented incidence columns of \(\Gamma(P)\); standard elementary path telescoping on each component shows

\[
D=\{z\in\mathbb R^n:\sum_{i\in C_a}z_i=0\text{ for }a=1,\ldots,c\},
\quad\dim D=n-c.
\]

Every nonzero finite response is a nonzero scalar multiple of \(A^{-1}d\), and each graph edge admits an interior nonzero perturbation. Hence the span of **all** such finite responses is \(A^{-1}D\), with dimension exactly \(n-c\). The same equality holds for first derivatives. If \(c>1\), these single-row perturbations cannot span all \(n-1\) zero-sum stationary response directions; this statement does **not** exclude additional inference using structural prior knowledge, simultaneous multirow perturbations, or time-series data.

**3. Finite-observation reconstruction.** Suppose \(\Gamma(P)\) is connected. Choose a spanning tree with \(n-1\) edges, and for each edge select any supporting row and a nonzero, support-preserving perturbation. Convert its measured \(\pi_\varepsilon\) into \(u_\varepsilon=V\pi_\varepsilon/(\mathbf1^{\mathsf T}V\pi_\varepsilon)\), and recover \(w=A^{-1}d\) via the boxed finite-response formula. The corresponding \(n-1\) incidence vectors \(d\) form a basis of \(H\), so these observations uniquely determine \(A^{-1}:H\to H\), and hence \(A\) and the restriction of \(P^{\mathsf T}=I-A\) to \(H\). The complementary one-dimensional action is known, \(P^{\mathsf T}\mathbf1=\mathbf1\), because the unknown baseline matrix is doubly stochastic. Therefore \(P^{\mathsf T}\), and thus \(P\), are uniquely reconstructed. Precisely \(n-1\) independent probes are needed to determine the *full linear response operator* by this basis method; no lower bound is claimed for the number required to identify \(P\) when additional structural constraints are available.

**4. Mixing does not force observability.** The following explicit matrix has six states (indices \(1,\ldots,6\)):

\[
P_* = \begin{pmatrix}
0&1/2&1/2&0&0&0\\
1/2&0&1/2&0&0&0\\
0&0&0&1/2&1/4&1/4\\
1/2&1/2&0&0&0&0\\
0&0&0&1/4&0&3/4\\
0&0&0&1/4&3/4&0
\end{pmatrix}.
\]

Every row and column sums to \(1\). The directed transition graph is strongly connected (indeed \((I+P_*)^5\) has strictly positive entries), and its cycles \(1\to2\to1\) and \(1\to3\to4\to1\) have coprime lengths \(2\) and \(3\), proving aperiodicity. Yet each row has all its positive destinations inside either \(\{1,2,3\}\) or \(\{4,5,6\}\), and positive pairs link all vertices within each triple. Thus \(\Gamma(P_*)\) has exactly two components and response rank \(6-2=4\).

## Verification

The standalone `verify.py` uses exact rational arithmetic with SymPy and is run using `python verify.py`. It independently checks the six-state matrix's double stochasticity, accessibility, period witnesses, common-target components, rank and all permissible row-transfer first-order equations. It also reconstructs a nonreversible four-state doubly stochastic matrix from three **finite-amplitude**, rational-valued occupation-response measurements, checks the exact fractional-linear response formula for every admissible probe in three-, four-, and six-state examples, and verifies conversion between jump-visit and time-occupation sensitivities for heterogeneous escape rates. These finite tests complement, and do not replace, the arbitrary-size algebraic proof above.

## Relationship to prior work

Calvert's equiaccessible McLennan formula (2026) establishes \(\pi_i\propto v_i^{-1}\) and general perturbative corrections for traffic imbalance, motivating the question of detecting otherwise hidden nonequilibrium structure. Hunter (2002, Theorem 6.3) already gives the underlying exact finite single-row stationary perturbation identity in terms of generalized inverses: the exact line-law here is an interpretation of established finite-state perturbation theory, **not** claimed as a new perturbation identity. Berkhout, Heidergott and Van Dooren (2024) study rank-one stochastic perturbations and one-row control, but their inverse problem takes the original transition matrix as known and seeks a perturbation producing a *target* stationary distribution. The present claim instead classifies the rank of all support-preserving observation responses by a common-target graph, reconstructs an **unknown** equiaccessible transition matrix from finite static experiments when the graph is connected, and supplies an aperiodic rank-deficient counterexample.

## Limitations

The unknown baseline must be irreducible and doubly stochastic with no self transitions; positive escape rates, all occupation coordinates, probe settings and the baseline support must be known. Reconstruction is exact and assumes ideal noiseless stationary measurements, not bounded statistical sample complexity or numerical conditioning. The rank-deficiency result concerns **the span of individual support-preserving single-row responses**; it neither proves nonidentifiability of all parameters under additional constraints nor rules out multirow, transient or higher-order intervention schemes. The finite-amplitude line law itself follows from known row-perturbation identities; novelty is assigned only to the particular complete response-rank classification, static tomography protocol and mixing counterexample. A potentially stronger general control/identifiability theorem could subsume these results and remains a publication-priority risk.

## References

1. J. Calvert, *A McLennan formula for equiaccessible steady states*, arXiv:2610.26755 (first posted 19 October 2026), https://arxiv.org/abs/2610.26755.
2. J. J. Hunter, *Generalized inverses, stationary distributions and mean first passage times with applications to perturbed Markov chains*, Research Letters in the Information and Mathematical Sciences **3** (2002), 99–116, https://mro.massey.ac.nz/items/84ef5574-9a1e-4311-bf55-681f86f306d9.
3. J. Berkhout, B. Heidergott, and P. Van Dooren, *Perturbation and inverse problems of stochastic matrices*, SIAM Journal on Matrix Analysis and Applications **45** (2024), 553–584, https://doi.org/10.1137/22M1489162.
4. E. Thiede, B. Van Koten, and J. Weare, *Sharp entrywise perturbation bounds for Markov chains*, SIAM Journal on Matrix Analysis and Applications **36** (2015), 917–941, https://pmc.ncbi.nlm.nih.gov/articles/PMC4610747/.
