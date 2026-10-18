---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The exact statistic is the ordinary least absent part, counted only when odd, with overlined and ordinary copies both counted for forced sizes. Terms of mex 2j+1 have factor 4^j, so j>=2 vanish mod 8 and j=1 contributes 4q^3/((1-q)(1-q^2)); the j=0 term is (1-q)/(1+q) times the inverse Jacobi theta series. Expand the inverse as 1-2Theta+4Theta^2 and apply Frobenius modulo 2 to obtain the displayed coefficient law. At n=m^2 the two 2-terms cancel and the remaining bracket m-1+floor((m^2-1)/2) is even in either parity. All non-squares have residue 2 or 6; interval-by-interval mod4 balance, with O(sqrt X) exceptional twice-squares, proves density 1/2 each. Independent coefficient DP from forced/unrestricted part sizes mod8 agreed for n=1..100, with zeros exactly the ten squares <=100. Not inferred from the finite test.

## originality

PASS

The initiating same-statistic September 2026 preprint proves an exact generating series and a square test mod4, and its modulo-eight result concerns self-convolution, not direct a(n) coefficient classes. The direct all-n mod8 formula, exact square divisibility by 8, and residue densities provide a nontrivial additional arithmetic consequence rather than an independent generating function. Published-finding similarity searches did not reveal same-statistic coverage; ambiguity in unindexed related 2026 work remains.

## value

PASS

A complete next 2-adic layer for the precise odd-mex overpartition sum closes the natural sharp boundary left by a mod4 square criterion. The exact coefficient law determines the three residue classes and their densities for every index, a reusable arithmetic statement beyond merely computing an existing generating function.

The dated certificate retains the supplied scientific assessment, sources and limitations.
