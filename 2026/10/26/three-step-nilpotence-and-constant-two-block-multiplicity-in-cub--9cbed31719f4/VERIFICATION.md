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

The file `verify_cube_edge_parity.py` is standalone Python 3 and uses only the standard library. Run `python3 verify_cube_edge_parity.py` in the directory containing the file; compare its console output with `verify_cube_edge_parity_output.txt`. It independently constructs edges and line-graph neighbourhoods and performs binary row elimination and matrix products using integer bit masks.

Actual checks: GF(2) ranks at four iterate levels for each \(d=2,3,4,5,6,7,8\) (28 rank comparisons); exact zero third powers on all seven tested graphs; exhaustive first-zero times over \(16+4096=4112\) initial configurations at dimensions two and three; 2560 seeded trajectory tests over dimensions four through eight; one-dimensional isolated-site boundary. The recorded output ended `CUBE_EDGE_PARITY_VERIFY_OK`.

The program does not prove the theorem for arbitrarily large dimensions. The infinite-parameter proof is the group-algebra argument in `RESULT.md`. The relevant 2010 coding paper was located by bibliographic and abstract evidence, but not inspected completely; only the related full-text 2013 thesis treatment was read in its relevant chapter sections. Independent audit is not yet performed.
