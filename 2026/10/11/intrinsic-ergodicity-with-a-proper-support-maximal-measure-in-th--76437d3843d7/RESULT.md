# Intrinsic ergodicity with a proper-support maximal measure in the one-sided balanced construction

## Finding
For every \(h>0\), let \(X\) be the coded system of Theorem 3.7 of Hong and Kim. Their construction uses a synchronizing marker \(\bar 1\), a one-block factor
\[
\pi:X\longrightarrow\mathsf X(S),\qquad \pi(\bar 1)=1,
\]
and a proper marker-free subshift \(Y\subsetneq X\) with variable specification and
\[
h(Y)=h(X)=h.
\]
Put \(\lambda=e^h\), write \(h(\mathsf X(S))=\log\eta<\log\lambda\), and take the construction parameter satisfying
\[
\alpha<1-\frac{\log\eta}{\log\lambda}.
\]
**For every ergodic** invariant probability measure \(\mu\) on \(X\), positive marker frequency implies the uniform entropy estimate
\[
\mu([\bar 1])>0\quad\Longrightarrow\quad
h_\mu(X)\le \log\eta+\alpha\log\lambda<\log\lambda=h(X).
\]
For an arbitrary (not necessarily ergodic) invariant measure, positive marker frequency still implies \(h_\mu(X)<h(X)\), but the displayed uniform quantitative bound need not hold.

Consequently every measure of maximal entropy on \(X\) gives the marker zero mass and is supported on \(Y\). The variable-specification subsystem \(Y\) has a unique fully supported measure of maximal entropy. Hence \(X\) also has a unique measure of maximal entropy, supported on the proper subshift \(Y\), even though \(X\) is not entropy minimal.

For every prescribed positive entropy this yields a synchronized one-sided-balanced shift that is intrinsically ergodic but not entropy minimal, and whose unique maximal measure is not fully supported on the ambient shift.

## Assumptions and scope
The assertion concerns the particular coded systems of Hong--Kim Theorem 3.7, not arbitrary synchronized or one-sided-balanced shifts. The notation \(\lambda,\eta,\alpha,Y,S,\bar1\) follows that construction. The marker-free subsystem is precisely \(Y\), as witnessed by the source's equality of the all-zero factor fibers with the word sets of \(Y\). The positive-entropy, strict parameter inequality and the source's factor-word lift estimates are hypotheses used here. Nothing is asserted about the uniqueness of equilibrium states for general potentials.

The qualifier **ergodic** in the quantitative inequality is essential. An arbitrary invariant measure can be a convex combination of a maximal measure supported on \(Y\) and a marker-positive invariant measure; its marker frequency can be positive but arbitrarily small, while its entropy approaches \(h(X)\). Such mixtures are not subject to a uniform entropy gap independent of marker frequency.

## Proof
For an \(n\)-letter word \(w\) in \(Z=\mathsf X(S)\), write \(R_n(w)\) for the number of terminal zeros following its last \(1\), and put \(R_n(0^n)=n\). The source's last-marker estimate, when the last \(1\) is at position \(k\), states
\[
|\pi^{-1}(w)|\le p c_Y^2\lambda^{k\alpha+(n-k)}.
\]
For the all-zero factor word it identifies \(\pi^{-1}(0^n)=\mathcal B_n(Y)\), and gives \(|\pi^{-1}(0^n)|\le c_Y\lambda^n\). Absorbing the fixed constants into \(C\ge1\), both cases give
\[
\log|\pi^{-1}(w)|\le \log C+\alpha n\log\lambda
 +(1-\alpha)R_n(w)\log\lambda.\tag{1}
\]

Let \(\mu\) be ergodic, with \(\delta=\mu([\bar1])>0\), and let \(\nu=\pi_*\mu\), also ergodic. Then \(\nu([1])=\delta\). By the pointwise ergodic theorem, the number of \(1\)'s among the first \(n\) coordinates is \(\delta n+o(n)\) almost surely. If \(R_n\ge\varepsilon n\) for infinitely many \(n\), then the count of \(1\)'s in the first \(n\) positions equals the count in at most the first \((1-\varepsilon)n\) positions on that subsequence, contradicting the same ergodic-frequency limit along the shorter prefixes. Thus \(R_n/n\to0\) almost surely. Since \(0\le R_n/n\le1\), dominated convergence gives
\[
\frac1n\int R_n\,d\nu\longrightarrow0.\tag{2}
\]

For the length-\(n\) word partitions \(\mathcal P_X^n\) and \(\mathcal P_Z^n\), conditioning on the factor word bounds conditional entropy by the logarithm of its number of lifts:
\[
H_\mu(\mathcal P_X^n)
\le H_\nu(\mathcal P_Z^n)+\int\log|\pi^{-1}(w)|\,d\nu(w).
\]
Divide by \(n\), use (1)--(2), and take the entropy limits. Since \(h_\nu(Z)\le h(Z)=\log\eta\),
\[
h_\mu(X)\le h_\nu(Z)+\alpha\log\lambda
\le\log\eta+\alpha\log\lambda<\log\lambda.
\tag{3}
\]
This proves the quantitative estimate for every **ergodic** marker-positive measure.

For a general invariant \(\mu\), write its ergodic decomposition as \(\mu=\int\mu_\omega\,d\rho(\omega)\). Entropy is affine under this decomposition. If \(\mu([\bar1])>0\), a positive-\(\rho\)-measure set of components has \(\mu_\omega([\bar1])>0\), and each such component satisfies (3), whereas all other components have entropy at most \(h(X)\). Therefore the average entropy is strictly less than \(h(X)\). Importantly, this does **not** put the same uniform upper bound from (3) on the entropy of the mixture: its marker-zero ergodic components may have entropy \(h(X)\).

In particular, if \(\mu\) is any measure of maximal entropy on \(X\), its ergodic components are almost surely maximal, since all their entropies are bounded above by \(h(X)\) and their average is \(h(X)\). By (3), none of those components can have positive marker frequency. Thus \(\mu([\bar1])=0\), and invariance makes every shift of the marker cylinder have measure zero. The measure is therefore supported on the closed marker-free subsystem, which the construction identifies with \(Y\).

Conversely, any maximal-entropy measure on \(Y\) is maximal on \(X\), since \(h(Y)=h(X)\). Hence the sets of maximal measures on \(X\) and on \(Y\) coincide. The source's variable-specification result supplies intrinsic ergodicity and full support for the unique maximal measure on \(Y\). Therefore this is the unique maximal measure on \(X\) too, with support exactly \(Y\subsetneq X\). The ambient system is not entropy minimal because it has this proper full-entropy subshift.

## Verification and precise scope of the repair
The proof uses the published factor-fiber bounds and the exact all-zero-fiber identification; these are not inferred from numerical experiments. The measure-theoretic step from positive marker frequency to sublinear terminal zero runs uses ergodicity. The passage from ergodic maximal measures to arbitrary maximal measures instead uses ergodic decomposition and entropy affinity.

The original version of the quantitative statement omitted the ergodicity hypothesis. That stronger version is unjustified and, whenever marker-positive invariant measures exist, false. Indeed, let \(\mu_Y\) be the maximal measure supported on \(Y\) and \(\nu\) any marker-positive invariant measure. For \(0<t<1\), the invariant mixture \(\mu_t=(1-t)\mu_Y+t\nu\) satisfies \(\mu_t([\bar1])>0\) and
\[
h_{\mu_t}(X)=(1-t)h(X)+t h_\nu(X)\longrightarrow h(X)
\quad(t\downarrow0).
\]
For sufficiently small \(t\), this exceeds the fixed strict upper bound \(\log\eta+\alpha\log\lambda\), while remaining below \(h(X)\). Correcting the quantitative quantifier leaves the maximal-measure localization and uniqueness conclusion unchanged.

## Relationship to prior work
Hong and Kim construct the one-sided-balanced examples, prove their topological entropy and proper equal-entropy variable-specification subsystem, and provide the word-lift estimates used here. Their main result about synchronized bi-balanced shifts concerns a different, entropy-minimal regime. The extra conclusion here is the localization of all maximal-entropy measures on the marker-free subsystem and resulting uniqueness for these one-sided-balanced examples.

Thomsen's synchronized-system theory gives general structural results for fully supported maximal measures, but does not itself establish uniqueness of a maximal measure with support strictly smaller than \(X\). An earlier result about entropy-minimal bi-balanced shifts concerns word-avoidance exponents rather than these proper-full-entropy one-sided-balanced examples.

## Limitations
The conclusion is specific to the Hong--Kim coded family and relies on its precise fiber estimates and variable-specification subsystem. It is not a statement about all synchronized shifts or all one-sided-balanced examples. There is no uniform entropy gap for arbitrary nonergodic marker-positive measures without controlling their marker-positive ergodic weight. No mixing rate, Bernoulli property, or uniqueness for nonzero potentials is established. An antecedent thesis cited by the source was not independently inspectable and may contain an earlier equivalent maximal-measure observation.

## References
1. S. Hong and M. Kim, *Bi-balanced shifts and variable specification*, arXiv:2609.33476v1 (2026).
2. K. Thomsen, *On the ergodic theory of synchronized systems*, Ergodic Theory and Dynamical Systems (2006).
