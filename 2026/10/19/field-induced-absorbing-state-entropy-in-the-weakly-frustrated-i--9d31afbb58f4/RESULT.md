# Field-induced absorbing-state entropy in the weakly frustrated Ising–Glauber ring

## Finding

**Theorem (complete zero-temperature absorbing-state phase diagram).** On the periodic ring with \(N\ge5\) spins and couplings \(J>0\), \(0<K<J/2\), every absorbing configuration for the dynamics described below belongs to precisely one of these field regimes:

1. **Zero field, \(h=0\):** the two uniform configurations, and (only when \(4\mid N\)) the four translates of the alternating two-spin-domain word \(++--++--\cdots\).
2. **Weak positive field, \(0<h<2K\):** the two uniform configurations, and all cyclic mixed configurations with every down-spin domain of length exactly two and every up-spin domain of length at least two.
3. **Intermediate field, \(2K\le h<2(J-K)\):** exactly the two uniform configurations.
4. **Strong field, \(h\ge2(J-K)\):** exactly the all-plus configuration.

Write \(B_N(z)=\sum_{s\text{ absorbing}}z^{d(s)}\), where \(d(s)\) is the number of down spins. In the weak positive field interval the **exact finite-volume counting polynomial** is

\[
B_N(z)=1+z^N+\sum_{k=1}^{\lfloor N/4\rfloor}\frac Nk\binom{N-3k-1}{k-1}z^{2k}
=z^N+\operatorname{tr}(T(z)^N),\qquad
T(z)=\begin{pmatrix}0&1&0&0\\0&0&1&0\\0&0&1&z\\z&0&0&0\end{pmatrix}.
\]

The transfer polynomial is \(\det(\lambda I-T(z))=\lambda^4-\lambda^3-z^2\). Consequently the weak-positive-field absorbing-state entropy per spin is

\[
s_{\mathrm{abs}}=\lim_{N\to\infty}\frac1N\log B_N(1)=\log\lambda_*\approx0.3222846159708578,
\quad \lambda_*^4-\lambda_*^3-1=0,\quad\lambda_*\approx1.3802775690973763.
\]

At exactly zero field and throughout \(h\ge2K\), this entropy is zero. Thus arbitrarily small *positive* longitudinal field creates an exponentially large family of strictly absorbing states in a regime where none exists at zero field. Under the uniform distribution on the absorbing configurations (not the dynamically reached-state distribution), the limiting down-spin fraction for \(0<h<2K\) is

\[
\rho_-=\frac{2(\lambda_*-1)}{4\lambda_*-3}\approx0.3016746809203235.
\]

## Assumptions and scope

For all integers \(N\ge5\), indices are taken modulo \(N\), and \(s_i\in\{-1,+1\}\). The Hamiltonian is

\[
H(s)=-J\sum_{i=1}^N s_i s_{i+1}+K\sum_{i=1}^N s_i s_{i+2}-h\sum_{i=1}^N s_i,
\qquad J>0,\quad 0<K<J/2,\quad h\ge0.
\]

At zero temperature, each proposed single-site flip of spin \(i\) occurs at a positive rate if and only if its energy increment is nonpositive. In particular, **energy-neutral flips remain allowed**. A configuration is *absorbing* if every single-site flip has strictly positive energy increment. Flip-clock normalizations do not affect this classification. The theorem is about absorbing states, not the probability of eventually visiting them or the low-positive-temperature stationary measure.

## Proof

**1. Exact spin-flip criterion.** Flipping a single spin gives

\[
\Delta_i H=2s_i F_i,\qquad F_i=J(s_{i-1}+s_{i+1})-K(s_{i-2}+s_{i+2})+h.
\]

Thus a configuration is absorbing exactly when \(s_iF_i>0\) for all \(i\). If a spin is a singleton domain, its nearest neighbors are both opposite: for a plus singleton, \(F_i\le-2J+2K+h<-2J+4K<0\) throughout \(0\le h<2K\); for a minus singleton, \(F_i\ge2J-2K+h>0\). Both contradict \(s_iF_i>0\). Hence all domains in an absorbing mixed configuration in this field range have length at least two.

**2. Boundary restrictions.** Consider the first minus spin \(i\) of a minus domain, preceded by an up domain. By the preceding argument, \(s_{i-2}=s_{i-1}=+1\) and \(s_i=s_{i+1}=-1\). The nearest-neighbor contribution cancels, giving

\[
F_i=h-K(1+s_{i+2}).
\]

Since \(s_i=-1\), absorption requires \(F_i<0\). For \(0\le h<2K\), this is possible only if \(s_{i+2}=+1\), and forces the minus domain to have **exactly two spins**. At the first plus spin \(j\) of an up domain, the preceding minus domain likewise has exactly two spins, and

\[
F_j=h-K(-1+s_{j+2}).
\]

If its up domain has exactly two sites, then \(s_{j+2}=-1\), so \(F_j=h+2K>0\); if the up domain has length at least three, then \(s_{j+2}=+1\), so \(F_j=h\). At \(h=0\) strict positivity therefore forces every up domain to have length two; for \(0<h<2K\), all up-domain lengths at least two are allowed. These boundary conditions are also sufficient: all spins in minus domains lie on boundaries, and the two ends of each up domain have positive local fields as calculated. A spin strictly inside a plus domain has both nearest neighbors plus and satisfies \(F_i\ge2J-2K+h>0\). The zero-field mixed words consequently consist of repeated \(++--\) blocks and have precisely four distinct translations when \(4\mid N\).

**3. No mixed states above the first threshold.** For \(h\ge2K\), a singleton minus spin is impossible because its local field is positive. At the first minus spin of any nonsingleton minus domain, one nearest neighbor is plus and one minus, whence \(F_i=h-K(s_{i-2}+s_{i+2})\ge h-2K\ge0\). Absorption requires a negative local field there, so no mixed configuration is absorbing. In the all-plus state \(F_i=2(J-K)+h>0\). In the all-minus state \(F_i=-2(J-K)+h\), so its strict stability is equivalent to \(h<2(J-K)\). This proves all four regimes, including equality cases.

**4. Enumeration and transfer matrix.** For a mixed weak-field configuration having \(k\) down dimers, the \(k\) up gaps all have length at least two. Placing a distinguished dimer start at any of the \(N\) labeled sites, then distributing the remaining \(N-4k\) up spins as nonnegative increments among \(k\) gaps, gives \(N\binom{N-3k-1}{k-1}\) marked configurations. Each unmarked configuration has exactly \(k\) choices of distinguished dimer, yielding the stated coefficient. The four automaton states encode (in order) 'first plus required', 'second plus required', 'free plus or begin minus dimer', and 'second minus required'. Its successive transitions are described by \(T(z)\), with weight \(z\) on each minus, and the trace counts each labeled cyclic mixed word once plus the all-plus word. The all-minus word is then added as \(z^N\). This proves the exact polynomial identity.

**5. Entropy and limiting typical magnetization.** The nonnegative transfer matrix at \(z=1\) is irreducible and aperiodic (there is a self-loop at the freely extendible plus state). Perron–Frobenius theory and \(\det(\lambda I-T(z))=\lambda^4-\lambda^3-z^2\) give a unique dominating root \(\lambda_*>1\), and \(\operatorname{tr}(T(1)^N)\sim\lambda_*^N\). Outside the weak positive field interval the number of blocked configurations is bounded by six, proving zero entropy there. With fugacity \(z\), the Perron eigenvalue is analytic near one; differentiating its characteristic equation gives the down-spin density under the normalized polynomial law,

\[
\lim_{N\to\infty}\frac1N\frac{B_N'(1)}{B_N(1)}
=\left.\frac{z\lambda'(z)}{\lambda(z)}\right|_{z=1}
=\frac{2(\lambda_*-1)}{4\lambda_*-3}.
\]

The two extra uniform words do not affect this limit. Every step applies uniformly over the stated open coupling region.

## Verification

A standalone standard-library checker, `check_absorbing.py`, independently constructs the full Hamiltonian and evaluates all proposed single-site flips without using the local-domain derivation. It exhaustively compares the number of absorbing words at each magnetization against the piecewise theorem for ring lengths \(5\le N\le14\), four coupling choices, and field samples on and around both transition surfaces. It reports **330 passing finite-state parameter comparisons**. For weak fields, the total counts for lengths \(5,6,8,10,12,14\) are respectively \(7,8,14,27,48,93\). The transfer-matrix characteristic polynomial was also checked symbolically. These finite experiments test the formulas but do not replace the preceding proof for arbitrary ring length.

## Relationship to prior work

Redner and Krapivsky (1998) and Grynberg (2014) study the competing-interaction Glauber chain at zero applied field, emphasizing domain-wall motion, metastable sectors, and finite-temperature spectral relaxation. Their zero-field domain arguments provide the central physical context, but the longitudinal-field strict-absorption phase diagram and the resulting singular absorbing-state entropy are not statements of their examined results. Pini and Rettori (2007) analyze linear response to a weak time-varying external field at finite temperature, distinct from exact zero-temperature strict absorption under a static field. De Smedt, Godrèche, and Luck (2002) compute blocked-state statistics for kinetically constrained one-dimensional spin models; the model constraints and Hamiltonian are different here. The domain-word transfer method itself is standard and is not claimed as new. The asserted contribution is the simultaneous exact weak-field freezing mechanism, complete finite-volume count, sharp field thresholds, and resulting entropy discontinuity for this natural competing-interaction Glauber dynamics.

## Limitations

The theorem assumes periodic rings of at least five sites, a strictly ferromagnetic-dominated next-nearest-neighbor coupling \(0<K<J/2\), a **uniform nonnegative longitudinal field**, and the zero-temperature convention admitting neutral flips. It does not cover the multiphase coupling boundary, field disorder, energy-neutral-suppressing dynamics, finite-temperature metastability, or the basins of attraction and kinetic selection probabilities. The entropy describes *all absorbing configurations*, not a thermodynamic Gibbs entropy or the dynamical distribution of final states. Although the literature comparison did not find this exact field-dependent classification, an unindexed equivalent local-pattern enumeration remains possible.

## References

- S. Redner and P. L. Krapivsky, *Slow Coarsening in an Ising Chain with Competing Interactions* (1998), arXiv:cond-mat/9805385, https://arxiv.org/abs/cond-mat/9805385.
- M. D. Grynberg, *Low temperature Glauber dynamics under weak competing interactions* (2014), arXiv:1412.6588, https://arxiv.org/abs/1412.6588.
- M. G. Pini and A. Rettori, *Effect of antiferromagnetic exchange interactions on the Glauber dynamics of one-dimensional Ising models* (2007), arXiv:0707.1953, https://arxiv.org/abs/0707.1953.
- G. De Smedt, C. Godrèche, and J. M. Luck, *Jamming, freezing and metastability in one-dimensional spin systems* (2002), arXiv:cond-mat/0202465, https://arxiv.org/abs/cond-mat/0202465.

