# Self-review

## Correctness

**PASS.** Every derivation is reconstructed from the Leibniz identity as
\[
\begin{pmatrix}
A&0\\
w&\operatorname{tr}A
\end{pmatrix},
\]
with \(A\in M_2(\mathbb F_q)\) and \(w\in\mathbb F_q^2\). The proof then separates trace-zero and nonzero-trace blocks, counts the two-by-two rank/trace strata exactly, and accounts for the row-space condition on \(w\). The four rank counts sum to \(q^6\). Nilpotency is equivalent to nilpotency of \(A\), yielding exactly \(q^4\) nilpotent derivations and the stated index-two/index-three split. The packaged verifier independently confirms the formulas over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7\), and for \(q=2,3\) it also recovers the derivation space by checking every linear map.

## Originality

**PASS.** The closest direct full-text structural comparison gives the same six-parameter ordinary Heisenberg derivation matrix over an arbitrary field and its dimension, but no finite-field rank, invertible-derivation, nilpotent-count, or nilpotency-index enumerator. The archive-era Heisenberg color-derivation paper establishes strong same-family structural context; its accessible publisher material likewise does not state these counts. Searches under rank distribution, invertible derivations, nilpotent derivations, Heisenberg derivation matrices, finite fields, and equivalent spectrum language returned adjacent finite-Heisenberg invariants and automorphism counts rather than an implication of the present claim. The inaccessible full text of the 2011 source remains an explicit residual risk.

## Value

**PASS.** Rank and nilpotency are intrinsic linear invariants of a derivation algebra. The result turns a standard structural description of \(\operatorname{Der}(H_3)\) into a complete finite-field census, including the exact density of nonsingular derivations and the full nilpotency-index split. The equality between the rank-one stratum and the nonzero square-zero stratum is a structural consequence rather than a table observation. This gives a concrete benchmark for higher Heisenberg ranks, where the defining block becomes conformal-symplectic.

## Closest literature and limitations

The closest archive structural source is Yang--Hu (2011), DOI 10.1080/00927872.2010.480950. The closest direct ordinary-matrix comparison is Alemi--Saeedi (2019), DOI 10.1080/25742558.2019.1624244, whose accessible full text displays the six-parameter derivation matrix and dimension. Calderón--Draper--Martín--Sánchez (2014), arXiv:1405.4093, supplies additional same-object symmetry context. The theorem is restricted to \(H_3\); no higher-rank Heisenberg formula is claimed.

Self-review: passed. Independent audit: not yet performed.
