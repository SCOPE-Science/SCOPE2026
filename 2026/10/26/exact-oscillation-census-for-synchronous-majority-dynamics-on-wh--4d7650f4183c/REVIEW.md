# Scientific review of the wheel-majority census

## Correctness
PASS. The local majority rule reduces to AND of rim neighbors when the hub is zero and OR when it is one. Two-step composition proves both the fixed-hub classification and the no-isolated-one step-two condition for hub-reversing cycles. The two hub-majority inequalities select exactly the relevant states. A marked-run composition argument derives every coefficient of the binomial generating polynomial. The symmetric-threshold energy has strict descent unless a two-step return occurs, ruling out longer terminal periods. The explicit `110`/`1100` family proves the exponential lower bound without statistical extrapolation. The standalone direct-update checker and independent run enumerators passed 262112 complete wheel configurations (rim 4–16), plus word enumerations (length 2–14). No finite test is substituted for an infinite proof.

## Originality
PASS under the accessible published-record and primary-source comparisons, with recorded residual uncertainty. Turau (arXiv:2202.01580v1) classifies tree threshold dynamics, not wheels. Zehmakan (arXiv:2302.06760v1) counts stable cycle configurations and studies random-majority behavior, not the deterministic wheel period-two census. Nakar–Ron (arXiv:2205.08972v1) study fixed-radius one-dimensional automata rather than a universal hub whose update depends on all rim votes. Earlier accessible research results contain cycle-majority and friendship-graph claims but no wheel-census implication; published research-record searches returned no directly covering claim. The classical symmetric-threshold period bound and cyclic-run enumeration methods are not claimed as new. Unindexed results could still coincide with the particular wheel theorem.

## Mathematical value
PASS. The result completely classifies recurrent colorings of an infinite, socially interpretable network family, not just a finite graph or an arbitrary coefficient. A universal hub collapses the many stable configurations known for bare cycles to two, while an explicitly counted exponentially large collection of two-cycles survives; the hub may itself keep flipping. This separates equilibrium-profile suppression from oscillatory persistence in a highly centralized social graph. The theorem gives exact labeled orbit counts rather than a computational sample. It does not predict attraction-basin masses.

## Evidence and limitations
Closest primary sources: Turau 2022, Zehmakan 2023, Nakar–Ron 2022 (see RESULT.md). Verification: `verify_wheel.py`. The exact domain is an unweighted wheel with synchronous open-neighborhood majority and hub-tie retention; no general-graph or stochastic extension is claimed. Unindexed literature remains the principal originality risk. Independent audit is pending.

Self-review: passed. Independent audit: not yet performed.
