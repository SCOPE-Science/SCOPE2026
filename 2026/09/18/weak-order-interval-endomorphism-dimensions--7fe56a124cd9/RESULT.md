# Exact interval-endomorphism dimensions for finite weak orders

Let
\[
P=A_1\oplus A_2\oplus\cdots\oplus A_h,\qquad h\ge 2,
\]
be the ordinal sum of nonempty antichains, with \(|A_i|=n_i\). Equivalently, \(P\) is a finite connected weak-order poset (also called a complete multipartite order) with level sizes \(n_1,\dots,n_h\). Let
\[
\Lambda_P=\operatorname{End}_P\!\left(\bigoplus_{S\in\operatorname{Int}(P)} I_S\right)^{\mathrm{op}}
\]
be the interval endomorphism algebra over a field \(k\).

Toshitaka Aoki proved that
\[
\operatorname{gldim}\Lambda_P=\Omega(P),
\]
where \(\Omega(P)\) is the maximum of
\[
\bar\omega(S,C)=|\operatorname{Max}(C\setminus S)|+|\operatorname{Min}(S\setminus C)|
\]
over saturated pairs of intervals \((S,C)\), and that for \(|P|>1\)
\[
\operatorname{int-res-gldim}_k P=\Omega(P)-2.
\]
The result below evaluates \(\Omega(P)\) exactly for every finite weak order.

## Theorem

For positive integers \(a,b\), define
\[
F(a,b)=
\begin{cases}
2,&a=b=1,\\
a+b-1,&\min(a,b)\le 2\text{ and }(a,b)\ne(1,1),\\
a+b-2,&\min(a,b)\ge3.
\end{cases}
\]
Then
\[
\boxed{
\Omega(P)=
\max\!\left
\{
\max_{1\le i<h}F(n_i,n_{i+1}),
\quad
\max_{\substack{1\le i<j\le h\\j-i\ge2}}(n_i+n_j)
\right\},
}
\]
where the second maximum is omitted when \(h=2\). Consequently,
\[
\boxed{\operatorname{gldim}\Lambda_P=\Omega(P)},
\qquad
\boxed{\operatorname{int-res-gldim}_k P=\Omega(P)-2}.
\]
In particular these dimensions are independent of the coefficient field.

### Height two

For the complete two-level poset with level sizes \(a,b\),
\[
\operatorname{gldim}\Lambda_P=F(a,b).
\]
Thus, apart from the two-point chain, a side of size at most two gives the sharp value \(|P|-1\), while if both levels have size at least three the value drops to \(|P|-2\).

### Uniform weak orders

If all \(h\ge3\) levels have the same size \(r\), then
\[
\boxed{\operatorname{gldim}\Lambda_P=2r},
\qquad
\boxed{\operatorname{int-res-gldim}_k P=2r-2},
\]
independently of the number of levels. Thus the interval-resolution global dimension stabilizes immediately once a third level is present.

### Equality in the universal bound

Let \(N=|P|\ge3\). Aoki's general bound gives \(\operatorname{gldim}\Lambda_P\le N-1\). Within finite weak orders, equality holds exactly in the following cases:

- \(h=2\) and \(\min(n_1,n_2)\le2\);
- \(h=3\) and \(n_2=1\).

## Proof

Write \(T_r=T\cap A_r\) for a subset \(T\subseteq P\).

### 1. Intervals in a weak order

A non-singleton interval meets at least two levels. If its lowest and highest occupied levels are \(i<j\), convexity forces every intermediate level \(A_{i+1},\dots,A_{j-1}\) to be present in full, while the endpoint pieces \(T_i\subseteq A_i\) and \(T_j\subseteq A_j\) may be arbitrary nonempty subsets. Conversely every subset of this form is a connected convex interval. A one-level interval is necessarily a singleton.

Now let \((S,C)\) be saturated and put \(T=S\cup C\). By Aoki's characterization, \(S\) is a relative downset of \(T\), \(C\) is a relative upset of \(T\), both boundary conditions are extremal, and \(T\) is the unique member of \(W(S,C)\).

If \(x\in\operatorname{Max}(C\setminus S)\) were not maximal in \(T\), choose \(y\in T\) with \(x<y\). Since \(C\) is an upset, \(y\in C\). If \(y\in S\), downward closure of \(S\) would force \(x\in S\), a contradiction; hence \(y\in C\setminus S\), contradicting maximality of \(x\). Therefore
\[
\operatorname{Max}(C\setminus S)\subseteq\operatorname{Max}(T).
\]
Dually,
\[
\operatorname{Min}(S\setminus C)\subseteq\operatorname{Min}(T).
\]
If \(T\) spans levels \(i<j\), this yields
\[
\bar\omega(S,C)\le |T_i|+|T_j|.
\tag{1}
\]

### 2. Nonadjacent endpoint levels

Suppose \(j-i\ge2\). From (1),
\[
\bar\omega(S,C)\le n_i+n_j.
\]
This bound is attained. Take the full interval
\[
T=A_i\cup A_{i+1}\cup\cdots\cup A_j,
\]
and set
\[
S=T\setminus A_j,\qquad C=T\setminus A_i.
\]
Both are intervals; \(S\) is a relative downset and \(C\) a relative upset of \(T\), with extremal boundaries \(A_j\) and \(A_i\). Any proper interval properly containing \(T\) must extend below \(A_i\) or above \(A_j\). The former destroys downward closure of \(S\), and the latter destroys upward closure of \(C\). Hence \(W(S,C)=\{T\}\), so the pair is saturated and
\[
\bar\omega(S,C)=n_i+n_j.
\tag{2}
\]

### 3. Adjacent endpoint levels

Suppose \(T=U\cup V\) spans two adjacent levels, with \(|U|=a\) below \(|V|=b\). A connected relative downset \(S\) is of one of two types:

1. \(S=\{u\}\) for some \(u\in U\); or
2. \(S=U\cup V_S\) with \(\varnothing\ne V_S\subseteq V\).

Dually, a connected relative upset \(C\) is either an upper singleton \(\{v\}\), or \(C=U_C\cup V\) with \(\varnothing\ne U_C\subseteq U\).

If both \(S\) meets \(V\) and \(C\) meets \(U\), then
\[
\bar\omega(S,C)
=(a-|U_C|)+(b-|V_S|)
\le a+b-2.
\tag{3}
\]
If \(S=\{u\}\), then the largest possible value is \(b\) when \(a=1\), and \(b+1\) when \(a\ge2\). The order-dual bounds are \(a\) when \(b=1\), and \(a+1\) when \(b\ge2\). If both are opposite singletons, the value is \(2\). Taking the maximum of these possibilities gives exactly \(F(a,b)\). The function \(F\) is nondecreasing in each argument, so allowing only partial endpoint subsets cannot exceed \(F(n_i,n_{i+1})\).

For the full adjacent levels \(U=A_i\), \(V=A_{i+1}\), every case of \(F(a,b)\) is attained by a saturated pair:

- if \(a=b=1\), take the two opposite singletons;
- if \(a=1<b\), take \(S=U\) and \(C=T\); use the order-dual choice when \(b=1<a\);
- if \(a=2\le b\), choose \(u_0\in U\) and take \(S=\{u_0\}\), \(C=(U\setminus\{u_0\})\cup V\); use the dual construction when \(b=2\le a\);
- if \(a,b\ge3\), choose \(u_0\in U\), \(v_0\in V\) and take
\[
S=U\cup\{v_0\},\qquad C=\{u_0\}\cup V.
\]

The stated relative downset/upset and extremal-boundary conditions are immediate. Since both endpoint levels are full, enlarging \(T\) can only add a lower or upper level; either enlargement violates one of the relative closure conditions. Thus these pairs are saturated. Therefore the optimal adjacent contribution for levels \(i,i+1\) is exactly \(F(n_i,n_{i+1})\).

Combining (2) with the adjacent calculation proves the formula for \(\Omega(P)\). Aoki's Theorem 6.5 and Corollary 6.7 then give the two homological-dimension formulas.

For uniform levels with \(h\ge3\), any two nonadjacent levels contribute \(2r\), while every adjacent contribution is at most \(2r\), proving the uniform formula.

Finally, if \(h=2\), the piecewise formula for \(F\) shows that \(\Omega(P)=N-1\) exactly when \(\min(n_1,n_2)\le2\) (for \(N\ge3\)). If \(h\ge3\), an adjacent contribution can equal \(N-1\) only in the degenerate all-singleton three-level case, which is contained in the next condition. A nonadjacent contribution \(n_i+n_j\) equals \(N-1\) exactly when there is precisely one omitted element; this forces \(h=3\), \(i=1\), \(j=3\), and \(n_2=1\). This proves the equality characterization. \(\square\)

## Verification

The accompanying script `artifacts/check_small_weak_orders.py` independently enumerates all intervals, computes Aoki's sets \(W(S,C)\) directly from the definitions, identifies saturated pairs, and compares the resulting \(\Omega(P)\) with the closed formula for all level profiles \((n_1,\dots,n_h)\) with \(2\le h\le4\), \(1\le n_i\le3\), and total size at most nine. The check returns no mismatches. This finite computation is supporting evidence only; the theorem is proved above for arbitrary level sizes.

## Literature context and originality boundary

Aoki's 2026 preprint proves the saturated-pair formula for all finite connected posets, derives the field-independent global dimension, and works out rectangular grids explicitly. Those results are prior work and are the input to the theorem here. Asashiba--Escolar--Nakashima--Yoshiwaki established finiteness and the relative-Auslander framework for interval-resolution global dimension, while Aoki--Escolar--Tada proved monotonicity under full-subposet inclusion and classified the zero-dimensional case; these are also prior work.

To the best of our knowledge, targeted searches for `weak order`, `ordinal sum of antichains`, `complete bipartite poset`, `complete multipartite order`, and synonymous formulations together with `interval endomorphism algebra` or `interval resolution global dimension` did not locate the closed formula above, the height-two threshold, or the uniform-height stabilization. The full texts of the three most directly relevant arXiv papers listed below were inspected for these formulations. Because the main input is a very recent first-version preprint and the specialization is combinatorial, an equivalent calculation could still exist under different terminology in the broader persistence or poset-representation literature.

## References

1. T. Aoki, *Interval endomorphism algebras of posets: Reedy structure, combinatorics, and homological theory*, arXiv:2609.15927v1 (2026). https://arxiv.org/abs/2609.15927
2. H. Asashiba, E. G. Escolar, K. Nakashima, M. Yoshiwaki, *Approximation by interval-decomposables and interval resolutions of persistence modules*, J. Pure Appl. Algebra 227 (2023), 107397; arXiv:2207.03663. https://arxiv.org/abs/2207.03663
3. T. Aoki, E. G. Escolar, S. Tada, *Summand-injectivity of interval covers and monotonicity of interval resolution global dimensions*, J. Appl. Comput. Topol. 9 (2025); arXiv:2308.14979. https://arxiv.org/abs/2308.14979
4. M. Pouzet, I. Zaguia, *Weak orders admitting a perpendicular linear order*, Discrete Math. 307 (2007), 97--107. https://doi.org/10.1016/j.disc.2006.05.038
