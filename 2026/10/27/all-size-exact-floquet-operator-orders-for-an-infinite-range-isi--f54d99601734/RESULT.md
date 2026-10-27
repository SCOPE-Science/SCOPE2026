# All-size exact Floquet operator orders for an infinite-range Ising drive

## Finding

For every integer \(N\ge2\), on the **full** \(2^N\)-dimensional qubit Hilbert space, consider
\[
 U_N=\exp\!\left(-\frac{i\pi}{4}\sum_{1\le j<k\le N}Z_jZ_k\right)
 \exp\!\left(-\frac{i\pi}{4}\sum_{j=1}^{N}Y_j\right),
 \qquad P_y=\prod_{j=1}^{N}Y_j.
\]
Here \(X_j,Y_j,Z_j\) are the standard Pauli operators, and scalar equality is ordinary matrix equality, **not** equality modulo global phase. The exact operator identities are
\[
 \boxed{\quad U_N^4=P_y\quad(N\text{ even}),\qquad
 U_{2m+1}^{6}=i^{m+1}P_y\quad(m\ge1).\quad}
\]
Consequently the least positive integer \(r\) with \(U_N^r=I\) is
\[
 \operatorname{ord}(U_N)=
 \begin{cases}
 8,&N\text{ even},\\
 12,&N\equiv3\pmod4,\\
 24,&N\equiv1\pmod4.
 \end{cases}
\]
For every odd \(N\ge3\), the least positive power that is merely scalar is \(12\); for even \(N\ge2\) it is \(8\). This uniform classification includes all qubit numbers beyond those treated by finite-size diagonalization in the source study. It proves operator recurrence, not the separately defined physical notion of quantum integrability.

## Assumptions and scope

Take the product convention \(ZX=iY\), \(XZ=-iY\), and \(H=2^{-1/2}\left(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\right)\). All products of site operators commute where their supports are disjoint. Set \(P_x=\prod_jX_j\), \(P_z=\prod_jZ_j\), \(F=H^{\otimes N}\), \(B=\exp(-i\pi\sum_jY_j/4)=FP_z\), and \(A=U_NB^{-1}\). There are no boundary conditions, randomness, limiting procedures or assumptions on initial states. The restriction \(N\ge2\) is essential to the stated three-branch formula.

## Proof

**1. Even sizes.** Write \(N=2m\ge2\). On a computational-basis vector of total \(Z\)-magnetization \(N-2k\), the pair sum equals \(((N-2k)^2-N)/2\). Reducing the phase by the parity of \(k\) gives the exact operator identity
\[
 A=e^{i\pi(m-1)/4}\exp\!\left(\frac{i\pi(-1)^m}{4}P_z\right).
\]
Conjugation by \(B\) sends \(P_z\) to \(P_x\) and, because \(N\) is even, its square commutes with both \(P_z\) and \(P_x\). These two global Pauli products commute for even \(N\); moreover \(B^4=I\). Squaring \(U_N^2=ABA B\) and using the preceding identity produces
\[
 U_N^4=(-1)^mP_zP_x=P_y,
\]
since \(P_zP_x=i^N P_y=(-1)^mP_y\). Thus \(U_N^8=I\). The non-scalar operator \(P_y\) implies that no divisor of \(8\) smaller than \(8\) is an ordinary or projective period.

**2. Odd sizes: diagonal quadratic form.** Let \(N=2m+1\ge3\) and \(CZ_{jk}=\operatorname{diag}(1,1,1,-1)\) on sites \(j,k\). With \(S=\operatorname{diag}(1,i)\), use, for each pair,
\[
 e^{-i\pi Z_jZ_k/4}=e^{-i\pi/4}S_jS_kCZ_{jk}.
\]
Every site occurs in \(2m\) pairs, so
\[
 A=e^{i\pi m/4}D,\qquad
 D=(-1)^{m(m+1)/2}P_z^m\prod_{j<k}CZ_{jk}.
\]
In the binary basis \(x\in\mathbb F_2^N\), the involution \(D\) is \(D|x\rangle=(-1)^{q(x)}|x\rangle\) with
\[
 q(x)=\frac{m(m+1)}2+m|x|+\binom{|x|}{2}\pmod2.
\]
The polarization is \(q(x+y)+q(x)+q(y)+q(0)=x\cdot y+p(x)p(y)\) over \(\mathbb F_2\), where \(p(x)=|x|\bmod2\). Because \(N\) is odd, its radical is spanned by the all-one vector \(\boldsymbol1\), and \(q(x+\boldsymbol1)=q(x)\). Consequently \(D\) commutes with both \(P_x\) and \(P_z\).

**3. Odd sizes: a uniform Walsh-cube identity.** Let \(C=DF\). Put \(S(t)=\sum_{y\in\mathbb F_2^N}(-1)^{q(y)+t\cdot y}\). Complement pairing and the quadratic polarization give
\[
 S(t)=0\quad\text{if }p(t)=1;\qquad
 S(t)=2^{(N+1)/2}(-1)^{q(t)+q(0)}\quad\text{if }p(t)=0.
\]
For the nonzero value, the needed root-of-unity binomial sum is explicitly
\[
 \sum_{k=0}^{2m+1}\binom{2m+1}{k}
 (-1)^{m(m+1)/2+mk+\binom{k}{2}}=2^{m+1},
\]
which follows, for example, from \((-1)^{\binom{k}{2}}=\cos(\pi k/2)+\sin(\pi k/2)\) and the binomial theorem. Expanding three kernels \(C_{xy}=2^{-N/2}(-1)^{q(x)+x\cdot y}\), carrying out the middle Walsh sum with the preceding formula, and then applying finite-character orthogonality yields
\[
 (C^3)_{xw}=\frac{(-1)^{p(x)}}{\sqrt2}\,\boldsymbol1_{w=x}
 +\frac1{\sqrt2}\,\boldsymbol1_{w=x+\boldsymbol1}.
\]
Thus \(C^3=(P_z+P_x)/\sqrt2\). Since \(P_zP_x=-P_xP_z\) for odd \(N\), we obtain \(C^6=I\). This is an identity on the full qubit Hilbert space and requires no spectral extrapolation.

**4. Odd powers and their minimality.** Define \(K=P_xP_z\), so \(K^2=-I\). The identities \(P_zCP_z=CK\) and \(CKC^{-1}=-K\) follow directly from \(C=DF\), from Hadamard exchange of \(X,Z\), and from commutation of \(D\) with the global Pauli products. Hence \(C^2\) commutes with \(K\) and
\[
 U_N^2=i^m C^2K,\qquad
 U_N^6=i^{3m}C^6K^3=i^{m+1}P_y.
\]
Therefore \(U_N^{12}=(-1)^{m+1}I\). To establish **minimal** projective order, track conjugation on Pauli vectors over \(\mathbb F_2\): representing \(X^xZ^z\) by \((x,z)\), the conjugation action of \(U_N\) is the invertible binary map
\[
 T(x,z)=(z,x+Mz),\qquad M=I+J,
\]
where \(J\) is the all-ones matrix over \(\mathbb F_2\). For odd \(N\), \(M\) vanishes on \(\langle\boldsymbol1\rangle\) and equals the identity on the even-parity hyperplane. On the first summand \(T\) has exact order \(2\); on the nonzero second summand it has exact order \(3\). Thus its order is \(6\). Any scalar power of \(U_N\) is therefore a multiple of \(6\), but \(U_N^6\) is the non-scalar operator \(i^{m+1}P_y\). The projective order is exactly \(12\). Since \(U_N^{12}=I\) for \(m\) odd and \(-I\) for \(m\) even, the ordinary order is respectively \(12\) and \(24\), as claimed.

## Verification

The accompanying self-contained integer checker `check.py` verifies the nontrivial Walsh-cube identity with exact arithmetic for odd sizes \(N=3,5,7,9\). Separately, direct complex matrix multiplication for \(N=2,3,4,5,6,7\) reproduced \(U_N^4=P_y\) and \(U_N^6=i^{(N+1)/2}P_y\) in their respective parity classes to floating-point precision better than \(3\times10^{-15}\). These finite checks corroborate but do not replace the all-size algebraic proof.

## Relationship to prior work

Sharma and Bhosale, arXiv:2307.14122, Eq. (3), introduced exactly this \(J=1\), \(\tau=\pi/4\) Floquet operator. They derived analytic unitary spectra and entanglement dynamics for sizes five through eleven, and presented larger sizes as numerical conjecture; our three-branch formula proves the all-size exact operator periods without diagonalization. Their later arXiv:2405.15797 analyzes chiefly the distinct interaction strength \(J=1/2\). The follow-up arXiv:2411.16670 reports analytical work up to twelve spins and numerical results for larger sizes; full text was not accessible for comparison, so some residual priority risk remains. The general cyclotomic recurrence criterion of Anand, Valluri and Ghose, arXiv:2610.17137, studies a **nearest-neighbor open-chain** kicked Ising unitary, not this complete-graph family, and does not supply these all-\(N\) operator identities. Generic finiteness of Clifford projective order does not determine the sharp three-case period or the global Pauli halfway identity.

## Limitations

The formula applies only to the displayed exactly tuned full-coupling drive, not to \(J=1/2\), other pulse angles, generic perturbations, open-chain nearest-neighbor Ising dynamics, or a claim of quantum integrability. An all-size period on the full Hilbert space need not be the minimal period of any particular initial state or entanglement diagnostic. The comparison of unavailable full-text follow-up material leaves a bounded originality risk; no independent scientific audit has been performed.

## References

1. H. Sharma and U. T. Bhosale, *Exactly solvable dynamics and signatures of integrability in an infinite-range many-body Floquet spin system*, arXiv:2307.14122 (first submitted 2023-07-26); Phys. Rev. B **109**, 014412 (2024), doi:10.1103/PhysRevB.109.014412.
2. H. Sharma and U. T. Bhosale, *Signatures of quantum integrability and exactly solvable dynamics in an infinite-range many-body Floquet spin system*, arXiv:2405.15797, Phys. Rev. B **110**, 064313 (2024).
3. H. Sharma and U. T. Bhosale, *Exact solvability of entanglement for arbitrary initial state in an infinite-range Floquet system*, arXiv:2411.16670 (2024).
4. A. Anand, D. Valluri and S. Ghose, *Cyclotomic structure and exact recurrences in Floquet many-body quantum dynamics*, arXiv:2610.17137 (2026).
