# Independent Audit — 2026/09/10/034

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `79e814409ee1d41311dd95edf726a2152bea745f`
- Disposition: **PASSED**

## Correctness

**PASS** — The residue calculation is sound. Over K=Q(sqrt(-2)), the divisor D_+: x0-sqrt(-2)x1=0 is a smooth geometrically integral plane quartic 6y1^4-5y2^4-10y3^4=0. The numerator has valuation one along D_+, x2 is generically a unit, and the quaternion residue is [-10]=[5]. Since 5 is not a square in K and K is algebraically closed in the function field of the geometrically integral projective curve, the residue remains nontrivial. A Brauer class unramified over Q would remain unramified after base change, so the displayed quaternion is not in Br(X*).

## Originality

**PASS** — Exact equation/symbol searches found no indexed prior carrying this named surface and this quaternion-symbol non-membership calculation. The cited diagonal-quartic literature gives surrounding Brauer-group results but does not supply this exact residue computation.

## Scientific value

**PASS** — Although narrow, the result decisively rejects a concrete proposed Brauer–Manin certificate by an explicit codimension-one residue, preventing downstream use of a ramified symbol as an Azumaya class. The record correctly limits itself to that negative conclusion and does not overclaim local solubility or a Hasse-principle obstruction.

## Limitations

- The audit does not decide whether a repaired quaternion symbol exists or whether X*(Q) is empty.
- The result's scientific scope is a falsification of one proposed class, not a classification of Br(X*).

## Sources

- Diagonal quartic surfaces and transcendental elements of the Brauer group: https://doi.org/10.1017/S1474748010000149 — Background on transcendental Brauer classes for diagonal quartics.
- Diagonal quartic surfaces with a Brauer-Manin obstruction: https://arxiv.org/abs/2201.04573 — Broader arithmetic context; no exact named-symbol calculation located.

This audit is independent of the record's pre-existing AUDIT.json. GitHub was read only as evidence; no repository mutation was performed in this audit chat.
