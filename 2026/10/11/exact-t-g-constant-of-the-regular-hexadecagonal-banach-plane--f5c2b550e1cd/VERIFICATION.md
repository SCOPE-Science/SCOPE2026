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
The exact target is
\[
T_{16}
=
1-\sqrt2+2\sqrt{4-2\sqrt2}.
\]
After reduction to the reference edge
\[
x=v_0+a(v_1-v_0),
\qquad
0\le a\le1,
\]
the feasible nondegenerate ordered edge pairs are exactly
\[
(2,13),\ (3,13),\ (3,14)
\]
and their exchanges. Their parameter ranges are
\[
[0,q],\ [q,1-q],\ [1-q,1],
\]
where
\[
q
=
2-\sqrt2-\frac32\sqrt{2-\sqrt2}
+\frac12\sqrt{2+\sqrt2}.
\]

The bundled `verify.py` reconstructs the regular hexadecagon from the edge equations, solves every ordered nonparallel edge pair, confirms those six branch intervals, checks the endpoint identity
\[
\kappa_1q=\kappa_2(1-2q),
\]
and verifies the equality configuration and target radical.

The branch enumeration is finite and exhaustive for the polygonal boundary. Numerical evaluation in the checker orders the algebraically specified branch endpoints and independently replays the stated branch formulas; the continuum proof is the exact edge classification in `RESULT.md`.

No independent audit or independent validation has been performed.
