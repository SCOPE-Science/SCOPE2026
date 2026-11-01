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
# Reproduction and limits

With Python 3 and `networkx`, execute `python3 verify_pappus_configuration.py` from the directory containing the supplied verifier. The program does not download source data; its Pappus graph is constructed from the explicit LCF sequence. The recorded deterministic program output is in `verification_output.txt`, ending in `VERIFY_OK`.

The exact checks enumerate 153 unordered zero-cells, 432 one-cells and 297 two-cells; verify \(\partial_1\partial_2=0\); verify rank 152 of \(\partial_1\) and ranks 269, 270, 270, 270 for \(\partial_2\) modulo 2, 3, 5 and 101; construct ten explicit fixed-spectator lifts of fundamental graph cycles; enumerate 216 automorphisms in thirteen conjugacy classes; check signed chain-map equivariance on every cell; and compute the complete traces and invariant averages. All arithmetic used for certificates and character traces is exact integer or finite-field arithmetic.

The modular ranks alone do not establish rational Betti numbers; the ten independent lifted cycles provide the matching rank upper bound. Signed Lefschetz traces use the proved rational homology concentration and are not interpreted as an integral representation decomposition. The model computes ordinary unordered collision-free configurations, not signed-local-system Borel–Moore homology. No independent mathematical audit has been performed.
