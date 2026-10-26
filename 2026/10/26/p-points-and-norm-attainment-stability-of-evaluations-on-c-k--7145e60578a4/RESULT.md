# \(P\)-points and norm-attainment stability of evaluations on \(C(K)\)

## Finding

Let \(K\) be a compact Hausdorff space and \(p\in K\). Call \(p\) a **\(P\)-point** if the intersection of every countable family of open neighborhoods of \(p\) is a neighborhood of \(p\). Then the following are equivalent:

1. \(p\) is a \(P\)-point.
2. For every equivalent lattice norm \(\|\cdot\|_L\) on the real Banach lattice \(C(K)\), the evaluation functional \(\delta_p(f)=f(p)\) attains its norm.

Thus the exceptional behavior of evaluation at the endpoint of \([0,\omega_1]\) is governed by a topological point property, not by the ordinal notation itself.

## Assumptions and scope

Throughout, \(K\) is compact Hausdorff and \(C(K)\) is real-valued. An equivalent lattice norm is a norm equivalent to the supremum norm and monotone for the pointwise order. Norm attainment means that some \(f\) with \(\|f\|_L=1\) satisfies \(|f(p)|=\|\delta_p\|_{L^*}\). A neighborhood need not itself be open, but it contains an open neighborhood.

## Proof

**\(P\)-point implies stability.** Fix an equivalent lattice norm \(\|\cdot\|_L\), and rescale it so that \(\|\delta_p\|_{L^*}=1\). For every integer \(n\ge1\), choose \(f_n\in C(K)_+\) with \(f_n(p)=1\) and \(\|f_n\|_L\le 1+1/n\); this follows from the definition of the dual norm by taking absolute values and rescaling an approximate norming vector.

For each fixed \(n\), continuity gives open neighborhoods \(V_{n,m}=\{x\in K:|f_n(x)-1|<1/m\}\) of \(p\), for all integers \(m\ge1\). Their intersection is \(f_n^{-1}(\{1\})\), which is a neighborhood because \(p\) is a \(P\)-point. Hence each \(f_n\) equals \(1\) on some neighborhood \(W_n\) of \(p\). Choose open neighborhoods \(O_n\subseteq W_n\) of \(p\). The \(P\)-point property implies that \(W=\bigcap_{n\ge1}O_n\) is a neighborhood of \(p\). Choose an open neighborhood \(G\) with \(p\in G\subseteq W\). By normality of compact Hausdorff spaces, there is \(g\in C(K)\) with \(0\le g\le1\), \(g(p)=1\), and support contained in \(G\). Since \(f_n=1\) on \(W\), we have \(0\le g\le f_n\) for every \(n\). Monotonicity gives \(\|g\|_L\le1+1/n\) for all \(n\), so \(\|g\|_L\le1\). Conversely, \(g(p)=1\) and \(\|\delta_p\|_{L^*}=1\) imply \(\|g\|_L\ge1\). Thus \(\|g\|_L=1\) and \(\delta_p\) attains its norm.

**Failure of the \(P\)-point property implies instability.** Choose open neighborhoods \(U_n\) of \(p\) such that \(U=\bigcap_{n\ge1}U_n\) is not a neighborhood of \(p\), and put \(F_n=K\setminus U_n\). Define
\[
\|f\|_* = \|f\|_\infty+\sum_{n\ge1}2^{-n}\|f|_{F_n}\|_\infty,\qquad f\in C(K),
\]
where the supremum over an empty set is taken as zero. This is a lattice norm, and
\[
\|f\|_\infty\le\|f\|_*\le2\|f\|_\infty,
\]
so it is equivalent to the usual norm.

For every \(N\ge1\), the finite intersection \(G_N=\bigcap_{n=1}^N U_n\) is an open neighborhood of \(p\). Choose \(g_N\in C(K)\) with \(0\le g_N\le1\), \(g_N(p)=1\), and support contained in \(G_N\). Then \(g_N|_{F_n}=0\) for \(n\le N\), and \(\|g_N|_{F_n}\|_\infty\le1\) for \(n>N\). Consequently,
\[
1\le\|g_N\|_*\le1+\sum_{n>N}2^{-n}=1+2^{-N}.
\]
For every \(f\in C(K)\), \(|f(p)|\le\|f\|_\infty\le\|f\|_*\), so \(\|\delta_p\|_{(C(K),\|\cdot\|_*)^*}\le1\). The displayed test functions imply \(\|\delta_p\|_{(C(K),\|\cdot\|_*)^*}\ge(1+2^{-N})^{-1}\) for every \(N\), hence \(\|\delta_p\|_{(C(K),\|\cdot\|_*)^*}=1\).

Now let \(f(p)=1\). By continuity, there is an open neighborhood \(H\) of \(p\) on which \(|f|>1/2\). Since \(U\) is not a neighborhood, \(H\) is not contained in \(U\); therefore some \(n\) has \(H\cap F_n\ne\varnothing\). It follows that \(\|f|_{F_n}\|_\infty>1/2\), so the added series term is strictly positive and \(\|f\|_*>1\). Replacing \(f\) by \(-f\) handles \(f(p)=-1\). Thus no unit vector can norm \(\delta_p\), although its dual norm is one.

The two implications prove the equivalence.

## Verification

The reverse construction uses only the failure of a countable intersection of neighborhoods to be a neighborhood; it does not require a sequence of points converging to \(p\), first countability, or countable tightness. The restriction seminorms are finite and continuous, their weights sum to one, and the explicit bounds establish equivalence of norms. The lower bound for the dual norm follows from \(g_N(p)=1\) and \(\|g_N\|_*\le1+2^{-N}\); nonattainment follows because every candidate with absolute value one at \(p\) incurs a positive restriction penalty.

## Relationship to prior work

Bilokopytov, García-Sánchez, de Hevia, Martínez-Cervantes, and Tradacete give a robust-attainment example at \(\omega_1\in[0,\omega_1]\): every continuous function is eventually constant there, and a clopen tail supplies a common norming vector for any lattice renorming (arXiv:2502.10165v1, Example 3.4). Their Theorem 3.1 also gives a global renorming result when a Banach lattice supports a strictly positive functional. In Proposition 5.1, they construct a nonattaining evaluation for a point that is a sequential accumulation point, using a weighted sum of point evaluations. These results leave open a pointwise criterion for arbitrary compact Hausdorff spaces.

The present construction replaces the point-evaluation penalties by restrictions to the closed sets \(F_n=K\setminus U_n\) arising from a countable family of neighborhoods. It therefore works for every non-P-point, even when no sequence of points converges to the chosen point. Combined with the P-point implication, it gives an exact classification rather than a single robust example or an existence result for some accumulation point.
## Limitations

The theorem concerns scalar real \(C(K)\) and equivalent lattice norms. It does not classify norm attainment for arbitrary Banach lattices, vector-valued function spaces, or renormings that do not preserve the lattice order. The proof is analytic and uses normality of compact Hausdorff spaces; no computational experiment or independent audit is claimed.

## References

1. E. Bilokopytov, E. García-Sánchez, D. de Hevia, G. Martínez-Cervantes, and P. Tradacete, *Norm-attaining lattice homomorphisms and renormings of Banach lattices*, arXiv:2502.10165v1 (first public version 14 February 2025), especially Theorem 3.1, Proposition 5.1, and Example 3.4.
