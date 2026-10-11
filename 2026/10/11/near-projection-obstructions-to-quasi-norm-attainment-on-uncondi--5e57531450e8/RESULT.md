# Near-projection obstructions to quasi norm attainment on unconditional block decompositions

## Finding
Let \(\mathbb K\in\{\mathbb R,\mathbb C\}\). Suppose a Banach space \(X\) over \(\mathbb K\) contains a \(1\)-complemented closed subspace \(Y\) with an infinite \(1\)-unconditional Schauder decomposition into nonzero closed subspaces \((Y_n)_{n\ge1}\). Write \(P:X\to Y\) for a projection of norm \(1\). For every \(0<\varepsilon<1\), put
\[
D_\varepsilon\bigl(\sum_{n\ge1}y_n\bigr)
 =\sum_{n\ge1}\bigl(1-\varepsilon/n\bigr)y_n,
\qquad S_\varepsilon=\iota_Y D_\varepsilon P:X\to X.
\]
Then
\[
\|D_\varepsilon\|=\|S_\varepsilon\|=1,
\quad \|D_\varepsilon-I_Y\|=\|S_\varepsilon-P\|=\varepsilon,
\quad\|D_\varepsilon^{-1}\|=(1-\varepsilon)^{-1}.
\]
The bounded operator \(D_\varepsilon\) is invertible on \(Y\), and its restriction to nonzero vectors is strictly contractive: \(\|D_\varepsilon y\|<\|y\|\). In addition,
\[
S_\varepsilon(B_X)=D_\varepsilon(B_Y)
\quad\text{is norm closed in }X,
\qquad S_\varepsilon(B_X)\cap S_X=\varnothing.
\]
Since the operator norm equals one, this proves \(S_\varepsilon\notin\operatorname{QNA}(X,X)\). Thus \(P\) lies in the norm boundary of \(\operatorname{QNA}(X,X)\), and the presence of such a subspace excludes the equality \(\operatorname{QNA}(X,X)=\mathcal L(X,X)\). For \(Y=X\), the examples are invertible and converge to \(I_X\) in operator norm. The same conclusions hold over both scalar fields.

## Assumptions and scope
A \(1\)-unconditional Schauder decomposition here means that every \(y\in Y\) has a unique norm-convergent expansion \(y=\sum_{n\ge1}y_n\) with \(y_n\in Y_n\), and whenever \((\zeta_n)\) is a bounded scalar sequence satisfying \(|\zeta_n|\le1\), the multiplier \(\sum y_n\mapsto\sum\zeta_ny_n\) is well defined with operator norm at most one. Each \(Y_n\) is required to be nonzero, but may be infinite dimensional and need not possess the approximation property. The projection \(P\) has \(\|P\|=1\) and restricts to the identity on \(Y\). In the definition of quasi norm attainment, \(T\in\operatorname{QNA}(X,X)\) exactly when \(\overline{T(B_X)}\cap\|T\|S_X\ne\varnothing\), with closure in norm.

## Proof
**Diagonal bounds and inverses.** Set \(\lambda_n=1-\varepsilon/n\). As \(1-\varepsilon\le\lambda_n<1\), the defining multiplier property gives \(\|D_\varepsilon\|\le1\). Restriction to a unit vector of \(Y_n\) has norm \(\lambda_n\), and \(\lambda_n\to1\), so \(\|D_\varepsilon\|=1\). Similarly, the diagonal coefficients of \(I_Y-D_\varepsilon\) are \(\varepsilon/n\), so its norm is exactly \(\varepsilon\), with equality on \(Y_1\). The reciprocal multiplier exists because its coefficients are bounded, and multiplying it by \(1-\varepsilon\) gives coefficients in \([0,1]\). The norm-one unconditionality therefore yields
\[
\|D_\varepsilon^{-1}\|\le(1-\varepsilon)^{-1}.
\]
Equality holds on \(Y_1\). Norm convergence of the coordinate expansions proves that these multiplier maps are inverse to each other, so \(D_\varepsilon\) is a Banach-space automorphism.

**The strict-contraction lemma.** For any \(y=\sum_ny_n\in Y\) and \(\phi\in Y^*\) with \(\|\phi\|=1\), the unconditional multiplier property implies
\[
\sum_{n\ge1}|\phi(y_n)|\le\|y\|.
\]
Indeed, for every finite set of indices choose phases on that set to align the values \(\phi(y_n)\), put zero phases elsewhere, and use the contraction property. Take the supremum over finite sets. Now let \(y\ne0\) and choose a supporting functional \(\phi\in S_{Y^*}\) satisfying \(\phi(D_\varepsilon y)=\|D_\varepsilon y\|\), rotating its phase if necessary in the complex case. Since \(D_\varepsilon\) is invertible, the latter scalar is positive, and at least one \(\phi(y_n)\) is nonzero. Thus
\[
\|D_\varepsilon y\|=
 \left|\sum_{n\ge1}\lambda_n\phi(y_n)\right|
 \le\sum_{n\ge1}\lambda_n|\phi(y_n)|
 <\sum_{n\ge1}|\phi(y_n)|\le\|y\|.
\]
The middle inequality is strict because every \(\lambda_n<1\) and at least one scalar summand is nonzero. This proves strict contraction at each nonzero vector although the operator norm is one.

**The projected endomorphism and closed image.** Since \(P\) is contractive and is the identity on \(Y\), restriction to \(Y\) yields
\[
\|S_\varepsilon\|=\|D_\varepsilon\|=1,
\qquad \|S_\varepsilon-P\|=\|D_\varepsilon-I_Y\|=\varepsilon.
\]
Moreover, \(P(B_X)=B_Y\): one inclusion follows from \(\|P\|=1\), the other from \(Y\subseteq X\) and \(P|_Y=I_Y\). Hence \(S_\varepsilon(B_X)=D_\varepsilon(B_Y)\). The latter set is closed in \(Y\), because \(D_\varepsilon\) is a bounded invertible operator and \(B_Y\) is closed; it is closed in \(X\) because \(Y\) is closed. Every point in this image has norm strictly less than one by the strict-contraction lemma, except zero, which also has norm less than one. Therefore its intersection with \(S_X\) is empty. Norm closedness now excludes quasi norm attainment at the norm-one operator \(S_\varepsilon\).

Finally, \(P\) is norm attaining and hence quasi norm attaining, while the non-quasi-norm-attainers \(S_\varepsilon\) converge to it as \(\varepsilon\downarrow0\). Thus \(P\) belongs to the norm boundary of the quasi-norm-attaining subset of \(\mathcal L(X,X)\). When \(P=I_X\), each \(S_\varepsilon=D_\varepsilon\) is invertible. Composing on the left with any surjective linear isometry \(U\) of \(X\) gives further non-quasi-norm-attaining automorphisms at exact distance \(\varepsilon\) from \(U\), because \(\|UD_\varepsilon x\|=\|D_\varepsilon x\|\).

## Verification
All equalities and strict inequalities above follow from the stated unconditionality hypothesis and basic Hahn–Banach supporting functionals; no finite experiment is treated as an infinite proof. Boundary tests: the first block realizes the exact \(\varepsilon\) multiplier norm and exact inverse norm; arbitrarily late blocks give operator norm one; for every fixed nonzero vector, the support-functional sum proves strictness. The argument uses no approximation property or finite-dimensionality of \(Y_n\).

As a concrete test, for every \(1\le p<\infty\), partition \((0,1]\) into \(E_n=(2^{-n},2^{1-n}]\), and on \(L_p[0,1]\) take multiplication by the function equal to \(1-\varepsilon/n\) on \(E_n\). These infinitely many nonzero bands form a \(1\)-unconditional Schauder decomposition, giving a norm-one invertible non-quasi-norm-attaining multiplication operator at exact norm distance \(\varepsilon\) from the identity; this includes the nonreflexive case \(p=1\). More generally, the theorem applies to the corresponding block decompositions of arbitrary \(\ell_p\)- and \(c_0\)-sums of nonzero Banach spaces (with the usual direct-sum norm).

## Relationship to prior work
Choi, Choi, Jung and Martín introduced quasi norm attainment and asked in their Problem 7.11 whether any infinite-dimensional Banach space has every endomorphism quasi norm attaining. Their Proposition 4.3 constructs a non-quasi-norm-attaining operator from an arbitrary infinite-dimensional \(X\) into \(c_0\), while Proposition 4.4 treats operators from \(\ell_1\) into arbitrary infinite-dimensional ranges. Their Lemma 2.1 shows a monomorphism can be quasi norm attaining only if it is norm attaining; the proof here gives a different, explicit **endomorphism** obstruction, including contractively complemented subspaces and exact approach to a prescribed projection. The classical Hilbert-space diagonal \(I-K\) with strictly positive compact diagonal \(K\) is known: no novelty is claimed for this special case. Ostrovskii's earlier necessary condition for universal norm attainment invokes a \(1\)-complemented infinite-dimensional subspace with the approximation property; that condition alone does not state the blockwise formula here or require no approximation property of the blocks. The endomorphism obstruction uses the norm-closed image of the unit ball rather than merely an unattained operator norm.

## Limitations
The result is a sufficient obstruction to universal quasi norm attainment, not a classification of all Banach spaces. Norm-one unconditionality, norm-convergent block expansion, and a contractive projection are essential to the proof; general unconditional decompositions with constant greater than one and infinite \(\ell_\infty\)-products are not covered. The strict-contraction property can fail for infinite \(\ell_\infty\)-products: the all-ones vector already attains the norm of the same coordinate multiplier. The construction does not show that the complement of quasi norm attainment is norm dense throughout the whole operator space, nor does it settle Problem 7.11 for Banach spaces lacking the specified structure. Possible unindexed or informal prior presentation of the abstract blockwise variant remains an originality risk.

## References
1. G. Choi, Y. S. Choi, M. Jung, M. Martín, *On quasi norm attaining operators between Banach spaces*, arXiv:2004.11025v1 (first public version 2020-04-23), especially Definition 1.1, Lemma 2.1, Propositions 4.3–4.4, Problem 7.11, and Remark 7.12; https://arxiv.org/abs/2004.11025 . Version of record: DOI 10.1007/s13398-022-01281-x.
2. M. I. Ostrovskii, *Norm-attaining operators*, Extracta Mathematicae 20 (2005), 65–66, Problem 12.1; see the public transcription at https://mathoverflow.net/questions/232291/ .
3. M. I. Ostrovskii and F. Petrov, comments on the classical Hilbert-space diagonal example, MathOverflow discussion (2016): https://mathoverflow.net/questions/232291/ .
