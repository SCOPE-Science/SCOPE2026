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

The proof has one source-dependent premise and one computability-theoretic translation.

The source-dependent premise is Pakhomov's Theorem 6.1: no arithmetical formula, even with set parameters, can uniformly enumerate the entire second-order universe of a model satisfying the relevant
\[
\Sigma^1_1\text{-}\mathsf{Rfn}
\]
instances.

For the translation, fix a set parameter \(A\) and a standard finite \(k\). There is an arithmetical relation
\[
\varphi_k(e,y,A)
\]
saying that the \(e\)-th oracle computation using \(A^{(k)}\) halts on \(y\) with output \(1\). Because \(k\) is fixed, the finitely iterated jump predicate can be unfolded into an arithmetical formula relative to \(A\).

If every model set \(B\) satisfied
\[
B\le_T A^{(k)},
\]
then each \(B\) would have some total characteristic index \(e\), and
\[
y\in B
\leftrightarrow
\varphi_k(e,y,A)
\]
would hold for every \(y\). This is exactly the forbidden uniform-enumeration statement.

Finite tuples are reduced to one set parameter using their Turing join, which exists in every omega-model of \(\mathsf{RCA}_0\).

## Limits

The argument is uniform only after \(k\) is fixed externally. It does not define all finite jumps simultaneously by one arithmetical predicate and therefore does not prove the existence of a single set escaping every finite jump.

No computation or finite experiment is used to replace the reflection theorem.
