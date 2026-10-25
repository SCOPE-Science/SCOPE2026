---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

For k>=2, n and m positive binary palindromes with canonical digits and m-n=2^k, split into L(n)<=k, same-length addition, and one-digit overflow. In the short case, reflecting the set of one-bit positions in n and m repeatedly translates positive indices by a=k-L(n)+1; this forces a|k and an exact arithmetic progression of one bits, one for each divisor. In the same-length case the changed-bit carry interval is reflection invariant and must be a singleton {k}, giving L=2k+1 and a central zero-to-one toggle with 2^(k-1) choices. In the overflow case, reflecting the new top bit and the forced upper zeros, using k>=2, makes every intermediate bit of n zero; n=2^k+1 and m=2^(k+1)+1 is unique. The three length classes do not overlap; their counts give 2^(k-1)+tau(k)+1. Independent bounded enumeration reconstructed entire pair sets for k=2..5 and searched larger lengths; the proof handles all k.

## originality

PASS

Best-of-knowledge comparison of exact theorem and implications, not title matching. The fixed-gap translate formulation is equivalent to the pair count, but qualitative finiteness for pure powers of two does not supply its three-family exact enumeration. The prior infinite-gap characterization excludes pure powers 2^k for k>=2, but cannot imply their precise finite multiplicities. General arithmetic-progression extremal results do not settle the correlation count. A database listing counts for individual k would not by itself prove the universal three-family classification; no all-k formula appeared in the inspected primary theorem. The submitted count implies finiteness and correct k>=2 boundary, not vice versa. Earlier results do not logically force the isolated overflow pair or the precise term tau(k).

## value

PASS

The binary gap family is the natural complement to the nonbinary analysis, and its extra carry-overflow pair is a genuine different structural phenomenon. It provides explicit multiplicities and a complete parametrization for all nontrivial pure powers in the finite-representation range of the JIS Question 26, resolving far more than a small numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
