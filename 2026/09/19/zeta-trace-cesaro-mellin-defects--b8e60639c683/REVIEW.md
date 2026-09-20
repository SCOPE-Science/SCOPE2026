# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The central identity is an exact lattice-sum versus multiplicative-convolution integral formula. For the logarithmic kernels
\[
\omega_r(t)=\mathbf 1_{(0,1]}(t)\frac{(-\log t)^{r-1}}{(r-1)!},
\]
the relevant integrand becomes \(k^{-1}e^{-t}\) times a fixed-degree polynomial in \(t\) and \(L-t\), with \(L=\log(n/k)\). Its endpoint value plus total variation is therefore
\[
O_{p,q}\!\left(k^{-1}(1+L)^{p+q-2}\right).
\]
This yields
\[
|(\Delta_{p,q})_{n,k}|
\lesssim_{p,q}
(nk)^{-1}(1+\log(n/k))^{p+q-2}.
\]
A dyadic summation gives column norms \(O_{p,q}(k^{-3/2})\); summability of these column norms gives an explicit nuclear decomposition and therefore trace-class membership.

The multi-factor result follows from the two-factor statement and the ideal property of \(\mathcal S_1\). The trace computation is independently forced by triangularity: \((W_1)_{n,n}=1/n\), while \((W_r)_{n,n}=0\) for \(r\ge2\). Thus the pure Cesàro word has diagonal \(n^{-s}\), producing \(\zeta(s)\), and every mixed word has zero diagonal. For \(s=2\), direct multiplication gives
\[
(C^2-W_2)_{n,k}
=
n^{-1}\bigl(H_n-H_{k-1}-\log(n/k)\bigr),
\]
providing a concrete check of both the trace-class estimate and the trace \(\pi^2/6\).

No compactness, complementability, duality, or inheritance claim is used implicitly.

## Originality

**PASS, to the best of our knowledge.** Bellavita--Stylogiannis arXiv:2609.09453v1 proves only the general Hilbert--Schmidt defect for its kernel algebra and explicitly identifies Schatten refinements as a natural open direction. The current v1 was inspected at the theorem, Cesàro-kernel, convolution-algebra, and concluding-question statements; it contains no trace-class or zeta-trace theorem for the Cesàro convolution powers.

Targeted searches for equivalent formulations involving Cesàro powers, sampled Mellin matrices, multiplicative-convolution defects, trace class, Schatten refinements, harmonic-number corrections, and zeta traces did not locate prior coverage. The 2025 Rhaly-matrix Schatten classification was checked as the closest source cited by the 2026 paper; it studies Schatten membership of Rhaly matrices themselves and does not supply the present defect theorem.

Residual risk: older work on Hausdorff/Cesàro matrices, high powers of the Cesàro operator, Euler--Maclaurin lattice corrections, or discrete Mellin calculi may contain an equivalent special-case estimate under different language. This is a residual bibliographic risk rather than concrete evidence of coverage.

## Value

**PASS.** The result answers the source paper's Schatten-refinement direction on a canonical infinite subsemigroup, improving the defect from \(\mathcal S_2\) to \(\mathcal S_1\). The exact trace anomaly
\[
\operatorname{Tr}(C^m-W(\omega^{\star m}))=\zeta(m)
\]
adds information not visible in the Calkin or Hilbert--Schmidt calculus and links the discretization error to a classical invariant. The proof mechanism is reusable for other sampled convolution semigroups whose logarithmic-coordinate kernels have controlled polynomial-exponential variation.

## Limitations

The proof does not show trace-class multiplicativity for arbitrary kernels in the source algebra, does not establish optimal Schatten membership below \(\mathcal S_1\), and does not treat weighted or \(\ell^p\) versions. The originality assessment is necessarily qualified by the breadth of older summability-matrix literature.
