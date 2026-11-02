# Sharp quadratic onset of three-planet transit visibility

## Finding
For three fixed circular planetary orbital planes with linearly independent unit normals, the solid-angle probability of observing all three transits has an exact positivity threshold as the three transit-band half-widths are scaled together. Immediately above this threshold, the probability turns on **quadratically** with a positive, explicitly computable coefficient determined by at most eight signed corners. This is a local geometric asymptotic, not an approximation to eccentric-orbit or detection-completeness effects.

Let \(n_1,n_2,n_3\in\mathbb R^3\) be unit normals, let \(h_1,h_2,h_3>0\), and let \(t>0\) satisfy \(th_i<1\) for all \(i\). For isotropic unit observer direction \(u\), the ideal triple-transit event is
\[
\mathcal T_t=\{u\in S^2: |n_i\cdot u|\le t h_i\text{ for }i=1,2,3\}.
\]
Write \(P(t)=\operatorname{area}(\mathcal T_t)/(4\pi)\), \(N=(n_i^\top)_{i=1}^3\), and \(D=\operatorname{diag}(h_1,h_2,h_3)\). If \(\operatorname{rank}N<3\), then \(P(t)>0\) for every admissible \(t>0\). Otherwise define
\[
A=N^{-1}D,\qquad H=\max_{s\in\{-1,1\}^3}\|As\|_2,\qquad t_c=H^{-1}.
\]
Then \(P(t)=0\) for \(t\le t_c\) and \(P(t)>0\) for \(t>t_c\). In particular the exact cutoff is obtained by checking only four antipodal sign classes, equivalently the four values \(s^\top D(NN^\top)^{-1}Ds\).

For every maximizing sign vector \(s\), define the unit vector \(u_s=As/H\) and the three positive numbers
\[
d_i(s)=s_i\,u_s\cdot A_i,\quad i=1,2,3,
\]
where \(A_i\) is column \(i\) of \(A\). The exact onset law is
\[
\boxed{P(t_c+\delta)=C\delta^2+O(\delta^3)\quad(\delta\downarrow0),\qquad C=\frac{H^2|\det A|}{8\pi}\sum_{\substack{s\in\{-1,1\}^3\\\|As\|_2=H}}\frac1{d_1(s)d_2(s)d_3(s)}>0.}
\]
For three pairwise perpendicular orbital normals with equal base half-widths \(h_i=1/\sqrt3\), this simplifies to \(t_c=1\) and \(C=3\sqrt3/\pi\).

## Assumptions and scope
The result concerns circular, stationary, non-precessing orbits, pointlike planetary occultation geometry with a prescribed transit impact limit, isotropically distributed observer directions, and three strictly positive half-widths. Strict inequalities between the scaled half-widths and one ensure that each individual ideal transit band is nondegenerate. The threshold and asymptotic coefficient are statements about a continuous artificial common scale \(t\); no stellar radius is required to vary physically.

## Proof
If \(\operatorname{rank}N<3\), choose a unit vector \(u\in\ker N\). All three transit inequalities hold strictly at this \(u\), and hence on an open spherical neighborhood; the probability is positive.

Suppose \(N\) is invertible. Set \(z=D^{-1}Nu\), so \(u=Az\). The three transit constraints become \(z\in[-t,t]^3\), while the observer condition is \(\|Az\|_2=1\). The positive-definite quadratic form \(\|Az\|_2^2\) is strictly convex. Its maximum over the cube is attained only at vertices, and its value is \(t^2H^2\). Thus no unit vector is feasible when \(tH<1\). At \(tH=1\), feasibility is confined to finitely many cube vertices, giving zero sphere area. At \(tH>1\), choosing a maximizing \(s\) and \(u_s=As/H\) yields \(|(D^{-1}Nu_s)_i|=1/H<t\) for every \(i\), so the admissible sphere area is strictly positive.

Now let \(t=t_c+\delta\), \(\delta>0\). At criticality, the intersection of the boundary of the cube image and the unit sphere consists exactly of the maximizing vertices \(u_s\). Distinct maximizing vertices are separated because \(A\) is invertible. Compactness therefore localizes all near-critical sphere patches to disjoint neighborhoods of these vertices.

For a maximizing sign vector \(s\), compare the adjacent cube vertex \(s-2s_i e_i\). Maximality gives
\[
\|As-2s_iA_i\|_2^2\le H^2
\quad\Longrightarrow\quad
d_i(s)\ge\frac{\|A_i\|_2^2}{H}>0.
\]
Parameterize the cube near the associated corner by \(z_i=s_i(t-y_i)\), where each \(y_i\ge0\). The sphere equation, using \(t_cH=1\), expands as
\[
\|A z\|_2^2-1=2H\delta-2\sum_{i=1}^3d_i(s)y_i+O(\delta^2+\delta\|y\|+\|y\|^2).
\]
Positivity of all \(d_i(s)\) forces \(y_i=O(\delta)\) on the local intersection. After rescaling \(y=\delta v\), the spherical patch converges smoothly to the plane triangle
\[
\{v_i\ge0:\ \sum_i d_i(s)v_i=H\}.
\]
This triangle has Euclidean area \(H^2\|d\|_2/[2d_1d_2d_3]\) in the \(v\)-coordinate plane. The linear map from \(v\) to the physical tangent plane is \(-A\operatorname{diag}(s)\). Its two-dimensional area factor is \(|\det A|/\|d\|_2\), since \(d=(A\operatorname{diag}(s))^\top u_s\) and \(\|u_s\|_2=1\). Thus the contribution of that corner is
\[
\frac{H^2|\det A|}{2d_1(s)d_2(s)d_3(s)}\delta^2+O(\delta^3)
\]
to spherical area. Summing the disjoint corner patches and dividing by \(4\pi\) proves the displayed coefficient. The smooth local quadratic parametrization yields the stated remainder order. There are no additional patches, by the critical compactness argument.

For the orthogonal example, \(A=I/\sqrt3\), every one of the eight sign vectors maximizes with \(H=1\), and all three corner coefficients have \(d_i=1/3\). Direct substitution gives \(C=3\sqrt3/\pi\).

## Verification
The accompanying \(\texttt{verify.py}\) performs exact rational vertex checks for six nonsingular three-dimensional parallelepipeds and independently integrates the isotropic spherical area for the orthogonal example. For \(\delta\) successively \(0.1,0.03,0.01,0.003,0.001\), the independently integrated values of \(P(t_c+\delta)/\delta^2\) converge numerically from approximately \(1.85686\) to \(1.65564\), consistent with \(3\sqrt3/\pi\approx1.65399\). These finite checks support but do not replace the arbitrary-geometry proof. Run \(\texttt{python verify.py}\) from the package directory with Python 3.

## Relationship to prior work
Ragozzine and Holman (2010) motivate multi-transit visibility and derive estimates for double-transit geometry. Brakensiek and Ragozzine (2016) present CORBITS, a general semi-analytical spherical-area procedure that already evaluates joint transit probabilities and can detect empty joint visibility regions. Neither underlying transit-band geometry nor the existence of general numerical computation is new here. The claimed additional result is a closed four-sign algebraic positivity threshold and, more importantly, the universal quadratic near-threshold law with its explicit corner-sum coefficient for arbitrary non-coplanar triples. An algorithm that evaluates the full probability at specified parameters does not itself state or establish this parameter-uniform local asymptotic. The possibility of an equivalent geometric asymptotic in other convex-body or astronomical literature remains a priority risk.

## Limitations
The theorem is geometric, not an assessment of real survey completeness, planetary stability, orbital eccentricity, dynamical precession, limb darkening, or time-domain detection. It does not give a full closed form for \(P(t)\) far above the threshold. The coefficient is for a common scaling of the three half-widths; independently varying widths can follow different local scalings. The result has not undergone independent audit.

## References
Ragozzine, D., and Holman, M. J. (2010), *The Value of Systems with Multiple Transiting Planets*, arXiv:1006.3727v1, first public 2010-06-18. https://arxiv.org/abs/1006.3727

Brakensiek, J., and Ragozzine, D. (2016), *Efficient Geometric Probabilities of Multi-Transiting Exoplanetary Systems from CORBITS*, arXiv:1602.07014v1, first public 2016-02-23. https://arxiv.org/abs/1602.07014 ; *Astrophysical Journal* 821, 47, doi:10.3847/0004-637X/821/1/47.
