# Independent mathematical audit

## correctness

PASS

For n>=10000 and positive powers a=n-tau(n), b=n+1-tau(n+1), an unequal exponent collision sigma(n)^a=sigma(n+1)^b forces both bases to powers of a common C>=2, with exponent s=b/gcd(a,b). The divisor pairing tau(m)<=2sqrt(m) bounds gcd(a,b)<=1+4sqrt(n+1), hence s>sqrt(n+1)/5-1, contradicting s<=log_2(sigma(n))<=log_2(n(1+log n)) by the checked endpoint and derivative comparison. For 2<=n<10000 an independently implemented exact sieve and prime-valuation equality check finds no powered collisions (only n=1 excluded). Therefore every n>=2 collision has equal exponents/bases, i.e. sigma(n)=sigma(n+1), tau(n+1)=tau(n)+1; converse immediate. Parity makes one member square, common odd sigma makes other twice square, yielding x^2-2y^2=+-1 and O(log X) Pell count.

## originality

PASS

PASS best of knowledge: OEIS A236288 defines exactly this weighted divisor-sum power and conjectures no consecutive nontrivial collisions, but does not prove that equality forces simultaneous equal sigma and divisor-count jump one. Benito 2007 Theorem 3 gives the Pell restriction after assuming equal odd sigma, not this new exponent-rigidity necessity. Other Resultary restricted prime-support/proper-divisor equations differ.

## value

PASS

PASS: for a precisely posed consecutive collision conjecture involving huge weighted powers, the theorem gives a necessary-and-sufficient structural reduction to simultaneous ordinary divisor-sum and divisor-count identities, and a sharp qualitative logarithmic sparsity upper bound via Pell solutions. It is a meaningful motivated reduction even though existence remains open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
