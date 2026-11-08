---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The Fourier product law c_chi=c_chi^-1*c_chi^2 is verified directly from e_x e_y=e_(2y-x). Nonzero support is invariant under inversion and doubling; multiplying inverse equations gives c_chi*c_chi^-1=1 and c_chi^2=c_chi squared. This forces roots of unity satisfying 2^m-1 or 2^(m/2)+1 and orbit independence. Right multiplication breaks into inverse-pair 2x2 blocks with eigenvalues +/-1 if occupied and 0 if empty, and an independent trivial-character 0/1 block. Independently counted 80 versus 512 for groups of order 9. This confirms all odd-order C algebraically rather than by finite sampling.

## originality

PASS

Precedent 2026 Fourier idempotence equation and right eigenvalue SET {0,1,-1} are explicitly credited; they do not by themselves supply integer root-orbit counts, all complex idempotents or a full eigenvalue multiplicity distribution. Relevant 2026 full paper text inaccessible, leaving substantive exact-enumeration priority uncertainty.

## value

PASS

Full arithmetic census for a natural finite family and an explicit same-dimension algebra distinction are mathematically motivated; multiplicity refinement is not equivalent to merely listing possible eigenvalues.

The dated certificate retains the supplied scientific assessment, sources and limitations.
