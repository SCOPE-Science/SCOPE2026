---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

PASS: On the ten antipodal regular-dodecahedron vertex lines, all pairwise off-diagonal dot products are ±1/3 or ±sqrt(5)/3; direct exact signed-Petersen identities D²=2I−D+J, U²=3I+W, UW=2U give the 1/5/4 even and 3/3/4 odd eigenspace multiplicities. The probability-sphere harmonic addition formula yields Gram G_l=(2l+1)P_l(x_i·x_j), with even normalized eigenvalues 1+3q+6p,1+q−2p,1−2q+p and odd 1+5q+2p,1−5q+2p,1−3p. Exact rational Legendre recurrences establish ranks (1,3,5,7,9,6,10,10,9,10,10,10,10,10,9) for l=0..14 and positivity for l=15..61. Bernstein Legendre inequality gives six |P_l(1/3)| plus three |P_l(sqrt5/3)| <1 from l=62 (explicit rational row-sum upper bound (1971/250)/sqrt(l+1/2)), hence positive definite by diagonal dominance for all larger degrees. Gram pseudoinverse proves feasibility/minimum-norm formula. Independently reconstructed exact rational recurrence and verified tail bounds; no finite extrapolation.

## originality

PASS

PASS best of knowledge: actual general-framework primary source text and result-set searches were checked against each exact claim, with the four distinct prior-implication tests documented. Specializing a stronger bandlimited interpolation theorem or a harmonic moment statement does not logically yield the asserted homogeneous-degree ranks. The accessible primary texts do not imply rank=10 for every l≥15 or the intervening failures; possible uninspected 1958 formulas remain residual risk. No failed search is equated to a novelty proof; unaccessed primary material is named explicitly.

## value

PASS

PASS: The ten antipodal dodecahedral axes are a canonical A5-symmetric sampling set. Exact recovery for one homogeneous harmonic degree is not bandlimited interpolation. Nonmonotone rank collapse at degree five (9 to 6), isolated mean-sector gaps at eight/fourteen, and exact sharp eventual degree-fifteen interpolation give a meaningful sampling/identifiability classification and explicit minimum-norm synthesis, not an arbitrary table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
