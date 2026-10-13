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

`verify.py` performs exact integer checks for the finite portion of the proof. It reconstructs the squarefree kernel from Legendre valuations, verifies the displayed values through \(10!\), confirms that no other prime kernel occurs through \(50!\), and checks that every \(11\le c\le50\) has at least two primes in \((c/2,c]\).

The infinite step is not inferred from computation. It uses Nagura's theorem: for every real \(x\ge25\), there is a prime between \(x\) and \(6x/5\). For \(c\ge51\), the choices \(x=c/2\) and \(x=5c/6\) yield two distinct primes in disjoint subintervals of \((c/2,c]\).

Limit: the supplied checker does not re-prove Nagura's theorem.
