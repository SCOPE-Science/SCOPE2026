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
The reproducible checks use the packaged exact Python and C++ programs plus the complete finite witness lists.

Executed `python3 verify_small.py`: `SMALL_CERTIFICATE_OK odd_z=38 exceptions=720 last=19067`.

Executed `g++ -O3 -std=c++17 verify_large.cpp -o verify_large && ./verify_large`: `PRACTICAL_COUNT=3197350 RESIDUES=99225 MAX_FIRST=41235272 RESIDUE=56897 BOUND=41236217 ODD_WITNESSES=1989 EXCEPTIONS_ABOVE_19067=1 FIRST_EXCEPTION=20177`, followed by `LARGE_CERTIFICATE_OK`.

Scope of finite checks: all integers through \(19067\) for the exception list; all \(99225\) residue classes for least practical representatives through \(42000000\); all odd integers between \(19069\) and \(41236216\) via certified odd Zumkeller witnesses and all even practical numbers in this range. The special odd target \(20177\) is covered by \(20176+1\). The unbounded tail is supplied by the coprime-multiplication progression, not by enumeration. No formal proof-assistant or independent audit was performed.
