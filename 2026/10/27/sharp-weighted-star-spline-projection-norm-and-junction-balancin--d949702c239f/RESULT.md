# Sharp weighted-star spline projection norm and junction balancing

## Finding
Let \(m\geq3\). Consider a compact metric star with a central junction and \(m\) closed arms of positive lengths \(\ell_1,\ldots,\ell_m\), meeting only at the junction. On arm \(i\), equip arclength with the strictly positive constant density \(w_i\). Put \(\mu_i=w_i\ell_i\), \(M=\sum_{i=1}^{m}\mu_i\), and \(\mu_*=\min_i\mu_i\). Let \(V\) be the space of functions continuous at the junction and affine on each arm, and let \(P:L^2(\mu)\to V\) be the orthogonal projection. Its extension from \(L^\infty(\mu)\) to continuous representatives satisfies the exact sharp formula
\[
\boxed{\|P\|_{L^\infty(\mu)\to L^\infty(\mu)}=\frac73-\frac{4\mu_*}{3(M+\mu_*)}.}
\]
The norm is realized at precisely the terminal vertices of arms of minimal \(\mu_i\); real sign-valued input functions attain the norm.

For every fixed \(m\ge3\), the complete sharp range over all positive arm lengths and densities is
\[
\boxed{\frac73-\frac4{3(m+1)}\le \|P\|_{\infty\to\infty}<\frac73.}
\]
The lower bound is attained if and only if the weighted arm masses are all equal. The upper endpoint is not attained for any positive data; it is approached by letting the weighted mass of one arm tend to zero while at least one other arm retains positive mass. Moreover, even the balanced minimum tends to \(7/3\) as the junction valence tends to infinity. In particular, the unweighted three-arm balanced star has norm exactly \(2\).

## Assumptions and scope
The metric star is the quotient of the intervals \([0,\ell_i]\) with all origins identified; different terminal vertices remain distinct. The probability normalization of the measure does not matter. Each \(w_i\) is constant and positive on its entire arm, and the norm on the input uses the measure \(w_i\,\mathrm{d}x\) there. The output takes its unique continuous, edgewise-affine representative. Both real and complex scalar inputs are allowed. Only one affine finite element per arm is considered, and the theorem is stated for junction valence at least three.

## Proof
**1. Basis and exact inverse.** Write \(s=x/\ell_j\in[0,1]\) on arm \(j\). The nodal hat functions are \(\phi_0=1-s\) on every arm and, for \(1\le i\le m\), \(\phi_i=s\) on arm \(i\) and zero on all other arms. Their Gram matrix \(G_{ab}=\int\phi_a\phi_b\,\mathrm{d}\mu\) has nonzero entries
\[
G_{00}=M/3,\qquad G_{0i}=G_{i0}=\mu_i/6,\qquad G_{ii}=\mu_i/3.
\]
The matrix is strictly positive definite because the hats form a linearly independent basis and every weight is positive. Eliminating the diagonal leaf block, the Schur complement equals \(M/4\). Thus its inverse \(H=G^{-1}\) satisfies
\[
H_{00}=4/M,\qquad H_{0i}=H_{i0}=-2/M,\qquad H_{ij}=3\delta_{ij}/\mu_i+1/M
\quad(1\le i,j\le m).
\]
These identities can also be verified directly by multiplication.

**2. Reproducing kernels and reduction to nodes.** The projection is an integral operator with continuous-output reproducing kernel
\[
K(x,y)=\sum_{a,b=0}^{m}\phi_a(x)H_{ab}\phi_b(y).
\]
For any fixed \(x\), the maximum of \(|Pf(x)|\) over \(\|f\|_\infty\le1\) is exactly \(\int|K(x,y)|\,\mathrm{d}\mu(y)\), attained for the real function \(f(y)=\operatorname{sgn}K(x,y)\). Along any arm the kernel is affine in \(x\); convexity of the absolute value therefore bounds its integrated absolute value by the larger of the two endpoint rows. Thus the norm is the largest nodal kernel integral.

**3. The central row.** Evaluating the kernel at the junction gives, on every arm,
\[
K(0,y)=\frac{4-6s}{M}.
\]
Its absolute integral is
\[
\sum_{j=1}^{m}\mu_j\int_0^1\frac{|4-6s|}{M}\,\mathrm{d}s=\frac53.
\]

**4. The leaf rows.** At the terminal vertex \(v_i\), the kernel on arm \(j\) is
\[
K(v_i,y)=\frac{-2+3s}{M}+\mathbf1_{\{j=i\}}\frac{3s}{\mu_i}.
\]
For \(j\ne i\), the unique sign change is at \(s=2/3\) and \(\int_0^1|-2+3s|\,\mathrm{d}s=5/6\). On arm \(i\), the sign change is at
\[
s_i=\frac{2\mu_i}{3(M+\mu_i)}\in(0,1).
\]
Integration of the two elementary triangles, including the weights, yields
\[
\begin{aligned}
\int|K(v_i,y)|\,\mathrm{d}\mu(y)
&=\frac{5(M-\mu_i)}{6M}
 +\frac32-\frac{\mu_i}{2M}
 +\frac{4\mu_i^2}{3M(M+\mu_i)}\\
&=\frac73-\frac{4\mu_i}{3(M+\mu_i)}.
\end{aligned}
\]
Every \(\mu_i<M\) because \(m\ge3\) and all arm masses are positive, so each leaf row is strictly larger than \(5/3\). Since \(u\mapsto u/(M+u)\) strictly increases, exactly the leaves with \(\mu_i=\mu_*\) maximize the nodal integral. In fact no interior point of an arm maximizes: for a point strictly between its center and its leaf, the central and leaf kernels have opposite signs on a positive-measure portion of any other arm, giving strict inequality in the convexity step.

**5. Extremal range and mass balancing.** Since \(\mu_*\le M/m\), with equality exactly for \(\mu_1=\cdots=\mu_m\), the formula gives the displayed optimal lower bound and its unique balancing condition. Positivity of \(\mu_*\) proves the strict upper bound; sending one mass to zero proves that its supremum \(7/3\) is sharp. For balanced masses \(\mu_i=M/m\), the norm equals \(7/3-4/[3(m+1)]\), which tends to \(7/3\) as \(m\to\infty\).

## Verification
The companion self-contained script `check_star.py` independently assembles the nodal Gram matrix from each weighted arm, inverts it by rational Gaussian elimination, integrates every absolute affine kernel row by exact rational triangle areas, and compares these independently computed row sums to the formula. It passed 225 rational input instances of valence one through nine (the lower-valence cases are consistency checks), as well as balanced and degenerating families. These finite checks test the algebra; they do not substitute for the exact proof for every positive real parameter.

For a direct hand check, if the three arm masses are equal, then \(\mu_*=M/3\), and the formula gives \(\|P\|=2\). If three masses are \((\varepsilon,1,1)\), \(\varepsilon>0\) small, then
\[
\|P\|=\frac73-\frac{4\varepsilon}{3(2+2\varepsilon)}\longrightarrow\frac73.
\]
For any minimizing leaf, the explicit sign pattern of its kernel supplies a norm-attaining bounded input.

## Relationship to prior work
Classical linear-spline projection theory studies intervals and mesh-independent bounds; see Crouzeix--Thomée, Kayumov, and Passenbrunner--Shadrin. Passenbrunner subsequently established mesh-independent boundedness for periodic splines. Those interval and circle geometries have no junction of valence at least three. The two-arm version of the above kernel calculation coincides with the elementary two-cell interval formula and is **not** asserted here as new. The present result treats all higher-valence star junctions with arbitrary positive, edgewise constant densities, gives their exact sharp norm, and completely classifies the mass-balancing minimizers and sharp nonattainment envelope.

## Limitations
The theorem does not cover multiple finite elements along one arm, nonconstant densities on an arm, non-star networks with cycles or several junctions, or other polynomial degrees. The norm is the supremum endpoint operator norm, not a Sobolev or derivative norm. The historical 1997 Ciesielski--Kamont article on interval splines was identifiable but its complete primary text was not available in this comparison; an unindexed network-specific precursor cannot be ruled out by search results alone. No independent scientific audit is claimed here.

## References
- A. Kayumov, *Least-squares approximation by second-order L-splines*, public arXiv version of 30 August 2004, arXiv:math/0408418. https://arxiv.org/abs/math/0408418
- M. Passenbrunner and A. Shadrin, *On almost everywhere convergence of orthogonal spline projections with arbitrary knots*, public arXiv version of 22 August 2013, arXiv:1308.4824. https://arxiv.org/abs/1308.4824
- M. Passenbrunner, *Orthogonal projectors onto spaces of periodic splines*, public arXiv version of 24 August 2016, arXiv:1608.06720. https://arxiv.org/abs/1608.06720
- M. Crouzeix and V. Thomée, *The stability in \(L^p\) and \(W^{1,p}\) of the \(L^2\)-projection onto finite element function spaces*, *Mathematics of Computation* 48 (1987), 521--532, doi:10.1090/S0025-5718-1987-0878688-2.
- Z. Ciesielski and A. Kamont, *Projections onto piecewise linear functions*, *Functional Approximation, Commentaries in Mathematics* 25 (1997), 129--143 (bibliographic record; full text unavailable in this review).
