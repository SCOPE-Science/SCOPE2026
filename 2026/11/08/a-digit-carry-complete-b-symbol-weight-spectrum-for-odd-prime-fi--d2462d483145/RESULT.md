# A digit-carry complete \(b\)-symbol weight spectrum for odd-prime first-order Reed–Muller codes

## Finding

Let \(p\ge3\) be an odd prime and \(m\ge2\). For the natural base-\(p\) digit ordering of the first-order affine evaluation code \(\mathrm{RM}_p(1,m)\), the complete cyclic \(b\)-symbol weight enumerator is given for **every** window length \(1\le b\le p^m\) by

\[
\boxed{W_{p,m,b}(z)=1+(p-1)z^{p^m}+p(p-1)\sum_{j=0}^{m-1}\sum_{M\ge0}[t^M]F_{m-j-1}(t)\,z^{p^m-Z_b(p^j,p^{m-j-1},M)}.}
\]

Here

\[
F_0(t)=1,\qquad F_s(t)=(p-1+t)\prod_{k=0}^{s-2}\left(p-1+t^{(p-1)p^k}\right)\quad(s\ge1),
\]

and for positive integers \(Q,B,b\) and nonnegative integer \(M\),

\[
Z_b(Q,B,M)=\begin{cases}
B(Q-b+1)+M(b-1),&1\le b\le Q,\\
M(2Q-b+1),&Q<b\le2Q,\\
0,&b>2Q.
\end{cases}
\]

The polynomial \(F_s\) has exactly \(2^s\) distinct nonzero monomials for odd \(p\). Thus the formula simultaneously supplies exact weight values, their multiplicities (including collisions between different scales), and the entire family of weight distributions.

For example, at \(p=3\), \(m=3\), and \(b=2\),

\[
W_{3,3,2}(z)=1+6z^{19}+6z^{20}+12z^{21}+6z^{24}+12z^{25}+12z^{26}+26z^{27}.
\]

## Assumptions and scope

Identify \(\mathbb F_p\) with residues \(\{0,1,\ldots,p-1\}\). Coordinates in the code are indexed in increasing order by

\[
\operatorname{index}(x_0,\ldots,x_{m-1})=\sum_{i=0}^{m-1}x_i p^i,
\]

so \(x_0\) is the fastest-moving digit. The code consists of all \(p^{m+1}\) evaluation words of the distinct affine functions

\[
f(x)=c+\sum_{i=0}^{m-1}\lambda_i x_i\quad(c,\lambda_i\in\mathbb F_p).
\]

The cyclic \(b\)-symbol weight of a word \(v\) of length \(n=p^m\) is the number of indices \(r\in\{0,\ldots,n-1\}\) for which \((v_r,v_{r+1},\ldots,v_{r+b-1})\ne(0,\ldots,0)\); subscripts are reduced modulo \(n\). Thus the enumerator is \(W_{p,m,b}(z)=\sum_{v\in C}z^{w_b(v)}\), counting codewords, not merely distinct weight values. No claim is made for coordinate permutations, nonlinear codewords, nonprime fields, or noncyclic windows.

For the summand of index \(j\), always set \(Q=p^j\), \(s=m-j-1\), and \(B=p^s\). The polynomial coefficient \([t^M]F_s(t)\) is zero except for finitely many \(M\ge0\), so the displayed sum is finite.

## Proof

**1. Zero runs have only two sizes.** Consider a nonconstant affine function and let \(j\) be the smallest index with \(\lambda_j\ne0\). For each fixed tuple \(y=(x_{j+1},\ldots,x_{m-1})\), the evaluation word has one block of length \(pQ\); inside this block the zero symbols form exactly one consecutive subblock of length \(Q\), corresponding to

\[
r(y)=-\lambda_j^{-1}\left(c+\sum_{i=j+1}^{m-1}\lambda_i x_i\right)\pmod p.
\]

There are \(B=p^s\) such blocks. The last zero subblock of one block joins the first zero subblock of its successor exactly when \(r(y)=p-1\) and \(r(y+1)=0\), where \(y+1\) means cyclic increment of the base-\(p\) block index. Let \(M\) count these joins. A zero subblock cannot join at both ends, because its location cannot be simultaneously the first and last of the \(p\ge3\) subblocks. Consequently the cyclic zero runs comprise exactly \(B-2M\) runs of length \(Q\) and \(M\) runs of length \(2Q\). In particular \(M\le B/2\). A cyclic zero run of length \(L\) contains exactly \((L-b+1)_+\) length-\(b\) all-zero windows. Hence

\[
\#\{\text{all-zero cyclic length-}b\text{ windows}\}=(B-2M)(Q-b+1)_++M(2Q-b+1)_+=Z_b(Q,B,M).
\]

The equality with the piecewise formula follows by considering \(b\le Q\), \(Q<b\le2Q\), and \(b>2Q\). Thus \(w_b(v)=p^m-Z_b(Q,B,M)\).

**2. The constant term of an affine function does not alter the number of joins.** If some coefficient above digit \(j\) is nonzero, let \(L\) be the highest such digit relative to \(j\): \(\lambda_{j+1+L}\ne0\) and all further coefficients vanish. Shifting the block index \(y\) by \(p^L\) modulo \(p^s\) increments its \(L\)-th digit by one in \(\mathbb F_p\); any carry reaches only digits with zero coefficient. Therefore \(r_0(y+p^L)-r_0(y)=-\lambda_j^{-1}\lambda_{j+1+L}\), independent of \(y\). Repeated shifts realize any constant offset, and shifting the block-index circle preserves its adjacent-join count. Thus the join count with arbitrary \(c\) equals that with \(c=0\). If every coefficient above \(j\) vanishes, \(r\) is constant and the join count is zero for every \(c\), so the same conclusion holds.

**3. Counting joins by carried digits.** Take \(c=0\). Write

\[
h_t=-\lambda_{j+1+t}/\lambda_j\in\mathbb F_p,\qquad H_t=\sum_{i=0}^t h_i\in\mathbb F_p\qquad(0\le t<s).
\]

Then \(r(y)=\sum_{t=0}^{s-1}h_t y_t\). In the transition from a block index \(y\) to \(y+1\), suppose that exactly \(t\) low digits carry from \(p-1\) to zero, where \(0\le t<s\). Since \(-(p-1)=1\) in \(\mathbb F_p\), the jump of \(r\) is exactly \(H_t\). A join requires \(r(y)=-1\) and \(H_t=1\).

For nonzero \((h_0,\ldots,h_{s-1})\), let \(L\) be its largest nonzero position. If \(t<L\), the highest nonzero higher digit makes \(r(y)\) uniformly distributed as the higher digits vary; precisely \((p-1)p^{s-t-2}\) choices meet \(r(y)=-1\), provided \(H_t=1\). At \(t=L\), the equation becomes \(h_L(y_L+1)=0\) and is impossible because \(y_L+1\in\{1,\ldots,p-1\}\). For \(t>L\), the condition holds for every allowable higher-digit choice precisely when \(H_L=1\), yielding \((p-1)p^{s-t-1}\) joins. The wrap-around transition \(y=p^s-1\) to \(0\) contributes one further join precisely when \(H_L=1\). The geometric sum of the \(t>L\) and wrap-around terms is \(p^{s-L-1}\mathbf1_{\{H_L=1\}}\). Equivalently (expanding this sum over the constant tail \(H_t=H_L\)), for all coefficient vectors including zero,

\[
\boxed{M=\mathbf1_{\{H_{s-1}=1\}}+(p-1)\sum_{t=0}^{s-2}p^{s-t-2}\mathbf1_{\{H_t=1\}}.}
\]

When \(s=0\), the block count is one and \(M=0\), agreeing with \(F_0=1\).

**4. Exact multiplicities and the polynomial.** The change of variables \((h_0,\ldots,h_{s-1})\mapsto(H_0,\ldots,H_{s-1})\) is triangular with unit diagonal, so it is a bijection of \(\mathbb F_p^s\). For each \(t\), the event \(H_t=1\) has exactly one field value, and its complement has \(p-1\). The preceding formula therefore proves that the generating polynomial \(\sum_h t^{M(h)}\) equals

\[
(p-1+t)\prod_{t=0}^{s-2}\left(p-1+t^{(p-1)p^{s-t-2}}\right)=F_s(t).
\]

For \(p\ge3\), the successive weights \(1,p-1,(p-1)p,\ldots\) are strictly superincreasing, so all \(2^s\) choices of indicators have different sums, proving the precise number of monomials. Every fixed \(j\) has \(p-1\) choices for \(\lambda_j\), \(p^s\) tuples of higher coefficients, and \(p\) choices for \(c\), totaling \(p(p-1)p^s\) distinct codewords. Combining the \(M\)-counting polynomial with Step 1 therefore yields the summand multiplied by \(p(p-1)\). The zero affine function contributes \(1\), and the \(p-1\) nonzero constant affine functions contribute \((p-1)z^{p^m}\). Summing over all possible lowest nonzero digit \(j\) proves the theorem. At \(z=1\) the count is \(p+(p-1)p\sum_{j=0}^{m-1}p^{m-j-1}=p^{m+1}\), as required.

## Verification

The standalone Python script `verify_prime_rm.py` calculates the predicted polynomial independently from the displayed product and, separately, enumerates all affine codewords and counts cyclic all-zero windows directly from their evaluation vectors. Running `python verify_prime_rm.py` completed successfully with `PASS: 117 complete enumerator comparisons`, covering every \(b\) at dimensions through \(m=3\) for \(p=3\), through \(m=2\) for \(p=5\), and nine selected \(b\) values for \(p=5,m=3\) and \(p=7,m=2\). It also checks small binary cases as a cross-check, though the claim here is restricted to odd primes. No finite computation is relied on as an infinite proof; Steps 1–4 provide the general derivation.

## Relationship to prior work

Ma and Luo (2019) give symbol-pair distributions for simplex and variation-simplex codes and explicitly emphasize sensitivity to the coordinate arrangement; their projective/cyclic simplex constructions have different evaluation lengths and ordering, and their results do not classify these \(p^m\)-length affine truth tables. Shi, Zhu and Helleseth (2021) give general identities connecting cyclic zero-run lengths and \(b\)-symbol weight, which is used here in Step 1; their result by itself does not determine the zero-run multiset or its exact multiplicities for the specified code. Pan, Ling and Liu (2023) derive minimum \(b\)-symbol distances for Reed–Muller codes but do not provide the entire symbol-weight distribution. A separately established **binary**, least-significant-digit-first affine Reed–Muller distribution is a genuine earlier specialization and is not asserted to be novel here. The odd-prime carry formula and resulting sparse product are the contribution being assessed.

## Limitations

The code depends on the stated coordinate order: symbol-pair and \(b\)-symbol metrics generally change under permutations. The formula is restricted to prime fields and first-order affine functions and does not claim results for higher-order Reed–Muller codes or for other coordinate orderings. Finite checks are supplementary rather than a formal mechanized proof. Some equivalent description in older or unindexed literature remains possible despite targeted comparisons; no independent external scientific audit is claimed.

## References

1. Junru Ma and Jinquan Luo, *Symbol-pair Weight Distributions of Some Linear Codes*, arXiv:1911.02184v1 (first public 2019-11-06), https://arxiv.org/abs/1911.02184.
2. Minjia Shi, Hongwei Zhu and Tor Helleseth, *The connections among Hamming metric, \(b\)-symbol metric, and \(r\)-th generalized Hamming metric*, arXiv:2109.13764v1 (first public 2021-09-28), https://arxiv.org/html/2109.13764v1.
3. Xu Pan, San Ling and Hongwei Liu, *New bounds for \(b\)-Symbol Distances of Matrix Product Codes*, arXiv:2309.08920v1 (first public 2023-09-16), https://arxiv.org/abs/2309.08920.
