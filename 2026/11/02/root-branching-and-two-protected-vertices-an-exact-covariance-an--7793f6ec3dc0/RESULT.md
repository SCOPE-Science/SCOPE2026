# Root branching and two-protected vertices: an exact covariance and a negative limiting constant

## Finding

Let \(T_n\) be the uniform random recursive tree with labels \(1,\ldots,n\), let \(D_n\) be the outdegree of its root (vertex \(1\)), and let \(P_n\) count **two-protected vertices**: vertices having at least one child, none of whose children is a leaf. For every integer \(n\ge3\), put
\[
L(z)=-\log(1-z),\qquad F(z)=1-e^{-z}-z+\frac{z^2}{2}.
\]
Then the following is an exact finite-size identity:
\[
\boxed{\begin{aligned}
\operatorname{Cov}(D_n,P_n)&=[z^{n-1}]\left(\frac{(1+L(z))F(z)}{(1-z)^2}
+\frac{(L(z)-z)e^{-z}}{1-z}\right)\\
&\quad-nH_{n-1}[z^n]\frac{F(z)}{1-z},
\end{aligned}}
\]
where \(H_j=\sum_{r=1}^{j}1/r\). In particular, as \(n\to\infty\),
\[
\boxed{\operatorname{Cov}(D_n,P_n)=\frac12-\frac3e+
\frac{1+e^{-1}}{2(n-1)}+O(n^{-2}).}
\]
The limiting covariance is strictly negative, approximately \(-0.6036383235\). At the first three orders the exact covariances are \(\operatorname{Cov}(D_3,P_3)=-1/4\), \(\operatorname{Cov}(D_4,P_4)=-5/12\), and \(\operatorname{Cov}(D_5,P_5)=-31/72\). It contrasts with the previously established positive limiting root-degree/leaf-count covariance; the two statistics measure different properties.

## Assumptions and scope

For each \(j=2,\ldots,n\), vertex \(j\) selects its parent independently and uniformly from \(\{1,\ldots,j-1\}\). Equivalently, each of the \((n-1)!\) recursive trees is equally likely. The root is vertex \(1\); its outdegree is its number of children, not the number of its descendants. A two-protected vertex is neither a leaf nor the parent of any leaf. The coefficient operator \([z^k]\) extracts the \(k\)-th coefficient of the Taylor expansion at zero. The formula covers every integer \(n\ge3\); the asymptotic expansion holds along positive integers \(n\to\infty\).

## Proof

**1. Increasing-tree marking.** Let \(T(z,q)\) be the exponential generating function of increasing rooted labeled trees, with a weight \(q\) for each two-protected vertex. A root's unordered collection of child subtrees contributes \(e^{T(z,q)}\) after differentiating to remove its smallest label. A child that is a leaf is represented by the singleton term \(z\); thus the root itself is two-protected exactly when its collection contains at least one child subtree, all of them nonsingletons. Marking that case yields the formal differential equation
\[
T'(z,q)=e^{T(z,q)}+(q-1)\big(e^{T(z,q)-z}-1\big),\quad T(0,q)=0.
\]
At \(q=1\) its solution is \(T(z,1)=L(z)\). Differentiating with respect to \(q\) and writing \(A(z)=\partial_q T(z,q)|_{q=1}\) gives
\[
A'(z)=\frac{A(z)}{1-z}+\frac{e^{-z}}{1-z}-1,\qquad A(0)=0.
\]
Direct substitution gives the unique solution
\[
A(z)=\frac{F(z)}{1-z},\qquad
\mathbb E[P_n]=n[z^n]A(z)
=n\left(\frac12-\sum_{j=0}^{n}\frac{(-1)^j}{j!}\right).
\]
The latter recovers the known protected-node first moment; it is not claimed as new.

**2. Distinguishing the root degree.** Let \(G(z,u,q)\) be the corresponding exponential generating function with an additional weight \(u\) for every child of the original root (but not for children at other vertices). Its child subtrees are still enumerated by \(T(z,q)\). Exactly the same decomposition gives
\[
G'(z,u,q)=e^{uT(z,q)}+(q-1)\big(e^{u(T(z,q)-z)}-1\big),
\qquad G(0,u,q)=0.
\]
The mixed formal derivative evaluated at \(u=q=1\) is
\[
\left.\partial_u\partial_qG'(z,u,q)\right|_{u=q=1}
=\frac{(1+L(z))F(z)}{(1-z)^2}+
\frac{(L(z)-z)e^{-z}}{1-z}.
\]
Since the number of increasing rooted trees on \(n\) labels is \((n-1)!\), the coefficient of \(z^{n-1}\) on the left equals \(\mathbb E[D_nP_n]\). Independence of the parent choices also gives \(\mathbb E[D_n]=H_{n-1}\). Subtracting the product of means proves the exact finite-size identity.

**3. Sharp asymptotics.** Write \(w=1-z\) and \(a=\frac12-e^{-1}\). Define entire functions (removable singularities filled in)
\[
U(w)=\frac{F(1-w)-a+w/e}{w^2},\qquad
V(w)=\frac{e^{-1}e^w-e^{-1}}{w}.
\]
They satisfy \(U(0)=\frac12-\frac1{2e}\), \(V(0)=e^{-1}\). The mixed derivative in step 2 is identically
\[
\frac{a(1+L(z))}{(1-z)^2}-\frac{2}{e(1-z)}
+L(z)\big(U(w)+V(w)\big)
+U(w)+e^{-1}+(w-1)V(w).
\]
For \(m\ge1\),
\[
[z^m]\frac{1+L(z)}{(1-z)^2}=(m+1)H_m+1.
\]
Since \(U+V\) is entire and equals \((1+e^{-1})/2\) at \(w=0\), its product with \(L(z)\) has coefficient \((1+e^{-1})/(2m)+O(m^{-2})\). To justify the error, subtract that constant, factor out \(1-z\), and use \([z^m](1-z)L(z)=-1/(m(m-1))\) for \(m\ge2\), together with absolute exponential decay of coefficients of the remaining entire factor. The last three analytic terms have exponentially decreasing coefficients. Thus, for \(m=n-1\),
\[
\mathbb E[D_nP_n]
=a\big(nH_{n-1}+1\big)-\frac2e+
\frac{1+e^{-1}}{2(n-1)}+O(n^{-2}).
\]
Finally \(\mathbb E[P_n]=an+O(1/n!)\), by the alternating exponential tail, and \(H_{n-1}=O(\log n)\). Subtracting \(H_{n-1}\mathbb E[P_n]\) establishes the asserted expansion.

## Verification

Run `python verify_protected_covariance.py` in the directory containing this document. The verifier uses exact rational power-series arithmetic, independently enumerates all recursive trees through nine vertices via parent arrays, and compares the first and mixed moments and covariances. It also checks the previously known exact mean through ninety vertices and numerical consistency with the proved asymptotic remainder at selected larger sizes. A successful run prints `PASS: 297 independent exact/finite checks`. The infinite assertions are established by the formal generating-function proof above; finite checking does not prove them.

## Relationship to prior work

Devroye and Janson (2013) derive the limiting proportion of protected nodes in random recursive trees using fringe-subtree limits, but do not give a covariance with the original root's degree. Mahmoud and Ward (2015) give an exact protected-node mean and linear-order variance; their tree decomposition does not supply this mixed root-degree moment. Holmgren and Janson (2015) prove broad limit laws and covariances for **counts of fringe-subtree types**, including protected-node totals and degree-count profiles, rather than the degree of one distinguished root. Toofanpour, Javanian and Imany-Nabiyyi (2022) study protected and nonprotected *depth profiles*, not the covariance between their total protected count and the root degree. The exact bivariate root-marked formula and its finite negative limiting constant are the assessed distinction, not the earlier protected-node expectation or the generic exponential-formula construction.

## Limitations

The result concerns uniformly grown random recursive trees, not plane recursive trees, preferential attachment trees, or uniformly random Cayley trees. The exact coefficient formula itself is not a simple finite product; a provided program evaluates it. The asymptotic expansion implies negative covariance for all sufficiently large sizes, but no general finite-size strict-sign theorem or stochastic-order comparison is asserted. Historical implicit coverage by a general marked-increasing-tree identity is possible; independent verification of literature priority has not been performed.

## References

1. Luc Devroye and Svante Janson, *Protected nodes and fringe subtrees in some random trees*, arXiv:1310.0665v1, first posted 2013-10-02. https://arxiv.org/abs/1310.0665 (especially Section 7).
2. Hosam M. Mahmoud and Mark D. Ward, *Asymptotic properties of protected nodes in random recursive trees*, Journal of Applied Probability 52 (2015), 290–297. https://doi.org/10.1239/jap/1429282623
3. Cecilia Holmgren and Svante Janson, *Limit laws for functions of fringe trees for binary search trees and random recursive trees*, Electronic Journal of Probability 20 (2015), article 4. https://doi.org/10.1214/EJP.v20-3627
4. Jaleh Toofanpour, Mehri Javanian and Ramin Imany-Nabiyyi, *Normal limit law for protected node profile of random recursive trees*, Theory of Probability and Its Applications 67 (2022), 452–464. https://doi.org/10.1137/S0040585X97T991040
