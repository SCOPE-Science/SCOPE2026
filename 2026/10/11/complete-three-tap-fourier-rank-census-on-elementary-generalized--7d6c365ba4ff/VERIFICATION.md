---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For each additive character χ of A=F_p^d, direct two-coset Fourier transformation of the left-regular action yields one 2×2 fiber Bχ=[[Rχ,Fχ],[conj(Fχ),conj(Rχ)]] (up to harmless conjugation/reindexing), across N characters, with det Bχ=|Rχ|²−|Fχ|². Mixed 2+1 coset support is singular precisely when χ(a−b) is a primitive third root; the singleton forces each such block rank 1. For all-in-one-coset triples the block vanishes precisely when their 3 character values form {1,ω,ω²}, with each zero block contributing 2 dimensions. Since each χ-value is a p-th root, vanishing is impossible unless p=3. For p=3 the number of χ with χ(v)=ω or ω² for nonzero v is 2N/3; with independent v1,v2 giving the two target pairs it is 2N/9. This proves mixed nullity 2N/3, collinear single-coset 4N/3 and noncollinear 4N/9. The combinatorial counts are 2*binom(N,2)*N=N²(N−1), 2*binom(N,2)/3=N(N−1)/3, and 2*binom(N,3)−N(N−1)/3=N(N−1)(N−3)/3. These sum to binom(2N,3). For p=2, inversion acts trivially but the same two-coset Fourier decomposition applies; for d=1 the noncollinear stratum is empty. Full proof is analytic for every prime p and integer d>=1.

## originality

PASS

Best-of-knowledge: the general finite Cayley Fourier block method is known (Arezoomand–Taeri 2013), and ordinary inverse-closed cyclic-dihedral cubic formulas are known (Huang–Huang–Lu 2016; Al-Tarimshawy–Siemons 2020). The distinct all-support, all-dimension prime-three nullity trichotomy plus labeled support multiplicity census was not contained in any inspected prior statement. Published elementary-abelian three-sparse Fourier support spectra and ternary Heisenberg support census are adjacent but not logically equivalent. The exactly matching search result is this assessed record, not independent prior art; search absence alone is not novelty proof.

## value

PASS

Convolution rank is a natural linear-algebraic/harmonic invariant of a finite group, measuring loss of information under a sparse translation filter. This result gives a complete, size-uniform classification for *all* unordered unweighted three-point supports on the elementary generalized dihedral family, identifies a sharp p=3 obstruction (all three-tap filters singular at p=3, all invertible otherwise), and provides exact kernel dimensions and incidence-geometric frequency counts. The distinction between mixed cosets, affine lines, and independent triples is a motivated structural partition, not an arbitrary small numerical slice; a researcher can directly use the precise rank distribution for sparse group filters. It does not claim a new representation decomposition or generality to weighted/larger-support filters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
