# Same-model review

## Correctness
PASS. The proof first excludes odd two-prime support by the sharp universal abundancy bound \(15/8<2\). For \(n=2^a p^b\), the divisor-sum inequalities for abundance and for deficiency of \(n/p\) force \(b=1\); abundance and deficiency of \(n/2\) then give exactly \(2^a<p<2^{a+1}-1\). This yields a bijection with non-Mersenne odd primes and the exact counting identity. The phase asymptotic follows uniformly from the prime number theorem because the relevant prime cutoff lies between \(2^m\) and \(2^{m+1}\), while the Mersenne-prime correction is only \(O(\log X)\). The included exact computation independently checks all two-prime-support integers through \(500000\) and 49 exact phase identities.

## Originality
PASS. The factor classification itself is not claimed new: a later full-text paper explicitly says Dickson found all even primitive abundant numbers with \(\omega\le3\). The originality check therefore targeted the exact formula \(P_2(X)=\pi(U)-2-\mathcal M(U)\), the equivalent non-Mersenne-prime parametrization used for counting, the piecewise phase function, and the constants \(2\) and \(2\sqrt2\). Searches of mathematical records, sequence databases, and broader distribution papers found no matching or stronger fixed-\(\omega=2\) counting statement. Global results of Ivić and Avidon concern all primitive abundant numbers and do not imply a fixed-support phase law.

## Value
PASS. The theorem isolates the smallest possible prime-support regime for strict primitive abundance and gives a complete quantitative description rather than another finite table. It shows a genuine structural phenomenon: the normalized count does not converge, but oscillates with an explicit base-4 phase between two exact limiting constants. This provides a clean benchmark for the much harder global distribution problem and distinguishes fixed-support behavior from the known all-support estimates.

## Closest literature and limitations
The closest historical source is Dickson’s 1913 “Even Abundant Numbers,” whose classification scope is explicitly summarized in the later full-text paper of Amato, Hasler, Melfi, and Parton. Ivić and Avidon are the closest distribution papers, but their counting functions range over all primitive abundant numbers. OEIS A071395, A133814, and A306986 provide sequence and counting data but not the fixed-support phase theorem. The main residual originality risk is a differently phrased result in older literature not exposed by modern indexing; the complete Dickson text was not available line-by-line in the inspected open sources.

Same-model review: passed. Independent audit: not yet performed.
