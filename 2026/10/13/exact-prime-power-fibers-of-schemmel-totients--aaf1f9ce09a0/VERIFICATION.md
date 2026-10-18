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

Multiplicativity of S_r and its prime-power rule S_r(p^a)=p^(a-1)(p-r) for p>r force every factor in any preimage of ell^t to be a power of ell. Each p≠ell can occur only once, and then p=r+ell^j, with j>=0; the j=0 case is the optional unit factor r+1. A repeated p=ell is possible only if ell-r is a positive ell-power less than ell, hence ell=r+1 prime, and its contribution is 1 for a=1 and ell^(a-1) for a>=2. Therefore the exact generating factor is (1+1_{r+1 prime})∏_{j>=1,r+ell^j prime}(1+x^j) for ell≠r+1, or (2+x+x²+...)∏... when ell=r+1; extracting x^t gives all preimages with no hidden repeats. The prime-target t=1 cases, exceptional ell=r+1 case, classical phi fibers, parity of r and equivalence with fixed-gap prime pairs for even r all follow. No claim of proving infinitude of prime pairs. Independent exact factorization enumeration supports 648 (r,ell,t) finite-window comparisons but the factor argument proves the general formula.

## originality

PASS

The exact inverse fiber N_r(m) is a classical object from Subbarao–Yip. Full primary text of the 1989 article has a special r=2, t=1 zero-fiber observation: if odd p+2 is composite then S_2(x)=p has no preimage. The classical Euler phi power-of-two case is also known; those pieces are prior. The present result determines complementary exact multiplicities, every order r, all exponents t and the full subset-sum coefficient with exceptional source prime ell=r+1, which do not follow from the specifically inspected archival statements. A 1989 Yip doctoral thesis is topically very close and could contain implicit prime-power formulas; complete thesis was unavailable, so PASS is explicitly best-of-knowledge and does not claim comprehensive historical priority.

## value

PASS

Inverse multiplicities N_r(m) are central objects in the Schemmel analogues of Carmichael and Sierpiński problems. Prime powers form the first natural multiplicatively atomic target class; a complete all-r, all-ell,t fiber formula is useful without tackling arbitrary targets. The explicit generating polynomial gives counts and actual preimages, explains the exceptional ell=r+1 factor, recovers Euler examples and sharpens an archival obstruction to exact multiplicity. The fixed-gap prime-pair equivalence for even orders connects the image question to a standard open family without claiming resolution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
