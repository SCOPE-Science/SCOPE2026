# Exact census and arithmetic rarity of rank-two recovery-balanced linear codes

## Finding

Fix a prime power \(q\geq 2\) and an integer \(n\geq 2\). Consider labeled linear \([n,2]_q\) codes and the uniform-with-replacement coordinate-sampling model. A code is *recovery balanced* if the expected numbers of draws needed to recover each of its \(n\) encoded coordinates agree. Let \(B_q(n)\) count distinct recovery-balanced subspaces of \(\mathbb F_q^n\) (not generator matrices).

The exact population is
\[
B_q(n)=\frac{(q-1)^n}{(q^2-1)(q^2-q)}
\sum_{\substack{2\le r\le q+1\\r\mid n}}
\binom{q+1}{r}\frac{n!}{((n/r)!)^r}.
\]
The sum is zero when it has no admissible divisor. The exact probability among nondegenerate \([n,2]_q\) codes (all coordinates are nonzero functions) is
\[
P_q^{\mathrm{nd}}(n)=
\frac{\displaystyle\sum_{\substack{2\le r\le q+1\\r\mid n}}
\binom{q+1}{r}\frac{n!}{((n/r)!)^r}}
{(q+1)^n-(q+1)}.
\]
The probability among *all* \([n,2]_q\) codes is
\[
P_q^{\mathrm{all}}(n)=\frac{(q-1)^n\displaystyle\sum_{\substack{2\le r\le q+1\\r\mid n}}\binom{q+1}{r}\frac{n!}{((n/r)!)^r}}
{(q^n-1)(q^n-q)}.
\]

For any \(n\) admitting an eligible divisor, define \(r_n=\max\{r:2\le r\le q+1,\ r\mid n\}\). For fixed \(q\), along such lengths with \(n\to\infty\),
\[
P_q^{\mathrm{nd}}(n)\sim
\binom{q+1}{r_n}\frac{r_n^{r_n/2}}{(2\pi n)^{(r_n-1)/2}}
\left(\frac{r_n}{q+1}\right)^n.
\]
In particular, if \(q+1\mid n\) the decay is polynomial of order \(n^{-q/2}\), while every eligible length not divisible by \(q+1\) lies in one of finitely many exponentially decaying subsequences. At lengths with no eligible divisor there are no recovery-balanced \([n,2]_q\) codes. The changing decay rate is an exact divisibility phenomenon, not a phase transition in field size.

## Assumptions and scope

A code is a two-dimensional linear subspace of \(\mathbb F_q^n\), with **labeled** coordinate positions. Two full-row-rank generator matrices specify the same code exactly when related by a left multiplier in \(\mathrm{GL}_2(\mathbb F_q)\). Sampling selects each position independently and uniformly from the \(n\) positions. For a generator column \(g_i\), its coordinate is recovered after the first draw for which \(g_i\) lies in the linear span of sampled columns; the expected draw count is \(E_i\). A zero generator column has \(E_i=0\).

The projective line \(\mathrm{PG}(1,q)\) has \(q+1\) nonzero column directions. For a code with no zero columns, let \(r\) be the number of occupied directions, with respective positive multiplicities \(a_1,\ldots,a_r\), summing to \(n\). Full row rank requires \(r\geq 2\). Codeword-coordinate recovery, rather than complete message recovery or a distinguished systematic information-coordinate problem, is the target.

## Proof

**1. Exact coordinate expectation.** Fix an occupied direction \(i\). Poissonize the discrete draws by attaching independent unit-rate exponential inter-arrival times. The arrival times for different sampled projective classes become independent exponential processes of respective rates \(a_j/n\). Poissonization preserves the expected number of draws: the independent unit-mean inter-arrival times sum to expected length equal to the expected stopping count. Since a direction \(i\) is spanned either by one sample from its own class or by samples from at least two *different* other classes, the event that it is unrecoverable at time \(t\) is the event that its class has not occurred and at most one other class has occurred.

Let \(p_j(t)=\exp(-a_jt/n)\). Independence gives
\[
\begin{aligned}
\Pr\{T_i>t\}
&=\prod_{j=1}^{r}p_j(t)
+\sum_{j\ne i}(1-p_j(t))\prod_{k\ne j}p_k(t)\\
&=\sum_{j\ne i}\exp\!\left[-(n-a_j)t/n\right]
-(r-2)\exp(-t).
\end{aligned}
\]
Integration over \(t\geq 0\) therefore yields
\[
E_i=n\sum_{j\ne i}\frac1{n-a_j}-(r-2)
=\left(n\sum_{j=1}^{r}\frac1{n-a_j}-(r-2)\right)-\frac n{n-a_i}.
\]
All denominators are positive because \(r\geq 2\). The map \(a\mapsto n/(n-a)\) is strictly increasing on \((0,n)\). Hence the \(E_i\) are equal exactly when all positive multiplicities \(a_i\) are equal. A code containing both a zero and a nonzero column cannot be balanced because the former has zero expected recovery and the latter positive expected recovery. Thus the complete structural characterization is: **there are no zero columns, and all occupied projective directions occur equally often**. Equal multiplicity means \(r\mid n\). (For such a code the common expectation is \(2\), consistently with the general expected-recovery identity.)

**2. Counting matrices and codes.** Fix an eligible \(r\). There are \(\binom{q+1}{r}\) choices of occupied directions and \(n!/((n/r)!)^r\) ways to distribute their directions over labeled columns. Every nonzero column in a chosen direction has \(q-1\) choices of scalar, independently. Therefore there are
\[
\binom{q+1}{r}\frac{n!}{((n/r)!)^r}(q-1)^n
\]
full-rank generator matrices with that number of directions. Different \(r\) are disjoint. The left action of \(\mathrm{GL}_2(\mathbb F_q)\) is free on full-row-rank matrices and its order is \((q^2-1)(q^2-q)\), so quotienting gives the formula for \(B_q(n)\). There is no hidden division by coordinate permutations: the coordinates remain labeled.

There are exactly \((q^2-1)^n-(q+1)(q-1)^n\) ordered rank-two generator matrices with no zero columns: from all nonzero columns, subtract sequences that lie on one projective line. Equivalently, their number of codes is this expression divided by the order of \(\mathrm{GL}_2\). Dividing \(B_q(n)\) by that count and using \(q^2-1=(q-1)(q+1)\) proves \(P_q^{\mathrm{nd}}(n)\). There are \((q^n-1)(q^n-q)\) ordered full-rank \(2\times n\) matrices, giving \(P_q^{\mathrm{all}}(n)\).

**3. Arithmetic asymptotics.** Stirling's formula applied to each fixed integer \(r\geq2\) gives
\[
\frac{n!}{((n/r)!)^r}
=\frac{r^{n+r/2}}{(2\pi n)^{(r-1)/2}}\left(1+O_r(n^{-1})\right)
\]
whenever \(r\mid n\). At fixed \(q\), the eligible \(r\) belong to the finite set \(\{2,\ldots,q+1\}\). The term with largest eligible \(r=r_n\) dominates every smaller eligible term by an exponentially small factor (uniformly in the finite set of possible \(r_n\)). Furthermore, \((q+1)^n-(q+1)\sim(q+1)^n\). Substitution proves the stated equivalent along all eligible lengths. If \(q+1\mid n\), then \(r_n=q+1\) and its exponential factor is one. If \(q+1\nmid n\), then \(r_n/(q+1)<1\) whenever an eligible divisor exists. This proves all asymptotic cases.

## Verification

A standalone exact-arithmetic verifier, `verify.py`, compares the derived Poissonized formula with an independent subset-spanning recovery identity for every occupied projective profile at binary lengths \(2\)–\(8\) and ternary lengths \(2\)–\(6\). It independently enumerates every ordered generator matrix over prime fields \(\mathbb F_2\) through length \(7\), \(\mathbb F_3\) through length \(5\), and \(\mathbb F_5\) through length \(4\). Counts are divided by the exact general-linear-group order and checked against the closed formulas. In particular, \(B_2(6)=25\), \(B_3(4)=20\), and \(B_5(4)=240\). The asymptotic leading term is also compared with the finite exact rational count on selected larger dimensions. The recorded execution ends with `RANK2_BALANCE_VERIFY_OK`.

These are finite verification checks only; the all-prime-power and all-length results follow from the preceding proofs. The finite-field generator-matrix enumeration portion of `verify.py` uses modular arithmetic for **prime** fields, not arbitrary extension fields, which are covered mathematically.

## Relationship to prior work

Gruica, Bar-Lev, Ravagnani and Yaakobi introduced coordinate recovery balance and derived general exact recovery formulas [1]. The August 2026 study of generalized random access by Gruica, Petrillo and Zullo [5] develops finite-geometric expectation and symmetry methods for information-coordinate recovery. The later October 2026 matroidal treatment of Bar-Lev, López, Matthews and Salizzoni [2] proves preservation under matroid duality and studies the prevalence of balance in unrestricted sparse-paving matroids, expressly distinguishing that population from finite-field representable matroids. The general expectation identities in [1,2] subsume the probabilistic starting point of the present proof. Rank-two individual-coordinate expectation expressions are also closely related to the information-coordinate special cases in [3]. None of those identities is claimed as a new general formula here.

The contribution is the field-uniform **census of distinct rank-two balanced codes**, including zero-column exclusion, the exact nondegenerate and unconditional proportions, and their divisor-sensitive polynomial-versus-exponential asymptotics. An existing rank-two full-message coverage-depth result [4] optimizes a different objective and is not a recovery-balance census. The present classification is much narrower than a general-rank theorem and is an elementary consequence of rank-two dependence structure; the explicit code population and oscillating rarity law provide its quantitative content.

## Limitations

Only dimension-two linear codes, uniform noiseless replacement sampling, and labeled coordinates are treated. The theorem concerns the fraction of code subspaces, not the fraction of matroid isomorphism classes or code equivalence classes under coordinate permutation/scaling. It does not establish asymptotic prevalence for fixed dimension three or higher, for variable field size, or for sparse-paving representable matroids. Novelty cannot be inferred from unsuccessful searches; an implicit equivalent enumeration in earlier matroid enumeration or coding work remains possible. Independent mathematical audit has not been performed.

## References

[1] A. Gruica, D. Bar-Lev, A. Ravagnani, and E. Yaakobi, *A Combinatorial Perspective on Random Access Efficiency for DNA Storage*, arXiv:2401.15722 (2024).

[2] D. Bar-Lev, H. H. López, G. L. Matthews, and F. Salizzoni, *A Matroidal Framework for Random Access in Linear Codes*, arXiv:2610.28820v1, first publicly posted 2026-10-20. https://arxiv.org/html/2610.28820v1

[3] E. Boruchovsky, O. Elishco, R. Gabrys, A. Gruica, I. Tamo, and E. Yaakobi, *Making it to First: The Random Access Problem in DNA Storage*, arXiv:2501.12274 (2025).

[4] *Exact rank-two optimum for DNA coverage depth*, publicly indexed mathematical research record, the title *Exact rank-two optimum for DNA coverage depth* (2026). Comparison is limited to the accessible abstract-level record; it addresses full-message retrieval, not coordinate-wise balance.

[5] A. Gruica, A. Petrillo, and F. Zullo, *The Generalized Random Access Problem for Linear Codes*, arXiv:2608.20152v1, first publicly posted 2026-08-20, Section 3 and Section 7. https://arxiv.org/html/2608.20152v1
