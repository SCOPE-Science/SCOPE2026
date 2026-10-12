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

The fixed components were checked directly in the primary reduction.

The proposition vocabulary is fixed before the PCP-dependent action construction:
\[
\{0,1,a,b,\mathrm{root},\mathrm{stg1},
\mathrm{empty},\mathrm{end},\mathrm{ntF},\mathrm{lp}\}.
\]

The displayed initial pointed model \(s_I\) is defined entirely from this vocabulary and therefore does not depend on the PCP instance.

The final reduction sets
\[
\mathrm{Act}
=
\{\mathrm{add}_i:1\le i\le n\}
\cup
\{\mathrm{nxt\_stg},\mathrm{rmv}_0,\mathrm{rmv}_1\}
\]
and fixes
\[
\Phi_G
=
K\neg\mathrm{empty}\wedge
K(\mathrm{tail}\wedge\neg\mathrm{failed}).
\]

Only the event models \(\mathrm{add}_i\) depend on the PCP words.

Theorem 3.19 proves
\[
B\text{ has a match}
\iff
(s_I,\mathrm{Act}_B,\Phi_G)\text{ has a plan}.
\]

For the upper bound, enumerate finite action sequences. Every candidate can be checked effectively because product update of finite Kripke and event models is finite and modal model checking is decidable.

Hence the restricted problem is recursively enumerable; the binary-PCP reduction makes it recursively enumerable complete.

## Limits

No constant bound on the number or total size of input actions is claimed.

No proposition-minimality statement is claimed.

The proof does not extend the source's undecidability result to single-agent logics with negative introspection.
