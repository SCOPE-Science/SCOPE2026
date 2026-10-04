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

The general statement is proved symbolically; no finite experiment or external certificate is required.

## Checked identities
For the pentagon, Proposition 3.6 of the cited 2026 source identifies \(c_{i,i+2}=c_{i+2,i}\). Substitution into the two displayed local exchange relations for the quadrangle \(i,i+1,i+2,i+3\) was checked separately and gives
\[
q_i=q_{i+1}^{-1}+q_{i+1}^{-1}q_{i+3},
\]
\[
q_i=q_{i+1}^{-1}+q_{i+3}q_{i+1}^{-1}.
\]
The left/right multiplications are order-sensitive and yield the same element \(1+q_{i+3}\), which proves adjacent commutativity rather than assuming it.

For cyclic distance \(2\), the checked chain is
\[
q_i(q_{i+1}q_{i+2}-1)=(q_{i+1}q_{i+2}-1)q_i,
\]
followed by adjacent commutativity and left cancellation of the unit \(q_{i+1}\). This gives \(q_iq_{i+2}=q_{i+2}q_i\). On five indices, every distinct pair has cyclic distance \(1\) or \(2\).

For height \(1\), the cited source gives \(ab=2\). Since \(2\) is central and \(a\) is a unit, \(b=2a^{-1}\), hence \(ba=2\).

## Source checks
The defining exchange relation and Proposition 3.6 were inspected in the primary PDF, including direct page images. The same PDF's Example 3.5 was inspected for sharpness: the displayed height-\(3\) frieze contains both \(i\) and \(j\), which do not commute in the Hamilton quaternions. The foundational 2024 PDF was also inspected by page image, and targeted full-text searches found no height-\(2\) or pentagon theorem there.

## Limits
This verifies only the boundary-one theorem stated in the package. It does not classify height-\(2\) solutions, extend to arbitrary boundary coefficients, or assert anything about commutativity of all height-\(3\) friezes.
