# Intrinsic ergodicity with a proper-support maximal measure in the one-sided balanced construction

## Finding
For every \(h>0\), let \(X\) be the coded system in Theorem 3.7 of Hong and Kim. Their construction uses a synchronizing marker \(\bar 1\), a one-block factor
\[
\pi:X\longrightarrow \mathsf X(S),
\]
with \(\pi(\bar 1)=1\), and a proper marker-free subshift \(Y\subsetneq X\) with variable specification and
\[
h(Y)=h(X)=h.
\]
Write \(\lambda=e^h\), let \(h(\mathsf X(S))=\log\eta<\log\lambda\), and let the construction parameter satisfy
\[
\alpha<1-\frac{\log\eta}{\log\lambda}.
\]
Then every invariant probability measure \(\mu\) on \(X\) with positive marker frequency satisfies
\[
\mu([\bar 1])>0
\quad\Longrightarrow\quad
h_\mu(X)\le \log\eta+\alpha\log\lambda<\log\lambda=h(X).
\]
Therefore every measure of maximal entropy of \(X\) gives zero mass to the marker and is supported on \(Y\). The subshift \(Y\) has variable specification, so it is intrinsically ergodic and its unique maximal-entropy measure is fully supported on \(Y\). Hence \(X\) is intrinsically ergodic too, with the same unique maximal-entropy measure, whose support is exactly the proper subshift \(Y\).

In particular, for every prescribed positive entropy there is a synchronized one-sided balanced shift that is intrinsically ergodic but not entropy minimal, and whose unique maximal-entropy measure is not fully supported on the ambient shift.

## Assumptions and scope
The statement concerns the specific coded systems constructed in Theorem 3.7 of Hong--Kim. The notation \(\lambda,\eta,\alpha,Y,S,\bar 1\) is exactly the notation of that construction. No assertion is made that every synchronized one-sided balanced shift is intrinsically ergodic, or that every proper full-entropy extension has the same localization property.

The marker-free subsystem is exactly \(Y\): the source's entropy count identifies the all-zero factor fiber \(\pi^{-1}(0^n)\) with \(\mathcal B_n(Y)\) for every \(n\). The strict inequality \(\log\eta+\alpha\log\lambda<\log\lambda\) is one of the defining parameter inequalities in the construction.

## Proof
For an \(n\)-word \(w\) in the factor \(\mathsf X(S)\), let \(R_n(w)\) be the number of trailing zeros after the last occurrence of \(1\); for \(w=0^n\), put \(R_n(w)=n\). The source proves that if the last \(1\) occurs at coordinate \(k\), then
\[
|\pi^{-1}(w)|
\le p c_Y^2\lambda^{k\alpha+(n-k)}.
\]
For the all-zero word it proves \(\pi^{-1}(0^n)=\mathcal B_n(Y)\), hence
\[
|\pi^{-1}(0^n)|\le c_Y\lambda^n.
\]
Thus there is a constant \(C\ge1\), independent of \(n\) and \(w\), such that
\[
\log|\pi^{-1}(w)|
\le \log C+\alpha n\log\lambda
 +(1-\alpha)R_n(w)\log\lambda.
\]

First let \(\mu\) be ergodic and suppose \(\delta=\mu([\bar 1])>0\). Put \(\nu=\pi_*\mu\). Then \(\nu([1])=\delta\). By the ergodic theorem, the final run of zeros in a typical length-
\(n\) factor block is sublinear:
\[
\frac{R_n}{n}\longrightarrow0
\quad\text{for }\nu\text{-almost every point}.
\]
Indeed, if \(R_n\ge\varepsilon n\) along an infinite subsequence, then the number of ones in the first \(n\) coordinates would equal the number in the first at most \((1-\varepsilon)n\) coordinates along that subsequence, contradicting the two ergodic-frequency limits. Since \(0\le R_n/n\le1\), dominated convergence also gives
\[
\frac1n\int R_n\,d\nu\longrightarrow0.
\]

Let \(\mathcal P_X^n\) and \(\mathcal P_Z^n\) be the length-
\(n\) word partitions of \(X\) and \(Z=\mathsf X(S)\). Conditional entropy on each factor cylinder is at most the logarithm of the number of lifts, so
\[
H_\mu(\mathcal P_X^n)
\le H_\nu(\mathcal P_Z^n)
 +\int\log|\pi^{-1}(w)|\,d\nu(w).
\]
Divide by \(n\) and let \(n\to\infty\). The preceding fiber estimate gives
\[
h_\mu(X)
\le h_\nu(Z)+\alpha\log\lambda
\le \log\eta+\alpha\log\lambda
<\log\lambda.
\]
Thus no ergodic maximal-entropy measure can assign positive mass to the marker.

For an arbitrary maximal-entropy measure, apply the ergodic decomposition and affinity of measure entropy. Since every ergodic component has entropy at most \(h(X)\) and their average equals \(h(X)\), almost every component is itself maximal; hence almost every component gives the marker zero mass. Therefore the original measure gives zero mass to every translate of the marker cylinder and is supported on the marker-free subsystem \(Y\).

Conversely, every maximal-entropy measure on \(Y\) is maximal on \(X\) because \(h(Y)=h(X)\). Thus the maximal-entropy measures of \(X\) and \(Y\) coincide. The source proves that variable specification yields intrinsic ergodicity with a fully supported maximal-entropy measure, so \(Y\) has a unique such measure. This proves the asserted uniqueness on \(X\), with support exactly \(Y\subsetneq X\).

Finally, \(X\) is not entropy minimal because it contains the proper subshift \(Y\) with \(h(Y)=h(X)\).

## Verification
The proof was checked directly against the construction's factor-fiber bounds. The critical source estimates are the bounds for \(\pi^{-1}(0^l1)\), the synchronization product estimate, the resulting last-marker estimate
\[
|\pi^{-1}(w)|\le p c_Y^2\lambda^{k\alpha+(n-k)},
\]
and the identification of the all-zero fiber with \(\mathcal B_n(Y)\). No finite experiment is used to infer an asymptotic statement.

The only new limiting step is the sublinearity of the terminal zero run under a factor measure with positive \(1\)-frequency; this is a direct consequence of the ergodic theorem. The conditional-entropy inequality is the standard finite-partition bound obtained by conditioning on the factor word. The non-ergodic case is handled by ergodic decomposition and entropy affinity rather than by assuming ergodicity.

## Relationship to prior work
Hong--Kim construct the one-sided balanced systems, prove their exact topological entropy, and show that they contain a proper full-entropy variable-specification subsystem. Their paper does not state that all maximal-entropy measures of these systems are supported on that subsystem, nor that the ambient examples are intrinsically ergodic. The additional point is that the source's fiber estimate becomes strictly entropy-losing as soon as the marker has positive invariant frequency.

Thomsen's work on synchronized systems gives general structure and uniqueness results for fully supported maximal-entropy measures, while Hong--Kim use those results in their bi-balanced theory. Those theorems do not imply uniqueness here because the maximal measure found above is deliberately not fully supported on \(X\). The uniqueness instead comes from localizing all maximal measures to the proper subsystem \(Y\).

A prior quantitative result for entropy-minimal bi-balanced shifts gives exact word-avoidance exponents. It concerns a different regime: the present result studies the one-sided-balanced, non-bi-balanced counterexamples and classifies their maximal-entropy measures through the marker factor rather than through word avoidance.

## Limitations
The argument depends on the particular marker construction and its explicit preimage estimates. It does not classify maximal-entropy measures for arbitrary right-balanced or synchronized shifts.

The theorem attributed by Hong--Kim to an earlier thesis was not located as a directly inspectable full text in the bounded source search. The present comparison therefore leaves a residual bibliographic risk that the same maximal-measure localization may have been observed there. No indexed statement found in the searches implied the claim, and the 2026 paper itself does not state it.

No claim is made about rates of convergence to the maximal measure, Bernoulli properties, equilibrium states for nonzero potentials, or uniqueness outside the maximal-entropy problem.

## References
1. Soonjo Hong and Minkyu Kim, *Bi-balanced shifts and variable specification*, arXiv:2609.33476v1, 2026.
2. Klaus Thomsen, *On the ergodic theory of synchronized systems*, Ergodic Theory and Dynamical Systems, 2006.
