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

# Verification of the digit-complement reflection theorem

## Reproduction
With Python 3, run `python3 verify.py`. The checker uses only the Python standard library and prints exactly:

`VERIFY_OK count_identities=158464 finite_progression_transfers=142800`

For the count identity, it exhausts all eligible patterns of lengths one through four over bases two through five, and tests the first 128 integer arguments with a sufficiently large padded digit width. For the progression identity, it exhausts eligible patterns of lengths one through three over bases two through four, moduli two, three and five, starting indices 0 through 15, positive differences one through five, and progression lengths one through five. These bounds are finite; they are diagnostic only.

## Proof checkpoints
1. For \(n<b^{K-r}\), the width-\(K\) expansion begins with at least \(r\) zeros. Consequently no factor equal to the nonzero-containing pattern starts outside the chosen width.
2. Complementing the width-\(K\) expansion gives exactly the width-\(K\) digits of \(b^K-1-n\). All interior pattern occurrences therefore correspond bijectively.
3. The only new left-boundary factor has the form \(0^t(b-1)^{r-t}\) with \(1\le t<r\), contributing the explicitly defined constant \(\chi(\bar v)\), independent of \(n\).
4. A sufficiently wide reflection sends \(n+(L-1-j)d\) to \(N+jd\) for every \(j\), preserves \(d\) and shifts all residues uniformly. Repeating with the patterns swapped yields equality of attainable length sets and suprema.

## Limits
There is no claim for the all-zero or all-maximum patterns, fixed-origin progressions, or exact numerical maxima. Finite tests are not an infinite proof; the general claim rests on the displayed elementary bijection and boundary analysis. Independent audit is not performed.
