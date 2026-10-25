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

The actual RESULT.md uses all odd fields and separates characteristic five. For p≠2,5, substitution u=s/2+x,v=s/2−x gives the exact quintic sum s^5/16+(5s³/2)x²+5s x⁴. At each nonzero s, equality of sums is equivalent to (x²−y²)(x²+y²+s²/2)=0, so the collision sum is (2q−1)+(q−χ(−1))−2(1+χ(−1))=3(q−1−χ(−1)). For this even quartic, positive representation levels are ≤4; only x=0 can produce odd level, equal to 2+χ(−2). Mass q and the exact collision second moment uniquely solve k2=(q+3ε)/4 and k4=(q−4−3ε−2η)/8 with k1=(1−η)/2, k3=(1+η)/2. The s=0 fiber has q representations of w=0; in characteristic5 Frobenius makes graph an additive subgroup with q outputs each of multiplicity q. Summing supports/squares proves exact size and energy. Character orthogonality with q^(-1) input normalization and counting measure F_q² yields fourth moment E/q². All claims hold for arbitrary odd prime powers, not only enumerated small fields. An independently written exact symbolic checker reconstructs binomial factorization; independent field arithmetic enumerates fifteen prime/prime-power cases (3,5,7,9,11,13,17,19,23,25,27,29,31,49,125), including q=11 and 31 outside the 2017 permutation regime. Finite checks corroborate but cannot establish the all-field theorem.

## originality

PASS

PASS is qualified and attaches ONLY to the strictly stronger all-odd-field statement, particularly the natural nonpermutation regime q ≡ 1 (mod 5) in characteristics other than 3 and 5; it does not credit the many previously known cases. The essential alias is differential spectrum: for the odd monomial f(t)=t^5, setting u=x+a and v=-x gives r(a,b)=#{x:f(x+a)-f(x)=b}. Panario–Santana–Wang (2017) already tabulate the EXACT same fifth-power differential spectrum for q not congruent to 1 mod 5, including its q mod 8 splits and char-five subgroup branch, not merely related estimates. Choi–Hong–No–Chung (2013) calculate the complete spectrum of x^((p^k+1)/2), including x^5 when p=3,k=2, for any characteristic-three field. Thus the classical alias and extensive coverage are decisive limitations; neither inspected source claims the infinite nonpermutation cases such as q=11,31,41. Li–Xiong (2024) give the slope-averaged intersection distribution of all quartic polynomials but explicitly distinguish the finer fixed-slope multiplicity distributions and pose their full classification as Open Problem 4. Their theorem is not an implication of this exact b=0 slice. The previously known energy-moment equivalence by Fourier orthogonality is not independently new. No compared source establishes the full nonpermutation fifth-power spectrum, so the all-q extension survives best-of-knowledge with explicit historical-priority risk.

## value

PASS

The differential spectrum of the fifth-power map is a canonical invariant in finite-field cryptography and is exactly the ordered two-sum spectrum of its odd monomial graph. The older full permutation-polynomial census purposely excludes q≡1 mod5, whereas the submitted proof fills that natural infinite nonpermutation family (q=11,31,41, etc.) with a complete 0–4 fiber distribution and explicit arithmetic χ(−1), χ(−2) split. A future researcher analyzing differential uniformity, additive doubling or Fourier energy for this natural monomial can use the exact missing distribution, not only its energy. Li–Xiong 2024 confirms fine fixed-slope quartic multiplicity data are a natural, nontrivial refinement over the general slope-averaged results. The characteristic-five and permutation regimes, basic fourth-moment identity and standard circle-count lemma are previously known/routine ingredients and are not separately used to justify value. The work does not address unrestricted weighted fourth-moment extremizers or characteristic two.

The dated certificate retains the supplied scientific assessment, sources and limitations.
