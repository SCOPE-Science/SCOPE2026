---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

PASS: At delta=0, hot sites 0 and 3 reset autonomously; spins (X,U,V,Y) form a closed four-spin Markov subsystem. Stationary generator equations give D=16-ab and <XU>=4a/D, <XV>=<UY>=ab/D, <XY>=0, <UV>=4(a+b)/D, <VY>=4b/D, <XUVY>=ab/D. Hence literal ordered-pair product defect F0= -a^2*b^2/D^2 and connected 4th cumulant -2a^2*b^2/D^2. Independently solved all sixteen stationary generator states using exact rational linear algebra for a=1/2,b=1/3 and got defect -1/9025. A shared marked-clock coupling of perturbed and hot-reference systems tracks a backward single ancestry until reset; probability of a different outcome at the first reference-hot reset is <=delta. For products of k spins, discrepancy <=2k delta, yielding |Fdelta-F0|<=8delta+4delta+4delta=16delta for every ring N and the infinite system (max copy probability<1 ensures ancestry termination). Thus for delta=1e-6,a=1/2,b=1/3 the certified upper bound is strictly negative; all baths are then distinct, positive and finite. Finite exact check corroborates local identities, not the infinite-volume coupling.

## originality

PASS

PASS (best-of-knowledge): The current explicit sign shows nonextension of the exact literal two-pair formula, not of a possibly modified sum over pairings. Period-three cannot be obtained by relabelling two alternating temperatures with all three distinct values. The prior general-looking multispin formulas are not under the claimed heterogeneous stationary hypotheses. A later multitemperature theorem may contain the computation, retained as priority risk. Earlier two-bath factorization cannot imply the opposite-sign period-three witness, and the proof establishes a genuine boundary of that exact formula. It does not rule out weighted modified pairing identities. Specific priority and access qualifications are recorded below.

## value

PASS

PASS: Resolves the literal ordered two-point stationary factorization extension queried for more than two periodically alternating baths in the primary 2002 work. Provides an explicit nonzero negative four-spin defect and uniform all-ring/all-finite-bath witness; does not pretend to refute all augmented representations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
