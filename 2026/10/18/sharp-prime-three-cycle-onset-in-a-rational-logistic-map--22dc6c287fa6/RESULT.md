# Sharp prime-three-cycle onset in a rational logistic map

## Finding

For the rational map
\[
K_\mu(x)=\frac{\mu x(1-x)}{1+x},\qquad x\in[0,1],\quad 0<\mu\le 3+2\sqrt2,
\]
let \(\mu_*\) be the unique root greater than \(1\) of
\[
A(\mu)=\mu^4-4\mu^3-10\mu^2+4\mu+1=0.
\]
Then \(5.641<\mu_*<5.642\), numerically \(\mu_*\approx5.64136371874529\). The **complete prime-period-three point count** is
\[
\#\{x\in[0,1]:K_\mu^3(x)=x,\ K_\mu(x)\ne x\}=
\begin{cases}
0,&0<\mu<\mu_*,\\
3,&\mu=\mu_*,\\
6,&\mu_*<\mu\le3+2\sqrt2.
\end{cases}
\]
Thus the threshold supports exactly one neutral three-cycle, while every larger admissible parameter supports exactly two distinct three-cycles. At the threshold, the product of the three derivatives around the orbit is exactly \(+1\). These assertions count *all* prime-period-three points, not merely attracting or numerically visible cycles.

## Assumptions and scope

The domain is the full closed interval \([0,1]\) with \(\mu>0\). The critical point is \(\sqrt2-1\), and the maximum of \(K_\mu\) on the interval is \(\mu(3-2\sqrt2)\). Consequently \(K_\mu:[0,1]\to[0,1]\) precisely for \(0<\mu\le3+2\sqrt2\); this is the complete interval-map parameter range used here. A point of *prime period three* satisfies \(K_\mu^3(x)=x\) but \(K_\mu(x)\ne x\). No statistical or topological characterization of all other orbits is asserted.

## Proof

**1. Dynatomic numerator and its denominator.** Put \(m=\mu\) for the displayed coefficients. Define the successive rational numerators and denominators by
\[
N_1=m x(1-x),\quad D_1=1+x,\quad
N_2=mN_1(D_1-N_1),\quad D_2=D_1(D_1+N_1).
\]
Thus \(K_m=N_1/D_1\), \(K_m^2=N_2/D_2\), and straightforward rational cancellation gives
\[
\frac{K_m^3(x)-x}{K_m(x)-x}
=\frac{P_m(x)}{(D_1+N_1)(D_2+N_2)}
\]
where, away from fixed points, the numerator is the following *degree-six* polynomial. As a polynomial identity the numerator remains defined at fixed points:
\[
P_m(x)=\sum_{j=0}^{6}c_j(m)x^j,
\]
\[
\begin{aligned}
c_0&=m^2+m+1,\\
c_1&=-(m^2-3)(m^2+m+1),\\
c_2&=(m^2+m+1)(2m^3-2m^2-2m+3),\\
c_3&=-m^6-3m^5+3m^4+2m^3-3m^2-3m+1,\\
c_4&=m(m^2-m+1)(3m^3+2m^2-2m-2),\\
c_5&=-m^2(3m^2-1)(m^2-m+1),\\
c_6&=m^4(m^2-m+1).
\end{aligned}
\]
For all admissible \(m\), each of \(D_1\), \(D_1+N_1\), \(D_2\) and \(D_2+N_2\) is positive on \([0,1]\), since \(K_m(x)\), then \(K_m^2(x)\), are nonnegative. Hence there are no spurious roots from denominator poles. At the two possible fixed points, \(0\) and \((m-1)/(m+1)\), direct substitution gives
\[
P_m(0)=m^2+m+1>0,
\]
\[
P_m\left(\frac{m-1}{m+1}\right)
=\frac{16m^4 B(m)}{(m+1)^6}>0,
\quad B(m)=m^4-6m^3+10m^2+6m+1
=(m^2-3m-1)^2+3m^2.
\]
Thus for \(m>1\), the zeros of \(P_m\) in \([0,1]\) are exactly the prime-period-three points, with multiplicities preserved in the polynomial equation.

**2. Algebraic collision parameters.** Exact polynomial elimination yields
\[
\begin{aligned}
\operatorname{Disc}_x(P_m)={}&256m^{16}(m^2-m+1)^2(m^2+m+1)^2\\
&\quad\cdot B(m)^2 A(m)^3.
\end{aligned}
\]
For \(m>0\), every displayed factor except \(A(m)\) is strictly positive. Descartes' rule gives at most two positive roots of \(A\). Since \(A(1/2)=1/16>0\), \(A(1)=-8<0\), and \(A(23/4)=6673/256>0\), there are exactly two, one between \(1/2\) and \(1\), and the other \(\mu_*\in(1,23/4)\). The latter is therefore the *sole possible* collision parameter for primitive three-cycles in \(m>1\).

**3. Rigorous six-root witness.** At the rational parameter \(m=23/4\), each of the six disjoint open intervals
\[
\begin{aligned}
&(725/10000,726/10000),\quad (1062/10000,1063/10000),\\
&(3606/10000,3607/10000),\quad (4935/10000,4936/10000),\\
&(9623/10000,9624/10000),\quad (9744/10000,9745/10000)
\end{aligned}
\]
contains a zero of \(P_m\). This follows from **exact rational signs**, alternating \((+,-),(-,+),(+,-),(-,+),(+,-),(-,+)\) at the six successive endpoint pairs. A degree-six polynomial has at most six roots counting multiplicity, so there are exactly six simple roots in \((0,1)\) at that parameter.

**4. Complete parameter count.** For \(0<m\le1\), \(K_m(x)<x\) for \(x\in(0,1]\), excluding all nontrivial periodic orbits. For \(m>1\), roots of \(P_m\) cannot enter or leave \([0,1]\) through an endpoint because \(P_m(0)=m^2+m+1\) and \(P_m(1)=8\) never vanish. They cannot cross into a fixed point because the two fixed-point substitutions in Step 1 are nonzero. Away from the unique discriminant root \(\mu_*\), all polynomial roots are simple and vary continuously, so their number in \((0,1)\) is constant on \((1,\mu_*)\) and \((\mu_*,3+2\sqrt2]\). The count is zero in the first component (by continuity from \(m=1\)) and six in the second (by Step 3).

**5. Threshold multiplicities and multiplier.** Let \(m\downarrow\mu_*\) from above. The six roots remain in the closed interval, and any limit is a root of \(P_{\mu_*}\); the fixed-point exclusions in Step 1 show that no limiting three-cycle can collapse to a fixed point. Because the discriminant vanishes, at least one limit root of \(P_{\mu_*}\) has multiplicity at least two. Its two forward images belong to the same prime-three orbit and have the same multiplicity, because local conjugation along that cycle is a diffeomorphism whenever a root of \(K_{\mu_*}^3(x)-x\) is multiple (its derivative must be one, so each branch derivative is nonzero). Thus the degree-six polynomial has exactly three distinct roots, each of multiplicity two. Differentiating \(K_{\mu_*}^3(x)-x\) at any of them gives \((K_{\mu_*}^3)'(x)-1=0\), proving the neutral multiplier \(+1\). The three points form precisely one prime-three cycle. This completes the all-parameter classification.

## Verification

The accompanying standalone `verify.py` uses exact symbolic rational-function arithmetic to reconstruct \(P_m\), confirm each coefficient, verify the complete discriminant factorization, confirm both fixed-point substitutions, and evaluate all six rational sign brackets exactly. It also checks the exact sign bracketing of the threshold polynomial. These computations certify the finite polynomial identities and exact finite sign witness; the continuation and collision arguments in Steps 4–5 are the analytical proof of the infinite parameter statement.

## Relationship to prior work

Kumar, Alzabut, Kumari, Rani and Chugh (2022) introduced this exact rational map and studied fixed points, period-doubling plots, Lyapunov exponents and numerical chaotic windows. Their complete accessible article gives approximate transitions near \(\mu\approx5.21\), not this prime-three dynatomic classification. Conejero, Lizama and Quijada (2025) included the same map as the endpoint of a family \(\mu x(1-x)/(1+\lambda x)\), again studying fixed-point stability and numerical bifurcations, not the exact prime-three boundary or count. This result is different from a general theorem *about* period three: it computes the parameter and **all** prime-three points of this particular rational family. By the classical period-three implications for continuous interval maps, the exact threshold also locates a parameter at which the all-period phenomenon is guaranteed; it does *not* locate the first onset of positive entropy or visually observed chaos.

## Limitations

The theorem is restricted to \(0<\mu\le3+2\sqrt2\), the full range where this particular map preserves \([0,1]\). It counts exactly prime-period-three points but not higher-period orbit counts, basins, stability of the two post-threshold cycles, or an onset of chaos. The polynomial discriminant identity is exact; the decimal approximation is informational only. Priority against every conceivable historical equivalent parameterization is not certified, and independent mathematical auditing is not claimed.

## References

1. A. Kumar, J. Alzabut, S. Kumari, M. Rani and R. Chugh, *Dynamical properties of a novel one dimensional chaotic map*, Mathematical Biosciences and Engineering **19** (2022), 2489–2505. Published 7 January 2022. DOI: 10.3934/mbe.2022115. https://www.aimspress.com/aimspress-data/mbe/2022/3/PDF/mbe-19-03-115.pdf
2. J. A. Conejero, C. Lizama and D. Quijada, *Dynamical Properties for a Unified Class of One-Dimensional Discrete Maps*, Mathematics **13** (2025), 518. DOI: 10.3390/math13030518. https://riunet.upv.es/server/api/core/bitstreams/187e1322-d70a-46c0-9fe1-6eb964e699cc/content
3. A. N. Sharkovsky, *Co-existence of cycles of a continuous mapping of the line into itself* (1964), classical period-forcing theorem. The all-period corollary is not a new result.
