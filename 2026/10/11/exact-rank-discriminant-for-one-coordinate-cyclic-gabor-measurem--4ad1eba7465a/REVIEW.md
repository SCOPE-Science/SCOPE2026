# Scientific review: exact rank discriminant for one-coordinate cyclic Gabor measurements

## Correctness — PASS

The classification is quantified over every integer \(n\ge3\) and every \(z\in\mathbb C\), with the degenerate point \(z=1\) handled separately. The known projector-Gram diagonalization by the Weyl ambiguity modulus, in Goldberger--Kang--Okoudjou Theorem 2, was checked against the normalization in the proof: projector Gram eigenvalues are \(n|B(a,b)|^2/(n-1+|z|^2)^2\). The four exhaustive index cases produce the three disjoint zero-label classes. A gcd-by-gcd count rigorously handles the congruence \(ab\equiv r\pmod n\), including composite moduli and the forbidden zero coordinates. The special cases \(z=1\), \(z=1+it\), and \(z=2+2i\) follow directly. The rational nonintegral root-of-unity trace argument is an infinite-dimensional-index proof, not a numerical heuristic. Direct Gram/projector rank checks over \(3\le n\le10\) are corroborative and were actually executed from `CHECK.py`.

## Originality — PASS with residual risk

The foundational paper of Goldberger--Kang--Okoudjou (arXiv:2106.01509v1, fully inspected) establishes the rank-as-ambiguity-nonzeros criterion for arbitrary windows; it does **not** display the complete \((n,z)\) rank discriminant, the congruence-derived divisor multiplicities, or the indicated prime/composite phase test. The earlier phase-retrieval study of Bojarovska--Flinth (arXiv:1503.05800v2, fully inspected) also lacks the operator-rank classification. The later Zhu--Wang work (arXiv:2608.11850v1, fully inspected) **does** cover special cases such as the \(z=0\), odd-dimensional cyclic construction and the real-window obstruction in even dimensions; these are not asserted to be newly discovered and do not entail the exact all-parameter rank function. Closest publicly indexed Gabor work involving two-sparse windows treats another support regime; its indexed summary does not cover the one-defect full-support stratum, although its full text was not available in the indexed comparison. Parameter-name variations and unindexed equivalent calculations remain possible residual risks; no claim of independent audit or complete global priority is made.

## Mathematical value — PASS

A constant window has highly degenerate operator-tomographic measurements. Perturbing **one coordinate** is the minimal local symmetry-breaking family; identifying exactly when the resulting \(n^2\) projectors recover all \(n^2\) matrix directions is a motivated, natural classification problem. The theorem supplies the full exceptional parameter geometry with exact kernel dimensions, exposes a sharp prime/composite distinction within a single one-real-parameter slice, and gives one explicit rational complex fiducial usable in every cyclic dimension. It does not assert a stability, SIC, or noise-resistance improvement over existing designs.

## Limits and closest references

The general ambiguity criterion is pre-existing [Goldberger--Kang--Okoudjou, arXiv:2106.01509v1]; this finding contributes the complete closed rank discriminant of the specified family. Zhu--Wang, arXiv:2608.11850v1, covers related cyclic constructions and some special obstructions. Finite checks are not substituted for the algebraic proof. Unindexed prior equivalences remain a risk. A separate independent validation has not occurred.

Same-model review: passed. Independent audit: not yet performed.
