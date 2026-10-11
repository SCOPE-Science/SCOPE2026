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

The proof has one literature-dependent structural input and an independent exact computation.

The structural input is the published classification that every Reinhardt polygon with fewer than \(30\) sides is periodic. For \(n=9\), a periodic composition has repetition count \(d=3\) or \(d=9\). Enumerating positive odd-length blocks of sum \(9/d\) leaves only \([(3)^3]\) and \([(1)^9]\).

The exact computation is replayed by `verify.py` from the packaged path. It constructs the \([(3)^3]\) nonagon as three equal three-chord subdivisions of the boundary arcs of a width-one Reuleaux triangle. Exact shoelace arithmetic in SymPy returns
\[
\frac92\sin\!\left(\frac{\pi}{9}\right)-\frac{\sqrt3}{2}.
\]
The script separately constructs the regular diameter-one nonagon and verifies
\[
9\sin^2\!\left(\frac{\pi}{18}\right)\cot\!\left(\frac{\pi}{9}\right).
\]
It also verifies the common side length \(2\sin(\pi/18)\), the common extremal perimeter, and the exact area-gap identity.

Finite enumeration is not being used to infer that all maximum-perimeter nonagons are periodic; that universal reduction is supplied by the inspected theorem. The checker verifies only the finite consequence and the exact geometry once that reduction is established.
