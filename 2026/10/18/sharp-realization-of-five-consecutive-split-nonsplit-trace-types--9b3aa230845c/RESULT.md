# Sharp realization of five consecutive split–nonsplit trace types

## Finding
Let \(p\) be an odd prime and let \(\chi_p\) be its quadratic character, with \(\chi_p(0)=0\). For \(j\in\{0,1,2,3,4\}\), set
\[
 f_j(t)=(t+j)^2-4\in\mathbb F_p[t].
\]
A sign word \(\varepsilon\in\{-1,1\}^5\) is *realized* if some \(t\in\mathbb F_p\) satisfies \(\chi_p(f_j(t))=\varepsilon_j\) for all five indices, with no zero discriminant. Every one of the \(32\) words is realized for **every odd prime \(p\ge239\)**. This is sharp: for \(p=233\), exactly one word is missing, namely \((-1,-1,-1,-1,-1)\).

The complete list of exceptional odd primes below the sharp threshold is
\[
\begin{gathered}
3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,\\
61,67,71,73,79,83,89,97,101,103,109,113,127,131,\\
139,149,157,163,173,179,181,223,227,233.
\end{gathered}
\]
All other odd primes below \(239\), including \(229\), realize every word.

## Assumptions and scope
For each trace \(u\in\mathbb F_p\), the characteristic polynomial of a determinant-one \(2\times2\) matrix with trace \(u\) is \(X^2-uX+1\), of discriminant \(u^2-4\). A nonzero-square discriminant gives two distinct eigenvalues over \(\mathbb F_p\) (regular split semisimple type); a nonsquare discriminant gives an irreducible quadratic (regular nonsplit semisimple type). Every trace is attained in \(\operatorname{SL}_2(\mathbb F_p)\), for example by the companion matrix of this polynomial. The assertion is about five *consecutive trace values* in the field, not about traces of powers of one fixed matrix or about simultaneous conjugacy of five chosen matrices.

The length \(5\) is the first consecutive window in which the discriminant polynomials share a zero over characteristic greater than \(8\): \(f_0\) and \(f_4\) share the root \(-2\). This first branch collision motivates the window rather than selecting an arbitrary numerical length.

## Proof
For any subset \(S\subseteq\{0,1,2,3,4\}\), put \(F_S(t)=\prod_{j\in S}f_j(t)\), and for \(\varepsilon\in\{-1,1\}^5\) set
\[
 Q_\varepsilon(t)=\prod_{j=0}^4(1+\varepsilon_j\chi_p(f_j(t))).
\]
Assume first \(p>8\). The zero sets of the five polynomials have union
\[
 R=\{2,1,0,-1,-2,-3,-4,-5,-6\},\qquad |R|=9.
\]
Outside \(R\), the product is \(32\) when the prescribed word occurs and is \(0\) otherwise. On \(R\), it lies between \(0\) and \(16\), since at least one factor equals \(1\) and every other factor is at most \(2\). Writing \(N_p(\varepsilon)\) for the number of realizations gives
\[
32N_p(\varepsilon)\ge\sum_{t\in\mathbb F_p}Q_\varepsilon(t)-144.
\tag{1}
\]
Expand the product. The empty subset contributes \(p\); the other \(31\) subsets contribute signed quadratic-character sums \(\sum_t\chi_p(F_S(t))\). If \(S\) does not contain both \(0\) and \(4\), then \(F_S\) has \(2|S|\) distinct simple roots. Its degree is \(2|S|\), it is not a square, and the classical quadratic Weil bound yields
\[
\left|\sum_t\chi_p(F_S(t))\right|\le(2|S|-1)\sqrt p.
\tag{2}
\]
There are exactly eight subsets containing both \(0\) and \(4\). For each, the single repeated factor \((t+2)^2\) can be removed, leaving a squarefree monic polynomial \(H_S\) of degree \(2|S|-2\). At \(t=-2\), removing that square changes the character value by at most \(1\), so the Weil bound instead gives
\[
\left|\sum_t\chi_p(F_S(t))\right|\le(2|S|-3)\sqrt p+1.
\tag{3}
\]
Summing the usual coefficients over all nonempty subsets gives
\[
\sum_{k=1}^5\binom5k(2k-1)=129.
\]
Accounting for the eight overlapping subsets subtracts \(16\) from the \(\sqrt p\) coefficient and adds at most \(8\) as an absolute correction. Applying these estimates to (1) yields, uniformly for every sign word,
\[
\boxed{32N_p(\varepsilon)\ge p-113\sqrt p-152.}\tag{4}
\]
This is strictly positive for \(p\ge14000\): at \(14000\), the right side is positive, and its derivative with respect to the real parameter is \(1-113/(2\sqrt p)>0\) in this range. Thus all words occur at all primes above the finite-search range.

For all odd primes \(3\le p<14000\), the finite calculation described in the next section examines every field element and every relevant word. It returns exactly the forty exceptions displayed above, with largest exception \(233\). The small primes \(3,5,7\), where the nine listed integers are not distinct modulo \(p\), are directly included in this enumeration rather than in the argument requiring \(p>8\). Because \(239\) is the next prime after \(233\), this proves the sharp threshold and the full exceptional set.

## Verification
Run `python3 verify.py` with Python 3, using only the standard library. It sieves every odd prime below \(14000\) (\(1651\) primes), represents all five-character words as the bits of a 32-bit integer, and constructs quadratic residues by exhaustive squaring. All \(t\in\mathbb F_p\) are examined until all words have occurred or the field is exhausted. The resulting exceptional-prime tuple is compared against the forty displayed primes.

As an independent arithmetic cross-check, a second implementation evaluates \(\chi_p\) using Euler's criterion rather than a squares table and compares full masks for all \(250\) odd primes below \(1600\). The verifier also confirms the missing-word mask at \(233\), completeness at \(229\), and strict positivity of the analytic bound at \(14000\). It returns `VERIFY_OK` only when each assertion succeeds.

## Relationship to prior work
Davenport's character-sum approach, as developed for simultaneous quadratic-residue patterns in Wright's *Quadratic Residues and Non-residues in Arithmetic Progression* (arXiv:1111.2236, first public 2011-11-09), supplies the established general method for eventual pattern occurrence. Theorem 2.3 there concerns prescribed signs of linear residue variables and asymptotic occurrence, not the sharp prime cutoff for five products of pairs of translated linear factors. Buchaev–Tsfasman's *Quadratic residue patterns of length 4 and 5* (arXiv:2607.17418) computes counts for sign words of five consecutive **integers**, also not for the present trace-discriminant products. Cohen's work on consecutive squares and nonsquares (arXiv:2402.10737) similarly concerns linear consecutive field elements.

For the present problem the variables satisfy \(\chi_p(f_j(t))=\chi_p(t+j-2)\chi_p(t+j+2)\). Thus this is a five-coordinate image of a length-nine ordinary character word, not a length-five ordinary residue word. General eventual existence or sharp results for shorter ordinary residue words cannot directly supply the sharp prime \(239\) without additional analysis. The claimed new scope is the simultaneous sharp cutoff, the complete exception set, and its particular one-word boundary obstruction, **not** the Weil bound or its general method.

## Limitations
The proof is unconditional for odd primes and for the explicit discriminant polynomials only. It does not give formulas for each word's exact number of occurrences at every prime, nor a classification of other window lengths, nor a statement for arbitrary prime powers. The finite component is exhaustive over its stated range but cannot itself establish existence at infinitely many primes; equation (4) supplies that part. Literature and database searches may miss an unindexed stronger theorem, so independent originality assessment remains appropriate.

## References
1. S. Wright, *Quadratic Residues and Non-residues in Arithmetic Progression*, arXiv:1111.2236 (first submitted 2011-11-09), especially Theorem 2.3 and the character-sum method. https://arxiv.org/abs/1111.2236
2. A. Buchaev and M. Tsfasman, *Quadratic residue patterns of length 4 and 5*, arXiv:2607.17418 (2026), sections 1–4. https://arxiv.org/abs/2607.17418
3. S. D. Cohen, *Triples and quadruples of consecutive squares or non-squares in a finite field*, arXiv:2402.10737 (2024), Theorem 1.1 and Section 2. https://arxiv.org/abs/2402.10737
4. A. Weil, classical bound for multiplicative-character sums of squarefree polynomials (used in the standard form stated in the proof); discussed in Wright, reference 1.
