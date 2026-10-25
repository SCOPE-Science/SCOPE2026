# Sharp fourth-order Gauss positivity on every positively weighted star

## Finding

Consider a finite star with hub vertex \(0\), \(m\ge 2\) leaves \(1,\ldots,m\), and arbitrary strictly positive conductances \(w_1,\ldots,w_m\). Put \(n=m+1\), \(w_* = \max_i w_i\), and \(L\) equal to the symmetric combinatorial weighted Laplacian. The completed two-stage fourth-order Gauss–Legendre step for \(u'=-Lu\) is
\[
T(h)=(12I-6hL+h^2L^2)(12I+6hL+h^2L^2)^{-1},\qquad h\ge0.
\]
Define \(d(z)=z^2+6z+12\), and for each leaf \(i\) define
\[
\Phi_i(h)=1+\sum_{k=1}^{m}\frac{h^2w_k(w_k-w_i)}{d(hw_k)},\quad
\Phi_*(h)=1-\sum_{k=1}^{m}\frac{h^2w_k(w_*-w_k)}{d(hw_k)}.
\]
The following is an exact all-weight classification:

**Theorem.** For every integer \(m\ge2\), every \(w_i>0\), and every real \(h\ge0\),
\[
T(h)\ge0\ \text{entrywise}\quad\Longleftrightarrow\quad\Phi_*(h)\ge0.
\]
In particular, \(T(h)\) is entrywise nonnegative for every finite \(h\ge0\) **if and only if**
\[
\boxed{\displaystyle w_*\sum_{i=1}^{m}\frac1{w_i}\le m+1.}
\]
If this inequality fails, \(\Phi_*\) is strictly decreasing and has exactly one positive zero \(H\); then
\[
\boxed{\displaystyle T(h)\ge0\ \text{entrywise}\ \Longleftrightarrow\ 0\le h\le H.}
\]
At \(h=H\), exactly the hub-to-leaf entries belonging to maximum-weight spokes vanish; all other off-diagonal entries are positive. For every \(h>H\), these hub-to-leaf entries are negative. Hence positivity never reenters. For all \(h\ge0\), the matrix \(T(h)\) is symmetric, positive definite, and has every row sum and column sum equal to one, even beyond the positivity interval. It is doubly stochastic exactly on the positivity interval.

The scalar threshold equation requires \(O(m)\) arithmetic operations per evaluation, and a unique positive root can be computed by bisection whenever one exists.

## Assumptions and scope

The graph is the simple star with \(m\ge2\) distinct leaves. Edge \(0i\) has a finite strictly positive real conductance \(w_i\); all leaf-to-leaf edge weights are zero. The weighted combinatorial Laplacian is normalized by \(L_{00}=\sum_i w_i\), \(L_{ii}=w_i\), \(L_{0i}=L_{i0}=-w_i\), and all remaining entries zero. The timestep \(h\) is a nonnegative real number. Positivity refers to the completed step acting on arbitrary nonnegative initial vectors; it does not require each internal Gauss stage to preserve positivity. No normalization of the weights or restriction on their ratios is assumed.

At \(h=0\), \(T(0)=I\). The nontrivial entry formulas and strict positivity statements below concern \(h>0\). For a tied maximum weight, all tied hub-to-leaf transitions reach zero simultaneously at a finite cutoff. If no finite cutoff exists, all entries are strictly positive for every finite \(h>0\).

## Proof

**1. Reduction to a complex resolvent.** The scalar stability function for the completed two-stage Gauss method is
\[
R(z)=\frac{z^2-6z+12}{z^2+6z+12}=1-\frac{12z}{z^2+6z+12}.
\]
For \(h>0\), set \(s=(3+i\sqrt3)/h=x+iy\), where \(x=3/h\), \(y=\sqrt3/h>0\). Since \(d(hL)=h^2(L+sI)(L+\bar sI)\), partial fractions yield, for every distinct pair of vertices \(u,v\),
\[
T(h)_{uv}=-\frac{12}{hy}\operatorname{Im}\!\big(s(L+sI)^{-1}_{uv}\big).
\]
The right side is real because \(L\) is real symmetric. This identity follows by subtracting the two conjugate resolvents; no numerical or asymptotic approximation is involved.

**2. Exact star resolvent.** Put
\[
\Omega(s)=1+\sum_{k=1}^{m}\frac{w_k}{s+w_k}.
\]
Schur complementation of the leaf diagonal block of \(L+sI\) gives
\[
(L+sI)^{-1}_{00}=\frac1{s\Omega(s)},\quad
(L+sI)^{-1}_{0i}=\frac{w_i}{s(s+w_i)\Omega(s)},
\]
\[
(L+sI)^{-1}_{ij}=\frac{w_iw_j}{s(s+w_i)(s+w_j)\Omega(s)}\qquad(i\ne j,\ i,j\ge1).
\]
These formulas are valid because \(L\) is positive semidefinite, \(\operatorname{Im}s>0\), and its resolvent exists. Define
\[
F_i(s)=\frac{w_i}{(s+w_i)\Omega(s)},\qquad
F_{ij}(s)=\frac{w_iw_j}{(s+w_i)(s+w_j)\Omega(s)}.
\]
Then the hub-to-leaf and distinct-leaf entries of the step are, respectively, \(-12\operatorname{Im}F_i/(hy)\) and \(-12\operatorname{Im}F_{ij}/(hy)\).

**3. Exact sign of each hub-to-leaf entry.** Define \(Z_i=1/F_i=(s+w_i)\Omega(s)/w_i\). Directly using \((s+w_i)/(s+w_k)=1+(w_i-w_k)/(s+w_k)\), one obtains
\[
\operatorname{Im}Z_i=\frac{y}{w_i}
\left(1+\sum_{k=1}^{m}\frac{w_k(w_k-w_i)}{|s+w_k|^2}\right)=\frac{y}{w_i}\Phi_i(h),
\]
because \(|s+w_k|^2=d(hw_k)/h^2\). As \(\operatorname{Im}F_i=-|F_i|^2\operatorname{Im}Z_i\),
\[
\boxed{\displaystyle T(h)_{0i}=\frac{12|F_i(s)|^2}{hw_i}\Phi_i(h).}
\]
The factor outside \(\Phi_i\) is strictly positive. Moreover, with \(A(h)=1+\sum_k h^2w_k^2/d(hw_k)\) and \(B(h)=\sum_k h^2w_k/d(hw_k)>0\), one has \(\Phi_i=A-w_iB\). Therefore the minimum \(\Phi_i\) occurs exactly at maximum-weight spokes, and all hub-to-leaf entries are nonnegative if and only if \(\Phi_*\ge0\).

**4. Noncritical entries cannot fail first.** The complex number \(s\) has argument \(\pi/6\). Each \(s+w_i\) lies in the open sector \(0<\arg(s+w_i)<\pi/6\), while each \(w_k/(s+w_k)\) lies in \(-\pi/6<\arg<0\). Since this sector is a convex cone, \(\Omega(s)=1+\sum_kw_k/(s+w_k)\) has argument between \(-\pi/6\) and \(0\). Consequently
\[
-\pi/6<\arg Z_i<\pi/6,\qquad\operatorname{Re}Z_i>0.
\]
For distinct leaves \(i\ne j\), the resolvent formulas imply \(1/F_{ij}=((s+w_j)/w_j)Z_i\). Therefore
\[
\operatorname{Im}(1/F_{ij})=
\frac{x+w_j}{w_j}\operatorname{Im}Z_i+
\frac{y}{w_j}\operatorname{Re}Z_i.
\]
Whenever \(\Phi_*\ge0\), every \(\operatorname{Im}Z_i\ge0\), so the expression is strictly positive. Since \(\operatorname{Im}F_{ij}=-|F_{ij}|^2\operatorname{Im}(1/F_{ij})\), every distinct-leaf entry of \(T(h)\) is strictly positive. Meanwhile \(R(z)=((z-3)^2+3)/((z+3)^2+3)>0\) for every \(z\ge0\); spectral calculus makes \(T(h)\) positive definite, hence its diagonal entries strictly positive. Finally, \(L\mathbf1=0\) gives \(T(h)\mathbf1=\mathbf1\), and symmetry gives unit column sums as well. These facts establish the first asserted equivalence, with no assumption that the entries remain nonnegative after a failure.

**5. Sharp classification in the timestep.** For each \(a>0\), the map \(h\mapsto h^2/d(ah)\) has derivative \((6ah^2+24h)/d(ah)^2>0\) for \(h>0\). Thus
\[
\Phi_*(h)=1-\sum_k w_k(w_*-w_k)\frac{h^2}{d(hw_k)}
\]
is nonincreasing; it is strictly decreasing if and only if not all weights are equal. Its endpoint values are
\[
\Phi_*(0)=1,\qquad
\lim_{h\to\infty}\Phi_*(h)=m+1-w_*\sum_k\frac1{w_k}.
\]
If the limit is nonnegative, \(\Phi_*(h)>0\) for every finite \(h>0\) (trivially so in the equal-weight case). If the limit is negative, continuity and strict monotonicity give exactly one positive root, with a positive sign before and a negative sign thereafter. The sign identity in Step 3 identifies all and only the initially vanishing off-diagonal entries, and proves permanent positivity failure after this root. This completes the proof.

**A four-vertex exact boundary.** For \(m=3\) and weights \((2,2,3)\), one has \(w_*\sum_i1/w_i=4=m+1\), so positivity is strict for every finite positive step, despite heterogeneous weights. For \(m=3\) and weights \((2,2,4)\), the scalar factor for the largest spoke is
\[
\Phi_*(h)=\frac{-h^2+3h+3}{h^2+3h+3},
\]
with exact sharp threshold \(H=(3+\sqrt{21})/2\). These examples separate the unconditional boundary from finite-time positivity failure without changing graph topology.

## Verification

The standalone script `verify.py` checks scalar Padé and monotonicity identities, the rational four-vertex examples, and exact rational step matrices for weighted stars with two to six leaves. It independently computes the full rational matrix quotient and compares hub-entry signs against \(\Phi_i\); on selected four-vertex examples it also compares exact complex-resolvent entry formulas. It checks symmetry, mass preservation, strict diagonal positivity and the relevant leaf-to-leaf implications. Run `python verify.py` with the dependency documented in `requirements.txt`. These finite calculations corroborate the separate all-weight analytical proof and do not establish its infinite quantifiers.

## Relationship to prior work

Gottlieb, Shu and Tadmor (2001, Section 6) established foundational restrictions for general implicit SSP methods, which are method-wide and do not classify the completed Gauss step on a fixed weighted star. Gottlieb and Gottlieb (2003, Sections 1–4) analyzed linear-operator SSP Runge–Kutta conditions and CFL bounds but did not derive the present star-specific rational sign criterion. Blanes, Iserles and Macnamara (2022, Sections 1 and 3) studied positivity through graph-Laplacian exponentials and related integrators rather than this two-stage Gauss–Padé quotient.

The known complete-multipartite Gauss classification covers unweighted stars, and a prior three-vertex weighted-network classification covers stars with exactly two spokes. Those statements do not imply the arbitrary-size, arbitrary-conductance condition or its sharp one-root nonreentry law for \(m\ge3\). Published mathematical-record searches for weighted-star Gauss/Padé positivity and for equivalent resolvent formulations yielded no covering theorem, but absence of a search hit does not prove priority.

## Limitations

The theorem concerns symmetric, static positive-weight stars and the **completed** two-stage Gauss step only. It does not characterize positivity of individual implicit stages, nonlinear or time-dependent rates, directed graphs, other graph topologies, or other Padé orders. The classification does not assert method-wide unconditional positivity. The root \(H\), if finite, is given by a one-dimensional monotone rational equation, not necessarily by radicals for arbitrarily many distinct weights. Exact arithmetic tests are finite; the all-weight assertion follows from the displayed resolvent argument. Literature outside the inspected sources may contain equivalent formulations; independent validation has not been carried out.

## References

1. S. Gottlieb, C.-W. Shu and E. Tadmor, “Strong Stability-Preserving High-Order Time Discretization Methods,” *SIAM Review* **43** (2001), 89–112, DOI: 10.1137/S003614450036757X. Electronic publication: 2001-02-02. Author-repository full text: https://drum.lib.umd.edu/bitstreams/faa96f40-0fbb-4af0-84a3-5e3b80c908df/download.
2. S. Gottlieb and L.-A. J. Gottlieb, “Strong Stability Preserving Properties of Runge–Kutta Time Discretization Methods for Linear Constant Coefficient Operators,” *Journal of Scientific Computing* **18** (2003), 83–109, DOI: 10.1023/A:1020338228736. Author-repository full text (within a compiled PDF): https://www.cfm.brown.edu/people/sg/SGmcg1.pdf.
3. S. Blanes, A. Iserles and S. Macnamara, “Positivity-preserving methods for ordinary differential equations,” *ESAIM: M2AN* **56** (2022), 1843–1870, DOI: 10.1051/m2an/2022042. Author full text: https://personales.upv.es/serblaza/2022_M2AN.pdf.
