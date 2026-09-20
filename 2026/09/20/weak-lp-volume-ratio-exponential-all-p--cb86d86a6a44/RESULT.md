# Exponential weak-Lp volume ratio for every finite p

**Same-model review: passed. Independent audit: not yet performed.**

## Result

For `0 < p < infinity`, let

\[
R_{p,n}=\frac{\operatorname{vol}(B^n_{p,\infty})}{\operatorname{vol}(B^n_p)},
\]

where `B^n_{p,\infty}` is the unit ball of the finite-dimensional weak
Lebesgue (Lorentz) space `ell^n_{p,\infty}` and `B^n_p` is the usual
`ell^n_p` unit ball.

**Theorem.** For every finite `p>0` there are constants `c_p>0` and `C_p>1`
such that

\[
R_{p,n}\ge c_p C_p^n\qquad(n\ge1).
\]

Equivalently,

\[
\liminf_{n\to\infty}\frac1n\log R_{p,n}>0.
\]

Dolezalova and Vybiral proved this for `0<p<=2` (their construction in fact
extends to `p<p_0`, `p_0\approx2.1086`) and explicitly left the range
`2<p<infinity` as an open problem. The theorem above gives a uniform
entropy/type argument valid for every finite `p`.

## Scaling and an empirical-tail description

Work first in the positive orthant and put

\[
W_{p,n}=n^{1/p}B^{n,+}_{p,\infty}.
\]

For `y=(y_1,...,y_n) in [0,infinity)^n`, write

\[
N_y(t)=\#\{i:y_i>t\}.
\]

The rearrangement condition

\[
y_k^*\le (n/k)^{1/p}\qquad(1\le k\le n)
\]

is equivalent to

\[
N_y(t)< n t^{-p}\qquad(t>0)
\]

up to the harmless boundary convention obtained by taking one-sided limits.
For `0<t<1` the inequality is automatic, so only `t>=1` matters.

The similarly scaled positive `ell_p` ball is

\[
L_{p,n}=n^{1/p}B_p^{n,+}.
\]

Dirichlet's volume formula and Stirling's formula give

\[
\lim_{n\to\infty}\frac1n\log\operatorname{vol}(L_{p,n})
=h_p,
\]

where

\[
h_p=\log\Gamma(1+1/p)+\frac{\log p+1}{p}.
\]

Thus it is enough to place inside `W_{p,n}` sets whose exponential volume
rate is strictly larger than `h_p`.

## An entropy-improving admissible density

Consider on `[0,infinity)` the generalized-Gaussian density

\[
f_p(x)=\frac{\exp(-x^p/p)}{p^{1/p}\Gamma(1+1/p)}.
\]

It has `E[X^p]=1` and differential entropy

\[
h(f_p)=h_p.
\]

For every `t>0`, strict Markov inequality gives

\[
S_p(t):=\int_t^\infty f_p(x)\,dx<t^{-p}.
\]

We now perturb `f_p` while retaining the tail constraints and increasing
entropy. Fix `0<a<1<T`, set `A=[0,a]` and `B=[T,T+1]`, and let

\[
\phi_A=a^{-1}{\bf1}_{A},\qquad
\phi_B={\bf1}_{B}.
\]

For small `epsilon>0`, set

\[
f_\epsilon=f_p+\epsilon(\phi_B-\phi_A).
\]

Because `S_p(t)<t^{-p}` continuously on the compact interval
`[1,T+1]`, the perturbation can be chosen small enough that `f_epsilon` is
nonnegative and

\[
\int_t^\infty f_\epsilon(x)\,dx<t^{-p}\qquad(t\ge1).
\]

Indeed, the survival function increases by at most `epsilon` before `T+1`
and is unchanged afterwards.

The entropy derivative at zero is explicit. Since `log f_p` is a constant
minus `x^p/p`,

\[
\left.\frac{d}{d\epsilon}h(f_\epsilon)\right|_{\epsilon=0}
=\frac1p\left(\frac1{|B|}\int_Bx^p\,dx
-\frac1{|A|}\int_Ax^p\,dx\right)>0.
\]

Hence, after shrinking `epsilon` if necessary,

\[
h(f_\epsilon)>h_p.
\]

For the finite-alphabet argument below, compactify this density without
losing either property. Choose `M>T+1`, remove the tail mass

\[
\tau_M=\int_M^\infty f_\epsilon(x)\,dx
\]

and put it back on `[0,a]`:

\[
q_M(x)=f_\epsilon(x){\bf1}_{[0,M]}(x)+\tau_M\phi_A(x).
\]

For `t>=1`, this only decreases the survival function, while
`h(q_M)->h(f_epsilon)` as `M->infinity`. Thus some compactly supported
probability density `q` on `[0,M]` satisfies

\[
h(q)>h_p,
\qquad
S_q(t)<t^{-p}\quad(t\ge1).
\]

By continuity and compactness there is a uniform margin

\[
\delta=\min_{1\le t\le M}\bigl(t^{-p}-S_q(t)\bigr)>0.
\]

## Type sets give exponential volume

Partition `[0,M]` into finitely many intervals

\[
I_j=[a_{j-1},a_j),\qquad j=1,...,m,
\]

with `1` among the endpoints and with the mesh above `1` fine enough that

\[
a_{j-1}^{-p}-a_j^{-p}<\delta/4
\]

for every interval lying above `1`. Let

\[
\alpha_j=\int_{I_j}q(x)\,dx.
\]

Choose integers `n_j` with `sum_j n_j=n` and `n_j/n -> alpha_j`.
Let `T_n` be the set of vectors in `[0,M]^n` having exactly `n_j`
coordinates in `I_j` for every `j`.

For `t in [a_{r-1},a_r)` with `a_{r-1}>=1`, every `y in T_n` obeys

\[
\frac{N_y(t)}n
\le \sum_{j\ge r}\frac{n_j}{n}
=S_q(a_{r-1})+o(1)
\le a_r^{-p}-\delta/2+o(1)
\le t^{-p}
\]

for all sufficiently large `n`. The constraints below `1` are automatic,
and those above `M` are trivial. Therefore

\[
T_n\subset W_{p,n}
\]

for all sufficiently large `n`.

Its volume is exactly

\[
\operatorname{vol}(T_n)
=\frac{n!}{\prod_j n_j!}\prod_j |I_j|^{n_j}.
\]

Stirling's formula yields

\[
\lim_{n\to\infty}\frac1n\log\operatorname{vol}(T_n)
=-\sum_j\alpha_j\log\alpha_j
+\sum_j\alpha_j\log|I_j|.
\]

The right-hand side is the differential entropy of the histogram density
that is constant with value `alpha_j/|I_j|` on `I_j`. Relative entropy
(nonnegativity of Kullback-Leibler divergence on each bin) gives

\[
-\sum_j\alpha_j\log\alpha_j
+\sum_j\alpha_j\log|I_j|\ge h(q)>h_p.
\]

Consequently,

\[
\liminf_{n\to\infty}\frac1n\log\operatorname{vol}(W_{p,n})>h_p.
\]

Combining this with the exact exponential rate `h_p` of
`vol(L_{p,n})` gives

\[
\liminf_{n\to\infty}\frac1n
\log\frac{\operatorname{vol}(B^{n,+}_{p,\infty})}
{\operatorname{vol}(B^{n,+}_p)}>0.
\]

Both balls are invariant under coordinate sign changes, so their full
volumes are `2^n` times their positive-orthant volumes. The same inequality
therefore holds for `R_{p,n}`. Choosing any exponential base below the
positive liminf and absorbing finitely many small dimensions into a
constant gives `R_{p,n}>=c_p C_p^n`.

## Why the argument crosses the former p=2 barrier

The previous proof selected a particular explicit subset of the weak ball;
its entropy rate ceases to beat the `ell_p` ball beyond a parameter near
`2.1086`. Here the subset is instead a type class for a probability density.
The `p`-Gaussian has exactly the same entropy rate as the scaled `ell_p`
ball and sits strictly inside the weak tail constraint. Moving an arbitrarily
small amount of mass from a low interval to a sufficiently higher interval
preserves that strict tail constraint while increasing entropy. This gives a
strict exponential-volume gain for every finite `p`.

## Limitations

- The proof is existential: it establishes a positive exponential gap but
  does not optimize the base `C_p` or determine the exact limit of
  `R_{p,n}^{1/n}`.
- The construction uses a finite partition/type approximation; no claim is
  made here about a full large-deviation principle or the limiting empirical
  law of a uniform point in the weak Lorentz ball.
- The statement concerns finite `p`; the limiting case `p=infinity` is a
  different geometry.

## References

1. A. Dolezalova and J. Vybiral, *On the volume of unit balls of
   finite-dimensional Lorentz spaces*, Journal of Approximation Theory 255
   (2020), 105407. https://doi.org/10.1016/j.jat.2020.105407
2. Z. Kabluchko, J. Prochno and M. Sonnleitner, *A probabilistic approach to
   Lorentz balls*, arXiv:2303.04728 (2023). https://arxiv.org/abs/2303.04728
3. J. Prochno, M. Sonnleitner and J. Vybiral, *Entropy numbers of
   finite-dimensional Lorentz space embeddings*, Studia Mathematica 283
   (2025), 105-131. https://doi.org/10.4064/sm240409-15-2
