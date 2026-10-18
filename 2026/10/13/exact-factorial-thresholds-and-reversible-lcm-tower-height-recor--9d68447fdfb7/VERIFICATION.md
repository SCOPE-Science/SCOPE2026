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

PASS. The least integer with h(m)≥k is E_k (E_1=2, E_{k+1}=2^{E_k}) by induction on the largest prime-power exponent. For factorials ν_p(N!)≤ν₂(N!); Legendre gives ν₂((E_{k−1}+1)!)=E_{k−1}−1 and ν₂((E_{k−1}+2)!)=E_{k−1} for k≥3, hence first hits F_k=E_{k−1}+2, F_1=2,F_2=4. For initial LCM, ν_p L(N)=floor(log_p N) gives first hits G_k=E_k and entire [E_k,2E_k) constant plateau. At 2E_k the 2-adic exponent is E_{k−1}+1, whose recursive height is too small; all odd-prime exponents <E_{k−1}. Exact lower bound at drop follows from prime p with ν_p L(2E_k)=a=E_{k−2}, by explicit p=5 for k3 and p=11 for k4, and Bertrand in (N^(1/(a+1)),N^(1/a)) for k≥5. The proof handles all k without enumerating impossible huge tower indices. Independently calculated factorial and LCM heights at all reachable first-hit and double endpoints through k4, and factorial k5=65538; computations corroborate, not replace the induction.

## originality

PASS

PASS, best of knowledge for the exact first-hit laws on factorials/LCMs AND unbounded disappearing LCM plateaux. De Koninck–Verreault 2023/2024 define this exact max-over-exponents height and establish general minimal E_k, which is credited. Their primary paper covers distribution, means and runs rather than this special-sequence record structure. Their separate work on arithmetic functions of factorials studies other functions. OEIS A288636 uses a different gcd-based recursive height, so coinciding minimal E_k data do not settle these max-height laws.

## value

PASS

PASS. Factorials and initial least common multiples are canonical multiplicative sequences exhibiting contrasting valuations. The nonmonotone height theorem gives exact all-level thresholds and arbitrarily long record intervals that vanish immediately at 2E_k, a mathematically motivated surprising phenomenon requiring a genuine prime-gap witness, rather than low-level numerical examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
