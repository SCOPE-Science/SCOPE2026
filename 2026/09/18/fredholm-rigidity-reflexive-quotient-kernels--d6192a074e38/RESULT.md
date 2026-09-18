# Fredholm rigidity transfers from reflexive quotients to kernels in \(\ell_\infty\)

## Result

Let \(M,N\subseteq \ell_\infty\) be closed subspaces such that
\[
X=\ell_\infty/M,\qquad Y=\ell_\infty/N
\]
are infinite-dimensional reflexive Banach spaces. If \(M\) and \(N\) are Fredholm equivalent, then \(X\) and \(Y\) are Fredholm equivalent.

Equivalently, within the class of closed subspaces of \(\ell_\infty\) having infinite-dimensional reflexive quotient, the Fredholm-equivalence class of the quotient is an invariant of the Fredholm-equivalence class of the subspace.

Here two Banach spaces are Fredholm equivalent when there is a Fredholm operator between them. Equivalently,
\[
E\sim_F F
\quad\Longleftrightarrow\quad
E\oplus G\cong F\oplus H
\]
for some finite-dimensional Banach spaces \(G,H\).

## Proof

Assume that \(U:M\to N\) is Fredholm. Put
\[
K=\ker U,\qquad R=\operatorname{ran}U.
\]
Then \(K\) is finite-dimensional, \(R\) is closed and of finite codimension in \(N\), and one may choose a closed complement
\[
M=M_0\oplus K.
\]
The restriction
\[
U_0=U|_{M_0}:M_0\longrightarrow R
\]
is an isomorphism.

The quotients by the finite-codimensional reductions remain reflexive and infinite-dimensional. Indeed, the canonical map
\[
\ell_\infty/M_0\longrightarrow \ell_\infty/M
\]
is surjective with finite-dimensional kernel \(M/M_0\cong K\), while
\[
\ell_\infty/R\longrightarrow \ell_\infty/N
\]
is surjective with finite-dimensional kernel \(N/R\). Hence both \(\ell_\infty/M_0\) and \(\ell_\infty/R\) are finite-dimensional extensions of \(X\) and \(Y\), respectively, and therefore are infinite-dimensional and reflexive.

The Lindenstrauss--Rosenthal extension theorem now applies to the isomorphism \(U_0:M_0\to R\): since the two ambient quotients are infinite-dimensional and reflexive, \(U_0\) has a Fredholm extension
\[
\widehat U:\ell_\infty\longrightarrow \ell_\infty.
\]
Because \(\widehat U(M_0)=R\), it induces
\[
\widetilde U:\ell_\infty/M_0\longrightarrow\ell_\infty/R,
\qquad
\widetilde U(x+M_0)=\widehat Ux+R.
\]
This induced operator is Fredholm. To see this directly, if \(\widehat Ux\in R\), choose \(m\in M_0\) with \(\widehat Um=\widehat Ux\). Then \(x-m\in\ker\widehat U\), so
\[
\ker\widetilde U
\cong
\ker\widehat U/(\ker\widehat U\cap M_0),
\]
which is finite-dimensional. Moreover,
\[
\operatorname{coker}\widetilde U
\cong
\ell_\infty/(\operatorname{ran}\widehat U+R),
\]
and this is finite-dimensional because \(\operatorname{ran}\widehat U\) is closed and finite-codimensional in \(\ell_\infty\). Thus
\[
\ell_\infty/M_0\sim_F\ell_\infty/R.
\]

Finally, the canonical quotient maps
\[
\ell_\infty/M_0\twoheadrightarrow X,
\qquad
\ell_\infty/R\twoheadrightarrow Y
\]
are Fredholm, since their kernels are finite-dimensional. Fredholm equivalence is an equivalence relation, so
\[
X\sim_FY.
\]
This proves the claim. \(\square\)

## Stable strengthening of the González--Kania construction

González and Kania construct, for every infinite \(A\subseteq[a,b]\subset(1,2)\) with a fixed \(1<s<a\), a reflexive space
\[
X_A=
\left(\bigoplus_{q\in A}\ell_{q'}\right)_{\ell_{s'}}
\]
and a quotient map
\[
Q_A:\ell_\infty\twoheadrightarrow X_A
\]
whose kernel contains the canonical copy of \(c_0\). They prove that the spaces \(X_A\) are pairwise Fredholm inequivalent for distinct \(A\), and their Proposition 2.2 uses the Lindenstrauss--Rosenthal theorem to conclude only that the kernels \(\ker Q_A\) are pairwise non-isomorphic Grothendieck spaces.

Applying the theorem above to those same kernels gives the stronger conclusion
\[
\boxed{
A\neq B
\quad\Longrightarrow\quad
\ker Q_A\not\sim_F\ker Q_B.
}
\]
Therefore \(\ell_\infty\) contains
\[
\boxed{2^{\mathfrak c}}
\]
pairwise Fredholm-inequivalent non-reflexive Grothendieck subspaces, all containing the canonical \(c_0\), and all having infinite-dimensional reflexive quotient.

Using the standard stable formulation of Fredholm equivalence, these spaces remain distinct after arbitrary finite-dimensional stabilization:
\[
A\neq B
\quad\Longrightarrow\quad
(\ker Q_A)\oplus F\not\cong(\ker Q_B)\oplus G
\]
for every pair of finite-dimensional Banach spaces \(F,G\).

The cardinal \(2^{\mathfrak c}\) is maximal: \(|\ell_\infty|=\mathfrak c\), so \(\ell_\infty\) has at most \(2^{\mathfrak c}\) subsets and hence at most \(2^{\mathfrak c}\) closed subspaces.

## Why the strengthening is not automatic from non-isomorphism

Fredholm equivalence is strictly weaker than isomorphism in general: it allows finite-dimensional kernels and cokernels, or equivalently finite-dimensional stabilization. Thus pairwise non-isomorphism does not by itself imply pairwise Fredholm inequivalence. The extra step is the finite-codimensional reduction of a hypothetical Fredholm map between the kernels, followed by a second use of the Lindenstrauss--Rosenthal extension theorem.

The argument can be summarized as the stable transfer principle
\[
M\sim_F N
\quad\Longrightarrow\quad
\ell_\infty/M\sim_F\ell_\infty/N
\]
whenever both quotients are infinite-dimensional and reflexive.

## Relation to the recent literature

The current version of González--Kania, arXiv:2609.20170v1, states:

- Theorem A: \(2^{\mathfrak c}\) pairwise non-isomorphic Grothendieck subspaces of \(\ell_\infty\), with the stated \(c_0\)-containment and reflexive quotient properties;
- Theorem B: \(2^{\mathfrak c}\) pairwise Fredholm-inequivalent infinite-dimensional reflexive quotients of \(\ell_\infty/c_0\);
- Proposition 2.2: pairwise Fredholm-inequivalent reflexive quotient targets yield pairwise non-isomorphic kernels.

The theorem proved here upgrades precisely the last transfer step from isomorphism rigidity to Fredholm rigidity. It uses the same classical Lindenstrauss--Rosenthal extension theorem, but after first reducing a hypothetical Fredholm map between kernels to an isomorphism between finite-codimensional subspaces.

## Limitations and originality boundary

Originality is claimed only to the best of our knowledge. The finite-codimensional transfer mechanism is built from classical Fredholm facts and the Lindenstrauss--Rosenthal extension theorem; those ingredients are not new. The new claim is restricted to the explicit stable transfer statement above and, in particular, the resulting strengthening of the 2026 González--Kania family from pairwise non-isomorphic to pairwise Fredholm-inequivalent Grothendieck subspaces.

The 1969 Lindenstrauss--Rosenthal paper and the corresponding treatment in Lindenstrauss--Tzafriri were not inspected in full text here. They are the sources most plausibly capable of containing the stable transfer statement in equivalent language. The current González--Kania paper gives the exact extension theorem needed and states only the weaker kernel conclusion. Targeted searches for Fredholm-equivalent kernels, stable-isomorphism versions of the theorem, and pairwise Fredholm-inequivalent Grothendieck subspaces did not locate a prior matching statement.

No assertion is made that the converse transfer implication holds. The proof is specific to the extension rigidity of subspaces of \(\ell_\infty\); it is not a general theorem for arbitrary ambient Banach spaces.

## References

1. M. González and T. Kania, *Grothendieck and \(\ell_\infty\)-Grothendieck subspaces of \(\ell_\infty\)*, arXiv:2609.20170v1 (2026), accepted for publication in *Mathematische Nachrichten*. https://arxiv.org/abs/2609.20170
2. J. Lindenstrauss and H. P. Rosenthal, *Automorphisms in \(c_0\), \(\ell_1\) and \(m\)*, Israel J. Math. 7 (1969), 227--239. https://doi.org/10.1007/BF02787616
3. J. Lindenstrauss and L. Tzafriri, *Classical Banach Spaces I and II: Sequence Spaces and Function Spaces*, Springer, 1996.
