---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For a 5-regular graph and total labels <=k, vertex weights range through 6,...,6k, giving k>=ceil((n+5)/6). Handshake forces even n; n<=10 permits only 6,8,10. At n6 the unique K6 has explicit two-label assignment with distinct weights 11,10,8,9,7,6. For n8 and n10, fixing vertex0 complement neighbors to {1..n-6} is w.l.o.g.; an independently written recursion over residual complement degrees with Erdős–Gallai pruning yields exactly 167 and 527481 labeled normalized completions. A SECOND independent program replayed the two source cert8 masks and ALL 149 source cert10 masks against EVERY completion, computing H=G∩F and constructing vertex labels by the same proved degree-class sufficient condition, checking actual weights: all 167 and all 527481 pass. The full 149-mask JSON was reconstructed byte-for-byte; Git blob SHA1 matches pinned e6fb480a1420419fa11715b5a83ac4824cd3d5c5, size 2431. This is genuinely exhaustive finite proof with a proved relabeling normalization, not sample enumeration.

## originality

PASS

Shan–Zhong arxiv:2609.30114v1 proves all-order d=3,4 and asymptotic sufficiently-large orders for fixed regular degree, and states unrestricted d>=5 remains open. Its abstract/readily accessible discussion does not supply an explicit small-degree-five n<=10 cutoff; the full primary PDF could not be obtained (arxiv PDF/HTML disabled; Oxford access vpn_disconnected), so source-inspection limits are recorded without automatic O failure. Broader dense-graph tvs result is an upper bound not stated sharp for all 5-regular n8/10. Resultary indexed corpus returns this result and unrelated regular graph enumerations. K6 case is prior trivial; novelty attaches to universal n8,n10 exclusion and min-counterexample n12.

## value

PASS

The small-order cutoff is a natural complete finite classification in degree five, the first degree the motivating 2026 regular-graph conjecture does not resolve uniformly. Excluding *all* such graphs below twelve with complete independently replayed certificate masks is a substantive exact finite bound rather than arbitrary unmotivated enumeration; no claim is made for n>=12.

The dated certificate retains the supplied scientific assessment, sources and limitations.
