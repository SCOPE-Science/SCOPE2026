# Sharp mean-width balancing and parity fluctuation laws for block-check codeword polytopes

## Finding

Let \(k\ge1\), \(m_j\ge3\), \(N=\sum_{j=1}^{k}m_j\), and let the sets \(B_j\) partition the \(N\) coordinates, with \(|B_j|=m_j\). Define the block-check codeword polytope
\[
 Q_{\mathbf m}=\operatorname{conv}\left\{\sigma\in\{-1,1\}^{N}:\prod_{i\in B_j}\sigma_i=1\ \text{for all }j\right\}.
\]
Write \(w(K)=\mathbb E_{U\in S^{N-1}}[h_K(U)+h_K(-U)]\) for intrinsic Euclidean mean width (uniform spherical \(U\)). Set
\[
 c=\sqrt{2/\pi},\qquad a_N=\sqrt2\,\Gamma((N+1)/2)/\Gamma(N/2),\qquad
 p_m=\int_0^\infty\operatorname{erfc}(t/\sqrt2)^m\,dt.
\]
The exact formula is
\[
 \boxed{w(Q_{\mathbf m})=\frac{2}{a_N}\left(Nc-\sum_{j=1}^kp_{m_j}\right).}
\]
For fixed \(N,k\), the block sizes that **uniquely maximize** width, up to permutation, differ by at most one. Those that **uniquely minimize** width, up to permutation, are \((N-3(k-1),3,\ldots,3)\). For \(k=1\) this comparison is vacuous. All these polytopes nonetheless have the same vertex count \(2^{N-k}\), vertex radius \(\sqrt N\), isotropic vertex covariance \(I_N\), and unique Löwner ellipsoid \(\sqrt N B_2^N\).

There is also an exact **directional parity law**. For independent standard Gaussian coordinates \(G_i\), put \(R=\lVert G\rVert_2\), \(U=G/R\), \(M_j=\min_{i\in B_j}|G_i|\), and \(B_j'=\mathbf1_{\{\prod_{i\in B_j}\operatorname{sgn}G_i=-1\}}\). The variables \(B_j'\) are independent fair Bernoulli variables independent of all \(M_j\). If \(\Delta(U)\) is the directional-width loss relative to \([-1,1]^N\), then almost surely
\[
 \boxed{R\Delta(U)=\sum_{j:m_j\text{ odd}}2M_j+\sum_{j:m_j\text{ even}}4B_j'M_j.}
\]
Consequently \(\Pr\{\Delta(U)=0\}=2^{-k}\) if every block size is even, and zero otherwise.

For equal-size blocks \(m_j=m\), \(N=km\), and \(m\to\infty\), the following consequences distinguish two scales. With fixed \(k\), for independent \(E_j\sim\mathrm{Exp}(c)\) and independent fair Bernoulli \(B_j'\), along the indicated parity subsequences,
\[
 m\sqrt N\,\Delta(U)\ \Longrightarrow\
 \begin{cases}
 2\sum_{j=1}^kE_j,&m\ \text{odd},\\
 4\sum_{j=1}^kB_j'E_j,&m\ \text{even}.
 \end{cases}
\]
If \(k\to\infty\) and \(m\to\infty\), then, again along odd and even \(m\) subsequences respectively,
\[
 \frac{m\sqrt N\,\Delta(U)-2km p_m}{\sqrt{k}}
 \ \Longrightarrow\ \mathcal N(0,2\pi)
 \quad\text{or}\quad\mathcal N(0,6\pi).
\]
For all such equal-block sequences the mean-width deficit satisfies
\[
 \boxed{w([-1,1]^N)-w(Q_{m^k})\sim \sqrt{2\pi}\frac{k^2}{N^{3/2}}.}
\]
Thus the absolute difference first remains of constant order when \(k\) is of order \(N^{3/4}\) (necessarily with \(m\to\infty\)).

## Assumptions and scope

The parity checks act on **disjoint** blocks. Each \(m_j\ge3\), which ensures full dimensionality and identity vertex covariance. The support is measured in the original Euclidean coordinates, with sign vertices \(\pm1\); changing to zero-one coordinates scales every width by \(1/2\). All Gaussian random variables above are independent unless explicitly coupled through \(R\). The limiting normal laws use variance parametrization, not standard deviation.

## Proof

**1. Vertices and enclosing ellipsoid.** Each even-sign vector is a vertex of the ambient cube and therefore of its convex subpolytope, and the number is \(2^{N-k}\). On a block of size at least three, an even-sign-uniform random vector has independent fair values in any one or two prescribed coordinates: specifying one or two coordinates leaves respectively \(2^{m-2}\) or \(2^{m-3}\) choices. Thus the uniform vertex distribution has mean zero and covariance \(I_N\), so the polytope is full-dimensional. Every vertex has squared norm \(N\). If an ellipsoid \(\{x:(x-z)^TA^{-1}(x-z)\le1\}\) contains these vertices, averaging their defining inequalities gives \(\operatorname{tr}(A^{-1})+z^TA^{-1}z\le1\). Arithmetic-geometric mean applied to the eigenvalues of \(A^{-1}\) implies \(\det A\ge N^N\), with equality only at \(z=0,A=NI_N\). Since the Euclidean ball \(\sqrt N B_2^N\) contains every vertex, it is the unique minimum-volume enclosing ellipsoid.

**2. The exact Gaussian support deficit.** For a Gaussian direction with no vanishing coordinate, the maximizing sign vector in a block, without parity, is its sign pattern. If its sign product is negative, the unique least costly way to restore positive product is to reverse the sign at an index of minimum absolute coordinate. This incurs support loss \(2M_j\). The signs of independent Gaussians are independent fair signs and are independent of the absolute values; hence each block has a fair independent parity mismatch indicator. Since \(G=RU\) with \(R\) independent of the uniform unit vector \(U\), and \(\mathbb ER=a_N\), taking the expectation of the support identities yields \(\mathbb Eh_Q(G)=Nc-\sum p_{m_j}\). The symmetry of the Gaussian law implies \(\mathbb E[h_Q(U)+h_Q(-U)]=2\mathbb Eh_Q(G)/a_N\). The tail-integral formula for a nonnegative random variable gives \(p_m=\int_0^\infty\Pr(M_m>t)\,dt\), proving the claimed exact expression.

**3. Strict balancing.** Let \(q(t)=\operatorname{erfc}(t/\sqrt2)\). For all integers \(r\ge2\),
\[
 p_{r-1}-2p_r+p_{r+1}=\int_0^\infty q(t)^{r-1}(1-q(t))^2dt>0.
\]
The integral is strictly positive since \(0<q(t)<1\) for positive finite \(t\). Hence \(p_m\) is strictly convex as a function of the integer block size. Replacing a pair \((a,b)\), \(a\ge b+2\), by \((a-1,b+1)\) strictly decreases \(p_a+p_b\), so it strictly increases the mean width. Repeating proves the unique balanced maximizer. Conversely, transferring one coordinate from a block greater than three to a block no smaller than itself increases the sum of the \(p_m\), attaining the unique \(3,\ldots,3,N-3(k-1)\) minimum.

**4. Directional parity.** Passing from \(G\) to \(-G\) flips every sign in a block. For an odd block, the sign product flips, so exactly one of \(G\) and \(-G\) incurs loss \(2M_j\). For an even block the sign product does not flip, so both directions incur loss \(2M_j\) precisely when the block has odd sign product. Adding support deficits for opposite directions proves the exact random formula. Since \(M_j>0\) almost surely, the zero-loss atom follows.

**5. Limit laws and visible threshold.** The minimum half-normal variable has survival function \(q(t)^m\). Taylor expansion \(q(t)=1-ct+O(t^3)\) at zero shows \(\Pr(mM_m>s)=q(s/m)^m\to e^{-cs}\). A uniform exponential envelope on \(s\le m\) and Gaussian tail outside this range establish convergence of moments of any fixed order. In particular \(mp_m\to1/c\) and \(m^2\mathbb E M_m^2\to2/c^2\). Slutsky's theorem with \(R/\sqrt N\to1\) gives both fixed-\(k\) distributional limits. For growing \(k\), the independent block contributions \(2mM_m\) (odd) and \(4B_j'mM_m\) (even) have means \(2mp_m\), uniformly bounded third centered moments, and limiting variances \(4/c^2=2\pi\) and \(12/c^2=6\pi\). Lyapunov's triangular-array central limit theorem applies. Multiplication by \(\sqrt N/R=1+O_{\mathbb P}(N^{-1/2})\) changes the normalized sum by \(O_{\mathbb P}(\sqrt{k/N})=o_{\mathbb P}(1)\), because \(m=N/k\to\infty\). Finally \(a_N\sim\sqrt N\) and \(p_m\sim1/(cm)\), giving the stated width asymptotic and its \(N^{3/4}\) crossover.

## Verification

The accompanying stand-alone `CHECK.py` enumerates all feasible vertices in eleven profiles (sizes three through twelve), checks identity vertex covariance, verifies the greedy Gaussian-support and opposite-direction width-loss identities on 176 independent test directions using integer arithmetic, and numerically checks positivity of discrete curvature, a nine-dimensional balancing comparison, and the asymptotic first/second moments of minimum half-normal variables. All assertions pass. The universal and asymptotic assertions follow from the proof, not from finite numerical tests.

For \(N=9,k=2\), the profiles \((4,5)\) and \((3,6)\) have equal vertex counts and equal enclosing balls but mean widths approximately \(4.5944052212\) and \(4.5665987079\), respectively. The numerical integrals are reproducible in `CHECK.py` with Simpson quadrature.

## Relationship to prior work

The parity-polytope construction and its linear descriptions are classical; see Jeroslow's 1975 inequalities and Ermel--Walter's 2018 study of parity polytopes and ordered binary blocks. Their primary article develops extended formulations, outer descriptions, separation, and integer-programming applications, not the present disjoint-check Euclidean width optimization. Del Pia--Khajavirad's 2023 study concerns polyhedral formulations of general pseudo-Boolean optimization, not the quantitative Gaussian width and fluctuation laws here. A published mathematical record on the John/Löwner ellipsoids of a **single** type-D spin polytope supplies related radii but neither the disjoint-block balancing theorem nor its mean-width and parity limit laws. The derived partition extremizers and parity-dependent fluctuation laws are the claim assessed here; elementary parity-polytope support optimization and existing single-block ellipsoid facts are not claimed to be new.

## Limitations

Only disjoint even-sign constraints of block size at least three are covered; overlapping parity checks, other codeword coordinate embeddings, and non-Gaussian angular distributions are not classified. The transition concerns the **absolute unscaled mean-width deficit**, not a claim of a nonzero relative-width loss. The novelty search did not yield a covering statement in inspected primary literature or related indexed mathematical records, but equivalent results under coding-theoretic or type-D product language remain possible. This is a mathematical argument with computational cross-checks, not independent certification.

## References

1. D. Ermel and M. Walter, *Parity Polytopes and Binarization*, arXiv:1803.10561, first posted 2018-03-28. https://arxiv.org/abs/1803.10561.
2. R. G. Jeroslow, *On defining sets of vertices of the hypercube by linear inequalities*, Discrete Mathematics (1975); cited as the classical even-parity formulation in Ermel--Walter.
3. A. Del Pia and A. Khajavirad, *The pseudo-Boolean polytope and polynomial-size extended formulations for binary polynomial optimization*, arXiv:2309.08693, first posted 2023-09-15. https://arxiv.org/abs/2309.08693.
4. *Exact John–Löwner ellipsoids of type-D spin weight polytopes*, publicly indexed mathematical research record, 2026-10-11, identifier `15c85fee505a` (background comparison only; not a source of the theorem proved here).
