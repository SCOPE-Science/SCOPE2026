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

The published Almeida--Cardoso theorem is taken as the literature input: under \(\sigma(N)/N=5/2\) and \(5\mid N\), it gives \(2^4\parallel N\), \(5^2\parallel N\), and \(31^2\mid N\).

The bundled `verify.py` checks the new arithmetic deductions only. It recomputes \(I(2^4)I(5^2)I(31^2)=993/400\), confirms that the resulting inequality makes \(149\) the least possible additional prime, and reduces the exact quotient for \(I(u)\) at \(\nu_{31}(N)=2,3,4,5\). The corresponding denominators force a prime below \(149\), eliminating all four exponents.

The universal conclusion is symbolic. No bounded enumeration is used as evidence for infinitely many inputs. The verifier output is stored in `verification_output.txt`.
