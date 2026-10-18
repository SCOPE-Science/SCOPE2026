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

The vertices are all nonempty proper subsets of [n], edges denote disjointness; degree 2^(n-|S|)-1 identifies singleton vertices. Singleton nonadjacency reconstructs every S, hence Aut(B_n)=S_n. Pointwise stabilizers of k chosen subsets act on [n] by coordinate permutations preserving each k-bit signature, so they are trivial exactly when the n signatures are pairwise distinct. The pigeonhole lower bound k>=ceil(log2 n) is attained because n>2^(k-1), so choosing n distinct k-bit words creates nonconstant and pairwise distinct subset rows. Injective word assignments number (2^k)!/(2^k-n)!, each unordered minimum family has k! row orderings. Thus exact count (2^k)!/((2^k-n)! k!); for n=5 k=3 gives 1120 and no pair determines. Independently reviewed finite exhaustive checker for 2<=n<=7 (counts 2,12,12,1120,3360,6720); no finite test substituted for the combinatorial arbitrary-n proof.

## originality

PASS

The numerical fixing number is known or claimed in earlier work for the same graph, and the n=5 two-vertex statement in the 2026 Boolean section is contradicted. The surviving contribution is classification of EVERY minimum set by distinct incidence columns, the exact multiplicity, and a proof correcting the n=5 statement. General symmetric-group bases use the same signature principle, but no located primary source supplies this exact graph-family enumeration; novelty is best-of-knowledge and limited by Ou et al inaccessible full text.

## value

PASS

Determining/fixing sets are a natural symmetry-breaking invariant of a canonical annihilating-ideal graph. The formula classifies all optimal landmark configurations, not just a known integer, and supplies a decisive small-rank obstruction to a published incorrect bound. The exact multiplicity can be used for optimal-set enumeration and random selection; meaningful despite elementary proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
