# Sharp differentiability strata of radial mean bodies of parallelotopes

## Finding

For every integer \(n\ge3\), every real \(p>-1\), and the cube \(Q=[-1,1]^n\), the Minkowski gauge \(G_p(v)=\|v\|_{R_pQ}\) has a complete differentiability stratification on \(\mathbb R^n\setminus\{0\}\):

1. On each open coordinate orthant, \(G_p\) is locally \(C^{2,1}\) (twice continuously differentiable with locally Lipschitz Hessian). It is real analytic at a vector whose coordinates are all nonzero and whose largest absolute coordinate is unique.
2. If any coordinate of \(v\ne0\) vanishes, \(G_p\) is not differentiable at \(v\).
3. If all coordinates are nonzero and exactly \(m\ge2\) absolute coordinates equal the largest magnitude, \(G_p\) has a Peano Taylor polynomial of degree \(m\) at \(v\), with a remainder \(o(\|h\|^m)\), but admits no Peano Taylor polynomial of degree \(m+1\). Thus, on a generic two-way maximum-tie hypersurface, it is \(C^2\) but not \(C^3\), and the third-order failure is sharp.

The nonzero leading coefficient in the last assertion is explicit. After a signed-coordinate permutation write the point as \(v_0=(a,\ldots,a,b_{m+1},\ldots,b_n)\), where \(a>0\), the first \(m\) entries equal \(a\), and \(0<b_j<a\). Put \(M_p(v_0)=\mathbb E S_{v_0}^p\) for \(p\ne0\), \(M_0(v_0)=1\), and \(S_v=\min_i U_i/|v_i|\), with independent uniform \(U_i\) on \([0,1]\). Let \(J_p(h)=\log G_p(v_0+h e_1)\), and let \(J_p^{\rm an}(h)\) be the real-analytic continuation obtained by holding the survival-integral cutoff fixed at \(1/a\). Then \(J_p(h)=J_p^{\rm an}(h)\) for sufficiently small \(h\le0\), whereas

\[
J_p(h)-J_p^{\rm an}(h)=-\frac{a^{-p-m-1}}{m(m+1)M_p(v_0)}\prod_{j=m+1}^n\!\left(1-\frac{b_j}{a}\right)h^{m+1}+O(h^{m+2})\quad(h\downarrow0).
\]

This coefficient is strictly negative for every \(p>-1\), including \(p=0\) with the stated convention. The classification transfers by invertible affine maps to radial mean bodies of all full-dimensional parallelotopes. The higher-order Peano assertion at \(m\ge3\) does **not** mean that the gauge is \(C^m\) on a neighborhood: two-way ties occur arbitrarily near such a point.

## Assumptions and scope

The radial \(p\)-mean body is defined by the Gardner--Zhang convention \(\rho_{R_pK}(u)=\big(\operatorname{Vol}(K)^{-1}\int_K\rho_{K-x}(u)^p\,dx\big)^{1/p}\) for \(p>-1\), \(p\ne0\), with the exponential of the mean logarithm at \(p=0\). The gauge is \(G_p(v)=1/\rho_{R_pQ}(v)\) for nonzero \(v\), using the degree \(-1\) extension of a radial function to nonunit arguments. The exponent \(p\) is finite. A Peano Taylor polynomial of degree \(k\) means a polynomial of total degree at most \(k\) whose difference from the function is \(o(\|h\|^k)\) as \(h\to0\); this is a pointwise statement, not neighborhood \(C^k\) regularity.

Set \(a_i=|v_i|\), \(a=\max_i a_i\), \(\tau=1/a\), and \(r_i=a_i/a\), with a zero-weight coordinate ignored in \(S_v\). Let \(e_k(r_1,\ldots,r_n)\) denote the elementary symmetric polynomial of degree \(k\). Then a computationally finite formula is

\[
G_p(v)=\frac a2\left[1+p\sum_{k=1}^n\frac{(-1)^ke_k(r_1,\ldots,r_n)}{p+k}\right]^{-1/p}\quad(p\ne0),
\]

and

\[
G_0(v)=\frac a2\exp\left[-\sum_{k=1}^n\frac{(-1)^ke_k(r_1,\ldots,r_n)}{k}\right].
\]

All denominators are positive because \(p>-1\), and the power bracket is positive by its probabilistic meaning. These expressions are exact for every \(n\ge3\) and every \(v\ne0\).

## Proof

**1. Exit-distance distribution and normalization.** Choose \(X\) uniformly in \(Q\). In direction \(v\), the distance to the boundary of \(Q-X\) is \(2S_v\), where for each nonzero \(v_i\) the independent random variable \(U_i=(1-\operatorname{sgn}(v_i)X_i)/2\) is uniform on \([0,1]\); indices with \(v_i=0\) are omitted. Consequently

\[
\Pr(S_v>t)=P_v(t)=\prod_{i=1}^n(1-a_it)\qquad(0\le t\le\tau),
\]

and the survival function is zero beyond \(\tau\). For \(p>-1\), \(p\ne0\), integration by parts after subtracting the constant term (to ensure integrability also when \(p<0\)) gives

\[
M_p(v)=\tau^p+p\int_0^\tau t^{p-1}\big(P_v(t)-1\big)\,dt.
\]

For \(p=0\), the same computation gives \(\mathbb E\log S_v=\log\tau+\int_0^\tau(P_v(t)-1)t^{-1}\,dt\). Expanding the finite product yields the formulas in the previous section. By definition, \(\log G_p(v)=-\log2-\log M_p(v)/p\) when \(p\ne0\), and \(\log G_0(v)=-\log2-\mathbb E\log S_v\). In a region of fixed nonzero coordinate signs and unique maximizing coordinate, all the formulas are real analytic.

**2. Exact nonsmoothness on coordinate hyperplanes.** If \(a_j=0\), varying only \(v_j\) keeps \(\tau\) fixed for sufficiently small perturbations. Differentiation with respect to the right-hand variable \(a_j=|v_j|\) gives

\[
\frac{\partial\log G_p}{\partial a_j}=\frac{\int_0^\tau t^p\prod_{i\ne j}(1-a_it)\,dt}{M_p(v)}>0\quad(p\ne0),
\]

while at \(p=0\) the same expression holds with \(t^p=1\) and denominator \(1\). Both integrals are finite and strictly positive for \(p>-1\). Because changing the sign of \(v_j\) changes \(a_j\) from \(v_j\) to \(-v_j\), the opposite one-sided derivatives disagree. Thus the gauge is not differentiable wherever a coordinate is zero.

**3. Boundary layer at an \(m\)-fold maximum.** Work in a fixed orthant. Near \(v_0\), let \(\delta\) bound the coordinate perturbation. Fixing the upper limit of the moment integral at \(1/a\) gives a real-analytic function in all perturbed coordinates near \(v_0\). The actual upper limit differs by at most \(O(\delta)\); throughout this short interval all \(m\) factors associated with maximal coordinates are \(O(\delta)\). Their product is \(O(\delta^m)\), and the remaining factors and integration weights are bounded. The difference between actual and analytically continued moments is therefore \(O(\delta^{m+1})\), also at \(p=0\) using the logarithmic integral. Smooth changes of variables from moment to log gauge preserve that estimate. Hence the Taylor polynomial of the analytic continuation through order \(m\) is a Peano \(m\)-jet of the actual log gauge, and consequently also of the gauge.

To see that the next order is genuinely singular, hold the final \(n-m\) coordinates fixed and increase the first maximal coordinate from \(a\) to \(a+h\). For \(h>0\), the actual cutoff is \(1/(a+h)\), while the analytic continuation uses \(1/a\). Writing \(t=1/a-u\), the product on the small interval has leading part

\[
(a u)^{m-1}\big(-h/a+(a+h)u\big)\prod_{j>m}(1-b_j/a).
\]

The interval has \(0\le u\le h/(a(a+h))\). Direct integration gives

\[
\int_{1/(a+h)}^{1/a}t^{p-1}P_{v_0+he_1}(t)\,dt
=-\frac{a^{-p-m-1}}{m(m+1)}\prod_{j>m}(1-b_j/a)h^{m+1}+O(h^{m+2}).
\]

For \(p\ne0\), the actual moment minus the fixed-cutoff analytic continuation is minus \(p\) times this integral. Applying \(-p^{-1}\log\) and evaluating the denominator at the unperturbed positive moment yields the displayed coefficient. For \(p=0\), the actual mean logarithm minus its fixed-cutoff continuation is minus the same integral with \(p=0\); applying the negative sign gives precisely the stated coefficient with \(M_0=1\). For \(h<0\), at least one of the other \(m-1\) unchanged coordinates still realizes the maximum, so the original cutoff does not move and the analytic continuation is exact. The different one-sided \((m+1)\)-st coefficients preclude any Peano polynomial of that degree.

**4. Uniform order-two regularity away from zero coordinates.** In any fixed open orthant, only finitely many analytic formulas (one for each maximizing index) occur. Their first- and second-order jets agree on every tie set by the \(O(\delta^3)\) boundary-layer estimate for \(m\ge2\). Accordingly they glue to a \(C^2\) function. Their third derivatives are bounded on compact subsets of the orthant, including one-sided derivatives up to each tie face. Following a line segment through its finitely many analytic cells, continuity of the Hessian and these uniform derivative bounds imply a locally Lipschitz Hessian. Thus \(G_p\) is locally \(C^{2,1}\). At a generic two-way tie the explicit nonzero cubic defect rules out \(C^3\).

**5. Affine covariance.** For any invertible \(A\) and any translation \(z\), the exit-distance definition directly gives \(R_p(z+AQ)=A(R_pQ)\). Hence the gauge of the radial mean body of a parallelotope \(z+AQ\) is \(v\mapsto G_p(A^{-1}v)\), transporting exactly these strata and all pointwise orders under the linear coordinate change.

## Verification

The accompanying standalone `verify.py` evaluates the finite elementary-symmetric formulas with exact rational arithmetic for integer parameters and with high-precision decimal arithmetic for \(p=0\) and a negative exponent. It independently evaluates the fixed-cutoff continuation and the moving-cutoff formula, compares their \((m+1)\)-st order defect against the positive closed-form coefficient, and tests the strict positive axial cusp derivative. The tested strata are generic two-way ties in dimension three, triple ties in dimension three, and triple ties with a lower fourth coordinate. Running `python3 verify.py` produces `SHARP_RADIAL_JET_CHECKS_OK`. These finite evaluations check normalization, signs, and constants; the analytic argument proves the statements for all dimensions, all permitted exponents, and all directions.

## Relationship to prior work

Gardner and Zhang introduced radial mean bodies and proved convexity for nonnegative parameters [1]. Langharst's 2026 theorem established convexity for the remaining range \(-1<p<0\) [2]. Langharst, Manui, and Zvavitch already computed an integral representation of the cube's radial function and specific axial/diagonal values in Proposition 34, Section 3.3, of [3]; that integral formula is **prior work** and is not presented as new. The novel assertion here is its all-dimensional **sharp differentiability classification**, including the exactly quantified order-of-contact at every multiple-maximum stratum and the optimal \(C^{2,1}\)-versus-\(C^3\) transition. The theorem explicitly restricts to \(n\ge3\) and does not assert novelty for the planar-square case. Haddad's planar convexity theorem [4] supplies further context but does not address these higher-dimensional regularity strata.

## Limitations

This is a statement about the gauge and its corresponding boundary regularity for finite real \(p>-1\). It does not establish a global boundary-regularity theorem for general convex bodies, a smoothness statement at \(p=\infty\), or neighborhood \(C^m\) regularity at a higher-multiplicity maximum tie. The exact cube radial integral is known from [3], so the contribution is the nontrivial differentiation and sharp contact analysis rather than a new representation formula. An equivalent higher-dimensional regularity classification could exist in older or unindexed literature; no independent validation has been performed.

## References

[1] R. J. Gardner and G. Zhang, *Affine inequalities and radial mean bodies*, American Journal of Mathematics 120 (1998), 505–528, DOI: 10.1353/ajm.1998.0021.

[2] D. Langharst, *Radial Mean Bodies Are Convex* (earliest public preprint 2026-03-14), arXiv:2603.14134.

[3] D. Langharst, A. Manui, and A. Zvavitch, *On the Fourier Mean Bodies of a Convex Body*, arXiv:2601.20117, Section 3.3, Proposition 34 (version 2, 2026-06-30).

[4] J. Haddad, *Planar radial mean bodies are convex*, arXiv:2412.01475, 2024-12-02; Proceedings of the American Mathematical Society 154 (2026), 833–848.
