# Density-zero gcd equality and divergence of the square-divisor gcd ratio

## Finding

For every positive integer \(m\), let \(\sigma(m)\) denote the sum of its positive divisors, and put
\[
R(m)=\frac{\gcd(m^2,\sigma(m^2))}{\gcd(m,\sigma(m^2))}.
\]
Then \(R(m)\) is a positive integer and, for every fixed real \(T\geq1\),
\[
\lim_{X\to\infty}\frac{1}{X}\#\{1\leq m\leq X:R(m)\leq T\}=0.
\]
In particular, the set
\[
\mathscr A=\{m\geq1:\gcd(m,\sigma(m^2))=\gcd(m^2,\sigma(m^2))\}
\]
has natural density zero. This establishes the assertion formulated as Conjecture 5.1 in Dris's *A new approach to odd perfect numbers via GCDs* [1]. The assertion concerns all positive integers, without assuming oddness, squarefreeness, or the existence of an odd perfect number.

## Assumptions and scope

The proof uses the classical existence of primitive cube roots in \((\mathbb Z/p\mathbb Z)^\times\), Hensel lifting of simple polynomial roots, the divergence of reciprocal primes in any fixed reduced residue class (a standard consequence of Dirichlet's theorem and its analytic proof), the Chinese remainder theorem, and multiplicativity of \(\sigma\). For a set \(S\) of positive integers, density means \(\lim_{X\to\infty}X^{-1}\#(S\cap[1,X])\), where real \(X\) is permitted.

A key intermediate assertion is: for each fixed prime \(p\equiv1\pmod3\) and fixed integer \(B\geq1\),
\[
\lim_{X\to\infty}\frac1X\#\{m\leq X:p^B\mid\sigma(m^2)\}=1.
\]
Both quantifiers are fixed before the limit; no assertion of uniformity in growing \(p\) or \(B\) is required.

## Proof

**1. Prime-power divisibility on a density-one set.** Fix a prime \(p\equiv1\pmod3\) and an integer \(B\geq1\). Necessarily \(p\geq7\). The cyclic group \((\mathbb Z/p\mathbb Z)^\times\) contains an element \(r\) of multiplicative order exactly \(3\). Thus \(r^2+r+1\equiv0\pmod p\), with \(r\not\equiv1\pmod p\). The derivative of \(f(U)=U^2+U+1\) at \(r\) is nonzero modulo \(p\): otherwise \(2r+1\equiv0\pmod p\) and \(4f(r)=(2r+1)^2+3\equiv3\pmod p\), an impossibility for \(p\geq7\).

Hensel's lemma therefore supplies a unit \(r_B\pmod{p^B}\) satisfying \(r_B^2+r_B+1\equiv0\pmod{p^B}\). By the divergence of the sum of reciprocal primes in a reduced arithmetic progression,
\[
\sum_{\substack{q\ \mathrm{prime}\\q\equiv r_B\ ({\rm mod}\ p^B)}}\frac1q=\infty.
\]
Let \(Q\) be an arbitrary finite set of these primes \(q\). For each \(q\), the condition \(q\parallel m\) means that \(q\mid m\) but \(q^2\nmid m\). Exactly \(q-1\) of the \(q^2\) residue classes modulo \(q^2\) have this property, so its density is \(1/q-1/q^2\). The conditions for distinct \(q\)'s involve pairwise coprime moduli. By the Chinese remainder theorem, the density of integers with none of the conditions \(q\parallel m\) for \(q\in Q\) is exactly
\[
\prod_{q\in Q}\left(1-\frac1q+\frac1{q^2}\right).
\]
Exhausting the primes in this progression makes the product tend to zero: its logarithm is at most \(-\sum_{q\in Q}(1/q-1/q^2)\), and that sum diverges. Hence the set of \(m\) for which there is **no** such \(q\parallel m\) has upper natural density zero. Whenever \(q\parallel m\), multiplicativity of the divisor sum gives the factor \(\sigma(q^2)=q^2+q+1\) in \(\sigma(m^2)\); the chosen congruence ensures \(p^B\mid q^2+q+1\). Therefore \(p^B\mid\sigma(m^2)\) on a density-one set, as asserted.

**2. Escape beyond every fixed bound.** Fix \(T\geq1\) and choose any finite set \(P\) of primes with \(p\equiv1\pmod3\) and \(p>T\). Apply Step 1 with \(B=2\) separately to each \(p\in P\). The intersection of these finitely many density-one sets is again density one; there, \(p^2\mid\sigma(m^2)\) for every \(p\in P\).

If such an \(m\) also satisfies \(p\parallel m\) for some \(p\in P\), then
\[
\nu_p\bigl(\gcd(m^2,\sigma(m^2))\bigr)=2,
\qquad
\nu_p\bigl(\gcd(m,\sigma(m^2))\bigr)=1,
\]
and thus \(p\mid R(m)\). Consequently \(R(m)\geq p>T\). It follows that, outside a set of density zero depending on finite \(P\), the condition \(R(m)\leq T\) forces \(p\nparallel m\) for every \(p\in P\).

Another direct application of the Chinese remainder theorem yields
\[
\overline d\{m:R(m)\leq T\}
\leq\prod_{p\in P}\left(1-\frac1p+\frac1{p^2}\right),
\]
where \(\overline d\) is upper natural density. Finally, let \(P\) exhaust all primes \(p\equiv1\pmod3\) with \(p>T\). Their reciprocal sum diverges, so the right-hand product tends to zero. The upper density is zero, and hence the natural density is zero. Since \(R(m)=1\) exactly when the two gcds coincide, the stated corollary follows. \(\square\)

## Verification

The accompanying standalone `verify.py` computes \(\sigma(m^2)\) by prime factorization and reproduces the source's equality counts through \(100000\); it also checks exact prime-power roots for four small primes, exact Chinese-remainder cylinder probabilities, and explicit prime-progression witnesses. Execute `python verify.py` using Python 3 standard libraries. Its actual output is recorded in `verification_output.txt`. These finite checks test identities and boundary cases; the two unrestricted density limits follow from the argument in the Proof section, not from the finite checks.

## Relationship to prior work

Dris [1, Section 5] established a strict upper bound below one for the density of the gcd-equality set and explicitly posed the zero-density statement as Conjecture 5.1. Meyerowitz's 2020 MathOverflow answer [2] supplied the central primitive-cube-root idea and wrote down the conjectural infinite product, explicitly leaving its probabilistic justification open. The present argument credits that idea, replaces the infinite-event heuristic by finite Chinese-remainder density calculations followed by two justified limits, and proves the stronger divergence-in-density statement for \(R(m)\). Pollack [3] analyzes a related but different random arithmetic quantity, \(\gcd(n,\sigma(n))\), and does not assert the present ratio theorem.

## Limitations

The theorem gives no quantitative rate of decay for \(\#\{m\leq X:R(m)\leq T\}/X\), and makes no claim that \(R(m)\) tends to infinity along every sequence of integers. In particular, prime powers provide infinitely many exceptional integers. The density-one prime-power divisibility lemma fixes \(p\) and \(B\) before passing to the limit. The proof makes no assertion about whether odd perfect numbers exist. Novelty comparison cannot rule out an unindexed equivalent prior argument.

## References

[1] J. A. B. Dris, *A new approach to odd perfect numbers via GCDs*, arXiv:2202.08116v1, publicly posted 10 February 2022, Section 5, especially Conjecture 5.1 and Remark 5.1. https://arxiv.org/html/2202.08116v1

[2] A. Meyerowitz, answer (18 August 2020) to *Is the asymptotic density of positive integers \(n\) satisfying \(\gcd(n,\sigma(n^2))=\gcd(n^2,\sigma(n^2))\) equal to zero?*, MathOverflow question 369441, answer 369521. https://mathoverflow.net/questions/369441/

[3] P. Pollack, *On the greatest common divisor of a number and its sum of divisors, II*, available author manuscript, especially introduction and theorems on \(\gcd(n,\sigma(n))\). https://www.pollack-math.net/gcdnsigmasequel.pdf
