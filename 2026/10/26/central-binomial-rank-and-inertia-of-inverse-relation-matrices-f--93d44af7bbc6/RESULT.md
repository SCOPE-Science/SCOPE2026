# Central-binomial rank and inertia of inverse-relation matrices for monotone transformations

## Finding
For each integer \(n\geq 1\), let \(\mathcal O_n\) be the multiplicative monoid of all weakly order-preserving self-maps of the chain \([n]=\{1,\ldots,n\}\), with multiplication by composition. Its **mutual-inverse matrix** \(A_n\) has rows and columns indexed by \(\mathcal O_n\), with entry \(1\) for a pair \((f,g)\) satisfying both \(fgf=f\) and \(gfg=g\), and entry \(0\) otherwise. This is a real symmetric matrix; loops at idempotents are retained on its diagonal.

**Theorem.** The real inertia (number of positive, negative and zero eigenvalues, in that order) of \(A_n\) is exactly
\[
\left(\frac{\binom{2n-2}{n-1}+2^{n-1}}{2},\quad
\frac{\binom{2n-2}{n-1}-2^{n-1}}{2},\quad
\binom{2n-1}{n}-\binom{2n-2}{n-1}\right).
\]
In particular,
\[
\operatorname{rank}_{\mathbb R} A_n=\binom{2n-2}{n-1}.
\]
More precisely, if \(A_{n,r}\) denotes the principal block indexed by the maps of image size \(r\), for each \(1\le r\le n\), and
\[
 a=\binom{n-1}{r-1},\qquad b=\binom nr,
\]
then
\[
\operatorname{In}(A_{n,r})=\left(\frac{a(a+1)}2,\ \frac{a(a-1)}2,\ a(b-a)\right),
\qquad \operatorname{rank} A_{n,r}=a^2.
\]
All these statements concern the ordinary real adjacency matrix of the *mutual-inverse relation*, with its diagonal present, not a Laplacian or an idempotent-only graph.

## Assumptions and scope
The chain and maps are finite; \(n\ge1\) and \(1\le r\le n\) are integers. An inverse in the sense of semigroup theory satisfies the two identities above; it need not be a two-sided unit. There are \(\binom{2n-1}{n}\) elements of \(\mathcal O_n\). The inertia refers to real eigenvalues counted with multiplicity, and is independent of how the monoid elements are ordered. The result does **not** assert existence of an involution matching, nor does it calculate the individual nonzero eigenvalues.

## Proof
**1. Kernel blocks and image sets.** Each rank-\(r\) map \(f\) has a unique ordered partition \(B=(B_1,\ldots,B_r)\) of \([n]\) into nonempty *interval* blocks and an increasing image set \(I=\{y_1<\cdots<y_r\}\), with \(f(B_i)=\{y_i\}\). There are \(a=\binom{n-1}{r-1}\) possible interval partitions and \(b=\binom nr\) possible image sets. Let \(\mathcal P_{n,r}\) and \(\mathcal Q_{n,r}\) denote those two finite indexing sets.

Two such maps \(f=(B,I)\) and \(g=(C,J)\) are mutual inverses exactly when \(J\) meets each block of \(B\) in one point and \(I\) meets each block of \(C\) in one point. Indeed, the inverse identities force equal ranks, and the monotonicity of the maps forces the selected kernel blocks to be paired in increasing order. Conversely, under the two transversal conditions, \(g(y_i)\in B_i\) and \(f(J_i)=y_i\), so both inverse identities hold on each block.

**2. Transversal matrix.** Define the \(a\)-by-\(b\) zero-one matrix \(M\) by
\[
 M_{B,I}=\begin{cases}1&\text{if }|B_i\cap I|=1\text{ for all }i,\\0&\text{otherwise.}\end{cases}
\]
The previous paragraph gives the entry formula
\[
 (A_{n,r})_{(B,I),(C,J)}=M_{B,J}M_{C,I}.
\]
Upon identifying vectors with real \(a\)-by-\(b\) matrices \(X\), the corresponding linear operator is therefore
\[
 \mathcal A(X)=M X^{\mathsf T}M.
\]
This identity is an *exact* matrix factorization, not a numerical approximation.

**3. Full row rank of the interval-transversal matrix.** To every \(B\in\mathcal P_{n,r}\), associate the homogeneous squarefree polynomial
\[
 P_B(z_1,\ldots,z_n)=\prod_{i=1}^{r}\left(\sum_{j\in B_i}z_j\right).
\]
The coefficient vector of \(P_B\) in the degree-\(r\) squarefree monomial basis is exactly the row of \(M\) indexed by \(B\). We prove their linear independence by induction on \(n\), simultaneously for all admissible \(r\), over *any* field. For \(r=1\), there is just one nonzero polynomial. In a putative linear dependence for \(r\ge2\), set \(z_n=0\). The terms from partitions whose final block has at least two elements become the distinct polynomials \(P_{B^-}\) on \([n-1]\) with \(r\) blocks; the terms from partitions with final singleton \(\{n\}\) vanish. By induction the coefficients of all nonsingleton-final-block terms vanish. The remaining relation is \(z_n\) times a linear relation among the \(P_{B^-}\) with \(r-1\) blocks on \([n-1]\), so induction eliminates those coefficients too. When \(r=n\), only the final-singleton case occurs. Thus \(M\) has full row rank \(a\).

**4. Inertia of each rank block.** Take a real singular-value decomposition
\[
 M=U\,[D\ \ 0]V^{\mathsf T},\qquad D=\operatorname{diag}(\sigma_1,\ldots,\sigma_a),\quad \sigma_i>0.
\]
Here \(b\ge a\). In the orthonormal coordinates \(X=UYV^{\mathsf T}\), the operator \(\mathcal A\) annihilates the last \(b-a\) columns of \(Y\), and sends its initial square \(a\)-by-\(a\) block \(Y_0\) to \(D Y_0^{\mathsf T}D\). The diagonal matrix units have positive eigenvalues \(\sigma_i^2\). On each two-dimensional span of \(E_{ij}\) and \(E_{ji}\), with \(i<j\), the eigenvalues are \(\sigma_i\sigma_j\) and \(-\sigma_i\sigma_j\). Consequently there are \(a(a+1)/2\) positive, \(a(a-1)/2\) negative, and \(a(b-a)\) zero eigenvalues. The claimed rank-\(r\) formula follows.

**5. Global formula.** Mutual inverses necessarily have equal image size; hence \(A_n\) is permutation-similar to the direct sum of \(A_{n,r}\) for \(r=1,\ldots,n\). Vandermonde's identity gives
\[
 \sum_{r=1}^{n}\binom{n-1}{r-1}^{\!2}=\binom{2n-2}{n-1},
 \qquad \sum_{r=1}^{n}\binom{n-1}{r-1}=2^{n-1}.
\]
The total matrix size is \(\sum_r ab=\binom{2n-1}{n}\). Summing the rank-block inertia triples therefore gives exactly the displayed global inertia and central-binomial rank.

## Verification
The accompanying self-contained script `verify.py` enumerates the entire monoid for \(1\le n\le5\), checks all two-sided inverse identities against the transversal-matrix factorization, checks the rank of the transversal matrix by integer elimination, and verifies the derived degree and idempotent counts. It terminates with `VERIFY_OK`. The optional script `verify_eigensigns.py` builds the real matrix and numerically checks its eigenvalue signs for all rank strata through \(n=5\), returning `SPECTRAL_VERIFY_OK`; this requires NumPy and is corroboration only. The unlimited assertion rests on Steps 1–5, not these finite tests.

To reproduce the included check, run `python3 verify.py` from the directory containing this document and script. No third-party packages are needed for the included check.

## Relationship to prior work
The October 2026 paper by P. M. Higgins establishes the existence of permutation matchings for the full monoid \(\mathcal O_n\) using balanced weightings and semigroup structure matrices. The present assertion concerns a **different invariant**, namely the full real inertia and matrix rank of the mutual-inverse relation at every image rank. The existence of a permutation matching alone does not specify this inertia, and the present inertia formula alone does not supply an involution matching.

Higgins's 2024 paper discusses inverse-pair bipartite graphs and the then-open permutation-matching question for \(\mathcal O_n\). His 2019 work treats inverse matchings for related, but distinct, semigroups of orientation-preserving and orientation-reversing transformations. Existing inverse-degree calculations for isotone transformation monoids give scalar degree information but do not, merely by degree counts, determine the ranks or signs of eigenvalues of their inverse-relation adjacency matrices. The proof here uses a full-row-rank incidence lemma and a transpose-twisted matrix factorization instead.

## Limitations
The full text of Higgins's October 2026 preprint could not be accessed through the attempted preprint and open-access routes. Its publicly available abstract reports a balanced-weighting existence theorem but not the inertia values asserted here; nevertheless, undiscovered overlap within its full body remains a genuine priority risk. No assertion of absolute priority or independent validation is made. The theorem does not determine individual nonzero eigenvalues, spectral gaps, or the number of involution matchings.

## References
- P. M. Higgins, *Balanced weightings and permutation matchings applied to the monoid of order-preserving mappings*, arXiv:2610.01912v1, first posted 2026-10-01, https://arxiv.org/abs/2610.01912.
- P. M. Higgins, *Finite regular semigroups with permutations that map elements to inverses*, Semigroup Forum 109 (2024), 141–147, https://doi.org/10.1007/s00233-024-10430-0.
- P. M. Higgins, *Involution matchings, the semigroup of orientation-preserving and orientation-reversing mappings, and inverse covers of the full transformation semigroup*, Semigroup Forum 98 (2019), 669–689, https://doi.org/10.1007/s00233-019-10018-z.
- P. Catarino, P. M. Higgins, I. Levi, *On inverse subsemigroups of the semigroup of orientation-preserving or orientation-reversing transformations*, Algebra and Discrete Mathematics 19 (2015), 162–171, https://repository.essex.ac.uk/13220/.
