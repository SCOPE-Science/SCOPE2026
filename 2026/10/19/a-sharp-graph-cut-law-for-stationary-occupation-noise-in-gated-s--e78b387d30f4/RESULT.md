# A sharp graph-cut law for stationary occupation noise in gated symmetric exclusion

## Finding

Consider the canonical symmetric simple exclusion process on a finite weighted graph, with an autonomous two-state gate simultaneously disabling a set of edges. Although the invariant distribution of particles does not depend on the gate's switching speed, the long-time variance of an integrated linear occupation observable has a precisely characterized slow-switching singularity.

Let the ON graph be connected with vertex set \(V\) of cardinality \(n\ge2\); the OFF graph retains a subset of its undirected edges, with unchanged positive symmetric rates, and has connected components \(C_1,\ldots,C_q\). There are \(1\le k<n\) indistinguishable particles. The independent gate changes ON to OFF at rate \((1-p)\kappa\) and OFF to ON at rate \(p\kappa\), for \(0<p<1\) and \(\kappa>0\).

For a real, vertex-centered field \(h\), with \(\sum_{x\in V}h_x=0\), define
\[
A_T(h)=\int_0^T\sum_{x\in V}h_x\bigl(\eta_t(x)-k/n\bigr)\,dt,
\qquad
\mathcal V_\kappa(h)=\lim_{T\to\infty}\frac{\operatorname{Var}(A_T(h))}{T}.
\]
Let \(P_0h\) replace the entries of \(h\) on each \(C_i\) by their arithmetic mean, and put
\[
\chi_{n,k}=\frac{k(n-k)}{n(n-1)}.
\]
The limit exists, and for every \(\kappa>0\) it obeys the **all-rate bound with an optimal leading coefficient**
\[
\boxed{\mathcal V_\kappa(h)\ge
\frac{2(1-p)}{p\kappa}\,\chi_{n,k}\,\|P_0h\|_2^2.}
\]
Its leading slow-switching coefficient is exactly the same:
\[
\boxed{\lim_{\kappa\downarrow0}\kappa\mathcal V_\kappa(h)
=\frac{2(1-p)}{p}\,\chi_{n,k}\,\|P_0h\|_2^2.}
\]
More sharply, \(\mathcal V_\kappa(h)\) stays bounded as \(\kappa\downarrow0\) **if and only if** the mean of \(h\) on *each* OFF component is zero. This includes all fields when the OFF graph remains connected. If \(h\) detects an OFF-component particle-number imbalance, the integrated noise diverges as \(1/\kappa\), even though the stationary equal-time law is unchanged.

For an OFF component \(A\) of size \(a\), choose \(h=\mathbf1_A-a/n\). Then
\[
\lim_{\kappa\downarrow0}\kappa\mathcal V_\kappa(h)
=\frac{2(1-p)k(n-k)a(n-a)}{p\,n^2(n-1)}.
\]
In fact, canonical sampling gives \(\operatorname{Var}_{\pi}(N_A)=k(n-k)a(n-a)/[n^2(n-1)]\), and therefore the *universal amplification ratio*
\[
\boxed{\lim_{\kappa\downarrow0}
\frac{\kappa\mathcal V_\kappa(\mathbf1_A-a/n)}
{\operatorname{Var}_{\pi}(N_A)}=\frac{2(1-p)}p.}
\]
This gives a finite-graph structural test: the leading divergence is present precisely for observations with a nonzero projection onto OFF-component contrasts, and its coefficient is measurable from static equilibrium data alone.

**An exact all-speed instance.** Let the ON graph be the complete graph on \(n\) vertices, with each edge exchanging particles at rate \(r>0\). Partition the vertices as \(A\sqcup B\), with \(|A|=a\ge1\) and \(|B|=b=n-a\ge1\); in OFF retain only edges internal to the two parts. For the integrated particle count in \(A\),
\[
\boxed{\mathcal V_\kappa(\mathbf1_A-a/n)
=\frac{2k(n-k)ab}{n^2(n-1)}
\left(\frac{1}{pn r}+\frac{1-p}{p\kappa}\right).}
\]
The stationary variance of the *instantaneous* count, by contrast, is the \(\kappa\)-independent quantity
\[
\operatorname{Var}\bigl(\sum_{x\in A}\eta(x)\bigr)
=\frac{k(n-k)ab}{n^2(n-1)}.
\]

## Assumptions and scope

Let \(E_\mathrm{on}\) be a connected simple undirected graph on \(V\), and let \(E_\mathrm{off}\subseteq E_\mathrm{on}\). Each edge \(\{x,y\}\in E_\mathrm{on}\) has a fixed, symmetric positive rate \(c_{xy}\). The particle space comprises all \(k\)-element subsets of \(V\), equivalently occupation vectors \(\eta\in\{0,1\}^{V}\) with \(\sum_x\eta_x=k\). When the gate is in state \(e\in\{\mathrm{on},\mathrm{off}\}\), a particle exchanges occupancy with a vacant neighbor across each active edge \(\{x,y\}\in E_e\) at rate \(c_{xy}\); attempts across occupied–occupied or vacant–vacant pairs do nothing. Gate switching is autonomous and independent of particles.

The particle process and the gate are initially sampled from their unique joint stationary law. The limit \(T\to\infty\) defining \(\mathcal V_\kappa\) precedes the limit \(\kappa\downarrow0\). No thermodynamic-limit assertion is made. In the complete-graph example, a singleton part is permitted, because its OFF state simply has no internal edges.

## Proof

**Stationarity and covariance.** For either fixed gate state, every legal occupancy exchange has the same reverse rate. Therefore the uniform canonical law \(U_{n,k}\) on the \(\binom nk\) configurations is reversible separately for both particle generators. The two-state gate has invariant probabilities \(p\) (ON) and \(1-p\) (OFF), and satisfies detailed balance. Their product \(\pi=U_{n,k}\otimes(p,1-p)\) is therefore reversible for the joint chain. Connectivity of the ON graph, together with both positive gate-switching rates, makes the joint chain irreducible and establishes uniqueness.

Define \(f_h(\eta)=\sum_x h_x(\eta_x-k/n)\) for any centered vector \(h\). Canonical sampling without replacement gives the exact covariance identity
\[
\mathbb E_{U_{n,k}}[f_hf_g]=\chi_{n,k}\langle h,g\rangle_{\mathbb R^V}
\quad\text{for all centered }h,g.
\]
In particular, the dependence on particle number enters the linear sector only through \(\chi_{n,k}\).

**Exact linear-sector reduction.** Write \(Q_e\) for the continuous-time one-particle generator on the weighted active graph, so
\[
(Q_eh)_x=\sum_{y:\{x,y\}\in E_e}c_{xy}(h_y-h_x).
\]
For the exclusion generator \(L_e\), a direct occupation-exchange calculation gives
\[
L_ef_h=f_{Q_eh}
\]
for every \(h\), without a low-density or mean-field approximation. The gate preserves this linear function subspace. On the Hilbert space \(\mathcal H\oplus\mathcal H\), with \(\mathcal H=\{h:\sum_xh_x=0\}\) and gate-weighted inner product
\[
\langle(u_1,u_0),(v_1,v_0)\rangle_\pi
=p\langle u_1,v_1\rangle+(1-p)\langle u_0,v_0\rangle,
\]
the positive joint generator is represented by
\[
\mathsf A_\kappa=\begin{pmatrix}
 -Q_{\mathrm{on}}+(1-p)\kappa I&-(1-p)\kappa I\\
 -p\kappa I&-Q_{\mathrm{off}}+p\kappa I
\end{pmatrix}.
\]
The irreducible finite reversible chain admits the Green–Kubo/Poisson formula, so for \(x_h=(h,h)\)
\[
\mathcal V_\kappa(h)=2\chi_{n,k}
\langle x_h,\mathsf A_\kappa^{-1}x_h\rangle_\pi.
\tag{1}
\]
Here the inverse is taken on the centered subspace; the global constant mode is not present.

**Finite-rate inequality.** Set \(h_0=P_0h\). Each OFF-component mean is preserved by \(Q_{\mathrm{off}}\), so \(Q_{\mathrm{off}}h_0=0\). Because \(h\) is globally centered, so is \(h_0\). Take the test vector \(w=(0,h_0)\). Direct evaluation yields
\[
\langle x_h,w\rangle_\pi=(1-p)\|h_0\|_2^2,
\qquad
\langle w,\mathsf A_\kappa w\rangle_\pi
=p(1-p)\kappa\|h_0\|_2^2.
\]
For positive self-adjoint \(\mathsf A_\kappa\), the variational identity
\[
\langle x,\mathsf A_\kappa^{-1}x\rangle
=\sup_w\bigl(2\langle x,w\rangle-\langle w,\mathsf A_\kappa w\rangle\bigr)
\]
and optimization over scalar multiples of this \(w\) prove the bound. The case \(h_0=0\) has the trivial nonnegative lower bound.

**Sharp asymptotic and exact boundary.** At zero switching, \(\mathsf A_0\) has on \(\mathcal H\oplus\mathcal H\) exactly the nullspace
\[
\mathcal D=\{(0,g):g\in\mathcal H,\ Q_{\mathrm{off}}g=0\}.
\]
This follows because the ON graph is connected, while the OFF kernel consists of vectors constant on each OFF component. The orthogonal complement of \(\mathcal D\) has a strictly positive \(\mathsf A_0\)-spectral gap, since the space is finite dimensional. Writing \(\mathsf A_\kappa=\mathsf A_0+\kappa\mathsf B\), its compression to \(\mathcal D\) is
\[
\left.\mathsf P_{\mathcal D}\mathsf B\mathsf P_{\mathcal D}\right|_{\mathcal D}=pI_\mathcal D.
\]
The finite-dimensional Schur complement therefore gives the norm limit
\[
\kappa\mathsf A_\kappa^{-1}\longrightarrow
p^{-1}\mathsf P_{\mathcal D}
\quad(\kappa\downarrow0).
\]
Moreover, after subtracting its \(\kappa^{-1}\) term, the inverse is uniformly bounded in norm. Since \(\mathsf P_{\mathcal D}x_h=(0,P_0h)\), formula (1) gives the stated limit and proves that \(\mathcal V_\kappa\) stays bounded if and only if \(P_0h=0\). If the projection is nonzero, the positive leading coefficient gives divergence.

**Complete-graph evaluation.** For \(h=\mathbf1_A-a/n\), the ON generator satisfies \(Q_{\mathrm{on}}h=-rn h\), while \(Q_{\mathrm{off}}h=0\). The two-component Poisson equation \(\mathsf A_\kappa(u_{\mathrm{on}},u_{\mathrm{off}})=(h,h)\) has the exact solution
\[
u_{\mathrm{on}}=\frac{h}{pn r},
\qquad
u_{\mathrm{off}}=\frac{h}{pn r}+\frac{h}{p\kappa}.
\]
Also \(\|h\|_2^2=ab/n\). Substitution in (1) gives the all-speed formula. The instantaneous count variance follows immediately from canonical sampling.

## Verification

The accompanying standalone program `verify.py`, using only SymPy, independently builds the entire \(2\binom nk\)-state exclusion/gate generator and the reduced \(2n\)-state vertex/gate generator. It solves the centered Poisson equations over exact rationals, checks their equal variance values, checks the complete-graph formula for several particle counts and switching rates, and tests both disconnected OFF graphs (including a field orthogonal to their component constants) and connected OFF graphs. Run with `python verify.py` after installing `requirements.txt`.

For an exactly checkable benchmark, take a four-vertex complete ON graph, two OFF components of size two, \(k=2\), \(p=2/5\), and \(r=3/2\). The formula is
\[
\mathcal V_\kappa=\frac1\kappa+\frac5{18}.
\]
For a five-cycle ON graph and OFF components \(\{0,1\}\) and \(\{2,3,4\}\), with \(k=2\), \(p=1/3\), and \(h=(3,3,-2,-2,-2)/5\), direct rational solution produces
\[
\mathcal V_\kappa=\frac{12(14\kappa^2+60\kappa+45)}{125\kappa(\kappa+3)},
\qquad \lim_{\kappa\downarrow0}\kappa\mathcal V_\kappa=\frac{36}{25}.
\]
These are independent finite-instance checks, not a replacement for the all-graph proof.

## Relationship to prior work

Symmetric exclusion on finite weighted graphs and its exact linear occupation-generator structure are classical. Mendonça analyzes finite complete and complete-bipartite exclusion eigenspectra [1]; no new spectral theorem for those static graphs is asserted here. Peres, Stauffer, and Steif study a *single* walk under independently evolving dynamical percolation edges, including slowing of mixing and hitting [2]. Franco, Gonçalves, and Neumann study occupation-time fluctuations of one-dimensional exclusion with **static** spatial conductances under large-system scaling [3]. Redig, Saada, and Sau establish dynamic-environment exclusion duality and hydrodynamic limits on an infinite lattice [4]; that duality, and not the duality step alone, is prior work.

The distinct finite-graph statement proved here is a **stationary canonical, all-particle-number, gated-cut integrated-noise classification**: an explicit, nonasymptotically valid sharp \(1/\kappa\) lower bound, its exact graph-component projection coefficient, the bounded-versus-divergent if-and-only-if criterion, and an all-rate complete-graph realization. These results are not contained as stated in the inspected portions and theorem formulations of [1]–[4]. General finite Markov-chain resolvent and slow-fast perturbation theory underlies the proof, so hidden equivalent formulations or broader existing results remain a material originality risk.

## Limitations

This theorem is finite-dimensional, stationary, reversible, and restricted to exchange-symmetric edge rates, an autonomous common gate with exponential on/off times, and linear integrated occupation observables. It does not describe driven asymmetric exclusion, state-dependent gates, arbitrary dynamic percolation processes, nonstationary initialization, higher occupation cumulants, or a thermodynamic limit. The divergence concerns the long-time variance **per unit time after stationarity**; the limit order matters. The novelty comparison is limited to materially inspected sources and searched records; it is not an exhaustive mathematical-literature uniqueness certificate. No independent external validation has been performed.

## References

[1] J. R. G. Mendonça, *Exact eigenspectrum of the symmetric simple exclusion process on the complete, complete bipartite, and related graphs*, arXiv:1207.4106 (first publicly posted 2012-07-17), https://arxiv.org/pdf/1207.4106.

[2] Y. Peres, A. Stauffer and J. E. Steif, *Random walks on dynamical percolation: mixing times, mean squared displacement and hitting times*, arXiv:1308.6193 (2013), https://arxiv.org/pdf/1308.6193.

[3] T. Franco, P. Gonçalves and A. Neumann, *Occupation times of exclusion processes with conductances*, arXiv:1311.5383 (2013), https://arxiv.org/pdf/1311.5383.

[4] F. Redig, E. Saada and F. Sau, *Symmetric simple exclusion process in dynamic environment: hydrodynamics*, arXiv:1811.01366 (2018), https://arxiv.org/pdf/1811.01366.
