# Independent mathematical audit

## correctness

PASS

The input is read from the least significant ternary digit. A carry c with next digit a in {0,1} is allowed exactly when (c+Ma) mod 3 is not 2, and maps to floor((c+Ma)/3). The carry interval [0,floor(M/2)] is invariant. Independent fixed-point enumeration starting from zero gave the 3 and 18 states and 4 and 24 edges, with no reachable sinks, so every counted prefix extends. Iterating the adjacent-state sum on an initial all-ones vector gave zero residual at all states for A13^3-A13^2-I and A85^9-A85^8-A85^4-2A85^2-I. Multiplication by A^k proves every subsequent recurrence, unlike a scalar finite fit. The computed initial coefficients give the displayed numerators. The factorization of the 85 denominator is exact; its second factor H=1+z^3+z^4+z^6 is positive on the positive real axis. Neither numerator vanishes at the unique root r in (0,1) of 1-z-z^3. Pringsheim's theorem rules out a smaller radius, and the cited right-resolving path-set theorem gives Hausdorff dimension log_3(1/r) in the stated metric. The denominator is even reduced: N85=(z^2+z+2)H-1, and 1-z-z^3 is irreducible over Q and cannot divide N85. The distinct length-three counts verify different prefix languages.

## originality

PASS

The pass concerns the specialized 85 prefix law and exact 85-to-13 dimension comparison, not the carry algorithm, the known 13 case, or the idea of obtaining different graphs with a common growth constant. The strongest nearby catalogue computation is for 31. The primary sequel's families and comparison examples do not give this exact 85 case.

## value

PASS

The multiplier is the next small sparse 3^k+4 case after 13 and the indexed 31 example. The exact prefix law resolves all scales of a natural intersection and exhibits the same entropy as the simpler 13 intersection despite different finite languages and graph sizes. That gives both a precise benchmark for sparse-multiplier classification and a concrete example of information the dimension discards, beyond a tabulated decimal or a short prefix sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
