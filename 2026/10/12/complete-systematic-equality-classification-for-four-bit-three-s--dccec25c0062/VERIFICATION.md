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

From the package directory execute `python3 verify.py`. No external Python packages, external code, downloaded papers, or other supplementary files are needed. A complete representative table is bundled as `orbit_representatives.tsv`, checked byte-for-byte against regenerated output.

The verifier independently checks the parity-XOR criterion and the unrestricted direct recovery-set criterion across all \(65536\) systematic parity matrices. It excludes \(0,1,2,3\) parity-column cases. It uses complete inclusion-minimal recovery lists to check the twenty possible three-request multisets for every successful code, computes canonical orbit representatives under the declared \(576\)-element group, independently sums Burnside fixed points, and checks incidence-lemma coverage, parity rank, and minimum Hamming distance.

Expected final line:

`VERIFY_OK systematic_optima=7800 orbits=26 batch_all=true incidence_lemma=456 other=7344 burnside=26`

The method proves the finite result for the stated binary systematic generator presentation space. It does not classify nonsystematic generator choices or prove a general three-PIR/three-batch equivalence beyond this finite case.
