---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Encode the rim in R=F2[X]/(X^n+1), with hub coupling via J=(X^n+1)/(X+1). The specified open-neighborhood XOR map is (c,U,V)->(U(1), cJ+(1+X)V, (1+X^-1)U). CRT separates the (X+1)^e primary ring R0 from invertible R1, where e=2^v2(n). In R0, J=t^(e-1), and the local 2e+1-dimensional map has an invertible hub/U pair plus (1) nilpotent block for odd n; for e=2 ranks 3,1,0 imply blocks (3,1,1); for e>=4 the exact ranks T,T²,T^j imply (e,e,1). Thus periodic dimensions are 2n for odd and 2n−2e for even n. Zero-primary nilpotent kernels give E_n(j)=2^(p_n+Σmin(j,ell)). On R1 the square B²=((X+1)^2/X)I yields gcd kernel formulas for even and odd return times; odd n contributes 1 or 2 hub dimensions, even n none. Mobius inversion correctly counts primitive t-cycles. Independent GF2 adjacency/matrix-power ranks and polynomial gcds checked n=3..20 and t=1..12, 340 exact comparisons. These finite tests corroborate, not replace, the all-n CRT argument. Verified e=2 special case and n powers of two.

## originality

PASS

Autonomous XOR iteration on a simple gear/bipartite wheel/Jahangir graph is distinguished from controllable Lights Out switching and threshold-density binary automata. Generic finite CA ring polynomial methods can in principle compute Fitting blocks and fixed spaces, but no inspected prior exact (e,e,1)/(3,1,1) gear-specific Jordan and gcd census. Published Resultary complete multipartite or distance-two cube parity censuses operate on different graphs. Martin–Odlyzko–Wolfram provides important general algebraic CA prior but does not visibly state a gear result in accessed sections; Sutner full 1990 paper not read. Explicit best-of-knowledge with meaningful risks.

## value

PASS

Every parameter n in a natural labelled family exhibits an exact zero-primary Jordan classification including exceptional short-ring fusion (3,1,1), arithmetic collapse at powers of two, nontrivial periodic-state dimension and a complete primitive orbit census for every return time. These classify the dynamics beyond generic finite-matrix algorithms and are reusable structural invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
