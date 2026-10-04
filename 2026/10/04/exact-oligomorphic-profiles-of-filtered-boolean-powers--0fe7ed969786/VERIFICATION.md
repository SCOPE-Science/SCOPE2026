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

The proof is deductive. The checker validates the finite-group arithmetic and the main numerical specialization.

For a supplied finite permutation group \(G\curvearrowright A\), `verify.py` computes \(q_k=|A^k/G|\) in two independent ways: direct orbit enumeration on \(A^k\), and Burnside's formula
\[
q_k=\frac1{|G|}\sum_{g\in G}|\operatorname{Fix}_A(g)|^k.
\]
It checks agreement for a nontrivial symmetric-group action in several arities.

It then implements signed Stirling inversion and verifies that
\[
b_k=\sum_{j=1}^k {k\brace j}a_j
\]
is inverted by
\[
a_k=\sum_{j=1}^k s(k,j)b_j.
\]

For Mayr–Ruškuc's Example 1.2, where \(|A|=2\), \(G\) is trivial, and \(r=2\), the checker verifies
\[
b_k=2^{2^k-2}
\]
for \(k\le6\), obtaining
\[
1,4,64,16384,1073741824,4611686018427387904,
\]
and the injective counts
\[
1,3,54,16038,1073580048,4611686002322639760.
\]
It also directly counts the abstract support supersets for each tested \(q_k,r\).

Running the script prints `VERIFY_OK`.

These finite checks do not prove that support sets classify tuple orbits. That infinite step is proved in `RESULT.md` from the semidirect automorphism theorem and the homogeneity of finite clopen partitions of Cantor space with finitely many marked points.
