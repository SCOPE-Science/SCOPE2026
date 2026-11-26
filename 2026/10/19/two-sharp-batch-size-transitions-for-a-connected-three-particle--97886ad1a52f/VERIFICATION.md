---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The two-sided reset construction is stationary, and coupling with the same driving processes removes every initial coordinate after its first reset, since each marginal reset rate is rm/N>0. Given reset times, the squared positions of distinct labels have independent conditional means 2D times their ages. Independently of the generator proof, order the k age thresholds in the integral of their joint survival function: going backward, the protected set has sizes k,k-1,...,1 on the successive intervals, with Poisson hit rates r*q_j. Integration over unconstrained successive interval lengths, and k! possible orderings, gives M_k=(2D/r)^k k!/product(q_j). Thus the displayed normalized V is the third cross-cumulant, with positive denominators since q_j>=m/N. An independent SymPy 1.14 replay at /workspace/branches/40acab28-45a3-4de5-93a4-d5f0d96e69b1/independent_check.py checked the rational reduction, divisibility by m-3, the exact comparison with m=3, all listed coefficients in both positivity ranges, and the endpoint comparison. The substitutions cover 4<=m<=N-2 in full for N>=10, and V(3)>V(N-1)>V(N)=2>V(1)=0. The last difference has sign opposite N^2-77N+228; its smaller root is below 10 and the larger is strictly between 73 and 74, so there are no integer ties in the remaining range. Exact enumeration at 3<=N<=9 gives the stated unique maxima and runner-up 2 each time. Boundary spot checks also give V_10(3)-V_10(2)=325/1836 and V_74(3)-V_74(2)=-50653/360289620. The proof for unbounded N uses coefficient positivity, not finite enumeration. The frozen checker, notes and dependency file were inspected, not executed.

## originality

PASS

The same process and its all-order marginal recursion are prior, and the third-cumulant formula is extractable from that recursion. The all-but-one endpoint is also covered by a broader catalogue theorem. Credit the complete integer optimization with two distinct transitions and exact exclusion of all other batch sizes, not the closure or endpoint.

## value

PASS

Batch size is the natural control parameter in this solvable correlated Brownian model; the connected third moment isolates collective dependence not optimized by the known pair criterion. The complete all-size optimizer and strict integer cutoffs identify when large synchronized batches, triples, or pairs maximize it, with robustness to diffusivity and Poisson rate scaling. This is an exact classification across the model's full batch domain, not a few convenient numerical slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
