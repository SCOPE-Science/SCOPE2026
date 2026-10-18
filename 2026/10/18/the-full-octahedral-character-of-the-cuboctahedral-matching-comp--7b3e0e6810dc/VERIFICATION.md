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

# Verification of the cuboctahedral matching-complex character

Run `python3 verify_cuboctahedral_character.py` using Python 3.10 or later. No external packages or nonlocal data files are needed.

The checker constructs the twelve cube edges and twenty-four cuboctahedral edges, enumerates all \(2649\) augmented matchings and verifies the complete size distribution. It runs the reversed-edge-index discrete-Morse algorithm, certifies \(1296\) pairs and exactly \(57\) critical size-four faces, and topologically sorts the entire \(9960\)-arrow augmented Hasse directed graph. This proves acyclicity and gives the integral reduced chain model with one free group of rank \(57\) in dimension three.

It enumerates the complete group of \(48\) signed cube-coordinate permutations and verifies that they yield distinct permutations of the complex vertices. For every group element, it calculates the rational third-homology trace in two independent ways: (1) direct inspection of each invariant oriented face, including its orientation sign, and (2) an orbit-by-orbit alternating sum over unions of disjoint edge orbits. Both agree for all forty-eight elements. The ten conjugacy-class traces, class sizes, two central projection characters, the exact \(S_4\) multiplicities, central eigenspace dimensions, and invariant dimension are then checked.

Expected final line: `VERIFY_OK`. This is a complete finite certificate for the **specific** labeled cuboctahedral graph; it does not supply an integral representation-lattice classification, a higher-cube theorem, or an independent external audit.
