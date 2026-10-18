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

# Exact verification

Files required: `certificates.json` and `verify.py` from the same package. Run `python3 verify.py` using a standard Python 3 interpreter. No network access or third-party packages are needed.

Observed output during mathematical checking:

```
EXACT_CERTIFICATES_OK=23; INDEPENDENT_CONSTRUCTIONS_OK=50
```

The verifier independently constructs all five Van der Laan window equations and all fifteen valid rank/inter-block/nonnegativity inequalities for each of the \(23\) nonidentity patterns. It checks, over exact rational numbers, the complete eight-coordinate linear-form identity reconstructing the first-block sum. In particular, every inequality coefficient is nonnegative and all \(23\) distinct nonidentity permutations appear exactly once. Therefore the certificates prove the infinite nonidentity case when combined with zero propagation. The identity branch is proved separately in `RESULT.md` and spot-checked on \(50\) admissible starting triples over \(100\) terms each. No conclusion for arbitrary other block sizes or unrestricted sequences is inferred from these finite checks.

The certificates and code are mathematical supporting artifacts, not an independent review. No independent audit or external formal certification is claimed.
