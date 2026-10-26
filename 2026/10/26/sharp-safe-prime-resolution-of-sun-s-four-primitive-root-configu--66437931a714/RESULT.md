# Sharp safe-prime resolution of Sun's four-primitive-root configuration

## Finding
For a safe prime \(p=2q+1\) (where \(q\) is prime), a **four-primitive-root witness** is a pair of distinct positive integers \(a,b\) such that \(a+b<p\) and all four integers \(a\), \(b\), \(a+b\), and \(ab(a+b)\) are primitive roots modulo \(p\).

**Theorem.** Every safe prime \(p\ge11\) has a four-primitive-root witness; the two smaller safe primes \(5\) and \(7\) do not. More precisely:

1. If \(p\equiv7\pmod8\), one may take
   \[a=\frac{p-1}{2},\qquad b=\frac{p-3}{2}.\]
2. If \(p\equiv3\pmod8\), the number of witnesses with \(a=2\), counted by the distinct values of \(b\), is exactly
   \[\boxed{\frac{p-7}{4}}.\]
   They are precisely the \(b\in\{1,\ldots,p-3\}\setminus\{2,p-3\}\) with \(\chi(b)=\chi(b+2)=-1\), where \(\chi\) denotes the Legendre symbol modulo \(p\). The restriction \(b<p-2\) ensures \(2+b<p\).

This establishes the complete safe-prime case of the existence property proposed in Sun's Conjecture 4.2(i), including both exceptional smaller safe primes, and strengthens it with explicit witnesses and an exact fixed-first-entry count.

## Assumptions and scope
The hypotheses are that \(p\) and \(q=(p-1)/2\) are rational primes. All assertions are uniform over such \(p\); no infinitude of safe primes is assumed. A primitive root means an element of multiplicative order \(p-1\) in \(\mathbb F_p^\times\). All inequalities involving \(a,b\) are for their stated ordinary integer representatives, not merely residues. In the counting claim, ordered pairs with first coordinate \(2\) are counted once per distinct second coordinate.

For \(p\ge11\), the prime \(q\ge5\) is odd. The congruence \(q\equiv1\pmod3\) would force \(3\mid p=2q+1\), impossible for \(p>3\). Hence \(q\equiv5\pmod6\) and
\[p\equiv11\pmod{12},\quad \chi(-1)=-1,\quad \chi(3)=1.\]
Since \(\mathbb F_p^\times\) is cyclic of order \(2q\), its quadratic nonresidues have order \(2\) or \(2q\). The only nonresidue of order \(2\) is \(-1\). Therefore
\[x\text{ is primitive}\iff \chi(x)=-1\text{ and }x\not\equiv-1\pmod p.\tag{1}\]

## Proof
**Case \(p\equiv7\pmod8\).** Here \(\chi(2)=1\). Set \(a=(p-1)/2\), \(b=(p-3)/2\), and \(c=a+b=p-2\). Their residue classes are \(-1/2\), \(-3/2\), and \(-2\), respectively. Quadratic-character multiplicativity, \(\chi(-1)=-1\), \(\chi(2)=1\), and \(\chi(3)=1\) give
\[\chi(a)=\chi(b)=\chi(c)=-1.\]
None is congruent to \(-1\) modulo \(p\): each hypothetical equality simplifies to \(1\equiv0\pmod p\). Thus all three are primitive by (1). Moreover \(ac\equiv(-1/2)(-2)=1\pmod p\), whence \(abc\equiv b\pmod p\), also primitive. The integers \(a,b\) are positive and distinct, and \(a+b=p-2<p\).

**Case \(p\equiv3\pmod8\).** Here \(\chi(2)=-1\), so \(2\) is primitive by (1). Also \(\chi(-2)=1\). For a residue \(x\), the Legendre symbols obey \(\chi(0)=0\). The classical quadratic-character sum
\[\sum_{x\in\mathbb F_p}\chi(x(x+2))=-1\tag{2}\]
has an elementary proof: the number of pairs \((x,y)\) with \(y^2=x(x+2)\) is \(p+\sum_x\chi(x(x+2))\). Rewriting this equation as \((x+1-y)(x+1+y)=1\), every nonzero first factor determines exactly one second factor and one pair \((x,y)\) because \(2\) is invertible. The number of pairs is \(p-1\), proving (2).

Exclude the two roots \(x=0,-2\). On the remaining \(p-2\) classes we have
\[\sum\chi(x)=-\chi(-2)=-1,\quad
\sum\chi(x+2)=-\chi(2)=1,\quad
\sum\chi(x)\chi(x+2)=-1.\]
Expanding \((1-\chi(x))(1-\chi(x+2))/4\), which is the indicator of two quadratic nonresidues on this restricted set, gives the exact count
\[\#\{x:\chi(x)=\chi(x+2)=-1\}=\frac{p-2-(-1)-1-1}{4}=\frac{p-3}{4}.\tag{3}\]
Among these classes, \(x=p-3\equiv-3\) is always included, since \(\chi(-3)=-1\) and \(\chi(-1)=-1\). It is forbidden because \(x+2=p-1\equiv-1\) is not primitive and \(2+x=p-1\) is at the boundary. No other class satisfying both character conditions is excluded by the integer constraints: \(x=0,p-2\) have a zero character; \(x=p-1\) gives \(\chi(x+2)=\chi(1)=1\); and \(x=2\) gives \(\chi(x+2)=\chi(4)=1\). Thus exactly
\[\frac{p-3}{4}-1=\frac{p-7}{4}\]
values of \(b\in\{1,\ldots,p-3\}\setminus\{2,p-3\}\) satisfy the conditions. For each, \(2,b,b+2\) are quadratic nonresidues, neither of the latter two is \(-1\), and they are primitive by (1). The fourth term \(2b(b+2)\) is also a quadratic nonresidue. If it were \(-1\) modulo \(p\), then
\[(b+1)^2\equiv\frac12\pmod p,\]
contradicting \(\chi(1/2)=\chi(2)=-1\). It therefore has order \(2q\), proving both existence and the exact enumeration. In particular, \(p=11\) has \(b=6\) as its single fixed-first-entry witness.

Finally, at \(p=5\) the only primitive roots are \(2\) and \(3\), whose sum equals \(p\). At \(p=7\) they are \(3\) and \(5\), whose sum exceeds \(p\). There is no admissible pair in either case. This proves all assertions.

## Verification
A standalone Python program `verify_safe_prime.py` tests safe primes through a user-adjustable bound using integer primality trials and a modular multiplicative-order criterion independent of the Legendre-symbol proof. The checked bound \(p\le50000\) contains \(389\) safe primes, comprising \(196\) in the \(3\pmod8\) class and \(193\) in the \(7\pmod8\) class; the program confirms the exact fixed-entry count, the explicit witness, and the exclusions at \(p=5,7\). Run `python3 verify_safe_prime.py 50000`. These finite checks are corroboration only: the complete proof above covers all safe primes.

## Relationship to prior work
Zhi-Wei Sun's *New observations on primitive roots modulo primes*, Conjecture 4.2(i), dated \(2015\)-\(08\)-\(05\) within the article, asks whether the stated four-root witnesses exist at every prime greater than \(13\). The associated OEIS sequence A260947 records the least attainable sum and exhibits the witness \(2+6=8\) for \(p=11\). These give the target question and individual data, rather than the uniform safe-prime construction and exact enumeration.

Cohen, Oliveira e Silva, and Trudgian prove a general two-primitive-root additive representation theorem. It does not demand that the sum or the product of the three numbers be primitive, nor that ordinary representatives sum to less than \(p\). The present claim is stronger in those respects but restricted to safe primes. The two are not equivalent through the cited theorem alone. Classical Legendre-symbol identities underlie the proof; no novelty is claimed for the identity (2) itself.

## Limitations
The classification is only for safe primes, and does not settle Sun's conjecture for arbitrary primes. Infinitely many safe primes are not known to exist. The exact count is for witnesses whose first component is \(2\) in one residue class; it is not a count of all witnesses. An equivalent safe-prime result may occur in unlocated literature, and independent mathematical review has not yet occurred.

## References
1. Zhi-Wei Sun, *New observations on primitive roots modulo primes*, arXiv:1405.0290, Conjecture 4.2(i) and Theorem 1.3; https://arxiv.org/abs/1405.0290 (first arXiv submission \(2014\)-\(04\)-\(21\); Conjecture 4.2(i) dated \(2015\)-\(08\)-\(05\)).
2. Zhi-Wei Sun, OEIS A260947, https://oeis.org/A260947 (authored \(2015\)-\(08\)-\(05\)).
3. S. D. Cohen, T. Oliveira e Silva, T. Trudgian, *A proof of the conjecture of Cohen and Mullen on sums of primitive roots*, arXiv:1402.2724; https://arxiv.org/abs/1402.2724.
