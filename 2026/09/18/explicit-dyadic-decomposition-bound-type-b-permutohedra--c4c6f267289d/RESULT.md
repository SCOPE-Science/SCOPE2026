# An explicit dyadic decomposition bound for type B generalized permutohedra

## Result

Let \(P\subseteq\mathbb R^n\) be a \(d\)-dimensional integral generalized permutohedron of type \(B\), with lattice \(\mathbb Z^n\). Then \(P\) has the dyadic decomposition property with exponent

\[
m=\max\!\left\{0,\left\lfloor\frac{d-1}{2}\right\rfloor\right\}.
\]

Equivalently, for every \(k\ge1\) and every \(x\in kP\cap\mathbb Z^n\), there exist
\[
p_1,\ldots,p_{2^m k}\in P\cap\mathbb Z^n
\]
such that
\[
2^m x=p_1+\cdots+p_{2^m k}.
\]

The same bound applies to integral type \(D\) generalized permutohedra.

More precisely, the regular triangulations obtained by the deletion-contraction construction of Vallée can be chosen so that every \(d'\)-simplex \(T\) appearing in them has edge-lattice quotient of exponent dividing
\[
2^{\,\max\{0,\lfloor(d'-1)/2\rfloor\}}.
\]
This refines the fact that the quotient has \(2\)-power order.

If \(\mu_d\) denotes the least exponent that works uniformly for all \(d\)-dimensional integral type \(B\) generalized permutohedra, then
\[
\mu_1=\mu_2=0,\qquad
\mu_3=\mu_4=1,
\]
and for every \(d\ge3\),
\[
1\le \mu_d\le \left\lfloor\frac{d-1}{2}\right\rfloor.
\]

## Lattice exponent of a simplex

For a lattice simplex
\[
T=\operatorname{conv}(v_0,\ldots,v_r),
\]
write
\[
\Lambda_T=\operatorname{dir}(T)\cap\mathbb Z^n,\qquad
\Gamma_T=\mathbb Z\langle v_i-v_0:1\le i\le r\rangle.
\]
Define \(q(T)\) to be the least \(q\ge0\) for which
\[
2^q\Lambda_T\subseteq\Gamma_T
\]
when such a \(q\) exists. Thus \(2^{q(T)}\) is the exponent of the finite \(2\)-group
\(\Lambda_T/\Gamma_T\), rather than its order. The distinction is important: normalized volume records the order of this quotient, while decomposition only requires an integer that annihilates it.

## Lemma 1: type \(B\) root subconfigurations have only elementary \(2\)-torsion

Let
\[
B^+=\{e_i\}\cup\{e_i-e_j:i<j\}\cup\{e_i+e_j:i<j\}.
\]
If \(E\subseteq B^+\) is linearly independent, set
\[
\Gamma_E=\mathbb Z\langle E\rangle,\qquad
\Lambda_E=\operatorname{lin}(E)\cap\mathbb Z^n.
\]
Then
\[
2\Lambda_E\subseteq\Gamma_E.
\]
Equivalently, \(\Lambda_E/\Gamma_E\) is an elementary abelian \(2\)-group.

### Proof

Let \(M\) be the integer matrix whose columns are the vectors of \(E\), and delete its zero rows. Every column has one or two nonzero entries, each equal to \(\pm1\).

If a row or column has exactly one nonzero entry, that entry is \(\pm1\). Integer row or column operations split off a \(1\times1\) identity block without changing the torsion of the cokernel; the remaining matrix is again of the same form. Iterate.

Suppose no row or column has degree one. If \(M\) has \(r\) columns and \(s\) nonzero rows, then every column has exactly two nonzero entries, so \(M\) has \(2r\) nonzero entries. Every row has at least two, hence \(2r\ge2s\). Column independence gives \(r\le s\). Therefore \(r=s\), and every row and every column has exactly two nonzero entries.

The bipartite support graph between rows and columns is then a disjoint union of cycles. After row and column permutations, \(M\) is block diagonal with one square block per cycle. A cycle block has determinant \(0\) or \(\pm2\); column independence excludes \(0\). Deleting one row and one column from such a block leaves a path matrix with determinant \(\pm1\). Hence its Smith form is
\[
\operatorname{diag}(1,\ldots,1,2).
\]
Thus every torsion invariant factor of \(M\) is \(2\), proving \(2\Lambda_E\subseteq\Gamma_E\). \(\square\)

## Lemma 2: a quantitative complementarity statement

Let \(V,W\subseteq\mathbb R^n\) be independent rational subspaces, each spanned by type \(B\) roots. Put
\[
\Lambda_V=V\cap\mathbb Z^n,\quad
\Lambda_W=W\cap\mathbb Z^n,\quad
\Lambda=(V+W)\cap\mathbb Z^n.
\]
Then
\[
2\Lambda\subseteq \Lambda_V\oplus\Lambda_W.
\]

Indeed, choose linearly independent type \(B\) root bases \(E_V\) and \(E_W\) of \(V\) and \(W\). Their union is linearly independent. Lemma 1 gives
\[
2\Lambda\subseteq
\mathbb Z\langle E_V\cup E_W\rangle
\subseteq \Lambda_V\oplus\Lambda_W.
\]

The same statement passes to arbitrary rational subspaces \(V'\subseteq V\) and \(W'\subseteq W\). If \(z=u+w\in(V'+W')\cap\mathbb Z^n\), then the displayed inclusion writes \(2z=a+b\) with \(a\in\Lambda_V\), \(b\in\Lambda_W\). Uniqueness of decomposition in \(V\oplus W\) forces \(a=2u\) and \(b=2w\), so \(a\in V'\cap\mathbb Z^n\) and \(b\in W'\cap\mathbb Z^n\).

## Lemma 3: one nontrivial join adds at most one binary denominator

Suppose lattice simplices
\[
T_0\subseteq\{x_1=0\},\qquad
T_1\subseteq\{x_1=1\}
\]
have independent direction spaces satisfying the conclusion of Lemma 2, and let
\[
T=\operatorname{conv}(T_0\cup T_1).
\]
If \(d_i=\dim T_i\), then
\[
q(T)\le
\begin{cases}
\max\{q(T_0),q(T_1)\}+1,& d_0,d_1>0,\\
\max\{q(T_0),q(T_1)\},& \min\{d_0,d_1\}=0.
\end{cases}
\]

### Proof

Choose vertices \(w_i\in T_i\) and put \(v=w_1-w_0\). Its first coordinate is \(1\). Set \(V_i=\operatorname{dir}(T_i)\) and
\[
\Lambda_U=(V_0+V_1)\cap\mathbb Z^n.
\]
Every \(z\in\Lambda_T\) has integral first coordinate \(a\), and \(z-av\in\Lambda_U\). Conversely \(\Lambda_U+\mathbb Zv\subseteq\Lambda_T\). Therefore
\[
\Lambda_T/\Gamma_T\cong
\Lambda_U/(\Gamma_{T_0}+\Gamma_{T_1}).
\]

If both \(V_i\) are positive-dimensional, Lemma 2 gives
\[
2\Lambda_U\subseteq
(V_0\cap\mathbb Z^n)\oplus(V_1\cap\mathbb Z^n).
\]
Multiplication by \(2^{\max(q(T_0),q(T_1))}\) then lands in
\(\Gamma_{T_0}+\Gamma_{T_1}\). If one \(V_i\) is zero, no factor \(2\) is needed. \(\square\)

## The triangulation bound

Consider Vallée's inductive regular triangulation of a delta-matroid polytope. At one deletion-contraction step, a simplex either lies in one coordinate slice, or is a join of simplices \(T_0,T_1\) in the two consecutive slices. In the second case the relevant face-direction spaces are independent and are spanned by type \(B\) roots; Lemma 2 therefore applies to the simplex-direction subspaces.

We prove by induction through this construction that every simplex \(T\) of dimension \(r\) satisfies
\[
q(T)\le b(r),\qquad
b(r)=\max\!\left\{0,\left\lfloor\frac{r-1}{2}\right\rfloor\right\}.
\]

If a simplex remains in one slice, the claim is inherited unchanged. If it is a join and one factor is a point, Lemma 3 adds no binary denominator and \(b\) is nondecreasing. If both factors have positive dimensions \(r_0,r_1\), then
\[
r=r_0+r_1+1
\]
and Lemma 3 yields
\[
q(T)\le 1+\max\{b(r_0),b(r_1)\}
\le b(r_0+r_1+1)=b(r).
\]
The final inequality follows immediately from \(r_0,r_1\ge1\).

For an arbitrary integral type \(B\) generalized permutohedron, Vallée first dices by integer coordinate hyperplanes. Each diced cell is an integer translate of a delta-matroid polytope, and the cellwise regular triangulations glue. Hence the same bound holds for every maximal simplex in the resulting triangulation. A maximal simplex of a \(d\)-dimensional polytope has dimension \(d\), so its quotient exponent divides \(2^{b(d)}\).

## From quotient exponent to decomposition

Let \(T=\operatorname{conv}(v_0,\ldots,v_d)\) be a maximal simplex containing \(x/k\), and write
\[
\frac{x}{k}=\sum_{i=0}^d\lambda_i v_i,\qquad
\lambda_i\ge0,\quad \sum_i\lambda_i=1.
\]
Since \(x-kv_0\in\Lambda_T\) and \(2^{b(d)}\Lambda_T\subseteq\Gamma_T\),
\[
2^{b(d)}(x-kv_0)
=
\sum_{i=1}^d c_i(v_i-v_0)
\]
for integers \(c_i\). Uniqueness of real coordinates in the edge basis gives
\[
c_i=2^{b(d)}k\lambda_i\in\mathbb Z_{\ge0}.
\]
Also
\[
c_0=2^{b(d)}k-\sum_{i=1}^d c_i
=2^{b(d)}k\lambda_0\in\mathbb Z_{\ge0}.
\]
Therefore
\[
2^{b(d)}x=\sum_{i=0}^d c_i v_i,
\]
which is precisely a sum of \(2^{b(d)}k\) lattice points of \(P\), counted with repetition.

## Low-dimensional sharpness

For \(d\le2\), the theorem gives exponent \(0\).

For every \(d\ge3\), exponent \(0\) cannot work uniformly. Let
\[
T_\triangle=
\operatorname{conv}\{000,110,101,011\}\subseteq\mathbb R^3.
\]
This is a type \(D\), hence type \(B\), delta-matroid polytope. The point \(111\) lies in \(2T_\triangle\) because
\[
\frac{111}{2}
=\frac14(000+110+101+011),
\]
but \(111\) is not a sum of two lattice points of \(T_\triangle\). Thus \(T_\triangle\) is not IDP. Taking
\[
T_\triangle\times[0,1]^{d-3}
\]
preserves type \(B\) edge directions and preserves this obstruction after projection, giving \(\mu_d\ge1\) for every \(d\ge3\).

Combining this with the upper bound gives
\[
\mu_3=\mu_4=1.
\]

## Relation to prior work

Vallée proves that every integral type \(B\) generalized permutohedron admits a regular dyadic triangulation and deduces a uniform dyadic decomposition exponent \(m_n\) in each ambient dimension. The published proof chooses \(m_n\) from the largest normalized volume among finitely many simplices and does not give an explicit bound. The argument above replaces quotient order by quotient exponent, strengthens the type \(B\) lattice step from unspecified \(2\)-primary torsion to exponent \(2\), and tracks how exponent can grow through joins.

Morales gives explicit nonnormal delta-matroid polytopes and, separately, records the tetrahedral obstruction above to ordinary integer decomposition. These establish that exponent \(0\) is genuinely impossible from dimension three onward.

To the best of our knowledge, no source located states the bound
\[
m\le\left\lfloor\frac{d-1}{2}\right\rfloor
\]
for type \(B\) generalized permutohedra, nor the stronger simplex-quotient exponent estimate used to obtain it.

## Limitations

The bound is not claimed optimal for \(d\ge5\). The presently established universal interval is
\[
1\le\mu_d\le\left\lfloor\frac{d-1}{2}\right\rfloor\qquad(d\ge3),
\]
with equality determined here only for \(d=3,4\).

The result concerns the dyadic decomposition property, not ordinary normality or IDP. It does not turn the triangulations into unimodular triangulations, and it does not bound their normalized volumes by \(2^{b(d)}\): the order of a simplex quotient can be much larger than its exponent.

The motivating preprint is very recent, so unindexed parallel work remains a residual originality risk.

## References

1. Mathieu Vallée, *Regular dyadic triangulations of delta-matroid polytopes*, arXiv:2609.18331 (2026). https://arxiv.org/abs/2609.18331
2. Santiago Morales, *Most \((0,1)\)-polytopes are not normal*, arXiv:2609.02778 (2026). https://arxiv.org/abs/2609.02778
