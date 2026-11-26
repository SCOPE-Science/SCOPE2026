---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For A an automorphism has f -> ue+tf, e -> t^2 e by preservation of [f,f], and tensor pushforward has weight t^4/t=t^3 on the parameter. For B use g=f-e: the only nonzero bracket is [g,e]=e, so preservation of Ke and the brackets forces e -> te and g -> g. Family I has delta(e)=0 and delta(g)=(A_0+gamma) e⊗e+gamma e⊗g, so the weights are 2 and 1, respectively. For gamma nonzero normalize uniquely to gamma=1; for gamma zero take square classes of the first coefficient. Family II has only delta(e)=lambda(e⊗g-g⊗e), so its input and output transformations cancel. Its nonzero members cannot lie in family I since the derived line has nonzero cobracket there. These arguments have no exceptional characteristic. Source witness formulas and the defining coalgebra and compatibility identities are integral polynomial formulas; the parameter identities holding over the reals are integral polynomial identities and specialize to every field. This argument does not transfer real-field completeness. A and B differ in nilpotence. Finite-field multiplicative cyclicity gives the gcd counts, and the raw reduced locus is a disjoint union of an affine line and a plane and line meeting at the origin. Thus over extensions its count is q^(2m)+2q^m-1 and the exponential generating definition of zeta gives the stated rational function, not the zeta of the orbit set. Read VERIFICATION.md and artifacts/verify.py and compared artifacts/verify_output.txt against the formulas; no uploaded code was run. The proof applies to arbitrary fields independently of the five retained prime-field enumerations.

## originality

PASS

The displayed witness families and even the automorphism group for B have relevant prior coverage. The distinct result is the orbit classification for these induced tensor maps with the witnesses forgotten, including its field dependence. No broader classification of triangular structures over arbitrary fields is claimed.

## value

PASS

The source tables pose a natural classification problem after forgetting redundant witnesses. The solution distinguishes genuinely different continuous moduli and arithmetic square/cube classes, and gives exact isomorphism counts over all finite fields. This is useful even though it intentionally does not classify all positive-characteristic triangular structures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
