# Exact high-threshold error tails of randomly pivoted LU on unitary matrices

## Finding
Fix an integer \(n\ge2\). For every complex unitary \(n\times n\) input \(U\), draw a nonzero pivot \((i,j)\) with probability \(|U_{ij}|^2/n\). After the rank-one LU cross update, set \(R=U-U_{:j}U_{i:}/U_{ij}\). For \(t>0\), let
\[
\mathcal T_n(t)=\sup_{U\in\mathrm U(n)}\Pr\{\|R\|_F>t\|U\|_F\}.
\]
Put \(b_n=\max\{2-2/n,\,1+n/4-2/n\}\). **For every \(t>\sqrt{b_n}\), the exact worst-case strict exceedance probability is**
\[
\boxed{\mathcal T_n(t)=\frac{n-1}{n(t^2-1)+2}.}
\]
The supremum is not attained: it is approached by an explicit one-phase, rank-one perturbation of the identity. Consequently,
\[
\boxed{\lim_{t\to\infty}t^2\mathcal T_n(t)=\frac{n-1}{n}.}
\]
This is a sharp dimension-dependent confidence tail despite every admissible input having spectral condition number exactly one. The theorem concerns a single exact-arithmetic cross update and the squared-entry pivot distribution, not multiple iterations or arbitrary input matrices.

## Assumptions and scope
Matrices are over \(\mathbb C\); \(\|\cdot\|_F\) is the Frobenius norm and \(U^*U=I_n\). A pivot with \(U_{ij}=0\) has probability zero and is not selected. All probabilities concern only pivot randomness. The strict inequality in the event matters: the reported value is a supremum, never a maximum. The dimension and threshold are fixed before optimizing over unitary inputs. The bound applies to all \(n\ge2\) and all \(t>\sqrt{b_n}\); no assertion of optimality for smaller thresholds is made.

## Proof
**1. Conditional residual amplitude.** Every row and column of \(U\) has Euclidean norm one. Let \(P_{ij}=U_{:j}U_{i:}/U_{ij}\), for \(U_{ij}\ne0\). Then \(\|P_{ij}\|_F^2=|U_{ij}|^{-2}\), and the complex Frobenius inner product satisfies \(\langle U,P_{ij}\rangle_F=1\), because \(U^*U_{:j}=e_j\) and \(U_{i:}e_j=U_{ij}\). Therefore
\[
\boxed{\|R_{ij}\|_F^2=n-2+|U_{ij}|^{-2}.}
\]
Write \(\delta=[n(t^2-1)+2]^{-1}\). For \(t>\sqrt{b_n}\), the denominator is positive, and the strict exceedance event at an eligible pivot is exactly \(|U_{ij}|^2<\delta\). Thus
\[
\Pr\{\|R\|_F>t\sqrt n\}=
\frac1n\sum_{i,j:\,0<|U_{ij}|^2<\delta}|U_{ij}|^2.
\]
**2. Universal sharp upper bound.** Since \(\sum_j|U_{ij}|^2=1\) for each row and \(\delta<1/n\), each row contains at least one entry with squared modulus greater than \(\delta\). At most \(n(n-1)\) entries can satisfy the strict exceedance condition. Each qualifying entry contributes strictly less than \(\delta/n\) to the probability. Therefore
\[
\Pr\{\|R\|_F>t\sqrt n\}< (n-1)\delta.
\]
For the threshold condition, \(t^2>2-2/n\) gives \(\delta<1/n\), and \(t^2>1+n/4-2/n\) gives \(\delta<4/n^2\).

**3. Matching complex unitary family.** Let \(v=(1,\ldots,1)^\mathsf T/\sqrt n\) and
\[
U_\theta=I_n+(e^{i\theta}-1)vv^*,\qquad 0<\theta<\pi.
\]
The projection \(vv^*\) is Hermitian idempotent, so \(U_\theta\) is unitary. Its \(n(n-1)\) off-diagonal entries all have squared modulus
\[
q=\frac{4\sin^2(\theta/2)}{n^2},
\]
while its \(n\) diagonal entries all have squared modulus \(1-(n-1)q\). Since \(\delta<\min\{1/n,4/n^2\}\), choose \(q=(1-\eta)\delta\) with any sufficiently small \(\eta>0\), realized by \(\theta=2\arcsin(n\sqrt q/2)\). Then every off-diagonal entry qualifies for the strict exceedance event and every diagonal entry fails it, because \(1-(n-1)q>1/n>\delta\). Therefore the exceedance probability equals
\[
\Pr_{U_\theta}\{\|R\|_F>t\sqrt n\}=(n-1)q=(n-1)(1-\eta)\delta.
\]
Letting \(\eta\downarrow0\) proves that the upper bound is the exact supremum. The upper inequality is strict for each fixed unitary matrix, so the supremum is not attained.

**4. Tail constant.** Multiply the exact formula by \(t^2\) and let \(t\to\infty\), obtaining \((n-1)/n\). This proves the claimed sharp asymptotic coefficient.

## Verification
Run `python3 check_unitary_tail.py` using the Python standard library. The verifier constructs \(U_\theta\) for dimensions \(2\) through \(22\), multiple thresholds and approaches to the extremum; it checks entrywise unitarity, direct pivot probabilities, the strict event and the sharp upper envelope. A recorded execution passed 34,902 deterministic assertions. The proof above, not the finite set of tests, establishes the result for all integers \(n\ge2\) and all thresholds in the specified regime.

## Relationship to prior work
Gilles and Wilber introduce the squared-entry randomized LU pivot and derive an expected Gram-matrix inequality (their equation (9)); they explicitly calculate the mean-squared one-step error for dense unitary matrices (Section 3.1). Those results motivate the setting, but they neither give the exact **worst-case strict tail probability over all unitary matrices** nor the dimension-dependent extremal family above. The upper tail uses the original pivot law plus an additional support-counting argument; sharpness requires an admissible unitary with almost all entries tuned immediately below the strict threshold.

Previous work on maximum-entry adaptive cross approximation studies a deterministic pivot selection, while multistage adaptive randomized pivoting analyzes orthogonal column-subset projection and expected errors. Neither supplies this unitary minimax tail statement.

## Limitations
The formula is proved only above the explicit threshold \(\sqrt{b_n}\) and for exactly unitary complex matrices. It is a supremal one-step probability, not a characterization of a multi-step process or machine-roundoff behavior. Unitary matrices approaching the supremum depend on the requested tail threshold; a single unitary need not attain the envelope for all thresholds. Historical originality has not been independently verified.

## References
- M. A. Gilles and H. Wilber, *Low-Rank Approximation by Randomly Pivoted LU*, arXiv:2601.22344 (first publicly posted 2026-01-29), Section 3.1 and equation (9). https://arxiv.org/abs/2601.22344
- R. Divan and M. A. Gilles, *Convergence rates of randomly pivoted methods for low-rank approximation*, arXiv:2609.06287 (2026), abstract inspected; full text was not available during comparison. https://arxiv.org/abs/2609.06287
