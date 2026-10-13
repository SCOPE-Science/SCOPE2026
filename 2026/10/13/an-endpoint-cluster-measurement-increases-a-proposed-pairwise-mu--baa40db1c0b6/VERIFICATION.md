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

The proof uses exact stabilizer reductions. For the four-qubit path graph, only the endpoint-adjacent pairs \(\{1,2\}\) and \(\{3,4\}\) contain a nonidentity stabilizer supported wholly on the pair; each corresponding reduced state has spectrum \(\{1/2,1/2,0,0\}\). The other four pair reductions are \(I/4\). Therefore the six initial mutual informations are exactly \(1,1,0,0,0,0\).

After a computational-basis measurement of qubit \(1\), each branch is a pure measured endpoint times a three-qubit path graph on \(2,3,4\), up to a local Pauli correction. The three remaining pairs each contain a nonidentity stabilizer supported on that pair, so their reduced spectra are all \(\{1/2,1/2,0,0\}\); pairs containing qubit \(1\) are product. The six branch mutual informations are therefore exactly \(1,1,1,0,0,0\).

The source normalization for four qubits is \(\mathcal M_{\mathcal{F}r}=\frac16\sum_{i<j}I(i:j)\), giving exact values \(1/3\) initially and \(1/2\) after either outcome. Since both outcomes occur with probability \(1/2\), the average postmeasurement value is exactly \(1/2\).

The bundled script `verify_cluster_counterexample.py` was executed from its packaged path and returned:

`VERIFY_OK initial_M=1/3 branch_M=1/2 average_post=1/2 gap=1/6 ratio=3/2`

The script is a finite exact check, not a substitute for the analytic proof. The result is limited to the specified four-qubit functional and protocol; it does not establish an optimal gap or make claims about the source's other probe or later total-correlation constructions.
