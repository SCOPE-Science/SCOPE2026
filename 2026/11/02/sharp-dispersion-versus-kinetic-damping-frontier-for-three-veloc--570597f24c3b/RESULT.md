# Sharp dispersion versus kinetic-damping frontier for three-velocity lattice Boltzmann advection

## Finding

Fix a nonzero subcharacteristic Courant number \(0<|c|<1\). For the second-order D1Q3 advection scheme with positive relaxation parameters \(0<s_v,s_w<2\), let
\[
 p=\left(\frac1{s_v}-\frac12\right)\left(\frac1{s_w}-\frac12\right),\qquad
 q_0=\max\{|1-s_v|,|1-s_w|\}.
\]
The two numbers defining \(q_0\) are the moduli of the two *zero-Fourier-frequency* nonconserved eigenvalues. Given an imposed bound \(q_0\le q<1\), define
\[
 \ell=\frac{1-q}{2(1+q)},\qquad
 P(\ell)=\frac{1-4\ell^2+\sqrt{1+24\ell^2+16\ell^4}}{16},\qquad
 q_*=5-2\sqrt6.
\]
Among **all uniformly \(\ell^2\)-stable schemes** satisfying these constraints, the exact least value of the magic parameter is
\[
 \boxed{p_{\min}(q)=\max\{\ell^2,P(\ell)\}
 =\begin{cases}
 \ell^2,&0\le q\le q_*,\\
 P(\ell),&q_*\le q<1.
 \end{cases}}
\]
Every bound is attained. If \(q\le q_*\), the unique minimizing pair is \(s_v=s_w=1+q\). If \(q>q_*\), the unique minimizing pair is obtained from
\[
 b=\ell,\qquad a=P(\ell)/\ell,\qquad
 s_v=\frac1{a+1/2},\qquad s_w=\frac1{b+1/2}=1+q.
\]
Here \(a=1/s_v-1/2\) and \(b=1/s_w-1/2\). In particular every admissible stable scheme satisfies \(p>1/8\), and \(1/8\) is the sharp unattained infimum when the kinetic-damping restriction is removed by taking \(q\uparrow1\).

For the analytic physical Fourier eigenvalue \(z_\varphi(\theta)\) near the origin, the third-order phase coefficient is exactly
\[
 \log z_\varphi(\theta)=-ic\theta+i c(1-c^2)(p-1/12)\theta^3+O(\theta^4).
\]
Consequently, with the constraint \(q_0\le q\), the sharp absolute cubic phase-error coefficient is \(|c|(1-c^2)(p_{\min}(q)-1/12)\). Without the constraint it has the strict, sharp lower bound \(|c|(1-c^2)/24\).

## Assumptions and scope

The spatial lattice is one-dimensional with velocities \(0,\pm\lambda\), where \(\lambda=\Delta x/\Delta t>0\). The conserved moment is \(u=f_0+f_++f_-\), and the two nonconserved equilibria are \(v^{\rm eq}=c\lambda u\) and \(w^{\rm eq}=c^2\lambda^2u/2\). Each time step consists of diagonal relaxation of these two moments with rates \(s_v,s_w\) followed by standard nearest-neighbor streaming. All parameters are real, and \(0<|c|<1\), \(0<s_v,s_w<2\). Uniform stability means uniform boundedness of all powers of the Fourier amplification matrices over every spatial frequency. The damping cap applies **only to the collision multipliers, equivalently the nonconserved eigenvalues at zero Fourier frequency**. It is not a uniform bound on ghost eigenvalues at nonzero frequencies.

## Proof

**Exact stability inequality.** The necessary and sufficient stability threshold established in Bellotti–Caetano–Dubois–Graille, Theorem 16 and equation (14), can be expressed with \(v=s_v-1\) and \(w=s_w-1\) as
\[
 F(v,w)=(v^2-6v+1)(w^2-1)+4(1-v^2)w\le0.
\]
For fixed \(-1<v<1\), the quadratic \(F(v,\cdot)\) has exactly one root in \((-1,1)\), because \(F(v,-1)=-4(1-v^2)<0\) and \(F(v,1)=4(1-v^2)>0\); that root is precisely the published stability boundary. Thus the polynomial inequality is equivalent to the published threshold, including its boundary. Set \(a=1/s_v-1/2>0\) and \(b=1/s_w-1/2>0\), so that \(v=(1-2a)/(1+2a)\) and \(w=(1-2b)/(1+2b)\). Direct expansion gives the exact identity
\[
 F(v,w)=-\frac{32\,[8a^2b+4ab^2-a-b]}{(1+2a)^2(1+2b)^2}.
\]
Hence the stability condition is precisely
\[
 \Phi(a,b)=8a^2b+4ab^2-a-b\ge0.\tag{1}
\]

**Constrained lower bound.** The cap \(q_0\le q<1\) is equivalent to \(a,b\in[\ell,h]\), with \(\ell=(1-q)/(2(1+q))\) and \(h=1/(4\ell)\). Put \(p=ab\). Equation (1) becomes
\[
 \Phi=a(8p-1)+b(4p-1)\ge0.\tag{2}
\]
If \(p\le1/8\), the right side is strictly negative, proving \(p>1/8\). If \(p<1/4\), (2) and \(a=p/b\) imply
\[
 p(8p-1)\ge b^2(1-4p)\ge\ell^2(1-4p),
\]
or equivalently \(8p^2+(4\ell^2-1)p-\ell^2\ge0\). This quadratic has one positive root, exactly \(P(\ell)\), and \(1/8<P(\ell)<1/4\). If \(p\ge1/4\), the same bound \(p\ge P(\ell)\) is automatic. Additionally \(p=ab\ge\ell^2\). This establishes \(p\ge\max\{\ell^2,P(\ell)\}\).

**Attainment and uniqueness.** The comparison \(P(\ell)\le\ell^2\) is equivalent to \(6\ell^2\ge1\), by evaluating the preceding quadratic at \(p=\ell^2\). When this holds, the corner \(a=b=\ell\) has \(\Phi=2\ell(6\ell^2-1)\ge0\), and uniquely attains \(p=\ell^2\). Otherwise, set \(b=\ell\) and \(a=P(\ell)/\ell\). Since \(\ell^2<P(\ell)<1/4\), this pair is inside \([\ell,1/(4\ell)]^2\). Its stability polynomial vanishes by the defining quadratic for \(P(\ell)\), so it lies on the stable boundary. Equality in the lower-bound chain forces \(b=\ell\), hence this pair is unique. The changeover \(\ell=1/\sqrt6\) is exactly \(q=q_*=5-2\sqrt6\). The expression for \(P(\ell)\) tends to \(1/8\) as \(\ell\downarrow0\), and no positive \(a,b\) achieve that infimum by (2).

**Phase coefficient.** Equation (23) of the motivating paper supplies the physical eigenvalue expansion. Substitution into \(\log(1+z)=z-z^2/2+z^3/3+O(z^4)\) cancels the additional cubic contribution \(c^3/6\) and yields precisely the displayed logarithmic expansion. Because \(p>1/8>1/12\) the cubic magnitude is monotone in \(p\), so the sharp stability-constrained phase bound follows from the attained optimization. This is a long-wavelength statement, not a global Fourier error bound.

## Verification

The standalone `verify_frontier.py` uses exact rational arithmetic for 720 independent checks of the nontrivial stability-polynomial change of variables, 9,801 comparisons with the published radical stability threshold, and 19,220 rational design points, including 17,826 stable points, to cross-check the required lower-bound inequalities. It also checks 103 optimal designs with 75-digit decimal arithmetic, tests both attainment branches and the crossover, and checks the \(q\uparrow1\) limiting constant. All checks pass. They are illustrative checks; the proof above is analytic for every permitted parameter.

## Relationship to prior work

Bellotti, Caetano, Dubois and Graille derive the complete uniform-stability set (their Theorem 16), third-order modified equation (their equation (8)), and the physical and parasitic eigenvalue expansions (their equation (23)). In particular, they already state that third-order accuracy cannot coexist with stability. Those are inputs, not findings claimed here. The additional result is a different optimization question: the globally sharp error-versus-kinetic-damping envelope, its two analytic branches and unique optimizers, and the sharp quantitative dispersion floor \(1/24\). In particular the prior stability theorem specifies feasibility but does not calculate this constrained optimum.

Earlier two-relaxation-time lattice Boltzmann work by Servan-Camas and Tsai (2008) analyzes a different advection–diffusion family and links dispersion and stability; its complete text was not accessible for a line-by-line comparison. Ginzburg and d'Humières (2009) develop magic collision numbers for predominantly steady flow and boundary error. Lallemand and Luo (2000) analyze general LBM dispersion and stability. These create residual historical-priority risk, especially for equivalent optimizations under different variables.

## Limitations

This result is restricted to the linear one-dimensional three-velocity advection model, nonzero subcharacteristic Courant numbers, and interior positive relaxation rates. The cap constrains only collision or zero-frequency kinetic factors, not all nonzero-wavenumber kinetic damping and not the norm of the full amplification matrix. The cubic phase coefficient does not itself control total solution error, finite-grid accuracy, nonlinear behavior, or floating-point errors. As the unrestricted infimum is approached, one relaxation rate tends to zero and the kinetic mode loses uniform damping; no uniform convergence constant is asserted in that singular limit. Independent mathematical validation and comprehensive historical priority verification have not been performed.

## References

1. T. Bellotti, F. Caetano, F. Dubois, B. Graille, *Numerical analysis of a Lax–Wendroff type lattice Boltzmann scheme for the advection equation*, arXiv:2610.32810v1, publicly posted 23 October 2026, https://arxiv.org/html/2610.32810v1, especially §§2–6, Theorem 16 and equations (8), (14), (23).
2. B. Servan-Camas and F. T. C. Tsai, *Lattice Boltzmann method with two relaxation times for advection-diffusion equation: Third order analysis and stability analysis*, Advances in Water Resources 31 (2008), 1113–1126, https://doi.org/10.1016/j.advwatres.2008.05.001.
3. I. Ginzburg and D. d'Humières, *Viscosity independent numerical errors for lattice Boltzmann models: From recurrence equations to “magic” collision numbers*, Computers & Mathematics with Applications 58 (2009), 823–840, https://doi.org/10.1016/j.camwa.2009.02.008.
4. P. Lallemand and L.-S. Luo, *Theory of the lattice Boltzmann method: Dispersion, dissipation, isotropy, Galilean invariance, and stability*, Physical Review E 61 (2000), 6546, https://doi.org/10.1103/PhysRevE.61.6546.
