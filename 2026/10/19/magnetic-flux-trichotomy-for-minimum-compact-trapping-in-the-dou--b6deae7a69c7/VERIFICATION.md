---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

At λ=±t, projecting the dimer equation onto its λ eigenspace gives T*h orthogonal to this eigenspace. The orthogonal part of z is T*h/(2λ); TT*=4t²I then makes the hub inner-product equation λ||h||²=2λ||h||², forcing h=0. Equivalently the projected equation relates adjacent hubs by a nonzero phase, so one zero vertex propagates to all hubs for a finitely supported state. Each occupied edge then contributes exactly its two dimer sites, and the residual condition is precisely the signed magnetic incidence equation. Its nonzero support has no degree-one vertex. A graph with minimum degree two and at most six edges is a single cycle: two distinct square cycles can share at most one edge, and a distinct cycle cannot be contained in a simple six-cycle. No even cycles shorter than four exist, and four- and six-cycles enclose one and two squares respectively. They are admissible exactly at the stated holonomies. In the seven-edge witness at the displayed origin the hub equations reduce, among others, to b-a+f=0, d-c-ωf=0, and -d-ω²g=0; the other three are a+e=0, g-b=0, and c-e=0. The supplied coefficients solve all six, with only f dropping out at ω=-1. The zero-flux square solves its four equations. Tail checkerboard parity gives the other energy, preserving every occupied site, and the energy difference is 2t in the stated time convention. No rational-flux assumption enters. I inspected the frozen nested verification/lieb5_flux_checker.py, which constructs the open matrix and checks numerical null vectors at five fluxes and both signs, plus finite candidate-edge enumeration. It was not run and does not certify infinite-lattice minimality or the printed symbolic witness; those follow from the analytic checks.

## originality

PASS

The distinct supported claim is the all-flux exact physical-site minimum at the two nonzero energies of the twice-subdivided Hamiltonian, using the reduction that excludes original-vertex amplitudes and identifies the full compact eigenspaces at those energies. The 4/6/7 ground-graph circuit answer, the zero-flux eight-site mode, and two-band beating at zero flux are not novel. The strongest indexed result has exactly the same reduced incidence kernel but is a one-midpoint Hamiltonian at zero eigenvalue; it supplies the complete incidence minimum once the additional nonzero-energy dimer reduction is proved, not the target physical minimum or that reduction by itself.

## value

PASS

The physically occupied-site cutoff matters for how many sites a localized input must address at either of the two flat-band energies of a single standard decorated lattice. The result proves sharp impossibility as well as constructions, including irrational flux: an arbitrarily small nonzero flux removes eight-site confinement, whereas the half-flux case allows twelve sites instead of the generic fourteen. Exact support transfer to both energy sectors also preserves the possibility of two-band beating within the same support. The value lies in the physical eigenspace and resource threshold, not in recounting the already covered incidence circuits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
