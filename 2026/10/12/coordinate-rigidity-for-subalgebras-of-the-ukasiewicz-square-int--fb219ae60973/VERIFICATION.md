---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

On every nonempty concrete subalgebra of ([0,1], max, 1-x, max(0,2x-1)), the term *(neg(x∨neg x)) equals zero and forces preservation of 0 and 1. Define lambda=neg*neg and sigma=*: their scalar actions are clipping 2x and 2x-1. Iterating yields unary term ramps R_{k,j}(x)=[2^k x-j]_0^1 for all k>=0,0<=j<2^k. If a<j/2^k then R(a)=0 forces h(a)<=j/2^k; if (j+1)/2^k<a then R(a)=1 forces h(a)>=(j+1)/2^k. Density of dyadic cuts gives h(a)=a without continuity, injectivity, or finiteness assumptions. All maps therefore are inclusions, and S_n⊆S_m iff n divides m; singleton/endpoint cases are explicitly covered.

## originality

PASS

The Coniglio--Esteva--Flaminio--Godo full paper gives detailed finite representability, skeleton structure, and componentwise embeddings (notably Proposition 5.9 and Theorem 5.16). That work is relevant and accounts for finite representable embeddings but it does not state a complete hom-set classification for *arbitrary*, including uncountable, concrete subalgebras, nor rule out all noninjective reduct-homomorphisms through dyadic term cuts. Full MV signature rigidity cannot simply be applied because this reduct is not always term-equivalent to MV-chains. Searches found no earlier equivalent full-category theorem; acknowledge potential implicit consequences of prior finite skeleton construction.

## value

PASS

This resolves a natural semantic morphism problem: whether the square-and-join reduct admits genuinely new homomorphisms despite losing MV operations. The answer gives an exact inclusion-poset category and rigidity for arbitrary subalgebras, including infinite and non-finitely generated ones, with explicit term separation. It is a complete structural statement and not a finite-grid count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
