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

Run `python3 verify.py` using the Python standard library. The checker regenerates all finite objects, rather than relying on stored tables or a precomputed search transcript.

1. Reconstruct the sixteen binary words, with their closed Hamming-radius-one neighborhoods both from four single-bit flips and from Hamming distance.
2. Enumerate all \(8008\) six-word and all \(11440\) seven-word subsets; require two independent implementations of identifying signatures to agree for each candidate.
3. Establish that no six-word set identifies all vertices and exactly \(960\) seven-word sets do. By monotonicity, there is no smaller identifying set.
4. Enumerate all \(384\) coordinate-permutation/translation automorphisms and prove they preserve every closed neighborhood.
5. Partition the complete minimum-code family into three orbits, check sizes \(192,384,384\), stabilizer orders \(2,1,1\), and their distinguishing Hamming-distance spectra.
6. Independently verify Burnside's orbit count by computing all fixed minimum codes for all \(384\) automorphisms and requiring total fixed count \(1152\).
7. Prove that the Gray map between \(\mathbb Z_4^2\) with Lee distance and \(Q_4\) with Hamming distance is an isometry on all \(256\) ordered vertex pairs. Verify that the earlier paper's two displayed codes correspond to only two of the three orbit profiles.

The checker prints:

`VERIFY_OK minima=960 orbits=3 orbit_sizes=192,384,384 stabilizers=2,1,1 burnside=1152`

This is finite exact verification of the specified graph and group. It proves nothing about larger cubes or alternative identifying-code notions.
