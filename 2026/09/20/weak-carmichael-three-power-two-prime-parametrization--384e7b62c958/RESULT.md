# A finite divisor parametrization for weak Carmichael numbers \(3^a p q\)

## Statement

A weak Carmichael number is an odd composite integer \(n\) such that \(r-1\mid n-1\) for every prime divisor \(r\mid n\). Fix \(a\ge 1\), put
\[
A=3^a,
\]
and consider
\[
n=A p q,\qquad 3<p<q,
\]
with \(p,q\) prime.

### Theorem 1 — exact finite parametrization

The weak Carmichael numbers \(A p q\) are in bijection with pairs of positive integers \((k,d)\) satisfying
\[
1\le k\le A-1,\qquad d>2,
\]
\[
d\mid (A-1)(A+k),
\]
\[
k\mid Ad+A-1,
\]
and
\[
k\mid A^2+\frac{(A-1)(A+k)}{d},
\]
for which
\[
p=d+1,\qquad
q=1+\frac{Ad+A-1}{k}
\]
are primes with \(3<p<q\).

For every such number,
\[
p\le 2A^2-3A+2,\qquad
q\le 2A^3-3A^2+2A.
\]
Consequently, for every fixed exponent \(a\), the complete classification of weak Carmichael numbers of the form \(3^a p q\) is a finite divisor computation.

Moreover every such pair satisfies
\[
p\equiv q\equiv 2\pmod 3.
\]

### Corollary 2 — complete \(9pq\) classification

The only weak Carmichael numbers of the form
\[
9pq,\qquad 3<p<q
\]
are
\[
\boxed{13833=3^2\cdot29\cdot53}
\]
and
\[
\boxed{321201=3^2\cdot89\cdot401}.
\]

Thus the two examples already present in the classical tables are not merely the examples below a numerical cutoff: they are the complete global list for the \(9pq\) slice.

### Corollary 3 — periodic lifting in the exponent

Fix primes \(3<p<q\). If \(3^{a_0}pq\) is weak Carmichael, then all exponents producing a weak Carmichael number are exactly
\[
a\equiv a_0\pmod L,
\]
where
\[
L=\operatorname{lcm}\!\left(
\operatorname{ord}_{p-1}(3),
\operatorname{ord}_{q-1}(3)
\right).
\]
In particular,
\[
3^{\,2+6t}\cdot29\cdot53
\quad\text{and}\quad
3^{\,2+20t}\cdot89\cdot401
\]
are weak Carmichael numbers for every integer \(t\ge0\).

## Proof of Theorem 1

The Korselt-type criterion for weak Carmichael numbers says that \(Apq\) is weak Carmichael exactly when
\[
p-1\mid Apq-1,\qquad q-1\mid Apq-1;
\]
the condition from the prime \(3\) is automatic because \(2\mid Apq-1\).

Reducing the two divisibilities modulo \(p-1\) and \(q-1\) gives
\[
p-1\mid Aq-1,\qquad q-1\mid Ap-1. \tag{1}
\]

Set
\[
d=p-1,\qquad
k=\frac{Ap-1}{q-1}.
\]
The second relation in (1) makes \(k\) a positive integer. Since \(q>p\),
\[
q-1>p,
\]
and hence
\[
1\le k=\frac{Ap-1}{q-1}<A.
\]
Thus \(1\le k\le A-1\).

Because \(p=d+1\),
\[
q-1=\frac{A(d+1)-1}{k}
=\frac{Ad+A-1}{k},
\]
so
\[
k\mid Ad+A-1. \tag{2}
\]

Now write
\[
C_k=(A-1)(A+k).
\]
Using the expression for \(q\),
\[
Aq-1
=\frac{A^2d+C_k}{k}. \tag{3}
\]
Condition \(d\mid Aq-1\) is therefore equivalent to
\[
kd\mid A^2d+C_k.
\]
This in turn is equivalent to the pair
\[
d\mid C_k,\qquad
k\mid A^2+\frac{C_k}{d}. \tag{4}
\]
Equations (2) and (4) are precisely the stated divisor conditions. Conversely, if those conditions hold and the resulting \(p=d+1\) and \(q=1+(Ad+A-1)/k\) are primes with \(3<p<q\), equations (2)–(4) reverse to give both divisibilities in (1), and hence \(Apq\) is weak Carmichael. The parameters are unique because necessarily
\[
d=p-1,\qquad k=\frac{Ap-1}{q-1}.
\]

Since \(d\mid C_k\),
\[
d\le C_k\le (A-1)(2A-1)=2A^2-3A+1,
\]
which yields
\[
p\le2A^2-3A+2.
\]
Also
\[
q-1=\frac{Ap-1}{k}\le Ap-1,
\]
hence
\[
q\le Ap\le2A^3-3A^2+2A.
\]

Finally, if \(p\equiv1\pmod3\), then \(3\mid p-1\), while
\[
Aq-1\equiv-1\pmod3,
\]
contradicting \(p-1\mid Aq-1\). Thus \(p\equiv2\pmod3\); the same argument gives \(q\equiv2\pmod3\).

## Proof of Corollary 2

Here \(A=9\), so \(k\in\{1,\dots,8\}\) and
\[
C_k=8(9+k).
\]
Applying the three exact divisor conditions of Theorem 1 leaves only the following structural candidates before primality is imposed:

| \(k\) | admissible \(d\) | resulting \((p,q)\) |
|---:|---:|---:|
| 1 | 4 | (5,45) |
| 1 | 5 | (6,54) |
| 1 | 8 | (9,81) |
| 1 | 10 | (11,99) |
| 1 | 16 | (17,153) |
| 1 | 20 | (21,189) |
| 1 | 40 | (41,369) |
| 1 | 80 | (81,729) |
| 2 | 8 | (9,41) |
| 2 | 88 | **(89,401)** |
| 5 | 8 | (9,17) |
| 5 | 28 | **(29,53)** |

Only the two bold pairs consist of primes, proving the classification.

## Proof of Corollary 3

For fixed \(p,q\), the weak Carmichael conditions are
\[
3^a q\equiv1\pmod{p-1},\qquad
3^a p\equiv1\pmod{q-1}. \tag{5}
\]
Any solution forces \(p,q\equiv2\pmod3\), so \(3\) is invertible modulo both \(p-1\) and \(q-1\). Also \(q\) is automatically invertible modulo \(p-1\), and the second congruence in (5) forces \(p\) to be invertible modulo \(q-1\). If \(a_0\) is one solution, the first congruence holds exactly for
\[
a\equiv a_0\pmod{\operatorname{ord}_{p-1}(3)},
\]
and the second exactly for
\[
a\equiv a_0\pmod{\operatorname{ord}_{q-1}(3)}.
\]
Their intersection is the single residue class modulo the stated least common multiple.

For \((p,q)=(29,53)\), both orders are \(6\). For \((p,q)=(89,401)\), the orders are \(10\) and \(20\), respectively.

## Verification

The accompanying exact-integer script independently implements the divisor parametrization and a direct search based only on the weak Carmichael divisibility criterion. The two methods agree for \(1\le a\le5\). The parametrization was additionally evaluated for \(a=6\). It reproduces the twelve structural candidates used in the hand-checkable \(a=2\) proof.

The computed solution pairs are:
\[
\begin{array}{c|l}
a & (p,q)\\ \hline
1&(11,17)\\
2&(29,53),(89,401)\\
3&(53,131),(59,797),(131,443)\\
4&(47,347),(7841,37361)\\
5&(11,17),(17,827),(41,587),(71,8627),(60017,2916827)\\
6&(29,4229),(137,49937),(3329,6761),(41777,1791497).
\end{array}
\]
These finite checks support the implementation and the small-\(a\) consequences; the general theorem is proved algebraically above.

## Relation to prior literature

Borwein and Wong's work on Giuga-type congruences supplies the divisibility characterization later used as the weak Carmichael Korselt criterion. Meštrović's 2013 paper introduced and developed the weak Carmichael terminology and explicitly singled out the family
\[
3^2p_2\cdots p_s.
\]
Remark 2.77 lists both
\[
13833=3^2\cdot29\cdot53,\qquad
321201=3^2\cdot89\cdot401,
\]
but the same remark then displays a computation asserting that the \(9pq\) intersection with \(3<p<q<10^5\) is empty. Those statements are mutually inconsistent. The theorem above resolves that discrepancy without a cutoff: exactly those two \(9pq\) numbers exist.

A 2026 manuscript by Meštrović retains both numbers in its tables and develops further weak Carmichael results, including two-distinct-prime exponent families. A text search of that manuscript did not locate the finite \(3^apq\) parametrization above or a global \(9pq\) classification. OEIS A225498 and A087442 likewise list weak Carmichael numbers but do not supply this classification.

To the best of our knowledge, the exact finite parametrization, the global \(9pq\) classification, and the fixed-\((p,q)\) exponent-period statement above have not previously been recorded in this form.

## Limitations

The theorem treats the three-distinct-prime support \(3^apq\) with the exponents of \(p\) and \(q\) equal to one. It does not classify \(3^ap^bq^c\) for \(b>1\) or \(c>1\), nor weak Carmichael numbers with four or more distinct prime factors.

The originality conclusion is necessarily literature-limited. Wong's 1997 thesis *Computations on Normal Families of Primes* uses the earlier term "pseudo-Carmichael" and contains general normal-family constructions and a converse characterization; an indexed excerpt was inspected, but the full thesis text was not directly available through the checked source. Equivalent specializations under that older terminology therefore remain the main residual originality risk.

## References

1. J. M. Borwein and E. Wong, *A survey of results relating to Giuga's conjecture on primality*, CRM Proceedings & Lecture Notes 11 (1997), 13–27, DOI: 10.1090/crmp/011/02.
2. R. Meštrović, *Generalizations of Carmichael numbers I*, arXiv:1305.1867 (2013).
3. R. Meštrović, *Weak Carmichael Numbers*, manuscript (2026), ResearchGate publication 403923179.
4. OEIS A225498, *Weak Carmichael numbers*.
5. OEIS A087442, *Weak Carmichael numbers that are not prime powers*.
6. E. Wong, *Computations on Normal Families of Primes*, M.Sc. thesis, Simon Fraser University (1997).
