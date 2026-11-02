---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For a three-term walk beginning at L_x≥3 (x≥2), write jumps k,ell and ratios u=L_{x+k}/L_x, v=L_{x+k+ell}/L_{x+k}. One-digit bounds give L_x/(L_x+1)<v/u<1+1/L_{x+k}; hence 3/4<v/u<4/3. The Lucas addition formula L_{m+j}/L_m=F_{j+1}+F_j L_{m-1}/L_m and the invariant predecessor intervals [1/3,3/4], [4/7,3/4] show ell>k would force v/u>4/3, using the exact positive difference (5/7)F_{k+1}; ell<k would force v/u≤3/4 by Fibonacci recurrence. Thus ell=k. The product identity L_{r+s}=L_r L_s−(−1)^sL_{r-s} gives d_2=(L_k−b)L_{x+k}−(−1)^k L_x. For odd k a nonzero L_k−b violates 0≤d_2<b; even k gives d_2<0 or d_2>b. Therefore k odd, b=L_k and d_2=L_x<b, forcing x<k. The first digit is d_1=−(−1)^xL_{k−x}; positivity forces odd x≥3, with digits L_{k−x},L_x, and conversely these all work. A four-value walk with second value c≥3 contradicts the necessary c<b for its last triple, whereas the first transition forces c≥b. With c=2, the sole candidate 1→2→4 in base 2 has no Lucas successor 8 or 9. Odd k≥3 produces 1→L_k→L_{2k} in base L_k since L_{2k}=L_k²+2, proving infinitely many sharp bases. Exact independently written integer search checks 1999 bases on 220 Lucas values: 8064 edges, 51 triples, 21 triples starting ≥3, no quadruple; 5382 addition and 4094 Lucas product identities and 1176 odd-family test pairs. These are finite corroborations only; the quantified conclusion rests on proof reconstruction.

## originality

PASS

Best-of-knowledge originality for the universal, sharp three-value bound and complete odd-index triple classification of classical second-kind Lucas values V_n(1,-1). The initiating Fibonacci theorems concern F=U(1,-1) in decimal and the later all-base theorem formally treats U(P,Q), not companion V(P,Q), with an O(log b) rather than base-independent sharp constant. The full accessible 2025 arXiv text and the 2022 primary PDF were compared statement by statement. Three Resultary semantic searches returned unrelated Lucas-arithmetic and digit-combinatorics findings, including Pell-Lucas vertex-law id 2026/10/11/402774cb80ae; none covers right-appending V walks. OEIS A000032 lists values but no unbounded-base structural classification. Remaining priority risk is an older all-base companion-digit result under a different alias or a more recent published revision.

## value

PASS

The classical companion Lucas sequence V(1,-1) is a canonical recurrence directly motivated by published Fibonacci digit-walk research. A sharp universal three-value maximum independent of arbitrarily large b, infinitely many equality bases, and a necessary-and-sufficient parametrization of every non-small triple determine a natural extremal invariant rather than a mere base-ten recomputation. The odd parity, equal-gap and L_k base rigidity illuminate the mechanism and contrast the Fibonacci behavior. This is mathematically nontrivial and independently useful despite its deliberately limited single-digit and companion-recurrence scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
