# Independent mathematical audit

## correctness

PASS

The identities A(n)=s_2(n) and B(n)=2s_2(n)-s_2(3n) follow exactly from Legendre. Since 3n is divisible by 3 but is not a power of 2, s_2(3n)>=2, hence 0<=B<=2k-2. Kummer count of carries in n+2n shows the first carry forces a second at the next bit, excluding B=1. For b=0 use z_k=(4^k-1)/3; for b=2j-2 use e_j=(2^(2j-1)+1)/3; for b=2j-3 use o_j=(2^(2j-2)+5)/3. Each has the asserted digit weight and valuation. Map P(n)=4n+1 increases A by one while fixing B, so every b=0 or b=2..2k-2 appears for all appropriate k; n->2^h*n gives infinitely many witnesses. Independent all-pair constructive check for k=1..20 tested 381 pairs and a separate direct scan n=1..9999 found no excluded value. Finite evidence is corroborative; proof covers every n and k.

## originality

PASS

Qualified best-of-knowledge originality: compare exact statement and model rather than terminology. Known foundational tools, marginal/special cases and directly overlapping results are credited. No actually inspected stronger result is shown to imply the complete final claim. Unavailable or only partially inspected plausible primary work is identified in residual risks; failed searches are not treated as proof of novelty.

## value

PASS

An exact attainable-support theorem for two natural 2-adic binomial valuations is a motivated fine-scale classification; its globally forbidden value 1, sharp upper endpoint 2k-2, and explicit infinite witnesses are not obtained from marginal divisibility results or finite scans. It can be used to distinguish feasible simultaneous divisibility profiles, though it claims no asymptotic frequencies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
