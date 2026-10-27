# Sharp finite-chain cutoff for partial uphill current in symmetric two-species exclusion

## Finding

For the boundary-driven hard-core two-species reaction-diffusion chain of Casini, Giardinà and Vernia, consider a symmetric diffusivity matrix with diagonal coefficient \(a>b>0\), off-diagonal coefficient \(b\), and reaction parameter \(U\ge 2b\). Let the chain consist of \(N\ge1\) sites; put \(L=N+1\). Fix physical reservoir densities whose **total** particle density falls by \(\delta>0\) from left to right while the difference between species A and B increases from \(-m\) to \(+m\). Here \(m>\delta/2\), so the A density at the right reservoir exceeds that at the left reservoir. Write

\[
\lambda=\operatorname{arcosh}\left(1+\frac{U}{a-b}\right),\qquad z=e^{-\lambda},\qquad
R=\frac{a+b}{a-b}\frac{\delta}{m},\qquad
F_L=L(1-z)\frac{1+z^{L-1}}{1-z^L}.
\]

The stationary discrete Fickian species-A current on **every link including both reservoir links** points from left to right, against the A boundary density increase, **if and only if** \(F_{N+1}<R\). For \(R>2\), \(F_L\) increases strictly from \(F_2=2\) to infinity; hence there is a unique sharp chain-length transition. At the equality \(F_{N+1}=R\), both reservoir-link currents vanish and all remaining link currents are positive. When \(F_{N+1}>R\), the two reservoir-link currents are negative, yet at least one interior link current is positive. If \(R\le2\), strict uphill current on all links is impossible for every \(N\ge1\).

For the exact physical parameters \(a=1\), \(b=1/2\), \(U=1\), \(m=1/4\), \(\delta=3/10\), and average reservoir total density \(t=1/2\), the threshold lies strictly between \(N=3\) and \(N=4\): \(F_4=10/3<R=18/5<F_5=170/41\). The four currents at \(N=3\) are \(1/240,11/240,11/240,1/240\), whereas the five at \(N=4\) are \(-7/1025,147/4100,43/1025,147/4100,-7/1025\).

## Assumptions and scope

Each site of \(\{1,\dots,N\}\) has state \(0\) (vacant), A, or B, with at most one particle. For any adjacent pair, exchange the pair at rate \(a\), and exchange while simultaneously swapping A and B (fixing vacancies) at rate \(b\). One may also include the nonnegative left/right colour-mutation rates \(U-2b-h\) and \(h\), respectively, where \(0\le h\le U-2b\), and use the associated boundary generator in equations (42)–(43) of [1]. These choices have the same exactly closed one-point equations, so the assertion is independent of \(h\). For the exact example and checker take \(h=0\), \(U=2b\), so there is no separate interior mutation rule.

Write \(\rho_j^A\) and \(\rho_j^B\) for stationary one-point occupations, setting the fictitious sites \(j=0\) and \(j=L\) to prescribed reservoir densities. Set \(T_j=\rho_j^A+\rho_j^B\) and \(M_j=\rho_j^A-\rho_j^B\). The four reservoir conditions are

\[
T_0=t+\delta/2,\quad T_L=t-\delta/2,\quad M_0=-m,\quad M_L=m,
\]

where \(m+\delta/2\le t\le1-\delta/2\); these inequalities ensure physical, nonnegative reservoir A, B and vacancy densities. The condition \(m>\delta/2\) is precisely \(\rho_L^A>\rho_0^A\). This is a natural anti-aligned pair of density gradients (falling total occupation but rising A-B imbalance), not an assumption on the unknown stationary profile.

Define the **discrete constitutive (Fickian) component** of the mean A current on link \(j\to j+1\) by

\[
J_{A,j}=a(\rho_j^A-\rho_{j+1}^A)+b(\rho_j^B-\rho_{j+1}^B),\qquad 0\le j\le N.
\]

The local A continuity equation also contains a reaction term; this is not a claim that A particle count is conserved. The first and last links encode reservoir fluxes through the imposed boundary values. The precise statement pertains to this constitutive current and **not** to unlabelled total-particle current or to a putative pure A-tracer crossing count of the swap-and-mutation transition.

## Proof

1. **Exact stationary closure.** Equations (28)–(30) of [1] give, for \(1\le j\le N\),
   \[
   a\Delta\rho_j^A+b\Delta\rho_j^B+U(\rho_j^B-\rho_j^A)=0,\qquad
   b\Delta\rho_j^A+a\Delta\rho_j^B+U(\rho_j^A-\rho_j^B)=0,
   \]
   where \(\Delta f_j=f_{j-1}-2f_j+f_{j+1}\). Adding and subtracting gives \(\Delta T_j=0\) and \((a-b)\Delta M_j-2UM_j=0\). Since the coefficients and boundary values fix a nonsingular Dirichlet problem, the unique mean solution is
   \[
   T_j=t+\delta/2-\delta j/L,\qquad
   M_j=m\frac{\sinh(\lambda(j-L/2))}{\sinh(\lambda L/2)},
   \]
   with \(\cosh\lambda=1+U/(a-b)\). These expressions also show \(T_j\in[0,1]\) and \(\lvert M_j\rvert\le m\le T_j\), so all stationary species densities are physical.

2. **Current and boundary extremality.** Substitution gives
   \[
   J_{A,j}=\frac12\left(\frac{(a+b)\delta}{L}-(a-b)(M_{j+1}-M_j)\right),
   \]
   and
   \[
   M_{j+1}-M_j=\frac{2m\sinh(\lambda/2)\cosh(\lambda(j+1/2-L/2))}{\sinh(\lambda L/2)}>0.
   \]
   The largest increment occurs **only** on \(j=0,N\) for \(N\ge2\) (both links tie when \(N=1\)). Its exact value is
   \[
   m(1-z)\frac{1+z^{L-1}}{1-z^L}=\frac{m}{L}F_L.
   \]
   The two boundary-link currents therefore attain the minimum, which is positive exactly when \(F_L<R\). At equality, the strictly smaller interior colour increments give positive interior currents. Beyond equality, both boundary currents are negative; if \(R>2\), at least one interior current remains positive because
   \[
   \sum_{j=0}^{N}J_{A,j}=\tfrac12((a+b)\delta-2(a-b)m)=\tfrac12(a-b)m(R-2)>0.
   \]

3. **Strict finite-size monotonicity.** With \(c=\lambda/2>0\), extend the boundary functional from integer lengths to real \(L\ge2\):
   \[
   F_L=\frac{2L\sinh c\cosh((L-1)c)}{\sinh(Lc)}.
   \]
   Logarithmic differentiation yields
   \[
   \frac{d}{dL}\log F_L
   =\frac1L-\frac{c\cosh c}{\sinh(Lc)\cosh((L-1)c)}>0,
   \]
   because \(\sinh(Lc)>Lc\) and \(\cosh((L-1)c)\ge\cosh c\) for every \(L\ge2\). Direct evaluation gives \(F_2=2\), while \(F_L\sim2L\sinh c\,e^{-c}=L(1-e^{-2c})\to\infty\). Thus every \(R>2\) has a unique real crossing and a sharp integer-chain cutoff. The case \(R\le2\) follows from \(F_L\ge2\).

4. **Exact example.** For \(a=1,b=1/2,U=1\), the recurrence is \(M_{j+1}-6M_j+M_{j-1}=0\), giving \(z=3-2\sqrt2\). The parameter choices yield reservoirs \((\rho_0^A,\rho_0^B)=(1/5,9/20)\) and \((\rho_L^A,\rho_L^B)=(3/10,1/20)\). Exact rational evaluation yields \(F_4=10/3\), \(F_5=170/41\), and the current vectors stated in the finding.

## Verification

The standalone `check.py` solves the finite stationary difference problem using rational arithmetic for \(1\le N\le60\), evaluates every link current, verifies the cutoff on those sizes, and independently constructs the **full** three-state-per-site continuous-time Markov generator from the pair and reservoir transition rules at \(N=1,2,3,4\). It solves the stationary distributions (up to \(3^4\) states) and checks all one-point means against the exact recurrence. It also checks strict increase of the real-length threshold functional at 1,000 points and the exact rational transition example. Running `python check.py` with the dependencies in `requirements.txt` produces the output stored in `checker_output.txt`; there are 1,445 passed assertions. These finite tests confirm normalization and dynamics, but the all-\(N\) result relies on the above exact proof, not numerical sampling.

## Relationship to prior work

Casini, Giardinà and Vernia [1], initially publicly available on 2022-10-04, construct exactly the hard-core, boundary-driven cross-diffusion/reaction process used here, derive its closed finite-chain one-point equations and establish the possibility of partial uphill diffusion on a lattice and its disappearance in the hydrodynamic limit. Their continuum stationary profile (their equation (10)), duality theorem and hydrodynamic results are prior work. The result here adds the **evaluated sharp length criterion for the finite discrete chain with opposing total and colour boundary gradients**, strict monotonicity of its threshold, and the precise sign-changing boundary-link regime. The continuum profile is not substituted for a finite-difference solution.

Floreani, Giardinà, den Hollander, Nandan and Redig [2] analyze a two-layer switching model with different layerwise exclusion rules and characterize global uphill transport and boundary layers. Their switching model allows distinct layer occupancies and is not the same one-site hard-core cross-diffusion generator; its bulk/total-current results do not imply the present species-A all-link cutoff.

The discrete closure in [1] is the essential starting point, so the result is an explicit extension of established equations, not a claim to have invented the model, the phenomenon of partial uphill current, the hyperbolic solution method, or finite-size effects generally. A mathematically equivalent length criterion derived in other literature remains a priority risk; independently verified priority is not claimed.

## Limitations

The threshold is exact for symmetric positive-definite two-species diffusivity, physical reservoirs in the stated anti-aligned family, and the constitutive species-A current including both reservoir links. It does not classify general asymmetric matrices, arbitrary reservoir values, raw microscopic species-transfer counting across swap-and-flip events, stochastic current fluctuations, or hydrodynamic joint scalings. The model's previously published one-point closure is an assumed and cited ingredient. All results here concern mean stationary currents, not sample paths.

## References

[1] F. Casini, C. Giardinà and C. Vernia, *Uphill in reaction-diffusion multi-species interacting particles systems*, arXiv:2210.01514v1 (first public 2022-10-04), later *Journal of Statistical Physics* (2023), DOI 10.1007/s10955-023-03141-3. https://arxiv.org/abs/2210.01514 and https://doi.org/10.1007/s10955-023-03141-3

[2] S. Floreani, C. Giardinà, F. den Hollander, S. Nandan and F. Redig, *Switching Interacting Particle Systems: Scaling Limits, Uphill Diffusion and Boundary Layer*, *Journal of Statistical Physics* 186, 33 (2022), DOI 10.1007/s10955-022-02878-7. https://doi.org/10.1007/s10955-022-02878-7
