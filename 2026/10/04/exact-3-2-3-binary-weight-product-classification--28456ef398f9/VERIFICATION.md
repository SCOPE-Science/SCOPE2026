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
Run `python3 verify.py`.

The verifier specializes the published bound to
\[
ab<2^{-13+4\cdot2\cdot3}=2048.
\]
It then enumerates every exponent triple
\[
1\le u\le10,
\qquad
1\le v<w\le10
\]
for
\[
a=1+2^u,
\qquad
b=1+2^v+2^w,
\]
retaining only products below the strict bound. There are exactly \(119\) retained triples.

Exactly two retained triples have product binary weight \(3\):
\[
(u,v,w)=(1,1,2)
\]
and
\[
(u,v,w)=(2,1,2).
\]
They yield
\[
(a,b,ab)=(3,7,21)
\]
and
\[
(a,b,ab)=(5,7,35).
\]

A second direct integer enumeration below the same rigorous bound reproduces the same two solutions.

A successful replay prints `VERIFY_OK`.
