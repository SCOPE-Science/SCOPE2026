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
The universal proof is symbolic. Its critical steps are:
- every subgroup outside \(A\) is uniquely \(H(B,x)=\langle B,x\gamma\rangle\) with \(\langle y\rangle\le B\le A\) and \(x\) modulo \(B\);
- direct multiplication gives
  \[
  H(B,x)H(C,z)=H(C,z)H(B,x)
  \quad\Longleftrightarrow\quad
  (xz^{-1})^2\in BC;
  \]
- the difference map from \(A/B\times A/C\) to \(A/BC\) is surjective with fiber size \(|A:B\cap C|\);
- acceptable images are exactly the \(2\)-torsion elements of \(A/BC\);
- all subgroups contained in \(A\) are normal;
- outside cyclic subgroups are exactly the \(|A:\langle y\rangle|\) groups \(\langle x\gamma\rangle\), and their permutability count is \(|Q|\,|Q[2]|\).

`artifacts/verify.py` independently constructs finite generalized dicyclic groups for several cyclic and noncyclic kernels, enumerates their complete subgroup lattices, checks \(HK=KH\) for every ordered pair, computes the two degrees directly, and compares them with the formulas. It also checks the published special values for \(\operatorname{Dic}_{12}\), \(\operatorname{Dic}_{16}\), \(C_2\times C_6\)-kernel examples, and the \(C_2\times Q_{16}\) specialization.

The replay returns `VERIFY_OK`.

Finite enumeration is not used to establish the universal theorem.
