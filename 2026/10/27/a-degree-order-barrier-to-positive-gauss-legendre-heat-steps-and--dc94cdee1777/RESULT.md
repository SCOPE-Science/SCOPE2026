# A degree–order barrier to positive Gauss–Legendre heat steps, and the exact toroidal-grid exception

## Finding

Let \(G\) be a finite, connected, simple, undirected, unweighted, \(d\)-regular graph with \(d\ge2\) and \(N\) vertices. Put \(L=dI-A\), where \(A\) is the adjacency matrix. For the completed two-stage, fourth-order Gauss–Legendre heat step,
\[
T_G(h)=(12I-6hL+h^2L^2)(12I+6hL+h^2L^2)^{-1},\qquad h\ge0,
\]
**every graph satisfying \(N\ge3d\) has an existing edge \(\{u,v\}\) with \((T_G(h))_{uv}<0\) for all sufficiently large finite \(h\)**. The sign failure is not a spectral instability: \(T_G(h)\) is symmetric positive definite, has unit row sums, and contracts the Euclidean norm for every \(h\ge0\).

For all integers \(m,n\ge3\), the unweighted periodic square-grid graph \(C_m\square C_n\) has **an entrywise nonnegative completed step for every \(h\ge0\) if and only if \(m=n=3\)**. In this exceptional nine-vertex case, with
\[
D(h)=(3h^2+3h+1)(3h^2+6h+4),
\]
the diagonal, adjacent off-diagonal, and nonadjacent off-diagonal entries are respectively
\[
\frac{9h^4+3h^3+h^2+2h+4}{D(h)},\qquad
\frac{4h(h+1)}{D(h)},\qquad
\frac{2h^2(3h+2)}{D(h)}.
\]
All nine-vertex entries are strictly positive at each positive step.

## Assumptions and scope

Graphs are finite, simple, connected, undirected, and have unit edge conductances. \(N=|V(G)|\), \(A\) is the symmetric adjacency matrix, and \(d\) the common degree; graph Laplacians are unnormalized. \(L^+\) means the Moore–Penrose pseudoinverse. The map refers only to the **completed numerical step**, not to internal Runge–Kutta stages, other Padé orders, or nonlinear flows. A matrix is entrywise nonnegative precisely when it sends every coordinatewise nonnegative vector to a nonnegative vector. For cycles \(C_j\) the integers satisfy \(j\ge3\), so each is a simple graph.

The degree–order inequality is **sufficient**; the conclusion can also hold when \(N<3d\). No optimal universal threshold in \(N/d\) is asserted. The toroidal-grid classification is, however, necessary and sufficient within the stated family.

## Proof

**1. The edge-pseudoinverse sum has a universal positive lower bound.** Since \(G\) is connected and regular, list the adjacency eigenvalues as \(d=\mu_1>\mu_2\ge\cdots\ge\mu_N\ge-d\). Its Laplacian eigenvalues are \(d-\mu_i\). For the orthogonal constant-vector projector \(J/N\), spectral calculus gives
\[
\operatorname{tr}(AL^+)=\sum_{i=2}^{N}\frac{\mu_i}{d-\mu_i}.
\]
The trace identities \(\sum_i\mu_i=0\) and \(\sum_i\mu_i^2=\operatorname{tr}(A^2)=Nd\) imply
\[
\begin{aligned}
\operatorname{tr}(AL^+)
&=-1+\frac1d\sum_{i=2}^{N}\frac{\mu_i^2}{d-\mu_i}\\
&\ge-1+\frac{\sum_{i=2}^{N}\mu_i^2}{2d^2}
=\frac{N-3d}{2d}.
\end{aligned}
\]
Here \(d-\mu_i\le2d\); equality term-by-term is possible only when each nonconstant adjacency eigenvalue lies in \(\{0,-d\}\). If \(N=3d\), equality would force exactly one occurrence of \(-d\), since \(\sum_{i=2}^{N}\mu_i=-d\), and would hence give \(\sum_{i=2}^{N}\mu_i^2=d^2\). But the true squared sum is \(Nd-d^2=2d^2\), a contradiction. Thus \(\operatorname{tr}(AL^+)>0\) for every \(N\ge3d\).

Because the graph is simple and undirected,
\[
\operatorname{tr}(AL^+)=2\sum_{\{u,v\}\in E(G)}(L^+)_{uv}.
\]
At least one **actual edge** therefore has \((L^+)_{uv}>0\). This is stronger than merely locating some positive pseudoinverse off-diagonal entry.

**2. Positive pseudoinverse edges force large-step negativity.** For a Laplacian eigenvalue \(\lambda\ge0\), the scalar stability function is
\[
R(h\lambda)=\frac{(h\lambda)^2-6h\lambda+12}{(h\lambda)^2+6h\lambda+12}.
\]
For \(\lambda>0\), \(0<R(h\lambda)<1\) at \(h>0\), and \(R(h\lambda)=1-12/(h\lambda)+O(h^{-2})\). The zero mode has \(R(0)=1\). Since there are finitely many strictly positive Laplacian eigenvalues,
\[
T_G(h)=I-\frac{12}{h}L^++O(h^{-2})
\]
in any fixed matrix norm as \(h\to\infty\). For an edge found in Step 1, its off-diagonal entry equals \(-12(L^+)_{uv}/h+O(h^{-2})<0\) for all sufficiently large \(h\). Since \(R(0)=1\), all row sums equal one. Moreover, \(0<R(h\lambda)\le1\) at every finite nonnegative \(h\), giving symmetry, positive definiteness, and Euclidean nonexpansivity by the spectral theorem.

**3. The exceptional torus has a positive closed form.** In \(C_3\square C_3\), the adjacency spectrum is \(4\) once, \(1\) four times, and \(-2\) four times. The Laplacian spectrum is consequently \(0,3,6\) with the same multiplicities. Its projectors are constant on the three vertex-pair classes. The identity mode contributes \(1/9\) to each entry. The \(3\)- and \(6\)-eigenspace projector entries are respectively \((4/9,4/9)\) on the diagonal, \((1/9,-2/9)\) on adjacent pairs, and \((-2/9,1/9)\) on nonadjacent pairs. Combining these coefficients with \(R(3h)\) and \(R(6h)\) gives precisely the three rational expressions in the Finding. Their denominators are positive and each numerator is positive at \(h>0\). At \(h=0\), \(T_G(0)=I\).

**4. All other tori eventually lose positivity.** Every \(C_m\square C_n\) with \(m,n\ge3\) is connected and four-regular, with \(N=mn\). Apart from \((m,n)=(3,3)\), we have \(N\ge12=3d\), so Steps 1–2 give a negative adjacent transition for every sufficiently large \(h\). This completes the classification.

## Verification

The accompanying standalone standard-library script `verify_regular_gauss.py` evaluates graph Laplacians, their exact-rational pseudoinverses, and the rational Gauss step at five nonnegative test magnitudes on seven selected regular graphs. It recomputes matrix inverses using rational Gaussian elimination, checks the pseudoinverse relation, traces and edge sums, entry symmetry and mass preservation, verifies all three formulas for \(C_3\square C_3\), and checks exact negative entries at \(h=100\) on \(C_3\square C_4\) and \(C_6\). The recorded output is `verify_output.txt`.

Counts: seven graphs; 35 exact-rational step matrices; 270 row-sum checks; 405 torus-formula entry checks; seven spectral-trace checks. The computer checks are **finite regressions**, not an exhaustive graph classification, and do not replace the infinite-family argument above.

To reproduce, run `python verify_regular_gauss.py` in a directory containing the embedded script; compare stdout to `verify_output.txt`. Python's standard library suffices.

## Relationship to prior work

The two-stage Gauss–Legendre method and its diagonal Padé stability function are classical. General Runge–Kutta monotonicity and absolute-monotonicity theory is established by Higueras and the implicit SSP literature; such method-wide analyses do not directly imply the graph-dependent signed edge sum derived here. The accessible full-text study of Bresten and collaborators treats **explicit multistep Runge–Kutta** methods and finite SSP timestep restrictions, rather than implicit two-stage Gauss steps on symmetric graph heat equations.

Previously obtained special-family classifications cover Gauss end-step positivity on unweighted cycles, hypercubes, complete multipartite graphs, and strongly regular graphs. In particular, the nine-vertex rook-graph positivity case is **covered** by the strongly regular classification; it is used here only as the necessary endpoint of the new **whole-toroidal-family** dichotomy. None of those special families encompasses all connected regular graphs satisfying \(N\ge3d\). The new statement is the structural degree–order obstruction, its edgewise pseudoinverse proof, and the complete classification across all Cartesian products of two cycles.

The authors did not establish that no specialized historical presentation of an equivalent edge-pseudoinverse inequality exists. Abstract-level and inaccessible full-text comparisons leave residual originality uncertainty.

## Limitations

No positivity guarantee is given for internal Runge–Kutta stages, directed or weighted networks, or nonregular graphs. The general obstruction is one-sided and may be true for some graphs with \(N<3d\). It does not furnish a universal explicit finite step threshold, though it guarantees existence. At \(h=0\), all completed matrices equal the identity. Numerical tests at finite graph orders cannot establish all-graph conclusions. The strongest residual literature risk is a previously published regular-graph edge-pseudoinverse bound or a specialized toroidal-grid Gauss positivity theorem; certain relevant publisher full texts were not accessible.

## References

1. I. Higueras, *Strong Stability for Additive Runge–Kutta Methods*, SIAM J. Numer. Anal. 44 (2006), 1735–1758, DOI: 10.1137/040612968. First published online 2006-09-26. Monotonicity framework; publisher abstract and bibliographic information inspected.
2. C. Bresten, S. Gottlieb, Z. Grant, D. Higgs, D. I. Ketcheson, and A. Németh, *Explicit Strong Stability Preserving Multistep Runge–Kutta Methods*, arXiv:1307.8058 (first version dated 2013-07-30). Full accessible HTML inspected: https://arxiv.org/html/1307.8058v2 .
3. D. I. Ketcheson, C. B. Macdonald, and S. Gottlieb, *Optimal Implicit Strong Stability Preserving Runge–Kutta Methods*, Applied Numerical Mathematics (2009), DOI: 10.1016/j.apnum.2008.03.034. Relevant competing method-wide comparison; publisher abstract available, full text not inspected.
