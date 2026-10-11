# Exact diameter law and exponential endpoint fluctuations for random cross-polytope hyperplane sections

## Finding

For each integer \(n\ge2\), let
\[
C_n=\left\{x\in\mathbb R^n:\sum_{j=1}^n|x_j|\le1\right\},\qquad E_n=U_n^\perp,
\]
where \(U_n\) is uniformly distributed on the Euclidean unit sphere. Write \(D_n=\operatorname{diam}_2(C_n\cap E_n)\) for the **Euclidean** diameter. For independent standard Gaussian \(G_1,\ldots,G_n\) define
\[
m_n=\min_{1\le i\le n}|G_i|,\qquad M_n=\max_{1\le i\le n}|G_i|.
\]
Then, exactly in distribution,
\[
D_n\stackrel d=\frac{2\sqrt{m_n^2+M_n^2}}{m_n+M_n}.
\]
Define the half-normal distribution function and density by
\[
H(y)=\operatorname{erf}(y/\sqrt2),\qquad h(y)=\sqrt{2/\pi}\,e^{-y^2/2}\quad(y\ge0).
\]
For every \(0\le r\le1\), the **entire finite-dimensional law** is
\[
\boxed{\mathbb P\left\{D_n\le\frac{2\sqrt{1+r^2}}{1+r}\right\}
=n\int_0^\infty h(y)\,[H(y)-H(ry)]^{n-1}\,dy.}
\]
The distribution is atomless and its support is exactly \([\sqrt2,2]\).

The limit at the upper endpoint is non-Gaussian:
\[
\boxed{n\sqrt{\log n}\,(2-D_n)\ \Longrightarrow\ \operatorname{Exp}(1/\sqrt\pi),}
\]
where \(\operatorname{Exp}(\lambda)\) has density \(\lambda e^{-\lambda t}\) for \(t\ge0\). In fact the limit holds in every fixed positive integral moment:
\[
\boxed{\lim_{n\to\infty}\mathbb E\bigl[n\sqrt{\log n}(2-D_n)\bigr]^k
=k!\,\pi^{k/2}\quad(k=1,2,\ldots).}
\]
In particular,
\[
\mathbb E(2-D_n)\sim\frac{\sqrt\pi}{n\sqrt{\log n}},\qquad
\operatorname{Var}(D_n)\sim\frac{\pi}{n^2\log n}.
\]

## Assumptions and scope

The hyperplane is central and distributed according to Haar measure on the Grassmannian of codimension-one linear subspaces. The cross-polytope has the displayed \(\ell_1\)-unit normalization, not Euclidean circumradius normalization under a further scaling. Diameter uses ambient Euclidean distance. Dimensions \(n\ge2\) are covered individually, and the limit sends the ambient dimension to infinity while keeping the hyperplane codimension exactly one. The a.s. genericity conditions (nonzero, pairwise unequal absolute normal coordinates) are consequences of Gaussian continuity; nongeneric normals need not be considered for distributional claims.

For a threshold \(t\in[\sqrt2,2]\), one can evaluate its CDF by substituting
\[
s=t/2,\qquad r(t)=\frac{1-s^2}{s^2+\sqrt{2s^2-1}}
\]
into the finite integral above. The CDF equals zero for \(t\le\sqrt2\) and one for \(t\ge2\).

## Proof

**1. Exact deterministic diameter.** Let \(u=(u_1,\ldots,u_n)\) be a normal vector with all coordinates nonzero. The cross-polytope \(C_n\) has vertices \(\pm e_i\), and each edge connects one signed vertex in coordinate \(i\) to one signed vertex in a different coordinate \(j\). In every pair \(i<j\), exactly two such edges cross \(u^\perp\) in relative interiors. Their intersection points are antipodal, namely
\[
\pm v_{ij},\qquad
v_{ij}=
\frac{|u_j|\operatorname{sgn}(u_i)e_i-|u_i|\operatorname{sgn}(u_j)e_j}
{|u_i|+|u_j|}.
\]
Every vertex of a hyperplane section of a polytope not passing through an original vertex is obtained by intersecting the hyperplane with an original edge. Hence these points are the complete vertex set of \(C_n\cap u^\perp\). The section is centrally symmetric. For any centrally symmetric compact convex set, the Euclidean diameter is twice its maximum norm: the triangle inequality supplies the upper bound, and the antipodal pair at maximal norm attains it. Therefore
\[
\operatorname{diam}_2(C_n\cap u^\perp)
=2\max_{i<j}\frac{\sqrt{|u_i|^2+|u_j|^2}}{|u_i|+|u_j|}.
\]
For \(0<a\le b\), this pair norm is \(f(a/b)\), where \(f(q)=\sqrt{1+q^2}/(1+q)\). Direct differentiation gives
\[
f'(q)=\frac{q-1}{(1+q)^2\sqrt{1+q^2}}\le0\quad(0<q\le1).
\]
Thus the maximal norm comes from the pair of smallest and largest coordinate absolute values. This proves the deterministic formula with \(a=\min_i|u_i|\) and \(b=\max_i|u_i|\).

**2. Exact random CDF.** The Gaussian direction \(G/\|G\|_2\) is Haar-uniform, and scaling the normal does not affect the ratio \(a/b\). Thus the deterministic identity yields the stated equality in law. Since \(f\) decreases on \([0,1]\), for \(0\le r\le1\),
\[
\left\{D_n\le2f(r)\right\}=\left\{m_n/M_n\ge r\right\}
\]
almost surely. Conditional on which of the \(n\) independent half-normal variables is the largest and on that maximum lying in \(dy\), every other observation must lie in \([ry,y]\). Summing over the possible maximum index gives exactly
\[
n\int_0^\infty h(y)[H(y)-H(ry)]^{n-1}\,dy.
\]
Gaussian continuity rules out atoms, and every open interval of ratios within \((0,1)\) has positive probability; this proves the asserted closed support. Solving \(t/2=f(r)\) gives the displayed inverse \(r(t)\).

**3. Exponential endpoint limit.** Put \(c=\sqrt{2/\pi}\). At the origin, \(H(z)=cz+O(z^3)\); hence for each fixed \(x\ge0\),
\[
\mathbb P\{nm_n>x\}=[1-H(x/n)]^n\longrightarrow e^{-cx}.
\]
Thus \(nm_n\Rightarrow\operatorname{Exp}(c)\). Standard Gaussian maximum estimates give
\[
M_n/\sqrt{2\log n}\longrightarrow1\qquad\text{in probability}.
\]
For completeness: the upper tail follows by a Gaussian union bound; the lower tail follows from \(\mathbb P\{M_n\le z\}=H(z)^n\) and the elementary Gaussian tail lower bound \(1-H(z)\ge c_0(1+z)^{-1}e^{-z^2/2}\) for \(z\ge1\). Since \(m_n/M_n\to0\) in probability and
\[
2-2f(q)=2q+O(q^2)\quad(q\to0),
\]
Slutsky's theorem gives
\[
n\sqrt{\log n}(2-D_n)
=\sqrt2\,(nm_n)\,\frac{\sqrt{2\log n}}{M_n}\,[1+o_{\mathbb P}(1)]
\Longrightarrow\sqrt2\operatorname{Exp}(c)
=\operatorname{Exp}(1/\sqrt\pi).
\]
The identity uses the usual scaling convention for an exponential variable; its limit rate is \(c/\sqrt2=1/\sqrt\pi\).

**4. Convergence of all fixed moments.** For \(0\le q\le1\), \(0\le2-2f(q)\le2q\), so with \(T_n=n\sqrt{\log n}(2-D_n)\), on \(\{M_n\ge\sqrt{\log n}\}\) one has \(T_n\le2nm_n\). The latter family has uniformly bounded moments of every finite order. Indeed, for \(0\le t\le n\), concavity of \(H\) yields \(H(t/n)\ge H(1)t/n\), so \(\mathbb P\{nm_n>t\}\le e^{-H(1)t}\); for \(t\ge n\), the Gaussian tail bound \(1-H(x)\le e^{-x^2/2}\) gives \(\mathbb P\{nm_n>t\}\le e^{-t^2/(2n)}\le e^{-t/2}\). Thus all its tail moments are uniformly bounded.

On the complementary event, the elementary bound \(T_n\le n\sqrt{\log n}\) applies, and the Gaussian lower-tail bound gives
\[
\mathbb P\{M_n<\sqrt{\log n}\}
=H(\sqrt{\log n})^n
\le\exp\{-c_1\sqrt n/\sqrt{\log n}\}
\]
for all sufficiently large \(n\) and some \(c_1>0\). Consequently every fixed moment of \(T_n\) is uniformly bounded, and, by applying this argument at an arbitrarily higher power, the fixed-power family is uniformly integrable. The distributional limit therefore implies convergence of each fixed moment. Taking the first two gives the stated mean and variance asymptotics. This completes the proof.

## Verification

The accompanying standard-library program `verify.py` enumerates every crossed signed edge for independent normal samples in dimensions \(2,3,4,7\), computes the literal all-pairs section-vertex diameter, and compares it against the closed min/max-coordinate formula. It also checks the independent half-normal order-statistic CDF integral against seeded Monte Carlo frequencies for four dimension/threshold pairs and tests both integral endpoints. Run `python verify.py` beside this document. The successful output ends with `CROSSPOLYTOPE_DIAMETER_FINITE_CHECKS_OK`.

These finite tests do not prove the asymptotic limit or moment uniform integrability, which are established in Step 3–4.

## Relationship to prior work

Guédon, Litvak, Tatarko and Vritsiou (2026) motivate the study of random section diameters through high-probability geometric inequalities and applications to \(\ell_p\)-ellipsoids. The exact codimension-one cross-polytope CDF, non-Gaussian endpoint law and all fixed moments here are different, distributional assertions; the source's complete manuscript was not available for full-text overlap inspection, so unrecognized stronger coverage remains an originality risk. König (2020) studies extremal volumes and boundary volumes of cross-polytope and other sections, rather than the Haar diameter law. Kabluchko, Litvak and Zaporozhets (2017) obtain Gaussian limit laws for **one-dimensional projection lengths**, a dual-looking but geometrically distinct observable. A special three-dimensional octahedron section-diameter distribution has already been studied; that case is explicitly not represented as new, and does not imply the \(n\to\infty\) endpoint law or the all-dimensional integral.

## Limitations

The conclusions apply to Haar central hyperplanes of \(\ell_1\) balls, not arbitrary codimension, deterministic hyperplane arrangements, or other polytopes. The Gaussian limit is not an independent audit of scientific novelty. Searches of accessible literature and indexed records do not prove uniqueness of the statement. In particular, the full text of the closely related September 2026 preprint could not be inspected; this limits the originality comparison but does not affect the self-contained geometric/probabilistic proof.

## References

1. O. Guédon, A. E. Litvak, K. Tatarko, B.-H. Vritsiou, *On random diameters of convex bodies*, first posted 21 September 2026, arXiv:2609.24131v1, https://arxiv.org/abs/2609.24131.
2. H. König, *Non-central sections of the simplex, the cross-polytope and the cube*, arXiv:2002.10743, https://arxiv.org/abs/2002.10743.
3. Z. Kabluchko, A. E. Litvak, D. Zaporozhets, *Mean Width of Regular Polytopes and Expected Maxima of Correlated Gaussian Variables*, Journal of Mathematical Sciences 225 (2017), 770–787, DOI 10.1007/s10958-017-3492-3.
4. S. Brazitikos, I. Pandis, *Restricted Hyperplane Sections of the Cross-Polytope and the Simplex*, arXiv:2606.07163, https://arxiv.org/abs/2606.07163.
