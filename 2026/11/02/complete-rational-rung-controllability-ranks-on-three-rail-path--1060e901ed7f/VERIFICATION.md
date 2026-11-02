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

# Reproducible mathematical checks

The proof in RESULT.md applies to every integer length \(n\ge2\), every allowed position and every rational \(r\ge1\). Two standalone scripts provide independent finite checks:

- `verify_grid.py` uses only the Python standard library. Its finite-field Krylov algorithm computes the rank of a scaled integer Laplacian at every input site for \(n=2,\ldots,16\) and eight rational rung strengths; it asserts 3240 rank equalities. The tested prime is 1000003. Scale the Laplacian by the positive rational denominator to get integer coefficients, which leaves the rational controllability rank unchanged. A modular match is additional evidence, not an all-length proof.
- `verify_gaps.py` uses SymPy and forms the exact characteristic polynomial \(p_n(x)=xU_{n-1}(1-x/2)\) up to an irrelevant sign, comparing \(\gcd(p_n(x),p_n(x-d))\) to the explicit factors for \(d=1,2,3\) and \(n=2,\ldots,50\). It asserts 147 exact polynomial identities. These finite checks complement the cyclotomic proof and cannot alone certify the infinite statement.

Commands: `python3 verify_grid.py`; `python3 -m pip install -r requirements.txt` followed by `python3 verify_gaps.py`.

All proof claims are conditional on unit longitudinal conductances, uniform rational rung conductances at least one and one unrestricted scalar input. Control-energy bounds, numerical conditioning, nonuniform grids, and irrational rung weights remain unresolved. Independent external verification has not been performed.
