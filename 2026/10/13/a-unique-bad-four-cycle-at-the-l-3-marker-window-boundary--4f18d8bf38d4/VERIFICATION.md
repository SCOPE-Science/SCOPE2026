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

The central obstruction is checked directly from the definitions. For
\[
D_0=\{-5,-1,3\},\quad
D_1=\{-4,0,4\},\quad
D_2=\{-3,1,5\},\quad
D_3=\{-6,-2,2,6\},
\]
each set is \(3\)-separated and \(3\)-covers \([-3,3]\cap\mathbb Z\). With \(Q=[-6,6]\cap\mathbb Z\), each transition \(D_i\to D_{i+1}\), cyclically, satisfies
\[
D_i\cap(-1+Q)=(-1+D_{i+1})\cap Q.
\]
The canonical direction on all four edges is therefore \(-1\), and the closed four-walk has total \(-4\).

The included `verify.py` reconstructs the whole \(L=3\) graph by exhaustive enumeration. It checks all \(2^{13}\) subsets of \(Q\), tests the separation and coverage predicates, tests both possible translation witnesses on every unordered pair, verifies witness uniqueness on every edge, enumerates simple four-cycles modulo rotation and reversal, and checks their direction sums.

Expected output is:

`VERIFY_OK`

`vertices=59`

`edges=75`

`simple_4_cycles=4`

`bad_canonical_4_cycles=1`

`exceptional_directions=(-1,-1,-1,-1)`

`exceptional_sum=-4`

The published source proves the corresponding canonical zero-sum statement for every \(L\ge4\). No claim is made about alternative noncanonical labelings of the \(L=3\) graph.
