# Sharp interaction-order threshold for arbitrarily many attracting endemic prevalences

## Finding

For a homogeneous higher-order susceptible–infected–susceptible (SIS) prevalence equation with strictly positive infection pressure from every group size up to a largest size, the maximum number of *simultaneously locally asymptotically stable, strictly positive endemic equilibria* is exactly
\[
\left\lceil\frac{M}{2}\right\rceil,
\]
where \(M\) is the largest number of infectious neighbours participating in one transmission event, so the largest interaction contains \(M+1\) individuals. This sharp count holds for every integer \(M\ge1\), despite the requirement that **all** interaction-order infection rates be strictly positive.

There is an explicit rational inverse construction of exactly \(M\) distinct hyperbolic endemic equilibria at any prescribed ordered prevalences \(0<r_1<\cdots<r_M<1\) satisfying \(\sum_{j=1}^{M}r_j\le1/2\). The equilibria alternate between attracting and repelling, giving the sharp number of attractors. Consequently, \(2k\)-body interactions are both necessary and sufficient to obtain \(k\) simultaneous strictly positive attracting endemic prevalences in this scalar family. In particular, six-body interactions are minimal for three endemic attractors, even on a homogeneous fully connected structure without communities or heterogeneous groups.

## Assumptions and scope

Fix an integer \(M\ge1\), recovery rate \(\gamma>0\), and strictly positive scaled infection rates \(\beta_j>0\) for every \(j=1,\ldots,M\). Let the fraction infectious be \(y(t)\in[0,1]\), governed by the deterministic autonomous scalar ODE
\[
\dot y=f(y):=-\gamma y+(1-y)\sum_{j=1}^{M}\beta_j y^j
=y\left[(1-y)Q(y)-\gamma\right],\qquad
Q(y)=\sum_{j=1}^{M}\beta_j y^{j-1}.
\]
The \(j\)-th term is the infection pressure contributed by groups of size \(j+1\), with exactly \(j\) infectious neighbours of a susceptible. In the notation of the higher-order complete-simplicial SIS mean-field equation in Kiss et al. (2023), the rescaled simplicial infectivity is \(s_j=j!\beta_j>0\). The interval \([0,1]\) is forward invariant because \(f(0)=0\) and \(f(1)=-\gamma<0\).

An *endemic equilibrium* is a constant solution \(y_*=r\in(0,1)\). Local asymptotic stability always refers to the scalar deterministic flow, not to a finite-population absorbing Markov chain. We do not assume small infectivity, monotone dose–response beyond positivity of \(\beta_j\), or a special initial condition.

## Proof

**1. Universal upper bound, including degenerate equilibria.** A strictly positive equilibrium \(r\) is a zero of
\[
h(y)=(1-y)Q(y)-\gamma.
\]
Since \(\beta_M>0\), this is a nonzero polynomial of degree exactly \(M\) and leading coefficient \(-\beta_M\); hence there are at most \(M\) distinct endemic equilibria. At a locally asymptotically stable interior equilibrium of any one-dimensional polynomial flow, the vector field is positive immediately to its left and negative immediately to its right. This property remains true if the zero is nonhyperbolic, because an even-multiplicity zero is not attracting from both sides and an odd-multiplicity attracting zero has the stated signs. Between any two successive attracting equilibria the sign therefore must change back from negative to positive, requiring at least one additional equilibrium. Thus \(k\) distinct attracting endemic equilibria require at least \(2k-1\) distinct zeros of \(h\), giving
\[
2k-1\le M,\qquad k\le\left\lceil\frac M2\right\rceil.
\]

**2. Inverse construction obeying every positivity constraint.** Prescribe any strictly ordered \(0<r_1<\cdots<r_M<1\) with \(\sum_jr_j\le1/2\), and set
\[
R(y)=\prod_{j=1}^{M}(y-r_j),\qquad C=R(1)=\prod_{j=1}^{M}(1-r_j)>0,
\]
\[
\gamma=1,\qquad Q(y)=\frac{1-R(y)/C}{1-y}.
\]
Because the numerator vanishes at \(y=1\), \(Q\) is a polynomial of degree exactly \(M-1\). It remains essential to prove that **all** its coefficients are positive; an arbitrary real polynomial with prescribed roots would not establish admissible contagion rates.

Write \(e_s=e_s(r_1,\ldots,r_M)>0\) for elementary symmetric sums, with \(e_0=1\). Polynomial division yields, for every \(0\le j\le M-1\),
\[
[y^j]Q(y)=\frac1C\sum_{s=0}^{M-j-1}(-1)^s e_s.
\]
For \(S=\sum_j r_j\le1/2\), each \(e_s\le S^s\) since the expansion of \(S^s\) contains each product of \(s\) distinct roots as a nonnegative term. Consequently,
\[
0<\sum_{s=1}^{M}e_s\le\sum_{s=1}^{M}2^{-s}<1.
\]
It follows, term by term, that
\[
[y^j]Q(y)\ge\frac{1-\sum_{s=1}^{M}e_s}{C}>0.
\]
Thus defining \(\beta_{j+1}=[y^j]Q(y)\) gives strictly positive infection rates at **every** order. The full vector field simplifies identically to
\[
f(y)=y[(1-y)Q(y)-1]=-\frac{yR(y)}{C}.
\]
The endemic equilibria are precisely the \(M\) prescribed roots, all in \((0,1)\). They are hyperbolic because
\[
f'(r_j)=-\frac{r_j}{C}\prod_{\ell\ne j}(r_j-r_\ell),\qquad
\operatorname{sgn}f'(r_j)=(-1)^{M-j+1}.
\]
Hence those with \(j\equiv M\pmod2\) are attracting and all others are repelling. There are exactly \(\lceil M/2\rceil\) attracting endemic states. The roots and strict positivity persist under sufficiently small perturbations of all infection rates, so sharpness is not confined to an equality or a zero-rate face of parameter space.

**3. Explicit rational witness and minimal group size.** For any \(M\ge1\), the choices
\[
r_j=\frac{j}{M(M+1)},\qquad 1\le j\le M,
\]
obey \(\sum_j r_j=1/2\) and give positive rational coefficients by the preceding proof. For \(M=5\), the required complete set of infection rates, in the order of pair, triple, quadruple, quintuple and six-body interactions, is
\[
(\beta_1,\beta_2,\beta_3,\beta_4,\beta_5)
=\left(\frac{118756}{118755},\frac{5275}{5278},
\frac{2675}{2639},\frac{2250}{2639},\frac{4500}{2639}\right),
\]
with \(\gamma=1\). Here \(C=2639/4500\), the five endemic equilibria are exactly
\[
\frac1{30},\ \frac1{15},\ \frac1{10},\ \frac2{15},\ \frac1{6},
\]
and the three attracting prevalences are \(1/30\), \(1/10\), and \(1/6\). The disease-free state is repelling in this example since \(\beta_1>\gamma\). For \(M\le4\), the first part bounds the number of endemic attractors by two. For any requested \(k\ge1\), the maximum allowed infectious-neighbour order must satisfy \(M\ge2k-1\), equivalently a maximum group size of at least \(2k\); the construction at \(M=2k-1\) attains it.

## Verification

The bundled self-contained `verify.py`, using only Python's standard-library exact `fractions.Fraction` arithmetic, reconstructs \(R\), divides by \(1-y\), confirms strict positivity of all coefficients, checks the complete polynomial vector-field identity, evaluates every rational equilibrium and the sign of its nonzero derivative, and asserts the displayed five-rate witness. It ran successfully for each integer \(M=1,\ldots,18\). These finite exact checks corroborate the algebra; the unrestricted \(M\) statement follows from the preceding proof rather than from finite enumeration.

## Relationship to prior work

Kiss, Iacopini, Simon and Georgiou (2023), arXiv:2309.12752v1, §II.C and §IV, formulate the arbitrary-order complete-simplicial mean-field equation and analyse up to four-body contagion. On manuscript p.14 (PDF p.14), they explicitly anticipate arbitrary numbers of positive endemic states as interaction order increases, without establishing a sharp all-order positive-rate realization or a stable-state count. The present result settles that specific deterministic question using a positivity-preserving polynomial inverse design; it neither proves their separately conjectured general hydrodynamic limit nor extends the stochastic claims to all orders.

The later Kiss–Bick–Simon study (arXiv:2410.15330v1; 2025 journal version) classifies three-/four-body scalar models and a two-population model, but its §§3–4 do not give this arbitrary-order sharp bound and construction. Iacopini et al. (2019) establish disease-free/endemic bistability for simplicial social contagion. Ferraz de Arruda et al. (2021 preprint; 2023 journal version) produce multistability and intermittency in community-structured critical-mass hypergraphs, using a different transmission rule. Alexandersen et al. (arXiv:2608.26528v1) obtain polynomial-degree bounds and several endemic attractors in a **coupled infection–activity feedback** system, not the positive-coefficient scalar complete-simplicial SIS family. These antecedents motivate and delimit, rather than imply, the strict-positive-rate inverse realization given here.

## Limitations

The theorem is restricted to a scalar autonomous homogeneous mean-field SIS ODE with finitely many positive group infection rates. Its count excludes the disease-free equilibrium and says nothing about transient quasi-stationary distributions, stochastic extinction at finite population size, graph heterogeneity, delayed feedback, diffusion, or global bifurcation classification throughout coefficient space. The explicit equilibria can lie close together and have weak linear attraction; no uniform robustness margin independent of \(M\) is claimed. The construction prescribes arbitrary **small-sum** ordered endemic levels, not arbitrary prescribed levels throughout \((0,1)\). No general-order finite-network hydrodynamic convergence is asserted.

## References

1. I. Z. Kiss, I. Iacopini, P. L. Simon, N. Georgiou, “Insights from exact social contagion dynamics on networks with higher-order structures,” *Journal of Complex Networks* **11** (2023), cnad044; first public arXiv:2309.12752v1 (22 September 2023), https://arxiv.org/abs/2309.12752 ; doi:10.1093/comnet/cnad044.
2. I. Z. Kiss, C. Bick, P. L. Simon, “Decoding how higher-order network interactions shape contagion dynamics,” *Journal of Mathematical Biology* **91** (2025), 29; first public arXiv:2410.15330v1 (20 October 2024), https://arxiv.org/abs/2410.15330 ; doi:10.1007/s00285-025-02247-4.
3. I. Iacopini, G. Petri, A. Barrat, V. Latora, “Simplicial models of social contagion,” *Nature Communications* **10** (2019), 2485, https://arxiv.org/abs/1810.07031.
4. G. Ferraz de Arruda, G. Petri, P. Martín Rodriguez, Y. Moreno, “Multistability, intermittency and hybrid transitions in social contagion models on hypergraphs,” *Nature Communications* **14** (2023), 1375, first public arXiv:2112.04273v1 (8 December 2021), https://arxiv.org/abs/2112.04273.
5. C. G. Alexandersen et al., “Hysteresis and multistability in network spreading with neuronal activity feedback,” arXiv:2608.26528v1 (2026), https://arxiv.org/abs/2608.26528.
