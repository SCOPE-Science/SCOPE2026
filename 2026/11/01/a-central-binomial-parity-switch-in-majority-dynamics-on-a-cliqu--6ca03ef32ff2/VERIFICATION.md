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

# Reproduction and scope

The proof of the all-size claim is the explicit majority update on the reduced triple \((k,h,\ell)\), followed by a complete parity case split and a binomial multiplicity calculation. The scripts are independent corroborating finite tests rather than infinite certificates.

Run `python3 verify_reduced.py` to reproduce the reduced update for all integer \(2\le r\le256\), asserting exact entry times, periods, first-entry class counts, and the total \(2^{r+2}\) labelled configurations. The recorded output is in `verify_reduced.log` and reports \(132600\) tested reduced triples.

Build `verify_full.cpp` using `g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_full.cpp -o verify_full` and run `./verify_full` to evolve the whole labelled graph using its direct adjacency relation, not the symbolic reduced updater. The recorded output is in `verify_full.log`: \(524272\) initial configurations for all \(2\le r\le16\). It verifies all stated first-entry classes and exact counts for each size.

No third-party data sets or generated files are required; the source files and saved result transcripts are embedded alongside this document. These finite tests cannot prove an unbounded theorem; only the algebraic case distinction in the main exposition provides that proof. This is a self-review, not independent validation.
