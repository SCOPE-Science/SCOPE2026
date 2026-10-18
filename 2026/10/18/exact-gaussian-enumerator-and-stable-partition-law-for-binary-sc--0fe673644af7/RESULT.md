# Exact Gaussian enumerator and stable partition law for binary scattered \(a b^{t} a\)-avoidance

## Finding

For any \(A\ge2\), \(B\ge0\), and \(t\ge3\), let \(N_t(A,B,C)\) count binary words with exactly \(A\) occurrences of \(a\), \(B\) occurrences of \(b\), and \(C\) scattered occurrences of \(ab\), **avoiding** the scattered pattern \(a b^t a\). Their entire distribution is the coefficient sequence of

\[
\boxed{\sum_{C=0}^{AB}N_t(A,B,C)q^C=\sum_{d=0}^{\min(B,t-1)}q^d\begin{bmatrix}A+d-2\\d\end{bmatrix}_q\sum_{z=0}^{B-d}q^{Az}.}
\]

In the low-count chamber \(A\ge\max(2,C+1)\) and \(B\ge C\), this specializes to

\[
\boxed{N_t(A,B,C)=p_{\le t-1}(C),\qquad |L_{A,B,C}|=p(C).}
\]

Here \(p(C)\) counts partitions of \(C\), with \(p(0)=1\), and \(p_{\le r}(C)\) counts those with at most \(r\) positive parts. For \(t\ge3\) fixed and \(C\to\infty\) within this chamber,

\[
\boxed{\mathbb P(a b^t a\text{ absent}\mid A,B,C)\sim\frac{4\sqrt3}{(t-1)!(t-2)!}\,C^{t-1}\exp\!\left(-\pi\sqrt{\frac{2C}{3}}\right).}
\]

The asymptotic is uniform over chamber choices of \(A,B\) because the probabilities are identically the same there. In particular, for the length-five scattered pattern \(a b^3 a\), the exact conditional **presence** probability in this chamber is \(1-(\lfloor C/2\rfloor+1)/p(C)\).

## Assumptions and scope

A scattered subsequence is a not-necessarily-contiguous sequence obtained by selecting increasing positions. The count \(C=|w|_{ab}\) is the number of ordered pairs of positions occupied by \(a\), then \(b\). The alphabet is \(\{a,b\}\), and all words with the three specified counts have equal weight. The Gaussian coefficient \(\begin{bmatrix}n\\k\end{bmatrix}_q\) denotes the polynomial \(\prod_{j=1}^{k}(1-q^{n-k+j})/(1-q^j)\) for \(0\le k\le n\), with the empty product equal to one. The formal variable is \(q\), unrelated to the alphabet size. The exact generating polynomial applies for every \(0\le C\le AB\); the stable equality requires the additional inequalities stated above. Pattern length is \(t+2\ge5\), excluding the previously studied length-four boundary.

## Proof

**1. Canonical gap factorization and the avoidance criterion.** Every word with \(A\ge2\) has one and only one factorization

\[
w=b^x a b^{u_1}a b^{u_2}\cdots a b^{u_{A-1}}a b^z,
\quad x,z,u_j\in\mathbb Z_{\ge0},\quad x+z+\sum_{j=1}^{A-1}u_j=B.
\]

The pattern \(a b^t a\) is a scattered subsequence if and only if at least \(t\) letters \(b\) occur strictly between some two \(a\)'s. Taking the first and last \(a\) shows this happens exactly when \(d=\sum_{j=1}^{A-1}u_j\ge t\). Therefore avoidance is equivalent to \(d\le t-1\). Every interior letter \(b\) in the \(j\)-th gap has exactly \(j\) letters \(a\) before it, every trailing \(b\) has \(A\), and every leading \(b\) has zero. Consequently,

\[|w|_{ab}=\sum_{j=1}^{A-1}j u_j+A z.\]

**2. Weighted enumeration.** For fixed interior total \(d\), summing the weights of all gap vectors gives the complete homogeneous polynomial

\[\sum_{u_1+\cdots+u_{A-1}=d}q^{\sum j u_j}=h_d(q,q^2,\ldots,q^{A-1})=q^d\begin{bmatrix}A+d-2\\d\end{bmatrix}_q.\]

The second equality follows by subtracting one from each of the \(d\) selected gap indices and identifying weakly increasing selections from \(0,\ldots,A-2\) with partitions inside the \(d\)-by-\((A-2)\) rectangle; equivalently it is the finite Gaussian-binomial generating identity. With \(d\le\min(B,t-1)\), the trailing count \(z\) runs through \(0,\ldots,B-d\). The leading count is forced to be \(x=B-d-z\), so there are no multiplicity factors. Multiplying by \(q^{Az}\) and summing over \(d,z\) proves the boxed polynomial without omissions or double counting.

**3. The stable coefficient.** Suppose \(A\ge\max(2,C+1)\) and \(B\ge C\). In a word of inversion count \(C\), a trailing letter \(b\) would contribute \(A>C\); thus \(z=0\). Remaining configurations contributing \(q^C\) are multisets of \(d\le t-1\) interior indices from \(1,\ldots,A-1\), summing to \(C\). Since \(A-1\ge C\), this upper bound on part size does not exclude any partition of \(C\); since \(B\ge C\), the available \(B\) letters do not exclude any partition either. Hence the numerator is exactly \(p_{\le t-1}(C)\).

Without the avoidance restriction, the same gap-index construction, allowing parts \(1,\ldots,A\) with suitable trailing treatment, is equivalently the standard Gaussian enumerator of all binary words:

\[\sum_{C=0}^{AB}|L_{A,B,C}|q^C=\begin{bmatrix}A+B\\A\end{bmatrix}_q.\]

Its coefficient counts partitions into at most \(B\) parts, each at most \(A\) (or equivalently, by conjugation, at most \(A\) parts each at most \(B\)). Both rectangle restrictions become vacuous at weight \(C\) when \(A\ge C+1\), \(B\ge C\); hence the denominator is \(p(C)\), a strictly positive integer. Subtraction from one yields the presence probability.

**4. Sharp fixed-pattern asymptotic.** For \(r=t-1\ge2\), partition conjugation supplies the generating function

\[\sum_{C\ge0}p_{\le r}(C)q^C=\prod_{j=1}^{r}(1-q^j)^{-1}.\]

Near \(q=1\), this has principal part \(\bigl(r!(1-q)^r\bigr)^{-1}\); every other root-of-unity singularity has pole order strictly less than \(r\). Coefficient extraction therefore gives

\[p_{\le r}(C)=\frac{C^{r-1}}{r!(r-1)!}+o(C^{r-1}).\]

The classical Hardy–Ramanujan asymptotic is \(p(C)\sim (4\sqrt3\,C)^{-1}\exp(\pi\sqrt{2C/3})\). Dividing these two equivalent forms yields the claimed constant and exponent \(C^r\), with \(r=t-1\). All limits are taken with fixed \(t\) while \(C\) grows; no simultaneous growing-\(t\) assertion is made.

## Verification

Run `python3 checker.py` using Python's standard library. The checker independently enumerates labeled binary words and directly tests the scattered pattern, computes the proposed polynomial by Gaussian recurrence, and compares every coefficient. It verifies 252 parameter triples and 3,354 coefficients, plus 320 stable-chamber partition checks up to \(C=39\). The recorded output is `CHECK_OUTPUT.txt`. These finite tests are a cross-check; the preceding argument proves the infinite-parameter theorem.

## Relationship to prior work

Fazekas, Huang, and Mercaş (2026, published 25 August in EPTCS 451; arXiv:2610.06717v1) introduce systematic fixed-Parikh-matrix conditional probabilities for scattered subsequence questions. Their discussion includes general enumeration methods, approximations and special patterns, rather than the all-parameter \(a b^t a\) formula and its sharp fixed-\(t\) stable-chamber asymptotic above. Richomme (2025, arXiv:2510.07159v1) gives the fundamental partition-lattice description of binary two-binomial equivalence classes: the unrestricted Gaussian denominator is therefore established prior structure, not claimed here as new. Atanasiu (2007) studies binary Parikh-matrix languages and gap-parametrizations; the present restricted interior-gap statistic and exact conditional law are separate. The Hardy–Ramanujan formula supplies a classical asymptotic ingredient. Standard Gaussian-polynomial identities themselves are not claimed as discoveries.

## Limitations

The result treats binary words and the single family of scattered patterns \(a b^t a\) for \(t\ge3\). The asymptotic does not cover fixed short \(A,B\), fixed small \(C\), varying \(t\), or other target patterns. General alphabets, other subsequence statistics, and finer error terms are open relative to this statement. Historical priority beyond the inspected relevant sources, including an independently derived equivalent restricted-partition enumeration, is not certified; no independent audit has been performed.

## References

1. Fazekas, Huang, and Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, Electronic Proceedings in Theoretical Computer Science 451 (published 25 August 2026), 140–154, https://doi.org/10.4204/EPTCS.451.10; arXiv:2610.06717v1 (5 October 2026), https://arxiv.org/abs/2610.06717.
2. G. Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, arXiv:2510.07159v1 (2025), https://arxiv.org/abs/2510.07159.
3. A. Atanasiu, *Binary Amiable Words*, International Journal of Foundations of Computer Science 18 (2007), 387–400, https://doi.org/10.1142/S0129054107004735.
4. G. H. Hardy and S. Ramanujan, *Asymptotic Formulae in Combinatory Analysis*, Proceedings of the London Mathematical Society 17 (1918), 75–115, https://doi.org/10.1112/plms/s2-17.1.75.
