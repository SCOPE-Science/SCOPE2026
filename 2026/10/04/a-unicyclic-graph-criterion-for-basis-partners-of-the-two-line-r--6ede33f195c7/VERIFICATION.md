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
# Verification

Run `python3 verify.py` with Python 3. The script uses only the standard library and prints

`VERIFY_OK exact_modular_cases=407 exhaustive_p3=84 p3_bases=75`

on success.

The replay has three layers. First, it exhausts all \(\binom{9}{6}=84\) frequency sets for \(p=3\) and checks the graph/nullity criterion, finding \(75\) invertible cases. Second, for \(p=5,7,11\) it checks an explicit spanning-unicyclic family with a four-cycle and deterministic candidate samples. Third, whenever the graph is unicyclic, it evaluates the Fourier determinant at exact finite-field specializations of a primitive \(p\)-th root and checks the conjugate-product form of
\[
|\det T(E_p,B)|^2=p^{2p}|S_C|^2.
\]
Two finite-field specializations are used for each tested prime.

The universal result does not depend on these finite experiments. Its proof is symbolic: Fourier inversion identifies the two incidence constraints; the standard rank theorem for a connected bipartite incidence matrix gives the cycle-space dimension; the minimal polynomial \(1+X+\cdots+X^{p-1}\) gives the exact prime cyclotomic zero criterion; and a reduced incidence determinant expansion gives the determinant formula. No claim is made for composite moduli or for the unresolved asymptotics of \(\rho(E_p)\).
