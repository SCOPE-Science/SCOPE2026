# Residue classes control joins in localization-cone field orders

## Statement

Let \(E\) be a field, let \(R\subseteq E\) be a subring, let \(0\neq t\in R\), and assume
\[
1\notin tR,\qquad E=R[t^{-1}].
\]
Let \(F\subseteq R\) be a totally ordered subfield. Following Wang–Yuan–Zhang–Zhu, define
\[
P_R=\{0\}\cup\bigcup_{n\in\mathbb Z}t^{-n}(F_{>0}+tR).
\]
Their localization theorem shows that \(P_R\) is the positive cone of a directed ring order on \(E\), and that every nonzero positive element has positive inverse.

The order has a sharper structural description.

### Theorem

For every \(0\neq x\in E\), the integer
\[
\nu_t(x)=\max\{j\in\mathbb Z:x\in t^jR\}
\]
exists. Define its leading residue
\[
\rho_t(x)=t^{-\nu_t(x)}x+tR\in (R/tR)\setminus\{0\}.
\]
Then
\[
x\in P_R\setminus\{0\}
\quad\Longleftrightarrow\quad
\rho_t(x)\in F_{>0}\subseteq R/tR.
\]

Consequently, for \(a\neq b\),
\[
a\preceq b
\quad\Longleftrightarrow\quad
\rho_t(b-a)\in F_{>0}.
\]

More strongly, if \(a\) and \(b\) are incomparable, then their set of common upper bounds has no minimal element, and their set of common lower bounds has no maximal element. In particular, neither \(a\vee b\) nor \(a\wedge b\) exists.

Hence the following are equivalent:
\[
\boxed{
\begin{array}{c}
(E,P_R)\text{ is a lattice-ordered field}\\
\Updownarrow\\
(E,P_R)\text{ is totally ordered}\\
\Updownarrow\\
R=F+tR\\
\Updownarrow\\
R/tR\cong F.
\end{array}}
\]
Under these equivalent conditions, \(R\) is a discrete valuation ring with uniformizer \(t\), maximal ideal \(tR\), residue field \(F\), and fraction field \(E\).

Thus the localization construction has a strict dichotomy: it is either a total order arising from a discrete-valuation first layer, or every incomparable pair fails to have even a minimal common upper bound.

## Proof

### 1. Finite \(t\)-depth is automatic

First,
\[
\bigcap_{n\ge 0}t^nR=\{0\}.
\]
Indeed, suppose \(0\neq x\) lies in every \(t^nR\). Since \(E=R[t^{-1}]\),
\[
x^{-1}=t^{-m}y
\]
for some \(m\ge0\) and \(y\in R\). Since \(x\in t^{m+1}R\), write
\[
x=t^{m+1}z,\qquad z\in R.
\]
Then
\[
1=xx^{-1}=tzy\in tR,
\]
contrary to \(1\notin tR\).

Now take \(0\neq x\in E\). Some \(m\ge0\) satisfies \(t^mx\in R\), so the set
\[
\{j\in\mathbb Z:x\in t^jR\}
\]
is nonempty. If it were unbounded above, then \(t^mx\) would belong to every sufficiently high power of \(tR\), contradicting the preceding intersection statement. Thus \(\nu_t(x)\) exists.

By maximality,
\[
u=t^{-\nu_t(x)}x\in R\setminus tR,
\]
so \(\rho_t(x)=u+tR\) is nonzero.

### 2. Positivity is exactly positivity of the leading residue

If
\[
x=t^{-n}(a+tr),\qquad a\in F_{>0},\ r\in R,
\]
then \(a+tr\notin tR\), because \(F\cap tR=\{0\}\). Therefore
\[
\nu_t(x)=-n,\qquad \rho_t(x)=a+tR.
\]
Thus \(x>0\) implies \(\rho_t(x)\in F_{>0}\).

Conversely, if \(\rho_t(x)=a+tR\) with \(a\in F_{>0}\), then
\[
t^{-\nu_t(x)}x=a+tr
\]
for some \(r\in R\), hence
\[
x=t^{\nu_t(x)}(a+tr)\in P_R\setminus\{0\}.
\]
This proves the leading-residue criterion.

Translation gives the comparison criterion for \(a,b\).

### 3. Every incomparable pair has no minimal common upper bound

It is enough to consider \(0\) and an incomparable nonzero element \(x\). Multiplication by any power of \(t\) is an order automorphism, since every \(t^j\) and \(t^{-j}\) is positive. Thus we may normalize
\[
x\in R\setminus tR,\qquad x+tR\notin F.
\]

Let \(u\) be any common upper bound of \(0\) and \(x\). Directedness guarantees that such \(u\) exists. Then
\[
u\in P_R\setminus\{0\},\qquad u-x\in P_R\setminus\{0\}.
\]
We claim that \(u\notin R\). If \(u\in R\), then the localization construction gives
\[
P_R\cap R\subseteq F_{\ge0}+tR.
\]
Hence the residues of both \(u\) and \(u-x\) lie in \(F\), forcing the residue of \(x\) to lie in \(F\), a contradiction.

Therefore \(u\notin R\). Write its unique positive form as
\[
u=t^{-n}(a+tr),\qquad n\ge1,\ a\in F_{>0},\ r\in R.
\]
Choose any \(\lambda\in F\) with \(0<\lambda<1\), for example \(\lambda=\tfrac12\). Then
\[
\lambda u>0
\]
and
\[
\lambda u-x
=t^{-n}\!\left(\lambda a+t(\lambda r-t^{n-1}x)\right)>0.
\]
Thus \(\lambda u\) is still a common upper bound. But
\[
u-\lambda u=(1-\lambda)u>0,
\]
so \(\lambda u\prec u\).

Hence every common upper bound can be strictly lowered while remaining a common upper bound. There is no minimal common upper bound, and therefore no least upper bound. Applying the same argument after negation shows that every common lower bound can be strictly raised; hence there is no maximal common lower bound.

Translation restores the assertion for arbitrary incomparable \(a,b\).

### 4. Totality and the residue quotient

If \(R/tR\cong F\), then every nonzero leading residue lies in \(F^\times\), hence is either positive or negative. The leading-residue criterion therefore makes every two elements comparable, so the order is total.

Conversely, if \(R/tR\) properly contains the image of \(F\), choose
\[
x\in R\setminus tR
\]
whose residue is not in \(F\). Then neither \(x\) nor \(-x\) is positive, so \(0\) and \(x\) are incomparable. Thus the order is not total; by the preceding section it is not a lattice order.

Since Lemma 2.1 of Wang–Yuan–Zhang–Zhu gives \(F\cap tR=\{0\}\), the natural map \(F\to R/tR\) is injective. Hence its surjectivity is exactly
\[
R=F+tR.
\]

### 5. The total case forces a DVR

Assume \(R=F+tR\). If \(u\in R\setminus tR\), write
\[
u=a+tr,\qquad a\in F^\times.
\]
Then
\[
u=a(1+t a^{-1}r),
\]
and \(1+tR\subseteq R^\times\) by the localization lemma. Thus every element outside \(tR\) is a unit.

For \(0\neq r\in R\), finite \(t\)-depth gives
\[
r=t^q u
\]
with \(q\ge0\) and \(u\in R\setminus tR=R^\times\). Therefore every nonzero element is a unit times a power of \(t\). It follows that \(R\) is local with maximal ideal \(tR\), and every nonzero ideal is generated by a power of \(t\). Hence \(R\) is a discrete valuation ring with uniformizer \(t\). Its residue field is \(R/tR\cong F\), and its fraction field is \(R[t^{-1}]=E\).

## Consequences

### A. Every residue direction is a no-join witness

If
\[
\bar x\in (R/tR)\setminus F,
\]
then any representative \(x\in R\) of \(\bar x\) is incomparable with \(0\), and the pair \(\{0,x\}\) has neither a join nor a meet. In fact its common upper bounds have no minimal element.

This upgrades the single explicit nonlattice witness in the recent complex-field construction to a complete mechanism: every first residue direction outside the ordered coefficient field obstructs joins.

### B. The complex-field construction already has real no-join witnesses

In the construction of arXiv:2609.20494v1, \(F=\mathbb A\) is the field of real algebraic numbers, while the integral closure \(\mathcal O_T\) contains the transcendental coefficient field \(k\). For any \(b\in k\setminus\mathbb A\), the class of \(b\) modulo \(t_T\mathcal O_T\) cannot lie in \(\mathbb A\): otherwise \(b-a\in t_T\mathcal O_T\) for some \(a\in\mathbb A\), while \(b-a\) lies in the subfield \(k(\mathbb A)\subseteq\mathcal O_T\), contradicting Lemma 2.1 applied to that subfield.

Hence \(0\) and such a real transcendental \(b\) have no join and no meet. The nonlattice phenomenon is therefore already visible on real elements; the imaginary-unit witness of Proposition 2.7 is one instance of a broader residue obstruction.

### C. The universal construction is automatically nonlattice in transcendence degree at least two

In Corollary 2.6 of arXiv:2609.20494v1, the ordered coefficient field is \(\mathbb Q\), while the integral-closure ring contains
\[
k_0=\mathbb Q(\mathcal T\setminus\{\theta\}).
\]
If
\[
\operatorname{trdeg}_{\mathbb Q}E\ge2,
\]
then \(k_0\neq\mathbb Q\). Any \(c\in k_0\setminus\mathbb Q\) gives a residue class outside \(\mathbb Q\), so the resulting directed order is nonlattice and \(\{0,c\}\) has no minimal common upper bound.

Thus the only possible total cases of that universal construction occur in transcendence degree one.

### D. Finite algebraic extensions of an ordered rational function field

Let \(F\) be a totally ordered field, put
\[
D=F[t]_{(t)},\qquad K=F(t),
\]
and let \(L/K\) be a finite algebraic extension. Let \(R\) be the integral closure of \(D\) in \(L\), and form the localization cone with coefficient field \(F\).

Then
\[
\boxed{
P_R\text{ is a lattice order}
\iff
P_R\text{ is total}
\iff
L=F(t).
}
\]

Indeed, if the cone were total, the theorem would make \(R\) a DVR with uniformizer \(t\) and residue field \(F\). Since \(F\) has characteristic zero, \(L/K\) is separable. For the integral closure of a DVR in a finite separable extension, the standard degree formula is
\[
[L:K]=\sum_i e_if_i.
\]
Here totality forces a single prime above \(t\), ramification index \(e=1\), and residue degree \(f=1\), hence \([L:K]=1\). The converse is the ordinary \(t\)-adic lexicographic order on \(F(t)\).

So every nontrivial finite algebraic extension produces a genuinely partial directed order in this construction, and every incomparable pair in that order lacks joins and meets.

## Relation to prior work

Wang–Yuan–Zhang–Zhu introduced the localization cone above and proved directedness, unique positive levels and leading coefficients, and closure of nonzero positives under inversion. Their Remark after Theorem 2.2 explicitly allows \(R/tR\) to be larger than the coefficient field, and Proposition 2.7 proves that \(0\) and \(i\) have no least upper bound for their complex-field family.

The classical implication
\[
\text{division-closed lattice-ordered field}\Longrightarrow\text{total order}
\]
is prior work: it appears in the ordered-ring literature and is discussed, for example, by Yang and by Ma–McGovern. It is not claimed here.

The new claim is the exact residue-level description of comparability and joins for the 2026 localization construction: every incomparable pair has no minimal upper bound or maximal lower bound, and totality is equivalent to the single algebraic condition \(R/tR=F\), equivalently to the DVR boundary above.

## Limitations

The theorem applies to the localization cones satisfying
\[
1\notin tR,\qquad E=R[t^{-1}]
\]
and does not classify arbitrary directed partial orders on fields. In particular, it does not resolve the Birkhoff–Pierce problem for \(\mathbb C\).

The finite-extension corollary uses the integral closure of \(F[t]_{(t)}\) in a finite algebraic extension. Infinite algebraic extensions may admit immediate valuation-theoretic behavior not covered by that corollary, although the main residue criterion still applies whenever the localization hypotheses hold.

Originality is asserted only to the best of our knowledge. The valuation-theoretic total-order case is closely related to classical Baer–Krull and ordered-valuation constructions; the claim does not include those classical facts. Older ordered-field literature may contain an equivalent residue formulation that was not located.

## References

1. W. Wang, R. Yuan, Y. Zhang, Y. Zhu, *Directed partial orders on the complex number field*, arXiv:2609.20494v1 (2026). https://arxiv.org/abs/2609.20494v1
2. Y. Yang, *A lattice-ordered skew-field is totally ordered if squares are positive*, arXiv:math/0505365; Amer. Math. Monthly 113 (2006), 265–266. https://arxiv.org/abs/math/0505365
3. J. Ma, W. W. McGovern, *Division closed partially ordered rings*, Algebra Universalis 78 (2017), 515–532. https://doi.org/10.1007/s00012-017-0467-7
4. N. Schwartz, Y. Yang, *Fields with directed partial orders*, J. Algebra 336 (2011), 342–348. https://doi.org/10.1016/j.jalgebra.2011.04.016
5. The Stacks Project, Section 15.112, *Extensions of discrete valuation rings*, especially Remark 15.112.6. https://stacks.math.columbia.edu/tag/09E8
