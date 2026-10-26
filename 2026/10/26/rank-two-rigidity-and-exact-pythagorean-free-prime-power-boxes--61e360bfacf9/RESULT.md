# Rank-two rigidity and exact Pythagorean-free prime-power boxes

## Finding
For distinct primes \(p<q\) and positive integers \(R,S\), write
\[
B_{p,q}(R,S)=\{p^a q^b:0\le a<R,\ 0\le b<S\}.
\]
A subset of this box is *Pythagorean-pair-free* if it contains no two distinct positive integers \(u,v\) for which \(u^2+v^2\) is a square; the hypotenuse need not belong to the box. Let \(F_{p,q}(R,S)\) be its largest possible cardinality.

**Theorem (complete rank-two obstruction graph).** If \((p,q)\ne(2,3)\), then \(F_{p,q}(R,S)=RS\); indeed, there is not even a single Pythagorean pair in the box. For \((p,q)=(2,3)\), the obstruction graph on exponent vectors is the disjoint union of paths on the sets \(a+2b=t\), where \(0\le t\le R+2S-3\). Put
\[
L_t=\max\left\{0,\min\left(S-1,\left\lfloor t/2\right\rfloor\right)-\max\left(0,\left\lceil\frac{t-R+1}{2}\right\rceil\right)+1\right\}.
\]
Then
\[
\boxed{F_{2,3}(R,S)=\sum_{t=0}^{R+2S-3}\left\lceil\frac{L_t}{2}\right\rceil.}
\]
Every extremal set is obtained by choosing a maximum independent vertex set separately on each of these paths. The number of extremal subsets is therefore
\[
\boxed{\prod_{\substack{0\le t\le R+2S-3\\ L_t>0\text{ even}}}(L_t/2+1).}
\]
In particular, for each \(n\ge1\), setting \(F_{p,q}(n)=F_{p,q}(n,n)\),
\[
\boxed{F_{2,3}(n)=
\begin{cases}
 n(n+1)/2,&n\equiv0\pmod4,\\
 n(n+2)/2,&n\equiv2\pmod4,\\
 (2n^2+3n-1)/4,&n\equiv1\pmod4,\\
 (2n^2+3n+1)/4,&n\equiv3\pmod4.
\end{cases}}
\]
Thus \(F_{2,3}(n)/n^2\to1/2\), whereas \(F_{p,q}(n)/n^2=1\) identically for every other pair of distinct primes.

## Assumptions and scope
The primes are distinct and ordered \(p<q\). The exponent bounds \(R,S\) are positive integers and include zero exponents, so \(1\in B_{p,q}(R,S)\). A Pythagorean obstruction concerns distinct legs only and an arbitrary integral hypotenuse. The claim does not assert a result for prime supports of size three or greater, or for more general exponent regions.

## Proof
**1. Primitive pairs.** Suppose \(u,v\) have prime support contained in \(\{p,q\}\) and \(u^2+v^2=w^2\). Divide all three quantities by \(d=\gcd(u,v)\). The new positive legs \(U,V\) are coprime and have support in \(\{p,q\}\); their hypotenuse \(W\) remains an integer because \(d\mid w\), as follows from \(d^2\mid w^2\) and valuation comparison. Two odd squares add to \(2\pmod4\), so one leg is even. Hence \(p=2\) and the other prime \(q\) is odd. The odd leg is \(q^b\), \(b\ge0\), and the even leg is \(2^a q^c\), \(a\ge1\), \(c\ge0\). If \(b=0\), the odd leg is \(1\), but \((2^a q^c)^2+1\) lies strictly between consecutive squares for \(2^a q^c\ge2\). Thus \(b\ge1\), and coprimality forces \(c=0\): the primitive legs are \(2^a,q^b\).

Now \(W\) is odd and
\[
(W-2^a)(W+2^a)=q^{2b}.
\]
Both factors are positive odd integers, have gcd dividing \(2^{a+1}\), and so are coprime. As their product is a power of one odd prime, the smaller factor must be \(1\). Therefore \(q^{2b}-1=2^{a+1}\), equivalently
\[
(q^b-1)(q^b+1)=2^{a+1}.
\]
The two positive powers of two on the left differ by \(2\); they must be \(2\) and \(4\). Hence \(q^b=3\), \(a=2\), and the *only* primitive pair with at most two prime supports is \(3,4\). Its hypotenuse is \(5\).

**2. Complete graph.** Any nonprimitive pair is a common positive multiple of \(3,4\). Because the original legs are in one two-prime box, the multiplier is \(2^i3^j\) with \(i,j\ge0\). The two exponent points are exactly \((i,j+1)\) and \((i+2,j)\), provided both are inside the box. Conversely, each such edge is valid, since \((3d)^2+(4d)^2=(5d)^2\). This proves absence of edges outside \((2,3)\) and identifies **every** edge inside it.

**3. Paths and optimization.** The translation \((a,b)\mapsto(a+2,b-1)\) preserves \(t=a+2b\). For each fixed \(t\), allowable \(b\) form the consecutive integer interval
\[
\max\left(0,\left\lceil\frac{t-R+1}{2}\right\rceil\right)
\le b\le
\min\left(S-1,\left\lfloor t/2\right\rfloor\right).
\]
Successive values of \(b\) give precisely the edges, so the component is a path of \(L_t\) vertices, including an isolated vertex when \(L_t=1\). Each path has independence number \(\lceil L_t/2\rceil\). For odd length its maximum independent set is unique; for even length \(2j\) there are exactly \(j+1\) maximum independent sets (select the \(j\) nonadjacent positions by distributing their one extra unselected position among the \(j+1\) gaps). Multiplying across disjoint components proves both formulas.

**4. Square-box closed form.** For \(R=S=n\), the coefficient sequence \(L_t\) is that of
\[
(1+z+\cdots+z^{n-1})(1+z^2+\cdots+z^{2(n-1)}).
\]
It has \(\sum_tL_t=n^2\); write \(O_n=\#\{t:L_t\text{ is odd}\}\). Pairing the coefficient sequence under \(t\leftrightarrow3n-3-t\) and counting the ascending pairs and central block yields
\[
O_n=\begin{cases}
n,&n\equiv0\pmod4,\\
2n,&n\equiv2\pmod4,\\
(3n-1)/2,&n\equiv1\pmod4,\\
(3n+1)/2,&n\equiv3\pmod4.
\end{cases}
\]
For completeness, if \(n=2m\), the two edge ramps contain each of \(1,\ldots,m-1\) four times in total, and the middle contains \(m\) on \(2m+2\) positions. If \(n=2m+1\), the ramps contain each of \(1,\ldots,m\) four times in total, and the central \(2m+1\) coefficients alternate \(m+1\) (\(m+1\) times) and \(m\) (\(m\) times). These observations give the four cases of \(O_n\). Since \(\lceil j/2\rceil=(j+\mathbf 1_{j\text{ odd}})/2\), the path sum is \((n^2+O_n)/2\), giving the stated quasi-polynomial and density limit. \(\square\)

## Verification
The accompanying `verify.py` uses exact integer arithmetic and tests every unordered pair of elements for all ten prime supports chosen from \(2,3,5,7,11\), at each \(1\le n\le9\). It compares the complete computed obstruction graph with the graph described by the theorem. It also checks the path-count formula for \(1\le n\le120\), and independently exhausts all candidate vertex subsets for \(1\le n\le4\). Execute `python3 verify.py`; expected terminal line: `CERTIFICATE_OK distinct_prime_pairs=10 supports_and_sizes=90 square_cutoffs=120 brute_independence_cutoffs=4`. The unbounded claim is proved mathematically, not inferred from these finite checks.

## Relationship to prior work
Xiao's arXiv:2610.11965v1 introduces the extremal Pythagorean-pair-free problem in prime-power boxes where both the number of primes and the exponent length equal \(N\), and proves an asymptotic upper bound as \(N\) grows. Xiao's arXiv:2610.20311v1 proves an improved asymptotic lower bound in that same growing-support regime. The present theorem instead fixes the number of prime coordinates to **two**, allows any pair of primes and arbitrary rectangular exponent cutoffs, and determines the full obstruction graph, its independence number, and its maximum-set count. Neither cited asymptotic statement supplies this exact finite-rank classification.

## Limitations
The proof is limited to two distinct prime supports and positive integer exponent cutoffs. It does not evaluate analogous extremal counts for three or more primes. The primitive-support rigidity depends on the classical factorization of a difference of squares; the contribution lies in the complete rank-two graph and exact extremal spectrum. No independent peer review is claimed. Unrecognized equivalent descriptions or earlier tables remain a literature risk.

## References
1. Rongzhong Xiao, *Pythagorean pairs in boxes of prime powers*, arXiv:2610.11965v1 (first public 2026-10-08), https://arxiv.org/abs/2610.11965.
2. Rongzhong Xiao, *Quantitative lower bound for Pythagorean pairs in boxes of prime powers*, arXiv:2610.20311v1 (first public 2026-10-14), https://arxiv.org/abs/2610.20311.
3. N. Frantzikinakis, O. Klurman and J. Moreira, *Partition regularity of generalized Pythagorean pairs*, arXiv:2407.08360, https://arxiv.org/abs/2407.08360 (background only).
