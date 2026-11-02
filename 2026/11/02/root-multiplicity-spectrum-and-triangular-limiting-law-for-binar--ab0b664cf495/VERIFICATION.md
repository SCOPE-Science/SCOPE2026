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

The analytical certificate is the explicit necessary-and-sufficient root criterion and binomial convolution in `RESULT.md`. These establish the formula for all integer semilengths; numerical tests only corroborate it at finite sizes.

The attached `checker.py` is standalone Python 3 and requires no third-party packages. Execute from the directory containing it and `checker_output.txt`:

```sh
python3 checker.py
```

The script independently tests each potential distinct root by a two-copy interleaving dynamic program, without relying on the displayed criterion to determine reachability. It then compares the exact root index set and the multiplicity histogram for every two-one word at semilengths 1–24, plus algebraic generating-coefficient identities through semilength 100. The recorded output reports 9,500 words and 175,100 root candidates checked, 6,924 words with at least one root, and all assertions passing. The test range is explicitly finite; no random sampling or numerical tolerance is involved.

The published 2023 total for weight-two shuffle squares serves as a consistency check, not an independently original claim. Neither the checker nor this document verifies global publication priority or performs an independent mathematical audit.
