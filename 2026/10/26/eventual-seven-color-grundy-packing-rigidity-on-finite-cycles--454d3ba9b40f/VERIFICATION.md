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

# Reproducible finite checks
Run `python3 verify.py`. The script requires only standard-library Python. It verifies nine displayed cyclic witness words of lengths \(22,23,24,26,27,28,29,30,31\), all four extension families at insertion parameters \(t\in\{0,1,2,3,4,5,10,25\}\), and the graph-distance and first-fit conditions separately. The deterministic output is contained in `verification_output.txt`. The finite checks certify the finite premises of the proof. The arbitrary-size extension follows from the explicitly stated radius-seven argument, not from extrapolating these tests. The bound from the doubly infinite path is from the cited primary source, not computationally recomputed here. No external or independent assessment was performed.
