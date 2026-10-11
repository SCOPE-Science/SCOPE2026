# Steinhaus permanence and its sharp exponent boundary for Banach direct sums

## Finding

**Theorem.** Let \(1<p<\infty\). For any nonempty family \((X_i)_{i\in I}\) of nonzero real Banach spaces, its \(\ell_p\)-sum
\[
E=\Big(\bigoplus_{i\in I} X_i\Big)_p,
\qquad \|x\|_E=\left(\sum_{i\in I}\|x_i\|_{X_i}^{p}\right)^{1/p},
\]
has Steinhaus property \((S)\) exactly when every \(X_i\) has \((S)\). If the family is finite, the same equivalence holds with **uniform property \((S)\)** in place of \((S)\).

These preservation assertions have the sharp universal exponent range \(1<p<\infty\): two one-dimensional summands each possess uniform \((S)\), whereas their \(\ell_1\)- and \(\ell_\infty\)-sums fail even ordinary \((S)\). The theorem does not assert an explicit uniform modulus or a universal direct-sum inequality for such moduli.

## Assumptions and scope

Throughout, scalars are real and the summands are Banach spaces. For a normed space \(X\), write \(S_X=\{x:\|x\|=1\}\). Property \((S)\) means
\[
\forall x,y\in S_X,\ x\ne y,\ \forall a>0,\ \exists h\in X:\quad
\|h\|<a,\quad \|x+h\|\ne\|y+h\|.
\]
The equivalent metric-ball formulation for Banach spaces is the Steinhaus property of Kania--Kochanek, by their Theorem A [1]. Define
\[
U_X(d;a)=\inf_{\substack{x,y\in S_X\\\|x-y\|\ge d}}
\ \sup_{\|h\|\le a}\big|\|x+h\|-\|y+h\|\big|
\qquad(0<d<2,\ a>0).
\]
Uniform property \((S)\) means \(U_X(d;a)>0\) for every such \(d,a\), as in [2]. All assertions concern the norms displayed, not merely isomorphic copies; \(I\) may be arbitrarily large for ordinary \((S)\), but the uniform equivalence asserted here is for **finite** nonempty \(I\).

## Proof

**1. Radial norm-germ lemma.** For every real normed space \(X\), every \(p>1\), and \(u,v\in X\), suppose that
\[
\|u+h\|^p-\|v+h\|^p
\]
is constant for all \(h\) in a neighborhood of zero. Then \(\|u\|=\|v\|\). If in addition \(X\) has \((S)\), then \(u=v\).

Indeed, put \(F_u(h)=\|u+h\|^p\). For every direction \(w\), the one-sided directional derivative \(D^+F_u(0;w)\) exists by convexity. Writing \(r=\|u\|\), the triangle inequality and the radial direction give the exact identity
\[
\sup_{\|w\|\le1}D^+F_u(0;w)=p r^{p-1},
\]
including the case \(r=0\), for which every such derivative is zero. If \(F_u-F_v\) is locally constant, all its directional derivatives vanish, so the displayed suprema agree. Strict monotonicity of the map \(r\mapsto p r^{p-1}\) gives \(\|u\|=\|v\|\). The constant difference then equals zero at the origin; hence \(\|u+h\|=\|v+h\|\) for every sufficiently small \(h\). If their common norm is zero, both vectors vanish. Otherwise, dividing \(u,v,h\) by their common positive norm contradicts \((S)\) unless \(u=v\). This proves the lemma.

**2. Arbitrary-index permanence.** If one summand \(X_j\) fails \((S)\), take distinct unit vectors of \(X_j\) with equal perturbed norms throughout some neighborhood of zero. Regard them as unit vectors of \(E\) supported only at index \(j\). The defining \(p\)-power identity shows that adding any sufficiently small element of \(E\) preserves equality of their norms: the other coordinates contribute the same nonnegative sum. Thus \(E\) fails \((S)\).

Conversely, assume all summands have \((S)\), but \(E\) fails it. There exist distinct \(x,y\in S_E\) and \(a>0\) such that \(\|x+h\|_E=\|y+h\|_E\) for every \(\|h\|_E<a\). Fix any index \(j\) and vary only the \(j\)-th coordinate \(h_j\). Raising the equality to the power \(p\) gives
\[
\|x_j+h_j\|_{X_j}^p-\|y_j+h_j\|_{X_j}^p
=\sum_{i\ne j}(\|y_i\|_{X_i}^p-\|x_i\|_{X_i}^p),
\]
where the right-hand side is independent of \(h_j\). The radial norm-germ lemma gives \(x_j=y_j\). This holds for every \(j\), forcing \(x=y\), a contradiction. The argument is valid for arbitrary index sets because all the sums are absolutely convergent and only one coordinate is varied at a time.

**3. Uniform finite-sum permanence.** For a nonzero Banach space \(X\), uniform \((S)\) implies that every ultrapower \(X^{\mathcal U}\) (relative to a nonprincipal ultrafilter on the positive integers) has ordinary \((S)\). To see this directly, represent two distinct unit vectors of the ultrapower by sequences whose norms tend to one along the ultrafilter. Their coordinatewise distances stay bounded below by some fixed \(d>0\) on an ultrafilter-large set. Normalize those representatives. The positive quantity \(U_X(d;a/2)\) supplies, on each such index, a perturbation of norm at most \(a/2\) separating their norms by a uniform positive amount. Passing to the ultrapower yields a common perturbation of norm less than \(a\) that separates the two limit vectors.

Now let \(I\) be finite and suppose each \(X_i\) has uniform \((S)\). Were \(E\) not uniform \((S)\), for some \(0<d<2\) and \(a>0\) there would be unit pairs \(x^{(n)},y^{(n)}\in E\), separated by at least \(d\), such that every perturbation of norm at most \(a\) separates their norms by less than \(1/n\). In an ultrapower they would define distinct unit vectors with identical norm germs near zero, contradicting \((S)\), since for finite \(I\)
\[
E^{\mathcal U}\cong\Big(\bigoplus_{i\in I}X_i^{\mathcal U}\Big)_p
\]
isometrically and each summand on the right has \((S)\) by the previous paragraph and Step 2.

Conversely, uniform \((S)\) of \(E\) implies that of each coordinate summand. Indeed, if \(u,v\in S_{X_j}\) are embedded as vectors supported at \(j\), and \(h=(h_i)\) is an arbitrary perturbation, write \(t=\sum_{i\ne j}\|h_i\|^p\). The function \(s\mapsto(s^p+t)^{1/p}\) is \(1\)-Lipschitz on the nonnegative real axis, so
\[
\big|\|(u,0)+h\|_E-\|(v,0)+h\|_E\big|
\le \big|\|u+h_j\|-\|v+h_j\|\big|.
\]
Taking suprema over \(\|h\|_E\le a\), with the reverse inequality obtained by setting all other perturbation coordinates to zero, yields the exact pointwise identity
\[
U_E((u,0),(v,0);a)=U_{X_j}(u,v;a).
\]
Consequently \(U_E(d;a)\le U_{X_j}(d;a)\), and positivity of all the left-hand moduli forces that of every summand. This completes the uniform assertion.

**4. Sharp endpoint obstructions.** Both copies of \(\mathbb R\) have uniform \((S)\). In \(\ell_1^2\), the distinct unit points \((1/4,3/4)\) and \((3/4,1/4)\) have the same norm after every common perturbation of \(\ell_1\)-norm less than \(1/4\): both points remain in the positive quadrant, where their coordinate sums are identical. In \(\ell_\infty^2\), the distinct unit points \((1,0)\) and \((1,1/2)\) have the same norm after every common perturbation of \(\ell_\infty\)-norm less than \(1/4\): the first coordinate remains strictly dominant in both vectors. Thus neither endpoint preserves \((S)\) for arbitrary summands.

## Verification

The mathematical verification consists of the four independent checks above: the radial derivative formula for every normed space and every \(p>1\); one-coordinate substitution in the defining absolutely convergent direct sum; ultrapower transfer with finite-index commutation; and explicit endpoint norm-germ witnesses. The displayed endpoint equalities were additionally tested with exact rational arithmetic at a grid of perturbations. Those finite tests merely corroborate the displayed identities; the proofs cover every allowed perturbation and index family. No external or infinite proof certificate is claimed.

## Relationship to prior work

Kania and Kochanek [1, Theorem A] introduced the metric-ball property and its equivalent local norm-germ formulation. They established examples that are not strictly convex [1, Example 3] and showed that atomless real \(L_1\) has \((S)\) [1, Proposition 6]. Their theorem does not state preservation under \(\ell_p\) direct sums. The present result, for example, gives ordinary \((S)\) for the countable atomic-base mixed-norm space \(\ell_p(L_1[0,1])\) whenever \(1<p<\infty\), although that space is not strictly convex.

Johnson and Kania [2] introduced uniform \((S)\), its moduli, and several permanence results; notably their Theorem A treats Bochner \(L_p\) over **atomless** base measures. Their Section 5, Problem (5), asks for a stronger **universal quantitative inequality** involving the moduli of \(X\), \(Y\), and \(\ell_p\) for two-term sums. The present theorem supplies a structural and finite-sum positivity result but **does not prove or imply a universal constant** of the form asked for there. Results about Daugavet constants, roughness, or Banach--Mazur distances for direct sums concern different invariants and do not imply the norm-germ rigidity used here.

## Limitations

The preservation theorem for ordinary \((S)\) is for real Banach spaces and \(1<p<\infty\), and the uniform assertion is restricted to finitely many nonzero summands. No claim is made about uniform \((S)\) for arbitrary infinite sums, about an optimal quantitative separation modulus, or about an absolute-norm direct-sum construction outside the displayed \(\ell_p\) norms. The endpoint examples disprove universal permanence, not permanence for every particular pair of summands. The originality comparison relies on the identified primary sources and indexed searches; unpublished or unindexed equivalent results may exist.

## References

[1] T. Kania and T. Kochanek, *Steinhaus' lattice-point problem for Banach spaces*, arXiv:1302.6443, first public version 26 February 2013, Theorem A, Example 3, Proposition 6. https://arxiv.org/abs/1302.6443

[2] W. B. Johnson and T. Kania, *Uniform Property (S)*, arXiv:2602.09106, first public version 9 February 2026, version 2 dated 15 June 2026, Definitions 1.1--1.2, Theorem A, Section 5 Problem (5). https://arxiv.org/abs/2602.09106
