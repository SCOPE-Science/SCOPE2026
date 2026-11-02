# Sharp arithmetic-progression occupancy and quadratic complexity for pure-power indicators

## Finding
Fix an integer base \(b\ge2\), and let \(c_b:\mathbb N_0\to\{0,1\}\) be the automatic binary word
\[
c_b(t)=\begin{cases}1,&t+1=b^a\text{ for some }a\in\mathbb N_0,\\0,&\text{otherwise}.\end{cases}
\]
For integers \(n\ge1\), \(s\ge0\), and \(d\ge1\), call \(x=(c_b(s+jd))_{0\le j<n}\) an arithmetic-progression factor. Let \(H_b(n)\) be its largest possible number of ones, and let \(P_b(n)\) count all distinct such length-\(n\) factors. Set
\[
G_r=\frac{b^{r-1}-1}{b-1}=\sum_{t=0}^{r-2}b^t\qquad(r\ge1),
\]
where the empty sum is zero. Then, for every \(n\ge1\),
\[
\boxed{H_b(n)=1+\left\lfloor\log_b\bigl((b-1)(n-1)+1\bigr)\right\rfloor.}
\]
At every critical length \(n=1+G_r\) (\(r\ge1\)), there is **exactly one** arithmetic-progression factor with \(r\) ones: it has ones precisely at zero-based indices \(G_1,G_2,\ldots,G_r\).

Furthermore \(P_b(1)=2\), and for every \(n\ge2\), writing \(L=\lfloor\log_b(n-1)\rfloor\),
\[
\boxed{P_b(n)\le1+n+\binom n2+\sum_{f=1}^{L}\sum_{j=1}^{n-1}\left\lceil\frac{j}{b^f}\right\rceil.}
\]
In particular,
\[
P_b(n)\le1+n+\binom n2+\frac{n(n-1)}{2(b-1)}+(n-1)\lfloor\log_b(n-1)\rfloor,
\]
and therefore
\[
\boxed{P_b(n)=O_b(n^2),\qquad\limsup_{n\to\infty}\frac{P_b(n)}{n^2}\le\frac{b}{2(b-1)}.}
\]
The quadratic assertion is an upper bound, **not** a claim of quadratic growth or an exact formula for \(P_b(n)\).

## Assumptions and scope
Indices begin at zero, the sampled progression has strictly positive integer step, and the sampled start is nonnegative. The powers include \(b^0=1\). Distinct factors are distinguished as binary words, not by the parameters generating them. Both the sharp occupancy theorem and the complexity bound hold simultaneously for every integer base \(b\ge2\). The factorial, logarithm and binomial notations have their usual real/integer meanings; \(\log_b\) is the real logarithm to base \(b\). The value of the empty finite sum at \(r=1\) is zero.

## Proof
**Normalized power-difference lemma.** Suppose a progression contains \(r\ge2\) ones at indices \(0\le i_1<\cdots<i_r<n\), corresponding respectively to powers \(b^{a_1}<\cdots<b^{a_r}\). Set \(f_j=a_j-a_1\) for \(j\ge2\), and \(g=\gcd(f_2,\ldots,f_r)\). Since the progression step \(d\) divides every difference \(b^{a_j}-b^{a_1}\),
\[
d\mid b^{a_1}\gcd_{j\ge2}(b^{f_j}-1)=b^{a_1}(b^g-1).
\]
The equality is the elementary power-difference gcd identity, obtained by the integer Euclidean algorithm from \(\gcd(b^u-1,b^v-1)=b^{\gcd(u,v)}-1\). Consequently,
\[
i_r-i_1=\frac{b^{a_1}(b^{f_r}-1)}d
\ge\frac{b^{f_r}-1}{b^g-1}
=\sum_{t=0}^{f_r/g-1}b^{gt}.
\]
The \(f_j\) are strictly increasing multiples of \(g\), so \(f_r/g\ge r-1\), whence
\[
i_r-i_1\ge\sum_{t=0}^{r-2}b^{gt}\ge G_r.
\]
For \(r=1\), the inequality \(i_r-i_1\ge G_1\) is trivial. Thus any length-\(n\) factor with \(r\) ones satisfies \(G_r\le n-1\).

Conversely, take \(s=0\) and \(d=b-1\). Then
\[
c_b(j(b-1))=1\quad\Longleftrightarrow\quad
1+j(b-1)=b^t\quad\Longleftrightarrow\quad j=G_{t+1}.
\]
The first \(n\) samples contain exactly the largest \(r\) with \(G_r\le n-1\) ones. Solving this inequality gives the claimed formula for \(H_b(n)\).

At \(n=1+G_r\), a factor with \(r\) ones has \(i_1=0\) and \(i_r=G_r\). For \(r\ge3\), equality in both inequalities above forces \(g=1\), \(f_r=r-1\), all \(f_j=j-1\), and \(d=b^{a_1}(b-1)\). Hence \(i_j=G_j\) for every \(j\), yielding the unique binary word. For \(r=2\), critical length two forces the word `11`; for \(r=1\), critical length one forces `1`. The witness progression above realizes each word.

**Quadratic factor bound.** Factors with at most two ones number at most \(1+n+\binom n2\). Consider a factor with at least three ones and denote its first three one-indices by \(i<j<k\). Write the first three corresponding powers as \(b^a,b^{a+f},b^{a+h}\), where \(0<f<h\), and set \(g=\gcd(f,h)\). The power-difference lemma specialized to the three powers gives
\[
k-i\ge\frac{b^h-1}{b^g-1}\ge b^{h-g}\ge b^f,
\]
because \(h\ge f+g\). Thus \(1\le f\le L=\lfloor\log_b(n-1)\rfloor\).

For all sampled positions \(t\ge i\), the integer under the indicator is
\[
s+td+1=b^a\left(1+\frac{(t-i)(b^f-1)}{j-i}\right).
\]
Hence its being a power of \(b\) is determined entirely by the triple \((i,j,f)\): the parenthesized rational number must be a nonnegative integral power of \(b\). Every position earlier than \(i\) is zero by the definition of the first one. Thus the triple determines the **entire** binary factor, independently of \(a,s,d\); if more than one triple is possible, choose the lexicographically least admissible one for an injective encoding. Moreover, positivity of the start gives
\[
1\le s+1=b^a-id\quad\Longrightarrow\quad
\frac{i(b^f-1)}{j-i}<1\quad\Longrightarrow\quad j>b^f i.
\]
For each \(f\in\{1,\ldots,L\}\) and each second index \(j\in\{1,\ldots,n-1\}\), the possible nonnegative integer values of \(i\) satisfying \(j>b^fi\) number exactly \(\lceil j/b^f\rceil\). Counting the encodings yields the displayed finite double-sum bound.

Finally, \(\lceil j/b^f\rceil\le j/b^f+1\). Summation over \(j\) and the geometric series \(\sum_{f\ge1}b^{-f}=1/(b-1)\) give
\[
\sum_{f=1}^L\sum_{j=1}^{n-1}\left\lceil\frac j{b^f}\right\rceil
\le \frac{n(n-1)}{2(b-1)}+(n-1)L.
\]
Since \(L=O_b(\log n)\), the quadratic upper bound and stated limsup follow. This completes the proof.

## Verification
Run `python verify.py` with Python 3 and no third-party dependencies. The standalone checker enumerates explicit arithmetic-progression factors for bases two through five over finite parameter grids, checks the occupancy formula for bases two through six and lengths through thirty, verifies rigid critical patterns in those ranges, tests the finite polynomial bound, and independently checks power-difference gcd identities on hundreds of exponent triples. In the reported execution it returned `VERIFY_OK 639077 assertions; finite tests only`.

The proof above, not finite testing, establishes all the infinitely quantified claims. The finite grid is neither an exhaustive enumeration of all arithmetic progressions nor a determination of exact \(P_b(n)\) values.

## Relationship to prior work
Konieczny and Müllner, *Arithmetical subword complexity of automatic sequences* (arXiv:2309.03180, first public 6 September 2023), introduce the effective alphabet parameter and give a general \(r^n\exp(o(n))\) upper bound. The pure-power indicator here has effective alphabet size one: its base-\(b\) language is eventually forced to zero by any fixed two-digit pattern containing both a nonzero digit and a zero, and the support has zero logarithmic density. Thus their general bound is subexponential, but it does not specify the quadratic upper bound, the exact number of ones in arithmetic factors, or the critical-pattern rigidity proved here.

A public 2026 note, *Sharp logarithmic support envelope for Abelian pattern Sturmian words*, proves a bound for occurrences in ordinary initial prefixes and identifies the characteristic support \(\{2^t-1\}\) as an extremizer. Counting ordinary prefix positions is not the same as maximizing over arbitrary starts and steps or counting distinct arithmetic-progression factors; its statement does not yield the quadratic bound here. Earlier work of Avgustinovich, Cassaigne, and Frid (2006) evaluates arithmetical complexity of different uniformly recurrent Toeplitz sequences, including the period-doubling family; its exact formulas are not formulas for the nonrecurrent pure-power indicator.

## Limitations
The quantitative bound for \(P_b(n)\) is not asserted to have sharp order or a sharp leading constant. The rigidity statement concerns precisely the critical lengths \(n=1+G_r\); it does not classify all maximizers at noncritical lengths. Search-based originality assessment is not a proof of novelty, and equivalent bounds may exist under number-theoretic language or in unpublished or unindexed work. This package does not claim independent verification or a machine-formalized proof.

## References
1. J. Konieczny and C. Müllner, “Arithmetical subword complexity of automatic sequences,” arXiv:2309.03180, first submitted 6 September 2023. https://arxiv.org/abs/2309.03180 .
2. S. V. Avgustinovich, J. Cassaigne, and A. E. Frid, “Sequences of low arithmetical complexity,” *RAIRO – Theoretical Informatics and Applications* 40 (2006), 569–582. https://www.numdam.org/item/10.1051/ita:2006041.pdf .
3. “Sharp logarithmic support envelope for Abelian pattern Sturmian words,” public research note (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-sharp-logarithmic-support-envelope-for-abelian-pattern-sturmian--71c60228ce20 .
