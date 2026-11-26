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

The support graph exactly represents the stipulated single stochastic rounding: an exact binary16 output has probability 1, otherwise both bracketing states have strictly positive probability. Independently enumerating scaled integers in units 2^-24 and finding the bracket by the local binary16 spacing reproduces all 15,361 states and 30,623 arcs and the transition SHA-256 94b900c38f4dfb6e88c690e7cdead1540bce5d3836c0daa46b0534d0b89c2917. The forward/backward reachability intersection at code 0x3a01 is one 1,746-state SCC; deleting it and ignoring singleton self-loops leaves an acyclic graph by a topological elimination, giving 13,616 SCCs total. This large SCC has an exit, and the only closed singleton classes are 0 and 3/4. Reverse walks give reachability sizes 15,359 and 46 with intersection 44, and only 1/4 and 3/4 reach 3/4 alone. The maximum shortest distance is 23 at seven states. An independent exact rational Tarjan computation agreed. To infer finite-time absorption, every start has a path of at most 23 arcs to a sink, so the smallest positive transition probability gives a uniform positive chance of absorption in each 23-step block, conditional on the start of the block. Every reachable absorber has positive hitting probability, giving the claimed partition. Replay: python3 /workspace/reproductions/binary16_logistic.py. The supplied verify.py was inspected, not run.

## originality

PASS

The supported distinct claim is the exhaustive recurrent-class and basin-reachability classification of the nonuniform IEEE binary16 chain with exact polynomial evaluation then ideal stochastic rounding once. Inspected logistic-map experiments, the uniform-grid stochastic classification, and the deterministic binary16 census do not give this classification. This is an assessment on the checked evidence, not a claim of priority or a general theorem about stochastic rounding.

## value

PASS

This is a complete natural-format support census motivated by the distinction between numerical recovery of finite-time chaotic behavior and the true infinite-horizon law. The two sinks and the exact mixed-outcome partition quantify that failure of indefinite nonperiodicity, even without deterministic rounding or a finite random-number period. They also distinguish near-universal certain fixation at zero from the blanket claim that every start fixes at zero.

The dated certificate retains the supplied scientific assessment, sources and limitations.
