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
# Verification and limitations

Run `python3 verify_heawood.py` using Python 3.10+ without installing packages. The script constructs the stated Fano incidence graph and checks its edge/point-line incidence, constructs a spanning tree with eight chords, and checks all \(256\) even-subgraph masks for even degree at every vertex. It enumerates each of the \(256\) normalized edge signings and all \(8192\) anchored spin configurations to obtain the exact unsatisfied-edge histograms. Separately it computes each histogram via the Krawtchouk transform of the signed even-subgraph enumerator, with exact integer divisibility checks.

The verification checks all moment identities through degree eight, all seven complete DOS signatures, their representative counts \(28+56+24+84+42+21+1=256\), and the two distinct frustration indices at \(c_6=0\). The success marker is `VERIFY_OK 256_signatures 8192_spin_cuts 256_even_subgraphs 7_DOS_types cutoff_8`. Every loop has a complete finite range backed by the dimension-eight cycle space and the \(2^{13}\) root-fixed cut space. Computation here is a finite exhaustive proof certificate, not an infinite proof. The tests do not cover other graphs or physical errors in estimated spectral moments. Independent external audit has not been performed.
