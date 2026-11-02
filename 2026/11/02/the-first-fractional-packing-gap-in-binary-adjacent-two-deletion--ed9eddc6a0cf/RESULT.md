# The first fractional-packing gap in binary adjacent-two-deletion codes

## Finding

Let \(A_2(n)\) be the largest size of a binary length-\(n\) code correcting **exactly two consecutive deletions**, and let \(F_2(n)\) be the optimum of its standard fractional deletion-shadow packing linear program (definitions below). Then

\[
\bigl(A_2(2),\ldots,A_2(8)\bigr)=(1,2,4,4,8,13,20),
\qquad
\bigl(F_2(2),\ldots,F_2(8)\bigr)=(1,2,4,4,8,13,21).
\]

Thus \(n=8\) is the **first length at which the exact-two-adjacent-deletion shadow-packing relaxation has a strict integrality gap**. At length eight the full integral optimum is \(A_2(8)=20\), and the relaxed optimum is \(F_2(8)=21\). There is a strictly stronger rational conflict-clique upper bound \(482/23\) for the integral problem.

## Assumptions and scope

Words have fixed length \(n\), lie in \(\{0,1\}^n\), and are indexed from the left without cyclic wraparound. An error deletes precisely two neighboring symbols and nothing else; the deletion location is unknown, but the received length \(n-2\) is known. For a word \(x=x_0\cdots x_{n-1}\), define

\[
D_2(x)=\bigl\{x_0\cdots x_{i-1}x_{i+2}\cdots x_{n-1}:0\le i\le n-2\bigr\}.
\]

This is a **set**, so repeated received words from different deletion positions occur only once. A correcting code \(C\) is a subset of \(\{0,1\}^n\) satisfying \(D_2(x)\cap D_2(x')=\varnothing\) for distinct \(x,x'\in C\). Let \(X_n=\{0,1\}^n\) and \(Y_n=\{0,1\}^{n-2}\). The fractional program has nonnegative variables \(a_x\), for \(x\in X_n\), and constraints

\[
\sum_{x:y\in D_2(x)}a_x\le1\qquad(y\in Y_n),
\qquad F_2(n)=\max\sum_{x\in X_n}a_x.
\]

Its dual has nonnegative variables \(b_y\), subject to \(\sum_{y\in D_2(x)}b_y\ge1\) for each \(x\), and minimizes \(\sum_y b_y\).

## Proof

**Finite formulation.** By definition a correcting code has pairwise disjoint received-output sets. Its indicator vector is integral-feasible for the fractional program. Therefore an explicit feasible code lower-bounds \(A_2(n)\), while any dual feasible \(b\) upper-bounds \(A_2(n)\) as well as \(F_2(n)\).

**Lengths two through seven.** The accompanying `certificate.json` contains for each \(n=2,\ldots,7\) an explicit correcting code with \(1,2,4,4,8,13\) words respectively, and exact rational feasible primal and dual vectors of the same objective value. The accompanying dependency-free `verify.py` verifies each nonzero coefficient and every inequality directly from the definitions above, for **all** \(2^n\) source words and \(2^{n-2}\) output words. Thus both optima equal the stated values at these lengths.

**Length-eight lower bound.** The following twenty binary words form a correcting code:

`00000000`, `00000101`, `00001010`, `00001111`, `00100100`, `01010000`, `01010101`, `01011010`, `01011111`, `01110001`, `10001110`, `10100000`, `10100101`, `10101010`, `10101111`, `11011011`, `11110000`, `11110101`, `11111010`, `11111111`.

Their deletion shadows are pairwise disjoint, as independently checked by two explicitly implemented shadow computations in `verify.py`.

**Length-eight fractional value.** The certificate includes a rational fractional feasible packing of total value \(21\) and a feasible deletion-shadow dual cover of total weight \(21\). Checking all \(256\) word constraints and all \(64\) received-output constraints proves \(F_2(8)=21\).

**Length-eight integral upper bound.** The certificate additionally supplies \(77\) explicitly listed families \(K_j\subseteq X_8\), with positive rational weights \(c_j\). Every two distinct words of each \(K_j\) share at least one received output, so every correcting code \(C\) meets \(K_j\) in **at most one** word. For each of the \(256\) words \(x\), the certificate has \(\sum_{j:x\in K_j}c_j\ge1\), and the total weight satisfies

\[
\sum_{j=1}^{77}c_j=\frac{482}{23}<21.
\]

For any correcting code \(C\), summing the coverage inequalities over its words yields

\[
|C|\le\sum_{x\in C}\sum_{j:x\in K_j}c_j
=\sum_j c_j|C\cap K_j|\le\sum_jc_j
=\frac{482}{23}<21.
\]

Since \(|C|\) is integral, \(|C|\le20\). Together with the explicit twenty-word code this gives \(A_2(8)=20\). Its comparison with the certified fractional value and the equalities at lengths two through seven proves the first-gap statement.

## Verification

Run `python3 verify.py` in the directory containing `verify.py` and `certificate.json`. It requires only the Python standard library. The checker (i) independently forms all deletion shadows by strings and bit operations, (ii) tests the explicit code at each length, (iii) evaluates every rational primal and dual inequality with `fractions.Fraction`, (iv) tests all unordered pairs in all \(77\) cliques, (v) tests weighted coverage of all \(256\) length-eight words, and (vi) confirms the exact objective values and the strict inequality \(482/23<21\). Successful replay prints `VERIFY_OK`. Certificate verification is finite and exhaustive in precisely the stated parameter range; it is not an extrapolation to arbitrary lengths.

## Relationship to prior work

Levenshtein's early adjacent-deletion constructions supply the historical framework. Schoeny, Wachter-Zeh, Gabrys, and Yaakobi, first publicly posted February 22, 2016, define the same exact-burst model and prove the general nonasymptotic bound \((2^{n-b+1}-2^b)/(n-2b+1)\). Substituting \(n=8,b=2\) yields \(124/5=24.8\), hence at most \(24\) codewords—strictly weaker than the exact value \(20\). Their paper develops general constructions and an asymptotic analysis, not the certified small-length optimum or first fractional-integrality gap here. Ye and Ge (2026) study stronger substring-edit models and asymptotic constructions, without a matching exact length-eight benchmark in their inspected main results. No historical priority claim is inferred merely from failed search; an inaccessible older primary source remains a residual risk.

## Limitations

The claim is an exact finite theorem only for binary source lengths \(2\) through \(8\), a *single burst* of *exactly two consecutive deletions*, and the natural unweighted shadow-packing LP. It does not determine \(A_2(n)\) for \(n\ge9\), the number of optimal codebooks, or optimality for one-or-two deletions or arbitrary nonadjacent deletions. The proof is a reproducible finite rational certificate, not a short human-only classification. Historical originality has not received independent verification.

## References

1. C. Schoeny, A. Wachter-Zeh, R. Gabrys, and E. Yaakobi, *Codes Correcting a Burst of Deletions or Insertions*, first submitted February 22, 2016, [arXiv:1602.06820](https://arxiv.org/abs/1602.06820), especially Sections II and IV, Theorem 4.
2. Z. Ye and G. Ge, *Substring Edit Correcting Codes and Optimal Single Burst-Deletion Correcting Codes*, first submitted October 5, 2026, [arXiv:2610.05696](https://arxiv.org/abs/2610.05696), Sections I and VI.
3. V. I. Levenshtein, *Asymptotically optimum binary code with correction for losses of one or two adjacent bits*, 1967. Historical source referenced by Schoeny and collaborators; the primary full text was not available for a complete comparison.
