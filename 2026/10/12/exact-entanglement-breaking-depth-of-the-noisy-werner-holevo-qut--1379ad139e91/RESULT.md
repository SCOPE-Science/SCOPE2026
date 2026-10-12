# Exact entanglement-breaking depth of the noisy Werner–Holevo qutrit family

## Finding
For the one-parameter qutrit channel
\[
\Phi_x(X)=(1-x)X+\frac{x}{2}\bigl(\operatorname{Tr}(X)I_3-X^{\mathsf T}\bigr),\qquad 0\le x\le1,
\]
write \(s=1-3x/2\) and \(a=1-x/2\). For every integer \(k\ge1\), the \(k\)-fold **composition** \(\Phi_x^k\) is entanglement-breaking exactly when
\[
5s^k+3a^k\le2,\qquad 3a^k-5s^k\le1. \tag{1}
\]
Thus the ordinary (unfiltered) entanglement-breaking index is the least positive integer satisfying (1), and is infinite only for \(x=0\). No member of this family is entanglement-breaking after exactly one use, whereas
\[
n_{\mathrm{EB}}(\Phi_x)=2\quad\Longleftrightarrow\quad
\frac{4+\sqrt2}{7}\le x\le1. \tag{2}
\]
For \(x=1/2\) the exact index is \(4\), despite its vanishing unassisted quantum and private classical capacities established in the motivating source. Furthermore,
\[
\lim_{x\downarrow0}x\,n_{\mathrm{EB}}(\Phi_x)=-2\log y_*\simeq1.463405430167, \tag{3}
\]
where \(y_*\in(0,1)\) uniquely solves \(5y_*^3+3y_*=2\). These assertions form a complete exact iteration-depth criterion and a sharp weak-noise asymptotic for this natural interpolation between identity and qutrit Werner–Holevo noise.

## Assumptions and scope
Matrices act on \(\mathbb C^3\); transposition is in the fixed computational basis. Each iteration applies the **same** completely positive, trace-preserving channel with no intermediate filtering, control or tensor-product encoding. The parameter is real and satisfies \(0\le x\le1\), and \(k\) is a positive integer. Entanglement-breaking means that the channel destroys entanglement with an arbitrarily large reference on every input; equivalently its normalized Choi state is separable. A channel's ordinary index is the minimum such \(k\), or infinity if there is none. The displayed rate concerns \(x\downarrow0\), not long-time continuous semigroup evolution.

## Proof
**1. Explicit iterates.** Every matrix \(X\) splits uniquely into a scalar part, a symmetric traceless part and a skew-transpose part:
\[
X=\frac{\operatorname{Tr}X}{3}I_3+S+T,\quad S^{\mathsf T}=S,\ \operatorname{Tr}S=0,\ T^{\mathsf T}=-T.
\]
The three sectors have eigenvalues \(1,s,a\), respectively, under \(\Phi_x\). Thus, for all \(k\ge1\),
\[
\Phi_x^k(X)=A_kX+B_kX^{\mathsf T}+C_k\operatorname{Tr}(X)I_3,
\]
\[
A_k=\frac{s^k+a^k}{2},\qquad B_k=\frac{s^k-a^k}{2},\qquad C_k=\frac{1-s^k}{3}. \tag{4}
\]
This also proves the stated formula at the singular parameter \(s=0\); no division by an eigenvalue was used.

**2. Choi partial transpose.** Set \(|\Omega\rangle=(|00\rangle+|11\rangle+|22\rangle)/\sqrt3\), \(P=|\Omega\rangle\langle\Omega|\), and let \(F|ij\rangle=|ji\rangle\). The normalized Choi matrix of (4) is
\[
\rho_k=A_k P+\frac{B_k}{3}F+\frac{C_k}{3}I_9.
\]
Partial transposition on either tensor factor interchanges \(P\) and \(F/3\), giving
\[
\rho_k^{\Gamma}=\frac{A_k}{3}F+B_k P+\frac{C_k}{3}I_9.
\]
Its three exact eigenvalues and multiplicities are
\[
\begin{array}{c|c}
\text{space}&\text{eigenvalue}\\ \hline
\text{antisymmetric, rank }3 &(2-5s^k-3a^k)/18\\
\mathbb C\Omega,\text{ rank }1 &(1+5s^k-3a^k)/9\\
\text{symmetric orthogonal to }\Omega,\text{ rank }5 &(2+s^k+3a^k)/18.
\end{array} \tag{5}
\]
For \(0\le x\le1\), \(a\in[1/2,1]\) and \(s\in[-1/2,1]\), so the last eigenvalue is strictly positive for every positive \(k\). Therefore (5) is positive semidefinite precisely when the two inequalities in (1) hold.

**3. Why partial-transpose positivity suffices here.** The Choi matrix is invariant under \(O\otimes O\) for every real orthogonal \(3\times3\) matrix \(O\). Every such invariant matrix belongs to the linear span of \(I_9,F,P\). To see this directly, invariance of its rank-four coefficient tensor under coordinate sign changes forces the four indices to occur in pairs; coordinate permutations give just the three possible pairings, and planar rotations enforce the relation between the all-equal component and those three pairings. Thus a normalized invariant Hermitian matrix is specified uniquely by
\[
f=\operatorname{Tr}(\rho F),\qquad g=\operatorname{Tr}(\rho P).
\]
For any **positive** invariant state \(\rho\) whose partial transpose is also positive, \(0\le f\le1\) follows from \(F\le I_9\) and \(f=3\operatorname{Tr}(\rho^\Gamma P)\), and \(0\le g\le1/3\) follows from \(g=\operatorname{Tr}(\rho^\Gamma F)/3\le1/3\). The four vertices of this rectangle arise from real-orthogonally twirling the pure product projectors built from
\[
(e_1,e_2),\qquad (z,z),\qquad (z,\overline z),\qquad (e_1,e_1),
\quad z=(e_1+i e_2)/\sqrt2.
\]
The corresponding \((f,g)\) values are exactly \((0,0),(1,0),(0,1/3),(1,1/3)\). Orthogonal twirling preserves separability, and the resulting states are unique at their coordinate pairs. Taking their convex combinations realizes every point in the rectangle. Hence **every PPT state in this invariant three-dimensional commutant is separable**. This proves (1), since a channel is entanglement-breaking if and only if its Choi state is separable.

**4. Exact low indices.** For \(k=1\), the two numerator conditions reduce to \(3(3x-2)\ge0\) and \(3(1-2x)\ge0\), demanding \(x\ge2/3\) and \(x\le1/2\) simultaneously, which is impossible. For \(k=2\), the two numerators are
\[
-6(x-1)(2x-1),\qquad\frac32(7x^2-8x+2).
\]
Both are nonnegative exactly for \(x\in[(4+\sqrt2)/7,1]\), proving (2). For \(x=0\) the channel is the identity and can never be entanglement-breaking. For \(0<x\le1\), both \(|s|<1\) and \(a<1\), so (1) holds for sufficiently large \(k\), proving finiteness.

At the source's physically significant \(x=1/2\), \(s=1/4\) and \(a=3/4\). The antisymmetric and distinguished-symmetric partial-transpose eigenvalues, respectively, for the first four powers are
\[
\begin{array}{c|cc}
k&\lambda_{-}&\lambda_{\Omega}\\ \hline
1&-1/12&0\\
2&0&-1/24\\
3&7/192&-1/48\\
4&11/192&1/128
\end{array}
\]
so its entanglement-breaking index is precisely \(4\). Composition with further channels preserves the entanglement-breaking property.

**5. Weak-noise constant.** For fixed \(t\ge0\) and integers \(k\) with \(kx\to t\) as \(x\downarrow0\), the pair \((s^k,a^k)\) converges to \((e^{-3t/2},e^{-t/2})\). The first inequality in (1) becomes \(5e^{-3t/2}+3e^{-t/2}\le2\), with a unique threshold \(t=\tau>0\) since its left side decreases strictly from \(8\) to \(0\). With \(y=e^{-t/2}\), this is precisely \(5y^3+3y=2\), and \(\tau=-2\log y_*\). The second limiting left side is \(3y-5y^3\), whose maximum over \(0\le y\le1\) is \(2/\sqrt5<1\). Thus for every \(\varepsilon>0\) the upper and lower integer brackets \(\lfloor(\tau-\varepsilon)/x\rfloor\), \(\lceil(\tau+\varepsilon)/x\rceil\) eventually lie respectively below and above the least permitted power. For sufficiently small \(x\), \(s>0\), so the first left side decreases with \(k\) and excludes every earlier integer at the lower bracket. This proves (3).

## Verification
A standalone Python program `verify.py` (dependency specification `requirements.txt`) reconstructs the normalized Choi matrix directly from repeated action on all nine matrix units, compares it with (4), computes all partial-transpose eigenvalues and verifies (1) on a grid of \(51\) noise values and \(12\) positive powers. It performs \(612\) comparisons of each type, checks the four separable rectangle corners, verifies the first four eigenvalue pairs by exact rational arithmetic and checks the weak-noise constant numerically. The observed terminal line is `VERIFY_OK 612 exact matrices + PPT + pure product corners; tau 1.463405430167`. This finite testing is supplementary; the universal result, sharp index and limit are certified by the algebraic proof above, not by extrapolation from tests. Run using `python -m pip install -r requirements.txt` and `python verify.py` in the extracted directory.

## Relationship to prior work
Zhu and Wang's 2026 channel-capacity theorem identifies \(\Phi_{1/2}\), proves its quantum and private capacities vanish, and obtains a negative partial-transpose eigenvalue for **one** use. The earlier noisy Werner–Holevo papers define the interpolation and calculate its one-step superoperator spectrum and channel capacities. These foundational facts are credited, not claimed as new. Lami and Giovannetti (2015, Example 5) establish that the **unmixed Werner-channel endpoint** has entanglement-breaking index two. Park (2026) and predecessors give qualitative eventual-breaking results for PPT maps and general composition bounds. Prior work on orthogonally invariant bipartite states provides symmetry/separability tools. The present statement solves the **full noisy interpolation's unfiltered iteration-depth phase diagram**, including the initially NPT zero-capacity channel's index four and the sharp small-noise constant. No claim is made about filtered entanglement-breaking indices.

## Limitations
This classification applies only to qutrits and to sequential powers of the same channel, without intermediate filters. The source's zero-capacity result for \(x=1/2\) is used as a cited theorem, not re-proved here. No quantitative physical error model for laboratory implementations or robustness of the thresholds under perturbations is established. A previously implicit or unindexed priority result cannot be ruled out by targeted searches.

## References
1. C. Zhu and X. Wang, *Quantum Incapacity beyond No-Cloning and PPT Mechanisms*, arXiv:2607.24693v1 (2026), https://arxiv.org/html/2607.24693v1.
2. V. Karimipour, *The noisy Landau-Streater (Werner-Holevo) channel in arbitrary dimensions*, arXiv:2402.07700v5 (2024), https://arxiv.org/html/2402.07700v5.
3. S. Roofeh and V. Karimipour, *Capacities of a two-parameter family of noisy Werner-Holevo channels*, arXiv:2405.11216v2 (2024), https://arxiv.org/html/2405.11216v2.
4. L. Lami and V. Giovannetti, *Entanglement-Breaking Indices*, arXiv:1411.2517v4 (2015), https://arxiv.org/html/1411.2517v4.
5. S.-J. Park, *Every PPT channel has finite entanglement-breaking index*, arXiv:2608.13551v1 (2026), https://arxiv.org/html/2608.13551v1.
6. K. Audenaert, B. De Moor, K. G. H. Vollbrecht and R. F. Werner, *Asymptotic Relative Entropy of Entanglement for Orthogonally Invariant States*, arXiv:quant-ph/0204143 (2002).
