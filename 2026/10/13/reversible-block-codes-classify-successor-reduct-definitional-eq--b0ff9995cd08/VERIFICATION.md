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

The general theorem is proof-driven. The decisive steps are:

1. The motivating source fixes the \(\mathbb N\)-part of every \(T(S)\) by the sentences \(R(\mathrm{suc}^n(0))\) or their negations and proves completeness for irregular \(S\).
2. Standard Gaifman locality, after replacing the successor function by its graph, implies that any one-variable first-order definition is eventually determined by a bounded colored-path neighborhood. Thus each predicate definition becomes a finite-radius binary tail rule.
3. The source explicitly notes that every finite pattern occurs infinitely often in an irregular set. Therefore a finite-radius composition that returns the original bit on all sufficiently remote positions of one irregular sequence must return the center bit on every possible finite input block. Applying this in both directions makes the two induced full-shift block maps inverse.
4. Conversely, a finite truth table can be expressed by a first-order formula using finitely many predecessors and successors; finitely many boundary values are named by \(0,\mathrm{suc}(0),\ldots\). Completeness then promotes the standard-model recoding to a joint definitional extension.

The bundled `verify.py` independently checks the finite radius-one refinement. It enumerates all \(256^2=65{,}536\) ordered pairs of radius-one binary rules. A composition has radius two, so testing all \(2^5=32\) five-bit neighborhoods in both directions is exhaustive. The program performs \(4{,}194{,}304\) such composition checks and finds exactly

\[
(15,85),(51,51),(85,15),(170,240),(204,204),(240,170).
\]

These are left/center/right projection and their complements, paired with their radius-one inverses. A second finite replay on a word containing every binary word through length eight checks the same recodings away from boundaries.

The exact run output is:

`VERIFY_OK 4215844 exact assertions`

No independent audit has yet been performed.
