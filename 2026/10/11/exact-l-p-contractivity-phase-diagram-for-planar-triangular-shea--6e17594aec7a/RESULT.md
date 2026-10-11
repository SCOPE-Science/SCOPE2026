# Exact \(L^p\) contractivity phase diagram for planar triangular shears
## Finding
Let \(a,c>0\), \(b\ge0\), and \(M_{a,b,c}=\begin{pmatrix}-a&b\\0&-c\end{pmatrix}\). For \(1<p<\infty\), the numerical abscissa, equivalently the logarithmic norm induced by \(\ell_p^2\), is \(\omega_p(M_{a,b,c})=\sup_{r\ge0}(-a+br-cr^p)/(1+r^p)\); at \(p=1\), \(\omega_1(M_{a,b,c})=\max\{-a,b-c\}\). Define \(\beta_1(a,c)=c\) and, for \(1<p<\infty\), \(\beta_p(a,c)=p\,a^{(p-1)/p}c^{1/p}/(p-1)^{(p-1)/p}\). Then \(\omega_p<0\), \(=0\), or \(>0\) exactly as \(b<\beta_p\), \(b=\beta_p\), or \(b>\beta_p\). The function \(p\mapsto\beta_p(a,c)\) increases strictly on \(1<p<1+a/c\), decreases strictly on \(p>1+a/c\), has maximum \(a+c\), and tends to \(a\) as \(p\to\infty\). Consequently, if \(\max\{a,c\}<b<a+c\), there are exactly two critical exponents \(p_-<1+a/c<p_+\), and prefactor-one contractivity holds exactly for \(p_-<p<p_+\). For the focal matrix \(M_{1,9,10}\), there is a unique critical exponent \(p_*>1.1\) determined by \(\beta_{p_*}(1,10)=9\), with strict prefactor-one exponential decay for \(1\le p<p_*\) and initial norm growth for \(p>p_*\). The same numerical abscissa governs constant-matrix multiplication on \(L^p((0,1);\ell_p^2)\), and whenever \(\omega_p<0\), the largest \(\gamma\) for which \(\|\exp(tM_{a,b,c})\|_{p\to p}\le\exp(-\gamma t)\) for every \(t\ge0\) is \(\gamma=-\omega_p(M_{a,b,c})\).

## Assumptions and scope
Assume \(a,c>0\) and \(b\ge0\). The matrix acts on the complex Banach plane \(\ell_p^2\); for finite \(p\), its constant-matrix multiplication operator acts on \(L^p((0,1);\ell_p^2)\). The recent focal source studies the special matrix \(M_{1,9,10}\) at \(p=1\) and \(p=2\). The theorem classifies the full finite-\(p\) scale for the natural three-parameter stable upper-triangular family. The eigenvalues remain \(-a\) and \(-c\); the issue is norm contractivity and transient growth, not spectral stability.

Write \(\omega_p(M)\) for the Banach-space numerical abscissa. For bounded matrices it equals the logarithmic norm induced by the same vector norm,
\[
\omega_p(M)=\lim_{h\downarrow0}\frac{\|I+hM\|_{p\to p}-1}{h}.
\]

## Proof
Fix \(1<p<\infty\). For a unit vector \(x=(x_1,x_2)\in\ell_p^2\), the unique norming functional is
\[
J_p(x)=\bigl(|x_1|^{p-2}\overline{x_1},|x_2|^{p-2}\overline{x_2}\bigr).
\]
With \(s=|x_1|\), \(t=|x_2|\), and \(s^p+t^p=1\), phase alignment gives
\[
\operatorname{Re}J_p(x)(M_{a,b,c}x)\le -a s^p-c t^p+b s^{p-1}t,
\]
and equality is attainable. Setting \(r=t/s\) yields
\[
\omega_p(M_{a,b,c})=\sup_{r\ge0}\frac{-a+br-cr^p}{1+r^p}.
\]
The denominator is positive, so \(\omega_p<0\) exactly when \(br<a+cr^p\) for every \(r>0\), equivalently
\[
b<\inf_{r>0}\left(\frac ar+c r^{p-1}\right).
\]
The expression has the unique minimizer
\[
r_0=\left(\frac{a}{c(p-1)}\right)^{1/p},
\]
which gives
\[
\beta_p(a,c)=\frac{p\,a^{(p-1)/p}c^{1/p}}{(p-1)^{(p-1)/p}}.
\]
At equality the scalar numerator vanishes at \(r_0\), so \(\omega_p=0\); above the threshold it is positive. For \(p=1\), the column-sum logarithmic-norm formula gives \(\omega_1=\max\{-a,b-c\}\), hence the same trichotomy with \(\beta_1=c\).

For \(1<p<\infty\),
\[
\frac{d}{dp}\log\beta_p=-\frac1{p^2}\log\!\left(\frac ca(p-1)\right).
\]
Thus \(\beta_p\) increases strictly up to \(p_0=1+a/c\), decreases strictly afterwards, and direct substitution gives \(\beta_{p_0}=a+c\). Also \(\beta_p\to c\) as \(p\downarrow1\) and \(\beta_p\to a\) as \(p\to\infty\). Therefore \(\max\{a,c\}<b<a+c\) produces exactly two crossings and a middle contractive interval.

For \(M_{1,9,10}\), one has \(\beta_1=10>9\), \(p_0=1.1\), \(\beta_{p_0}=11\), and \(\lim_{p\to\infty}\beta_p=1<9\). Strict decrease after \(p_0\) gives one unique crossover \(p_*>1.1\).

If \(B_p\) denotes multiplication by \(M_{a,b,c}\) on \(L^p((0,1);\ell_p^2)\), pointwise domination and constant-function witnesses give \(\|\exp(tB_p)\|=\|\exp(tM_{a,b,c})\|_{p\to p}\). The logarithmic-norm inequality gives \(\|\exp(tM)\|\le\exp(t\omega_p(M))\). Conversely, any bound with prefactor one and exponent \(\gamma\) forces \(\omega_p(M)\le-\gamma\) by the right derivative at \(t=0\). Hence the optimal exponent is exactly \(-\omega_p(M)\) whenever \(\omega_p(M)<0\).

## Verification
The proof is symbolic. The numerical-range problem is reduced exactly to one scalar ratio; the sign threshold is obtained from a unique one-variable minimizer; and the exponent phase diagram follows from the exact derivative of \(\log\beta_p\). No finite sampling is used to infer an infinite statement.

The focal endpoint values are recovered exactly:
\[
\omega_1(M_{1,9,10})=-1,\qquad\omega_2(M_{1,9,10})=\frac{9\sqrt2-11}{2}>0.
\]

## Relationship to prior work
Boubaker, Gernandt, and Selmi develop numerical ranges for linear relations and use the fixed matrix \(M_{1,9,10}\) to compare semigroup behavior in the \(p=1\) and \(p=2\) geometries. Their example establishes decay at one endpoint and transient growth at the other. The inspected source does not give the intermediate-\(p\) crossover, the general \((a,b,c)\) threshold, or the two-crossing reentrant regime.

Classical logarithmic-norm theory supplies the equivalence between numerical abscissa, infinitesimal norm growth, and prefactor-one semigroup estimates. It does not by itself state this specialized parameter/exponent phase diagram.

## Limitations
The theorem is restricted to constant \(2\times2\) upper-triangular shears and induced \(\ell_p\) norms. It does not classify larger matrices, time-dependent coefficients, weighted norms, or optimal exponential bounds with prefactors greater than one. An older equivalent calculation may exist under logarithmic-norm, matrix-measure, dissipativity, Lozinskii-measure, or contraction terminology.

## References
1. W. Boubaker, H. Gernandt, and W. Selmi, *On the Numerical Range of Linear Relations in Banach Spaces*, arXiv:2608.19913v1, 2026.
2. G. Söderlind, *The logarithmic norm. History and modern theory*, BIT Numerical Mathematics 46 (2006), 631--652, DOI:10.1007/s10543-006-0069-9.
