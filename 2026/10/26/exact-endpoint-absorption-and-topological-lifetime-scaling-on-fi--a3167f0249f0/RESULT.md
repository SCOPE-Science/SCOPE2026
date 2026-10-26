# Exact endpoint absorption and topological lifetime scaling on finite dimerized quantum chains

## Finding
For each integer \(m\ge1\), consider the \(2m\)-site open chain with consecutive positive hopping strengths \(a,b,a,b,\ldots,a\). An irreversible absorber of strength \(\gamma>0\) is placed at site \(1\), and the initial particle is at the opposite endpoint \(2m\). The exact integrated survival time is
\[
T_m(\gamma)=\frac{m}{\gamma}+\gamma B_m,\qquad
B_m=\frac{m-1}{b^2}+\frac{b^{2m-2}}{2a^{2m}}.
\]
There is complete eventual absorption for every finite \(m\). The unique positive minimizer and minimum are
\[
\gamma_*=\sqrt{\frac m{B_m}},\qquad T_m(\gamma_*)=2\sqrt{mB_m}.
\]
At fixed \(b>a\), the minimized time is asymptotic to \(\sqrt{2m}\,b^{m-1}/a^m\), whereas at fixed \(a>b\) it is asymptotic to \(2m/b\), and at \(a=b\) to \(2m/a\). Thus optimized remote-end capture is exponentially costly on the boundary-mode side of the dimerization transition, but only linearly costly on the other side.

## Assumptions and scope
Work in units with \(\hbar=1\). On the orthonormal site basis \(\{|j\rangle:1\le j\le2m\}\), define the real symmetric adjacency Hamiltonian
\[
H=\sum_{j=1}^{2m-1}t_j(|j\rangle\langle j+1|+|j+1\rangle\langle j|),\quad
 t_j=\begin{cases}a,&j\text{ odd},\\b,&j\text{ even}.\end{cases}
\]
Let \(K_\gamma=H-i\gamma|1\rangle\langle1|\). The claimed lifetime is \(T_m(\gamma)=\int_0^\infty\|e^{-itK_\gamma}|2m\rangle\|^2\,dt\), not the conditional mean given survival. The parameters \(a,b,\gamma\) are fixed positive reals for each finite chain; the large-\(m\) statements hold with \(a,b\) fixed and \(\gamma\) optimized separately for each \(m\). There is exactly one absorbing site and no environmental dephasing.

## Proof
**Decay and integrated Gramian.** Positive off-diagonal entries make \(H\) a real Jacobi matrix with simple spectrum, and every eigenvector has a nonzero first entry: otherwise the eigenvector recurrence annihilates every entry. Consequently \(-iH-\gamma|1\rangle\langle1|\) has strictly negative real-part spectrum. Indeed, any eigenvalue with zero real part would give a Hamiltonian eigenvector vanishing at site \(1\), a contradiction. The Hermitian integral Gramian \(Q_\gamma=\int_0^\infty e^{A_\gamma^\dagger t}e^{A_\gamma t}\,dt\), \(A_\gamma=-iH-\gamma|1\rangle\langle1|\), exists uniquely and solves \(A_\gamma^\dagger Q_\gamma+Q_\gamma A_\gamma=-I\).

**Exact affine-in-loss lemma.** More generally, let \(H\) be any real symmetric finite matrix with distinct eigenvalues \(E_j\) and a real unit absorber vector \(v\) having nonzero overlap \(v_j\) with every real normalized eigenvector. In this energy basis set \(w=Q_\gamma v\). The diagonal Lyapunov equations give \(\operatorname{Re}w_j=1/(2\gamma v_j)\). For \(j\ne k\), the remaining equation is
\[
i(E_j-E_k)(Q_\gamma)_{jk}=\gamma(v_j\overline{w_k}+w_jv_k).
\]
Writing \(w_j=1/(2\gamma v_j)+i\kappa_j\) shows
\[
\operatorname{Im}(Q_\gamma)_{jk}=-\frac{v_j/v_k+v_k/v_j}{2(E_j-E_k)},\quad
\kappa_j=-\frac12\sum_{k\ne j}\frac{v_j+v_k^2/v_j}{E_j-E_k}.
\]
Thus the imaginary parts and every \(\kappa_j\) are independent of \(\gamma\). The real off-diagonal entries are \(\gamma(\kappa_jv_k-v_j\kappa_k)/(E_j-E_k)\), and the real diagonal entries, obtained from \(\operatorname{Re}w_j=\sum_k\operatorname{Re}(Q_\gamma)_{jk}v_k\), are an explicit sum of a \(1/\gamma\) term and a \(\gamma\) term. Therefore, for any real initial vector \(c\),
\[
c^TQ_\gamma c=\frac{1}{2\gamma}\sum_j\frac{c_j^2}{v_j^2}+\gamma\,\mathcal B(c),
\]
for some \(\mathcal B(c)\) independent of \(\gamma\). The formula is exact at every positive \(\gamma\), including exceptional points of the lossy matrix, because it follows from the uniquely solvable Lyapunov equation.

**Weak-loss coefficient.** Reflection across the midpoint commutes with the even SSH Hamiltonian. Since its eigenvalues are simple, every normalized eigenvector has definite reflection parity; its endpoint amplitudes have equal squared magnitude. Taking \(c=|2m\rangle\) and \(v=|1\rangle\) in the affine lemma gives the exact coefficient \(\frac12\sum_{j=1}^{2m}c_j^2/v_j^2=m\).

**Strong-loss coefficient.** Delete the absorbing first site to obtain the \((2m-1)\)-site Hermitian chain \(H_\perp\), whose first coupling is \(b\) and last coupling is \(a\). Its spectrum is simple and the first reduced site is cyclic. A block Schur complement of \(A_\gamma\) shows that each slow eigenvalue associated with normalized \(H_\perp\)-eigenvector \(u_j\) has real part \(-a^2|u_j(2)|^2/\gamma+O(\gamma^{-2})\). The fast eigenmode has decay order \(\gamma\). Distinct real eigenenergies make cross terms in the time-integrated norm \(O(1)\) as \(\gamma\to\infty\), so the slow diagonal terms give
\[
\mathcal B(|2m\rangle)=\lim_{\gamma\to\infty}\frac{T_m(\gamma)}\gamma
=\frac{1}{2a^2}\sum_{j=1}^{2m-1}\frac{|u_j(2m)|^2}{|u_j(2)|^2}.
\]
This limit identifies the exact \(\gamma\) coefficient because of the affine lemma; no asymptotic remainder is inserted into the final lifetime identity.

Reorder the reduced chain into the \(m\) sites \(2,4,\ldots,2m\) and the \(m-1\) sites \(3,5,\ldots,2m-1\). Its off-diagonal block \(D\) has \(D_{j,j}=b\) and \(D_{j+1,j}=a\). The positive eigenvalues of \(D^TD\) are \(a^2+b^2+2ab\cos(\pi k/m)\), with sine eigenvectors indexed by \(1\le k\le m-1\); these are distinct. For each nonzero pair of \(H_\perp\)-eigenmodes, the end-site amplitude ratio has squared magnitude \(a^2/b^2\), since \((Dz)_1=bz_1\), \((Dz)_m=az_{m-1}\), and \(|z_{m-1}|=|z_1|\) for the sine modes. The unique zero mode satisfies \(b y_j+a y_{j+1}=0\), hence its squared endpoint ratio is \((b/a)^{2m-2}\). Therefore
\[
\sum_j\frac{|u_j(2m)|^2}{|u_j(2)|^2}
=2(m-1)\frac{a^2}{b^2}+\left(\frac ba\right)^{2m-2},
\]
and \(\mathcal B=(m-1)/b^2+b^{2m-2}/(2a^{2m})\), including \(m=1\) (only the zero mode). Substituting both exact coefficients yields the claimed lifetime.

**Optimization and scaling.** Since \(B_m>0\), differentiation of \(m/\gamma+\gamma B_m\) gives the unique global minimum stated above. For \(b>a\), the geometric term dominates; for \(a>b\), the \((m-1)/b^2\) term dominates; for \(a=b\), \(B_m=(m-1/2)/a^2\). These comparisons give the three asymptotic statements.

## Verification
Run `python verify_ssh.py` with the versions listed in `requirements.txt`. The self-contained script constructs the actual complex dissipative generator, solves its continuous Lyapunov equation independently, checks the matrix residual and compares the last diagonal Gramian entry with the formula for \(m=1,\ldots,10\) over four distinct dimerizations and three loss strengths. It additionally evaluates exact symbolic Lyapunov systems for \(m=1,2,3\), and independently checks the reflection-based weak-loss coefficient through real symmetric eigendecompositions. In the recorded run, all 276 checks passed; the worst relative numerical formula discrepancy was \(4.26\times10^{-10}\). Numerical tests are supplementary, not the proof for all \(m\).

## Relationship to prior work
Varbanov, Krovi, and Brun (2008) studied arrival times defined by measurements at random Poisson times, not by the present continuous rank-one imaginary absorber. Rudner and Levitov (2008) studied a bipartite periodic quantum walk with loss on an entire sublattice and derived topological mean displacement and a near-transition mean-decay-time expression, not this exact finite single-boundary-loss lifetime. Burke, Wiersig, and Haque (2019) analyzed scattering from a local imaginary impurity on an otherwise uniform tight-binding lattice, rather than the dimerized finite-chain time integral from the remote endpoint. Ivanov et al. (2023) investigated the macroscopic Zeno effect in coupled lossy SSH photonic arrays, measuring propagation and transmission; their loss geometry and observable differ from a single endpoint absorber. An unweighted path is recovered by setting \(a=b\), so the specifically dimerized geometric term and its sharp exponential-versus-linear optimized scaling are essential to the present statement. These comparisons do not establish exhaustive historical priority.

## Limitations
Only a real, finite, single-particle, two-periodic nearest-neighbor chain with one loss term is covered. No uniform-in-\(m\) perturbation theory is needed or asserted; the strong-loss expansion is used for each fixed finite \(m\) solely to identify an exact coefficient. No continuum, disorder, many-body, gain, time-dependent absorption, or finite-time distribution claim is made. The terms 'topological side' and 'dimerization transition' refer to the standard SSH boundary-mode regime, not a finite-system discontinuity.

## References
1. M. Varbanov, H. Krovi, T. A. Brun, *Hitting time for the continuous quantum walk*, arXiv:0803.3446 (first public 2008-03-24), https://arxiv.org/abs/0803.3446 .
2. M. S. Rudner and L. S. Levitov, *Topological Transition in a Non-Hermitian Quantum Walk*, arXiv:0807.2048 (first public 2008-07-13), https://arxiv.org/abs/0807.2048 .
3. P. C. Burke, J. Wiersig, M. Haque, *Non-Hermitian scattering on a tight-binding lattice*, arXiv:1910.07439 (first public 2019-10-16), https://arxiv.org/abs/1910.07439 .
4. Ivanov et al., *Macroscopic Zeno effect in Su–Schrieffer–Heeger photonic topological insulator*, arXiv:2308.00523 (first public 2023), https://arxiv.org/abs/2308.00523 .
