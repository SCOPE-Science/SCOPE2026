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

Run `python3 verify.py`. The program uses only Python integer arithmetic. It reconstructs \(E_m(t)=U_{2m}(\sqrt{1-768^2t})\) through the recurrence
\[
E_m=\bigl(4(1-768^2t)-2\bigr)E_{m-1}-E_{m-2},
\]
builds \(P=768E_{384}\) and \(Q=P^2-4\cdot769^2(1-769^2t)\), and checks the exact coefficient valuations used in the proof. Successful replay prints `VERIFY_OK`.

The checker does not prove the Newton-polygon theorem itself. That standard theorem is used analytically: a single lower segment of reduced slope \(-1/384\) forces every local irreducible factor degree to be divisible by \(384\), because a root of valuation \(1/384\) can lie only in an extension whose ramification index, and hence degree, is divisible by \(384\).

No floating-point computation is used as evidence. The proof does not claim minimality of the chosen side lengths or any classification beyond the displayed polygon.
