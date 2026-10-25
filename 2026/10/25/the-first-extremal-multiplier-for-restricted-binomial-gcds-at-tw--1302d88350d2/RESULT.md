# The first extremal multiplier for restricted binomial GCDs at twice a prime minus one

## Finding
For each odd prime \(p\), set \(m=2p-1\) and, for integers \(q\ge2\), set
\[H_p(q)=\gcd\left\{\binom{mq}{md}:1\le d<q\right\}.\]
The entire initial multiplier window has the exact valuation profile
\[\nu_p(H_p(q))=\begin{cases}2,&q=(p+1)/2,\\0,&q=p+1,\\1,&2\le q\le p\text{ and }q\ne(p+1)/2.\end{cases}\]
Consequently the first multiplier at which the largest possible valuation is attained is \(q=(p+1)/2\); the least corresponding binomial row is \((2p-1)(p+1)/2\). The profile includes a rise, a return to valuation one, and a final drop to zero.

## Assumptions and scope
The prime \(p\ge3\) is odd; \(q\) ranges over every integer from \(2\) through \(p+1\), inclusive. The gcd is over all positive integer \(d<q\). The valuation \(\nu_p\) is the usual exponent of \(p\). No assertion is made about the complete multiplier spectrum beyond this window. The general valuation ceiling is \(2\) because \(m<p^2\), by the restricted-binomial-GCD maximal-valuation theorem in the first reference; it is also attained explicitly here.

## Proof
Write \(b=(p-1)/2\), \(q_0=b+1\) and \(m=2p-1\). Kummer's theorem identifies \(\nu_p\binom{N}{K}\) with the number of base-\(p\) borrows in subtracting \(K\) from \(N\), equivalently the number of carries when adding \(K\) and \(N-K\). The following four disjoint ranges exhaust the stated window.

First let \(2\le q\le b\). Then \(N=mq=(2q-1)p+(p-q)<p^2\). Every permitted \(K=md\), \(1\le d<q\), has low digit \(p-d>p-q\). Exactly one borrow occurs (at the units digit), with no possible further borrow above \(p^2\). Thus all permitted coefficients have valuation one.

Next, at \(q=q_0\), \(N=mq_0=p^2+b\), with base-\(p\) digits \((b,0,1)\) from low to high. Each permitted \(d\) lies between \(1\) and \(b\), and \(K=md=(2d-1)p+(p-d)<p^2\). Since \(p-d>b\), the units subtraction borrows, and because \(K\bmod p^2>b=N\bmod p^2\), the next digit borrows again from the \(p^2\) place. Since \(K<N<p^3\), no higher borrow occurs. Every permitted coefficient has valuation exactly two.

Now let \(q=q_0+j\), where \(1\le j\le b\). One has \(N=mq=p^2+2jp+(b-j)\), with base-\(p\) digits \((b-j,2j,1)\). For any \(1\le d<q\), if \(d\le b\), the units digit of \(md\) is \(p-d\ge b+1>b-j\). Otherwise \(d=q_0+t\), with \(0\le t<j\); the units digit is \(b-t>b-j\). Thus every selected coefficient incurs at least one borrow. Taking \(d=q_0\), its lower index is \(K=p^2+b\) and its complement is \(N-K=mj=(2j-1)p+(p-j)\). In their base-\(p\) addition, \(b+(p-j)\) produces one carry and \(0+(2j-1)+1=2j\le p-1\) produces no second carry. Hence the minimum valuation is exactly one throughout this range, including \(q=p\).

Finally, at \(q=p+1\), the upper index is \(N=2p^2+(p-1)\), with digits \((p-1,0,2)\). The permitted choice \(d=q_0\) yields \(K=p^2+b\), with digits \((b,0,1)\), each at most the corresponding digit of \(N\). Lucas's theorem (or Kummer's theorem with no borrows) shows that \(\nu_p\binom NK=0\). This establishes the last value and the claimed least extremal multiplier. \(\square\)

## Verification
The accompanying standalone Python program `verify.py` computes each valuation independently through the exact digit-borrow criterion. It checks all odd primes through \(71\) and all multipliers \(2\le q\le p+1\), comparing the minimum over every allowed \(d\) with the displayed formula. The run reports `CERTIFICATE_OK 637`. This is finite corroboration, not the proof of the universal statement.

## Relationship to prior work
The first reference proves a general restricted-binomial-GCD maximal-valuation ceiling and treats some extremal-row families, including moduli of the form \(p^a+1\) with \(a\ge2\), but does not give this complete first-window profile for \(m=2p-1\). The second examines primes congruent to \(-1\) modulo the fixed restriction modulus; those congruence hypotheses do not apply to \(m=2p-1>p\). The third concerns a different restricted-binomial framework and does not state this profile. The present result determines a natural previously unfilled threshold and all preceding multipliers in one infinite family.

## Limitations
The window ends at \(q=p+1\). No subsequent valuation classification is proved. The result relies on Kummer's theorem and the established global upper bound; the exact first-window profile has a direct digit proof. A prior-literature comparison cannot exclude every implicit or unpublished equivalent formulation. Independent mathematical assessment has not been performed.

## References
1. Fairfax-Ball, *Restricted binomial greatest common divisors and extremal valuations*, arXiv:2610.01328v1, first publicly available 2026-10-01. https://arxiv.org/abs/2610.01328
2. Fairfax-Ball, *Restricted Binomial GCDs at Primes Congruent to -1*, arXiv:2609.37754. https://arxiv.org/abs/2609.37754
3. McTague, *On the greatest common divisor of certain binomial coefficients*, arXiv:1510.06696. https://arxiv.org/abs/1510.06696
