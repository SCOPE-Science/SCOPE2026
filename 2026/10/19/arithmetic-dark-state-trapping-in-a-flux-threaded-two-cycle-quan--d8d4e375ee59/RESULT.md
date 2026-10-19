# Arithmetic dark-state trapping in a flux-threaded two-cycle quantum network

## Finding
Let two finite simple cycles of lengths \(m,n\ge3\) share exactly one vertex \(o\), with all hopping moduli equal and loss supported only at \(o\). In contrast to two independently lossy, nonzero-flux rings, their coupled network can retain coherent trapped states. If neither total cycle flux belongs to \(\pi\mathbb Z\), the number of linearly independent nondecaying modes equals \(\gcd(m,n)-1\). Site-selective complete absorption is characterized exactly by divisibility of the distance from the hub by this gcd.

For the particularly natural quadrature-flux choice \(\phi_m,\phi_n\equiv\pi/2\pmod\pi\), every other non-hub vertex has precisely the same asymptotic survival probability:
\[
\lim_{t\to\infty}\|e^{-itK}|i,j\rangle\|^2
=\begin{cases}
0,&\gcd(m,n)\mid j,\\[2pt]
\dfrac{\gcd(m,n)}{m+n},&\gcd(m,n)\nmid j.
\end{cases}
\]
This plateau is exact for every positive hopping magnitude and absorption rate; it is not a large-system or weak-loss approximation. For example, cycles of lengths \(6\) and \(9\) have a two-dimensional dark subspace, the surviving non-hub sites have probability \(1/5\), and sites at distances divisible by \(3\) are completely absorbed.

## Assumptions and scope
The vertex set consists of one common hub \(o\) and two disjoint path interiors \((i,j)\), with \(i\in\{m,n\}\) and \(1\le j\le i-1\). Within each cycle the path edges \((i,j)\leftrightarrow(i,j+1)\) have matrix entry \(J>0\), as does the edge between the hub and \((i,1)\). The closing edge has \(H_{o,(i,i-1)}=J e^{i\phi_i}\) and conjugate reverse entry, defining the oriented gauge flux \(\phi_i\). All onsite potentials vanish. For \(\gamma>0\), take
\[K=H-\frac{i\gamma}{2}|o\rangle\langle o|.\]
The no-click evolution of a normalized basis state \(|i,j\rangle\) is \(e^{-itK}|i,j\rangle\), and its squared norm is the probability of no absorption by time \(t\). Throughout, \(\phi_m,\phi_n\notin\pi\mathbb Z\). Denote \(g=\gcd(m,n)\).

For each integer \(1\le r<g\), set
\[
A_r=\frac{|1-(-1)^{mr/g}e^{i\phi_m}|^2}{m},\qquad
B_r=\frac{|1-(-1)^{nr/g}e^{i\phi_n}|^2}{n}.
\]
The complete general-flux result, before specializing to quadrature flux, is
\[
S_{m,j}=\frac{2}{m}\sum_{r=1}^{g-1}
\frac{B_r}{A_r+B_r}\sin^2\!\left(\frac{\pi rj}{g}\right),\qquad
S_{n,j}=\frac{2}{n}\sum_{r=1}^{g-1}
\frac{A_r}{A_r+B_r}\sin^2\!\left(\frac{\pi rj}{g}\right).
\]
Here \(S_{i,j}=\lim_{t\to\infty}\|e^{-itK}|i,j\rangle\|^2\). Empty sums vanish when \(g=1\).

## Proof
**1. Nondecaying vectors are precisely real-energy hub-dark eigenvectors.** For every eigenpair \(Kv=\lambda v\), taking the imaginary part of \(\langle v,Kv\rangle\) gives
\[\operatorname{Im}\lambda\,\|v\|^2=-\frac\gamma2|v_o|^2.\]
Thus \(\operatorname{Im}\lambda\le0\), and equality forces \(v_o=0\) and \(Hv=\lambda v\). Conversely, such an eigenvector is undamped. Their span is reducing for both \(H\) and \(K\), since the hub loss annihilates it. Every eigenvalue of the restriction to the orthogonal complement has strictly negative imaginary part. Its finite-dimensional propagator tends to zero, even if a decaying eigenvalue has a Jordan block. Consequently the infinite-time norm is the squared norm of the orthogonal projection onto the hub-dark eigenspace.

**2. Two Dirichlet paths and one constraint.** Deleting the hub leaves disjoint unweighted paths with \(m-1\) and \(n-1\) vertices. The first has the simple eigenvalues \(2J\cos(\pi k/m)\), \(1\le k<m\), and normalized eigenvector \(u_{m,k}(j)=\sqrt{2/m}\sin(\pi kj/m)\); similarly for the second. Since cosine is strictly decreasing on \((0,\pi)\), common eigenvalues occur exactly when \(k/m=\ell/n=r/g\), where \(1\le r<g\). If an eigenvalue belongs to only one path, the hub boundary equation is its nonzero boundary amplitude multiplied by \(1-(-1)^k e^{i\phi_i}\), which cannot vanish under the flux assumptions. Thus such a path eigenvalue contributes no dark state.

For a common eigenvalue, write \(k=mr/g\), \(\ell=nr/g\), and let \(u_r,v_r\) denote the corresponding normalized eigenvectors supported on the first and second paths, respectively. Their couplings to the hub are
\[
 c_{m,r}=J\sqrt{2/m}\sin(\pi r/g)\bigl(1-(-1)^k e^{i\phi_m}\bigr),
\quad
 c_{n,r}=J\sqrt{2/n}\sin(\pi r/g)\bigl(1-(-1)^\ell e^{i\phi_n}\bigr).
\]
Both are nonzero. The entire dark eigenspace at that energy is spanned by
\[
 d_r=\frac{c_{n,r}u_r-c_{m,r}v_r}
{\sqrt{|c_{m,r}|^2+|c_{n,r}|^2}}.
\]
These \(g-1\) vectors are orthonormal because distinct \(r\) have distinct Hermitian eigenvalues. There are no other dark vectors, proving the dimension formula.

**3. Exact site survival and site-selective absorption.** The orthogonal dark projection is \(P_D=\sum_{r=1}^{g-1}|d_r\rangle\langle d_r|\). Taking its diagonal entry at each basis site, and canceling the common positive factor \(2J^2\sin^2(\pi r/g)\) in the coupling ratios, gives precisely the two finite sums displayed under Assumptions and scope. Under the nonintegral-\(\pi\) flux assumptions each ratio is strictly positive. If \(g\mid j\), every sine factor vanishes. If \(g\nmid j\), already the term \(r=1\) is positive. Hence \(S_{i,j}=0\) exactly at the stated divisible distances. Since the total absorption probability equals \(1-S_{i,j}\), the perfect-absorption criterion follows.

**4. Uniform quadrature-flux plateau.** If both fluxes are \(\pi/2\) modulo \(\pi\), then each squared boundary factor equals \(2\), regardless of the parity of \(k\) or \(\ell\). Thus \(A_r=2/m\), \(B_r=2/n\), and the ratios are respectively \(m/(m+n)\) and \(n/(m+n)\). The elementary root-of-unity identity
\[
\sum_{r=1}^{g-1}\sin^2(\pi rj/g)=
\begin{cases}0,&g\mid j,\\ g/2,&g\nmid j,\end{cases}
\]
now yields the common value \(g/(m+n)\) at every nondivisible site. No asymptotic approximation enters.

## Verification
A standalone `verify.py` uses only NumPy. It independently constructs the Hermitian adjacency matrix (including complex closing edges), computes the derived orthonormal dark vectors, checks their eigenvalue equations, and checks sitewise diagonal dark-projection weights against the general formula and the quadrature plateau. On lengths \(3\) through \(15\) for both cycles and four phase pairs, it compares \(10,816\) vertex probabilities, with maximum absolute residual below \(5\times10^{-15}\). Separate finite loss-matrix calculations for six graph sizes confirm the expected count of real eigenvalues. Run `python verify.py` with NumPy installed. Finite checks support, but do not substitute for, the proof for all lengths and fluxes.

## Relationship to prior work
Lorz and collaborators' photonic figure-eight quantum walk uses a discrete-time coined walk with four-dimensional coins, not the present continuous-time Hamiltonian with one absorbing common vertex and two Peierls phases [1]. Segawa, Koyama, Konno and Štefaňák study survival and trapped components in discrete-time Grover walks on a ladder, with different geometry, spectrum, and dynamics [2]. Finocchiaro and collaborators analyze local monitoring in a *single* flux-threaded ring, using stroboscopic projective measurements rather than continuous single-site loss [3]. Those papers motivate the combination of cyclic interference and survival, but none of their stated mechanisms yields this two-cycle gcd classification or the site-independent quadrature-flux plateau. No assertion is made that the underlying Dirichlet path spectrum is new.

## Limitations
The exact formula assumes equal positive hopping magnitudes, zero onsite energies, exactly two cycles meeting only at the lossy hub, and fluxes outside \(\pi\mathbb Z\). The excluded zero-/half-turn-flux cases can have additional single-cycle dark modes and are not covered by these formulas. Results concern long-time no-jump single-particle survival; no convergence rate, multi-particle extension, or robustness to disorder is asserted. The statement-level literature comparison does not establish independent scientific priority verification.

## References
[1] S. Lorz et al., *Photonic quantum walks with four-dimensional coins*, arXiv:1809.00591 (first posted 2018-09-03), https://arxiv.org/abs/1809.00591.

[2] E. Segawa, T. Koyama, N. Konno and M. Štefaňák, *Survival probability of the Grover walk on the ladder graph*, arXiv:2205.13188 (first posted 2022-05-26), https://arxiv.org/abs/2205.13188.

[3] F. Finocchiaro et al., *Optimal quantum transport on a ring via locally monitored chiral quantum walks*, arXiv:2507.10669 (first posted 2025-07-14), https://arxiv.org/abs/2507.10669.
