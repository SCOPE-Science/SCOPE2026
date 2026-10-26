# Sharp clique-edge activation threshold for fastest mixing on pineapple graphs

## Finding
Let \(P_{n,m}\) be the **pineapple graph** obtained by attaching \(m\) distinct pendant leaves to a single vertex of the complete graph \(K_n\). For every integer \(n\ge3\), integer \(m\ge2\), and total budget \(B>0\), allow arbitrary nonnegative, undirected edge conductances \(w_e\) with \(\sum_e w_e=B\). Let \(L(w)\) be the unnormalized weighted Laplacian and \(\lambda_2(L(w))\) its second-smallest eigenvalue.

Put \(S_n=\sqrt{n(n-1)/2}\), \((z)_+=\max(z,0)\), and
\[
D_{n,m}=n+m-1-\frac{(S_n-m)_+^2}{n+m}.
\]
Then the **exact unrestricted optimum** is
\[
\boxed{\max_{w_e\ge0,\ \sum_e w_e=B}\lambda_2(L(w))=\frac{B}{D_{n,m}}.}
\]
The clique edges **not incident** with the leaf-attachment vertex obey a sharp allocation dichotomy:

* If \(m\ge S_n\), **every** globally optimal allocation gives every such clique edge weight zero. The uniform star on the \(n+m-1\) hub edges is optimal.
* If \(2\le m<S_n\), **every** globally optimal allocation gives positive weight to at least one such clique edge. An optimal allocation exists giving strictly positive weight to *each* available edge.

Thus the point at which all interior clique edges become dispensable is determined by the comparison of \(m\) with \(\sqrt{n(n-1)/2}\); no symmetry is assumed of competing conductances.

## Assumptions and scope
The clique consists of a hub \(v\) and \(n-1\) other vertices; each of the \(m\) leaves attaches only to \(v\). Conductances are permitted to vanish. The Laplacian convention is \(L_{ij}=-w_{ij}\) for adjacent distinct vertices and \(L_{ii}=\sum_{j\ne i}w_{ij}\); zero is its lowest eigenvalue. There is no per-edge upper bound, and the total unweighted conductance cost is exactly \(B\). This result does not cover \(m=1\), unequal edge costs, prescribed positive minimum conductances, or discrete-time Markov-chain optimization.

An explicit optimal design follows. Set \(\rho=B/D_{n,m}\). If \(m\ge S_n\), give each hub-to-clique and hub-to-leaf edge weight \(\rho\), and every edge between two non-hub clique vertices weight zero. If \(2\le m<S_n\), define
\[
a_* =\frac{m+1+m(n-1)/S_n}{n+m},\qquad
b_* =\frac{1-a_*}{n-1},\qquad
c_* =\frac{n+S_n}{n+m}.
\]
Give every hub-to-other-clique edge weight \(\rho a_*\), every edge between two other clique vertices weight \(\rho b_*\), and each pendant edge weight \(\rho c_*\). Here \(0<a_*<1\), \(b_*>0\), and \(c_*>1\).

## Proof
**1. Unrestricted symmetrization.** On the subspace \(\mathbf1^\perp\), the Rayleigh-quotient characterization makes \(w\mapsto\lambda_2(L(w))\) concave. Permuting the non-hub clique vertices and independently permuting the leaves preserves the graph and the budget. Averaging any feasible allocation over \(S_{n-1}\times S_m\) cannot lower \(\lambda_2\). It is therefore enough **for the optimal value** to consider three conductances: \(a\) on the \(n-1\) hub-to-clique edges, \(b\) on the \(\binom{n-1}{2}\) clique-internal edges, and \(c\) on the \(m\) pendant edges. Their cost is
\[
C(a,b,c)=(n-1)a+\frac{(n-1)(n-2)}2b+mc.
\]
This averaging argument is valid for arbitrary nonsymmetric competitors; it does not assert that all optimizers are symmetric.

**2. Exact spectral decomposition.** The leaf-difference subspace supplies eigenvalue \(c\) with multiplicity \(m-1\). The non-hub-clique-difference subspace supplies \(a+(n-1)b\) with multiplicity \(n-2\). On the three-dimensional subspace of vectors constant on each of the hub, other-clique, and leaf classes, the eigenvalues are zero and the two roots \(\mu_-\le\mu_+\) of
\[
\mu^2-[na+(m+1)c]\mu+(n+m)ac=0.
\]
Consequently \(\lambda_2=\min\{c,a+(n-1)b,\mu_-\}\). A positive target gap requires \(a,c>0\).

**3. Normalize the target gap to one.** Positive homogeneity reduces the maximum-gap problem to minimizing \(C(a,b,c)\) subject to \(\lambda_2\ge1\). Since \(m\ge2\), necessarily \(c\ge1\); also \(a+(n-1)b\ge1\). For \(a>0\), \(c\ge1\), and \(m\ge2\), the sum of the two quotient roots is \(na+(m+1)c>3\), hence \(\mu_+>1\). The condition \(\mu_-\ge1\) is therefore equivalent to
\[
F(a,c):=1-na-(m+1)c+(n+m)ac\ge0.
\]
If \(0<a<1\), this and \(c\ge1\) are feasible only when
\[
a>\frac{m+1}{n+m},\qquad
c\ge c_{\min}(a):=\frac{na-1}{(n+m)a-(m+1)}>1.
\]
The minimum affordable \(b\) is \((1-a)/(n-1)\). If \(a\ge1\), taking \(b=0,c=1\) is feasible, and the least cost in that region is attained at \(a=1\), namely \(n+m-1\).

For \((m+1)/(n+m)<a<1\), the minimum budget at fixed \(a\) is the strictly convex function
\[
G(a)=\frac n2a+\frac{n-2}2+m\,\frac{na-1}{(n+m)a-(m+1)},
\]
with derivatives
\[
G'(a)=\frac n2-\frac{m^2(n-1)}{((n+m)a-(m+1))^2},\qquad
G''(a)=\frac{2m^2(n-1)(n+m)}{((n+m)a-(m+1))^3}>0.
\]
As \(a\) approaches its lower feasible endpoint, \(G'(a)\to-\infty\), while \(G'(1)=n/2-m^2/(n-1)\). Hence the unique interior minimum occurs precisely if \(m<S_n\); otherwise the global minimum is the boundary \(a=1\). In the interior case, solving \(G'(a)=0\) gives the listed \(a_*,b_*,c_*\), and direct substitution yields
\[
G(a_*)=n+m-1-\frac{(S_n-m)^2}{n+m}.
\]
All the spectral constraints are met, with \(\mu_-=1\), \(a_*+(n-1)b_*=1\), and \(c_*>1\). At the boundary allocation \(a=c=1,b=0\), the quotient roots are \(1\) and \(n+m\); the leaf and clique-difference eigenvalues are also \(1\). Scaling these unit-gap optimal allocations by \(B/D_{n,m}\) proves the exact optimal value.

**4. Support statements for every optimizer.** In the regime \(m\ge S_n\), strict convexity and the boundary analysis show that the *unique averaged optimal* triple has \(b=0\). The averaged internal-clique weight is the mean of nonnegative weights of all original internal clique edges; therefore every such weight in **any** original optimizer must be zero. In the regime \(m<S_n\), \(D_{n,m}<n+m-1\). If an allocation used no internal clique edges, the remaining permitted graph would be a star with \(n+m-1\) edges. Symmetry averaging on that star shows its maximum achievable gap under budget \(B\) is \(B/(n+m-1)\), strictly less than \(B/D_{n,m}\). Hence no global optimum in this regime can have all internal clique conductances zero.

## Verification
The included `verify.py` reconstructs every weighted Laplacian from its edge list; independently checks the three-block eigenvalue factorization, exact budget, predicted optimizer, and threshold across \(16\times15\) parameter pairs; and checks the global bound against many nonsymmetric random budgets. On its recorded run it completed **1,779 checks without assertion failure**. These finite checks are supporting evidence only; the proof above supplies the all-parameter result. Run with `python3 verify.py` in an environment with NumPy installed.

The special threshold equality \(m=S_n\) occurs, for example, at \((n,m)=(9,6)\), and correctly belongs to the zero-internal-edge regime. In contrast, at \((n,m)=(4,2)\) the interior-clique weight is strictly positive and the optimal spectral gap strictly exceeds that of the uniform star.

## Relationship to prior work
The objective is the continuous-time fastest-mixing Markov-process / weighted algebraic-connectivity problem introduced by Sun, Boyd, Xiao and Diaconis; their general semidefinite and geometric-duality framework does not supply this closed-form two-parameter pineapple allocation law. Ghosh and Boyd explain convexity and symmetry in related algebraic-connectivity optimization, but do not derive this pendant-clique threshold. Topcu, Sorgun and Haemers investigate adjacency cospectrality of the *same graph family*, not an arbitrary-conductance Laplacian optimization. Previously established network-design formulas for a clique with two leaves attached at distinct vertices, for wheels with a hub leaf, and for vertex-transitive graphs with leaves attached to every vertex concern different attachment patterns; none specializes to this theorem. A reported pineapple curvature-distortion optimization addresses a different invariant and does not supply this spectral-gap budget objective.

## Limitations
The claim concerns the exact convex optimum and the universal *support dichotomy* only. It does not classify all potentially asymmetric optimal conductance vectors. No assertion of independent verification or publication priority is made. Specialized or nonindexed historical work on weighted pineapple graphs may still establish the same result; the literature searches are evidence of a bounded comparison, not proof of uniqueness in the literature. The finite program is not an infinite mathematical certificate. Extensions to unequal costs or one leaf require separate analysis.

## References
1. A. Ghosh and S. Boyd, “Upper bounds on algebraic connectivity via convex optimization,” *Linear Algebra and its Applications* **418** (2006), 693–707, DOI: `10.1016/j.laa.2006.03.006`; openly available online **2006-05-05**.
2. J. Sun, S. Boyd, L. Xiao, and P. Diaconis, “The fastest mixing Markov process on a graph and a connection to a maximum variance unfolding problem,” *SIAM Review* **48** (2006), 681–699, DOI: `10.1137/S0036144504443821`; electronic publication **2006-11-02**.
3. H. Topcu, S. Sorgun, and W. H. Haemers, “On the spectral characterization of pineapple graphs,” arXiv:`1511.08674`, first posted **2015-11-27**.
