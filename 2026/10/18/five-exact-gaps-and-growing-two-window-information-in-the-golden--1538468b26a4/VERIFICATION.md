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

The exact relation F_kα=F_{k−2}+(−1)^k r^k and r²=1−r produces the single-block three-gap successor cycle (modular addition by F_{k−2}, gcd(F_{k−2},F_k)=1). For even k the second block is translated +2r^k; odd k reduces by circle reflection. The explicit insertions into each short/medium/long initial gap partition it into five possible lengths; multiplicities sum to 2F_k+2. For the Sturmian partition the length-n cylinders have the n+1 rotation endpoints. Since all marginal arcs are shorter than 1/2, a nonempty intersection of two arcs is connected and each joint word labels a single refined interval; thus joint entropy equals the five-gap entropy, no multiplicity collapse. Binet limits give I=log F_k+C+o(1), matching independently recomputed C. Independently high-precision Decimal-90 exhaustive gaps across k=6..14 match both histograms exactly within 10^-68, but all-order proof depends on the exact insertion/successor argument.

## originality

PASS

Kupsa–Starosta gives standard consecutive Sturmian partitions and Rokhlin towers; Mishra–Philip/Chung–Graham give ≤6 gap lengths for unions of two progressions. These do not yield exactly five golden-Fibonacci lengths and multiplicities, nor the two-window Shannon information constant.

## value

PASS

Two separated equal observation windows in a zero-entropy symbolic dynamical system are natural: an explicit exact gap refinement and logarithmic divergence of shared information quantify nonmixing across a full intervening block. The complete histogram, not merely a bound on count of gaps, is an independently useful invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
