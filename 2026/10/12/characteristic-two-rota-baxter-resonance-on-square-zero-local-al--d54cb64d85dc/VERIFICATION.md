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

The included `verify.py` is executable with Python 3 and no extra libraries. It enumerates **all** linear operators on six small split square-zero algebras, tests the Rota–Baxter identity directly on ordered basis pairs (sufficient by bilinearity), and compares the answers with the theorem's normal form and enumerator. In particular, the characteristic-two extension field \(\mathbb F_4\) is represented using a root of \(t^2+t+1\).

Actual command: `python3 verify.py`.

Observed checks:

| Radical dimension | Field order | All candidate linear maps | Exact weight-zero maps | Index 1 / 2 / 3 |
| ---: | ---: | ---: | ---: | --- |
| 1 | 2 | 16 | 2 | 1 / 1 / 0 |
| 1 | 3 | 81 | 3 | 1 / 2 / 0 |
| 2 | 2 | 512 | 16 | 1 / 9 / 6 |
| 2 | 3 | 19,683 | 33 | 1 / 32 / 0 |
| 3 | 2 | 65,536 | 176 | 1 / 91 / 84 |
| 2 | 4 | 262,144 | 256 | 1 / 75 / 180 |

Final program line: `VERIFY_OK`.

The program does not verify all fields or dimensions. Those quantifiers depend on the separate algebraic proof using coefficient comparisons and the count of image/kernel pairs for square-zero endomorphisms. No computer algebra package, external certificate, or independent audit was used.
