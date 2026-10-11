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

The upper and lower bounds reconstruct exactly. The continuous surjection \(\Psi:\Delta_{m-1}\times K^m\to\mathcal M_{\le m}(K)\) intertwines \(\mathrm{id}\times T^{\times m}\) with \(T_*\), so factor monotonicity and the compact product entropy formula give the upper bound \(m h_{\mathrm{top}}(T|_K)\). For the lower bound, binary weights \(2^{i-1}/(2^m-1)\) have distinct subset sums, so \(\Phi_m(x)=\sum_i a_i\delta_{x_i}\) remains injective even when coordinates collide; its image is a compact invariant subsystem conjugate to \(T^{\times m}\). The argument remains valid when the entropy is infinite.

## originality

PASS

The complete Huo--Wang paper was read. Its Lemma 3.1 introduces exactly the binary-weight product embedding and Proposition 3.2 uses it to obtain a lower bound inside the full supported-measure space. The paper's theorems concern upper-capacity, packing and Bowen entropy of the full \(\mathcal M(K)\), and nowhere state the exact ordinary topological entropy of the finite-support stratum. The matching upper bound from the simplex parametrization is not supplied there. Targeted Resultary and literature searches found no prior statement of the finite-atomic equality.

## value

PASS

Support cardinality is the natural finite filtration of the induced probability-measure system. The theorem gives its exact entropy at every finite level and quantitatively explains how the product-embedding amplification grows before the full measure space reaches the known zero/infinite dichotomy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
