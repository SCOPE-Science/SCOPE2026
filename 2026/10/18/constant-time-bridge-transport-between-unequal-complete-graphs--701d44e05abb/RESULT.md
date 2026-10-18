# Constant-time bridge transport between unequal complete graphs

## Finding
Let \(p,q\ge2\) be integers and \(w>0\). Connect a distinguished vertex \(a\) of the unweighted complete graph \(K_p\) to a distinguished vertex \(b\) of the disjoint complete graph \(K_q\) by a single edge of weight \(w\); leave all other edge weights equal to one. Let \(H_{p,q}(w)\) be its zero-diagonal, real symmetric weighted adjacency Hamiltonian and put \(U_{p,q}(t)=\exp(-\mathrm{i}tH_{p,q}(w))\).

Write \(m=\min\{p,q\}\), \(\alpha_r=\sqrt{1-r^{-1}}\), and \(T_w=\pi/(2w)\). For every fixed \(w>0\) and \(T>0\), uniformly for real \(|t|\le T\) as \(m\to\infty\),
\[
\langle b|U_{p,q}(t)|a\rangle=-\mathrm{i}e^{\mathrm{i}t}\alpha_p\alpha_q\sin(w\alpha_p\alpha_q t)+O_{w,T}(m^{-2}).
\]
In particular,
\[
\left|\langle b|U_{p,q}(T_w)|a\rangle\right|^2
=1-\frac1p-\frac1q+O_w(m^{-2}).
\]
The limit requires only \(\min\{p,q\}\to\infty\), not convergence of the clique-size ratio. Hence the probability of transfer at the *fixed* time \(T_w\) tends to one despite the single-edge bottleneck. For any fixed \(p\ne q\), however, the two bridge endpoints do not have pretty good state transfer at any sequence of times: their squared-Hamiltonian diagonal moments differ by \(p-q\).

## Assumptions and scope
The model is a single-excitation coherent continuous-time quantum walk, with no search oracle, sink, onsite potential, or dephasing. The bridge weight \(w\) is fixed and positive independently of \(p,q\); the error bounds are not claimed uniformly as \(w\to0\), \(w\to\infty\), or observation time diverges. The clique sizes are arbitrary and need not be equal. The fixed-time sharp asymptotic is distinct from optimizing over times for a fixed finite graph.

## Proof
**Exact invariant reduction.** In each clique of order \(r\), define \(|u_r\rangle=r^{-1/2}\sum_{x\in K_r}|x\rangle\), and let \(|v_r\rangle\) be the unit vector proportional to the distinguished vertex minus the uniform superposition, fixed by the convention \(\langle a_r|v_r\rangle=\alpha_r>0\). Explicitly \(|v_r\rangle=\alpha_r|a_r\rangle-(r(r-1))^{-1/2}\sum_{x\ne a_r}|x\rangle\). The adjacency of \(K_r\) gives eigenvalues \(-1\) on \(|v_r\rangle\) and \(r-1\) on \(|u_r\rangle\). The source and target belong to the four-dimensional invariant subspace spanned by \(|v_p\rangle,|v_q\rangle,|u_p\rangle,|u_q\rangle\); all other clique contrasts are orthogonal to them and cannot contribute to the transition amplitude.

In this ordered basis the exact Hamiltonian is
\[
\begin{pmatrix}K&B\\ B^{\mathsf T}&D\end{pmatrix},\quad
K=\begin{pmatrix}-1&w\alpha_p\alpha_q\\w\alpha_p\alpha_q&-1\end{pmatrix},\quad
B=\begin{pmatrix}0&w\alpha_p/\sqrt q\\w\alpha_q/\sqrt p&0\end{pmatrix},\quad
D=\begin{pmatrix}p-1&w/\sqrt{pq}\\w/\sqrt{pq}&q-1\end{pmatrix}.
\]
The source decomposes as \(|a\rangle=\alpha_p|v_p\rangle+p^{-1/2}|u_p\rangle\), and the target analogously as \(|b\rangle=\alpha_q|v_q\rangle+q^{-1/2}|u_q\rangle\).

**Uniform low-energy estimate.** Fix \(w>0\), and take \(m\) sufficiently large depending only on \(w\). The two eigenvalues of \(K\) are \(\kappa_\pm=-1\pm w\alpha_p\alpha_q\), separated by at least \(w\); both are a distance \(\Omega_w(m)\) below the spectrum of \(D\). Also \(\|B\|=O_w(m^{-1/2})\). Weyl's inequalities show that the full matrix has two eigenvalues near those of \(K\) and two near those of \(D\). For either low eigenvalue \(\lambda\), decompose a corresponding eigenvector into low and high components \((x,y)\). The high equation gives
\[
y=-(D-\lambda I)^{-1}B^{\mathsf T}x,
\qquad \|y\|=O_w(m^{-3/2})\|x\|.
\]
Substitution gives \((K-B(D-\lambda I)^{-1}B^{\mathsf T})x=\lambda x\). The correction has norm \(O_w(m^{-2})\), so the two low eigenvalues differ from \(\kappa_\pm\) by \(O_w(m^{-2})\); their normalized low components differ from the corresponding normalized eigenvectors \((1,\pm1)/\sqrt2\) of \(K\) by \(O_w(m^{-2})\). To see the last assertion, project the perturbed eigenvalue equation onto the *other* eigenvector of \(K\) and divide by its nonzero eigenvalue gap; normalization contributes only \(O_w(m^{-3})\). Orthogonality shows each high eigenvector has low-component norm \(O_w(m^{-3/2})\). Therefore, for every bounded \(|t|\le T\), the low-low propagator block differs from \(e^{-itK}\) by \(O_{w,T}(m^{-2})\), and each low-high propagator block has norm \(O_w(m^{-3/2})\).

**High-high contribution.** Write the full matrix as \((K\oplus D)+\left(\begin{smallmatrix}0&B\\B^{\mathsf T}&0\end{smallmatrix}\right)\). Twice applying Duhamel's formula, using that a single off-diagonal coupling cannot return to the high sector, gives a high-high block difference from \(e^{-itD}\) of norm at most \(t^2\|B\|^2/2=O_{w,T}(m^{-1})\). Another application of Duhamel's formula to \(D=\operatorname{diag}(p-1,q-1)+(w/\sqrt{pq})\sigma_x\) gives \(|\langle u_q|e^{-itD}|u_p\rangle|\le |t|w/\sqrt{pq}\). Multiplying by the two endpoint coefficients \(1/\sqrt p\) and \(1/\sqrt q\) makes the full high-high contribution \(O_{w,T}(m^{-2})\). Each mixed low-high contribution is also \(O_{w,T}(m^{-2})\), since it includes a factor at most \(m^{-1/2}\).

Combining the four terms, and using
\[
\langle v_q|e^{-itK}|v_p\rangle=-\mathrm{i}e^{\mathrm{i}t}\sin(w\alpha_p\alpha_q t),
\]
proves the uniform amplitude formula. At \(t=T_w\), \(\alpha_p\alpha_q=1-\frac1{2p}-\frac1{2q}+O(m^{-2})\), hence \(\sin(\pi\alpha_p\alpha_q/2)=1+O(m^{-2})\). Squaring the modulus gives \(\alpha_p^2\alpha_q^2+O_w(m^{-2})=1-p^{-1}-q^{-1}+O_w(m^{-2})\).

**Unequal finite cliques.** If arbitrarily good transfer from \(a\) to \(b\) occurred, there would be times \(t_j\) and phases \(\gamma_j\) with \(U(t_j)|a\rangle-\gamma_j|b\rangle\to0\). Because \(H\) commutes with \(U(t_j)\), taking expectations of \(H^2\) and passing to the limit forces \(\langle a|H^2|a\rangle=\langle b|H^2|b\rangle\). But these numbers are \(p-1+w^2\) and \(q-1+w^2\), respectively. They differ when \(p\ne q\), a contradiction.

## Verification
Run `python verify_bridge_transfer.py` with NumPy and SciPy. The script independently constructs full weighted adjacency matrices and four-dimensional reductions, verifies the orthogonal low/high block form, compares full-graph and reduced propagators at multiple times, and evaluates the asymptotic leading coefficient over both balanced and unbalanced size sequences. The supplied run completed 108 checks. These finite calculations corroborate the algebra and cannot prove the asymptotic or all-size statements; their proof is above.

## Relationship to prior work
Coutinho, Godsil, Juliano, and van Bommel prove nonexistence of *perfect* transfer between adjacent cut vertices with nontrivial attached graphs (arXiv:2112.03374v1, Theorem 13). Ackelsberg, Brehm, Chan, Mundinger, and Tamon prove *pretty good* transfer between the two distinguished vertices of the equal-clique corona \(K_2\circ K_r\) (arXiv:1605.05260; EJC 24(2), 2017, Theorem 5.3). Neither is a uniform constant-time limit for unequal cliques with the explicit sharp leading infidelity \(p^{-1}+q^{-1}\). Razzoli, Paris, and Bordone analyze a different sink-based transport efficiency on equal-clique bridges (arXiv:2011.13794, Section 4.3). Duda and Wong analyze a marked-vertex quantum-search Hamiltonian, not the oracle-free bridge-to-bridge propagator (arXiv:2408.08244, Sections II–V). The new statement concerns fixed-time, oracle-free transfer in arbitrarily unbalanced cliques; it does not claim discovery of barbell pretty-good transfer or absence of perfect transfer.

## Limitations
The error constant depends on the fixed hopping \(w\) and bounded observation-time interval. No finite-size all-time optimal fidelity, minimum transfer time, or joint limit with \(w\) scaling with clique size is determined. For \(p=q\), known pretty-good transfer at some arbitrarily late times is compatible with the fixed-time asymptotic. The argument does not extend without new analysis to Laplacian generators, onsite disorder, open-system absorption, or multipartite assemblies. Priority risk remains for an equivalent fixed-time asymptotic hidden under alternative graph-transfer terminology.

## References
- G. Coutinho, C. Godsil, E. Juliano, and C. M. van Bommel, *Quantum walks do not like bridges*, arXiv:2112.03374v1, first public 2021-12-06, especially Theorem 13 and Section 6, https://arxiv.org/abs/2112.03374.
- E. Ackelsberg, Z. Brehm, A. Chan, J. Mundinger, and C. Tamon, *Quantum State Transfer in Coronas*, Electron. J. Combin. 24(2), P2.24 (2017), Theorem 5.3; preprint arXiv:1605.05260, https://arxiv.org/abs/1605.05260.
- L. Razzoli, M. G. A. Paris, and P. Bordone, *Transport efficiency of continuous-time quantum walks on graphs*, arXiv:2011.13794, Section 4.3, https://arxiv.org/abs/2011.13794.
- J. Duda and T. G. Wong, *Searching Weighted Barbell Graphs with Laplacian and Adjacency Quantum Walks*, arXiv:2408.08244, https://arxiv.org/abs/2408.08244.
