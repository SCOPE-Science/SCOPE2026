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

The theorem has a direct proof from linear algebra and homogeneity of the infinite pair. The accompanying `verification.py` checks finite consequences rather than serving as the proof of the infinite extension statement.

For each tuple, the coefficient map has two recoverable subspaces: its kernel \(K\) and the preimage \(U\) of the distinguished subspace. The finite generated pair is the quotient \(\mathbb F_q^n/K\) with distinguished subspace \(U/K\). Therefore equal flags give isomorphic marked generated pairs, and any such finite pair embeds because the ambient predicate and quotient both have infinite dimension.

The script independently enumerates all subspaces in reduced row-echelon form over \(\mathbb F_2\) through dimension five and over \(\mathbb F_3\) through dimension four. It then enumerates every nested pair \(K\le U\), verifies the Gaussian formula
\[
\sum_{0\le a\le b\le n}{n\brack b}_q{b\brack a}_q,
\]
and builds the full coefficient signature recording whether each vector lies in \(K\), in \(U\setminus K\), or outside \(U\). Every flag has a distinct signature.

The script also checks the equivalent Gaussian-multinomial sum for several fields and dimensions. Finally, for every \(0\le n\le100\), it independently maximizes the exponents and verifies
\[
\max_{a+b+c=n}(ab+ac+bc)=\lfloor n^2/3\rfloor,
\qquad
\max_{0\le b\le n}b(n-b)=\lfloor n^2/4\rfloor.
\]

Running `python3 verification.py` performs 8,999 assertions and prints `VERIFY_OK`.
