# Arithmetic rigidity of prime-cyclic Gabor tomography for positive rational windows

## Finding

Let \(p\) be an odd prime and let \(g\in\mathbb Q_{\geq0}^{\mathbb F_p}\setminus\{0\}\). Let \(S=\{x:g_x>0\}\), \(D=S-S\), and \(v_{t,k}=M_kT_tg\), where \((T_tg)_x=g_{x-t}\) and \((M_kg)_x=e^{2\pi ikx/p}g_x\). On the full complex matrix space set
\[
\mathcal L_g(H)_{t,k}=\operatorname{tr}(H v_{t,k}v_{t,k}^{*}),\qquad(t,k)\in\mathbb F_p^2.
\]
All matrix norms used below are Hilbert--Schmidt norms, and no normalization is imposed on \(g\).

**Exact arithmetic classification.** If \(S\neq\mathbb F_p\), then
\[
\operatorname{rank}_{\mathbb C}\mathcal L_g=p|D|,\qquad
\dim_{\mathbb C}\ker\mathcal L_g=p(p-|D|).
\]
The ambiguity coefficients
\[
A_g(a,b)=\sum_{x\in\mathbb F_p}g_xg_{x-a}e^{2\pi ibx/p}
\]
vanish exactly for \(a\notin D\), independently of \(b\). Consequently the kernel is the complex span of the Weyl operators \(M_bT_a\) with \(a\notin D\), all \(b\in\mathbb F_p\). If \(S=\mathbb F_p\), then the rank is \(p\) if \(g\) is constant and \(p^2\) otherwise; in the constant case the kernel is the span of \(M_bT_a\) with \(b\neq0\), and in the nonconstant case it is zero.

For all such windows, **complete signal phase retrieval up to a global phase** holds exactly when \(\mathcal L_g\) is injective: for proper support precisely when \(S-S=\mathbb F_p\), and for full support precisely when \(g\) is nonconstant. Moreover, the singular values of \(\mathcal L_g\), counted with multiplicity, are exactly
\[
\left\{\sqrt p\,|A_g(a,b)|:(a,b)\in\mathbb F_p^2\right\}.
\]
This singular-value identity is a prior known Weyl-diagonalization result, included to fix the normalization and recover the kernel/rank conclusions; novelty is claimed only for the rational-positive arithmetic classification and its consequences.

For every proper \(S\) of size \(s\), the lower rank bound \(\operatorname{rank}\mathcal L_g\ge p\min(p,2s-1)\) is sharp whenever an arithmetic progression of length \(s\) is used. A proper-support window is informationally complete if its support is a difference cover, without requiring a classical constant-multiplicity difference set. For example, \(S=\{0,1,2,5\}\) in \(\mathbb F_{11}\) has all eleven differences, but unequal nonzero difference multiplicities. **Every** assignment of positive rational weights to these four sites gives an injective \(121\)-measurement lifting.

## Assumptions and scope

All primes are odd; entries of \(g\) are rational and nonnegative, with at least one positive entry. \(\mathcal L_g\) is a complex-linear operator acting on all \(p\times p\) complex matrices, not only Hermitian matrices. The phase-retrieval assertion concerns arbitrary signals in \(\mathbb C^p\), including vectors with zeros; no stability lower bound uniform over positive rational weights is asserted. An empty support is excluded.

## Proof

**Cyclotomic lemma.** Fix a primitive \(p\)-th root \(\zeta\). If \(c_0,\ldots,c_{p-1}\in\mathbb Q\) and \(b\neq0\pmod p\), then
\[
\sum_{x=0}^{p-1}c_x\zeta^{bx}=0
\quad\Longleftrightarrow\quad c_0=c_1=\cdots=c_{p-1}.
\]
Indeed the polynomial \(\sum_x c_{b^{-1}x}X^x\), degree at most \(p-1\), vanishes at \(\zeta\), so it is a rational multiple of the irreducible cyclotomic polynomial \(\Phi_p(X)=1+X+\cdots+X^{p-1}\). For \(b=0\), a nonnegative coefficient sum vanishes exactly when every summand vanishes.

Apply this lemma to \(c_x=g_xg_{x-a}\), a nonnegative rational sequence. If \(S\) is proper, some \(c_x=0\) for every \(a\), because the support of \(c\) lies inside \(S\). Thus for nonzero \(b\), vanishing forces every \(c_x=0\); for \(b=0\) the same conclusion follows by nonnegativity. Finally \(c\equiv0\) exactly when \(S\cap(a+S)=\varnothing\), equivalently \(a\notin D\). This proves the asserted complete zero pattern for proper support.

If \(S=\mathbb F_p\), then every \(c_x>0\), hence \(A_g(a,0)>0\). For \(b\neq0\), the cyclotomic lemma says \(A_g(a,b)=0\) exactly when \(g_xg_{x-a}\) is constant in \(x\). If \(a=0\), positivity implies that \(g_x\) is constant. For \(a\neq0\), let the common product be \(C>0\). From \(g_xg_{x-a}=g_{x-a}g_{x-2a}=C\) and \(g_{x-a}>0\), one obtains \(g_x=g_{x-2a}\). Since \(2a\neq0\) generates the cyclic group \(\mathbb F_p\), \(g\) must be constant. Conversely a constant window has \(A_g(a,b)=0\) for every \(a\) and every \(b\neq0\).

**Operator spectrum and kernel.** The \(p^2\) Weyl operators \(W_{a,b}=M_bT_a\) form an orthogonal Hilbert--Schmidt basis with \(\|W_{a,b}\|_{HS}=\sqrt p\). Conjugation by \(W_{t,k}\) acts diagonally on this basis by the distinct characters \(\zeta^{bt-ak}\). Hence, for \(P_{t,k}=v_{t,k}v_{t,k}^*\), the values \(\operatorname{tr}(W_{a,b}P_{t,k})\) are a character on \(\mathbb F_p^2\) times the seed overlap \(\operatorname{tr}(W_{a,b}gg^*)\). Its modulus is \(|A_g(a,b)|\): conjugations, shifts and complex conjugation affect only a unit-modulus phase or change \((a,b)\) bijectively. Fourier orthogonality of these \(p^2\) characters gives the singular values \(\sqrt p|A_g(a,b)|\) of \(\mathcal L_g\), and its Weyl-basis kernel is exactly the zero-coefficient span (with the same parameter convention for \(W_{a,b}\)); this also follows directly from the standard spreading-function calculation in [1]. Counting the zeros already classified proves both rank cases and all kernel formulas.

**Necessity and sufficiency for phase retrieval.** If \(\mathcal L_g\) is injective and the measured intensities for \(f\) and \(h\) agree, then \(ff^*=hh^*\), so \(h\) equals \(f\) up to a unit scalar. Conversely, for proper \(S\) missing a nonzero difference \(a\), no translate of \(S\) meets both \(0\) and \(a\). Thus the two non-proportional signals \(e_0+e_a\) and \(e_0+i e_a\) have identical Gabor intensities. For a constant full-support window, all translates are constant and measurements reduce to Fourier magnitudes; \(e_0\) and \(e_1\) have identical intensities. These exhaust the noninjective cases.

**Sharp support bound and example.** The Cauchy--Davenport inequality gives \(|S-S|\ge\min(p,2s-1)\); arithmetic progressions attain equality as long as \(2s-1\le p\), and once \(2s-1\ge p\) every support already has full difference cover. Direct subtraction modulo \(11\) shows that \(\{0,1,2,5\}-\{0,1,2,5\}=\mathbb F_{11}\), but difference \(1\) occurs twice while difference \(2\) occurs once. The classification therefore applies regardless of the four rational weights.

## Verification

The accompanying `verify.py` independently constructs the full \(p^2\)-by-\(p^2\) intensity lifting, computes its numerical singular values and the ambiguity array, and compares them with exact support-theoretic ranks and predicted cyclotomic zeros. It passed \(348\) test windows over \(p\in\{3,5,7,11\}\), including exhaustive nonempty supports for \(3,5,7\) under multiple rational weightings. This is a finite consistency check only, not a substitute for the prime-uniform proof above. Run `python verify.py` with NumPy installed.

## Relationship to prior work

Bojarovska and Flinth [1] establish the full Gabor nonvanishing-ambiguity criterion and diagonal lifting bounds (their Theorems 2.2--2.3), construct characteristic windows from classical difference sets (Proposition 2.2), and prove phase-retrieval obstructions for missing ambiguity bands (Proposition 2.3). Those results supply important machinery and implications. The present statement specializes the coefficient arithmetic differently: it classifies **all** nonnegative rational windows in odd prime dimensions and gives a support-only rank/kernel formula, a full-support constant-versus-nonconstant dichotomy, and non-difference-set examples with arbitrary rational weights. It does not claim invention of the Weyl singular values or general phase-retrieval criterion. Feichtinger, Kozek and Luef [2] supply general finite-group Gabor/spreading theory, not this coefficient-specific rank classification. The elementary cyclotomic and Cauchy--Davenport inputs are classical.

## Limitations

Rationality and positivity play distinct essential roles. The result cannot extend to arbitrary positive real weights: for any prime \(p\ge5\) and \(0<\varepsilon<1\), set \(g_x=\sqrt{1+\varepsilon\cos(4\pi x/p)}\). Then \(g\) is positive and nonconstant with full support, but \(A_g(0,1)=0\). Allowing negative rational weights can similarly invalidate positivity-based noncancellation at zero frequency. Rank statements give no field-independent or weight-independent lower bound on the smallest positive singular value. Historical equivalence to an unstated specialization of classical Gabor/cyclotomic literature remains a priority risk; no independent literature certification is asserted.

## References

[1] I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800, first posted 2015-03-19; especially §§2.2--2.4. https://arxiv.org/abs/1503.05800

[2] H. G. Feichtinger, W. Kozek and F. Luef, *Gabor analysis over finite Abelian groups*, arXiv:math/0703228, first posted 2007-03-08. https://arxiv.org/abs/math/0703228

[3] Classical prime cyclotomic irreducibility and the Cauchy--Davenport inequality, used in their elementary standard forms.
