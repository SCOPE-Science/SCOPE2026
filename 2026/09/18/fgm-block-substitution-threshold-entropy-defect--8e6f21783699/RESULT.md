# Exact FGM thresholds and entropy defects for blockwise copula substitution

## Statement

Let
\[
\Phi_\theta(u,v)=uv\{1+\theta(1-u)(1-v)\},\qquad |\theta|\le 1,
\]
be the bivariate Farlie--Gumbel--Morgenstern (FGM) copula, and let
\[
\Pi_m(x_1,\ldots,x_m)=\prod_{i=1}^m x_i
\]
be the \(m\)-dimensional independence copula. Consider the blockwise substitution
\[
F_{m,\theta}(x_1,\ldots,x_m,v)
=
\Phi_\theta(\Pi_m(x_1,\ldots,x_m),v).
\]

This is a basic test case for proposals that substitute multivariate copulas directly into the scalar arguments of another copula.

### Theorem 1: exact admissibility threshold

For every integer \(m\ge 1\),
\[
\boxed{
F_{m,\theta}\text{ is an }(m+1)\text{-copula}
\iff
|\theta|\le \frac{1}{2^m-1}.
}
\]

Its full mixed derivative is
\[
\boxed{
g_{m,\theta}(x_1,\ldots,x_m,v)
=
1+\theta(1-2^m\Pi_m(x))(1-2v).
}
\]

Hence the obstruction is sharp. In particular, for \(m=2\) and \(\theta=1/2\), both factors are bounded absolutely continuous copulas with bounded densities, but
\[
g_{2,1/2}(x,y,v)=1+\frac12(1-4xy)(1-2v)
\]
has infimum \(-1/2\); the substituted function is therefore not a copula.

For every fixed nonzero FGM parameter, admissibility is eventually lost as the independence block dimension grows.

### Theorem 2: the correct differential operator for an independence block

Let \(C\) be a sufficiently smooth bivariate copula with density
\[
c(u,v)=\partial_u\partial_v C(u,v),
\]
and set
\[
F_m(x_1,\ldots,x_m,v)=C\!\left(\prod_{i=1}^m x_i,v\right).
\]
Then
\[
\boxed{
\partial_{x_1}\cdots\partial_{x_m}\partial_v F_m
=
(1+u\partial_u)^{m-1}c(u,v)
\bigg|_{u=\prod_i x_i}.
}
\]

Consequently, under the stated smoothness,
\[
\boxed{
F_m\text{ is a copula}
\iff
(1+u\partial_u)^{m-1}c(u,v)\ge0
\quad\text{for }(u,v)\in(0,1)^2.
}
\]

Thus direct substitution of a genuinely multivariate distribution function into a scalar copula argument does not obey the ordinary univariate chain-rule density formula. The higher mixed derivatives are exactly encoded by powers of the Euler operator \(u\partial_u\).

### Theorem 3: strict entropy defect inside the admissible region

For an absolutely continuous copula with density \(g\), write
\[
H(g)=-\int g\log g.
\]
The independence copula has entropy zero.

For every \(m\ge2\) and
\[
0<|\theta|<\frac{1}{2^m-1},
\]
the valid copula \(F_{m,\theta}\) satisfies
\[
\boxed{
H(F_{m,\theta})<H(\Phi_\theta)+H(\Pi_m)
=H(\Phi_\theta).
}
\]

More quantitatively,
\[
\boxed{
H(\Phi_\theta)-H(F_{m,\theta})
\ge
\frac{2\theta^2}
{9\{1+|\theta|(2^m-1)\}}
\left[
\left(\frac43\right)^{m-1}-1
\right].
}
\]

For example, \(m=2,\theta=1/4\) lies strictly inside the copula-admissible range and all relevant densities are bounded and strictly positive, yet
\[
\boxed{
H(F_{2,1/4})
\le
H(\Phi_{1/4})-\frac1{378}.
}
\]

Thus failure of entropy additivity is logically separate from failure of copula closure: it persists even for a valid bounded positive composite.

## Proof

### 1. Exact FGM threshold

Write
\[
U=\Pi_m(x)=\prod_{i=1}^m x_i.
\]
Then
\[
F_{m,\theta}
=
Uv+\theta(U-U^2)(v-v^2).
\]
Since
\[
\partial_{x_1}\cdots\partial_{x_m}U=1,
\qquad
\partial_{x_1}\cdots\partial_{x_m}U^2=2^mU,
\]
and
\[
\partial_v(v-v^2)=1-2v,
\]
the full mixed derivative is
\[
g_{m,\theta}=1+\theta(1-2^mU)(1-2v).
\]

Now
\[
1-2^mU\in[-(2^m-1),1],
\qquad
1-2v\in[-1,1],
\]
and their product ranges over the full interval
\[
[-(2^m-1),\,2^m-1].
\]
Therefore \(g_{m,\theta}\ge0\) everywhere exactly when
\[
|\theta|(2^m-1)\le1.
\]

The function \(F_{m,\theta}\) is grounded. If all coordinates except \(x_i\) are set to one, then
\[
F_{m,\theta}(1,\ldots,x_i,\ldots,1,1)=\Phi_\theta(x_i,1)=x_i,
\]
and similarly the \(v\)-margin is uniform. Hence nonnegativity of the continuous full mixed derivative is sufficient and necessary for the copula property. This proves the threshold.

### 2. Euler-operator identity

For any smooth scalar function \(h\) and \(U=\prod_i x_i\), introduce \(y_i=\log x_i\). Since \(U=e^{y_1+\cdots+y_m}\),
\[
\partial_{x_1}\cdots\partial_{x_m}h(U)
=
U^{-1}(u\partial_u)^m h(u)\big|_{u=U}.
\]
The elementary identity
\[
u^{-1}(u\partial_u)^m h(u)
=
(1+u\partial_u)^{m-1}h'(u)
\]
then gives
\[
\partial_{x_1}\cdots\partial_{x_m}\partial_v C(U,v)
=
(1+u\partial_u)^{m-1}c(u,v)\big|_{u=U}.
\]

Groundedness and all one-dimensional uniform margins hold automatically because \(C\) is a copula. Under the smoothness assumption, the composite is therefore a copula exactly when the displayed full mixed derivative is nonnegative.

For the FGM density
\[
c_\theta(u,v)=1+\theta(1-2u)(1-2v),
\]
successive application of \(1+u\partial_u\) sends
\[
1-2u\mapsto 1-4u\mapsto\cdots\mapsto1-2^m u,
\]
recovering Theorem 1.

### 3. Entropy comparison by a mean-preserving spread

Let \(X_1,\ldots,X_m,V\) be independent uniform variables on \([0,1]\). Put
\[
Y_i=2X_i,\qquad
A_m=1-\prod_{i=1}^mY_i,\qquad
B=1-2V.
\]
Then
\[
g_{m,\theta}=1+\theta A_mB.
\]
For \(m\ge2\), write
\[
W=\prod_{i=2}^mY_i.
\]
Because \(\mathbb E W=1\),
\[
\mathbb E[A_m\mid Y_1]=1-Y_1=:A_1.
\]
Thus \(A_m\) is a mean-preserving spread of \(A_1\).

For fixed \(b\), define
\[
q_b(a)=(1+\theta ba)\log(1+\theta ba).
\]
Inside the strict admissible range,
\[
q_b''(a)=\frac{\theta^2b^2}{1+\theta ba}
\ge
\frac{\theta^2b^2}
{1+|\theta|(2^m-1)}.
\]
Conditional Jensen therefore gives
\[
\mathbb E[q_B(A_m)]-\mathbb E[q_B(A_1)]
\ge
\frac{\theta^2}{2\{1+|\theta|(2^m-1)\}}
\mathbb E[B^2]\,
\mathbb E[Y_1^2]\,
\operatorname{Var}(W).
\]
The elementary moments are
\[
\mathbb E B^2=\frac13,\qquad
\mathbb E Y_1^2=\frac43,\qquad
\operatorname{Var}(W)=\left(\frac43\right)^{m-1}-1.
\]
Hence
\[
\int g_{m,\theta}\log g_{m,\theta}
-
\int c_\theta\log c_\theta
\ge
\frac{2\theta^2}
{9\{1+|\theta|(2^m-1)\}}
\left[
\left(\frac43\right)^{m-1}-1
\right].
\]
Changing sign gives the entropy inequality. Strictness follows for \(m\ge2\) and \(\theta\ne0\).

At \(m=2,\theta=1/4\), the right-hand side equals \(1/378\).

## Relation to recent and classical literature

Lu (2026) proposes a symmetric operad on all multivariate copulas using direct blockwise "Sklar substitution", states a product-form density obtained from an ordinary chain rule, and derives additive copula entropy on finite-entropy subfamilies. Theorems 1--3 above give explicit bounded smooth counterexamples to those claims as stated. The density discrepancy is already visible for an independence block: the correct factor is \(1-2^mU\), not the factor obtained by treating the multivariate inner copula as a univariate distribution function.

The underlying reason is classical. If \(X\) has a genuinely multivariate copula \(C\), then \(C(X)\) is generally not uniform; its distribution is the Kendall distribution. Hierarchical Kendall copulas use the Kendall distribution transform precisely to obtain a scalar uniform aggregate before applying a higher-level copula. Brechmann (2014) also records the older obstruction that an arbitrary scalar copula cannot universally link non-overlapping multivariate marginals by naive direct substitution.

There are established alternatives for coupling multivariate blocks. Li, Scarsini and Shaked (1996) introduced linkage functions for distributions with non-overlapping multivariate marginals. Fan and Henry (2023) developed vector copulas using measure transport and proved a vector version of Sklar's theorem.

The contribution here is not the general observation that naive substitution can fail. It is the sharp FGM/independence-block phase boundary \(1/(2^m-1)\), the explicit Euler-operator criterion for that block geometry, and a quantitative entropy-additivity defect that remains strictly positive inside the valid-copula regime.

## Limitations

- The sharp phase diagram is proved for a bivariate FGM outer copula and an \(m\)-dimensional independence inner block.
- The Euler-operator criterion assumes sufficient smoothness and one independence-product block; it is not a complete characterization for arbitrary collections of multivariate inner copulas.
- The entropy bound is a one-sided lower bound on the additivity defect and is not claimed optimal.
- No replacement operad is constructed here. Hierarchical Kendall copulas, linkage functions and vector copulas are relevant established alternatives, but their algebraic properties are not analyzed.
- Originality is to the best of our knowledge. Older literature on non-overlapping multivariate marginals and linkage constructions could contain equivalent special-case differential criteria under different notation.

## References

1. X. Lu, "Copula Operad and Copula Entropy", arXiv:2609.20512 (2026). https://arxiv.org/abs/2609.20512
2. E. C. Brechmann, "Hierarchical Kendall copulas: Properties and inference", Canadian Journal of Statistics 42 (2014), 78--108. https://doi.org/10.1002/cjs.11204
3. H. Li, M. Scarsini, M. Shaked, "Linkages: A Tool for the Construction of Multivariate Distributions with Given Nonoverlapping Multivariate Marginals", Journal of Multivariate Analysis 56 (1996), 20--41. https://doi.org/10.1006/jmva.1996.0002
4. Y. Fan, M. Henry, "Vector copulas", Journal of Econometrics 234 (2023), 128--150. https://doi.org/10.1016/j.jeconom.2021.11.012
