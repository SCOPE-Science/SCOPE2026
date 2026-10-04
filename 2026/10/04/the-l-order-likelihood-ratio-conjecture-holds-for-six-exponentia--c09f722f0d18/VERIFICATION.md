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

The analytic proof was reconstructed from the definitions and the likelihood-ratio reduction in Wang–Cheng. The complete six-coordinate basic-vector split was checked: all zero-containing negative vectors have at most five nonzero coordinates, while the only new full-support negative patterns have \(p=3,4,5\) initial positive entries. The source's Lemma A.1 and the needed Lemma A.2 parameter cases \((2,2)\), \((3,3)\), and \((4,4)\) were inspected in the full article.

`verify.py` checks the identity
\[
P_{p-1,p-1}(x_1,y)=G(x_1)+(p-1)G(y)
\]
for \(p=3,4,5\), stress-tests the three imported \(P\)-inequalities on a deterministic grid, and stress-tests all three new full-support directional derivatives on 20,000 deterministic pseudorandom ordered six-tuples. It returns `VERIFY_OK`. These finite computations are supplementary only; the theorem follows from the analytic source lemmas and the case split in `RESULT.md`.

No assertion is made for seven or more components, and no independent audit has been performed.
