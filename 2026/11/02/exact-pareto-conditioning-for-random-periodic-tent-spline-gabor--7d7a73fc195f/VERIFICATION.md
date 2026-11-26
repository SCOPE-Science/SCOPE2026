---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The indexed unit-step coefficient sum is a Zak multiplication operator. On each unit cell the tent has just two adjacent terms, with a nonnegative cross coefficient, so frequency 0 simultaneously maximizes all contributions and frequency 1/2 minimizes them. Continuity identifies extrema with essential extrema. This gives the stated m and circular least-squares bounds even with repeated offsets. Independently, A/4 is the squared distance of the projected phase vector to the lattice P Z^m in the orthogonal complement of the diagonal, with P orthogonal projection; minimizing over the common real center and all integer lifts gives this identity. The images of e_2,...,e_m form a lattice basis with Gram determinant 1/m. A nonconstant integer vector has at least m-1 unequal unordered pairs, so the shortest nonzero projected lattice vector has length sqrt((m-1)/m), attained by e_1. The ball of radius sqrt(a)/2 for the stated 0<a<1/4 injects into the quotient. Haar probability is its Euclidean volume divided by lattice covolume 1/sqrt(m), exactly the stated expression. Substitution gives the Pareto coefficient; integrating the tail gives the strict moment cutoff and logarithmic divergence at the threshold. For m=2, the shorter-distance law gives A=2 delta^2 and kappa=delta^(-2), including the stated K=4 endpoint. Read VERIFICATION.md and CHECK.py as evidence; the frozen rational/grid tests were not run and are not the proof.

## originality

PASS

Best-of-knowledge pass for the exact fixed-m random conditioning law and its moment consequence. The deterministic bounds and frame criterion coincide with the indexed cubic-gap-defect record, and are not credited as distinct on their own. Catalogue dates are not proof of priority. The strongest same-model literature gives the Zak multiplier and sufficient high-probability estimates, not the exact level-set identification and probability with this normalization.

## value

PASS

The exact tail resolves a finite-window stability question not settled by almost-sure frame existence or large-m high-probability estimates: three random shifts still have infinite mean condition number, whereas four have finite mean. The coefficient also quantifies the frequency of near-singular frames, for the same model and not just up to asymptotic constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
