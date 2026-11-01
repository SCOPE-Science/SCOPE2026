---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducibility and verification

Run `python3 CHECK.py` using Python 3's standard library. The code exhaustively constructs all nontrivial cyclic subgroups, selects those maximal by inclusion, builds the complete set of coset rows, multiplies them as an exact integer Gram matrix, compares every Gram entry against its subgroup-incidence formula, enumerates all character-annihilator eigenvalues, and checks exclusive direction witnesses. It runs for primes \(2,3,5,7\).

Expected final message: `VERIFY_OK four_primes=PASS direct_coset_Gram=PASS exact_abelian_Fourier=PASS witnesses=PASS weighted_spectrum=PASS`.

Observed output included dimensions \(8,27,125,343\), respectively, row counts \(12,36,150,392\), and the precise eigenvalue multiplicities stated in RESULT.md. The weighted-spectrum check uses the special positive weighting \(\alpha_t=p^{-2}\), \(\beta_s=p^{-1}\), which makes unique-direction Fourier eigenvalues equal to one and the exceptional \(p-1\)-dimensional sector equal to \(p\). The symbolic proof covers arbitrary positive real weights.

Finite computational checks do not establish the universal case; exact character orthogonality and the inequality in RESULT.md do. This reproduction is not an independent mathematical audit.
