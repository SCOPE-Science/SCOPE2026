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

# Reproducibility

Run `python3 verify.py`. The script is self-contained (Python 3 standard library), constructs the de Bruijn edge graph from first principles, enumerates all \(3^8=6561\) complement-compatible edge subsets, checks directed reachability on their active vertices, verifies all \(20\) possible nonempty strongly connected supports and their six maximal templates, verifies the precise unique/nonunique family-membership rule, reconstructs \(8\times8\) adjacency traces and their characteristic determinants by exact integer Newton recurrences, and checks the separation formulas to length \(36\). Independently it enumerates every binary labeled circular word for lengths \(1\) through \(16\), testing the wraparound four-block complement condition exactly.

Expected success begins `COMPLEMENT4_CYCLIC_PASS` and lists the first \(20\) counts. The file's Python assertions halt if a stated certificate fails. The all-length step uses the finite strong-connectivity classification and formal trace determinant identity; direct enumeration through \(16\) does not on its own prove infinitely many cases. No runtime, publisher, or external verification service is necessary. A separate mathematical audit has not been performed.
