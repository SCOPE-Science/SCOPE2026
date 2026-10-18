# Joint time-and-depth excursions at a countably branched interval-map transition

## Finding

For the countably piecewise-affine auxiliary interval map \(T_\lambda\) of Ji and Ma, the first visit from its fifth Markov cell to the fourth has an exact **joint duration-and-ceiling law**. Its finite-ceiling probability generating function is a ratio of explicitly defined second-order polynomials, simultaneously determining every finite first-passage-time distribution restricted by the maximum cell index. The same theorem supplies the unrestricted Catalan distribution and the separate time and depth crossover laws on both sides of \(\lambda=1/2\). The latter are consequences of the joint description, not claims that Catalan counting or branching-process crossover functions are new in isolation.

Let \(0<\lambda<1\), \(V_i=(\lambda^i,\lambda^{i-1}]\), and sample \(x\) according to normalized Lebesgue measure on \(V_5\). Before reaching \(V_4\), iterate
\[
T_\lambda(x)=\frac{x-\lambda^i}{\lambda(1-\lambda)}\qquad(x\in V_i,\ i\ge5).
\]
Write \(\alpha_n=i\) when \(T_\lambda^n(x)\in V_i\), and define \(\tau=\inf\{n\ge1:\alpha_n=4\}\). For each integer \(m\ge6\), set \(\sigma_m=\inf\{n\ge0:\alpha_n\ge m\}\) and
\[
H_m(z)=\mathbb E_\lambda\!\left[z^\tau\mathbf1_{\{\tau<\sigma_m\}}\right],\qquad 0\le z\le1,
\]
with the indicator vanishing when \(\tau=\infty\). Set \(c=z\lambda(1-\lambda)\), \(P_0=1\), \(P_1=1-c\), and \(P_{j+1}=P_j-cP_{j-1}\) for \(j\ge1\). Then for every \(m\ge6\),
\[
\boxed{H_m(z)=\frac{z(1-\lambda)P_{m-6}(z)}{P_{m-5}(z)}.}
\]
Every denominator on this range is strictly positive. Thus the coefficient of \(z^n\) is exactly \(\Pr_\lambda(\tau=n,\max_{0\le j<\tau}\alpha_j<m)\), jointly rather than marginally describing return duration and visited depth.

For every integer \(n\ge1\),
\[
\boxed{\Pr_\lambda(\tau=n)=\frac1n\binom{2n-2}{n-1}(1-\lambda)^n\lambda^{n-1}.}
\]
For each integer \(m\ge6\), if \(M=\sup_{0\le j<\tau}\alpha_j\), taking \(M=\infty\) on nonreturning paths,
\[
\boxed{\Pr_\lambda(M\ge m)=
\begin{cases}
\dfrac{q-1}{q^{m-3}-1},&\lambda\ne\frac12,\\[2mm]
\dfrac1{m-3},&\lambda=\frac12,
\end{cases}\qquad q=\frac{1-\lambda}{\lambda}.}
\]
The probability of never returning is \(0\) for \(\lambda\le1/2\), and \((2\lambda-1)/\lambda\) for \(\lambda>1/2\).

For fixed \(t,u>0\), as \(\varepsilon\downarrow0\), with \(\lambda_{\pm}=\frac12\pm\varepsilon\), the **two critical crossover functions** are
\[
\boxed{\begin{aligned}
\lim_{\varepsilon\downarrow0}\varepsilon^{-1}\Pr_{\lambda_-}
  (\tau>\lfloor t/\varepsilon^2\rfloor)
 &=\frac1{2\sqrt\pi}\int_t^\infty v^{-3/2}e^{-4v}\,dv,\\
\lim_{\varepsilon\downarrow0}\varepsilon^{-1}\Pr_{\lambda_+}
  (\tau>\lfloor t/\varepsilon^2\rfloor)
 &=4+\frac1{2\sqrt\pi}\int_t^\infty v^{-3/2}e^{-4v}\,dv,\\
\lim_{\varepsilon\downarrow0}\varepsilon^{-1}\Pr_{\lambda_-}
  (M\ge\lfloor u/\varepsilon\rfloor)
 &=\frac4{e^{4u}-1},\\
\lim_{\varepsilon\downarrow0}\varepsilon^{-1}\Pr_{\lambda_+}
  (M\ge\lfloor u/\varepsilon\rfloor)
 &=\frac4{1-e^{-4u}}.
\end{aligned}}
\]
In particular, at the critical parameter \(\lambda=1/2\), \(\Pr(\tau=n)\sim(2\sqrt\pi)^{-1}n^{-3/2}\) and \(\Pr(\tau>n)\sim(\pi n)^{-1/2}\). These two asymptotics and the exact depth tail show distinct time and spatial excursion scales.

## Assumptions and scope

All probabilities refer to **Lebesgue-uniform initial points in \(V_5\)**, not to a stationary distribution. The formula for \(T_\lambda\) on cells \(V_i\) with \(i\ge5\) is the original auxiliary map's corresponding branch; the map's other branches are immaterial before the stopping event. A first visit to a cell with index below five must land in \(V_4\), since the index can decrease by at most one in one iteration. Parameter \(\lambda\) ranges over the entire open interval \((0,1)\), and the ceiling index satisfies \(m\ge6\). The generating-function variable is real with \(0\le z\le1\); no analytic continuation assertion is needed. Null sets of boundary points have no effect on the probability laws. A nonreturning orbit is assigned \(\tau=\infty\) and \(M=\infty\).

The original bimodal map and this auxiliary map are **not semiconjugate** in the source. Consequently the stated excursion statistics belong to the auxiliary interval map alone, not automatically to physical return times of the original bimodal map. On the specified tail, the transition probabilities also coincide, after an index shift, with a previously studied countable-branch map of Bruin and Todd.

## Proof

**Exact state transitions.** For each \(i\ge5\), the affine map takes \(V_i\) onto \((0,\lambda^{i-2}]\), and the fraction of its image falling in \(V_{i-1+r}\) is \((1-\lambda)\lambda^r\), for \(r=0,1,\ldots\). Conditional on any previously specified finite itinerary, the current position is uniform in its Markov cell: each relevant inverse branch is an affine bijection onto the whole target cell and sends uniform measure to uniform measure. Induction therefore yields a Markov state process with transitions
\[
\alpha_{n+1}=\alpha_n-1+R_n,\qquad
\Pr(R_n=r)=(1-\lambda)\lambda^r\quad(r\ge0),
\]
where the \(R_n\) are independent until absorption at \(4\).

**Joint duration-and-ceiling transform.** For \(4\le i<m\), let \(f_i(z)=\mathbb E_i[z^\tau\mathbf1_{\{\tau<\sigma_m\}}]\), with the hitting time now taken from the current state, and impose \(f_4=1\), \(f_i=0\) for \(i\ge m\). Put \(a=z(1-\lambda)\). The Markov recurrence is
\[
f_i=a\sum_{r\ge0}\lambda^r f_{i-1+r},\qquad 5\le i<m.
\]
At the highest allowed state, \(f_{m-1}=a(f_{m-2}+\lambda f_{m-1})\). For \(5\le i\le m-2\), subtracting \(\lambda\) times the equation at \(i+1\) gives \(f_i-\lambda f_{i+1}=af_{i-1}\). Beginning with \(f_{m-1}\), backward substitution gives \(f_{m-1-j}=f_{m-1}P_j/a^j\), where \(P_0=1\), \(P_1=1-a\lambda\), and \(P_{j+1}=P_j-a\lambda P_{j-1}\). The boundary condition \(f_4=1\) yields the displayed formula for \(f_5=H_m\); \(z=0\) follows by continuity. Positivity of its denominator follows from the roots \(r_\pm=(1\pm\sqrt{1-4c})/2\) of the polynomial recurrence: for distinct roots, \(P_j=(r_+^{j+2}-r_-^{j+2})/(r_+-r_-) >0\), and for the repeated root it is \((j+2)2^{-j-1}>0\).

**Catalan first passage.** From state five to four in exactly \(n\) steps, the nonnegative integer increments must satisfy \(\sum_{j=1}^n R_j=n-1\), and all earlier partial sums of \(R_j-1\) must be nonnegative. The cyclic lemma gives precisely one valid cyclic ordering for every orbit of cyclic permutations of such an \(n\)-tuple. There are \(\binom{2n-2}{n-1}/n\) valid sequences. All have probability \((1-\lambda)^n\lambda^{n-1}\), proving the formula. Equivalently the unrestricted transform solves \(H=z(1-\lambda)/(1-\lambda H)\), so
\[
H(z)=\frac{1-\sqrt{1-4\lambda(1-\lambda)z}}{2\lambda}.
\]
Its value at \(z=1\) gives the nonreturn probability. At \(\lambda=1/2\), Stirling's formula gives the two displayed critical duration tails, whose exponents force infinite mean return time.

**Maximum index.** Each finite strip of states \(5,\ldots,m-1\) has a uniform positive probability of reaching \(4\) within at most \(m-5\) steps, so the first exit from the strip occurs almost surely. For \(q=(1-\lambda)/\lambda\ne1\), the function \(i\mapsto q^i\) is harmonic for the unrestricted step law because \(\mathbb E[q^{R-1}]=1\). At the first upward crossing of \(m\), the overshoot is geometrically distributed with parameter \(1-\lambda\), conditionally independent of the crossing state, and \(\mathbb E[q^{\mathrm{overshoot}}]=q\). Applying the harmonic optional-stopping identity at the finite-strip exit gives
\[
q^5=(1-p_m)q^4+p_m q^{m+1},\qquad p_m=\Pr(M\ge m),
\]
which rearranges to the exact height formula. At \(\lambda=1/2\), the state index itself is harmonic and the mean overshoot is one, so \(5=4(1-p_m)+(m+1)p_m\). Truncation and the geometric overshoot's finite exponential moment justify the stopped expectations. Also \(p_m=1-H_m(1)\) directly checks consistency.

**Critical crossover.** Set \(\lambda=\frac12\pm\varepsilon\). Then \(q=1\mp4\varepsilon+O(\varepsilon^2)\). Substitution into the exact height formula with \(m=\lfloor u/\varepsilon\rfloor\) proves both depth limits. For durations, the Catalan coefficient has, uniformly when \(n\varepsilon^2\) stays in compact positive intervals,
\[
\Pr(\tau=n)=\frac{1+o(1)}{2\sqrt\pi}\,n^{-3/2}e^{-4n\varepsilon^2}.
\]
A bound by a constant times \(n^{-3/2}e^{-4n\varepsilon^2}\) controls the infinite upper tail, so summation for \(n>t/\varepsilon^2\) is a Riemann sum converging to the displayed integral. On the supercritical side, the exact nonreturn mass is \((2\lambda-1)/\lambda=4\varepsilon+O(\varepsilon^2)\); it produces the additional constant four.

## Verification

The accompanying standard-library script `artifacts/verify.py` checks Catalan first-hit probabilities by exact path counting, bounded-ceiling generating functions by direct rational linear-system solutions, the analytic polynomial ratio at several rational \(\lambda,z\) and ceiling indices, and both depth-critical crossover branches numerically at two small perturbations. It reports `EXACT_CATALAN_HEIGHT_AND_GENERATING_FUNCTION_CHECK_OK` and `FINITE_SCALING_CHECK_OK`. Its finite tests neither enumerate infinite orbits nor replace the preceding proofs. All dependencies are contained in Python's standard library.

## Relationship to prior work

Ji and Ma (2023) define \(T_\lambda\), its cell partition, and the transition matrix, using the chain for conservativity/dissipativity of their auxiliary model and a related induced bimodal system. Their full article was checked through the last section and does not state the finite-ceiling **joint return-time/max-index** transform or the exact two-observable critical-window result. Bruin and Todd's earlier infinitely branched interval map (2011 arXiv preprint; later revision) has *the same Markov tail after index translation*. Their sections on invariant measures and an appendix with critical binomial matrix identities therefore give strong background and partial combinatorial coverage; these are not represented as new. Their inspected full text does not supply the bivariate finite-ceiling first-passage transform. Classical cycle-lemma and geometric-offspring branching-process theory already furnish the unbounded Catalan marginal. García-Millán, Font-Clos, and Corral (2015) give the general critical survival crossover for Galton–Watson generations: the height marginal here matches a geometric-offspring specialization. These earlier facts are credited, not repackaged as independent discoveries. The contribution isolated here is the explicit complete finite-ceiling transform for the interval-map tail, joining **duration and maximum Markov depth**, with its mutually consistent parameter scaling. Literature equivalence outside these inspected sources remains possible.

## Limitations

Only Lebesgue-uniform starts in the fifth cell are treated. The findings concern the auxiliary stopped Markov map, **not** return statistics of the original Fibonacci bimodal maps; a semiconjugacy is unavailable. The joint distribution is encoded by the exact rational transform; no independent closed-form expression for each individual bivariate coefficient is claimed beyond coefficient extraction. The parameter-window limits are pointwise for each fixed \(t,u>0\), not uniform at zero. Every parameter-independent conclusion uses the analytic arguments above, and no claim of publication priority or external independent validation is made.

## References

1. H. Ji and W. Ma, *Phase transition for piecewise linear fibonacci bimodal map*, AIMS Mathematics **8** (2023), 8403–8430, DOI: 10.3934/math.2023424, public source dated 2023-02-03; full text: https://www.aimspress.com/aimspress-data/math/2023/4/PDF/math-08-04-424.pdf.
2. H. Bruin and M. Todd, *Transience and thermodynamic formalism for infinitely branched interval maps*, arXiv:1104.5452; full text: https://arxiv.org/pdf/1104.5452 (original preprint 2011; version inspected 2019).
3. R. García-Millán, F. Font-Clos, and Á. Corral, *Finite-size scaling of survival probability in branching processes*, Physical Review E **91** (2015), 042122, DOI: 10.1103/PhysRevE.91.042122; open text: https://fontclos.github.io/files/Garcia-Millan_2015_Finite_size_branchings.pdf.
