---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The state equivalence refinement of a single proposition on row-column S5 gives type (cell bit, set of bits in its row, set in its column). On the regular event, each active row/column has both bits among active rows/columns; active-active contributes distinct 0 and 1 types, and zero-row/zero-column combinations add exactly a+b+ab distinct 0 types, so K=2+a+b+ab. Successor type sets depend only on row or column inactivity, proving depth-one stabilization by induction. In critical density p=(ln n+c)/n, inactive row/column counts X,Y have joint factorial moments (n)_a(n)_b(1-p)^[n(a+b)-ab]→(e^-c)^(a+b); thus independent Poisson limits. Markov on numbers of inactive rows/columns and a binomial tail union bound for max degree < n/2 justify regularity with probability 1-o(1). Cardinality is 2^K. Fixed p∈(0,1) gives exactly four whp by a 2n[p^n+(1-p)^n] union bound. Independent modal refinement of all n=2 and n=3 regular matrices found respective K distributions n=2:{2:2}, n=3:{2:102,3:36,5:18}, agreeing with 2+a+b+ab. Finite cases do not prove Poisson convergence.

## originality

PASS

Existing Df2-cylindric/subalgebra structural theory and Poisson isolated-row/column threshold are prior; the assessed precise three-point law for the size of the one-generator bimodal Boolean algebra and its depth-one structural mechanism are not the same as either. Best-of-knowledge, natural random relational language parameters fixed.

## value

PASS

The limiting distribution of a naturally generated modal algebra at the sparse-isolation threshold quantifies logical expressivity in a random finite epistemic model, with sharp three-point law and uniform bounded modal depth despite n² worlds. This is a motivated exact probability law and structural bridge to the Poisson isolated-class phenomenon, not mere rephrasing of known isolated-vertex counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
