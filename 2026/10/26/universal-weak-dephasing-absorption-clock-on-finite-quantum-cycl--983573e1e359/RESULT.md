# Universal weak-dephasing absorption clock on finite quantum cycles

## Finding
For every integer \(n\ge3\), absorption strength \(\gamma>0\), and density matrix \(\rho\ge0\) with \(\operatorname{Tr}\rho=1\), let \(H\) be the adjacency matrix of the simple cycle \(C_n\), \(P_j=|j\rangle\langle j|\), and consider
\[
\mathcal L_\kappa(X)=-i[H,X]-\gamma\{P_0,X\}+\kappa\left(\sum_{j=0}^{n-1}P_jXP_j-X\right),\quad\kappa>0.
\]
The integrated survival time \(T_\kappa(\rho)=\int_0^\infty\operatorname{Tr}(e^{t\mathcal L_\kappa}\rho)\,dt\) is finite for every \(\kappa>0\). Define reflection by \(R|j\rangle=|-j\pmod n\rangle\), and its odd projector \(Q=(I-R)/2\). Then
\[
\boxed{\lim_{\kappa\downarrow0}\kappa T_\kappa(\rho)=2\operatorname{Tr}(Q\rho).}
\]
In particular, for a site-localized initial state \(\rho=P_a\), the limit is \(1\) for all \(a\not\equiv0\pmod n\) except \(a=n/2\) when \(n\) is even; at those fixed points the limit is \(0\) and \(T_\kappa(P_a)=O(1)\). Thus the universal coefficient for nonexceptional localized sites is independent of ring size and positive sink strength.

## Assumptions and scope
Indices are modulo \(n\). The graph is the simple unweighted cycle, with hopping amplitude one on each edge; the fixed absorber is modeled by the non-Hermitian anticommutator \(-\gamma\{P_0,X\}\), so the physical probability loss is \(2\gamma X_{00}\). Pure site dephasing is normalized so that every off-diagonal matrix element of \(X\) receives a direct dissipative term \(-\kappa X_{ab}\), \(a\ne b\). Time, \(n\), and \(\gamma\) are fixed while \(\kappa\downarrow0\). No additional uniform recombination or competing loss is present. All density matrices are allowed, including coherent superpositions.

## Proof
Write \(\mathcal L_0=-i[H,\cdot]-\gamma\{P_0,\cdot\}\) and \(D(X)=\sum_jP_jXP_j-X\). Reflection commutes with \(H\) and fixes \(|0\rangle\). The reflection-odd subspace \(\mathcal Q=Q\mathbb C^n\) consists of the sine waves
\[
u_k(j)=\sqrt{2/n}\sin(2\pi kj/n),\qquad 1\le k\le\lfloor(n-1)/2\rfloor.
\]
They are orthonormal eigenvectors of \(H\) with mutually distinct eigenvalues \(\varepsilon_k=2\cos(2\pi k/n)\), and vanish at the trap. Each spectral eigenspace of \(H\) has a trap-visible reflection-even cosine vector, and its sole trap-invisible part is odd. The compression \(K_+=H|_{\mathcal Q^\perp}-i\gamma P_0\) has all eigenvalues with strictly negative imaginary part: if an eigenvalue were real, the dissipative imaginary-part identity would force a zero trap amplitude and hence a trap-invisible eigenvector in the even subspace, impossible. Therefore \(\mathcal L_0\) has a semisimple zero eigenspace exactly spanned by \(E_k=|u_k\rangle\langle u_k|\), and its Riesz projection is
\[\Pi(X)=\sum_k\langle u_k,Xu_k\rangle E_k.\]
All other eigenvalues of \(\mathcal L_0\) are nonzero: off-diagonal odd-mode coherences have nonzero purely imaginary frequencies, while every block involving the even sector decays.

The reduced first-order dephasing operator \(\Pi D\Pi\), in the orthonormal Hilbert–Schmidt basis \(E_k\), is \(B-I\), with
\[B_{k\ell}=\sum_{j=0}^{n-1}|u_k(j)|^2|u_\ell(j)|^2.\]
Here \(B\) is symmetric and entrywise nonnegative. By sine-wave completeness, \(\sum_\ell|u_\ell(j)|^2=Q_{jj}\), which equals \(1/2\) at each vertex moved by reflection and zero at reflection-fixed vertices. Every \(u_k\) vanishes at fixed vertices. Hence \(\sum_\ell B_{k\ell}=1/2\) for every \(k\). All eigenvalues of \(B\) have modulus at most \(1/2\), so \(I-B\) is invertible and the row vector of all ones satisfies \(\boldsymbol1^\top(I-B)^{-1}=2\boldsymbol1^\top\).

Since zero is a semisimple isolated eigenvalue of \(\mathcal L_0\) and \(-\Pi D\Pi=I-B\) is invertible, finite-dimensional analytic block inversion (Schur complement about \(\Pi\)) gives
\[
\lim_{\kappa\downarrow0}\kappa(-\mathcal L_\kappa)^{-1}=\Pi(I-B)^{-1}\Pi,
\]
where the inverse acts on the full operator space and \((I-B)^{-1}\) on populations. Taking trace of the image of \(\rho\) proves the boxed result because \(\operatorname{Tr}\Pi(X)=\operatorname{Tr}(QX)\). The same block inverse shows that an input with \(\Pi(\rho)=0\) has bounded \((-\mathcal L_\kappa)^{-1}\rho\) as \(\kappa\downarrow0\), establishing the exceptional \(O(1)\) statement.

To establish existence of the integral for each \(\kappa>0\), use Hilbert–Schmidt dissipation:
\[
\operatorname{Re}\langle X,\mathcal L_\kappa X\rangle=-\gamma(\|P_0X\|_2^2+\|XP_0\|_2^2)-\kappa\sum_{a\ne b}|X_{ab}|^2.
\]
A peripheral eigenoperator must be diagonal and vanish in row and column zero. For its eigenvalue to have zero real part, the diagonal must commute with the connected-cycle adjacency matrix, hence be scalar; vanishing at the trap forces zero. Every eigenvalue consequently has strictly negative real part, and the semigroup is exponentially stable.

## Verification
The standalone program `verify.py` builds the complex Liouvillian using column-vectorization, solves its integrated master equation independently for each sampled density matrix, and compares extrapolated \(\kappa T_\kappa\) with \(2\operatorname{Tr}(Q\rho)\). It also checks the trap-cyclic Krylov rank and diagonal reflection projection. Its deterministic run reports **220 successful finite comparisons**, for sizes \(3\) through \(10\), three sink strengths, all localized sources, and randomly generated coherent initial pure states. The analytic proof applies to all \(n\ge3\); finite tests are illustrative, not exhaustive proof.

## Relationship to prior work
Fedichkin, Solenov and Tamon [1] established dephasing-induced mixing results for quantum walks on finite cycles, without a localized irreversible absorber. Kassal and Aspuru-Guzik [2, sections on rings and dephasing-assisted trapping] studied the combination of ring geometry, dephasing and trapping with uniform background loss; their transport efficiency and weak-loss optimization address a different observable and limiting regime. The present theorem instead fixes trap strength, removes competing background loss, and computes the exact leading weak-dephasing coefficient of integrated survival for every initial density matrix. Bressanini, Benedetti and Paris [3] investigated classicalization under position dephasing rather than absorbing lifetime. A 2004 Haken–Strobl trapping-network article by Gaab and Bardeen [4] was available only as an abstract here; whether its full analysis already implies this specialization remains a priority risk. The formula is not claimed to be universally unprecedented without further historical verification.

## Limitations
The theorem is finite-dimensional with fixed \(n\) and fixed positive \(\gamma\). It does not establish uniform simultaneous limits in size, trap rate, and dephasing, or a complete absorption-time distribution. Site-independent dephasing and a single site absorber are essential assumptions. The existing literature on dephasing and trapping is broad; historical-priority verification remains incomplete, including one inaccessible primary full text.

## References
[1] L. Fedichkin, D. Solenov, C. Tamon, *Mixing and Decoherence in Continuous-Time Quantum Walks on Cycles*, arXiv:quant-ph/0509163v1 (first public preprint September 22, 2005), https://arxiv.org/abs/quant-ph/0509163.

[2] I. Kassal, A. Aspuru-Guzik, *Environment-assisted quantum transport in ordered systems*, arXiv:1201.5202v1 (January 25, 2012), https://arxiv.org/abs/1201.5202.

[3] G. Bressanini, C. Benedetti, M. G. A. Paris, *Decoherence and classicalization of continuous-time quantum walks on graphs*, arXiv:2204.01836v1 (April 4, 2022), https://arxiv.org/abs/2204.01836.

[4] K. M. Gaab, C. J. Bardeen, *The effects of connectivity, coherence, and trapping on energy transfer in simple light-harvesting systems studied using the Haken–Strobl model with diagonal disorder*, J. Chem. Phys. 121, 7813–7820 (2004), DOI:10.1063/1.1786922. Full text not available for substantive comparison here.
