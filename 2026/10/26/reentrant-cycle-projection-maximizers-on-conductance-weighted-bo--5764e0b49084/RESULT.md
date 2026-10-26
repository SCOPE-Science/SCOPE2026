# Reentrant cycle-projection maximizers on conductance-weighted Boolean cubes

## Finding

Let \(d\ge 2\), and give every coordinate-\(i\) edge of the Boolean cube \(\{0,1\}^d\) the same positive electrical conductance \(w_i\). Orient the edges arbitrarily, let \(D\) have the corresponding signed vertex-incidence columns multiplied by \(\sqrt{w_i}\), and define the real Euclidean-orthogonal edge cut and cycle projections
\[
Q=D^{\mathsf T}(DD^{\mathsf T})^+D,\qquad P=I-Q.
\]
For every direction \(i\), put
\[
q_i=1+\sum_{j\ne i}\frac{\sqrt{w_iw_j}}{w_i+w_j},\qquad
r_i=\frac1{2^{d-1}}\sum_{\substack{S\subseteq\{1,\ldots,d\}\\i\in S}}\frac{w_i}{\sum_{j\in S}w_j},\qquad
p_i=1+q_i-2r_i.
\]
Every edge column in direction \(i\) has absolute cut sum \(q_i\), cut diagonal \(r_i\), and absolute cycle sum \(p_i\). Consequently,
\[
\|Q\|_{1\to1}=\|Q\|_{\infty\to\infty}=\max_i q_i,
\qquad
\|P\|_{1\to1}=\|P\|_{\infty\to\infty}=\max_i p_i.
\]
For the geometric profile \(w_i=\rho^{2(i-1)}\), \(\rho>1\), the cut-projection norm is attained precisely at the central coordinate(s): coordinate \((d+1)/2\) if \(d\) is odd, and coordinates \(d/2,d/2+1\) if \(d\) is even.

For \(d=4\), the cycle-projection maximizing direction has a *reentrant* phase diagram. There are exactly two parameters \(\alpha,\beta\), with
\[
\frac{181}{100}<\alpha<\frac{183}{100},\qquad
\frac{321}{100}<\beta<\frac{323}{100},
\]
such that the maximizing direction is uniquely direction \(1\) for \(1<\rho<\alpha\) and \(\rho>\beta\), and uniquely direction \(2\) for \(\alpha<\rho<\beta\). Exactly directions \(1,2\) tie at either threshold. In contrast, the cut norm always maximizes in directions \(2,3\). The transition parameters are the only real roots above \(1\) of the explicit degree-24 polynomial in the proof.

## Assumptions and scope

Conductance means the coefficient in the weighted graph Laplacian, *not* an edge length in a shortest-path metric. The square-root conductance in \(D\) is essential: \(Q\) is the symmetric transfer-current (orthogonal) projection in the standard coordinate Euclidean edge space. The endpoint Banach norms are those of this particular matrix acting on real coordinate \(\ell_1\) and \(\ell_\infty\). There is no assertion that these are minimum norms among all projections onto the corresponding subspaces. All conductances are strictly positive. In the geometric specialization, coordinates are indexed starting at \(1\), so directions of increasing conductance have increasing indices.

## Proof

**1. Heat-kernel formula and signs.** Write \(e_i\) for the \(i\)-th coordinate vector and orient the distinguished edge from \(0\) to \(e_i\). The graph Laplacian is the sum of independent two-point Laplacians. Its heat kernel is therefore
\[
K_t(x,y)=2^{-d}\prod_{k=1}^d\bigl(1+(-1)^{x_k+y_k}e^{-2w_kt}\bigr).
\]
Because the vector \(\delta_0-\delta_{e_i}\) has zero sum, its potential may be obtained by integrating the heat kernel:
\[
h_i(x)=\sqrt{w_i}\,2^{1-d}(-1)^{x_i}
\int_0^\infty e^{-2w_it}
\prod_{k\ne i}\bigl(1+(-1)^{x_k}e^{-2w_kt}\bigr)\,dt.
\]
All product factors in the integrand are strictly positive for \(t>0\). For an edge \(f=(x,x+e_j)\), oriented with \(x_j=0\), its projector coefficient is \(Q_{fe}=\sqrt{w_j}\,[h_i(x)-h_i(x+e_j)]\). If \(j=i\), this coefficient is positive. If \(j\ne i\), its sign is \((-1)^{x_i}\), independently of the other coordinates. Thus *all* absolute values can be removed with explicitly known signs.

**2. Absolute column sums.** For the parallel direction \(i\), summing the coefficients over the \(2^{d-1}\) edges cancels all product factors by the binomial identity \(\sum_{\epsilon\in\{0,1\}}(1+(-1)^\epsilon z)=2\). The sum is
\[
2w_i\int_0^\infty e^{-2w_it}\,dt=1.
\]
For any transverse direction \(j\ne i\), the same sum, now of absolute values, gives
\[
2\sqrt{w_iw_j}\int_0^\infty e^{-2(w_i+w_j)t}\,dt
=\frac{\sqrt{w_iw_j}}{w_i+w_j}.
\]
This proves the claimed \(q_i\). Cube translations and coordinate reflections (which respect direction conductances) give the same column sum at every edge of a fixed direction.

**3. Diagonal and complementary projection.** The coefficient at the distinguished edge is
\[
Q_{ee}=w_i2^{2-d}\int_0^\infty e^{-2w_it}
\prod_{k\ne i}(1+e^{-2w_kt})\,dt.
\]
Expanding the finite product and integrating each exponential gives exactly \(r_i\) as stated. Since \(Q\) is an orthogonal projection, \(0\le r_i\le1\); the diagonal of \(I-Q\) is \(1-r_i\), while every other entry of its \(e\)-th column is the negative of the corresponding cut entry. Hence the cycle column has absolute sum \(p_i=1+q_i-2r_i\). Since both matrices are symmetric, maximum absolute row and column sums coincide.

**4. The geometric cut norm.** Set
\[
a_h=\frac{\rho^h}{1+\rho^{2h}}=\frac1{\rho^h+\rho^{-h}}\quad(h\ge0).
\]
For \(\rho>1\), \(a_h\) strictly decreases as the integer \(h\ge0\) increases. In particular,
\[
q_i=\frac12+\sum_{j=1}^d a_{|i-j|},\qquad
q_{i+1}-q_i=a_i-a_{d-i}.
\]
The difference is positive for \(i<d/2\), negative for \(i>d/2\), and zero only when \(i=d/2\). This proves the exact central-direction maximizer statement in every dimension.

**5. Diagonal ordering and the four-dimensional reduction.** For any two directions \(i,j\) with \(w_i<w_j\), the diagonal formula implies \(r_i<r_j\). Indeed, pairing subsets differing only by the presence of \(i,j\) and writing \(s\ge0\) for the sum of the conductances in the remaining subset gives
\[
r_j-r_i=2^{1-d}\sum_{T\subseteq[d]\setminus\{i,j\}}
\left(\frac{w_j}{w_j+s}-\frac{w_i}{w_i+s}
+\frac{w_j-w_i}{w_i+w_j+s}\right)>0.
\]
For \(d=4\) with geometric conductances, symmetry gives \(q_1=q_4<q_2=q_3\), whereas \(r_1<r_2<r_3<r_4\). Thus \(p_1>p_4\) and \(p_2>p_3\): only directions \(1\) and \(2\) can maximize the cycle norm.

**6. Exact two-switch certificate.** Direct substitution of \(w_i=\rho^{2(i-1)}\) into \(p_1-p_2\), followed by rational simplification, yields
\[
p_1-p_2=\frac{(\rho^2-1)F(\rho)}{H(\rho)},
\]
where
\[
\begin{aligned}
F(t)={}&t^{24}-4t^{23}+3t^{22}-4t^{21}+9t^{20}-8t^{19}
+15t^{18}-12t^{17}+24t^{16}-4t^{15}\\
&+33t^{14}-8t^{13}+33t^{12}+8t^{11}+38t^{10}+4t^9
+27t^8+12t^7\\
&+24t^6+8t^5+14t^4+4t^3+6t^2+4t+4,
\end{aligned}
\]
and
\[
H(t)=4(t^2+1)(t^4+1)(t^2-t+1)(t^2+t+1)
(t^4-t^2+1)(t^6+t^2+1)(t^6+t^4+1).
\]
The denominator \(H(t)\) is strictly positive for every \(t>1\). A rational-polynomial Sturm computation (reproduced by the standalone checker) gives the following exact sign-variation counts for the Sturm sequence of \(F\):
\[
\begin{array}{c|rrrrrrrr}
t&1&181/100&183/100&2&321/100&323/100&4&+\infty\\\hline
V(t)&13&13&12&12&12&11&11&11
\end{array}
\]
The exact polynomial identity is checked by clearing rational denominators, and the sequence uses \(F,F'\) followed by negative Euclidean remainders. These variations show precisely two distinct roots in \((1,\infty)\), one in each asserted rational interval; \(\gcd(F,F')=1\) confirms simplicity. Finally \(F(1)=231>0\), \(F(2)=-2860764<0\), and \(F(4)=43813323124596>0\). Therefore \(p_1-p_2\) has signs \(+,-,+\) across the three intervals, with equality exactly at the two roots. This completes the phase classification.

## Verification

Run `python check.py` with SymPy 1.14.0. The standalone code rebuilds weighted incidence matrices and exact grounded-Laplacian inverses on eight cube configurations (all their columns), compares every absolute column sum and diagonal with the formulas, symbolically verifies the degree-24 rational factorization, and computes Sturm variations using exact rational arithmetic. Its recorded successful run was:

`ANISOTROPIC_CUBE_EXACT_OK graphs=8 grounded_columns=188 sturm_variations=[13, 13, 12, 12, 12, 11, 11, 11] phase_roots=2`

The finite graph checks are corroboration; the heat-kernel derivation covers every real positive conductance tuple and every integer \(d\ge2\). The Sturm computation is an exact finite certificate for the two-transition statement and is independently reconstructible from the polynomial and algorithm.

## Relationship to prior work

Dilworth, Kutzarova, and Ostrovskii (2023, arXiv:2305.12582v1), Theorem 45 and Corollary 60, give the unweighted Hamming-cube endpoint norms. Specializing the present formulas to \(w_1=\cdots=w_d\) reproduces their cut value \((d+1)/2\) and the corresponding cycle value, but their calculations do not provide this conductance-dependent direction law or the reentrant phase classification.

Gurel-Gurevich, Nachmias, and Sachdeva (2026, arXiv:2605.24130v1), Theorem 1.3, explicitly study the same symmetric weighted transfer-current projector and bound the spectral norm of its entrywise absolute value on arbitrary weighted graphs by \(2\log |V|\). That universal bound neither determines the exact coordinate \(\ell_1\)/\(\ell_\infty\) norms of a weighted cube nor classifies maximizing directions. The present result does not improve their global spectral-norm estimate.

## Limitations

The norm statements concern the canonical square-root-conductance orthogonal cut and cycle projections, not physical-current coordinates without symmetrization, arbitrary nonorthogonal projections, minimum projection constants, conductances varying among edges of the same direction, or intermediate \(\ell_p\) norms. The exact cycle-maximizer classification outside dimension four is not asserted; its norm remains explicitly determined by the finite maximum formula for every dimension. Published equivalents not found by literature searches remain a possibility; novelty has not been independently audited.

## References

1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1, first posted 21 May 2023, Sections 2.6–2.7, especially Theorem 45 and Corollary 60. https://arxiv.org/abs/2305.12582
2. O. Gurel-Gurevich, A. Nachmias and S. Sachdeva, *A Tight Bound on Localization of Electrical Flows*, arXiv:2605.24130v1, first posted 22 May 2026, Section 1.1, especially Theorem 1.3. https://arxiv.org/abs/2605.24130
