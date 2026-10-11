---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The general proof uses three exact ingredients.

First, for a spider and any nonempty edge set \(A\),
\[
\beta(A)=L(A)+(2-d)\mathbf 1_{\{C\subseteq A\}},
\]
because leaves have coefficient \(1\), degree-two vertices coefficient \(0\), and the center coefficient \(2-d\).

Second, when \(r\ge3\),
\[
\lambda(C)=\frac{2-r}{d}<0.
\]
Every set omitting a center edge has nonnegative ratio. For every strict superset \(A\supsetneq C\), with \(k=|A|-d>0\) and \(\ell=L(A)-(d-r)\ge0\),
\[
d(2-r+\ell)-(d+k)(2-r)=d\ell+k(r-2)>0.
\]
Thus \(C\) is the unique minimizer.

Third, the limiting curvature equations on the supported star give
\[
q_L=\frac{r-2}{d(d-2)},
\qquad
q_U=\frac{d+r-2}{d(d-2)},
\]
where \(q_i=(p_iD)^{-1}\). Normalization then gives
\[
p_L=\frac{d+r-2}{2d(r-1)},
\qquad
p_U=\frac{r-2}{2d(r-1)}.
\]

The bundled checker exhaustively tests the set minimizer on multiple nontrivial spiders and verifies the weight and curvature identities with exact rational arithmetic.

The finite computations are not an exhaustive proof of the infinite family. They are consistency checks for the analytic argument above.

Unproved limits: no convergence rate, no exact unnormalized asymptotics, no result for spiders with \(r\le2\), and no general-tree convergence theorem.
