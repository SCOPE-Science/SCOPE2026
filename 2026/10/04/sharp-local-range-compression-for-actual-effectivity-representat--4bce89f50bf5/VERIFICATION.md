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

For a fixed world, the verifier treats a neighborhood family
\[
\Sigma_a
\]
as a finite set of nonempty subsets of the carrier.

It exhaustively enumerates every two-agent pair of such families on carriers of size at most three satisfying common union and independence.

For every admissible pair it constructs actions
\[
(s,v),
\qquad
s\in\Sigma_a,\ v\in O,
\]
where
\[
O=\bigcup\Sigma_a,
\]
uses a cyclic group on \(O\), and implements the product-or-fallback outcome rule.

It then computes the exact output set of every action and confirms that the induced actual-effectivity family is precisely the original \(\Sigma_a\).

The same construction is exhaustively checked for all admissible three-agent frames on two-element carriers.

For the sharpness family
\[
\Sigma_a=\Sigma_b=\{O\},
\]
the verifier checks the cyclic realization through
\[
|O|=12.
\]
The lower bound itself is symbolic: with \(m_b\) actions available to the second agent, a fixed first-agent action occurs in only \(m_b\) deterministic profiles and therefore has at most \(m_b\) distinct outcomes. Exact output set \(O\) forces
\[
m_b\ge |O|,
\]
and symmetrically for the first agent.

The script prints `VERIFY_OK`.

## Limits

The exhaustive replay covers small finite frames and corroborates the construction. The arbitrary finite theorem follows from the group-cancellation proof. No exact minimum-action formula for general frames is claimed.
