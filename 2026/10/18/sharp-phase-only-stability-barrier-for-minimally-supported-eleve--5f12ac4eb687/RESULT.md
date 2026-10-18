# Sharp phase-only stability barrier for minimally supported eleven-point Gabor tomography

## Finding
Let \(G=\mathbb Z/11\mathbb Z\), and let \(g\in\mathbb C^G\) have \(\|g\|_2=1\). Define
\[
A_g(a,b)=\sum_{j\in G}g_j\overline{g_{j-a}}e^{-2\pi ibj/11},
\qquad
\gamma(g)=\min_{(a,b)\ne(0,0)}|A_g(a,b)|.
\]
Every window supported on at most three sites has \(\gamma(g)=0\). Among four-supported windows with all nonzero moduli \(1/2\), the sharp value is
\[
\boxed{\max\gamma(g)=\tfrac12\sin(\pi/22).}
\]
The maximum is attained precisely as follows. The four-site support \(S\) must satisfy \(S-S=G\). Exactly one unoriented nonzero difference class \(\{\delta,-\delta\}\) then has two unordered representations, so that there are distinct ordered pairs \((r,s)\), \((u,v)\) in \(S^2\) with \(r-s=u-v=\delta\). Write \(g_j=\tfrac12e^{i\psi_j}\) for \(j\in S\). Then the phase equality condition is
\[
\boxed{e^{i(\psi_r-\psi_s-\psi_u+\psi_v)}\in\{e^{2\pi ik/11}:0\le k<11\}.}
\]
The condition is independent of the choice of sign for the repeated difference or the ordering of its two representations. No other equality cases exist.

For instance, \(S=\{0,1,2,5\}\), with all four phases zero, attains the maximum. On the SAME support, the unequal positive window
\[
g_0=7/\sqrt{83},\quad g_1=g_2=3/\sqrt{83},\quad g_5=4/\sqrt{83}
\]
(and all other coordinates zero) instead has
\[
\boxed{\gamma(g)=12/83>\sin(\pi/22),}
\]
a strict improvement by more than a factor of two. No claim of global optimality among arbitrary unequal four-tap windows is made.

For the full Gabor intensity lifting \(\mathcal L_g:\mathbb C^{11\times11}\to\mathbb C^{G^2}\),
\[
\mathcal L_g(X)_{t,k}=\operatorname{tr}\bigl(X(M_kT_tg)(M_kT_tg)^*\bigr),
\]
with Hilbert--Schmidt and Euclidean norms, the singular values are \(\sqrt{11}|A_g(a,b)|\). Consequently the minimum condition number for any four-tap equal-modulus window is \(2/\sin(\pi/22)\), and the displayed unequal-modulus example has condition number \(83/12\).

## Assumptions and scope
All indices, differences, and characters are on the cyclic group of order eleven. Translation is \((T_tg)_j=g_{j-t}\), and modulation is \((M_kg)_j=e^{2\pi ikj/11}g_j\). The four-point phase-only class includes EVERY support of cardinality four and EVERY assignment of complex phases of common modulus \(1/2\). The sharp result concerns the minimum ambiguity magnitude over all nontrivial time-frequency points, not the largest off-diagonal Gabor coherence, and the condition number of a matrix-space lifting, not the condition number of the original four-column Fourier matrix.

## Proof
**1. Minimal support and difference multiplicities.** If \(S=\operatorname{supp}(g)\), the ambiguity function vanishes identically at every shift \(a\notin S-S\). A support of cardinality at most three has at most \(1+3\cdot2=7\) distinct differences, fewer than eleven, so its margin is zero. For four sites, all ten nonzero differences can occur only if \(S-S=G\). Under this condition, consider the five unoriented classes \(\{a,-a\}\), \(a\ne0\). Six unordered support pairs distribute among these five classes, each present at least once. Hence exactly one class occurs twice and the other four classes once. Thus eight nonzero *oriented* shifts have one ordered representation each, and the remaining opposite pair have two representations each. This also proves uniqueness of the repeated class.

**2. Exact upper bound and all equality phases.** For a phase-only window, every singly represented nonzero shift has \(|A_g(a,b)|=1/4\) for all modulation frequencies \(b\). For the shift \(\delta\) with two representations \((r,s)\) and \((u,v)\),
\[
A_g(\delta,b)=\tfrac14e^{i(\psi_r-\psi_s)}e^{-2\pi ibr/11}
 +\tfrac14e^{i(\psi_u-\psi_v)}e^{-2\pi ibu/11}.
\]
Since the ordered pairs are distinct yet have equal differences, \(r-u\not\equiv0\pmod{11}\), so varying \(b\) samples all eleven equally spaced relative phases. One of those eleven phases is within \(\pi/11\) radians of \(\pi\); consequently
\[
\min_b|A_g(\delta,b)|\le\tfrac12\sin(\pi/22).
\]
The inequality is equality exactly when the relative-phase circle positions are centered halfway between the two neighbors of the antipodal point. Since the eleven positions are a rotated regular eleven-gon, this occurs exactly when the unmodulated relative phase is an eleventh root of unity, which is the displayed cross-ratio criterion. The opposite shift has the same set of magnitudes by the standard ambiguity conjugation symmetry. All singleton shifts have magnitude \(1/4\), strictly larger than \(\tfrac12\sin(\pi/22)\).

For zero shift and \(b\ne0\), the squared Fourier magnitude of the flat four-site support is exactly
\[
|A_g(0,b)|^2=\tfrac1{16}\left(3+2\cos(2\pi b\delta/11)\right)\ge\tfrac1{16}.
\]
Indeed \(\bigl|\sum_{j\in S}e^{-2\pi ibj/11}\bigr|^2\) equals four plus twice the cosine sum over its six unordered differences: one representative from each of five classes plus one extra at \(\delta\). The five-class cosine sum is \(-1/2\) for \(b\ne0\), yielding the formula. Thus zero-shift frequencies cannot reduce the sharp bound. Every cover with the root-of-unity phase condition attains it, and a non-cover has zero margin. This proves the exact optimum and exhaustive equality classification.

**3. Explicit strictly better amplitude taper.** Set \(S=\{0,1,2,5\}\) and take the positive amplitudes specified above; their squares sum to \((49+9+9+16)/83=1\). The repeated shifts \(\pm1\) have two phasors of absolute amplitudes \(21/83\) and \(9/83\), so every modulation has magnitude at least \(12/83\) by the reverse triangle inequality. The singleton shifts \(\pm3\) and \(\pm4\) each have exactly one product \(3\cdot4/83=12/83\), for every modulation. All other singleton shifts are larger, with products \(21/83\) or \(28/83\). At zero shift and \(b\ne0\), the \(49/83\) diagonal contribution dominates the other three powers, whose sum is \(34/83\), so \(|A_g(0,b)|\ge15/83\). The identity frequency \((0,0)\) is excluded from the margin. Hence the minimum is **exactly** \(12/83\). Finally \(\sin(\pi/22)<\pi/22<1/7<12/83\), where the middle inequality uses \(\pi<22/7\), proving the stated factor-of-two improvement.

**4. Lifting condition numbers.** The normalized Weyl operators \(11^{-1/2}M_bT_a\) form an orthonormal basis of the complex Hilbert–Schmidt matrix space. The conjugation orbit of \(gg^*\) evaluates each Weyl basis vector as its initial overlap \(A_g(a,b)\) times a character in the translation-modulation parameters. Orthogonality of the eleven-by-eleven character matrix therefore gives all singular values as \(\sqrt{11}|A_g(a,b)|\), counted with multiplicity. By Cauchy–Schwarz, \(|A_g(a,b)|\le1\), with \(A_g(0,0)=1\), so the largest singular value is \(\sqrt{11}\). Therefore the full-rank spectral condition number is \(1/\gamma(g)\); for a vanishing margin the lifting is singular. The two asserted condition numbers follow.

## Verification
A standalone Python standard-library checker is embedded as `check.py`. It exhaustively checks all \(\binom{11}{4}=330\) supports for the cover multiplicity dichotomy and verifies the numerical ambiguity matrices of the displayed flat and tapered windows at all \(121\) shifts and modulations. The checker corroborates the formulas within floating-point tolerance. The exact optimum, equality classification, and amplitude-taper lower bound follow from the analytic arguments above, not from numerical sampling or exhaustive enumeration of phases.

## Relationship to prior work
Bartusel, *Uncertainty Principles as a Tool for STFT Phase Retrieval* (2026), establishes phase retrieval from sufficiently broad **nonzero patterns** of an ambiguity function, rather than sharp quantitative minimum magnitudes for minimally supported eleven-point windows. Bojarovska and Flinth, *Phase Retrieval from Gabor Measurements* (2015), prove the nonvanishing ambiguity condition and the **general Weyl/PhaseLift spectral frame-bound identity**, explicitly used and credited here; their classical difference-set construction does not give this phase-only near-cover optimum, equality phases, or the tapered factor-of-two gap. A published arithmetic rigidity result proves nonvanishing for positive rational windows from difference covers (including precisely the support \(\{0,1,2,5\}\)), but it does not give a sharp eleven-point ambiguity margin. An exact four-point Fourier fourth-moment result studies the **sum of squared cyclic autocorrelation magnitudes**, whereas the present extremum concerns a minimum over modulation frequencies of the cyclic autocorrelation Fourier transform. Its stated classification does not imply this one. The present theorem neither claims originality of the lifting singular-value identity nor of the bare difference-cover injectivity criterion.

## Limitations
The sharp optimization is only within the four-tap equal-modulus class in dimension eleven. The displayed unequal positive taper proves a strict improvement but is **not** asserted optimal among all weighted windows. Neither arbitrary prime dimensions nor other support sizes are classified. Finite numerical verification is not an independent proof. Despite comparisons with relevant accessible original studies and published theorem records, unindexed sequence-design tables or an unrecognized older reformulation could affect historical priority; independent audit and publication-level priority certification have not been performed.

## References
[1] D. Bartusel, *Uncertainty Principles as a Tool for STFT Phase Retrieval*, arXiv:2605.31507v1, first public 2026-05-29, https://arxiv.org/html/2605.31507v1.

[2] I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1, first public 2015-03-19, https://arxiv.org/abs/1503.05800, especially Theorem 2.3, Proposition 2.2.

[3] D. Bartusel, *Injectivity conditions for STFT phase retrieval on \(\mathbb Z\), \(\mathbb Z_d\) and \(\mathbb R^d\)*, arXiv:2206.06729v1, 2022-06, https://arxiv.org/abs/2206.06729.

[4] *Arithmetic rigidity of prime-cyclic Gabor tomography for positive rational windows* (2026), publicly available scientific record, especially its exact rank theorem and its eleven-point four-site example.

[5] *Four-point support geometry quantizes the phase-only fourth Fourier moment* (2026), publicly available scientific record, especially its autocorrelation formulation.
