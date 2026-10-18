# Sharp bridge-activation threshold for dual numerical-radius functionals on double stars

## Finding

Let \(D_{p,q}\) be the diameter-three tree obtained by joining two hubs, with \(p\ge1\) leaves at the first and \(q\ge1\) at the second. Orient edges away from any chosen root. On \(\ell^2(V(D_{p,q});\mathbb C)\), define the weighted shift \(S_a e_u=\sum_{u\to v}a_{uv}e_v\), with freely variable complex edge weights \(a\). The edge-space norm is \(N(a)=w(S_a)\), where \(w(T)=\sup_{\|h\|_2=1}|\langle Th,h\rangle|\).

For each real \(\beta\ge0\), let
\[
L_\beta(a)=\sum_{e\ \mathrm{pendant}} a_e+\beta a_{e_0},
\]
where \(e_0\) is the bridge joining the hubs. The exact dual norm is
\[
\boxed{\|L_\beta\|_{N^*}=\begin{cases}
2(\sqrt p+\sqrt q),&0\le\beta\le(pq)^{1/4},\\[3pt]
2\sqrt{p+q+\beta^2+pq/\beta^2},&\beta>(pq)^{1/4}.
\end{cases}}
\]
The bound is attained. Among weights constant on the two leaf orbits, the bridge weight in every maximizer vanishes up to and including the critical threshold, and is strictly positive above it. This is an exact activation threshold for an entire family of dual functionals rather than a single path evaluation.

## Assumptions and scope

The field is complex; \(p,q\) are arbitrary positive integers, and \(\beta\in[0,\infty)\). All \(p+q+1\) edge coordinates are independent. The orientation may be any orientation rooted at a vertex; the numerical-radius norm and the stated dual-functional value are invariant under such a choice. No positivity constraint is imposed on admissible complex edge vectors: positivity is established as an allowable reduction for this particular positive-coefficient functional. All suprema are over the full closed numerical-radius unit ball; finite dimensionality ensures attainment. The bridge and pendant sums each count edges exactly once.

## Proof

**1. Numerical radius as a tree adjacency norm.** Write \(A_{|a|}\) for the real symmetric weighted adjacency matrix of the undirected tree, with weight \(|a_e|\) on each edge. Unique root-to-vertex paths permit a diagonal unitary gauge that makes all nonzero tree-shift coefficients nonnegative. Further, the depth grading satisfies \(e^{i\theta}S_a\) unitarily similar to \(S_a\). Hence the standard numerical-radius formula gives
\[
N(a)=\max_{\theta\in\mathbb R}\lambda_{\max}\!\left(\operatorname{Re}(e^{i\theta}S_a)\right)
=\frac12\lambda_{\max}(A_{|a|})=\frac12\rho(A_{|a|}).
\]
The last equality is Perron–Frobenius for a symmetric nonnegative matrix. The formula shows \(N\) is an absolute, permutation-invariant norm on the edge coordinates (positivity and the norm axioms also follow from the numerical-radius norm on operators).

**2. Symmetrization without loss.** For any complex weight vector with \(N(a)\le1\), triangle inequality and the preceding formula yield \(|L_\beta(a)|\le L_\beta(|a|)\) and \(N(|a|)=N(a)\). Average \(|a|\) over independent permutations of the \(p\) and \(q\) pendant edges. Convexity of \(N\) preserves feasibility, and the functional value stays unchanged. Thus there is an optimal nonnegative vector with a common weight \(x\) on the first pendant orbit, a common weight \(y\) on the second, and bridge weight \(c\ge0\). The objective becomes \(p x+q y+\beta c\).

**3. Four-vertex reduction and exact feasible region.** The adjacency matrix vanishes on all leaf-difference subspaces. On the orthogonal complement spanned by the two normalized leaf sums and the two hubs, it becomes the weighted four-vertex path whose consecutive weights are
\[
u=\sqrt p\,x,\qquad c,\qquad v=\sqrt q\,y.
\]
Under its bipartition, the positive eigenvalue bound reduces to the largest singular value of
\[
M=\begin{pmatrix}u&0\\c&v\end{pmatrix}.
\]
Consequently \(N(a)\le1\) is equivalent to \(\|M\|_{2\to2}\le2\). For nonnegative \(u,v,c\), the exact semidefinite criterion \(4I-M^{\mathsf T}M\succeq0\) is
\[
0\le u\le2,\quad0\le v\le2,\quad
4c^2\le(4-u^2)(4-v^2).
\]
(The determinant condition and the first principal-minor condition imply the remaining diagonal condition for \(0\le u,v\le2\); all boundary cases are included.) Since \(\beta\ge0\), take the maximum admissible \(c=\tfrac12\sqrt{(4-u^2)(4-v^2)}\) whenever it is useful. Put \(u=2\cos\theta\), \(v=2\cos\phi\), where \(\theta,\phi\in[0,\pi/2]\). Then the resulting objective is
\[
2\left(\sqrt p\cos\theta+\sqrt q\cos\phi+
\beta\sin\theta\sin\phi\right).
\]

**4. One-variable maximization.** For fixed \(\theta\), maximizing over \(\phi\) gives
\[
2\left(\sqrt p\cos\theta+
\sqrt{q+\beta^2\sin^2\theta}\right).
\]
Set \(z=\sin^2\theta\in[0,1]\). The desired norm is precisely twice the maximum of
\[
F(z)=\sqrt p\sqrt{1-z}+\sqrt{q+\beta^2 z}.
\]
This continuous function is strictly concave in \(z\) (the first summand already is), with
\[
F'(0)=\frac12\left(\frac{\beta^2}{\sqrt q}-\sqrt p\right).
\]
If \(\beta^2\le\sqrt{pq}\), concavity forces its unique maximum to occur at \(z=0\), of value \(\sqrt p+\sqrt q\). If \(\beta^2>\sqrt{pq}\), the unique interior critical point is
\[
z_* =\frac{\beta^4-pq}{\beta^2(\beta^2+p)}\in(0,1).
\]
The derivative equation \(\beta^4(1-z_*)=p(q+\beta^2 z_*)\) yields
\[
F(z_*)=\frac{\sqrt{(\beta^2+p)(\beta^2+q)}}{\beta}.
\]
Multiplying by two gives the two advertised branches, which meet continuously at \(\beta=(pq)^{1/4}\). No finite-grid argument is used in this maximization.

**5. Sharpness and activation.** Below and at the threshold choose \(u=v=2\), \(c=0\); equivalently, set \(x=2/\sqrt p\), \(y=2/\sqrt q\). This gives \(N(a)=1\) and objective \(2(\sqrt p+\sqrt q)\). Above threshold, take \(z=z_*\), \(\sin\theta=\sqrt{z_*}\), and select
\[
\cos\phi=\frac{\sqrt q}{\sqrt{q+\beta^2z_*}},\qquad
\sin\phi=\frac{\beta\sqrt{z_*}}{\sqrt{q+\beta^2z_*}}.
\]
Choose \(x=2\cos\theta/\sqrt p\), \(y=2\cos\phi/\sqrt q\), \(c=2\sin\theta\sin\phi\). These coefficients satisfy the singular-value constraint with equality and attain the second branch. Moreover \(c>0\) there, whereas strict concavity forces \(\theta=\phi=0\) and thus \(c=0\) for any orbit-symmetric optimal triple at or below the threshold (at \(\beta=0\), \(c\) is still forced to zero by \(u=v=2\)). This proves the stated activation law and completes the argument.

## Verification

The standalone Python 3 standard-library program `verify_double_star.py` evaluates the exact formula, checks the optimizing witness against the two-by-two spectral feasibility condition, verifies the stationary identity with exact rational arithmetic, checks rational equality certificates at small dimensions, and compares to an independently enumerated finite grid. The program should print `VERIFY_OK`. Its floating-point tests confirm specific examples only: the proof for all \(p,q,\beta\) is entirely analytic and appears above.

For a simple exact witness, at \(p=q=1\) and \(\beta=2\), assign pendant weights \(1\) on each side and bridge weight \(3/2\). The corresponding two-by-two matrix has largest singular value exactly \(2\) because \((4-1)(4-1)=4(3/2)^2\), and the functional value is \(1+1+2(3/2)=5\), matching the second branch.

## Relationship to prior work

Budzynski–Dymek–Planeta–Ptak (2017) develop the Hilbert-space weighted-shift framework on directed trees, including multiplier algebra, reflexivity, and Wold-type decompositions; their inspected text does not evaluate these finite double-star numerical-radius dual functionals. Sharif (2023) studies numerical radius as a norm of unilateral weighted-shift coefficients and its relation to Banach limits. His finite block calculations concern path shifts; the double-star branching and independent bridge multiplier are different parameters.

A publicly indexed graph-edge numerical-radius result establishes strict convexity exactly for stars and triangles and classifies smooth points for general graphs; its complete publicly accessible result concerns geometry of the **primal** norm rather than the **dual support value** of the sum-of-pendant-edges functional on a double star. The already-known special case of a three-link uniform path agrees with \(p=q=1,\beta=1\) and is not claimed anew. The contribution here is the all-branching exact dual norm and its sharp bridge-activation transition.

## Limitations

The result treats only free complex edge coefficients on finite double stars with positive pendant counts and a nonnegative, uniform bridge multiplier. It does not classify arbitrary signed or unequal coefficients in the dual or numerical-radius support functionals on general trees. The equality description concerns orbit-symmetric representatives, not uniqueness among all nonsymmetric optimal weight vectors. The proof is self-contained but no independent mathematical audit has been performed. An equivalent expression may exist in unindexed literature under Perron-root support-function or weighted-path language.

## References

1. P. Budzynski, P. Dymek, A. Planeta, M. Ptak, *Weighted shifts on directed trees. Their multiplier algebras, reflexivity and decompositions*, arXiv:1702.00765v1, first public 2017-02-02, https://arxiv.org/abs/1702.00765, especially §§1–4,6; primary MSC 47B37.
2. A. Sharif, *On the numerical radius of weighted shifts on \(\ell^2\) as a norm on \(\ell^\infty\) and connections to Banach limits*, arXiv:2303.00876v1, first public 2023-03-02, https://arxiv.org/abs/2303.00876, especially §§1–2 and 4.
3. *Strict convexity and the full smooth locus of graph-edge numerical-radius norms*, publicly accessible RESULT.md, record identifier ending `12716bf88722`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-strict-convexity-and-the-full-smooth-locus-of-graph-edge-numeric--12716bf88722, especially Finding and Proof.
