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
# Reproducible verification

The result is proved by a three-part reduction: the established three-round threshold for single simple cycles, closure of three-round equivalence under disjoint unions, and truncating each isomorphism-type component multiplicity to three. Consequently only \(4^5-1=1023\) canonical nonempty unions of \(3\)-, \(4\)-, \(5\)-, \(6\)- and \(7\)-cycles remain.

Run `python3 checker.py` using standard Python 3. It exhausts all 1023 cases and constructs exact rank-three empty-tuple types by three successive back-and-forth extension operations. It independently evaluates the six displayed sentences and verifies that equality of the six bits is equivalent to equality of full rank-three types. It prints the 12 representatives, each six-bit signature and reduced-class population; `enumeration.txt` is the checked output.

Run `python3 game_crosscheck.py` using standard Python 3. It computes a separate alternating-player three-round EF game recurrence, verifying each of the 144 ordered pairs of the twelve representatives and five additional same-class pairs. Both scripts terminate without network access or external dependencies.

These computations are finite and complete only for the 1023 canonical cases. The proof that every allowed graph has such a canonical representative depends on the cycle theorem of Brown–Hoshino and the elementary disjoint-union game strategy; it cannot be replaced by the computer enumeration. No formal proof-assistant certification or independent audit is claimed.
