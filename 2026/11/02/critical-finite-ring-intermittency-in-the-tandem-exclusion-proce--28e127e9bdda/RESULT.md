# Critical finite-ring intermittency in the tandem exclusion process

## Finding

Consider the continuous-time tandem exclusion process on a periodic ring of \(N\) sites: a local word \(110\) changes to \(101\) at rate \(\alpha\), and \(101\) changes to \(011\) at rate \(\beta_N\). Set \(q_N=\beta_N/\alpha\). Work in its active stationary class at fixed particle number \(K_N\). Let \(A_N\) and \(B_N\) count occurrences of \(110\) and \(101\), respectively, including cyclic triples, and define the *instantaneous stationary current intensity per bond* by

\[
 j_N(\eta)=\frac{\alpha A_N(\eta)+\beta_N B_N(\eta)}{N}.
\]

This is a configuration-dependent jump intensity, *not* the integrated current or its time-averaged trajectory variance. Assume the following simultaneous limits with \(\alpha>0\), \(0<\rho<1\), and \(0<\lambda<\infty\):

\[
 N\longrightarrow\infty,\qquad K_N/N\longrightarrow\rho,\qquad q_N/N^2\longrightarrow\lambda.
\]

Write \(C_N\) for the number of maximal occupied runs on the ring, and set \(z=\rho(1-\rho)/\lambda\). In the active stationary ensemble,

\[
 \Pr(C_N=c)\longrightarrow
 \frac{z^{c-1}}{c!(c-1)!S(z)},\qquad c=1,2,\ldots,
 \qquad S(z)=\sum_{c\ge1}\frac{z^{c-1}}{c!(c-1)!}=\frac{I_1(2\sqrt z)}{\sqrt z}.
\]

The central *current intermittency* result is

\[
 j_N\xrightarrow{\Pr}0,\qquad
 \mathbb E j_N\longrightarrow\alpha\rho,\qquad
 \frac{\operatorname{Var}(j_N)}{N}\longrightarrow\alpha^2\lambda\rho.
\]

More generally, for each fixed integer \(m\ge1\),

\[
 \lim_{N\to\infty}\frac{\mathbb E[j_N^m]}{N^{m-1}}
 =\alpha^m\lambda^{m-1}\rho.
\]

In addition, the exceptional high-intensity snapshots have a sharp frequency: for any \(0<t<\alpha\lambda\),

\[
 N\Pr(j_N/N>t)\longrightarrow\frac\rho\lambda,
\]

whereas the same limit is zero for \(t>\alpha\lambda\). Thus snapshots with current intensity of order \(N\) occur with probability of order \(N^{-1}\), producing a positive mean although the typical intensity tends to zero.

## Assumptions and scope

The ring is periodic, particles obey exclusion, and only the two directed local transitions specified above are permitted. The reference rate \(\alpha\) does not vary with \(N\); \(\beta_N=\alpha q_N\). At each size the law is the canonical active stationary law with probability proportional to \(q_N^{H(\eta)}\), where \(H(\eta)=\sum_x\eta_x\eta_{x+1}\). This stationary law is established for the tandem exclusion process in the cited 2026 model paper; the finite-state balance can also be checked directly by cyclic telescoping. The active class excludes isolated absorbing configurations when they exist. No assumptions about the initial distribution or mixing time are made: this is an equilibrium-in-the-stationary-ensemble statement about an out-of-equilibrium jump process.

The proof applies to every integer sequence satisfying the displayed limits. In intermediate finite calculations, take \(3\le K_N\le N-3\), which holds for all sufficiently large \(N\) under the stated density assumption.

## Proof

**0. Stationarity of the canonical ensemble.** The Gibbs weight used above is independently checked by global balance. Fix a target binary configuration, and let \(A_x,B_x,D_x\) indicate cyclic occurrences of \(110,101,011\) beginning at \(x\). An incoming head transition to a \(101\) target has Gibbs weight ratio \(q_N^{1-\eta_{x+3}}\), while an incoming follower transition to a \(011\) target has ratio \(q_N^{\eta_{x-1}-1}\). Since \(\beta_N=\alpha q_N\), incoming weighted rate minus outgoing weighted rate, divided by \(\alpha q_N^{H(\eta)}\), is

\[
 \sum_x \left[D_x-A_x+(q_N-1)\bigl(\eta_{x-1}D_x-\eta_{x+3}B_x\bigr)\right].
\]

The first difference sums to zero because every occupied run of length at least two contributes exactly one \(110\) and one \(011\). The two terms in parentheses count the same cyclic four-site word \(1011\), so their sums also agree. This proves stationarity of \(q_N^H\) on the whole fixed-composition state space; restriction to the invariant active class preserves stationarity. Uniqueness in the active class is established in the model's original paper.

**1. Exact cyclic composition count.** Put \(L_N=N-K_N\). Any configuration with \(c\ge1\) occupied runs alternates \(c\) positive occupied lengths totaling \(K_N\) and \(c\) positive vacant lengths totaling \(L_N\). By rooting a run at one of the \(N\) sites and dividing by the \(c\) choices of root,

\[
 \#\{\eta:C_N(\eta)=c\}=\frac{N}{c}
 \binom{K_N-1}{c-1}\binom{L_N-1}{c-1}.
\]

Because \(H=K_N-C_N\), the full canonical probability mass in that class is proportional to the displayed count times \(q_N^{-c}\). Relative to the one-run class, its weight is

\[
 R_{N,c}=\frac1c\binom{K_N-1}{c-1}
 \binom{L_N-1}{c-1}q_N^{-(c-1)}.
\]

For each fixed \(c\), \(R_{N,c}\to z^{c-1}/[c!(c-1)!]\). Moreover, for large \(N\) and all \(c\),

\[
 0\le R_{N,c}\le\frac{M^{c-1}}{c!(c-1)!}
\]

with a constant \(M\) because \(K_N L_N/q_N\) stays bounded. The summable bound remains summable after multiplication by any fixed polynomial in \(c\). Dominated convergence proves the stated run-count law and convergence of all polynomial moments. In particular, a series shift gives

\[
 \lim_{N\to\infty}\mathbb E[C_N(C_N-1)]=z.
\]

The source model conditions on its active class. Any frozen configuration has no adjacent occupied pair, and thus Gibbs weight one. Since the full partition sum is at least \(Nq_N^{K_N-1}\), the total full-Gibbs probability of frozen configurations is at most \(2^N/(Nq_N^{K_N-1})\), which tends to zero faster than every inverse power of \(N\). The full and active distributions consequently have identical limits for the observables and scaled moments used here; frozen configurations contribute zero jump intensity.

**2. Exact conditional pattern counts.** Conditional on \(C_N=c\), occupied and vacant run lengths form two independent uniform positive compositions. A \(110\) occurs once at the end of each occupied run of length at least two; a \(101\) occurs once for each vacant run of length exactly one. Therefore

\[
 \mathbb E[A_N\mid C_N=c]=\frac{c(K_N-c)}{K_N-1},
 \qquad
 \mathbb E[B_N\mid C_N=c]=\frac{c(c-1)}{L_N-1}.
\]

For every fixed integer \(k\ge1\), writing \((x)_{\underline k}\) for the falling factorial, the vacant-composition identity is

\[
 \mathbb E[(B_N)_{\underline k}\mid C_N=c]
 =\frac{(c)_{\underline k}(c-1)_{\underline k}}{(L_N-1)_{\underline k}},
\]

with value zero when there are fewer than \(k\) eligible runs. For fixed \(k\) the unconditional falling-factorial moment is \(O(N^{-k})\): the numerator has uniformly bounded moments of every order by step 1, and \(L_N\asymp N\). In particular,

\[
 N\mathbb E B_N\to \frac{z}{1-\rho}=\frac\rho\lambda,
 \quad \mathbb E[B_N(B_N-1)]=O(N^{-2}),
 \quad \mathbb E[B_N^m]=\frac\rho{\lambda N}+o(N^{-1})
\]

for every fixed positive integer \(m\), by the Stirling-number expansion of ordinary moments in falling factorials. The last identity also shows \(N\Pr(B_N\ge1)\to\rho/\lambda\), since the probability of two or more unit vacant runs is \(O(N^{-2})\).

**3. Current law and moment anomaly.** Almost surely \(A_N\le C_N\). As \(C_N\) is tight and \(\Pr(B_N\ge1)=O(N^{-1})\), the formula for \(j_N\) gives \(j_N\to0\) in probability. On the other hand,

\[
 \mathbb E j_N=\frac\alpha N\mathbb E A_N
 +\frac{\alpha q_N}{N(L_N-1)}\mathbb E[C_N(C_N-1)]
 \longrightarrow\alpha\rho.
\]

For a fixed integer \(m\ge2\), expand the \(m\)-th power of \(\alpha A_N/N+\alpha q_NB_N/N\). The all-\(B_N\) term, divided by \(N^{m-1}\), converges to \(\alpha^m\lambda^{m-1}\rho\). Every mixed term containing at least one \(A_N\) vanishes on this scale: its coefficient is \(O(N^{2k-m})\) when it contains \(k<m\) factors of \(B_N\), and its expected product is \(O(N^{-1})\) for \(k\ge1\), or \(O(1)\) when \(k=0\). The case \(m=1\) was established above. In particular the second moment grows as \(\alpha^2\lambda\rho N\); the bounded squared mean does not affect the variance coefficient.

Finally, when \(B_N=1\), one has \(j_N/N\to\alpha\lambda\) uniformly in the run-count part of the formula, because \(A_N\le C_N\) is tight; when \(B_N=0\), \(j_N/N\to0\). Events \(B_N\ge2\) have probability \(O(N^{-2})\). The rare-event frequency follows for thresholds strictly below or above \(\alpha\lambda\).

## Verification

The self-contained `verify.py` uses only Python's standard library. It enumerates periodic binary configurations at small sizes, checks exact run-count multiplicities and five conditional pattern moments, verifies all global stationary balance equations at several finite particle numbers using rational transition rates, and evaluates stable positive run-count sums at larger sizes. The reference execution completed 2,239 finite assertions. The finite tests do **not** prove the infinite-size limits; the proof is the combinatorial and dominated-convergence argument above.

Run from a directory containing the two files:

```bash
python verify.py
```

## Relationship to prior work

Ngoc, Nhung and Thi (2026) introduce this tandem process and establish the canonical active Gibbs measure, fixed-parameter current, and strong-recovery thermodynamic current. These inputs are credited; no claim is made to a new stationary Gibbs structure or to the limit \(\alpha\rho\) alone. The contribution here is the simultaneous finite-ring high-rate regime and its configuration-level current-intensity intermittency, anomalous moments and rare-event probability.

Antal, Droz and Rácz (2003/2004) develop domain-wall counting and finite-size low-temperature Ising scaling. Because the canonical tandem Gibbs measure is an Ising-type ring law at fixed composition, its static run-count limit is related to that pre-existing framework and is **not** asserted to be novel in isolation. The fast follower transition rate and the ensuing stationary *jump-intensity* moments do not belong to the equilibrium Ising observables analyzed there. Gabel, Krapivsky and Redner (2010) study a facilitated exclusion process without the independent high-rate follower transition used here.

## Limitations

This result concerns the probability law of the **instantaneous total transition intensity divided by ring length**, sampled at stationarity. It does not compute the variance, large deviations, or scaling of *time-integrated* particle current. The single-time intensity is not a direct measurement of trajectory shot noise. There is no claim about temporal mixing, metastable residence times, hydrodynamic limits, or finite-size convergence rates. The scaling \(q_N/N^2\to\lambda\in(0,\infty)\) is essential; the theorem does not cover alternative joint regimes. The static block-count ingredient is a standard Ising-type combinatorial reduction, and priority relative to broader kinetic rare-event analyses remains a possible limitation.

## References

1. N. P. N. Ngoc, L. T. Nhung and H. A. Thi, *Tandem Exclusion Process*, arXiv:2606.01568, first submitted 2026-06-01, https://arxiv.org/abs/2606.01568 .
2. T. Antal, M. Droz and Z. Rácz, *Probability distribution of magnetization in the one-dimensional Ising model: Effects of boundary conditions*, arXiv:cond-mat/0308442 (2003), Journal of Physics A 37 (2004), https://arxiv.org/abs/cond-mat/0308442 .
3. A. Gabel, P. L. Krapivsky and S. Redner, *Facilitated asymmetric exclusion*, Physical Review Letters 105, 210603 (2010), https://arxiv.org/abs/1007.3217 .
