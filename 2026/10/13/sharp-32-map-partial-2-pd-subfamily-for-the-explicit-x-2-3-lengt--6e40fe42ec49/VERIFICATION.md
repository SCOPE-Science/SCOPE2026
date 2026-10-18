---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Reconstructed exact GF(64) bit-polynomial arithmetic, all 128 rational affine points, 64 information and 64 check coordinates, 128 source automorphisms and their permutation action. Exactly T={0,1,theta^56} vertical fibers lie wholly in H; W=span_F2(1,theta^56) has size four and partitions x-values into sixteen cosets, each map covers just 3 of 4 vertical pairs in a coset, forcing >=2 parameters per coset -> >=32 maps. Independently verified the displayed 32 selected maps each belong to family and cover every one of C(128,2)=8128 unordered position pairs with minimum multiplicity one; exact cover histogram reproduced. This is complete finite exhaustive verification plus structural universal subfamily bound, not a heuristic solver timeout.

## originality

PASS

The primary named source constructs a 128-map partial 2-PD family. Accessible bibliographic abstract and partial preview did not disclose a 32-map optimized subfamily; full same-source text could not be retrieved via OA, arXiv or authorized Oxford due disconnected VPN, so its actual Theorem 4.5/Example 4.6 and possible appendix optimization were not fully checked. The independent exact certificate establishes what the new claimed computation says but cannot by itself prove priority. Best-of-knowledge O PASS with major explicit source-access risk, subject to later full-text check. Another published Hermitian/norm-trace PD result concerns different codes.

## value

PASS

For a published explicit family of 128 permutation-decoding maps, minimizing the number of maps while retaining complete 2-error coverage reduces decoder trial complexity fourfold. The exact 32 lower bound is a natural fixed-family optimization with a combinatorial coset obstruction and verifiable complete finite certificate; no downstream broad theorem required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
