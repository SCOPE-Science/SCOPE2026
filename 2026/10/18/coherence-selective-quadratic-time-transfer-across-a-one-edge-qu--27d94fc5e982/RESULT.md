# Coherence-selective quadratic-time transfer across a one-edge quantum barbell

## Finding

Let \(B_n\), for every integer \(n\ge 3\), consist of two copies of \(K_n\) connected by exactly one edge between their distinguished bridge vertices. Give every edge unit weight. Let \(H_n=D_n^{-1/2}A_nD_n^{-1/2}\) be the symmetric normalized-adjacency Hamiltonian and \(U_n(t)=\exp(-itH_n)\). Write \(L_n\) and \(R_n\) for normalized equal-amplitude states on the \(n-1\) **nonbridge** vertices in the left and right cliques, respectively, and \(P_R\) for the orthogonal projection onto **all** right-clique vertices, including its bridge vertex.

For any normalized complex state \(\psi\) supported on the left nonbridge vertices, define its bright weight \(w(\psi)=|\langle L_n,\psi\rangle|^2\) and its right-clique transfer probability \(p_n(t;\psi)=\|P_RU_n(t)\psi\|^2\). The following statements hold simultaneously for every such \(\psi\), every \(n\ge3\), and every \(t\ge0\).

**Exact coherence selection.** The left-nonbridge sum-zero component never reaches the right clique, and
\[
p_n(t;\psi)=w(\psi)\,p_n(t;L_n),\qquad 0\le p_n(t;\psi)\le w(\psi).
\]

**Uniform-in-time two-level transfer.** Define
\[
a_n=\frac{n-2}{n-1},\qquad
\theta_n=\frac{n^2-3n+1+\sqrt{(n^2-3n+1)^2+4n(n-1)(2n-3)}}{2n(n-1)},
\qquad \Delta_n=1-\theta_n.
\]
Then \(\Delta_n>0\), \(\Delta_n=2n^{-2}+O(n^{-3})\), and
\[
\boxed{\ \left|p_n(t;\psi)-w(\psi)\sin^2\!\left(\frac{\Delta_n t}{2}\right)\right|
\le \frac{8n}{(n-1)^2}\,w(\psi).\ }
\]
The estimate is valid on arbitrarily long time intervals; its error constant does not depend on time, launch phases, or the choice of the left-nonbridge state.

**Sharp macroscopic transfer and preparation criterion.** For every fixed finite \(T>0\), uniformly over \(0\le\tau\le T\) and all normalized supported launch states,
\[
p_n(n^2\tau;\psi)=w(\psi)\bigl(\sin^2\tau+O_T(n^{-1})\bigr).
\]
At the explicit time \(t_n=\pi/\Delta_n=(\pi/2)n^2+O(n)\),
\[
w(\psi)\left(1-\frac{8n}{(n-1)^2}\right)
\le p_n(t_n;\psi)\le\sup_{t\ge0}p_n(t;\psi)\le w(\psi).
\]
Consequently a sequence of left-nonbridge normalized packets \(\psi_n\) admits right-clique transfer probability tending to one **if and only if** \(w(\psi_n)\to1\). A single nonbridge vertex has \(w=1/(n-1)\), so its best right-clique transfer probability satisfies
\[
\lim_{n\to\infty}(n-1)\sup_{t\ge0}p_n(t;|j\rangle)=1,
\]
whereas \(\sup_{t\ge0}p_n(t;L_n)\to1\). If \(t=o(n^2)\), every such packet has right-clique transfer probability tending to zero, uniformly in its choice. Finally, for each fixed \(0<\varepsilon<1\), the **first** time that the bright packet attains right-clique population at least \(1-\varepsilon\) obeys
\[
\frac{\inf\{t>0:p_n(t;L_n)\ge1-\varepsilon\}}{n^2}
\longrightarrow\arcsin\sqrt{1-\varepsilon}.
\]
This is a collective-region transfer statement. It does not assert vertex-to-vertex perfect state transfer or a uniform limit for arbitrary unnormalized graphs.

## Assumptions and scope

The Hilbert space is \(\mathbb C^{2n}\) with its ordinary orthonormal vertex basis. Both cliques have exactly \(n\) vertices, the one bridge is unweighted, all other edges have weight one, and there are no loops or added potentials. The nonbridge degrees are \(n-1\), and the bridge degrees are \(n\). The Hamiltonian is specifically \(H_n=D_n^{-1/2}A_nD_n^{-1/2}\), not the unnormalized adjacency matrix or the combinatorial Laplacian. Dynamics are closed and coherent, with a single final-time projective region measurement. Initial states may have arbitrary complex phases but must be normalized and supported entirely on the \(n-1\) nonbridge vertices of the left clique.

Big-O estimates hold as the integer \(n\to\infty\). The uniform-in-time error is a finite-\(n\) theorem, not just an expansion at one selected measurement time. The \(O_T\) constant may depend on the bounded scaled-time horizon \(T\), but never on the initial packet.

## Proof

**1. Dark space and four-dimensional reduction.** Any vector supported on the left nonbridge vertices whose components sum to zero is an eigenvector of \(H_n\) with eigenvalue \(-1/(n-1)\): adjacency within its clique produces the negative of each component, and its total coupling to the left bridge vertex vanishes. Such a vector therefore remains supported on the left clique at all times. The left-nonbridge Hilbert space splits orthogonally as \(\operatorname{span}\{L_n\}\oplus\mathcal D_L\), giving the exact factorization of the right-projected norm and its upper bound by \(w(\psi)\).

The orthogonal complement of the two dark spaces is invariant and is spanned by \((L_n,u,v,R_n)\), where \(u,v\) are the two bridge basis vectors. In this basis the Hamiltonian is exactly
\[
Q_n=\begin{pmatrix}
a&b&0&0\\ b&0&c&0\\0&c&0&b\\0&0&b&a
\end{pmatrix},\qquad
a=\frac{n-2}{n-1},\quad b=\frac1{\sqrt n},\quad c=\frac1n.
\]
Reflection about the bridge diagonalizes the action into even and odd sectors with matrices
\[
M_+=\begin{pmatrix}a&b\\b&c\end{pmatrix},\qquad
M_-=\begin{pmatrix}a&b\\b&-c\end{pmatrix}.
\]
Their spectral data are exact: \(\operatorname{spec} M_+=\{1,-1/[n(n-1)]\}\). Let \(\theta_n\) and \(\eta_n\) be the larger and smaller eigenvalues of \(M_-\). Solving its quadratic yields precisely the displayed formula for \(\theta_n\) and \(\eta_n=a-c-\theta_n\). The top odd eigenvalue satisfies \(a<\theta_n<1\), the upper inequality following from the simplicity of the Perron eigenvalue \(1\) of the connected nonnegative normalized-adjacency matrix (the eigenvector for eigenvalue one belongs to the even sector). Moreover,
\[
\Delta_n(1-\eta_n)=\det(I-M_-)
=(1-a)(1+c)-b^2=\frac2{n(n-1)}.
\]
Here \(\eta_n=O(n^{-1})\), since the sum of the two odd eigenvalues is \(a-c\) and \(\theta_n\to1\). Consequently \(\Delta_n=2n^{-2}+O(n^{-3})\), strictly positive for every admissible \(n\).

**2. Quantitative spectral concentration.** Set \(q_n=n/(n-1)^2\). The squared first-coordinate weight of the top eigenvector of \(M_+\) is exactly
\[
w_+=\frac1{1+n/(n-1)^2},\qquad1-w_+\le q_n.
\]
The corresponding top weight of \(M_-\) is \(w_-=[1+n(\theta_n-a)^2]^{-1}\). Since \(a<\theta_n<1\), we have \(\theta_n-a<1/(n-1)\), hence \(1-w_-\le q_n\). With
\[
f_\pm(t)=\langle e_1,e^{-itM_\pm}e_1\rangle,\qquad
 g_\pm(t)=\langle e_2,e^{-itM_\pm}e_1\rangle,
\]
the spectral decomposition of each real symmetric two-by-two block gives, **for every real \(t\)**,
\[
|f_+(t)-e^{-it}|\le2q_n,
\qquad|f_-(t)-e^{-i\theta_nt}|\le2q_n,
\qquad |g_\pm(t)|\le2\sqrt{q_n}.
\]
The final bound uses that the off-diagonal matrix exponential has magnitude at most twice the product of the two normalized eigenvector coordinates, bounded by \(2\sqrt{1-w_\pm}\).

**3. Uniform region probability.** Reflection symmetry yields exact amplitudes
\[
F_n(t)=\langle R_n,U_n(t)L_n\rangle=\frac{f_+(t)-f_-(t)}2,
\qquad
G_n(t)=\langle v,U_n(t)L_n\rangle=\frac{g_+(t)-g_-(t)}2.
\]
Thus \(p_n(t;L_n)=|F_n(t)|^2+|G_n(t)|^2\). Let \(Z_n(t)=(e^{-it}-e^{-i\theta_nt})/2\); then \(|Z_n(t)|^2=\sin^2(\Delta_nt/2)\). Step 2 implies \(|F_n-Z_n|\le2q_n\) and \(|G_n|^2\le4q_n\). Since \(|F_n|,|Z_n|\le1\),
\[
\bigl||F_n|^2-|Z_n|^2\bigr|\le4q_n,
\qquad
\bigl|p_n(t;L_n)-\sin^2(\Delta_nt/2)\bigr|\le8q_n.
\]
Multiplication by the exact factor \(w(\psi)\) proves the boxed theorem simultaneously for all times and packets.

**4. Scaling, earliest transition, and optimal preparation.** Since \(n^2\Delta_n/2=1+O(n^{-1})\), the bounded-\(\tau\) limit follows uniformly from the Lipschitz continuity of \(\sin^2\) and the error in step 3. At \(t_n=\pi/\Delta_n\), the sine-squared envelope equals one; the dark bound from step 1 supplies the matching universal upper bound, and \(t_n=(\pi/2)n^2+O(n)\). Therefore \(\sup_t p_n(t;\psi_n)\to1\) is equivalent to \(w(\psi_n)\to1\). For a single nonbridge vertex, the exact overlap is \(1/(n-1)\), which gives the sharp localized-state maximum by squeezing between the two bounds. At times \(o(n^2)\), the sine-squared envelope and \(q_n\) both vanish. For fixed \(0<\varepsilon<1\), \(\sin^2\tau\) first reaches \(1-\varepsilon\) at \(\tau=\arcsin\sqrt{1-\varepsilon}\) on \([0,\pi/2]\); uniform convergence on a compact interval containing that threshold, together with continuity of the finite-\(n\) probability, proves the claimed first-hitting-time limit.

## Verification

The standalone script `check_tunneling.py` builds the exact graph Hamiltonian and the two parity blocks, checks their eigenvalues and characteristic-polynomial identities, compares full-matrix propagation with the reduced model, and verifies arbitrary complex launch packets and the all-time envelope at representative test times. It also tests the large-\(n\) splitting and explicit peak times. From the embedded package, run `python check_tunneling.py` after installing `requirements.txt`; the program reports 482 passing matrix, spectral, and numerical assertions. These finite tests are reproducibility diagnostics; the uniform infinite-family conclusions follow from the proof, not test coverage.

## Relationship to prior work

Dhamapurkar and Subrahmanyam, *Localization Without Disorder: Quantum Walks on Structured Graphs* (arXiv:2603.05643v1, first made public March 5, 2026), supply the exact normalized-adjacency barbell eigenspectrum, dark-subspace construction, eigenstate and dynamical inverse-participation ratios, and a qualitative discussion of slow bridge leakage. Those results—including the existence of even and odd near-degenerate eigenmodes—are **prior**. The claim here is not a new diagonalization: it is the finite-\(n\), all-time packet-to-region estimate, the sharp scaled transfer law, the optimal coherence criterion for arbitrary initial packets, and the first macroscopic arrival scale.

Duda and Wong, *Searching Weighted Barbell Graphs with Laplacian and Adjacency Quantum Walks* (arXiv:2408.08244), study oracle-assisted search and variable bridge weights with unnormalized adjacency/Laplacian dynamics; their transport observables, preparation and timescales differ. Brown, Martin, and Wright, *Continuous Time Quantum Walks on Graphs: Group State Transfer* (arXiv:2103.08837), study exact group transfer predominantly for adjacency evolution, not a sharp approximate population transfer in this normalized-adjacency family. General two-level near-degeneracy methods and the original eigenspectrum might make part of this derivation implicit in broader literature; no priority beyond the precisely stated quantitative assertion is established here.

## Limitations

The assertion is specific to equal-clique unit-edge barbells with symmetric normalized adjacency and initial support on the nonbridge region. It gives probability of being found in the **entire opposite clique** at a chosen time, not the first detection time, individual vertex transfer, a dynamical noisy channel, or state transfer for arbitrary source/target shapes. The error bound is explicit and uniform but not asserted to be the optimal finite-\(n\) constant. The theorem does not classify possible exact revivals at finite \(n\), and no independent verification or exhaustive literature certification is claimed. Earlier exact eigenvalues imply a route to some of these formulas; that potential implicit coverage is the principal originality risk.

## References

1. S. Dhamapurkar and K. V. Subrahmanyam, *Localization Without Disorder: Quantum Walks on Structured Graphs*, arXiv:2603.05643v1 (2026-03-05). https://arxiv.org/abs/2603.05643
2. J. Duda and T. G. Wong, *Searching Weighted Barbell Graphs with Laplacian and Adjacency Quantum Walks*, arXiv:2408.08244v1 (2024-08-15). https://arxiv.org/abs/2408.08244
3. L. C. Brown, W. J. Martin, and D. Wright, *Continuous Time Quantum Walks on Graphs: Group State Transfer*, arXiv:2103.08837v1 (2021-03-16). https://arxiv.org/abs/2103.08837
