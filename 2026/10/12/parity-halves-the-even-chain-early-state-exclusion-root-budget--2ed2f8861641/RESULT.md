# Parity halves the even-chain early-state-exclusion root budget
## Finding
For an even chain of order \(2n\) in the reduced symmetric perfect-state-transfer normalization, let
\[
\sigma(J)=\{{\pm\lambda_1,\ldots,\pm\lambda_n\}},
\qquad 0<\lambda_1<\cdots<\lambda_n,
\]
with first perfect-state-transfer time \(\pi\). The reduced-spectrum condition makes every \(2\lambda_k\) an odd integer. If \(E\) denotes the number of early-state-exclusion zeros of the return amplitude in \(0<t<\pi\), counted with multiplicity, then
\[
E\le \lambda_n-n+\frac12.
\]
Consequently the number of distinct early-state-exclusion times satisfies the same bound. In particular, if \(\lambda_n=n-\tfrac12\), there is no early state exclusion before the first perfect transfer.

## Assumptions and scope
The statement concerns the even-order reduced symmetric spectra used in the cited perfect-state-transfer and early-state-exclusion framework. The normalization fixes the first perfect-state-transfer time to \(\pi\). The result counts zeros of the endpoint return amplitude before that time. It does not claim that the bound is attained for every admissible spectrum, nor does it address nonsymmetric spectra, non-persymmetric Jacobi matrices, or transport outside the single-excitation model.

## Proof
Write the return amplitude in the even case as
\[
A(t)=\sum_{k=1}^n \widetilde c_k\cos(\lambda_k t),
\]
where the spectral weights \(\widetilde c_k\) are nonzero. Put \(x=\cos(t/2)\). Since \(2\lambda_k\) is odd,
\[
\cos(\lambda_k t)=T_{2\lambda_k}(x),
\]
so
\[
P(x):=A(2\arccos x)=\sum_{k=1}^n \widetilde c_k T_{2\lambda_k}(x)
\]
is an odd polynomial. Its degree is \(2\lambda_n\), because the top spectral weight is nonzero.

The spectral-fusion analysis proves that \(A\) has a zero of multiplicity \(2n-1\) at \(t=\pi\). Since \(x=\cos(t/2)\) has a simple zero at \(t=\pi\), \(P\) has a zero of the same multiplicity at \(x=0\). Hence
\[
P(x)=x^{2n-1}Q(x).
\]
Both \(P\) and \(x^{2n-1}\) are odd, so \(Q\) is even, and
\[
\deg Q=2\lambda_n-(2n-1)=2\lambda_n-2n+1.
\]
The map \(t\mapsto x=\cos(t/2)\) is a bijection from \(0,\pi\) onto \(0,1\). Thus early-state-exclusion zeros are exactly the positive roots of \(Q\) lying in \(0,1\), with multiplicity preserved. Every positive root of the even polynomial \(Q\) is paired with a negative root of the same multiplicity. Therefore at most half of the total degree can be spent on positive roots:
\[
E\le\frac{\deg Q}{2}=\lambda_n-n+\frac12.
\]

## Verification
The argument is algebraic and all-parameter. The only imported non-elementary premise is the cited \(2n-1\) multiplicity of the return-amplitude zero at the first transfer time. The parity step uses the standard identity \(T_m(-x)=(-1)^mT_m(x)\). A bundled checker verifies the parity and degree arithmetic over representative admissible half-integer spectral endpoints; it is corroborative and is not used as an infinite proof.

## Relationship to prior work
Bailey, Costa, Derevyagin, Findley, and Zuang introduced the early-state-exclusion problem for Jacobi Hamiltonians and developed the Chebyshev-polynomial formulation. Escobar, Garcia, and Minenkova subsequently proved that, in the even-order reduced symmetric case, the return amplitude has multiplicity \(2n-1\) at \(t=\pi\) and stated the upper bound \(2\lambda_n-n\) for the number of early-state-exclusion instances. The present observation retains the parity forced by the odd Chebyshev indices after removing the compulsory root at the transfer time. That makes the residual polynomial even and halves its available positive-root budget, yielding \(\lambda_n-n+\tfrac12\).

## Limitations
The result is an upper bound, not an existence theorem or an assertion of sharpness for every spectrum. It relies on the exact reduced-spectrum parity and on the multiplicity theorem at \(t=\pi\). It does not compare implementation robustness or transfer fidelity under perturbations. Literature searches found no statement of this parity-halved even-order bound, but recent work may still be incompletely indexed.

## References
1. R. Bailey, S. Costa, M. Derevyagin, C. Findley, and K. Zuang, “Hamiltonians that realize perfect quantum state transfer and early state exclusion,” Quantum Information Processing 24, 51 (2025), DOI:10.1007/s11128-025-04667-z; preprint arXiv:2411.06047.
2. M. Escobar, V. Garcia, and A. Minenkova, “Spectral Fusion for Identifying Early State Exclusion in Symmetric Quantum Spin Chains,” arXiv:2606.04353v1 (2026).
