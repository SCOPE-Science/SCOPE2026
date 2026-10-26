# Review

## Correctness

PASS. The exact posterior formula splits the first candidate's likelihood from later listed candidates and the unseen tail. The bound \(p_{n,q_2}\le A_n\le L_n p_{n,q_2}\) makes the aggregate of the later list entries have the same exponential rate as the second entry whenever \(\log_2 L_n=o(n)\). The tail term retains the fixed-list exponent under \(y_L<1\). These facts yield the stated strict-sign cases for \(\Delta\). The critical case \(\Delta=0\) is not claimed.

## Originality

PASS, subject to the stated residual risk. The closest primary source, arXiv:2610.02458, explicitly assumes fixed list size and does not state uniformity in a growing list. The recent result arXiv:2607.00205 treats a list-guesswork moment exponent, not the conditional posterior probability given the list-rank tuple. Deduplication searches found no direct matching claim. Search failure is not treated as proof of global uniqueness.

## Value

PASS. Subexponential and polynomial list sizes are standard in list decoding. Extending the reliability boundary to this regime shows whether the first candidate remains trustworthy as the output list grows, and shows that the first, second, and last rank exponents still control the strict-sign boundary.

## Closest literature and limitations

- Struss, Médard, and Duffy, arXiv:2610.02458: exact posterior formula and fixed-list asymptotic reliability.
- Tavakoli, arXiv:2607.00205: subexponential list size for a different quantity, the constrained-guesswork moment exponent.
- The claim assumes the source paper's large-deviation regularity, a uniform random codebook, \(L_n=2^{o(n)}\), and \(y_L<1\). It does not resolve \(\Delta=0\) or exponential list sizes.

Self-review: passed. Independent audit: not yet performed.
