# A convex-order optimum and Poisson–Bernoulli crossover for matching-weighted bipartite spanning trees

## Finding
Let \(n\ge3\) be an integer, let \(K_{n,n}\) have labeled classes \(\{a_1,\ldots,a_n\}\) and \(\{b_1,\ldots,b_n\}\), and give edges \(a_i b_i\) conductance \(t>0\), and all other edges conductance \(1\). A spanning tree is sampled with probability proportional to the product of its conductances. Write \(D_n(t)\) for the **ordinary (unweighted)** degree of a fixed vertex, and \(L_n(t)\) for the number of leaves in the random tree.

Set
\[
 p_{n,t}=\frac{n-1+t}{n(n-2+2t)},\qquad q_{n,t}=\frac{t}{n-2+2t}.
\]
The exact rooted-degree law is
\[
 \boxed{D_n(t)\ \stackrel{d}{=}\ 1+\operatorname{Bin}(n-2,p_{n,t})+\operatorname{Bernoulli}(q_{n,t}),}
\]
where the two random summands on the right are independent. In particular, \(\mathbb E D_n(t)=2-1/n\), independent of \(t\).

For convex order, \(X\le_{\mathrm{cx}}Y\) means that \(\mathbb E\phi(X)\le\mathbb E\phi(Y)\) for every real-valued convex function \(\phi\) on the common finite support. The family has the sharp two-sided monotonicity:
\[
 0<t_1<t_2\le1\ \Longrightarrow\ D_n(t_1)\le_{\mathrm{cx}}D_n(t_2),
 \qquad
 1\le t_1<t_2\ \Longrightarrow\ D_n(t_2)\le_{\mathrm{cx}}D_n(t_1).
\]
Each comparison between distinct parameters on the same side is strict for every strictly convex function on the support. Thus \(t=1\) is the unique maximizer of the degree variance and the probability of being a leaf, and hence of the expected number of leaves. Quantitatively,
\[
 \operatorname{Var}(D_n(1))-\operatorname{Var}(D_n(t))
 =\frac{(n-2)(n-1)(t-1)^2}{n^2(n-2+2t)^2},
\]
\[
 \mathbb E L_n(t)=2n(1-q_{n,t})(1-p_{n,t})^{n-2},\qquad
 \max_{t>0}\mathbb E L_n(t)=2n(1-1/n)^{n-1}.
\]

For any sequence \(t_n>0\) with \(t_n/n\to c\in[0,\infty]\), interpret \(c=\infty\) by its one-sided limit and set \(u=(1+c)/(1+2c)\), so \(u=1/2\) at \(c=\infty\). Then
\[
 D_n(t_n)\ \Longrightarrow\ 1+\operatorname{Pois}(u)+\operatorname{Bernoulli}(1-u),
 \qquad \frac{\mathbb E L_n(t_n)}n\longrightarrow2u e^{-u},
\]
with independent limiting summands. This identifies an order-\(n\) conductance crossover from the usual \(1+\operatorname{Pois}(1)\) rooted degree law to \(1+\operatorname{Pois}(1/2)+\operatorname{Bernoulli}(1/2)\), even though the mean rooted degree is fixed.

## Assumptions and scope
All graphs are labeled, finite and undirected; weights are positive conductances, **not** random minimum-spanning-tree edge lengths. A tree \(T\) has probability \(\prod_{e\in T}w_e/Z_n(t)\). Ordinary degrees count edges rather than conductance. The theorem applies for every integer \(n\ge3\), every real \(t>0\), and every fixed vertex. It compares the one-parameter family in which all \(n\) diagonal matching edges share the same conductance. No assertion is made for arbitrary nonuniform matching conductances or for joint degrees of different vertices. When \(n=2\), all resulting trees are paths and \(D_2(t)\stackrel d=1+\operatorname{Bernoulli}(1/2)\) for every \(t>0\), so uniqueness is false and excluded.

## Proof
**1. Weighted rooted tree enumerator.** Fix root \(a_1\), multiply its \(n\) incident edge weights by a marker \(z\), and let \(Z_n(t;z)\) be the resulting weighted tree sum. The weighted matrix-tree theorem identifies \(Z_n(t;z)\) with the cofactor of the weighted Laplacian at \(a_1\). Order remaining left vertices \(a_2,\ldots,a_n\), then right vertices \(b_2,\ldots,b_n,b_1\). Put \(m=n-1\), \(A=n-1+t\), and \(r=n-2+t\). The cofactor has block form
\[
 \mathcal L(z)=\begin{pmatrix} A I_m&-C\\-C^{\mathsf T}&\operatorname{diag}((r+z)I_m,m+tz)\end{pmatrix},
 \qquad C=J_m+(t-1)I_m\ \big|\ \mathbf 1_m,
\]
where \(J_m\) denotes the all-ones square matrix, and the final displayed column is appended to the first \(m\) columns of \(C\). Its Schur complement after eliminating \(AI_m\) is
\[
 S(z)=\operatorname{diag}((r+z)I_m,m+tz)-A^{-1}C^{\mathsf T}C.
\]
On the \((m-1)\)-dimensional subspace of the first \(m\) right coordinates summing to zero, its eigenvalue is \((d+Az)/A\), with
\[
 d=Ar-(t-1)^2=n^2-3n+1+(2n-1)t.
\]
On the remaining two-dimensional space spanned by the first \(m\) coordinates' all-ones vector and the final coordinate, the determinant is exactly \(z(r+tz)\) by direct \(2\times2\) multiplication. Hence
\[
 \boxed{Z_n(t;z)=Az(d+Az)^{n-2}(r+tz).}
\]
In particular, \(Z_n(t;1)=n^{n-2}(n-2+2t)^{n-1}(n-1+t)\). The ratio \(Z_n(t;z)/Z_n(t;1)\) is the probability generating function \(\mathbb E[z^{D_n(t)}]\), so
\[
 \mathbb E[z^{D_n(t)}]
 =z\left(1+p_{n,t}(z-1)\right)^{n-2}\left(1+q_{n,t}(z-1)\right).
\]
Both probabilities lie strictly between zero and one for \(n\ge3,t>0\); therefore this is the asserted independent binomial–Bernoulli law. Moreover, \((n-2)p_{n,t}+q_{n,t}=(n-1)/n\), proving the mean statement.

**2. Convex-order monotonicity.** Write \(m=n-2\), \(p=p_{n,t}\), \(q=q_{n,t}\), and \(B=n-2+2t\). Direct differentiation gives
\[
 p'=-B^{-2},\quad q'=mB^{-2}=-mp',\quad q-p=\frac{(n-1)(t-1)}{nB}.
\]
For any function \(\phi\) defined on the finite integer support, let \(\Delta\phi(j)=\phi(j+1)-\phi(j)\). Differentiating the binomial–Bernoulli expectation, using \(X\sim\operatorname{Bin}(m-1,p)\), yields the exact identity
\[
 \frac{d}{dt}\mathbb E\phi(D_n(t))
 =m p'(q-p)\,\mathbb E[\Delta^2\phi(1+X)]
 =-\frac{(n-2)(n-1)(t-1)}{n(n-2+2t)^3}\,
 \mathbb E[\Delta^2\phi(1+X)].
\]
For convex \(\phi\), all terms \(\Delta^2\phi\) are nonnegative. This proves both monotone convex-order statements, and strictness for strictly convex \(\phi\) follows because the binomial random variable has strictly positive mass on its finite support. Taking \(\phi(j)=j^2\) gives the variance identity by direct simplification. Taking \(\phi(j)=(2-j)_+\), which equals \(1\) precisely when the tree degree is \(1\), gives strict increase of leaf probability up to \(t=1\) and strict decrease thereafter: here \(\Delta^2\phi(1+X)=\mathbf1_{\{X=0\}}\), which has positive expectation. Since the weighted graph is vertex transitive, \(\mathbb E L_n(t)=2n\Pr(D_n(t)=1)\). Evaluating the independent Bernoulli zero-probabilities proves both leaf formulas and uniqueness.

**3. The scaling crossover.** For a sequence \(t_n/n\to c\), the explicit parameters obey \((n-2)p_{n,t_n}\to u\), \(p_{n,t_n}\to0\), and \(q_{n,t_n}\to1-u\). Thus the binomial pgf tends to \(\exp(u(z-1))\) and the Bernoulli pgf tends to \(u+(1-u)z\). Their product gives convergence in distribution to the independent Poisson–Bernoulli sum. Evaluating the exact zero-summand probability \((1-p)^{n-2}(1-q)\) gives \(\mathbb E L_n(t_n)/n\to2u e^{-u}\). These limits include \(c=0\) and \(c=\infty\) without requiring a stronger growth assumption.

## Verification
The accompanying `verify.py` uses Python standard-library rational arithmetic. It independently evaluates weighted Laplacian cofactors for \(2\le n\le7\), multiple rational conductances and incident-edge markers; it also enumerates **all** spanning trees for \(n=2,3,4\), reconstructs root-degree probabilities and leaf expectations, and verifies the explicit variance identity. Running `python3 verify.py` returns `VERIFY_OK 212 exact rational assertions`. This finite testing is supplementary: the block determinant, discrete convex derivative identity, and pgf limit provide the proofs for all claimed parameters.

## Relationship to prior work
The weighted matrix-tree theorem and the general node-degree polynomial for Gibbs-distributed spanning trees are established tools. Fita Sanmartín, Schnörr and Hamprecht (2024, arXiv:2409.13472) give a general degree-generating determinant for weighted graphs, but do not evaluate the matching-weighted \(K_{n,n}\) factorization or compare its entire family in convex order. Rapoport (2023, arXiv:2312.14992) studies unweighted UST degree fields, not this weighted-parameter ordering. Klee and Stamps (2020, arXiv:2008.01669), Proposition 8, give the Laplacian spectrum of \(K_{n,n}\) with a perfect matching *removed*, a boundary case of the host, but not its degree law, the order-\(n\) crossover, or leaf-maximizing conductance. The new contribution is the explicit familywise convex-order classification with its binomial–Bernoulli factorization and scaling transition, not the general determinant principle.

## Limitations
This is a local marginal degree theorem, not a characterization of correlations or the joint leaf-count distribution. Convex-order maximality is restricted to a **common** conductance on all edges of a fixed perfect matching; it does not assert global optimality over all edge-weight assignments. The two asymptotic laws are single-vertex marginal limits, and no rate of convergence is claimed. The earliest cited mathematical source for the direction is arXiv:2312.14992v1, posted on 2023-12-22. Priority beyond the explicitly compared literature remains subject to independent evaluation.

## References
- A. Rapoport, *Correlations in uniform spanning trees: a fermionic approach*, arXiv:2312.14992v1 (2023-12-22), https://arxiv.org/html/2312.14992v1 . See Sections 3.2 and 4, especially the complete-graph subsection.
- E. Fita Sanmartín, C. Schnörr, F. A. Hamprecht, *Expectation and Variance of the Degree of a Node in Random Spanning Trees*, arXiv:2409.13472v2 (2024-10-17), https://arxiv.org/html/2409.13472v2 . See Sections 3–4, especially the determinant coefficient formulation.
- S. Klee, M. T. Stamps, *Eigenvalues of graph Laplacians via rank-one perturbations*, arXiv:2008.01669v1 (2020-08-04), https://arxiv.org/pdf/2008.01669 . See Proposition 8, the crown-graph Laplacian spectrum.
