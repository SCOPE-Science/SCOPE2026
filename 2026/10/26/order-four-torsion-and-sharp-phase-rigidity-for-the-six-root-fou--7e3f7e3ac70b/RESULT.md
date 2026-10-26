# Order-four torsion and sharp phase rigidity for the six-root Fourier packet

## Finding

Let \(q\ge4\) be an integer, \(G_q=(\mathbb Z/q\mathbb Z)^2\) carry Haar probability measure, and let \(\chi_v(x)=\exp(2\pi i\langle v,x\rangle/q)\). Take the six-frequency root packet
\[
R=\{\pm(1,0),\ \pm(0,1),\ \pm(1,-1)\}\subset\widehat G_q.
\]
For arbitrary six complex coefficients write
\[
P_q=\sum_{j=1}^3(a_j\chi_{v_j}+b_j\chi_{-v_j}),\quad
S=\sum_{j=1}^3(|a_j|^2+|b_j|^2),
\]
with the positive roots \(v_1=(1,0)\), \(v_2=(0,1)\), and \(v_3=(1,-1)\). The following sharp inequality and complete equality classification hold:
\[
\boxed{\frac{\|P_q\|_{L^4(G_q)}^4}{S^2}\le
\begin{cases}8/3,&q=4,\\ 5/2,&q\ge5,\end{cases}}
\]
for nonzero coefficient vectors. At \(q=4\), equality holds if and only if all six coefficient moduli coincide, all three products \(a_jb_j\) agree, and \(a_j/b_j\in\{1,-1\}\) for each \(j\). Consequently there are **exactly 32 projective complex lines** of fourth-moment maximizers. At every \(q\ge5\), equality holds if and only if all coefficient moduli coincide and the three products \(a_jb_j\) agree; the relative phases then form a continuous projective three-torus.

Both sharp inequalities admit exact nonnegative deficit identities displayed below. The genuine order-four phenomenon is the extra fourth-order character collision, which raises the sharp fourth-power coefficient from \(5/2\) to \(8/3\) and collapses the equality torus to 32 lines.

## Assumptions and scope

Every \(q\) is an **integer** at least four. Complex coefficients are arbitrary, including zeros; the equality classification is for nonzero coefficient vectors. The characters of the six distinct frequencies are orthonormal in \(L^2(G_q)\), so \(\|P_q\|_2^2=S\). The bound is for the normalized fourth power \(\|P_q\|_4^4/S^2\), not its fourth root. Projective equivalence identifies nonzero complex scalar multiples and makes no further quotient by translations, automorphisms, or conjugation. We do not assert this formula for \(q=3\).

## Proof

**1. Exact Fourier-convolution identities.** Parseval and finite-character orthogonality give
\[
\|P_q\|_4^4=\sum_{s\in G_q}\bigg|\sum_{r+t=s}\!c_rc_t\bigg|^2,
\]
where \(c_{v_j}=a_j\), \(c_{-v_j}=b_j\), and both indices range over the six-point support. For \(q\ge5\), the ordered-pair sum fibers have sizes one (six fibers), two (twelve fibers), and six (one fiber, the zero sum). At \(q=4\), the three opposing pairs of single-term square frequencies collide, leaving fifteen two-term fibers and one six-term fiber. Denote \(z_j=a_jb_j\). Summing the cross terms in these explicit fibers yields
\[
\boxed{\|P_q\|_4^4=2S^2-\sum_j(|a_j|^4+|b_j|^4)
+8\sum_{i<j}\operatorname{Re}(z_i\overline{z_j})}
\quad(q\ge5)
\]
and
\[
\boxed{\|P_4\|_4^4=2S^2-\sum_j(|a_j|^4+|b_j|^4)
+8\sum_{i<j}\operatorname{Re}(z_i\overline{z_j})
+2\sum_j\operatorname{Re}(a_j^2\overline{b_j}^{\,2}).}
\]
The last term is exactly the extra order-four aliasing effect, rather than an approximation.

**2. Exact deficits and sharp upper bounds.** Put
\[
X_j=|a_j|^2+|b_j|^2,\qquad
D_j=|a_j|^2-|b_j|^2,\qquad
F_{ij}=X_iX_j/4-\operatorname{Re}(z_i\overline{z_j}).
\]
Each \(F_{ij}\ge0\) since \(|z_j|\le X_j/2\); also
\(\sum_jX_j^2-S^2/3=\tfrac13\sum_{i<j}(X_i-X_j)^2\ge0\).
Direct substitution of the formulas in step 1 gives the **exact identities**
\[
\begin{aligned}
\frac83S^2-\|P_4\|_4^4
={}&\left(\sum_jX_j^2-\frac13S^2\right)
+\sum_jD_j^2+8\sum_{i<j}F_{ij}\\
&+2\sum_j\left(|z_j|^2-\operatorname{Re}(a_j^2\overline{b_j}^{\,2})\right),
\end{aligned}
\]
\[
\boxed{\frac52S^2-\|P_q\|_4^4
=\frac32\left(\sum_jX_j^2-\frac13S^2\right)
+\frac12\sum_jD_j^2+8\sum_{i<j}F_{ij}\quad(q\ge5).}
\]
Every displayed summand is nonnegative; in particular the final order-four term is nonnegative because \(|a_j^2\overline{b_j}^{\,2}|=|z_j|^2\). Equality in either deficit is attained by taking all six coefficients equal and nonzero, so both constants are sharp.

**3. All equality cases.** If the deficit vanishes and \(S>0\), the first two terms force \(X_1=X_2=X_3=S/3\) and \(D_j=0\). Thus all six moduli equal \(\sqrt{S/6}\), and each \(z_j\) has modulus \(S/6\). Vanishing of the three \(F_{ij}\) forces \(z_1=z_2=z_3\). Conversely these conditions make the higher-order deficit zero. At order four, one must additionally have
\[
\operatorname{Re}(a_j^2\overline{b_j}^{\,2})=|a_jb_j|^2,
\]
which, since \(a_j,b_j\ne0\), holds precisely when \(a_j/b_j=\pm1\). These necessary and sufficient conditions prove the asserted classification.

**4. Count of projective order-four extremizers.** Fix the common nonzero modulus and choose an overall complex scalar so that \(z_1=z_2=z_3=1\). Each pair can then be written
\[
(a_j,b_j)=(t_j,t_j^{-1}),\qquad t_j\in\{1,-1,i,-i\}.
\]
There are \(4^3=64\) choices. The only residual scalar preserving the chosen products is multiplication by \(-1\), acting freely on these 64 choices; hence exactly \(64/2=32\) projective lines. For \(q\ge5\), the corresponding \(t_j\) are arbitrary in the unit circle, modulo simultaneous sign, giving a connected projective three-torus. No additional equality cases are possible because the deficit identities exhaust them.

## Verification

The standalone dependency-free program `verify_root_packet.py` enumerates all 36 ordered coefficient pair sums and independently reconstructs the fourth moment. It checks the exact fiber multiplicities for \(q=4,5,7\) and an unaliased integer lattice, tests both claimed formulas and deficits on reproducible complex-integer coefficients, exhaustively checks the \(4^6=4096\) fourth-root coefficient configurations, and counts the 32 distinct projective maximizing directions. It reports `PASS 5067 exact collision/deficit/phase assertions; 32 projective q=4 optimizers`. The finite checks are subsidiary to the algebraic identities above; floating-point tests do not replace the proof.

## Relationship to prior work

Bennett and Jeong, arXiv:2011.13762v1 (2020), establish general Fourier-duality identities for Brascamp–Lieb constants on abelian groups, but their group-wide duality theory does not state or entail the explicit order-four restricted six-root convolution norm and equality count. Gu, Zhou, Adhikary, Feng and Fan, arXiv:2108.05657v1 (2021), construct two-dimensional complementary **pairs** with zero-correlation zones, rather than sharp fourth moments and all arbitrary complex extremizers for one six-root packet. Published six-point triangular-aperture work optimizes phase-only arrays on a **different frequency support** with no order-four aliasing. Published six-point anisotropic-sphere results address a **different group and additive relation lattice**; their shared antipodal-product structure covers aspects of the unaliased comparison, which is not presented here as independently new. The claimed new component is specifically the \(q=4\) torsion collision, resulting exact constant, stability identity, and 32-line classification.

## Limitations

The proof concerns only the six specified root frequencies, even fourth moments, and cyclic orders \(q\ge4\). It does not establish a sharp statement for arbitrary frequency sets, other even moments, or order three. The established general Fourier-duality and autocorrelation frameworks may admit this computation as a specialization; an earlier unpublished or poorly indexed exact order-four calculation cannot be excluded by targeted searches. No external independent mathematical or priority audit has been conducted.

## References

1. J. Bennett and E. Jeong, *Fourier duality in the Brascamp–Lieb inequality*, arXiv:2011.13762v1, first public 2020-11-27, https://arxiv.org/abs/2011.13762.
2. Z. Gu, Z. Zhou, A. R. Adhikary, Y. Feng and P. Fan, *New Constructions of Golay Complementary Pair/Array with Large Zero Correlation Zone*, arXiv:2108.05657v1, first public 2021-08-12, https://arxiv.org/abs/2108.05657.
3. *Sharp fourth-moment phase rigidity for the six-point triangular Fourier aperture*, published result identifier `2026/10/11/SCOPE-sharp-fourth-moment-phase-rigidity-for-the-six-point-triangular--bea9cf2ed885`.
4. *Small-field phase dichotomy for anisotropic sphere extremizers*, published result identifier `2026/10/4/SCOPE-small-field-phase-dichotomy-for-anisotropic-sphere-extremizers--973050ba74a9`.
