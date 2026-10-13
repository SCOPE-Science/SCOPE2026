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

Run `python3 verify.py` beside `certificate.json`. Only Python 3 and its standard library are required.

The script reconstructs all \(192\) elementary states \((c_1,c_2,c_3,p)\), with the carry bounds \(0\le c_j\le j\), directly from binary addition. It computes the exact high-bit terminal reachability for each of eight relative masks and exhaustively discovers all \(195\) subset states reachable after the obligatory low bit \(1\) of an odd difference.

The verifier checks that exactly five, six, and 184 reachable subsets admit hexadecimal terminal masks `0x6e`, `0xf7`, and `0xff`, respectively. It checks every transition-closure condition that proves the exceptional LSB-first digit classes and verifies the precise zero-orbit structures. This is a complete *finite-state certificate*: no maximum difference or starting index is assumed.

It independently builds explicit starting-position witnesses from carry paths for every accepted mask at each difference \(1\le d\le511\), checks their Thue–Morse digit sums, and checks complements. Finally it enumerates all four-term arithmetic factors within the first 80,000 positions at each \(1\le d\le128\), matching the exact count and missing-pattern descriptions. These supplementary bounded tests validate the implementation but do not establish the infinite theorem without the finite-state proof.

The checker has no dependencies on external services or unpublished files and reports the exact numbers of states and witnesses upon success.
