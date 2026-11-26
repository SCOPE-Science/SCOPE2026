# Independent mathematical audit

## correctness

PASS

For either sign, the next odd term is y_i k_i after j_i steps. Escape excludes k_i=1 (a repeated odd term), y_i=1, and zero. Since k_i divides y_i+epsilon and all earlier multipliers divide y_i, induction gives precisely the pairwise coprimality and the additive formula for omega. The resulting odd-prime product is at least (r+2)!/2; monotone inversion of r log r gives r <= (1+o(1)) L_r/log L_r for L_r=log y_r, even when L_r is much larger. At T_r <= t < T_{r+1}, x_t >= y_r, and bounding each j_i for i<=r by log(y_r+1)/log 2 gives t <= (1/log 2+o(1)) L_r^2/log L_r. Thus t log t <= (2/log 2+o(1))L_r^2, giving the exact stated constant in the ordinary iteration clock. Proof line 33 means additivity, not multiplicativity, of omega on coprime arguments; the displayed formula is correct. The attached Python test and its recorded output check finite return blocks and prime products, not the rate; the infinite proof was reconstructed without running the archived code.

## originality

PASS

Best-of-knowledge pass for the prime-support refinement and full-clock bound, not for the known return formulas or escape classification. The closest inspected papers supply the return multiplications and return-count growth, but not the factorial prime-support step and its conversion to ordinary time.

## value

PASS

This quantifies escape in the natural iteration clock for every escaping orbit of both signed maps, where long halving runs prevent an odd-return rate from being read directly as a time rate. New prime support gives the substantive sqrt(log t) gain over the analogous estimate based only on geometric growth at the odd returns. It complements the known qualitative classification and does not depend on a distribution of seeds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
