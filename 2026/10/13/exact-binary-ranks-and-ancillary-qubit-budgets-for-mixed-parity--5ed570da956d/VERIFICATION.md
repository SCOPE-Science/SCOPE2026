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

# Checks of the mixed-parity Hamming-box formula

To reproduce the exact finite calculations, run `python3 verify.py` with Python 3 and no third-party packages. The program constructs each \(K_{q_1}\square\cdots\square K_{q_d}\) adjacency row by independently enumerating neighboring coordinate tuples; it does *not* generate the matrix from the Kronecker-sum proof. It computes its rank over \(\mathbb F_2\) by bitset Gaussian elimination, then compares \(N-\operatorname{rank}A\) with \((Q+H)(P+(-1)^dR)/4\).

Observed output after extraction and replay of this package:

`VERIFY_OK all=1222 mixed_parity=1034 odd_only=26 even_only=162 max_N=324`

The 1,222 checked ordered parameter tuples have alphabet sizes in \(\{2,3,4,5,6\}\), lengths \(1\) to \(5\), and at most \(350\) vertices. The 1,034 mixed-parity instances fall inside the claim; the remaining 188 cases are controls testing formula boundaries. Since these are finite observations, they do not establish the unbounded theorem. The proof in RESULT.md proves it for every allowed size and dimension, including the zero-homology boundary \(q_i=2\).

The connection to physical-resource counting depends on the mixed-graph framework's external Lemmas 4.1 and 4.2 and on orienting every edge exactly once; no claim is made for graph models with retained undirected edges. No hardware implementation, numerical quantum simulation, or independent external validation is claimed.
