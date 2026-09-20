# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof was checked at the points where extending the two-fold argument could fail.

For arbitrary commutative artinian base R, the cyclic r-fold matrix algebra is self-injective. The functional obtained by summing evaluation at 1 over the r dual-bimodule entries gives a nondegenerate right pairing: varying a single dual entry in the second factor detects one diagonal coordinate, and varying a single diagonal coordinate detects one dual coordinate. The induced map from the regular right module to its Matlis dual is therefore injective and, by equality of finite R-lengths, an isomorphism.

For every r >= 2 and first-layer idempotent e, the corner and row identities are exactly
\[
eT_r(\Lambda)e=\Lambda,
\qquad
{}_{\Lambda}eT_r(\Lambda)\cong\Lambda\oplus D\Lambda.
\]
No additional summands appear. Thus the Tor calculation in Enomoto's Proposition 2.4 is unchanged: Ext^i_\Lambda(X,\Lambda)=0 implies Tor_i^\Lambda(X,D\Lambda)=0 by the exact duality D, hence Tor_i^\Lambda(X,eT_r(\Lambda))=0.

Enomoto's Lemma 2.1 is an arbitrary-idempotent statement rather than a special property of T_2. Applying it to T_r gives
\[
Ext^n_{T_r(\Lambda)}(F_rX,F_rY)\cong Ext^n_\Lambda(X,Y)
\]
under the same Tor hypothesis, while induction reflects projectivity. Therefore an ARC counterexample over \(\Lambda\) induces a TC2 counterexample over \(T_r(\Lambda)\), proving the contrapositive as well as the stated implication.

For the field case, the Nakayama-period claim was checked modulo the square-zero off-diagonal ideal I. The standard cyclic Nakayama automorphism induces an r-cycle on the factors of \(A^r=T_r(A)/I\). If a proper positive power were inner, its quotient action would be inner and hence fix the center pointwise, contradicting movement of the factor idempotents. Thus its outer order is exactly r. For basic A, the same shift sends each primitive idempotent through an r-cycle, so the Nakayama permutation has only r-cycles.

The equivalence with the restricted basic self-injective class uses Morita invariance of ARC and the fact that a basic representative B has T_r(B) basic self-injective with precisely that Nakayama cycle type.

## Originality

**PASS, to the best of our knowledge.** Enomoto's arXiv:2609.19172v1 was inspected directly at the arbitrary-idempotent Ext lemma, the two-fold trivial-extension Tor calculation, and Theorem 3.1. It states the reduction only for T_2. Chan--Darpö--Iyama--Marczinzik were inspected directly at their definition of T_r(A): they record the r-by-r matrix form, self-injectivity, and cyclic Nakayama automorphism. Those structural facts are prior art.

Targeted searches combining Tachikawa/TC2, Auslander--Reiten, r-fold trivial extension, Nakayama automorphism, Nakayama permutation, and fixed cycle length did not locate the theorem that TC2 for T_r(\Lambda) implies ARC for \(\Lambda\) for every r >= 2, nor the consequence that each prescribed nontrivial Nakayama cycle length is individually universal-hard.

No specific inaccessible source produced concrete evidence of prior coverage. The main residual risks are terminological and contemporaneous: older work on repetitive/orbit algebras could phrase the same cyclic construction differently, and Enomoto's preprint is very recent, so an independent follow-up may not yet be indexed. The originality claim is explicitly limited to the best of our knowledge.

## Value

**PASS.** The result changes the interpretation of Enomoto's reduction. The choice r=2 is not essential: every cyclic cover length r >= 2 carries the same ARC-detecting induced modules. This gives an infinite family of sharply restricted TC2 test classes, one for each Nakayama cycle length. In particular, fixing any nontrivial finite Nakayama cycle length does not reduce the universal difficulty of TC2: that single cycle type already suffices to recover universal ARC.

The result also extends the individual-algebra reduction over a general commutative artinian base, not only over fields, while the field case identifies a concrete representation-theoretic invariant of the witness class. Contrapositively, one ARC counterexample would propagate to TC2 counterexamples at every exact nontrivial finite Nakayama outer period, giving a uniform obstruction across all such strata. The r=1 symmetric case remains outside the argument, which sharply locates the boundary of this mechanism.

## Review status

No independent validation, formal verification, expert attestation, or journal peer review is asserted.
