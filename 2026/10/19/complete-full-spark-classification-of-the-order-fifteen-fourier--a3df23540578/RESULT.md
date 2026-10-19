# Complete full-spark classification of the order-fifteen Fourier frame

## Finding

Let \(G=\mathbb Z/15\mathbb Z\), let \(\omega=\exp(2\pi i/15)\), and let \(F=(\omega^{rc})_{r,c\in G}\) be the unnormalized Fourier matrix. Given any nonempty proper subset \(M\subset G\) with \(k=|M|\), let \(F[M,G]\) denote its \(k\)-by-\(15\) row restriction. It is **full spark** when every square \(k\)-by-\(k\) submatrix \(F[M,C]\), with \(C\subset G\) and \(|C|=k\), is invertible.

**Theorem.** The frame \(F[M,G]\) is full spark if and only if both conditions hold:

1. For each \(d\in\{3,5\}\), the cardinalities \(|\{r\in M:r\equiv j\pmod d\}|\), over \(j\in\{0,\ldots,d-1\}\), differ by at most one.
2. Neither \(M\) nor \(G\setminus M\) is an affine image of one of the following five exceptional sets under \(r\mapsto ar+b\), where \(\gcd(a,15)=1\):

\[
\begin{aligned}
E_1&=\{0,1,2,4,8\},\\
E_2&=\{0,1,2,3,4,5,8\},\\
E_3&=\{0,1,2,3,4,6,8\},\\
E_4&=\{0,1,2,3,4,7,11\},\\
E_5&=\{0,1,2,3,7,9,11\}.
\end{aligned}
\]

There are exactly \(2310\) full-spark nonempty proper row subsets. The full \(15\)-row matrix is itself invertible. An important nonmonotone phenomenon is that divisor balance suffices for all sizes at most four, fails for one affine orbit of five-row sets, suffices again for all six-row sets, and fails for four seven-row orbits (and their complements).

## Assumptions and scope

All row and column indices are distinct elements of \(G\). There are no weights, perturbations, or numerical thresholds. The result holds for the exact complex fifteenth root \(\omega\); changing the Fourier sign conjugates the matrix and does not affect spark. A row set is considered without ordering. Affine equivalence means \(M'=aM+b\) as subsets of \(G\), with \(a\in G^\times\). The zero-row case is excluded; the complete \(15\)-row matrix is treated separately.

The balanced-row census, organized by \(k=1,2,3,4,5,6,7\), is

| \(k\) | Total row sets | Balanced row sets | Full-spark row sets | Balanced affine orbits |
|---:|---:|---:|---:|---:|
| 1 | 15 | 15 | 15 | 1 |
| 2 | 105 | 60 | 60 | 1 |
| 3 | 455 | 60 | 60 | 1 |
| 4 | 1365 | 180 | 180 | 2 |
| 5 | 3003 | 90 | 60 | 2 |
| 6 | 5005 | 180 | 180 | 2 |
| 7 | 6435 | 930 | 600 | 10 |

For larger proper sizes, take the complement: the full-spark counts for \(k=8,\ldots,14\) are \(600,180,60,180,60,60,15\).

## Proof

**1. Necessity of balanced residue classes.** The general necessary direction in Alexeev–Cahill–Mixon [1, Theorem 9, proof] applies to every composite order, not only prime powers: if a selected row set is not uniformly distributed over the residue classes modulo some divisor \(d\mid15\), a square Fourier submatrix can be selected with linearly dependent columns. Their proof partitions rows and columns into quotient-coset blocks of rank one and bounds the total rank by \(k-1\). For \(15\), only the nontrivial proper divisors \(3\) and \(5\) are relevant. Thus condition (1) is necessary.

**2. Reduction to affine classes of at most seven rows.** Translating row indices by \(b\) multiplies each Fourier column by a nonzero scalar; multiplying rows by a unit \(a\) permutes the columns. Neither operation changes vanishing of maximal minors. Because the full Fourier matrix is invertible and scalar-unitary, Jacobi's complementary-minor identity shows that \(F[M,C]\) is singular if and only if \(F[G\setminus M,G\setminus C]\) is singular. Therefore full spark is invariant under complement, and it suffices to classify sets of size \(1\le k\le7\) up to affine equivalence.

**3. Exhaustive balanced-orbit census.** The included `order15_fullspark_checker.py` enumerates every one of the \(\binom{15}{k}\) row sets for each \(1\le k\le7\), tests balance mod \(3\) and \(5\), and computes the lexicographically first member of every orbit under the \(8\cdot15\) affine maps. The orbit representatives passing balance number \(1,1,1,2,2,2,10\), respectively. This loop is exhaustive, with no probabilistic sampling or floating-point arithmetic.

**4. Exact singular witnesses for the five exceptional affine classes.** For each row set \(R\) below, the indicated \(C\) has equal cardinality and a zero determinant:

| Exceptional \(R\) | Witness columns \(C\) |
|---|---|
| \(\{0,1,2,4,8\}\) | \(\{0,1,2,7,10\}\) |
| \(\{0,1,2,3,4,5,8\}\) | \(\{0,1,3,6,9,11,12\}\) |
| \(\{0,1,2,3,4,6,8\}\) | \(\{0,1,2,5,6,11,12\}\) |
| \(\{0,1,2,3,4,7,11\}\) | \(\{0,1,2,4,5,8,10\}\) |
| \(\{0,1,2,3,7,9,11\}\) | \(\{0,1,2,3,5,8,12\}\) |

Indeed, for each pair the determinant expansion

\[
D_{R,C}(X)=\sum_{\sigma\in S_k}\operatorname{sgn}(\sigma)
X^{\sum_{j=1}^{k}r_jc_{\sigma(j)}\bmod15}
\]

has **all fifteen integer coefficients zero** in \(\mathbb Z[X]/(X^{15}-1)\). The checker independently builds these coefficient vectors by an exact permutation recursion, tests every coefficient, and does not merely test a floating-point evaluation. Substitution \(X=\omega\) therefore proves singularity exactly.

**5. Exhaustive nonvanishing certificates for all remaining balanced classes.** For every other balanced orbit representative \(R\), the checker enumerates all \(\binom{15}{k}\) column sets \(C\) of the matching size. It evaluates \(\det(\zeta^{rc})\) by exact finite-field elimination, first for \((p,\zeta)=(31,7)\), then, only if zero, for \((p,\zeta)=(61,12)\). Both \(7\pmod{31}\) and \(12\pmod{61}\) have multiplicative order exactly \(15\). They are therefore roots of \(\Phi_{15}(X)\) in their respective prime fields. If the characteristic-zero determinant vanished at a primitive complex fifteenth root, its integer determinant polynomial would be divisible by \(\Phi_{15}\) and would vanish in **both** prime-field specializations. Thus nonzero determinant in either field rigorously certifies nonzero determinant over \(\mathbb C\).

There are \(54{,}928\) such maximal minors in the selected balanced orbit representatives. Exactly \(53{,}803\) are certified by the first field, and the remaining \(1{,}125\) by the second. No balanced representative outside the five displayed exceptions has a column minor vanishing in both fields. Consequently, every such representative is full spark. By step 2 this settles every balanced row set.

**6. Counts.** The certified counts \(15,60,60,180,60,180,600\) through seven rows sum to \(1155\). Complement symmetry doubles this number to \(2310\) nonempty proper full-spark row sets. This completes the classification. \(\square\)

## Verification

Run `python3 order15_fullspark_checker.py` with Python 3 and no external packages. The embedded checker reconstructs all affine row orbits, verifies the five exact zero-determinant identities coefficient by coefficient, and certifies every positive case by finite-field residues. Its reproducible expected final line is `PASS: finite exhaustive certificate without floating point.` The program prints all seven cardinality counts and the \(54{,}928\) nonvanishing certificate total. A separate independently written optimized modular implementation reproduced the same positive/negative orbit separation; the included checker contains the complete necessary reproduction paths.

The proof is finite and exhaustive: a modular nonzero is a mathematical witness, and an explicitly zero polynomial is an exact singularity certificate. The verifier does not infer nonvanishing from a failed numerical search or from a finite experiment about an infinite family.

## Relationship to prior work

Alexeev, Cahill, and Mixon [1] introduced the uniform-distribution condition, proved it necessary for arbitrary cyclic orders, proved sufficiency for prime-power orders, and gave a composite-order counterexample at order \(10\). These results establish the key balance obstruction but do **not** classify the first odd semiprime order \(15\) or its five exceptional affine orbits. Published complete classifications at other orders \(10\), \(12\), and \(14\), and a published general three-row criterion, do not imply the five- and seven-row classifications here; their different moduli or row cardinalities leave precisely the present cases open. Caragea and Lee [2] investigate *principal* Fourier minors (identical row and column sets); nonvanishing principal minors cannot guarantee full spark, which demands nonvanishing for all independent row/column choices. The exceptional witnesses above are nonprincipal and do not challenge a squarefree principal-minor conjecture.

## Limitations

The result is specific to Fourier order \(15\). It neither provides an arbitrary semiprime theorem nor condition-number estimates. Exhaustive finite-field arithmetic certifies nonzero complex determinants but says nothing quantitative about their smallest absolute values. The literature comparison did not uncover a prior complete order-fifteen classification, but an unidentified equivalent formulation in broader frame or uncertainty literature remains possible. No independent mathematical audit has been performed.

## References

[1] B. Alexeev, J. Cahill, and D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548 (first public version October 17, 2011), especially Definition 7, Theorem 9, and its proof, pp. 11–16. Journal of Fourier Analysis and Applications 18 (2012), 1167–1194.

[2] A. Caragea and D. G. Lee, *On the principal minors of Fourier matrices*, arXiv:2409.09793 (first posted September 15, 2024), especially Theorems 1.1–1.2 and Conjecture 1.3.
