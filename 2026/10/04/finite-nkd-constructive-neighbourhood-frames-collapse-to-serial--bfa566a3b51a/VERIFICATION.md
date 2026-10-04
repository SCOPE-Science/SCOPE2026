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

The proof is symbolic and rests on two local equivalences.

For every finite admissible neighbourhood family \(\mathcal N\), binary-intersection closure and pairwise nonempty intersection imply that
\[
C=\bigcap\mathcal N
\]
is itself a nonempty member of \(\mathcal N\). Consequently, for every \(A\),
\[
(\exists U\in\mathcal N)\ U\subseteq A
\quad\Longleftrightarrow\quad
C\subseteq A,
\]
and
\[
(\forall U\in\mathcal N)\ U\cap A\ne\varnothing
\quad\Longleftrightarrow\quad
C\cap A\ne\varnothing.
\]

The bundled `verify.py` exhaustively enumerates all neighbourhood families on carriers of sizes \(1\) through \(4\). For every family satisfying the three structural assumptions, it verifies the nonempty core and both equivalences against every subset of the carrier. It also checks that all nonempty subsets occur as principal cores.

The infinite tail boundary is proved directly rather than inferred from finite computation.

## Limits

The verification establishes a finite-frame semantic reduction, not a finite-model property. It does not quotient canonical cores by world isomorphism or modal equivalence.
