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

The proof was replayed directly from the definitions.

For a prescribed \(\varepsilon>0\), choose bounded compatible factor metrics and the weighted product metric \(\delta(x,y)=\sum_{i\ge1}2^{-i}d_i(x_i,y_i)\). Compactness makes the identity from \((X,\delta)\) to the given metric space \((X,d)\) uniformly continuous. Therefore agreement on a sufficiently long finite prefix implies \(d\)-distance below \(\varepsilon\).

A nontrivial coordinate beyond that prefix exists because infinitely many factors are non-singletons. Two points differing only there remain equal on the controlling prefix after every coordinatewise group action, so their distance stays below \(\varepsilon\) for every group element. This is stronger than the definition requiring closeness only on one horoball, and therefore places every horofunction in \(\operatorname{ND}_{\varepsilon}(X)\). Intersecting over all positive \(\varepsilon\) gives the asserted equality for \(\operatorname{ND}(X)\).

The finite-support expansiveness boundary was checked separately: with finitely many non-singleton factors the system is a finite product, while a nonexpansive factor can be isolated by taking two product points equal in all other coordinates. No numerical computation or finite experiment is part of the proof.

Scientific limits: the argument assumes coordinatewise action on a countable compact metrizable product. It does not apply unchanged to skew products in which a tail difference can feed into finitely many controlling coordinates.
