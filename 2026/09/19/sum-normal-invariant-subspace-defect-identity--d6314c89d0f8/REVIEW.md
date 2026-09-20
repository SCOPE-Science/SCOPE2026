# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The central identity was checked directly from the \(2\times2\) block decomposition
\[
T_j=\begin{pmatrix}A_j&X_j\\0&B_j\end{pmatrix}
\]
associated with a joint invariant subspace.  Its upper-left self-commutator block is
\[
[A_j^*,A_j]-X_jX_j^*,
\]
so
\[
D_{\bf A}=P_{\mathcal M}D_{\bf T}|_{\mathcal M}+\sum_jX_jX_j^*.
\]
All conclusions follow from positivity.  In particular, when \(D_{\bf T}=0\), the restriction defect is exactly the positive leakage operator \(\sum_jX_jX_j^*\); it vanishes exactly when every \(X_j\) vanishes, equivalently when the invariant subspace is reducing.

The counterexample was checked in the one-variable and arbitrary-\(d\) forms.  Multiplication by \(z\) on \(L^2(\mathbb T)\) is unitary.  Its invariant Hardy subspace \(H^2\) is not reducing, its restriction is the unilateral shift \(S\), and
\([S^*,S]=P_{\mathbf 1}\ne0\).  Appending zero coordinates gives the same counterexample for every \(d\ge1\).

The finite-dimensional corollary uses only that a positive finite-dimensional operator with zero trace is zero.  Since the trace of every finite-dimensional commutator vanishes, a finite-dimensional invariant restriction of a sum-normal tuple has zero defect and is therefore reducing.

The current full text of arXiv:2609.19287v1 was inspected.  Remark 1.2(b) explicitly asserts sum-normal inheritance for every invariant subspace.  The paper's later equation (3.3) instead gives exactly the positive leakage identity in the sum-normal case, and Remark 3.1 states the compatible reducing-subspace criterion.  Remark 3.4 explicitly invokes Remark 1.2(b) to make invariant restrictions sum-normal before applying Theorem 2.1.  That invocation is therefore invalid.  Theorem 2.2 has a separate proof and is not affected by this correction.

## Originality

The novelty claim is deliberately narrow.  It does not claim that the bilateral-shift example, block-operator multiplication, or the general fact that normal operators may have nonnormal invariant restrictions is new.  Those are classical.

The inspected arXiv version is v1, submitted 16 September 2026, and the current arXiv full text still contains the disputed sentence.  Searches for the arXiv identifier together with “Remark 1.2”, “sum-normal”, “invariant subspace”, “correction”, and synonymous formulations did not locate a public correction.  Internal SCOPE records were also checked by the mathematical object and claim family and no overlap was found.

The claimed contribution is the paper-specific correction and its sharp formulation: the exact defect-transfer identity, the iff boundary between sum-normal restriction and reducingness, the all-\(d\) counterexample, and the identification of Remark 3.4 as the downstream argument that relies on the false inheritance step.

No inaccessible paper was identified as a plausible source that would overturn this paper-specific originality claim.  Older literature certainly contains equivalent block-matrix identities in one form or another; that possibility does not affect the correction itself and is why the elementary identity is not presented as a new general theorem of operator theory.

## Value

Remark 1.2(b) is a basic structural assertion used later in the same paper.  Replacing it by the exact formula prevents a common but consequential confusion between invariant and reducing subspaces.  The correction also delineates impact: the auxiliary triangular-chain argument in Remark 3.4 fails as written, whereas the main compact decomposition theorem remains supported by its independent proof.

The finite-dimensional invariant-subspace corollary supplies a clean positive replacement, complementary to the paper's finite-codimensional theorem.

## Scope and limitations

This record does not resolve whether every sum-normal tuple is normal and does not address the compact quasinilpotent open problem.  It does not claim any of Theorems 2.1--2.4 are false.  Its target is the blanket inheritance assertion in Remark 1.2(b) and the auxiliary reasoning in Remark 3.4 that uses it.

Originality is to the best of our knowledge.
