# An exact four-term strong-superadditivity counterexample for Rényi-\(2\) entanglement


## Finding
For qubits ordered as \(A_1,A_2,B_1,B_2\), define
\[
|\psi\rangle=\frac{3|0000\rangle+2|0101\rangle+6|1010\rangle+3|1111\rangle}{\sqrt{{58}}}.
\]
For the Rényi-\(2\) entanglement \(\mathcal R_2\) used by Cornelio and de Oliveira, this state violates strong superadditivity exactly:
\[
\mathcal R_2(A_1A_2:B_1B_2)-\mathcal R_2(A_1:B_1)-\mathcal R_2(A_2:B_2)
=\log_2\!\left(\frac{{611618}}{{619817}}\right)<0.
\]
Numerically the residual is approximately \(-0.0192114589\) bits.

## Assumptions and scope
For a pure bipartite state, \(\mathcal R_2\) is the order-\(2\) Rényi entropy of either reduced state. For a two-qubit mixed state, the source proves the convex-roof formula in terms of concurrence; at order \(2\) it reduces to
\[
\mathcal R_2(\rho)=-\log_2\!\left(1-\frac{{C(\rho)^2}}{{2}}\right).
\]
Strong superadditivity for this four-qubit ordering is
\[
\mathcal R_2(A_1A_2:B_1B_2)\ge \mathcal R_2(A_1:B_1)+\mathcal R_2(A_2:B_2).
\]
The result is an exact witness, not an optimization theorem. It does not assert that the displayed state is a global minimizer of the residual, and it does not prove or disprove the broader conjecture in the source that Rényi-\(2\) strong-superadditivity violations coincide with second-order-monogamy violations.

## Proof
Across the bipartition \(A_1A_2:B_1B_2\), the four terms already use matching orthonormal basis labels on the two sides. Hence the Schmidt probabilities are
\[
\frac9{{58}},\quad\frac4{{58}},\quad\frac{{36}}{{58}},\quad\frac9{{58}}.
\]
Their squared sum is
\[
\operatorname{{Tr}}(\rho_{{A_1A_2}}^2)=\frac{{9^2+4^2+36^2+9^2}}{{58^2}}=\frac{{737}}{{1682}},
\]
so
\[
\mathcal R_2(A_1A_2:B_1B_2)=\log_2\!\left(\frac{{1682}}{{737}}\right).
\]

Tracing out \(A_2B_2\) gives
\[
\rho_{{A_1B_1}}=\frac1{{58}}
\begin{{pmatrix}}
13&0&0&24\\
0&0&0&0\\
0&0&0&0\\
24&0&0&45
\end{{pmatrix}},
\]
and tracing out \(A_1B_1\) gives the same nonzero block with the two diagonal entries interchanged. For a two-qubit X-state supported on \(\operatorname{{span}}\{{|00\rangle,|11\rangle\}}\), Wootters' spin-flip formula yields
\[
C=2|\rho_{{00,11}}|.
\]
Thus both direct pairs have concurrence
\[
C(A_1:B_1)=C(A_2:B_2)=\frac{{48}}{{58}}=\frac{{24}}{{29}}.
\]
Substituting into the source's order-\(2\) formula gives
\[
1-\frac12\left(\frac{{24}}{{29}}\right)^2=\frac{{553}}{{841}},
\qquad
\mathcal R_2(A_i:B_i)=\log_2\!\left(\frac{{841}}{{553}}\right).
\]
Therefore
\[
\Delta
=\log_2\!\left(
\frac{{(553/841)^2}}{{737/1682}}
\right)
=\log_2\!\left(\frac{{611618}}{{619817}}\right).
\]
Since \(619817-611618=8199>0\), the residual is strictly negative.

For either cross pair \(A_1B_2\) or \(A_2B_1\), the four amplitudes have mutually orthogonal traced-out labels, so all cross terms disappear. The reduced density matrix is diagonal in the computational basis and is therefore separable.

## Verification
The accompanying `verify.py` uses exact rational arithmetic to check normalization, the global purity, both direct-pair concurrences, the order-\(2\) factors, the exact residual ratio, and the strict integer inequality \(611618<619817\). Running it from the packaged path prints `VERIFY_OK`.

The proof is analytic; the checker is only a reproducibility aid. No numerical sampling is used to infer the sign of the residual.

## Relationship to prior work
Cornelio and de Oliveira introduced this Rényi entanglement measure, proved its two-qubit concurrence formula, and reported four-qubit violations of strong superadditivity found by Monte Carlo minimization. Their order-\(2\) search required targeted numerical minimization after a large random search found no violation, and their displayed violating state was described through approximate reduced spectra and entanglement values rather than explicit amplitudes. The exact residual they report is about \(-0.0197\), close to but not identical with the exact witness above.

Kim and Sanders studied Rényi-entanglement monogamy inequalities, while Wang, Mu, Vedral, and Fan later developed analytic formulas for Rényi entanglement in several state families. Searches for the exact coefficient pattern, exact rational residual, and equivalent four-qubit strong-superadditivity statements did not locate an implication-equivalent exact witness. Gour and Wallach's work on four-qubit Rényi entanglement is relevant to the same mathematical subject but addresses extremal average bipartite entanglement rather than this strong-superadditivity residual.

## Limitations
The result supplies one exact witness only. It does not characterize all violating states, determine the most negative possible residual, extend the witness to every Rényi order above \(1\), or settle the proposed equivalence between strong-superadditivity and second-order-monogamy violations. Literature searches cannot exclude an obscure or poorly indexed earlier exact witness.

## References
1. M. F. Cornelio and M. C. de Oliveira, “Strong superadditivity and monogamy of the Rényi measure of entanglement,” arXiv:0906.0332; Phys. Rev. A 81, 032332 (2010), DOI: 10.1103/PhysRevA.81.032332.
2. J. S. Kim and B. C. Sanders, “Monogamy of multi-qubit entanglement using Rényi entropy,” J. Phys. A 43, 445305 (2010), DOI: 10.1088/1751-8113/43/44/445305.
3. Y.-X. Wang, L.-Z. Mu, V. Vedral, and H. Fan, “Entanglement Rényi \(\alpha\)-entropy,” Phys. Rev. A 93, 022324 (2016), DOI: 10.1103/PhysRevA.93.022324.
4. G. Gour and N. R. Wallach, “All maximally entangled four-qubit states,” J. Math. Phys. 51, 112201 (2010), DOI: 10.1063/1.3511477.
