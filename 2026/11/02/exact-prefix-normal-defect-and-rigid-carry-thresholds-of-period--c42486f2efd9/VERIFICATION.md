---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The period-doubling fixed point μ(0)=01, μ(1)=00 has p_j=1 iff ν2(j+1) is odd, so prefix weight H(n)=Σ_{r>=1}(-1)^(r-1) floor(n/2^r). For factor [a,a+ℓ) its excess H(a+ℓ)-H(a)-H(ℓ) is the alternating sum of binary carries γ_{2i-1}-γ_{2i} for a+ℓ. A positive term γ_{2i-1}-γ_{2i}=1 requires x_{2i-1}=1 for x=a+ℓ, hence excess <= number Q(x) of set odd-position binary digits. The least x with Q(x)>=t is 2(4^t-1)/3; the half x/2=(4^t-1)/3 doubled gives exactly t alternating carry pairs and attains it. Equality at this minimal x forces a=ℓ=(4^t-1)/3 by the binary carry transition constraints, yielding uniqueness. Thus Δ(N)=floor(log_4(3N/2+1)), with dyadic boundary from threshold inequalities. Independent exhaustive factor-endpoint calculations over all initial prefixes through N=1400, including unique witnesses at 2,10,42,170,682, agreed. The all-N result is a symbolic carry proof, not an extrapolation.

## originality

PASS

Fici–Lipták's prefix-normal theory gives the maximum-one-factor function, prefix-normal forms and general equivalence notions, not the exact fixed period-doubling prefix defect or first locations. The published Resultary ordinary paperfolding deficit concerns a different 2-automatic word; the Resultary period-doubling string attractor concerns a different invariant. A general 2-regular Abelian-complexity theorem describes factor frequency classes in the infinite language, not exact initial-prefix endpoint optimization. No actual prior implication identifying the 4-adic threshold was found; specialized automatic-word papers remain possible.

## value

PASS

For a canonical automatic infinite word, the all-prefix maximum violation of prefix normality is a natural jumbled-index invariant. The exact logarithmic defect, sharp thresholds and unique carry witnesses quantify a structured divergence from prefix-normal behavior rather than a routine reformulation. Its bounds distinguish finite prefixes from the full infinite language.

The dated certificate retains the supplied scientific assessment, sources and limitations.
