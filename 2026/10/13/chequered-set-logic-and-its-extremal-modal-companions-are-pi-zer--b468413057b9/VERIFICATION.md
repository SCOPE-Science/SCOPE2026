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

Pawlowski's primary result states that
\[
\mathsf{Med}
\]
is \(\Pi^0_1\)-complete under computable many-one reductions.

Xiao's Theorem 6.1 gives a computable formula map \(C\) satisfying
\[
\varphi\in\mathsf{Med}
\quad\Longleftrightarrow\quad
C(\varphi)\in\mathsf{Cheq}.
\]
Therefore \(\mathsf{Cheq}\) is \(\Pi^0_1\)-hard.

For the upper bound, enumerate the finite frames \(\mathbf V_n\), all persistent valuations of the finitely many input variables, and all worlds. A nonvalid formula has a witness in this enumeration. Hence the complement of \(\mathsf{Cheq}\) is recursively enumerable, so
\[
\mathsf{Cheq}\in\Pi^0_1.
\]

The G\"odel translation \(T\) reduces \(\mathsf{Cheq}\) to either modal companion by the defining modal-companion equivalence. Thus both \(\mathsf{S4.FPFA}\) and \(\mathsf{L}_{\infty}\) are \(\Pi^0_1\)-hard.

Their upper bounds use the source's effective finite semantics:
\[
\mathsf{L}_{\infty}=\mathsf{ML}(\{\mathbf A_n:n\ge1\})
\]
and
\[
\mathsf{S4.FPFA}=\mathsf{ML}(\{\mathbf A_n:n\ge1\}^{\bullet}).
\]
The first frame class is uniformly computable. The second is recursively enumerable by enumerating finite preorders and retaining those whose mutual-accessibility quotient is isomorphic to some \(\mathbf A_n\). Exhaustive valuation search semidecides nonvalidity in either logic.

Thus all three validity sets are \(\Pi^0_1\)-complete.

## Limits

No bounded running-time claim is made for the semidecision procedures.

No statement is made about restricted fragments or arbitrary modal companions beyond the two explicit Cheq companions.
