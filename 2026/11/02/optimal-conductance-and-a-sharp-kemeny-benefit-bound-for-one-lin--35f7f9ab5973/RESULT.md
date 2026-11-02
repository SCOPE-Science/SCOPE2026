# Optimal conductance and a sharp Kemeny benefit bound for one link in a biclique

## Finding

Let \(K_{a,b}\) have parts of sizes \(a\ge2\) and \(b\ge1\), with conductance one on every original cross-part edge. Give one edge joining two vertices of the size-\(a\) part conductance \(t\ge0\), leaving every other conductance unchanged. Let \(K_{a,b}(t)\) be the Kemeny constant of the *discrete-time, conductance-normalized random walk*: from vertex \(i\), choose neighbor \(j\) with probability \(w_{ij}/\sum_k w_{ik}\). Define \(\Delta_{a,b}(t)=K_{a,b}(t)-K_{a,b}(0)\). For every allowed integer pair and every real \(t\ge0\),

\[
K_{a,b}(0)=a+b-\frac32,
\qquad
\boxed{\Delta_{a,b}(t)=\frac{t(4(a-2)t-3b)}{2(b+2t)(ab+t)}.}
\]

The exact conductance-design classification is:

1. There is a **unique** minimizing conductance \(t_*(a,b)>0\) for every \(a\ge2,b\ge1\). With \(x_*=t_*/b\), it is the unique positive zero of
\[
(8a^2-12a-2)x_*^2+8a(a-2)x_*-3a=0.
\]
The Kemeny constant decreases strictly on \(0<t<t_*\) and increases strictly on \(t>t_*\).
2. Any sufficiently weak new link strictly improves Kemeny's constant. For \(a=2\), every finite positive conductance improves it. For \(a\ge3\), the improvement switches to a Braess penalty precisely when \(t>3b/[4(a-2)]\); equality gives no change.
3. **Sharp universal bound:** for every \(a\ge2,b\ge1,t\ge0\),
\[
\boxed{\Delta_{a,b}(t)\ge-\frac16,}
\]
with equality **if and only if** \(a=2\) and \(t=b\). Hence the maximum possible decrease over every biclique size and single added-link strength is exactly \(1/6\) expected random-walk steps.
4. On balanced bicliques \(a=b=n\), adding a unit-conductance edge is neutral at \(n=8\), harmful for \(n\ge9\), yet the optimal conductance satisfies \(t_*(n,n)\to3/8\), and
\[
 n^2\Delta_{n,n}(1)\to\frac12,
 \qquad n^2\Delta_{n,n}(t_*(n,n))\to-\frac9{32}.
\]
Thus continuous conductance tuning reverses the sign of a *known* unweighted Braess effect.

## Assumptions and scope

Graphs are undirected and finite; weights are symmetric conductances, not transition probabilities or additive delays. The total degree of each of the two endpoints of the new link is \(b+t\), and all other degrees are unchanged. The original graph is connected for all \(a,b\) in the stated range, including \(b=1\). Zero conductance means the new edge is absent. No change to the weights of the original \(ab\) edges is allowed. Kemeny's constant uses the standard convention \(K(P)=\sum_{\lambda\ne1}(1-\lambda)^{-1}\), eigenvalues counted with algebraic multiplicity; it coincides with the stationary-averaged hitting time that counts hitting the initial state as time zero. It is well-defined even for the periodic unperturbed bipartite chain. The parameter \(a\) counts the part containing the new link; it need not be the larger part.

## Proof

### Spectral reduction and exact identity

Write \(P\) for the weighted transition matrix. For \(a\ge3\), partition vertices into the two linked endpoints, the other \(a-2\) vertices of their part, and the \(b\) opposite-part vertices. The subspace antisymmetric on the linked endpoints is invariant under \(P\), with eigenvalue \(-t/(b+t)\). Differences among the \(a-2\) unlinked vertices and among the \(b\) opposite-part vertices give a total of \(a+b-4\) zero eigenvalues (the first family has dimension \(a-3\), the second \(b-1\)). The remaining eigenvalues are those of the row-stochastic quotient

\[
Q=\begin{pmatrix}
\dfrac{t}{b+t}&0&\dfrac{b}{b+t}\\
0&0&1\\
\dfrac2a&\dfrac{a-2}{a}&0
\end{pmatrix}.
\]

Its characteristic polynomial factors as

\[
\det(zI-Q)=(z-1)
\left(z^2+\frac{b}{b+t}z-\frac{t(a-2)}{a(b+t)}\right).
\]

For the two nonunit roots \(\lambda_2,\lambda_3\), Vieta's formulas give

\[
\frac1{1-\lambda_2}+\frac1{1-\lambda_3}
=\frac{2-\lambda_2-\lambda_3}{(1-\lambda_2)(1-\lambda_3)}
=\frac{a(3b+2t)}{2(ab+t)}.
\]

The antisymmetric eigenvalue contributes \((b+t)/(b+2t)\). Therefore

\[
K_{a,b}(t)=a+b-4+\frac{a(3b+2t)}{2(ab+t)}
+\frac{b+t}{b+2t}.
\]

For \(a=2\), the middle class is empty. Instead the quotient is
\[
Q_2=\begin{pmatrix}t/(b+t)&b/(b+t)\\1&0\end{pmatrix}
\]
with eigenvalues \(1,-b/(b+t)\), while the antisymmetric mode contributes \(-t/(b+t)\) and there are \(b-1\) zero eigenvalues. This gives \(K_{2,b}(t)=b-1+(b+t)/(2b+t)+(b+t)/(b+2t)\), algebraically identical to the displayed all-\(a\) formula. At \(t=0\), either expression simplifies to \(a+b-3/2\). Subtraction and collecting factors proves the boxed difference identity, including the boundary cases.

### Unique optimal strength and sign transition

Put \(x=t/b\). The exact difference becomes
\[
\Delta_a(x)=\frac{x(4(a-2)x-3)}{2(1+2x)(a+x)},
\]
independent of \(b\) after this rescaling. Its derivative has the denominator \(2(1+2x)^2(a+x)^2>0\) and numerator
\[
F_a(x)=(8a^2-12a-2)x^2+8a(a-2)x-3a.
\]
For every integer \(a\ge2\), the leading coefficient is positive, the linear coefficient is nonnegative, and the constant term is negative. Hence \(F_a\) is strictly increasing for \(x>0\), starts negative and tends to positive infinity. There is exactly one positive root, with negative derivative before it and positive derivative afterward. This proves the unique global minimum, including the case \(a=2\), where \(F_2(x)=6(x^2-1)\) and \(x_*=1\). The sign of \(\Delta_a(x)\) itself follows directly from the numerator: if \(a=2\), it is negative for all \(x>0\); otherwise it changes sign exactly at \(x=3/[4(a-2)]\). In particular \(\Delta_a'(0)=-3/(2a)<0\).

### Universal sharp bound

For fixed \(x>0\), treat \(a\ge2\) temporarily as a real variable. Direct differentiation gives
\[
\frac{\partial \Delta_a(x)}{\partial a}
=\frac{x(2x+3)}{2(a+x)^2}>0.
\]
Consequently \(\Delta_a(x)\ge\Delta_2(x)=-3x/[2(1+2x)(2+x)]\), with strict inequality for \(a>2\). The elementary identity
\[
(1+2x)(2+x)-9x=2(x-1)^2\ge0
\]
then gives \(\Delta_2(x)\ge-1/6\), with equality precisely at \(x=1\). At \(x=0\) the difference is zero. Since \(x=t/b\), equality holds precisely when \(a=2,t=b\); any \(b\ge1\) is permitted. This completes the universal optimization proof.

### Balanced asymptotics

Substituting \(a=b=n\) and any fixed \(t>0\), the exact formula yields
\[
\lim_{n\to\infty}n^2\Delta_{n,n}(t)=\frac{t(4t-3)}2.
\]
For the unique optimum set \(t_n=n x_*(n)\). Dividing the quadratic equation \(F_n(x_*)=0\) by \(n\) and writing \(x_*=t_n/n\) gives
\[
\left(8-\frac{12}{n}-\frac2{n^2}\right)t_n^2
+8\left(n-2\right)t_n-3n=0,
\]
For \(n>2\), positivity of the quadratic coefficient shows \(t_n<3n/[8(n-2)]\), so the positive roots are uniformly bounded and the displayed equation implies \(t_n\to3/8\). The fixed-\(t\) limit can be applied uniformly on a compact neighborhood of \(3/8\), yielding \(-9/32\). At \(t=1\), the exact numerator in the boxed formula is \(n-8\), and the first limit is \(1/2\). The claims follow.

## Verification

The accompanying `verify.py` computes \(K(P)=\operatorname{tr}(I-P+\mathbf1\pi^{\mathsf T})^{-1}-1\) *independently* using exact rational Gauss–Jordan elimination. Here \(\pi_i\) is the normalized weighted degree. It compares the matrix value with the closed formula for all \(2\le a\le7\), \(1\le b\le8\), and five conductances \(0,1/3,1,5/2,10\): 240 exact comparisons. Additional exact checks test the sharp bound, balanced-graph sign transitions and the optimizer's derivative sign. The analytic proof above, not the finite-range computation, establishes the universal claims. Replay with a standard Python 3 installation by running `python verify.py`.

## Relationship to prior work

Hu and Kirkland's 2019 manuscript [1], especially Theorem 2.0.1 and its spectral proof, already computes the effect of inserting a **unit-weight** edge between twin vertices of a complete bipartite graph and classifies the unweighted Braess regimes. The unit-weight specialization of the formula here, \(\Delta_{a,b}(1)=(4a-3b-8)/[2(b+2)(ab+1)]\), is **not new** and is not claimed. The contribution is the continuous conductance-strength phase diagram, uniqueness and explicit value of the optimal strength for every biclique, the sharp graph-uniform improvement bound with equality cases, and the balanced-graph sign reversal under optimal conductance design. These results do not follow by taking a different *unit-edge* size in the published classification.

Altafini and colleagues [2] derive general edge-removal and inverse-matrix formulas for Kemeny's constant on weighted networks. Such formulas provide computational methods for individual weighted perturbations and are consistent with the present spectral calculation; the inspected source does not present the biclique-wide optimization, its sharp \(1/6\) bound, or the neutral-strength threshold. The general paper could in principle be specialized to recover the formulas here; the claim is a specific analytic classification, not a new general Kemeny perturbation identity. Faught, Kempton and Knudson [3] treat 1-separation formulas and Braess edges in other graph structures, not this full weighted biclique design problem.

## Limitations

The result concerns only one new *within-part* link with variable symmetric conductance, on otherwise unit-weight complete bipartite graphs. It does not classify simultaneous addition of several edges, varying original cross-part weights, directed networks, continuous-time generators, alternative normalization conventions, or global optimal edge design on arbitrary graphs. The paper [1] completely covers the unweighted specialization. No claim of independent scientific validation or historical uniqueness is made; another weighted family-specific calculation may exist beyond the inspected primary sources and indexed searches.

## References

[1] Y. Hu and S. Kirkland, *Complete Multipartite Graphs and Braess Edges*, manuscript dated June 6, 2019. https://mspace.lib.umanitoba.ca/server/api/core/bitstreams/04a4246d-2b67-4e4c-9c4b-60f0c5417031/content

[2] D. Altafini, D. A. Bini, V. Cutini, B. Meini and F. Poloni, *An edge centrality measure based on the Kemeny constant*, arXiv:2203.06459, first posted March 12, 2022. https://arxiv.org/abs/2203.06459

[3] N. Faught, M. Kempton and A. Knudson, *A 1-Separation Formula for the Graph Kemeny Constant and Braess Edges*, arXiv:2108.01061, first posted August 2, 2021. https://arxiv.org/abs/2108.01061
