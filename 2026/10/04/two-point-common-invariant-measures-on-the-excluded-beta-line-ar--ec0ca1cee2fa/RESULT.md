# Two-point common invariant measures on the excluded beta line are fixed-point mixtures
## Finding
Let \(\beta>1\) be irrational and let \(\gamma>1\) be distinct from \(\beta\). Assume
\[
\frac{\gamma-1}{\beta-1}=\frac{m}{n}\in\mathbb{Q}_{>0},\qquad \gcd(m,n)=1.
\]
For \(b>1\), write \(T_b(x)=b x-\lfloor b x\rfloor\) on \([0,1)\). If a Borel probability measure \(\mu\) is invariant under both \(T_\beta\) and \(T_\gamma\) and \(|\operatorname{supp}\mu|\le 2\), then
\[
\operatorname{supp}\mu\subseteq F:=\left\{\frac{n\ell}{\beta-1}:\ell\in\mathbb{Z}_{\ge 0},\ n\ell<\beta-1\right\}.
\]
Consequently, every common invariant probability with exactly two support points is
\[
\mu=t\delta_x+(1-t)\delta_y,
\]
where \(x,y\in F\), \(x\ne y\), and \(0<t<1\). Conversely, every such measure is common invariant. Thus a two-point support cannot realize the nontrivial-permutation possibility left open by the fixed-point classification.

## Assumptions and scope
The bases are distinct, \(\beta\) is irrational, and the ratio of their distances from one is a positive rational number in lowest terms. The claim concerns only common invariant probability measures with support of cardinality at most two. It makes no claim about common invariant measures supported on three or more points, or about nonatomic singular measures on the excluded relation.

A finite-support invariant probability for a deterministic map has its support mapped bijectively onto itself: every support point maps to a support point, and invariance supplies a support preimage for every support point. Hence, on a two-point support \(S=\{x,y\}\), each map restricts either to the identity or to the transposition.

## Proof
If \(|S|=1\), its unique point is fixed by both maps, so the conclusion follows from the common fixed-point calculation recalled below. Assume now that \(S=\{x,y\}\) with \(x\ne y\).

Suppose first that \(T_\beta\) transposes \(x\) and \(y\). With
\[
d=\lfloor\beta x\rfloor,\qquad e=\lfloor\beta y\rfloor,
\]
the equations \(T_\beta x=y\) and \(T_\beta y=x\) imply
\[
(\beta+1)(x-y)=d-e\in\mathbb{Z}\setminus\{0\}.
\]
If \(T_\gamma\) also transposes the two points, the same calculation gives \((\gamma+1)(x-y)\in\mathbb{Z}\setminus\{0\}\). Therefore \((\gamma+1)/(\beta+1)\in\mathbb{Q}\). But
\[
\gamma+1=\frac{m}{n}\beta+2-\frac{m}{n}.
\]
If \(\gamma+1=q(\beta+1)\) for \(q\in\mathbb{Q}\), irrationality of \(\beta\) forces both rational coefficients to agree: \(q=m/n\) and \(q=2-m/n\). Hence \(m=n\), which would give \(\gamma=\beta\), contrary to the distinctness assumption. Thus the two maps cannot both transpose \(S\).

If instead \(T_\gamma\) fixes both points, then \((\gamma-1)(x-y)\in\mathbb{Z}\setminus\{0\}\), while the transposition relation above gives \((\beta+1)(x-y)\in\mathbb{Z}\setminus\{0\}\). Hence \((\gamma-1)/(\beta+1)\in\mathbb{Q}\). Using \(\gamma-1=(m/n)(\beta-1)\), a rational identity
\[
\frac{m}{n}(\beta-1)=q(\beta+1)
\]
would force simultaneously \(q=m/n\) and \(q=-m/n\), impossible because \(m>0\). Therefore \(T_\beta\) cannot transpose \(S\).

By symmetry of the remaining case, if \(T_\beta\) fixes both points while \(T_\gamma\) transposes them, then both \((\beta-1)(x-y)\) and \((\gamma+1)(x-y)\) are nonzero integers, so \((\gamma+1)/(\beta-1)\in\mathbb{Q}\). A rational identity \(\gamma+1=q(\beta-1)\), together with the displayed affine formula for \(\gamma+1\), would force \(q=m/n\) and \(-q=2-m/n\), which gives \(0=2\), again impossible.

Thus neither map can transpose a two-point common invariant support. Both maps fix \(x\) and \(y\) individually. A point \(z\in[0,1)\) is fixed by \(T_b\) exactly when \((b-1)z\in\mathbb{Z}_{\ge 0}\). Under \(\gamma-1=(m/n)(\beta-1)\) with \(m,n\) coprime, the simultaneous condition is
\[
z=\frac{n\ell}{\beta-1},\qquad \ell\in\mathbb{Z}_{\ge0},\qquad n\ell<\beta-1.
\]
This is precisely \(F\). Every probability supported on \(F\) is fixed pointwise by both transformations, proving the converse as well.

## Verification
The proof uses only finite-support invariance, integer digit identities, irrationality of \(\beta\), and the reduced rational relation between \(\gamma-1\) and \(\beta-1\). The three possible cases involving a transposition were checked separately: transposition/transposition, transposition/fixing, and fixing/transposition. Each would force an affine rational identity in the irrational number \(\beta\), and coefficient comparison gives a contradiction.

The common fixed-point formula agrees with Proposition 5.1 of arXiv:2609.31156v1. No numerical experiment or unproved exhaustion is used.

## Relationship to prior work
Hang Zhao, arXiv:2609.31156v1, classifies common invariant probabilities away from the relation \((\gamma-1)/(\beta-1)\in\mathbb{Q}\). On that excluded relation, Proposition 5.1 classifies the common fixed points. The subsequent discussion explicitly notes that this does not classify all common atomic measures because a finite support could, in principle, carry nontrivial permutations, and it asks which finite sets can carry a common invariant probability. The present result resolves the first nontrivial support cardinality: cardinality two permits no such permutation at all.

Yan Huang and Zhiqiang Wang, arXiv:2501.08116, classify coincidence of the absolutely continuous Rényi–Parry measures; their result does not classify finite atomic common invariant measures. Karma Dajani and Niels Langeveld, arXiv:2603.12877v1, study coincident absolutely continuous invariant measures for alternate-base transformations, again a different measure class and dynamical object.

## Limitations
The argument is sharp only at support cardinality two. For three or more points, the two maps may induce different permutations with cycles of length greater than two, and the simple sum/difference obstruction used here no longer classifies all possibilities. The result also does not address nonatomic singular common invariant measures on the excluded relation.

## References
1. Hang Zhao, “Common invariant measures for beta-transformations with rational affine relations,” arXiv:2609.31156v1, 25 September 2026. See Proposition 5.1 and Section 5.
2. Yan Huang and Zhiqiang Wang, “The coincidence of Rényi–Parry measures for beta-transformation,” arXiv:2501.08116, first posted 14 January 2025.
3. Karma Dajani and Niels Langeveld, “Coincidence of invariant measure for the alternate base transformations,” arXiv:2603.12877v1, first posted 13 March 2026.
