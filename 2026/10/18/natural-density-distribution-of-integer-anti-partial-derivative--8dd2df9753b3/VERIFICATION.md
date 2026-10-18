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

# Reproduction and scope

Run `python3 verify.py` with the Python 3 standard library. The program completes direct integer derivative enumeration, independent formula-based inverse counting, exact rational inclusion--exclusion generating polynomials, independent finite-modulus residue enumerations, and exact normalization of all truncated probability distributions. The expected terminal marker is `ALL_TESTS_PASSED`.

Exact checked ranges: target \(1\le y\le10000\) for \(p\in\{2,3,5,7\}\), with every possible preimage \(1\le x\le p\cdot10000\) covered; finite residue checks for \(0\le v\le15\) when the lcm is at most 200000; truncated distributions through \(V=45\) for \(p=2\) and \(V=22\) for \(p=3,5,7\). Their omitted tail probabilities are respectively \(2^{-46}\), \(3^{-23}\), \(5^{-23}\), and \(7^{-23}\). Computations are exact rational until decimal display.

The code does not prove the infinite distribution by finite enumeration. The proof in `RESULT.md` derives all infinite results from valuation factorization, residue-class counting, and a geometric tail; all-multiplicity positivity also uses the named, inspected prior constructive theorem. No external expert or independent audit was performed.
