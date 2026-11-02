# Exact phase-alphabet fourth moments and rigidity gaps for a four-by-two Fourier aperture

## Finding
Let \(\mu_q=\{\exp(2\pi i t/q):0\le t<q\}\), where \(q\in\{2,3,4,6\}\). For an array \(c=(c_{jk})\in\mu_q^{4\times2}\), define
\[
P_c(z,w)=\sum_{j=0}^{3}\sum_{k=0}^{1}c_{jk}z^jw^k,
\qquad
\mathcal M(c)=\int_{\mathbb T^2}|P_c(z,w)|^4\,dm(z,w),
\]
with normalized Haar measure. The exact minima, numbers of **all ordered** attaining arrays, and strict gaps to the next possible fourth moment are:

| Phase alphabet | Minimum \(\mathcal M\) | All minimizers | Next attainable value | Gap | Symmetry orbits |
|---|---:|---:|---:|---:|---:|
| \(q=2\) | 88 | 48 | 96 | 8 | 3 |
| \(q=3\) | 84 | 54 | 96 | 12 | 1 |
| \(q=4\) | 88 | 896 | 92 | 4 | 7 |
| \(q=6\) | 84 | 3024 | 86 | 2 | 3 |

The orbit count identifies arrays modulo common phase, multiplication by coordinate characters, reversal of either coordinate, and conjugation. Every minimizing orbit is specified by an explicit five-exponent representative in `CERTIFICATE.json`; no other optimizers exist. In particular, ternary phases strictly outperform quaternary phases for this aperture, while adding all sixth roots to the ternary alphabet does not lower the optimum but introduces further minimizing arrays.

These values also hold exactly for the normalized fourth moment of the same Fourier polynomial on \(\mathbb Z_M\times\mathbb Z_N\), for **every** pair of integers \(M\ge7\), \(N\ge3\); thus the sharp discrete-grid conclusion is not restricted to a finite sampling cutoff.

## Assumptions and scope
The support is the **full** rectangle \(\{0,1,2,3\}\times\{0,1\}\). All eight coefficients have modulus exactly one and belong to the specified discrete alphabet. The result does not assert optimality for arbitrary continuous phases or for other supports or phase alphabets. Counts distinguish the eight labelled coefficient positions. Symmetry orbits additionally identify horizontal/vertical reversals and complex conjugation. For finite sampling, characters have the standard integer frequencies on \(\mathbb Z_M\times\mathbb Z_N\) and the moment is normalized by \(1/(MN)\).

## Proof
**1. Exact Fourier identity.** For integers \((u,v)\) let the aperiodic autocorrelation be
\[
R_{u,v}(c)=\sum_{\substack{0\le j,j+u<4\\0\le k,k+v<2}}
 c_{j+u,k+v}\overline{c_{jk}}.
\]
Expanding \(|P_c|^2\) in characters and applying orthogonality gives
\[
\mathcal M(c)=\sum_{u=-3}^{3}\sum_{v=-1}^{1}|R_{u,v}(c)|^2
 =64+2\sum_{(u,v)\in\mathcal S_+}|R_{u,v}(c)|^2,
\]
where \(\mathcal S_+=\{(0,1)\}\cup\{(u,v):1\le u\le3,\ -1\le v\le1\}\) contains exactly ten shifts. This identity is algebraic and holds without approximation.

Equivalently, writing \(C_{a,b}=\sum_{j+j'=a,\ k+k'=b}c_{jk}c_{j'k'}\), Parseval applied to \(P_c^2\) yields the independent formula
\[
\mathcal M(c)=\sum_{a=0}^{6}\sum_{b=0}^{2}|C_{a,b}|^2.
\]
Both expressions are recalculated independently for **every** candidate by the embedded checker.

**2. Removal of three phase freedoms.** Since \(c_{jk}\mapsto\lambda\alpha^j\beta^kc_{jk}\), with \(\lambda,\alpha,\beta\in\mu_q\), leaves the fourth moment unchanged, there is a unique normalized representative with \(c_{00}=c_{01}=c_{10}=1\). Indeed choose \(\lambda=c_{00}^{-1}\), \(\alpha=c_{00}/c_{10}\), \(\beta=c_{00}/c_{01}\). Writing \(\zeta_q=\exp(2\pi i/q)\), every normalized representative is uniquely encoded by five integers
\[
(t_1,t_2,t_3,t_4,t_5)\in\{0,\ldots,q-1\}^5,
\quad
(c_{00},c_{01},c_{10},c_{11},c_{20},c_{21},c_{30},c_{31})
=(1,1,1,\zeta_q^{t_1},\zeta_q^{t_2},\zeta_q^{t_3},\zeta_q^{t_4},\zeta_q^{t_5}).
\]
Hence the exhaustive normalized spaces have exactly \(32\), \(243\), \(1024\), and \(7776\) elements respectively. Each normalized case represents exactly \(q^3\) ordered arrays; there are no unexamined phase choices.

**3. Exact integer certificate.** For \(q=2,4\), sums of roots of unity lie in the Gaussian integers \(\mathbb Z[i]\), represented by pairs \((a,b)\) with squared norm \(a^2+b^2\). For \(q=3,6\), they lie in \(\mathbb Z[\omega]\), \(\omega=\exp(2\pi i/3)\), represented by pairs \((a,b)\) with squared norm \(a^2-ab+b^2\). The six roots satisfy \(\exp(\pi i/3)=1+\omega\). Thus each correlation squared modulus and each moment is computed using **integers only**.

The accompanying `CHECK.py` implements the two explicit finite formulas from step 1 in separate loops, for every one of the \(9075\) gauge-fixed possibilities in step 2. It verifies equality of these two independent integer sums and compares the entire resulting moment histogram with `CERTIFICATE.json`. The enumerated minima, all equality cases, and next attainable values are the table in the Finding. This is a complete finite proof because both the normalization bijection and every loop bound have been proved; finite samples outside that bijection are not invoked.

**4. Complete orbit and count classification.** Normalize any minimizing array as in step 2. Its five-tuple occurs in the certificate's exact winner set. The transformations \(j\mapsto3-j\), \(k\mapsto1-k\), and \(c\mapsto\overline c\), followed by unique gauge normalization, generate the additional declared equivalence. The checker constructs each full orbit, confirms that every transformed candidate remains a minimizer, and partitions the complete winner set. The gauge-fixed orbit sizes are, in order, \((2,2,2)\), \((2)\), \((2,2,2,2,2,2,2)\), and \((2,4,8)\) for \(q=2,3,4,6\). Multiplying the total gauge-fixed winner counts \((6,2,14,14)\) by \(q^3\) gives \((48,54,896,3024)\).

**5. Uniform alias-free sampling.** In \(P_c^2\) the first Fourier degree belongs to \(\{0,\ldots,6\}\), and the second to \(\{0,1,2\}\). For \(M\ge7\) and \(N\ge3\), all these characters remain distinct on \(\mathbb Z_M\times\mathbb Z_N\). Therefore discrete Parseval gives exactly the same second formula in step 1, with no aliasing. The entire classification transfers to every such finite torus.

## Verification
The package includes `CHECK.py` (Python standard library only) and its exact, complete `CERTIFICATE.json` histogram. Run `python3 CHECK.py` in their common directory. The verified execution reports `CHECK_OK 9075 exact exhaustive normalized arrays, double evaluated`. The checker uses no floating point, no optimization heuristic and no external files. It independently computes both difference-correlation and sum-convolution formulas for every normalized array, and it checks minimum, second value, all minimizer counts and all geometric symmetry-orbit representatives. The resulting certificate is an exhaustive finite calculation, not an extrapolation to unexamined supports or alphabets.

## Relationship to prior work
Zhang, Fan and Mesnager study two-dimensional complementary **pairs** and zero-correlation zones, rather than the best total sidelobe energy of a **single** full rectangular array. Recent finite-aperture Fourier modeling motivates exact phase-quantized aperture comparisons. The previously reported exact six-mode \(3\times2\) rectangle has a continuous-phase minimum \(50\) and a different three-orbit structure; adding two **mandatory unimodular** terms is not a specialization of that theorem. The separately investigated full \(3\times3\) nine-mode square has other alphabet minima \(113,97,105,97\), and cannot cover a full \(4\times2\) array without setting forbidden coefficients to zero. Published results on the eight-frequency Fourier cube concern independent three-dimensional character relations, not the one-dimensional four-term progression in this rectangle. These differences are geometric/additive, not merely naming conventions.

## Limitations
This is a finite-alphabet, fixed-eight-coefficient classification, with a theorem valid on infinitely many alias-free sampling grids. No claim is made for arbitrary coefficients on the unit circle, larger arrays, or frequency grids below the stated alias-free thresholds. The proof's exhaustive component is explicitly restricted to \(9075\) normalized configurations. An equivalent earlier polyphase-array catalog not found in the inspected primary sources remains a bibliographic risk. Independent mathematical verification has not been conducted.

## References
1. K. Chen, H. Q. Yang and H. Wong, *Finite-Aperture Modeling of Pattern-Reconfigurable Antennas for Multiuser Beamforming*, arXiv:2610.09381v1, first publicly submitted 2026-10-07; finite-aperture Fourier representation and phase-control context.
2. H. Zhang, C. Fan and S. Mesnager, *New constructions of \(q\)-Ary 2-D Z-Complementary Array Pairs*, arXiv:2107.11599v1, first publicly submitted 2021-07-24.
3. *Exact fourth-moment range and all phase orbits of a six-mode Fourier rectangle*, publicly available mathematical research record (2026-10-11; record identifier 5147476c65ae).
4. *Sharp phase-alphabet fourth moments for the nine-mode square Fourier aperture*, publicly available mathematical research record (2026-10-11; record identifier f31c28437f0d).
