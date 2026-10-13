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

Run `python3 verify.py` beside `certificate.json`.

Engine A checks all \(3000\) maps of ranks \(2\), \(3\), and \(4\). For each map it builds the complete simultaneous subset-pair graph under the cyclic generator and that map, then reverse-searches from the states where exactly one component is a singleton. All \(45\) initial pairs are reached. The exact shortest-distance histogram is
\[
45000,42360,28420,13525,4395,1005,235,50,10
\]
for lengths \(1,\ldots,9\).

Engine B quotients maps by independent cyclic rotations on the domain and image, leaving \(12+60+48=120\) representatives. It also quotients pairs of distinct \(2\)-subsets by simultaneous rotation, leaving \(9\) representatives. For every representative map it generates the entire transformation monoid and directly scans for a distinguishing element for every representative pair.

The finite verification establishes strong sync-maximality of \(C_5\). The extension to all primitive degree-\(5\) groups is the elementary deductive argument stated in the result.

Independent audit has not been performed.
