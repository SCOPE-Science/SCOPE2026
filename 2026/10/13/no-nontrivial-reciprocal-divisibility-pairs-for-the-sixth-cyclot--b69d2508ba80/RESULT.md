# No nontrivial reciprocal divisibility pairs for the sixth cyclotomic polynomial

## Finding

Define the sixth cyclotomic polynomial by \(F(t)=\Phi_6(t)=t^2-t+1\). The following pair system has exactly one solution among positive integers:

\[
 a\mid F(b),\qquad b\mid F(a)
 \quad\Longleftrightarrow\quad a=b=1.
\]

In particular, the directed divisibility graph with vertices \(2,3,4,\ldots\) and an arrow \(u\to v\) exactly when \(v\mid F(u)\) has no loops and no directed two-cycles. For the arithmetic function

\[
 \mathcal H(n)=\sum_{i=1}^{n}\frac{1}{\gcd(i,n)},
\]

no squarefree integer \(n>1\) with fewer than three distinct prime factors has integral \(\mathcal H(n)\). This eliminates the squarefree two-prime cycle case in the dependency-graph approach to the integral values of \(\mathcal H\).

## Assumptions and scope

All divisibilities are in ordinary positive integers. The pair statement includes the boundary \(a=1\) or \(b=1\), and includes equal operands. The graph only involves integer vertices larger than one. The arithmetic consequence concerns *squarefree* integers only; prime powers and mixed prime-power products with exponent larger than one are not classified.

## Proof

**Step 1: remove diagonal and unit boundaries.** We have \(F(t)\equiv1\pmod t\) for every positive integer \(t\). Hence \(t\mid F(t)\) implies \(t=1\). If \(a=1<b\), then \(b\mid F(1)=1\) is false; similarly for \(b=1<a\). The pair \((1,1)\) satisfies both divisibilities.

**Step 2: exact descending transformation.** Suppose a nontrivial positive solution exists, and choose one minimizing \(\max(a,b)\). By symmetry and Step 1 we may assume \(2\le a<b\). Define

\[
 c=\frac{F(a)}{b}.
\]

This is a positive integer by \(b\mid F(a)\). Since \(b\ge a+1\) and \(F(a)=a^2-a+1<a(a+1)\), we have \(1\le c<a\). We already know \(c\mid F(a)\), and the relation \(bc=F(a)\equiv1\pmod a\) gives

\[
 c^2 F(b)=(bc)^2-c(bc)+c^2
 \equiv1-c+c^2=F(c)\pmod a.
\]

Since \(a\mid F(b)\), the left side is zero modulo \(a\). Therefore \(a\mid F(c)\). Both divisibilities hold for the new pair \((c,a)\), whose maximum is \(a<b\), contradicting minimality. This proves that \((1,1)\) is the only positive pair. The reduction makes no primality or coprimality assumption.

**Step 3: directed-graph consequence.** A loop at \(u>1\) would require \(u\mid F(u)\), ruled out by Step 1. A directed two-cycle between distinct \(u,v>1\) is exactly the forbidden reciprocal divisibility system. Thus such loops and two-cycles do not exist.

**Step 4: arithmetic consequence.** Group the terms of \(\mathcal H(n)\) by their gcd with \(n\). Using Euler's totient \(\varphi\),

\[
 \mathcal H(n)=\frac1n\sum_{d\mid n}d\varphi(d)
 =\frac1n\prod_{p^{\alpha}\parallel n}\frac{p^{2\alpha+1}+1}{p+1}.
\]

In particular, for distinct primes \(p,q\),

\[
 \mathcal H(pq)=\frac{F(p)F(q)}{pq}.
\]

Because \(p\) and \(q\) are distinct primes and \(F(p)\equiv1\pmod p\), \(F(q)\equiv1\pmod q\), the value \(\mathcal H(pq)\) is integral if and only if \(p\mid F(q)\) and \(q\mid F(p)\). The pair theorem excludes this. For a single prime \(p\), \(\mathcal H(p)=F(p)/p\) is nonintegral because \(F(p)\equiv1\pmod p\). Thus squarefree integral inputs larger than one must have at least three distinct prime factors. The argument does not show whether three factors suffice.

## Verification

The supplied standalone `verify.py` can be run with `python3 verify.py` (Python standard library only). It enumerates all possible larger factors \(b>a\) of \(F(a)\) for \(2\le a\le5000\), checks the descending congruence and absence of reciprocal solutions for each, directly tests the \(200\times200\) positive grid, and independently checks the gcd-sum/product identity at six specified inputs, including \(614341=7\cdot13\cdot43\cdot157\). The expected summary is in `verification_output.txt`. These computations are finite sanity checks. The universal claim depends on the complete descent proof above, not on enumeration.

## Relationship to prior work

De Koninck and Letendre (arXiv:2610.10572v1, submitted 4 October 2026, MSC2020 11N37) study integral values of \(\mathcal H(n)\). Their Section 5, Proposition 1, considers the exact simultaneous divisibility system for two *distinct odd primes* and derives an upper bound on its number of solutions. The present theorem treats the same two reciprocal divisibilities without primality restrictions and proves that the solution set is empty above one; an upper bound alone does not imply emptiness. Their other graph cases with squared prime factors are not eliminated.

OEIS A317480 lists the integral-value sequence and the same multiplicative arithmetic function. Its list and implementation supply independent context for the arithmetic object, but a finite table cannot exclude all semiprimes. Searches for the reciprocal-divisibility statement and its graph, polynomial, and gcd-sum formulations did not identify a covering theorem. A negative search does not prove novelty.

## Limitations

The theorem does not classify integral values of \(\mathcal H(n)\) at arbitrary prime-power support, does not rule out all directed cycles of length three or more, and does not assert a sharp least possible prime support for nontrivial squarefree integral inputs. It does not improve the global asymptotic bound for the counting function from the cited preprint. Potential independent earlier formulations not found in consulted searchable sources remain a literature risk.

## References

1. J.-M. De Koninck and P. Letendre, *The Integer Values of \(\sum_{i=1}^{n}1/\gcd(n,i)\)*, arXiv:2610.10572v1 (4 October 2026), especially Sections 1, 2, 5 (Proposition 1), and 7; https://arxiv.org/html/2610.10572v1 .
2. OEIS A317480, *Numbers m such that Sum_{k=1..m} 1/gcd(k,m) is an integer*, https://oeis.org/A317480 .
