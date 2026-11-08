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

For an induced vertex subset of K_(n1,...,nr), two original parts each contributing >=2 vertices create an induced K2,2=C4, not a threshold graph. If at most one contributes >=2, all singly represented other parts are universal; removing them leaves an independent set. Thus a color class is threshold iff at most one heavy part. For each named color its labelled EGF is F_r=prod_i(1+x_i)+sum_i(e^(x_i)-1-x_i)prod_(j!=i)(1+x_j); formal coefficient extraction of F_r^k multiplied by prod n_i! counts exactly all allowed functions into k named colors, including unused. Onto counts follow color inclusion-exclusion, unordered partitions divide by k!. Pigeonhole gives necessary # {i:n_i>k}<=k; choose distinct heavy colors for large parts and injectively distribute each remaining part to construct a coloring whenever the inequality holds. All boundary cases k=0,r=1, singleton part sizes included. Independent direct graph enumeration and formal coefficient arithmetic reproduced 64 assignments for K_(3,2,2) with k2 and 55,566 for K_(4,4,4) with k3, plus small profiles.

## originality

PASS

Bang-Jensen–Bessy–Reinald (2026) prove the equivalence between alternating bichromatic cycle-free color classes and threshold-induced parts (especially two colors) and hardness for arbitrary graphs, but do not supply complete multipartite named-palette enumerators. Demange–Ekim–de Werra (2005/2006) study polynomial optimization on cographs and split-coloring; the threshold minimum may be efficiently computable already. The exact EGF all k, onto/unordered refinements and explicit size threshold are the assessed additions, not novelty of polynomial decision.

## value

PASS

The complete multipartite family is a natural graph class, and enumerating all threshold-induced vertex partitions with named and unnamed colors gives useful exact polynomials and sharp minimal palette formula, not a mere renaming of ordinary proper coloring. The EGF formula simultaneously tracks any part-size profile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
