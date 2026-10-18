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

# Reproducible mathematical verification

With a standard Python 3 interpreter, run `python verify.py` with `CERTIFICATE.json` in the same directory. `OUTPUT.txt` records the exact observed output, ending with `VERIFY_OK`.

The replay reconstructs all graph edges and independent faces from the graph definition; checks that each of 98 orbit cells is well-defined and that the antipodal action is free; verifies an explicit spanning tree and 37 triangular edge eliminations (so the original independence complex is simply connected); and checks all 32 elementary regular-CW collapses against current coface incidence. It independently evaluates mod-two boundary ranks and obtains Betti numbers (1,1,2,0,0). No third-party Python packages are needed.

These finite certificates prove only the described finite graph facts. The integral homology deductions use the covering theorem, cellular homology, and Euler characteristic. The cup-square conclusion uses the integral Bockstein and \(\rho\delta=\mathrm{Sq}^1\), not a claim that homology alone determines cup products. No higher-homotopy or homotopy-wedge result is certified.
