# Signed stochastic regression of cell counts in Fisher–Yates contingency tables

## Finding
Let \(T=(T_{ij})\) be a random contingency table with fixed positive row margins \(a_1,\ldots,a_I\) and column margins \(b_1,\ldots,b_J\), each summing to \(N\). Under the Fisher–Yates law (the table induced by a uniform random permutation), choose distinct cells \(X=T_{ij}\) and \(Y=T_{k\ell}\). For every two attainable conditioning values \(x<x'\), and every integer threshold \(u\),

\[
\begin{aligned}
\Pr(Y\ge u\mid X=x')&\le\Pr(Y\ge u\mid X=x), && i=k\text{ or }j=\ell,\\
\Pr(Y\ge u\mid X=x')&\ge\Pr(Y\ge u\mid X=x), && i\ne k\text{ and }j\ne\ell.
\end{aligned}
\]

Thus for any two nondecreasing real-valued functions \(f,g\), \(\operatorname{Cov}(f(X),g(Y))\le0\) for cells in the same row or column, whereas \(\operatorname{Cov}(f(X),g(Y))\ge0\) for cells in distinct rows and columns. In particular, the joint locations of zero cells obey precisely this signed pairwise association: two zero-cell indicators have negative covariance if the cells share a row/column and positive covariance if they are in separate rows and columns; equality is permitted in degenerate margin configurations.

The exact ordinary count covariance is

\[
\operatorname{Cov}(T_{ij},T_{k\ell})=
\begin{cases}
-\dfrac{a_i(N-a_i)b_jb_{\ell}}{N^2(N-1)}, &i=k,\ j\ne\ell,\\[5pt]
-\dfrac{a_i a_k b_j(N-b_j)}{N^2(N-1)}, &i\ne k,\ j=\ell,\\[5pt]
\dfrac{a_i a_k b_jb_{\ell}}{N^2(N-1)}, &i\ne k,\ j\ne\ell.
\end{cases}
\]

The new assertion assessed here is the *full stochastic regression ordering*, not the familiar hypergeometric mean/covariance formulas or the Fisher–Yates distribution itself.

## Assumptions and scope
Fix integers \(N\ge2\), \(I,J\ge2\) and positive integers \(a_i,b_j\) with \(\sum_i a_i=\sum_j b_j=N\). Partition the row positions \([N]\) into specified sets \(A_i\) of sizes \(a_i\), and the column labels into \(B_j\) of sizes \(b_j\). Draw a uniform bijection \(\pi:[N]\to[N]\), and set \(T_{ij}=|\pi(A_i)\cap B_j|\). Equivalently, the table mass is

\[
\Pr(T=t)=\frac{\prod_i a_i!\,\prod_j b_j!}{N!\prod_{i,j}t_{ij}!}
\]

for every nonnegative integer table with the stated margins. Every conditional comparison is over the support \(\{x:\Pr(X=x)>0\}\). Stochastic increasing means all upper-tail probabilities are nondecreasing at every integer threshold. No independent-entry approximation is assumed. The probability law is **not** the uniform law over fixed-margin tables.

## Proof
**Sampling lemma.** Let \(H(M,s,d)\) denote the number of distinguished labels in a uniformly drawn \(d\)-subset of an \(M\)-element population containing \(s\) distinguished labels; this is a hypergeometric law. A single fixed random ordering of the population couples \(H(M,s,d)\) so it is nondecreasing as \(d\) increases; a single ordering followed by nested marked sets couples it to be nondecreasing as \(s\) increases. These are almost-sure monotone couplings, valid including endpoints.

**Cells in one row.** Put \(a=a_i\), \(b=b_j\), \(d=b_{\ell}\). Conditional on \(X=x\), the \(a-x\) selected labels outside \(B_j\) form a uniform \((a-x)\)-subset of the \(N-b\) remaining labels. Hence

\[
Y\mid X=x\ \stackrel{d}{=}\ H(N-b,d,a-x).
\]

Increasing \(x\) decreases the sample size, proving the stated decreasing order. If the cells share a column instead, invert \(\pi\): with \(a=a_i\), \(b=b_j\), \(c=a_k\),

\[
Y\mid X=x\ \stackrel{d}{=}\ H(N-a,c,b-x),
\]

which again decreases stochastically with \(x\).

**Cells in distinct rows and columns.** Put \(a=a_i\), \(b=b_j\), \(c=a_k\), \(d=b_{\ell}\) and let \(U=\pi(A_i)\), a uniform \(a\)-subset of \([N]\). Conditional on \(X=|U\cap B_j|=x\), set \(K=|U\cap B_{\ell}|\). Sampling the \(a-x\) points of \(U\) outside \(B_j\) gives

\[
K\mid X=x\ \stackrel{d}{=}\ H(N-b,d,a-x).
\]

Conditional on the entire \(U\), the image \(\pi(A_k)\) is an independent uniform \(c\)-subset of \([N]\setminus U\), which has \(N-a\) points of which \(d-K\) belong to \(B_{\ell}\). Therefore

\[
Y\mid (X=x,K=k)\ \stackrel{d}{=}\ H(N-a,d-k,c).
\]

As \(x\) increases, the sampling lemma couples \(K\) to *decrease*, hence couples \(d-K\) to *increase*. Applying the same lemma to the second conditional hypergeometric law couples \(Y\mid X=x\) to increase. The two couplings combine by using common random orderings, proving the assertion for every pair of feasible \(x<x'\).

**Transform covariance.** For any nondecreasing \(g\), the function \(h(x)=\mathbb E[g(Y)\mid X=x]\) has the indicated monotonicity. Because \(\operatorname{Cov}(f(X),g(Y))=\operatorname{Cov}(f(X),h(X))\), and, with \(X'\) independent of \(X\),

\[
2\operatorname{Cov}(f(X),h(X))=\mathbb E[(f(X)-f(X'))(h(X)-h(X'))],
\]

its sign is as claimed. For a zero-cell indicator, \(-\mathbf1_{\{X=0\}}\) is nondecreasing; changing the sign of both indicator functions preserves their covariance.

**Covariance formula.** Write \(T_{ij}=\sum_{u\in A_i}\mathbf1_{\{\pi(u)\in B_j\}}\), expand pairwise expectations using sampling without replacement, and simplify. Equivalently, for distinct cells the compact identity is

\[
\operatorname{Cov}(T_{ij},T_{k\ell})=\frac{a_i b_j}{N-1}\left(\mathbf1_{\{i=k\}}-\frac{a_k}{N}\right)\left(\mathbf1_{\{j=\ell\}}-\frac{b_{\ell}}{N}\right),
\]

which expands to the three displayed cases. These moment formulas are included to make the stronger stochastic sign theorem quantitatively interpretable, not as a separate novelty claim.

## Verification
The accompanying standalone `verify.py` enumerates all permutations for 151 positive-margin pairs with \(2\le N\le6\), including every composition into two or three groups when \(N\le5\), and selected three-group cases for \(N=6\). It independently computes each conditional distribution by counting permutations, verifies all upper-tail stochastic-order inequalities with exact rational arithmetic, and checks the covariance identity. The completed run reported 48,818 exact comparisons and identities.

For \(N=6\) and margins \(a=b=(2,2,2)\), a marked cell is empty with probability \(2/5\). Its empty event has covariance \(23/450\) with the empty event at a cell in another row and column, versus covariance \(-7/75\) with one in the same row. These numbers follow from exact counts of the 720 permutations: joint empty-event probabilities \(19/90\) and \(1/15\), respectively. Exhaustive finite checking is not substituted for the arbitrary-size coupling proof.

## Relationship to prior work
The Fisher–Yates contingency-table law and its asymptotic entry covariance structure are classical and are explained by Diaconis–Simper (2021, Section 5, especially Theorem 5.2). Paguyo (2021 preprint, Section 1) identifies the positions of zero entries among natural questions and studies different statistics of permutations from fixed double cosets. Simper (2022) treats the random-transposition chain and multivariate orthogonal polynomials of the same distribution. Their inspected statements concern the table law, marginal/global fluctuation questions, or dynamical eigenfunctions; they do not give the full conditional stochastic ordering across all cell positions. The claim here strengthens pairwise covariance signs to all increasing transforms and in particular all threshold/zero indicators.

The result uses elementary finite-population sampling couplings, so an equivalent formulation might exist implicitly in older multivariate hypergeometric, random-permutation negative-dependence, or exact-conditional-inference literature. A nonappearance in searched material cannot establish absolute historical priority.

## Limitations
This is a pairwise statement, not global positive/negative association of arbitrary collections of cells. The signs need not be strict for nonlinear statistics, and the law on *uniformly sampled fixed-margin tables* is not covered. No full joint process of zero locations or asymptotic limit theorem is claimed. An independent historical-priority audit has not been performed.

## References
1. P. Diaconis and M. Simper, *Statistical Enumeration of Groups by Double Cosets*, arXiv:2102.04576 (first posted 2021-02-08), Section 5.
2. J. E. Paguyo, *Fixed Points, Descents, and Inversions in Parabolic Double Cosets of the Symmetric Group*, arXiv:2112.07728 (first posted 2021-12-14), Sections 1–2.
3. M. Simper, *Random Transpositions on Contingency Tables*, arXiv:2208.10700 (first posted 2022-08-23), Sections 1–2.
4. K. Joag-Dev and F. Proschan, *Negative Association of Random Variables with Applications*, Annals of Statistics 11 (1983), 286–295; conceptual comparison with finite-population negative-dependence methods.
