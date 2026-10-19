# Discontinuous rare-sublattice enhancement of trimer parking on an alternating line

## Finding

Consider irreversible deposition of length-three lattice rods (trimers) on the integer line. A trimer starting at an even site is attempted at rate one; a trimer starting at an odd site is attempted at rate \(\varepsilon\ge0\), independently across starts. The initially empty substrate accepts an attempted trimer exactly when all its three sites are vacant. Let \(J(\varepsilon)\) be the limiting expected vacant-site density as deposition time tends to infinity.

**Theorem.** The following exact one-sided limit and discontinuity hold:
\[
J(0)=\frac14+\frac34e^{-2},\qquad
\lim_{\varepsilon\downarrow0,\;\varepsilon>0}J(\varepsilon)=\frac14-\frac34e^{-2},\qquad
J(0)-\lim_{\varepsilon\downarrow0}J(\varepsilon)=\frac32e^{-2}>0.
\]
Numerically the two endpoint densities are \(0.351501462427\ldots\) and \(0.148498537573\ldots\), a jump of \(0.203002924855\ldots\). Thus an arbitrarily rare but positive odd-start flux has a nonvanishing effect on final coverage. In particular, its limiting vacancy is smaller than the homogeneous-rate value \(J(1)=0.176347036823\ldots\).

For every \(\varepsilon>0\), the entire time-dependent expected coverage is determined by a **three-equation linear system**, given and proved below. The singular limit is taken **after** the infinite-time jamming limit; exchanging these two limits yields the first displayed value instead of the second.

## Assumptions and scope

Each start \(i\in\mathbb Z\) has its own independent Poisson arrival process. If an arrival is rejected, that start can be attempted again, but no later arrival can succeed once an earlier attempt was rejected, because occupancy only increases. Equivalently one may assign one independent exponential first-arrival clock per start, with rate one on even sites and rate \(\varepsilon\) on odd sites. At \(\varepsilon=0\) odd starts never arrive. A finite-time configuration is well defined by standard finite-range graphical construction; the law is invariant under translation by two sites.

Write \(E_{n,s}(t)\) for the probability that the \(n\) consecutive sites starting at parity \(s\in\{0,1\}\) are empty at time \(t\). These probabilities are bounded between zero and one; at time zero all equal one. Let \(\lambda_0=1\), \(\lambda_1=\varepsilon\), and \(L=1+\varepsilon\). Site vacancy density is \(v(t)=(E_{1,0}(t)+E_{1,1}(t))/2\), and \(J(\varepsilon)=\lim_{t\to\infty}v(t)\). Since vacancies can only disappear, this limit exists.

## Proof

**1. Exact empty-interval equations.** For each \(n\ge2\), a trimer that intersects an empty interval of size \(n\) starts at one of \(n+2\) possible positions. Conditional on all required sites being empty, the blocked interval together with that trimer has length \(n\), \(n+1\), or \(n+2\). Summing its rate gives, for \(m\ge1\),
\[
\begin{aligned}
\dot E_{2m,s}&=-L(m-1)E_{2m,s}-L E_{2m+2,s}
 -\lambda_0 E_{2m+1,0}-\lambda_1 E_{2m+1,1},\\
\dot E_{2m+1,s}&=-[m\lambda_s+(m-1)\lambda_{1-s}]E_{2m+1,s}
 -2\lambda_s E_{2m+3,s}
 -\lambda_{1-s}(E_{2m+2,0}+E_{2m+2,1}).
\end{aligned}
\]
The first equation is the same for both parities apart from its own diagonal term; equality of the two even-length probabilities therefore follows by bounded uniqueness. The direct one-site equation is
\[
\dot E_{1,s}=-2\lambda_s E_{3,s}-\lambda_{1-s}E_{3,1-s},
\qquad \dot v=-\frac32(\lambda_0 E_{3,0}+\lambda_1 E_{3,1}).
\]
These are identities of the exact infinite-volume adsorption process, not mean-field closures.

**2. Finite-dimensional reduction.** Set \(z(t)=e^{-Lt}\) and define \(A,B_0,B_1\) by
\[
 E_{2m,s}(t)=z(t)^{m-1}A(t),\qquad
 E_{2m+1,s}(t)=z(t)^{m-1}e^{-\lambda_st}B_s(t).
\]
Substituting into the interval equations yields the closed system
\[
\begin{aligned}
 A'&=-LzA-e^{-t}B_0-\varepsilon e^{-\varepsilon t}B_1,\\
 B_0'&=-2zB_0-2\varepsilon e^{-\varepsilon t}A,\\
 B_1'&=-2\varepsilon zB_1-2e^{-t}A,
\end{aligned}\qquad A(0)=B_0(0)=B_1(0)=1.
\]
This solution is nonnegative and componentwise nonincreasing, as follows either from its probabilistic representation or by the original positive empty-interval system. The equation for the vacant fraction integrates to
\[
 J(\varepsilon)=1-\frac32\int_0^\infty
       \left[e^{-t}B_0(t)+\varepsilon e^{-\varepsilon t}B_1(t)\right]dt.
\]
To justify that the ansatz solves the actual hierarchy, apply bounded uniqueness: the difference of two bounded solutions to the infinite interval equations, with zero initial conditions, has an integral inequality involving at most four off-diagonal terms and coefficients bounded uniformly in interval size. Iterating \(k\) times bounds each fixed difference on \([0,T]\) by \(2(4\max\{1,\varepsilon\}T)^k/k!\), which tends to zero. Diagonal terms are harmless by integrating factors. The explicit ansatz is bounded, so uniqueness applies.

**3. The zero-rate formula.** At \(\varepsilon=0\), the three-equation solution simplifies to
\[
 A_0(t)=B_{0,0}(t)=B_{1,0}(t)=\exp[-2(1-e^{-t})].
\]
Consequently
\[
 \int_0^\infty e^{-t}B_{0,0}(t)\,dt
 =\int_0^1 e^{-2(1-x)}dx=\frac{1-e^{-2}}2,
\]
while the odd-start integral vanishes identically. This proves \(J(0)=1/4+3e^{-2}/4\).

**4. The positive-rate singular limit.** Dependence of the finite-dimensional ODE on \(\varepsilon\) is continuous uniformly on compact time intervals, so \((A_\varepsilon,B_{0,\varepsilon},B_{1,\varepsilon})(t)\) converges to the preceding zero-rate solution at each fixed \(t\). Bounded convergence gives
\[
 \lim_{\varepsilon\downarrow0}\int_0^\infty e^{-t}B_{0,\varepsilon}(t)\,dt
 =\frac{1-e^{-2}}2.
\]
For the rare-rate term, integrate the third ODE:
\[
 B_{1,\varepsilon}(t)=1-2\varepsilon\int_0^t e^{-(1+\varepsilon)s}B_{1,\varepsilon}(s)ds
 -2\int_0^t e^{-s}A_\varepsilon(s)ds.
\]
The first integral multiplied by \(2\varepsilon\) is at most \(2\varepsilon/(1+\varepsilon)\), uniformly in time. For each fixed \(u>0\), the upper limit \(u/\varepsilon\) tends to infinity, and bounded convergence for the second integral gives
\[
 \lim_{\varepsilon\downarrow0}B_{1,\varepsilon}(u/\varepsilon)
 =1-2\int_0^\infty e^{-s}A_0(s)ds=e^{-2}.
\]
On substituting \(u=\varepsilon t\) and applying bounded convergence once again,
\[
 \lim_{\varepsilon\downarrow0}\int_0^\infty\varepsilon e^{-\varepsilon t}B_{1,\varepsilon}(t)dt
 =\int_0^\infty e^{-u}e^{-2}du=e^{-2}.
\]
Combining the two limits proves the stated right-hand limit and jump. In the exceptional equal-rate case the ODE instead reduces to \(A=B_0=B_1=\exp[-2(1-e^{-t})-(1-e^{-2t})]\), yielding
\[
 J(1)=1-3\int_0^1e^{-3+2x+x^2}\,dx.
\]
The numerical value quoted above follows by standard one-dimensional quadrature.

**5. Structural explanation.** In the exactly zero-rate process, possible even trimer starts form the sites of a nearest-neighbor-exclusion greedy process: accepted start indices cannot be adjacent. Equivalently this is ordinary dimer parking on an auxiliary integer line. Its final vacant-site density is \(e^{-2}\) and accepted-dimer density is \((1-e^{-2})/2\). Consecutive accepted even-trimer starts can be separated by two or three auxiliary steps. A separation of two leaves one original substrate vacancy; a separation of three leaves exactly three consecutive original vacancies. These latter voids are filled by odd-start trimers on the slow time scale when any positive odd flux is present. The exact ODE proof above also establishes the required interchange of infinite-time and weak-rate limits without assuming independence among the voids.

## Verification

The standalone `verify.py` computes every overlapping-trimer union coefficient for interval lengths from two through seventeen and both start parities at unequal integer rates; these are exact integer identities. It independently integrates the three-equation system and compares the resulting vacant fractions against seeded random-priority deposition on 1000-site periodic lattices at four rate ratios. It checks the two endpoint constants and the equal-rate value. Run `python verify.py` with Python 3, NumPy, and SciPy. All packaged checks passed. These finite experiments test formulas and implementation, not the infinite-line proof; that proof is the hierarchy, uniqueness, and dominated-convergence argument above.

## Relationship to prior work

Classical one-dimensional \(k\)-mer RSA and its homogeneous vacancy laws are established background (Fan–Percus, Rodgers). Privman–Yan study a different singular perturbation: broadening the spatial landing sites changes lattice parking to continuum parking, rather than assigning a small positive Poisson arrival rate to an otherwise absent parity of exactly lattice-aligned trimer starts. Zuppa–Ciacera–Zgrablich examine cooperative deposition of dimers and trimers on heterogeneous substrates with random and patchwise topographies, by Monte Carlo; their available abstract does not provide the above parity-clock formula or a one-sided zero-clock theorem. Percus studies nonuniform flux in a nearest-neighbor-exclusion setting, which motivates caution about general reduction techniques, but the inaccessible full paper could not be conclusively compared against the present range-two trimer exclusion and its weak-rate constant. No claim of universal priority over all possible representations is made.

## Limitations

The theorem concerns expected vacant density on an infinite integer line at infinite deposition time. It does not assert a fluctuation central limit theorem, a mixing-rate estimate uniform in \(\varepsilon\), or a finite-ring finite-size scaling function. The model has fixed-length rods, no desorption, no diffusion, and a period-two fixed arrival pattern. The result is analytically proved here but has not undergone independent scientific validation. Relevant older nonuniform-flux literature unavailable in full leaves a finite bibliographic risk.

## References

1. Y. Fan and J. K. Percus, “Asymptotic coverage in random sequential adsorption on a lattice,” *Physical Review A* **44**, 5099 (1991), DOI: 10.1103/PhysRevA.44.5099; public date 1991-10-01.
2. G. J. Rodgers, “Random sequential adsorption of different-sized k-mers on a line,” *Physical Review A* **45**, 3432 (1992), DOI: 10.1103/PhysRevA.45.3432.
3. J. K. Percus, “Lattice RSA and the Gaussian-mean spherical strategy,” *Colloids and Surfaces A* **165**, 345–361 (2000), DOI: 10.1016/S0927-7757(99)00443-4.
4. C. Zuppa, M. Ciacera, and G. Zgrablich, “Cooperative Sequential Adsorption of k-mers on Heterogeneous Substrates,” *Langmuir* **15**, 5984–5989 (1999), DOI: 10.1021/la981338y.
5. V. Privman and H. Yan, “Random Sequential Adsorption on Imprecise Lattice,” arXiv:1606.01823, first posted 2016-06-06; full preprint inspected, especially Sections 1–3.
