# Anchored ordinal sums yield maximal convex spaceability at every finite Lipschitz exponent

## Finding

For every real \(1\le p<\infty\), let \(\mathcal L_p\) consist of bivariate copulas \(C\) satisfying
\[
 |C(z)-C(z')|\le\|z-z'\|_p\quad(z,z'\in[0,1]^2)
\]
but failing this inequality with \(p\) replaced by every \(p'>p\), including \(p'=\infty\). Then \(\mathcal L_p\) contains a **compact convex subset** \(\mathcal K_p\) with a linearly independent subset of cardinality continuum. In particular, \(\mathcal L_p\) is maximally convex spaceable in the sense of Definition 2.5 of de Amo et al. (2026).

An explicit compact witness is obtained by fixing one full-strength Lipschitz block in an infinite ordinal sum and allowing a free independently weighted copula interpolation in every other block. This strengthens the previously established maximal convex lineability for the same precise class.

## Assumptions and scope

All copulas are distribution functions on \([0,1]^2\) with two uniform margins. The ambient topology is the supremum norm on continuous functions on that square. Here \(\|z\|_p=(|z_1|^p+|z_2|^p)^{1/p}\) and \(\|z\|_\infty=\max(|z_1|,|z_2|)\). Convex spaceability means the existence **inside the class** of a closed convex set containing infinitely many linearly independent elements; maximal means continuum many, the largest possible cardinality for continuous functions on a compact metric space. This is not the existence of a closed linear subspace consisting of copulas.

Fix \(p\in[1,\infty)\), and write
\[
q=\begin{cases}\infty,&p=1,\\p/(p-1),&p>1,\end{cases}
\qquad c=2-2^{1/q}\in(0,1],\qquad \sigma=\frac1{2-c}=2^{-1/q},
\]
where \(2^{1/\infty}=1\). Let
\[
M(u,v)=\min(u,v),\qquad
B_c(u,v)=\min\left\{u,v,\max\left(\frac{u+v-c}{2-c},0\right)\right\}.
\]
Define intervals \(I_0=[1/2,1]\) and \(I_n=[2^{-(n+1)},2^{-n}]\) for integers \(n\ge1\). For every sequence \(x=(x_n)_{n\ge1}\in[0,1]^{\mathbb N}\), define a bivariate copula \(F_x\) by the standard ordinal sum with component \(B_c\) on \(I_0\), and component \((1-x_n)M+x_nB_c\) on \(I_n\). Explicitly, if \((u,v)\in I_n^2\), where \(I_n=[a_n,b_n]\) and \(h_n=b_n-a_n\), put
\[
F_x(u,v)=a_n+h_n H_n\left(\frac{u-a_n}{h_n},\frac{v-a_n}{h_n}\right),\quad
H_0=B_c,\quad H_n=(1-x_n)M+x_nB_c\ (n\ge1).
\]
At every other point put \(F_x(u,v)=M(u,v)\). The expressions agree on shared boundaries. Set \(\mathcal K_p=\{F_x:x\in[0,1]^{\mathbb N}\}\).

## Proof

**1. Elementary copula and gradient lemma.** For \(0<c<1\), \(B_c\) is grounded and has both correct uniform margins, directly from its formula. For any fixed \(u\in(0,1)\), except where two affine branches meet, \(\partial_u B_c(u,v)\), as \(v\) increases, takes successively the values \(0\), \(\sigma\), and \(1\). The two transitions occur at
\[
\ell_c(u)=\max\left\{0,c-u,\frac{u-c}{1-c}\right\},
\qquad h_c(u)=c+(1-c)u,
\]
with \(\ell_c(u)\le h_c(u)\). This follows by comparing the three competing affine branches \(u\), \(v\), and \((u+v-c)/(2-c)\) and the zero branch. Consequently, for \(v_1\le v_2\), the derivative \(\partial_u[B_c(u,v_2)-B_c(u,v_1)]\) is nonnegative for almost every \(u\). Integration in \(u\) proves nonnegative volume on every rectangle, hence \(B_c\) is a copula. At \(c=1\), the formula reduces to the lower Fréchet copula \(B_1(u,v)=\max(u+v-1,0)\), with the same conclusion. At \(c=0\), \(B_0=M\), also a copula.

At almost every point, the gradient of \(B_c\) is one of
\[
(0,0),\quad (1,0),\quad(0,1),\quad(\sigma,\sigma).
\]
Their \(\ell_q\) norms are at most one because \(2^{1/q}\sigma=1\). Therefore \(B_c\) is one-Lipschitz with respect to \(\ell_p\), by integrating its piecewise affine gradient along line segments. The same is true of \(M\) and of every convex combination \((1-t)M+tB_c\), \(t\in[0,1]\).

**2. Each ordinal sum has precisely the required Lipschitz exponent.** The ordinal sum of bivariate copulas is a copula: its joint probability measure places mass \(h_n\) in each diagonal square \(I_n^2\), with the rescaled component law inside that square. Since \(\sum_{n\ge0}h_n=1\), each margin remains uniform; the distribution function is exactly \(F_x\) above. Away from the countable block boundaries and affine transition lines, its gradient is either a gradient of \(H_n\) or a gradient of \(M\), so its dual \(\ell_q\) norm does not exceed one. A locally Lipschitz function on the convex square with this a.e. gradient bound is one-Lipschitz for \(\ell_p\); equivalently, integrate along line segments avoiding the null set of boundaries, then use continuity. Thus every \(F_x\) satisfies the \(p\)-Lipschitz inequality.

On the fixed top block, \(F_x\) equals the rescaled \(B_c\), independently of \(x\). At the interior point \((u,v)=(7/8,7/8)\) of this block, the middle affine branch of \(B_c\) is strict: for any \(c>0\), at \((3/4,3/4)\) its value is \((3/2-c)/(2-c)<3/4\), and it is positive. Hence
\[
\nabla F_x(7/8,7/8)=(\sigma,\sigma).
\]
For every \(p'>p\), its dual exponent \(q'<q\) obeys
\[
\|(\sigma,\sigma)\|_{q'}=2^{1/q'-1/q}>1.
\]
The derivative of any one-Lipschitz function must have dual norm at most one wherever it exists. This is a contradiction, so \(F_x\) is not one-Lipschitz for any larger exponent, including \(p'=\infty\). Therefore \(\mathcal K_p\subseteq\mathcal L_p\).

**3. Compact convex witness.** The mapping \(x\mapsto F_x\) is affine with respect to pointwise convex combinations of sequences. For sequences \(x,y\),
\[
\|F_x-F_y\|_\infty
=\sup_{n\ge1}\left(h_n|x_n-y_n|\right)\|B_c-M\|_\infty.
\]
For any fixed \(N\), the tail with \(n>N\) is bounded by \(2^{-(N+2)}\|B_c-M\|_\infty\), uniformly in \(x,y\), while the first \(N\) coordinates are continuous. Thus \(x\mapsto F_x\) is continuous for the product topology of \([0,1]^{\mathbb N}\). The latter is compact, hence \(\mathcal K_p\) is compact and therefore closed in the supremum norm. It is convex by affinity.

**4. Continuum-sized linear independence.** For every \(t\in(0,1)\) take \(x^{(t)}_n=t^n\) and denote \(G_t=F_{x^{(t)}}\). Suppose \(t_1,\ldots,t_k\) are distinct and \(\sum_{j=1}^k a_jG_{t_j}\equiv0\). Evaluating at \((1,1)\), since all are copulas, yields \(\sum_j a_j=0\). Within block \(I_n\), choose the rescaled point \((3/4,3/4)\). The strict difference of the two component copulas is
\[
M(3/4,3/4)-B_c(3/4,3/4)=\frac{c}{4(2-c)}>0.
\]
The resulting linear relation, after cancellation of the common terms, is \(\sum_{j=1}^k a_jt_j^n=0\) for every \(n\ge1\). Taking \(n=1,\ldots,k\) produces a Vandermonde matrix with determinant \((\prod_jt_j)\prod_{i<j}(t_j-t_i)\ne0\). Hence all \(a_j=0\). The family \(\{G_t:t\in(0,1)\}\) is linearly independent and has cardinality continuum. As every continuous function on \([0,1]^2\) is determined by a countable dense subset, this cardinality is maximal. The theorem follows.

## Verification

Run `python3 check.py` using Python 3 and its standard library only. The script checks the base copula's finite-grid rectangle volumes and margins for five representative exponents, checks finite ordinal sums' margins, symmetry, rectangle volumes and Lipschitz inequalities, checks the anchored gradient numerically, and evaluates a three-by-three Vandermonde determinant exactly as a rational number. The test output is `PASS 12706 finite identities and representative inequalities` and `exact Vandermonde determinant: 3/1024`. All infinite statements, especially the endpoint \(p\)-classification, closedness, and continuum-sized independence, are proved above rather than inferred from these finite tests.

## Relationship to prior work

The source article of de Amo, Fernández-Sánchez, García-Fernández and Úbeda-Flores, first posted on 6 February 2026, establishes maximal convex **lineability** of the same sharp Lipschitz-exponent class (preprint Theorem 6; journal Theorem 3.6), and explicitly leaves **convex spaceability** unresolved (preprint Section 4; journal Section 4). It gives the basic family \(B_c\) and uses ordinal sums built from almost-disjoint index sets. The present theorem uses a single fixed exact-exponent block plus a whole compact product of freely variable blocks; this is what supplies closure without losing the sharp exponent. The 2010 paper of De Baets, De Meyer and Mesiar studies Lipschitz continuity and its preservation by ordinal and convex sums, providing useful background tools, but the compact convex witness and continuum independence are additional arguments. A separate fractal-support copula spaceability question concerns a different property and does not imply the present theorem.

## Limitations

The statement concerns bivariate copulas, each fixed \(p\in[1,\infty)\), the *one*-Lipschitz constant, and supremum-norm closure. It does not settle a higher-dimensional extension, the \(p=\infty\) endpoint, or the existence of a nonzero closed linear subspace of copulas. The computer checks are finite spot checks, not completeness proofs. Literature searches and inspection of the 2026 full text did not uncover an existing theorem implying this closed-family statement, but unindexed equivalent work is possible. The full 2010 journal article was not obtainable through accessible open repositories or the available institutional route, so comparison with its full text is a residual priority limitation.

## References

1. E. de Amo, J. Fernández-Sánchez, D. García-Fernández, M. Úbeda-Flores, *Convex lineability in copula and quasi-copula sets*, arXiv:2602.06918v1 (first public posting 2026-02-06), https://arxiv.org/abs/2602.06918; later published in *Mediterranean Journal of Mathematics* 23, 131 (2026), https://doi.org/10.1007/s00009-026-03129-9.
2. B. De Baets, H. De Meyer, R. Mesiar, *Lipschitz continuity of copulas w.r.t. \(L_p\)-norms*, *Nonlinear Analysis* 72 (2010), 3722–3731, https://doi.org/10.1016/j.na.2010.01.009.
