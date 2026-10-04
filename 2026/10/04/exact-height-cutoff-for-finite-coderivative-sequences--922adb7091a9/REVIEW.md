# Review

## Correctness

PASS. The strict-successor characterization gives a clean induction: a point remains outside the \(k\)-th coderivative iterate exactly when a chain of \(k+1\) complement points starts there. Since the complement of an upset is a downset, the induction step preserves membership in the complement. The iterate reaches the top exactly at the complement height.

On a finite poset, every proper upset has a complement-maximal point that is added by one coderivative step, so the top is the unique fixed point. Hence the least-fixed-point sentence \(M\) is valid. The sequence inequalities then force \(P_i\) from below by \(\nabla^{N-i}(\varnothing)\); the explicit valuation \(P_j=\nabla^{N-j}(\varnothing)\) proves sharpness.

The bundled checker exhaustively verifies the iterate and fixed-point statements for every labelled poset of order at most four and independently exhausts the truncated-sequence semantics for all labelled posets of order at most three and \(N\le3\).

## Originality

PASS. The recent source proves the strict-successor formula for \(\nabla\), introduces \(M\) and the free \(\nabla\)-sequence, and in its nonderivability proof identifies long chains as witnesses that \(\nabla^N(\varnothing)\) is not top. It does not state the arbitrary-upset iterate formula, the finite-poset fixed-point consequence, or the exact semantic profile \(T_N\models P_i\) iff the remaining depth reaches the poset height.

Searches combining point-free coderivative, finite poset, height, longest chain, truncated free sequence, and forcing profile found no equivalent theorem in the checked sources or published-finding index.

## Value

PASS. The result gives an exact finite cutoff, not just an upper bound: poset height is precisely the amount of a truncated free coderivative sequence needed to force each variable. This identifies the finite-model boundary behind the source paper's use of arbitrarily long chains and supplies a complete finite-poset semantic profile for the truncations used in the strong-incompleteness argument.

## Closest literature and limitations

The closest source is Kocsis's 2026 paper, especially Proposition 3.10 and Lemma 5.13. The special case \(X=\varnothing\) of the chain-witness observation appears inside that proof, so that component is not claimed as new in isolation. The accepted claim is the full finite-height classification and exact truncated-theory consequence profile.

The theorem is finite. It does not classify transfinite coderivative ranks on infinite posets.

Same-model review: passed. Independent audit: not yet performed.
