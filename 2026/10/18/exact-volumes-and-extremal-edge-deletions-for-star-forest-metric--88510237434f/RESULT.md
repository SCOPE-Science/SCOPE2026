# Exact volumes and extremal edge deletions for star-forest metric Lipschitz balls

## Finding

**Theorem.** Fix integers \(N\ge3\) and \(1\le M\le N-2\). Let \(H\) be a star forest on a labeled \(N\)-vertex set, with exactly \(M\) edges and nontrivial components \(K_{1,m_1},\ldots,K_{1,m_s}\), where each \(m_i\ge1\). Its other vertices are isolated. Form the connected graph \(G=K_N\setminus E(H)\), equipped with its unit-edge shortest-path metric. Write \(V(G)\) for the \((N-1)\)-dimensional Lebesgue volume of the anchored real Lipschitz unit ball. Then

\[
\boxed{V(G)=N+\sum_{i=1}^{s}\frac{2m_i}{N-m_i}.}
\]

With \(N\) and \(M\) fixed, \(V(G)\) is maximized uniquely up to graph isomorphism when the deleted edges form one star \(K_{1,M}\), with the remaining \(N-M-1\) vertices isolated. Its maximum is \(N+2M/(N-M)\). It is minimized uniquely up to graph isomorphism when there are \(s_*:=\min\{M,N-M\}\) nontrivial deleted stars whose numbers of leaves differ by at most one. Precisely, writing \(M=q s_*+r\), where \(0\le r<s_*\), the minimum is

\[
\boxed{V_{\min}=N+2\left(\frac{(s_*-r)q}{N-q}+\frac{r(q+1)}{N-q-1}\right).}
\]

In particular, for \(N\ge2M\), the minimizing deletion forest is a matching and has volume \(N+2M/(N-1)\).

## Assumptions and scope

For a fixed base vertex \(v_0\), the anchored Lipschitz ball is

\[
Q_G=\bigl\{(f(v))_{v\ne v_0}:f(v_0)=0,\ |f(u)-f(v)|\le1\ \text{for every edge }uv\in E(G)\bigr\}.
\]

A change of base vertex is a unimodular integral change of coordinates, so \(V(G)=\operatorname{vol}_{N-1}(Q_G)\) is independent of the anchor. The graph \(G\) has diameter at most two because each deleted star has a vertex outside its component, which is adjacent to both endpoints of each deleted edge. Consequently the edge inequalities encode the full Lipschitz norm of the shortest-path metric. The theorem concerns *star forests of missing edges*, not arbitrary forests or weighted graphs.

## Proof

**1. The equilateral baseline.** For \(K_N\), fixing one coordinate at zero identifies its Lipschitz ball with the set of \(N-1\) other coordinates having global range at most one, including the fixed zero. Directly integrating over the position of the minimum gives \(V(K_N)=N\). Equivalently, the \(d\)-cube section \(\{x\in[-1,1]^d:\max x-\min x\le1\}\) has volume \(d+1\) for \(d=N-1\).

**2. One deleted star.** Suppose the missing edges are exactly those joining a center \(c\) to \(m\) leaves. Put \(k=N-m-1\ge1\) and anchor \(f(c)=0\). The \(k\) other vertices form a clique with the leaves, whereas the center is adjacent to all of the \(k\) other vertices. Write \(y\in[-1,1]^k\) for their potentials, with range \(r=\max_j y_j-\min_j y_j\le1\). Conditional on \(y\), all \(m\) leaf potentials lie inside a common interval of length \(2-r\in[1,2]\) and have mutual range at most one. For any positive integer \(m\), the volume of \(m\) points in a length-\(L\) interval with range at most one is \(mL-(m-1)\) for \(L\ge1\). To see this for \(m\ge2\), integrate the joint density \(m(m-1)(L-r)r^{m-2}\) of the range from zero to one; the case \(m=1\) is immediate. Thus the conditional leaf volume is \(m+1-mr\).

Define
\[
J_k=\int_{[-1,1]^k}\mathbf1_{\{\operatorname{range}(y)\le1\}}\,dy,
\quad R_k=\int_{[-1,1]^k}\operatorname{range}(y)\mathbf1_{\{\operatorname{range}(y)\le1\}}\,dy.
\]
For \(k=1\), \(J_1=2\) and \(R_1=0\). For \(k\ge2\), the range density on \([0,1]\) is \(k(k-1)(2-r)r^{k-2}\); therefore \(J_k=k+1\), \(R_k=k-2/(k+1)\). Substitution yields
\[
V(K_N\setminus K_{1,m})=(m+1)J_k-mR_k=N+\frac{2m}{N-m}.
\]
The notation on the left means deletion of precisely the edges of a specified embedded star.

**3. Additivity for disjoint deleted stars.** The original equilateral ball is contained in \(Q_G\). Away from measure-zero ties, a potential in \(Q_G\) but outside that ball has a unique global minimum and maximum separated by more than one. That pair cannot be adjacent in \(G\), so it must be a missing edge belonging to exactly one star of \(H\). Call this exceptional region \(A_i\) if its extreme pair belongs to star \(i\). The \(A_i\) are disjoint. If the extreme separation is \(r>1\), every vertex outside star \(i\) is adjacent in \(G\) to both extreme vertices, and hence its potential lies in the intersection of their unit neighborhoods, an interval of length \(2-r<1\). In particular, all missing-edge constraints belonging to other stars already hold automatically. Thus \(A_i\) is exactly the exceptional region of the graph with only star \(i\) deleted. Its volume is \(2m_i/(N-m_i)\) by step 2. Adding these disjoint region volumes to the equilateral baseline proves the asserted formula.

**4. Sharp extremal shapes.** For \(1\le m<N\), let \(\phi(m)=2m/(N-m)\). For positive \(a,b\) with \(a+b\le M\), \(\phi(a+b)>\phi(a)+\phi(b)\); merging two deleted stars strictly increases the volume. Therefore a single \(M\)-edge star is the unique maximizer. Conversely, when \(s<s_*\), there is an unused vertex (since \(M+s<N\)) and some star has at least two leaves (since \(M>s\)). Splitting that star into two nontrivial stars using the unused vertex strictly reduces volume. Hence a minimizer must have \(s=s_*\). For fixed \(s_*\), the discrete increments
\[
\phi(m+1)-\phi(m)=\frac{2N}{(N-m-1)(N-m)}
\]
are strictly increasing in \(m\). Moving one leaf from a star exceeding another by at least two to the smaller one strictly decreases total volume. Thus every minimizing leaf-size profile is as balanced as possible; substituting its sizes gives the displayed minimum. These inequalities are strict except for relabeling or permutation of equal component sizes.

## Verification

The accompanying standalone Python checker independently enumerates integer points in the dilates of eleven small-dimensional anchored Lipschitz balls. For each dimension \(d=N-1\), it recovers the leading Ehrhart coefficient using the \(d\)-th forward finite difference divided by \(d!\), and compares this exact rational value to the formula. Tested graph orders are \(N=4,5,6,7\), with up to three deleted stars; all eleven comparisons agree. As the defining edge-difference inequalities have integer right-hand sides and a totally unimodular constraint matrix, all vertices are integral, so these are ordinary Ehrhart polynomials. The finite checks corroborate, but do not substitute for, the analytical proof of the all-dimensional statement.

Run the checker with a standard Python interpreter: `python verify_starforest.py`.

## Relationship to prior work

The transportation-cost/Lipschitz-free identification and representation of the corresponding finite graph spaces as quotients of edge-coordinate spaces are part of the established functional-analytic framework [1]. General finite-metric Lipschitz-free volume products and equilateral bodies are studied in [2]. Combinatorial descriptions of Lipschitz polytopes are developed in [3]. Those works supply context, but the inspected sections do not give the stated additive formula for complements of star forests or the exact extremal deletion theorem. The matching case of the formula is an elementary specialization and agrees with earlier separate computations for graphs with disjoint deleted pairs; it is not separately asserted as new. There is no claim of originality for the general range-density integral used in the proof.

## Limitations

Only deletions forming a disjoint union of stars are covered, and \(M\le N-2\) ensures the complement has the specified diameter-two shortest-path metric. The theorem does not establish volume additivity for general missing-edge graphs. The volume is normalized in anchored (integer-lattice) coordinates, not orthonormal zero-sum Euclidean coordinates. Independent scientific review has not yet been performed. Bibliographic searches may miss equivalent results expressed in different language.

## References

[1] O. Ostrovska and M. I. Ostrovskii, *On relations between transportation cost spaces and \(\ell_1\)*, arXiv:1910.03625, publicly posted 8 October 2019, https://arxiv.org/abs/1910.03625.

[2] M. Alexander, M. Fradelizi, L. C. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642, publicly posted 24 November 2019, https://arxiv.org/abs/1911.10642.

[3] J. Gordon and F. Petrov, *Combinatorics of the Lipschitz Polytope*, arXiv:1608.06848 (first public preprint 2016; journal 2017), https://arxiv.org/abs/1608.06848.
