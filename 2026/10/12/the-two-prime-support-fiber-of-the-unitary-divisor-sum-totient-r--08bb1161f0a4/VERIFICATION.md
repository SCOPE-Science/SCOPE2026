---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

PASS: For n=∏p^a, the local ratio R_p(a)=(1+p^a)/(p^{a-1}(p-1))=p/(p-1)(1+p^(−a)) decreases in a, and R_2(a)>2 excludes all even n; n=1 fails. A one-odd-prime equation p^{a-1}(p−2)=1 forces n=3. For 3<=p<q with p>=5, maximum (p+1)/(p−1)*(q+1)/(q−1)<= (6/4)(8/6)=2 with equality only 5*7. For p=3,q>=11, R_3(a)R_q(b)<=R_3(2)R_11(1)=2 with equality only 3²*11=99, given a>=2 since a=1 factor already 2. For q=7, b=1 gives >2, b>=2 gives <=125/63<2; for q=5, b=1 >2, b>=2 leads 3^a≡−1 mod5 so a≡2 mod4, with a=2 >2 and a>=6 <=949/486<2. This exhausts all supports<=2; direct n=1045=5*11*19 has σ*=1440=2φ. Independent exact integer factoring through 50,000 found precisely 3,35,99 at support<=2 and 1045 first support3. Finite checks supplement the all-exponent congruence/inequalities.

## originality

PASS

PASS best-of-knowledge: Broughan–Delbourgo's Theorem 11 (2013) classifies ordinary σ(n)=2φ(n) through three supports (3,35,1045), but its distinct function misses nonsquarefree n=99 for which σ*(99)=120=2φ(99) but σ(99)=156. Trudgian (arXiv:1312.4615) proves unitary-sum growth/comparison, not exact φ ratio. OEIS A034448 is unitary-sum value sequence, A062699 ordinary ratio, not this all-exponent classification. Resultary two-prime unitary findings address iterated σ* or unitary-versus-exponential equations, not σ*/φ=2. Search does not establish absolute novelty; unindexed elementary duplicates remain a risk.

## value

PASS

PASS: Multiplier-two divisor-sum/totient fibers are naturally studied in an established integer-sequence/classification program. The unitary analogue changes the answer at first nonsquarefree layer (99), and a complete support<=2 classification with a global parity obstruction and explicit sharp three-support boundary 1045 is a precise usable cutoff, not a recomputation of an ordinary known table. It does not claim an exhaustive higher-support census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
