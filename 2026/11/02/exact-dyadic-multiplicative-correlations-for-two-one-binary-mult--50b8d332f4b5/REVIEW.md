# Independent mathematical audit

## correctness

PASS

For m=2^k+1 odd, low-bit multiplication with carry c yields next d=floor((c+mb)/2), sign factor (-1)^c independent of chosen input bit b, hence row transition M_{c,d}=(-1)^c(sum indicators). After j<=k digits the low and shifted copies do not overlap and R_j=sum_{a<2^j}e_{a2^{k-j}}. Summing parity-cancelled endpoints gives R_{k+1}=e_{2^{k-1}}-e_{2^k}, next row explicit, and exact row equality R_{k+2}-R_{k+1}-R2+3R1-2R0=0 for all k>=2. Multiply by M^r and final carry vector tau(c) to obtain unrestricted recurrence; initial 1, k+1 zeros, 2 give displayed rational GF. Independently checked exact row relation k=2..8 and 70 direct finite dyadic sums. k=1 excluded; r=0 included; sums are ordinary integers.

## originality

PASS

Marginal Thue-Morse along arithmetic multipliers, translation-shift correlations and automata recurrences are known, but the exact two-factor dilation correlation for the infinite family m=2^k+1 and its universal k-dependent all-r GF was not found in inspected sources.

## value

PASS

An unexpectedly short exact recurrence simultaneously for all binary two-one multipliers quantifies dyadic cancellation depths and later oscillations in a natural digital-correlation problem. Its infinite parameter uniformity and explicit generating function exceed a one-off computational table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
