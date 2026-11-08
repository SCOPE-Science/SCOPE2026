---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For the exact rectangular torus T=∏(R/a_i Z) with quotient l_infinity metric, independent Haar-uniform points induce independent U_i uniform on [0,c_i=a_i/2] in each shortest circular coordinate. D has the law max_i U_i, so F(t)=∏_i min(t/c_i,1). The small-t log-log slope recovers d; jumps of tF'/F at the thresholds recover every c_i and multiplicity, including the terminal jump. This is an injective metric-parameter reconstruction only within rectangular max-Finsler tori, not Euclidean quotient tori. On (0,b=max_i c_i), m(t)=tF'/F lies in {1,...,d}; F(t)/t^d is nonincreasing and F(t)/t is nondecreasing. Inverse quantile Q therefore has Q(u)/u^(1/d) nondecreasing and Q(u)/u nonincreasing. For p>q>0 interpolate positive increasing quantile functions A to B with B/A monotone via Z_t=A^(1−t) B^t. Derivative of log(E Z_t^p/(E Z_t^q)^(p/q)) is p times the difference of log(B/A) expectations under p- and q-size biased measures; monotone likelihood ratio makes it of the appropriate strict sign. This gives exact bounds [d/(d+p)]/[d/(d+q)]^(p/q) <= ratio < [1/(1+p)]/[1/(1+q)]^(p/q), lower equality precisely when all side lengths agree; degenerate lengths approaching zero give sharp unattained upper value. The p=2,q=1 bound becomes 1+1/[d(d+2)] <= E[D²]/(ED)² < 4/3. The pinned verify.py's exact piecewise CDF integration is consistent with this derivation; independent rational calculation of 205 sorted length profiles across d=2..6 confirmed samples. Neither finite checks nor citation to star ordering replaces the full quantile proof.

## originality

PASS

The inverse distribution formula and inequalities are phrased here as exact invariants of max-Finsler rectangular tori, not new general principles of star or dispersive order. Kochar–Torrado 2015 compare maxima of scale families via likelihood-ratio/reversed-hazard/majorization, rather than explicitly identifying this two-sided all-real-exponents optimum for max-of-uniforms or the length reconstruction. Generic star-order principles are acknowledged and might imply the moment inequalities as a corollary once the particular quantile-ratio sandwich is established. A materially relevant stronger general majorization theorem remains an originality risk, especially because corollary coverage counts even if its parameters differ. The full-law inverse rigidity remains a distinct exact geometric claim.

## value

PASS

The random-distance distribution is a natural inverse geometric observable. Within this explicit rectangular max-norm torus family it determines dimension and every circle length, unlike a finite low-order moment; sharp normalized dispersion envelopes for every p>q quantify the exact extremal isotropy-versus-collapse behavior. This is a self-contained complete inverse classification and sharp all-exponent bound with uniquely characterized extremizers, not merely a recomputed random-sampling table. Its restricted norm and product metric are essential and clearly stated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
