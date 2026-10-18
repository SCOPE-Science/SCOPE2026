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

# Reproducibility and scope

The included standalone `windmill_forcing_verify.py` uses standard-library integer combinatorics and a graph-neighbourhood implementation of the local colouring rule. Run `python windmill_forcing_verify.py`; no network calls or third-party modules are required.

The checker enumerates all \((m+2)^{km+1}\) possible labelled blank-or-colour assignments for each of the seven pairs \((k,m)=(1,2),(2,2),(3,2),(4,2),(1,3),(2,3),(1,4)\), a total of \(366142\) assignments. It rejects incompatible starting colours, repeatedly fills vertices whose neighbours exhibit exactly \(m\) distinct colours, and compares exact coefficient counts with the claimed formula. The \(k=1\) computations serve solely as an external boundary sanity check. For the claimed domain \(2\le k,m\le7\), the checker also verifies one explicit minimum successful seed pattern for every initial choice of hub hue. All listed checks succeeded.

The proof's critical steps are the invariant preventing any first force in a blade with at least two blanks; the hub-first characterization when the hub is blank; the exact enumeration of the \(m\) common-omission obstructions per full proper colouring; and unique full completion for successfully forced initial assignments. These mathematical arguments, not enumeration, prove the infinite theorem. The verification code does not certify all integer parameter values or search all existing literature. Independent validation and external audit have not been performed.
