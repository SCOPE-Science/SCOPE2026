# Kanazawa's flopped gCICY has no fibration over a curve
## Finding
Let \(X_-\) be the general flopped Calabi--Yau threefold in Kanazawa's non-Gorenstein \([3,-1]\) gCICY example. Then
\[
D\in N^1(X_-)_\mathbf Q,\qquad D^2=0\text{ in }N^2(X_-)_\mathbf Q
\]
implies
\[
D=0.
\]
Consequently \(X_-\) admits no nonconstant morphism to a projective curve. Equivalently, it has no surface fibration over a curve; in particular, it has no K3 or abelian-surface fibration by a morphism.

This is a chamber-sensitive contrast: the pre-flop model \(X_+\) has the natural K3 fibration
\[
X_+\longrightarrow \mathbf P^1,
\]
whereas the flopped model \(X_-\) has no morphism at all to a positive-dimensional projective curve.

## Assumptions and scope
Kanazawa works over \(\mathbf C\) and proves the assertions below for general defining data. The two smooth projective Calabi--Yau threefolds \(X_+\) and \(X_-\) are related by the simultaneous Atiyah flop of \(16\) disjoint \((-1,-1)\)-curves.

For \(X_-\), Kanazawa proves
\[
\operatorname{Pic}(X_-)/\operatorname{tors}
\simeq
\mathbf Z H_-\oplus\mathbf Z F_-
\]
and computes
\[
H_-^3=7,\qquad H_-^2F_-=8,\qquad H_-F_-^2=4,\qquad F_-^3=0.
\]
Thus every rational numerical divisor class can be written
\[
D=aH_-+bF_-,\qquad a,b\in\mathbf Q.
\]

The conclusion concerns morphisms from \(X_-\) to projective curves. It does not rule out rational maps with indeterminacy, fibrations after further birational modification, or the genus-one fibration \(X_-\to\mathbf P^2\) whose base has dimension \(2\).

## Proof
Write
\[
D=aH_-+bF_-.
\]
If \(D^2=0\) numerically, then intersecting with the basis divisors \(F_-\) and \(H_-\) gives
\[
0=D^2F_-
 =8a^2+8ab
 =8a(a+b)
\]
and
\[
0=D^2H_-
 =7a^2+16ab+4b^2.
\]

The first equation has two cases. If \(a=0\), then the second equation becomes
\[
4b^2=0,
\]
so \(b=0\). If \(a+b=0\), so that \(b=-a\), then the second equation becomes
\[
(7-16+4)a^2=-5a^2=0,
\]
so again \(a=b=0\). Therefore
\[
D^2=0\quad\Longrightarrow\quad D=0
\]
in \(N^1(X_-)_\mathbf Q\).

Now suppose that a nonconstant morphism
\[
f:X_-\longrightarrow C
\]
to a projective curve existed. Passing to the Stein factorization and normalizing the curve if necessary, it is enough to consider a surjective morphism with connected fibers onto a smooth projective curve. Choose an ample divisor \(A\) of positive degree on \(C\) and put
\[
D=f^*A.
\]
Because the base has dimension \(1\),
\[
D^2=f^*(A^2)=0.
\]
The class \(D\) is nevertheless nonzero: for any ample divisor \(L\) on \(X_-\), a general fiber surface \(S\) of \(f\) satisfies
\[
D\cdot L^2=\deg(A)\,(L|_S)^2>0.
\]
This contradicts the square-zero calculation above. Hence no such morphism exists.

Kanazawa also proves directly that \(X_+\to\mathbf P^1\) is a K3 fibration, so the absence of every curve-base morphism on \(X_-\) is a genuine difference between the two birational chambers.

## Verification
The numerical input was checked in the full text of Kanazawa's companion paper on the non-Gorenstein example. Proposition 2.7 gives the four cubic intersection numbers on \(X_-\), Proposition 2.8 gives the integral Picard basis modulo torsion, and the same section records the rational even cohomology ring
\[
\mathbf Q[H_-,F_-]/
\bigl(4H_-^2-8H_-F_-+9F_-^2,\ F_-^3\bigr).
\]
The displayed two-equation calculation independently reconstructs the needed consequence: there is no nonzero rational divisor class whose square is numerically zero.

The K3 comparison was checked both in the companion paper, where the projection \(X_+\to\mathbf P^1\) is described explicitly, and in Kanazawa's general \([3,-1]\)-block paper, Proposition 3.9. The latter also describes the natural genus-one fibration on the minus phase and, for the non-Gorenstein example, notes that the minus phase has a single genus-one fibration of index \(4\). That statement concerns curve fibers over a surface and is distinct from the present obstruction to surface fibers over a curve.

No finite experiment or unproved classification is used. The only general geometric input after the intersection calculation is that the pullback of a divisor from a curve has square zero.

## Relationship to prior work
Kanazawa computes the Picard group, cubic form, and genus-one fibration of \(X_-\), and explicitly exhibits the K3 fibration of \(X_+\). The papers do not state the global consequence that \(X_-\) has no nonconstant morphism to any projective curve.

The companion general paper compares natural K3 and genus-one fibrations across \([3,-1]\) phases and states that the non-Gorenstein minus phase has a single genus-one fibration of index \(4\). This does not imply the present result: a genus-one fibration has a two-dimensional base, while the present theorem excludes every one-dimensional base by ruling out all nonzero square-zero divisor classes.

Earlier gCICY literature develops examples with K3 and elliptic fibrations and treats the generalized complete-intersection construction itself, but it predates the specific flopped model \(X_-\) and does not supply this chamber-specific square-zero obstruction.

## Limitations
The result is numerical and morphism-theoretic. It does not determine the full nef or movable cone, and it does not exclude rational maps to curves that become morphisms only after modifying \(X_-\).

The argument uses the Picard-rank-two intersection form of this specific non-Gorenstein example. It is not asserted for arbitrary gCICY flops or for the other \([3,-1]\) configurations in Kanazawa's classification.

## References
A. Kanazawa, “Mirror symmetry for gCICY threefolds (I): a \([3,-1]\) block and a non-Gorenstein toric phase,” arXiv:2610.03719v1, first public 2026-10-02; especially Theorem 1.1 and Propositions 2.7 and 2.8.

A. Kanazawa, “Mirror symmetry for gCICY threefolds (II): \([3,-1]\) blocks, VGIT, and toric phases,” arXiv:2610.03688v1, first public 2026-10-02; especially Proposition 3.9 and the fibration comparison in the introduction.

A. Garbagnati and B. van Geemen, “A remark on generalized complete intersections,” arXiv:1708.00517.

P. Berglund and T. Hübsch, “On Calabi--Yau generalized complete intersections from Hirzebruch varieties and novel K3-fibrations,” arXiv:1606.07420.
