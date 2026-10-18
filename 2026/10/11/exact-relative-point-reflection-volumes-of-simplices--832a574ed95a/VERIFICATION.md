---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Normalize affinely to Δ=conv(0,e1,...,en) with Euclidean vol 1/n!, and M=(Δ-Δ)/2. Rogers--Shephard point reflection maximizes vol(conv(Δ∪(2x−Δ))) at a vertex with value 2^n/n!, and difference-body equality gives vol(M)=C(2n,n)/(2^n n!). Hence Busemann factor v_n/vol(M) yields 4^n v_n/C(2n,n). The polar inequalities |y_i−y_j|<=2 (y0=0) describe a range<=2 polytope with vertices ±2 1_S; sign-pattern integral ∫_{a+b≤2}k(n-k)a^(k-1)b^(n-k-1) da db gives 2^n per sign-count k=0..n, so vol(M°)=(n+1)2^n and Holmes--Thompson value 4^n(n+1)/(n!v_n). Gromov mass: maxima of cross-polytope determinants occur on doubled M vertices e_i−e_j; reduced directed-incidence matrices are totally unimodular so max det for M generators is 2^-n, largest cross-polytope vol=1/n! and normalized reflection volume=4^n/n!. Mass*: polar vertices ±2 1_S and multilinear absolute determinant convexity reduce maximal polar cross determinant to 2^n D_n, D_n=max zero-one determinant; the polar volume product vol(P)vol(P°)=4^n/n! gives minimal enclosing parallelotope vol=1/D_n, and mass* value 4^n D_n/n!. Independent scipy hull geometry reproduces vol(M),vol(M°),D_n=(1,2) at n=2,3: (3/4,12,1) and (5/12,32,2). Finite hull checks corroborate, not replace all-n unimodularity and polarity. D_n is left exact without pretending all-n closed form.

## originality

PASS

Lángi arXiv:1308.2500 defines exactly these four relative norm measures, gives Problem 4 on all-body extrema, but inspected full 10-page text (especially final Definition 2, Problem 4) does not state the all-n simplex benchmark. Classical Rogers--Shephard reflection and difference-body maxima provide Euclidean factors and simplex extremizers and are credited. The new mathematical content is explicitly computing all four norm-specific scalars for M, especially dual parallelotope determinant D_n; a normed volume formulation is not merely a restatement of Euclidean bound. No existing exact all-n simplex benchmark located by aliases of Busemann, Holmes--Thompson, mass, mass*, root polytopes or maximal determinant, but later renamed normed-volume literature remains a risk. Resultary failed; not used as evidence.

## value

PASS

A canonical n-simplex is the equality object of the classic Rogers--Shephard theorems and a natural baseline for Lángi's open relative reflection-volume problem. The four exact normalizations give useful all-dimensional benchmarks, and mass* establishes a nonobvious structural bridge to the discrete maximal 0/1 determinant invariant, indicating genuine combinatorial dependence rather than routine rescaling. No general minimum/maximum over arbitrary bodies is claimed, and formula 5 does not compute unknown D_n in closed form.

The dated certificate retains the supplied scientific assessment, sources and limitations.
