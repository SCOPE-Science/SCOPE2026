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

The primary source supplies one-point canonical models for every
\[
\Lambda\subseteq\{\mathsf M,\mathsf C,\mathsf N,\mathsf K\}.
\]

A candidate satisfiability witness therefore consists of a propositional valuation and a finite closure generator from the source's polynomial-size syntactic fragment.

The nontrivial verification issue is \(\mathsf C\): unrestricted closure under conjunction can be infinite.

For a fixed input \(\varphi\), let \(R\) contain the source's relevant finite fragment, all its syntactic subformulas, and \(\top\). To decide whether a required box argument belongs to the generated closure, saturate only \(R\).

This restriction is complete for targets in \(R\). A conjunction created outside \(R\) cannot create new relevant information by later \(\mathsf M\)-decomposition, because its conjuncts were already present before the \(\mathsf C\)-step. The rules \(\mathsf M\) and \(\mathsf C\) never create implications, so every implication used by \(\mathsf K\) comes from the finite relevant source fragment and may be retained inside \(R\).

Each formula of \(R\) is inserted at most once. A worklist or repeated scan therefore terminates in polynomial time.

After saturation, the input formula is evaluated bottom-up in the singleton model. Thus satisfiability has polynomially checkable certificates.

Propositional SAT embeds unchanged, giving NP-hardness. Therefore satisfiability is NP-complete.

A formula is invalid exactly when its negation is satisfiable, so validity is in coNP; propositional tautology gives coNP-hardness. Strong completeness transfers the same bound to theoremhood.

## Limits

This check does not claim that the unrestricted closure is finite.

It covers only the systems with no modal inference rules, namely parameter sets contained in \(\{\mathsf M,\mathsf C,\mathsf N,\mathsf K\}\).

The closest non-congruential semantic paper could be inspected only at abstract level, leaving a stated literature-access risk but no contradictory or covering evidence.
