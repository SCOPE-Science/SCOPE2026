# Compact quasinilpotent sum-hyponormal multishifts with rank-one defect

## Statement

For every integer \(d\ge 2\), there is a commuting \(d\)-tuple
\[
\mathbf T=(T_1,\ldots,T_d)
\]
of compact quasinilpotent operators on \(\ell^2(\mathbb N_0^d)\) such that
\[
\boxed{\sum_{j=1}^d[T_j^*,T_j]=dP_0,}
\]
where \(P_0\) is the rank-one projection onto the basis vector indexed by \(0\in\mathbb N_0^d\).

Consequently, \(\mathbf T\) is strictly sum-hyponormal but not sum-normal, every coordinate \(T_j\) fails to be hyponormal, and \(\mathbf T\) is completely nonnormal. In particular, compactness does not force a sum-hyponormal commuting tuple to be sum-normal or normal.

## Construction

Let \((e_\alpha)_{\alpha\in\mathbb N_0^d}\) be the canonical orthonormal basis of
\[
H=\ell^2(\mathbb N_0^d),
\qquad |\alpha|=\alpha_1+\cdots+\alpha_d.
\]
For \(k=|\alpha|\), define positive weights
\[
w_{\alpha,j}^2
=
\frac{d!\,k!\,(\alpha_j+1)}{(k+d)!},
\qquad j=1,\ldots,d,
\]
and set
\[
T_je_\alpha=w_{\alpha,j}e_{\alpha+e_j}.
\]

For later use, put
\[
m_k^2=\frac{d!(k+1)!}{(k+d)!}
      =\frac{d!}{(k+2)(k+3)\cdots(k+d)}.
\]
Then \(w_{\alpha,j}\le m_k\) for every \(|\alpha|=k\), and \(m_k\downarrow0\) when \(d\ge2\).

## Proof

### Commutativity

Write
\[
c_k=\frac{d!\,k!}{(k+d)!}.
\]
For \(j\ne \ell\),
\[
w_{\alpha,\ell}^2w_{\alpha+e_\ell,j}^2
=
c_kc_{k+1}(\alpha_\ell+1)(\alpha_j+1)
=
w_{\alpha,j}^2w_{\alpha+e_j,\ell}^2.
\]
All weights are positive, hence
\[
w_{\alpha,\ell}w_{\alpha+e_\ell,j}
=
w_{\alpha,j}w_{\alpha+e_j,\ell},
\]
so \(T_jT_\ell=T_\ell T_j\).

### Compactness

For fixed \(j\), the vectors \(T_je_\alpha\) have pairwise distinct supports. Hence the norm of the restriction of \(T_j\) to the span of levels \(|\alpha|\ge N\) is
\[
\sup_{|\alpha|\ge N}w_{\alpha,j}\le m_N.
\]
Since \(m_N\to0\), truncation to finitely many levels approximates \(T_j\) in operator norm by finite-rank operators. Thus every \(T_j\) is compact.

### Exact self-commutator sum

Both \(T_j^*T_j\) and \(T_jT_j^*\) are diagonal in the basis \((e_\alpha)\).

If \(|\alpha|=k\), then
\[
\sum_{j=1}^d\|T_je_\alpha\|^2
=
\frac{d!k!}{(k+d)!}\sum_{j=1}^d(\alpha_j+1)
=
\frac{d!k!}{(k+d-1)!}.
\]
For \(k\ge1\), the incoming contribution is
\[
\sum_{\alpha_j>0}
\|T_j^*e_\alpha\|^2
=
\frac{d!(k-1)!}{(k+d-1)!}\sum_{j=1}^d\alpha_j
=
\frac{d!k!}{(k+d-1)!}.
\]
Thus the diagonal coefficient of
\(\sum_j[T_j^*,T_j]\) vanishes at every \(e_\alpha\) with \(|\alpha|\ge1\).

At the root \(\alpha=0\), there is no incoming contribution and
\[
w_{0,j}^2=1
\]
for every \(j\). Hence
\[
\sum_{j=1}^d[T_j^*,T_j]=dP_0.
\]

### Quasinilpotence

Since \(m_k\) is decreasing,
\[
\|T_j^n\|
\le
\prod_{s=0}^{n-1}m_s.
\]
Given \(\varepsilon>0\), all sufficiently large \(m_s\) are below \(\varepsilon\). Therefore
\[
\lim_{n\to\infty}\|T_j^n\|^{1/n}=0,
\]
so every \(T_j\) is quasinilpotent.

By the projection property of the Taylor spectrum,
\[
\pi_j(\sigma(\mathbf T))=\sigma(T_j)=\{0\}
\]
for each \(j\). Since the Taylor spectrum is nonempty,
\[
\sigma(\mathbf T)=\{(0,\ldots,0)\}.
\]
Thus the tuple itself is quasinilpotent.

### No coordinate is hyponormal

On the ray \(\alpha=ke_j\), \(k\ge1\),
\[
\langle[T_j^*,T_j]e_{ke_j},e_{ke_j}\rangle
=
m_k^2-m_{k-1}^2.
\]
But
\[
\frac{m_k^2}{m_{k-1}^2}=\frac{k+1}{k+d}<1
\qquad(d\ge2),
\]
so this diagonal entry is negative. Hence no \(T_j\) is hyponormal.

### Complete nonnormality

Every weight is strictly positive, so every \(T_j\) is injective. If a nonzero reducing subspace \(M\) carried a normal restriction of the tuple, then each \(T_j|_M\) would be a normal quasinilpotent operator, hence zero. This contradicts injectivity. Therefore \(\mathbf T\) is completely nonnormal.

## Consequence for a recent question

Chavan, Reza and Sequeira define a commuting tuple to be sum-hyponormal when
\[
\sum_j[T_j^*,T_j]\ge0
\]
and ask in Question 1.3(i) whether every sum-hyponormal tuple of compact operators must be sum-normal or normal. Their Theorem 2.2 decomposes a compact sum-hyponormal tuple into a normal summand and a completely nonnormal quasinilpotent sum-hyponormal summand, while Theorem 2.3 proves that a sum-hyponormal tuple whose coordinates are nilpotent must vanish. They explicitly ask whether nilpotence can be weakened to quasinilpotence.

The construction above gives a negative answer to Question 1.3(i) for every \(d\ge2\). It also shows that the nilpotence hypothesis in Theorem 2.3 cannot be replaced by quasinilpotence: the tuple is nonzero, compact, quasinilpotent and sum-hyponormal.

For \(d=2\), the weights take the particularly simple form
\[
w_{(m,n),1}^2
=
\frac{2(m+1)}{(m+n+1)(m+n+2)},
\qquad
w_{(m,n),2}^2
=
\frac{2(n+1)}{(m+n+1)(m+n+2)},
\]
and
\[
[T_1^*,T_1]+[T_2^*,T_2]=2P_{(0,0)}.
\]

## Literature context and originality

The result is claimed only to the best of our knowledge.

The closest earlier terminology located is the literature on spherical \(p\)-hyponormality of commuting pairs. In particular, Kim, Kim and Yoon state that they completely characterize spherically \(p\)-hyponormal two-variable weighted shifts. This is a material originality risk for the \(d=2\) case because the \(p=1\) condition is closely related to the same spherical self-commutator inequality. The available abstract and bibliographic record were inspected, but the full theorem statements and examples in that paper were not accessible for comparison. Exact and synonymous searches did not locate a compact quasinilpotent weighted-shift example with the rank-one defect above, nor an earlier negative answer to the compact sum-hyponormal question.

Accordingly, the novelty claim is restricted to the explicit compact/quasinilpotent rank-one-defect multishift construction and its application to the 2026 Question 1.3(i), not to the general algebra of multivariable weighted shifts or to spherical hyponormality as a concept.

## Limitations

This example is sum-hyponormal but not sum-normal. It therefore does not answer Question 1.3(ii), does not produce a nonzero quasinilpotent sum-normal tuple, and does not classify compact sum-hyponormal tuples. No sharp uniqueness statement for the displayed weights is claimed.

## References

1. S. Chavan, M. R. Reza, S. S. Sequeira, *Sum of self-commutators of commuting operators*, arXiv:2609.19287v1 (2026). https://arxiv.org/abs/2609.19287
2. H. W. Kim, J. Kim, J. Yoon, *Spherical Aluthge transform, spherical \(p\) and log-hyponormality of commuting pairs of operators*, Linear and Multilinear Algebra 70 (2022), 2047–2064. https://doi.org/10.1080/03081087.2020.1781040
