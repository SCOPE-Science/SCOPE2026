# The independence cutoff and third-order clustering of fixed-length palindromic matches

## Finding

Let \(q\ge2\) and \(k\ge2\) be integers. In an independent uniform \(q\)-symbol word \(X_0,\ldots,X_{N-1}\), \(N\ge k\), let \(A_i\) be the indicator that the contiguous word \(X_i,\ldots,X_{i+k-1}\) is a palindrome, for \(0\le i<M=N-k+1\). Put \(r=\lfloor k/2\rfloor\) and \(p=q^{-r}\).

**Complete joint-success law.** For any subset \(S\subseteq\{0,\ldots,M-1\}\), form the undirected graph \(G_{k,S}\) on the indices appearing in its selected windows. For each \(i\in S\) add edges \(\{i+j,i+k-1-j\}\), \(0\le j<r\). If \(v\) and \(c\) denote the graph's vertex and connected-component counts, then
\[
\Pr(A_i=1\text{ for every }i\in S)=q^{-(v-c)}.
\]
For \(S=\varnothing\), the probability is one. This specifies every finite-dimensional law by inclusion-exclusion.

**Sharp independence classification.** For every \(k\), distinct \(A_i\) and \(A_j\) are independent, even when their windows overlap. The entire indicator family is mutually independent if and only if \(k\le3\) or \(M\le2\). Hence the count \(S_{N,k}=\sum_{i=0}^{M-1}A_i\) has
\[
\mathbb E S_{N,k}=Mp,\qquad \operatorname{Var}(S_{N,k})=Mp(1-p),
\]
but its law is \(\operatorname{Bin}(M,p)\) exactly if and only if \(k\le3\) or \(M\le2\).

**Third-order obstruction.** For three consecutive starts,
\[
\Pr(A_i=A_{i+1}=A_{i+2}=1)=q^{-(2r+1)},\qquad
\kappa(A_i,A_{i+1},A_{i+2})=p^3(q^{r-1}-1).
\]
For \(k\ge4\) and \(M\ge3\), the count's third cumulant is strictly greater than the third cumulant of \(\operatorname{Bin}(M,p)\), by at least \(6(M-2)p^3(q^{r-1}-1)\). At lengths \(k=4\) or \(5\) this bound is an equality:
\[
\kappa_3(S_{N,k})=Mp(1-p)(1-2p)+6\max\{M-2,0\}p^3(q-1).
\]

**Rigidity beyond uniform sources.** For an independent nonuniform word on a positive finite probability vector \((w_a)\), and \(N\ge2k-1\), the two palindrome indicators at starts zero and \(k-1\) have covariance
\[
\biggl(\sum_a w_a^2\biggr)^{2r-2}
\biggl[\sum_a w_a^3-\biggl(\sum_a w_a^2\biggr)^2\biggr].
\]
It is strictly positive unless all positive \(w_a\) are equal. Thus, for this window range, pairwise independence characterizes the uniform i.i.d. source.

## Assumptions and scope

Palindromes mean literal reversal equality, **not** reverse-complement DNA palindromes. The sample positions and lengths are finite, \(q,k,N\) are integers as above, and the symbol probabilities are independent and uniform unless the nonuniform extension is stated. No independence of partially overlapping windows is assumed. The third-cumulant formula for \(k=4,5\) holds for every admissible \(N\); the strict inequality for all \(k\ge4\) requires \(M\ge3\). The stated nonuniform rigidity only asserts the pair relation when both windows exist, \(N\ge2k-1\).

## Proof

**1. Joint law.** The event that all selected windows are palindromes imposes only symbol equalities along edges of \(G_{k,S}\). Each connected component has one freely chosen symbol; there are \(q^c\) satisfying assignments of the \(v\) involved coordinates, out of \(q^v\) equally likely assignments. Indices not in the graph contribute a factor one. Inclusion-exclusion determines joint probabilities for arbitrary zero-one indicator configurations.

**2. Pairwise independence.** Each single palindrome contributes a matching of exactly \(r\) equality edges (with an unused central coordinate if \(k\) is odd). Two distinct windows have different reflection centers. Their matchings share no edge, and their union cannot contain a cycle: in an alternating cycle, applying the two different reflections in succession translates the index by twice the nonzero difference between the starts, impossible on a finite cycle of integer indices. Thus the union contains \(2r\) independent equality edges. Its probability is \(q^{-2r}=p^2\).

**3. Mutual independence threshold.** If \(k=2\), every palindrome equality is a nearest-neighbor edge; if \(k=3\), every equality is an edge joining indices two apart. The union over any collection of starts is a subgraph of one path or two disjoint paths, respectively, so is a forest. All joint-success probabilities factor, proving mutual independence. The same is immediate for at most two indicators.

If \(k\ge4\), the union of three matchings from successive windows occupies \(k+2\) coordinates. For even \(k=2r\), all coordinates in that union lie in one equality component; for odd \(k=2r+1\), the even and odd coordinates form its two components. One verifies this by composing adjacent reflections, which links indices two apart, and using the middle matching to connect opposite parities when \(k\) is even. Thus in both cases the equality-constraint rank is \(2r+1\), giving the triple formula. Because \(r\ge2\), the triple probability exceeds \(p^3\), so these three indicators cannot be mutually independent.

**4. Third cumulant and nonbinomiality.** Any three selected windows contribute at most \(3r\) independent equalities. Consequently every triple joint-success probability is at least \(p^3\). By pairwise independence, each joint third cumulant for three distinct positions equals the triple probability minus \(p^3\), and is nonnegative. Expanding \(\kappa_3(\sum_i A_i)\), all contributions with repeated indices equal those of independent Bernoulli variables; the contributions with three distinct indices are six times their joint third cumulants. Each of the \(M-2\) consecutive triples contributes \(p^3(q^{r-1}-1)>0\). This yields the stated lower bound and proves the count cannot be binomial when \(k\ge4\), \(M\ge3\). For \(k=4,5\), direct enumeration of all translated triples \((0,a,b)\) with \(1\le a<b\le2k-2\) shows that the only nonzero equality-constraint deficit is \((a,b)=(1,2)\), with deficit one. For \(b\ge2k-1\), one outer window is isolated from the other two, so no deficit is possible. This finite exhaustive reduction proves the exact displayed cumulant formula. The included independent checker evaluates these finite ranks directly.

**5. Nonuniform rigidity.** Put \(s_2=\sum_a w_a^2\) and \(s_3=\sum_a w_a^3\). A palindrome requires \(r\) independent paired equalities, so has probability \(s_2^r\). At separation \(k-1\), the two windows share just one coordinate. Their two outer mirror constraints produce a triple equality of probability \(s_3\); the other \(2r-2\) constraints are disjoint paired equalities. Subtracting the product of marginals gives \(s_2^{2r-2}(s_3-s_2^2)\). Cauchy--Schwarz gives \(s_3\ge s_2^2\), with equality for a positive probability vector only when all masses are equal.

## Verification

The standalone standard-library Python script `check_palindrome_count.py` exhaustively enumerates small uniform words, checks exact rational means, variances, pair probabilities, consecutive triples, all finite-dimensional joint-success probabilities on sampled sizes, and the third-cumulant formulas. It also checks the complete finite set of triple overlap offsets needed for \(k=4,5\), and compares the nonuniform overlap covariance to direct finite-word enumeration. Run: `python check_palindrome_count.py` (tested successfully with 2931 exact assertions). The unbounded claims are proved analytically above; finite enumeration alone is not a proof for arbitrary \(k,N\).

## Relationship to prior work

Rubinchik and Shur (2015, arXiv:1505.08043) count **distinct** palindromic factors and state the expected number of positional occurrences (Lemma 3.2); this work concerns the complete location-indexed dependence law, independence cutoff, and third cumulants. Gabric and Shallit (2019, arXiv:1906.03689, Theorem 7) give an exact adjacent-sum correspondence between odd and even palindromic **prefix** orders. That correspondence is acknowledged and no parity-coupling or even/odd equidistribution is claimed here. Lillo and Spanò (2007, DOI:10.1103/PhysRevE.76.041914) investigate mirror and inverted repeats in random nucleotide models. Špoljarić and Ugrina (2013, DOI:10.1080/03610926.2012.739253) study fixed-length reverse-complement DNA-palindrome counts and normal approximations; full text was not accessible in the present comparison. Its scope is a significant residual historical-priority risk, and its abstract alone cannot establish noncoverage. General word-occurrence frameworks also provide algorithmic approaches to count laws; such methods are not represented as absent.

## Limitations

The claim is about ordinary palindromes, not reverse-complement matching under a nontrivial alphabet involution. It does not provide a closed-form full histogram for arbitrary \(k,N,q\), although the graph law determines it algorithmically. No finite enumeration proves the all-parameter theorem independently of the graph proof. Statistical calibration beyond moments, such as finite-tail error bounds, is not established. The 2013 DNA-palindrome paper could not be inspected in full, and an independent historical-priority check has not been performed.

## References

1. F. Lillo and M. Spanò, *Inverted and mirror repeats in model nucleotide sequences*, Physical Review E 76, 041914 (2007), https://doi.org/10.1103/PhysRevE.76.041914.
2. D. Špoljarić and I. Ugrina, *On Statistical Properties of Palindromes in DNA*, Communications in Statistics—Theory and Methods 42, 1373–1385 (2013), https://doi.org/10.1080/03610926.2012.739253.
3. M. Rubinchik and A. M. Shur, *The Number of Distinct Subpalindromes in Random Words*, arXiv:1505.08043 (first posted 2015-05-29), https://arxiv.org/abs/1505.08043.
4. D. Gabric and J. Shallit, *Borders, Palindrome Prefixes, and Square Prefixes*, arXiv:1906.03689 (first posted 2019-06-09), https://arxiv.org/abs/1906.03689.
