---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

`verify.py` checks the theorem directly from the definition on every complete multipartite isomorphism profile through order \(9\). For each nonempty terminal set \(W\), it enumerates connected vertex supersets containing \(W\), identifies those of minimum order, unions their vertices to obtain the literal Steiner interval, and tests whether that interval is all of \(V(G)\).

The script then compares this literal decision with the structural classification for every subset. It independently accumulates the cardinality distribution of literal Steiner sets and compares every coefficient with

\[
F_G(x)=x^N+\sum_{i:n_i\ge2}x^{n_i}.
\]

Finally it computes inclusion-minimal literal Steiner sets, then checks both the minimum Steiner-set size and the maximum size of an inclusion-minimal Steiner set against the stated lower and upper formulas.

The finite range is a reproducibility and boundary stress test only. The proof in `RESULT.md` establishes the theorem for arbitrary positive part sizes and arbitrary numbers of parts.
