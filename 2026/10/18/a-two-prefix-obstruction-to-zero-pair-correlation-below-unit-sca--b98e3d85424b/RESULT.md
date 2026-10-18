# A two-prefix obstruction to zero pair correlation below unit scale

## Finding
For any infinite sequence of points \((x_j)_{j\ge1}\) on the unit circle, set
\[
R_N(a)=\frac1N\#\left\{(i,j):1\le i\ne j\le N,\ \|x_i-x_j\|\le\frac aN\right\},
\]
where the norm is distance to the nearest integer. The points need not be distinct or uniformly distributed. For every \(0<a<1\),
\[
\boxed{\limsup_{N\to\infty}R_N(a)\ge\max\left\{0,4-2\sqrt2-\frac1a\right\}.}
\]
This follows from the following **finite two-prefix inequality**. For every pair of integers \(N\ge3\) and \(N<M<2N\), putting \(\varepsilon=(M-N)/N\),
\[
\boxed{R_N(a)+R_M(a)\ge 2\left(1+\frac{\varepsilon(1-\varepsilon)}{1+\varepsilon}-\frac1a\right).}
\]
Consequently, if \(R_N(a)\to f(a)\) exists, then \(f(a)>0\) whenever \((2+\sqrt2)/4<a<1\). The threshold \((2+\sqrt2)/4=0.8535533905\ldots\) is the exact threshold of positivity provided by this two-prefix inequality, **not** an assertion of the globally optimal threshold.

## Assumptions and scope
Work on the circle \(\mathbb R/\mathbb Z\). Each prefix consists of its first \(N\) labeled points, allowing coincidences. The circular order is taken with a fixed tie-breaking rule consistent across prefixes (e.g., by increasing point coordinate and then increasing index). The distance \(\|u-v\|\) is the shorter circular distance. The result applies to each fixed real \(a\in(0,1)\), and does not require that the entire family of limits \(f(a)\) exist.

## Proof
Fix \(N\ge3\), \(N<M<2N\), and write \(\varepsilon=(M-N)/N\in(0,1)\). Order the first \(N\) labeled points around the circle, and denote their \(N\) successive oriented gap lengths by \(g_1,\ldots,g_N\), so that \(\sum_i g_i=1\). For each old gap \(i\), let \(r_i\) be the number of new labels from indices \(N+1,\ldots,M\) that lie between its old endpoints in the consistently tied circular ordering. Thus \(\sum_i r_i=M-N=\varepsilon N\), and the old gap is subdivided into exactly \(r_i+1\) new consecutive gaps.

Let \(b_i=1\) when \(g_i\le a/N\), and let \(b_i=0\) otherwise. Write \(s_i\) for the number of its \(r_i+1\) subgaps having length at most \(a/M\). All other subgaps have length strictly greater than \(a/M\); therefore
\[
g_i\ge(r_i+1-s_i)\frac aM.
\]
The following stronger *case-dependent* inequality holds for each old gap:
\[
\boxed{g_i\ge (1-b_i)\frac aN+r_i(1-\varepsilon)\frac aM-s_i\frac aM.}\tag{1}
\]
Indeed, if \(r_i=0\) and \(b_i=0\), the assertion is the definition \(g_i>a/N\) (and \(s_i=0\)). If \(r_i=0\) and \(b_i=1\), the right side is nonpositive. If \(r_i\ge1\) and \(b_i=1\), inequality (1) follows from the subgap estimate, since \(r_i+1\ge r_i(1-\varepsilon)\). Finally, when \(r_i\ge1\) and \(b_i=0\), subtracting the right side of (1) from the subgap estimate gives exactly \(a\varepsilon(r_i-1)/M\ge0\), because \(a/N=a(1+\varepsilon)/M\). These cases include coincident point locations under the fixed tie policy.

Sum (1) over the \(N\) original gaps. Let \(B_N=\sum_i b_i\) and \(S_M=\sum_i s_i\). We obtain
\[
1\ge a\left(1-\frac{B_N}{N}\right)+a\frac{\varepsilon(1-\varepsilon)}{1+\varepsilon}-a\frac{S_M}{M}.\tag{2}
\]
Each old gap counted by \(B_N\) joins two different labels at circle distance at most \(a/N\); each short new subgap counted by \(S_M\) also joins two different labels at circle distance at most \(a/M\). Since \(N\ge3\) and \(M>N\), distinct successive cyclic edges represent distinct unordered label pairs, even in the presence of coincident coordinates. Accordingly,
\[
\frac{B_N}{N}\le\frac{R_N(a)}2,\qquad
\frac{S_M}{M}\le\frac{R_M(a)}2.
\]
Inserting these estimates into (2) proves the claimed two-prefix inequality.

Now choose \(M_N=\lfloor\sqrt2N\rfloor\); for all sufficiently large \(N\), \(N<M_N<2N\), and \(\varepsilon_N=(M_N-N)/N\to\sqrt2-1\). The elementary identity
\[
\frac{\varepsilon(1-\varepsilon)}{1+\varepsilon}
=3-2\sqrt2-\frac{(\varepsilon+1-\sqrt2)^2}{1+\varepsilon}
\]
shows that the attained limiting value is \(3-2\sqrt2\), the maximum of the ratio over \(\varepsilon\in(0,1)\). Denote \(L=\limsup_N R_N(a)\), potentially infinite. If \(L<\infty\), applying the two-prefix inequality and then taking limits along \(N\to\infty\) yields
\[
2L\ge2\left(4-2\sqrt2-\frac1a\right).
\]
The nonnegativity \(L\ge0\) and the trivial case \(L=+\infty\) finish the claim. The positive regime is precisely \(a>1/(4-2\sqrt2)=(2+\sqrt2)/4\).

## Verification
The standalone Python 3 program `proof_check.py` checks the gap-by-gap inequality (1), the adjacency estimates, and the final finite two-prefix bound with exact rational arithmetic for 5,430 combinations of rational circle configurations, prefix lengths, and scale values. It includes repeated points, complete collisions, and distinct regularly spaced inputs; it also checks the algebraic positivity threshold at high decimal precision. To reproduce, run `python3 proof_check.py` from a directory containing this result and the program. These finite tests are supplementary checks only; the proof above is valid for all infinite sequences and real \(a\in(0,1)\).

## Relationship to prior work
Christian Weiß, *Sharp Bounds for Limits of N-Point Correlation*, arXiv:2610.13468v1 (first public version October 9, 2026), proves optimal **pointwise** lower bounds for \(\liminf_N R_N(a)\). For \(0<a<1\) that lower bound is zero, attained along subsequences, and the paper's upper bounds conditioned on \(f(a)=0\) do not exclude zero full-prefix limits in the interval treated here. The present bound instead couples **two nested prefixes of the same infinite sequence** and thereby forces a positive **limsup** above the stated scale. Its conclusion neither contradicts nor weakens the pointwise sharpness of the earlier construction.

Fiedler and Weiss (2025) address non-continuity of limiting functions under a restricted finite-gap assumption. Weiß (2023) computes empirical pair correlations for a particular van der Corput sequence (whose limit exists and vanishes through scale \(1/2\)). Neither result supplies an unrestricted two-prefix lower bound.

## Limitations
The constant \((2+\sqrt2)/4\) is a rigorous exclusion threshold from the stated method; no claim of its universal optimality is made. The theorem does not construct a sequence realizing equality, compute all possible limiting functions, or establish a positive **liminf** at this scale. It does not rule out sequences with arbitrarily small pair correlation along sparse subsequences in \((0,1)\).

## References
1. Christian Weiß, *Sharp Bounds for Limits of N-Point Correlation*, arXiv:2610.13468v1, October 9, 2026. https://arxiv.org/html/2610.13468v1
2. Jasmin Fiedler and Christian Weiss, *On the pair correlation statistic of sequences with the finite gap property*, *Archiv der Mathematik* **125** (2025), 107–113. https://doi.org/10.1007/s00013-025-02126-w
3. Christian Weiß, *On the finite pair correlation function of van der Corput sequences*, arXiv:2306.10437v1, June 17, 2023. https://arxiv.org/html/2306.10437v1
