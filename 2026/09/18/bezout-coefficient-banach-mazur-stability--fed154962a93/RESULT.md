# Explicit Banach--Mazur stability from the Bézout mixed-volume coefficient

## Statement

Let \(K\subset\mathbb R^n\), \(n\ge 2\), be a full-dimensional convex body. Define its optimal two-body Bézout coefficient by
\[
\beta(K)=\inf\left\{c\ge 0:
V_n(K)V_n(K[n-2],A,B)
\le c\,V_n(K[n-1],A)V_n(K[n-1],B)
\quad\text{for all convex }A,B
\right\}.
\]
Fenchel's inequality and the choice \(A=B=K\) give \(1\le\beta(K)\le2\).
Langharst--Wang (2026) proved that \(\beta(K)=1\) if and only if \(K\) is a simplex.

Put
\[
\phi_n(b)=1-\left(1-b^{1-n}\right)^{1/n},\qquad 1\le b\le2,
\]
and
\[
J_n(a)=\int_0^1(1-at)^n t^{n-1}\,dt
       =\sum_{j=0}^n(-1)^j\binom nj\frac{a^j}{n+j}.
\]
Then the following quantitative strengthening holds.

**Theorem.** If \(b=\beta(K)\), then:

1. For every full-dimensional convex body \(M\),
   \[
   \frac{r(K,M)V_n(K[n-1],M)}{V_n(K)}\ge \phi_n(b).
   \]

2. For every \(v\in\mathbb S^{n-1}\), if \(\ell_K(v)\) is the longest chord of \(K\) parallel to \(v\), then
   \[
   \frac{\ell_K(v)V_{n-1}(P_{v^\perp}K)}{nV_n(K)}\ge \phi_n(b).
   \]

3. Writing \(DK=K-K\),
   \[
   \frac{V_n(DK)}{V_n(K)}
   \ge
   \frac{1}{n\,b^{\,n-1}J_n(\phi_n(b))}.
   \]

Consequently, with \(C_n=\binom{2n}{n}\) and
\[
\Psi_n(b)=
1-\frac{1}{C_n\,n\,b^{\,n-1}J_n(\phi_n(b))},
\]
the Rogers--Shephard deficit
\[
\varepsilon_{\rm RS}(K)
=
1-\frac{V_n(DK)}{C_nV_n(K)}
\]
satisfies \(0\le\varepsilon_{\rm RS}(K)\le\Psi_n(\beta(K))\). Böröczky's sharp-order stability theorem for Rogers--Shephard therefore gives the explicit global estimate
\[
\boxed{
d_{\rm BM}(K,\Delta_n)
\le
1+n^{50n^2}\Psi_n(\beta(K)),
}
\]
where \(\Delta_n\) is any \(n\)-simplex.

In particular, as \(\varepsilon\downarrow0\),
\[
\Psi_n(1+\varepsilon)
=
n(n-1)^{1/n}\varepsilon^{1/n}
+O_n(\varepsilon^{2/n}),
\]
and hence
\[
\boxed{
d_{\rm BM}(K,\Delta_n)
\le
1+n^{50n^2+1}(n-1)^{1/n}
(\beta(K)-1)^{1/n}
+O_n((\beta(K)-1)^{2/n}).
}
\]
Thus the recently established qualitative characterization \(\beta(K)=1\iff K\) is a simplex admits an explicit Banach--Mazur stability theorem.

## Proof

### 1. Relative inradii

Fix a full-dimensional \(M\), write
\[
r=r(K,M),\qquad K_s=K\ominus sM,\qquad
m=V_n(K[n-1],M).
\]
For \(0\le s<r\), the iterated Alexandrov--Fenchel inequality gives
\[
V_n(K_s[n-1],M)
\le
\frac{V_n(K[n-2],K_s,M)^{n-1}}{m^{n-2}}.
\]
The definition of \(b=\beta(K)\) yields
\[
V_n(K[n-2],K_s,M)
\le
b\,\frac{V_n(K[n-1],K_s)m}{V_n(K)}.
\]
Since \(K_s+sM\subseteq K\),
\[
V_n(K[n-1],K_s)\le V_n(K)-sm.
\]
Combining these inequalities,
\[
V_n(K_s[n-1],M)
\le
b^{n-1}
\frac{m}{V_n(K)^{n-1}}
\bigl(V_n(K)-sm\bigr)^{n-1}.
\]
The inner-parallel-body identity
\[
V_n(K)=n\int_0^rV_n(K_s[n-1],M)\,ds
\]
therefore implies, for
\[
\eta=\frac{rm}{V_n(K)}\le1,
\]
that
\[
1
\le
b^{n-1}n\int_0^\eta(1-t)^{n-1}\,dt
=
b^{n-1}\bigl(1-(1-\eta)^n\bigr).
\]
Hence
\[
(1-\eta)^n\le1-b^{1-n},
\]
which is exactly \(\eta\ge\phi_n(b)\).

### 2. Longest chords

Fix \(v\in\mathbb S^{n-1}\), put
\[
\ell=\ell_K(v),\qquad
K^s=K\cap(K-sv),\qquad
P=V_{n-1}(P_{v^\perp}K),\qquad
q=\frac{P}{nV_n(K)}.
\]
For \(0<s<\ell\), the inclusion
\[
K^s+[0,sv]\subseteq K
\]
and the defining Bézout inequality with \(A=K^s\), \(B=[0,v]\) give, after the standard projection formula,
\[
V_{n-1}\!\left(
(P_{v^\perp}K)[n-2],P_{v^\perp}K^s
\right)
\le
bP(1-qs).
\]
Minkowski's first inequality in \(v^\perp\) then yields
\[
V_{n-1}(P_{v^\perp}K^s)
\le
b^{n-1}P(1-qs)^{n-1}.
\]
The right side is nonnegative for \(s<\ell\), so \(q\ell\le1\). The layer-cake identity
\[
V_n(K)=\int_0^\ell V_{n-1}(P_{v^\perp}K^s)\,ds
\]
gives, with \(\chi=q\ell\),
\[
1
\le
b^{n-1}\bigl(1-(1-\chi)^n\bigr).
\]
Thus \(\chi\ge\phi_n(b)\), proving the second assertion.

### 3. From chords to the difference body

The same estimate retains more information. For \(0\le t\le1\), the covariogram
\[
g_K(x)=V_n(K\cap(K+x))
\]
satisfies
\[
\begin{aligned}
g_K(-t\ell v)
&=\int_{t\ell}^{\ell}
V_{n-1}(P_{v^\perp}K^s)\,ds\\
&\le
b^{n-1}V_n(K)
\left[
(1-\chi t)^n-(1-\chi)^n
\right]\\
&\le
b^{n-1}V_n(K)(1-\phi_n(b)t)^n.
\end{aligned}
\]
The radial function of \(DK\) in direction \(v\) is \(\ell_K(v)\). Using
\[
V_n(K)^2=\int_{\mathbb R^n}g_K(x)\,dx
\]
and polar integration,
\[
\begin{aligned}
V_n(K)^2
&\le
b^{n-1}V_n(K)
\int_{\mathbb S^{n-1}}
\int_0^{\ell_K(v)}
\left(1-\phi_n(b)\frac{r}{\ell_K(v)}\right)^n
r^{n-1}\,dr\,dv\\
&=
b^{n-1}V_n(K)J_n(\phi_n(b))
\int_{\mathbb S^{n-1}}\ell_K(v)^n\,dv\\
&=
n\,b^{n-1}V_n(K)V_n(DK)J_n(\phi_n(b)).
\end{aligned}
\]
This proves the difference-body lower bound.

The classical Rogers--Shephard inequality gives
\[
V_n(DK)\le C_nV_n(K).
\]
At \(b=1\), \(\phi_n(1)=1\) and
\[
J_n(1)=B(n,n+1)=\frac{1}{nC_n},
\]
so the new lower bound agrees exactly with the simplex equality value. In general it yields
\[
\varepsilon_{\rm RS}(K)\le\Psi_n(b).
\]
Böröczky proved that
\[
V_n(DK)=(1-\delta)C_nV_n(K)
\quad\Longrightarrow\quad
d_{\rm BM}(K,\Delta_n)\le1+n^{50n^2}\delta.
\]
Substituting \(\delta=\varepsilon_{\rm RS}(K)\le\Psi_n(b)\) proves the global Banach--Mazur estimate.

Finally, if \(b=1+\varepsilon\), then
\[
1-\phi_n(b)
=
(1-b^{1-n})^{1/n}
=
((n-1)\varepsilon)^{1/n}(1+O_n(\varepsilon)).
\]
Also
\[
J_n(1)=\frac1{nC_n},
\qquad
J_n'(1)=-nJ_n(1).
\]
Taylor expansion of the explicit formula for \(\Psi_n\) gives
\[
\Psi_n(1+\varepsilon)
=
n(n-1)^{1/n}\varepsilon^{1/n}
+O_n(\varepsilon^{2/n}),
\]
as claimed.

## Relation to prior work

Soprunov and Zvavitch introduced the mixed-volume Bézout inequalities and conjectured that the unit constant characterizes simplices. Subsequent work established several partial and variant characterizations. Langharst and Wang proved the full \(r=2\) conjecture in all dimensions in arXiv:2609.20380 (submitted 17 September 2026). Their proof already highlights a structural connection with Chakerian's proof of the Rogers--Shephard inequality and gives exact longest-chord and relative-inradius characterizations.

The result above retains the optimal Bézout coefficient throughout those integral arguments. The additional step is a quantitative covariogram estimate that converts near-unit Bézout coefficient into a near-maximal Rogers--Shephard ratio, after which Böröczky's 2005 Rogers--Shephard stability theorem converts that deficit into Banach--Mazur distance from a simplex.

To the best of our knowledge, targeted searches of the Bézout mixed-volume literature, Rogers--Shephard stability literature, and exact/synonymous formulations did not locate a prior inequality bounding the Rogers--Shephard deficit or Banach--Mazur distance in terms of the optimal two-body Bézout coefficient.

## Limitations

The exponent \(1/n\) and the displayed constants are not claimed optimal. The factor \(n^{50n^2}\) is inherited from Böröczky's general Rogers--Shephard stability theorem and is very large. The result gives a quantitative implication from the Bézout coefficient to simplex proximity; it does not provide a matching converse estimate for \(\beta(K)-1\) in terms of Banach--Mazur distance.

The motivating all-dimensional characterization is extremely recent, so unindexed or unpublished parallel work remains a residual originality risk.

## References

1. D. Langharst and S. Wang, *The Bézout inequality for mixed volumes characterizes simplices*, arXiv:2609.20380 (2026), https://arxiv.org/abs/2609.20380.
2. I. Soprunov and A. Zvavitch, *Bezout inequality for mixed volumes*, International Mathematics Research Notices (2016), DOI: 10.1093/imrn/rnv390.
3. K. Böröczky, Jr., *The stability of the Rogers--Shephard inequality and of some related inequalities*, Advances in Mathematics 190 (2005), 47--76, DOI: 10.1016/j.aim.2003.11.015.
