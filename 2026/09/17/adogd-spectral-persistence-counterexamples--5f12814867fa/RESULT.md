# Spectral-persistence counterexamples and a repair for AdOGD

## Statement

Wang, Ballotta, Carli, Cao, and Schenato introduce Adaptive Optimal Gradient
Descent (AdOGD) for strongly convex quadratics. In their notation, for
\[
f(\xi)=\frac12\xi^\top\Lambda\xi,\qquad
\mu=\lambda_{\min}(\Lambda)<\lambda_{\max}(\Lambda)=L,
\]
the local curvature is
\[
L_k=\frac{\|\Lambda(\xi_k-\xi_{k-1})\|}
          {\|\xi_k-\xi_{k-1}\|},
\]
the running estimators are
\[
\widehat\mu_k=\min_{1\le j\le k}L_j,\qquad
\widehat L_k=\max_{1\le j\le k}L_j,
\]
and, after an initial seed step \(\alpha_0>0\),
\[
\alpha_k=\frac{2}{\widehat\mu_k+\widehat L_k},\qquad k\ge1.
\]
Their Theorem 8 states that if every spectral coordinate of \(\xi_0\) is
nonzero, then
\[
\alpha_k\longrightarrow \alpha^\star:=\frac{2}{\mu+L}.
\]

There are two separate missing conditions in the current arXiv v1 analysis.

1. **Theorem 8 is false as written.** An allowed initial seed can annihilate an
   endpoint eigenspace exactly before AdOGD begins estimating the spectrum.
   In dimension two this yields a closed-form family whose stepsizes converge
   to a constant different from \(\alpha^\star\).

2. **The lower-stepsize branch of Lemma 4 is false as written.** Merely requiring
   \(\alpha_k\le\alpha^\star-\varepsilon\) does not force the local curvature
   toward \(\mu\): a summable positive stepsize sequence can leave every
   spectral component at nonzero limiting amplitude.

Both issues admit simple repairs. For the lower branch of the varying-stepsize
curvature lemma, a divergent cumulative step mass such as
\(\sum_k\alpha_k=\infty\) is sufficient. For AdOGD itself, it is enough to
require persistence only of the two endpoint eigenspaces. In particular,
Theorem 8 becomes valid under the weaker spectral initialization
\[
P_\mu\xi_0\ne0,\qquad P_L\xi_0\ne0,
\]
together with
\[
\alpha_0\notin\{1/\mu,1/L\},
\]
where \(P_\mu,P_L\) are the orthogonal projections onto the minimal and maximal
eigenspaces. No nonzero assumption on intermediate eigenspaces is needed.

## Counterexample to Theorem 8

Take
\[
\Lambda=\operatorname{diag}(\mu,L),\qquad 0<\mu<L,
\]
and
\[
\xi_0=(u,v)^\top,\qquad uv\ne0.
\]
For any positive initial seed \(\alpha_0\), the first local-curvature estimate
is independent of the magnitude of \(\alpha_0\):
\[
r:=L_1
=\sqrt{\frac{\mu^4u^2+L^4v^2}{\mu^2u^2+L^2v^2}}.
\]
Because both coordinates are nonzero,
\[
\mu<r<L.
\]
Hence
\[
\widehat\mu_1=\widehat L_1=r,\qquad
\alpha_1=\frac1r.
\]

### Killing the maximal eigenspace

Choose the allowed seed
\[
\alpha_0=\frac1L.
\]
Then
\[
\xi_1=\bigl((1-\mu/L)u,\,0\bigr)^\top.
\]
All later iterates remain in the \(\mu\)-eigenspace. Therefore
\[
L_k=\mu,\qquad k\ge2.
\]
Consequently
\[
\widehat\mu_k=\mu,\qquad
\widehat L_k=r,\qquad
\boxed{\alpha_k=\frac{2}{\mu+r}\quad(k\ge2)}.
\]
The surviving coordinate is never subsequently annihilated because
\[
1-\frac{2\mu}{\mu+r}=\frac{r-\mu}{r+\mu}\ne0.
\]
Since \(r<L\),
\[
\boxed{\lim_{k\to\infty}\alpha_k=\frac{2}{\mu+r}
      >\frac{2}{\mu+L}=\alpha^\star.}
\]

### Killing the minimal eigenspace

Symmetrically, choose
\[
\alpha_0=\frac1\mu.
\]
Then \(\xi_1\) lies entirely in the \(L\)-eigenspace, so
\[
L_k=L,\qquad k\ge2,
\]
and
\[
\boxed{\alpha_k=\frac{2}{r+L}\quad(k\ge2)}.
\]
Because \(r>\mu\),
\[
\boxed{\lim_{k\to\infty}\alpha_k=\frac{2}{r+L}
      <\frac{2}{\mu+L}=\alpha^\star.}
\]

Thus the hypothesis used in Theorem 8,
\(\xi_0^i\ne0\) for all \(i\), does not ensure the persistence condition needed
by its proof.

### Concrete numerical instance

With
\[
\mu=1,\qquad L=2,\qquad \xi_0=(1,1)^\top,
\]
one has
\[
r=\sqrt{\frac{17}{5}}\approx1.843908891.
\]
For \(\alpha_0=1/2\),
\[
\alpha^\star=\frac23,\qquad
\alpha_1=\sqrt{\frac5{17}}\approx0.542326145,
\]
but
\[
\alpha_k=\frac{2}{1+\sqrt{17/5}}
\approx0.703257410,\qquad k\ge2.
\]
For \(\alpha_0=1\), instead,
\[
\alpha_k=\frac{2}{2+\sqrt{17/5}}
\approx0.520303695,\qquad k\ge2.
\]

These exceptional trajectories still converge to the minimizer. The discrepancy
is spectral: after an endpoint mode is removed exactly, the original
full-spectrum benchmark \(2/(\mu+L)\) is no longer the natural optimal constant
step for the surviving one-dimensional trajectory.

## Counterexample to the lower branch of Lemma 4

The current Lemma 4 asserts, in particular, that if all coordinates are
nonzero at some index and
\[
\alpha_k\le\alpha^\star-\varepsilon
\]
eventually, then \(L_k\to\mu\). The argument passes from a pointwise ratio
strictly below one to the conclusion that a product of such ratios tends to
zero. A lower-bound or cumulative-step condition is missing.

Let
\[
\Lambda=\operatorname{diag}(1,2),\qquad \xi_0=(1,1)^\top,
\qquad \alpha_k=\frac1{(k+3)^2}\quad(k\ge0).
\]
Here \(\alpha^\star=2/3\), and, for example,
\[
\alpha_k\le\frac16=\alpha^\star-\frac12
\]
for every \(k\ge0\). Every update factor is strictly positive:
\[
1-\alpha_k>0,\qquad 1-2\alpha_k>0.
\]
Moreover,
\[
\sum_{k=0}^{\infty}\alpha_k<\infty.
\]
Hence both infinite products
\[
\prod_{k=0}^{\infty}(1-\alpha_k),\qquad
\prod_{k=0}^{\infty}(1-2\alpha_k)
\]
converge to positive numbers. In fact the first one telescopes to \(2/3\).
Thus
\[
\xi_k\longrightarrow (a,b)^\top
\]
for some \(a,b>0\), rather than having all higher modes vanish relative to the
minimal one. Since
\[
L_k^2
=\frac{\xi_{k-1,1}^2+16\xi_{k-1,2}^2}
       {\xi_{k-1,1}^2+4\xi_{k-1,2}^2},
\]
we obtain
\[
\lim_{k\to\infty}L_k
=\sqrt{\frac{a^2+16b^2}{a^2+4b^2}}
\in(1,2),
\]
not \(\mu=1\).

The missing step in the published proof is therefore substantive:
\(0<q_k<1\) for each \(k\) does not by itself imply
\(\prod_k q_k=0\).

## A repaired varying-stepsize condition

For the lower branch, the natural repair is to require enough cumulative motion.
Suppose, after some index,
\[
0<\alpha_k\le\alpha^\star-\varepsilon
\quad\text{and}\quad
\sum_k\alpha_k=\infty,
\]
and the projection onto the \(\mu\)-eigenspace is nonzero. For every
\(\lambda>\mu\), define
\[
q_\lambda(\alpha)
=\frac{|1-\alpha\lambda|}{|1-\alpha\mu|}.
\]
On \(0<\alpha\le\alpha^\star-\varepsilon\),
\(q_\lambda(\alpha)<1\). Moreover
\[
-\frac{\log q_\lambda(\alpha)}{\alpha}
\]
has a positive limit \(\lambda-\mu\) as \(\alpha\downarrow0\), and away from
zero it has a positive minimum on compact subintervals (with a zero numerator
only strengthening the conclusion). Hence there is \(c_\lambda>0\) such that
\[
q_\lambda(\alpha)\le e^{-c_\lambda\alpha}.
\]
Therefore
\[
\prod_k q_\lambda(\alpha_k)
\le \exp\!\left(-c_\lambda\sum_k\alpha_k\right)\longrightarrow0,
\]
which is the product-decay step needed to conclude \(L_k\to\mu\).

A simpler sufficient repair is \(\inf_k\alpha_k>0\).

## Repaired AdOGD theorem

The central AdOGD conclusion can be recovered without assuming every spectral
coordinate remains nonzero.

**Proposition.** Let \(\mu<L\), let the initial state have nonzero projections
onto both endpoint eigenspaces,
\[
P_\mu\xi_0\ne0,\qquad P_L\xi_0\ne0,
\]
and let the seed satisfy
\[
\alpha_0>0,\qquad \alpha_0\notin\{1/\mu,1/L\}.
\]
Generate \(L_1\) from the seed step and then use AdOGD. Then
\[
\boxed{\alpha_k\longrightarrow\frac{2}{\mu+L}.}
\]

**Proof.** Since both endpoint projections are present in the seed displacement,
\[
\mu<L_1<L.
\]
Because \(L_1\) remains among the historical local-curvature observations,
\[
\mu\le\widehat\mu_k\le L_1
\quad\text{and}\quad
L_1\le\widehat L_k\le L.
\]
Thus, for every \(k\ge1\),
\[
\frac1L<\alpha_k=\frac{2}{\widehat\mu_k+\widehat L_k}<\frac1\mu.
\]
The seed was assumed not to equal either endpoint reciprocal, so neither the
\(\mu\)- nor the \(L\)-eigenspace can ever be annihilated.

The monotone bounded estimators have limits, so \(\alpha_k\to\widehat\alpha\).
If \(\widehat\alpha<\alpha^\star\), then for some \(\varepsilon>0\), eventually
\[
\frac1L\le\alpha_k\le\alpha^\star-\varepsilon.
\]
For each \(\lambda>\mu\), the ratio
\[
\frac{|1-\alpha\lambda|}{|1-\alpha\mu|}
\]
is strictly below one throughout this compact interval, hence is bounded by a
common constant \(q_\lambda<1\). Since the \(\mu\)-projection persists, all
higher modes decay geometrically relative to it, and therefore
\(L_k\to\mu\). It follows that \(\widehat\mu_k\to\mu\), so
\[
\widehat\alpha
=\frac{2}{\mu+\overline L}
\ge\frac{2}{\mu+L}
=\alpha^\star,
\]
a contradiction.

If \(\widehat\alpha>\alpha^\star\), the symmetric argument uses the persistent
\(L\)-projection and the compact interval
\[
\alpha^\star+\varepsilon\le\alpha_k\le\frac1\mu.
\]
All lower modes then decay geometrically relative to the \(L\)-mode, so
\(L_k\to L\), implying \(\widehat L_k\to L\) and
\[
\widehat\alpha
=\frac{2}{\overline\mu+L}
\le\frac{2}{\mu+L}
=\alpha^\star,
\]
again a contradiction. Hence
\(\widehat\alpha=\alpha^\star\). \(\square\)

This repair also shows that requiring every coordinate of \(\xi_0\) to be
nonzero is stronger than necessary: only the two endpoint eigenspaces matter
for the asymptotic identification argument.

## Finite-horizon instability near endpoint annihilation

The exact counterexamples use the two isolated seed values \(1/L\) and
\(1/\mu\). Nevertheless, the phenomenon is not harmless from a finite-iteration
viewpoint. For every fixed horizon \(N\), the first \(N\) AdOGD updates depend
continuously on the seed in a neighborhood of either counterexample trajectory:
all denominators on the limiting trajectory are nonzero. Therefore seeds
arbitrarily close to \(1/L\) (or \(1/\mu\)), but not equal to it, can make the
first \(N\) stepsizes arbitrarily close to the corresponding nonoptimal
constant trajectory above. Thus no uniform finite-horizon identification rate
can follow from the paper's stated nonzero-coordinate assumption alone.

This is consistent with eventual convergence under the repaired theorem; it
shows that endpoint near-annihilation can make spectral identification
arbitrarily ill-conditioned even when exact annihilation is avoided.

## Context and originality

The current arXiv v1 of Wang et al. states Theorem 8 exactly with the initial
nonzero-coordinate hypothesis and invokes Lemma 4 in both contradiction
branches. Lemma 4 itself assumes only eventual separation of the stepsizes from
\(\alpha^\star\) on the relevant side; its lower branch does not impose a
positive lower bound or a divergent cumulative step mass.

Targeted searches for the paper title, `AdOGD`, Theorem 8, counterexamples,
errata, corrections, endpoint-mode annihilation, and equivalent
local-curvature/spectral-identification descriptions located no public
correction or prior statement of the counterexamples above. The arXiv record
still lists only v1 (4 August 2026). Public summaries located for the paper
continue to repeat the claimed convergence to \(\alpha^\star\).

The paper was presented at the 23rd IFAC World Congress in August 2026; the
public conference program repeats the high-level convergence claim. A
separately searchable final proceedings text with theorem-level detail was not
located and therefore was not inspected. If such a version differs from arXiv
v1, it is the most plausible source that could already contain a repair.

Originality is therefore claimed only **to the best of our knowledge**.

## Limitations

- The counterexample addresses the theorem as written in the current arXiv v1.
  A later or final proceedings version could contain modified hypotheses.
- Exact failure of Theorem 8 occurs at endpoint-reciprocal seed values. These
  form an exceptional set, although nearby seeds can shadow the bad trajectory
  for arbitrarily long finite horizons.
- The repaired theorem is for the quadratic AdOGD setting analyzed in the
  source paper. It does not establish analogous endpoint-persistence results
  for general nonquadratic objectives.
- The Lemma 4 counterexample concerns its lower-stepsize branch. The additional
  cumulative-step condition supplied here is sufficient; it is not claimed to
  be a uniquely minimal repair.

## References

1. Y. Wang, L. Ballotta, R. Carli, X. Cao, and L. Schenato,
   *Pursuing Optimal Stepsize in Adaptive Gradient-Based Quadratic
   Optimization*, arXiv:2608.03546v1, 2026.
2. Y. Malitsky and K. Mishchenko,
   *Adaptive Gradient Descent without Descent*, ICML 2020.
3. D. Zhou, S. Ma, and J. Yang,
   *AdaBB: Adaptive Barzilai--Borwein Method for Convex Optimization*,
   Mathematics of Operations Research, 2025.
