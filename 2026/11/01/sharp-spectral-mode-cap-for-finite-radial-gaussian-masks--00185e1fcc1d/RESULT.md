# Sharp spectral mode cap for finite radial Gaussian masks

## Finding
For any integer \(K\geq 1\), let
\[
E=\bigcup_{j=1}^{K}[a_j,b_j],\qquad
0\leq a_1<b_1<a_2<b_2<\cdots<a_K<b_K<\infty.
\]
On normalized Gaussian Bargmann–Fock space, let \(T_E\) be the Toeplitz concentration operator with indicator symbol \(\mathbf 1_{\{|z|^2\in E\}}\). Its monomial-indexed eigenvalues are
\[
\lambda_n(E)=\frac1{n!}\int_E e^{-t}t^n\,dt,\qquad n=0,1,2,\ldots.
\]
**The sharp modal-complexity theorem** is that the adjacent-difference sequence \((\lambda_{n+1}-\lambda_n)_{n\geq0}\), after zero terms are discarded, has at most \(2K-1\) sign changes. Hence \((\lambda_n)_{n\geq0}\) has at most \(K\) strict local maxima, with \(n=0\) counted as a one-sided local maximum. **Both bounds are sharp for every \(K\):** some union of exactly \(K\) annuli attains \(2K-1\) sign changes and exactly \(K\) strict modal peaks.

These are statements about eigenvalues in their *natural monomial/Hermite degree order*, not their decreasing rearrangement. The rearranged eigenvalues are of course monotone by definition.

## Assumptions and scope
Use the Hilbert space of entire functions with
\[
\|f\|_{\mathcal F^2}^{2}
=\frac1\pi\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)<\infty.
\]
The orthonormal basis is \(e_n(z)=z^n/\sqrt{n!}\). The operator is the bounded positive form
\[
\langle T_Ef,g\rangle
=\frac1\pi\int_{\{|z|^2\in E\}}f(z)\overline{g(z)}e^{-|z|^2}\,dA(z).
\]
Here the intervals have positive length, distinct ordered endpoints, and bounded union; the innermost component may be a disk when \(a_1=0\). A strict local maximum means \(\lambda_{n-1}<\lambda_n>\lambda_{n+1}\) at an interior integer \(n\geq1\); at \(n=0\) it means \(\lambda_0>\lambda_1\). The bound concerns all integer degrees and all choices of endpoints simultaneously.

## Proof
**Diagonal reduction.** Rotational invariance makes distinct monomials orthogonal for the concentration form. Using \(t=|z|^2\) gives the asserted integral representation. For every integer \(n\geq0\), integrating the derivative
\[
\frac{d}{dt}\bigl(t^{n+1}e^{-t}\bigr)
=(n+1-t)t^ne^{-t}
\]
yields the exact difference identity
\[
(n+1)!\bigl(\lambda_{n+1}-\lambda_n\bigr)
=F(n+1),\qquad
F(x):=\sum_{j=1}^K\bigl(a_j^xe^{-a_j}-b_j^xe^{-b_j}\bigr).
\]
Here \(x>0\) throughout; when \(a_1=0\), its term is defined to be zero. All other bases are strictly positive and pairwise distinct.

**Exponential-polynomial zero lemma.** A nonzero real sum of \(r\) exponentials with strictly increasing distinct real exponents,
\[
G(x)=\sum_{j=1}^r c_je^{\alpha_jx},\qquad \alpha_1<\cdots<\alpha_r,\quad c_j\ne0,
\]
has at most \(r-1\) distinct real zeros. Indeed divide by \(e^{\alpha_1x}\). Its derivative is a nonzero sum of \(r-1\) exponentials with distinct exponents. By induction it has at most \(r-2\) real zeros; if the original quotient had \(r\) distinct zeros, Rolle's theorem would give at least \(r-1\) derivative zeros, a contradiction. The base case is constant nonzero. Applied to \(F\), there are at most \(2K-1\) distinct zeros on \((0,\infty)\), and at most \(2K-2\) if \(a_1=0\).

Each sign reversal of the nonzero sampled values \(F(1),F(2),\ldots\) forces a different real zero between the corresponding sample arguments. Therefore there are at most \(2K-1\) sign reversals of the adjacent differences. If there are \(m\) strict local maxima of \((\lambda_n)\) and none is at \(n=0\), successive positive-to-negative patterns at those maxima, with a negative-to-positive reversal in between, require at least \(2m-1\) sign reversals. If the first maximum is the boundary mode \(n=0\), the other \(m-1\) maxima require at least \(2m-2\) reversals. Both inequalities imply \(m\leq K\).

**Sharpness at every component count.** For each integer \(M\geq2\), take one squared-radius interval \(I_M=[M,M+\tfrac12]\). Its contribution to \(F(x)\) is
\[
F_M(x)=M^xe^{-M}-(M+\tfrac12)^xe^{-(M+1/2)}.
\]
Because \(t^Me^{-t}\) strictly decreases on \((M,\infty)\), while \(t^{M+1}e^{-t}\) strictly increases on \((0,M+1)\),
\[
F_M(M)>0,\qquad F_M(M+1)<0.
\]
Thus its \(M\)-th eigenvalue is a strict local maximum.

Choose \(M_1\geq2\) and inductively append \(I_{M_j}\) with each new integer \(M_j\) sufficiently large. At the finitely many previous strict maxima, contributions \(F_M(x)\) from the newly appended interval tend to zero as \(M\to\infty\) for each fixed \(x>0\), so their strict inequalities persist. At the new index \(M\), the contribution of the old finite union is \(O(B^{M+1})\), where \(B\) is its largest endpoint. The newly added contribution has the asymptotics
\[
\frac{F_M(M)}{e^{-M}M^M}
=\frac1{8M}+O(M^{-2}),\qquad
\frac{F_M(M+1)}{e^{-M}M^{M+1}}
=-\frac3{8M}+O(M^{-2}).
\]
These follow by expanding \(\log(1+1/(2M))\) to second order. The old contribution is negligible compared with either displayed nonzero term, since
\[
\frac{B^{M+1}}{e^{-M}M^M/M}
=O\!\left(M^2(eB/M)^M\right)\longrightarrow0.
\]
Hence \(F(M)>0\) and \(F(M+1)<0\) for the enlarged union; the new degree \(M\) is an additional strict local maximum. Induction produces at least \(K\), and the upper bound makes this exactly \(K\). The first mode is interior and the signs on each side of all \(K\) peaks force at least \(2K-1\) sign reversals. The upper bound yields exactly \(2K-1\), proving sharpness of both bounds.

## Verification
All infinitely quantified assertions above follow from the explicit identity, Rolle induction, and asymptotic separation; no computer enumeration is needed. A reproducibility script `verify_modes.py` provides supplementary 90-digit decimal checks for the four finite masks with squared-radius bands starting at \(4,30,120,350\) and of width \(1/2\). It verifies the selected strict peaks, the corresponding \(2K-1\) sign reversals for \(K=1,2,3,4\), and 32 exact-formula comparisons evaluated numerically to tolerance \(10^{-70}\). This finite illustration is not used to infer the general theorem.

## Relationship to prior work
Daubechies (1988) established the Hermite diagonalization and radial eigenvalue integral. Knutsen (2020), Section 3.1, analyzes the modal ordering of a **single ring**; the present result addresses the optimal number of peaks for *arbitrary finite unions* and proves simultaneous attainment of the maximum. Halvdansson (arXiv:2502.11805v1, 2025), Proposition 2.3, treats large-scale, **decreasingly rearranged** eigenvalue profiles for finite unions of annuli, not the exact finite-scale sign variation in natural Hermite degree order. Yu (2011), Theorem 3 and Section 3, records general Poisson-mixture unimodality and total-positivity variation-diminishing principles. Those classical principles provide related upper-bound machinery; they are not claimed as new. The specific sharp \(K\)-component spectral cap and realization are the result here.

## Limitations
The theorem is restricted to finite unions of centered radial intervals and the Gaussian (lowest-Hermite) localization window. It concerns natural-degree modal structure, not the counting function after rearrangement, higher-dimensional multiplicities, weighted unions, nonradial observation sets, or quantitative separation thresholds. The recursive existence construction need not give a smallest-spacing formula. Historical literature may contain the same sharp realization implicit in general total-positivity constructions; exhaustive historical originality cannot be guaranteed.

## References
1. I. Daubechies, *Time-frequency localization operators: A geometric phase space approach*, IEEE Transactions on Information Theory 34 (1988), 605–612, doi:10.1109/18.9761.
2. H. Knutsen, *Daubechies' Time–Frequency Localization Operator on Cantor Type Sets I*, Journal of Fourier Analysis and Applications 26, article 47 (2020), doi:10.1007/s00041-020-09751-9; particularly Sections 2.3 and 3.1.
3. S. Halvdansson, *Empirical plunge profiles of time-frequency localization operators*, arXiv:2502.11805v1 (first publicly posted 2025-02-17), especially Proposition 2.3.
4. Y. Yu, *On Normal Variance-Mean Mixtures*, arXiv:1106.2333v1 (2011), Theorem 3 and Section 3 on total positivity.
5. S. Karlin, *Total Positivity*, Stanford University Press (1968), foundational general variation-diminishing theory (cited through Yu's discussion; the complete book was not inspected).
