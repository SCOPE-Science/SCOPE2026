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

For every integer n>=2, d(n)=floor(n²/4)/n obeys d(n)-2n/9=n/36>0 for even n and (n²−9)/(36n)>=0 for odd n, with equality only n=3. Summing the actual source definitions gives delta>=2N/9, so N<=floor(9chi/2) under delta<=chi. When chi is even and N=9chi/2 all fibers must be I3, count 3chi/2. For odd chi at N=(9chi−1)/2 the entire positive defect is <=1/9. Only sizes 2,4,5 have nonzero defect within budget: e2=1/18,e4=1/9,e5=4/45. Since N=1 mod3 and fibers I3 contribute residue zero, only one 4 or two 2s have viable residue/defect. Remaining fibers are exactly 3(chi−1)/2 I3. The source geometrically realizes chi=3 pattern I4+3I3+23I1 at N=13. All other equality patterns are necessary numerical conditions, not asserted geometrically realized. Separate exact finite enumeration chi=3..8 is corroboration, not proof.

## originality

PASS

The Laface–Li 2026 initiating abstract introduces delta,N and a chi=3 boundary example; its full manuscript remained unavailable from lawful open channels and authenticated Oxford reported disconnected VPN. The predecessor Laface–Li–Liu manuscript gives single-fiber geometric Mori/polyhedral thresholds, not the arbitrary-multiset sharp 9chi/2 envelope and exact equality pattern restriction. A best-of-knowledge comparison found no equivalent general statement; hidden remarks in inaccessible full Laface–Li text are a material residual risk, not automatically failure.

## value

PASS

Both delta and N are central natural numeric invariants explicitly controlling the source paper’s polyhedral Mori cone and semiampleness criteria. Their sharp quantitative comparison is a motivated structural boundary; the complete necessary extremal fiber-size patterns identify the special role of I3 and show that the source’s chi=3 example attains the absolute numerical ceiling. Although the proof is elementary and gives no new existence theorem, it is a useful exact polyhedrality constraint, not an arbitrary unmotivated numeric slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
