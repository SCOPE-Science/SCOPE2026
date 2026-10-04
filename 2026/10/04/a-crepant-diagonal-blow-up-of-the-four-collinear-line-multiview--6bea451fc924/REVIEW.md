# Review

## Correctness

PASS. The correction equation has exact transverse quadratic part \(q(a,b,c)\) whose Hessian determinant is twice the full Vandermonde product in the four camera parameters, so distinct centers give a nondegenerate quadric and exact multiplicity two along the small diagonal. The supplied symbolic replay checks this identity and all three blow-up charts. The global exceptional divisor follows from \(N_{\Delta/(\mathbb P^1)^4}\cong\mathcal O(2)^{\oplus3}\) and \(\mathcal O(1,1,1,1)|_\Delta\cong\mathcal O(4)\), which trivialize the family of normal quadrics. The crepant formula is the standard codimension-three blow-up canonical formula combined with the multiplicity-two strict transform, so the discrepancy cancels exactly.

## Originality

PASS. The line-multiview primary source supplies the correction determinant but not this resolution. The closest broader source, Aluffi--Faber, constructs a smooth model of a symmetric \(\mathrm{PGL}_2\)-orbit closure by blowing up base lines in the projective space of \(2\times2\) matrices. That construction does not imply that the ordered correction hypersurface is resolved intrinsically by blowing up its small diagonal, nor does it identify the exceptional surface or establish zero discrepancy. Targeted published-index and web searches for the exact cross-ratio/diagonal/crepant statement returned no covering result. Residual risk remains for equivalent language in classical ordered-configuration compactifications.

## Value

PASS. The result converts the correction equation from a singular compatibility condition into a concrete birational model: a one-step crepant resolution with explicit exceptional geometry and weak-Fano anticanonical class. This gives usable global geometry of the natural non-generic four-collinear correction space rather than another local singularity check.

Closest literature and limitations are detailed in `RESULT.md` and `AUDIT.json`.

Same-model review: passed. Independent audit: not yet performed.
