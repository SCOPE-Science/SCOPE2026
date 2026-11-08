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

For any finite directed multiquiver, including loops and parallel arrows, in characteristic two the vertex coefficients of a=s+r satisfying a^3=a must be in {0,1}, because c^3-c=c(c-1)^2? In characteristic 2, c^3-c=c(c+1)^2, so roots 0,1 as SET but the zero scheme may be nonreduced. The arrow coefficient is (c_u^2+c_uc_v+c_v^2-1)r_alpha; it vanishes as a constraint exactly for endpoint values other than (0,0). Consequently each reduced root stratum U={zero vertex coefficients} is an open-and-closed affine space of dimension m-e_Q(U), yielding 2^|V| irreducible components, finite-field polynomial sum q^(m-e_Q(U)) and leading coefficient equal to independent vertex-set count. Decomposing a into e=a² and n=a+a² gives e²=e, n²=0, ene=n and crossing-arrow idempotent coefficients, internal-S nilpotents. The 1+J conjugation shifts only crossing arrows, giving q^b(S) orbits each q^c(S). The #P reduction is parsimonious by orienting any finite simple graph; membership follows by guessing and checking U. Independent exact check on oriented triangle gives dimensions 3:4, 2:3, 0:1 and N(2)=45; source verifier checks small characteristic-two quivers. These are REDUCED geometries; no claim is made about nonreduced scheme.

## originality

PASS

Best-of-knowledge: the evaluated exact final statement differs from inspected antecedents on hypothesis, characteristic, invariant or quantifier; fundamental mechanisms/prior special cases credited. The source inspections and four implication comparisons below state actual reading and residual priority risks, without interpreting a failed search as proof of novelty.

## value

PASS

An arbitrary radical-square-zero quiver algebra is a canonical representation-theoretic object, and the pointwise tripotent equation a³=a is natural in ring theory. Its *entire* affine-component dimension profile and 1+J orbit partition are controlled by induced-arrow counts. Relating top-dimensional tripotent components parsimoniously to independent sets gives a useful exact graph-algebra bridge and a sharp counting-complexity boundary, beyond a routine single evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
