# Independent mathematical audit

## correctness

PASS

The finite-difference argument applied to F(x)=binom((n-1)x,n-1) yields D(n-1)|n. At each prime p^a||n, the Kummer residue/carry count gives the uniform lower bound a-b, with b=floor(log_p(n/p^a)), by counting the first a carries and the extra a+h carries when v_p(q-1)>b; the explicit multiplier q=1+p^a(m-p^b), or q=2 for m=1, yields exactly a-b carries, with the published Guo et al. Lemma 9 handling zero valuation when m>p^a. Independently used Legendre factorial valuations over every q=2..n for n=3..349: 680 local prime checks, all exact; tested 313 nonzero-val minimizer witnesses. The theorem is exactly for n>=3 and q in this finite window.

## originality

PASS

The local Guo–Qiu–Cao–Feng–Gao criterion settles whether a prime divides the gcd and when the gcd is 1; it does not state the exact multiplicity p^(a-b) or explicit minimizer for every p||n. Kummer is a classical proof method, not a competing exact formula. Published theorem and its full HTML were inspected; no indexed exact-power formula was located, but unindexed older formulas remain a risk.

## value

PASS

The gcd D(k) is an OEIS-motivated natural integer-valued binomial invariant, and its exact prime-power factorization distinguishes the previously unknown degree of shared divisibility even where the known gcd-one predicate gives no information. The explicit extremal multipliers are a structural local result, not a random finite slice or merely numeric new row.

The dated certificate retains the supplied scientific assessment, sources and limitations.
