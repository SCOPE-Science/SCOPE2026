# Rational resonance governs approximation-number decay of contracting composition mixtures
## Finding
Let \(\mathcal H\) be a complex Hilbert space of analytic functions on \(\mathbb D\) with continuous point evaluations, in which the monomials \(1,z,z^2,\ldots\) are nonzero, mutually orthogonal and complete. Fix \(0<r<1\), finitely many angles \(\theta_j\in\mathbb R\), and coefficients \(c_j\in\mathbb C\), and define
\[
T=\sum_{j=1}^m c_j C_{\varphi_j},\qquad \varphi_j(z)=r e^{i\theta_j}z,\qquad f(n)=\sum_{j=1}^m c_j e^{in\theta_j}.
\]
Suppose \(f\) is not identically zero on the nonnegative integers. Merge coincident angles modulo \(2\pi\) and cancel zero combined coefficients. Write \(j\sim k\) when \((\theta_j-\theta_k)/(2\pi)\in\mathbb Q\); let \(\mathcal E\) be the resulting classes. Let \(q\ge1\) be the least positive integer for which \(q(\theta_j-\theta_k)/(2\pi)\in\mathbb Z\) whenever \(j\sim k\). For each residue \(s\in\{0,\ldots,q-1\}\), write
\[
B_{E,s}=\sum_{j\in E}c_j e^{is\theta_j},\quad E\in\mathcal E,\qquad
k_0=\#\{s:B_{E,s}=0\ \text{for every}\ E\in\mathcal E\},\quad a=1-\frac{k_0}{q}>0.
\]
With approximation numbers \(a_N(T)=\inf_{\mathrm{rank}K<N}\|T-K\|\) and \(\mathcal N_T(\varepsilon)=\#\{N\ge1:a_N(T)>\varepsilon\}\), the exact logarithmic counting law and exponential approximation rate are
\[
\boxed{\mathcal N_T(\varepsilon)=\frac{a}{\log(1/r)}\log(1/\varepsilon)+o\!\left(\log(1/\varepsilon)\right)},\qquad \varepsilon\downarrow0,
\]
\[
\boxed{\lim_{N\to\infty}a_N(T)^{1/N}=r^{1/a}=r^{q/(q-k_0)}}.
\]
In particular, this rate depends **only on the rational-resonance extinction classes**, not on the monomial norms, irrational Diophantine type or sizes of nonvanishing coefficients. The possible rates at fixed \(r\), over all nonzero finite complex mixtures, are exactly
\[
\boxed{\{r^\xi:\xi\in\mathbb Q,\ \xi\ge1\}}.
\]
For \(T_\alpha=C_{rz}-C_{r e^{2\pi i\alpha}z}\), the rate is \(r\) at every irrational \(\alpha\); it is \(r^{q/(q-1)}\) at every nonintegral rational \(\alpha=p/q\) in lowest terms. At integral \(\alpha\), \(T_\alpha=0\) and the rate is zero. Although \(\alpha\mapsto T_\alpha\) is continuous in operator norm, its exponential approximation rate is continuous precisely at irrational parameters and discontinuous at every rational parameter.

## Assumptions and scope
The coefficients are complex; the finite mixture may have arbitrary signs and phases. An analytic coefficient Hilbert space with continuous point evaluations and complete orthogonal monomials suffices, including \(H^2\), standard weighted Bergman spaces and monomial-orthogonal Dirichlet spaces. No unconditional-basis assumption beyond Hilbert orthogonality is needed. The zero operator is excluded from the general logarithmic law because \(a_N(0)=0\); it is covered explicitly in the two-term family. The denominator \(q=1\) if no two distinct angles have a rational difference modulo \(2\pi\). Extinguished residues are defined using **all** rational-equivalence class sums; isolated zeros at other indices do not count as extinct residues.

## Proof
**1. Exact singular-value model.** Normalize \(e_n=z^n/\|z^n\|_{\mathcal H}\). Then \(C_{r e^{i\theta}z}e_n=r^n e^{in\theta}e_n\). Hence \(T e_n=r^nf(n)e_n\), so \(T\) is compact and its singular values are the decreasing rearrangement (including zeros) of \(r^n|f(n)|\), \(n\ge0\). Indeed \(|f(n)|\le M=\sum_j|c_j|\), so the diagonal entries tend to zero. It follows exactly that
\[
\mathcal N_T(\varepsilon)=\#\{n\ge0:r^n|f(n)|>\varepsilon\}.
\]
The use of an arbitrary monomial-normalizing weight cancels from this formula.

**2. Rational residues and compact group.** Fix representatives \(\theta_E\) for \(E\in\mathcal E\). By the choice of \(q\), \(e^{iq\theta_j}=\mu_E:=e^{iq\theta_E}\) for every \(j\in E\). Therefore
\[
f(qt+s)=\sum_{E\in\mathcal E}B_{E,s}\mu_E^t,\qquad t\ge0,\quad 0\le s<q.
\]
For distinct classes, \(\mu_E/\mu_F\) is not a root of unity; otherwise \(qM(\theta_E-\theta_F)/(2\pi)\in\mathbb Z\) for some integer \(M>0\), contradicting distinctness. An extinguished residue gives identically zero entries. For an active residue, at least one class coefficient is nonzero.

Fix such an active residue. Let \(G=\overline{\{(\mu_E^t)_{E\in\mathcal E}:t\in\mathbb Z\}}\), a compact subgroup of the finite torus, and set \(g=(\mu_E)_E\). Haar equidistribution of the forward orbit \(g^t\) in \(G\) follows directly from the character criterion: every nontrivial continuous character \(\chi\) on \(G\) obeys \(\chi(g)\ne1\) since \(g\) topologically generates \(G\), and the geometric averages of \(\chi(g)^t\) tend to zero. Denote the coordinate characters by \(\chi_E\). The group \(G\) has finitely many connected components and its identity component \(G^0\) is a torus. The restrictions \(\chi_E|_{G^0}\) are pairwise distinct: if two agreed, their quotient would factor through the finite group \(G/G^0\), so some power of the quotient would be trivial on all of \(G\), implying that \(\mu_E/\mu_F\) is a root of unity.

Now consider \(F_s(x)=\sum_E B_{E,s}\chi_E(x)\). On each component \(hG^0\), the characters remain distinct and orthogonal as characters of \(G^0\); therefore \(F_s\) cannot vanish identically on any component, because at least one coefficient \(B_{E,s}\) is nonzero. Its restriction to each connected torus is a nonzero real-analytic complex-valued function. The zero set has Haar measure zero: applying the standard fact to the nonzero real-analytic function \(|F_s|^2\) suffices. The same conclusion holds for a zero-dimensional component, where nonidentical means nonzero at that point. Thus Haar measure of \(\{|F_s|\le\delta\}\) decreases to zero as \(\delta\downarrow0\). Haar equidistribution and the closed-set upper bound imply
\[
\lim_{\delta\downarrow0}\limsup_{L\to\infty}\frac{1}{L}\#\{0\le t<L:|f(qt+s)|\le\delta\}=0
\]
for every active residue. In particular, positive entries on active residues have asymptotic density one within that residue, even if their amplitudes approach zero along subsequences. There are \(q-k_0\) active residue classes, so their union has density \(a\).

**3. Level counting.** Put \(\lambda=\log(1/r)>0\), \(L=\lambda^{-1}\log(1/\varepsilon)\). Since \(|f(n)|\le M\), every counted index obeys \(n<L+\lambda^{-1}\log M\). Because all extinguished residue classes contribute zero, this proves \(\limsup_{\varepsilon\downarrow0}\mathcal N_T(\varepsilon)/L\le a\). For any fixed \(0<\eta<1\) and \(\delta>0\), when \(n\le(1-\eta)L\) and \(|f(n)|>\delta\) one has \(r^n|f(n)|\ge\delta\varepsilon^{1-\eta}>\varepsilon\) for sufficiently small \(\varepsilon\). By the preceding zero-density bound, \(\delta\) may be chosen so that among the first \((1-\eta)L\) indices the fraction of active indices failing \(|f(n)|>\delta\) has arbitrarily small upper density. Therefore \(\liminf\mathcal N_T(\varepsilon)/L\ge(1-\eta)a\). Letting \(\eta\downarrow0\) proves the counting law. Since the nonzero singular-value sequence is infinite, the usual inverse-counting inequalities imply \(-\log a_N(T)/N\to\lambda/a\). This is the asserted exponential approximation rate.

**4. Every rational rate is realized.** Fix \(q\ge1\), \(1\le h\le q\), and any set \(S\subset\{0,\ldots,q-1\}\) with \(|S|=h\). Choose \(\theta_j=2\pi j/q\) and
\[
c_j=\frac1q\sum_{s\in S}e^{-2\pi i j s/q},\qquad 0\le j<q.
\]
Fourier inversion gives \(f(n)=1\) when \(n\bmod q\in S\) and \(f(n)=0\) otherwise, exactly. The nonzero diagonal singular coefficients are therefore \(r^n\) at a set of density \(h/q\), so the rate is \(r^{q/h}\). Every rational exponent at least one has this form. The general theorem already ensures no other rates are possible.

**5. Two-symbol discontinuity.** For \(T_\alpha\), \(f(n)=1-e^{2\pi i n\alpha}\). If \(\alpha\) is irrational, the two angles are in different rational-equivalence classes, so \(q=1\), \(k_0=0\). If \(\alpha=p/q\notin\mathbb Z\) is reduced, \(f(n)=0\) exactly when \(q\mid n\), so \(k_0=1\). For integers the operator is zero. The map \(\alpha\mapsto T_\alpha\) is norm-Lipschitz, since
\[
\|T_\alpha-T_\beta\|\le 2\pi|\alpha-\beta|\sup_{n\ge0}nr^n<\infty\cdot|\alpha-\beta|.
\]
Near an irrational point, any sequence of distinct rational approximants has denominators tending to infinity and their rates converge to \(r\); irrational approximants have rate \(r\). Every rational point is approximated by irrationals of rate \(r\), different from its own rate. This proves the exact continuity classification.

## Verification
The proof is analytic and infinite-dimensional. The exact singular-value diagonalization, finite-group/torus equidistribution, componentwise zero-set argument, cutoff inequalities and discrete Fourier inversion are the critical steps. A standalone Python file `check_examples.py` performs 1144 supplementary finite diagnostics for rational and irrational two-symbol examples and Fourier-inverse residue filters. The diagnostic tolerance tests are *not* the proof of zero-density, Haar equidistribution or the asymptotic limit. All required asymptotic assertions follow from the arguments above; no independent audit has been performed.

## Relationship to prior work
Li, Wang and Zhao (2026), arXiv:2609.28111v1, characterize **compactness** of finite sums of composition operators on Bergman–Orlicz spaces. Their results motivate asking how fast approximation numbers decay after compactness; they do not state the Hilbert-space rational-resonance counting and realization theorem. Bayart, Gilmore and Şahin (2025), arXiv:2509.19797v1, study approximation numbers of **differences** and obtain upper/lower estimates for boundary-contact and corner-type symbols. The present strictly contracting, same-radius finite-phase model is diagonal and has exact arithmetic limit laws, rather than their boundary-geometry estimates. Li, Queffélec and Rodríguez-Piazza (2014), arXiv:1407.2171, determine the exponential approximation-number limit for an **individual** composition operator with image compactly inside the disk; a finite complex linear combination with cancellations is not itself generally a composition operator, and its rate may be strictly smaller than that of each summand. Classical compact-torus equidistribution and Fourier character orthogonality are acknowledged as standard ingredients, not asserted as new results. Prior work on exponential sums may contain equivalent density statements; the new assertion is their complete approximation-number consequence and inverse rate realization for these operator mixtures.

## Limitations
The theorem addresses common-modulus contracting linear symbols and complex Hilbert coefficient spaces with orthogonal monomials. It does not classify nonlinear symbols, unequal moduli, arbitrary Banach–Orlicz spaces or precise multiplicative prefactors for approximation numbers. The logarithmic counting remainder is only \(o(\log(1/\varepsilon))\) in general: irrational phases may preclude a uniform bounded error. A search and comparison of available literature does not prove global publication priority; an earlier treatment using exponential-polynomial zero density is a residual risk. Finite diagnostic code is not a substitute for independent mathematical validation.

## References
1. Y. Li, Z. Wang, L. Zhao, *Compact linear combination of composition operators on Bergman-Orlicz spaces*, arXiv:2609.28111v1 (first posted 2026-09-23), https://arxiv.org/abs/2609.28111.
2. F. Bayart, C. Gilmore, S. Şahin, *Approximation Numbers of Differences of Composition Operators*, arXiv:2509.19797v1 (2025), https://arxiv.org/html/2509.19797v1.
3. D. Li, H. Queffélec, L. Rodríguez-Piazza, *A spectral radius type formula for approximation numbers of composition operators*, arXiv:1407.2171v1 (2014), https://arxiv.org/abs/1407.2171.
4. Standard compact-abelian-group character equidistribution and analytic zero-set facts, as proved in the text for this application.
