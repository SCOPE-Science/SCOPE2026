# Wall--Sun--Sun exceptional branch in Fibonacci-totient residue classes

## Statement

Let \(F_n\) be the Fibonacci sequence, let \(z(N)\) denote the rank of apparition of \(N\), and let \(\pi(q)\) be the Pisano period modulo an odd prime \(q\ne5\). Following Goel, define
\[
S(q)=\{r\bmod \pi(q): q\mid \varphi(F_m)\text{ for every positive }m\equiv r\pmod{\pi(q)}\}.
\]
Write \(P=\pi(q)\) and \(z=z(q)\). For a residue class \(r\bmod P\), consider the positive integers \(m\equiv r\pmod P\) for which \(q^2\mid F_m\).

**Theorem (exact square-witness density).** The relative density of those integers inside the progression \(m\equiv r\pmod P\) exists and equals
\[
\delta_q(r)=
\begin{cases}
1, & q\text{ is a Wall--Sun--Sun prime and }z\mid r,\\
0, & q\text{ is a Wall--Sun--Sun prime and }z\nmid r,\\
1/q, & q\text{ is not a Wall--Sun--Sun prime and }z\mid r,\\
0, & q\text{ is not a Wall--Sun--Sun prime and }z\nmid r.
\end{cases}
\]
Here a Wall--Sun--Sun prime is equivalently an odd prime for which \(z(q^2)=z(q)\); otherwise the standard rank-lifting relation gives \(z(q^2)=qz(q)\).

Consequently, if \(q\) is Wall--Sun--Sun, then
\[
\boxed{\{r\bmod P:z(q)\mid r\}\subseteq S(q)}
\]
and therefore
\[
\boxed{|S(q)|\ge \frac{\pi(q)}{z(q)}}.
\]
Thus every Wall--Sun--Sun prime would make \(S(q)\) nonempty by a mechanism that does not require a prime \(p\equiv1\pmod q\) dividing all Fibonacci numbers in the progression.

There is also an unconditional repair of the external-witness step. If \(r\in S(q)\) and either \(q\) is not Wall--Sun--Sun or \(z(q)\nmid r\), then infinitely many positive \(m\equiv r\pmod P\) have \(q^2\nmid F_m\). For every such \(m\), some prime divisor \(p\ne q\) of \(F_m\) satisfies
\[
p\equiv1\pmod q.
\]
More precisely, the relative density of progression terms on which such an external witness is forced is at least \(1-1/q\) when \(q\) is non-Wall--Sun--Sun and \(z(q)\mid r\), and is \(1\) when \(z(q)\nmid r\). In the Wall--Sun--Sun case with \(z(q)\mid r\), the condition \(q^2\mid F_m\) itself holds throughout the progression, so divisibility by \(q\) of \(\varphi(F_m)\) alone does not force an external prime witness.

## Proof

For every positive integer \(N\), the defining property of the rank of apparition gives
\[
N\mid F_m\quad\Longleftrightarrow\quad z(N)\mid m.
\]
Set \(d=z(q^2)\). Hence \(q^2\mid F_m\) is exactly the condition \(d\mid m\).

If \(q\) is Wall--Sun--Sun, then \(d=z\). Since \(z\mid P\), every member of the progression \(m\equiv r\pmod P\) is divisible by \(z\) exactly when \(z\mid r\). This gives density \(1\) or \(0\) as stated.

Suppose instead that \(q\) is not Wall--Sun--Sun. Then \(d=qz\). Wall's period divisibility gives \(P\mid q^2-1\) for \(q\ne5\), hence \(q\nmid P\). Since \(z\mid P\),
\[
\gcd(d,P)=\gcd(qz,P)=z.
\]
The simultaneous congruences
\[
m\equiv r\pmod P,\qquad m\equiv0\pmod{qz}
\]
therefore have a solution exactly when \(z\mid r\). When solvable, their intersection is one residue class modulo
\[
\operatorname{lcm}(P,qz)=qP,
\]
so exactly one out of every \(q\) members of the progression has \(q^2\mid F_m\). This proves the density formula.

If \(q\) is Wall--Sun--Sun and \(z\mid r\), the first part gives \(q^2\mid F_m\) for every positive \(m\equiv r\pmod P\). Since \(q^2\mid N\) implies \(q\mid\varphi(N)\), the displayed block of residue classes lies in \(S(q)\). There are exactly \(P/z\) such classes.

Finally take \(r\in S(q)\) outside that persistent Wall--Sun--Sun branch. The density formula supplies infinitely many progression terms with \(q^2\nmid F_m\). Factor
\[
F_m=\prod_i p_i^{a_i}.
\]
Because \(r\in S(q)\), we have \(q\mid\varphi(F_m)=\prod_i p_i^{a_i-1}(p_i-1)\). On a term for which \(q^2\nmid F_m\), the factor \(q\) cannot arise from \(p_i^{a_i-1}\) with \(p_i=q\). Therefore it must divide \(p_i-1\) for some prime divisor \(p_i\ne q\), giving \(p_i\equiv1\pmod q\). The density lower bounds follow by subtracting the square-witness densities from \(1\). ∎

## Relation to the recent literature

Goel's 2026 preprint introduces \(S(q)\) and, in Lemma 4.3, seeks to show that every \(r\in S(q)\) has infinitely many terms whose totient divisibility is witnessed by a prime \(p\ne q\) with \(p\equiv1\pmod q\). The proof excludes the alternative \(q^2\mid F_m\) throughout a progression by saying that \(q\) is not Wall--Sun--Sun because no such prime has been found in finite searches. Finite non-detection does not establish this for an arbitrary prime \(q\). The theorem above isolates the missing exceptional branch exactly.

The same proof also states that, after excluding persistent square divisibility, \(q^2\mid F_m\) can occur only finitely often along the progression. The exact density formula shows that this stronger assertion is false even for ordinary non-Wall--Sun--Sun primes whenever \(z(q)\mid r\): the square divisibility recurs with relative density \(1/q\).

A concrete example is \(q=3\). Here
\[
z(3)=4,\qquad \pi(3)=8,\qquad z(9)=12.
\]
The class \(r=0\pmod8\) belongs to \(S(3)\), since \(7\mid F_m\) for every \(8\mid m\) and \(7\equiv1\pmod3\). But \(9\mid F_m\) precisely when \(12\mid m\), so among \(m=8,16,24,32,\ldots\) it occurs at \(24,48,72,\ldots\): exactly every third term, not finitely often.

This note does **not** exhibit a Wall--Sun--Sun prime, does not disprove Goel's Conjecture 4.4, and does not invalidate the paper's independent sufficient criterion based on a fixed prime \(p\equiv1\pmod q\). It identifies the exact square-power mechanism that a universal converse argument must retain. If Conjecture 4.4 is true as stated, then every hypothetical Wall--Sun--Sun prime would in addition have to admit a fixed prime \(p\equiv1\pmod q\) with \(z(p)\mid\pi(q)\), even though \(S(q)\ne\varnothing\) already follows from the square-power branch.

## Verification

`artifacts/verify.py` uses exact modular Fibonacci recurrences. For every odd prime \(q\le200\), \(q\ne5\), it computes \(z(q)\), \(\pi(q)\), and \(z(q^2)\), checks the non-Wall--Sun--Sun rank lift and \(\gcd(z(q^2),\pi(q))=z(q)\), and verifies the recurring \(q=3\) pattern. This finite computation is a sanity check only; the proof above is general.

## References

1. A. Goel, *Sophie Germain Primes and the Totient of Fibonacci Numbers*, arXiv:2604.17847v3 (2026). https://arxiv.org/abs/2604.17847
2. D. D. Wall, *Fibonacci Series Modulo m*, American Mathematical Monthly 67 (1960), 525--532. https://doi.org/10.1080/00029890.1960.11989541
3. R. J. McIntosh and E. L. Roettger, *A search for Fibonacci-Wieferich and Wolstenholme primes*, Mathematics of Computation 76 (2007), 2087--2094. https://doi.org/10.1090/S0025-5718-07-01955-2
