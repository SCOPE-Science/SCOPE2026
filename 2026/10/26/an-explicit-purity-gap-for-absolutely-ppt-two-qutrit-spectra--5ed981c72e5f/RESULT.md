# An explicit purity gap for absolutely PPT two-qutrit spectra

## Finding

Let \(\rho\) be a density operator on \(\mathbb C^3\otimes\mathbb C^3\). If \(\rho\) is absolutely positive under partial transpose (APPT), then
\[
\operatorname{Tr}(\rho^2)\leq \frac{312737}{2120625}
=\frac{25}{169}-\frac{12544}{27568125}.
\]
The outer spectral polytope obtained from a necessary APPT inequality has maximum purity \(25/169\), attained at
\[
\lambda_*=\frac1{13}(3,3,1,1,1,1,1,1,1).
\]
The displayed bound gives a strictly positive, explicit rational gap below that outer-polytope value. It is not asserted to be sharp and does not determine the exact maximum APPT purity.

## Assumptions and scope

Write the ordered eigenvalues of \(\rho\) as
\[
\lambda_1\geq\lambda_2\geq\cdots\geq\lambda_9\geq0,
\qquad \sum_{j=1}^9\lambda_j=1.
\]
The quantity being bounded is \(F(\lambda)=\sum_{j=1}^9\lambda_j^2\). APPT means that every global-unitary conjugate of \(\rho\) is PPT for the fixed \(3\otimes3\) bipartition.

Hildebrand's spectral criterion implies that every APPT spectrum lies in the outer polytope
\[
\mathcal S_9=\left\{\lambda:\lambda_1\geq\cdots\geq\lambda_9\geq0,\ 
\sum_{j=1}^9\lambda_j=1,\ \lambda_1\leq\lambda_7+\lambda_8+\lambda_9\right\}.
\]
For an APPT spectrum, the first qutrit Hildebrand matrix
\[
K(\lambda)=
\begin{pmatrix}
2\lambda_9&\lambda_8-\lambda_1&\lambda_6-\lambda_2\\
\lambda_8-\lambda_1&2\lambda_7&\lambda_5-\lambda_3\\
\lambda_6-\lambda_2&\lambda_5-\lambda_3&2\lambda_4
\end{pmatrix}
\]
is positive semidefinite. Only these necessary conditions are used; the result is specific to \(3\otimes3\).

## Proof

The vertices of \(\mathcal S_9\) belong to the following three families:
\[
\begin{aligned}
\text{Type 1: }&\frac1i(1^i,0^{9-i}), && i=7,8,9,\\
\text{Type 2: }&\frac1{8+i}(2^i,1^{8-i},0), && i=1,\ldots,6,\\
\text{Type 3: }&\frac1{9+2i}(3^i,1^{9-i}), && i=1,\ldots,6.
\end{aligned}
\]
Here \(a^i\) means \(i\) repeated entries equal to \(a\), not exponentiation of a vector. The function \(F\) is strictly convex, so its maximum over this compact polytope occurs at a vertex. Exact evaluation of the fifteen listed vertices shows that its unique maximum is
\[
F(\lambda_*)=\frac{25}{169},
\]
and that the second-largest vertex value is \(11/75\), attained by the Type 3 vertex with \(i=3\). Set
\[
F_*=\frac{25}{169},\qquad
\gamma=F_*-\frac{11}{75}=\frac{16}{12675}.
\]
For every other vertex \(v\), exact evaluation also gives
\[
q(v):=2\langle\lambda_*,\lambda_*-v\rangle\geq
q_0:=\frac{16}{845},\qquad
\|\lambda_*-v\|_2^2\leq D^2:=\frac{58}{1183}.
\]
Both bounds are attained among the listed vertices. By linearity of \(q\) and convexity of the squared distance, the same inequalities hold for every \(\mu\) in the convex hull of all vertices other than \(\lambda_*\).

At the outer maximizer,
\[
K(\lambda_*)=\frac1{13}
\begin{pmatrix}2&-2&-2\\-2&2&0\\-2&0&2\end{pmatrix}.
\]
The eigenvalues of the integer matrix displayed here are \(2\), \(2+2\sqrt2\), and \(2-2\sqrt2\). Hence \(K(\lambda_*)\) has least eigenvalue \(-(2\sqrt2-2)/13\). For any APPT spectrum \(\lambda\), \(K(\lambda)\succeq0\), so Weyl's eigenvalue inequality yields
\[
\|K(\lambda)-K(\lambda_*)\|_{\mathrm{op}}\geq
\frac{2\sqrt2-2}{13}.
\]
If \(\delta=\lambda-\lambda_*\), the matrix entries give
\[
\|K(\lambda)-K(\lambda_*)\|_F^2
=4(\delta_9^2+\delta_7^2+\delta_4^2)
+2\!\left[(\delta_8-\delta_1)^2+(\delta_6-\delta_2)^2+
(\delta_5-\delta_3)^2\right]
\leq4\|\delta\|_2^2.
\]
Consequently
\[
\|\lambda-\lambda_*\|_2\geq d_0:=\frac{\sqrt2-1}{13}.
\]

Express \(\lambda=(1-t)\lambda_*+t\mu\), where \(t\in(0,1]\) and \(\mu\) is a convex combination of the other vertices. Such a representation exists by the vertex description; \(t>0\) because \(\lambda_*\) is not APPT. The vertex-distance bound gives
\[
\|\lambda-\lambda_*\|_2\leq tD,\qquad
t\geq t_0:=\frac{d_0}{D}=\frac{7(\sqrt2-1)}{\sqrt{406}}.
\]
Define
\[
G:=F_*-F(\lambda),\qquad
t_*:=\frac{q_0-\gamma}{D^2}=\frac{784}{2175}.
\]
Convexity of \(F\) and the second-largest vertex value imply \(G\geq\gamma t\). Expanding the quadratic exactly and using the bounds on \(q(\mu)\) and \(\|\mu-\lambda_*\|_2^2\) gives the second bound
\[
G=t\,q(\mu)-t^2\|\mu-\lambda_*\|_2^2
\geq q_0t-D^2t^2.
\]
The comparisons \(2/15<t_0<7/40<1/3<t_*<1/2\) follow from elementary square bounds for \(\sqrt2\) and \(\sqrt{406}\) and the rational value of \(t_*\). Also,
\[
q_0t_0-D^2t_0^2
> \frac{32}{12675}-\frac1{676}
> \frac8{12675}
> \gamma t_*
\]
show that, for \(t_0\leq t\leq t_*\), the concave quadratic \(q_0t-D^2t^2\) is at least \(\gamma t_*\): its minimum on this interval is at an endpoint, and both endpoints satisfy that bound. For \(t\geq t_*\), the bound \(G\geq\gamma t\geq\gamma t_*\) applies. Thus in all cases
\[
F(\lambda)\leq F_*-\gamma t_*
=\frac{25}{169}-\frac{12544}{27568125}
=\frac{312737}{2120625}.
\]
This proves the claim.

## Verification

The accompanying standard-library script enumerates the fifteen vertices using exact rational arithmetic and verifies the values of \(F_*\), \(\gamma\), \(q_0\), \(D^2\), \(t_*\), the rational gap, and the final upper bound. The matrix eigenvalues and norm estimate are given analytically above. No finite experiment is used to infer an infinite-dimensional statement; the theorem concerns the fixed nine-dimensional spectrum.

## Relationship to prior work

Tran's 2026 paper proves that the \(3\otimes n\) APPT purity is strictly below the maximum of the outer spectral polytope and explicitly notes that the exact maximum remains open. The present claim supplies a quantitative, rational lower bound on that strict gap in the \(3\otimes3\) case. It does not claim an exact maximizer or resolve the open optimization problem. The matrix \(K\) is a necessary condition from the Hildebrand spectral criterion, written explicitly for two qutrits in the 2026 classification of APPT extreme points with three distinct eigenvalues.

## Limitations

The bound is non-sharp: it combines a spectral-distance estimate with outer-polytope vertex bounds. It is not an exact formula for the largest APPT purity. The result uses only one of the necessary qutrit matrix inequalities and makes no claim for \(3\otimes n\) when \(n>3\), for absolute separability beyond the implication AS \(\subseteq\) APPT, or for a characterization of all maximizers. Literature searches cannot certify global novelty, and independent audit has not been performed.

## References

1. A. T. Tran, *Spectral Optimization for Absolutely PPT States: Purity, Entropy, and Volume Decay*, arXiv:2609.18568, first posted 2026-09-16. https://arxiv.org/abs/2609.18568
2. R. Hildebrand, *PPT from spectra*, arXiv:quant-ph/0502170, first posted 2005-02-25; published as *Positive partial transpose from spectra*, Phys. Rev. A 76, 052325 (2007). https://arxiv.org/abs/quant-ph/0502170
3. N. Wang, L. Chen, and Z. Song, *Extreme points of absolutely PPT states with exactly three distinct eigenvalues*, arXiv:2603.20717, first posted 2026-03-21. https://arxiv.org/abs/2603.20717
