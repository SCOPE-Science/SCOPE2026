# Independent mathematical audit

## correctness

PASS

Both divisor sums are multiplicative with local factors 1+p^a and sum_{d|a}p^d. For a=1 their ratio is >1, for a>=2 their local ratio reverses, ruling out prime powers, squarefree integers, and p²q². For p^a q with a=2,3, equality rearranges to (p-1)q=p^a+1; p-1|2 forces p=2 or 3 and yields only p²q=20,45. For p²qr, equation (p²+1)(q+1)(r+1)=p(p+1)qr implies q,r>p+1. At p=2 divisibility by 5 contradicts q,r>5. At odd p, B=(p²+1)/2>1 is coprime to p(p+1), so B|qr; since B<qr and qr squarefree, B=q or r. Setting q=B gives (p-3)r=p²+3, so p-3|12 and p=5 or 7; r=14 or q=25 invalid. Exhaustion of all exponent partitions with Omega<=4 completes the universal proof. Independently enumerated 152318 low-Omega integers <=200000 with sole hits 1,20,45; finite test is not the proof.

## originality

PASS

Trudgian introduced the equality question and examples, while OEIS records examples without an exhaustive proof. Published Resultary work classifies p^a q for 2<=a<=49, covering two-prime cases in this theorem, but not the genuinely different p²qr support. A more general unindexed low-Omega classification remains possible.

## value

PASS

The total prime-factor multiplicity Omega is a natural arithmetic complexity parameter. The theorem proves a complete infinite-domain low-complexity cutoff motivated by the open-ended unitary/exponential equality problem. The new p²qr obstruction adds real three-prime-support information beyond known p^a q calculations; this is not merely a numeric table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
