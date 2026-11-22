---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For odd a>=3 the three positive generators a,b=a+2,c=a+4 are pairwise coprime; nonunit roots of 1/[(1-z^a)(1-z^b)(1-z^c)] are simple, so r_a(n) is a quadratic polynomial (n^2+3bn)/(2P)+constant plus P-periodic part, P=abc. Hence r(n+P)-r(n)=n+(P+3b)/2 and adjacent first difference increases by exactly 1 on each P-step, for ALL n>=0. Using b(x+y+z)+2(z-x)=n, the nonnegative branch decomposition gives exact T(E,L) sums at n=bK,bK+1; parity count formula T(E,L)=(m+1)(1+E/2)-Lm(m+1)/4-eta/2 yields base counts (8q^3+6q^2,8q^3+6q^2-q) for a=4q-1 and (32q^3+64q^2+35q+4,32q^3+64q^2+34q+4) for a=4q+1. All floor cutoffs m_i and parity contributions checked symbolically, including q=1 endpoints. At t=q-1 period shifts the difference is -1; summing the exact shift recovers both stated fifth-degree polynomial expressions R, with SymPy reducing their differences to 0 identically. Thus N in S_(R-1) but N+1 not, so S_p is not a terminal ray; any universal all-higher-p ray onset T(a) is >=R. The theorem does not assert existence or sharpness of T(a). Independent dynamic-programming representation counts for all 19 odd a=3..39 confirm both base and final pairs; this finite corroboration is not an infinite proof.

## originality

PASS

Best-of-knowledge noncoverage after separate searches in Resultary, published related records, and primary papers. Komatsu–Ying 2023 Theorem 1 covers p<=floor(a/2) for three-term arithmetic progressions; the claimed p=R_a-1 is quintic in a. The 2026 consecutive-odd paper studies generator sets {2k+1,2k+3,...,4k+1 or 4k+3}, not a three-element family for unbounded odd a. The 2024 symmetry theory defines p-complete symmetry but does not yield the explicit residue-class high-p drop. The related exact 17,18,19 threshold concerns mixed-parity consecutive integers, not all-odd step-two triples. An index hit for the exact same finding is the same underlying record and is not independent prior art. No stronger statement found which implies all odd-a values; unindexed equivalence and implicit derivation remain real residual risks.

## value

PASS

The canonical fixed-three-odd-denomination family is a natural unresolved higher-p regime in Komatsu–Ying 2023 §7. The exact adjacent downward witness at p=R_a-1 gives a nontrivial, parameter-uniform lower bound on any eventual complete-symmetry onset, R_a=a^5/32+O(a^4), and identifies separate mod-4 polynomial branches. This is a motivated structural boundary rather than a renamed period-shift lemma, isolated small enumeration, or routine corollary of low-p results. It does not settle the sharp threshold, eventual existence or entire exceptional p-spectrum, but those omissions do not erase the utility of the explicit infinite obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
