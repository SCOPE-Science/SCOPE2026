# An exact leaf regression for pendant root branches in random recursive trees

## Finding

Let \(T_n\) be the uniform recursive tree on labels \(1,\ldots,n\), rooted at vertex \(1\). Write \(L_n\) for its total number of leaves and \(Z_n\) for the number of children of the root having no children of their own. For every integer \(n\ge2\) and every \(z\) with \(\Pr(Z_n=z)>0\),

\[
\boxed{\mathbb E[L_n\mid Z_n=z]=\frac{n-1+z}{2}.}
\]

In particular, conditioning on an additional singleton branch at the root increases the expected total leaf count by precisely \(1/2\), without finite-size approximation or restrictions on the other branches. For \(n\ge3\), this yields

\[
\operatorname{Cov}(L_n,Z_n)=\frac12,\qquad
\operatorname{Corr}(L_n,Z_n)=\sqrt{\frac3n}.
\]

The auxiliary marginal law of \(Z_n\) is the classical fixed-point (rencontres) law for a uniform permutation on \(n-1\) points. This *marginal law is not claimed as new*: it is also a specialization of the root-branch enumerator of Seelbach Benkner and Wagner [2]. The asserted contribution is the **exact finite-size conditional regression** relating root singleton branches to *all* leaves.

## Assumptions and scope

For \(j=2,\ldots,n\), independently choose the parent of vertex \(j\) uniformly from \(\{1,\ldots,j-1\}\). This is the uniform measure on the \((n-1)!\) recursive trees. A leaf is a vertex of outdegree zero; since \(n\ge2\), the root is not a leaf. The statistic \(Z_n\) counts root-adjacent vertices of outdegree zero, not the whole root degree. All expectations are under this single growth law. The displayed conditional identity is asserted only for \(z\) in the support of \(Z_n\); no conditioning on zero-probability events is used.

## Proof

**1. Joint transition.** Fix a tree with \(n\ge2\) vertices and statistics \((Z_n,L_n)=(z,\ell)\). There are exactly \(z\) pendant root children, \(\ell-z\) non-root-adjacent leaves, and \(n-1-\ell\) non-root internal vertices. Attaching vertex \(n+1\) at a uniformly selected existing vertex produces the following exhaustive transitions, with the indicated *numerators* of their probabilities (each divided by \(n\)):

\[
\begin{array}{c|c|c}
\text{attachment target}&(Z_{n+1},L_{n+1})&\text{weight}\\
\hline
\text{root}&(z+1,\ell+1)&1\\
\text{pendant root child}&(z-1,\ell)&z\\
\text{other leaf}&(z,\ell)&\ell-z\\
\text{other nonleaf}&(z,\ell+1)&n-1-\ell.
\end{array}
\]

The weights sum to \(n\), including boundary cases \(z=0\) or \(\ell=n-1\).

**2. Probability and mixed transforms.** Define ordinary polynomials

\[
G_n(u)=\mathbb E[u^{Z_n}],\qquad H_n(u)=\mathbb E[L_nu^{Z_n}].
\]

Conditioning on the four transitions, and collecting terms (the quadratic terms in \(\ell\) cancel), gives

\[
\begin{aligned}
nG_{n+1}(u)&=(u+n-1)G_n(u)+(1-u)G_n'(u),\\
nH_{n+1}(u)&=(u+n-2)H_n(u)+(1-u)H_n'(u)
 +(u+n-1)G_n(u).
\end{aligned}
\tag{1}
\]

At \(n=2\) the tree is the single edge, so \(G_2(u)=H_2(u)=u\).

**3. Exact invariant.** Put \(\mathcal A_n f=(u+n-1)f+(1-u)f'\) and \(\mathcal Df=uf'\). Direct differentiation gives the operator identity

\[
(n+\mathcal D)\mathcal A_n
=(\mathcal A_n-1)(n-1+\mathcal D)+2(u+n-1).
\tag{2}
\]

The first equation in (1) is \(nG_{n+1}=\mathcal A_nG_n\), and the second is \(nH_{n+1}=(\mathcal A_n-1)H_n+(u+n-1)G_n\). Since \(H_2=(1+\mathcal D)G_2/2\), identity (2) proves by induction that

\[
\boxed{H_n(u)=\frac{n-1}{2}G_n(u)+\frac u2G_n'(u)}
\qquad(n\ge2).
\tag{3}
\]

Indeed, multiply the desired relation at \(n+1\) by \(n\), substitute the first recurrence and then apply (2) and the second recurrence. Because \(uG_n'(u)=\mathbb E[Z_nu^{Z_n}]\), coefficient comparison in (3) yields

\[
\mathbb E[L_n\mathbf1_{\{Z_n=z\}}]
=\frac{n-1+z}{2}\Pr(Z_n=z)
\]

for every integer \(z\). Division by a positive mass completes the conditional regression.

**4. Auxiliary marginal and correlations.** The first recurrence of (1), with \(G_2(u)=u\), has solution

\[
G_n(u)=\sum_{r=0}^{n-1}\frac{(u-1)^r}{r!}.
\tag{4}
\]

To verify (4), differentiate the truncated exponential and substitute; its difference from the next truncation is \((u-1)^n/n!\). This agrees with [2, Section 5.2] by marking a one-vertex root branch, so (4) is a known marginal, included here to evaluate the new joint identity.

For \(n\ge3\), (4) gives \(\mathbb E[Z_n]=\operatorname{Var}(Z_n)=1\). The leaf-growth law is \(L_{n+1}=L_n+B_n\) conditionally on \(L_n\), where \(B_n\) has success probability \((n-L_n)/n\). Hence \(\mathbb E[L_n]=n/2\) for \(n\ge2\), while

\[
\operatorname{Var}(L_{n+1})
=\left(1-\frac2n\right)\operatorname{Var}(L_n)+\frac14.
\]

Starting at \(\operatorname{Var}(L_3)=1/4\), this gives \(\operatorname{Var}(L_n)=n/12\) for \(n\ge3\). Taking covariance with \(Z_n\) in the conditional regression gives \(\operatorname{Cov}(L_n,Z_n)=\operatorname{Var}(Z_n)/2=1/2\), and the stated correlation follows. At \(n=2\), both variables are constant, so their correlation is undefined; the regression remains valid.

## Verification

The standalone `verify.py` uses only Python's standard library. It enumerates every recursive tree up to \(n=9\) via independent parent assignments, counts every realized pair \((Z_n,L_n)\), verifies every positive-mass conditional mean exactly, and compares the marginal with exact derangement probabilities. It separately checks the polynomial recurrences and invariant by rational coefficient calculations through \(n=25\). Run `python verify.py` in the directory containing this result and the script. The induction and the operator identity, rather than the finite checks, prove the claims for all \(n\).

## Relationship to prior work

Seelbach Benkner and Wagner [2, Section 5.2, root-branch exponential generating function] give the distribution of counts of copies of any fixed tree as root branches. Choosing the singleton tree reproduces (4); **there is no originality claim for (4)**. Their stated goals and inspected formulas do not include mixed marking by the total number of leaves or the conditional regression (3). Janson [1, Example 12.4] treats scaled metric limits of recursive trees and does not give a root-local/global leaf regression. Devroye and Janson [3] analyze protected vertices and fringe trees, including a Poisson-aged root offspring calculation; those local/limit results are distinct from an exact fixed-size conditional expectation. Nearby work on covariances of total leaves with the *root degree* addresses a different conditioning variable: the root degree counts all children, not only children which are themselves leaves. Neither the known univariate root-singleton distribution nor that root-degree covariance determines \(\mathbb E[L_n\mid Z_n]\).

## Limitations

Only the conditional mean is classified, not the full conditional distribution or conditional variance. The result is for uniform recursive trees; it is not asserted for preferential attachment, plane-oriented trees, or Galton--Watson conditioned trees. The distribution (4) is pre-existing; the originality judgment pertains solely to (3). Classical permutation/tree bijections and older generating-function literature may contain an equivalent implicit mixed identity; absence of an identified equivalence is not proof of worldwide novelty.

## References

1. Svante Janson, *Tree limits and limits of random trees*, arXiv:2005.13832, first public 2020-05-28, particularly Example 12.4; primary MSC 60C05. https://arxiv.org/abs/2005.13832
2. Louisa Seelbach Benkner and Stephan Wagner, *Distinct Fringe Subtrees in Random Trees*, arXiv:2105.04231, first public 2021-05-10, Section 5.2; later *Algorithmica* **84** (2022), 3686–3728. https://arxiv.org/abs/2105.04231 ; https://doi.org/10.1007/s00453-022-01013-y
3. Luc Devroye and Svante Janson, *Protected nodes and fringe subtrees in some random trees*, *Electronic Communications in Probability* **19** (2014), 1–10. https://doi.org/10.1214/ECP.v19-3048
