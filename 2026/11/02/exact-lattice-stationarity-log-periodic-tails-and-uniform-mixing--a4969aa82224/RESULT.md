# Exact lattice stationarity, log-periodic tails, and uniform mixing in an accelerated random walk

## Finding

Consider the symmetric discrete-time, integer-position random walk of Lima and Curado, with the smallest permitted threshold and rule parameters. Its *exact discrete stationary law* is sparse and geometrically weighted, rather than a continuous density. Its tail has exact discrete-scale invariance with a nonconvergent multiplicative power-law coefficient, yet the chain is uniformly geometrically ergodic from every integer starting point.

Write \(a_k=3\cdot2^{k-1}-1\) for integers \(k\ge1\). There is exactly one invariant probability measure \(\pi\) on \(\mathbb Z\), and it satisfies
\[
\pi(0)=\pi(1)=\pi(-1)=\frac15,\qquad
\pi(a_k)=\pi(-a_k)=\frac{1}{5\cdot2^k}\quad(k\ge1),
\]
with zero mass at every other integer. For any real \(z\) with \(a_k\le z<a_{k+1}\), the strict stationary survival probability is
\[
S(z):=\pi\{|n|>z\}=\frac{2}{5\cdot2^k}.
\]
Consequently, for \(z\ge2\),
\[
S(2z+1)=\frac12S(z),\qquad
\liminf_{z\to\infty}zS(z)=\frac35,\qquad
\limsup_{z\to\infty}zS(z)=\frac65.
\]
In particular, there is no asymptotic constant \(c\) for which \(S(z)\sim c/z\). Stationary absolute moments obey \(\mathbb E_\pi|N|^p<\infty\) exactly for \(0<p<1\); the stationary absolute first moment diverges.

Despite this, for the transition kernel \(P\),
\[
\inf_{n\in\mathbb Z}P^4(n,\{0\})=\frac1{16},
\qquad
\sup_{n\in\mathbb Z}\|P^t(n,\cdot)-\pi\|_{\mathrm{TV}}
\le\left(\frac{15}{16}\right)^{\lfloor t/4\rfloor}
\quad(t\in\mathbb Z_{\ge0}).
\]
Here total variation is \(\sup_A|\mu(A)-\nu(A)|\). Equality in the four-step minorization occurs for the starting states \(n=\pm1\).

## Assumptions and scope

Let \((\sigma_t)_{t\ge0}\) be independent fair signs taking values \(\pm1\), and let \(N_0\in\mathbb Z\) be arbitrary. Define
\[
N_{t+1}=N_t+\sigma_t s(N_t),\qquad
s(n)=\begin{cases}1,&|n|\le1,\\ |n|+1,&|n|>1.\end{cases}
\]
This is precisely the discrete walk's original rule with integer parameters \(l=r=1\) and physical lattice increment normalized to one; the symbol \(r\) here is the source paper's positive *step-rule* parameter, not a resetting rate. No diffusion approximation, interpolation, limit in \(l\), or explicit reset operation is imposed. All uniqueness and mixing assertions concern the original transition kernel on the entire integer state space.

## Proof

**1. Reachable class and transition graph.** At \(0\) the two destinations are \(\pm1\). From \(1\) the destinations are \(0,2\), and from \(-1\) they are \(-2,0\). For any integer \(n\ge2\), the destinations are \(-1\) and \(2n+1\), each with probability \(1/2\); for \(n\le-2\), they are \(1\) and \(2n-1\). Thus the closed class reached from \(0\) is
\[
\mathcal C=\{0,1,-1\}\cup\{a_k,-a_k:k\ge1\},
\qquad a_{k+1}=2a_k+1,\quad a_1=2.
\]
Every state outside \(\mathcal C\) enters \(\mathcal C\) almost surely: successive outward moves have probability \(2^{-m}\) through \(m\) trials, and the first inward move lands in \(\pm1\). All states within \(\mathcal C\) communicate (a branch can return to \(\pm1\) and hence to \(0\)); therefore this is the only closed communicating class.

**2. Exact invariant law.** Put mass \(b\) at each of \(0,1,-1\), and mass \(b2^{-k}\) at each \(\pm a_k\). Balance at \(0\) is \(b=b/2+b/2\). Balance at \(a_1\) comes from \(1\) with probability \(1/2\), and the balance at \(a_{k+1}\) comes from \(a_k\) with probability \(1/2\); the negative branch is symmetric. The inflow at \(1\) is \(b/2\) from \(0\) plus \((b/2)\sum_{k\ge1}2^{-k}=b/2\) from negative outward states, totaling \(b\). Balance at \(-1\) is symmetric. Since \(3b+2b\sum_{k\ge1}2^{-k}=5b\), normalization gives \(b=1/5\). The closed irreducible class has a finite invariant measure and hence a unique invariant probability. Every external state hits this class almost surely, so no invariant probability gives external states positive mass. This proves existence and uniqueness on \(\mathbb Z\).

**3. Exact tail and moment boundary.** If \(a_k\le z<a_{k+1}\), only outward states indexed by \(j\ge k+1\) exceed \(z\); hence
\[
S(z)=\frac25\sum_{j=k+1}^\infty 2^{-j}=\frac{2}{5\cdot2^k}.
\]
Because \(a_{k+1}=2a_k+1\), the map \(z\mapsto2z+1\) sends the entire \(k\)-th shell to the next shell, proving the stated exact scale identity. Inside a shell \(zS(z)\) increases from \(a_k\,2/(5\cdot2^k)\to3/5\) to values arbitrarily close to \(a_{k+1}\,2/(5\cdot2^k)\to6/5\). These subsequences establish the exact liminf and limsup and exclude a single tail coefficient. Finally
\[
\mathbb E_\pi|N|^p=\frac25+\frac25\sum_{k\ge1}2^{-k}a_k^p
\]
for every \(p>0\). Since \(a_k\sim(3/2)2^k\), the series converges precisely when \(p<1\).

**4. Uniform four-step regeneration.** Starting at \(0\), the sequence of events \(0\to\pm1\to0\to\pm1\to0\) gives \(P^4(0,\{0\})\ge1/4\). From any \(n\ge2\), the route \(n\to-1\to0\to\pm1\to0\) has probability \((1/2)(1/2)(1)(1/2)=1/8\); the negative case is symmetric. From \(n=1\), the route \(1\to2\to5\to-1\to0\) has probability \(1/16\); the negative route is symmetric. Enumeration of the four transition levels from \(\pm1\) shows that no other length-four route reaches zero, so the bound is sharp. Therefore
\[
P^4(n,\cdot)\ge\tfrac1{16}\delta_0(\cdot)\quad\hbox{for all integers }n.
\]
The resulting common-atom decomposition gives a contraction factor at most \(15/16\) every four steps in total variation. Iterating, and using that Markov kernels cannot increase total variation, proves the bound for all \(t\). It also gives convergence from every starting state.

## Verification

A dependency-free Python script, `verify.py`, checks the integer transition rule independently of the derived formulas, the exact balance equations, geometric-tail algebra, and four-step return probabilities. It uses rational arithmetic, including an independent four-step state-distribution enumeration on all starting integers from \(-1000\) through \(1000\). It also checks the branch recurrences over 40 consecutive levels. Its finite checks do **not** prove the infinite-state assertions; those follow from the explicit balance, geometric series, tail shells and uniform path arguments above. Running `python3 verify.py` produced `PASS 4488 exact finite checks`.

## Relationship to prior work

Lima and Curado introduced this exact discrete model and its parameters, and analyzed a continuum diffusion approximation with a Lorentz-like stationary density of inverse-square decay. Their simulations emphasize larger thresholds, particularly \(l=10\) and \(l=100\). The present result does not claim their inverse-square envelope is new. It isolates the smallest integer-parameter version of **their original discrete dynamics** and gives the full invariant atomic measure, exact lacunary tail corrections, moment cutoff, and uniform mixing rate. The low-threshold discrete regime is not asserted to be within the uniform validity of their continuous approximation.

Log-periodicity generated by intermittent multiplicative amplification is a known mechanism, notably in Jögi, Sornette and Blank's studies of random affine maps. Thus discrete-scale invariance *as a phenomenon* is prior art. The assessed result is the explicit characterization and four-step uniform ergodicity of this named accelerated-walk kernel, not a generic invention of log-periodic scaling.

## Limitations

The proof treats the natural minimal positive-integer parameter pair \(l=r=1\) only. It does not classify the source model at larger thresholds, establish universality of the oscillation amplitudes under perturbations, or furnish a physical-continuum error bound. The total-variation estimate is a guaranteed global rate, not an assertion of the optimal spectral mixing exponent. The invariant distribution has no finite absolute first moment, so one must not assign an ordinary finite stationary mean merely from its symmetry. Wider prior results on random affine recursions may offer alternative derivations; no independent literature-wide priority certification is claimed.

## References

1. H. S. Lima and E. M. F. Curado, *Emergent heavy-tailed distributions from a Markovian random walk*, arXiv:2605.22933v1 (first public 21 May 2026), https://arxiv.org/pdf/2605.22933 ; published in Physical Review E **114**, 034114 (2026), https://doi.org/10.1103/f1bd-1242 . The discrete transition kernel is Eqs. (1)-(2), and the continuum argument is in Eqs. (8)-(14).
2. P. Jögi, D. Sornette and M. Blank, *Fine structure and complex exponents in power law distributions from random maps*, arXiv:cond-mat/9708220v1 (1997), https://arxiv.org/pdf/cond-mat/9708220 ; Physical Review E **57**, 120 (1998), https://doi.org/10.1103/PhysRevE.57.120 . Prior theory and examples of log-periodic corrections to multiplicative random-map distributions.
