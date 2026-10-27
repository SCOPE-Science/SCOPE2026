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

# Verification procedures and boundaries

The exact finite proof first constructs 17,576 capped signatures and 109,512 occupied tagged-vertex states. The Python verifier computes all functional-graph entry times and periods, checks \(T^{21}=T^9\) on every tagged state, checks canonical signature templates by finite set equality, and evaluates the exact weighted multinomial census at a range of parameters. Expected recurrent signature counts by physical period are: 174 for period one, 1,826 for period three, 18 for period four, six for period six, and 126 for period twelve. The maximum tagged-entry time is nine.

Commands from the artifact directory:

```sh
python3 verify_tripartite_cca.py
c++ -std=c++17 -O2 direct_vertex_check.cpp -o direct_vertex_check
./direct_vertex_check
```

The C++ checker independently builds the original adjacency structure using the three part memberships and enumerates 322,218 labelled initial configurations on six small examples. The result is `DIRECT_VERTICES_OK`; the exact factor checker reports `FINITE_CERTIFICATE_OK`. Recorded output is provided in `verification_output.txt`. No compiler executable is needed from the package: the supplied C++ source is standalone.

The all-size theorem relies on the mathematical proof that saturation at two and the tagged-vertex lift preserve the relevant dynamics exactly. The small-instance checks are corroborative and would not establish the infinite-family statement on their own. No external or independent audit has been performed.
