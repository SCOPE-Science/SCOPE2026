# Eventual exact odd-alphabet quantization of the cubic Fourier fourth moment

## Finding

For each odd integer \(q\ge3\), put \(\mu_q=\{e^{2\pi i j/q}:0\le j<q\}\). For the complete three-dimensional two-point-per-axis Fourier aperture, define
\[
P_c(z,w,u)=\sum_{(i,j,k)\in\{0,1\}^3}c_{ijk}z^iw^ju^k,
\qquad c_{ijk}\in\mu_q,
\]
and \(\mathcal M(c)=\int_{\mathbb T^3}|P_c|^4\,dm\), with normalized Haar measure. There exists an absolute odd integer \(q_0\) such that **for every odd \(q\ge q_0\)** the exact minimum is
\[
\boxed{\min_{c_{ijk}\in\mu_q}\mathcal M(c)
=136-64\cos(\pi/q)+16\cos^2(\pi/q).}
\tag{1}
\]
It follows that
\[
\boxed{\lim_{\substack{q\to\infty\\q\text{ odd}}}
q^2\big(\min\mathcal M-88\big)=16\pi^2.}
\tag{2}
\]
All minimizers are classified: modulo multiplication by \(\lambda\alpha^i\beta^j\gamma^k\) with \(\lambda,\alpha,\beta,\gamma\in\mu_q\), there are exactly **24** normalized minimizers, so the number of coefficient arrays attaining (1) is exactly \(24q^4\).

To specify all 24, normalize \(c_{000}=c_{100}=c_{010}=c_{001}=1\) and write \((A,B,C,D)=(c_{110},c_{101},c_{011},c_{111})\). Start with the base pattern \((1,-1,-1,1)\). Put \(\theta=\pi/q\), and for each vector
\[
\begin{split}
\mathcal V=\{&(-2,-1,-1,-2),(0,-1,-1,-2),
(0,-1,-1,0),(0,-1,1,0),\\
&(0,1,-1,0),(0,1,1,0),(0,1,1,2),(2,1,1,2)\},
\end{split}
\tag{3}
\]
set \((A,B,C,D)=(e^{i\theta v_A},-e^{i\theta v_B},-e^{i\theta v_C},e^{i\theta v_D})\). The remaining 16 normalized minimizers come from the two other positions of the positive entry in the ordered triple \((A,B,C)\): permute the first three coordinates of these eight arrays so that their zero-alphabet limits are \((-1,1,-1,1)\) and \((-1,-1,1,1)\). These 24 are distinct for all sufficiently large odd \(q\). No assertion is made here that the formula or the equality classification holds for every smaller odd \(q\).

## Assumptions and scope

The coefficients have magnitude one and lie in the same finite, **odd-order**, root-of-unity alphabet. The integral is a fourth power with normalized Haar measure on \(\mathbb T^3\), not a Walsh fourth moment on a Boolean group. The theorem is eventual: its proof establishes existence of \(q_0\) but supplies no explicit numerical value. The 24 orbit count does **not** quotient by permutations of the spatial axes; only scalar and coordinate-character phases are identified. All claims concern one array's aperiodic autocorrelation energy, not sums of correlation energies over complementary array pairs.

## Proof

**1. Exact normalization and sum-of-squares identity.** Multiplication by \(\lambda\alpha^i\beta^j\gamma^k\), with all four parameters in \(\mu_q\), uniquely normalizes the four coefficients at \((0,0,0),(1,0,0),(0,1,0),(0,0,1)\) to one. Every normalized array has exactly \(q^4\) original lifts. Orthogonality of the 27 Fourier-convolution coefficients gives, for unimodular \(A,B,C,D\), the exact identity
\[
\begin{split}
\mathcal M=88+2\big(&|A+B+C+D|^2
+|1+A+B+D\overline C|^2\\
&+|1+A+C+D\overline B|^2
+|1+B+C+D\overline A|^2\big).
\end{split}
\tag{4}
\]
This may also be obtained from the 13 nonzero aperiodic autocorrelation pairs. As a separate algebraic check, put \(U=1+A+B+C\) and \(V=A+B+C+AB+AC+BC\); expansion of (4) gives
\[
\mathcal M=104+4|U|^2+8\operatorname{Re}(D\overline V).
\tag{5}
\]
Newton's identity \(2V=U^2-(1+A^2+B^2+C^2)\) implies \(2|V|\le|U|^2+4\). Thus (5) gives \(\mathcal M\ge88\). Equality forces \(A,B,C\in\{\pm1\}\), \(U=0\), \(V=-2\), and \(D=1\). Therefore the complete continuous minimum locus consists of exactly the three isolated normalized points
\[
(1,-1,-1,1),\quad(-1,1,-1,1),\quad(-1,-1,1,1).
\tag{6}
\]
(The equality conclusion is also explicitly established in the prior cubic-aperture result cited below; the argument here verifies it independently.)

**2. Strict local quadratic rigidity.** Near \((1,-1,-1,1)\), let \(x=(x_A,x_B,x_C,x_D)\in\mathbb R^4\) be the phase offsets:
\[
(A,B,C,D)=(e^{ix_A},-e^{ix_B},-e^{ix_C},e^{ix_D}).
\]
The four complex expressions inside (4) vanish at \(x=0\), and their linear terms are \(iRx\), where
\[
R=\begin{pmatrix}
1&-1&-1&1\\
1&-1&1&-1\\
1&1&-1&-1\\
-1&-1&-1&1
\end{pmatrix}.
\]
Hence
\[
\mathcal M-88=x^{\mathsf T}Gx+O(\|x\|^3),\qquad
G=2R^{\mathsf T}R=
\begin{pmatrix}8&0&0&-4\\0&8&0&-4\\0&0&8&-4\\-4&-4&-4&8\end{pmatrix}.
\tag{7}
\]
The eigenvalues of \(G\) are \(8,8,8-4\sqrt3,8+4\sqrt3\), all positive. Permuting \(A,B,C\) gives the same positive-definite local geometry near each of the other two points (6). In particular, in a fixed neighborhood of each point, \(\mathcal M-88\ge c\|x\|^2\) for some \(c>0\).

**3. The odd-alphabet tangent lattice.** Write \(\theta=\pi/q\). Because \(q\) is odd, any \(q\)-th root of unity near \(1\) is of the form \(e^{i\theta v}\) with **even** integer \(v\), and one near \(-1\) is \(-e^{i\theta v}\) with **odd** integer \(v\). Therefore the tangent lattice at the first point (6) consists of
\[
(v_A,v_B,v_C,v_D)\in(2\mathbb Z)\times(2\mathbb Z+1)
\times(2\mathbb Z+1)\times(2\mathbb Z).
\]
Writing \(v_D=2m\), the exact quadratic form is
\[
Q(v)=v^{\mathsf T}Gv
=8\big((v_A-m)^2+(v_B-m)^2+(v_C-m)^2+m^2\big).
\tag{8}
\]
If \(m\) is even, the second and third squares are at least one, and the minimum \(Q=16\) occurs only at \(m=0,v_A=0,v_B,v_C\in\{-1,1\}\), four vectors. If \(m\) is odd, the first square is at least one, and \(Q=16\) occurs only at \(m=\pm1\), \(v_B=v_C=m\), and \(v_A=m\pm1\), four more vectors. These are precisely the eight vectors (3). Every other lattice vector satisfies \(Q(v)\ge48\). Permuting the positions of \(A,B,C\) yields eight analogous lattice vectors at each of the other two continuous minimizers.

**4. Exact candidate values.** Substituting each of the eight vectors (3) into the Laurent-polynomial identity (4), and using \(2\cos\theta=e^{i\theta}+e^{-i\theta}\), gives **exactly**
\[
\mathcal M=136-64\cos\theta+16\cos^2\theta.
\tag{9}
\]
This is an exact algebraic identity, not a Taylor approximation. The same holds for the other 16 vectors by permutation symmetry. Every displayed array belongs to \(\mu_q\), by the parity restrictions in step 3. Its value is \(88+16\theta^2+O(\theta^4)\).

**5. Global optimality for all sufficiently large odd orders.** Let \(q\) run through odd integers tending to infinity and let \(c_q\) be a normalized global minimizer. Step 4 gives \(\mathcal M(c_q)-88=O(q^{-2})\). Compactness of the four-torus and step 1 force \(c_q\) into shrinking neighborhoods of the finite set (6). The positive Hessian in step 2 then strengthens the phase-distance estimate to \(O(q^{-1})\). Consequently, when \(c_q\) is expressed around the nearest point as in step 3, the corresponding parity-lattice vector \(v_q\) is bounded independently of \(q\). Uniformly over such bounded vectors, (7) gives
\[
\frac{q^2}{\pi^2}(\mathcal M(c_q)-88)=Q(v_q)+O(q^{-1}).
\]
The explicit candidates in step 4 have leading value \(16\). Since the lattice minimum is exactly \(16\) and all other lattice values are at least \(48\), a global minimizer cannot use any other lattice vector for all sufficiently large odd \(q\). Thus its normalized tuple belongs to the 24 explicit candidates, which all attain the exact same (9). Each has \(q^4\) coefficient-array lifts, giving \(24q^4\) minimizers. Equation (2) follows from (1). This completes the proof.

## Verification

The standalone standard-library program `CHECK.py` expands all 27 convolution coefficients as integer Laurent polynomials and verifies the independent identity (4). It checks the Hessian matrix, enumerates exactly the eight parity-lattice vectors with \(Q=16\) in a bounding box (the unbounded lattice classification is proved in step 3), and verifies (9) as a **formal Laurent-polynomial identity** for all 24 candidate patterns. Separate complex-arithmetic convolution enumerations for odd \(q=3,5,7,9\) agree with the candidate minimum; the number of normalized minimizers is 56 for \(q=3\) and 24 for \(q=5,7,9\). The finite numerical enumerations are supplementary tests only, not proof for arbitrary orders. Replay with `python3 CHECK.py` in the extracted package directory.

## Relationship to prior work

The public result *Exact fourth-moment rigidity of the eight-mode cubic Fourier aperture* (11 October 2026) establishes (for arbitrary unimodular phases) the sharp range \([88,216]\), proves the three continuous minimizing orbits, and shows that a \(q\)-phase alphabet attains the **unrestricted** minimum \(88\) exactly when \(q\) is even. Its inspected full statement and proof explicitly leave the actual odd-\(q\) minimum undetermined. The present theorem answers the different quantitative question: for all sufficiently large **odd** orders it gives the exact positive excess, its sharp coefficient \(16\pi^2\), and all 24 normalized equality configurations. The previous lower bound and the odd nonattainment fact alone do not imply these conclusions.

Xu Wang's 16 June 2026 preprint develops constructions for two-phase and four-phase Golay **complementary sequence sets**; those constructions concern correlation cancellations across multiple sequences and do not provide this single three-dimensional array's odd-phase optimum. Related full-support results for a \(3\times3\) Fourier square or a six-point triangular aperture involve different coefficient supports and phase lattices and do not imply the present theorem. No bibliographically exhaustive priority claim is made; an earlier unindexed polyphase-array calculation remains a risk.

## Limitations

The threshold \(q_0\) is existential and not explicitly bounded. No all-odd-order equality classification is asserted, and \(q=3\) has extra numerical minimizers. The theorem does not handle amplitudes other than one, even-alphabet optima (already covered by prior work), supports other than the complete \(2\times2\times2\) cube, or higher Fourier moments. The exact result is mathematical but has not undergone independent audit; the supplementary numerical tests cannot certify the theorem on their own.

## References

1. *Exact fourth-moment rigidity of the eight-mode cubic Fourier aperture*, published-finding corpus public mathematical record, 11 October 2026: https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-exact-fourth-moment-rigidity-of-the-eight-mode-cubic-fourier-ape--486a31ac0a2d/RESULT.md .
2. Xu Wang, *A construction method for 2-phase and 4-phase Golay Complementary Sequences*, arXiv:2606.17651v1, first publicly submitted 16 June 2026: https://arxiv.org/abs/2606.17651 .
3. C.-Y. Pai and C.-Y. Chen, *Two-Dimensional Golay Complementary Array Sets from Generalized Boolean Functions*, arXiv:2102.04043v1, 8 February 2021: https://arxiv.org/abs/2102.04043 .
4. *Sharp phase-alphabet fourth moments for the nine-mode square Fourier aperture*, published-finding corpus public mathematical record, 11 October 2026: https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-sharp-phase-alphabet-fourth-moments-for-the-nine-mode-square-fou--f31c28437f0d/RESULT.md .
5. *Sharp fourth-moment phase rigidity for the six-point triangular Fourier aperture*, published-finding corpus public mathematical record, 11 October 2026: https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-sharp-fourth-moment-phase-rigidity-for-the-six-point-triangular--bea9cf2ed885/RESULT.md .
