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

The verifier builds
\[
F_2=\mathrm{MO}_2\times2^4
\]
with \(96\) elements and explicit meet, join, and orthocomplement tables.

For each of the \(96^2\) ordered pairs, it computes the least operation-closed set containing the pair. This is exactly the image of the unique endomorphism determined by that pair. The resulting exact rank count is
\[
\{2:4,\ 4:564,\ 8:3720,\ 12:32,\ 16:2880,\ 24:672,\ 48:1152,\ 96:192\}.
\]

The verifier separately constructs every complement-preserving permutation of the four middle \(\mathrm{MO}_2\) elements and every permutation of the four Boolean coordinates. It obtains \(8\cdot24=192\) automorphisms, checks preservation of every basic operation, and verifies the \(15\)-orbit profile.

It also verifies that the standard two free generators generate all \(96\) elements and that exactly \(192\) ordered pairs do so.

The script prints `VERIFY_OK`.

## Limits

The exhaustive calculation is complete only because \(F_2\) is finite. No analogous exhaustive claim is made for free orthomodular lattices on three or more generators.
