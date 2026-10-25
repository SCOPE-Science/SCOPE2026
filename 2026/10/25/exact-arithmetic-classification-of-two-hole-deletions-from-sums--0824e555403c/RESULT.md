# Exact arithmetic classification of two-hole deletions from sums of two squares

## Finding

Let \(\mathcal S=\{a^2:a\in\mathbb Z_{\ge0}\}\). For distinct positive integers \(u<v\), write \(\mathcal S_t=\mathcal S\setminus\{t^2\}\), \(\mathcal S_{u,v}=\mathcal S\setminus\{u^2,v^2\}\), and set
\[
P(N)=\prod_{\substack{p\equiv1\pmod4\\p\mid N}}\bigl(\nu_p(N)+1\bigr),\qquad
\delta(t)=\mathbf1_{\{\exists p\equiv1\pmod4:\ p\mid t\}}.
\]
The empty product is one. The exact two-hole classification is
\[
\boxed{\mathcal S_u+\mathcal S_v=\mathcal S+\mathcal S
\iff\delta(u)=\delta(v)=1,}
\]
\[
\boxed{\mathcal S_{u,v}+\mathcal S=\mathcal S+\mathcal S
\iff\delta(u)=\delta(v)=1\text{ and }P(u^2+v^2)\ge3.}
\]
In particular the two allocation patterns are not equivalent: \((u,v)=(5,13)\) preserves the sumset when the holes are in different factors but not when both are in one factor. There exist infinitely many coprime pairs that preserve the sumset even with both holes in one factor; hence a common splitting prime is not necessary.

## Assumptions and scope

All sumsets are sets of nonnegative integers, not multisets; \(0\in\mathcal S\). The only excluded elements are the indicated *positive* squares, and \(1\le u<v\). An integer \(p\equiv1\pmod4\) in the prime conditions is a rational prime. \(\nu_p\) is the ordinary exponent in an integer's prime factorization. All conditions and conclusions concern the entire infinite sumset, with no asymptotic, density, or finite cutoff restriction.

## Proof

**Reduction to finitely many sums.** For the one-sided deletion, any expression \(N=a^2+b^2\) can be oriented with the first square retained unless \(a,b\in\{u,v\}\). Thus a failure of \(\mathcal S_{u,v}+\mathcal S=\mathcal S+\mathcal S\) can occur only at the three *distinct* sums \(2u^2,u^2+v^2,2v^2\). At any one of those three sums, the displayed forbidden unordered pair is the unique unordered pair chosen from \(\{u,v\}\). Hence the sum survives precisely when it admits some *other* unordered nonnegative-square representation.

For the two-sided deletion, every unordered pair \(\{a,b\}\) with \(a\ne b\) can be ordered so that its first root is not \(u\) and its second root is not \(v\), because \(u\ne v\). An equal pair \(\{a,a\}\) is obstructed only when \(a=u\) or \(a=v\). Thus the only potentially lost integers are \(2u^2\) and \(2v^2\). For each, an alternative unordered representation succeeds automatically: a non-diagonal representation has a permissible order; a different diagonal representation avoids both holes.

**Jacobi multiplicities.** The classical two-square formula counts ordered signed representations of any positive sum of two squares:
\[
r_2(N)=\#\{(x,y)\in\mathbb Z^2:x^2+y^2=N\}=4P(N).
\]
For \(N=2t^2\), the obvious signed diagonal solutions \((\pm t,\pm t)\) contribute exactly four. Therefore another unordered representation exists iff \(P(2t^2)>1\). But \(P(2t^2)=\prod_{p\equiv1\ (4),\ p\mid t}(2\nu_p(t)+1)\), so this is equivalent to \(\delta(t)=1\).

For \(N=u^2+v^2\) with \(0<u<v\), the eight sign/order variants of \((u,v)\) are distinct. Any other signed representation gives an alternative unordered square pair, and conversely. Hence such an alternative exists iff \(4P(N)>8\), equivalently \(P(N)\ge3\). Applying these two equivalences at exactly the obstructed integers proves both boxed classifications, with all directions of implication.

**Distinct-prime behavior and infinitude.** At \((u,v)=(5,13)\), both \(\delta\)'s equal one, but \(5^2+13^2=194=2\cdot97\), so \(P(194)=2\). This witnesses the difference between the allocations. At \((5,37)\), the three critical sums have alternative square pairs:
\[
2\cdot5^2=1^2+7^2,\quad5^2+37^2=13^2+35^2,\quad 2\cdot37^2=23^2+47^2.
\]
The roots 5 and 37 are coprime, so no common rational prime divides them.

For infinitely many further coprime pairs fix \(u=5\) and choose \(v\) in the Chinese-remainder class
\[
v\equiv0\pmod{13},\quad v\equiv1\pmod5,\quad v\equiv3\pmod{17},\quad v\equiv4\pmod{41}.
\]
Its modulus is \(5\cdot13\cdot17\cdot41=45305\), and it contains positive integers \(v>5\) (least positive representative \(38831\)). The split prime 13 divides \(v\), whereas \(\gcd(5,v)=1\); moreover 17 and 41 both divide \(25+v^2\). Thus \(P(25+v^2)\ge4\), and all these pairs satisfy the one-sided classification. The arithmetic progression provides infinitely many distinct examples.

## Verification

A standalone Python 3 checker `verify.py` performs 7,140 independent \((u,v)\) tests with \(1\le u<v\le120\). The expected classification is calculated by trial prime factorization; a separate oracle enumerates unordered pairs of nonnegative integer squares representing each of the three potentially obstructed integers, for both allocations. All 7,140 comparisons passed. There were 954 one-sided successes, 1,540 two-sided successes and 586 examples in which the split allocation succeeded while the joint allocation failed. The checker also verifies the explicit arithmetic identities above and the CRT witness; its terminator is `CERTIFICATE_OK`. The finite checks are not used in the proof of the infinite statements.

To reproduce: `python3 verify.py` using only the Python standard library.

## Relationship to prior work

Elsholtz--Stadlmann, arXiv:2610.20554v1, Theorem 2(1)/Lemma 17, establish a broad sufficient construction when both deleted-square root sets consist of multiples of a *single common* prime \(p\equiv1\pmod4\) and are disjoint across the two factors. Their proof recalls Jacobi's classical multiplicity formula. The present finite-hole theorem provides a necessary-and-sufficient classification for both placements of two deletions, and includes infinitely many coprime pairs whose roots have no common prime. It also detects the mixed obstruction \(P(u^2+v^2)=2\), invisible from checking each hole individually. The two results address different regimes: neither the current two-hole classification nor the cited common-prime theorem subsumes the other.

Elsholtz--Wurzinger, *Sumsets in the set of squares* (2024), concerns sumsets **contained in** the set of squares, rather than deletion of square summands that preserve the set of sums of two squares; the title alone is not taken as coverage. The classical Jacobi formula, used as an input here, predates both investigations.

## Limitations

The result only classifies two positive holes with distinct roots and the two stated allocations; it does not classify arbitrary finite or infinite deletion patterns. The proof uses classical two-square representation counts, so the arithmetic calculation is elementary. Mathematical originality is assessed against the inspected sources and searched records; implicit prior coverage remains possible. No independent audit has been performed.

## References

1. C. Elsholtz and J. Stadlmann, *The Large Sieve Inequality and Additive decompositions of sums of squares*, arXiv:2610.20554v1 (first publicly available 2026-10-14), particularly Theorem 2 and Section 4, https://arxiv.org/html/2610.20554v1.
2. C. Elsholtz and L. Wurzinger, *Sumsets in the set of squares*, Quarterly Journal of Mathematics 75 (2024), 1243--1254, DOI:10.1093/qmath/haae044; institutional abstract https://research-explorer.ista.ac.at/record/18930.
3. Classical Jacobi two-square representation theorem, cited in Reference 1, Section 4.1. Its multiplicative formula is explicitly used in the proof.
