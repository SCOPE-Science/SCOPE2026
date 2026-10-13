# Self-review: The zero-inflow avoidance face invalidates full uniform persistence

## Correctness
**PASS.** At the stated admissible endpoint \(p=v=0\), the printed avoidance equation factors exactly as \(A'=-q(t)A\) with \(q(t)\ge\mu>0\). The explicit solution gives \(A(t)\le A(0)e^{-\mu t}\), so any interior trajectory approaches the boundary \(A=0\). This alone contradicts full-state uniform persistence. The face is invariant, and direct substitution verifies the boundary endemic equilibrium for every \(R_0>1\). An exact witness with \(R_0=2\) is checked by `verify.py`.

## Originality
**PASS.** The primary article states the opposite stronger conclusion over a parameter domain that includes \(p=v=0\). Its supplementary proof explicitly uses the strict inequality \(p\gamma I+vS>0\) on \(A=0\), which is false at that allowed endpoint. Targeted searches for the source title together with the endpoint, persistence terminology, and boundary inflow did not locate a correction or another source giving this counterexample. The comparison is statement-level: the source's full-state conclusion is contradicted, rather than merely specialized.

## Value
**PASS.** Uniform persistence is a qualitative long-time theorem, not a numerical side calculation. The counterexample identifies an invariant boundary face omitted from the source's maximal-invariant-boundary argument and separates the paper's biologically central disease-persistence conclusion from the stronger all-compartment claim. It also supplies the exact missing endpoint condition for the failed strict-inflow step without overclaiming a complete repaired theorem.

## Closest literature and limitations
The closest source is the article itself and its Supplementary Section S1.5, because that is where the stronger persistence claim and its proof occur. Generic persistence theory cannot restore the conclusion when an extra invariant boundary set exists. No claim is made here that the disease variables \(I,P\) fail to persist, nor that \(p+v>0\) is sufficient for all other persistence hypotheses.

Self-review: passed. Independent audit: not yet performed.
