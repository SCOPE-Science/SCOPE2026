# Sharp sixth-moment phase contrast for analytic trinomials

## Finding
For nonnegative magnitudes \(A,B,C\), not all zero, consider all analytic trinomials \(P(z)=a+bz+cz^2\) with \(|a|=A\), \(|b|=B\), and \(|c|=C\). Integrals on the unit circle use normalized Haar measure. Define the fixed-magnitude phase contrast
\[
\mathcal D(A,B,C)=\frac{\max_{\arg a,\arg b,\arg c}\int_{\mathbb T}|P(z)|^6\,dm(z)}{\min_{\arg a,\arg b,\arg c}\int_{\mathbb T}|P(z)|^6\,dm(z)}.
\]
Then
\[
\boxed{1\le\mathcal D(A,B,C)\le R_*:=1+\frac{24t_*(t_*+3)}{(t_*+2)(t_*^2+4t_*+10)}=3.7977375224747556\ldots,}
\]
where \(t_*=2.6807222254986205\ldots\) is the unique positive root of
\[
t^4+6t^3-40t-60=0.
\]
Equality in the upper bound holds precisely for \(A=C>0\) and \(B^2=t_*A^2\). For these magnitudes, the maximizing phases obey \(b^2/(ac)>0\) and minimizing phases obey \(b^2/(ac)<0\), with both ratios real. Thus the sharp ratio of the maximum to minimum sixth **norm** (rather than sixth moment) is \(R_*^{1/6}=1.2490720514206386\ldots\). If any of \(A,B,C\) is zero, the contrast is one.

## Assumptions and scope
The coefficient phases vary independently while their magnitudes remain fixed. The integration measure is \(dm(e^{i\theta})=d\theta/(2\pi)\). The zero polynomial is excluded, so the denominator is positive. The degree-two analytic support \(\{0,1,2\}\) can be translated or rescaled to any three distinct integer frequencies in arithmetic progression: these operations preserve the normalized circle moment. The theorem concerns the sixth moment and does not assert analogous optimizing magnitudes for other exponents or general three-point supports.

## Proof
**Exact phase reduction.** Write \(A=|a|\), \(B=|b|\), and \(C=|c|\). Since \(\int|P|^6=\int|P^3|^2\), Parseval expresses the moment as the sum of squared moduli of the seven coefficients of \(P^3\):
\[
(a^3,\;3a^2b,\;3a(ac+b^2),\;b(6ac+b^2),\;3c(ac+b^2),\;3bc^2,\;c^3).
\]
A direct expansion gives
\[
\int_{\mathbb T}|P|^6\,dm=Q+K\cos\delta,\qquad \delta=2\arg b-\arg a-\arg c,
\]
where
\[
\begin{aligned}
Q={}&A^6+B^6+C^6+9(A^4B^2+A^4C^2+A^2B^4+A^2C^4+B^4C^2+B^2C^4)+36A^2B^2C^2,\\
K={}&6AB^2C(3A^2+2B^2+3C^2).
\end{aligned}
\]
In particular \(Q>K\) for all nonzero polynomials (the minimum integral cannot vanish), and the phase extrema are \(Q+K\) and \(Q-K\). If \(ABC=0\), then \(K=0\) and the contrast equals one. Otherwise \(K>0\) and the cosine has its unique maximum/minimum phase values at \(\delta\equiv0,\pi\pmod{2\pi}\), respectively.

**Endpoint balancing.** Suppose \(ABC>0\). Introduce
\[
S=\frac{A^2+C^2}{AC}\ge2,\qquad T=\frac{B^2}{AC}>0.
\]
Normalize by \((AC)^3\). Expansion gives
\[
\frac{Q-K}{(AC)^3}=H(S,T):=S^3+6S+9TS^2-18TS+18T+9T^2S-12T^2+T^3,
\]
while \(2K/(AC)^3=12T(3S+2T)\). Hence
\[
\mathcal D=1+\frac{12T(3S+2T)}{H(S,T)}.
\]
The denominator is strictly positive, because it equals the normalized minimum sixth moment. Differentiating the nonconstant fraction with respect to \(S\) and simplifying its numerator yields
\[
-36T\bigl(2S^3+12ST^2+5T^3+T(11S^2-14)\bigr).
\]
This is strictly negative for \(S\ge2\) and \(T>0\), because \(11S^2-14\ge30\). Thus for any fixed \(T\), the contrast is strictly maximized at \(S=2\), equivalent by arithmetic–geometric mean to \(A=C\).

**Global one-variable optimization.** On \(S=2\), the denominator factors as \(H(2,T)=(T+2)(T^2+4T+10)\), so
\[
\mathcal D(2,T)=1+\frac{24T(T+3)}{(T+2)(T^2+4T+10)}.
\]
The derivative is
\[
\frac{d\mathcal D(2,T)}{dT}=-\frac{24(T^4+6T^3-40T-60)}{(T+2)^2(T^2+4T+10)^2}.
\]
The numerator quartic has exactly one positive real root: its nonzero coefficient signs have one change, while its value at zero is negative and it tends to positive infinity. Consequently \(\mathcal D(2,T)\) increases strictly until \(T=t_*\), then decreases strictly. Its limits as \(T\to0^+\) and \(T\to\infty\) are both one. Therefore its unique global maximum occurs at \(T=t_*\). With \(S=2\), this means \(A=C>0\), \(B^2=t_*A^2\). The phase characterization above is necessary and sufficient. This proves the sharp constant and all equality cases.

## Verification
Run `python artifacts/verify.py` after installing the version-compatible dependency listed in `requirements.txt`. The script expands the cubic convolution symbolically, checks the normalized two-variable reduction, checks the strict-derivative factorization and quartic derivative, verifies the positive root numerically, and independently compares the Fourier integral with its closed formula in five cases using an 8192-point periodic trapezoidal rule. Its recorded terminal output appears in `artifacts/check_output.txt`. These finite numerical comparisons corroborate the exact symbolic calculations; the proof's positivity and uniqueness arguments establish the universal result.

## Relationship to prior work
The 2007 preprint of Neuwirth studies the maximum modulus of trigonometric trinomials, a supremum-norm and Sidon-constant problem rather than the sixth-moment fixed-magnitude phase-contrast ratio. Krenedits' 2010 preprint studies the Hardy–Littlewood majorant problem for three-term idempotents, emphasizing prescribed coefficient magnitudes and non-even exponents; it does not optimize the present sixth-moment ratio over unequal magnitudes.

The published mathematical results *Exact \(L^2\)-to-\(L^6\) Nikolskii constant for analytic quadratics* and *Sharp sixth moments and the order-seven transition for three-character progressions* determine the **maximum sixth moment divided by coefficient energy cubed** and its amplitude optimizer \(B^2/A^2=(\sqrt{105}-5)/4\). That is a different objective: it does not identify the minimum moment at fixed magnitudes or determine the ratio of the two phase extrema. The new contrast optimizer has \(B^2/A^2=t_*\), which differs from the energy-normalized maximizer. The published result *Even phase moments recover the normalized geometry of a three-frequency spectrum* gives a collision formula for unimodular trinomials, but fixes \(A=B=C\); it does not establish the non-unimodular global contrast bound. The earlier identities and cubic-convolution method themselves are not new claims.

## Limitations
The constant concerns one very specific natural invariant, the **worst multiplicative sensitivity of the sixth Fourier moment to coefficient phases at fixed coefficient magnitudes**. It does not imply new sharp Nikolskii constants, new Hardy–Littlewood majorant failures, or higher-degree phase contrast classifications. The proof is elementary after the cubic convolution is expanded. Older general metric-inequality literature—including Arestov's 1980 work—could conceal an equivalent ratio bound; its complete primary text was not available for assessment. The originality judgment is qualified pending independent expert comparison. All correctness and literature assessments here are not an independent mathematical audit.

## References
1. Stefan Neuwirth, *The maximum modulus of a trigonometric trinomial*, arXiv:math/0703236v1, first posted 2007-03-08.
2. Sándor Krenedits, *Three-term idempotent counterexamples in the Hardy–Littlewood majorant problem*, arXiv:1006.0409v1, first posted 2010-06-02, primary MSC 42A05.
3. *Exact \(L^2\)-to-\(L^6\) Nikolskii constant for analytic quadratics*, published mathematical record 0b2c2efe6412.
4. *Sharp sixth moments and the order-seven transition for three-character progressions*, published mathematical record 1a8e79d7e85a.
5. *Even phase moments recover the normalized geometry of a three-frequency spectrum*, published mathematical record 7849dda51c79.
6. V. V. Arestov, *Inequality of different metrics for trigonometric polynomials*, Mathematical Notes 27 (1980), 265–269, DOI 10.1007/BF01140526; not inspected in complete text.
