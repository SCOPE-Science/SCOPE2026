---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For X=Sym^d(P^n_C), n,d>=2, N=nd, the ordered configuration F=(P^n)^d minus diagonals has complement codimension n>=2 and an etale S_d-quotient U. Equivariant Picard descent and the lifted symmetric external tensor product give Pic(U)=Z[L] plus sign Z/2; codimension-2 invariance yields Cl(X)=Pic(U), while sign does not descend as Cartier at a transposition, so Pic(X)=Z[L]. Simple connectivity of F and H²(F,Z)=Z^d plus integral Cartan–Leray give H²(U,Z)=Z[L] plus H²(S_d,Z)=Z/2 represented by c1(sign). The invariant free generator lifts, eliminating possible differentials and showing c1 is an integral isomorphism. Chow and Borel–Moore localization (collision dimension <=N−n and n>=2) identify CH_{N−1}(X)→H_{2N−2}(X,Z) with that same c1 isomorphism. For point multiplicity blocks lambda_i, the stabilizer is product S_{lambda_i} and no element acts as a pseudo-reflection since each swap moves n>=2 normal directions; its character group is (Z/2)^r for r repeated blocks, and the global sign restricts diagonally. The canonical permutation determinant is sign^n, and the minimum nonidentity age is n/2, proving K=−(n+1)L+(n mod2)tau, Cartier iff even n, canonical n=2 and terminal n>=3. These are uniform exact topological and quotient arguments, not finite experiments.

## originality

PASS

The recent Chen–Hu 2026 symmetric-product Chow paper already covers a special sign torsion class for Sym²(P²) and gives general bounded-cokernel/split-injection context. The present claim purports full divisor-degree integral cycle isomorphism for every n,d plus diagonal global-to-completed-local obstruction and canonical parity. General Benson–Nakajima/Schmitt quotient character results cover the local group mechanism but do not alone imply global integral cycle classes. Full Chen–Hu primary text was inaccessible in this run despite OA/authorized retrieval attempts; no whole-paper NOT_COVERING assertion is made. Earlier configuration-space spectral sequence formulations may imply the claim and remain serious priority risk.

## value

PASS

Integral algebraicity of every divisor-degree homology class, including a non-Cartier sign torsion class, is a natural sharp degree boundary next to known codimension-two torsion obstructions. The exact global/local diagonal image and the Gorenstein parity are intrinsic geometric invariants across a canonical infinite family, not arbitrary special-case calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
