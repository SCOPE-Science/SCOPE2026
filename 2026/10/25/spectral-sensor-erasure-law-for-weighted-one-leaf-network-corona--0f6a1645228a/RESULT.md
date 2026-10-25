# Spectral sensor-erasure law for weighted one-leaf network coronas

## Finding
Let a connected undirected weighted graph have Laplacian \(L\) on \(n\ge2\) vertices. Attach to each vertex a private leaf through a conductance \(s>0\). For any nonempty set \(S\) of measured modules, observe a **local aggregate** of its core and leaf states, \(y_i(t)=u_i(t)+\beta_i v_i(t)\), where \(\beta_i\ge0\) may depend on \(i\).

For every eigenvalue \(\alpha\in\sigma(L)\), write \(E_\alpha=\ker(L-\alpha I)\), \(m_\alpha=\dim E_\alpha\), and define the resonant sensor gain
\[
 b_s(\alpha)=\frac{\alpha+\sqrt{\alpha^2+4s^2}}{2s}.
\]
Define \(S_\alpha=\{i\in S:\beta_i\ne b_s(\alpha)\}\), and let \(r_\alpha(T)\) be the rank of restriction \(E_\alpha\to\mathbb R^T\), \(w\mapsto(w_i)_{i\in T}\), with \(r_\alpha(\varnothing)=0\). Then the **exact unobservable dimension** of the \(2n\)-dimensional continuous-time diffusion system is
\[
\boxed{\dim\mathcal U=\sum_{\alpha\in\sigma(L)}\bigl(2m_\alpha-r_\alpha(S)-r_\alpha(S_\alpha)\bigr).}
\]
In particular, full-state observability is equivalent to
\[
\boxed{r_\alpha(S_\alpha)=m_\alpha\quad\text{for every }\alpha\in\sigma(L).}
\]
This is a **spectrally selective sensor-erasure rule**: a local aggregate with gain \(b_s(\alpha)\) supplies no information about the upper lifted mode associated with \(E_\alpha\), even though it still observes the lower lifted mode.

Two consequences highlight the effect. First, if all measured gains coincide at \(\beta\), then the system is observable exactly when the underlying graph is observable from \(S\) and \(\beta\notin\{b_s(\alpha):\alpha\in\sigma(L)\}\). In particular \(\beta=1\) always destroys observability, **even if every module is measured**. Second, if every module is measured and the \(n\) nonnegative gains are pairwise distinct, the system is fully observable for **every connected weighted base graph and every positive pendant conductance**.

## Assumptions and scope
The core graph is finite, connected, undirected, with strictly positive conductance on each of its existing edges; isolated core vertices are excluded by \(n\ge2\) and connectedness. The private pendant conductance is the same fixed \(s>0\) at every core vertex. Sensors are indexed by a nonempty \(S\subseteq\{1,\ldots,n\}\). Each sensor returns one real-valued scalar aggregate with a fixed nonnegative gain \(\beta_i\). The dynamics are noiseless continuous-time diffusion \(\dot z=-\mathcal L_s z\), and observability means unique recovery of every initial state from the complete output trajectory over any nontrivial time interval. The theorem is not a generic structural-observability statement: it evaluates the exact weighted numerical system.

In core-then-leaf coordinate order,
\[
 \mathcal L_s=\begin{pmatrix}L+sI&-sI\\-sI&sI\end{pmatrix},
 \qquad Cz=(u_i+\beta_i v_i)_{i\in S}.
\]
The dimension formula counts the real unobservable subspace and includes all repeated eigenvalues of the core.

## Proof
Fix an eigenvalue \(\alpha\ge0\) of \(L\) with eigenspace \(E_\alpha\). On the invariant space \(E_\alpha\oplus E_\alpha\), the Laplacian is the tensor of the identity on \(E_\alpha\) with the real symmetric matrix
\[
 \begin{pmatrix}\alpha+s&-s\\-s&s\end{pmatrix}.
\]
Its two eigenvalues, with the lower sign and upper sign respectively, are
\[
 \lambda_\pm(\alpha)=\frac{\alpha+2s\pm\sqrt{\alpha^2+4s^2}}2.
\]
For each \(w\in E_\alpha\), their lifted eigenvectors have the form \((w,\rho_\pm(\alpha)w)\), with
\[
 \rho_\pm(\alpha)=\frac{s}{s-\lambda_\pm(\alpha)}.
\]
Because \(0\le\lambda_-(\alpha)<s\) and \(\lambda_+(\alpha)\ge2s\), \(\rho_-(\alpha)>0\) and \(\rho_+(\alpha)<0\). Both \(\lambda_-(\alpha)\) and \(\lambda_+(\alpha)\) are strictly increasing functions of \(\alpha\). Their ranges are disjoint. Consequently lifted eigenspaces for distinct ordered pairs \((\alpha,\pm)\) have distinct eigenvalues; multiplicity inside \(E_\alpha\) is retained exactly.

On the lower eigenspace, sensor \(i\) evaluates
\[
 (1+\beta_i\rho_-(\alpha))w_i.
\]
Every factor is strictly positive because \(\beta_i\ge0\). The rank of this observation restriction is therefore exactly \(r_\alpha(S)\). On the upper eigenspace the analogous factor is \(1+\beta_i\rho_+(\alpha)\). This vanishes exactly at
\[
 \beta_i=-1/\rho_+(\alpha)=\lambda_+(\alpha)/s-1=b_s(\alpha).
\]
Deleting its zero rows and rescaling the remaining rows gives rank exactly \(r_\alpha(S_\alpha)\).

For a real symmetric matrix, the Popov–Belevitch–Hautus observability criterion says an eigenspace contributes as many unobservable dimensions as the dimension of its intersection with \(\ker C\). Summing those nullities over the distinct lifted eigenspaces gives
\[
 \sum_\alpha\{(m_\alpha-r_\alpha(S))+(m_\alpha-r_\alpha(S_\alpha))\},
\]
proving both boxed statements.

If every gain equals \(\beta\), then \(S_\alpha=S\) unless \(\beta=b_s(\alpha)\), in which case \(S_\alpha=\varnothing\). Since \(b_s(0)=1\) and the constant core vector is an eigenvector, the all-unity aggregate is always blind to the lifted antisymmetric constant mode \((\mathbf1,-\mathbf1)\). If all \(n\) modules are measured with pairwise distinct gains, for each \(\alpha\), at most one sensor is erased because \(b_s(\alpha)\) is a single number. A nonzero eigenvector of a connected graph cannot be supported on one vertex: the eigenvalue equation at a neighboring vertex of that lone nonzero coordinate would be violated by the positive edge conductance. Thus restriction to at least \(n-1\) remaining coordinates is injective on \(E_\alpha\), establishing the second consequence.

## Verification
The standalone `verify.py` constructs each Laplacian and observability matrix directly and evaluates ranks exactly with rational SymPy matrices. The script passed 18 full-observability checks across two three-vertex core graphs, 24 independent heterogeneous-gain invisible-dimension checks, and three exact full-module resonance checks. Two separate six-cycle examples were checked by numerical rank: modules at separation two yield rank 12, while antipodal modules fail, at gain \(1/2\) and pendant conductance 1. Numerical checks are illustrative only; the arbitrary-size theorem is proved above.

One exact witness uses the three-vertex path with unit core conductances, private pendant conductance \(s=2\), and all three modules measured. Its core eigenvalue 3 has \(b_2(3)=2\). Uniform gain 2 makes the six-state observability rank 5; uniform gain 1 also gives rank 5, while uniform gain \(1/2\) gives rank 6. Reproduce with `python verify.py`, requiring `sympy` and `numpy`.

## Relationship to prior work
Parlangeli and Notarstefano (arXiv:1109.3556v1, 2011) analyze direct vertex-state reachability/observability for paths and cycles. Liu (2014) provides the Laplacian spectrum of graph coronas, including the spectral eigenvalue lifting used here as background. Hsu (arXiv:1808.03022, 2018, Theorem 3.5) transfers **single-core-vertex input controllability** across certain composite graphs, a different observation operator. Liu and Ji (2017, DOI:10.1002/rnc.3870) study leader placement on path/cycle graphs. These sources do not state the heterogeneous-gain spectral-erasure rank identity or the loss and recovery of observability when entire core–leaf modules are summed. The spectral decomposition and the classical PBH criterion alone are insufficient to infer the precise sensor-gain rule without evaluating each lifted eigenspace under the aggregate operator.

## Limitations
The result assumes undirected diffusive coupling, identical strictly positive pendant conductances, simultaneous continuous-time observation, and nonnegative fixed gains. It does not cover heterogeneous pendant conductances, nonlinear sensors, graph uncertainty, discrete-time sampling aliases, observability conditioning, or reconstruction under noise. The numerical examples are finite checks, not substitutes for the analytic argument. Although relevant literature was compared, specialized aggregate-sensing results not found in the inspected sources could affect originality.

## References
1. G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556v1 (first public 2011-09-16), https://arxiv.org/abs/1109.3556.
2. Q. Liu, *The Laplacian spectrum of corona of two graphs*, Kragujevac Journal of Mathematics **38** (2014), 163–170, https://imi.pmf.kg.ac.rs/kjm/pub/14040480672304_11_the_laplacian_spectrum_of_corona_of_two_graphs.pdf.
3. S.-P. Hsu, *Laplacian Controllability of Interconnected Graphs*, arXiv:1808.03022 (2018), https://arxiv.org/abs/1808.03022.
4. X. Liu and Z. Ji, *Controllability of multiagent systems based on path and cycle graphs*, International Journal of Robust and Nonlinear Control, first online 2017-06-30, https://doi.org/10.1002/rnc.3870.
5. G. Notarstefano and G. Parlangeli, *Controllability and observability of grid graphs via reduction and symmetries*, arXiv:1203.0129v1 (2012), https://arxiv.org/abs/1203.0129.
