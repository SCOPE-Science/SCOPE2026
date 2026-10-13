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

Run `python3 verify.py` with a standard Python 3 interpreter. The source and recorded output are included in the package. The script enumerates every one-monomial omission in degrees \(3\) through \(16\), reconstructs all standard nonbasepoint coordinate charts and both exceptional blowup charts when a pure power is omitted, and tests whether their integer semigroups are full or have exactly the missing tangent generator. It also reconstructs powers of the maximal ideal \((v,u^2)\mathbb C[u,v]\) in \(\mathbb C[v,u^2,uv,u^3]\) by bounded exact monomial enumeration and checks Hilbert–Samuel colengths for powers \(1\) through \(10\). It verifies \(60\) exact graded Hilbert-function values against the three projective Hilbert polynomials for degree \(3\) through \(7\).

The symbolic proof in `RESULT.md` establishes the atlas and ideal identities for every integer \(d\ge3\). The finite checks do not establish statements for untested \(d\), and no infinite formal verification, independent audit or external proof certification has been carried out. The historical literature comparison, especially the full original article of Schenzel (1978), is not exhaustive.
