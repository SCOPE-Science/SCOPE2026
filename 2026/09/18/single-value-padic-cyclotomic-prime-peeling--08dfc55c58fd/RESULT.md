# Single-value p-adic peeling of cyclotomic index radicals

## Statement

Let \(n>1\), put
\[
r=\operatorname{rad}(n),\qquad a=\frac nr,
\]
and let \(x\in\mathbb Z\setminus\{0\}\). Fix a prime \(\ell\mid x\), write
\[
w=\nu_\ell(x),
\]
and set
\[
C=\Phi_n(x).
\]

The local radical identity
\[
\nu_\ell(C-1)=aw
\]
recovers \(a\), and hence \(r=n/a\), from the single evaluation \(C\).

The following gives a prime-by-prime refinement.

**Theorem (single-value local peeling).** Assume that \(\mu(r)\) is known. Let
\[
p_1<p_2<\cdots<p_s
\]
be the distinct prime divisors of \(r\). For \(0\le j<s\), put
\[
P_j=\prod_{i=1}^j p_i,\qquad P_0=1,
\]
and define the rational \(\ell\)-adic unit
\[
R_j
=
C\prod_{d\mid P_j}
\left(1-x^{ad}\right)^{-\mu(r/d)}.
\]
Then
\[
\boxed{\nu_\ell(R_j-1)=aw\,p_{j+1}.}
\]
Equivalently,
\[
\boxed{p_{j+1}=\frac{\nu_\ell(R_j-1)}{aw}.}
\]
Every denominator occurring in \(R_j\) is prime to \(\ell\), so the valuation is well defined.

Moreover, \(\mu(r)\) itself is recoverable from \(C\) whenever either

1. \(\ell\) is odd, or
2. \(\ell=2\) and \(aw\ge2\).

Indeed, with
\[
U=\frac{C-1}{x^a}\in\mathbb Z,
\]
one has
\[
U\equiv-\mu(r)\pmod\ell
\]
for odd \(\ell\), while if \(\ell=2\) and \(aw\ge2\),
\[
U\equiv-\mu(r)\pmod4.
\]

Consequently, under either condition above, the single cyclotomic value
\[
\Phi_n(x)
\]
together with the known index \(n\) and base \(x\) gives an explicit factorization-free recursion that returns all distinct prime divisors of \(n\) in increasing order. No further cyclotomic evaluation is needed.

Three useful specializations are immediate:

- for every \(n>1\), the single value \(\Phi_n(3)\) gives the full radical by \(3\)-adic peeling;
- for every \(n>1\), the single value \(\Phi_n(4)\) gives the full radical by \(2\)-adic peeling;
- for every nonsquarefree \(n>1\), the single binary value \(\Phi_n(2)\) gives the full radical by \(2\)-adic peeling.

The last point is complementary to the binary plus-extractor of Shunia: for nonsquarefree \(n\), that extractor has
\[
\nu_2(\Phi_n(2)+1)=1,
\]
whereas the normalized residuals \(R_j\) above recover every distinct prime factor.

## Proof

### 1. Radical reduction and the first local scale

The classical radical reduction is
\[
\Phi_n(X)=\Phi_r(X^a).
\]
For squarefree \(r>1\), the Möbius product gives
\[
\Phi_r(Y)
=
\prod_{d\mid r}(1-Y^d)^{\mu(r/d)}.
\]
Its first term at the origin is
\[
\Phi_r(Y)=1-\mu(r)Y+Y^2H_r(Y)
\]
for some \(H_r\in\mathbb Z[Y]\). Substituting \(Y=x^a\),
\[
C-1
=
x^a\left(-\mu(r)+x^aH_r(x^a)\right).
\]
Because \(\ell\mid x\) and \(\mu(r)=\pm1\), the parenthesized factor is an \(\ell\)-adic unit. Hence
\[
\nu_\ell(C-1)=a\nu_\ell(x)=aw.
\]

The same expansion gives
\[
U=\frac{C-1}{x^a}
=
-\mu(r)+x^aH_r(x^a).
\]
If \(\ell\) is odd, reduction modulo \(\ell\) distinguishes \(+1\) from \(-1\), so \(U\bmod\ell\) determines \(\mu(r)\). If \(\ell=2\) and \(aw\ge2\), then \(4\mid x^a\), so reduction modulo \(4\) again distinguishes the two signs.

### 2. Removing the already recovered divisor lattice

From the Möbius product after radical reduction,
\[
C
=
\prod_{d\mid r}
(1-x^{ad})^{\mu(r/d)}.
\]
For \(P_j=p_1\cdots p_j\), multiplication by the inverse factors with \(d\mid P_j\) leaves
\[
R_j
=
\prod_{\substack{d\mid r\\d\nmid P_j}}
(1-x^{ad})^{\mu(r/d)}.
\]
Here \(d\nmid P_j\) means that \(d\) contains at least one unrecovered prime divisor of \(r\).

Among all such \(d\), the unique smallest one is \(p_{j+1}\): every remaining divisor contains \(p_{j+1}\) or a larger unrecovered prime, while any product with an already recovered prime is larger than \(p_{j+1}\).

Set \(q=p_{j+1}\). The factor indexed by \(q\) has expansion
\[
(1-x^{aq})^{\mu(r/q)}
=
1-\mu(r/q)x^{aq}+O_\ell(x^{2aq}),
\]
while every other remaining divisor \(d\) satisfies \(d>q\). Therefore
\[
R_j
=
1-\mu(r/q)x^{aq}+x^{aq}E
\]
with \(E\in\ell\mathbb Z_\ell\). Since \(\mu(r/q)=\pm1\),
\[
\frac{R_j-1}{x^{aq}}
\]
is an \(\ell\)-adic unit. Thus
\[
\nu_\ell(R_j-1)=aq\,\nu_\ell(x)=awq,
\]
which proves the peeling formula.

Finally, after \(\mu(r)\) is known, all exponents needed in the normalization are known without factoring the unrecovered part: since \(r\) is squarefree and \(d\mid P_j\),
\[
\mu(r/d)=\mu(r)\mu(d).
\]
The recursion therefore depends only on \(C,n,x,\ell\) and the primes already returned. It stops when their product is \(r=n/a\).

## Examples

For \(n=900\) and \(x=2\),
\[
\Phi_{900}(2)
=
1766847066423888886904503541470640004349646523777212942116503594152755201.
\]
The first local valuation gives
\[
a=\nu_2(\Phi_{900}(2)-1)=30,
\qquad
r=900/30=30.
\]
Since \(a\ge2\), the normalized unit determines \(\mu(30)=-1\). The successive residual valuations then return
\[
2,\ 3,\ 5.
\]

For the squarefree index \(n=105\), the base \(x=3\) avoids the binary sign ambiguity. From the single value
\[
\Phi_{105}(3)=114691588192970532438241
\]
the \(3\)-adic recursion gives
\[
3,\ 5,\ 7.
\]

For \(n=30\) and \(x=4\), the condition \(aw\ge2\) holds even though \(n\) is squarefree, because \(\nu_2(4)=2\). The same recursion recovers
\[
2,\ 3,\ 5.
\]

## Verification

The accompanying program uses exact rational arithmetic and SymPy 1.14.0 cyclotomic values. It checks the theorem for every \(2\le n\le120\) at the bases \(x=3,4,5\), and additionally at \(x=2\) for every nonsquarefree \(n\) in the same range. In all checked cases the recursively recovered prime list equals the exact prime support of \(n\).

This computation is a regression check; the result is proved by the Möbius-product argument above.

## Relation to prior work

Shunia, *Cyclotomic Prime Extractors* (arXiv:2609.18480v1, submitted 16 September 2026), proves the local radical identity
\[
\nu_\ell(\Phi_n(x)-1)=\frac{n}{\operatorname{rad}(n)}\nu_\ell(x),
\]
and at the binary base proves
\[
\nu_2(\Phi_n(2)+1)
=
\begin{cases}
\operatorname{lpf}(n),&n\text{ squarefree},\\
1,&n\text{ nonsquarefree}.
\end{cases}
\]
For squarefree indices, that paper also gives factor stripping by repeated use of the binary plus-extractor, and separately develops Archimedean factor-peeling formulas from normalized cyclotomic values.

The theorem here is different: it gives a purely local \(p\)-adic recursion for every successive prime factor after normalization by already recovered divisor factors; it works at arbitrary bases having a suitable prime divisor, and in particular gives complete prime peeling from a single binary value for nonsquarefree indices, where the unnormalized binary plus-valuation is identically \(1\).

Pomerance and Rubinstein-Salzedo, *Cyclotomic Coincidences* (Experimental Mathematics 31 (2022), 596--605; arXiv:1903.01962), provide the classical Möbius product, radical reduction, and first-gap/Archimedean estimates used in the recent extractor literature. Those results do not state the residual \(p\)-adic recursion above.

Originality is claimed only to the best of our knowledge. Searches for p-adic cyclotomic factor stripping, normalized residual valuations, recovery of the prime support of the index from one cyclotomic value, and equivalent Möbius-product formulations did not locate this recursive theorem. The motivating preprint is extremely recent, so unindexed contemporaneous work remains a residual risk.

## Limitations

The result assumes the index \(n\) and base \(x\) are known; it is an extractor for the prime support of the index, not an inversion theorem recovering an unknown index from an unlabeled integer.

At the binary base \(x=2\), the sign extraction used here does not cover squarefree \(n\), because then \(a\nu_2(x)=1\). Shunia's binary least-prime theorem and its other peeling methods remain available in that regime. The new single-value binary corollary asserted here is therefore restricted to nonsquarefree indices.

No claim is made that these identities yield a competitive integer-factorization algorithm: evaluating \(\Phi_n(x)\) for a large unfactored index is itself a separate computational problem.
