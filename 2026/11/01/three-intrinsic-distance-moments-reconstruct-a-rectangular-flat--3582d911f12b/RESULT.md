# Three intrinsic distance moments reconstruct a rectangular flat three-torus, with sharp cubic-root stability

## Finding
Let \(T=\mathbb R^3/(a\mathbb Z\oplus b\mathbb Z\oplus c\mathbb Z)\) carry its quotient Euclidean geodesic metric, where \(a,b,c>0\). For independent normalized-volume-uniform points \(X,Y\in T\), put \(D=d_T(X,Y)\) and \(m_j=\mathbb E[D^{2j}]\) for \(j=1,2,3\). **The three numbers \((m_1,m_2,m_3)\) determine \(T\) up to Riemannian isometry**, and the criterion for a triple of real numbers to arise from such a torus is an explicit cubic discriminant condition.

Define
\[
\begin{aligned}
 p_1&=3m_1,\\
 p_2&=\frac{45}{4}(m_2-m_1^2),\\
 p_3&=\frac{945}{16}(m_3-3m_1m_2+2m_1^3),\\
 e_1&=p_1,\quad e_2=\frac{p_1^2-p_2}{2},\quad e_3=\frac{p_1^3-3p_1p_2+2p_3}{6}.
\end{aligned}
\]
Then the multiset of squared quarter-periods \(\{a^2/4,b^2/4,c^2/4\}\) is exactly the multiset of roots of
\[
 P(t)=t^3-e_1t^2+e_2t-e_3.
\]
In particular the squared volume is \(\operatorname{Vol}(T)^2=64e_3\). A moment triple is realizable if and only if \(e_1,e_2,e_3>0\) and
\[
 \Delta=e_1^2e_2^2-4e_2^3-4e_1^3e_3-27e_3^2+18e_1e_2e_3\ge0.
\]
Zero discriminant is allowed and represents repeated periods, including cubic tori.

The first **two** such moments uniquely determine the rectangular three-torus only in the cubic case \(a=b=c\). Every noncubic torus lies in a continuous family of pairwise nonisometric rectangular tori sharing those two moments.

For any fixed squared-quarter-period bounds \(0<\alpha\le a^2/4,b^2/4,c^2/4\le\beta<\infty\), the recovered ordered periods have a global inverse modulus
\[
 \max_{1\le i\le3}|a_{(i)}-a'_{(i)}|\le C_{\alpha,\beta}
 \left(\max_{1\le j\le3}|m_j-m_j'|\right)^{1/3}.
\]
The exponent \(1/3\) is optimal even in an arbitrarily small neighborhood of a cubic torus: no uniformly larger exponent holds for pairs of rectangular three-tori there.

## Assumptions and scope
The lattice is orthogonal, and the metric is the induced intrinsic shortest-path metric; it is *not* the ambient distance between representatives. The three periods are positive but may coincide. The sampling law is normalized Haar/Riemannian volume, and all three moments are exact population moments. An isometry may permute the three period axes. Throughout, \(a_{(1)}\le a_{(2)}\le a_{(3)}\) denotes the sorted periods.

## Proof
**Step 1: the exact distance law and cumulants.** The difference of two independent Haar-uniform points in the compact group \(T\) is Haar-uniform. Its unique shortest coordinate representatives, apart from a null set, are independent uniforms \(V_i\) on \([-a_i/2,a_i/2]\), where \((a_1,a_2,a_3)=(a,b,c)\). Hence, with \(x_i=a_i^2/4\) and independent \(U_i\sim\operatorname{Uniform}[-1,1]\),
\[
 D^2\ \overset{\rm law}=\ \sum_{i=1}^3x_iU_i^2.
\]
For \(Z=U^2\), the raw moments are \(\mathbb E[Z^j]=1/(2j+1)\). Its first three cumulants, computed by subtracting products of lower moments, are \(1/3\), \(4/45\) and \(16/945\). Cumulants add under independent summation and scale by the power of their order, so the first three cumulants of \(D^2\) equal \(\frac13\sum x_i\), \(\frac4{45}\sum x_i^2\), and \(\frac{16}{945}\sum x_i^3\). The ordinary-to-cumulant relations are \(\kappa_1=m_1\), \(\kappa_2=m_2-m_1^2\), \(\kappa_3=m_3-3m_1m_2+2m_1^3\). Therefore \(p_k=\sum x_i^k\) for \(k=1,2,3\).

**Step 2: exact inversion, isometry and feasible region.** Newton's identities give \(e_1=\sum x_i\), \(e_2=\sum_{i<j}x_ix_j\), and \(e_3=x_1x_2x_3\). These are precisely the coefficients of \(P(t)=\prod_i(t-x_i)\). Conversely the discriminant condition \(\Delta\ge0\) guarantees three real roots counted with multiplicity. The strict positivity of all \(e_1,e_2,e_3\) forces those roots to be positive: their product is positive, so the only alternative to three positive roots is one positive root \(w\) and two negative roots \(-u,-v\), \(u,v>0\). But \(e_1=w-u-v>0\) implies \(w>u+v\), whereas then \(e_2=uv-w(u+v)<0\), a contradiction. Thus the conditions are both necessary and sufficient, including discriminant zero. The periods are \(2\sqrt{x_i}\). Their multiset classifies rectangular flat tori: the successive minima of the orthogonal lattice are its three sorted periods, since any lattice vector of length strictly below the next period has zero coordinate in that axis and every longer-axis basis vector witnesses the next independent length. In particular \(\operatorname{Vol}(T)=abc=8\sqrt{x_1x_2x_3}\).

**Step 3: precise two-moment obstruction.** Fixing \(m_1,m_2\) fixes \(p_1,p_2\), hence the intersection of the plane \(x_1+x_2+x_3=p_1\) with the sphere \(x_1^2+x_2^2+x_3^2=p_2\). If the point is cubic, Cauchy–Schwarz gives equality \(p_2=p_1^2/3\), leaving exactly one triple. Otherwise this intersection is a genuine circle centered on the positive diagonal; an open arc around any strictly positive \((x_1,x_2,x_3)\) stays in the positive octant, giving uncountably many period multisets. An explicit pair is \((x_1,x_2,x_3)=(1,2,3)\) and \((2-1/\sqrt3,2-1/\sqrt3,2+2/\sqrt3)\). Both have \(p_1=6\) and \(p_2=14\), hence \((m_1,m_2)=(2,236/45)\), but their third power sums differ by \(2/\sqrt3\).

**Step 4: global inverse modulus.** On \([\alpha,\beta]^3\), the map from \((m_1,m_2,m_3)\) to the coefficients \((e_1,e_2,e_3)\) is polynomial and therefore uniformly Lipschitz. Write \(\varepsilon=\max_j|m_j-m_j'|\); all coefficients of the two monic cubics differ by at most \(C\varepsilon\). On the bounded complex disk containing every root and its unit neighborhood, their polynomial values differ by at most \(C_0\varepsilon\). If \(\varepsilon=0\), the cubics are identical and there is nothing to prove. If \(\varepsilon>0\) is sufficiently small let \(r=(2C_0\varepsilon)^{1/3}\), and take the union of the three radius-\(r\) disks centered on the roots of the first cubic. On the boundary of every connected component, the first cubic has absolute value at least \(r^3>C_0\varepsilon\), hence Rouché's theorem gives equal root counts for the two cubics within each component. Every component has diameter at most \(6r\), since it is formed from at most three overlapping radius-\(r\) disks. The real roots of the two cubics can consequently be matched in increasing order within distance \(6r\). Taking square roots on \([\alpha,\beta]\) gives the claimed \(C_{\alpha,\beta}\varepsilon^{1/3}\) period bound. For larger \(\varepsilon\), enlarge the constant using the bounded period range.

**Step 5: optimality.** With \(0<t<1\), consider the positive squared-quarter-period triples
\[
 x(t)=(1-t,1,1+t),\qquad
 y(t)=(1-t/\sqrt3,1-t/\sqrt3,1+2t/\sqrt3).
\]
They satisfy \(p_1(x)=p_1(y)=3\) and \(p_2(x)=p_2(y)=3+2t^2\) exactly, whereas \(p_3(y)-p_3(x)=2t^3/\sqrt3\). Therefore their first two distance moments agree and the third differs by exactly \(32t^3/(945\sqrt3)\). Their sorted period triples differ by at least a fixed positive multiple of \(t\) as \(t\downarrow0\). Any putative inverse estimate with exponent \(\gamma>1/3\) would force \(ct\le C't^{3\gamma}\), impossible for small \(t\). Both families approach the same cubic torus, completing the sharpness proof.

## Verification
Execute `python3 check.py` using Python's standard library. It verifies the first three exact cumulant-to-polynomial identities for rational period data, the cubic discriminant and roots, the exact two-moment collision, and the near-cubic sharpness algebra numerically at multiple scales. A separate direct sampling calculation draws independent pairs in the original rectangular torus coordinates and compares shortest-path moments to the exact predicted moments. The recorded execution ended with `ALL_CHECKS_PASSED`. This is supplementary verification; the existence, completeness and stability statements above follow from the analytic proof, not from finite tests.

## Relationship to prior work
Mémoli and Needham, *Distance distributions and inverse problems for metric measure spaces*, arXiv:1810.09646 (first submitted October 23, 2018), develop distance histograms as inverse invariants. Their Example 3.18 discusses an equal-distance-histogram construction involving **skew** two-dimensional lattices. The present proof does not rely on the claimed isometry classification of those examples; in any case this is not an inverse criterion on orthogonal three-tori. Glorieux and Yarmola, *Random triangles on flat tori*, arXiv:2003.08190 (first submitted March 18, 2020), study probabilities for homotopy classes of random geodesic triangles; their rectangular-torus extremality does not reconstruct periods from pair distances. Holmin, Kurlberg and Månsson, *On free path length distribution for linear motion in an n-dimensional box*, arXiv:1702.08096 (2017), address a linear-motion/billiard exit statistic rather than the shortest distance between independent Haar points. The coefficient-extraction method is elementary; the present result concerns this particular exact finite-data inverse geometry statement, its full admissible moment region, and the sharp worst-case inverse exponent. Historical priority outside the inspected sources is not established.

## Limitations
This theorem does not apply to general skew flat lattices, whose inverse-histogram behavior is a separate problem. Its moment characterization is exact and noiseless. The cubic-root inverse modulus is deterministic, not a finite-sample estimation guarantee; no statistical confidence bound is asserted. The reconstruction assumes dimension three, an orthogonal lattice, and genuine Riemannian intrinsic shortest-path distance. Prior-art searches cannot prove historical novelty, and earlier equivalent formulas may exist under different terminology.

## References
- F. Mémoli and T. Needham, *Distance distributions and inverse problems for metric measure spaces*, arXiv:1810.09646, first version 2018-10-23, especially §3, Example 3.18. https://arxiv.org/abs/1810.09646
- O. Glorieux and A. Yarmola, *Random triangles on flat tori*, arXiv:2003.08190, 2020-03-18. https://arxiv.org/abs/2003.08190
- P. Holmin, P. Kurlberg and D. Månsson, *On free path length distribution for linear motion in an n-dimensional box*, arXiv:1702.08096, 2017. https://arxiv.org/abs/1702.08096
