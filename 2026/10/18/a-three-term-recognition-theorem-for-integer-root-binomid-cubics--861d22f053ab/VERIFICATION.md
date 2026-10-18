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

# Reproducibility and limits

The standalone `verify.py` and its output `verification_output.txt` are provided alongside this document. Execute `python3 verify.py` using Python 3's standard library; no network access or external packages are needed.

The script determines all candidates for integral \(f_2/f_1\) by the exact rational equation \(c+1=K/(m-K)\) after the proof's uniform bounds on \(a\) and \(b\). It checks the twelve rational triples and the three survivors, \(15{,}450\) integral generalized binomial coefficients, \(350\) Pascal-column determinant identities, and \(45{,}100\) additional finite parameter triples. These operations are deterministic integer or rational arithmetic.

The unrestricted theorem uses the monotonic inequalities and candidate equation to reduce infinitely many root-shift parameters to twelve cases; the finite tests are diagnostics rather than a replacement for that reduction. Sufficiency for all \(n,k\) depends on the displayed published integer-determinant identity for Pascal columns, together with the termwise-product property. Independent validation or a formal proof certificate has not been produced.
