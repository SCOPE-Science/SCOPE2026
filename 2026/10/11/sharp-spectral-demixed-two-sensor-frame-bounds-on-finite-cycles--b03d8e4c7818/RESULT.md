# Sharp spectral-demixed two-sensor frame bounds on finite cycles

## Finding

Let \(N\ge5\) be an integer and \(1\le K<N/2\) an integer. Equip the undirected, unweighted cycle \(C_N\) with vertices \(\mathbb Z/N\mathbb Z\) and normalized Laplacian \(L=I-(T+T^{-1})/2\), where \((Tf)(x)=f(x+1)\). Set
\[
H_K=\operatorname{span}\{e_j:j=0,\pm1,\ldots,\pm K\},\qquad e_j(x)=N^{-1/2}e^{2\pi ijx/N}.
\]
Write \(P_0\) for the orthogonal projector onto \(\operatorname{span}\{e_0\}\), and \(P_k\) for the projector onto \(\operatorname{span}\{e_k,e_{-k}\}\) for \(1\le k\le K\). For an integer separation \(1\le s<N\), let the **spectrally demixed two-site sample** be
\[
\mathcal S_s f=\bigl((P_kf)(0),(P_kf)(s)\bigr)_{k=0}^{K},\qquad f\in H_K,
\]
with the standard Euclidean norm on its output. Its optimal lower and upper frame bounds are
\[
A_s=\frac2N(1-C_s),\qquad B_s=\frac2N(1+C_s),\qquad
C_s=\max_{1\le k\le K}\left|\cos\frac{2\pi ks}{N}\right|.
\]
The lower bound may vanish for some separations, in which case reconstruction is impossible from those two sites. Define
\[
g=\gcd(N,2),\qquad M=N/g,\qquad q=\left\lfloor\frac{M}{K+1}\right\rfloor.
\]
Then \(q\ge1\), and the **sharp global optimum over distinct sensor separations** is
\[
\boxed{\max_{1\le s<N}A_s=\frac2N\left(1-\cos\frac{\pi q}{M}\right)},\qquad
\boxed{\min_{1\le s<N}\frac{B_s}{A_s}=\cot^2\frac{\pi q}{2M}},
\]
where a vanishing denominator means an infinite frame condition number. Any separation satisfying
\[
\frac2g s\equiv q\pmod M
\]
is optimal. If \(K+1\mid M\), *all* optimal separations satisfy
\[
\frac2g s\equiv aq\pmod M,\qquad 1\le a\le K,\quad\gcd(a,K+1)=1,
\]
and their number in \(\{1,\ldots,N-1\}\) is exactly \(g\varphi(K+1)\). The exact finite-grid loss disappears precisely in this divisible case: the optimal angular separation is then \(1/(K+1)\), its continuous-circle ceiling.

## Assumptions and scope

All scalar functions and frame spaces are over \(\mathbb C\). The cutoff excludes the Nyquist eigenvalue when \(N\) is even, so each positive-frequency eigenvalue has multiplicity exactly two. The **demixed** norm uses the individual spectral outputs \(P_k f\) and is not the Euclidean norm of untreated time trajectories. The graph Fourier basis is orthonormal for counting measure on vertices. Two sites are necessary for any full recovery of \(H_K\) from powers of \(L\), since one site supplies at most one linear functional on each two-dimensional eigenspace.

## Proof

The Fourier vectors diagonalize \(L\), with eigenvalues
\[
\lambda_k=1-\cos(2\pi k/N),\qquad 0\le k\le K.
\]
Strict monotonicity of cosine on \([0,\pi)\) makes these \(K+1\) eigenvalues distinct. For \(k\ge1\), the restriction of the two-site map to \(\operatorname{span}\{e_k,e_{-k}\}\) is, in the ordered Fourier basis,
\[
N^{-1/2}\begin{pmatrix}1&1\\ e^{2\pi iks/N}&e^{-2\pi iks/N}\end{pmatrix}.
\]
Its Gram eigenvalues are \((2/N)(1\pm|\cos(2\pi ks/N)|)\); the one-dimensional constant-eigenvalue block has Gram eigenvalue \(2/N\). Orthogonality of the output blocks indexed by \(k\) therefore proves the asserted exact \(A_s,B_s\).

For a real number \(t\), write \(\|t\|_{\mathbb R/\mathbb Z}=\min_{m\in\mathbb Z}|t-m|\). If
\[
u_s\equiv(2/g)s\pmod M,\qquad
\delta_s=\min_{1\le k\le K}\|k u_s/M\|_{\mathbb R/\mathbb Z},
\]
then \(C_s=\cos(\pi\delta_s)\), since \(|\cos(\pi t)|=\cos(\pi\|t\|_{\mathbb R/\mathbb Z})\). The map \(s\mapsto u_s\) from \(\mathbb Z_N\) onto \(\mathbb Z_M\) is surjective, with fibers of cardinality \(g\): for odd \(N\) multiplication by two is invertible, and for even \(N\) the map is reduction modulo \(N/2\).

We prove the finite cyclic spacing identity
\[
\max_{u\in\mathbb Z_M}\min_{1\le k\le K}\|ku/M\|_{\mathbb R/\mathbb Z}=\frac{q}{M}.
\]
For every \(u\), place the \(K+1\) residues \(0,u,\ldots,Ku\) on the circle of circumference \(M\). If any two coincide, the displayed minimum is zero. Otherwise, their \(K+1\) cyclic neighbor gaps sum to \(M\), so some gap is at most \(\lfloor M/(K+1)\rfloor=q\). Its endpoints differ by \(ku\) for a nonzero index difference \(k\) of absolute value at most \(K\), giving the upper bound. Conversely choose \(u=q\); then \(q\le kq\le Kq\le M-q\) for every \(1\le k\le K\), hence every circular distance is at least \(q\), with equality for \(k=1\). This proves the exact optimum and the given maximizing separation.

As \(\cos(\pi t)\) decreases strictly for \(0\le t\le1/2\), maximizing the minimum angular separation simultaneously maximizes \(A_s\) and minimizes \(B_s/A_s\). The identity \((1+\cos\theta)/(1-\cos\theta)=\cot^2(\theta/2)\) yields the asserted sharp values.

Suppose \(M=(K+1)q\), and a residue \(u\) attains the optimum. The \(K+1\) distinct points \(0,u,\ldots,Ku\) must have every cyclic gap at least \(q\); their total length is exactly \((K+1)q\), so all gaps equal \(q\). Therefore these points form \(q\mathbb Z_M\), and \(u=aq\) is a generator of this cyclic subgroup of order \(K+1\), equivalently \(\gcd(a,K+1)=1\). Every such generator attains the bound, yielding exactly \(g\varphi(K+1)\) nonzero sensor offsets by the fiber count. If \(K+1\nmid M\), then \(q/M<1/(K+1)\), giving strict lattice loss.

Finally, for either sampled vertex \(x\),
\[
(L^t f)(x)=\sum_{k=0}^{K}\lambda_k^t(P_k f)(x),\qquad 0\le t\le K.
\]
The matrix \((\lambda_k^t)_{0\le t,k\le K}\) is a square Vandermonde matrix with nonzero determinant \(\prod_{i<j}(\lambda_j-\lambda_i)\). Hence raw trajectory data at the two sites and \(K+1\) times recover exactly the demixed samples, and an optimizing pair recovers all \(2K+1\) Fourier coefficients. With only \(K\) times there are at most \(2K<2K+1\) scalar measurements, so \(K+1\) times are also necessary for two sensors under this simultaneous time-sampling protocol.

## Verification

An accompanying dependency-free Python program (`verify.py`) checks the finite cyclic spacing identity for every \(5\le N\le120\) and every permitted cutoff, directly compares all two-site angular expressions, verifies the equality-class cardinality when \(K+1\mid M\), and separately diagonalizes the two-by-two Fourier Gram blocks numerically. These are cross-checks of a proof valid for all integers \(N,K\), not a replacement for the global pigeonhole argument.

## Relationship to prior work

Bulai, Cabrelli, Cordero, Molter and Saliani (2026) develop the graph Paley–Wiener dynamical sampling framework and discuss finite-graph frames, with a path graph as their numerical model. Yang, Yang and Huang (2021) give general graph sampling and node-selection methods and numerical ring-graph experiments. Aldroubi and collaborators (2024) study space–time recovery conditions and noisy node selection. These results motivate the two-sensor spectral frame optimization but the materially inspected text of Yang–Yang–Huang does not calculate the displayed sharp all-parameter cycle constants or the totient rigidity of optimum placements. The finite cyclic spacing principle and Fourier block-diagonalization used in the proof are elementary known techniques; novelty is claimed only for their sharp combined spectral-demixed two-sensor frame classification. A complete text comparison with the 2026 preprint could not be completed, so possible overlap beyond its abstract remains a literature risk.

## Limitations

The constants are for exactly the \(2K+1\)-dimensional low-pass space and the **spectrally demixed** output norm. Vandermonde demixing is invertible, but may amplify noise; the theorem does not optimize the condition number of the original unweighted time-trajectory observation matrix. It does not address irregular graphs, more than two sensors, arbitrary spectral subsets, or non-Laplacian evolution. No independent verification or literature certification is asserted.

## References

- I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter, S. Saliani, *Dynamical Sampling in Graph Paley–Wiener Spaces*, arXiv:2609.25472, first submitted 21 September 2026; https://arxiv.org/abs/2609.25472.
- G. Yang, L. Yang, C. Huang, *An Orthogonal Partition Selection Strategy for the Sampling of Graph Signals with Successive Local Aggregations*, Signal Processing **188** (2021), 108211; DOI:10.1016/j.sigpro.2021.108211.
- A. Aldroubi, V. Bailey, I. A. Krishtal, B. Miller, A. Petrosyan, *Reconstructing Graph Signals from Noisy Dynamical Samples*, arXiv:2411.12670; https://arxiv.org/abs/2411.12670.
