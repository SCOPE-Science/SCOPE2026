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
# Reproducibility and checks

Run `python3 verify.py` in a directory containing the standalone script. Core assertions require only the Python standard library. The check records the exact rational table of four orbit probabilities at the observation times \(0,\pi/3,2\pi/3,\pi\), the four rational weights, each exact expected value \(1/6\), row stochasticity, and the exact \(n=4\) instantaneous probabilities \(1/8\).

When NumPy and SciPy are installed, the script also constructs the entire \(2n\)-vertex adjacency matrix directly and compares numerically exponentiated transition probabilities against the analytic orbit formulas at seven observation times for each of four graph orders. Optional tests do not enter the unrestricted proof. The nonexistence proof uses the analytic inequality \(p_1(t)+p_3(t)\le4/n^2\) for all real \(t\) and integers \(n\ge3\), derived from \(2-2\cos(nt)\le4\). The sample integer scan in the script does not purport to establish the infinite inequality.

The theorem is conditional only on the graph and Hamiltonian definitions stated in RESULT.md. No claim is made about broader graph classes, edge weight perturbations, or all possible optimal sampling laws. Independent evaluation is not yet performed.
