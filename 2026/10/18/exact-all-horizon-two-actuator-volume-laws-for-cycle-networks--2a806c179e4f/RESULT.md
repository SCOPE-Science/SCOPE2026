# Exact all-horizon two-actuator volume laws for cycle networks

## Finding
Let \(C_n\) be the unweighted undirected cycle, \(n\ge3\), let \(L_n\) be its combinatorial Laplacian, and fix real \(a,b\) with \(b\ne0\). Two independent unit-strength scalar controls act at vertices \(0\) and \(d\), where \(1\le d\le\lfloor n/2\rfloor\). For \(A=aI-bL_n\), \(B_d=[e_0,e_d]\), and integer horizon \(T\ge1\), define the full-state finite-horizon reachability Gramian
\[
W_{n,d}(T)=\sum_{t=0}^{T-1}A^tB_dB_d^{\mathsf T}A^t.
\]
The following gives its determinant and global two-actuator D-optimal placement, for **every** time horizon and every allowed affine diffusion parameter.

Write \(\lambda_k=a-b(2-2\cos(2\pi k/n))\). For an ordered index set \(I\), put
\[
H_T(I)=\det\left[\sum_{t=0}^{T-1}(\lambda_i\lambda_j)^t\right]_{i,j\in I},\qquad H_T(\varnothing)=1.
\]
A range \(r{:}s\) denotes all integer indices from \(r\) through \(s\), inclusive.

**Odd cycles.** If \(n=2m+1\), all determinants vanish for \(T\le m\). For every \(T\ge m+1\),
\[
\det W_{n,d}(T)=
\begin{cases}
\displaystyle\frac{2}{n^{n-1}}H_T(0{:}m)H_T(1{:}m),&\gcd(d,n)=1,\\
0,&\gcd(d,n)>1.
\end{cases}
\]
Thus every controllable pair is globally determinant-optimal, with *exactly the same* positive determinant, independent of separation, for every sufficiently long finite horizon.

**Even cycles.** If \(n=2m\), all determinants vanish for \(T<m\). For every \(T\ge m\),
\[
\det W_{n,d}(T)=
\begin{cases}
\displaystyle n^{2-n}H_T(0{:}m-1)H_T(1{:}m),&\gcd(d,m)=1,\ d\text{ odd},\\
\displaystyle n^{2-n}H_T(0{:}m)H_T(1{:}m-1),&\gcd(d,m)=1,\ d\text{ even},\\
0,&\gcd(d,m)>1.
\end{cases}
\]
For \(T=m\) the even-distance expression is zero. For \(T\ge m+1\) both displayed products are positive. The first (odd-distance) expression is always at least the second: **every odd separation coprime to \(m\) is globally D-optimal at every horizon \(T\ge m\)**. In particular, adjacent actuators always form a globally D-optimal pair. All odd separations coprime to \(m\) tie exactly, regardless of their geometric lengths.

## Assumptions and scope
Vertices are labeled modulo \(n\). The two input channels are independent and enter with identical unit scale. The objective is the *full-state* determinant, including the spatially constant Laplacian mode; it is neither the pseudodeterminant of a disagreement-only Gramian nor a trace-based robustness metric. No restriction on the sign, stability, or magnitude of \(a\) and \(b\) is needed because the horizon is finite; the condition \(b\ne0\) ensures distinct eigenvalues across distinct cycle frequencies. The theorem does not claim a continuous-time infinite-horizon counterpart. If \(T\) is too short, rank alone forces the stated zero determinant.

## Proof
**1. Fourier block factorization.** In an orthonormal real Fourier eigenbasis for \(L_n\), the zero-frequency mode has control row \(n^{-1/2}(1,1)\). Each interior frequency \(k\) has a two-dimensional cosine-sine eigenspace, with projected control block
\[
D_k=\sqrt{2/n}\begin{pmatrix}1&\cos(2\pi kd/n)\\0&\sin(2\pi kd/n)\end{pmatrix}.
\]
The corresponding block of the Krylov matrix \(K=[B_d,AB_d,\ldots,A^{T-1}B_d]\) is \(D_k[I_2,\lambda_kI_2,\ldots,\lambda_k^{T-1}I_2]\). Consequently, when its block is nonsingular, factoring \(D_k\) out of the rows multiplies \(\det(KK^{\mathsf T})\) by \((\det D_k)^2=(4/n^2)\sin^2(2\pi kd/n)\). If a sine vanishes, the corresponding frequency block has rank less than two, so the complete Gramian is singular. This factorization remains valid as a determinant identity at singular parameter values by continuity.

**2. Odd-order normalization.** For \(n=2m+1\), there are exactly \(m\) two-dimensional nonconstant Fourier blocks. After factoring them out and extracting the scalar \(1/\sqrt n\) from the constant row, rotate the two input channels to their symmetric and antisymmetric combinations. The constant mode occupies only the symmetric channel, with amplitude \(\sqrt2\); each interior frequency contributes one row in each channel. The determinant of the remaining row Gramian is therefore
\[
2H_T(0{:}m)H_T(1{:}m).
\]
For \(\gcd(d,n)=1\), multiplication by \(d\) permutes the nonzero residues modulo the odd integer \(n\), up to sign, and the classical sine product gives
\[
\prod_{k=1}^m\sin^2(2\pi kd/n)=\frac{n}{4^m}.
\]
Combining this with the Fourier normalization \(n^{-1}(4/n^2)^m\) gives the asserted constant \(2/n^{n-1}\). If \(\gcd(d,n)>1\), at least one of the sine factors vanishes: choose \(k=n/\gcd(d,n)\le m\). The distinct \(\lambda_k\) make both moment Gramians positive definite once \(T\ge m+1\), by polynomial interpolation at distinct nodes.

**3. Even-order normalization.** For \(n=2m\), there are \(m-1\) cosine-sine blocks and two scalar modes. The latter are the constant mode with control row \(n^{-1/2}(1,1)\) and the alternating mode with control row \(n^{-1/2}(1,(-1)^d)\). If \(\gcd(d,m)>1\), an interior sine vanishes at a frequency between \(1\) and \(m-1\). If \(\gcd(d,m)=1\), the product is
\[
\prod_{k=1}^{m-1}\sin^2(\pi kd/m)=\frac{m^2}{4^{m-1}}.
\]
The normalization from the two scalar rows, the interior blocks, and the orthogonal input-channel rotation is
\[
\frac1{n^2}\left(\frac4{n^2}\right)^{m-1}\frac{m^2}{4^{m-1}}\cdot4=n^{2-n}.
\]
When \(d\) is odd, the alternating and constant modes occupy opposite rotated input channels, yielding the Gram determinants on index sets \(0{:}m-1\) and \(1{:}m\). When \(d\) is even, both occupy the symmetric channel, yielding \(0{:}m\) and \(1{:}m-1\). This proves both exact formulas, including singularity of the even-distance case at \(T=m\).

**4. Global optimality.** Put \(v_k=(1,\lambda_k,\ldots,\lambda_k^{T-1})\in\mathbb R^T\), and let \(E\) be the span of \(v_1,\ldots,v_{m-1}\). For \(T\ge m\), this family is linearly independent. Define residuals \(u=v_0-P_Ev_0\) and \(w=v_m-P_Ev_m\), where \(P_E\) is orthogonal projection. Schur complements of the common interior Gram matrix \(G_E\) give
\[
\begin{aligned}
&H_T(0{:}m-1)H_T(1{:}m)=(\det G_E)^2\|u\|^2\|w\|^2,\\
&H_T(0{:}m)H_T(1{:}m-1)=(\det G_E)^2(\|u\|^2\|w\|^2-\langle u,w\rangle^2).
\end{aligned}
\]
Their difference is \((\det G_E)^2\langle u,w\rangle^2\ge0\). Thus no even-distance pair can outperform an eligible odd-distance pair, and no noncoprime pair can outperform its strictly positive determinant. In an even cycle the adjacent pair has \(d=1\), hence is eligible. In an odd cycle every coprime pair realizes the only positive value. This settles global optimization over *all* unordered pairs by rotational and reflection symmetry.

## Verification
The included standalone \(\texttt{verify.py}\) computes complete finite-horizon Gramians with exact integer arithmetic, evaluates their determinants by fraction-free Bareiss elimination, tests every pair separation on small cycles and multiple horizons, and independently checks the explicit spectral products at cycle orders with rational eigenvalues. Execute \(\texttt{python3 verify.py}\). The expected output begins with \(\texttt{VERIFY_OK}\). An exhaustive finite experiment is not presented as a proof for arbitrary graph order; the proof above establishes the quantified statements.

## Relationship to prior work
Parlangeli and Notarstefano, *On the Reachability and Observability of Path and Cycle Graphs* (arXiv:1109.3556, first made public September 16, 2011), studies algebraic conditions for reachability and observability on paths and cycles. It does not give the determinant-volume identities, all-horizon placement ties, or the Schur-complement comparison of the two parity classes. Its stated two-node cycle criterion is not directly assumed here: the present rank conclusion follows independently from the explicit Fourier blocks (notably, at even cycle order the alternating scalar mode must be treated separately).

Zhang, Camlibel, and Cao, *Controllability of Diffusively-Coupled Multi-Agent Systems with General and Distance Regular Coupling Topologies* (2011), establishes that two adjacent leaders render a cycle controllable and gives general multi-leader dimension criteria. Its inspected cycle theorem concerns full rank, not equality or optimization of the positive determinant at arbitrary finite horizons.

Fitch and Leonard, *Optimal Leader Selection for Controllability and Robustness in Multi-agent Networks* (European Control Conference, 2016), studies controllability-volume criteria, including an infinite-horizon Gramian projected onto the disagreement subspace, and reports a cycle leader example. Its continuous-time projected/pseudodeterminant objective is not the full-state discrete finite-horizon determinant here, and its general spectral expression does not state the proved horizon-independent exact tie classes or even-order comparison. The related joint-centrality theory optimizes noisy-leader robustness, a different objective.

Liu and Ji, *Controllability of Multiagent Systems Based on Path and Cycle Graphs* (first published June 30, 2017), is relevant to controllability ranks, but its accessible bibliographic material and abstract did not establish an all-horizon determinant classification; the unavailable complete comparison is an originality risk.

## Limitations
The result is confined to uniform unweighted undirected cycles, exactly two independent controls with identical gains, an affine Laplacian state matrix, and the full-state determinant. The exact formulas do not imply equality of individual Gramian eigenvalues, trace-inverse criteria, worst-case control energy, continuous-time objectives, unequal input gains, or arbitrary circulant couplings. The even-order comparison is non-strict in general; possible cross-parity ties are governed by \(\langle u,w\rangle=0\) and are not excluded. Independent literature-priority review and independent mathematical audit have not been performed.

## References
1. G. Parlangeli and G. Notarstefano, *On the Reachability and Observability of Path and Cycle Graphs*, arXiv:1109.3556v1 (2011-09-16); IEEE Transactions on Automatic Control 57 (2012), 743–748. https://arxiv.org/pdf/1109.3556
2. K. Fitch and N. E. Leonard, *Optimal Leader Selection for Controllability and Robustness in Multi-agent Networks*, European Control Conference (2016). https://naomi.princeton.edu/wp-content/uploads/sites/744/2021/03/Fitch_Leonard_ECC_16_final.pdf
3. S. Zhang, M. K. Camlibel, and M. Cao, *Controllability of Diffusively-Coupled Multi-Agent Systems with General and Distance Regular Coupling Topologies*, IEEE CDC-ECC (2011), 759–764. https://skoge.folk.ntnu.no/prost/proceedings/cdc-ecc-2011/data/papers/0872.pdf
4. X. Liu and Z. Ji, *Controllability of Multiagent Systems Based on Path and Cycle Graphs*, International Journal of Robust and Nonlinear Control 28 (2018), 296–309; first online 2017-06-30. https://doi.org/10.1002/rnc.3870
5. T. H. Summers, F. L. Cortesi, and J. Lygeros, *On Submodularity and Controllability in Complex Dynamical Networks*, arXiv:1404.7665 (2014).
