# Global exponential equilibration in a destination-blind two-house segregation model

## Finding
For the two-house, two-population mean-field relocation dynamics of Cao and Cortez, any positive background relocation rate removes all multiplicity of equilibrium even when social intolerance is positive. For every \(\beta>0\), \(\lambda\geq0\), \(\rho_B>0\), \(\rho_R>0\), and \(\rho_B+\rho_R<1\), every compatible initial neighborhood distribution converges exponentially to the same strictly positive equilibrium. This equilibrium has an explicit two-fugacity form and its mixed-neighborhood probability decreases strictly as intolerance increases at fixed densities, with strict suppression below the independent-occupancy baseline for \(\lambda>0\).

Write \(a=\beta/(\beta+\lambda)\). There are unique \(z,w>0\) satisfying the density constraints below. In the order \((0,0),(1,0),(0,1),(2,0),(0,2),(1,1)\), the limiting distribution is
\[
 p^*=Z^{-1}(1,2z,2w,z^2,w^2,2azw),\qquad
 Z=1+2z+2w+z^2+w^2+2azw,
\]
where
\[
 \rho_B=\frac{z(1+z+aw)}{Z},\qquad
 \rho_R=\frac{w(1+w+az)}{Z}.
\]
In particular, for \(\lambda>0\), \(0<p^*_{1,1}<2\rho_B\rho_R\); at \(\lambda=0\), equality holds. Moreover \(\lambda\mapsto p^*_{1,1}\) is strictly decreasing for fixed positive \(\beta\) and densities.

## Assumptions and scope
Each neighborhood contains two houses. States \(s=(b,r)\) count blue and red households with \(b,r\geq0\), \(b+r\leq2\). A blue household departs its source at intensity \(\beta+\lambda r\), and a red household at intensity \(\beta+\lambda b\); their destinations are uniformly chosen vacant houses. The deterministic large-number-of-neighborhoods limit is the six-dimensional polynomial ODE in Cao–Cortez, Section 2.1, equation (2.5), and is considered on the simplex with conserved per-house occupancies \(\rho_B=\tfrac12\sum_s b p_s\), \(\rho_R=\tfrac12\sum_s r p_s\). The initial distribution may have zero components; only the stated strictly positive densities and strictly positive vacancy fraction are assumed. Convergence and exponential rate concern this deterministic ODE, not finite-population mixing or spatially structured neighborhoods.

More precisely, for some \(c>0\), \(C<\infty\) depending on the fixed parameters and densities (and possibly the initial distribution),
\[
 \|p(t)-p^*\|_1\leq C e^{-ct}\qquad(t\geq0).
\]
No parameter-uniform exponent is asserted.

## Proof
**1. Flux representation and the three conserved quantities.** Let \(V_s=2-b-r\). The blue transition from source \(s=(b,r)\) to destination \(t=(B,R)\), when \(b\geq1\), \(V_t\geq1\), has flux
\[
 F_B(s,t;p)=\frac{bV_t}{2}(\beta+\lambda r)p_s p_t.
\]
It changes the ordered pair \((s,t)\) into \(((b-1,r),(B+1,R))\). The red flux is \(F_R(s,t;p)=rV_t(\beta+\lambda b)p_sp_t/2\). Summing their incoming and outgoing contributions gives exactly equation (2.4), hence equation (2.5), of the source. Every event preserves total neighborhood count and total counts of each color. The constraints therefore define a compact forward-invariant convex set. Let \(e=1-\rho_B-\rho_R>0\).

**2. Unique Gibbs candidate.** For \(u=\log z\), \(v=\log w\), put \(\Phi(u,v)=\log Z(e^u,e^v)-2\rho_Bu-2\rho_Rv\). Its Hessian is the covariance of the random vector \((b,r)\) under the six strictly positive weights in the displayed equilibrium, hence is strictly positive definite. Since \((2\rho_B,2\rho_R)\) lies in the interior of the triangle with vertices \((0,0),(2,0),(0,2)\), the support-function lower bound makes \(\Phi\) coercive. It has a unique minimizer. Its gradient equations are exactly the two displayed density constraints, establishing unique positive fugacities.

**3. Reversibility at that candidate.** Write
\[
 c_{b,r}=\frac{2!}{b!r!(2-b-r)!}a^{br},\qquad p^*_{b,r}=c_{b,r}z^bw^r/Z.
\]
Every blue relocation exchanges one blue occupancy between source and destination. In the reverse event, the new destination is the former source. Combinatorial factorials cancel, and the remaining identity is
\[
 (\beta+\lambda r)a^r=\beta\qquad(r\in\{0,1\}).
\]
The same identity holds for red relocations after interchanging colors. Thus every elementary oriented relocation flux is exactly balanced by its reverse at \(p^*\). This identity relies on the fact that an occupied source in a two-house neighborhood has at most one opposite-type neighbor.

**4. Strict entropy dissipation.** For interior \(p\), set
\[
 H(p\mid p^*)=\sum_s p_s\log\frac{p_s}{p^*_s}.
\]
Pair each relocation event with its unique reverse, with forward and reverse fluxes \(F,G\). Conservation and the preceding detailed balance yield
\[
 \frac{d}{dt}H(p(t)\mid p^*)=-\sum_{\mathrm{reversible\ event\ pairs}}(F-G)\log(F/G)\leq0.
\]
For equality all elementary flux pairs must balance. In particular, the three reactions \((1,0)+(1,0)\rightleftarrows(0,0)+(2,0)\), \((0,1)+(0,1)\rightleftarrows(0,0)+(0,2)\), and \((1,0)+(0,1)\rightleftarrows(0,0)+(1,1)\) force
\[
 p_{1,0}^2=4p_{0,0}p_{2,0},\quad p_{0,1}^2=4p_{0,0}p_{0,2},\quad 2p_{0,0}p_{1,1}=a p_{1,0}p_{0,1}.
\]
For a strictly positive distribution these imply precisely the Gibbs form with some \(z,w\), and the conserved densities then imply \(p=p^*\). Conversely \(p^*\) balances all reactions.

**5. No boundary limits; exponential convergence.** The one-neighborhood marginal also evolves as a time-dependent six-state birth–death Markov chain. At time \(t\), blue and red addition rates into a neighborhood of vacancy count \(V\) are \(VA_B(t)/2\), \(VA_R(t)/2\), where \(A_B(t)=2\beta\rho_B+\lambda p_{1,1}(t)\) and \(A_R(t)=2\beta\rho_R+\lambda p_{1,1}(t)\). Blue and red departure rates are \(eb(\beta+\lambda r)\), \(er(\beta+\lambda b)\), respectively. All allowable transition rates have parameter-dependent positive lower bounds and finite upper bounds. The triangular six-state transition graph is connected. A fixed-time path expansion or uniformization therefore gives \(p_s(t)\geq\eta>0\) for all states and all \(t\geq1\), with \(\eta\) depending only on the fixed parameters and densities. The entropy Lyapunov principle on this compact positive set now forces \(p(t)\to p^*\).

For a quantitative rate, the entropy production quadratic form at \(p^*\) is positive definite on the three-dimensional tangent space of conserved mass and color densities. Indeed, its null space must annihilate the three linearly independent reaction vectors displayed in step 4, which span that tangent space; the Hessian of \(H\) is also positive definite there. Hence \(-\dot H\geq c_0 H\) in a neighborhood of \(p^*\), for some \(c_0>0\). Compactness and uniqueness of the zero of dissipation yield the same bound, with a possibly smaller constant, on the uniformly positive invariant region. Thus \(H(t)\leq H(1)e^{-c_0(t-1)}\) for \(t\geq1\). Pinsker's inequality yields the asserted exponential \(\ell^1\) convergence.

**6. Strict intolerance response.** Regard \((b,r,br)\) as sufficient statistics of the strictly positive exponential family with natural parameters \((u,v,\log a)\). At fixed means \((2\rho_B,2\rho_R)\), differentiate the mean of \(br\) with respect to \(\log a\). The result is the strictly positive Schur complement
\[
 \operatorname{Var}(br)-\operatorname{Cov}(br,(b,r))\operatorname{Cov}(b,r)^{-1}\operatorname{Cov}((b,r),br)>0.
\]
Strictness holds because \(br\) is not an affine function of \((b,r)\) on the six-state support. As \(\lambda\) increases, \(\log a\) strictly decreases. Finally, direct subtraction gives
\[
 (1+z+aw)(1+w+az)-aZ=(1-a)\bigl[1+z+w+(1+a)zw\bigr].
\]
Using the density identities, this is equivalent to \(p^*_{1,1}<2\rho_B\rho_R\) whenever \(a<1\), with equality at \(a=1\).

## Verification
Run \(\texttt{python verify.py}\) with Python 3.10 or later. The standalone checker constructs every ordered source/destination relocation using exact rational arithmetic, compares the resulting six-component ODE with its equilibrium, checks all eventwise forward/reverse balances across 81 parameter choices (1,458 event comparisons), verifies the conserved densities and the strict mixed-neighborhood inequality, and tests negative entropy production for one non-equilibrium compatible interior state. No numerical test is used as a substitute for the global convergence, quantitative rate, or monotonicity proofs above.

## Relationship to prior work
Cao and Cortez (2026), equations (2.4)–(2.5), introduce exactly these destination-agnostic dynamics. In Section 2.1 they prove local segregation when \(\beta=0\) and convergence to a trinomial law when \(\lambda=0\), including a five-reaction entropy computation (Proposition 2.4). Their stated results do not treat the joint regime \(\beta>0\), \(\lambda>0\) at two houses. This finding completes that joint regime and gives a strict intolerance-response law.

Durrett and Zhang (2014), Section 'Special Case \(L=2\)', already derive a detailed-balance equilibrium with the same algebraic relations for a different, happiness-dependent source-and-destination relocation mechanism under equal color densities. The *static two-house detailed-balance identities themselves are not claimed as novel*. Their L=2 discussion explicitly concerns fixed points of their different dynamics, not exponential global attraction for the 2026 destination-blind ODE with arbitrary unequal densities. The new content is the all-initial-data kinetic convergence and strict response under the 2026 rate mechanism. General entropy methods for reversible chemical reaction systems supply conceptual precedent, not an independently claimed methodological innovation.

## Limitations
The proof uses exactly two houses; the factorial cancellation in the reversible flux condition does not persist unchanged for three or more houses under a linear intolerance law. Strict positivity of the baseline rate and of both population densities and vacancy fraction is essential to uniform irreducibility. The exponential rate is not numerically optimized, and the result makes no claim about heterogeneous destinations, finite-N fluctuations, nonlocal network migration, or global segregation in larger neighborhoods. Historical originality remains subject to independent specialist review, including possible general reaction-network formulations of the same kinetic conclusion.

## References
1. Fei Cao and Roberto Cortez, 'Relocation without preference: A destination-agnostic Schelling-type metapopulation model,' arXiv:2604.24998v1 (publicly posted 2026-04-27), https://arxiv.org/html/2604.24998v1, especially Sections 1.1 and 2.1, equations (2.4)–(2.5) and Proposition 2.4.
2. Richard Durrett and Yuan Zhang, 'Exact solution for a metapopulation version of Schelling’s model,' Proceedings of the National Academy of Sciences 111 (2014), 14036–14041, DOI:10.1073/pnas.1414915111, open full text https://pmc.ncbi.nlm.nih.gov/articles/PMC4191761/, especially 'Special Case L = 2'.
