# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof reduces a nontrivial strongly clean decomposition modulo the Jacobson radical. In the only two mixed diagonal cases, the residue matrix is idempotent. If \(p,e\) are commuting idempotents and \(p-e\) is invertible, then
\[
(p-e)(p+e-1)=0,
\]
forcing \(e=1-p\). This fixes the residue of the idempotent in the strong clean decomposition.

The relevant image or kernel of that idempotent is then a rank-one free module over the local ring. Its residue line contains a vector with second coordinate \(1\), so a basis vector can be normalized to \((t,1)^T\). Invariance under the triangular matrix yields
\[
at+b=tc.
\]
That equation constructs an upper triangular commuting idempotent directly. In each case the difference from the original matrix has unit diagonal, and hence is invertible in the triangular ring.

The proof was checked for multiplication order in the noncommutative case; no commutativity is used.

## Originality

**PASS, to the best of our knowledge.** Borooah--Diesl--Dorsey explicitly formulate the elementwise descent question as Problem 49, primarily for local rings, and the ring-level implication as Problem 48. Their 2007 work treats strong cleanness criteria for triangular matrix rings. Yang--Zhou characterize the ring-level property for \(M_2(R)\) over general local rings, while Tang--Zhou give triangular embedding/similarity results under a bleaching condition.

Targeted searches for the exact elementwise implication
\[
A\in T_2(R),\ A\text{ strongly clean in }M_2(R)
\Longrightarrow
A\text{ strongly clean in }T_2(R)
\]
and synonymous formulations did not locate a prior statement for arbitrary local rings.

Residual risk remains because the full texts of Yang--Zhou (2008) and Tang--Zhou (2017) were not inspected; accessible abstracts and bibliographic metadata were checked. An unstated equivalent corollary in those or older local-ring literature cannot be excluded.

## Value

**PASS.** The theorem answers the first nontrivial matrix size of a clearly stated open problem, and does so without the extra commutativity or bleaching hypotheses present in important neighboring results. The proof also isolates a compact mechanism: residue-level uniqueness of the commuting idempotent forces a rank-one invariant graph whose defining equation produces a triangular idempotent.

## Limitations

The argument does not address \(n\ge3\), where the invariant summands need not be rank one and a single graph equation no longer captures the required triangularization.
