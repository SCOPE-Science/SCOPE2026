# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

### Fixed-point existence

For each orthogonal projector \(P_i\) and \(0<\lambda<2\),

\[
\|(I-\lambda P_i)v\|_2^2
=
\|v\|_2^2-\lambda(2-\lambda)\|P_i v\|_2^2.
\]

Thus every factor is nonexpansive and equality occurs exactly on
\(\ker P_i\). If a full ordered product preserved the norm of a nonzero vector,
then equality would have to hold successively at every factor. Each factor would
therefore leave that vector unchanged, placing it in every \(\ker P_i\).
The assumption \(\sum_i P_i\succ0\) excludes such a nonzero vector. The complete
sweep is consequently a strict contraction and has one affine fixed point.

### Expansion

The ordered product and affine term have the expansions

\[
Q_\pi
=
I-\lambda S+\lambda^2
\sum_{p<q}P_{\pi_q}P_{\pi_p}+O(\lambda^3),
\]

and

\[
c_\pi
=
\lambda\sum_i q_i
-
\lambda^2\sum_{p<q}P_{\pi_q}q_{\pi_p}
+O(\lambda^3).
\]

After factoring the common \(\lambda\) from \(I-Q_\pi\) and \(c_\pi\),
invertibility of \(S\) gives an analytic fixed-point continuation at
\(\lambda=0\). Matching the first two powers yields

\[
S h_\pi
=
\sum_{p<q}P_{\pi_q}r_{\pi_p}.
\]

No commutativity between different projectors is used.

### Reverse-order cancellation

The least-squares condition gives \(\sum_i r_i=0\), and
\(r_i\in\operatorname{range}(P_i)\) gives \(P_i r_i=r_i\). Pairing every ordered
pair once across a permutation and its reverse produces

\[
S(h_\pi+h_{\pi^R})
=
\sum_jP_j\sum_{i\ne j}r_i
=
-\sum_jP_jr_j
=
-\sum_jr_j
=
0.
\]

Since \(S\) is nonsingular, \(h_{\pi^R}=-h_\pi\). The midpoint therefore has no
linear term.

### Edge cases checked

- In a consistent system all \(r_i=0\), so the first-order bias vanishes, as it
  should.
- Repeated or parallel constraints are allowed as long as the total projector
  sum spans the ambient space.
- The one-dimensional example
  \(P_i=1\), \((q_1,q_2,q_3)=(0,0,1)\) has an exact midpoint error
  \(\lambda^2/[6(3-3\lambda+\lambda^2)]\), confirming that second order is
  generally sharp.
- The proof does not rely on a particular permutation beyond pairing it with its
  exact reverse.

**Correctness assessment: PASS.**

## Originality

The closest established starting point is Censor--Eggermont--Gordon (1983),
which states that strong underrelaxation drives cyclic Kaczmarz limit points
toward the weighted least-squares solution, with a block-Kaczmarz proof.
The present statement adds a first-order expansion of the cyclic fixed point and
an order-reversal identity for its coefficient.

The literature search also checked:

- Popa's 1995 and 1998 Kaczmarz-based least-squares extensions;
- recent surveys of Kaczmarz methods for inconsistent and least-squares systems;
- symmetric Kaczmarz/SOR literature, where a forward sweep and a backward sweep
  are composed into one symmetric iteration;
- average and extended block Kaczmarz variants;
- generic symmetrically weighted sequential operator splitting, where opposite
  time-stepping orders are averaged to obtain second-order temporal accuracy.

These neighboring results establish that neither reverse sweeps nor
forward/reverse averaging are new ideas in isolation. The searched sources did
not, however, state the fixed-point coefficient

\[
S^{-1}\sum_{p<q}P_{\pi_q}r_{\pi_p},
\]

its sign reversal under \(\pi\mapsto\pi^R\), or the resulting
\(O(\lambda^2)\) midpoint approximation to the weighted least-squares solution.

The full text of Censor--Eggermont--Gordon (1983) was not inspected end-to-end;
its abstract and later descriptions of its theorem were checked. This is the
source most likely to contain an unobserved local expansion. The full text of
Popa (1995) was also not inspected; its abstract establishes exact
least-squares-convergent Kaczmarz combinations but does not reveal the detailed
construction. Either source could reduce the originality claim if it contains
the same reverse-order fixed-point cancellation.

**Originality assessment: PASS, to the best of our knowledge, with the stated
residual source-access risk.**

## Value

The theorem supplies three pieces of reusable information:

1. an explicit leading error formula for strong underrelaxation;
2. a precise statement of how cyclic ordering enters that error;
3. a bias-correction mechanism requiring only the opposite ordering.

The result is structurally broader than single-row Kaczmarz because it is stated
for arbitrary finite families of orthogonal block projectors. It also gives a
sharp example, so the order improvement is not merely an artifact of a loose
bound.

The practical value is qualified. Two underrelaxed cyclic solves can be slow,
and dedicated least-squares methods may be preferable when raw solution time is
the objective. The contribution is therefore primarily a convergence-structure
and bias-correction result rather than a claim of superior solver complexity.

**Value assessment: PASS.**

## Sources checked

- Y. Censor, P. P. B. Eggermont, D. Gordon (1983),
  https://doi.org/10.1007/BF01396307
- C. Popa (1995),
  https://doi.org/10.1080/00207169508804364
- C. Popa (1998),
  https://doi.org/10.1007/BF02510922
- D. Dax (2022),
  https://doi.org/10.1155/2022/6143444
- Current Kaczmarz survey,
  https://doi.org/10.1007/s11075-024-01945-2
- Operator-splitting comparison containing symmetrically weighted sequential
  splitting,
  https://doi.org/10.1016/j.apnum.2008.03.031

## Scientific limitations

The theorem assumes finite-dimensional orthogonal projectors and
\(\sum_iP_i\succ0\). Rank-deficient extensions, finite-\(\lambda\) error
constants, floating-point behavior, stopping rules for the two cyclic solves,
and end-to-end complexity comparisons are not established here.
