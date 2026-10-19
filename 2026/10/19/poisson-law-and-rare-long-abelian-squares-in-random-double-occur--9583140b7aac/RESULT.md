# Poisson law and rare long Abelian squares in random double-occurrence words

## Finding

Let \(q\ge1\) be an integer, and choose uniformly a length-\(2q\) word \(W_q\) on the labeled alphabet \(\{1,\ldots,q\}\) in which every letter occurs exactly twice. Let \(Y_q\) count all *occurrences* of contiguous Abelian squares, counting a separate occurrence for each starting position and positive half-length. An Abelian square is a factor \(uv\) with \(|u|=|v|\ge1\) and identical Parikh (letter-count) vectors. Let \(X_q\) count adjacent equal-letter pairs in \(W_q\).

Then
\[
\mathbb E Y_q=\sum_{k=1}^{q}\frac{k!(2q-2k+1)!!}{(2q-1)!!}
=1+\frac{1}{q}+O(q^{-2}),\qquad
\mathbb E(Y_q-X_q)=\frac{1}{q}+O(q^{-2}).
\]
More precisely, \(\mathbb E(Y_q-X_q)=2/(2q-1)+O(q^{-2})\). As \(q\to\infty\),
\[
d_{\mathrm{TV}}\bigl(\mathcal L(Y_q),\operatorname{Poisson}(1)\bigr)=O(q^{-1}),
\qquad
\Pr(W_q\text{ is Abelian-square-free})=e^{-1}+O(q^{-1}).
\]
In particular, the probability of **any** Abelian square with half-length at least two is \(O(q^{-1})\). The Poisson limit counts *all occurrences*, not just distinct Abelian-square factors.

There is also a finite exact formula for the adjacency-free probability:
\[
\Pr(X_q=0)=\sum_{r=0}^{q}(-1)^r\binom{2q-r}{r}
\frac{(2q-2r-1)!!}{(2q-1)!!}.
\]
Here \((-1)!!=1\), and probability refers to the uniform fixed-multiplicity ensemble described above.

## Assumptions and scope

Words are linear, not cyclic; windows never wrap around. Each of the \(q\) distinct labeled letters appears exactly twice. The total number of labeled words is \((2q)!/2^q\). Equivalently, discard the arbitrary labels and connect the two positions of each letter: the resulting pairing of \(\{1,\ldots,2q\}\) is a uniformly random perfect matching. There are \((2q-1)!!\) such matchings and each has exactly \(q!\) labelings.

The theorem applies to every integer \(q\ge1\), with asymptotic assertions as \(q\) tends to infinity. The variable \(X_q\) counts factors \(aa\); \(Y_q-X_q\) counts occurrences with half-length at least two. Different windows count separately even if they have identical content.

## Proof

**1. A matching characterization and exact first moment.** Fix a window of length \(2k\) with left and right halves of length \(k\). Since every letter occurs exactly twice in the entire word, equal half-Parikh vectors hold if and only if each of the \(k\) paired positions inside the window joins one position in the left half to one in the right half. This is a *complete* characterization: no letter can occur twice in both halves or have just one occurrence in the window.

There are exactly \(k!\) ways to match the two sets of \(k\) positions; the remaining \(2q-2k\) positions can be paired in \((2q-2k-1)!!\) ways. Dividing by \((2q-1)!!\) gives the probability for a prescribed window. Summing over all \(2q-2k+1\) starting positions gives
\[
E_{q,k}:=\mathbb E A_{q,k}
=\frac{k!(2q-2k+1)!!}{(2q-1)!!},
\]
where \(A_{q,k}\) is the number of Abelian squares with half-length \(k\). In particular,
\[
E_{q,1}=1,\quad E_{q,2}=\frac{2}{2q-1},\quad
\frac{E_{q,k+1}}{E_{q,k}}=\frac{k+1}{2q-2k+1}\quad(1\le k<q).
\]
The displayed ratio strictly increases with \(k\), so the sequence \((E_{q,k})_{k=1}^{q}\) is log-convex and its maximum on any interval occurs at an endpoint.

To control all lengths simultaneously, assume \(q\ge4\), put \(m=\lfloor q/2\rfloor\), and observe that the ratios up to the transition from \(m\) to \(m+1\) are at most \(3/4\). Thus
\[
\sum_{k=3}^{m+1} E_{q,k}\le4E_{q,3}=O(q^{-2}),\qquad
E_{q,m+1}\le E_{q,2}(3/4)^{m-1}.
\]
For \(k\ge m+1\), log-convexity bounds \(E_{q,k}\) by \(\max\{E_{q,m+1},E_{q,q}\}\). Moreover,
\[
E_{q,q}=\frac{q!}{(2q-1)!!}
=\frac{2^q(q!)^2}{(2q)!}=O(\sqrt q\,2^{-q})
\]
by the standard central-binomial-coefficient estimate. Hence
\[
\sum_{k=3}^{q}E_{q,k}
\le4E_{q,3}+qE_{q,m+1}+qE_{q,q}
=O(q^{-2}).
\]
Consequently the expected number of longer squares is \(2/(2q-1)+O(q^{-2})\), and Markov's inequality gives \(\Pr(Y_q\ne X_q)=O(q^{-1})\).

**2. Exact factorial moments for adjacent equal pairs.** Regard \(X_q\) as the number of matching edges equal to one of the \(2q-1\) consecutive pairs \(\{i,i+1\}\). A set of \(r\) prescribed consecutive edges can occur in a perfect matching only when its edges are vertex-disjoint. There are \(\binom{2q-r}{r}\) such edge subsets in the path of \(2q\) vertices. Each is present with probability \((2q-2r-1)!!/(2q-1)!!\). Therefore
\[
a_{q,r}:=\mathbb E\binom{X_q}{r}
=\frac{\binom{2q-r}{r}}{(2q-1)(2q-3)\cdots(2q-2r+1)}
=\frac1{r!}\prod_{j=0}^{r-1}
\left(1-\frac{r-j-1}{2q-2j-1}\right)
\]
for \(0\le r\le q\), with the empty product equal to one; set \(a_{q,r}=0\) for \(r>q\). All product factors lie in \([0,1]\), so \(0\le a_{q,r}\le1/r!\). When \(r\le q/2\), the elementary product inequality \(1-\prod(1-t_j)\le\sum t_j\) yields
\[
0\le\frac1{r!}-a_{q,r}
\le\frac{r(r-1)}{2(q+1)r!}.
\]
For \(r>q/2\) use the bound \(1/r!\).

**3. A total-variation bound by binomial inversion.** If a nonnegative integer-valued variable has finite support, its binomial moments satisfy
\[
\Pr(X_q=s)=\sum_{r=s}^{q}(-1)^{r-s}\binom rs a_{q,r}.
\]
For a Poisson variable of mean one the same formula holds with \(a_{q,r}\) replaced by \(1/r!\), with absolutely convergent sums. By the triangle inequality, interchange of nonnegative sums, and \(\sum_{s=0}^r\binom rs=2^r\),
\[
2d_{\mathrm{TV}}(\mathcal L(X_q),\operatorname{Poisson}(1))
\le\sum_{r\ge0}2^r\left(\frac1{r!}-a_{q,r}\right)
\le\frac{1}{2(q+1)}\sum_{r\ge0}\frac{2^r r(r-1)}{r!}
+\sum_{r>q/2}\frac{2^r}{r!}
=O(q^{-1}).
\]
The first series is \(4e^2\); the second is super-polynomially small in \(q\). The natural coupling \(Y_q=X_q+(Y_q-X_q)\) gives
\[
d_{\mathrm{TV}}(\mathcal L(Y_q),\operatorname{Poisson}(1))
\le\Pr(Y_q\ne X_q)+d_{\mathrm{TV}}(\mathcal L(X_q),\operatorname{Poisson}(1))
=O(q^{-1}).
\]
Taking the singleton event \(\{0\}\) proves the asserted Abelian-square-free probability. Finally, inclusion–exclusion applied to the forbidden path edges and the already-counted \(r\)-subsets gives the exact finite expression for \(\Pr(X_q=0)\).

## Verification

A standalone Python checker enumerates perfect matchings on \(2q\) points and converts each to the uniquely first-occurrence-normalized double-occurrence word. For each word, it checks all contiguous even-length windows using direct Parikh-vector comparison, independently counts the adjacent matched pairs, and aggregates the exact histograms. It verifies the first-moment formula for every half-length and the binomial-moment formula for each feasible \(r\), for \(q=1,\ldots,7\). It also checks the observed initial numbers of Abelian-square-free normalized words:
\[
0,0,1,15,195,2630,38519.
\]
The enumeration comprises \(1+3+15+105+945+10395+135135=146599\) perfect matchings. All infinite-parameter and asymptotic statements are established by the preceding proof, not by extrapolation from finite enumeration.

Run from the folder containing the files with `python3 verify.py`. The script uses only the Python standard library.

## Relationship to prior work

Fici and Puzynina's survey (arXiv:2207.09937), notably Sections 4.3 and 5, develops Abelian-square enumeration and avoidance, including asymptotics for random *fixed-binary-alphabet* words. The present result instead samples all permutations of a growing alphabet with exactly two occurrences per symbol. Those different sampling hypotheses do not imply the Poisson result, and the distinct-factor enumeration in the survey differs from the occurrence-count statistic here.

Cruz et al. (arXiv:1811.11739) study double-occurrence words and insertions of repeated/return patterns; their equivalence and insertion analysis does not calculate contiguous Abelian-square occurrences in the uniform ensemble. Grytczuk, Pawlik and Pleszczyński (arXiv:2308.13882) study shuffle-square decompositions, which do not require the two blocks to be contiguous, so their statements do not determine this local count. Classical Poisson approximations for rare prescribed matching edges provide conceptual background for the adjacent-edge portion; the additional contribution here is the exact Abelian-square window counting and the quantitative suppression of *all* longer windows.

## Limitations

The result concerns linear words with precisely two occurrences per symbol and an alphabet size that grows with the word length. It does not apply to circular factors, to a fixed alphabet with arbitrary multiplicities, or to shuffle-square counts. The rate \(O(q^{-1})\) is not presented with an optimal leading coefficient for the avoidance probability. Equivalent results under different matching or consecutive-pattern terminology cannot be definitively excluded without a complete literature census. The results have undergone a mathematical consistency review but no independent mathematical audit.

## References

1. D. A. Cruz, M. M. Ferrari, N. Jonoska, L. Nabergall and M. Saito, *Insertions Yielding Equivalent Double Occurrence Words*, arXiv:1811.11739, publicly posted November 28, 2018. https://arxiv.org/abs/1811.11739
2. G. Fici and S. Puzynina, *Abelian Combinatorics on Words: a Survey*, arXiv:2207.09937, first posted July 20, 2022; especially Sections 4.3 and 5. https://arxiv.org/abs/2207.09937
3. J. Grytczuk, B. Pawlik and M. Pleszczyński, *Variations on shuffle squares*, arXiv:2308.13882, publicly posted August 26, 2023. https://arxiv.org/abs/2308.13882
