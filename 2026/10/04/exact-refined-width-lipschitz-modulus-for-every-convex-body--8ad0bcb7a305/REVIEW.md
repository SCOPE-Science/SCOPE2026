# Review

## Correctness

PASS. Fix a direction \(u\) and choose opposite support points \(A,B\) that realize \(s_K(u)\). Their difference decomposes as \(A-B=w_K(u)u+y\), with \(\lVert y\rVert=p_K(u)\). Moving on the great circle in the tangential direction \(y/\lVert y\rVert\) gives the exact lower support estimate
\[
w_K(v_t)\ge w_K(u)\cos t+p_K(u)\sin t.
\]
Dividing by the spherical distance \(t\) yields the missing local lower bound \(w'_K(u)\ge p_K(u)\). Proposition 4.4 of the inspected primary paper supplies the independently checked upper bound. Maximizing \(p_K\) and reusing the same local witness yields the global equality. Edge case \(p_K(u)=0\) is forced by the published upper bound. No differentiability, uniqueness of support points, or finite experiment is used in the proof.

## Originality

PASS with residual search risk. The current 2026 published version of Mushkarov--Nikolov--Thomas explicitly states Open Question 4.5 asking whether precisely these two inequalities are equalities for every convex body. It proves equality for polytopes and computes equality for an ellipse, but the inspected full text does not contain the all-convex-body support-pair lower witness. Searches for the literal question, the equality \(w'_K(u)=p_K(u)\), support-face aliases, and the equivalent support-function local-modulus statement found no covering result. The older Martini--Wenzel work gives a general Lipschitz condition, not this refined exact identity.

## Value

PASS. The result resolves an explicit open question in the primary source, simultaneously at every direction and for the global refined Lipschitz constant, with no regularity assumptions on the convex body. The proof also identifies a direct geometric witness: the tangential component of a longest chord joining the two opposite support faces. This is a structural completion of the source inequality rather than a parameter specialization or recomputation.

Closest literature and limitations are detailed in `AUDIT.json` and `RESULT.md`. The separate diameter-function questions are not claimed.

Same-model review: passed. Independent audit: not yet performed.
