# The Nakamura--Shibata counterexamples have a singular line but only one non-Gorenstein point
## Finding
For every integer \(m\ge2\), consider the threefold of Nakamura and Shibata
\[
X_m=(Y\times\mathbf A^1)/G,
\]
where \(Y\) is the affine cone over an elliptic curve polarized by a degree-\(m\) line bundle, \(0_Y\) is the cone vertex, \(G\simeq\mathbf Z/m\mathbf Z\) acts through an order-\(m\) torsion translation on the elliptic curve, and a generator acts on the affine-line coordinate by \(t\mapsto\xi t\) for a primitive \(m\)-th root of unity \(\xi\).

Let
\[
\Sigma_m:=q(\{0_Y\}\times\mathbf A^1)\subset X_m,
\]
where \(q:Y\times\mathbf A^1\to X_m\) is the quotient map. Then
\[
\boxed{\Sigma_m\simeq\mathbf A^1,\qquad
\operatorname{Sing}(X_m)=\operatorname{Nklt}(X_m)=\Sigma_m.}
\]
Moreover, for every closed point \(x\in X_m\),
\[
\operatorname{mld}_x(X_m)=
\begin{cases}
1,&x\in\Sigma_m,\\
3,&x\notin\Sigma_m,
\end{cases}
\]
and the local Cartier index of \(K_{X_m}\) is
\[
\operatorname{ind}_x(K_{X_m})=
\begin{cases}
m,&x=0,\\
1,&x\ne0.
\end{cases}
\]
Thus the canonical index has an arbitrarily large isolated jump at one point of a single irreducible non-klt singular stratum, even though the closed-point minimal log discrepancy is constant along that entire stratum.

## Assumptions and scope
The ground field is algebraically closed of characteristic zero, as in Nakamura--Shibata. The integer satisfies \(m\ge2\). The elliptic curve is denoted \(C\), the polarization \(L\) has degree \(m\), and
\[
Y=\operatorname{Spec}\bigoplus_{n\ge0}H^0(C,L^{\otimes n}).
\]
The source proves that \(Y\) is normal and Gorenstein, that its natural resolution \(\widetilde Y\to Y\) is an isomorphism away from \(0_Y\), and that \(\operatorname{mld}_{0_Y}(Y)=0\). It also proves that the induced \(G\)-action on \(\widetilde Y\) is free, that the diagonal action on \(Y\times\mathbf A^1\) is virtually free, and that at the distinguished origin of \(X_m\),
\[
\operatorname{mld}_0(X_m)=1,
\qquad
\operatorname{ind}_0(K_{X_m})=m.
\]

The finding concerns the pointwise singularity, non-klt, minimal-log-discrepancy, and canonical-index stratification of this same affine threefold. It does not assert a boundedness statement for other classes of singularities.

## Proof
First determine the stabilizers of the diagonal action on \(Y\times\mathbf A^1\). Nakamura--Shibata construct a \(G\)-equivariant resolution
\[
p:\widetilde Y\longrightarrow Y
\]
that is an isomorphism over \(Y\setminus\{0_Y\}\), and the action of \(G\) on \(\widetilde Y\) is free. Hence no nonidentity element of \(G\) can fix a point of \(Y\setminus\{0_Y\}\): otherwise its unique lift under \(p\) would be fixed in \(\widetilde Y\).

At a point \((0_Y,t)\), the first coordinate is fixed, but a nonidentity element represented by \(k\) sends the second coordinate to \(\xi^k t\). If \(t\ne0\), equality \(\xi^k t=t\) forces \(\xi^k=1\), hence \(k=0\) in \(G\). Therefore the diagonal action is free on
\[
(Y\times\mathbf A^1)\setminus\{(0_Y,0)\}.
\]
For a finite group in characteristic zero, the quotient map is étale on the free locus. Consequently
\[
q:(Y\times\mathbf A^1)\setminus\{(0_Y,0)\}
\longrightarrow X_m\setminus\{0\}
\]
is étale.

The singular locus of \(Y\) is exactly \(\{0_Y\}\): the resolution is an isomorphism away from the vertex, while \(\operatorname{mld}_{0_Y}(Y)=0\) shows that the vertex is not smooth. Hence
\[
\operatorname{Sing}(Y\times\mathbf A^1)=\{0_Y\}\times\mathbf A^1.
\]
Regularity is étale-local. Thus every nonzero point of the image of this line is singular, every point outside its image is smooth, and the distinguished origin is singular because its canonical index is \(m>1\). Therefore
\[
\operatorname{Sing}(X_m)=\Sigma_m.
\]

The line \(\{0_Y\}\times\mathbf A^1\) is \(G\)-stable and its coordinate ring is \(k[t]\), with the generator acting by \(t\mapsto\xi t\). Since invariants are exact for finite groups in characteristic zero, its quotient embeds as the image stratum and has coordinate ring
\[
k[t]^G=k[t^m].
\]
Hence \(\Sigma_m\simeq\mathbf A^1\).

For minimal log discrepancies, Nakamura--Shibata prove that virtually free finite quotients preserve the closed-point minimal log discrepancy, and they prove that the present diagonal action is virtually free. Let \(x\in\Sigma_m\) and choose a point \((0_Y,t)\) above it. Then
\[
\operatorname{mld}_x(X_m)
=
\operatorname{mld}_{(0_Y,t)}(Y\times\mathbf A^1)
=
\operatorname{mld}_{0_Y}(Y)+\operatorname{mld}_{t}(\mathbf A^1)
=0+1=1.
\]
If \(x\notin\Sigma_m\), then \(x\) is a smooth closed point of the threefold, so \(\operatorname{mld}_x(X_m)=3\).

The same local description identifies the non-klt locus. Away from \(\Sigma_m\) the variety is smooth, hence klt. Along \(\Sigma_m\setminus\{0\}\), the quotient is étale-locally the product of the log-canonical non-klt cone vertex with a smooth curve, so it is not klt. At the origin, Nakamura--Shibata explicitly prove that the germ is log canonical but not klt. Hence
\[
\operatorname{Nklt}(X_m)=\Sigma_m.
\]

Finally, \(Y\times\mathbf A^1\) is Gorenstein. Since the quotient map is étale over \(X_m\setminus\{0\}\), Gorensteinness descends there; equivalently, \(K_{X_m}\) is Cartier at every point other than \(0\). Nakamura--Shibata prove that its Cartier index at \(0\) is exactly \(m\). This gives the stated index function.

## Verification
The initiating paper was inspected in full text at Example 3.1, Theorem 3.2, and its proof. In particular, the following source premises were checked directly:

- \(Y\) is normal and Gorenstein.
- \(\widetilde Y\to Y\) is an isomorphism away from \(0_Y\), with \(\widetilde Y\) smooth and exceptional divisor an elliptic curve.
- \(\operatorname{mld}_{0_Y}(Y)=0\).
- the action of \(G\) on \(\widetilde Y\) is free;
- the diagonal action on \(Y\times\mathbf A^1\) is virtually free;
- virtually free quotients preserve the closed-point minimal log discrepancy;
- \(\operatorname{mld}_0(X_m)=1\);
- the Cartier index of \(K_{X_m}\) at \(0\) is exactly \(m\);
- the origin is log canonical but not klt.

The companion paper on virtually free actions was inspected at its definition and equivalent characterizations of virtual freeness, its minimal-log-discrepancy preservation proposition, and its localized formulation. Those results concern the quotient mechanism but do not state the pointwise singular/Gorenstein stratification of the later family \(X_m\).

No finite experiment is used. The only additional ingredients are stabilizer calculation, étale locality of regularity and Gorensteinness, exactness of finite-group invariants in characteristic zero, and the standard product formula for minimal log discrepancies with a smooth affine-line factor.

## Relationship to prior work
Nakamura--Shibata's main theorem isolates the distinguished closed point \(0\in X_m\) and proves two facts there: its closed-point minimal log discrepancy is \(1\), and the Cartier index of its canonical divisor is exactly \(m\). Their proof develops the virtually free quotient mechanism needed for these facts.

The present statement instead determines the whole pointwise stratification of the same threefold. It shows that the singular and non-klt loci are the entire affine line \(\Sigma_m\), that the closed-point minimal log discrepancy is constantly \(1\) along that line, and that the large canonical index occurs only at one point while all neighboring singular points are already Gorenstein. The initiating paper does not state this global stratification.

The authors' earlier work on virtually free actions develops the general quotient theory and localized virtual-freeness criteria. It does not contain the later elliptic-cone family \(X_m\) with arbitrary canonical index. Targeted searches for the source identifier together with “singular locus”, “Gorenstein locus”, “punctured”, “Cartier index”, and the equivalent formulation “constant minimal log discrepancy along a singular curve” did not locate a published statement implying this stratification.

## Limitations
The result is specific to the Nakamura--Shibata family and to closed-point minimal log discrepancies. The equality \(\operatorname{mld}_x(X_m)=1\) along \(\Sigma_m\) does not mean the germ is klt: the non-klt behavior comes from divisors whose centers have positive dimension, which is precisely why the source's example lies outside the klt setting.

No assertion is made that canonical index is semicontinuous in arbitrary families or strata. The statement only computes the index function on this explicit affine threefold.

## References
Y. Nakamura and K. Shibata, “A non-klt counterexample to Shokurov's index conjecture,” arXiv:2608.28038v1, first public 2026-08-28; especially Example 3.1, Theorem 3.2, and its proof.

Y. Nakamura and K. Shibata, “A characterization of virtually free actions via arc spaces and its application to the lower semi-continuity conjecture,” arXiv:2606.24592v1, first public 2026-06-23; especially the definition and characterization of virtually free actions and the minimal-log-discrepancy preservation statement.

Y. Nakamura and K. Shibata, “A counterexample to the PIA conjecture for minimal log discrepancies,” arXiv:2404.06164, first public 2024-04-09; later published in Duke Mathematical Journal 175 (2026), no. 10, 1715--1736.
