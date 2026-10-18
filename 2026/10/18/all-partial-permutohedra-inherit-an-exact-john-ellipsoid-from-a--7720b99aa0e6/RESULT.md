# All partial permutohedra inherit an exact John ellipsoid from a simplex or a capped cube

## Finding

For integers \(m\ge2\) and \(n\ge1\), let the **standard partial permutohedron** be
\[
\mathcal P(m,n)=\operatorname{conv}\{x\in\{0,1,\ldots,n\}^{m}:\text{nonzero coordinate values of }x\text{ are pairwise distinct}\}.
\]
Write \(\mathbf1\in\mathbb R^m\) for the all-one vector, \(H=\mathbf1\mathbf1^{\mathsf T}/m\), and \(B=\sum_{j=0}^{\min(m,n)-1}(n-j)\). The unique maximum-volume inscribed Euclidean ellipsoid is
\[
E_{m,n}=\{x:(x-t\mathbf1)^{\mathsf T}Q^{-1}(x-t\mathbf1)\le1\},
\qquad Q=(q-h)I+h\mathbf1\mathbf1^{\mathsf T},
\]
with the following exact center coordinate, diagonal covariance, and off-diagonal covariance:
\[
\boxed{(t,q,h)=\begin{cases}
\left(\dfrac{n(n+1)}{2(m+1)},\dfrac{n^2(n+1)^2}{4(m+1)^2},-\dfrac{n^2(n+1)^2}{4m(m+1)^2}\right),&m\ge n,\\[6pt]
\left(\dfrac n2,\dfrac{n^2}4,\dfrac{(n-m)^2-m}4\right),&m\le n\le m+\sqrt m,\\[6pt]
\left(\dfrac n2,\dfrac{n^2}4,0\right),&n\ge m+\sqrt m.
\end{cases}}
\]
The expressions agree at their shared boundaries; hence each integer parameter pair determines exactly one ellipsoid. Its two squared principal semiaxes are \(a=q-h\), repeated \(m-1\) times, and \(\ell=q+(m-1)h\), repeated once. Both are positive. The Euclidean volume is exactly \(\kappa_m a^{(m-1)/2}\ell^{1/2}\), where \(\kappa_m=\pi^{m/2}/\Gamma(m/2+1)\).

**Complete contact law.** All \(m\) lower coordinate facets \(x_i=0\) always touch. The \(m\) upper coordinate facets \(x_i=n\) touch if and only if \(n\ge m\). The total-sum facet \(\sum_i x_i=B\) touches if and only if \(n\le m+\sqrt m\). Every genuine upper facet indexed by a proper subset of cardinality between \(2\) and \(m-1\) is **strictly separated** from the ellipsoid. Thus the exact numbers of tangent facets are \(m+1\) for \(m>n\), \(2m+1\) for \(m\le n\le m+\sqrt m\), and \(2m\) for \(n>m+\sqrt m\). At an integer transition \(n=m+\sqrt m\), which occurs only when \(m\) is a perfect square, the John ellipsoid is already round but still touches the total-sum facet.

Equivalently, the original polytope has the **same John ellipsoid** as the simplex \(\{x\ge0:\sum_i x_i\le B\}\) when \(m\ge n\), and as the capped cube \(\{0\le x_i\le n:\sum_i x_i\le B\}\) when \(n\ge m\). The less obvious assertion is that **all omitted subset inequalities remain satisfied by those ellipsoids**, including in the anisotropic transition regime.

## Assumptions and scope

The ambient geometry is the coordinate Euclidean space \(\mathbb R^m\); the ellipsoid matrix \(Q\) contains squared semiaxes, not inverse semiaxes. All vertices and facets are those of the standard partial permutohedron, not of an arbitrary affine realization. The full facet system from the primary literature consists of the lower coordinate facets and subset-sum facets \(\sum_{i\in S}x_i\le f_k\) for \(k=|S|\) in the genuine facet index range \(1\le k\le n-1\), plus the full-set facet. Here
\[
f_k=\sum_{j=0}^{\min(k,n)-1}(n-j)
\]
for every cardinality \(k\), including redundant inequalities; when \(n\ge m\), all proper cardinalities \(1\le k<m\) are genuine. The total-sum facet is always genuine; upper singleton facets are genuine when \(n\ge2\), but touch the asserted ellipsoid only in the range \(n\ge m\). The proof checks even redundant cardinality inequalities where useful.

## Proof

**1. Euclidean support of an exchangeable ellipsoid.** Let \(E(t,q,h)\) be the displayed ellipsoid, with \(q-h>0\) and \(q+(m-1)h>0\). Its upper support in the direction of a \(k\)-element set indicator is exactly
\[
\max_{x\in E}\sum_{i\in S}x_i=kt+\sqrt{kq+k(k-1)h}.
\tag{1}
\]
The lower support for the coordinate \(i\) equals \(t-\sqrt q\). Thus verifying (1) against the complete subset facet system, plus nonnegativity, proves ellipsoid containment in \(\mathcal P(m,n)\).

**2. The simplex-controlled range \(m\ge n\): containment of the simplex John ellipsoid.** Put \(B=n(n+1)/2\) and \(t=B/(m+1)\), \(q=t^2\), \(h=-q/m\). The eigenvalues are \(a=q(m+1)/m\) and \(\ell=q/m\), hence positive. The lower supports equal zero, and the upper support of the total sum is \(mt+\sqrt{m\ell}=B\).

For any proper subset cardinality \(1\le k\le n-1\), (1) becomes
\[
 kt+t\sqrt{\frac{k(m-k+1)}m}.
\]
Since \(v=k(m-k+1)/m\ge1\), its square root is at most \(v\), and therefore this support does not exceed
\[
\frac{n(n+1)}{2(m+1)}\,\frac{k(2m-k+1)}m.
\tag{2}
\]
For fixed \(k\ge1\), the function \(g_k(z)=(2z-k+1)/(z(z+1))\) is strictly decreasing on \(z\ge k\), as follows by differentiation or factoring the difference quotient. Because \(m\ge n\ge k+1\), (2) is at most \(k(2n-k+1)/2=f_k\). The inequality is strict if \(k\ge2\) (since \(v>1\)) or if \(m>n\) (since \(g_k(m)<g_k(n)\)); the only possible proper upper equality is \(k=1,m=n\). Thus the simplex ellipsoid belongs to \(\mathcal P(m,n)\) and has precisely the claimed contacts.

To establish global John optimality, consider the containing simplex \(S_B=\{x\ge0:\sum x_i\le B\}\). The proposed ellipsoid has contact directions, after its shape-normalization to the unit ball, \(u_i=-Q^{1/2}e_i/t\) for the \(m\) lower facets, and \(v=\mathbf1/\sqrt m\) for the total-sum facet. Give each of these \(m+1\) contact directions weight \(w=m/(m+1)\). Their weighted vector sum is zero. Their weighted matrix sum is
\[
 w\left(\frac Qq+vv^{\mathsf T}\right)=I,
\]
whose transverse and axial eigenvalues both equal one. These are the two John contact identities, with positive weights, so the ellipsoid is the unique John ellipsoid of \(S_B\). Since it lies in the smaller polytope \(\mathcal P(m,n)\), its optimality and uniqueness transfer there as well.

**3. The capped-cube-controlled range \(n\ge m\): strict subset screening.** Put \(t=n/2\), \(q=n^2/4\), and
\[
h=\min\left\{0,\frac{(n-m)^2-m}{4}\right\}.
\tag{3}
\]
The transverse eigenvalue \(a=q-h\) is positive, and the axial eigenvalue \(\ell=q+(m-1)h\) is positive: at the most negative allowed value, attained when \(n=m\), it equals \(m/4\); increasing \(n\) can only increase it.

The two coordinate support extremes are precisely zero and \(n\). For \(1\le k\le m\), the upper subset support constraint (1), with \(f_k=k(2n-k+1)/2\), is equivalent (both sides nonnegative) to
\[
h\le T(k):=\frac{(n-k)^2-k}{4}\quad(k\ge2).
\]
More directly, cancelling \(k\) in the **squared inequality** gives the simpler, exactly equivalent identity
\[
\bigl(f_k-kt\bigr)^2-\bigl(kq+k(k-1)h\bigr)
=\frac{k(k-1)}4\left((n-k)^2-k-4h\right),\quad k\ge2.
\tag{4}
\]
The upper singleton inequalities are equalities because \(t+\sqrt q=n\). For \(2\le k\le m\), the threshold \(\bigl((n-k)^2-k\bigr)/4\) is strictly decreasing with \(k\), since consecutive differences are \((k-n)/2<0\) for \(k<m\le n\). By (3), \(h\le\bigl((n-m)^2-m\bigr)/4\), so (4) is nonnegative for every cardinality and strictly positive whenever \(2\le k<m\). The total-set constraint is an equality precisely when \(n\le m+\sqrt m\), including the transition, and is strict above that threshold. Thus the candidate lies in \(\mathcal P(m,n)\) with exactly the stated contacts.

**4. Global maximal-volume certificate in the capped cube.** Normalize by \(Q^{-1/2}\). Let \(u_i=Q^{1/2}e_i/\sqrt q\), so \(\pm u_i\) are the coordinate-facet contact normals, and let \(v=\mathbf1/\sqrt m\) be the total-sum contact normal when \(h<0\). Put
\[
\beta=\frac q{q-h},\qquad \gamma=-\frac{mh}{q-h}\ge0,\qquad
\delta=-\gamma\sqrt{\frac q{m\ell}}.
\]
Give the upper coordinate normal \(u_i\) weight \((\beta+\delta)/2\), the lower coordinate normal \(-u_i\) weight \((\beta-\delta)/2\), and the total-sum normal \(v\) weight \(\gamma\). At \(h=0\), take \(\gamma=\delta=0\), giving the ordinary coordinate contact certificate for a cube. Otherwise the individual weights are nonnegative because
\[
\beta^2-\delta^2
=\frac{q\ell-mh^2}{(q-h)^2\ell}\,q
\ge0,
\quad q\ell-mh^2=(q-h)(q+mh)\ge0
\]
for the range \(-q/m\le h\le0\) realized here. (The square-root formula permits zero upper weights at \(n=m\).) Since \(\sum_i u_i=\sqrt{m\ell/q}\,v\), the weighted first contact moment is
\[
\delta\sum_i u_i+\gamma v=0.
\]
Their weighted second contact moment is
\[
\beta\sum_i u_i u_i^{\mathsf T}+\gamma vv^{\mathsf T}
=\frac{\beta}{q}Q+\gamma vv^{\mathsf T}=I,
\]
as seen by checking the \((m-1)\)-dimensional transverse eigenvalue \(\beta(q-h)/q=1\) and the axial eigenvalue \(\beta\ell/q+\gamma=1\). Hence the exact John identities hold and certify maximal volume **against all ellipsoids**, not merely symmetric alternatives. The ellipsoid is uniquely maximal for its containing capped cube. Since it also lies in \(\mathcal P(m,n)\), it is the unique John ellipsoid of the partial permutohedron. The analogous signed coordinate weights without total support give the round-ball endpoint.

**5. Boundary matching and contact counts.** At \(m=n\), the simplex and capped-cube formulas both give \(t=m/2,q=m^2/4,h=-m/4\). At \(n=m+\sqrt m\), the middle and cube formulas both give \(h=0\). The strict support gaps in steps 2–3 rule out all intermediate subset contacts. The literature's irredundant facet classification converts the remaining supporting-hyperplane equalities into the facet counts stated above.

## Verification

Run `python3 verify.py` after extracting that script from the package. The standalone script uses only exact rational arithmetic from the Python standard library and checks all 9,900 integer profiles with \(2\le m\le100\) and \(1\le n\le100\); it checks 504,900 exact subset cardinalities and 69,394 individual subset masks for smaller dimensions. It recomputes all squared supports, strict inequalities, positivity, contact cardinalities, and both types of John moment certificates. It prints `PASS: 9900 exact parameter profiles; 504900 cardinality comparisons; 69394 individual subsets.` These finite checks do not prove the infinitely many parameter cases; steps 1–5 supply the general argument.

## Relationship to prior work

Heuer and Striker established the partial permutation polytope family and its subset inequalities; Behrend and coauthors gave the complete irredundant partial-permutohedron facet description (Proposition 2.8), with primary MSC2020 \(52B05\). Those sources study face structure and enumerative geometry, not these inscribed ellipsoids. An earlier exact Euclidean **inball** of partial permutohedra gives a different, scalar optimization; likewise previous Löwner **outer** ellipsoid calculations concern the opposite inclusion direction. The published *Three-phase John ellipsoid of a capped hypercube* does compute the John ellipsoid of the **larger capped-cube envelope** used in step 4. Accordingly, the cube's formula, its three phases, and its optimality certificate by themselves are prior material. The specific new assertion here is that every missing genuine subset facet of \(\mathcal P(m,n)\) screens out harmlessly, yielding **the complete same-ellipsoid theorem** for all \(m,n\); steps 2–3 establish that nonautomatic implication. The simplex envelope is similarly familiar, but the proof of its feasibility inside the smaller polytope is specific to the partial-permutohedron rank values.

## Limitations

The theorem concerns the standard Euclidean coordinate realization and not affine-equivalent metrics. Although complete for this two-parameter family, it does not imply an all-polymatroid John-ellipsoid theorem. Existing larger-envelope results are explicitly credited rather than presented as independently new formulas. The examined literature does not exclude an older equivalent result stated using symmetric polymatroids, truncated permutations, or optimal design; bibliographic originality is therefore qualified. No independent mathematical audit has been performed.

## References

1. D. Heuer and J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901v1 (first publicly available 2020-12-17), especially the complete inequality and facet discussion. https://arxiv.org/abs/2012.09901.
2. R. E. Behrend, F. Castillo, A. Chavez, A. Diaz-Lopez, L. Escobar, P. E. Harris and E. Insko, *Partial Permutohedra*, arXiv:2207.14253v1 (first publicly available 2022-07-28), especially Proposition 2.8, primary MSC2020 \(52B05\). https://arxiv.org/abs/2207.14253.
3. *Three-phase John ellipsoid of a capped hypercube*, published mathematical result (2026), full result and proof at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-phase-john-ellipsoid-of-a-capped-hypercube--9b8726b32127.
4. *The redundant-facet regime of partial permutohedra has a simplex-controlled inball*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-redundant-facet-regime-of-partial-permutohedra-has-a-simplex--ebf0d41dcf43.
5. *A sharp Löwner contact-orbit transition for second partial permutohedra*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-l-wner-contact-orbit-transition-for-second-partial-permu--dc2610ed29db.
