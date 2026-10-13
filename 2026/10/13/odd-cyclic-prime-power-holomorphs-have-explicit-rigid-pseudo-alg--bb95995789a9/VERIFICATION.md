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
The proof is symbolic.

The packaged checker `artifacts/verify.py` independently enumerates the representation parameters supplied by the explicit odd-prime irreducible-representation theorem.

For each
\[
p\in\{3,5,7,11\}
\]
and
\[
2\le n\le5,
\]
it enumerates all linear quotient characters by their exact orders and all nonlinear parameters
\[
(k,\omega).
\]
If \(\omega\) has exact order \(p^s\), it computes
\[
|\ker\rho_{k,\omega}|=p^{2(n-k)-s},
\qquad
\rho_{k,\omega}(1)=\varphi(p^k),
\]
and derives the codegree from the group order.

The resulting multiplicity table is compared to the closed formula in the finding.

The checker separately verifies
\[
\sum_{\chi\in\operatorname{Irr}(G)}\chi(1)^2=|G|
\]
using the full degree parametrization, and reconstructs \(p\) and \(n\) from the largest codegree and its multiplicity.

For
\[
\operatorname{Hol}(C_9)
\]
it obtains
\[
\{(1,1),(2,1),(3,3),(6,2),(9,3)\}.
\]

The checker returns `VERIFY_OK`.

Finite parameter checks are not used to prove the infinite family.
