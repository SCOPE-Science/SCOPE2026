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

# Verification summary

Run `python3 verify.py` with Python 3 and no third-party dependencies. The program independently enumerates the full space of partial functions from the labeled vertex set of \(K_{1,m}\) to itself, directly tests preimages of all vertex and edge simplices, and counts maps by image rank. It also counts idempotents from the exact condition \(f(v)=v\) for every \(v\) in the image. For \(1\le m\le5\), it enumerates every choice of image-fiber representatives and checks whether any resulting partial section is continuous, thus independently counting nonregular maps. For \(m=6\), it checks all-map and idempotent rank distributions but not regularity by section search.

Actual run returned:

```
m=1 maps=9 idempotents=6 regular=9 verified
m=2 maps=36 idempotents=14 regular=32 verified
m=3 maps=185 idempotents=31 regular=149 verified
m=4 maps=1278 idempotents=68 regular=990 verified
m=5 maps=10857 idempotents=149 regular=8357 verified
m=6 maps=106664 idempotents=326 regular=not brute-checked verified
VERIFY_OK
```

The exact proof for every \(m\ge3\) is in RESULT.md. These checks are finite, and `VERIFY_OK` is not an external certificate or an exhaustive test of unbounded \(m\). The case \(m=1\) is a complete graph and \(m=2\) a path: they are verification boundaries, not priority claims.
