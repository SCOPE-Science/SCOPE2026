# Independent mathematical audit

## correctness

PASS

For all n>=0, Apéry A(n)=Σ binom(n,k)^2binom(n+k,k)^2 and signed AZ B(n)=Σ_{k<=n/3}(-3)^(n−3k)binom(n,3k)binom(n+k,k)binom(2k,k)binom(3k,k). Legendre ν2(binomial(2k,k))=s2(k) and Lucas yield the known A(n)≡1+4β(n) mod16. Chan–Zudilin exact alternate AZ expansion has kth multiplier (4k)!/(k!)^4 with ν2=3s2(k), so only k=0 and 2^j survive mod16. For k=2^j the factor mod16 is 8, and Lucas gives B(n)≡1+4n+8H(n), where H(n) parity of sum bits (n+3·2^j)_(j+2). Binary carry algebra gives 2H(n)≡n+β(n) mod4, so B(n)≡1+4β(n)+8n≡A(n)+8n mod16. Arbitrary candidate period d has even multiple a=2^r(2^s−1), choose n=2^k far higher: β(n)=2, β(n+a)=4, residues differ 8, ruling out eventual periodicity. Independent direct binomial-definition checks for n=0..14 passed; original verify.py independently compares two B formulas n<=256 and binary carry n<100000, but these bounded checks do not establish all n.

## originality

PASS

Best-of-knowledge originality for the precise claim; general ingredients and prior examples credited. Full-text gaps and implication risks listed explicitly.

## value

PASS

This explicit cross-sequence arithmetic bridge is a natural unknown relation between two much-studied Apéry-like sequences; the coefficientwise modulus16 result identifies a sharp transition in AZ residue dynamics from known mod8 periodicity to non-eventual periodicity. It is not just a rephrasing of either one-sequence congruence; it uses valuations and a nontrivial binary-carry identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
