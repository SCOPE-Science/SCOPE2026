# Exact pointwise Daugavet–Delta profile in scalar–Daugavet \(\ell_p\)-sums

## Finding

Let \(Y\) be a real Banach space and let \(x\in S_Y\) be a **Daugavet point**. Fix \(1<p<\infty\), and equip
\[
Z=\mathbb R\oplus_pY,
\qquad
\|(s,y)\|_Z=(|s|^p+\|y\|_Y^p)^{1/p}
\]
with its usual norm. For \(-1\le t\le1\), set
\[
a=|t|,\qquad b=(1-a^p)^{1/p},\qquad z=(t,bx)\in S_Z.
\]
The Choi–Jung pointwise Daugavet and Delta constants obey the **simultaneous sharp identities**
\[
\boxed{\operatorname{dc}_Z(z)=\big((1-a)^p+b^p\big)^{1/p},
\qquad
\delta c_Z(z)=2b.}
\tag{1}
\]
For every \(0\le a<1\),
\[
\operatorname{dc}_Z(z)<\delta c_Z(z),
\tag{2}
\]
whereas both constants vanish at \(a=1\). When \(Y\) has the Daugavet property, (1) is the **complete unit-sphere profile** of both constants on \(Z\); consequently, its Delta points are exactly
\[
\{0\}\times S_Y,
\]
and it has no Daugavet points.

## Assumptions and scope

All scalar fields are real. A slice of a closed unit ball is
\[
S(B_E,f,\eta)=\{w\in B_E:f(w)>1-\eta\},
\qquad f\in S_{E^*},\ \eta>0.
\]
The pointwise constants are equivalently defined by
\[
\operatorname{dc}_E(z)=\inf_{S\text{ a slice of }B_E}\sup_{w\in S}\|z-w\|,
\tag{3}
\]
\[
\delta c_E(z)=\inf_{\substack{S\text{ a slice of }B_E\\z\in S}}\sup_{w\in S}\|z-w\|.
\tag{4}
\]
These are the exact slice-infimum formulations of Choi and Jung (2023, Definition 2.1). A **Daugavet point** \(x\in S_Y\) means that every slice \(T\) of \(B_Y\) contains elements \(w\) at distance arbitrarily close to \(2\) from \(x\). This is a condition on the selected point, not necessarily on the entire space \(Y\).

The scalar reflection \((s,y)\mapsto(-s,y)\) is an isometry. We may therefore prove all identities with \(t=a\ge0\). The endpoints \(a=0\) and \(a=1\) are included.

## Proof

Write \(b=(1-a^p)^{1/p}\) and \(z=(a,bx)\).

**1. Lower bound for the Daugavet constant.** Fix a slice
\[
S=\{(u,v)\in B_Z:\lambda u+\varphi(v)>1-\eta\},
\]
where \((\lambda,\varphi)\in S_{Z^*}\) and \(\eta>0\). Choose an extremal pair of scalar lengths \(u_0\in\mathbb R\), \(r\ge0\), such that
\[
|u_0|^p+r^p=1,
\qquad
\lambda u_0+r\|\varphi\|=1.
\tag{5}
\]
Such a pair exists by equality in the two-dimensional Hölder inequality; if \(\varphi=0\) one can take \(r=0\).

If \(r>0\) and \(\varphi\ne0\), the Daugavet-point property supplies, for every sufficiently small \(\varepsilon>0\), a \(w\in B_Y\) with
\[
\varphi(w)>\|\varphi\|-\varepsilon,
\qquad
\|x-w\|>2-\varepsilon.
\tag{6}
\]
Then \((u_0,rw)\in S\) for sufficiently small \(\varepsilon\). Furthermore, using
\[
\|bx-rw\|\ge(b+r)\|x-w\|-b-r,
\tag{7}
\]
we may make its second-coordinate distance arbitrarily close to \(b+r\). When \(r=0\), the same reasoning is immediate without choosing \(w\).

For any such \((u_0,r)\),
\[
\begin{aligned}
|a-u_0|^p+(b+r)^p
&\ge |a-u_0|^p+b^p+r^p\\
&\ge (1-a)^p+b^p.
\end{aligned}
\tag{8}
\]
The first inequality uses \((b+r)^p\ge b^p+r^p\); the second is the reverse triangle inequality in \(\ell_p^2\), since \(\|(u_0,r)\|_p=1\) and \(\|(a,0)\|_p=a\). Thus every slice \(S\) has distance supremum at least
\[
D=\big((1-a)^p+b^p\big)^{1/p},
\]
so \(\operatorname{dc}_Z(z)\ge D\).

**2. Upper bound for the Daugavet constant.** For \(0<\eta<1\), consider the scalar-coordinate slice
\[
S_\eta=\{(u,v)\in B_Z:u>1-\eta\}.
\]
Every element satisfies \(\|v\|\le(1-u^p)^{1/p}\), whence
\[
\|z-(u,v)\|^p
\le |a-u|^p+\bigl(b+(1-u^p)^{1/p}\bigr)^p.
\]
As \(\eta\downarrow0\), the supremum on the right converges to \((1-a)^p+b^p\), proving \(\operatorname{dc}_Z(z)\le D\). This gives the first identity of (1).

**3. Lower bound for the Delta constant.** Suppose \(b>0\). Let \(S\) be any slice containing \(z\), defined by \((\lambda,\varphi)\) as above. Since
\[
\lambda a+b\varphi(x)>1-\eta,
\]
there is a positive margin \(\kappa\) such that every \(w\in B_Y\) with \(\varphi(w)>\varphi(x)-\kappa\) yields \((a,bw)\in S\). If \(\varphi\ne0\), such \(w\) can be chosen with \(\|x-w\|\) arbitrarily close to \(2\), by applying the Daugavet-point property to this nonempty slice of \(B_Y\); if \(\varphi=0\), take \(w=-x\). Hence
\[
\sup_{y\in S}\|z-y\|\ge\sup\,b\|x-w\|=2b,
\]
and \(\delta c_Z(z)\ge2b\). If \(b=0\), the lower bound is trivial.

**4. Upper bound for the Delta constant.** If \(a=0\), the universal estimate \(\delta c_Z(z)\le2=2b\) suffices. If \(a=1\), the slices \(S_\eta\) from step 2 contain \(z=(1,0)\) and have distance supremum tending to zero. Now assume \(0<a<1\). For any small \(\eta\in(0,a)\), the slice
\[
T_\eta=\{(u,v)\in B_Z:u>a-\eta\}
\]
contains \(z\). Define \(h(u)=(1-u^p)^{1/p}\), for \(u\in[0,1]\). For every \((u,v)\in T_\eta\),
\[
\|z-(u,v)\|^p
\le |u-a|^p+(b+h(u))^p.
\tag{9}
\]
For \(u\in[a,1]\), the right side is nonincreasing: at \(a<u<1\), its derivative divided by \(p\) is
\[
(u-a)^{p-1}
-\left(\frac{u(b+h(u))}{h(u)}\right)^{p-1}
\le0,
\tag{10}
\]
since \(u-a\le u\le u(b+h(u))/h(u)\). Its maximum there is therefore \((2b)^p\), reached at \(u=a\). On \([a-\eta,a]\), the right-hand side of (9) tends uniformly to \((2b)^p\) as \(\eta\downarrow0\) by continuity. Thus \(\delta c_Z(z)\le2b\), proving the second identity of (1).

**5. Strict gap and the qualitative loci.** For \(0<a<1\),
\[
(1-a)^p<1-a^p=b^p,
\]
so
\[
\operatorname{dc}_Z(z)^p<(2b^p)<(2b)^p,
\]
where the final inequality uses \(p>1\). For \(a=0\), (1) reads \(\operatorname{dc}=2^{1/p}<2=\delta c\). At \(a=1\), both are zero. If every point of \(S_Y\) is a Daugavet point, apply the theorem to every unit \((t,y)\in S_Z\), writing \(y=bx\) when \(y\ne0\). From (1), the Delta constant equals \(2\) exactly when \(a=0\), and the Daugavet constant is everywhere strictly below \(2\). This completes the proof.

## Verification

The bundled `verify.py` checks exact rational instances of the two scalar inequalities (8), verifies superadditivity for integer exponents, and stress-tests the monotonic envelope (9)--(10) on a grid of eight real exponents. It also checks the strict quantitative gap and both endpoint regimes. Re-run with `python verify.py` using Python 3, standard library only.

The checker is a supplementary finite test. The global identities for all \(1<p<\infty\), all real Banach spaces carrying a Daugavet point, and every admissible scalar parameter follow from the slice argument and analytic inequalities above, **not** from discretized sampling.

## Relationship to prior work

Haller, Pirk and Veeorg (2020/2021) study the **qualitative** existence and inheritance of Daugavet and Delta points in arbitrary absolute sums; their Theorem 4.1 gives a qualitative obstruction to Delta points with a nonzero scalar component. Choi and Jung (2023) introduce the pointwise constants in (3)--(4), prove general estimates, and establish some \(\ell_1\)- and \(\ell_\infty\)-sum stability bounds. The inspected sections do not give the simultaneous exact profile (1) for a scalar–Daugavet mixed \(\ell_p\)-sum.

The closest separately indexed calculation treats the **scalar axis** \((t,0)\) in the unit ball of \(\mathbb R\oplus_pY\), obtaining \(\operatorname{dc}=1-|t|\) and \(\delta c=(1-|t|^p)^{1/p}\). The present unit-sphere point \((t,bx)\) with \(b>0\) is outside that axis: its Delta constant is exactly **twice** the axis value at the same scalar coordinate. Other nearby records calculate Daugavet constants of \(\ell_p\)-sums in which **every** component has the Daugavet property, or treat \(\ell_1\)-direct sums. Neither covers a finite-dimensional scalar summand together with a Daugavet point for \(1<p<\infty\).

## Limitations

The theorem requires a Daugavet point in \(Y\) and treats the real scalar summand for \(1<p<\infty\). It does not claim these formulas for arbitrary base points of spaces lacking that property, for multiple independent atomic coordinates, or for the endpoints \(p=1,\infty\). The classification of all Delta points is asserted only when the **whole** space \(Y\) has the Daugavet property.

The slice proofs are intrinsic and do not require separability or reflexivity. Literature search cannot prove absolute novelty; an equivalent formula under another normalization of pointwise slice thickness remains a residual bibliographic possibility.

## References

1. R. Haller, K. Pirk and T. Veeorg, *Daugavet- and Delta-points in absolute sums of Banach spaces*, arXiv:2001.06197v1 (17 January 2020); *Journal of Convex Analysis* **28** (2021), 41–54. MSC 46B20, 46B04.
2. G. Choi and M. Jung, *The Daugavet and Delta-constants of points in Banach spaces*, arXiv:2307.10647v1 (20 July 2023), Definition 2.1 and §4; *Proceedings of the Royal Society of Edinburgh, Section A*, doi:10.1017/prm.2024.83.
