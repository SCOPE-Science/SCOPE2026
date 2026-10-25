# Gcd-controlled Euclidean inballs of rectangular Monge polytopes

## Finding
For every pair of integers \(p,q\ge2\), let \(N=pq\), \(g=\gcd(p,q)\), and let \(\mathcal M_{p,q}\) consist of real \(p\)-by-\(q\) matrices \(X\) satisfying
\[
X_{ij}\ge0,\qquad \sum_{i,j}X_{ij}=1,\qquad
\Delta_{ij}X:=X_{ij}+X_{i+1,j+1}-X_{i,j+1}-X_{i+1,j}\ge0.
\]
Here \(0\le i<p-1\), \(0\le j<q-1\) in the last inequality, with zero-based indices throughout. Reversing column order gives the conventional Monge inequality; this is an ambient Euclidean isometry.

**Theorem.** The intrinsic Euclidean inradius in the affine hyperplane \(\sum X_{ij}=1\), using the Frobenius metric, is
\[
\boxed{\displaystyle
 r_{p,q}=\left[\sqrt{N(N-1)}+
 \frac{N^{2}-p^{2}-q^{2}+g^{2}}6\right]^{-1}.}
\]
The affine dimension of the entire set of centers of maximum-radius balls is exactly \(g-1\). Thus the incenter is unique if and only if \(p\) and \(q\) are coprime, while rectangular dimensions sharing a factor have a positive-dimensional center locus.

The center set also has an explicit all-parameter description. Define half-open integer intervals \(I_i=[iq,(i+1)q)\) and \(J_j=[N-(j+1)p,N-jp)\), and write \(\lambda_{ij}=|I_i\cap J_j|\). Put
\[
T_{p,q}=\sum_{a=1}^{p-1}\sum_{b=1}^{q-1}\min\{ab,(p-a)(q-b)\}
=\frac{N^2-p^2-q^2+g^2}{12}.
\]
Every maximum-ball center, and no other, is
\[
X=r_{p,q}\sqrt{1-N^{-1}}\,\mathbf1+2r_{p,q}Y,
\]
where \(Y_{ij}\ge0\), every \(\Delta_{ij}Y=1\), and \(Y_{ij}=0\) whenever \(\lambda_{ij}>0\). This is a nonempty bounded affine polytope of dimension \(g-1\). At every center all adjacent-Monge facets are tangent; the coordinate facets indexed by positive \(\lambda_{ij}\) are also tangent.

For \(p=q=n\), the formula reduces to the already known square-Monge radius, \(\big[n^2\sqrt{1-n^{-2}}+n^2(n^2-1)/6\big]^{-1}\). The new aspect is the full rectangular formula and its coprimality/center-degeneracy dichotomy.

## Assumptions and scope
Both dimensions are integers at least two; no symmetry of the matrix is imposed. All balls lie in the intrinsic \((N-1)\)-dimensional affine hull, not the full \(\mathbb R^N\). Distances use the unweighted Frobenius norm. If the opposite sign convention for Monge inequalities is used, reversing the column order preserves all results. All assertions hold without genericity assumptions on \(p,q\).

## Proof
**1. Exact insphere constraints.** The irredundant facets of the generic normalized Monge polytope are precisely the \(N\) coordinate nonnegativity inequalities and the \((p-1)(q-1)\) adjacent-Monge inequalities (Erickson--Kretschmann, Theorem 5.3). In \(\sum X_{ij}=1\), a coordinate functional has gradient norm \(\alpha=\sqrt{1-1/N}\); an adjacent Monge functional has gradient norm \(2\), since its four coefficients sum to zero and have squared sum four. Thus a closed intrinsic ball of radius \(r\), centered at \(X\), is contained in \(\mathcal M_{p,q}\) exactly when
\[
X_{ij}\ge r\alpha,\qquad \Delta_{ij}X\ge2r.
\]
For \(r>0\), setting \(Y=(X-r\alpha\mathbf1)/(2r)\) reduces these constraints to \(Y\ge0\), \(\Delta Y\ge1\), and \(\sum Y=(1-Nr\alpha)/(2r)\).

**2. A sharp transport bound.** The integer matrix \(\lambda\) above has row sums \(q\), column sums \(p\), and total mass \(N\). Let \(U\) denote the all-ones matrix, which has the same margins. For any real array \(Y\), discrete summation by parts gives
\[
\sum_{i,j}(U_{ij}-\lambda_{ij})Y_{ij}
=\sum_{a=1}^{p-1}\sum_{b=1}^{q-1}w_{ab}\Delta_{a-1,b-1}Y,
\qquad
w_{ab}=\sum_{i\ge a,j\ge b}(U_{ij}-\lambda_{ij}).
\]
Because \(\lambda\) counter-pairs the two interval partitions, its mass in the upper-right subrectangle is \(\max\{0,N-aq-bp\}\). Therefore
\[
w_{ab}=(p-a)(q-b)-\max\{0,N-aq-bp\}
=\min\{ab,(p-a)(q-b)\}>0.
\]
If \(Y\ge0\) and \(\Delta Y\ge1\), we consequently have
\[
\sum Y=\sum\lambda_{ij}Y_{ij}+
\sum_{a,b}w_{ab}\Delta_{a-1,b-1}Y\ge T_{p,q}.
\]
Equality is possible only when every adjacent mixed difference equals one and every entry on the positive support of \(\lambda\) vanishes.

**3. Attainment and strict relative interior.** The transportation cost matrix \(c_{ij}=ij\) is strictly supermodular. If a transportation plan gives positive mass to cells \((i,j)\) and \((k,l)\) with \(i<k\) and \(j<l\), shifting an equal amount to \((i,l)\) and \((k,j)\) decreases the objective strictly by the product of the row and column gaps. Thus the counter-paired plan \(\lambda\) is the *unique* minimum-cost plan with row margins \(q\) and column margins \(p\). Uniqueness also follows by filling the first row from the largest available columns and inducting.

Finite-dimensional transportation duality supplies numbers \(a_i,b_j\) satisfying \(a_i+b_j\le ij\), with equality on the positive support of \(\lambda\). In fact the inequalities can be made strict off this support. To see this without assuming strict complementarity, perturb the cost to \(c'_{ij}=ij-\varepsilon\) on the zero support cells and leave the other costs unchanged. The transportation polytope has finitely many vertices and \(\lambda\) has a strictly positive objective gap from every other vertex, so for sufficiently small \(\varepsilon>0\) it remains optimal. Dual potentials for this perturbed cost therefore give \(Y_{ij}=ij-a_i-b_j=0\) on the positive support and \(Y_{ij}\ge\varepsilon\) off it. Mixed differences of this array are identically one, and it attains \(\sum Y=T_{p,q}\). Conversely the equality conditions in step 2 describe every minimizer.

**4. The gcd evaluation.** For \(k=0,\dots,N-1\), the two anti-paired cells have zero-based indices \(i=\lfloor k/q\rfloor\) and \(j=q-1-\lfloor k/p\rfloor\). Write \(r_m(k)\) for the remainder of \(k\) on division by \(m\). Direct expansion of the floor products, using the identity \(\lfloor k/m\rfloor=(k-r_m(k))/m\), gives
\[
T_{p,q}=\sum_{k=0}^{N-1}\left\lfloor\frac{k}{q}\right\rfloor
\left\lfloor\frac{k}{p}\right\rfloor-\frac{N(p-1)(q-1)}4.
\]
The required elementary sums are
\[
\sum_{k=0}^{N-1}k\,r_m(k)=\frac{N(m-1)(3N+m-2)}{12}
\quad(m=p,q),
\]
and
\[
\sum_{k=0}^{N-1}r_p(k)r_q(k)
=\frac{N(g^2+3N-3p-3q+2)}{12}.
\]
For the second identity, put \(p=gP\), \(q=gQ\). By the Chinese remainder theorem, each pair of remainders congruent modulo \(g\) occurs exactly \(g\) times among \(N\) consecutive integers. Summing the arithmetic progressions in each congruence class yields the stated expression. Combine these sums with \(\sum k^2=N(N-1)(2N-1)/6\) to obtain
\[
T_{p,q}=\frac{N^2-p^2-q^2+g^2}{12}.
\]
This identity independently shows its numerator is divisible by twelve.

**5. Radius and dimension.** Steps 1--3 force \(1\ge r(N\alpha+2T_{p,q})\), and equality is achieved by the constructed \(Y\). This proves the radius and center characterization. It remains to count free center parameters. Any array with all \(\Delta Y=1\) is of the form \(Y_{ij}=ij-a_i-b_j\), with \(p+q-1\) free affine parameters after quotienting the common potential shift. The bipartite graph whose edges are positive cells of \(\lambda\) has exactly \(g\) connected components, each a tree: its components correspond to the intervals between consecutive common partition boundaries, which occur at multiples of \(\operatorname{lcm}(p,q)=N/g\). Hence it has \(p+q-g\) edges, imposing that many independent equations \(Y_{ij}=0\). The nonnegativity constraints introduce no further *affine* equalities because step 3 constructed a minimizer strictly positive at every remaining cell. Thus the incenter locus has dimension \((p+q-1)-(p+q-g)=g-1\), as claimed.

## Verification
The accompanying standard-library exact-rational script `monge_rectangular_exact_check.py` checks the interval coupling, both margins, support forest, equality dual potentials, strict positivity off the transport support, all adjacent mixed differences, weighted summation identity, gcd-square specialization, and exact mass formula for every \(2\le p,q\le12\) (121 cases). A separate symbolic integer sweep checked the gcd closed form for 1,156 pairs with \(2\le p,q\le35\). Independent numerical Chebyshev linear programs corroborated the formula at \((p,q)=(2,2),(2,3),(3,4),(4,6),(5,6),(6,9)\). Finite computations corroborate, but do not establish, the theorem for all parameters; the proof above does.

To rerun: `python3 monge_rectangular_exact_check.py`. It requires only the Python standard library.

## Relationship to prior work
Erickson and Kretschmann (2023), arXiv:2311.07522, fully accessible HTML text, establish the complete generic Monge facet system and motivate approximation by near-Monge matrices; their paper discusses combinatorial structure and volume, not this metric inball classification. Erickson and Jones (2026), arXiv:2609.09508, publicly available September 8, study a lattice-path formula for normalized volume and Ehrhart series. Its full text was not accessible in this review; its abstract, title and metadata were examined, so absence of any unadvertised inball result cannot be certified. A previously published research record, *An affine \(n-1\)-cube of Euclidean incenters for square Monge polytopes* (October 2026), covers the **square** specialization of the radius and center locus. That known specialization is not claimed here as new. The rectangular gcd formula, the unique-incenter criterion for coprime dimensions, and the transport-support description do not follow as stated from a theorem restricted to square shapes.

## Limitations
The contribution concerns the standard Frobenius metric on the normalized *nonsymmetric* Monge polytope, not an arbitrary affine metric or the symmetric/hollow-symmetric subpolytopes. The incenter face is specified by exact equations and inequalities and its dimension is determined, but no independent enumeration of its vertices or Euclidean volume is claimed. Novelty is limited by inaccessible full text of one relevant September 2026 preprint and by possible earlier results under transportation-duality terminology; historical priority requires further human bibliographic inspection. Independent scientific audit has not been performed.

## References
1. W. Q. Erickson and J. Kretschmann, *The structure and normalized volume of Monge polytopes*, arXiv:2311.07522 (first posted 2023-11-13), Sections 1, 2 and 5, especially Theorem 5.3. https://arxiv.org/abs/2311.07522
2. W. Q. Erickson and N. B. Jones, *A lattice path model for the volume of the Monge polytope*, arXiv:2609.09508 (first posted 2026-09-08). https://arxiv.org/abs/2609.09508
3. *An affine \(n-1\)-cube of Euclidean incenters for square Monge polytopes*, published research record, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-affine-n-1-cube-of-euclidean-incenters-for-square-monge-polyt--b3dc6b94166a
