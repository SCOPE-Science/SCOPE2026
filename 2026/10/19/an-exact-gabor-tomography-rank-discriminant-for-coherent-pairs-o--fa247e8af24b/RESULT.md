# An exact Gabor-tomography rank discriminant for coherent pairs of quadratic chirps

## Finding
For an odd prime \(p\), a nonzero slope \(d\in\mathbb F_p\), and any \(z\in\mathbb C\), consider the two-chirp window
\[
g_{d,z}(x)=1+z\zeta^{d x^2},\qquad \zeta=e^{2\pi i/p},\quad x\in\mathbb F_p.
\]
Let \(T_a f(x)=f(x-a)\), \(M_b f(x)=\zeta^{bx}f(x)\), and \(P_g=gg^*\). Define the full *complex-linear intensity lift*
\[
\mathcal L_g:\mathbb C^{p\times p}\longrightarrow\mathbb C^{p^2},\qquad
\mathcal L_g(X)_{a,b}=\operatorname{tr}\bigl(XM_bT_aP_gT_a^*M_b^*\bigr).
\]
Set
\[
G_d=\sum_{x\in\mathbb F_p}\zeta^{d x^2},\quad
\kappa=(-1)^{(p-1)/2},\quad S_p=\{-\kappa\zeta^j:1\le j\le p-1\}.
\]
For \(z\ne0\), write \(Q=2\operatorname{Re}(zG_d)\) and \(h=z/\overline z\). The exact rank formula is
\[
\boxed{\operatorname{rank}_{\mathbb C}\mathcal L_{g_{d,z}}
=p^2-(p-1)\left(\mathbf1_{h\in S_p}
+\mathbf1_{Q=-p}+\mathbf1_{Q=-p|z|^2}\right).}
\]
For \(z=0\), the rank is exactly \(p\). The displayed three indicator terms count mutually disjoint classes of ambiguity zeros.

There is a particularly simple *unit-amplitude* combination for every \(p,d\):
\[
\boxed{z=\frac{\overline{G_d}}{\sqrt p},\qquad |z|=1.}
\]
This window satisfies \(\operatorname{rank}\mathcal L_g=p^2\), so its complete Gabor spectrogram determines arbitrary complex matrices through their lift and, in particular, any vector up to a unimodular scalar. Thus two elementary chirps jointly give informational completeness even though either chirp on its own has a rank-deficient Gabor lift.

For \(p\ge5\), the possible rank defect is at most \(2(p-1)\). In the exceptional dimension \(p=3\), all three deficit packets may occur together (for example \(d=1\), \(z=1+\zeta\)), leaving rank three.

## Assumptions and scope
All arithmetic in exponents and parameters \(a,b,d\) is in the prime field \(\mathbb F_p\). The additive character has the fixed positive phase above. The ambiguity function is
\[
A_g(a,b)=\sum_{x\in\mathbb F_p}g(x)\overline{g(x-a)}\zeta^{-bx}.
\]
The rank refers to the complex vector-space rank of \(\mathcal L_g\) on **all** matrices, not only Hermitian matrices or rank-one projectors. No normalization by the nonzero norm of \(g\) is made; such normalization leaves rank unchanged. A zero-free ambiguity function is sufficient for global nonlinear phase retrieval, but the converse is not asserted for \(p\ge5\).

## Proof
**Step 1: an exact four-term ambiguity formula.** Expand
\[
g(x)\overline{g(x-a)}=1+z\zeta^{dx^2}+\overline z\zeta^{-d(x-a)^2}+|z|^2\zeta^{d(2ax-a^2)}.
\]
Additive-character orthogonality and completing the square give, for *every* \(a,b\in\mathbb F_p\),
\[
\begin{aligned}
A_g(a,b)={}&p\mathbf1_{b=0}+p|z|^2\zeta^{-da^2}\mathbf1_{b=2da}\\
&+zG_d\zeta^{-b^2/(4d)}
+\overline z\,\overline{G_d}\zeta^{b^2/(4d)-ab}.
\end{aligned}
\tag{1}
\]
The division by \(4d\) means its multiplicative inverse modulo \(p\). Standard quadratic-Gauss identities give \(|G_d|^2=p\) and \(\overline{G_d}=\kappa G_d\). For clarity, the former follows by the invertible substitution \((x,y)\mapsto(x-y,x+y)\) in \(G_d\overline{G_d}\); the second follows by changing the quadratic coefficient from \(d\) to \(-d\), whose Gauss sums have ratio given by the Legendre symbol of \(-1\).

**Step 2: classify every zero.** Assume \(z\ne0\). At \((0,0)\), equation (1) is \(\|g\|_2^2>0\). This is strict because the function \(1+z\zeta^{dx^2}\) cannot vanish for both \(x=0\) and \(x=1\).

On the line \(b=0\), excluding the origin, equation (1) is \(p+Q\). Hence *either* the whole set of \(p-1\) nonzero translations vanishes when \(Q=-p\), *or* none does. On the distinct line \(b=2da\), excluding the origin, factor out \(\zeta^{-da^2}\) to obtain \(p|z|^2+Q\). Again either all \(p-1\) nonorigin points vanish or none.

Off these two lines, equation (1) has just its two Gauss terms. Their cancellation is equivalent to
\[
\frac{z}{\overline z}=-\kappa\zeta^j,
\qquad j=\frac{b^2}{2d}-ab.
\tag{2}
\]
Here \(b\ne0\), and the exclusion \(b=2da\) is precisely \(j\ne0\). For any prescribed nonzero \(j\in\mathbb F_p\), there is *exactly one* admissible \(a\) for each of the \(p-1\) possible nonzero \(b\). Thus the off-line zeros form exactly one packet of \(p-1\) pairs if \(h\in S_p\), and none otherwise. Distinct nonzero \(j\) give distinct values of \(-\kappa\zeta^j\). All three packets are pairwise disjoint by their definitions, proving the exact ambiguity-zero count.

**Step 3: ambiguity zeros equal missing lifted matrix directions.** The \(p^2\) Weyl operators \(M_bT_a\) are orthogonal with respect to the Hilbert–Schmidt product and form a basis of \(\mathbb C^{p\times p}\). In that basis the coefficient of \(P_g\) at translation/modulation \((a,b)\) is, up to a nonzero unit phase, \(A_g(a,b)\). Conjugating by all Weyl operators multiplies each such coefficient by a different phase-space character. Orthogonality of those \(p^2\) characters shows that the span of the full Weyl orbit of \(P_g\) consists of *exactly* those basis directions whose ambiguity coefficients do not vanish. Therefore
\[
\operatorname{rank}_{\mathbb C}\mathcal L_g
=\#\{(a,b)\in\mathbb F_p^2:A_g(a,b)\ne0\},
\]
which combined with Step 2 gives the boxed formula. If \(z=0\), then \(A_g(a,b)=p\mathbf1_{b=0}\), giving rank \(p\).

**Step 4: explicit full-rank unit-amplitude windows and the low-prime exception.** Choose \(z=\overline{G_d}/\sqrt p\). Since \(|G_d|=\sqrt p\), it has modulus one, \(Q=2\sqrt p>0\), and
\[
h=\frac{\overline{G_d}}{G_d}=\kappa.
\]
This is not in \(S_p\): otherwise \(\zeta^j=-1\), impossible for odd \(p\). Neither line condition can occur because \(Q>0\), proving full rank for every odd prime. Finally, if both line indicators were one, then \(|z|=1\) and \(2\operatorname{Re}(zG_d)=-p\); the Gauss magnitude inequality would imply \(p\le2\sqrt p\), hence \(p\le4\). Thus \(p\ge5\) forbids simultaneous line deficits, so no more than two deficit packets can occur. At \(p=3\), \(d=1\) and \(z=1+\zeta\), one checks \(|z|=1\), \(Q=-3\), and \(h=\zeta\in S_3\), making all three indicators one.

## Verification
The standalone script `verify_two_chirps.py` independently constructs the four coefficient sums of \(A_g\), viewed as a polynomial in \(z\) and \(\overline z\), and checks them against the four terms in (1). Every check is performed by **exact integer arithmetic in the prime cyclotomic ring**: two degree-at-most-\(p-1\) polynomials agree at \(\zeta\) if and only if their coefficient difference is constant, since the defining cyclotomic polynomial is \(1+t+\cdots+t^{p-1}\). It also verifies the two Gauss identities used in the derivation. The script checks both slopes \(d=1,2\) at prime orders \(3,5,7,11,13,17,19\), totaling 8,184 exact coefficient identities, all passed. The all-prime statement is established by the algebraic proof, *not* by finite testing.

## Relationship to prior work
Bartusel's 2022 study of cyclic STFT phase retrieval develops the ambiguity-support criterion and proves that its converse fails in some dimensions. It also proves generic nonvanishing, which alone does **not** classify a fixed two-chirp family or its operator-span rank. Bojarovska and Flinth's finite Gabor phase-retrieval framework provides the general criterion underlying Step 3. Salanevich's 2023 construction concerns multi-window measurements and sampling efficiency, rather than exact one-parameter two-chirp rank defects. Published Gabor projector results for constant-plus-one-coordinate impulses and chirp-plus-impulse windows concern different coefficient profiles and do not give equation (1)'s two-line/off-line discriminant. No assertion is made that the general Weyl diagonalization or generic phase-retrieval principle is new.

## Limitations
The theorem treats cyclic groups of **odd prime order** and a single pair of chirps with nonzero quadratic slope. It does not prove stability under noise, optimal conditioning, or the necessity of nonvanishing ambiguity for arbitrary nonlinear phase retrieval. The rank statement concerns recovery of arbitrary matrices from linear lifted measurements; lower rank does not by itself establish a nontrivial ambiguity between rank-one positive semidefinite matrices. An older equivalent formulation of the exact discriminant among radar ambiguity calculations or two-chirp waveform constructions remains a literature risk.

## References
- D. Bartusel, *Injectivity conditions for STFT phase retrieval on \(\mathbb Z\), \(\mathbb Z_d\) and \(\mathbb R^d\)*, arXiv:2206.06729v1 (public 2022-06-14), especially Sections 2.2 and 4.1.
- I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.5800 (general finite Gabor criterion).
- P. Salanevich, *Injectivity of Multi-window Gabor Phase Retrieval*, arXiv:2307.00834v1 (public 2023-07-03).
- *Single-impulse quadratic chirps: exact cyclic Gabor tomography spectrum and arithmetic rank obstruction*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-single-impulse-quadratic-chirps-exact-cyclic-gabor-tomography-sp--03361b3cff9c.
- *Exact rank discriminant for one-coordinate cyclic Gabor measurements*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-rank-discriminant-for-one-coordinate-cyclic-gabor-measurem--4ad1eba7465a.
