# Euler-characteristic obstruction in the cube-degeneration dual complex

## Finding

Let \(\Pi_C\) be the finite four-dimensional \(\Delta\)-complex reported for the cube degeneration of \(\operatorname{Hilb}^{2}(\mathrm{K3})\) in Shafi–Tschanz, arXiv:2512.21190v1. Their Theorem 3.3.1 gives the face vector
\[
(f_0,f_1,f_2,f_3,f_4)=(21,120,420,480,192).
\]
Its Euler characteristic is
\[
\chi(\Pi_C)=21-120+420-480+192=33.
\]
A finite \(\Delta\)-complex homeomorphic to \(\mathbb{CP}^{2}\) has Euler characteristic \(3\). Thus the reported face vector cannot describe a complex homeomorphic to \(\mathbb{CP}^{2}\). This is an exact obstruction to the paper's stated comparison of the computed dual complex with \(\mathbb{CP}^{2}\).

## Assumptions and scope

The claim concerns the listed face counts and their compatibility with the stated \(\mathbb{CP}^{2}\) topological comparison. For any finite \(\Delta\)-complex, the Euler characteristic is the alternating sum of its numbers of cells. The standard cell structure of \(\mathbb{CP}^{2}\) has one cell in dimensions \(0,2,4\), so \(\chi(\mathbb{CP}^{2})=3\). The conclusion is only that the two pieces of reported data cannot both hold for the same complex; it does not identify which count or hypothesis requires correction.

## Proof

By the definition of a finite \(\Delta\)-complex, each open simplex contributes one cell. Therefore its Euler characteristic is invariantly
\[
\chi=\sum_{i=0}^{4}(-1)^i f_i.
\]
Substituting the five counts from Theorem 3.3.1 gives
\[
21-120=-99,\quad -99+420=321,\quad 321-480=-159,\quad -159+192=33.
\]
If \(|\Pi_C|\) were homeomorphic to \(\mathbb{CP}^{2}\), invariance of Euler characteristic would force \(\chi(\Pi_C)=3\), contradicting \(33\ne3\). Hence the reported face vector and the claimed \(\mathbb{CP}^{2}\) comparison are incompatible.

## Verification

The integer calculation is reproduced by the standalone standard-library script `verify_euler.py`, embedded with this result. It computes the alternating sum directly and checks that it equals \(33\), not \(3\). This verifies the numerical obstruction only; it does not recalculate the geometric strata or determine the corrected face vector.

## Relationship to prior work

Shafi and Tschanz, *From logarithmic Hilbert schemes to degenerations of hyperkähler varieties* (arXiv:2512.21190v1, first public 2025-12-24), state in Remark 3.1.2 that the dual complex of a type-III semistable degeneration of \(\operatorname{Hilb}^{m}(\mathrm{K3})\) is homeomorphic to \(\mathbb{CP}^{m}\), and say the computations should therefore give triangulations of \(\mathbb{CP}^{2}\) when \(m=2\). Their Theorem 3.3.1 reports the face vector used above for the cube degeneration. Kollár, Laza, Saccà, and Voisin, *Remarks on degenerations of hyper-Kähler manifolds* (arXiv:1704.02731, Theorem 0.11(ii)), independently state that the dual complex of a type-III minimal dlt degeneration is a rational homology \(\mathbb{CP}^{n}\), which also forces Euler characteristic \(3\) for \(n=2\) when its hypotheses apply.

The comparison is an invariant-level implication, not a claim that the present calculation identifies the source of the discrepancy. The cited minimal-dlt theorem has hypotheses that should not be silently transferred to a stack model; the paper's own Remark 3.1.2 is the direct source for the stated \(\mathbb{CP}^{2}\) comparison.

## Limitations

No corrected face count is inferred. The result does not determine whether the error is in the enumeration, the identification of the relevant dual complex, or the applicability of the cited topological theorem to the stack construction. It establishes only the exact Euler-characteristic incompatibility between the reported face vector and a \(\mathbb{CP}^{2}\)-homeomorphic complex.

## References

1. Q. Shafi and C. Tschanz, *From logarithmic Hilbert schemes to degenerations of hyperkähler varieties*, arXiv:2512.21190v1, submitted 2025-12-24; Remark 3.1.2 and Theorem 3.3.1.
2. J. Kollár, R. Laza, G. Saccà, and C. Voisin, *Remarks on degenerations of hyper-Kähler manifolds*, arXiv:1704.02731; Theorem 0.11(ii); published in *Annales de l'Institut Fourier* 68 (2018), 2837–2882.
