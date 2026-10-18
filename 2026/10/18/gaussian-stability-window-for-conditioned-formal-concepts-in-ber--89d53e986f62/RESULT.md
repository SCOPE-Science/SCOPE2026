# Gaussian stability window for conditioned formal concepts in Bernoulli contexts

## Finding
Fix an incidence density \(p\in(0,1)\). For finite nonempty labelled sets of objects \(G\) and attributes \(M\), every incidence indicator is independent Bernoulli-\(p\). Fix nonempty sets \(A\subseteq G\), \(B\subseteq M\), with \(|A|=a\ge1\), \(|B|=b\ge1\), \(|G|=r\ge a\), and \(|M|=m>b\). Put \(N=m-b\ge1\). Let \(E\) denote the event that \((A,B)\) is a formal concept, and condition throughout on \(E\), which has positive probability.

Write \(X'\) for the attributes common to all objects of \(X\subseteq G\), using \(\varnothing'=M\), and define the intensional stability of \((A,B)\) by
\[
\sigma=2^{-a}\bigl|\{X\subseteq A:X'=B\}\bigr|.
\]
Its *entire conditional law* depends only on \((a,N,p)\), not on \((r,b)\). Its first two conditional moments are exactly
\[
\mathbb E(\sigma\mid E)=2^{-a}\sum_{t=0}^{a}\binom at\left(\frac{1-p^t}{1-p^a}\right)^N,
\tag{1}
\]
\[
\mathbb E(\sigma^2\mid E)=4^{-a}\sum_{S,T\subseteq A}\left(\frac{1-p^{|S|}-p^{|T|}+p^{|S\cup T|}}{1-p^a}\right)^N.
\tag{2}
\]
The variance follows by subtracting the square of (1).

Let \(h=\log N/(-\log p)\), and write \(\Phi\) for the standard Gaussian cumulative distribution function. There are constants \(a_0(p)\), \(C_p<\infty\) such that for all \(a\ge a_0(p)\) satisfying \(a/4\le h\le3a/4\),
\[
\boxed{\mathbb E\left[\left|\sigma-\Phi\!\left(\frac{a-2h}{\sqrt a}\right)\right|\,\middle|\,E\right]\le C_p\frac{\log a}{\sqrt a}.}
\tag{3}
\]
In particular, along any sequence of admissible parameter choices with \(a\to\infty\) and \((h-a/2)/(\sqrt a/2)\to z\in\mathbb R\), the conditioned stability converges in probability and in mean to \(1-\Phi(z)\). This is a *conditional* law for a fixed labelled concept candidate, not an assertion about an unconditioned uniformly chosen concept.

## Assumptions and scope
A formal context is the bipartite incidence structure \((G,M,I)\). Define \(X'=\{j\in M:\forall i\in X,\ iIj\}\) and \(Y'=\{i\in G:\forall j\in Y,\ iIj\}\). The pair \((A,B)\) is a concept exactly when \(A'=B\) and \(B'=A\). All probabilities are with respect to the independent-entry Bernoulli model; \(A,B,G,M\) are deterministic labelled sets. Both \(A\) and \(B\) are nonempty, \(N=m-b\ge1\), and \(p\) remains fixed independently of \(a\). Empty-extent, empty-intent, and \(N=0\) degenerate cases are not part of the quantitative theorem.

## Proof
**Conditioning and exact law.** The event \(E\) is the conjunction of three constraints on disjoint blocks of incidence entries: all \(ab\) entries in \(A\times B\) equal one; every column outside \(B\) has at least one zero within \(A\); every row outside \(A\) has at least one zero within \(B\). The remaining block is unrestricted. Independence therefore gives
\[
\Pr(E)=p^{ab}(1-p^a)^N(1-p^b)^{r-a}>0.
\tag{4}
\]
Conditioned on \(E\), the \(N\) column vectors restricted to \(A\) outside \(B\) are independent Bernoulli-\(p\) vectors conditioned to be *not* identically one; all other restricted entry blocks are independent of these. The indicator \(\mathbf1\{X'=B\}\) for each \(X\subseteq A\) depends only on these \(N\) truncated columns. Hence the joint law of these indicators, and the law of their average \(\sigma\), depend only on \((a,N,p)\).

For fixed \(X\subseteq A\), \(|X|=t\), a truncated column fails to be all one on \(X\) with probability \((1-p^t)/(1-p^a)\). It follows that
\[
\Pr(X'=B\mid E)=\left(\frac{1-p^t}{1-p^a}\right)^N.
\tag{5}
\]
Averaging (5) over all \(2^a\) subsets gives (1). For a pair \(S,T\subseteq A\), the probability that the column fails to be all one on *both* subsets equals \((1-p^{|S|}-p^{|T|}+p^{|S\cup T|})/(1-p^a)\), by inclusion–exclusion. Independence of the columns and averaging over the \(4^a\) ordered pairs gives (2). This second moment can alternatively be evaluated as a four-block multinomial sum using \(|S\setminus T|\), \(|T\setminus S|\), \(|S\cap T|\), and \(|A\setminus(S\cup T)|\).

**Uniform Gaussian window.** Independently choose a uniformly random subset \(U\subseteq A\), and set \(K=|U|\sim\mathrm{Bin}(a,1/2)\). Conditional on a realized context, \(\sigma=\Pr_U(U'=B)\). Let \(q_a=\Pr(K\ge h)\) and set \(w=2\log a/(-\log p)\). For \(t\ge h+w\), the union bound and (5) give
\[
\Pr(U'\ne B\mid E,K=t)\le\frac{N(p^t-p^a)}{1-p^a}\le\frac{p^w}{1-p^a}=\frac{a^{-2}}{1-p^a}.
\tag{6}
\]
For \(t\le h-w\), the inequality \(1-u\le e^{-u}\) gives
\[
\Pr(U'=B\mid E,K=t)\le
\exp\left(-\frac{Np^t-Np^a}{1-p^a}\right)
\le\exp\left(-\frac{a^2-Np^a}{1-p^a}\right).
\tag{7}
\]
The allowed range of \(h\) implies \(Np^a=p^{a-h}\le p^{a/4}\), so the right side of (7) is exponentially small in \(a^2\). The central binomial bound \(\max_t\Pr(K=t)\le C/\sqrt a\) implies
\[
\Pr(|K-h|\le w)\le C(2w+3)/\sqrt a=O_p(\log a/\sqrt a).
\tag{8}
\]
By Jensen's inequality, the mean absolute discrepancy between \(\sigma\) and \(q_a\) does not exceed \(\Pr_{E,U}(\mathbf1\{U'=B\}\ne\mathbf1\{K\ge h\})\). Partition this mismatch by the three regions in (6)–(8), obtaining
\[
\mathbb E(|\sigma-q_a|\mid E)=O_p(\log a/\sqrt a)
\]
uniformly for \(a/4\le h\le3a/4\). The uniform de Moivre–Laplace normal approximation (or Berry–Esseen for fair Bernoulli sums, including the lattice rounding error) yields
\[
\left|q_a-\Phi\!\left(\frac{a-2h}{\sqrt a}\right)\right|=O(a^{-1/2}).
\]
Combining these bounds proves (3). In the stated critical scaling the Gaussian argument tends to \(-z\), yielding the limit \(\Phi(-z)=1-\Phi(z)\). Convergence in mean follows from (3) and boundedness of \(\sigma\in[0,1]\). The finite exact formulas require no asymptotic approximations.

## Verification
Run \(\texttt{python3 verify_stability.py}\) using only the Python standard library. The checker enumerates every incidence matrix for all \(r,m\in\{1,2,3\}\) and all admissible nonempty labelled \(A,B\) with \(B\ne M\), for each \(p\in\{1/3,1/2,2/3\}\). Using exact rational weights, it compares (4), (1), and (2) against direct concept tests and exact stability values. There are 264 complete conditional test instances, and the expected output begins \(\texttt{VERIFY_OK 264}\). These finite enumerations independently test the normalizations and boundary cases but do not prove the infinite Gaussian bound; that bound is proved above.

For illustration, at \(a=2,N=1,p=1/2\), the conditioned stability takes the value \(3/4\) with probability \(1/3\) and \(1/2\) with probability \(2/3\); hence \(\mathbb E\sigma=7/12\) and \(\operatorname{Var}(\sigma)=1/72\).

## Relationship to prior work
Kuznetsov (2007) introduced and studied formal-concept stability and its combinatorial and computational properties. Zhi (2014) gives deterministic minimal-generator and inclusion–exclusion formulas for stability. Sakurai (2021) studies Bernoulli random formal contexts and exact expected *numbers of concepts*. Mouakher and Kő (2022) study efficient exact computation of stability in a given concept lattice. Buzmakov, Kuznetsov and Napoli (2014) report experiments on reproducibility of concept stability across independently sampled datasets and observed empirical asymptotic trends, without a conditional Bernoulli concentration theorem. The present conditional random-concept *stability moments* and the uniform quenched Gaussian transition (3) concern a different invariant and conditional experiment: a fixed prescribed concept is conditioned to exist, then its fraction of intent-preserving object subsets is evaluated. The general deterministic stability formulas can compute an individual instance and do not, without additional probabilistic analysis, imply (3). A separate randomized *fuzzy* context/stability model in Antoni–Krajči–Krídlo (2015) uses Gaussian fuzzy randomization rather than the fixed-density binary model. None of the material inspected established the joint conditional-moment and concentration statement; this is not proof of absolute priority.

## Limitations
This result concerns a *specified* labelled \((A,B)\) conditioned on being a concept, not stability of a uniformly sampled concept or the maximum stability over all concepts. Conditioning can be extremely rare; the theorem makes no lower bound on \(\Pr(E)\). The asymptotic assumes fixed \(p\in(0,1)\), growing \(a\), and \(N=m-b\) on the stipulated exponential scale, with no corresponding growth restriction on \(r,b\) beyond admissibility. It does not address sparse \(p=p_a\), the joint behavior of distinct conditioned concepts, or algorithmic worst-case complexity. Equivalence to an earlier result in alternate terminology cannot be ruled out; the 2022 stability-computation article's full text was unavailable for complete comparison. Independent external scientific validation has not been carried out.

## References
1. S. O. Kuznetsov, *On stability of a formal concept*, Annals of Mathematics and Artificial Intelligence 49 (2007), 101–115. DOI:10.1007/s10472-007-9053-6.
2. H.-L. Zhi, *On the Calculation of Formal Concept Stability*, Journal of Applied Mathematics (2014), Article 917639. DOI:10.1155/2014/917639.
3. T. Sakurai, *On formal concepts of random formal contexts*, arXiv:2101.11023 (first posted 2021-01-26).
4. A. Mouakher and A. Kő, *Efficient assessment of formal concept stability in the Galois lattice*, International Journal of General Systems 51 (2022), 791–821, first online 2022-07-31. DOI:10.1080/03081079.2022.2084728.
5. A. Buzmakov, S. O. Kuznetsov and A. Napoli, *Concept Stability as a Tool for Pattern Selection*, FCA4AI workshop proceedings (2014), 8 pages.
6. L. Antoni, S. Krajči and O. Krídlo, *Randomized fuzzy formal contexts and relevance of one-sided concepts*, Lecture Notes in Computer Science 9113 (2015), 183–199. DOI:10.1007/978-3-319-19545-2_12.
