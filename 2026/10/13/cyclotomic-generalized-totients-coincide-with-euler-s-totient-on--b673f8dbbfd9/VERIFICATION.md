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

The proof is symbolic and unbounded. The following checks were performed independently of the proof text:

1. For each prime-power cyclotomic index \(m\in\{3,4,5,7,8,9,11,16,25,27\}\), construct \(\Phi_m\) directly.
2. For every \(2\le n\le400\), count residues \(r\) with \(\gcd(\Phi_m(r),n)=1\) from the definition.
3. Independently compute the predicted local product using the root-count rule \(ho_m(\ell)=1\), and \(ho_m(p)=arphi(m)\) exactly when \(p
e\ell\) and \(p\equiv1\pmod m\).
4. Compare both values with Euler's totient and verify that equality occurs exactly when the prime support of \(n\) is \(\{\ell\}\).

The extracted script reports:

`VERIFY_OK m_cases=10 n_limit=400 checked=3990`

The finite range is a regression check only. The general statement depends on the CRT product, the exact root classification in finite fields, and the parity argument in `RESULT.md`.
