---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

PASS. Standard Johnson-scheme eigenvalues at the top level reduce to (-1)^i binom(k,i) on the intersection-drop i relation. The odd-graph distance min{2i,2(k-i)+1} assigns these coefficients to the correct even/odd metric shells. Folded-cube characters with even weight j=k+(k mod2) yield Krawtchouk coefficients from (1-z)^j(1+z)^(2k+1-j)=(1+(-1)^k z)(1-z^2)^k; the identity holds for each independent phi(t), not only powers. For k=3, the three displayed nonconstant eigenvalues for the 35-vertex odd graph and the three for the 64-vertex folded cube have correct multiplicities; a=2^p, b=3^p and b>=1.5 a-0.5 keep all branches except common g(p)=3b-3a-1 strictly negative up to its unique root alpha approximately 0.5165843743; g increases, is positive afterward. Centered Schoenberg Gram ranks at alpha are 6+14=20 and 21+7=28. Independent exact coefficient comparisons for k=2..21 yielded 230 equalities; direct metric-formula/full numerical spectra in 10 comparisons support k=3 (the inspected package check.py separately implements BFS). k=2 and p=0 conventions were checked, not assumed by continuity. No claim of all-k equal thresholds.

## originality

PASS

PASS with association-scheme priority risk. Aalipour et al. (arXiv:1509.01196) prove the odd-graph metric and Johnson/Eberlein eigenvalues used here; Mančinska et al. (arXiv:1808.02051) define folded-cube antipodal quotient and cubelike characters. Sánchez (arXiv:1108.0451) gives finite-metric negative-type machinery. Their inspected primary passages do not assert the all-k coefficientwise cross-family top-harmonic/Walsh equality nor the coincidence of sharp Schoenberg exponents for KG(7,3) and F7 with distinct endpoint ranks. This is more specific than claiming the underlying polynomial identities individually novel.

## value

PASS

PASS. Comparing two canonical but nonisomorphic distance-regular graph families across every radial kernel is a motivated structural relation of association schemes, not a renamed individual spectrum. The k=3 consequence determines a sharp natural negative-type threshold and embedding dimensions for both finite graph metrics, potentially useful in Schoenberg-type graph embeddings and metric spectra. Neither equality of whole spectra nor general k threshold is overstated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
