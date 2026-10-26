# A sharp stability-mode transition in two-circle polynomial phase retrieval

## Finding
Fix an integer \(m\ge2\). The real differential of two-radius **intensity** measurements on analytic polynomials of degree at most \(2m\) has a complete, explicitly computable singular spectrum at the central monomial. Its least positive singular value exhibits a sharp angular-mode switch when the two measured circles coalesce.

For \(0<r<R<1\), define
\[
S_j=r^{4m+2j}+r^{4m-2j}+R^{4m+2j}+R^{4m-2j},\qquad
\Delta_j=(rR)^{2m-j}(R^{2j}-r^{2j})\quad(1\le j\le m).
\]
The nonzero real singular values of the derivative are exactly
\[
2\sqrt{r^{4m}+R^{4m}}\quad\text{(once)},\qquad
\sqrt{S_j\pm\sqrt{S_j^2-4\Delta_j^2}}\quad\text{(twice each for every }1\le j\le m\text{)}.
\]
Its one-dimensional real kernel consists precisely of constant-phase perturbations.

Write \(R=r+h\) and let \(h\downarrow0\), with \(m,r\) fixed and \(r+h<1\). Then
\[
\sigma_{\min}^{+}=
2r^{2m-1}h\min\left\{\frac{r}{\sqrt{1+r^4}},
\frac{mr^m}{\sqrt{1+r^{4m}}}\right\}+O_{m,r}(h^2).
\]
There is a unique transition radius \(r_m\in(0,1)\) determined by
\[
m^2r_m^{2(m-1)}(1+r_m^4)=1+r_m^{4m}.
\]
The least-stable Fourier perturbation index is \(j=m\) for \(r<r_m\), and \(j=1\) for \(r>r_m\); they tie at order \(h\) exactly for \(r=r_m\). For \(m\ge3\), no interior angular index minimizes the leading-order coefficient. As degree grows,
\[
-m\log r_m=\log m+\frac{\log2}{2}+o(1),\qquad
1-r_m\sim\frac{\log m}{m}.
\]

## Assumptions and scope
Let \(\mathcal P_{2m}\) be the complex vector space of all \(p(z)=\sum_{k=0}^{2m}a_kz^k\), considered as a real Hilbert space with coefficient norm \(\|p\|_{\rm coeff}^2=\sum|a_k|^2\). Let \(\mathbb T\) carry normalized Haar probability measure. Give \(L^2(\mathbb T;\mathbb R)\oplus L^2(\mathbb T;\mathbb R)\) the ordinary sum-of-squares real norm. The measurement map is
\[
\mathcal M_{r,R}(p)(\theta)=\bigl(|p(re^{i\theta})|^2,\ |p(Re^{i\theta})|^2\bigr).
\]
All singular values refer to the **real** Fréchet derivative \(D\mathcal M_{r,R}|_{p_0}\) at \(p_0(z)=z^m\). The operator has real domain dimension \(4m+2\). A positive singular value is counted with real multiplicity. The limit statement takes fixed \(m,r\), not a uniform joint degree/radius limit. "Least-stable angular mode" concerns its linearization and the first-order coefficient as the circles coalesce, rather than an assertion for all finite separations or about global nonlinear recovery.

## Proof
**Step 1: Exact real angular block decomposition.** Write \(q(z)=\sum_{k=0}^{2m}b_kz^k\). Differentiating the intensity gives, on a circle of radius \(s\),
\[
D\mathcal M_s|_{p_0}[q](\theta)
=2\operatorname{Re}\left(\overline{s^me^{im\theta}}\sum_{k=0}^{2m}b_ks^ke^{ik\theta}\right).
\]
The constant Fourier coefficient equals \(2s^{2m}\operatorname{Re}b_m\). For each positive frequency \(j=1,\ldots,m\), the coefficient at frequency \(j\) equals
\[
s^{2m+j}b_{m+j}+s^{2m-j}\overline{b_{m-j}}.
\]
By real Parseval, the squared output norm of an angular block (summing over the two radii) equals twice the squared complex Euclidean norm of the output of
\[
B_j=\begin{pmatrix}
r^{2m+j}&r^{2m-j}\\
R^{2m+j}&R^{2m-j}
\end{pmatrix}
\]
on \(v_j=(b_{m+j},\overline{b_{m-j}})\). The complex conjugation in this coordinate change is a **real isometry**. Therefore each complex singular value of \(B_j\), multiplied by \(\sqrt2\), occurs twice as a real singular value. The real part of \(b_m\) contributes the singular value \(2\sqrt{r^{4m}+R^{4m}}\); its imaginary part is the phase kernel.

**Step 2: Exact singular values and kernel.** The squared Frobenius norm of \(B_j\) is \(S_j\), while
\[
|\det B_j|=\Delta_j=(rR)^{2m-j}(R^{2j}-r^{2j})>0.
\]
Thus the two eigenvalues of \(B_j^*B_j\) are \(\frac12(S_j\pm\sqrt{S_j^2-4\Delta_j^2})\). Multiplying their square roots by \(\sqrt2\) gives exactly the two announced real singular values. Because each \(\Delta_j\) is positive, all angular blocks are injective. Hence the complete derivative has rank \(4m+1\) and kernel \(\mathbb R\, i z^m\).

**Step 3: Coalescing-circle asymptotics.** With \(R=r+h\),
\[
\Delta_j=2j r^{4m-1}h+O_{m,r}(h^2).
\]
At \(h=0\), the nonzero complex singular value of \(B_j\) is \(\sqrt{2}\,r^{2m-j}\sqrt{1+r^{4j}}\). Since the product of the two complex singular values is \(\Delta_j\), the smaller **real** singular value has expansion
\[
s_{j,-}(r,r+h)=\frac{2j\,r^{2m+j-1}}{\sqrt{1+r^{4j}}}h+O_{m,r}(h^2).
\]
All larger block singular values and the constant-mode singular value have positive limits as \(h\downarrow0\). The finite minimum thus reduces to minimizing \(g_j(r)=j r^j/\sqrt{1+r^{4j}}\) over \(1\le j\le m\).

**Step 4: Only extreme angular indices can be least stable.** Directly,
\[
\frac{g_{j+1}(r)}{g_j(r)}=
\left(1+\frac1j\right)r\sqrt{\frac{1+r^{4j}}{1+r^{4j+4}}}.
\]
For fixed \(0<r<1\), both the factor \(1+1/j\) and the ratio \((1+r^{4j})/(1+r^{4j+4})\) decrease strictly as \(j\) increases (for the latter, put \(x=r^{4j}\) and observe \((1+x)/(1+r^4x)\) strictly increases in \(x\), while \(x\) decreases in \(j\)). Therefore \(\{g_j\}\) is **strictly log-concave**. A positive strictly log-concave finite sequence attains its minimum only at an endpoint. This proves the sharp two-mode reduction, including strict exclusion of all interior indices when \(m\ge3\).

**Step 5: A unique angular-mode transition.** The endpoint ratio is
\[
H_m(r)=\frac{g_m(r)}{g_1(r)}
=m r^{m-1}\sqrt{\frac{1+r^4}{1+r^{4m}}}.
\]
Put \(x=r^4\in(0,1)\), \(A=x/(1+x)\) and \(B=x^m/(1+x^m)\). Because \(B<A<1/2\),
\[
\frac{d\log H_m}{d\log r}=(m-1)+2A-2mB
>(m-1)(1-2A)>0.
\]
Also \(H_m(r)\to0\) as \(r\downarrow0\), and \(H_m(r)\to m>1\) as \(r\uparrow1\). Hence there is exactly one solution \(H_m(r_m)=1\), equivalent to the displayed polynomial equation; the phase classification follows.

For the degree-asymptotic statement, the defining relation shows \(r_m\to1\): otherwise the factor \(m^2r_m^{2(m-1)}\) tends to zero along a subsequence bounded away from one. It also yields \(r_m^m=O(m^{-1})\), since \(m^2r_m^{2m}\le r_m^2(1+r_m^{4m})/(1+r_m^4)\le2\). Consequently \(r_m^{4m}\to0\) and \(r_m^4\to1\). Taking logarithms in the defining equation gives
\[
(m-1)(-\log r_m)=\log m+\tfrac12\log(1+r_m^4)-\tfrac12\log(1+r_m^{4m})
=\log m+\tfrac12\log2+o(1).
\]
Because \(-\log r_m=O(\log m/m)\), replacing \(m-1\) with \(m\) changes the left side by \(o(1)\), proving both asymptotic assertions.

## Verification
The accompanying standalone Python program `verify_spectrum.py` builds the sampled **real** Jacobian using normalized equispaced circle nodes and compares its nonzero SVD against every stated exact singular value for \(m\in\{2,3,5,7\}\) at three radius pairs. It separately checks the leading coalescence coefficient for four degrees and three inner radii, and numerically solves the critical-radius equation for eight degrees through \(m=100\). All 32 check cases passed with the stated numerical tolerances. Circle sampling is exact for the quadratic Gram form here because the sampling mesh resolves every derivative Fourier frequency; the finite tests nonetheless corroborate, rather than prove, the all-degree analytic statements. Execute `python verify_spectrum.py` with NumPy and SciPy available.

## Relationship to prior work
Chalendar and Partington, *Phase retrieval on circles and lines* (arXiv:2403.16255, first version 2024-03-24), establish global uniqueness up to phase from measurements on two concentric circles. **Global uniqueness is not asserted here as new**, and does not specify the precise real Jacobian spectrum at a central monomial or the sharp least-stable angular-mode switch as circles coalesce. Freeman, Oikhberg, Pineau and Taylor, *Stable phase retrieval in function spaces* (arXiv:2210.05114), study abstract stability principles; the introductory framework does not provide these specific modal constants. The present result is an explicit, finite-degree, locally quantitative calculation for a natural geometry whose qualitative uniqueness is already understood.

## Limitations
The theorem treats intensity (squared modulus) observations, not modulus observations. It is local at \(p_0(z)=z^m\), not a uniform global inverse theorem and not a statement about arbitrary base polynomials. The transition selects the mode with smallest **leading first-order singular coefficient** when the two radii meet; an exact switch at finite separation is not claimed. The error constant may depend on fixed \(m,r\), and the large-degree transition asymptotic is not uniform in the coalescence parameter. The computations supply independent finite tests only, not proof or independent mathematical certification. Historical priority is subject to further specialist literature review.

## References
1. I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255 (first public version 2024-03-24), https://arxiv.org/abs/2403.16255.
2. D. Freeman, T. Oikhberg, M. Pineau, and M. A. Taylor, *Stable phase retrieval in function spaces*, arXiv:2210.05114 (2022), https://arxiv.org/abs/2210.05114.
