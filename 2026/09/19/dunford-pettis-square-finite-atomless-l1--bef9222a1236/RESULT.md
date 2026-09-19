# Exact square separation for Dunford--Pettis ideals on finite measure L1 spaces

## Statement

Let \((\Omega,\Sigma,\lambda)\) be a finite measure space, let
\[
Z=L^1(\lambda),\qquad \mathcal D_Z=\operatorname{DP}(Z),
\]
and define the closed square ideal
\[
\mathcal I_2(Z)=\overline{\operatorname{span}}\{ST:S,T\in\mathcal D_Z\}^{\|\cdot\|}.
\]
Let \(\mathcal G_Z\) denote the ideal of representable operators on \(Z\).

If the measure algebra of \(\lambda\) has a nonzero atomless part, then
\[
\boxed{\mathcal G_Z\subsetneq \mathcal I_2(Z)\subsetneq \mathcal D_Z.}
\]
Moreover, there are a compact perfect strongly independent set \(P\subset\mathbb T\), a contractive linear map
\[
\Theta_Z:\mathcal D_Z\longrightarrow M_0(P),
\]
and an isometric linear map
\[
J_P:M_0(P)\longrightarrow \mathcal D_Z
\]
such that
\[
\Theta_Z\bigl(\mathcal I_2(Z)\bigr)=0,
\qquad
\Theta_ZJ_P=\operatorname{Id}_{M_0(P)}.
\]
Consequently, for every \(\mu\in M_0(P)\),
\[
\boxed{\operatorname{dist}\bigl(J_P\mu,\mathcal I_2(Z)\bigr)=\|\mu\|,}
\]
and \(\mathcal D_Z/\mathcal I_2(Z)\) contains a contractively complemented isometric copy of \(M_0(P)\), hence also a contractively complemented isometric copy of \(L^1[0,1]\).

The boundary is exact among finite measure spaces: if the measure algebra is purely atomic, then \(Z\) has the Schur property, so
\[
\mathcal D_Z=\mathcal B(Z),\qquad \mathcal I_2(Z)=\mathcal B(Z).
\]
Thus
\[
\boxed{\mathcal I_2(Z)\subsetneq\mathcal D_Z
\quad\Longleftrightarrow\quad
\lambda\text{ has a nonzero atomless part}.}
\]

The construction also shows that \(\mathcal I_2(Z)\) is large: it contains an infinite-rank projection onto a complemented copy of \(\ell^1\), and therefore is not contained in the strictly singular operators.

## Context

Nasseri proved the corresponding exact distance formula and strict ideal chain for \(L^1(0,1)\). The same paper extended the approximate-identity obstruction to arbitrary finite measure spaces with a nonzero atomless part, but explicitly noted that the complemented-copy argument does not transfer the square-ideal theorem, because compressing a product introduces operators on the ambient \(L^1\) space. It then asked whether the exact square-ideal separation extends to every nonseparable finite atomless \(L^1\) space.

The point here is that the intermediate ambient operators can still be controlled. The needed statement is a cross-space version of the two-atomless-disintegrations argument.

## Cross-space polar-product lemma

Put \(Y=L^1(\mathbb T,m)\), with normalized Haar measure \(m\). Let \(Z=L^1(\lambda)\) for an arbitrary finite measure space. Let
\[
A:Y\to Z,\qquad B:Z\to Y
\]
be Dunford--Pettis operators. Let \(\sigma:\mathcal B(Y)\to M(\mathbb T)\) be the translation-averaging symbol used for operators on \(Y\). For the strongly independent set \(P\) appearing in Nasseri's theorem,
\[
\boxed{\sigma(BA)|_P=0.}
\]

### Positive case

Assume first that \(A,B\ge0\). Split the finite measure algebra into its atomless and purely atomic bands, so that
\[
Z=Z_c\oplus_1 Z_a,\qquad Z_a\cong\ell^1(I)
\]
for an at most countable index set \(I\). Writing the identity as the sum of the two band projections gives
\[
BA=B P_cA+B P_aA.
\]
The atomic term factors through \(\ell^1\), hence is representable as an operator on \(Y\) by Lewis--Stegall. Its translation-averaging symbol is absolutely continuous with respect to Haar measure, and therefore has zero restriction to \(P\), which is Haar-null. It remains to treat the atomless intermediate band, so below we may assume \(\lambda\) is atomless.

A kernel representation for operators from an \(L^1\) space over a compact metric probability space into an atomless \(L^1\) space gives a measurable family of finite positive measures \((\beta_\omega)_{\omega\in\Omega}\) on \(\mathbb T\) such that
\[
Af(\omega)=\int_{\mathbb T}f(y)\,d\beta_\omega(y)
\]
for continuous \(f\), and hence by density for \(L^1\)-classes in the usual kernel sense.

For \(B\), restrict \(B^*:L^\infty(\mathbb T)\to L^\infty(\lambda)\) to the separable space \(C(\mathbb T)\). After choosing compatible representatives on a countable dense subspace and applying Riesz representation pointwise, one obtains a weak-star measurable family of finite positive measures \((\alpha_\omega)\) such that
\[
B^*g(\omega)=\int_{\mathbb T}g(x)\,d\alpha_\omega(x)
\qquad(g\in C(\mathbb T)).
\]
For \(f,g\in C(\mathbb T)\), Fubini gives
\[
\int g\,BAf\,dm
=
\int_\Omega
\left(\int g\,d\alpha_\omega\right)
\left(\int f\,d\beta_\omega\right)d\lambda(\omega).
\]
Therefore the operator measure of \(BA\) is
\[
\Gamma_{BA}=\int_\Omega \alpha_\omega\otimes\beta_\omega\,d\lambda(\omega),
\]
and its translation-averaging symbol is
\[
\boxed{\sigma(BA)=\int_\Omega \alpha_\omega*\check\beta_\omega\,d\lambda(\omega).}
\]

It remains to show that both kernels are atomless almost everywhere.

Suppose first that \(\beta_\omega\) has an atom on a set of positive \(\lambda\)-measure. The measurable enumeration of atoms of finite measures on a compact metric space yields a positive-measure set \(F\), a measurable map \(\tau:F\to\mathbb T\), and a measurable \(a\ge\varepsilon>0\) on \(F\) such that
\[
a(\omega)\delta_{\tau(\omega)}\le\beta_\omega.
\]
The corresponding positive suboperator
\[
A_0f(\omega)=1_F(\omega)a(\omega)f(\tau(\omega))
\]
satisfies \(0\le A_0\le A\). It is well defined on \(L^1(m)\), because
\[
\eta:=\tau_*(a1_F\lambda)
\]
is absolutely continuous with respect to \(m\): for Borel \(E\),
\[
\eta(E)
\le \int_\Omega\beta_\omega(E)\,d\lambda(\omega)
=\int_E A^*1\,dm.
\]
Dunford--Pettis operators between \(L^1\) spaces form an order ideal among regular operators, so \(A_0\) is Dunford--Pettis. But the standard Rademacher sequence \((r_n)\) is weakly null in \(L^1(m)\), while
\[
\|A_0r_n\|_1=\int_F a\,d\lambda>0,
\]
a contradiction. Hence \(\beta_\omega\) is atomless almost everywhere.

Now suppose \(\alpha_\omega\) has an atom on a positive-measure set. Select \(F,\tau,a\) as above and let \(B_0\) be the positive suboperator determined by
\[
\int_{\mathbb T}g\,B_0h\,dm
=
\int_F a(\omega)h(\omega)g(\tau(\omega))\,d\lambda(\omega).
\]
Again \(0\le B_0\le B\), so \(B_0\) is Dunford--Pettis. The measure
\[
\eta=\tau_*(a1_F\lambda)
\]
is nonzero and satisfies
\[
\eta(E)
\le \int_\Omega\alpha_\omega(E)\,d\lambda(\omega)
=\int_E B1_\Omega\,dm,
\]
so \(\eta\ll m\) and is atomless. Choose a \(\{\pm1\}\)-valued Rademacher sequence \((r_n)\) for the finite atomless measure \(\eta\), and set
\[
h_n(\omega)=1_F(\omega)r_n(\tau(\omega)).
\]
Then \((h_n)\) is weakly null in \(L^1(\lambda)\). Indeed, for \(\phi\in L^\infty(\lambda)\), the pushforward
\[
\lambda_\phi=\tau_*(\phi1_F\lambda)
\]
satisfies \(|\lambda_\phi|\le \varepsilon^{-1}\|\phi\|_\infty\eta\), and hence
\[
\int \phi h_n\,d\lambda=\int r_n\,d\lambda_\phi\to0.
\]
Writing \(q=d\eta/dm\), one has
\[
B_0h_n=qr_n,
\qquad
\|B_0h_n\|_1=\eta(\mathbb T)>0,
\]
again contradicting the Dunford--Pettis property. Thus \(\alpha_\omega\) is atomless almost everywhere.

Nasseri's polar-set lemma for the strongly independent set \(P\) states that if \(\alpha,\beta\) are finite atomless measures on \(\mathbb T\), then
\[
(\alpha*\check\beta)|_P=0.
\]
Applying this almost everywhere in the displayed integral for \(\sigma(BA)\) proves the lemma for positive \(A,B\).

### General case

Every bounded real operator between \(L^1\) spaces is regular, and the Dunford--Pettis operators form an order ideal in the regular-operator lattice when the domain is an AL-space and the range is weakly sequentially complete. Hence a real Dunford--Pettis operator is a linear combination of positive Dunford--Pettis operators. Applying this to real and imaginary parts handles the complex case. Bilinearity then reduces the general pair \((A,B)\) to the positive case above.

## Transfer to an arbitrary finite measure space

Assume now that \(\lambda\) has a nonzero atomless part. Equal-measure bisection inside that part and conditional expectation give contractions
\[
J:Y\to Z,\qquad Q:Z\to Y,
\qquad QJ=I_Y,
\]
with \(J\) isometric, exactly as in Nasseri's finite-measure extension of the approximate-identity obstruction.

Define, for \(T\in\mathcal D_Z\),
\[
\Theta_Z(T)=\sigma(QTJ)|_P.
\]
Since \(QTJ\) is Dunford--Pettis on \(Y\), its symbol is Rajchman; restriction to \(P\) is again Rajchman. Thus \(\Theta_Z\) is a contraction from \(\mathcal D_Z\) to \(M_0(P)\).

If \(S,T\in\mathcal D_Z\), set
\[
A=TJ:Y\to Z,
\qquad
B=QS:Z\to Y.
\]
Both are Dunford--Pettis, and
\[
QSTJ=BA.
\]
The cross-space lemma gives
\[
\Theta_Z(ST)=\sigma(BA)|_P=0.
\]
By linearity and norm closure,
\[
\boxed{\Theta_Z\bigl(\mathcal I_2(Z)\bigr)=0.}
\]
This is precisely the point not supplied by compression alone.

For \(\mu\in M_0(P)\), let \(C_\mu:Y\to Y\) be convolution by \(\mu\), and define
\[
J_P\mu=JC_\mu Q.
\]
Rajchman convolution operators on \(Y\) are Dunford--Pettis, so \(J_P\mu\in\mathcal D_Z\). Also
\[
Q(J_P\mu)J=C_\mu,
\]
and therefore
\[
\|J_P\mu\|=\|C_\mu\|=\|\mu\|.
\]
Because \(\mu\) is supported on \(P\),
\[
\Theta_Z(J_P\mu)=\mu.
\]
Thus, for any \(W\in\mathcal I_2(Z)\),
\[
\|J_P\mu-W\|
\ge \|\Theta_Z(J_P\mu-W)\|
=\|\mu\|.
\]
The reverse inequality follows from \(W=0\), proving
\[
\operatorname{dist}(J_P\mu,\mathcal I_2(Z))=\|\mu\|.
\]
The induced contraction
\[
\widetilde\Theta_Z:\mathcal D_Z/\mathcal I_2(Z)\to M_0(P)
\]
has the isometric right inverse
\[
\mu\mapsto J_P\mu+\mathcal I_2(Z),
\]
so the range is contractively complemented.

## The representable ideal and strictness on the lower side

By the Lewis--Stegall theorem, a representable operator from a finite-measure \(L^1\) space factors through \(\ell^1\). Since the atomless part of \(Z\) contains a contractively complemented copy of \(\ell^1\), choose contractions
\[
U:\ell^1\to Z,\qquad V:Z\to\ell^1,
\qquad VU=I_{\ell^1}.
\]
If \(G\in\mathcal G_Z\) factors as \(G=AB\) through \(\ell^1\), then
\[
G=(AV)(UB).
\]
Both factors again factor through \(\ell^1\), hence are representable and therefore Dunford--Pettis. Thus
\[
\mathcal G_Z\subseteq\mathcal I_2(Z).
\]

Let \(\mu\) be the Rajchman probability supported on \(P\) supplied by Nasseri. Then
\[
(J_P\mu)^2=JC_{\mu^{*2}}Q\in\mathcal I_2(Z).
\]
The measure \(\mu^{*2}\) is singular. If this operator were representable on \(Z\), it would factor through \(\ell^1\); after compression by \(Q\) and \(J\), \(C_{\mu^{*2}}\) would factor through \(\ell^1\), hence be representable on \(Y\). But a convolution operator on \(L^1(\mathbb T)\) is representable exactly when its measure is absolutely continuous with respect to Haar measure. This contradicts singularity. Therefore
\[
\mathcal G_Z\subsetneq\mathcal I_2(Z).
\]
The exact-distance formula already gives
\[
\mathcal I_2(Z)\subsetneq\mathcal D_Z.
\]

Finally, the projection \(UV\) onto the complemented copy of \(\ell^1\) factors through \(\ell^1\), so it belongs to \(\mathcal G_Z\subseteq\mathcal I_2(Z)\). It is not strictly singular, proving largeness.

## Purely atomic boundary

If the finite measure algebra is purely atomic, then \(L^1(\lambda)\) is an \(\ell^1\)-space and has the Schur property. Hence every bounded operator on \(Z\) is Dunford--Pettis, so
\[
\mathcal D_Z=\mathcal B(Z).
\]
Since the identity is in \(\mathcal D_Z\), every \(T\in\mathcal B(Z)\) is itself a product \(T=TI\) of two Dunford--Pettis operators. Therefore
\[
\mathcal I_2(Z)=\mathcal B(Z).
\]
This proves the stated if-and-only-if boundary for properness of the closed square.

## Relation to prior literature

The ingredients taken from prior work are explicit:

1. Nasseri constructs the strongly independent compact perfect set \(P\), the Rajchman probability on \(P\), the translation-averaging symbol \(\sigma\), the polar convolution lemma on \(P\), the characterization of representable convolution operators, and the exact square theorem on \(L^1(0,1)\). The same paper explicitly leaves the nonseparable finite atomless square-separation extension open.
2. After splitting off the purely atomic band, the measure-kernel representation and measurable enumeration of atoms used for \(A:Y\to Z_c\) are classical; a convenient source is Liu's 1998 account of Kalton's representation theorem for operators from \(L^1\) over a compact metric space into an atomless \(L^1\) space.
3. The order-solid behavior of Dunford--Pettis operators between AL-spaces is classical Banach-lattice theory; Kalton--Saab prove the relevant order-ideal result.
4. Representable operators from finite-measure \(L^1\) spaces factor through \(\ell^1\) by the Lewis--Stegall theorem.

The new step is the cross-space polar-product lemma above and its use to make the compression map annihilate the ambient square ideal. This removes the obstruction identified in Nasseri's Remark 6.2 and answers the finite nonseparable atomless extension question.

## Limitations

The result concerns finite measure \(L^1\) spaces. It does not address general infinite or merely localizable measure spaces, higher closed powers \(\overline{\operatorname{span}}\mathcal D_Z^n\) for \(n\ge3\), classification of all closed ideals between \(\mathcal G_Z\) and \(\mathcal D_Z\), or incompressibility. The proof uses the compact-metric circle model inside a complemented separable atomless component; it does not assert a canonical symbol intrinsic to the full ambient measure algebra.

## References

- A. B. Nasseri, *Large ideals in B(L1(0,1))*, arXiv:2609.18348v1 (2026). https://arxiv.org/abs/2609.18348
- Z. Liu, *A decomposition theorem for operators on L1*, Journal of Operator Theory **40** (1998), 3--34. https://www.theta.ro/jot/archive/1998-040-001/1998-040-001-001.pdf
- N. J. Kalton and P. Saab, *Ideal properties of regular operators between Banach lattices*, Illinois Journal of Mathematics **29** (1985), 382--400. https://kaltonmemorial.missouri.edu/assets/docs/illjm1985.pdf
- D. R. Lewis and C. Stegall, *Banach spaces whose duals are isomorphic to l1(Gamma)*, Journal of Functional Analysis **12** (1973), 177--187. https://doi.org/10.1016/0022-1236(73)90022-0
