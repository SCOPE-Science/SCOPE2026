# Sharp even Schatten numerical-radius moments under circle covariance

## Finding
Let \(m\ge1\) be an integer, let \(0\le t\le1\), and put \(s=1-t\). If a compact operator \(T\) on a complex Hilbert space belongs to \(\mathcal S_{2m}\) and admits a circle grading \(U_\theta T U_\theta^*=e^{i\theta}T\) with unitaries \(U_\theta\) for every real \(\theta\), then its weighted Schatten numerical radius is exactly a single Schatten norm,
\[
 W_{t,2m}(T):=\sup_{\theta\in\mathbb R}
 \|t e^{i\theta}T+s e^{-i\theta}T^*\|_{2m}
 =\|tT+sT^*\|_{2m},
\]
and obeys the dimension-independent **sharp** inequality
\[
 \boxed{\ W_{t,2m}(T)^{2m}\le C_m(t)\|T\|_{2m}^{2m},\qquad
 C_m(t)=\sum_{k=0}^m\binom{m}{k}^{\!2}t^{2k}(1-t)^{2(m-k)}.\ }
\]
For \(m\ge2\) and \(0<t<1\), equality holds **only** for \(T=0\); nevertheless the coefficient \(C_m(t)\) cannot be decreased, even for finite-dimensional nilpotent shifts. For \(m=1\) or \(t\in\{0,1\}\), equality holds for every eligible \(T\). At \(t=1/2\), the sharp constant is \(C_m(1/2)=\binom{2m}{m}/4^m\).

The quartic case has the stronger exact defect identity
\[
 \boxed{\ C_2(t)\|T\|_4^4-W_{t,4}(T)^4
 =2t^2(1-t)^2\|T^*T-TT^*\|_2^2.\ }
\]
The inequality, equality classification, optimality, and quartic identity form a single sharp even-moment theorem.

## Assumptions and scope
The Hilbert space may be finite- or infinite-dimensional. The Schatten class \(\mathcal S_q\) has norm \(\|T\|_q=(\operatorname{Tr}|T|^q)^{1/q}\), with the usual trace on positive trace-class operators. Circle covariance means that for each real \(\theta\) a unitary \(U_\theta\) satisfies \(U_\theta T U_\theta^*=e^{i\theta}T\); a strongly continuous unitary circle representation is sufficient but not needed. Examples include finite or infinite strictly one-step block shifts between orthogonal graded levels, subject to the Schatten assumption. No commutativity between \(T\) and \(T^*\) is assumed.

## Proof
**1. Removal of the phase.** By covariance, \(U_\theta T^*U_\theta^*=e^{-i\theta}T^*\), so conjugation by \(U_\theta\) takes \(tT+sT^*\) to the operator in the supremum. Unitary invariance of the Schatten norm gives phase independence.

**2. Balanced-word trace bound.** Set \(S=\operatorname{Tr}((T^*T)^m)=\|T\|_{2m}^{2m}\) and \(R=tT+sT^*\). Then
\[
 \|R\|_{2m}^{2m}=\operatorname{Tr}((R^*R)^m),\qquad R^*R=t^2T^*T+s^2TT^*+ts(T^2+(T^*)^2).
\]
Expand the alternating product \((R^*R)^m\) into words of length \(2m\) in \(T\) and \(T^*\). A word with \(a\) occurrences of \(T\) and \(b\) of \(T^*\) is carried by unitary conjugation to \(e^{i(a-b)\theta}\) times itself. Every such word is trace class by the Schatten Hölder inequality; trace invariance then shows that its trace is zero unless \(a=b=m\). For every balanced word \(X_1\cdots X_{2m}\), noncommutative Schatten Hölder gives
\[
 \left|\operatorname{Tr}(X_1\cdots X_{2m})\right|
 \le \prod_{j=1}^{2m}\|X_j\|_{2m}=S.
\]
Every scalar coefficient in the expansion is nonnegative. The sum of coefficients of the balanced words is
\[
 \sum_{k=0}^m\binom mk^{\!2}t^{2k}s^{2m-2k}=C_m(t),
\]
as one sees by splitting the alternating product \((R^*R)^m\), or by extracting the constant coefficient of \((t z^{-1}+sz)^m(tz+sz^{-1})^m\). Therefore \(\operatorname{Tr}((R^*R)^m)\le C_m(t)S\).

**3. Strictness and equality.** For \(m\ge2\), write \(A=T^*T\), \(B=TT^*\), so \(A,B\in\mathcal S_m\), \(\operatorname{Tr}(A^m)=\operatorname{Tr}(B^m)=S\). In the balanced expansion of \(((tT^*+sT)(tT+sT^*))^m\) there is, with positive coefficient \(t^{2m-2}s^2\), the trace \(\operatorname{Tr}(A^{m-1}B)\). The Hölder inequality for positive \(\mathcal S_m\) operators is strict here unless \(A=B\), because equality with identical positive \(m\)-norms forces equality of the positive operators. Thus if \(A\ne B\), this single term lies strictly below \(S\), while all others are bounded above by \(S\), proving strictness.

If \(A=B\), then \(T\) is normal. A nonzero compact normal operator has a nonzero eigenvalue; circle covariance forces its entire rotational orbit to belong to the spectrum, impossible for a compact operator whose nonzero spectrum consists of discrete eigenvalues of finite multiplicity with no nonzero accumulation point. Hence a nonzero eligible \(T\) has \(A\ne B\). The cases \(m=1\) and \(t=0\) or \(1\) yield equality immediately by the balanced-word computation.

**4. Sharpness.** Let \(J_N\) denote the \(N\)-dimensional nilpotent shift \(J_N e_j=e_{j+1}\) for \(0\le j<N-1\), \(J_Ne_{N-1}=0\). Diagonal phase unitaries make it circle-covariant. Its Schatten moment is \(\|J_N\|_{2m}^{2m}=N-1\). Put \(R_N=tJ_N+sJ_N^*\). For any basis vector farther than \(2m\) from either endpoint, its contribution to \(\operatorname{Tr}((R_N^*R_N)^m)\) is the constant term of \((t z^{-1}+sz)^m(tz+s z^{-1})^m\), namely \(C_m(t)\). Only at most \(4m\) endpoint vectors differ; for fixed \(m,t\) their contributions are uniformly bounded because \(\|R_N\|\le1\). Thus
\[
 \lim_{N\to\infty}\frac{\|R_N\|_{2m}^{2m}}{\|J_N\|_{2m}^{2m}}=C_m(t).
\]
This proves that no smaller uniform coefficient works, although no nonzero Schatten member attains it in the strict regime.

**5. Exact fourth-moment defect.** When \(m=2\), the balanced terms in \(\operatorname{Tr}((R^*R)^2)\) are
\[
 \operatorname{Tr}((R^*R)^2)
 =(t^4+s^4)S+4t^2s^2\operatorname{Tr}(AB),
\]
where cyclicity identifies \(\operatorname{Tr}((T^*)^2T^2)=\operatorname{Tr}(AB)\). Since
\[
 \|A-B\|_2^2=2S-2\operatorname{Tr}(AB),
\]
subtracting from \(C_2(t)S=(t^4+s^4+4t^2s^2)S\) yields the claimed identity.

## Verification
The standalone Python 3 script `verification/verify_even_schatten.py` uses exact rational arithmetic and no external dependencies. It checks the balanced-word coefficient identity for every integer \(1\le m\le8\) at six rational weights; all positive moments \(1\le m\le5\) for shifts of size \(2\le N\le9\) and a genuinely non-scalar three-level block shift; exact inequality and strict/end-point cases; and the quartic commutator identity. Execution produces `GRADED_SCHATTEN_EXACT_BALANCED_WORDS_AND_COMMUTATOR_OK`. These finite checks are additional reproducibility evidence, not a substitute for the proof for all \(m\) and all Schatten operators.

## Relationship to prior work
Kittaneh, Sahoo and Stanković [1], first publicly available March 31, 2025, introduce and study inequalities for the Schatten numerical radius in their Section 4. Their general estimates do not give the binomial-square optimal coefficient for the entire class of circle-covariant operators, nor its all-even-moment rigidity and quartic defect identity. Zamani [2] develops the weighted Hilbert–Schmidt numerical radius at exponent two; the equality at \(m=1\) is consistent with that earlier treatment. Pal and Chandok [3] investigate weighted Schatten radii through generalized Aluthge transforms and obtain general estimates, but their inspected results do not cover this sharp symmetry-specific hierarchy. Related work on exact Schatten-fourth radii of finite scalar weighted shifts establishes a smaller, dimension-sensitive special-case optimization, not this all-even exponent bound on multi-level graded operators or the sharp asymptotic/nonattainment dichotomy.

The present result is **not** a claim that the coefficient is sharp for a fixed matrix size or for every prescribed set of shift weights, and does not address non-even Schatten exponents.

## Limitations
The circle covariance hypothesis is essential to the balanced-word argument, and all Schatten operators here are compact. The optimal coefficient is a *uniform supremum*, not an attained value except at the stated degeneracies. The fourth-order identity does not assert corresponding exact positive commutator identities at higher orders. Full priority cannot be established by database searches alone; an equivalent estimate in older operator-ideal or noncommutative moment literature remains possible. No independent verification or audit is claimed.

## References
[1] F. Kittaneh, S. Sahoo, H. Stanković, *On inequalities involving the spherical operator transforms*, arXiv:2503.24015, first posted 2025-03-31, https://arxiv.org/abs/2503.24015 .

[2] A. Zamani, *The weighted Hilbert-Schmidt numerical radius*, arXiv:2111.14222, https://arxiv.org/abs/2111.14222 .

[3] K. Pal, S. Chandok, *On weighted Schatten p-numerical radii via generalized Aluthge transformation*, arXiv:2610.11336, first posted 2026-10-08, https://arxiv.org/abs/2610.11336 .
