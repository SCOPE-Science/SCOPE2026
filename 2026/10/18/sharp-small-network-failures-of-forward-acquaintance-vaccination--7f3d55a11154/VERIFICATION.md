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

Exactly as defined (random first vertex, random OUT-neighbor for vaccination, random surviving seed, iid open directed arcs), a_v=(1/n) sum_{u->v}1/outdeg(u), and exact Bernstein coefficient expansion Δ=[nL(n-1)]^-1 sum B_k p^k(1-p)^(m-k). Inspecting original C++ confirmed enumeration of all 2^(n(n-1)) directed labels with reachability closure; independent compiled C++ independently enumerated all strongly connected n=2..4 graphs (counts 1,18,1606) with 24 relabelings as sole positive-Bernstein n=4 exceptions, and independently enumerated all n=5 graphs with <=8 arcs (34059 strongly connected), finding exactly 120 eight-arc full-transmission harmful graphs in a single asymmetric orbit and none at <=7 arcs. Exact G4 B=(0,1,0,-20,-60,-75,-44,-10) yields Δ=p(1-6p-5p²)/72. G5 B=(0,-18,-150,-486,-786,-660,-252,-12,12) yields displayed polynomial and Δ(1)=1/20. Complete original code also enumerates 2^20 n=5 graphs; independent checker covers only the decisive <=8-edge cutoff.

## originality

PASS

Acquaintance immunization introduced for undirected heterogeneous networks and epidemic thresholds; directed epidemic studies distinguish infection risk and onward spread but do not establish the precise smallest finite strongly connected counterexamples for this out-neighbor rule, uniform post-vaccination seed, and expected Reed--Frost reachability. Analogous friendship-paradox sampling statements do not mathematically imply these exact finite extremizers.

## value

PASS

Sharp smallest-network counterexamples in a concrete directed intervention model expose two distinct performance boundaries (any transmissibility versus full transmission), with exactly classified graph witnesses; natural finite optimization and model-design caution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
