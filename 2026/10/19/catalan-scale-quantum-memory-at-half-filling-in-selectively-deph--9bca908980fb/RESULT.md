# Catalan-scale quantum memory at half filling in selectively dephased Johnson walks

## Finding
Let \(n\ge3\) and \(1\le k<n\). The vertices of the Johnson graph \(J(n,k)\) are the \(k\)-subsets of \(\{1,\ldots,n\}\); vertices are adjacent when they differ in one element. Put the adjacency Hamiltonian \(H=A(J(n,k))\) on the one-particle Hilbert space. Independently dephase, at **arbitrary strictly positive rates**, all vertices (subsets) that contain element \(n\), leaving the remaining vertices unmonitored.

Write \(D\) for the orthogonal projector onto the subspace of unmonitored amplitudes annihilated by the hopping block into the monitored sites. Its exact dimension is
\[
d_{n,k}=\operatorname{rank}D=\max\left\{0,\binom{n-1}{k}-\binom{n-1}{k-1}\right\}.
\]
For every initial density matrix \(\rho_0\), the **ordinary, non-time-averaged** limit exists and equals
\[
\lim_{t\to\infty}\rho_t=D\rho_0D+\frac{1-\operatorname{tr}(D\rho_0)}{\binom nk-d_{n,k}}(I-D).
\]
The entire complex stationary operator algebra is \(\mathcal B(D\mathcal H)\oplus\mathbb C(I-D)\), of dimension \(d_{n,k}^{2}+1\); there are no nonzero purely imaginary Liouvillian eigenvalues. In particular, when \(n\le2k\), the limit is the maximally mixed state for every initialization. When \(n>2k\), arbitrary density matrices supported on the \(d_{n,k}\)-dimensional dark sector retain all their coherences.

For an initial vertex \(S\) that does not contain \(n\), define
\[
w_{n,k}=\frac{d_{n,k}}{\binom{n-1}{k}}=\max\left\{0,\frac{n-2k}{n-k}\right\},\qquad b_{n,k}=\binom nk-d_{n,k}.
\]
Its post-relaxation return probability is exactly
\[
R_{n,k}^{\rm unmon}=w_{n,k}^{2}+\frac{(1-w_{n,k})^{2}}{b_{n,k}}.
\]
For an initially monitored vertex, the return is \(1/b_{n,k}\).

A sharp half-filling effect follows. At \(n=2k\), the dark sector is absent and \(R_{2k,k}^{\rm unmon}=\binom{2k}{k}^{-1}\), exponentially small in \(k\). At \(n=2k+1\), the dark dimension **jumps to the Catalan number**
\[
d_{2k+1,k}=C_k=\frac1{k+1}\binom{2k}{k},
\]
and the exact return becomes
\[
R_{2k+1,k}^{\rm unmon}=\frac1{(k+1)^2}+\frac{k}{2(k+1)^2C_k},\qquad \lim_{k\to\infty}k^2R_{2k+1,k}^{\rm unmon}=1.
\]
Thus adding one distinguished-element option at half filling changes long-time unmonitored return from exponential to polynomial decay, while creating an exponentially large coherent memory sector.

## Assumptions and scope
The Hamiltonian has real equal nearest-neighbor Johnson-graph hopping amplitudes and no site potentials. The Lindblad generator is
\[
\mathcal L(X)=-i[H,X]+\sum_{T\ni n}\gamma_T\left(P_TXP_T-\tfrac12\{P_T,X\}\right),
\]
where \(P_T=|T\rangle\langle T|\), each \(\gamma_T>0\), and \(\{\ ,\ \}\) denotes the anticommutator. Dephasing acts **separately** at every monitored vertex. Rates may be unequal and need not have a uniform lower bound as \(n\) varies. The statements concern finite \(n,k\), with the long-time limit taken first; no uniform mixing-time estimate is claimed. The strict inequality \(\gamma_T>0\) is required for every monitored \(T\).

## Proof
**1. Boolean-level incidence and exact dark dimension.** Put \(m=n-1\) and separate the vertices into unmonitored \(k\)-subsets \(S\subset[m]\), with count \(u=\binom mk\), and monitored \((k-1)\)-subsets \(T\subset[m]\), with count \(v=\binom m{k-1}\). In the ordered decomposition \(\mathcal H=\mathcal H_M\oplus\mathcal H_U\), write
\[
H=\begin{pmatrix}A_M&B\\B^*&A_U\end{pmatrix},\qquad B_{T,S}=\mathbf1\{T\subset S\}.
\]
Here \(A_U=A(J(m,k))\) and \(A_M=A(J(m,k-1))\). Counting common \((k-1)\)-subsets of two \(k\)-subsets gives the exact identity \(B^*B=kI_U+A_U\). Hence \(D\mathcal H=\ker B\subset\mathcal H_U\) is \(H\)-invariant and \(H\) acts on it as \(-kI\).

For completeness, the incidence rank can be proved without invoking a spectral table. Let \(V_\ell\) be the space of complex functions on \(\ell\)-subsets of \([m]\), let \(U_\ell:V_\ell\to V_{\ell+1}\) sum over included \(\ell\)-subsets, and set \(D_{\ell+1}=U_\ell^*\). Directly counting add/remove paths yields
\[
D_{\ell+1}U_\ell-U_{\ell-1}D_\ell=(m-2\ell)I_{V_\ell},
\]
with the missing boundary operator interpreted as zero. Therefore, when \(\ell<m/2\),
\[
\|U_\ell f\|^2=\|D_\ell f\|^2+(m-2\ell)\|f\|^2,
\]
so \(U_\ell\) is injective. Since \(B^*=U_{k-1}\), it follows that \(B\) has full row rank for \(k\le(m+1)/2\). For \(k>(m+1)/2\), complementing subsets identifies \(B\) with \(U_{m-k}\), which is injective, giving full column rank. Thus \(\operatorname{rank}B=\min(u,v)\) and \(\dim\ker B=\max(0,u-v)\), as claimed. This also covers the central square incidence matrix and all endpoint values of \(k\).

**2. The complete fixed operator space.** For arbitrary matrices \(X\), the Hilbert–Schmidt dissipation identity is
\[
\operatorname{Re}\langle X,\mathcal L(X)\rangle_{HS}=-\frac12\sum_{T\ni n}\gamma_T\|[P_T,X]\|_{HS}^2.
\]
If \(\mathcal L(X)=0\), positivity of every rate implies \([P_T,X]=0\) for each monitored \(T\). Thus \(X\) has a diagonal monitored block and an arbitrary unmonitored block, with no cross entries. Then \([H,X]=0\); since the Johnson graph on monitored \((k-1)\)-subsets is connected (the one-vertex case included), its diagonal monitored entries are a common scalar \(c\). The cross-block equations become \(BX_U=cB\) and \(X_UB^*=cB^*\). Hence \(Y=X_U-cI_U\) obeys \(BY=YB^*=0\), so \(Y=D Y D\). Conversely any such \(Y\) commutes with \(H\), because \(HD=-kD\), and it commutes with each monitored projector. Consequently the fixed operator space is exactly \(\{c(I-D)+DYD:c\in\mathbb C,\,Y\in\mathcal B(\mathcal H)\}\).

**3. No undamped oscillations; convergence.** If \(\mathcal L(X)=i\omega X\) with real \(\omega\), the same dissipation identity makes \(X\) block diagonal as above. For \(\omega\ne0\), the diagonal entries of its monitored block vanish, because the monitored diagonal of \([H,X]\) is zero. The cross-block eigen-equations then force \(BX_U=X_UB^*=0\), making \(X_U\) supported on \(\ker B\), where \([H,X]=0\). Thus \(X=0\), a contradiction. The semigroup is contractive in Hilbert–Schmidt norm by the displayed identity, so no nontrivial Jordan block occurs on the imaginary axis. All other eigenmodes decay, giving an ordinary limit in finite dimension.

**4. Which fixed state is reached.** Since \(D\) commutes with \(H\) and all \(P_T\), one has \(D\rho_tD=D\rho_0D\) for all \(t\). Trace conservation fixes the remaining bright-state weight, and its only fixed operator is a scalar multiple of \(I-D\). This gives the stated limiting density matrix.

**5. Return probabilities and the Catalan boundary.** Permutations of \([m]\) preserve \(D\) and act transitively on the unmonitored \(k\)-subsets, so every diagonal entry \(\langle S|D|S\rangle\) is \(d_{n,k}/u\). For an initial local pure state, evaluating the limiting matrix element gives \(w_{n,k}^2+(1-w_{n,k})^2/b_{n,k}\). For monitored vertices it gives \(1/b_{n,k}\). At \(n=2k+1\), the binomial difference equals \(C_k\), the bright dimension is \(2kC_k\), and \(w=1/(k+1)\), yielding the exact formula. Since \(C_k\) grows exponentially and \(\binom{2k}{k}\sim4^k/\sqrt{\pi k}\), the advertised polynomial versus exponential return follows.

## Verification
The standalone program `verify_johnson.py` constructs the adjacency and inclusion matrices directly from subsets; checks \(B^*B=kI+A_U\), incidence rank, the dark eigenvalue, and the uniform local dark weight; and independently builds the full Lindblad superoperator for small graphs with distinct positive monitoring rates. It tests stationary multiplicities, absence of nonzero peripheral modes, and finite-time convergence toward the predicted limit. Run with `python verify_johnson.py` after installing the standard numerical requirements in `requirements.txt`. Exact rank identities in the proof, not finite testing, establish the infinite family. The program reports its tested finite cases when executed.

## Relationship to prior work
Johnson-graph continuous-time quantum search and its symmetry reductions were studied by Thomas G. Wong, *Quantum Walk Search on Johnson Graphs*, arXiv:1601.04212 (first publicly submitted 16 January 2016). That work studies a Hamiltonian search oracle and coherent search times, not a Lindblad evolution with independent dephasing of all subsets containing a fixed element. Known Johnson-scheme harmonic eigenspaces and their multiplicities are developed by Yuval Filmus, *Orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142, especially the harmonic dimension lemma and Johnson eigenspace discussion. Accordingly neither the inclusion rank nor the Johnson spectral multiplicity is claimed as new in isolation. General asymptotic Lindblad-state decompositions appear in B. Baumgartner and H. Narnhofer, *Analysis of quantum semigroups with GKS–Lindblad generators II. General*, arXiv:0806.3164. The specific contribution here is the **complete Johnson-family stationary algebra, exact local-return law, and adjacent central-rank Catalan jump** for the stated site-selective monitoring. General Lindblad structure alone does not state these Johnson-specific quantities. Closely related discrete-time quantum search and other monitoring conventions are different dynamics, not equivalent statements. This work does not claim a first discovery of Johnson incidence ranks or of the general commutant method.

## Limitations
The result is restricted to one distinguished element defining the monitored set, individual positive site-dephasing rates, and the unweighted Johnson adjacency Hamiltonian. The precise asymptotic return depends on taking \(t\to\infty\) at fixed finite \(n\) before allowing \(k\to\infty\). It does not provide finite-time mixing or robustness bounds, nor a statement for measurements grouped into a single collective Lindblad operator. The available literature comparison cannot exclude an unindexed equivalent treatment of exactly this monitor geometry. Numerical spectra are supporting checks, not independent proof or independent scientific validation.

## References
1. T. G. Wong, *Quantum Walk Search on Johnson Graphs*, arXiv:1601.04212, initially public 2016-01-16, https://arxiv.org/abs/1601.04212.
2. Y. Filmus, *Orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142, initially public 2014-06-01, https://arxiv.org/abs/1406.0142.
3. B. Baumgartner and H. Narnhofer, *Analysis of quantum semigroups with GKS–Lindblad generators II. General*, arXiv:0806.3164, initially public 2008-06-19, https://arxiv.org/abs/0806.3164.
4. V. Kendon and B. Tregenna, *Decoherence can be useful in quantum walks*, Physical Review A 67, 042315 (2003), https://doi.org/10.1103/PhysRevA.67.042315.
