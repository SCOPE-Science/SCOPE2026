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

The inspected Margolis–Rhodes strict semigroup Lemma 3.3 represents each partial map by a matching in the domain, independent image and edge-to-image bijection. From f²=f every image point must be fixed, and since its domain matching edges are disjoint, the image of each edge must lie on that same edge; converse is immediate. For a path these objects are monomer–domino tilings, with each domino oriented L/R by its chosen endpoint. Independence forbids exactly adjacent R,L dominoes; all other pairs of chosen endpoints are separated. Conditioning on final monomer or domino gives I_n=I_(n-1)+2y I_(n-2)-y² I_(n-4) with I_0=I_1=1, I_2=1+2y, I_3=1+4y. Thus OGF 1/(1-x-2yx²+y²x⁴), whose direct multinomial expansion gives e_{n,k}=sum_j(-1)^j2^{k-2j}(n-k-j)!/[(n-2k)!(k-2j)!j!]. Independent tiling enumeration through n=12 matched coefficient recurrence and yielded P6 ranks 1,10,21,4. This all-n result is symbolic, not finite extrapolation.

## originality

PASS

The endpoint-collapse characterization is largely anticipated in the source Theorem 7.2 and not attributed independent priority. The newly quantified result is a natural all-path, rank-refined enumeration and rational generating function; primary full text computes entire St(P_n) order but does not give idempotent counts or this forbidden-orientation recurrence.

## value

PASS

Idempotents control regularity, local units and Green structure of transformation semigroups. For a natural canonical graph family, the theorem determines every idempotent rank, exact multiplicity, recurrence and generating function, unlike the previously published total-order count. The enumeration is compact and independently useful for semigroup structural and combinatorial comparisons. Its simple transfer-matrix technology does not make the new full family census a mere textbook substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
