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

For reduced positive-degree complex plane support, Bézout connects the components. The normalization map identifies finite fibers, lowering Euler characteristic by the sum of branch counts minus one; identifying finite subsets does not change H_2, so b_2 is the number of components. It follows that b_* = 2 + 2 sum g_i + sum_p(b_p−1). Substitution of the genus–delta and Milnor–branch identities and splitting b_p−1 into the within-component contributions and k_p−1 gives exactly the stated local defect after Bézout. At k_p≥2, the intersection sum is at least binom(k_p,2); vanishing defect forces k_p=2 and multiplicity one there, and zero component Milnor numbers force smoothness. Successively choosing general components gives these transverse double points and avoids prior crossings. The fixed-r objective depends positively on sum d_i², strictly improved by transferring a unit from a smaller degree >1 to a larger one. Strict convexity in r leaves the endpoint comparison: the reducible endpoint difference is (d−5)(d−2)/2; the global maximum is 2,3,5,8 for degrees 1–4 and d²−3d+4 thereafter. The quartic global tie and the quintic reducible-only tie are correct. A nonreduced divisor has support of degree ≤d−1 and inherits its Betti numbers; M(d) is increasing and M(d−1)=d²−5d+8 is below the reducible threshold by d−1 for d≥6, justifying the certificate for all divisors. Independently checked 271 positive-degree partitions through degree 12 by recursive generation and the global Milnor formula at the nodal extremizer (python /workspace/branches/independent_math_checks.py, section 3). This is an algebraic finite check, not a topological proof. Inspected the frozen checks/betti_envelope.py without executing it.

## originality

PASS

The supported distinction is the sharp finite envelope for each degree partition, including equality geometry and exact comparisons among component counts. The constituent topological and singularity identities are classical; in particular the defect identity can be rewritten using a global Milnor sum and is not itself a new singularity formula. The sources compared do not supply the sharp partition and finite extremizer classification. This is a bounded scientific judgment, not priority certification.

## value

PASS

Finite evaluation of the natural plane linear-system supremum is not supplied by its limiting volume. The partition envelope identifies exactly how distributing component degrees can beat a smooth curve in low degree, and the reducible envelope gives a practical sharp sufficient Betti threshold for reduced irreducibility. The quartic and quintic ties arise from competing geometries, not from an arbitrary set of tabulated degrees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
