# A universal John-ellipsoid contact transition for homothetic frusta

## Finding

Let \(d\ge 2\). For **every** convex body \(K\subset\mathbb R^{d-1}\), the John ellipsoid of the frustum joining a copy of \(K\) to a homothetic copy of scale \(q\in[0,1]\) is computable solely from the John ellipsoid of \(K\). It has a sharp, base-shape-independent upper-cap contact transition at \(q=(d-1)/(d+1)\).

Write \(J(K)=c+T B_{d-1}\), where \(B_{d-1}\) is the Euclidean unit ball and \(T\) is any invertible linear map representing this ellipsoid. Define
\[
F_q(K)=\{((1-kz)x,z):x\in K,\ 0\le z\le1\},\qquad k=1-q.
\]
Put
\[
b=\begin{cases}
\dfrac{1}{(d+1)k},&0\le q\le\dfrac{d-1}{d+1},\\[4pt]
\dfrac12,&\dfrac{d-1}{d+1}\le q\le1,
\end{cases}\quad
 a=\sqrt{1-2kb}.
\]
(The first formula is used only when \(k>0\); the formulas agree at the transition.) The **unique** maximum-volume ellipsoid inside \(F_q(K)\) is
\[
\boxed{J(F_q(K))=\left\{\bigl((1-kz)c+Ty,z\bigr):
\frac{\|y\|^2}{a^2}+\frac{(z-b)^2}{b^2}\le1\right\}.}
\]
Its volume equals \(\kappa_d|\det T|a^{d-1}b\), where \(\kappa_d=\pi^{d/2}/\Gamma(1+d/2)\). In particular the normalized shape and the cap contact transition are independent of all asymmetry and nonsmoothness in \(K\).

For \(q<(d-1)/(d+1)\), this ellipsoid does not meet the upper cap \(z=1\). For \(q=(d-1)/(d+1)\) the ellipsoid meets it at one point but that cap is unnecessary in a John certificate. For \(q>(d-1)/(d+1)\) the upper cap has a strictly positive John-certificate weight.

## Assumptions and scope

The base \(K\) is a full-dimensional compact convex body in \(\mathbb R^{d-1}\), with no smoothness, central symmetry, or finite-facet assumption. Dimensions satisfy \(d\ge2\); the frustum ratio satisfies \(0\le q\le1\). The two endpoint bodies are a pyramid/cone over \(K\) and a product prism, respectively. The axial interval is normalized to \([0,1]\); an arbitrary nonzero physical height is obtained by an invertible affine rescaling. The theorem concerns the maximum-volume **inscribed** ellipsoid, not the minimum-volume containing ellipsoid.

## Proof

**1. Normalize the base.** The affine shear and horizontal linear map
\[
\Phi(y,z)=\bigl(Ty+(1-kz)c,z\bigr)
\]
carry the standard frustum \(F_q(K')\) onto \(F_q(K)\), where \(K'=T^{-1}(K-c)\). Affine equivariance of maximal-volume inscribed ellipsoids reduces the problem to \(J(K')=B_m\), with \(m=d-1\). The latter implies \(B_m\subset K'\). By the nonsymmetric John-contact characterization [1,2], there exist boundary points \(u_i\in\partial K'\cap S^{m-1}\) and positive \(\lambda_i\) such that
\[
\sum_i\lambda_i u_i=0,\qquad
\sum_i\lambda_i u_i u_i^{\mathsf T}=I_m,\qquad
\sum_i\lambda_i=m.
\]

**2. Containment of the candidate.** In the normalized coordinates let
\[
E=\{(y,z):\|y\|^2/a^2+(z-b)^2/b^2\le1\}.
\]
Because \(0<b\le1/2\), its heights lie in \([0,1]\). A point on its boundary has \(z=b(1+w)\) and \(y=a\sqrt{1-w^2}\,v\) with \(w\in[-1,1]\), \(\|v\|=1\). Cauchy–Schwarz gives
\[
\|y\|+kz\le kb+
\max_{-1\le w\le1}\{a\sqrt{1-w^2}+kb\,w\}
=kb+\sqrt{a^2+k^2b^2}=1,
\]
since \(a^2=1-2kb\). Thus \(\|y\|\le1-kz\), so \(y\in(1-kz) B_m\subset(1-kz)K'\). The entire ellipsoid \(E\) is contained in \(F_q(K')\).

**3. Lateral contacts.** Normalize \(E\) to the unit \(d\)-ball using \((v,w)\mapsto(av,b+bw)\). Define
\[
t=\frac{kb}{1-kb},\qquad s=\sqrt{1-t^2}=\frac{a}{1-kb}.
\]
For each \(u_i\), the containing halfspace of the normalized frustum is \(u_i\cdot y+kz\le1\). In unit-ball coordinates its unit supporting normal is \(p_i=(s u_i,t)\). Indeed, its transformed affine support has normal \((a u_i,kb)=(1-kb)p_i\) and support value \(1-kb\); hence \(p_i\in\partial B_d\cap\partial E^{-1}(F_q(K'))\). Give this lateral contact weight \(\mu_i=\lambda_i/s^2\).

**4. Axial contacts and exact moment identities.** The lower cap gives \(p_-=(0,-1)\), and the upper cap gives \(p_+=(0,1)\) exactly when \(2b=1\). Set
\[
\mu_- =\frac12\left(1+\frac{mt}{1+t}\right),\qquad
\mu_+ =\frac12\left(1-\frac{mt}{1-t}\right).
\]
The explicit cases for \(b\) yield \(0\le t\le1/d\), with \(t=1/d\) for \(q\le(d-1)/(d+1)\). Thus \(\mu_->0\), \(\mu_+\ge0\); also \(\mu_+=0\) exactly for \(q\le(d-1)/(d+1)\). A zero-weight upper point is omitted, so all retained contact weights are positive and correspond to genuine boundary contacts. The base identities now yield the full nonsymmetric John identities
\[
\sum_i\mu_i p_i+\mu_-p_-+\mu_+p_+=0,
\qquad
\sum_i\mu_i p_ip_i^{\mathsf T}
+\mu_-p_-p_-^{\mathsf T}+\mu_+p_+p_+^{\mathsf T}=I_d.
\]
For verification, the horizontal block is \(s^2\sum_i\mu_i u_i u_i^{\mathsf T}=I_m\), the off-diagonal block vanishes by \(\sum_i\lambda_i u_i=0\), and the vertical identities reduce to
\[
\frac{mt}{s^2}-\mu_-+\mu_+=0,\qquad
\frac{mt^2}{s^2}+\mu_-+\mu_+=1.
\]
All equalities follow by substitution. The nonsymmetric John theorem [1,2] therefore certifies \(E\) as the **unique** maximum-volume ellipsoid of \(F_q(K')\), with no assumption of rotational or discrete symmetry. The affine map \(\Phi\) proves the asserted general formula and volume.

**5. The sharp threshold.** The uppermost height of \(E\) is \(2b\); this is strictly below \(1\) iff \(q<(d-1)/(d+1)\). At equality the cap first contacts; above equality its John multiplier \(\mu_+\) is strictly positive. Since the exact ellipsoid is unique, the threshold is sharp.

## Verification

Run `python verify_homothetic_frusta.py` in an environment with NumPy. The program checks finite-dimensional non-symmetric John moment identities for both regular-simplex and box contact designs in dimensions \(2\) through \(8\), five axial ratios per dimension (including both endpoints and the exact transition), lateral supporting equality, random-point containment, and numerical maximization of the scalar volume objective. It returns \(70\) passing cases ending with `ALL_FRUSTUM_JOHN_CONTACT_AND_OPTIMALITY_DIAGNOSTICS_OK`. These checks are finite diagnostics; the general proof above is analytical and rests on the stated contact theorem.

As an independent scalar check for a rotationally symmetric base, containment imposes \(a^2\le1-2kb\), so maximizing \(b a^m\) over \(0<b\le1/2\) gives exactly the stated \(b\). The arbitrary-base result is stronger than this symmetric optimization.

## Relationship to prior work

The general nonsymmetric John certificate is classical; its modern proof in [2] is an input, not a novel contribution. Güler and Gürtuna [1] analyze both extremal ellipsoid problems, including a truncated second-order cone/ellipsoidal-cylinder family. Their introduction explicitly says that they **do not solve the inscribed-ellipsoid problem for that family** (Section 1, discussion of Section 8). Their Section 8 instead solves the **circumscribed** ellipsoid problem. The present theorem supplies an inscribed solution for the larger class of frusta over arbitrary convex bases, including bases with trivial symmetry groups. Other homothetic-frustum results about Santaló points and volume products concern different invariants and do not determine this John ellipsoid.

## Limitations

This is the inscribed John ellipsoid of **homothetic** frusta, not frusta with arbitrary unrelated end sections. The theorem is not about the Löwner (outer) ellipsoid or about general nonconvex bases. The historical-priority comparison is provisional for uncatalogued or inaccessible older literature, although the most directly relevant accessible primary work [1] explicitly leaves the corresponding inscribed problem untreated. No independent mathematical validation has yet been performed.

## References

[1] O. Güler and F. Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707v1, publicly posted 5 September 2007, especially the introduction (pp. 2–3) and Section 8. https://arxiv.org/abs/0709.0707

[2] P. M. Gruber and F. E. Schuster, *An Arithmetic Proof of John's Ellipsoid Theorem*, arXiv:1207.7246v1, publicly posted 31 July 2012, Theorem 2. https://arxiv.org/abs/1207.7246
