# A marked small-overlap law and affine-curvature rigidity for two convex bodies

## Finding

For two independently specified smooth, positively curved planar convex bodies, the near-zero cross-covariogram has a universal **two-thirds probability exponent**, a direction-resolved curvature density, and a universal **independent beta-distributed overlap fraction**. The limiting normal-angle law is the affine-arclength law of the difference body **exactly for a homothetic reflected pair**. In addition, the unconditioned angular intensity, together with the difference body, recovers the **unordered individual contact curvature radii**. These statements form one contact-geometry theorem.

Put \(c=(9/32)^{1/3}\). With notation from the next section, for every Borel \(E\subset[0,2\pi)\) and \(0\le z\le1\),
\[
\Pr\bigl(0<G(T)\le z\varepsilon,\ \Theta(T)\in E\bigr)
=\frac{c\,z^{2/3}\varepsilon^{2/3}}{|M|}
\int_E m(\theta)q(\theta)^{1/3}\,d\theta+O(\varepsilon).
\tag{1}
\]
The error is uniform in \(E\) and \(z\). In particular, the corresponding conditional joint law tends to the product of (i) the angle measure with density \(m q^{1/3}/\int m q^{1/3}\) and (ii) the beta distribution with cumulative distribution function \(z^{2/3}\).

## Assumptions and scope

Let \(K,L\subset\mathbb R^2\) be compact convex bodies with nonempty interior. Suppose their boundaries are \(C^3\), strictly convex, and have curvature bounded strictly away from zero. Let \(M=K-L=K+(-L)\), and choose a translation \(T\) uniformly according to planar Lebesgue area on \(M\). Define the cross-overlap area \(G(t)=|K\cap(L+t)|\), where vertical bars mean Euclidean planar area. The interior of \(M\) is exactly the positivity set of \(G\); \(G=0\) on its boundary.

For \(u_\theta=(\cos\theta,\sin\theta)\), denote by \(x_K(\theta)\) and \(x_L(\theta+\pi)\) the unique boundary points with outer normals \(u_\theta\) and \(-u_\theta\). Their positive curvature radii are
\[
\rho_1(\theta)=\kappa_K(x_K(\theta))^{-1},\qquad
\rho_2(\theta)=\kappa_L(x_L(\theta+\pi))^{-1}.
\]
Write \(m(\theta)=\rho_1(\theta)+\rho_2(\theta)\) and \(q(\theta)=\rho_1(\theta)^{-1}+\rho_2(\theta)^{-1}\). A point \(t\) in a sufficiently thin inner tubular neighborhood of \(\partial M\) has a unique nearest point on \(\partial M\); define \(\Theta(t)\) as that nearest boundary point's outer-normal angle. Since all sufficiently small positive overlaps occur in this tube, the event in (1) is well-defined for small \(\varepsilon\). All probability statements refer to fixed \(K,L\) and \(\varepsilon\downarrow0\).

## Proof

**Step 1: support-normal parameterization.** Let \(h_K,h_{-L}\) be support functions. Their sum \(h_M=h_K+h_{-L}\) is the support function of \(M\), whose radius of curvature at angle \(\theta\) is \(h_M+h_M''=m(\theta)>0\). The boundary point is
\[
t_0(\theta)=x_K(\theta)-x_L(\theta+\pi).
\]
For sufficiently small \(s>0\), the map \((\theta,s)\mapsto t_0(\theta)-s u_\theta\) is one-to-one, and its area Jacobian is exactly \(m(\theta)-s\). (Indeed \(t_0'(\theta)=m(\theta)u_\theta^\perp\), while \(u_\theta'=u_\theta^\perp\).) A strictly positive lower bound for \(m\) gives a uniform tube radius.

**Step 2: two-body lens expansion.** Translate and rotate coordinates so the two boundaries contact at the origin, their common tangent is horizontal and the first body's outer normal is the positive vertical direction. When the translation moves inward by \(s\), the two local arcs have separating heights
\[
s-\frac{q(\theta)}2 y^2+O(|y|^3),
\]
uniformly in \(\theta\), on a horizontal interval of width \(O(\sqrt s)\). Positive curvature ensures that all intersection area for sufficiently small \(s\) is confined to this local neighborhood. Consequently
\[
G(t_0(\theta)-s u_\theta)
=\int_{-\sqrt{2s/q}}^{\sqrt{2s/q}}
\left(s-\frac{q y^2}{2}\right)dy+O(s^2)
=\frac43\sqrt{\frac2{q(\theta)}}s^{3/2}+O(s^2).
\tag{2}
\]
Uniformity follows by finite charts, compactness, bounded third derivatives, and uniform positive upper and lower curvature bounds. The error bound includes the endpoint perturbations, which change area by no more than the stated order.

**Step 3: invert and integrate.** Set \(C(\theta)=\frac43\sqrt{2/q(\theta)}\). Overlap is strictly increasing along a sufficiently short inward normal segment: differentiating the local lens-section integral with its zero-height moving endpoints gives \(\partial_s G=2\sqrt{2s/q(\theta)}+O(s)>0\) uniformly at small positive \(s\). Thus for every \(v\in(0,\varepsilon]\), its cutoff depth is
\[
s_v(\theta)=\bigl(v/C(\theta)\bigr)^{2/3}+O(v)
=c\,q(\theta)^{1/3}v^{2/3}+O(v),
\tag{3}
\]
uniformly in \(\theta\). The same estimate extends to \(v=0\). Integrating the exact tubular Jacobian gives
\[
\frac1{|M|}\int_E\int_0^{s_{z\varepsilon}(\theta)}
(m(\theta)-s)\,ds\,d\theta,
\]
which yields (1), because \(s_{z\varepsilon}=O(\varepsilon^{2/3})\). Taking ratios at fixed angle sets and fixed \(z\), and then using continuity of the limiting beta distribution, proves joint weak convergence and independence.

**Step 4: recovery.** Let \(b(\theta)\,d\theta\) be the limit of \(\varepsilon^{-2/3}\Pr\bigl(0<G(T)\le\varepsilon,\Theta(T)\in d\theta\bigr)\), so that \(b=c m q^{1/3}/|M|\). The support of \(G\) determines \(M\), and hence its area and the known curvature radius \(m\). Therefore
\[
q(\theta)=\left(\frac{|M|b(\theta)}{c m(\theta)}\right)^3,
\quad \rho_1+\rho_2=m,\quad\rho_1\rho_2=m/q.
\]
The unordered pair \(\{\rho_1,\rho_2\}\) is exactly the pair of roots of \(x^2-mx+m/q=0\). This is pointwise unordered recovery, not a claim to assign the two radii consistently to the named bodies.

**Step 5: affine-arclength rigidity.** Normal-angle affine arclength on the smooth convex curve \(\partial M\) is \(\kappa_M^{1/3}\,ds_M=m^{2/3}d\theta\). The limiting conditional angle distribution equals normalized affine arclength if and only if \(m q^{1/3}\) is proportional to \(m^{2/3}\), equivalently \(m q\) is constant. Write \(r(\theta)=\rho_1(\theta)/\rho_2(\theta)\). Then
\[
mq=2+r+r^{-1}.
\]
If this is constant, the continuous image of the connected circle under \(r\) lies in a set of at most two positive numbers, forcing \(r\) itself to be constant. Thus \(\rho_K(\theta)=\lambda\rho_{-L}(\theta)\) for some \(\lambda>0\). The difference of support functions \(h_K-\lambda h_{-L}\) satisfies \(f''+f=0\), so it equals \(a\cos\theta+b\sin\theta\), a translation support function. Hence \(K\) is a translate of \(\lambda(-L)\). Conversely, such a homothetic reflected pair has constant radius ratio, hence the affine-arclength angle law. This proves the rigidity equivalence.

## Verification

The standalone file `verify.py` independently evaluates lens areas for three pairs of tangent ellipses by numerical one-dimensional quadrature and confirms the coefficient in (2). For unequal disks it integrates the exact translated-disk lens numerically, inverts the threshold, and checks the two-thirds tail and beta conditional CDF. Additional checks confirm the curvature-pair inversion and the affine-arclength rigidity diagnostic on similar and nonsimilar pairs. Run with `python verify.py`; Python 3, NumPy and SciPy are required. These checks do not establish the general infinite-dimensional claim, which follows from the proof above.

## Relationship to prior work

Meyer–Reisner–Schmuckenschläger [1] give smoothness properties of convolution bodies and a contact-curvature volume formula for \(K\) intersecting its own homothetic translate; the local lens idea is classical. Their Theorem 3.1 is for the same source body and does not state the present mixed-body marked translation law or its affine-arclength equality characterization. Alonso-Gutiérrez–González–Jiménez [2] study volume inequalities and **near-maximal** overlap convolution bodies for general pairs, rather than the **near-zero** joint direction/overlap law. Alonso-Gutiérrez–Martín Goñi [3] establish global Brunn–Minkowski inequalities for overlap superlevel sets, not sharp smooth-boundary contact intensities. Haddad [4] studies volumes of one-body convolution superlevel sets and their extremal behavior. Schmuckenschläger [5] is an especially relevant earlier study of the scalar distribution for the convolution square of a symmetric body; its full text was unavailable during comparison, so its precise overlap remains a historical-priority risk. The present contribution is the **two-distinct-body marked limiting law, unordered curvature recovery, and affine-perimeter rigidity criterion**; no novelty is claimed for single-body local curvature expansions alone.

## Limitations

The theorem requires fixed \(C^3\) strictly positively curved planar convex bodies. It does not cover polygons, flat curvature, higher dimensions, or jointly vanishing overlap and evolving body shape. The inverse determines only the unordered two curvature radii at each normal; global separate-body identifiability is not claimed. The exact \(O(\varepsilon)\) remainder is an absolute error for fixed bodies, not a uniform bound over all shapes. Historical priority remains provisional, particularly because [5] was inaccessible in full. No independent mathematical audit has been performed.

## References

1. M. Meyer, S. Reisner, M. Schmuckenschläger, *The Volume of the Intersection of a Convex Body with its Translates*, arXiv:math/9204212v1, first posted 14 April 1992. https://arxiv.org/html/math/9204212v1
2. D. Alonso-Gutiérrez, B. González, C. H. Jiménez, *Volume inequalities for the i-th-convolution bodies*, arXiv:1312.6005, first posted 20 December 2013; J. Math. Anal. Appl. 424 (2015), 385–401. https://arxiv.org/abs/1312.6005
3. D. Alonso-Gutiérrez, J. Martín Goñi, *Brunn–Minkowski Inequality for θ-Convolution Bodies via Ball’s Bodies*, J. Geom. Anal. 34 (2024), article 58, first online 29 December 2023. https://doi.org/10.1007/s12220-023-01508-2
4. J. Haddad, *On the Volume of Convolution Bodies in the Plane*, J. Geom. Anal. 35 (2025), article 314. https://doi.org/10.1007/s12220-025-02143-9
5. M. Schmuckenschläger, *The Distribution Function of the Convolution Square of a Convex Symmetric Body in R^n*, Israel J. Math. 78 (1992), 309–334. https://doi.org/10.1007/BF02808061
