# Exact adjacent-gap law and correlation reversals in three-term generalized Zeckendorf expansions

## Finding
For each pair of integers \(p,q\ge1\), let \((H_n)\) be the positive linear recurrence sequence with coefficient word \((1,0^{p-1},1,0^{q-1},1)\), its usual generalized-Zeckendorf initial conditions, and recurrence
\[
H_{n+1}=H_n+H_{n-p}+H_{n-p-q}.
\]
For each \(n\), pool the ordered pairs of *successive* gaps between nonzero summand indices in the unique legal expansions of all integers in \([H_n,H_{n+1})\). Divide their two-gap counts by the total number of successive-gap pairs, obtaining a probability measure \(\nu_n\) on positive-integer pairs. The measure converges pointwise to \(\nu_{p,q}\), with the following explicit bivariate probability-generating function:
\[
\boxed{\sum_{g,h\ge1}\nu_{p,q}(g,h)u^gv^h=
\frac{b u^p v^{q+1}K(v)+[A(u)+B(u)][A(v)+b v^p]}{1+b}.}
\]
Here \(z\in(0,1)\) is the unique solution of \(1-z=z^{p+1}+z^{p+q+1}\), and
\[
b=\frac{z^q}{1+z^q},\quad a=1-b,\quad K(t)=\frac{1-z}{1-zt},\quad A(t)=a t^{p+1}K(t),\quad B(t)=b t^{q+1}K(t).
\]
The expression is valid for all \(p,q\ge1\), including \(p\ge q+2\). In particular, if \(G,G'\) denote an ordered adjacent gap pair under \(\nu_{p,q}\), put \(d=p-q\) and \(h_0=(1-z)^{-1}\). Then the exact covariance is
\[
\boxed{\operatorname{Cov}(G,G')=-\frac{b}{(1+b)^2}(d-bh_0)(bd-h_0).}
\]
For the fixed second spacing \(q=1\), the covariance is exactly zero when \(p=2\), strictly positive when \(p=3\), and strictly negative when \(p=20\). Thus successive summand gaps of these recurrences exhibit rigorously distinct zero, positive, and negative lag-one covariance phases.

## Assumptions and scope
The coefficients \(H_n\) are fixed by \(H_1=1\), \(H_{j+1}=\sum_{i=1}^j c_i H_{j+1-i}+1\) for \(1\le j<p+q+1\), and the displayed recurrence thereafter, with \(c_1=c_{p+1}=c_{p+q+1}=1\) and other coefficients zero. A legal digit string has the standard PLRS meaning: it is a proper initial prefix of the coefficient word, or it first matches the coefficient word, becomes strictly smaller at the next digit, then has zero digits until the next legal nonempty suffix. Since coefficients are zero or one, all legal digits belong to \(\{0,1\}\). Gap size means difference between the indices of consecutive summands, and a *pair* means two successive such differences, not two arbitrary differences. When an expansion contains fewer than three summands it contributes no gap pair. The pooled count normalization is used, not an unnormalized expectation of a per-integer ratio.

## Proof
Write \(L=p+q+1\) and the coefficient word as \(c=10^{p-1}10^{q-1}1\). At the first departure of a legal word from \(c\), the dropped unit coefficient is at position \(p+1\) or \(L\). Up to the next nonzero digit, the resulting full block is therefore exactly one of
\[
\mathsf A_k=10^{p+k},\qquad \mathsf B_k=10^{p-1}10^{q+k}\qquad (k\ge0).
\]
Conversely a concatenation of these full blocks followed by a proper prefix of \(c\) is legal, and the decomposition into blocks and terminal prefix is unique. There are \(L\) possible terminal prefixes, including empty, of lengths \(0,1,\ldots,L-1\). Consequently the length-enumerating generating function for legal words, including the empty word, is
\[
\frac{T(t)}{1-C(t)},\qquad T(t)=\sum_{j=0}^{L-1}t^j,\quad C(t)=\frac{t^{p+1}+t^{p+q+1}}{1-t}.
\]
The equation \(C(z)=1\) uniquely determines \(z\in(0,1)\). The pole is simple, and it is the sole singularity of minimum modulus: nonnegative block weights and the consecutive allowed lengths \(p+1,p+2,\ldots\) force aperiodicity. Differentiation of the geometric series of blocks shows that a uniformly counted full block in the bulk has limiting mass \(z^{p+1+k}\) for \(\mathsf A_k\), or \(z^{p+q+1+k}\) for \(\mathsf B_k\). These masses sum to one. In particular, its type is \(\mathsf A\) with probability \(a=(z^{p+1})/(1-z)\) and \(\mathsf B\) with probability \(b=(z^{p+q+1})/(1-z)\); equivalently \(b=z^q/(1+z^q)\). Conditional on either type, \(k\) has law \((1-z)z^k\). Finite collections of consecutive bulk blocks have the limiting product law, by marking those blocks in the rational generating function; the terminal prefix has a vanishing fraction of all occurrences. More concretely, one marked full block gives the double-pole term \(T(t)W(t)/(1-C(t))^2\); two marked consecutive blocks give the analogous term with their weight product. Coefficient extraction at the simple pole \(t=z\), followed by division by the total block count, yields the stated product law without asserting that finite strings consist of independent blocks.

Each \(\mathsf A_k\) has one unit digit and contributes the *external* gap \(p+1+k\) to the next block. Each \(\mathsf B_k\) has two unit digits, with an *internal* gap \(p\) and an external gap \(q+1+k\). Every bulk block contributes one external-to-next-first ordered gap pair; every \(\mathsf B\) block contributes one additional internal-to-external ordered pair. The mean number of such pairs per block is \(1+b\). For the internal-to-external pairs, the generating-function contribution is \(b u^p v^{q+1}K(v)\). For external-to-next-first pairs, the contribution is the product \([A(u)+B(u)][A(v)+bv^p]\). Their sum divided by \(1+b\) proves the boxed bivariate law. Its evaluation at \(u=v=1\) equals one, so it is indeed a probability law. The root's geometric tails guarantee all required moments exist.

For the covariance, set \(h_0=(1-z)^{-1}\). The mean external gap is \(D=p+1+(h_0-1)+b(q-p)\), and the mean first gap of the next block is \(F=(1-b)(p+h_0)+bp\). There are \(b\) internal-to-external pairs per block with mean product \(p(q+h_0)\), and one external-to-next-first pair per block with mean product \(DF\). The common marginal mean of a gap is \(\mu=(D+bp)/(1+b)\). Thus
\[
\operatorname{Cov}(G,G')=\frac{bp(q+h_0)+DF}{1+b}-\mu^2
=-\frac{b}{(1+b)^2}(p-q-bh_0)(b(p-q)-h_0),
\]
by expansion and cancellation.

For \((p,q)=(2,1)\), the root is \(z=(\sqrt5-1)/2\) and \(b=1-z\), so \(bh_0=1=p-q\): the covariance vanishes. For \((3,1)\), direct rational substitution in the root equation gives \(2/3<z<7/10\). Throughout that interval, \(2>z/(1-z^2)=bh_0\), while \(2b<h_0\); the covariance is strictly positive. For \((20,1)\), rational substitution gives \(87/100<z<88/100\); throughout that interval \(19>z/(1-z^2)=bh_0\) and \(19z(1-z)>1+z\), equivalently \(19b>h_0\). The covariance is strictly negative. These rational brackets establish the signs without numerical approximations.

## Verification
The supplied self-contained `check.py` independently enumerates binary words using the recursive legal-word definition, checks their integer values give precisely \([H_n,H_{n+1})\), and compares with the full-block encoding for six fixed \((p,q,n)\) triples, including the previously untreated \(p\ge q+2\) domain. For \((1,2,8)\) it also recovers the source paper's 33 single gaps of length one and 34 of length two. Exact rational arithmetic certifies the displayed root brackets and covariance signs. Running `python3 check.py` gave `VERIFY_OK`. The infinite limit is proved by coefficient extraction and is not inferred from these finite experiments.

## Relationship to prior work
Chen, Chen, Hii and Miller (2026) study the same three-term recurrence. Their Theorems 1.6 and 1.7 determine large-gap probabilities and a transfer-matrix formula for single small-gap probabilities when \(p<q+2\), and Appendix B explicitly notes a difficulty in the remaining range. Neither states the two-variable adjacent-gap law or its covariance sign reversal. Ben-Ari and Miller (2016), Theorems 4.1–4.2, obtain general limiting *single-gap* distributions through a Markov model. Their Markov construction in principle determines higher-dimensional statistics, so this exact evaluation is not claimed to invent the Markov/renewal principle. The contribution asserted here is the uniform explicit rational two-gap distribution for this recurrence and the resulting sign reversal, not a general finite-state existence theorem.

## Limitations
The convergence proved is for pooled successive-gap pairs at fixed \(p,q\). There is no uniform-in-parameter rate, assertion of independence at the zero-covariance parameter, or classification of every covariance sign. The broad 2016 finite-state representation may provide an alternative derivation; this is a genuine originality-overlap risk even though the explicit bivariate evaluation and phase witnesses were not located in the inspected statements. An unindexed source may already tabulate these pair correlations. No independent audit has been performed.

## References
1. Yinxi Chen, Zongyun Chen, Brian Hii, Steven J. Miller, *Gaps for PLRS with zero coefficients*, arXiv:2610.23991v1, first posted 2026-10-14, Theorems 1.6–1.7 and Appendix B. https://arxiv.org/html/2610.23991v1
2. Iddo Ben-Ari, Steven J. Miller, *A Probabilistic Approach to Generalized Zeckendorf Decompositions*, SIAM Journal on Discrete Mathematics 30 (2016), 1302–1332, Theorems 4.1–4.2. https://arxiv.org/pdf/1405.2379
3. Olivia Beckwith et al., *The Average Gap Distribution for Generalized Zeckendorf Decompositions*, Fibonacci Quarterly 51 (2013), 13–27. https://arxiv.org/abs/1208.5820
