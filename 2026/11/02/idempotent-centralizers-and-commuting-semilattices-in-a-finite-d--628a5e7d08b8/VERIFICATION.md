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

# Reproduction and limits

Use Python 3 standard library: `python verify_path_centralizers.py`.

The independent enumeration generates maps from an initial value and each of the \(2^{n-1}\) binary increment words, discarding those that exceed \(n\). It checks the known size of the monoid and confirms idempotents by the actual test \(f\circ f=f\). For each clamp, it directly tests the multiplication equality \(f\circ e=e\circ f\) for *all* enumerated \(f\), comparing exact multiplicities with the theorem. It also confirms the total commuting-pair formula and each ordered idempotent-pair overlap criterion. These comparisons run for \(1\le n\le10\). Direct subset enumeration checks every clique coefficient and maximal clique for \(1\le n\le5\). The extra \(n=1\) check confirms the degenerate extension, though the theorem is stated for \(n\ge2\).

Successful output ends in `VERIFY_OK`; examples include \(A_4=102\) and \(A_{10}=28779\). No external dependencies or downloaded data are required. Finite checking is not an infinite proof, and neither the finite checks nor a bibliographic search are independent mathematical audits or global priority certificates.
