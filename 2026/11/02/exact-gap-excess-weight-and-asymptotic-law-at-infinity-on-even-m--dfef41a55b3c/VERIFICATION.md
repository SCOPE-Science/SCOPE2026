---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The factors A0 and B0 have q and b=q(q-1) disjoint simple roots, respectively; B0 has nonzero derivative at a root because A0 is then nonzero. With N=br+q+1 and r=1 mod q+1, both r and the degree N-1 of the Kummer right-hand side are coprime to N. The extension is tame and infinity and all q+b finite roots are totally ramified, yielding genus (q^2-1)(N-1)/2. The functions z^j/B0^floor(jr/N) have no finite poles, with pole orders w_j=qj+b(jr mod N) at infinity. They cover all residues modulo N and generate a union with exactly the geometric genus many missing orders, proving completeness. Summing each gap progression gives the two Apéry moments plus the stated constant. The cross moment is the Dedekind sum for r,N; using N=br+q+1 and r=1 mod q+1 in reciprocity gives 12s=b(q+2)/(q+1)-b(r^2+1)/((q+1)N). Substituting r=(d-q)/b and removing g(g+1)/2 produces the stated polynomial; independent symbolic reduction also gave zero residual. Its B and C coefficients are positive for q>=3, proving strict decrease and both limits. The blockwise maximum of w_j is achieved at s=q+1 because b ceil(r/(q+1))<d, giving the stated conductor. Exact residue-by-residue replay gave (g, conductor, W)=(324,594,12906) at (3,4) and (1920,3648,449280) at (4,4), with no execution of supplied code.

## originality

PASS

The complete semigroup, exact Apéry representatives, conductor and genus have direct prior coverage, including a matching indexed result for the same curve. Only the evaluated gap-excess polynomial and the strict normalized law survive as the distinct claim. They require evaluating a correlated Apéry second moment using two-step reciprocity; a general gap algorithm or a matching genus/conductor does not supply this evaluation or monotonicity. No inspected primary source or indexed record gives that polynomial or normalized law.

## value

PASS

For a naturally occurring maximal-curve family, the gap excess measures how far the entire infinity gap sequence departs from the ordinary gap sequence, rather than measuring just its length or endpoint. A quadratic expression uniform in q^n makes quantitative comparison possible without enumerating a growing gap set. It gives the strict finite-parameter trend, positive limiting proportion and large-q behavior; the two-step rotation moment explains these features structurally. The contribution is this evaluated invariant, not a new semigroup algorithm or a generic ramification theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
