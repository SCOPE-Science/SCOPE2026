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

For binary words with exactly r>=1 ones and m>=0 zeros, the gap representation 0^{g1}1...0^{gr}1 bijects quasinecklaces with nonnegative r-compositions with first coordinate maximum. Burnside enumerates necklaces by cyclic gap orbits. Verified Q_r(m)=sum_h [x^{m-h}](1+...+x^h)^{r-1}; N_r(m)=sum_{d|gcd(r,m)}phi(d)binom(m/d+r/d-1,r/d-1)/r; r=1,2 equal; r=3 excess floor(m/2)-floor(m/3). For FIXED r>=3, count ties of exactly two maximum gaps, inclusion-exclusion and beta integral yield (Q-N)~m^{r-2}/(2r(r-2)!) with O_r(m^{r-3}) error; nonidentity periodic tuples contribute only O_r(m^{r-3}); hence Q/N=1+(r-1)/(2m)+O_r(m^-2). Independent integer enumeration of gap vectors and necklace orbits for 1<=r<=6, 0<=m<=12 matched both exact formulas, and inspected source verifier check_quasinecklace.py. Finite samples are not the asymptotic proof; periodic and zero-zero gap edge cases were checked.

## originality

PASS

Best-of-knowledge PASS: new fixed-CONTENT binary coefficient/excess and sharp first-order candidate overhead beyond the prior unconstrained constant-factor bound. The generating construction and quasinecklace definition are prior art; no independence of sources or blanket priority is claimed.

## value

PASS

The fixed-weight output-sensitive overhead of a natural necklace-generation candidate class is an intrinsic, parameterized enumeration; the explicit first correction quantifies asymptotically wasted candidates, and exact smallest weight excess locates genuine loss of uniqueness. Nontrivial tie-pattern analysis is needed beyond generic necklace Burnside counting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
