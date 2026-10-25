# Beta-prime energy law and critical-window crossover for differential Hilbert sections

## Finding
Fix \(-1<\alpha<0\). Write \(A^2_\gamma\) for the weighted Bergman Hilbert space with norm
\[
\|f\|_{A^2_\gamma}^2=\frac{\gamma+1}{\pi}\int_{|z|<1}|f(z)|^2(1-|z|^2)^\gamma\,dA(z),\qquad \gamma>-1,
\]
and let \(\mathcal H_2f(z)=\int_0^1f(s)/(1-sz)^2\,ds\) on polynomials. For \(N\ge2\) and fixed real \(\lambda\), put \(\beta_N=\alpha+2+\lambda/\log N\), and let \(T_{N,\lambda}\) be the square compression of \(\mathcal H_2:A^2_\alpha\to A^2_{\beta_N}\) onto the monomials of degrees at most \(N\) in both spaces.

Define the positive finite measure on \([0,1]\times(0,\infty)\) by
\[
\mu_{N,\lambda}=\frac1{\log N}\sum_{n=1}^N\sum_{k=1}^N|b_{nk}^{(N,\lambda)}|^2\,\delta_{(\log n/\log N,\ k/n)},
\]
where the entries \(b_{nk}^{(N,\lambda)}\) are specified below. **For every bounded continuous test function** \(F\) on \([0,1]\times(0,\infty)\),
\[
\lim_{N\to\infty}\int F\,d\mu_{N,\lambda}
=\frac{\Gamma(\alpha+4)}{\Gamma(\alpha+2)}
\int_0^1\int_0^\infty F(t,x)e^{-\lambda t}
\frac{x^{\alpha+1}}{(1+x)^2}\,dx\,dt. \tag{1}
\]
The convergence is uniform for \(\lambda\) in any prescribed compact interval. Thus the logarithmic row scale and the column-to-row index ratio asymptotically separate; the latter has the beta-prime law with parameters \(\alpha+2\) and \(-\alpha\), and the former has exponential tilt \(e^{-\lambda t}\).

Write \(\Phi(\lambda)=\int_0^1e^{-\lambda t}\,dt\) (with \(\Phi(0)=1\)) and \(C_\alpha=\Gamma(\alpha+4)\Gamma(-\alpha)\). The **sharp finite-section Hilbert–Schmidt crossover**, including negative \(\lambda\), is
\[
\|T_{N,\lambda}\|_{\mathcal S_2}^2=C_\alpha\,\Phi(\lambda)\log N+O_{\alpha,L}(1),
\qquad |\lambda|\le L,\quad N\to\infty. \tag{2}
\]
As a separate limit of the same matrix-energy calculation, for the full operator above the compactness threshold,
\[
\|\mathcal H_2:A^2_\alpha\to A^2_{\alpha+2+\varepsilon}\|_{\mathcal S_2}^2
=\frac{C_\alpha}{\varepsilon}+O_\alpha(1),\qquad \varepsilon\downarrow0. \tag{3}
\]

## Assumptions and scope
Every result holds for each fixed \(\alpha\in(-1,0)\). In (1), uniformity in \(\lambda\) means that the supremum of the absolute error over any fixed \([-L,L]\) tends to zero for each fixed bounded continuous test \(F\). The finite matrices are defined for all sufficiently large \(N\) so that \(\beta_N>-1\). The full operator in (3) is only used at \(\varepsilon>0\). The two-index empirical measure records squared matrix-entry energy, **not** the singular-value counting distribution of the compressed operator.

For \(m\ge0\), define
\[
w_m(\gamma)=\|z^m\|_{A^2_\gamma}^2
=\frac{\Gamma(\gamma+2)\Gamma(m+1)}{\Gamma(m+\gamma+2)}.
\]
Using normalized monomials in input and output gives exactly
\[
b_{nk}^{(N,\lambda)}=\frac{n+1}{n+k+1}
\sqrt{\frac{w_n(\beta_N)}{w_k(\alpha)}},\qquad 0\le n,k\le N.\tag{4}
\]
This follows by integrating the monomial term \((n+1)s^{n+k}\) in \((1-sz)^{-2}\). In particular, the squared Frobenius norm of this explicit matrix equals the Hilbert–Schmidt norm appearing in (2).

## Proof
**1. Uniform gamma-ratio and beta integral.** For \(\gamma\) in any fixed compact subset of \((-1,\infty)\), Stirling's gamma-ratio estimate gives uniformly as \(m\to\infty\)
\[
w_m(\gamma)=\Gamma(\gamma+2)m^{-\gamma-1}(1+O(m^{-1})).\tag{5}
\]
For \(k\ge1\), \(w_k(\alpha)^{-1}=k^{\alpha+1}/\Gamma(\alpha+2)+O_\alpha(k^{\alpha})\). Set \(h_\alpha(x)=x^{\alpha+1}/(1+x)^2\). Both \(h_\alpha\) and its derivative are integrable on \((0,\infty)\), since \(-1<\alpha<0\); in particular \(h_\alpha\) has finite total variation. Hence its Riemann sums satisfy
\[
\frac1n\sum_{k\ge1}h_\alpha(k/n)=\int_0^\infty h_\alpha(x)\,dx+O_\alpha(n^{-1}).\tag{6}
\]
Euler's beta integral gives
\[
\int_0^\infty h_\alpha(x)\,dx
=\mathrm B(\alpha+2,-\alpha)=\Gamma(\alpha+2)\Gamma(-\alpha).\tag{7}
\]
These formulas also identify the normalized beta-prime density stated in the theorem.

**2. Precise row mass.** Let
\[
S_n(\alpha)=\sum_{k\ge0}\frac1{w_k(\alpha)(n+k+1)^2}.
\]
The \(k=0\) term is \(O(n^{-2})\). Replacing \(w_k(\alpha)^{-1}\) by \(k^{\alpha+1}/\Gamma(\alpha+2)\) for \(k\ge1\) causes \(O_\alpha(n^{\alpha-1})\) error, by splitting \(k\le n\) and \(k>n\) and summing \(k^\alpha/(n+k)^2\). Replacing \(n+k+1\) by \(n+k\) causes the same error. Formula (6) therefore yields
\[
S_n(\alpha)=\Gamma(-\alpha)n^\alpha+O_\alpha(n^{\alpha-1}),\qquad n\ge1.\tag{8}
\]
For \(\beta=\alpha+2+\varepsilon\) with \(\varepsilon\) in a fixed small interval, (5) and (8) imply
\[
(n+1)^2w_n(\beta)S_n(\alpha)
=\Gamma(\beta+2)\Gamma(-\alpha)n^{-1-\varepsilon}
+O_\alpha(n^{-2-\varepsilon}),\tag{9}
\]
uniformly in \(\varepsilon\). The \(n=0\) row contributes a uniformly bounded amount.

**3. The sharp bounded-window formula.** For \(\varepsilon=\lambda/\log N\) and \(|\lambda|\le L\), summing (9) through \(N\) produces a remainder bounded uniformly in \(N\) and \(\lambda\). The missing column tail \(k>N\) contributes only \(O_{\alpha,L}(1)\) in the rows \(n\le N\): since \(k>N\ge n\),
\[
\sum_{k>N}\frac1{w_k(\alpha)(n+k+1)^2}\le C_\alpha N^\alpha,
\]
while \(\sum_{n\le N}(n+1)^2w_n(\beta_N)\le C_{\alpha,L}N^{-\alpha}e^{L}\). Thus
\[
\|T_{N,\lambda}\|_{\mathcal S_2}^2
=\Gamma(\beta_N+2)\Gamma(-\alpha)\sum_{n=1}^Nn^{-1-\lambda/\log N}+O_{\alpha,L}(1).\tag{10}
\]
A uniform integral comparison shows that this sum equals \((\log N)\Phi(\lambda)+O_L(1)\). Also \(\Gamma(\beta_N+2)=\Gamma(\alpha+4)+O_{\alpha,L}(1/\log N)\). This proves (2) with the stated additive \(O(1)\) error, not merely relative convergence.

**4. Joint distribution.** For \(n,k\to\infty\) with \(x=k/n\) in a fixed compact subinterval of \((0,\infty)\), (4)--(5) give uniformly for \(|\lambda|\le L\)
\[
|b_{nk}^{(N,\lambda)}|^2
=\frac{\Gamma(\beta_N+2)}{\Gamma(\alpha+2)}
n^{-2-\lambda/\log N}
\frac{x^{\alpha+1}}{(1+x)^2}
(1+O_\alpha(n^{-1}+k^{-1})).\tag{11}
\]
Consequently, the column sum on a fixed ratio interval \(a\le k/n\le b\) is a Riemann sum of \(h_\alpha\), and the row sum is a logarithmic Riemann sum: \(t=\log n/\log N\) gives
\[
\frac1{\log N}\sum_{n\le N}\frac{e^{-\lambda\log n/\log N}}n\,G(\log n/\log N)
\longrightarrow\int_0^1e^{-\lambda t}G(t)\,dt\tag{12}
\]
for continuous \(G\), uniformly in bounded \(\lambda\). Restrict first to \(\eta\le t\le1-\eta\) and \(a\le x\le b\): then the cutoff \(k\le N\) does not interfere for all sufficiently large \(N\), and (11)--(12) prove (1) for continuous functions supported in that region.

The omitted ratio tails are uniformly negligible. Specifically, for \(0<a<1<b\), (4)--(5) give the row estimates
\[
\sum_{1\le k<an}|b_{nk}^{(N,\lambda)}|^2
\le C_{\alpha,L}a^{\alpha+2}n^{-1-\lambda/\log N},
\qquad
\sum_{k>bn}|b_{nk}^{(N,\lambda)}|^2
\le C_{\alpha,L}b^{\alpha}n^{-1-\lambda/\log N},\tag{13}
\]
with harmless bounded-small-index corrections of total \(o(\log N)\). For the row coordinate \(t\), (9) bounds the mass of \(t<\eta\) and \(t>1-\eta\) by \(C_{\alpha,L}\eta+o(1)\) after division by \(\log N\). Since \(\alpha+2>0\) and \(\alpha<0\), send \(a\downarrow0\), \(b\uparrow\infty\), and \(\eta\downarrow0\). Tightness and boundedness then extend convergence from compactly supported continuous tests to every bounded continuous \(F\), proving (1). Taking \(F\equiv1\), or directly (2), gives its total mass \(C_\alpha\Phi(\lambda)\).

**5. Supercritical infinite operator.** For \(0<\varepsilon<\varepsilon_0\), sum (9) over all rows and use its summable uniform remainder; the \(n=0\) row remains bounded. Then
\[
\|\mathcal H_2\|_{\mathcal S_2}^2
=\Gamma(\alpha+4+\varepsilon)\Gamma(-\alpha)
\sum_{n=1}^\infty n^{-1-\varepsilon}+O_\alpha(1).
\]
The standard integral comparison \(\sum_{n\ge1}n^{-1-\varepsilon}=\varepsilon^{-1}+O(1)\) and smoothness of \(\Gamma\) prove (3).

## Verification
The gamma-ratio asymptotics, finite-variation Riemann-sum estimate, beta integral, row remainder and uniform tail estimates above constitute the analytical proof for all permitted parameters. The separate `verification_checker.py` uses direct normalized monomial moments and finite matrix sums to test the exact identities and the limiting constants for selected parameters. Its finite computations do not prove the infinite limits. Run it with a standard Python 3 interpreter: `python3 verification_checker.py`.

## Relationship to prior work
Li and Zhou (arXiv:2610.05672v1, first public October 5, 2026) characterize boundedness, compactness and Schatten membership of the differential Hilbert operator and supply the infinite Hilbert–Schmidt sum for the strictly supercritical range. The exact matrix coefficients in (4) are theirs; no priority is asserted for those coefficients or for their operator classification. The joint beta-prime index-ratio limit (1) and the signed critical-window finite-section profile (2), which includes nonbounded full-operator regimes, are distinct quantified asymptotic statements not provided by that work. Formula (3) follows from an asymptotic analysis of their sum and is included as a boundary comparison, not presented as an independent structural result.

Norrbo (arXiv:2610.00252v1, September 23, 2026) treats the nondifferential Hilbert matrix on logarithmically weighted Bergman spaces. Davis and Ghatage (1990) analyze spectral density for a symmetric Bergman–Hilbert matrix. Kalvoda and Šťovíček (arXiv:1506.01064v1) diagonalize a family of symmetric Hankel matrices. Their operators and spectral questions differ from the present asymmetric power-weighted differential Hilbert squared-entry distribution. Related general Mellin or homogeneous-kernel asymptotics may contain implicit analogous results; no exhaustive historical priority or independent review is claimed.

## Limitations
The measure concerns entrywise squared Hilbert–Schmidt energy in canonical monomial bases, not eigenvalues or singular-value empirical measures. The exact beta-prime factorization is proved only for \(-1<\alpha<0\), square truncations, and fixed compact windows of \(\lambda\); the full-operator comparison requires positive \(\varepsilon\). Uniformity does not extend to \(\lambda\) increasing with \(N\). The numerical checker verifies only finite instances. Broad classical literature on homogeneous matrices could contain an implicitly equivalent form, and independent scholarly verification and priority review are outstanding.

## References
1. S. Li and M. Zhou, *The Differential Hilbert Operator Between Weighted Bergman Spaces*, arXiv:2610.05672v1 (October 5, 2026), https://arxiv.org/html/2610.05672v1 .
2. D. Norrbo, *The Hilbert Matrix Operator into the Bergman Space*, arXiv:2610.00252v1 (September 23, 2026), https://arxiv.org/html/2610.00252v1 .
3. C. Davis and P. Ghatage, *On the Spectrum of the Bergman-Hilbert Matrix II*, Canadian Mathematical Bulletin 33 (1990), 60--64, DOI 10.4153/CMB-1990-010-7.
4. T. Kalvoda and P. Šťovíček, *A Family of Explicitly Diagonalizable Weighted Hankel Matrices Generalizing the Hilbert Matrix*, arXiv:1506.01064v1 (2015), https://arxiv.org/html/1506.01064v1 .
