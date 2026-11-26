# Independent mathematical audit

## correctness

PASS

For the repaired claim, use the known row norms in the square-root conductance normalization. At fixed t, g_0 decreases in n while a(g_0−g_m)=(1−x)(1−y)/(1−xy) with x=r^floor(n/2), y=r^ceil(n/2) increases: one exponent increments and each partial derivative in x,y is strictly negative. This also bounds the latter expression by one, so every spoke row is strictly below two. The rim row strictly increases in n. At five rims multiply R_5<2 by positive quantities and substitute sqrt(t)=(1−u²)/u, u=sqrt(r). The resulting (1−u^4)p(u) is positive: p>=15/64 for u<=1/2 and the cleared polynomial in v=(2u−1)/(1−u) has all coefficients positive on the other half. With n=6,t=1/4 the exact periodic Green recurrence gives g_0=1188/1105 and g_3=512/1105 and rim row 2292/1105>2. Thus this same weight works for every n>=6 and no weight works at sizes 3–5. The repair's exact standard-library verifier ran successfully, checking both coefficient identities and the full rational Green column and witness. The frozen script was inspected, not executed.

## originality

PASS

Credit is confined to an exact finite-size crossing boundary for level two, with an all-weight sign certificate ruling out the smaller sizes. The known exact two-row norm, crossover asymptotic and global/fixed-weight limits are credited as inputs or omitted. The same-family publications inspected do not give the repaired six-rim cutoff; the different six-rim circulation projection result is not equivalent. This is a bounded assessment, not a historical priority certification.

## value

PASS

The coordinatewise norm is the worst possible amplification of normalized measurement error. Locating the first wheel size where it can exceed a factor of two separates an all-weights guarantee at small sizes from an explicit construction that works at every larger size. The global sign certificate is essential to ruling out smaller counterexamples; the exact rational witness and already known formula, by themselves, would not establish the cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
