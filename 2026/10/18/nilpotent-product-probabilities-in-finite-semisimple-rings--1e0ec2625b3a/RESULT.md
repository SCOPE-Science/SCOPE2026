# Nilpotent product probabilities in finite semisimple rings

## Finding
For any nonzero finite semisimple ring \(R\), choose a Wedderburn decomposition
\[
R\cong\prod_{i=1}^{s}M_{n_i}(\mathbb F_{q_i}),
\qquad s\ge1,\quad n_i\ge1,
\]
where each \(q_i\) is a prime power. For each integer \(m\ge1\), let \(X_1,\ldots,X_m\) be independent uniformly sampled elements of \(R\). The exact nilpotent-product probability is
\[
\boxed{\Pr(X_1\cdots X_m\text{ is nilpotent})
=\prod_{i=1}^{s}\bigl[1-(1-q_i^{-n_i})^m\bigr].}
\]
The central single-block identity is
\[
\Pr(A_1\cdots A_m\text{ is nilpotent in }M_n(\mathbb F_q))
=1-(1-q^{-n})^m.
\]
For \(m=2\), this is \((2q^n-1)/q^{2n}\). Remarkably, the entire \(m\)-fold nilpotent-product probability sequence for \(M_n(\mathbb F_q)\) coincides with the \(m\)-fold *zero*-product probability in the commutative field \(\mathbb F_{q^n}\), for all \(m\). Hence the analogous coincidence holds between \(R\) and \(\prod_i\mathbb F_{q_i^{n_i}}\).

## Assumptions and scope
Every ring in the statement is finite, associative, unital, nonzero, and semisimple; all random choices are independent and uniform. A matrix is nilpotent if some positive power is zero. In dimension \(n\), this is equivalent to its \(n\)-th power being zero. For a direct product, a tuple is nilpotent exactly when each coordinate is nilpotent. The integer \(m\) counts factors, not a nilpotency index. The empty-product/trivial-zero-ring case is excluded.

## Proof
**Lemma 1 (nilpotent endomorphism count).** For every prime power \(q\) and integer \(r\ge0\), the number \(N_r\) of nilpotent linear maps on \(\mathbb F_q^r\) is \(q^{r^2-r}\), with \(N_0=1\). To prove this, put \(G_r=|\operatorname{GL}_r(\mathbb F_q)|\), \(G_0=1\). Fitting decomposition uniquely expresses each endomorphism of an \(r\)-space as a direct sum of a nilpotent operator on a \(j\)-space and an invertible operator on its invariant complement. There are \(G_r/(G_jG_{r-j})\) ordered complementary subspace pairs of dimensions \(j,r-j\). Summing over \(j\) gives
\[
q^{r^2}=\sum_{j=0}^r\frac{G_r}{G_jG_{r-j}}N_jG_{r-j}
=G_r\sum_{j=0}^r\frac{N_j}{G_j}.
\]
Write \(F_r=q^{r^2}/G_r=\prod_{k=1}^r(1-q^{-k})^{-1}\), and \(F_0=1\). Subtracting the preceding identity at dimensions \(r\) and \(r-1\) yields, for \(r\ge1\),
\[
\frac{N_r}{G_r}=F_r-F_{r-1}=q^{-r}F_r,
\quad\text{so}\quad N_r=q^{r^2-r}.
\]
In particular a uniform \(r\)-square matrix is nilpotent with probability \(q^{-r}\).

**Lemma 2 (conditional rank law).** Fix \(C\in M_n(\mathbb F_q)\) of rank \(r\). For independent uniform \(B\in M_n(\mathbb F_q)\),
\[
\Pr(CB\text{ is nilpotent}\mid C)=q^{-r}.
\]
Choose invertible matrices \(P,Q\) with \(C=P\operatorname{diag}(I_r,0)Q\). The conjugate \(P^{-1}CBP=\operatorname{diag}(I_r,0)\,(QBP)\) has block form
\[
\begin{pmatrix}T&U\\0&0\end{pmatrix},
\]
with \(T\) uniform in \(M_r(\mathbb F_q)\). This block matrix is nilpotent if and only if \(T\) is nilpotent: powers restrict to powers of \(T\) in the upper-left block, while nilpotent \(T\) makes the full matrix nilpotent at most one power later. Lemma 1 gives \(q^{-r}\), including \(r=0\).

**The matrix law.** For \(m=1\) it is Lemma 1 with \(r=n\). For \(m\ge2\), set \(C=A_1\cdots A_{m-1}\) and take an independent uniform column vector \(v\in\mathbb F_q^n\). Since for every fixed \(C\),
\[
\Pr(Cv=0\mid C)=\frac{|\ker C|}{q^n}=q^{-\operatorname{rank}C},
\]
Lemma 2 and the tower property show
\[
\Pr(A_1\cdots A_m\text{ nilpotent})=\Pr(A_1\cdots A_{m-1}v=0).
\]
Read the latter product's action on \(v\) from right to left. The starting vector is nonzero with probability \(1-q^{-n}\). For each fixed nonzero column \(w\), an independent uniform matrix \(A\) sends \(w\) uniformly to \(\mathbb F_q^n\), since its evaluation map is a surjective linear map with equal-size fibers. Thus each subsequent multiplication preserves a nonzero vector with conditional probability \(1-q^{-n}\), whereas zero is absorbing. After \(m-1\) matrix multiplications, survival probability is \((1-q^{-n})^m\). Its complement is the asserted nilpotent-product probability.

**Semisimple extension.** The Wedderburn–Artin theorem expresses every finite semisimple ring as a product of full matrix rings over finite division rings; the finite division rings are fields. Under uniform independent sampling, coordinate processes for different factors are independent. A coordinatewise product is nilpotent exactly when every factor product is nilpotent. Multiplying the single-block probabilities proves the displayed formula.

Finally, in the field \(\mathbb F_{q^n}\), a product of \(m\) elements is zero exactly when at least one factor is zero. That probability is \(1-(1-q^{-n})^m\), proving the coincidence.

## Verification
The enclosed standalone Python checker `verification/verify_nilpotent_products.py` performs exhaustive *weighted product enumeration* over four small prime-field matrix rings, checking nilpotency by the actual matrix power rather than the rank lemma. Its captured run is `verification/exhaustive_counts.txt`. Counts of matrices and factors are finite and exhaustive for each tested \((n,q,m)\):

| \(n\) | \(q\) | \(m\) | Nilpotent products | All ordered tuples | Probability |
|---|---|---|---:|---:|---:|
| 2 | 2 | 2 | 112 | 256 | \(7/16\) |
| 2 | 3 | 2 | 1377 | 6561 | \(17/81\) |
| 3 | 2 | 2 | 61440 | 262144 | \(15/64\) |
| 3 | 2 | 3 | 44302336 | 134217728 | \(169/512\) |

The checker also verifies \(m=1,2,3,4\) in the specified small dimensions. These are finite consistency tests; the dimension- and field-uniform claim follows from Lemmas 1–2 and the vector-survival argument, not extrapolation.

## Relationship to prior work
Sarma and Subedi [1] introduced nilpotent product probability for two random finite-ring elements and obtained structural bounds, complete results for commutative rings, and formulas for upper-triangular and scalar-upper-triangular matrix subrings. Their Theorem 2.24, read in full, treats triangular subrings, not arbitrary full matrix rings. Their Proposition 2.2 proves a direct-product rule for two factors; the noncommutative full-matrix exact law and arbitrary product lengths above are separate inputs. The field-values in their table do not identify all noncommutative rings that can share those probabilities.

The classical theorem counting nilpotent matrices, stated and proved in Leinster [2] and originally due to Fine–Herstein [3], gives only the \(m=1\) case. Here its combination with a *conditional-rank* lemma yields an all-length product law. The earlier matrix-factorization results [4,5] enumerate constrained idempotent–nilpotent products or torsion-unit-plus-nilpotent *sums*. Their full statements do not imply the probability that a product of unrestricted independent matrices is nilpotent; no factor in this theorem is required to be idempotent, nilpotent, or invertible. Conversely, these more specialized factorization counts cannot be recovered from the single aggregate probability given here.

## Limitations
The argument applies to uniform independent factors; it does not establish the same probability for correlated or nonuniform factors. The semisimplicity assumption is essential to the displayed decomposition; the statement makes no claim about finite rings with a nonzero Jacobson radical. Exact code tests are restricted to prime fields and small dimensions, while the proof covers all prime powers. The searches found no stronger source encompassing the all-length full-matrix formula, but unindexed or unpublished enumeration literature remains a residual originality risk.

## References
1. D. Sarma and T. Subedi, *Nilpotent Product Probability of Finite Rings*, arXiv:2610.07892v1 (first posted 6 October 2026), especially Proposition 2.2 and Theorem 2.24. https://arxiv.org/pdf/2610.07892
2. T. Leinster, *The probability that an operator is nilpotent*, arXiv:1912.12562v2 (2020), especially Theorem 5. https://arxiv.org/pdf/1912.12562
3. N. J. Fine and I. N. Herstein, *The probability that a matrix be nilpotent*, Illinois Journal of Mathematics 2 (1958), 499–504; cited as the original count in [2].
4. *Exact fibers of idempotent–nilpotent factorizations in two dimensions*, published mathematical finding (2026), specifically its Finding and Proof for constrained products.
5. *Exact t-fine decomposition multiplicities for two-by-two finite-field matrices*, published mathematical finding (2026), specifically its Finding and Proof for additive decompositions.
