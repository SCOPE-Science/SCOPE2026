---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Probability-normalized torus orthogonality counts pairs of ordered triples with equal linear and cubic sums. The diagonal multiset weights yield 4+12·9+4·36=256. For four distinct real frequencies the rows 1,n,n³ are independent (a nonzero cubic cannot vanish at four distinct arguments), so lattice differences lie on one primitive integer line. The positive mass of a nonzero relation is at least two by the linear moment constraint, so any size-three collision uses the primitive relation up to sign. Canceling common frequencies leaves masses two or three, with disjoint supports of total size at most four: pure constant-vs-constant is impossible, leaving exactly the five listed types. At mass two, using the cubic sum identity for pairs shows that nonidentical pairs of the same linear and cubic sum have zero sum, including the repeated-entry case whose repeated value is then zero. At mass three, 2a+b=3w gives a=w+h, b=w−2h and the residual cubic moment is 6h²(3w−h), forcing the ratio (−5,1,4) in the nontrivial three-site case. The two four-site mass-three conditions are precisely as stated. Their weighted pair surpluses and that of the three-site mass-three case are 18, 12 and 6. Mass two allows four choices of common frequency; the two pair types give products (6,9,9,18) or four 18s and hence surpluses 84 or 144. No fiber of three is possible: endpoints would differ by at least twice a primitive relation, of mass at least four. Strict convexity on positive frequencies rules out the distinct-vs-constant mass-three type and signs rule out the symmetric and ratio types. Independently computed all six witnesses and the positive baseline witness; python3 /workspace/branches/check_5.py counts ordered triples directly and checks the exact conditions on all 58,905 four-subsets of [−18,17]. The primitive kernel proof is universal; the sweep is supplementary.

## originality

PASS

The collision-free baseline and balanced single-defect surplus are covered by a prior more general group-character calculation. Credit applies to the distinct complete integer cubic-graph classification, including the other four defect types, their exclusivity and attainable energies, and the arithmetic restriction for positive supports; do not present 256 or the conditional 274 formula as independently new.

## value

PASS

The probability-normalized sixth moment is a standard way to detect integer third-order resonances for Airy dispersion. Four modes give the first rank-one moment kernel on arbitrary distinct supports and permit balanced four-site defects that three modes cannot realize. An exact level set with arithmetic tests and comparison to all-positive frequencies distinguishes large sign-driven excesses from the much smaller balanced excess; this is an exact benchmark for sparse periodic Airy spectra and not just a bounded search for examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
