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

For a unit-circumradius regular \(N\)-gon, the verifier uses the exact geometric reduction
\[
m(P_N)
=
1-
\max_{d\in\partial P_N}
\max_{x\in P_N\cap(P_N-d)}
\frac{n_d\cdot x}{h_{P_N}(n_d)}.
\]

Dihedral symmetry reduces \(d\) to
\[
d(t)=(1-t)v_0+t v_1,
\qquad
0\le t\le\frac12.
\]
The script directly forms all half-plane constraints of
\[
P_N\cap(P_N-d(t)),
\]
enumerates candidate vertices, checks feasibility, and maximizes the normalized height.

The numerical reconstruction agrees with the two closed forms for deterministic representatives from both infinite residue classes, including large side counts. It separately checks:
\[
m(P_{10})=\frac{7-3\sqrt5}{2},
\]
the active-line switch locations, and convergence toward
\[
1-\frac{\sqrt3}{2}.
\]

The finite reconstruction is only a regression test. The theorem for every allowed \(N\) is proved by the two exact active-line chamber calculations in `RESULT.md`.
