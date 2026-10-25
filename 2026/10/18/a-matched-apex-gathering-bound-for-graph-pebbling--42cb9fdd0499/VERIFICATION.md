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

For initial hub load h and O odd outer loads in u active matched pairs, sending pairs to the hub leaves H=(t+h-O)/2. Clearing each pair costs one hub pebble and requires hub >=2 at each initiating move, hence it suffices that H>=u+1. Since Q=O+2u<=4r, all t>=4r obey this except potential t=4r,h=0 and all outer loads odd; then at least one matched pair has load >=3. The two legal internal moves a->b->a make both loads even and use two pebbles. Transfers then give hub exactly r with r-1 remaining active pairs, so all residuals clear. Checked boundary t=4r, r=1,2,3,4 by enumerating respectively 15, 495, 18,564 and 735,471 weak compositions and directly replaying this construction; higher t follows analytically by the Q/parity inequalities.

## originality

PASS

Csernák–Soukup define stacking and prove a general 2|V|2^diam upper bound and exact complete, multipartite, path cases. Their full HTML text was inspected, including bounds and examples; no matching fixed-hub matched-outer-pairs theorem was found in inspected relevant sections. The specific unconditional fixed-center bound sharpens the general estimate for universal-vertex matching graphs. Classical cover-pebbling and target-pebbling parameters are distinct, not interchangeable.

## value

PASS

The matched remainder supplies a natural structural graph condition enabling an explicit fixed-destination gathering strategy. The linear size bound applies uniformly to all friendship graphs and edge supergraphs, substantially sharper than general diameter-two stacking bounds. It is a motivated class-wide constructive theorem rather than a tiny case, although universal exact equality is not asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
