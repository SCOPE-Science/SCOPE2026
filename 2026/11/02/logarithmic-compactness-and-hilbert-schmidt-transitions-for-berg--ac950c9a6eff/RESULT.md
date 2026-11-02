# Logarithmic compactness and Hilbert–Schmidt transitions for Bergman-kernel Cesàro operators

## Finding
Let \(s>1\) and \(\gamma\in\mathbb R\). Consider the Bergman-kernel-induced operator \(T_{s,\gamma}\) on the Hardy space \(H^2(\mathbb D)\), initially defined on polynomials by
\[
(T_{s,\gamma}f)(z)=\int_0^1 \frac{f(tz)(1-t)^{s-1}}{(1-tz)^s\,[\log(e/(1-t))]^{\gamma}}\,dt.
\]
Then \(T_{s,\gamma}\) is unbounded if \(\gamma<0\), bounded and noncompact if \(\gamma=0\), and compact if \(\gamma>0\). Among compact cases it is Hilbert–Schmidt precisely for \(\gamma>1/2\). Thus the entire interval \(0<\gamma\le1/2\) gives compact operators that are not Hilbert–Schmidt.

Writing \(P_N\) for the orthogonal projection onto \(\operatorname{span}\{1,z,\ldots,z^N\}\), the sharp transition constants are
\[
\lim_{N\to\infty}\frac{\|P_NT_{s,\gamma}\|_{\mathcal S_2}^2}{(\log N)^{1-2\gamma}}=\frac1{(2s-1)(1-2\gamma)} \quad (\gamma<1/2),
\]
\[
\lim_{N\to\infty}\frac{\|P_NT_{s,1/2}\|_{\mathcal S_2}^2}{\log\log N}=\frac1{2s-1},\qquad
\lim_{\gamma\downarrow1/2}(2\gamma-1)\|T_{s,\gamma}\|_{\mathcal S_2}^2=\frac1{2s-1}.
\]
At the bounded noncompact boundary, \(\|T_{s,0}\|=\|T_{s,0}\|_{\rm ess}=\mathrm B(1/2,s)\). The operator-norm identity for the equivalent classical Cesàro matrix is known; the new assertion is the full logarithmic compactness/Schatten transition and its exact quantitative constants.

## Assumptions and scope
The Hardy norm is \(\|\sum_{k\ge0}a_kz^k\|_{H^2}^2=\sum_{k\ge0}|a_k|^2\). Here \(\mathcal S_2\) denotes the Hilbert–Schmidt class, \(\mathrm B(x,y)=\Gamma(x)\Gamma(y)/\Gamma(x+y)\), \(P_N\) is the *output* Fourier truncation, and \(s>1\) is arbitrary real, with standard weighted Bergman kernel \((1-tz)^{-s}\) corresponding to Bergman weight exponent \(s-2>-1\). No assertion is made for the kernel exponent \(s\le1\), other measure classes, or other Schatten exponents.

Set
\[
b_j=\frac{\Gamma(j+s)}{\Gamma(s)\Gamma(j+1)},\quad
m_n(\gamma)=\int_0^1 t^n(1-t)^{s-1}[\log(e/(1-t))]^{-\gamma}\,dt.
\]
The matrix on \(\{z^k\}\) is \((T_{s,\gamma})_{nk}=m_n(\gamma)b_{n-k}\) for \(0\le k\le n\), and zero otherwise. The integral defines an analytic function of \(z\in\mathbb D\) for polynomial inputs. The unbounded case means this densely defined polynomial operator admits no bounded extension on \(H^2\).

## Proof
**1. Exact coefficients and asymptotics.** Expanding \((1-tz)^{-s}=\sum_{j\ge0}b_jt^jz^j\) and integrating termwise on compact subdisks gives the stated triangular matrix. Set \(u=n(1-t)\) in the moment integral. Standard dominated convergence gives, for each real \(\gamma\),
\[
 m_n(\gamma)=\Gamma(s)n^{-s}(\log n)^{-\gamma}(1+o(1)). \tag{1}
\]
Indeed \((1-u/n)^n\to e^{-u}\), and on the main range \(n^{-1/2}<u<n^{1/2}\), the logarithmic factor divided by \((\log n)^{-\gamma}\) converges pointwise to one; the excluded ranges are negligible by integrable power control at zero (since \(s>1\)) and the exponential decay at infinity. For \(\gamma\) in a fixed compact interval, splitting at \(u=n^{-1/2}\) and \(u=n^{1/2}\), and then using \(\log(e/(1-t))=\log n+1-\log u\), yields the locally uniform strengthening
\[
 m_n(\gamma)=\Gamma(s)n^{-s}(\log n)^{-\gamma}\bigl(1+O_s((1+|\gamma|)/\log n)\bigr),\quad n\to\infty.\tag{2}
\]
Here the implied constant can depend on the chosen compact \(\gamma\)-interval. The elementary gamma-ratio asymptotic and comparison of sums with integrals give
\[
b_j=\frac{j^{s-1}}{\Gamma(s)}(1+O_s(j^{-1})),\qquad
\sum_{j=0}^n b_j^2=\frac{n^{2s-1}}{(2s-1)\Gamma(s)^2}(1+o(1)).\tag{3}
\]
Consequently the squared norm of the \(n\)-th output row obeys
\[
R_n(\gamma):=m_n(\gamma)^2\sum_{j=0}^n b_j^2
=\frac{1+o(1)}{(2s-1)n(\log n)^{2\gamma}}.\tag{4}
\]
The error in (4) is \(O(1/\log n)\) uniformly when \(\gamma\) stays in a compact interval about \(1/2\). This makes the \(\gamma\downarrow1/2\) passage below legitimate.

**2. Boundedness and compactness.** At \(\gamma=0\), \(m_n(0)=\mathrm B(n+1,s)\); hence \(T_{s,0}\) is exactly \(1/s\) times the classical order-\(s\) Cesàro matrix, because
\[
\frac1s\frac{\binom{s+n-k-1}{n-k}}{\binom{s+n}{n}}
=\mathrm B(n+1,s)b_{n-k}.
\]
The standard sharp Hardy–Cesàro inequality gives \(\|T_{s,0}\|=\mathrm B(1/2,s)\); we explicitly treat this norm formula as established prior work. Moreover, for any \(\gamma\),
\[
T_{s,\gamma}=D_{s,\gamma}T_{s,0},\quad
D_{s,\gamma}=\operatorname{diag}(d_n),\quad
d_n=\frac{m_n(\gamma)}{m_n(0)}\sim(\log n)^{-\gamma}.
\]
For \(\gamma>0\), \(D_{s,\gamma}\) is compact, so \(T_{s,\gamma}\) is compact. For \(\gamma=0\), take normalized positive vectors supported on \(N\le k<2N\), with entries \(N^{-1/2}\). They converge weakly to zero. For \(2N\le n\le3N\), a fixed fraction of the summands satisfy \(n-k\asymp N\); (1) at \(\gamma=0\) and \(b_{n-k}\asymp N^{s-1}\) imply every such output coefficient is at least \(c_sN^{-1/2}\). Thus the output norm remains bounded below, proving noncompactness. The same test, with \(d_n\asymp(\log N)^{-\gamma}\), proves unboundedness for \(\gamma<0\).

For the claimed exact *essential* norm at \(\gamma=0\), the upper bound follows from the classical exact operator norm. For the reverse inequality, take positive logarithmic blocks \(f_k=k^{-1/2}\) on \(N\le k\le N e^L\), zero elsewhere, and normalize by \(\|f\|\sim\sqrt L\). For \(n\) in the central logarithmic subinterval \([Ne^a,Ne^{L-a}]\), the matrix's Riemann-sum approximation is
\[
(T_{s,0}f)_n=(\mathrm B(1/2,s)+o_{N\to\infty}(1)+O_s(e^{-a/2}))n^{-1/2},
\]
where \(a>0\) is fixed and the bound is uniform in that central subinterval. The omitted input fraction \(k<n e^{-a}\) contributes at most \(O_s(e^{-a/2})\), while the remaining Riemann sum tends the beta integral \(\int_0^1u^{-1/2}(1-u)^{s-1}du\). Hence for every \(L>2a\), the output has squared norm at least \((\mathrm B(1/2,s)-o(1)-O_s(e^{-a/2}))^2(L-2a)/L\). Let \(N\to\infty\), then \(L\to\infty\), then \(a\to\infty\). These input blocks converge weakly to zero, so every compact perturbation has norm at least \(\mathrm B(1/2,s)\). Thus the essential norm equals the known operator norm.

**3. Exact Schatten transition and coefficients.** Since the monomials form an orthonormal basis, Tonelli's theorem yields
\[
\|P_NT_{s,\gamma}\|_{\mathcal S_2}^2=\sum_{n=0}^N R_n(\gamma).
\]
Combining (4) with the integral test for \(1/[n(\log n)^{2\gamma}]\) gives the power and iterated-logarithm limits and the condition \(T_{s,\gamma}\in\mathcal S_2\iff\gamma>1/2\). To obtain the parameter-boundary limit, use the error form of (4), uniform for \(\gamma\) near \(1/2\). The row-error series is uniformly absolutely convergent because it is majorized by \(C/[n(\log n)^2]\). Its product with \(2\gamma-1\) therefore vanishes. Finally
\[
\lim_{\gamma\downarrow1/2}(2\gamma-1)\sum_{n\ge2}\frac1{n(\log n)^{2\gamma}}=1,
\]
which proves the asserted sharp Hilbert–Schmidt norm blow-up.

## Verification
The supplemental standard-library script `verify.py` checks exactly 200 consecutive \(s=2,\gamma=0\) row formulas and their finite harmonic-number sums, and checks 18 beta moments and nine asymptotic row scalings numerically. Executing it prints `EXACT_ROWS_OK 200`, `BETA_MOMENTS_OK 18`, `LOG_ROW_SCALE_OK 9`, and `ALL_CHECKS_OK`.

For an independent explicit normalization check, when \(s=2,\gamma=0\), \(m_n=1/[(n+1)(n+2)]\) and \(b_j=j+1\), whence
\[
R_n(0)=\frac{2n+3}{6(n+1)(n+2)},\qquad
\sum_{n=0}^N R_n(0)=\frac{H_{N+1}+H_{N+2}-1}{6}
\sim\frac13\log N.
\]
This matches \(1/(2s-1)=1/3\). Numerical tests do not prove the infinite-family assertions; Steps 1–3 do.

## Relationship to prior work
Blasco and Pennanen (2026, arXiv:2609.21657, first posted September 18) define the Bergman-kernel Cesàro operator in precisely the required generality and characterize Hardy/Bergman boundedness using tail and moment tests. Their inspected full text does not provide this Hardy-space compactness-versus-Hilbert–Schmidt phase, its exact logarithmic trace-growth coefficient, or its blow-up constant. The gamma-zero matrix is a rescaled *classical* order-\(s\) Cesàro matrix, and its sharp norm is credited to the Hardy–Cesàro theory, as recorded by Roopaei (2024). Mas, Merchán and de la Rosa (2024) treat a different Bergman-kernel-derived Cesàro operator whose kernel is integrated in the spatial variable before evaluation. Earlier Cauchy-kernel measure operators correspond to a different kernel exponent and do not directly imply the \(s>1\) sharp coefficient.

The nearest accessible research comparison in higher-dimensional Bergman balls establishes a Hilbert–Schmidt classification with a dimension-dependent transition for a different underlying Hilbert space and operator normalization; its statement does not imply (4) for \(H^2(\mathbb D)\). The classical Cesàro norm and elementary diagonal compactness principle are not presented as new.

## Limitations
The result concerns only the positive power-logarithmic measure family and the standard radial Bergman kernel on the disk, with input/output \(H^2\) and \(s>1\). The work does not classify arbitrary slowly varying measures, general Schatten \(\mathcal S_p\) membership, or numerical singular-value asymptotics. Possible equivalent logarithmic estimates in older, incompletely indexed sources remain an originality risk. Self-review was conducted; independent audit has not been performed.

## References
1. O. Blasco and A. Pennanen, *Cesàro operator induced by a Bergman kernel*, arXiv:2609.21657v1 (public September 18, 2026), https://arxiv.org/html/2609.21657v1.
2. H. Roopaei, *Factorization of Hausdorff Operators*, Axioms 13 (2024), 813, https://doi.org/10.3390/axioms13120813. Section 4 records the classical generalized Cesàro \(\ell_p\) norm.
3. A. Mas, N. Merchán and E. de la Rosa, *Generalized Cesàro operator acting on Hilbert spaces of analytic functions*, Ann. Funct. Anal. 15 (2024), article 56, https://doi.org/10.1007/s43034-024-00365-6.
4. P. Galanopoulos, D. Girela and N. Merchán, *Cesàro-type operators associated with Borel measures on the unit disc acting on some Hilbert spaces of analytic functions*, J. Math. Anal. Appl. 526 (2023), 127287.
