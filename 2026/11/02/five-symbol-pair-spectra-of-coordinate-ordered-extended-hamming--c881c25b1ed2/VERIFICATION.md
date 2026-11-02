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

The analytical argument partitions all coordinate-ordered extended Hamming codebooks into five classes. Its essential identities are the count of fourteen zero-XOR affine-plane supports, three affine planes through each pair of affine points, and the exact conditional probability one third for an opposite four-window to be a plane. The conditional alternating-plane analysis gives an independent exact five-row joint count, not extrapolation from samples.

`verify.py` uses Python's standard library only and reproduces all five joint multiplicities by enumerating \(5040\) normalized permutations. It computes each codebook in two independent forms (zero-XOR four-subsets and affine Boolean evaluations), verifies that there are thirty distinct codebooks each occurring \(168\) times, then compares all sixteen actual codeword pair weights against the proven enumerator formula. Execute `python3 verify.py` and check the final line `VERIFY_OK`.

The computational test is finite and exact, while the combinatorial proof supplies the exhaustive classification independently of program execution. The claim does not address other lengths or other code families. Independent external mathematical audit has not been performed.
