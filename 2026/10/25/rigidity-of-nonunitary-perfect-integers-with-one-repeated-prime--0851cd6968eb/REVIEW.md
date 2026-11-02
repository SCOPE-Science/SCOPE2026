# Independent mathematical audit

## correctness

PASS

For rho(n)=0 every divisor is unitary and sigma(n)-sigma*(n)=0. For rho(n)=1 write n=p^a s, a>=2, squarefree s coprime to p: multiplicativity gives sigma(s) times T=sum(p^j,j=1..a-1). If p is odd, parity excludes odd s>1, while s=1 gives T<p^a; for s=2t, v2(sigma(t)) forces omega(t)<=1 and sigma(t)/t<=4/3. Therefore (sigma-sigma*)/n < (3/2)(4/3)/(p-1)<=1. Hence p=2. Put M=2^{a-1}-1: M sigma(s)=(M+1)s. At a=2 the required odd squarefree perfect s is impossible. At a>=3 M divides s; divisor-sum monotonicity and sigma(M)>=M+1 force both equalities, so s=M prime. Conversely n=2^{r+1}(2^r-1) with Mersenne prime 2^r-1 satisfies the equation. All quantifiers include arbitrarily many odd squarefree factors. Independent exact divisor-sum enumeration 1..60000 returned only 24,112,1984,32512 and matched their repeated-prime counts. The finite enumeration supports but does not replace the unrestricted argument.

## originality

PASS

The classical Ligh–Wall construction/conjecture is acknowledged, but its published forward direction does not yield the unrestricted converse for rho(n)<=1. The 2024 two-prime-support argument does not cover arbitrarily many singleton prime factors. Best-of-knowledge PASS, subject to old folklore and unpublished number theory.

## value

PASS

This is an exact structural restriction on the classical Ligh–Wall nonunitary-perfect problem: any counterexample to its full conjecture must contain at least two distinct squared primes. Arbitrarily many squarefree cofactor primes are handled uniformly; the result is not simply a lookup-table restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
