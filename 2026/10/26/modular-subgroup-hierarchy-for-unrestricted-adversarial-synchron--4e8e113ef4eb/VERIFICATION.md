---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For G=Z/n, n≥2, a(x)=x+1 and b(x)=f(x) arbitrary, define Φ(K)={d:∀x, f(x+d)−f(x)∈K}. Φ maps subgroups to subgroups by telescoping and is monotone; H_0={0}, H_{t+1}=Φ(H_t) grows until fixed after ≤Ω(n) strict subgroup inclusions. Bob can translate a marked pair to any x with a-word, while Alice's a preserves d and b sends d to f(x+d)−f(x). Induction with arbitrary Bob prefixes proves two states force-merge in ≤t Alice moves iff d∈H_t, even with Bob first. Sequential pair merges reduce full image size (Bob words cannot expand image sets), so Alice wins iff H∞=G; if H∞ proper, Bob chooses a perpetual losing marked difference. Each step tests n² differences and ≤log₂ n strict stages. For n prime H1=G iff f constant. Composite nonconstant f periodic mod nontrivial divisor r with outputs in one residue mod r gives H2=G. At n=pq, subgroup lattice forces winning iff f factors mod p or q and values all lie in a single residue class for that divisor. Counts p(n/p)^p plus q(n/q)^q minus n intersection constants (one option if p=q), yielding p^{p+1}, or p q^p+q p^q−pq. Independently iterated all n^n maps for n=2..6, counts exactly 2,3,8,5,36, total 50,068 maps. Source's separate subset-game attractor method was inspected; finite counts support but do not replace all-n induction.

## originality

PASS

Lipin–Volkov 2026 defines this unrestricted game and proves general relation/two-token recognition, which are clear prior stronger *decision* tools over arbitrary automata. Its inspected Section 3 does not give this cyclic map subgroup hierarchy, prime/composite dichotomy or exact semiprime labeled-function enumeration. The cycle arithmetic classification is a specialization with substantially more explicit structure. Ordinary circular automata synchronization is weaker than adversarial winning; earlier prime-order ordinary reset results do not imply this theorem. No demonstrated earlier formula dominates the counts; a specialization of the general relation operator could produce the subgroup criterion, and this derivability is acknowledged.

## value

PASS

A complete criterion and finite algorithm for the whole natural class of cycle-plus-map automata, a sharp prime-versus-composite existence boundary, and exact semiprime map enumeration constitute an infinite-family structural classification rather than a single instance. It isolates the exact obstruction under adversarial interleavings, a distinction material for reset games.

The dated certificate retains the supplied scientific assessment, sources and limitations.
