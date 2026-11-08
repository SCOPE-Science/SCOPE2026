# Independent mathematical audit

## correctness

PASS

Legendre identity gives v_q binom(qn,n)=s_q((q-1)2^e)/(q-1) exactly. Lucas/Kummer parity gives binom(q^2,q) even for every odd prime q, excluding t=1. When q>2^e, the base-q digits of (q-1)2^e sum to q-1, excluding t>=2; equality q=2^e cannot occur for odd q. CRT reduces remaining finite checks to binomial mod 2^e. Recomputed every possible (q,t) candidate for e<=4 with exact integers and full-modulus checks: 36 and 400 alone survive. The unrestricted finiteness rests on the digit-and-carry argument.

## originality

PASS

Qualified best-of-knowledge comparison of actual statements with primary literature and published mathematical results; not a claim of exhaustive historical-priority verification.

## value

PASS

A uniform finite-prime obstruction at each fixed 2-adic layer for a natural binomial-congruence problem, with complete initial layers. It goes beyond lookup of two existing examples: the quantified bound makes an infinite two-parameter search finite and illuminates dyadic versus odd cofactor behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
