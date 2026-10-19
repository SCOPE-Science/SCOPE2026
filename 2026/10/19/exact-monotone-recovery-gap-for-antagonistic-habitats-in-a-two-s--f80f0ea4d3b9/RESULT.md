# Exact monotone recovery gap for antagonistic habitats in a two-species metacommunity

## Finding

For the two-species, two-habitat rank-one colonization model specified below, every baseline fitness \(r>1\) and every differentiation strength \(0<\delta<r\) yield a **unique strictly positive equilibrium**. Both species retain mean occupancy \((r-1)/(2r)\), and the total occupancy of each habitat equals \((r-1)/r\), *independently of \(\delta\)*. Nevertheless, the dominant linear relaxation exponent is

\[
\Lambda(r,\delta)=\frac{2-r}{2r}-\frac{r}{r^2-\delta^2}
+\sqrt{\frac14+\frac{\delta^2}{(r^2-\delta^2)^2}}.
\]

It is strictly negative and strictly decreasing as \(\delta\) increases from zero to \(r\). Thus the local asymptotic linear recovery rate \(g=-\Lambda\) is strictly increasing, starts at zero, and approaches \((r-1)/(2r)\). Near indistinguishable habitats it obeys the exact sharp asymptotic law

\[
 g(r,\delta)=\frac{r-1}{r^4}\delta^2+O_r(\delta^4),
 \qquad \lim_{\delta\downarrow0}\delta^2/g(r,\delta)=\frac{r^4}{r-1}.
\]

At \(\delta=0\), the strict coexistence equilibrium is replaced by a one-dimensional neutrally stable equilibrium segment. The result concerns **local equilibrium resilience**, not a global convergence theorem or a stochastic extinction time.

## Assumptions and scope

There are two species, denoted \(u\) and \(v\), and two equal-capacity habitats, denoted \(A\) and \(B\). All occupancy fractions are nonnegative and satisfy \(u_i+v_i\leq1\) for each \(i\in\{A,B\}\). Write species means as \(\bar u=(u_A+u_B)/2\) and \(\bar v=(v_A+v_B)/2\). Fix real parameters \(r>1\) and \(0\leq\delta<r\), and local fitnesses

\[
 (r_{uA},r_{uB},r_{vA},r_{vB})
  =(r+\delta,r-\delta,r-\delta,r+\delta).
\]

With unit species-specific colonization coefficients and a uniform rank-one mixing kernel \(K_{\alpha,ij}=1/2\), the four-dimensional population equation is

\[
 \dot u_i=-\frac{u_i}{r_{ui}}+(1-u_i-v_i)\bar u,
 \qquad
 \dot v_i=-\frac{v_i}{r_{vi}}+(1-u_i-v_i)\bar v,
 \quad i\in\{A,B\}.
\]

This is the finite two-habitat specialization of the competitive colonization equation with the rank-one mean-field kernel used in the motivating literature. Positive fitnesses imply positive local death rates. At an empty species coordinate, its derivative is nonnegative; at a full habitat, the sum occupancy derivative is strictly negative. Hence the biological occupancy polytope is forward invariant. No conclusion is asserted for non-rank-one kernels, unequal habitat capacities, or \(\delta\ge r\).

## Proof

**1. Exact equilibrium and uniqueness.** At any strictly positive stationary state, put \(x=\bar u>0\), \(y=\bar v>0\), and \(Q_i=1-u_i-v_i\). The equations imply \(u_i=r_{ui}Q_i x\) and \(v_i=r_{vi}Q_i y\). Averaging separately gives

\[
 2=(r+\delta)Q_A+(r-\delta)Q_B
   =(r-\delta)Q_A+(r+\delta)Q_B.
\]

When \(\delta>0\), their difference yields \(Q_A=Q_B\); each sum then gives \(Q_A=Q_B=1/r\). Since the two habitat occupancy equations are \((r+\delta)x+(r-\delta)y=r-1\) and \((r-\delta)x+(r+\delta)y=r-1\), subtracting yields \(x=y=s=(r-1)/(2r)\). Hence the sole positive stationary state is

\[
 (u_A,u_B,v_A,v_B)^*
 =\frac{r-1}{2r^2}(r+\delta,r-\delta,r-\delta,r+\delta).
\]

This vector is strictly positive and has total occupancy \(1-1/r<1\) at each habitat. Substitution checks it is an equilibrium. At \(\delta=0\), the same stationary equations allow every symmetric allocation \(u_A=u_B=x>0\), \(v_A=v_B=y>0\) with \(x+y=(r-1)/r\), proving the stated neutral segment.

**2. Exact spectral factorization.** In the coordinate order \((u_A,u_B,v_A,v_B)\), define \(a=1/(r+\delta)\), \(b=1/(r-\delta)\), \(s=(r-1)/(2r)\), and \(q=1/(2r)\). Differentiating the vector field at the positive equilibrium gives

\[
 J=\begin{pmatrix}
 -a-s+q&q&-s&0\\
 q&-b-s+q&0&-s\\
 -s&0&-b-s+q&q\\
 0&-s&q&-a-s+q
 \end{pmatrix}.
\]

The simultaneous swap of species and habitats commutes with \(J\). On vectors of shape \((x,y,y,x)\) and \((x,y,-y,-x)\), respectively, its two invariant restrictions are

\[
 B_{+}=\begin{pmatrix}-a-s+q&q-s\\q-s&-b-s+q\end{pmatrix},
 \qquad
 B_{-}=\begin{pmatrix}-a-s+q&q+s\\q+s&-b-s+q\end{pmatrix}.
\]

The four eigenvalues of \(J\) are the two eigenvalues of each real symmetric \(2\times2\) block, namely

\[
 \lambda_{\pm}^{(\sigma)}
 =-\frac{a+b}{2}-s+q
 \pm\sqrt{\frac{(a-b)^2}{4}+(q-\sigma s)^2},
 \qquad \sigma\in\{+1,-1\}.
\]

As \(q+s=1/2>|q-s|\) for \(r>1\), the strict largest eigenvalue belongs to \(B_-\). Using \((a+b)/2=r/(r^2-\delta^2)\) and \((a-b)^2/4=\delta^2/(r^2-\delta^2)^2\), this gives the claimed exact expression \(\Lambda(r,\delta)\). All eigenvalues are real, so the spectral abscissa is this largest eigenvalue.

**3. Strict monotonicity and sharp endpoints.** Set \(t=r^2-\delta^2>0\). Direct differentiation, valid for \(0<\delta<r\), yields

\[
 \frac{\partial\Lambda}{\partial\delta}
 =\frac{2\delta}{t^2}\left[-r+
 \frac{r^2+\delta^2}{\sqrt{t^2+4\delta^2}}\right].
\]

The bracket is negative because both compared quantities are positive and

\[
 r^2(t^2+4\delta^2)-(r^2+\delta^2)^2
 =(r^2-1)t^2>0.
\]

Since \(\Lambda(r,0)=0\), this proves \(\Lambda(r,\delta)<0\) and strict increase of \(g=-\Lambda\). Taylor expansion at zero gives \(\Lambda=-(r-1)\delta^2/r^4+O_r(\delta^4)\). Finally, as \(\delta\uparrow r\), writing the radical as \(\sqrt{1/4+(\delta/t)^2}=\delta/t+o(1)\) and noting \((r-\delta)/t=1/(r+\delta)\) gives \(\Lambda\to-(r-1)/(2r)\). This also proves local exponential asymptotic stability for each \(\delta>0\) by the linearization theorem; the decay rate of the linearized semigroup is the exact \(g\), with the dominant real mode attained by its eigenvector.

## Verification

The bundled `verify.py` is a standard-library-only exact-rational test. Running `python3 verify.py` performs, for five rational values of \(r\) and four rational differentiation fractions, all of the following: (i) direct substitution of the closed-form equilibrium into the original nonlinear vector field, (ii) direct differentiation of its full \(4\times4\) Jacobian, (iii) invariant-block checks on three vectors in each symmetry sector, (iv) equality of the full characteristic determinant with the product of the two block determinants at five rational spectral parameters, and (v) the exact positive inequality required for strict monotonicity. It reports 20 parameter instances passing. The unlimited-parameter theorem follows from the algebraic proof above, **not** from these finite tests.

## Relationship to prior work

Bernardi et al., arXiv:2602.06640 (first public 2026-02-06), derive the competitive dispersal equation and a mean-field colonization kernel, stationary self-consistency equations, the marginal homogeneous coexistence manifold, and large-community heterogeneity conditions. Padmanabha et al. (2024) introduced and analyzed related mean-field fitness and heterogeneous coexistence with an implicit stationary solution. Costa, Kubasch, and Loeuille (2026) establish persistence and coexistence criteria for competing species in two habitat types with general colonization rates. Those results motivate the present finite, perfectly anticorrelated habitat configuration. Their general coexistence conditions do not provide the four-mode characteristic factorization, the exact monotonic dominant linear recovery exponent, or the sharp quadratic loss of resilience quantified here. The correlation structure here is deterministic and does not assume independent random habitat fitnesses; the result is not an assertion about large random communities.

## Limitations

Only local asymptotic stability and the exact linearized decay rate are proved; global attraction, global persistence, stochastic extinction times, nonlinear uniform relaxation estimates, and robustness to arbitrary perturbations of all habitat parameters are not claimed. At zero heterogeneity the equilibrium is nonhyperbolic, so the limiting small-\(\delta\) time-scale statement is restricted to positive differentiation strengths. The limit \(\delta\uparrow r\) approaches unbounded death rates in the disadvantaged habitat and is not itself an admissible boundary model. Literature comparisons cannot establish absolute uniqueness; a supplementary appendix in the older source was not retrieved through the available open pathway.

## References

1. D. Bernardi, A. Doimo, G. Nicoletti, P. Padmanabha, A. Rinaldo, S. Suweis, S. Azaele, and A. Maritan, *Habitat heterogeneity and dispersal network structure as drivers of metacommunity dynamics*, arXiv:2602.06640v2, originally submitted 2026-02-06, https://arxiv.org/html/2602.06640v2, especially equations (34), (37)–(44), and Section VI.
2. P. Padmanabha, G. Nicoletti, D. Bernardi, S. Suweis, S. Azaele, A. Rinaldo, and A. Maritan, *Landscape and environmental heterogeneity support coexistence in competitive metacommunities*, PNAS 121, e2410932121 (2024), doi:10.1073/pnas.2410932121, https://pmc.ncbi.nlm.nih.gov/articles/PMC11536131/, especially equations (1), (6), and (7).
3. M. Costa, M. Kubasch, and N. Loeuille, *Metacommunity persistence on spatially heterogeneous landscapes*, arXiv:2607.11291v1 (2026-07-13), https://arxiv.org/abs/2607.11291, especially the two-habitat system (2), Theorems 3.3–3.4, and Section 3.
