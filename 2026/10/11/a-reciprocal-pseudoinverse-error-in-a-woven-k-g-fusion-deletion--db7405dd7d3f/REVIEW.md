# Review
## Correctness
PASS. The example uses
\[
K=\frac12I,\qquad K^\dagger=2I,
\]
and two identical two-channel source families whose full weaving energy is exactly \(\|f\|^2\). The valid bounds \(A=B=3\) satisfy the full woven inequalities. The source's deletion constant is \(C=2\), so its hypothesis \(C<A\|K^\dagger\|^2\) holds. After deleting the first channel, the remaining energy vanishes at \(e_1\), contradicting any positive \(K\)-lower bound.

The corrected estimate follows from
\[
\|f\|^2\le\|K^\dagger\|^2\|K^*f\|^2
\]
on \(R(K)\) and yields the lower constant
\[
A-C\|K^\dagger\|^2.
\]

## Originality
PASS. The exact theorem, reciprocal-threshold aliases, deletion/removal formulations, Moore--Penrose scaling, earlier \(K\)-\(g\)-fusion removal literature, and later woven-\(K\)-frame excess literature were compared.

The closest earlier removal theorem uses orthogonality to \(R(K)\), while later excess work addresses a different invariant. No checked indexed source states the scaled two-dimensional counterexample or the reciprocal correction.

## Value
PASS. The source theorem is a deletion-stability criterion. Its printed condition can approve removal of an essential channel and thereby destroy the entire \(K\)-lower bound. The corrected scaling is therefore substantive for robustness and redundancy claims.

## Closest literature and limitations
Huang--Yang prove a geometrically different removal theorem under orthogonality assumptions. Agheshteh Moghaddam--Arefijamaal study excess of woven \(K\)-frames rather than this numerical deletion threshold.

The corrected \(C\)-condition is sufficient rather than necessary, because \(C\) may overestimate the deleted energy of a specific weaving.

Same-model review: passed. Independent audit: not yet performed.
