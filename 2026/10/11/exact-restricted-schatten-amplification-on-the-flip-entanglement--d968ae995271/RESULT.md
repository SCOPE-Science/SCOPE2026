# Exact restricted Schatten amplification on the flip–entanglement plane

## Finding

Let \(P_n(A)=(A+A^{\mathsf T})/2\) on complex \(n\times n\) matrices with the Schatten \(p\)-norm. Set \(Q_n=\operatorname{id}_{M_n}\otimes P_n\). Its intrinsic flip–entanglement plane admits a **closed-form exact restricted norm for every integer \(n\ge2\) and every \(1\le p\le\infty\)**. Write
\[
C_{p,n}=\frac{\big((n+1)^p+n^2-1\big)^{1/p}}{2n}
\left(1+\left(\frac{(n-1)^p}{n^2-1}\right)^{1/(p-1)}\right)^{(p-1)/p}
\qquad(1<p<\infty).
\]
At the endpoints \(C_{1,n}=C_{\infty,n}=(n+1)/2\). Then \(C_{p,n}=1\) precisely at \(p=2\), with strict excess for all other exponents. The maximizing input is explicit and is unique up to scalar multiples when \(1<p<\infty\).

This gives a uniform, quantitative two-level noncontractivity witness for transpose symmetrization in every base matrix size \(N\ge2\):
\[
\|\operatorname{id}_{M_2}\otimes P_N\|_{S_p^{2N}\to S_p^{2N}}\ge C_{p,2}>1
\quad (p\in[1,\infty]\setminus\{2\}).
\]
The **full** two-level endpoint values, in contrast, are determined exactly:
\[
\|\operatorname{id}_{M_2}\otimes P_N\|_{S_1^{2N}\to S_1^{2N}}
=\|\operatorname{id}_{M_2}\otimes P_N\|_{S_\infty^{2N}\to S_\infty^{2N}}=\frac32;
\]
the corresponding Hilbert–Schmidt norm is exactly \(1\). At \(p=4\), the canonical four-dimensional witness already has the exact amplification factor
\[
C_{4,2}=\left(\frac{7(1+\sqrt[3]{3})^3}{64}\right)^{1/4}=1.1234973384\ldots.
\]
The general formula concerns the **restriction to a specified natural invariant plane**; it is not a formula for the full amplified norm at intermediate exponents.

## Assumptions and scope

All matrices and tensor products are over \(\mathbb C\). Fix an integer \(n\ge2\) and \(1\le p\le\infty\). On \(M_n\otimes M_n\), let \(\Theta_n=\operatorname{id}_{M_n}\otimes({\cdot})^{\mathsf T}\), so \(Q_n=(I+\Theta_n)/2\). Here \(\|X\|_p=(\operatorname{Tr}|X|^p)^{1/p}\), with the operator norm when \(p=\infty\). Put
\[
F=\sum_{i,j=1}^n E_{ij}\otimes E_{ji},\qquad B=\sum_{i,j=1}^n E_{ij}\otimes E_{ij},\qquad V_n=\operatorname{span}_{\mathbb C}\{F,B\}.
\]
The flip \(F\) is a selfadjoint unitary, while \(B=n|\Omega\rangle\langle\Omega|\) for \(\Omega=n^{-1/2}\sum_i e_i\otimes e_i\). The plane is the minimal \(\Theta_n\)-invariant linear space containing the canonical flip; both tensors commute with the simultaneous real orthogonal group, so the choice is not a coordinate-dependent arbitrary slice. No assertion is made about arbitrary infinite-dimensional Schatten operators.

## Proof

**1. Invariant block and exact spectra.** Directly transposing the second tensor leg gives \(\Theta_n(F)=B\) and \(\Theta_n(B)=F\), hence
\[
Q_n(aF+bB)=\frac{a+b}{2}(F+B).
\]
On the line \(\mathbb C\Omega\), the input \(X=aF+bB\) has eigenvalue \(a+nb\). On its orthogonal complement, \(B=0\) and \(F\) has eigenvalues \(+1\) and \(-1\); consequently all remaining \(n^2-1\) singular values equal \(|a|\). Likewise \(F+B\) has singular values \(n+1\) once and \(1\) with multiplicity \(n^2-1\). Therefore for \(1\le p<\infty\),
\[
\|aF+bB\|_p^p=|a+nb|^p+(n^2-1)|a|^p,
\]
\[
\|Q_n(aF+bB)\|_p=
\frac{|a+b|}{2}\big((n+1)^p+n^2-1\big)^{1/p}.
\]
For \(p=\infty\), replace the respective sums by maxima of the same absolute eigenvalues.

**2. Sharp restricted norm.** Substitute \(x=a+nb\) and \(y=a\), so \(a+b=(x+(n-1)y)/n\). The quotient to be maximized is therefore a constant times the norm of the linear functional
\[
(x,y)\longmapsto\frac{x+(n-1)y}{n}
\]
on the weighted \(\ell_p^2\)-space with norm \((|x|^p+(n^2-1)|y|^p)^{1/p}\). Weighted Hölder duality gives exactly
\[
\frac1n\left(1+\frac{(n-1)^{p/(p-1)}}{(n^2-1)^{1/(p-1)}}\right)^{(p-1)/p}
\]
for \(1<p<\infty\), which yields the stated \(C_{p,n}\). Strict Hölder equality gives \(x/y=(n+1)^{1/(p-1)}\) with aligned phases, yielding the stated unique maximizing input up to a nonzero common scalar. For \(p=1\), the functional dual norm is \(1/n\), and the output factor is \(n(n+1)/2\). For \(p=\infty\), the functional norm is \(1\), and the output factor is \((n+1)/2\). This proves both endpoint expressions.

**3. Strictness for all non-Hilbert exponents.** The nonzero vector \(F+B\) is fixed by \(Q_n\), so the restricted norm is at least \(1\). For \(1<p<\infty\), in the variables above this fixed vector has ratio \(x/y=n+1\). The weighted Hölder maximizer has ratio \((n+1)^{1/(p-1)}\); by strictness of Hölder, equality with the fixed-vector ratio occurs only at \(p=2\). At \(p=2\), \(\Theta_n\) is an orthogonal isometry for the Hilbert–Schmidt inner product, hence \(Q_n\) is an orthogonal projection of norm \(1\). The endpoint constants are \((n+1)/2>1\). Thus \(C_{p,n}>1\) for every \(p\ne2\).

**4. Two-level consequence and full endpoint norms.** For each \(N\ge2\), embed a \(2\times2\) matrix corner of the base \(M_N\). The map \(\operatorname{id}_{M_2}\otimes P_N\) restricts on the resulting \(M_2\otimes M_2\) corner to \(Q_2\). Its norm is therefore at least \(C_{p,2}\), uniformly in \(N\).

For the upper endpoint estimates, the partial transpose on \(M_2\otimes M_N\) satisfies \(\|\operatorname{id}_{M_2}\otimes({\cdot})^{\mathsf T}\|_{S_\infty\to S_\infty}\le2\). Indeed, the transpose on \(M_2\) has an amplification representation \(\sum_{i,j=1}^{2}(E_{ij}\otimes I_N)X(E_{ij}\otimes I_N)\), whose operator norm is at most \(2\|X\|_\infty\) by the row–column operator Cauchy–Schwarz inequality; composing with the full matrix transpose (an isometry) switches which leg is transposed. The same bound holds on \(S_1\) by trace duality. The triangle inequality consequently yields \(\|\operatorname{id}_{M_2}\otimes P_N\|\le(1+2)/2=3/2\) on both endpoint spaces. The embedded \(n=2\) vectors above attain \(3/2\). At \(p=2\), partial transpose is a Hilbert–Schmidt isometry, and symmetrization is an orthogonal projection of norm one.

**5. Explicit fourth-power value.** Substituting \(p=4\), \(n=2\) into the weighted-Hölder formula yields
\[
C_{4,2}^4=\frac{84}{256}(1+3^{-1/3})^3
=\frac{7}{64}(1+3^{1/3})^3.
\]
This identity is exact; the decimal is only for orientation.

## Verification

The embedded standalone `verify_brauer.py` independently constructs \(F\), \(B\), and their partial transposes over exact integer matrices for sizes \(2\le n\le5\), checks all spectral/multiplicity and invariance identities, and checks exact fourth powers of the norm ratios against the analytical formula in the sample \(p=4\), \(n=2\) case (the non-rational cube-root maximizer is checked numerically). It separately tests weighted-Hölder sharpness on numerical samples. These tests do not prove the universal assertions, which follow from the spectral and duality calculations above. The verifier requires only the Python standard library and was executed from the extracted, hash-checked package. No external certificate or automated independent audit is claimed.

## Relationship to prior work

Arhancet, *A modular theory of contractive projections on Banach spaces with applications to noncommutative L^p-spaces* (arXiv:2610.03375v1, publicly available 2026-10-02), Introduction (1.2) and Remark 6.4, establishes scalar contractivity of transpose symmetrization and explicitly gives a qualitative non-2-contractivity argument for the \(p=4\), \(2\times2\) case. The present result does **not** claim that qualitative failure as new. Instead it computes the exact noncontractivity profile on the canonical flip–entanglement invariant plane across **every exponent and size**, characterizes its extremizers, and obtains sharp full two-level endpoint values. Its quantification is not a direct numerical statement of the cited qualitative implication.

Earlier work of Arazy–Friedman describes contractively complemented subspaces of Schatten spaces, and Ando–Sano studies norm estimates for the partial transpose. These make it essential to distinguish a restricted norm formula from full amplification norms; the 2008 Ando–Sano full text was not available for comparison. The classical symmetry of flip operators and maximally entangled tensors is acknowledged. Their elementary relations are inputs to the computation rather than novelty claims.

## Limitations

For \(1<p<\infty\), \(p\ne2\), the formula is exact **only on \(V_n\)**; it gives a lower bound, not a proved full amplified norm. No optimal full two-level norm at these exponents is claimed. The full endpoint norm is proved specifically for **two-level** amplification (and the stated base sizes). The paper of Ando–Sano could not be inspected in full; an equivalent calculation in older operator-space or quantum-information literature is a residual originality risk. No claim of independence, completeness of literature coverage, or journal acceptance is made.

## References

1. C. Arhancet, *A modular theory of contractive projections on Banach spaces with applications to noncommutative L^p-spaces*, arXiv:2610.03375v1 (first posted 2026-10-02), especially Introduction (1.2), Theorem 6.3 and Remark 6.4. https://arxiv.org/html/2610.03375v1
2. J. Arazy and Y. Friedman, *Contractive projections in \(C_p\)*, 1992 (classification and symmetric-matrix examples; bibliographic metadata in Arhancet's references).
3. T. Ando and T. Sano, *Norm Estimates of the Partial Transpose Map on the Tensor Products of Matrices*, *Positivity* **12** (2008), 9–24, DOI:10.1007/s11117-007-2121-7 (abstract inspected; full text unavailable).
4. K. G. H. Vollbrecht and R. F. Werner, *Entanglement Measures under Symmetry*, *Phys. Rev. A* **64** (2001), 062307, DOI:10.1103/PhysRevA.64.062307 (context for symmetry-restricted tensor operators).
