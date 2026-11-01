# A square-law inball transition for uniform cross-polytope sums

## Finding

The complete uniform-hypergraph sum of coordinate cross-polytopes has an exact insphere and an abrupt change in the number of facets touched by that insphere. For integers \(n\ge k\ge3\), set
\[
H_{n,k}=\sum_{\substack{I\subseteq[n]\\|I|=k}}\operatorname{conv}\{\pm e_i:i\in I\}\subset\mathbb R^n.
\]
Its unique largest Euclidean ball is centered at the origin, and its radius is
\[
\boxed{r_{n,k}=\binom{n-1}{k-1}\min\left\{1,\frac{\sqrt n}{k}\right\}.}
\]
The number of **facets** tangent to this ball is exactly \(2^n\) when \(n<k^2\), exactly \(2^n+2n\) when \(n=k^2\), and exactly \(2n\) when \(n>k^2\). More precisely, the outward unit normals of tangent facets are precisely the sign vectors \(\varepsilon/\sqrt n\) for \(n<k^2\), the coordinate normals \(\pm e_i\) for \(n>k^2\), and their union when \(n=k^2\). No other facet touches the maximum ball.

## Assumptions and scope

We use the standard Euclidean metric on \(\mathbb R^n\), unit vectors \(e_1,\ldots,e_n\), and ordinary, unweighted Minkowski addition. The parameter range is the complete set of integers \(3\le k\le n\). The **inradius** is the radius of the largest Euclidean ball contained in the full-dimensional polytope. A facet is **tangent** if its supporting hyperplane meets that ball. The symbol \(\binom ab\) is zero for integers \(0\le a<b\). The equal-weight complete \(k\)-uniform hypergraph is essential; no assertion is made for arbitrary hypergraphs or nonuniform weights.

For \(1\le j\le n\), define
\[
B_j=\binom nk-\binom{n-j}k,\qquad A_j=\binom{n-j-1}{k-1}\quad(0\le j<n),
\]
with \(A_j=0\) once its upper binomial argument is below \(k-1\). Then \(B_j=\sum_{\ell=0}^{j-1}A_\ell\).

## Proof

**1. Exact support and halfspaces.** The support function of each summand is \(h_{\diamond_I}(u)=\max_{i\in I}|u_i|\). If \(0\le a_1\le\cdots\le a_n\) are the ordered absolute coordinates of \(u\), then counting \(k\)-subsets by their greatest index gives
\[
h_{H_{n,k}}(u)=\sum_{j=k}^{n}\binom{j-1}{k-1}a_j. \tag{1}
\]
In particular, the maximum of \(\sum_{i\in J}\varepsilon_i x_i\), over \(x\in H_{n,k}\), equals \(B_j\) whenever \(|J|=j\) and all \(\varepsilon_i\in\{-1,1\}\). Hence all inequalities
\[
\sum_{i\in J}\varepsilon_i x_i\le B_{|J|}\quad(\varnothing\ne J\subseteq[n],\ \varepsilon\in\{-1,1\}^J) \tag{2}
\]
are valid. They define **exactly** \(H_{n,k}\): for an arbitrary \(u\), sort its coordinate magnitudes and express \(u\) as a nonnegative sum of the signed indicator vectors of the successive upper-level coordinate sets. Multiplying the corresponding inequalities in (2) by the successive magnitude gaps gives the right side of (1), the exact support value. Equality of support functions proves the halfspace representation.

**2. A discrete square-root-ratio lemma.** For any nonnegative, weakly decreasing, log-concave sequence \(A_0,A_1,\ldots,A_{m-1}\) with no internal zeros and \(A_0>0\), put \(S_j=\sum_{\ell<j}A_\ell\). Then \(S_j/\sqrt j\), for \(1\le j\le m\), first weakly increases and then weakly decreases. To prove this, write \(T_j=jA_j/S_j\) for \(1\le j<m\), setting \(T_j=0\) when \(A_j=0\). We claim that \(T_j\) is nonincreasing. If \(A_{j+1}=qA_j\) with \(0<q\le1\), log-concavity gives \(A_{j-r}/A_j\le q^{-r}\) for \(1\le r\le j\). Thus
\[
\frac{S_j}{A_j}\le\sum_{r=1}^{j}q^{-r}.
\]
The condition \(T_{j+1}\le T_j\) is equivalent to
\[
((j+1)q-j)S_j\le jA_j.
\]
When the coefficient on the left is nonpositive this is immediate. Otherwise the geometric-sum estimate implies it by the Bernoulli inequality \(q^{j+1}\ge (j+1)q-j\). The zero cases follow directly, and so \(T_j\) is nonincreasing. Finally,
\[
\frac{S_{j+1}}{\sqrt{j+1}}\ge\frac{S_j}{\sqrt j}
\quad\Longleftrightarrow\quad
T_j\ge\frac1{1+\sqrt{1+1/j}}.
\]
The right side increases strictly with \(j\), whereas \(T_j\) does not increase. Hence there is at most one change from increasing to decreasing; the minimum of \(S_j/\sqrt j\) occurs at one or both endpoints.

For the present binomial sequence, \(A_j=\binom{n-j-1}{k-1}\), its successive positive quotients are \((n-j-k)/(n-j-1)\), which are weakly decreasing; thus the lemma applies. In addition, all *interior* indices have strictly larger ratio than the smaller endpoint. Indeed \(A_{n-1}=0\), so the final step is strictly decreasing; and if \(n\ge k^2\), then the first step is strictly increasing, since \(A_1/A_0=(n-k)/(n-1)\ge k/(k+1)>\sqrt2-1\) for \(k\ge3\). If \(n<k^2\), the final endpoint is strictly smaller than the initial one. The one-peak property and these strict endpoint comparisons exclude all interior minimizers in each case.

**3. Radius and sharp phase.** A radius-\(r\) Euclidean ball centered at zero satisfies every inequality in (2) precisely when \(r\sqrt j\le B_j\) for every \(j\). The lemma therefore yields
\[
\min_{1\le j\le n}\frac{B_j}{\sqrt j}
=\min\left\{B_1,\frac{B_n}{\sqrt n}\right\}
=\binom{n-1}{k-1}\min\left\{1,\frac{\sqrt n}{k}\right\}. \tag{3}
\]
The two candidate supporting distances coincide exactly when \(n=k^2\). Central symmetry of \(H_{n,k}\) shows that any contained ball may be reflected about the origin, and their midpoint ball of equal radius is centered at zero; hence (3) is the global inradius. The positive/negative active endpoint normals span \(\mathbb R^n\), so a radius-maximizing ball centered at \(c\) would need \(\langle u,c\rangle\le0\) and \(\langle-u,c\rangle\le0\) for all active pairs \(\pm u\), forcing \(c=0\). The maximal ball is unique.

**4. All touching facets.** By the strict interior-index statement in Step 2, only constraints with \(j=n\) and/or \(j=1\) can touch the centered ball. Every all-sign normal is genuinely facet-defining: the exposed face of each summand is the simplex on \(\{\varepsilon_i e_i:i\in I\}\), and differences between its vertices span the \((n-1)\)-dimensional sign-orthogonal hyperplane (every coordinate pair lies in some \(k\)-subset). Every coordinate normal is facet-defining whenever it can be active, because in the range \(n\ge k^2\) there are enough \(k\)-subsets not containing the designated coordinate, and the corresponding exposed summands span its \((n-1)\)-dimensional orthogonal hyperplane. Thus the active supporting inequalities are distinct facets, giving the claimed counts: \(2^n\), \(2^n+2n\), or \(2n\). No other supporting hyperplane can touch the inball: every boundary point of a polytope must lie on a face defined by an active halfspace from (2), and all the other halfspaces lie strictly farther than the inradius from the origin. This completes the proof.

## Verification

The self-contained program `checks/verify.py` performs three families of *finite corroborating checks*: direct Minkowski support sums against ordered-coordinate support and halfspace decompositions for \(3\le k\le n\le8\), exact-integer inequalities for all \(3\le k\le n\le150\), and exact endpoint phase comparisons across the same finite range. A recorded run passed **5,040 support comparisons, 1,113,626 squared-distance inequalities, and 11,026 endpoint classifications**. Run with `python3 checks/verify.py` in a standard Python 3 environment. Infinite-dimensional-range correctness rests on the proof above, not on those finite computations.

## Relationship to prior work

Wang, Hou, Thawinrak, Liu and Dai (2026) introduce and study \(Q_G\), general sums of coordinate cross-polytopes, emphasizing lattice-point enumeration, volumes and Ehrhart positivity. The present complete \(k\)-uniform special family lies in that framework. Their Proposition 3.5 already gives a general halfspace description of \(Q_G\); the present halfspaces specialize that earlier result. The new claim is the sharp simplification of the ensuing Euclidean distance minimum, the square-law transition, uniqueness and exact tangent facet orbit counts. Eur, Fink, Larson and Spink (2024) develop the broader signed-permutohedron/type-B generalized-permutohedron framework, including face and lattice perspectives; a type-B halfspace description alone does not give the sharp endpoint-minimizer comparison or transition classification. Previous results about vertex-transitive zonotopes give exact radii for that narrower class; they do not imply the stated \(k\ge3\) family (which already contains the non-zonotopal \(n=k\) cross-polytope). No equivalent published complete-uniform-hypergraph insphere theorem was located in the checked sources. Priority remains subject to broader literature review.

## Limitations

The result holds only for the full, equally weighted \(k\)-uniform collection, \(n\ge k\ge3\), and Euclidean inspheres. It does not give a facet enumeration of the whole polytope, formulas for nonuniform weights, nor an analogous phase law for other norms. The halfspace inequalities used in the proof are a complete description but can be redundant. The finite verifier cannot prove the full theorem. The novelty assessment is evidence-limited and is not independent mathematical validation.

## References

1. H. Wang, Q. Hou, W. Thawinrak, Z. Liu, and Z. Dai, *Counting Lattice Points in Minkowski Sums of Cross Polytopes*, arXiv:2608.16037 (first posted 2026-08-17), https://arxiv.org/abs/2608.16037 .
2. C. Eur, A. Fink, M. Larson, and H. Spink, *Signed permutohedra, delta-matroids, and beyond*, arXiv:2209.06752 (first posted 2022-09-14), https://arxiv.org/abs/2209.06752 .
3. *Exact Euclidean radii and tangent facets of vertex-transitive zonotopes*, online mathematical research finding, 2026-10-11; relevant to the comparison with the zonotope class, not to the complete \(k\)-uniform case with \(k\ge3\).
