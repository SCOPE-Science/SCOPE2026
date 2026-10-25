---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The independently checked six-spin swap-energy identity ΔH/J=(c-d)[(1-r)(b-e)+r(a-f)] gives only r=1/2 and r=1 sign boundaries; the 32-state shift transfer construction is a bijection with length-n cyclic spin words, B_n(r)=tr(T_r^n). Independent exact 16x16 reversal-even block characteristic polynomials reproduce p0=x^6-x^5-x^4-x^2+1, p-=x^5-x^4-x^2-x-1, p*=x^9-2x^8+x^7-x^6-x^4+x^3-x+1, p+=x^9-2x^8+x^7-x^6+x+1. Source proves unique primitive dominant component and Perron growth; strict numerical root separation has exact root-isolation witnesses in package. Independent Hamiltonian recomputation for every spin word n=6..9 at all five regime representatives exactly matches the transfer/local condition and counts; n=6/8 respectively (32,70),(34,72),(34,68),(46,100),(34,84). Difference of full block eigenvalue multisets at r=1/2 is (+1,-1) replacing zero eigenvalues, hence B_n(1/2)-B_n(1/4)=1+(-1)^n for all n>=6. The uniform infinity claims rely on shift-matrix and PF arguments, NOT the bounded checks.

## originality

PASS

Best of knowledge after inspection of specified pinned source and actual primary literature. The same energy difference and r=1/2,1 thresholds are credited; quantification over sequences of neutral swaps is strictly stronger than checking individual swaps. The different equal-coupling rates (~1.4655 published kinetic vs 1.80239 immediate) make the possible conflation concrete; full original paper inaccessible this execution is a residual comparison risk. No theorem found in inspected material makes the stated four roots or parity correction a direct corollary; same Hamiltonian and transition ratios alone do not imply the distinct all-magnetization weak-blocked combinatorics.

## value

PASS

Counting one-step weakly blocked spin configurations, as opposed to kinetic metastable traps allowing neutral paths, is a natural thermodynamic invariant. The all-coupling exact entropy spectrum and isolated equal-coupling spike, plus a separate nonextensive parity correction at half-coupling, reveal different structural mechanisms rather than a renamed prior kinetic count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
