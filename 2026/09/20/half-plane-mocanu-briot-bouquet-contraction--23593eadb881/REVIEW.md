# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The proof was rederived from the normalized half-plane formulation rather than relying on the disputed general-convex-domain machinery. If an affine map sends the target half-plane to the right half-plane and fixes the normalized value 1, then it preserves the signed combination defining \(\mathcal K_\mu\). The source's classical criterion therefore becomes
\[
Q\in\mathcal K_\mu(h_0)
\iff
\int_0^{2\pi}|\operatorname{Re}Q(re^{it})|\,dt\le(4\mu-2)\pi
\quad(0<r<1).
\]

The parameter reduction was checked directly. Writing the target half-plane as \(B+A\{\operatorname{Re}\zeta>0\}\), the hypothesis
\[
\operatorname{Re}\{\beta(B+A\zeta)+\gamma\}\ge0
\quad(\operatorname{Re}\zeta>0)
\]
forces \(c=\beta A\) to be positive real: a nonzero imaginary part is impossible because \(\operatorname{Im}\zeta\) is unrestricted, and a negative real value is impossible as \(\operatorname{Re}\zeta\to\infty\). It also gives \(\operatorname{Re}(\beta B+\gamma)\ge0\), hence \(a=(\beta B+\gamma)/c\) has nonnegative real part.

The transformed differential expression is exactly
\[
R=Q+\frac1c\frac{zQ'}{Q+a}.
\]
Analyticity of the original expression forces \(Q+a\) to be zero-free: a zero at a nonzero point would produce a nonremovable pole in its logarithmic derivative, and the value at zero is \(1+a\ne0\).

For the key contraction, set \(W=Q+a\), \(\alpha=\operatorname{Re}a\), and let \(\theta=\arg W\) on a circle. The identity
\[
\frac{d\theta}{dt}=\operatorname{Re}\frac{zW'}W
\]
is exact. The dual lower bound reduces the desired inequality to
\[
J=\int\operatorname{sgn}(\operatorname{Re}W-\alpha)\,d\arg W\ge0.
\]
When \(\alpha=0\), zero winding of a zero-free analytic function makes this integral exactly zero via a periodic primitive of \(\operatorname{sgn}(\cos\theta)\). When \(\alpha>0\), smooth approximation and Stokes' theorem give
\[
J_\varepsilon=
\iint s_\varepsilon'(X-\alpha)
\frac{X|W'|^2}{|W|^2}\,dA\ge0,
\]
because the derivative of the cutoff is supported where \(X>\alpha-\varepsilon>0\). The limiting step is legitimate on each fixed circle because the boundary functions are smooth and the zero set of \(\operatorname{Re}Q\) has measure zero unless it is identically zero; the latter is excluded by its mean value \(\operatorname{Re}Q(0)=1\).

No interpolation, duality, or standard differential-subordination theorem located in the search immediately subsumes the signed \(L^1\) estimate. The argument is therefore not a restatement of the classical \(\mu=1\) Carathéodory implication.

## Originality

PASS, to the best of our knowledge.

Dziok's 2013 article was inspected at Problem 1 and Remark 2. It explicitly presents the nonlinear implication as open after proving the linear case. The 2014 erratum was also inspected in full; it only adds an assumption to Lemma 1 and Theorem 3 and does not change Problem 1. Dziok and Noor's 2017 paper was inspected at its corresponding Problem 1; it generalizes the setup to two convex targets and says that the \(\beta\ne0\) problem is still open and “seems to be false.”

Searches covered the exact nonlinear expression, the 2013 and 2017 titles and DOIs, “bounded Mocanu variation,” “bounded boundary rotation,” “Briot-Bouquet differential subordination,” half-plane targets, Paatero/Pinchuk terminology, and later citing papers. The 2015 Dziok paper *Generalizations of multivalent Mocanu functions* was inspected through its available full-text rendering; it contains a standard differential-subordination lemma but no located version of the boundary-winding \(L^1\) contraction. The 2020 Aghalary–Kazemzadeh paper cites both the 2013 and 2017 sources while developing another bounded-Mocanu generalization; no located later source states the present half-plane theorem.

The main residual risk is prior coverage phrased as a Hardy-space or boundary-rotation norm inequality rather than as a solution of Dziok's problem. No specific inaccessible source was found with concrete evidence that it contains the present result.

## Value

PASS.

The finding resolves a broad, natural branch of an explicit nonlinear open problem: every normalized half-plane target and every \(\mu\ge1\). The result also isolates a reusable mechanism. The logarithmic derivative contributes the angular velocity of a zero-free analytic curve, and Stokes converts its signed boundary contribution at a positive vertical level into a nonnegative area integral. This explains structurally why the half-plane case survives the nonlinear transform even though the later two-target problem was suspected to fail in general.

## Limitations

- General convex targets are not settled.
- The two-distinct-target version from Dziok–Noor is not settled.
- Equality in the contraction lemma is not classified.
- Equivalent prior coverage under different Hardy-space or boundary-rotation language cannot be ruled out exhaustively.
