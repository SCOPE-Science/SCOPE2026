---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

In the projective generator model, a column is zero on U exactly when its vector lies in W=U-perp. If a=dim(W intersect V1) and b=dim(W intersect V2), the support formula is q^k-q^(k-r)-q^k1-q^k2+q^a+q^b. Grassmann dimension inequalities give a>=max(0,k1-r) and b>=max(0,k2-r), so the minimizers are exactly simultaneous equality cases. Fixing the two intersections A,B, the quotient W/(A direct-sum B) meets both coordinate summands trivially and hence is uniquely the graph of an isomorphism T:X->Y between c_r-dimensional subspaces. Counting A,B,X,Y,T gives the formula bijectively. An independent arithmetic recomputation reproduced the packaged sample multiplicities (21,42,42,21,1) over F_2 and (104,624,624,104,1) over F_3; the general proof is linear-algebraic rather than experimental.

## originality

PASS

Kwiatkowski introduces the SR-sum, studies its ordinary weight distribution, and advertises Griesmer-optimal simplex constructions; the publisher full text was access-restricted and no verified institutional PDF could be obtained in this run, so hidden same-family coverage is retained as an explicit risk rather than treated as negative evidence. Kurz--Landjev--Rousseva cover generalized Griesmer weight values in stronger generality, but not the number or structure of all minimizing subcodes. Resultary searches for SR-sum generalized-weight minimizer multiplicities did not return a covering published finding.

## value

PASS

Generalized Hamming weights are a standard code invariant, and the number and geometry of all minimizing subcodes is a natural refinement useful for understanding the newly introduced Griesmer-optimal SR-sum family. The result gives an all-q, all-r structural classification rather than a finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
