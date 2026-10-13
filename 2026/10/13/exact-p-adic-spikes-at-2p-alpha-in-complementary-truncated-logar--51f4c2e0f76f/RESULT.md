# Exact \(p\)-adic spikes at \(2p^\alpha\) in complementary truncated logarithms

## Finding
Let \(p\) be an odd prime, let \(a\in\mathbb Z\) satisfy \(p\nmid a\), and put
\[
S_n(p,a)=\sum_{k=1}^{n}\frac{p^k}{k}\left(\frac1{a^k}+\frac1{(p-a)^k}\right).
\]
For **every** integer \(\alpha\ge1\), the exact valuation at the index immediately after an extremal index in Farhi's bound is
\[
\boxed{\nu_p\bigl(S_{2p^\alpha}(p,a)\bigr)=2p^\alpha+\alpha+2.}
\]
The formula is independent of the unit \(a\). Moreover Farhi's theorem gives \(\nu_p(S_{2p^\alpha-1}(p,a))=2p^\alpha-\alpha\); consequently the adjacent valuations jump by exactly \(2\alpha+2\).

## Assumptions and scope
The valuation \(\nu_p(u/v)\) on nonzero rational numbers is the exponent of \(p\) in the numerator minus that in the denominator. Both \(a\) and \(p-a\) are nonzero and prime to \(p\). The claim ranges over all odd primes, all such integers \(a\) (including negative ones), and all positive exponents \(\alpha\); it makes no claim for \(p=2\) or general indices.

## Proof
Fix \(p,a,\alpha\), set \(N=2p^\alpha\) and \(x=p/a\), so that \(\nu_p(x)=1\). The second argument in the truncated logarithm is \(y=p/(p-a)=-x/(1-x)\). Consider the rational function
\[
F_N(X)=\sum_{k=1}^{N}\frac{X^k+(-X/(1-X))^k}{k}.
\]
As \(N\) is even, direct differentiation, with \(Y=-X/(1-X)\), yields
\[
F_N'(X)=\frac{Y^N-X^N}{1-X}
=X^N\bigl((1-X)^{-N-1}-(1-X)^{-1}\bigr).
\]
Since \(F_N(0)=0\), the binomial theorem and termwise formal integration give the exact identity of formal power series over \(\mathbb Q\):
\[
F_N(X)=\sum_{j\ge1}
\frac{\binom{N+j}{j}-1}{N+j+1}X^{N+j+1}.
\tag{1}
\]
The series converges at \(X=x\) in \(\mathbb Q_p\) (each coefficient has at most logarithmic denominator valuation), and \(F_N(x)=S_N(p,a)\).

For \(j=1\), the summand of (1) is \(NX^{N+2}/(N+2)\). Because \(p\) is odd, \(p\nmid N+2\), hence its valuation at \(x\) is exactly \(N+\alpha+2\). For \(j=2\), the coefficient simplifies exactly to \(N/2\), so its summand has valuation \(N+\alpha+3\).

It remains to prove that **each** term indexed by \(j\ge3\) has valuation at least \(N+\alpha+3\). The telescoping binomial identity
\[
\binom{N+j}{j}-1
=N\sum_{h=1}^j\frac1h\binom{N+h-1}{h-1}
\tag{2}
\]
shows, by integrality of binomial coefficients and the ultrametric inequality, that
\[
\nu_p\left(\binom{N+j}{j}-1\right)
\ge\alpha-\lfloor\log_p j\rfloor.
\]
Thus the valuation of the \(j\)-th term in (1) is at least
\[
N+j+1+\alpha-\lfloor\log_p j\rfloor-\nu_p(N+j+1).
\tag{3}
\]
For \(j=3\), \(p\nmid N+4\). Also \(\lfloor\log_p3\rfloor\le1\), so (3) is at least \(N+\alpha+3\). For \(j=4\), \(\lfloor\log_p4\rfloor\le1\) and \(\nu_p(N+5)\le1\): this follows by reduction modulo \(p\), with the only possible divisor \(p=5\), when \(\nu_5(N+5)=1\). Consequently (3) is at least \(N+\alpha+3\) as well.

For all \(j\ge5\), if \(j+1<p^\alpha\), then \(\nu_p(N+j+1)=\nu_p(j+1)\); otherwise \(N+j+1\le3(j+1)\). Either way,
\[
\nu_p(N+j+1)\le\lfloor\log_3(3(j+1))\rfloor.
\]
Also \(\lfloor\log_p j\rfloor\le\lfloor\log_3 j\rfloor\). For \(j=5,6,7\), direct integer bounds show
\[
\lfloor\log_3 j\rfloor+\lfloor\log_3(3(j+1))\rfloor\le j-2.
\]
For every \(j\ge8\), the inequality \(3j(j+1)\le3^{j-2}\) holds (at \(j=8\), and thereafter by induction, since multiplication by \(3\) dominates the successive quadratic factor); it implies the same logarithmic bound. Substitution into (3) proves valuation at least \(N+\alpha+3\) for every \(j\ge5\).

Exactly the \(j=1\) term has valuation \(N+\alpha+2\), and the entire remaining convergent sum has valuation at least \(N+\alpha+3\). The ultrametric inequality with unequal valuations therefore gives
\(\nu_p(F_N(x))=N+\alpha+2\), as asserted. The adjacent-index comparison uses Farhi's published extremal-index formula; it is not needed to establish the new valuation identity itself. \(\square\)

## Verification
The accompanying standalone Python verifier uses `fractions.Fraction` and integer binomial coefficients, not floating-point approximations. It verifies 68 exact rational valuation cases, including \(\alpha=4\) for \(p=3\), six signed unit choices where applicable, and 120 finite coefficient identities. Run `python3 verify.py` from this directory. These checks are regression tests; the proof above establishes the unrestricted statement.

## Relationship to prior work
Farhi's Theorem 1 (initially publicly posted on 2022-12-01) gives for all \(n\ge1\)
\[
\nu_p(S_n(p,a))\ge (n+1)-\log_p\!\left(\frac{n+1}{2}\right),
\]
with equality exactly when \(n=2p^\alpha-1\) for \(\alpha\ge0\). Theorem 2 addresses general lower bounds and Theorem 3 unboundedness; the paper's remaining arguments establish the bound through recurrence and a logarithmic identity. None of the checked statements supplies the exact valuation at the **next** index \(2p^\alpha\). The formal derivative expansion (1) isolates its first nonzero \(p\)-adic term; this is a stronger index-specific conclusion rather than a restatement of the global lower bound. An unindexed or differently formulated exact evaluation remains possible.

## Limitations
The result applies to odd primes and the specified prime-power-adjacent indices only. It neither classifies valuations at all indices nor addresses arbitrary combinations of paired logarithmic arguments. The searches and primary-text comparison support, but cannot certify, bibliographic novelty; independent mathematical validation has not been performed.

## References
1. Bakir Farhi, *Nontrivial lower bounds for the p-adic valuations of some type of rational numbers*, arXiv:2212.00446v1 (2022-12-01), https://arxiv.org/abs/2212.00446 .
2. Bakir Farhi, *Nontrivial Lower Bounds for the p-adic Valuation of Certain Rational Numbers*, Journal of Integer Sequences 26 (2023), Article 23.6.1, https://cs.uwaterloo.ca/journals/JIS/VOL26/Farhi2/farhi42.pdf .
