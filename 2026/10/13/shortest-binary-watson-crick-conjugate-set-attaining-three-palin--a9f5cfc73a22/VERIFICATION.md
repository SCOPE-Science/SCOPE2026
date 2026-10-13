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
# Verification

Run `python3 verify.py` beside `certificate.json`.

For every binary word of lengths \(1\) through \(7\), the verifier constructs \(C_\theta(w)\) from every cut \(w=uv\) as \(\theta(v)u\). Independently, it enumerates candidate words \(v\) and retains exactly the solutions of
\[
qv=\theta(v)w.
\]
The two sets must agree for every input word.

Ordinary palindromes are then recognized by direct reversal equality. The verified maximum counts by length are
\[
2,2,2,2,2,2,3.
\]
At length \(7\), exactly \(\mathtt{0100011}\) and \(\mathtt{1011100}\) attain three. The verifier checks their complete palindrome sets and the binary-complement relation between the two witnesses.

The computation proves only the stated finite shortest-attainment classification. Independent audit has not been performed.
