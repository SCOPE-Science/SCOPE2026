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

The verifier constructs the relevant finite objects directly rather than using the theorem's closed conclusion as its input.

For every labeled poset on \(n\le4\) points, it enumerates all upsets, then all nonempty downsets of the resulting inclusion poset. This reproduces the classical labeled-poset totals \(1,3,19,219\) and the full carrier-size distributions.

For every strict relation inclusion \(P\subsetneq Q\) among those posets, it checks
\[
|\operatorname{Dw}^{+}(\operatorname{Up}(Q))|
<
|\operatorname{Dw}^{+}(\operatorname{Up}(P))|.
\]
It also explicitly builds the proof map
\[
D\longmapsto\downarrow_{\operatorname{Up}(P)}D
\]
for every source downset and verifies that intersection with \(\operatorname{Up}(Q)\) recovers \(D\). Finally it verifies the chain and antichain equality cases against \(n+1\) and \(M_n-1\).

Replay:

```text
python3 verify_order_refinement.py
```

Expected output:

```text
VERIFY_OK 63276 exact assertions; 242 labeled posets; 3064 strict refinements; 26554 injection images
```

The finite replay checks the mechanism exhaustively through four points. The proof for arbitrary finite size is the injection and explicit non-surjectivity witness in RESULT.md. Independent audit has not been performed.
