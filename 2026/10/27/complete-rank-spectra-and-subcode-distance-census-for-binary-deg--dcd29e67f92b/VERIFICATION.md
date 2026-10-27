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

# Verification record

The complete proof is in `RESULT.md`. The independent finite sanity checker `verify.py` uses standard-library Python and requires no external packages. From the directory containing the files, execute:

```sh
python3 verify.py
```

The stored output `verification_output.txt` is the exact output from the checked execution. It includes `VERIFY_OK` on the last line. The verifier constructs every binary matrix induced by \(L_{a,b}(x)=ax+bx^2\) over explicit polynomial-basis fields for \(m=2,3,4,5\), rather than assigning weights solely from coefficient patterns. It checks the kernel/rank dichotomy and all coefficient hyperplanes directly.

It enumerates every binary subcode for \(m=2,3,4\), identifies both axis-intersection dimensions by binary rank calculations, and checks the exact population formula for every dimension. It additionally computes weight enumerators directly from all subcode elements for \(m\le3\). For \(m=2,3\), an independent search of all dimension-\(m\) subspaces confirms exactly two with only full-rank nonzero elements.

These are finite exhaustive tests only for the displayed extension degrees; the statements for all \(m\ge2\) rely on the explicit field-kernel and graph-counting proof. No external independent audit or human verification is asserted.
