# Sharp prime-power ambiguity of left-right orbit signatures

## Finding

Let \(p\) be a prime, \(k\geq1\), and \(N=p^k\). For any cyclic permutation \(\sigma\) of a strictly ordered set \(S=\{x_1<\cdots<x_N\}\), write \(\mathcal U(\sigma)\) for the invertible residues \(u\pmod N\) satisfying

\[
\operatorname{sgn}(\sigma^{ut}(x)-x)=\operatorname{sgn}(\sigma^{t}(x)-x)
\quad\text{for every }x\in S\text{ and every }t\geq1.
\]

Thus each \(u\in\mathcal U(\sigma)\) gives an \(N\)-cycle \(\sigma^u\) with the same *complete left-right behavior* as \(\sigma\). The sharp extremum is

\[
\boxed{\max_{\sigma\text{ an }N\text{-cycle}} |\mathcal U(\sigma)|=p^{k-1}.}
\]

A maximizing cycle is explicitly constructed by ordering the time indices \(0,\ldots,N-1\) according to the reversal of their \(k\) base-\(p\) digits. For this cycle,
\[
\mathcal U(\sigma)=\{u\pmod N:u\equiv1\pmod p\}.
\]

For \(k\geq2\), there are consequently \(p^{k-1}\) **distinct powers of one orbit permutation** with identical signatures. No assertion is made about the full number of arbitrary cycles sharing a signature.

## Assumptions and scope

The set \(S\) is strictly linearly ordered, with no repeated points. An \(N\)-cycle permutes every point in a single orbit; \(\operatorname{sgn}\) takes values \(-1,0,1\) according to the sign of the difference of two ordered points. Powers \(\sigma^u\) are restricted to units \(\gcd(u,N)=1\), ensuring that they too are \(N\)-cycles. The all-time condition is equivalent to checking \(1\leq t<N\) because all orbit signs are \(N\)-periodic and zero when \(N\mid t\).

The theorem applies to every prime \(p\) and integer \(k\geq1\); it optimizes among powers of a fixed cycle and then maximizes over all such cycles on \(S\). It is a finite orbit-combinatorics theorem motivated by recovery of interval-map periodic orbit dynamics.

## Proof

**1. Universal bound from the second-smallest point.** Fix an arbitrary \(N\)-cycle \(\sigma\). As \(x_1\) is the only point strictly below \(x_2\), there is a unique residue \(t_0\in\{1,\ldots,N-1\}\) such that \(\sigma^{t_0}(x_2)=x_1\). The sign of \(\sigma^t(x_2)-x_2\) is negative precisely when \(t\equiv t_0\pmod N\). If \(u\in\mathcal U(\sigma)\), comparing signs at time \(t=t_0\) yields \(\sigma^{ut_0}(x_2)=x_1\), and therefore
\[
(u-1)t_0\equiv0\pmod{p^k}.
\]
Write \(v=\nu_p(t_0)\), so \(0\leq v\leq k-1\). This congruence forces \(u\equiv1\pmod{p^{k-v}}\). There are exactly \(p^v\) such residues modulo \(p^k\), and all of them are units. Hence \(|\mathcal U(\sigma)|\leq p^v\leq p^{k-1}\). This includes \(k=1\).

**2. Digit-reversal construction.** Identify the time indices with \(j\in\{0,\ldots,p^k-1\}\) and write uniquely \(j=\sum_{a=0}^{k-1}j_a p^a\) with \(j_a\in\{0,\ldots,p-1\}\). Set
\[
R(j)=\sum_{a=0}^{k-1}j_a p^{k-1-a}.
\]
On the ordered set \(S=\{0,1,\ldots,N-1\}\), define \(\sigma(R(j))=R(j+1\bmod N)\). As \(R\) is a bijection, this is an \(N\)-cycle.

For any \(j\) and \(1\leq t<N\), put \(a=\nu_p(t)\). The base-\(p\) digits of \(j+t\bmod N\) and \(j\) agree in all positions \(b<a\), while the digit at position \(a\) differs. Because \(R\) reverses digit significance, the sign of \(R(j+t\bmod N)-R(j)\) depends only on comparing the two digits at position \(a\). Specifically, writing \(t=p^a h\) with \(p\nmid h\), the digit at position \(a\) changes from \(j_a\) to \((j_a+h)\bmod p\), and no digit at smaller index changes.

If \(u\equiv1\pmod p\), then \(\nu_p(ut\bmod N)=a\), and the nonzero digit of \(ut\) at position \(a\) is the same as that of \(t\). Thus the changed digit—and hence the full sign—is exactly the same for the increments \(t\) and \(ut\) at every \(j\). Therefore \(\mathcal U(\sigma)\) includes every unit \(u\equiv1\pmod p\), of which there are \(p^{k-1}\). Together with the universal bound this proves both the extremum and exact equality for the construction. \(\square\)

## Verification

The standalone standard-library program `verify.py` directly constructs digit-reversal cycles for several prime powers and compares, for every unit multiplier, the complete orbit sign matrices rather than relying on the digit lemma. It also enumerates *every* full cycle on ordered sets of sizes \(4\), \(8\), and \(9\), checks the general upper bound, and reports the attained maxima. Run `python3 verify.py`. Those finite tests confirm boundary cases but do not constitute the proof for arbitrary \(p\) and \(k\); the two arguments above establish the universal theorem.

## Relationship to prior work

Fuhrmann, Gröger, and Passeggi, Section 2, define the complete left-right behavior of a finite periodic orbit and prove uniqueness of a prime-length cycle (Lemma 2.1). Their Figure 2 and accompanying remarks show that distinct composite-length cycles can share such behavior. The present claim is more specific in one respect (it compares **powers of a common cycle**, not all possible cycles) but adds the sharp exact *maximum multiplicity at every prime-power length* and a uniform maximizing construction. Their composite-period existence observation does not imply the number \(p^{k-1}\) or its sharpness.

A separately published quadratic-time prime-cycle reconstruction result addresses the prime-length case and does not determine composite prime-power ambiguity. Digit reversal is a standard ordering device; only its new application to this extremal signature invariant is assessed here.

## Limitations

The theorem does not count cycles outside the cyclic subgroup generated by \(\sigma\), does not optimize over general composite lengths having multiple prime factors, and does not assert existence of any specified global interval map realizing a selected finite cycle. Related p-adic order combinatorics may yield alternative formulations, so historical priority is not independently certified. The accompanying finite enumeration is not an infinite verification. An independent audit has not been performed.

## References

- G. Fuhrmann, M. Gröger, A. Passeggi, *Period spectrum and rigidity of interval maps*, arXiv:2610.07435v1, publicly posted 2026-10-05, Section 2, Lemma 2.1 and Figure 2. https://arxiv.org/html/2610.07435v1
- *Quadratic-time reconstruction of prime cycles from left-right orbit signatures*, published research record `2026/10/11/SCOPE-quadratic-time-reconstruction-of-prime-cycles-from-left-right-or--f270190d0cd7`, comparison limited to published indexed claim, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-quadratic-time-reconstruction-of-prime-cycles-from-left-right-or--f270190d0cd7
