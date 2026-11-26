# Exact adjacent-gap law and correlation reversals in three-term generalized Zeckendorf expansions

## Finding
Fix integers \(p,q\ge1\). Let \((H_n)\) be the positive linear recurrence sequence with coefficient word \((1,0^{p-1},1,0^{q-1},1)\) and the generalized Zeckendorf initial conditions described below. Its recurrence is
\[
H_{n+1}=H_n+H_{n-p}+H_{n-p-q}.
\]
For each integer in \([H_n,H_{n+1})\), list its legal summand indices in **decreasing** order \(j_1>\cdots>j_m\) and put \(g_i=j_i-j_{i+1}\). Pool the ordered pairs \((g_i,g_{i+1})\) over all those integers and divide by the total number of such pairs, whenever this total is positive. In particular, the total is positive for \(n\ge p+q+2\). The resulting probability measures converge pointwise to \(\nu_{p,q}\), with bivariate probability-generating function
\[
\boxed{\sum_{g,h\ge1}\nu_{p,q}(g,h)u^gv^h=
\frac{b u^p v^{q+1}K(v)+[A(u)+B(u)][A(v)+b v^p]}{1+b}.}
\]
Here \(z\in(0,1)\) is the unique solution of \(1-z=z^{p+1}+z^{p+q+1}\), and
\[
b=\frac{z^q}{1+z^q},\quad a=1-b,\quad K(t)=\frac{1-z}{1-zt},\quad A(t)=a t^{p+1}K(t),\quad B(t)=b t^{q+1}K(t).
\]
If summand indices are instead listed in increasing order, interchange \(u\) and \(v\). For either order, writing \(d=p-q\) and \(h_0=(1-z)^{-1}\), the lag-one covariance of the limiting gap pair is
\[
\boxed{\operatorname{Cov}(G,G')=-\frac{b}{(1+b)^2}(d-bh_0)(bd-h_0).}
\]
In particular, for \(q=1\) this covariance is zero at \(p=2\), strictly positive at \(p=3\), and strictly negative at \(p=20\). The bivariate law and covariance formula hold for all \(p,q\ge1\), including \(p\ge q+2\).

## Assumptions and scope
Let \(L=p+q+1\) and write the coefficient word as \(c=c_1\cdots c_L=10^{p-1}10^{q-1}1\). The initial conditions are \(H_1=1\) and \(H_{j+1}=1+\sum_{i=1}^j c_i H_{j+1-i}\) for \(1\le j<L\); the full recurrence applies for \(j\ge L\). The usual PLRS notion of legality is used: a legal word is a proper initial prefix of \(c\), or it matches \(c\) up to some digit, is strictly smaller at the next digit, and is followed by zeros and a legal suffix (possibly empty). Nonempty legal words start with 1 and are written from highest to lowest summand index. Legal length-\(n\) words represent exactly the integers in \([H_n,H_{n+1})\) by the generalized Zeckendorf theorem. Expansions with fewer than three summands contribute no pair; the normalization is by all pair occurrences, not by a per-integer ratio.

## Proof
At the first departure from \(c\) in a nonterminal part of a legal word, a unit digit is dropped at position \(p+1\) or \(L\). Include every following zero up to the next 1 (or the end of the word). The resulting full block is one of
\[
\mathsf A_k=10^{p+k},\qquad \mathsf B_k=10^{p-1}10^{q+k},\qquad k\ge0.
\]
This parsing is unique, since legality fixes the first departure and the next 1 fixes the end of the block. Conversely any concatenation of full blocks followed by a proper prefix of \(c\) is legal. The legal word \(\mathsf B_{n-(L+1)}1\) has three summands for every \(n\ge L+1\), establishing positivity of the normalization in the stated range.

The length-counting generating function is \(T(t)/(1-C(t))\), with
\[
T(t)=\sum_{j=0}^{L-1}t^j,\qquad C(t)=\frac{t^{p+1}+t^{p+q+1}}{1-t}.
\]
Here \(T\) counts terminal prefixes, including the empty one. The equation \(C(z)=1\) determines \(z\) uniquely because \(C\) increases strictly from zero to infinity on \((0,1)\). This root is simple. For \(|t|<z\), \(|C(t)|<1\); at \(|t|=z\), the equality \(C(t)=1\) requires all positive-weight monomials to have phase one. Since the allowed lengths include successive integers \(p+1,p+2\), this forces \(t=z\). Thus \(z\) is the unique pole of minimum modulus in the length-counting function.

Counting one distinguished full block with weight series \(W(t)\) gives \(T(t)W(t)/(1-C(t))^2\). Two distinguished **consecutive** full blocks of specified types or lengths give the same formula with \(W(t)\) the product of their weight series. This follows by allowing arbitrary lists of blocks to the left and right of the distinguished block or adjacent pair of blocks. The total block count corresponds to \(W(t)=C(t)\), with a nonzero double pole. Thus the length-\(n\) total block count is of order \(n z^{-n}\), whereas the word count is of order \(z^{-n}\). Ratios of marked-block counts to total block counts tend to \(W(z)\) by the leading double-pole coefficient. This gives the bulk block probabilities \(z^{p+1+k}\) and \(z^{p+q+1+k}\) for \(\mathsf A_k\) and \(\mathsf B_k\), and the product law for consecutive bulk blocks. The type probabilities are \(a=z^{p+1}/(1-z)\) and \(b=z^{p+q+1}/(1-z)\). Conditional on either type, the surplus \(k\) has probability \((1-z)z^k\). Boundary discrepancies are bounded by a constant per word, so they are negligible compared with the total block count.

In the decreasing-index order, \(\mathsf A_k\) contributes the external gap \(p+1+k\) to the next block; \(\mathsf B_k\) contributes first an internal gap \(p\) and then an external gap \(q+1+k\). Each bulk block contributes one external-to-next-first pair. Each bulk \(\mathsf B\) also contributes an internal-to-external pair. Their mean counts per full block sum to \(1+b\). The two contributions to the unnormalized PGF per block are \([A(u)+B(u)][A(v)+bv^p]\) and \(b u^p v^{q+1}K(v)\), respectively. For every fixed \((g,h)\), marking the appropriate one or two blocks proves the coefficient limit after normalization. The PGF has nonnegative coefficients, equals one at \(u=v=1\), and has geometric tails in both variables. Reversing the summand-index order reverses each consecutive pair, so the PGF is transposed.

For the covariance, the external-gap mean is \(M=p+h_0-bd\), and the first-gap mean of the next block is \(F=p+(1-b)h_0\). Both pooled marginals have mean \(\mu=(M+bp)/(1+b)\) since the only discrepancy between the first and second gap counts is at the two ends of each list. Equivalently the marginals agree by the PGF. The product moment is \([bp(q+h_0)+MF]/(1+b)\). Subtracting \(\mu^2\) gives
\[
\operatorname{Cov}(G,G')=-\frac{b}{(1+b)^2}(d-bh_0)(bd-h_0).
\]
For \((p,q)=(2,1)\), the root is \(z=(\sqrt5-1)/2\), with \(b=1-z\), giving \(bh_0=d=1\). For \((3,1)\), rational substitution brackets the root in \((2/3,7/10)\). There \(bh_0=z/(1-z^2)<2\) and \(2b<h_0\), so the covariance is positive. For \((20,1)\), rational substitution gives \(87/100<z<88/100\). Throughout that interval \(bh_0=z/(1-z^2)<19\). Also \(19z(1-z)\ge 19(88/100)(12/100)>1+88/100\), so \(19b>h_0\). Both factors in the covariance are positive and the covariance is negative.

## Verification
The supplied standard-library `check.py` enumerates length-\(n\) words by the recursive legality test, compares the set with the full-block encoding at six finite parameter triples, and checks the represented integers against \([H_n,H_{n+1})\). Its gap counts scan the word from the highest index to the lowest. It recovers the 33 single gaps of length one and 34 of length two for \((1,2,8)\) in the source paper, and checks the rational root brackets. These finite checks supplement rather than replace the pole argument above.

## Relationship to prior work
Chen, Chen, Hii and Miller study the same three-term recurrence. Their Theorems 1.6 and 1.7 give single-gap results (large-gap probabilities and a transfer-matrix formula for small gaps when \(p<q+2\)); Appendix B describes a limitation of their small-gap method for \(p\ge q+2\). Ben-Ari and Miller's general conditioned Markov model gives limiting single-gap laws in Theorems 4.1–4.2 and suggests alternative derivations of higher-dimensional laws. The explicit ordered two-gap law, its evaluation for all \(p,q\ge1\), and the particular lag-one covariance witnesses are the contributions here, not the general Markov or renewal method.

## Limitations
The limit is taken for fixed \(p,q\) with pooled successive-gap weighting. No uniform-in-parameter convergence rate, independence at the zero-covariance parameter, or full sign classification is asserted. The broad conditioned Markov construction may provide an alternative derivation; the comparison with the cited results does not settle historical priority.

## References
1. Yinxi Chen, Zongyun Chen, Brian Hii, Steven J. Miller, *Gaps for PLRS with zero coefficients*, arXiv:2610.23991v1, Theorems 1.6–1.7 and Appendix B. https://arxiv.org/html/2610.23991v1
2. Iddo Ben-Ari, Steven J. Miller, *A Probabilistic Approach to Generalized Zeckendorf Decompositions*, SIAM Journal on Discrete Mathematics 30 (2016), 1302–1332, Theorems 4.1–4.2. https://arxiv.org/pdf/1405.2379
3. Olivia Beckwith et al., *The Average Gap Distribution for Generalized Zeckendorf Decompositions*, Fibonacci Quarterly 51 (2013), 13–27. https://arxiv.org/abs/1208.5820
