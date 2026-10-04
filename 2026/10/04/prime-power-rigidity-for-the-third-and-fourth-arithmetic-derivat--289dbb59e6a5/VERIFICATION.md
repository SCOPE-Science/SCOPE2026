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

The checker implements integer factorization and the arithmetic derivative from scratch using the Python standard library. It exhausts exactly the finite ranges left by the proof:
\[
e=2,\quad p<64,
\]
and
\[
e=3,\quad p<128
\]
for the fourth iterate.

It also performs a broader regression for both \(D^3(p^e)=p^e\) and \(D^4(p^e)=p^e\) over every prime \(p<500\) and every exponent \(1\le e\le12\).

The broader scan is not part of the infinite proof. The large-prime cases are proved symbolically in `RESULT.md`.

A successful replay prints `VERIFY_OK`.
