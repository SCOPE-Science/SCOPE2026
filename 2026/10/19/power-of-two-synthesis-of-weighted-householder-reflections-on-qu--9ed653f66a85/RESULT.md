# Power-of-two synthesis of weighted Householder reflections on quantum spiders

## Finding

For each integer \(k\ge3\), positive integer \(L\), and positive edge weights \(w_1,\dots,w_k\), form a spider graph with a common hub and \(k\) arms, each of length \(L\), with every edge on arm \(i\) of weight \(w_i\). Let \(H=I-D^{-1/2}AD^{-1/2}\) be its weighted normalized Laplacian and \(U(t)=e^{-itH}\). Put \(W=\sum_iw_i\) and \(v=(\sqrt{w_1/W},\dots,\sqrt{w_k/W})^T\). Define \(R\) to fix the hub and to act independently on every arm-depth layer as the weighted Householder matrix \(2vv^T-I_k\).

**Theorem (one claim, with its exact dynamical consequences).** For every real \(t\),
\[
\boxed{\|U(t)-R\|_{\mathrm{op}}=\big\|e^{-it\mathcal L(P_{2L+1})}-J_{2L+1}\big\|_{\mathrm{op}},}
\]
where \(\mathcal L(P_{2L+1})\) is the usual normalized Laplacian of the unweighted path and \(J_{2L+1}\) reverses that path. Therefore there exist positive times \(t_n\to\infty\) with \(U(t_n)\to R\) in operator norm **if and only if** \(L\) is a power of two. Exact equality \(U(t)=R\) is possible for a positive time **if and only if** \(L=1\); then \(t=\pi\) works.

For distinct arms \(i\ne j\), writing \(|i,L\rangle\) for the terminal vertex of arm \(i\), there is also an **all-time amplitude identity**
\[
\boxed{\langle j,L|U(t)|i,L\rangle=\frac{2\sqrt{w_iw_j}}{W}\,\langle 2L+1|e^{-it\mathcal L(P_{2L+1})}|1\rangle.}
\]
In particular, \(\Pr_{i\to j}(t)\le4w_iw_j/W^2\) for every \(t\), and the *supremum over real times* equals this upper bound exactly when \(L\) is a power of two. It is attained at finite time only when \(L=1\).

## Assumptions and scope

The underlying Hilbert space has the orthonormal basis consisting of a hub \(|h\rangle\) and vertices \(|i,d\rangle\) indexed by \(1\le i\le k\) and \(1\le d\le L\). The adjacency matrix is real symmetric with \(A_{h,(i,1)}=w_i\), \(A_{(i,d),(i,d+1)}=w_i\) for \(1\le d<L\), and all other off-diagonal entries zero. The diagonal weighted degree is \(D_{xx}=\sum_yA_{xy}\). Edge weights may be arbitrary positive real numbers, with no commensurability or equality assumption between arms; only weights within each individual arm are constant. The time parameter is real, and positive times are used for the recurrence statements. No many-particle, dissipative, noisy, or scattering dynamics is asserted.

## Proof

**1. An exact orthogonal splitting.** Let \(v_i=\sqrt{w_i/W}\), so \(\sum_i v_i^2=1\). For each depth \(1\le d\le L\), let \(|v,d\rangle=\sum_i v_i|i,d\rangle\). The span of \(|h\rangle,|v,1\rangle,\ldots,|v,L\rangle\) is invariant under \(H\). In the ordered basis \((|h\rangle,|v,1\rangle,\ldots,|v,L\rangle)\), its matrix is precisely \(\mathcal L(P_{L+1})\): the endpoint-to-interior normalized couplings are \(-1/\sqrt2\), the interior couplings are \(-1/2\), and the one-edge case has coupling \(-1\). This follows directly by substituting degrees \(D_h=W\), \(D_{(i,d)}=2w_i\) for \(1\le d<L\), and \(D_{(i,L)}=w_i\) into the definition. The orthogonal complement consists of \(k-1\) copies of a fixed \(L\)-site Jacobi matrix \(T_-\): its diagonal is \(1\), and its successive off-diagonal entries are \(-1/2\) in the interior and \(-1/\sqrt2\) at the terminal edge (with the obvious one-site case). Thus
\[
 H\simeq H_+\oplus\bigl(I_{k-1}\otimes T_-\bigr),\qquad H_+=\mathcal L(P_{L+1}).
\]
The reflection \(R\) acts as \(+I\) on the \(H_+\) sector and as \(-I\) on each \(T_-\) sector.

**2. The doubled-path correspondence.** The reflection \(J_{2L+1}\) of the unweighted path \(P_{2L+1}\) has an even sector of dimension \(L+1\) and an odd sector of dimension \(L\). The normalized-path operator on the even sector, in the natural folded basis, is \(H_+\); on the odd sector it is \(T_-\). The reflection acts as \(+I\) and \(-I\), respectively. Consequently
\[
\begin{aligned}
 \|U(t)-R\|_{\mathrm{op}}
 &=\max\{\|e^{-itH_+}-I\|_{\mathrm{op}},\|e^{-itT_-}+I\|_{\mathrm{op}}\}\\
 &=\|e^{-it\mathcal L(P_{2L+1})}-J_{2L+1}\|_{\mathrm{op}}.
\end{aligned}
\]
This identity holds for *every time and every positive weight vector*. In particular, the number of arms and their strengths do not affect the approximation error in operator norm.

**3. Why end-to-end path transfer decides global reflection.** The normalized Laplacian of a path is an irreducible symmetric tridiagonal matrix: every normalized eigenvector has a nonzero endpoint entry, and its eigenvalues are simple. Its eigenvectors have definite reflection parity. If \(\big|\langle 2L+1|e^{-itH_P}|1\rangle\big|\to1\) along times, the finitely many eigenphases in the endpoint spectral expansion must tend to a common reflected phase. The normalized zero eigenvector has positive endpoint entries and eigenvalue zero, forcing that common phase to be \(+1\). Since the endpoint sees *every* eigenvalue, all eigenphases converge to the appropriate reflection parity signs. Thus end-to-end pretty good state transfer is equivalent to \(\|e^{-itH_P}-J\|_{\mathrm{op}}\to0\) along a sequence. Conversely, operator-norm convergence immediately implies endpoint transfer.

The normalized-Laplacian path theorem recorded by Coutinho and Baptista gives end-to-end pretty good state transfer on \(P_n\) exactly for \(n=2^a+1\), \(a\ge0\) [1,2]. Substituting \(n=2L+1\) proves the power-of-two criterion. Since arbitrarily accurate approximations occur on a compact finite-dimensional unitary torus, the approximating times may be chosen unbounded, and when exact transfer is impossible they must be unbounded. Exact end-to-end transfer under the normalized Laplacian occurs only for the paths with two or three vertices [2,3]. As \(2L+1\ge3\), exact reflection is possible only for \(L=1\); direct diagonalization of \(P_3\) yields \(e^{-i\pi\mathcal L(P_3)}=J_3\), so \(U(\pi)=R\).

**4. Exact channel amplitudes and sharpness.** At depth \(L\), decompose the channel vector \(e_i=v_i v+(e_i-v_iv)\). The symmetric-sector terminal return amplitude is \(a(t)\), and the antisymmetric-sector terminal return amplitude is \(b(t)\). For distinct \(i,j\), orthogonality gives \(\langle j,L|U(t)|i,L\rangle=v_iv_j(a(t)-b(t))\). The normalized path's symmetric and antisymmetric terminal projections have equal squared norm \(1/2\), hence its end-to-end amplitude is \((a(t)-b(t))/2\), proving the identity. The inequality follows from unitarity of the path propagator. If the supremum attained the bound, a sequence of times would exhibit path pretty good transfer; conversely, pretty good transfer attains the supremum as a limit. The characterization and the finite-time conclusion follow from Step 3.

## Verification

The accompanying self-contained `VERIFY.py` independently builds each weighted graph and the corresponding normalized path from their edge lists, diagonalizes both real-symmetric Hamiltonians, and compares (a) the all-time operator-norm identity and (b) terminal cross-arm amplitudes. It checks multiple lengths, positive weight configurations, arm counts, and times, including the exact \(L=1\), \(t=\pi\) gate and an improving sequence for \(L=2\). The general all-length theorem relies on Steps 1–4 and the cited published path-transfer classification, **not** on numerical sampling. Run using `python VERIFY.py` with NumPy installed.

## Relationship to prior work

Coutinho and Baptista [2], building on earlier normalized-Laplacian transfer theory and a result in their reference [19], explicitly report the end-to-end pretty-good-transfer classification for unweighted paths. Alvir and collaborators [3] establish the absence of normalized-Laplacian perfect end-to-end transfer for paths on at least four vertices. These path results are inputs, not claimed as new here. The novel candidate is the **all-time exact intertwining** from an arbitrary-weight finite spider to the reversal of one path, including the full operator-norm equality, coherent multiport Householder synthesis, and sharp weighted cross-channel supremum. Earlier adjacency-Hamiltonian pretty-good transfer results for graphs assembled from stars [4] use a different Hamiltonian and state-transfer geometry. Symmetric scattering on metric stars can also produce Householder-type matrices; that different time-continuous scattering framework does not itself establish this finite normalized-Laplacian evolution statement.

## Limitations

The edge strength is constant *along* each arm, though the arms can have different weights. The spider has equal arm lengths. The statement concerns a finite, single-particle unitary \(e^{-itH}\) and does not imply robustness under loss, off-model detuning, noise, or changes to the Hamiltonian normalization. For \(L\ge2\) the gate is approximate only; the theorem supplies no quantitative minimum time for a desired error. The power-of-two classification relies on the previously established normalized-path pretty-good-transfer theorem. The exact factorization makes the result mathematically checkable but is not an independent proof of novelty against all possible equivalent representations in the broader graph-transport literature.

## References

[1] P. V. F. Baptista, *Pretty Good State Transfer*, Universidade Federal de Minas Gerais thesis (2021), repository record https://repositorio.ufmg.br/handle/1843/43127 (repository date 2021-11-10; full document not independently retrieved here).

[2] G. Coutinho and P. F. Baptista, *Quantum Walks in the Normalized Laplacian*, arXiv:2209.04668v1 (2022-09-10), https://arxiv.org/html/2209.04668v1, especially Section 5 and the transfer criteria of Section 3.

[3] R. Alvir, S. Dever, B. Lovitz, J. Myer, C. Tamon, Y. Xu, and H. Zhan, *Perfect State Transfer in Laplacian Quantum Walk*, arXiv:1409.5840v1 (2014-09-20), https://arxiv.org/html/1409.5840v1, Section 6.2.

[4] H. Hou, R. Gu, and M. Tong, *Pretty good state transfer on 1-sum of star graphs*, Open Mathematics 16 (2018), 1483–1489, https://doi.org/10.1515/math-2018-0119.
