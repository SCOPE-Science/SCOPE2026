# Closed form and finite-size correction for root–leaf covariance in an attachment tree

## Finding

Start with the single edge on vertices \(1,2\). For each \(n\ge2\), attach vertex \(n+1\) to an old vertex \(v\) with probability \(\deg(v)/(2(n-1))\). Let \(D_n\) be the degree of vertex 1 and \(L_n\) the number of leaves (vertices of undirected degree one). Put
\[
p_n=4^{-(n-2)}\binom{2n-4}{n-2}.
\]
The exact covariance sum previously given for this model [1] reduces to the following expression with no sum over tree sizes, valid for every \(n\ge2\):
\[
\boxed{\operatorname{Cov}(D_n,L_n)=\frac{2p_n}{3}\bigl[n-2(2n-3)p_n\bigr].}
\]
In particular the explicit constant correction to the known leading square-root term is
\[
\operatorname{Cov}(D_n,L_n)=\frac{2}{3\sqrt\pi}\sqrt n-\frac{8}{3\pi}+O(n^{-1/2}).
\]
The covariance vanishes for \(n=2,3\), and its strict positivity for \(n\ge4\) is known from [1]. The variance normalization gives
\[
\boxed{\sqrt n\,\operatorname{Corr}(D_n,L_n)\longrightarrow\sqrt{\frac{2}{\pi-2}}.}
\]
Thus the unnormalized dependence grows with \(n\), whereas the correlation decays. The contribution is the summation-free evaluation and the explicit constant correction; the normalization is included to interpret the size of the effect.

## Assumptions and scope

Weights are undirected degrees throughout; the seed is one edge between two initially equivalent vertices. The leaf count includes both initial vertices whenever their undirected degree remains one. The result does not concern a uniform recursive tree. Rooted plane-oriented descriptions require care about the seed, initial root weight, and whether a root can count as a leaf. In the conventional rooted insertion rule with weight one plus outdegree, the root has an extra unit relative to its undirected degree in a tree on at least two vertices; nonroot weights then agree. The name of a model alone is not enough to distinguish it from the edge-seeded process here. The correlation is undefined at \(n=2,3\) because \(L_n\) is deterministic.

## Proof

While the tagged vertex remains a leaf, its selection probability at size \(j\) is \(1/(2(j-1))\). Hence \(p_n=\Pr(D_n=1)\) by multiplying the successive avoidance probabilities. In particular \(p_2=1\) and \(p_{n+1}/p_n=(2n-3)/(2n-2)\).

Write \(d_n=\mathbb ED_n\), \(\ell_n=\mathbb EL_n\), \(m_n=2(n-1)\). Let \(I_n\) indicate selection of vertex 1 and \(J_n\) selection of any leaf in the step from size \(n\) to size \(n+1\). Then \(D_{n+1}=D_n+I_n\) and \(L_{n+1}=L_n+1-J_n\). Conditionally on the tree, the means of \(I_n,J_n,I_nJ_n\) are \(D_n/m_n,L_n/m_n,\mathbf 1_{\{D_n=1\}}/m_n\), respectively. Thus
\[
d_{n+1}=(1+1/m_n)d_n,\qquad \ell_{n+1}=(1-1/m_n)\ell_n+1.
\]
Using \(d_2=1\), \(\ell_2=2\) and the recursion for \(p_n\) gives the known means \(d_n=(2n-3)p_n\), \(\ell_n=[2(n-1)+4p_n]/3\).

For completeness, the two conditional contributions \(I_nL_n\) and \(-D_nJ_n\) to the mixed product cancel in expectation. The resulting increment of \(\mathbb E[D_nL_n]\) is \(d_{n+1}-p_n/m_n\). Subtracting the increment of \(d_n\ell_n\) gives the known covariance increment [1, Eq. (3)]
\[
\operatorname{Cov}(D_{n+1},L_{n+1})-\operatorname{Cov}(D_n,L_n)
=\frac{(n-3)p_n}{3(n-1)}+\frac{(2n-3)p_n^2}{3(n-1)^2}.
\]
To telescope the two summands, the survival ratio gives
\[
(n+1)p_{n+1}-np_n=\frac{(n-3)p_n}{2(n-1)},\quad
(2n-1)p_{n+1}^2-(2n-3)p_n^2=-\frac{(2n-3)p_n^2}{4(n-1)^2}.
\]
Both the covariance and \(2np_n/3-4(2n-3)p_n^2/3\) vanish at \(n=2\). Matching their increments proves the formula. The increment is zero at \(n=2\) and positive for \(n\ge3\), recovering the prior sign result.

For the variance of \(D_n\), write \(H_n=\mathbb E[D_n(D_n+1)]\). Conditional selection increases the product by \(2(D_n+1)\) with probability \(D_n/m_n\). Thus \(H_{n+1}=(1+2/m_n)H_n\); since \(H_2=2\), this gives \(H_n=2(n-1)\), and
\[
\operatorname{Var}(D_n)=2(n-1)-d_n-d_n^2\qquad(n\ge2).
\]
For \(V_n=\operatorname{Var}(L_n)\), \(\operatorname{Cov}(L_n,J_n)=V_n/m_n\) by conditioning and \(J_n\) is Bernoulli with mean \(\ell_n/m_n\). Therefore
\[
V_{n+1}=\left(1-\frac{2}{m_n}\right)V_n+\frac{\ell_n}{m_n}-\left(\frac{\ell_n}{m_n}\right)^2.
\]
Here \(V_2=0\). At \(n=3\) there are always two leaves, so \(V_3=0\). Substituting the means and the recursion for \(p_n\) shows that
\[
\operatorname{Var}(L_n)=\frac{n-1+4p_n-16p_n^2}{9}\qquad(n\ge3),
\]
which has the required initial value at \(n=3\) and satisfies the variance recursion for all \(n\ge3\). The displayed expression for the leaf variance is not valid at the edge seed \(n=2\).

Stirling's formula gives \(p_n=(\pi n)^{-1/2}+O(n^{-3/2})\). In the telescoped covariance the term \(2np_n/3\) gives the leading square root with an \(O(n^{-1/2})\) error, and \(-4(2n-3)p_n^2/3\) gives \(-8/(3\pi)+O(n^{-1})\). The variances are \((2-4/\pi)n+O(\sqrt n)\) and \(n/9+O(1)\). Their leading terms in the denominator of the correlation yield the stated limit. The two variances are positive when \(n\ge4\) because the covariance is nonzero there.

## Verification

The accompanying `verify.py` uses only the Python 3 standard library. The verification enumerates the exact masses of the possible degree vectors at sizes 2 through 10 and compares the means, mixed moment, variances, covariance and signs. It handles the seed leaf variance separately. Exact rational recurrence tests are carried out through size 500; the leaf-variance recurrence comparison is included from size 3. Large-size numerical comparisons illustrate the asymptotics; the exact identities and limits follow from the argument above, not from finite experiments.

## Relationship to prior work

The earlier exact increment, sum, strict sign and leading square-root asymptotic [1] concern precisely the same model and the same two random variables, with \(q_n=p_n\). The covariance itself was therefore already known as a finite sum. The two telescoping identities give a shorter exact representation and evaluate the constant term beyond the leading square root. Brightwell and Łuczak [2] study degree counts for this attachment rule and note its treatment under plane-oriented recursive-tree terminology. Peköz, Röllin and Ross [3] treat degrees of fixed early vertices jointly; Hartle and Krapivsky [4] consider covariance of aggregate degree or leafdegree categories. Neither distinction changes the direct same-model overlap with [1].

## Limitations

The result is for the specified one-edge seed and one tagged endpoint. It gives a second-order statistic, not a joint law, independence, or a stochastic ordering. The constant correction and closed form are compared to the inspected exact prior results, not asserted to establish exhaustive historical priority.

## References

1. *Oldest-hub degree has positive square-root covariance with leaf abundance*, Resultary record `2026/10/13/SCOPE-oldest-hub-degree-has-positive-square-root-covariance-with-leaf--a3885e62cb19`, Eqs. (1)–(6), (14), (15).
2. G. Brightwell and M. J. Łuczak, *Vertices of high degree in the preferential attachment tree*, arXiv:1012.5550, §1.
3. E. Peköz, A. Röllin, and N. Ross, *Joint degree distributions of preferential attachment random graphs*, arXiv:1402.4686.
4. H. Hartle and P. L. Krapivsky, *Leaves of preferential attachment trees*, arXiv:2602.01021.
