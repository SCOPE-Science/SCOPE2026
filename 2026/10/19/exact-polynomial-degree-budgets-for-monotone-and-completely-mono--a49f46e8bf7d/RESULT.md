# Exact polynomial degree budgets for monotone and completely monotone exponential dense output

## Finding
For the exact two-state conservative decay flow with normalized step \(z>0\), a polynomial continuous extension matching both endpoint values **and both physical endpoint slopes** can preserve positivity and monotone transfer at a degree growing only as \(2\sqrt z+O(1)\). If every derivative must alternate in sign (complete monotonicity), the sharp minimum instead grows as \(z+O(1)\). We prove exact finite-degree existence criteria, give constructive extremizers, and establish the complete-monotonicity minimum in closed form.

Let \(a_z=z/(1-e^{-z})\), \(b_z=ze^{-z}/(1-e^{-z})\), and let \(n\) denote a permitted upper bound on the polynomial degree. For \(n\le 2\), no such monotone polynomial exists for positive \(z\). For every integer \(k\ge1\):

\[
\begin{aligned}
\deg p\le 2k+1\quad\text{is feasible}\quad&\Longleftrightarrow\quad
\frac{a_z+b_z-2\sqrt{a_zb_z}/(k+1)}{k(k+2)}\le1,\\
\deg p\le 2k+2\quad\text{is feasible}\quad&\Longleftrightarrow\quad
\frac{a_z+b_z}{(k+1)(k+2)}\le1.
\end{aligned}
\]

Both inequalities have one sharp positive step threshold, increasing through every listed threshold degree. The thresholds at degrees three through six are respectively \(3.407945408841015\ldots\), \(5.969409170715773\ldots\), \(8.089517561626475\ldots\), and \(11.999852518060361\ldots\).

With complete monotonicity, the **exact** minimum degree is
\[
N_{\mathrm{cm}}(z)=\left\lceil\frac{z(1-e^{-z})}{1-(1+z)e^{-z}}\right\rceil.
\]
The minimum degree for monotonicity alone satisfies \(N_{\mathrm{mon}}(z)=2\sqrt z+O(1)\) as \(z\to\infty\), while \(N_{\mathrm{cm}}(z)=z+O(1)\).

## Assumptions and scope
Consider \(y_1'=-\lambda y_1\), \(y_2'=\lambda y_1\), with \(\lambda>0\), \(y_1(0)=a\in(0,1)\) and \(y_2(0)=1-a\). For a step \(\Delta t>0\), write \(z=\lambda\Delta t\), \(\theta\in[0,1]\), and a polynomial dense output as \(y_1^{\mathrm{dense}}(\theta)=a p(\theta)\), \(y_2^{\mathrm{dense}}(\theta)=1-a p(\theta)\). The exact endpoint Hermite conditions are
\[
p(0)=1,\qquad p(1)=e^{-z},\qquad p'(0)=-z,\qquad p'(1)=-ze^{-z}.
\]

*Monotone shape preservation* means \(p'(\theta)\le0\) for all \(\theta\in[0,1]\). This makes the two components strictly positive, bounded, and mass-conserving for all \(\theta\), because \(e^{-z}\le p(\theta)\le1\) and \(a<1\). *Complete monotonicity* requires \((-1)^j p^{(j)}(\theta)\ge0\) for all integers \(j\ge0\) and all \(\theta\in[0,1]\); derivatives beyond the degree vanish. All calculations concern polynomial extensions with **exact** endpoint data. The construction is not claimed to be an MPRK update or to have a specified global interpolation order.

## Proof
**1. Reduction to a nonnegative polynomial with fixed endpoint values and mass.** Set
\[
q(\theta)=-\frac{p'(\theta)}{1-e^{-z}}.
\]
The four Hermite constraints and monotonicity are equivalent to
\[
q\ge0\text{ on }[0,1],\qquad q(0)=a_z,\quad q(1)=b_z,\quad \int_0^1q(\theta)\,d\theta=1,
\]
with \(\deg q\le n-1\). Conversely \(p(\theta)=1-(1-e^{-z})\int_0^\theta q(t)\,dt\) reconstructs an admissible output. The nonzero endpoint values guarantee this integral is strictly increasing. Degrees zero or one for \(p\) are impossible by unequal endpoint derivatives. If \(\deg p\le2\), the density \(q\) is affine, forcing \(\int_0^1q=(a_z+b_z)/2=\tfrac z2\coth(z/2)>1\); this is impossible.

**2. Odd output degrees.** For \(n=2k+1\) (\(k\ge1\)), the Markov–Lukács interval representation says any nonnegative \(q\) of degree at most \(2k\) has
\[
q(\theta)=A(\theta)^2+\theta(1-\theta)B(\theta)^2,\quad \deg A\le k,\quad \deg B\le k-1.
\]
At the endpoints, \(A(0)^2=a_z\) and \(A(1)^2=b_z\). Thus \(\int q\ge\int A^2\), and the optimal endpoint signs are chosen to exploit the signed endpoint reproducing kernel. In the degree-\(k\) shifted Legendre space with Lebesgue inner product, the kernel has
\[
K_k(0,0)=K_k(1,1)=(k+1)^2,\qquad K_k(0,1)=(-1)^k(k+1).
\]
The minimum squared \(L^2\) norm of a degree-\(k\) polynomial having endpoint values \(\sqrt{a_z}\), \((-1)^k\sqrt{b_z}\) is the Gram-inverse quadratic form
\[
I_o(z,k)=\frac{a_z+b_z-2\sqrt{a_zb_z}/(k+1)}{k(k+2)}.
\]
The other sign choice cannot lower this value. Let \(A_*\) denote the unique least-norm interpolant. If \(I_o\le1\), then
\[
q=A_*^2+6(1-I_o)\theta(1-\theta)
\]
has exactly the prescribed endpoint values and integral, remains nonnegative, and has degree at most \(2k\). If \(I_o>1\), the minimal-integral bound rules out every admissible \(q\). This proves both directions.

**3. Even output degrees.** For \(n=2k+2\), a nonnegative polynomial \(q\) of degree at most \(2k+1\) has the interval representation
\[
q(\theta)=\theta A(\theta)^2+(1-\theta)B(\theta)^2,\quad\deg A,\deg B\le k.
\]
The endpoint conditions become \(B(0)^2=a_z\), \(A(1)^2=b_z\). The degree-\(k\) Jacobi endpoint evaluation functional has squared norm \((k+1)(k+2)\) in each weighted space \(L^2([0,1],(1-\theta)\,d\theta)\) at \(0\), and \(L^2([0,1],\theta\,d\theta)\) at \(1\). Independently minimizing the two squared norms yields
\[
I_e(z,k)=\frac{a_z+b_z}{(k+1)(k+2)}.
\]
If \(I_e\le1\), choose weighted least-norm endpoint interpolants \(B_*\) and \(A_*\) and put
\[
q=\theta A_*^2+(1-\theta)B_*^2+6(1-I_e)\theta(1-\theta).
\]
This proves sufficiency, while the two weighted kernel lower bounds prove necessity. For explicit reproducibility, the weighted reproducing kernels are
\[
K_B(\theta)=\sum_{j=0}^k 2(j+1) P_j^{(0,1)}(1-2\theta),\quad
K_A(\theta)=\sum_{j=0}^k 2(j+1)(-1)^jP_j^{(1,0)}(1-2\theta),
\]
with \(B_*=(\sqrt{a_z}/[(k+1)(k+2)])K_B\) and \(A_*=(\sqrt{b_z}/[(k+1)(k+2)])K_A\). Here \(P_j^{(\alpha,\beta)}\) are Jacobi polynomials.

**4. Thresholds and degree asymptotics.** The identities
\[
a_z+b_z=z\coth(z/2),\qquad 2\sqrt{a_zb_z}=z\operatorname{csch}(z/2)
\]
show both degree criteria have strictly increasing left-hand sides in \(z>0\), as \(z\coth(z/2)\) is strictly increasing and \(z\operatorname{csch}(z/2)\) is strictly decreasing. For each \(k\ge1\), the left side starts below one at \(z=0^+\) and diverges, so exactly one positive cutoff exists. For \(z\to\infty\), \(a_z=z+o(1)\) and \(b_z=O(ze^{-z})\); the two inequalities require and achieve \(k=\sqrt z+O(1)\), giving \(N_{\mathrm{mon}}(z)=2\sqrt z+O(1)\).

**5. Complete monotonicity.** Any degree-\(n\) polynomial can be uniquely written \(p(\theta)=\sum_{j=0}^n c_j(1-\theta)^j\). It is completely monotone on \([0,1]\) if and only if all \(c_j\ge0\): necessity follows by evaluating every signed derivative at \(\theta=1\), sufficiency term by term. The endpoint data force \(c_0=e^{-z}\), \(c_1=ze^{-z}\), and
\[
\sum_{j=2}^n c_j=S_z:=1-(1+z)e^{-z}>0,\quad
\sum_{j=2}^n j c_j=M_z:=z(1-e^{-z}).
\]
Thus the weighted mean index of these nonnegative coefficients is \(R_z=M_z/S_z>2\), and necessarily \(n\ge\lceil R_z\rceil\). The strict inequality follows from \(M_z-2S_z=z-2+(z+2)e^{-z}>0\), whose derivative is \(1-(z+1)e^{-z}>0\). Conversely, with \(j=\lfloor R_z\rfloor\), take
\[
c_j=S_z(j+1-R_z),\qquad c_{j+1}=S_z(R_z-j)
\]
and all other coefficients \(c_\ell=0\) for \(\ell\ge2\). These coefficients are nonnegative, obey both moment constraints and have degree \(\lceil R_z\rceil\) (if \(R_z\) is integral the second coefficient vanishes). Finally \(R_z=z+O(z^2e^{-z})\) as \(z\to\infty\), hence \(N_{\mathrm{cm}}(z)=z+O(1)\).

## Verification
The accompanying reproducible `verify.py` independently checks Legendre endpoint Gram matrices, weighted Jacobi kernels, norm identities and explicit minimal-density constructions symbolically for degrees up to twelve; it also checks the threshold equations at 50-digit precision and the finite-degree separation at representative stiffness levels. All checks passed (236 deterministic assertions). These finite computations verify algebraic specializations; the all-degree and all-parameter statements follow from the exact interval SOS representations, kernel minimizations, and moment arguments above. Example cutoffs are numerical evaluations of stated implicit equations, not additional axioms.

## Relationship to prior work
Izgin, *A Boot-Strapping Technique to Design Dense Output Formulae for Modified Patankar–Runge–Kutta Methods* (arXiv:2406.16718v1, 2024), develops conservative positivity-preserving dense output and discusses possible negative output from explicit higher-order interpolation, including cubic-Hermite sufficient criteria (Sec. 3.1–3.2). It does not state an exact minimal polynomial degree for the exponential two-state Hermite endpoint data or compare it with complete monotonicity. Classical work by Fritsch–Carlson and Dougherty–Edelman–Hyman establishes shape-preserving cubic and quintic interpolation conditions; in particular cubic Hermite monotonicity is not claimed as new. Markov–Lukács representations, Legendre/Jacobi kernels, and endpoint least-norm interpolation are also standard. The additional statement here is their exact all-degree synthesis for this natural stiff-decay benchmark and the sharp square-root-versus-linear growth contrast.

## Limitations
The endpoints and slopes are assumed **exact**; neither an algorithm for obtaining them from a practical multistage integrator nor a global approximation-order guarantee is proved. The polynomial minimizing degree is not asserted to approximate the interior exponential in a strong norm. The result concerns a scalar two-state conservative transfer; arbitrary nonlinear or multicomponent production–destruction problems are not covered. Exact positivity follows from monotonicity in this special model, not conversely. The cited classical polynomial techniques may give an alternate derivation of the benchmark; the absence of an identical theorem in the inspected sources does not certify publication priority. No independent review has been performed.

## References
1. T. Izgin, *A Boot-Strapping Technique to Design Dense Output Formulae for Modified Patankar–Runge–Kutta Methods*, arXiv:2406.16718v1 (submitted 24 June 2024), https://arxiv.org/html/2406.16718v1 .
2. F. N. Fritsch and R. E. Carlson, *Monotone Piecewise Cubic Interpolation*, SIAM J. Numer. Anal. 17 (1980), 238–246, DOI:10.1137/0717021.
3. R. L. Dougherty, A. Edelman and J. M. Hyman, *Nonnegativity-, Monotonicity-, or Convexity-Preserving Cubic and Quintic Hermite Interpolation*, Math. Comp. 52 (1989), 471–494, DOI:10.1090/S0025-5718-1989-0962209-1.
4. Classical Markov–Lukács nonnegative interval polynomial representation and the reproducing kernels of shifted Legendre/Jacobi polynomial systems (used with explicit definitions and derivations above).
