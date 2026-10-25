# No finite basis test certifies collective limitedness

## Finding

For every finite family of orthonormal bases \(\mathcal B^{(1)},\ldots,\mathcal B^{(m)}\) of the real Hilbert space \(\ell_2\), there is a uniformly bounded sequence of rank-one operators \(T_n:\ell_2	o c_0\) such that each tested union \(igcup_{n,k}T_n b_k^{(j)}\) is relatively compact, while \(igcup_n T_n(B_{\ell_2})\) is not limited. Thus no finite list of orthonormal-basis tests certifies collective limitedness, even for rank-one operators.

More explicitly, one can choose unit vectors \(u_n\in\ell_2\) with
\[
\max_{1\le j\le m}\sup_{b\in\mathcal B^{(j)}}|\langle b,u_n\rangle|\longrightarrow0,
\]
and then set \(T_nx=\langle x,u_n\rangle e_n\), where \((e_n)\) is the standard unit sequence in \(c_0\).

## Assumptions and scope

The tested list of bases is finite and fixed in advance. The Hilbert domain is the real separable space \(\ell_2\); the codomain is \(c_0\) with its supremum norm. A set \(A\subset Y\) is limited when every weak-star-null sequence \((f_r)\subset Y^*\) satisfies \(\sup_{a\in A}|f_r(a)|\to0\). Relatively compact sets are limited.

## Proof

**Simultaneous small-coordinate lemma.** Fix \(\varepsilon>0\). Write the finitely many bases as \(\mathcal B^{(j)}=(b_k^{(j)})_{k\ge1}\). Choose \(N\) and a \(d\)-dimensional subspace \(E\subset\bigcap_{j=1}^m\operatorname{span}\{b_k^{(j)}:k\le N\}^{\perp}\); this intersection is infinite-dimensional, so \(d\) can be arbitrarily large. For \(k>N\), put \(v_{jk}=P_Eb_k^{(j)}\). Parseval gives \(\sum_{k>N}\|v_{jk}\|^2=d\), and \(\|v_{jk}\|\le1\).

Let \(g\) be a standard Gaussian vector in \(E\). The lower-tail estimate gives \(\mathbb P(\|g\|<\sqrt{d/2})\le e^{-d/16}\). For \(a_{jk}=\|v_{jk}\|^2\in[0,1]\), the Gaussian tail bound gives
\[
\mathbb P\bigl(|\langle g,v_{jk}\rangle|>\varepsilon\sqrt{d/2}\bigr)\le 2e^{-\varepsilon^2d/(4a_{jk})}.
\]
When \(C=\varepsilon^2d/4\ge1\), \(e^{-C/a}\le a e^{-C}\) for \(0<a\le1\). Hence the sum of these probabilities over all \(j,k\) is at most \(2md e^{-\varepsilon^2d/4}\). Choose \(d\) so large that
\[
e^{-d/16}+2md e^{-\varepsilon^2d/4}<1.
\]
There is then a realization with \(\|g\|\ge\sqrt{d/2}\) and all the displayed coordinates at most \(\varepsilon\sqrt{d/2}\). The first \(N\) coordinates vanish because \(E\) is orthogonal to them. Thus \(u=g/\|g\|\) is a unit vector with \(\sup_{j,k}|\langle u,b_k^{(j)}\rangle|\le\varepsilon\). Taking \(\varepsilon=1/n\) constructs \((u_n)\).

Define \(T_nx=\langle x,u_n\rangle e_n\). Each \(T_n\) has rank one and norm one. For every tested basis, \(T_nb_k^{(j)}\in\{\lambda e_n:|\lambda|\le1/n\}\). The union of these shrinking line segments together with zero is relatively compact: any sequence either has bounded segment index, hence a convergent subsequence, or its norms tend to zero.

On the other hand, \(T_nu_n=e_n\), so \(\{e_n:n\ge1\}\subset\bigcup_nT_n(B_{\ell_2})\). The coordinate functionals \(\delta_n\in(c_0)^*=\ell_1\) are weak-star-null, since \(\delta_n(x)=x_n\to0\) for every \(x\in c_0\), but \(\sup_k|\delta_n(e_k)|=1\). Thus \(\{e_n\}\), and therefore the full union of unit-ball images, is not limited.

## Verification

The Gaussian estimate is summable because the projected basis vectors satisfy \(\sum_k\|P_Eb_k^{(j)}\|^2=d\). The finite union of tested image sets is relatively compact by the shrinking-segment argument, while non-limitedness is witnessed explicitly by \((\delta_n)\). No finite-dimensional experiment is used to infer an infinite-dimensional statement; the proof covers every finite \(m\) and every prescribed finite family of bases.

## Relationship to prior work

Gorokhova's *On compact (limited) operators between Hilbert and Banach spaces* proves that a family \(\mathcal T\subset\mathcal L(H,Y)\) is collectively limited exactly when the union \(\{Tx_n:T\in\mathcal T,n\ge1\}\) is limited for every orthonormal sequence \((x_n)\). The same paper notes that one fixed orthonormal basis cannot replace the universal test for a single operator. The result here is a family-level strengthening: no finite list of bases suffices, even when every operator in the family has rank one and every tested image union is relatively compact. It does not contradict the universal-sequence criterion.

## Limitations

The construction rules out finite predetermined lists of bases. It does not characterize which infinite test families suffice, and it makes no claim about alternative tests using information beyond basis images. The literature search did not establish that this finite-family strengthening is absent from all sources; that remains a residual priority risk.

## References

1. S. Gorokhova, *On compact (limited) operators between Hilbert and Banach spaces*, arXiv:2403.06262, first submitted 10 March 2024; v5 dated 3 July 2024. Theorem 1 (collective compactness/limitedness), Theorems 2–3, and the discussion of the limitation of a single-basis test. https://arxiv.org/abs/2403.06262
