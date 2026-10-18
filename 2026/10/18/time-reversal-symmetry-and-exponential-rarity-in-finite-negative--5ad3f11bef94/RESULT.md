# Time-reversal symmetry and exponential rarity in finite negative-tense Heyting chains

## Finding
For each integer \(n\ge1\), fix the \((n+1)\)-element Gödel chain and uniformly select a negative-tense Heyting expansion with operators \(g,h,f,p\). Let \(T_n\) be the total count and \(Q_n\) the count obeying \(g=h\) and \(f=p\). Then
\[
Q_n\le 1+4^n,\qquad T_n\ge1+C_n^2,\qquad C_n=\frac{1}{n+1}\binom{2n}{n}.
\]
Therefore
\[
\Pr(g=h\ \text{and}\ f=p)\le\frac{1+4^n}{1+C_n^2}=O\!\left(\frac{n^3}{4^n}\right).
\]
More precisely, each nonempty time-symmetric dual relation is uniquely the complement of a **transpose-invariant northwest Ferrers shape and a transpose-invariant southeast co-Ferrers shape** subject to the row-interval admissibility conditions below. The empty relation contributes one additional expansion.

## Assumptions and scope
The base Heyting algebra is the fixed totally ordered set of \(n+1\) elements, and expansions satisfy axioms (T1)–(T8) of Almiñana, Pelaitay and Zuluaga. Its finite Esakia dual is the ordered set \(X_n=\{0,\ldots,n-1\}\). The published tense-space representation identifies every expansion with a unique relation \(R\subseteq X_n^2\); its four operators are formed from row and column relational universal/existential tests. It identifies \((g,h,f,p)\) with the operators of \(R\) and \((h,g,p,f)\) with those of \(R^\mathsf T\). Uniqueness implies time-reversal symmetry if and only if \(R=R^\mathsf T\).

An admissible nonempty relation has, for each \(i\in X_n\), the nonempty row interval \(R(i)=\{j:\ell_i\le j\le u_i\}\), with \(\ell_0\ge\cdots\ge\ell_{n-1}=0\), \(n-1=u_0\ge\cdots\ge u_{n-1}\), \(\ell_i\le u_i\), and \(\ell_i\le u_{i+1}+1\) for \(0\le i<n-1\). This form follows directly by expressing the four tense-space upset-preservation conditions on the finite chain: row and column lower/upper thresholds must be monotone; the adjacent inequality is equivalent to having no empty column. The empty relation separately satisfies the conditions.

## Proof
**Corner-shape decomposition.** For a nonempty admissible relation, define
\[
L=\{(i,j):j<\ell_i\},\qquad U=\{(i,j):j>u_i\}.
\]
Then \(X_n^2\setminus R=L\mathbin{\dot\cup}U\). Since the endpoint sequences are nonincreasing, \(L\) is a northwest Ferrers order ideal in the product grid and \(U\) is a southeast co-Ferrers order filter. Both are disjoint and every row of their complement is a nonempty interval.

Suppose \(R=R^\mathsf T\). If \((i,j)\in L\), put \(k=\ell_i>j\). Since \((i,k)\in R\), symmetry gives \((k,i)\in R\), so \(u_k\ge i\). Monotonicity and \(j<k\) imply \(u_j\ge u_k\ge i\); hence \((j,i)\notin U\). But \((j,i)\notin R\) by symmetry, so \((j,i)\in L\). Thus \(L=L^\mathsf T\). Likewise if \((i,j)\in U\), let \(k=u_i<j\). Symmetry gives \((k,i)\in R\), hence \(\ell_k\le i\). Since \(k<j\), monotonicity gives \(\ell_j\le\ell_k\le i\). Therefore \((j,i)\notin L\), and symmetry places \((j,i)\in U\); thus \(U=U^\mathsf T\). Conversely, if both corner shapes are transpose invariant, so is their complement \(R\). This is the claimed if-and-only-if normal form, together with the displayed admissibility constraints.

**Upper bound.** A self-conjugate Ferrers shape in an \(n\times n\) grid has distinct diagonal hook lengths chosen from \(1,3,\ldots,2n-1\) via Frobenius coordinates. There are exactly \(2^n\) such shapes, including the empty shape. Transpose-invariant southeast co-Ferrers shapes have the same count after a half-turn. Every nonempty symmetric relation determines one compatible pair of those shapes, so at most \(2^n\cdot2^n=4^n\) choices occur. Adding the empty relation proves \(Q_n\le1+4^n\).

**Lower bound for all expansions.** Independently choose a weakly nonincreasing integer sequence \(\ell_i\) with \(0\le\ell_i\le n-1-i\), and a weakly nonincreasing sequence \(u_i\) with \(n-1-i\le u_i\le n-1\). Each family has \(C_n\) members by the standard staircase lattice-path/Catalan bijection. Every paired choice satisfies \(\ell_{n-1}=0\), \(u_0=n-1\), \(\ell_i\le u_i\), and \(\ell_i\le n-1-i\le u_{i+1}+1\). Hence the \(C_n^2\) paired interval-row relations are all distinct admissible nonempty relations. Add the empty relation to conclude \(T_n\ge1+C_n^2\).

Finally Stirling's formula yields \(C_n\sim4^n/(\sqrt\pi\,n^{3/2})\), so the displayed ratio is \(O(n^3/4^n)\), as claimed.

## Verification
The included standalone standard-library script `verify.py` checks the exact admissible and time-symmetric counts through \(n=8\), enumerates all binary relations directly for \(1\le n\le4\) and compares the tense-space upset conditions to the interval-row characterization, and independently enumerates unary operator pairs satisfying the time-symmetric forms of axioms (T1)–(T8) on Gödel chains through \(n+1=6\) elements. All checks produce `VERIFY_OK`. The total counts for \(1\le n\le8\) are \(2,5,30,267,2763,31005,367286,4526471\); the corresponding time-symmetric counts are \(2,5,14,47,167,611,2270,8519\). These are finite cross-checks, not substitutes for the unrestricted proof.

## Relationship to prior work
The general negative-tense definitions, representation and duality are due to Almiñana, Pelaitay and Zuluaga (2022 preprint). Finite-chain interval parametrizations provide a broader description of **all** such expansions. The present statement isolates the time-reversal-fixed subfamily, proves its two-self-conjugate-Ferrers structural criterion and establishes an exponential upper bound on its proportion. The displayed initial numbers also coincide with an existing integer sequence, OEIS A026641, after aligning indices; numerical coincidence is not claimed as new enumeration, nor is an unproved all-indices sequence identity asserted.

## Limitations
The exponential upper bound is not an exact asymptotic equivalent. The argument does not give a closed form for \(Q_n\); it shows an injection into pairs of self-conjugate shapes, not surjectivity onto every pair. Uniformity refers to distinct labeled expansions of one fixed finite chain, not to unlabelled structures or arbitrary underlying Heyting algebras. Published combinatorial interpretations of the matching integer sequence may contain equivalent descriptions, and prior general endpoint classifications reduce the strength of any priority claim. No independent audit has been performed.

## References
1. F. Almiñana, G. Pelaitay and W. Zuluaga, *On Heyting algebras with negative tense operators*, arXiv:2212.14756, initially public 2022-12-23, https://arxiv.org/abs/2212.14756.
2. OEIS Foundation, *A026641*, https://oeis.org/A026641 (prior numerical data and interpretations).
