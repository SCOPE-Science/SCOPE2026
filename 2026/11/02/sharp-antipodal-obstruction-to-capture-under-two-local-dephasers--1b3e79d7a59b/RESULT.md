# Sharp antipodal obstruction to capture under two local dephasers on hypercubes

## Finding

Let \(d\ge3\) be an integer. A coherent particle moves on the vertices of the binary hypercube \(Q_d\), one vertex \(a\) absorbs particles, and two other distinct vertices \(b,c\) undergo strictly positive local pure dephasing. For the precisely specified trace-decreasing Lindblad dynamics below, the maximal non-decaying Hilbert subspace \(\mathcal D\) has dimension
\[
\dim\mathcal D=\begin{cases}
2^d-2d,&\text{if some pair among }a,b,c\text{ is antipodal},\\
2^d-3d+1,&\text{otherwise}.
\end{cases}
\]
Here antipodal means that two binary strings disagree in every coordinate. For **every** initial density matrix \(\rho_0\ge0\) with \(\operatorname{tr}\rho_0=1\), its eventual absorption probability exists and is exactly
\[
P_{\mathrm{abs}}(\rho_0)=1-\operatorname{tr}(\Pi_{\mathcal D}\rho_0).
\]
In particular, for an initially uniform *incoherent* mixture, the absorption probability is \(2d/2^d\) if one pair is antipodal and \((3d-1)/2^d\) otherwise. Thus a single antipodal pair discards exactly \(d-1\) bright dimensions. Three distinct monitored vertices ensure eventual capture of **every** initial state precisely in dimension \(d=3\) and precisely when no pair is antipodal; for \(d\ge4\), some dark states always remain.

## Assumptions and scope

Write \(V=\{0,1\}^d\) and \(\mathcal H=\mathbb C^{2^d}\), with orthonormal site basis \(\{|x\rangle:x\in V\}\). Let \(H=J A(Q_d)\), where \(J\in\mathbb R\setminus\{0\}\) and \(A(Q_d)\) joins pairs differing in one bit. Select pairwise distinct \(a,b,c\in V\), an absorbing population rate \(\kappa>0\) at \(a\), and local phase-noise strengths \(\gamma_b,\gamma_c>0\) at \(b,c\). With \(P_x=|x\rangle\langle x|\), the unnormalized one-excitation density matrix satisfies
\[
\dot\rho=-i[H,\rho]-\frac\kappa2\{P_a,\rho\}+\sum_{z\in\{b,c\}}\gamma_z\left(P_z\rho P_z-\frac12\{P_z,\rho\}\right).
\]
Absorption into an external sink is represented by the trace loss; there is no other loss or gain. All positive rate values are allowed. The eventual absorption probability is \(1-\lim_{t\to\infty}\operatorname{tr}\rho(t)\). Define the distinct eigenspaces \(E_k\) of \(H\) for eigenvalue \(J(d-2k)\), \(k=0,\ldots,d\). The claimed dark subspace is
\[
\mathcal D=\bigoplus_{k=0}^{d}\{\psi\in E_k:\langle a|\psi\rangle=\langle b|\psi\rangle=\langle c|\psi\rangle=0\}.
\]

## Proof

**1. The surviving space is exactly \(\mathcal D\).** Every vector in \(\mathcal D\) is orthogonal to the three monitored vertices and \(\mathcal D\) is invariant under the Hermitian \(H\). Its orthogonal projector \(\Pi_{\mathcal D}\) commutes with \(H\), while \(P_x\Pi_{\mathcal D}=\Pi_{\mathcal D}P_x=0\) for \(x=a,b,c\). Therefore \(\operatorname{tr}(\Pi_{\mathcal D}\rho(t))=\operatorname{tr}(\Pi_{\mathcal D}\rho_0)\) for all time.

Positivity and the decreasing trace imply existence of \(\ell=\lim_{t\to\infty}\operatorname{tr}\rho(t)\). For any \(T>0\), let \(\overline\rho_T=T^{-1}\int_0^T\rho(t)\,dt\). Every convergent subsequence has a positive semidefinite limit \(R\) of trace \(\ell\), and the master equation gives \(\mathcal L(R)=\lim_{T\to\infty}(\rho(T)-\rho(0))/T=0\). The trace of the stationary equation forces \(\operatorname{tr}(P_aR)=0\), whence \(P_aR=RP_a=0\) by positivity. The exact stationary purity identity is
\[
0=2\operatorname{tr}(R\mathcal L(R))=-2\kappa\operatorname{tr}(RP_aR)-\sum_{z=b,c}\gamma_z\|[P_z,R]\|_2^2.
\]
Every term on the right is nonpositive, hence \([P_z,R]=0\) for both noisy sites. The stationary equation now reduces to \([H,R]=0\). Suppose \(\langle z|R|z\rangle>0\) for \(z\in\{b,c\}\). Commutation with \(P_z\) makes \(|z\rangle\) an eigenvector of \(R\) with positive eigenvalue. Thus \(|z\rangle\) belongs to its support. Since \([H,R]=0\), that support is \(H\)-invariant, so it contains \(H^h|z\rangle\) for \(h\) the Hamming distance from \(z\) to \(a\). Yet \(\langle a|H^h|z\rangle=J^h h!\ne0\), because exactly \(h!\) shortest walks join the two sites. This contradicts \(P_aR=0\). Hence \(P_bR=P_cR=0\) as well. The support of \(R\) is an \(H\)-invariant subspace orthogonal to all three monitored vertices, and so lies in \(\mathcal D\). The conserved dark weight therefore equals \(\ell\): the inequality \(\ell\ge\operatorname{tr}(\Pi_{\mathcal D}\rho_0)\) holds at all times, while \(R\) supported in \(\mathcal D\) gives equality. This proves the absorption formula for arbitrary initial density matrices, not just mixtures.

**2. Spectral ranks.** Translate all three vertices by bitwise XOR with \(a\). The three monitored sites become \(0,u,v\), with \(u,v\ne0\), \(u\ne v\). For each integer \(0\le k\le d\), let \(\mathcal S_k\) be all \(k\)-subsets of \(\{1,\ldots,d\}\). The Walsh eigenbasis in \(E_k\) has components \(2^{-d/2}(-1)^{|S\cap x|}\) at vertex \(x\) for \(S\in\mathcal S_k\). Thus the rank of the three evaluation functionals restricted to \(E_k\) is the rank of the three rows
\[
\bigl(1\bigr)_{S\in\mathcal S_k},\qquad
\bigl((-1)^{|S\cap u|}\bigr)_{S\in\mathcal S_k},\qquad
\bigl((-1)^{|S\cap v|}\bigr)_{S\in\mathcal S_k}.
\]
At \(k=0,d\), there is one column, hence rank \(1\).

For \(1\le k\le d-1\), suppose **no** pair of sites is antipodal. Among the \(d\) coordinate-pattern pairs \((u_j,v_j)\in\{(0,0),(0,1),(1,0),(1,1)\}\), there must be at least three distinct patterns: if there were only one or two, the fact that \(u,v\) are nonzero and distinct forces either \(u\) or \(v\) to be all ones, or \(u\oplus v\) to be all ones, producing an antipodal pair. Any three different corners of this two-bit square include two patterns differing only in the first bit and two patterns differing only in the second bit. Suppose a linear relation
\[
\alpha+\beta(-1)^{|S\cap u|}+\delta(-1)^{|S\cap v|}=0
\quad\text{for every }S\in\mathcal S_k.
\]
Choose coordinate indices \(i,j\) with equal second pattern bit but unequal first bit. Because \(1\le k\le d-1\), a \(k\)-subset exists containing \(i\) but not \(j\). Exchanging \(i\) for \(j\) leaves the constant and the second Walsh sign unchanged while reversing the first, forcing \(\beta=0\). Repeating for indices differing only in the second pattern bit gives \(\delta=0\), and then \(\alpha=0\). Consequently the three rows are independent, with rank \(3\) at every interior level.

If instead some pair is antipodal, then one of \(u\), \(v\), \(u\oplus v\) is the all-ones binary string. On every fixed weight level \(k\), its Walsh sign is the constant \((-1)^k\), making one of the three rows dependent on the other two. The other two rows are independent for \(1\le k\le d-1\): a nonzero proper bitstring has both a zero and a one coordinate, whose swap on a fixed-size subset changes its parity. Hence interior rank \(2\).

**3. Total dimension and complete-capture cutoff.** The orthogonal complement of \(\mathcal D\) consists, at each spectral level, of the span of the projections of the three monitored site vectors. Its total dimension is \(2+(d-1)\cdot3=3d-1\) if no pair is antipodal, and \(2+(d-1)\cdot2=2d\) otherwise. Subtracting from \(2^d\) gives the theorem. The inequality \(3d-1<2^d\) holds for every \(d\ge4\) (by induction, starting with \(d=4\)); when \(d=3\), \(3d-1=2^d=8\). This proves the complete-capture dichotomy, including the boundaries.

## Verification

A stand-alone Python 3 checker is included at `verify.py`. It constructs exact integer Walsh-evaluation Gram matrices, exhaustively checks all unordered \(u,v\ne0\) with \(u\ne v\) for anchored triples \((0,u,v)\) through dimension \(7\), and checks that each interior-level rank is exactly the value predicted. There are \(59{,}988\) exact interior rank assertions. The code separately builds the full Lindblad superoperator and propagates maximally mixed states on dimensions \(3\) and \(4\) for antipodal and non-antipodal examples; four separate numerical evaluations converge to the predicted capture fractions. Run `python3 verify.py` with NumPy and SciPy installed. Finite calculations corroborate but do not replace the all-dimensional proof.

## Relationship to prior work

Strauch (2008) analyzes global vertex/subspace decoherence and finite-time hitting on hypercubes; its decoherence acts across all vertices or coordinate subspaces, not at two selected sites with a permanent absorber. Novo and collaborators (2014) derive the single-trap hypercube bright cyclic space, of dimension \(d+1\), in a coherent no-dephasing model. Le and collaborators (2017) develop graph-based dark-state arguments and discuss dephasing but do not state the present antipodal-versus-nonantipodal *triple*-monitor spectral rank and exact asymptotic capture law. The earlier two-marked-vertex hypercube dimension dichotomy, and the general dark-state framework, are not asserted as new here. Their methods alone do not furnish the independent third Walsh evaluation row or the dimension-three complete-capture boundary, which are the specific contributions assessed.

## Limitations

The result is restricted to a homogeneous, nonzero real nearest-neighbor hopping matrix on a binary hypercube, one absorber, exactly two distinct strictly positive *sitewise* Markovian dephasers, and no other population losses. It does not imply any finite-time capture rate or robustness to imperfect monitoring. It does not cover detuned couplings, nonlocal noise, additional absorbing sites, or arbitrary graph topologies.

## References

1. F. W. Strauch, "Reexamination of decoherence in quantum walks on the hypercube," arXiv:0808.3403 (initial public posting 2008-08-25), https://arxiv.org/abs/0808.3403.
2. L. Novo et al., "Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs," arXiv:1412.7209 (2014), https://arxiv.org/abs/1412.7209.
3. T. P. Le et al., "How to Suppress Dark States in Quantum Networks and Bio-Engineered Structures," arXiv:1707.07482 (2017), https://arxiv.org/abs/1707.07482.
