# Exact negative Zagreb–Wiener dependence in uniform random recursive trees

## Finding
For every integer \(n\ge2\), let \(T_n\) be the rooted recursive tree obtained by giving each new vertex \(j\), \(2\le j\le n\), a parent chosen independently and uniformly from \(\{1,\ldots,j-1\}\). All degrees below are **undirected**. Define the first Zagreb index \(Z_n=\sum_{v\in T_n}\deg(v)^2\), the Wiener index \(W_n=\sum_{\{u,v\}\subset T_n}\operatorname{dist}(u,v)\), and harmonic sums \(H_n=\sum_{j=1}^n j^{-1}\), \(H_n^{(2)}=\sum_{j=1}^n j^{-2}\).

Then the exact mixed covariance is
\[
\operatorname{Cov}(Z_n,W_n)=n(n+1)\left[4H_n^{(2)}-2H_n+1+\frac{6}{n+1}-4H_n\left(\frac1n+\frac1{n+1}\right)\right]. \tag{1}
\]
It is zero for \(n=2,3\) and strictly negative for every \(n\ge4\). In particular,
\[
\operatorname{Cov}(Z_n,W_n)=-2n^2\log n+O(n^2). \tag{2}
\]
Using the previously established marginal variance asymptotics, the correlation satisfies
\[
\operatorname{Corr}(Z_n,W_n)\sim-\frac{3}{\sqrt{31-3\pi^2}}\,\frac{\log n}{\sqrt n}. \tag{3}
\]
The mechanism is stronger than an average sign: for **every fixed tree** \(T\) with \(n\ge3\) vertices, attaching one new leaf to a uniformly chosen vertex makes the two index increments strictly negatively correlated. Precisely,
\[
\operatorname{Cov}(\Delta Z,\Delta W\mid T)=\frac{8W(T)}{n^2}-2(n-1)<0. \tag{4}
\]

## Assumptions and scope
The model is the uniform increasing-parent tree, not the uniform unrooted Cayley tree or a preferential-attachment model. \(Z_n\) is the sum of *undirected* degree squares. \(W_n\) sums each unordered distinct pair once. The exact identity (1) is for every integer \(n\ge2\), the strict sign begins at \(n=4\), and asymptotics concern integer \(n\to\infty\). Conditional statement (4) applies to any deterministic tree with at least three vertices and a uniform attachment vertex; it does not assert global negative dependence for arbitrary random initial-tree laws.

## Proof
**1. A deterministic transmission identity.** For an arbitrary tree \(T\) on \(n\) vertices, write \(s(v)=\sum_u\operatorname{dist}(v,u)\). For each fixed root \(u\), deleting an edge whose component away from \(u\) has \(k\) vertices contributes \(2k-1\) to \(\sum_v\deg(v)\operatorname{dist}(u,v)\). Summing over the edges gives \(\sum_v\deg(v)\operatorname{dist}(u,v)=2s(u)-(n-1)\). Summing over \(u\) therefore yields
\[
\sum_v\deg(v)s(v)=4W(T)-n(n-1). \tag{5}
\]
This tree identity is classical as the Schultz/degree-distance relation; its use here is in the *joint random-index calculation*.

**2. Conditional increments.** Given a tree \(T\) of order \(n\), attach the new vertex at a uniform vertex \(V\). Directly from the definitions, \(\Delta Z=2\deg(V)+2\) and \(\Delta W=n+s(V)\). Because \(\sum_v\deg(v)=2(n-1)\) and \(\sum_v s(v)=2W(T)\), identity (5) gives
\[
\operatorname{Cov}(\deg(V),s(V)\mid T)=\frac{4W(T)}{n^2}-(n-1),
\]
which proves the equality in (4). The classical bound \(W(T)\le n(n^2-1)/6\) makes (4) at most \(-2(n-1)(n-2)/(3n)<0\) for \(n\ge3\). For completeness, the Wiener bound follows inductively: deleting a leaf \(\ell\) attached at \(v\) leaves a tree on \(n-1\) vertices, and adds \((n-1)+s(v)\) to \(W\); sorting distances from \(v\) gives \(s(v)\le(n-1)(n-2)/2\). Summation from the two-vertex tree yields the bound, attained by a path.

**3. Mixed covariance recurrence.** Conditioned on \(T_n\),
\[
\mathbb E[Z_{n+1}\mid T_n]=Z_n+6-\frac4n,\qquad
\mathbb E[W_{n+1}\mid T_n]=\left(1+\frac2n\right)W_n+n.
\]
Writing \(c_n=\operatorname{Cov}(Z_n,W_n)\), total covariance and (4) give
\[
c_{n+1}=\frac{n+2}{n}c_n+\frac8{n^2}\mathbb EW_n-2(n-1). \tag{6}
\]
The displayed Wiener mean recurrence, initialized at \(\mathbb EW_1=0\), has solution \(\mathbb EW_n=n(n+1)H_n-2n^2\); equivalently this mean is in Neininger's 2002 theorem. Therefore
\[
c_{n+1}=\frac{n+2}{n}c_n+\frac{8(n+1)}nH_n-2n-14,\qquad c_2=0. \tag{7}
\]
Normalize by \(n(n+1)\) and telescope (7). Using \(H_{n+1}=H_n+1/(n+1)\) and \(H_{n+1}^{(2)}=H_n^{(2)}+1/(n+1)^2\), direct substitution shows that the right side of (1), divided by \(n(n+1)\), has the increments prescribed by (7) and is zero at \(n=2\). This proves (1). Since \(c_3=0\) and all the conditional covariance terms in (6) are strictly negative from order three onward, \(c_n<0\) for all \(n\ge4\).

**4. Asymptotics.** The harmonic estimates \(H_n=\log n+\gamma+O(n^{-1})\) and \(H_n^{(2)}=\pi^2/6+O(n^{-1})\) give (2). Feng and Hu (2011) prove \(\operatorname{Var}(Z_n)\sim8n\); Neininger (2002) proves \(\operatorname{Var}(W_n)\sim(31-3\pi^2)n^4/18\). Combining them with (2) yields (3).

## Verification
The accompanying standalone `verify.py` uses only Python's standard library and exact rational arithmetic. It enumerates all \(5{,}913\) increasing-parent trees on orders \(2\) through \(8\), independently computes indices and vertex transmissions by graph traversal, and checks (1), (4), (5), the Wiener bound and mean. It also checks the covariance recurrence and strict sign through order \(300\). One execution produced `PASS trees=5913 exact_assertions=24271 exhaustive_orders=2..8 recurrence_orders=2..300`. These finite tests are diagnostics; the all-size proof is the argument above.

## Relationship to prior work
Feng and Hu, *On the Zagreb Index of Random Recursive Trees* (2011, DOI below), study the **marginal** Zagreb index: its mean, variance and normal limit (full text, pp. 1189–1195). Neininger, *The Wiener Index of Random Trees* (2002), treats the Wiener index and its joint asymptotic behavior with **internal path length** (full text, pp. 587–596). Neither source's theorems yield or state the mixed \(\operatorname{Cov}(Z_n,W_n)\). Eu, Yang and Yeh (2005) present the previously known **deterministic** Schultz–Wiener identity on trees, which is (5); (5) alone does not supply the mixed covariance recurrence. Hollas (2005) studies asymptotic independence of indices involving **independent random vertex marks** under a random tree model, not the present dependent tree-structural pair. Together these references motivate but do not imply the new exact formula and conditional-negative-increment mechanism.

## Limitations
This is a result on uniform recursive trees; no statement is made for Cayley trees, binary search trees, or nonuniform attachment. The asymptotic correlation relies on published marginal variance constants. The source comparison is a best-knowledge originality assessment, not a guarantee that no earlier equivalent identity exists. The finite verifier does not prove the infinite claim.

## References
1. R. Neininger (2002), *The Wiener Index of Random Trees*, Combinatorics, Probability and Computing 11, 587–597, DOI:10.1017/S0963548302005321.
2. Q. Feng and Z. Hu (2011), *On the Zagreb Index of Random Recursive Trees*, Journal of Applied Probability 48, 1189–1196, DOI:10.1239/jap/1324046027.
3. S.-P. Eu, B.-Y. Yang and Y.-N. Yeh (2005), *Generalized Wiener Indices in Hexagonal Chains*, publicly accessible manuscript, https://www.iis.sinica.edu.tw/papers/byyang/2380-F.pdf; see Section 1.2, Theorem 1 for the known Schultz identity on trees.
4. B. Hollas (2005), *Asymptotically Independent Topological Indices on Random Trees*, Journal of Mathematical Chemistry 38, 379–387, DOI:10.1007/s10910-005-6474-5.
