# Joint one-step descendant spectra for length-one and length-two tandem duplication

## Finding

Let \(q\ge2\), \(n\ge2\), and \(w\in\Sigma^n\), where \(|\Sigma|=q\). Write \(B_1(w)\) and \(B_2(w)\) for the numbers of **distinct** words obtained by duplicating precisely one contiguous factor of length one or two, respectively. The exact joint enumerator is

\[
F_{q,n}(x,y):=\sum_{w\in\Sigma^n}x^{B_1(w)-1}y^{B_2(w)-1}
=q\begin{pmatrix}1&(q-1)x\end{pmatrix}
\begin{pmatrix}1&(q-1)xy\\y&x(1+(q-2)y)\end{pmatrix}^{n-2}
\begin{pmatrix}1\\1\end{pmatrix}.
\]

Consequently, for uniform \(W\in\Sigma^n\) the marginal variables \(B_1(W)-1\) and \(B_2(W)-1\) are binomial with parameters \((n-1,(q-1)/q)\) and \((n-2,(q-1)/q)\), respectively. **Their covariance is exactly zero, but they are not independent for any \(n\ge3\).** More precisely, for \(L=n-1\) and every \(0\le k\le L\),

\[
\mathbb E[B_2(W)-1\mid B_1(W)-1=k]
=\frac{2k(L-k)+\frac{q-2}{q-1}k(k-1)}{L}.
\]

The union of the two one-step channels is disjoint by output length, so its size \(S(w)=B_1(w)+B_2(w)\) has

\[
\mathbb E S(W)=2+(2n-3)\frac{q-1}{q},\qquad
\operatorname{Var}S(W)=(2n-3)\frac{q-1}{q^2}.
\]

The minimum \(S(w)=2\) is attained by exactly \(q\) constant words. For \(q\ge3\), the maximum is \(2n-1\), attained by precisely \(q(q-1)(q-2)^{n-2}\) words. For the binary alphabet the maximum instead is

\[
\max_w S(w)=2+\left\lfloor\frac{3n-4}{2}\right\rfloor,
\]

attained by exactly two words if \(n\) is even, and exactly \(n+3\) words if \(n\) is odd.

## Assumptions and scope

The alphabet has \(q\ge2\) labeled letters. The source length is \(n\ge2\). A tandem duplication replaces \(uvz\) with \(uvvz\), with \(|v|=1\) or \(|v|=2\) and exactly one duplication; duplicate outcomes are counted only once within each length. Only distinct exact-one descendants are counted: the result does not concern substitution, reverse-complement duplication, multiple duplications, or deduplication ancestors. Matrix multiplication is over the polynomial ring \(\mathbb Z[x,y]\); a power of zero is the identity.

## Proof

**Distinct descendant counts.** Identify the alphabet bijectively with \(\mathbb Z/q\mathbb Z\), without imposing a semantic order. For each \(\ell\in\{1,2\}\) define the injective fixed-length difference encoding

\[
\phi_\ell(w)=(w_1,\ldots,w_\ell;d_1,\ldots,d_{n-\ell}),\qquad d_i=w_{i+\ell}-w_i\pmod q.
\]

The leading \(\ell\) symbols and the differences determine the whole word successively. Duplicating the block starting at index \(i+1\) inserts \(\ell\) consecutive zeros in the difference string after its first \(i\) entries, with its leading \(\ell\) letters unchanged. Insertions of identical zero blocks at two cuts of a difference string yield the same encoded word if and only if every intervening original difference entry is zero. Thus its \(n-\ell+1\) cuts partition into \(1+\#\{i:d_i\ne0\}\) distinct outputs, proving

\[
B_1(w)=1+\sum_{i=1}^{n-1}{\bf1}_{w_i\ne w_{i+1}},\qquad
B_2(w)=1+\sum_{i=1}^{n-2}{\bf1}_{w_i\ne w_{i+2}}.
\]

**Joint transfer.** Let the current state record whether the last two symbols are equal (state E) or different (state D). The first two letters contribute the weighted counts \(q\) and \(q(q-1)x\). Appending one letter to state E allows one equal continuation of weight \(1\), or \(q-1\) unequal continuations, each of weight \(xy\). From state D there is one continuation equal to the preceding letter, weight \(y\); one continuation equal to the letter two places back, weight \(x\); and \(q-2\) other continuations, each of weight \(xy\). The transfer matrix therefore is precisely the stated matrix. After \(n-2\) steps, summing both terminal states proves the polynomial identity. Its \(x^a y^b\) coefficient is the exact number of sources with \((B_1,B_2)=(a+1,b+1)\).

**Moments and conditional law.** On a uniform independent-letter word, the equality/inequality indicators along the edges of any forest are jointly independent Bernoulli variables with inequality parameter \(p=(q-1)/q\): reveal one root symbol per tree, then each successive symbol has one equality choice and \(q-1\) inequality choices independently. The distance-one edges form one path, and distance-two edges form two paths. This proves both binomial marginals. Any one distance-one edge and one distance-two edge meet in at most one vertex; their inequality indicators are therefore independent. Summing these pairwise covariances proves covariance zero and the formulas for \(S\). In contrast, \(B_1=1\) forces the word to be constant and hence \(B_2=1\), while \(\Pr(B_2=1)=q^{-(n-2)}<1\) whenever \(n\ge3\): the two variables are not independent.

For the conditional formula, write \(L=n-1\) and let \(K=B_1-1\). Conditional on \(K=k\), the locations of the \(k\) adjacent inequalities are a uniformly chosen \(k\)-subset of the \(L\) edge locations. Each distance-two inequality involves two successive adjacent edges. If exactly one of them is an inequality, the distance-two inequality occurs certainly; if neither is, it does not occur; if both are, it occurs with probability \((q-2)/(q-1)\), since among the \(q-1\) choices for the next symbol differing from the current one, precisely one equals the symbol two places earlier. The expected counts of positions with exactly one and with two adjacent inequalities are respectively \(2k(L-k)/L\) and \(k(k-1)/L\), by sampling without replacement. Summing these contributions proves the displayed conditional expectation, including \(n=2\).

**Extremes.** Each descendant count is at least one; both attain one together only when all adjacent letters agree, giving \(q\) constant words. For \(q\ge3\), both indicators in every summand can equal one: choose the first symbol in \(q\) ways, the second differently in \(q-1\) ways, and thereafter choose every new symbol different from both preceding symbols in \(q-2\) ways. These and only these sources attain \(B_1=n\), \(B_2=n-1\), hence \(S=2n-1\).

For \(q=2\), form the adjacent difference bits \(e_i=w_i\mathbin{\oplus}w_{i+1}\), \(1\le i\le L=n-1\). The two counts above give

\[
S(w)-2=\sum_{i=1}^{L}e_i+\sum_{i=1}^{L-1}(e_i\mathbin{\oplus}e_{i+1})
=\frac{e_1+e_L}{2}+\sum_{i=1}^{L-1}h(e_i,e_{i+1}),
\]

where \(h(0,0)=0\), \(h(1,1)=1\), and \(h(0,1)=h(1,0)=3/2\). Every edge contributes at most \(3/2\) and the endpoints contribute at most one, so the integer total is at most \(\lfloor(3L-1)/2\rfloor\). If \(L\) is odd, equality requires both endpoints one and every edge alternating, forcing the unique derivative \(101\cdots01\). If \(L\) is even, equality requires either perfect alternation (two derivatives) or both endpoints one and exactly one adjacent \(11\) edge with all other edges alternating (exactly \(L/2\) derivatives). These attain the bound; adjacent \(00\) edges or additional \(11\) edges reduce the total. Each derivative determines exactly two binary source words, by freely choosing the first source bit. For even \(n\) this gives two maxima; for odd \(n\) it gives \(2(2+L/2)=n+3\) maxima. Replacing \(L\) with \(n-1\) proves the binary expression.

## Verification

The standalone `verify.py` reconstructs both distinct descendant sets by direct substring duplication, not by a difference encoding; it compares their sizes with both local indicator formulas and the independent transfer polynomial, then independently checks exact extrema, extremizer counts, covariance, and the conditional mean with integer arithmetic. It exhausts all words for \(q=2\), \(2\le n\le12\); \(q=3\), \(2\le n\le8\); \(q=4\), \(2\le n\le6\); and \(q=5\), \(2\le n\le5\). The checked total is \(27381\) source words. All unbounded conclusions follow from the preceding proofs; finite checks are supplementary.

## Relationship to prior work

Yehezkeally and Schwartz's uniform tandem-duplication reconstruction theory uses the injective difference transform for a **fixed duplication length**, providing the standard underlying idea for the single-length descendant-count identities. Their 2018 paper develops reconstruction-code bounds and descendant cone geometry, but its inspected definitions and principal results do not supply the mixed length-one/length-two joint enumerator, nonlinear conditional dependence, or the alphabet-dependent sharp maxima above. The earlier bounded-window coding work of Jain, Farnoud, Schwartz and Bruck treats duplications of length at most two, including optimal *error-correcting codes* and unique roots, but not this per-source joint output-size distribution. Their 2020 follow-up treats list-decoding for fixed-length duplication, explicitly contrasting this with channels allowing more than one duplication length. The present contribution is the **joint** spectrum and its dependence/extremal laws, not a claim that the derivative encoding or single-length sphere identities are new.

## Limitations

The formulas apply only to exact one-step tandem duplication of block length one or two, uniform source sampling when probabilities are used, and alphabets with at least two symbols. They do not imply independence from zero covariance, and do not give a joint law for other duplication lengths or for a sequence of two or more events. Relevant unindexed literature may contain an equivalent two-length refinement; an independent literature and proof audit has not been performed.

## References

1. Y. Yehezkeally and M. Schwartz, *Reconstruction Codes for DNA Sequences with Uniform Tandem-Duplication Errors*, first public arXiv version 2018-01-18, arXiv:1801.06022, https://arxiv.org/abs/1801.06022.
2. S. Jain, F. Farnoud, M. Schwartz and J. Bruck, *Duplication-Correcting Codes for Data Storage in the DNA of Living Organisms*, arXiv:1606.00397, https://arxiv.org/abs/1606.00397 (supporting earlier bounded-window coding theory, not the literature date anchor).
3. Y. Yehezkeally and M. Schwartz, *Uncertainty of Reconstruction with List-Decoding from Uniform-Tandem-Duplication Noise*, first public arXiv version 2020-01-20, arXiv:2001.07047, https://arxiv.org/abs/2001.07047.
