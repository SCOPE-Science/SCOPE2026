# Parity classification of Fourier zeros for phase-only consecutive quadrinomials
## Finding
Let \(N\ge 4\), let \(\zeta_N=e^{2\pi i/N}\), and let \(f:\mathbb Z_N\to\mathbb C\) have support exactly \(\{0,1,2,3\}\). Assume the four nonzero values of \(f\) have one common magnitude. Then
\[
\#\{k\in\mathbb Z_N:\widehat f(k)=0\}\in
\begin{cases}
\{0,1,2\},&N\text{ odd},\\
\{0,1,2,3\},&N\text{ even},
\end{cases}
\]
and every listed value occurs. Equivalently, the attainable Fourier-support sizes are \(\{N,N-1,N-2\}\) for odd \(N\ge5\), and \(\{N,N-1,N-2,N-3\}\) for even \(N\ge4\).

The key structural statement is independent of \(N\): if a cubic has four coefficients of one common nonzero modulus and has three roots on the unit circle, then two of those roots are antipodal. Conversely, three unit-circle roots containing an antipodal pair determine, after unimodular scaling, a cubic whose four coefficients have one common modulus.

## Assumptions and scope
Use the Fourier convention
\[
\widehat f(k)=\sum_{j\in\mathbb Z_N} f(j)\zeta_N^{-jk}.
\]
Changing the sign in the exponent only permutes the samples, so the zero count is convention-independent. Multiplying \(f\) by a nonzero scalar does not change its Fourier zeros; hence the common coefficient magnitude may be normalized to \(1\). The restriction \(N\ge4\) ensures that \(0,1,2,3\) are distinct support points in \(\mathbb Z_N\).

## Proof
Write
\[
P(z)=a_0+a_1z+a_2z^2+a_3z^3,\qquad |a_0|=|a_1|=|a_2|=|a_3|=1.
\]
The Fourier zero count equals the number of roots of \(P\) in the finite set \(\mu_N=\{z:z^N=1\}\), because \(\{\zeta_N^{-k}:k\in\mathbb Z_N\}=\mu_N\). A cubic has at most three such roots.

Suppose first that all three roots \(r_1,r_2,r_3\) of \(P\) lie on the unit circle. After division by \(a_3\), Vieta's formulas give
\[
P(z)/a_3=z^3-e_1z^2+e_2z-e_3,
\]
where \(e_1=r_1+r_2+r_3\), \(e_2=r_1r_2+r_1r_3+r_2r_3\), and \(e_3=r_1r_2r_3\). Since \(|r_j|=1\),
\[
e_2=e_3\,\overline{e_1},
\]
so \(|e_2|=|e_1|\), while \(|e_3|=1\). Thus the four coefficient moduli are all \(1\) exactly when \(|e_1|=1\).

Rotate the roots so that \(r_1=1\), and write \(r_2=e^{i\alpha}\), \(r_3=e^{i\beta}\). The condition \(|1+e^{i\alpha}+e^{i\beta}|=1\) is equivalent to
\[
1+\cos\alpha+\cos\beta+\cos(\alpha-\beta)=0.
\]
Putting \(s=(\alpha+\beta)/2\) and \(d=(\alpha-\beta)/2\), the left side factors as
\[
2\cos d\,(\cos s+\cos d).
\]
If \(\cos d=0\), then \(r_2=-r_3\). If \(\cos s=-\cos d\), then \(s\equiv \pi\pm d\pmod{2\pi}\), so either \(r_2=-r_1\) or \(r_3=-r_1\). Hence an antipodal pair is necessary. It is also sufficient: if the roots are \(u,-u,v\), then
\[
e_1=v,\qquad e_2=-u^2,\qquad e_3=-u^2v,
\]
and all three have modulus \(1\).

It remains to realize the possible finite-grid counts. A root triple of the form \(\{u,-u,v\}\) always gives a phase-only cubic. For zero Fourier zeros, choose \(u,v\) so that none of \(u,-u,v\) lies in \(\mu_N\). For one zero, take \(v\in\mu_N\) and choose \(u\) with \(u,-u\notin\mu_N\). For two zeros when \(N\) is odd, take distinct \(r,s\in\mu_N\) and the root triple \(\{r,-r,s\}\); because \(-r\notin\mu_N\), exactly \(r,s\) are sampled zeros. For two zeros when \(N\) is even, take an antipodal pair \(r,-r\in\mu_N\) and choose \(v\notin\mu_N\). Finally, three sampled zeros occur exactly when an antipodal pair belongs to \(\mu_N\), which is possible exactly when \(-1\in\mu_N\), i.e. exactly when \(N\) is even. For even \(N\ge4\), choose distinct roots \(1,-1,\zeta_N\). This proves both necessity and attainability.

## Verification
The accompanying verifier independently constructs witnesses for every asserted zero count for each \(4\le N\le300\), checks that every polynomial coefficient has modulus \(1\), evaluates every Fourier sample, and confirms the predicted counts. This finite replay is corroborative only; the all-\(N\) conclusion is supplied by the analytic antipodal-pair proof above.

## Relationship to prior work
Neuwirth's 2007 trigonometric-trinomial work studies continuous maximum-modulus and phase-extremal questions for spectra of size three, including unimodular Fourier multipliers and Sidon constants. Its objects have three Fourier coefficients, so it does not state the four-coefficient root classification here. The later four-frequency Sidon problem for \(\{0,1,2,3\}\) optimizes a continuous supremum norm and is explicitly a different extremal problem; finite sampled zero multiplicities are not its asserted invariant. General work on self-inversive polynomials gives criteria for all roots to lie on the unit circle, but does not provide this equal-coefficient-modulus antipodal classification or its exact parity consequence on \(\mu_N\).

## Limitations
The theorem is specific to four consecutive support points and equal coefficient magnitudes. It does not classify arbitrary four-point supports, unequal magnitudes, multiplicities away from the sampled roots, or continuous maximum-modulus behavior. The literature search cannot exclude differently indexed older sequence-design or cyclotomic literature that may contain an equivalent special case.

## References
1. S. Neuwirth, *The maximum modulus of a trigonometric trinomial*, arXiv:math/0703236, first submitted 2007-03-08; Journal d'Analyse Mathématique 104 (2008), 371-396.
2. M. N. Lalín and C. J. Smyth, *Unimodularity of zeros of self-inversive polynomials*, arXiv:1201.0774, first submitted 2012-01-03; Acta Mathematica Hungarica 138 (2013), 85-101.
3. S. Neuwirth, *On the (Fourier analytic) Sidon constant of \(\{0,1,2,3\}\)*, arXiv:2603.28229, first submitted 2026-03-30.
