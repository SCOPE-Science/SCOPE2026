---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Checked direct substitution Newton N(0)=1,N(1)=0,Q(0)=33,Q(1)=-181,Q′(0)=-33,Q′(1)=-181,Q″(0)=0 and squarefree Q. Rebuilt exact Fraction rational interval arithmetic independently (not relying on script exit logs): on both Halley intervals and all three Schröder intervals, each split into 64 subsegments, enclosed polynomial values and derivative rational functions with all denominators sign-separated; Q excludes zero throughout. Derivative upper bounds H (<0.1,<1.5) and S (<0.9,<2.4,<0.05), image-center errors <1e-8 and <1e-17 respectively, strict cyclic interval containment. Banach contraction for H² and S³ (return bounds 0.15 and 0.108) yields primitive extraneous cycles, and analyticity gives open COMPLEX basins. This is exact full-interval certification, not finite sampling of orbits.

## originality

PASS

Most relevant Basti–Cremaschi paper explicitly proposed THIS exact quartic and offered numerical evidence for Newton, Halley, and Schröder extraneous cycles; source candidly credits polynomial and Newton cycle. Accessible abstract describes rigorous Newton–Halley obstruction for a DIFFERENT quartic while the three-method example remained numerical. New claim is rigorous rational 64-part interval enclosure proving the two additional cycles on the same quartic, with full complex local basins; not claiming original polynomial, numerical discovery or minimal degree. Full October paper could not be obtained (arxiv/OA access failure and Oxford VPN disconnected), so any hidden rigorous Appendix A remains a source-specific residual priority risk rather than fabricated NOT_COVERING.

## value

PASS

Rigorous resolution of a concrete previously numerically suggested degree-four three-method failure example. Exact trapping intervals turn candidate cycles into attracting orbits with certified nonzero open basins for Newton, Halley and Chebyshev–Schröder on the identical quartic, a motivated question in root-finding complex dynamics distinct from numerical plotting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
