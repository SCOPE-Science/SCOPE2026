# Independent scientific audit — 2026-10-01

Record: `SCOPE-20260920-1d34d1fcd5a6`

Disposition: **passed**

The claim in `RESULT.md` is accepted unchanged. This audit assesses one final claim and requires separate correctness, originality, and scientific-value passes.

## Correctness — PASS

Writing the degree-​\(b\) and degree-​\(a\) classes as \(X,Y\), LIC makes the cross-edge graph connected, hence every vertex has a cross-neighbor and \(|X|+|Y|\ge b+1\). The degree sum gives \(\mu=((b-2)|X|+(a-2)|Y|)/2+1\). For \(a\ge3\), the lower bound is strictly increasing in \(|X|\); \(|X|=1\) is feasible exactly when a \((a-1)\)-regular graph on \(b\) vertices exists, i.e. \(b(a-1)\) is even, while the opposite parity forces \(|X|\ge2\). Equality forces exactly the stated joins. The \(a=1\) star case and \(a=2\) identity \(\mu=(b-2)|X|/2+1\) separately yield the exceptional odd-\(b\) family; its common/private-neighbor decomposition follows from degree two and connectedness of the irregular-edge subgraph. Thus the formula and full threshold classification are proved for all boundaries, independent of the finite Atlas check.

The package computations, where present, were treated as supporting checks rather than substitutes for the general proof.

## Originality — PASS

### Equivalent formulations

**Searches/source IDs**
- Published SCOPE archive query: locally irregular-connected degree set prescribed cycle rank bidegree cyclomatic minimum
- Published SCOPE archive query: LIC graph degree set cycle rank two prescribed r Chartrand Zhang
- DOI:10.3390/math14111827

**Evidence**
- The published SCOPE search returned the audited result as the only direct all-parameter bidegree threshold match.
- Chartrand--Zhang Theorem 9 states that the two-element degree sets admitting LIC cycle rank 2 are exactly \(\{2,3\}\) and \(\{2,4\}\).

**Reasoning**

The audited theorem varies the degree pair and minimizes cycle rank; this is not equivalent to the source paper's fixed cycle-rank-2 classification or its minimum-order theorem.

### Broader coverage

**Searches/source IDs**
- Chartrand--Zhang, Locally Irregular-Connected Graphs (2026), full text
- Tripathi--Vijay least-size degree-set literature

**Evidence**
- The primary LIC paper characterizes cycle rank at most two and minimum order, but does not state the all-parameter first-cycle-rank function.
- The unrestricted least-size literature concerns edge count without the LIC minimum-cycle-rank constraint.

**Reasoning**

Neither source family dominates the claimed invariant; the audited result recovers the known rank-two pairs as exactly those with threshold two.

### Exact database or table

**Searches/source IDs**
- Published SCOPE semantic search for LIC/bidegree/cyclomatic aliases

**Evidence**
- No separate database/table entry with the formula or complete extremal classification was located.

**Reasoning**

The claim is a symbolic extremal theorem rather than a finite-table lookup; no known table mechanically supplies it.

### Claim versus prior implication

**Searches/source IDs**
- Chartrand--Zhang Theorem 9 and concluding higher-cycle-rank discussion
- Published SCOPE search

**Evidence**
- Theorem 9 supplies only the threshold-two special cases; its statements do not imply the parity-dependent threshold for arbitrary \(a,b\).

**Reasoning**

The new lower bound uses degree-class counts and parity, and the equality analysis classifies minimizers. Those conclusions require additional argument beyond the prior fixed-rank result.


### Source inspections

- **Locally Irregular-Connected Graphs** — `https://doi.org/10.3390/math14111827`. Trigger: Direct source introducing the same LIC degree-set/cycle-rank framework. Material read: Open-access full text, including the cycle-rank-two classification and Theorem 9. Method: Lawful open-access full text. Assessment: NOT_COVERING beyond the special cycle-rank-two cases; it gives exactly \(\{2,3\}\) and \(\{2,4\}\) for two-element sets at rank two. Evidence: Theorem 9 explicitly gives the two bidegree cycle-rank-two cases and minimum orders.

### Checked sources

- DOI:10.3390/math14111827
- DOI:10.1016/j.dam.2006.04.003
- DOI:10.1016/j.dam.2023.02.012
- published SCOPE archive search

### Residual originality risks

- Very recent follow-up work or older results indexed under bidegreed/cyclomatic terminology could contain an equivalent threshold theorem.

## Scientific value — PASS

This closes a natural extremal parameter introduced with LIC graphs: for every two-degree set it gives the exact first attainable cycle rank and classifies every minimizer, strictly extending the previously known rank-two cases. The parameter is structurally motivated by the source paper's prescribed-degree-set and cycle-rank program, not an arbitrary finite slice.

## Limitations

The theorem treats two-element positive degree sets and determines the minimum attainable cycle rank, not every larger attainable rank. The unrestricted least-size problem is prior art. Very recent or differently indexed bidegree/cyclomatic work remains a residual originality risk.

## Final assessment

Correctness: **PASS**  
Originality: **PASS**  
Scientific value: **PASS**  
Disposition: **passed**
