---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Independently reconstructed the proof for every odd prime p and nonzero g in Q_{>=0}^{F_p}. For each lag a, the rational nonnegative overlap c_x=g_x g_{x-a} satisfies a cyclotomic rigidity lemma: at b≠0, sum_x c_x ζ^{bx}=0 iff all p coefficients equal; at b=0 positivity forces every coefficient zero. For proper S, at least one overlap coefficient is zero for every a, so a whole modulation row vanishes iff S∩(S+a)=empty, exactly a∉D=S−S. For full S, zero at b≠0 forces g_x g_{x-a} constant. If a=0, positivity makes g constant; if a≠0, subtracting adjacent product equations yields g_x=g_{x−2a}, and 2a generates F_p because p odd, so again g constant. General Weyl conjugation/Fourier orthogonality gives singulars √p|A_g(a,b)| for UNNORMALIZED g and exact kernel in W_{a,b}=M_bT_a basis. Thus rank=p|D| proper, and rank=p if full constant / p² full nonconstant. When a∉D, e_0+e_a and e_0+i e_a give different pure states with same intensities; for full constant g, e_0 vs e_1 do so. Full rank implies all-signal phase retrieval, so the equivalence is exact. Cauchy–Davenport supplies p min(p,2|S|−1), attained by arithmetic progressions; the p11 set {0,1,2,5} has D=F11 with unequal differences. Rebuilt p²×p² lifting independently of the source verifier and compared exact-rank predictions and √p spectrum on 67 windows over p=3,5,7,11; max absolute singular-error under 10^{-12}. This finite check corroborates rather than proves the uniform statement. Scope does not extend to arbitrary positive reals, even p=2, non-prime groups, or uniform stability.

## originality

PASS

Best-of-knowledge qualified PASS for the full arithmetic classification of arbitrary nonnegative rational windows over all odd primes, NOT for general Weyl eigenvalue identities, cyclotomic irreducibility, Cauchy–Davenport, or the existence of Gabor phase-retrieving probes. Goldberger–Kang–Okoudjou Theorems 1–2 already exactly give the general rank/ambiguity criterion and Gram spectrum, while Bojarovska–Flinth provide nonvanishing sufficiency, difference-set indicators, and missing-band obstructions. Full-text inspections of these primary sources, recent Li, finite Abelian operator calculus, and three published related rank classifications did not reveal the full all-weights rank-by-difference-cover and full-positive-support dichotomy. The increment is a short classical-lemma specialization of the known general mechanism and could have an unindexed equivalent; explicitly qualified, not a historical priority certificate.

## value

PASS

A natural and practically motivated observable is the exact complex linear span/rank and kernel of the full p² cyclic Gabor intensity lifting; for a large arithmetic family this becomes a combinatorial invariant D=S−S independent of any positive rational weight choices. The theorem classifies exactly which support sets give all-signal retrieval, distinguishes full-support constant windows, provides every missing Weyl direction and a sharp support-size deficiency, and yields difference-cover (nonuniform-multiplicity) examples not limited to classical difference sets. A researcher designing exact-arithmetic p-dimensional tomography windows could need these exact facts; no unjustified stability or recovery-speed claim is made. Value derives from complete natural family/boundary classification, not from numerical verification or rebranding the previously known spectral theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
