# A sharp depth crossover for root branching in uniform plane trees

## Finding

Let \(T_n\) be a uniformly random rooted ordered (plane) tree on \(n\) vertices. Set \(R_n\) equal to the root's number of children and \(N_{n,h}\) equal to its number of vertices at distance \(h\) from the root. For all integers \(n\ge2\) and \(1\le h\le n-1\), write \(C_{n-1}=\frac1n\binom{2n-2}{n-1}\). Then

\[
\boxed{\operatorname{Cov}(R_n,N_{n,h})=\frac{2(2n-1)(n+1-h-2h^2)}{(n+1)(n+h)(n+h+1)}\frac{\binom{2n-2}{n-h-1}}{C_{n-1}}.}
\]

Every factor outside \(n+1-h-2h^2\) is positive. In particular the covariance is strictly positive when \(2h^2+h<n+1\), strictly negative when \(2h^2+h>n+1\), and zero precisely when \(n=2h^2+h-1\). At each fixed size \(n\ge3\), increasing the depth yields a single transition from positive to negative, possibly through one zero. The root profile at depth zero is deterministic and has covariance zero.

For any sequence of integer depths with \(h_n/\sqrt n\to t\in(0,\infty)\),

\[
\boxed{\operatorname{Cov}(R_n,N_{n,h_n})\longrightarrow4(1-2t^2)e^{-t^2}.}
\]

The crossover is at \(t=1/\sqrt2\). Thus root branching favors population at shallow depths while suppressing population at sufficiently deep levels, and this qualitative change persists at macroscopic square-root depth.

## Assumptions and scope

A plane tree is a finite rooted tree with a linear order on the children of every vertex. Trees of order \(n\) are equiprobable, so each has probability \(1/C_{n-1}\). The distance of a vertex from the root is its number of edges on the root path. The statement covers all admissible positive depths and all sizes, without any asymptotic assumption for the exact identity. At depth \(h=0\), \(N_{n,0}=1\); for \(h\ge n\), \(N_{n,h}=0\). The limit concerns covariances, not correlations or joint weak convergence.

## Proof

Write \(T(z)=\sum_{n\ge1}C_{n-1}z^n\). Decomposing at the root gives \(T=z/(1-T)\), with the unique series solution \(T=(1-\sqrt{1-4z})/2\). Set \(u=T/(1-T)\). For an integer depth \(h\ge0\), let

\[
A_h(z)=\sum_{\tau}z^{|\tau|}N_h(\tau),
\]

where the sum runs over all finite plane trees, and \(N_h(\tau)\) is the number of vertices at depth \(h\) of \(\tau\). Since the root is the unique depth-zero vertex, \(A_0=T\). For \(h\ge1\), the distinguished depth-\(h\) vertex belongs to one of the root's ordered child subtrees. Marking one child among \(k\) yields

\[
A_h=z\sum_{k\ge1}kT^{k-1}A_{h-1}=\frac{z}{(1-T)^2}A_{h-1}=uA_{h-1},
\]

where the last equality uses \(z=T(1-T)\). Hence \(A_h=Tu^h\). Lagrange inversion applied to \(T=z/(1-T)\) yields, for integers \(n\ge h+1\),

\[
a_{n,h}:=[z^n]A_h(z)=\frac{2h+1}{n+h}\binom{2n-2}{n-h-1}.
\]

This also holds for \(h=0\), where it reduces to the Catalan number. One way to check the coefficient is to express \(Tu^h=T^{h+1}(1-T)^{-h}\), apply \([z^n]F(T(z))=(1/n)[u^{n-1}]F'(u)(1-u)^{-n}\), and simplify the two resulting binomial terms with factorial identities.

For \(h\ge1\), let \(B_h(z)=\sum_{\tau}z^{|\tau|}R(\tau)N_h(\tau)\). Before specialization, give the root \(k\) children an auxiliary weight \(v^k\). The expression for the depth-marked trees is \(zvA_{h-1}/(1-vT)^2\). Differentiating with respect to \(v\) at \(v=1\) gives

\[
B_h=\frac{zA_{h-1}(1+T)}{(1-T)^3}=A_h\frac{1+T}{1-T}=A_h+2A_{h+1}.
\]

Thus \(\mathbb E[R_nN_{n,h}]=(a_{n,h}+2a_{n,h+1})/C_{n-1}\), and \(\mathbb E[N_{n,h}]=a_{n,h}/C_{n-1}\). Since \(R_n=N_{n,1}\), the coefficient formula gives \(\mathbb E[R_n]=3(n-1)/(n+1)\). Consequently,

\[
\operatorname{Cov}(R_n,N_{n,h})=\frac{2a_{n,h}}{C_{n-1}}\left(\frac{a_{n,h+1}}{a_{n,h}}-\frac{n-2}{n+1}\right).
\]

For \(1\le h\le n-1\), including the top depth with \(a_{n,n}=0\),

\[
\frac{a_{n,h+1}}{a_{n,h}}=\frac{(2h+3)(n-h-1)}{(2h+1)(n+h+1)}.
\]

Combining the fractions in the preceding covariance expression yields

\[
\frac{a_{n,h+1}}{a_{n,h}}-\frac{n-2}{n+1}
=\frac{(2n-1)(n+1-h-2h^2)}{(2h+1)(n+h+1)(n+1)}.
\]

Substituting the explicit \(a_{n,h}\) proves the exact formula. Because the polynomial \(n+1-h-2h^2\) is strictly decreasing in positive integer \(h\), and is positive at \(h=1\) for \(n\ge3\) and negative at \(h=n-1\), the single sign-transition statement follows. The equality case is the integer equation \(n=2h^2+h-1\).

For the limit, divide the two central-binomial terms using the telescoping product

\[
\frac{\binom{2n-2}{n-h-1}}{\binom{2n-2}{n-1}}
=\prod_{j=0}^{h-1}\frac{n-1-j}{n+j}.
\]

When \(h/\sqrt n\to t\in(0,\infty)\), a uniform Taylor expansion of logarithms gives the log of the product as \(-h^2/n+o(1)\), so it tends to \(e^{-t^2}\). Substituting \(C_{n-1}=\binom{2n-2}{n-1}/n\) into the exact covariance formula shows that its other factor tends to \(4(1-2t^2)\). Multiplication proves the asserted scaling limit.

## Verification

The standalone standard-library Python script `verify.py` enumerates every rooted plane tree on two through twelve vertices: 82,499 trees total. It computes root degree and the full depth profile directly, checks their exact rational means and covariances against the closed formulas for every permitted depth, then checks signs and exact zero cases algebraically for every size from 2 through 300. An execution returns `VERIFY_OK trees 82499 assertions 45024`. This finite test detects algebraic or indexing mistakes but is not the proof for arbitrary size, which is given above. Reproduce with `python3 verify.py`.

## Relationship to prior work

The Catalan/conditioned Galton–Watson representation, root-degree asymptotics, and vertex depth profiles are classical, as developed in Janson's 2011 survey. Janson's 2003 paper gives joint Wiener-index and internal-path-length asymptotics but does not state a root-degree by depth-level covariance. The later distance-profile study establishes profile distributions and analyzes conditioning on root degree; its general limiting statements do not directly determine the exact finite-depth sign polynomial. The present claim concerns the exact mixed moment of the distinguished root and each whole generation, including the unique finite-size sign boundary and the square-root-depth crossover.

## Limitations

This is a mathematical proof and a finite independent implementation check, not an independently audited priority determination. Broad generating-function frameworks could imply or reproduce the identity after a separate calculation. The limit assumes depths are of order \(\sqrt n\) with a positive finite scaling parameter; it does not assert a uniform error bound over all depths, nor a joint distribution theorem. No claims are made for nonuniform simply generated trees.

## References

1. S. Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, arXiv:1112.0510 (first posted 2011-12-02), https://arxiv.org/abs/1112.0510.
2. S. Janson, *The Wiener Index of Simply Generated Random Trees*, Random Structures & Algorithms 22 (2003), 337–358, DOI:10.1002/rsa.10074.
3. *The distance profile of rooted and unrooted simply generated trees*, Combinatorics, Probability and Computing, https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/distance-profile-of-rooted-and-unrooted-simply-generated-trees/ (full article; bibliographic authorship not asserted here).
4. S. Wagner, *Central Limit Theorems for Additive Tree Parameters with Small Toll Functions*, Combinatorics, Probability and Computing (2014), DOI:10.1017/S0963548314000443.
