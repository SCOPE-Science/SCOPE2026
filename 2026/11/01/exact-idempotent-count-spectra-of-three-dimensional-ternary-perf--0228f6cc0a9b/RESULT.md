# Exact idempotent-count spectra of three-dimensional ternary perfect evolution algebras

## Finding

Let \(E_W\) be the evolution algebra over \(\mathbb F_3\) with natural basis \(e_1,e_2,e_3\), with \(e_i e_j=0\) for \(i\ne j\) and \(e_i^2=\sum_{j=1}^3w_{ij}e_j\), where \(W=(w_{ij})\in\operatorname{GL}_3(\mathbb F_3)\). Let \(k(W)\) be the number of **nonzero** idempotents, and let \(s(W)\) indicate whether \(E_W\) is simple. These quantities are intrinsic to the algebra. The complete distributions are:

| Nonzero idempotents \(k\) | Labeled perfect matrices | Labeled simple matrices | Perfect isomorphism classes | Simple isomorphism classes |
|---:|---:|---:|---:|---:|
| 0 | 3600 | 3408 | 78 | 74 |
| 1 | 5056 | 3256 | 111 | 73 |
| 2 | 1800 | 768 | 40 | 17 |
| 3 | 600 | 72 | 15 | 2 |
| 4 | 120 | 0 | 3 | 0 |
| 5 | 48 | 0 | 1 | 0 |
| 6 | 0 | 0 | 0 | 0 |
| 7 | 8 | 0 | 1 | 0 |
| **Total** | **11232** | **7504** | **249** | **166** |

Thus the possible nonzero-idempotent counts among perfect algebras are exactly \(\{0,1,2,3,4,5,7\}\); **six is impossible**. Among simple perfect algebras the possibilities are exactly \(\{0,1,2,3\}\). In particular, a simple three-dimensional evolution algebra over \(\mathbb F_3\) has **at most three nonzero idempotents**, and \(3408/7504=213/469\) of the labeled simple perfect matrices have none. The exact probability of zero nonzero idempotents in the simple model is \(3408/7504=213/469\).

The aggregate number of isomorphism classes, \(249\), is **not claimed as new**: it follows from Wei and Zou's 2023 general isomorphism-class formula. The new refinement is the exact idempotent distribution, including the simple stratum and class-by-class counts.

## Assumptions and scope

All fields in the theorem are exactly \(\mathbb F_3\); all algebras have vector-space dimension exactly three. “Labeled” means a distinct \(3\times3\) structure matrix in the prescribed ordered natural basis. “Simple” is equivalent to invertibility of \(W\) and strong connectivity of the directed graph with arrow \(i\to j\) precisely when \(w_{ij}\ne0\). Zero is always an idempotent, but it is excluded from \(k(W)\). Isomorphism classes are for \(\mathbb F_3\)-linear algebra isomorphisms, not for merely permuting matrix entries.

## Proof

**Step 1 (support test).** Every \(x=(x_1,x_2,x_3)\in\mathbb F_3^3\) has \(x_i^2=0\) when \(x_i=0\), and \(x_i^2=1\) otherwise. For a subset \(S\subseteq\{1,2,3\}\), define
\[
 c_j(S)=\sum_{i\in S}w_{ij}\pmod3,\qquad j=1,2,3.
\]
The unique possible idempotent with support exactly \(S\) is \(x_j=c_j(S)\). It exists if and only if \(c_j(S)\ne0\) precisely for \(j\in S\). Necessity follows from the equations \(x_j=\sum_iw_{ij}x_i^2\); sufficiency follows because this support condition gives \(x_i^2=1\) precisely on \(S\). Thus each of the seven nonempty supports contributes zero or one idempotent, and
\[
 k(W)=\sum_{\varnothing\ne S\subseteq\{1,2,3\}}
 \prod_{j\in S}\mathbf1_{c_j(S)\ne0}
 \prod_{j\notin S}\mathbf1_{c_j(S)=0}.
\]
This exact finite formula is also a conceptual reduction of quadratic idempotent equations to support consistency in characteristic three over the prime field.

**Step 2 (complete finite matrix space).** There are exactly \(3^9=19683\) matrices over \(\mathbb F_3\), indexed by their nine entries. The standard determinant test identifies the \(11232\) invertible matrices (also \(\prod_{i=0}^2(27-3^i)=11232\)). For each matrix, evaluate all seven support conditions from Step 1. Count the matrices in each \(k\)-stratum and, separately, those whose directed nonzero pattern is strongly connected, using exact finite graph reachability. This is a finite exhaustion of a **specified complete search space**, not a sample or heuristic. The output is the first two columns of the table. The same matrix classes are independently tested by direct enumeration of all \(27\) vectors for the idempotent equations, a second nonsingularity test by elimination, and an independent breadth-first graph search. All outputs agree; see the embedded standalone `census.py` and its observed `census_output.txt`.

**Step 3 (isomorphism orbits).** A perfect evolution algebra has a natural basis unique up to permutation and nonzero rescaling, so in the row-square convention used here the \(48=3!\cdot2^3\) changes of basis act by
\[
 W'_{ij}=\varepsilon_j\,w_{\sigma(i),\sigma(j)}
 \quad(\sigma\in S_3,\;\varepsilon_j\in\{1,2\}\subset\mathbb F_3).
\]
Indeed, if \(e'_i=\varepsilon_i e_{\sigma(i)}\), then \((e'_i)^2=\varepsilon_i^2\sum_jw_{\sigma(i),\sigma(j)}e_{\sigma(j)}=\sum_j\varepsilon_j^{-1}w_{\sigma(i),\sigma(j)}e'_j\), and \(\varepsilon_j^{-1}=\varepsilon_j\) in \(\mathbb F_3\). Therefore these orbits are exactly algebra-isomorphism classes. The two invariants are constant on each orbit. For each matrix, the checker counts its stabilizer in this 48-element group; the number of orbits in each \(k\)-stratum is then the exact integer \(\frac1{48}\sum_W|\operatorname{Stab}(W)|\), with the sum restricted to that stratum. It independently obtains the same counts by enumerating the distinct orbit sets themselves. This proves the last two columns.

**Step 4 (witnesses and boundary checks).** Representatives of simple algebras with respectively \(0,1,2,3\) nonzero idempotents, written row-major, are
\[
(0,0,1;\ 0,1,1;\ 1,1,1),\quad
(0,0,1;\ 0,1,1;\ 1,1,0),
\]
\[
(0,0,1;\ 1,1,2;\ 0,1,1),\quad
(0,1,1;\ 1,1,2;\ 1,2,1).
\]
The semicolons separate rows. Substitution verifies that each is invertible, strongly connected, and has the stated count. The maximum \(k=7\) occurs at exactly eight invertible diagonal matrices: to have all three singleton supports produce idempotents, each row must have no off-diagonal entry, and conversely any invertible diagonal matrix has an idempotent on every support. The sum of the labeled counts is \(11232\), the isomorphism-class counts sum to \(249\), and the weighted first moment satisfies \(\sum_Wk(W)=11232\), recovering the previously known mean of one nonzero idempotent.

## Verification

Run `python3 census.py` using Python 3 with its standard library. The expected first line is `VERIFY_OK`, followed by the four complete histograms and witness matrices reproduced above. The standalone checker enumerates every \(3\times3\) matrix, compares the direct \(27\)-vector solution test with the independent seven-support test, compares determinant with Gaussian elimination, compares transitive closure with breadth-first reachability, and uses both stabilizer weights and disjoint orbit enumeration for the isomorphism-class counts. All assertions passed. No floating-point operations, random samples, outside data, or unproved infinite extrapolations enter the certificate.

## Relationship to prior work

Kaygorodov, Martín González and Viruel (2026, arXiv:2610.22248, Question 22 and Conjecture 2) ask about random evolution-algebra idempotent distributions and identify the mean-one law. Their large-field fixed-point heuristic is not an exact distribution at \(q=3\), and their survey does not give the refined counts here. Wei and Zou (2023, arXiv:2310.12368, Sections 1 and 5) determine the number of perfect evolution-algebra isomorphism classes in dimension three over finite fields and supply the monomial orbit description; the known total \(249\) is not part of the novelty claim. Hu (2026, preprint 202610.1039, Sections 1–5) analyzes full-support solutions and their exceptional complex locus, rather than the complete ternary finite-field distribution or the simple-subpopulation counts.

## Limitations

The scope is finite and exact: dimension three, base field \(\mathbb F_3\), perfect algebras. The theorem gives no classification over \(\mathbb F_{3^r}\) for \(r>1\), no large-field asymptotics, no arbitrary-dimension formula, and no proof of the generic Galois-group conjecture. Exact enumeration proves this finite statement but does not establish absolute literature priority. Earlier classifications could implicitly encode parts of these counts despite no identical statement found in the inspected texts.

## References

1. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248 (initial public date 2026-10-15), especially Section 2.2, Question 22, and Section 2.3, Conjecture 2. https://arxiv.org/abs/2610.22248
2. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, Linear Algebra and its Applications 675 (2023), 142–178; arXiv:2310.12368, especially Corollary 1.1 and Theorem 5.1. https://arxiv.org/html/2310.12368v1
3. X.-Y. Hu, *Full-Support Solutions and Rigidity for Three-Dimensional Evolution Algebras*, Preprints.org, version 2, posted 2026-10-15, identifier 202610.1039. https://www.preprints.org/manuscript/202610.1039
