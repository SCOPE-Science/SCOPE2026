# Natural-density distribution of integer anti-partial derivative multiplicities

## Finding

Fix a prime \(p\). For every positive integer \(y\), let
\[
D_p(x)=\frac{x\nu_p(x)}p,\qquad i_p(y)=\#\{x\in\mathbb Z_{>0}:D_p(x)=y\}.
\]
For \(v\ge0\), put
\[
A_{p,v}=\{a\ge1:a-1+\nu_p(a)=v\},\qquad b_a=\frac{a}{p^{\nu_p(a)}}.
\]
For the empty set, define its least common multiple to be \(1\), and set
\[
P_{p,v}(z)=\sum_{J\subseteq A_{p,v}}
  \frac{(z-1)^{|J|}}{\operatorname{lcm}\{b_a:a\in J\}}.
\]
Then for **every** integer \(r\ge0\) the natural density \(\delta_{p,r}\) of positive integers with exactly \(r\) positive integral anti-partial derivatives exists and is
\[
\boxed{\delta_{p,r}=[z^r]\sum_{v=0}^{\infty}
 \frac{p-1}{p^{v+1}}P_{p,v}(z).}
\]
This is a fully effective coefficient formula: truncation after \(v=V\) has absolute error at most \(p^{-(V+1)}\) for every coefficient. All masses \(\delta_{p,r}\) are **strictly positive** and sum to \(1\). Their first moment has the closed form
\[
\boxed{\sum_{r\ge0}r\delta_{p,r}=(p-1)\log\frac{p}{p-1}.}
\]
Moreover, for every \(r\ge1\),
\[
\boxed{\sum_{j\ge r}\delta_{p,j}\le p^{-(p^{r-1}-1)}.}
\]
Hence every exponential moment of this discrete distribution is finite. The positive-density conclusion strengthens the earlier result that every fiber multiplicity occurs infinitely often; neither existence of positive densities nor their full coefficient law is assumed from prior work.

## Assumptions and scope

All inputs and inverse images are **positive integers**, \(p\) is any fixed rational prime, and \(\nu_p\) is the usual nonnegative \(p\)-adic valuation. There are no assumptions on unproved hypotheses, and no sign choices or rational anti-derivatives are counted. For any subset \(J\) in the display, the least common multiple is taken over the corresponding **prime-to-\(p\)** integers \(b_a\). The density is taken as \(X\to\infty\) through positive integers:
\[
\delta_{p,r}=\lim_{X\to\infty}\frac1X\#\{1\le y\le X:i_p(y)=r\}.
\]
The source date for the subject is the first public version (January 28, 2022) of Emmons--Xiao's arithmetic partial derivative paper. The pertinent primary MSC2020 is \(11\mathrm A25\), explicitly recorded in their subsequent generalization.

## Proof

**1. Exact inverse multiplicity.** Write a candidate inverse image uniquely as \(x=p^a m\), with \(a\ge1\) and \(p\nmid m\), since \(y>0\) forces \(a\ge1\). Then
\[
D_p(x)=a p^{a-1}m=p^{a-1+\nu_p(a)}b_a m.
\]
Writing \(y=p^v u\) with \(p\nmid u\), the equalities \(D_p(x)=y\) are therefore equivalent to \(a\in A_{p,v}\), \(b_a\mid u\), and \(m=u/b_a\). Conversely, each such \(a\) determines precisely one positive \(x\). Thus
\[
\boxed{i_p(p^v u)=\sum_{a\in A_{p,v}}\mathbf 1_{b_a\mid u},\quad p\nmid u.}\tag{1}
\]
The set \(A_{p,v}\) is finite since \(1\le a\le v+1\), and all \(b_a\) are prime to \(p\). This proof does not assume injectivity of \(a\mapsto b_a\) (the displayed sum counts distinct exponents \(a\), as required).

**2. Conditional generating polynomial.** Fix \(v\). For any positive integer \(u\) coprime to \(p\), expand the product of indicator factors using (1):
\[
z^{i_p(p^v u)}=\prod_{a\in A_{p,v}}\left(1+(z-1)\mathbf 1_{b_a\mid u}\right)
=\sum_{J\subseteq A_{p,v}}(z-1)^{|J|}\mathbf 1_{L_J\mid u},
\]
where \(L_J=\operatorname{lcm}(b_a:a\in J)\). Because \(p\nmid L_J\), among positive integers \(u\) coprime to \(p\), the fraction divisible by \(L_J\) tends to \(1/L_J\): this follows by elementary counting modulo \(pL_J\). Averaging the last identity over these \(u\) gives exactly \(P_{p,v}(z)\). It is consequently a probability-generating polynomial with nonnegative rational coefficients summing to one, although its displayed inclusion--exclusion expansion alternates in sign.

**3. Passage to all valuation strata.** Integers satisfying \(\nu_p(y)=v\) have density \((p-1)/p^{v+1}\). Restricting to \(0\le v\le V\) gives a finite sum of periodic residue conditions and hence the polynomial
\[
G_{p,V}(z)=\sum_{v=0}^{V}\frac{p-1}{p^{v+1}}P_{p,v}(z).
\]
The omitted integers lie in \(p^{V+1}\mathbb Z\), a set of density \(p^{-(V+1)}\). Thus the limiting frequency of **each** prescribed fiber size exists by squeezing the finite-stratum densities; it is the claimed coefficient, and its truncation error is at most \(p^{-(V+1)}\). In particular the masses sum to \(1\). For complex \(|z|\le1\), each omitted conditional expectation has absolute value at most one, giving the identical uniform error bound for the series of generating functions.

**4. Closed mean.** Conditional on \(\nu_p(y)=v\), equation (1) and the residue-class count yield
\[
\mathbb E[i_p(y)\mid \nu_p(y)=v]=\sum_{a\in A_{p,v}}\frac1{b_a}.
\]
The nonnegative series can be rearranged by the distinct positive exponents \(a\). Since \(v=a-1+\nu_p(a)\) and \(b_a=a/p^{\nu_p(a)}\),
\[
\sum_{v\ge0}\frac{p-1}{p^{v+1}}\sum_{a\in A_{p,v}}\frac1{b_a}
=(p-1)\sum_{a\ge1}\frac1{ap^a}
=(p-1)\log\frac{p}{p-1}.
\]
Uniform integrability follows independently from \(i_p(y)\le 1+\lfloor\log_p(\nu_p(y)+1)\rfloor\) and the geometric valuation tail; hence this is also the limit of the finite empirical averages \(X^{-1}\sum_{y\le X}i_p(y)\), not merely a formal expectation.

**5. Strict positivity and the tail.** For \(r=0\), no positive exponent \(a\) can satisfy \(a-1+\nu_p(a)=p-1\): for \(a<p\) the left side is at most \(p-2\), and for \(a\ge p\) it is at least \(p\). Hence every integer of valuation \(p-1\) has no inverse image, giving \(\delta_{p,0}\ge(p-1)/p^p>0\).

For each \(r\ge1\), Emmons and Xiao, *The Arithmetic Partial Derivative* (2022), Theorem 21 and its constructive proof, provide a positive integer \(y_0=p^v u_0\) having exactly \(r\) integral anti-partial derivatives. In (1), let \(L=\operatorname{lcm}(b_a:a\in A_{p,v})\). Every prime-to-\(p\) integer \(u\equiv u_0\pmod L\) has the identical fiber multiplicity \(r\); this class has positive conditional density \(1/L\), and hence \(\delta_{p,r}\ge(p-1)/(p^{v+1}L)>0\). Only the established existence of one witness is used from the cited theorem; the density upgrade follows from (1).

Finally, each \(a\in A_{p,v}\) has its unique \(k=\nu_p(a)\) with \(0\le k\le\lfloor\log_p(v+1)\rfloor\), while \(a=v+1-k\) is determined by \(k\). Therefore \(i_p(y)\le1+\lfloor\log_p(v+1)\rfloor\). If \(i_p(y)\ge r\), then \(v\ge p^{r-1}-1\), whose valuation-stratum probability is \(p^{-(p^{r-1}-1)}\). This proves the tail bound. Summation by parts proves finiteness of \(\sum_r e^{tr}\delta_{p,r}\) for every real \(t\).

## Verification

The accompanying standalone Python 3 program `verify.py` uses only the standard library. It computes the rational conditional generating polynomials by exact subset--lcm inclusion--exclusion, confirms their nonnegative coefficients and normalization, tests the result against direct residue enumeration whenever the modulus is at most 200000, and independently enumerates derivatives \(D_p(x)\) for \(1\le x\le pY\) to check **every** target \(1\le y\le Y=10000\) for \(p=2,3,5,7\). The exhaustive bound \(x\le pY\) is valid for a target \(y\le Y\), since \(D_p(x)=a x/p\ge x/p\) whenever \(D_p(x)>0\). It additionally computes exact finite-valutation distributions and checks the geometric truncation mass.

For example, at \(p=2\), truncating at \(V=45\) gives, with absolute error at most \(2^{-46}\) in each reported density:
\[
(\delta_{2,0},\delta_{2,1},\delta_{2,2},\delta_{2,3})
\approx(0.349033858108,\ 0.608793981086,\ 0.042163282944,\ 0.000008877862).
\]
The exact mean is \(\log2\). These finite tests are corroboration rather than a proof of all-prime/all-index statements, which are established above.

## Relationship to prior work

Emmons and Xiao (2022) developed an explicit integral anti-partial-derivative criterion and showed that each nonnegative finite multiplicity occurs infinitely often. Their Theorem 21 supplies the existence witness needed for our positive-density assertion. The present finding instead concerns the **global natural-density distribution** of all inverse multiplicities, an effective coefficient formula, a closed first moment, and a superexponential large-multiplicity tail. In particular, this is neither a proposed new pointwise inverse criterion nor a claim of originality for existence of arbitrarily large fibers.

Their 2023 generalization studies arithmetic derivatives over \(p\)-adic and number fields and again proves existence of arbitrary finite inverse multiplicities. The inspected relevant original sections do not give this integer-input density law. The new conclusions are arithmetic averages and uniform infinite-stratum estimates that go beyond a restatement of a single fiber criterion, although the existing exact inverse classification is a strong prerequisite and may make the global results accessible by further deduction.

## Limitations

The coefficient series is effective but generally not a finite elementary closed form for individual masses; the closed elementary formula is for the **mean**. The displayed numerical probabilities are accompanied by rigorous truncation bounds but are not alleged to be rational or elementary constants. Only positive *integer* inverse images are counted, so no claim is made about rational, negative, or \(p\)-adic inverses. No independent audit has been performed. An equivalent density calculation in unindexed or inaccessible literature cannot be ruled out; the 2012 original partial-derivative source was located but its full text was not materially inspected in this investigation.

## References

1. Brad Emmons and Xiao Xiao, *The Arithmetic Partial Derivative*, arXiv:2201.12453v1 (January 28, 2022), revised v2 (June 1, 2022), *Journal of Integer Sequences* 25 (2022), Article 22.4.7; see Section 3 and Theorem 21. https://arxiv.org/html/2201.12453v2
2. Brad Emmons and Xiao Xiao, *A Generalization of Arithmetic Derivative to \(p\)-adic Fields and Number Fields*, arXiv:2307.04912v1 (July 10, 2023); see Section 2.3, primary MSC2020 11A25. https://arxiv.org/abs/2307.04912
3. Jurij Kovič, *The Arithmetic Derivative and Antiderivative*, *Journal of Integer Sequences* 15 (2012), Article 12.3.8 (background on partial derivatives; only abstract inspected). https://cs.uwaterloo.ca/journals/JIS/VOL15/Kovic/kovic4.html
