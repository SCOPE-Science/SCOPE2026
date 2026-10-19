# Sharp regularity rarity and the Gaussian diagonal-image law in finite magma monoids

## Finding
Let \(X\) be a labeled set of size \(n\geq 1\), and let \(\mathcal M_n\) denote all binary operations on \(X\), equipped with the magma-monoid product
\[
 (u\triangleleft v)(a,b)=v(u(a,b),u(b,a)).
\]
Write \(\mathcal R_n\) for its von Neumann regular elements, so \(u\in\mathcal R_n\) exactly when \(u\triangleleft v\triangleleft u=u\) for some \(v\in\mathcal M_n\). Let \(E_n(u)=n-|\{u(a,a):a\in X\}|\) be the number of labels omitted from the diagonal image. The natural uniform distribution on \(\mathcal R_n\) is understood in the assertions below.

Define \(z=e^{-1/2}\) and the unique \(x\in(0,1)\) solving
\[
 (1-x)e^x=1-z.
\]
Put
\[
 \theta=\frac{z}{xe^x},\qquad
 \sigma^2=\theta(1-\theta)-\frac{\theta^2}{x},\qquad
 \rho=e^{x-1},\qquad
 C=\frac{\exp(\theta/2-\theta^2/4)}{\sqrt{x}}.
\]
Then \(0<\rho<1\), \(\sigma^2>0\), and, as \(n\to\infty\),
\[
 \boxed{\frac{|\mathcal R_n|}{n^{n^2}}\sim C\rho^n,}
 \qquad
 \boxed{\frac{E_n-\theta n}{\sqrt n}\ \Longrightarrow\ \mathcal N(0,\sigma^2)
 \quad\text{for a uniform }u\in\mathcal R_n.}
\]
Numerically,
\[
 x=0.828102026619079\ldots,\quad
 \rho=0.842065081839284\ldots,\quad
 C=1.256970100571444\ldots,
\]
\[
 \theta=0.319984374206401\ldots,\qquad
 \sigma^2=0.093950190003772\ldots.
\]
Thus regularity is exponentially rare, but conditioned regular operations have a Gaussian diagonal-image deficiency centered at about \(0.319984n\), rather than the unconditional occupancy center \(e^{-1}n\).

## Assumptions and scope
All finite sets are nonempty; there are no associativity, commutativity, or identity assumptions on their binary operations. The asymptotic parameter is the cardinality \(n\to\infty\). Uniformity is over the \(n^{n^2}\) labeled binary operations, or, in the conditional assertion, over the regular operations alone. The multiplication is the composition product defined above, not the underlying binary operation on \(X\). The Gaussian statement is convergence in distribution, not an exact finite-sample normal law.

## Proof
**1. Algebraic reduction.** Given a binary operation \(u\), form the pair map \(F_u:X^2\to X^2\), \(F_u(a,b)=(u(a,b),u(b,a))\). It commutes with the coordinate swap \(s(a,b)=(b,a)\); conversely every map commuting with \(s\) is uniquely obtained in this way. The magma-monoid product corresponds to ordinary composition of these maps.

We prove the regularity criterion directly. Let \(F\) commute with \(s\), let \(\Delta=\{(a,a):a\in X\}=\operatorname{Fix}(s)\), and write \(I=F(X^2)\). Then \(F\) has a flip-equivariant inner inverse if and only if
\[
 I\cap\Delta=F(\Delta). \tag{1}
\]
Necessity: if \(FGF=F\) with \(G\) flip-equivariant and \(y\in I\cap\Delta\), then \(y=FG(y)\), and \(G(y)\in\Delta\), hence \(y\in F(\Delta)\). Sufficiency: for every fixed point \(y\in I\cap\Delta\), choose a fixed preimage; for each nonfixed swapped pair of outputs \(\{y,s(y)\}\subset I\), choose a preimage of one and its swapped mate for the other. This gives an equivariant section of \(F\) over its image. Extend equivariantly to the remaining outputs, sending unused fixed points to any element of \(\Delta\). Then \(FGF=F\). In particular, \(u\) is regular precisely when every diagonal value hit by a pair-map output already occurs among \(u(a,a)\).

**2. Exact finite probability.** Put \(N=\binom n2\). For a uniform binary operation, the \(n\) diagonal values \(u(a,a)\) are independent uniform labels; for each unordered pair \(\{a,b\}\), the ordered value pair \((u(a,b),u(b,a))\) is independently uniform on \(X^2\). If \(E_n=j\), exactly \(j\) of the \(n^2\) possible pair outputs are prohibited by (1). Hence
\[
 P_n:=\frac{|\mathcal R_n|}{n^{n^2}}
 =\mathbb E\left[\left(1-\frac{E_n}{n^2}\right)^N\right], \tag{2}
\]
where the expectation in (2) is for the *unconditioned* diagonal occupancy. Equivalently, with \(S(n,d)\) the Stirling number of the second kind,
\[
 |\mathcal R_n|=\sum_{d=1}^{n}\binom nd d!S(n,d)(n^2-n+d)^N. \tag{3}
\]
Equation (3) is the established exact regular-element count; neither (1) nor (3) is claimed as a novel result.

**3. Uniform exponential correction.** For every integer \(0\le j\le n\), Taylor's theorem, uniformly for \(n\ge2\), gives
\[
 \left(1-\frac{j}{n^2}\right)^N
 =z^j\exp\left(\frac{j}{2n}-\frac{j^2}{4n^2}+O(n^{-1})\right). \tag{4}
\]
Here the error bound does not depend on \(j\). In particular, the factor multiplying \(z^j\) is uniformly bounded above and away from zero.

**4. A tilted occupancy model.** Set \(f(t)=e^t-1+z\). For the unconditioned occupancy distribution of \(E_n\), exact exponential generating functions give
\[
 H_n(z):=\mathbb E[z^{E_n}]
 =\frac{n!}{n^n}[t^n]f(t)^n. \tag{5}
\]
The equation \((1-x)e^x=1-z\) is equivalent to \(x f'(x)/f(x)=1\) and to \(f(x)=xe^x\). Uniqueness follows because \((1-t)e^t\) decreases strictly from \(1\) to \(0\) on \((0,1)\).

Let \(Y_1,\ldots,Y_n\) be independent with
\[
 \Pr(Y_i=0)=\frac z{f(x)},\qquad
 \Pr(Y_i=k)=\frac{x^k}{k!f(x)}\quad(k\ge1).
\]
These are genuine probabilities, with mean \(1\) and variance \(x\). Let \(S_n^*=\sum_iY_i\) and \(Z_n=\sum_i\mathbf1_{\{Y_i=0\}}\). The weighted occupancy distribution with weights \(z^{E_n}\) is exactly the distribution of \(Z_n\) conditional on \(S_n^*=n\). Furthermore,
\[
 H_n(z)=\frac{n!}{n^n}\frac{f(x)^n}{x^n}
 \Pr(S_n^*=n). \tag{6}
\]
The aperiodic lattice local central limit theorem gives \(\Pr(S_n^*=n)\sim(2\pi nx)^{-1/2}\), because the summands have all nonnegative integers in their support. Stirling's formula and \(f(x)=xe^x\) therefore yield
\[
 H_n(z)\sim\frac{e^{(x-1)n}}{\sqrt{x}}. \tag{7}
\]

**5. Conditional Gaussian law and the prefactor.** For each \(i\), let \(J_i=\mathbf1_{\{Y_i=0\}}\). Then
\[
 \mathbb E J_i=\theta,\quad
 \operatorname{Var}(J_i)=\theta(1-\theta),\quad
 \operatorname{Cov}(J_i,Y_i)=-\theta,\quad
 \operatorname{Var}(Y_i)=x.
\]
The support \((0,1),(1,0),(2,0)\) for \((Y_i,J_i)\) generates the full two-dimensional lattice, so the bivariate lattice local central limit theorem, conditional on \(\sum_iY_i=n\), implies
\[
 \frac{Z_n-\theta n}{\sqrt n}
 \Longrightarrow\mathcal N\left(0,\theta(1-\theta)-\theta^2/x\right),
 \qquad Z_n/n\longrightarrow\theta\text{ in probability}. \tag{8}
\]
The conditional variance is strictly positive since \(J_i\) is not an affine function of \(Y_i\), as seen at three support points.

By (4), the true law of \(E_n\) among regular operations differs from this \(z\)-tilted law by a factor depending on \(E_n/n\) that converges in probability, under the tilted law, to \(\exp(\theta/2-\theta^2/4)\). The factors are uniformly bounded, so normalized reweighting preserves (8) and multiplies (7) by this constant. Combining with (2) proves both displayed claims.

## Verification
The accompanying self-contained `verify.py` exactly counts regular operations using independent image-size recurrences for \(n=2,3\), checks the criterion by enumerating all binary-operation tables in these sizes, and directly tests inner-inverse existence for all \(16\) binary operations when \(n=2\). It also computes exact integer regularity probabilities and conditional vacancy moments through \(n=320\); the ratios to the asymptotic are \(0.998780316342\) at \(n=20\), \(0.999705005652\) at \(n=80\), and \(0.999926864225\) at \(n=320\). Exact results are \(|\mathcal R_2|=14\) and \(|\mathcal R_3|=14619\). All checks completed successfully. The general limit law relies on the displayed local-limit proof, not on the finite computations.

Run with `python3 verify.py`; the program uses only the Python standard library.

## Relationship to prior work
The pair-map realization, algebraic regularity criterion (1), and exact count (3) are established by Baiduk and Kozerenko, *Transformation Semigroup Perspective on the Magma Monoid*, arXiv:2607.13746 (first posted July 15, 2026), especially Theorem 3, Proposition 24, and Theorem 25. The contribution here is the sharp exponential constant and prefactor in the *proportion* of regular binary operations, together with the conditional Gaussian law of their diagonal-image deficiency. These are not asserted in the inspected primary article. López-Permouth (2026) concerns idempotent counts and larger arities, while López-Permouth, Owusu-Mensah, and Rafieipour (2022) introduce and analyze the monoid itself. Standard local central limit theorems are used as mathematical tools and are not claimed as new.

## Limitations
The assertions concern labeled binary operations with no structural restrictions beyond regularity in this particular magma-monoid product. They are asymptotic as \(n\to\infty\); the proof gives no uniform local central limit error bound, no higher-order asymptotic term, and no separate classification of regularity in the higher-arity variants. The earlier exact count implies a route to these asymptotics, and a formally equivalent unpublished asymptotic analysis may exist. Independent verification of originality and proof has not been performed.

## References
1. Y. Baiduk and S. Kozerenko, *Transformation Semigroup Perspective on the Magma Monoid*, arXiv:2607.13746v1, 2026-07-15, https://arxiv.org/abs/2607.13746 .
2. S. R. López-Permouth, *Idempotent elements in binary and s-ary magma monoids*, São Paulo Journal of Mathematical Sciences 20 (2026), article 14, https://doi.org/10.1007/s40863-025-00519-x .
3. S. R. López-Permouth, I. Owusu-Mensah, and A. Rafieipour, *A monoid structure on the set of all binary operations over a fixed set*, Semigroup Forum 104 (2022), 667–688, https://doi.org/10.1007/s00233-022-10280-8 .
