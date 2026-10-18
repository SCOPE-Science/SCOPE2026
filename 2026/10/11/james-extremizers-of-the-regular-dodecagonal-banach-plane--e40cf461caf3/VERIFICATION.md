---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Unit ball P is the regular 12-gon with Euclidean circumradius 1, apothem c=cos(pi/12). Norm comparison gives ||z||_2<=N_12(z)<=||z||_2/c. For any unit x,y, min(N_12(x+y),N_12(x-y))<=sqrt(2)/c by parallelogram. The vertex pair v_0=(1,0), v_3=(0,1) attains it because sum/difference lie on edge-normal rays; sqrt(2)/c=2(sqrt(3)-1). Equality forces both Euclidean chords length sqrt(2), x,y length 1 and perpendicular, hence dodecagon vertices differing by 3 or 9 indices. Converse holds for every dihedral image. No missed edge-interior optimizer.

## originality

PASS

PASS best-of-knowledge based on specific prior publication chronology: Komuro–Saito–Tanaka gives a sqrt(2) endpoint symmetry criterion but not exact dodecagon value nor all maximizers. The dodecagon result was imported at 2026-10-11T13:10:54Z. The all-odd-m theorem in J2, which subsequently covers it exactly, was imported at 13:10:55Z, one second later, so is later coverage not earlier coverage. Other earlier result entries searched do not yield the equality-set classification. This is historical source-order originality only, not a claim of independent discovery.

## value

PASS

PASS: Exact James constant of the first nonsquare 4 mod 8 regular polygon and exhaustive rigid equality set form a natural finite polygonal-Banach invariant. It is a self-contained motivated complete classification at a notable symmetry boundary, not an arbitrary small test; its incremental importance is now reduced by subsequent broad theorem, noted as a risk.

The dated certificate retains the supplied scientific assessment, sources and limitations.
