# A transverse cubic-Veronese quotient along a singular plane of the Han–Kwak fourfold

## Finding
Let \(X\subset\mathbb P^7_{\mathbb C}\) be the normal degree-eleven fourfold given by the eight cubic coordinates of Han and Kwak, Example 6.3 [1]. Let
\[
\Pi=V(x_0,x_1,x_4,x_5,x_6)\subset\mathbb P^7,
\qquad
\Pi^\circ=\Pi\cap\{x_2x_3x_7\ne0\}.
\]
Then \(\Pi^\circ\subset\operatorname{Sing}(X)\), and at **every closed point** \(P\in\Pi^\circ\) the completed local ring is
\[
\widehat{\mathcal O}_{X,P}\cong
\frac{\mathbb C[[T,Q,U_0,U_1,U_2,U_3]]}
{(U_0U_2-U_1^2,\ U_0U_3-U_1U_2,\ U_1U_3-U_2^2)}.
\]
Thus the transverse analytic singularity is uniformly the cone over the rational normal cubic, equivalently the cyclic quotient \(\mathbb A^2/\mu_3\) with scalar weights \(\frac13(1,1)\). The reduced singular locus of \(X\) on the open chart \(x_2x_3x_7\ne0\) is **exactly** \(\Pi^\circ\). Its generic transverse multiplicity is three, its canonical Cartier index is three, and the germ is rational and klt but **not canonical**. Blowing up the smooth singular plane on this open set resolves the germ; the exceptional divisor is locally a \(\mathbb P^1\)-bundle with normal degree \(-3\) on its fibers and discrepancy \(-1/3\).

## Assumptions and scope
The ground field is \(\mathbb C\). The projective coordinates are \(x_0,\ldots,x_7\). The fourfold is the closure of the image of the rational map \(\mathbb P^4\dashrightarrow\mathbb P^7\) with coordinate forms, in order,
\[
(y_0y_2^2,\ y_2y_3y_4,\ y_1^3,\ y_0y_2y_4,\ y_1y_2y_3,\ y_1^2y_2,\ y_2^2y_4,\ y_0y_1y_2+y_3^2y_4).
\]
The theorem concerns the indicated dense two-dimensional open part of one singular plane. No claim is made about the other planes, singular quadric, line, or points of \(\Pi\) outside \(\Pi^\circ\).

## Proof
Work on the affine chart \(x_2=1\); write \(t=x_3\), \(q=x_7\), and \((A,B,C,D,E)=(x_0,x_1,x_4,x_5,x_6)\). On the dense parametric chart \(y_1=1\), with \((\alpha,\beta,\gamma,\delta)=(y_0,y_2,y_3,y_4)\), the coordinate map is
\[
(A,B,t,C,D,E,q)=(\alpha\beta^2,\ \beta\gamma\delta,\ \alpha\beta\delta,\ \beta\gamma,\ \beta,\ \beta^2\delta,\ \alpha\beta+\gamma^2\delta).
\]
Direct substitution shows that the following four polynomials vanish on \(X\):
\[
\begin{aligned}
F_1&=A^2+qBC+tC^2-q^2D^2,\\
F_2&=AD+BC-qD^2,\\
F_3&=AB-tCD,\\
F_4&=B^2+tD^2-qE.
\end{aligned}
\]
Localize at \(tq\ne0\) and formally choose a square root \(s\) of \(t\) near any chosen nonzero \(t_0\). Since \(q\) is invertible, \(F_4\) eliminates \(E\). Make the invertible linear substitutions (with coefficients regular in \(t,q,s\))
\[
a=A/q,\quad b=B/s,\quad c=sC/q,\quad d=D,
\qquad
U_0=a,\quad U_1=c,\quad U_2=d-a,\quad U_3=b-c.
\]
The three standard Hankel minors satisfy the **exact identities**
\[
\begin{aligned}
U_0U_2-U_1^2&=F_2/q-F_1/q^2,\\
U_0U_3-U_1U_2&=F_3/(qs),\\
U_1U_3-U_2^2&=2F_2/q-F_1/q^2.
\end{aligned}
\]
In particular \((F_1,F_2,F_3,F_4)\) becomes the defining prime ideal of the product of a smooth two-dimensional parameter base with the affine cone over the twisted cubic. The latter ideal is prime: it is the kernel of
\[
\mathbb C[U_0,U_1,U_2,U_3]\longrightarrow\mathbb C[u,v],
\quad(U_0,U_1,U_2,U_3)\longmapsto(u^3,u^2v,uv^2,v^3).
\]
This identification holds faithfully flat after adjoining \(s\), and thus proves primeness over the original parameter ring as well. Its total dimension is four.

The actual affine ideal of \(X\) is prime and contains these four equations. It has dimension four because the parametrization is birational on \(D=x_5\ne0\): there \(\beta=D\), \(\gamma=C/D\), \(\delta=E/D^2\), and \(\alpha=A/D^2\). Hence these two prime ideals, one contained in the other and both of dimension four, coincide upon localization at \(tq\ne0\). This proves the asserted full analytic local-ring presentation, not merely an equality of tangent cones. The twisted-cubic cone is smooth away from its vertex, proving the precise reduced singular locus on this open chart.

The Veronese subring \(\mathbb C[u^3,u^2v,uv^2,v^3]\) is \(\mathbb C[u,v]^{\mu_3}\) for simultaneous multiplication of \(u,v\) by a third root of unity. The scalar action is free away from the origin; the quotient is a normal rational klt surface singularity. Its canonical character has order three and the nontrivial group element has age \(2/3<1\), so it is not canonical. Blowing up the vertex gives \(\operatorname{Tot}(\mathcal O_{\mathbb P^1}(-3))\). If \(E_0\) denotes the exceptional zero section, \(E_0^2=-3\) and \(K\cdot E_0=1\) by adjunction, hence its discrepancy is \(-1/3\). Taking the product with the smooth two-dimensional base proves all geometric assertions.

## Verification
The exact-arithmetic script `verify.py` checks the four polynomial identities against the actual cubic parametrization, the three invertible coordinate-change identities, and the standard Veronese minors. It returns `VERIFY_OK`. The equality of ideals is justified independently by primeness, inclusion, and dimension in the proof; the script is not an infinite-case or priority certificate.

## Relationship to prior work
Han–Kwak [1, Example 6.3] prove that the degree-eleven example is normal and ACM and that its singular locus is the union of a line, three planes, and a quadric surface. Their computation notebook [2, Example 6.3] computes the homogeneous kernel and decomposes the singular locus; neither source specifies a local analytic normal form or a canonical discrepancy for this plane. The classification of the twisted-cubic cone as a cyclic quotient is standard background, used here after an explicit new identification of the completed germ. The result concerns Example 6.3, not the different Example 6.2.

## Limitations
Only the locus \(x_2x_3x_7\ne0\) is classified. The formal square root of \(t\) need not be globally single-valued on its punctured parameter space, so the statement is analytic or étale-local, not a claim of global Zariski product decomposition. Nothing here classifies the remaining singular strata or the scheme structure at their intersections. A broader, currently unlocated determinantal classification could independently imply this specialized normal form.

## References
[1] J. I. Han and S. Kwak, *Linear syzygies and linear subspaces whose lines are multisecant*, arXiv:2610.12078v1 (first public 2026-10-08), Example 6.3 and Section 6. https://arxiv.org/html/2610.12078v1

[2] J. I. Han and S. Kwak, `multisecant/code.m2`, the source authors' accompanying computation notebook, Example 6.3 block. https://github.com/jihan099/multisecant/blob/main/code.m2
