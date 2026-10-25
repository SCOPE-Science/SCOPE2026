---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For p≥5 and all n≥0, count R_(p,n)(a) for x³+y³=a mod p^n. Mod p, nonsingular roots at all (x,y)≠(0,0); unit fibres lift with p^(n−1), divisible target nonsingular fibres contribute c_p p^n (c_p=gcd(3,p−1)(p−1)/p). Singular branch with x,y divisible by p exists only if p³|a and contributes p^4 R_(p,n−3)(a/p³), accounting for redundant last digits. Cubic character convolution gives sum of squares S_p, including |Jacobi(χ,χ)|²=p; averaging squared recurrences yields M_n−L_p=p^(−1)(M_(n−3)−L_p), with explicit initial M0/M1/M2 and L_p=1+gamma_p/p+1/p² (gamma=7 or1 mod3). Iterating valuation shells produces F_p(T)=c_p(p^k−1)/(p−1)+p^k B(U), Haar shell mass ≍p^(−3k), and sharp L^s iff 0<s<3. Independent complete convolution of residues for ten tested (p,n) pairs corroborated all exact rational formulas, not a proof for unbounded n,p.

## originality

PASS

The finite-field limiting numeric constant L_p is already available from Fermat cubic surface point counts (Massarenti 2026 Corollary 8.3) and is not claimed alone novel. Brüdern–Vaughan 2021 analyzes asymptotic variance of positive two-cube representations over progressions and uses modular counts, but does not in inspected relevant primary text give every finite p-power collision moment and Haar fibre law. The new joint all-prime finite-level closed formula plus exact limiting target densities and endpoint L^3 divergence remains a distinct assertion; Igusa local zeta/Poincare machinery may imply portions or all indirectly, priority residual.

## value

PASS

The natural map (x,y)↦x³+y³ over Z/p^n has exact collision energy and local fibre densities; the exact modulus-depth correction and sharp integrability threshold quantify concentration at the isolated cubic singularity. These are natural arithmetic invariants useful independently of global positive integer sums, not a known-table recomputation or a one-prime finite curiosity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
