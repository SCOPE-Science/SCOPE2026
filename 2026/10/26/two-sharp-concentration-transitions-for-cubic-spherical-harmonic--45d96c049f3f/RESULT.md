# Two sharp concentration transitions for cubic spherical harmonics on antipodal caps

## Finding

Let \(d\ge 3\) be an integer and let \(\mathcal H_3(S^{d-1})\) be the real or complex Hilbert space of restrictions to the unit sphere of homogeneous harmonic polynomials of degree three on \(\mathbb R^d\). For \(0<t<1\), put
\[
C_t=\{x\in S^{d-1}:x_d^2\ge t\},\qquad
\mathcal K_{d,t}=P_3\,\mathbf 1_{C_t}|_{\mathcal H_3},
\]
where \(P_3\) is the orthogonal projection in spherical \(L^2\) onto \(\mathcal H_3\). Equivalently, the maximal eigenvalue of \(\mathcal K_{d,t}\) is the optimal proportion of degree-three harmonic energy lying in the two antipodal caps \(C_t\).

There are **exactly two transitions** in the maximizing harmonic type, at
\[
t_1=\frac1{d+2},\qquad t_2=\frac3{d+2}.
\]
Writing \(x=(y,u)\in\mathbb R^{d-1}\times\mathbb R\), define the four harmonic subspaces
\[
\begin{aligned}
V_0&=\operatorname{span}\{(d-1)u^3-3u|y|^2\},\\
V_1&=\{\big((d+1)u^2-|y|^2\big)H_1(y):H_1\in\mathcal H_1(\mathbb R^{d-1})\},\\
V_2&=\{uH_2(y):H_2\in\mathcal H_2(\mathbb R^{d-1})\},\\
V_3&=\{H_3(y):H_3\in\mathcal H_3(\mathbb R^{d-1})\}.
\end{aligned}
\]
Here \(\mathcal H_m(\mathbb R^k)\) denotes homogeneous harmonic polynomials of degree \(m\) on \(\mathbb R^k\). Restrictions to the sphere are implicit. The full maximizing eigenspace is
\[
\begin{array}{c|ccccc}
\text{range of }t&(0,t_1)&\{t_1\}&(t_1,t_2)&\{t_2\}&(t_2,1)\\\hline
\text{maximizing space}&V_2&V_0\oplus V_1\oplus V_2&V_1&V_0\oplus V_1&V_0
\end{array}
\]
and \(V_3\) is strictly suboptimal for every \(0<t<1\). At the first transition the top eigenvalue has multiplicity \(\frac{d(d+1)}2-1\); at the second it has multiplicity \(d\). Away from these transitions, the multiplicities are respectively \(\frac{(d-2)(d+1)}2\), \(d-1\), and \(1\).

## Assumptions and scope

The surface measure on the sphere is its standard rotation-invariant measure; a scalar multiple does not change energy ratios. Caps are closed, but their boundaries have measure zero. Only the **pure degree-three** harmonic space is used: this is *not* the standard low-pass space containing all degrees at most three. The sphere is real, \(d\ge3\), and the operator is the positive compression of multiplication by the cap indicator. For \(t=0\) or \(t=1\), all degree-three harmonics tie (concentration fractions \(1\) and \(0\), respectively), so the classification above deliberately assumes \(0<t<1\).

The fixed axis is arbitrary by rotational invariance. Complex-valued harmonics have the same eigenvalues and complexifications of the displayed optimizing spaces.

## Proof

**1. Complete orthogonal decomposition.** The displayed \(V_m\) are harmonic: apply the Euclidean Laplacian and use \(\Delta_y(|y|^2H_1)=2(d+1)H_1\), \(\Delta_y|y|^2=2(d-1)\). The other two types are immediate. They have distinct degrees \(m\in\{0,1,2,3\}\) in the transverse variable, so are orthogonal under the rotation group \(O(d-1)\). The dimension identity
\[
1+(d-1)+\frac{(d-2)(d+1)}2+\frac{(d-1)(d-2)(d+3)}6
=\frac{d(d-1)(d+4)}6=\dim\mathcal H_3(S^{d-1})
\]
shows that these four spaces exhaust \(\mathcal H_3\). Because \(C_t\) is invariant under \(O(d-1)\), its concentration form is scalar on each \(V_m\), with all mixed terms vanishing by transverse-harmonic orthogonality.

**2. Four normalized eigenbranches.** Let \(s=u^2\). Under normalized spherical measure,
\[
s\sim\operatorname{Beta}\left(\tfrac12,\tfrac{d-1}2\right),\qquad
w_d(s)=\frac{s^{-1/2}(1-s)^{(d-3)/2}}{B(1/2,(d-1)/2)}.
\]
The squared norms of the four harmonic types have their \(s\)-dependence, up to positive constants independent of \(s\), given by
\[
\begin{aligned}
R_0(s)&=s((d+2)s-3)^2,\\
R_1(s)&=(1-s)((d+2)s-1)^2,\\
R_2(s)&=s(1-s)^2,\\
R_3(s)&=(1-s)^3.
\end{aligned}
\]
Consequently, for every \(m=0,1,2,3\), the common concentration eigenvalue on \(V_m\) is the explicit beta integral
\[
\lambda_m(t)=\frac{\int_t^1 R_m(s)w_d(s)\,ds}{N_m},\qquad
N_m=\int_0^1R_m(s)w_d(s)\,ds.
\]
The moments \(\mathbb E[s^k]=(1/2)_k/(d/2)_k\) give
\[
\begin{aligned}
N_0&=\frac{6(d-1)}{d(d+4)},\\
N_1&=\frac{2(d-1)(d+1)}{d(d+4)},\\
N_2&=\frac{(d-1)(d+1)}{d(d+2)(d+4)},\\
N_3&=\frac{(d-1)(d+1)(d+3)}{d(d+2)(d+4)}.
\end{aligned}
\]
All denominators are strictly positive for \(d\ge3\).

**3. Exact eigenvalue differences.** Set
\[
b_d(t)=\frac{\sqrt{t}(1-t)^{(d-1)/2}}{B(1/2,(d-1)/2)}>0\quad(0<t<1).
\]
Direct differentiation yields \(b_d'(t)=w_d(t)(1-dt)/2\). As \(\lambda_m'(t)=-w_d(t)R_m(t)/N_m\) and both sides of each identity below vanish at \(t=0\), elementary expansion gives the **exact**, not asymptotic, formulas
\[
\begin{aligned}
\lambda_0-\lambda_1
 &=b_d(t)\frac{d(d+4)((d+2)t-3)((d+2)t-1)}{3(d-1)(d+1)},\\
\lambda_0-\lambda_2
 &=b_d(t)\frac{d(d+4)t((d+2)t-1)}{3(d+1)},\\
\lambda_1-\lambda_2
 &=b_d(t)\frac{d(d+4)(1-t)((d+2)t-1)}{(d-1)(d+1)},\\
\lambda_2-\lambda_3
 &=b_d(t)\frac{2d(d+2)(d+4)(1-t)^2}{(d-1)(d+1)(d+3)}.
\end{aligned}
\]
To check these without integration, differentiate each right-hand side, divide by \(w_d\), and compare the resulting degree-three polynomials with \(-R_i/N_i+R_j/N_j\). The constant of integration is zero because the factors \(b_d(t)\) and each eigenvalue difference vanish at \(t=0\). These are polynomial identities for symbolic \(d\), not conclusions from a finite test sample.

**4. Comparison and sharpness.** The last difference is strictly positive on \((0,1)\), so \(V_3\) can never maximize. For \(0<t<t_1\), the second and third displayed differences are negative, proving \(\lambda_2>\lambda_0,\lambda_1\). At \(t=t_1\), the first three branches coincide. For \(t_1<t<t_2\), the first difference is negative and the third positive, proving \(\lambda_1>\lambda_0,\lambda_2\). At \(t=t_2\), \(\lambda_0=\lambda_1>\lambda_2\); for \(t_2<t<1\), the first two differences are positive, proving \(\lambda_0>\lambda_1,\lambda_2\). The maximizing eigenspaces and multiplicities now follow from the orthogonal decomposition. Every stated maximum is attained by any nonzero harmonic in its maximizing subspace.

## Verification

The accompanying standalone `check_degree3.py` uses only Python's standard library and checks the rational beta-moment normalizations, four differential difference identities, and eigenspace dimensions for 104 integer dimensions (from \(3\) through \(100\), plus \(101,125,150,200,500,1000\)). The executed script returned `PASS`. This finite computation is a consistency check, **not** a proof for all dimensions; that proof is the symbolic derivation above. Direct quadrature was also compared with all four normalized branches at the two thresholds for sample dimensions \(3,4,5,10\), giving the predicted double and triple coincidences.

## Relationship to prior work

The spherical Slepian framework of Simons, Dahlen and Wieczorek (2004 preprint; 2006 journal version) reduces concentration to finite spectral matrices and develops polar-cap eigenproblems. Simons and Dahlen (2006) explicitly derive commuting operators and parity-block matrices for **two antipodal caps**, the closest source for the same region. Their analysis is on the two-sphere and concerns arbitrary low-pass harmonic bandwidths; their numerical fixed-order examples do not give the two universal, all-dimension transitions for the *pure cubic* space. The present proof uses a different four-type decomposition and evaluates the complete eigenvalue ranking in closed form, rather than introducing a general Slepian method. Bates, Khalid and Kennedy (2016 preprint) address efficient computation of low-pass Slepian bases on the two-sphere, not the present closed phase diagram.

The exact matrix descriptions in those papers are relevant background and can computationally recover low-dimensional instances. The substantive additional assertion here is the universal pair of closed transition locations, including the triple collision and complete all-dimensional optimizing-space classification. No assertion of priority against unindexed literature is made.

## Limitations

This theorem does not determine optimal concentration over mixtures of different spherical harmonic degrees; it does not cover a single cap, displaced or unequal caps, or higher pure degrees. The endpoint cases \(t=0,1\) have the full space as optimizing eigenspace. The originality assessment is based on the particular published works and searches described in the review; a more specialized unindexed identity or general theorem could exist. Independent external mathematical auditing has not occurred.

## References

1. F. J. Simons, F. A. Dahlen, and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424v1 (first posted 2004-08-31); SIAM Review **48** (2006), 504–536, doi:10.1137/S0036144504445765.
2. F. J. Simons and F. A. Dahlen, *Spherical Slepian functions and the polar gap in geodesy*, arXiv:math/0603271v1 (posted 2006-03-11); Geophysical Journal International **166** (2006), 1039–1061, doi:10.1111/j.1365-246X.2006.03065.x.
3. A. P. Bates, Z. Khalid, and R. A. Kennedy, *Efficient computation of Slepian functions for arbitrary regions on the sphere*, arXiv:1608.05479 (initial submission 2016-08-19); IEEE Transactions on Signal Processing **65** (2017), 4379–4393, doi:10.1109/TSP.2017.2712122.
