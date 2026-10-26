# Exact Abelian-unbordered factor spectrum of binary words with two marked symbols

## Finding

For a nonempty binary word \(v\), write \(\mathcal P(v)=(|v|_0,|v|_1)\). Call \(v\) *Abelian unbordered* when there is no integer \(1\le k<|v|\) for which its length-\(k\) prefix and suffix have equal Parikh vectors. Let \(U(w)\) denote the **number of distinct**, rather than position-counted, nonempty Abelian-unbordered contiguous factors of \(w\).

**Theorem.** Fix nonnegative integers \(a,b,c\) and set
\[
w=0^a1\,0^b1\,0^c,\qquad m=a+b+c,\qquad n=m+2,
\quad T=\max\{a,b,c,a+c-b\}.
\]
If \(m=0\), then \(U(11)=1\). If \(m\ge1\), then
\[
\boxed{U(w)=2+2T.}
\]
More precisely, its Abelian-unbordered factor set is
\[
\begin{split}
\{0,1\}&\cup\{0^j1:1\le j\le\max(a,b)\}
\\&\cup\{1\,0^j:1\le j\le\max(b,c)\}\\
&\cup\{0^j1\,0^b1:b<j\le a\}
\cup\{1\,0^b1\,0^j:b<j\le c\}.
\end{split}
\]
For \(m\ge1\), the minimum and maximum over all length-\(n\) weight-two binary words are exactly
\[
\boxed{2+2\lceil m/3\rceil\le U(w)\le2m+2.}
\]
All minimizers are precisely the triples satisfying \(a,b,c\le\lceil m/3\rceil\) and \(a+c-b\le\lceil m/3\rceil\). All maximizers are precisely \(b=0\) with \(a+c=m\), together with \((a,b,c)=(0,m,0)\); there are exactly \(m+2\) maximizers.

For a uniformly selected length-\(n\) binary word with exactly two ones (equivalently a uniform triple \((a,b,c)\) of nonnegative integers summing to \(m\)), define
\[N_m(t)=\#\{(a,b,c):a+b+c=m,\ T\le t\}\quad (t\in\mathbb Z).\]
The **exact finite cumulative distribution** for \(m\ge1\) is
\[
\boxed{N_m(t)=
\begin{cases}
0,&t<\lceil m/3\rceil,\\
\displaystyle\sum_{b=\lceil(m-t)/2\rceil}^{t}
\bigl(m-b+1-2\max\{m-b-t,0\}\bigr),
&\lceil m/3\rceil\le t<m,\\
\binom{m+2}{2},&t\ge m.
\end{cases}}
\]
In particular \(\Pr(U(w)\le2+2t)=N_m(t)/\binom{m+2}{2}\).

There is also a **nondegenerate asymptotic law**. As \(m\to\infty\), \(T/m\) converges in distribution to a variable \(X\) with
\[
\boxed{\Pr(X\le x)=
\begin{cases}
0,&x<1/3,\\
\frac34(3x-1)^2,&1/3\le x\le1/2,\\
\frac{-5x^2+14x-5}{4},&1/2\le x\le1,\\
1,&x>1.
\end{cases}}
\]
Its first two moments are \(\mathbb E X=2/3\) and \(\operatorname{Var}(X)=1/36\). Consequently, for uniform weight-two binary words of length \(n\),
\[
\boxed{\mathbb E[U]=\frac43n+O(1),\qquad
\operatorname{Var}(U)=\frac19n^2+O(n).}
\]

## Assumptions and scope

All factors are **contiguous and linear**; repetitions of the same factor count only once. Abelian borders compare the full Parikh vectors of an equally long nonempty proper prefix and suffix; the empty border is excluded. The alphabet is fixed as \(\{0,1\}\) and the specified family has exactly two occurrences of \(1\), including the exceptional word \(11\). The random model is uniform across the \(\binom n2\) distinct words with exactly two ones, not uniform across factor occurrences or across ordinary binary words. This is a statement for all nonnegative gap triples, with no asymptotic assumption except in the limit-law part.

## Proof

**1. Reduction to short borders.** If a word of length \(L\) has an Abelian border of length \(k>L/2\), subtracting both equal Parikh vectors from the Parikh vector of the whole word shows that the complementary prefix and suffix of length \(L-k<L/2\) also have equal Parikh vectors. Thus a factor is Abelian unbordered precisely when it has no Abelian border of length \(1\le k\le\lfloor L/2\rfloor\).

**2. Complete factor classification.** Any factor of length at least two whose first and last symbols coincide has a length-one ordinary (and therefore Abelian) border, so only factors with different endpoints can qualify. Factors with zero ones then contribute exactly the one-letter word \(0\). A factor with one one and different endpoints has one of the forms \(0^j1\) and \(1\,0^j\), with \(j\ge1\); each is Abelian unbordered because every proper prefix and suffix of the same length differ in the number of ones, after complementing if needed. The maximal zero runs adjacent to a one yield exactly the indicated two ranges of \(j\).

A factor with two ones and different endpoints must be of the form \(0^j1\,0^b1\) for \(1\le j\le a\), or its one-to-zero counterpart \(1\,0^b1\,0^j\) for \(1\le j\le c\). In the first form the total length is \(L=j+b+2\). If \(j>b\), then \(j+1>L/2\): every prefix of length at most \(L/2\) consists solely of zeros, whereas the corresponding suffix contains the final one, so no Abelian border exists. If \(j\le b\), the length-\(j+1\) prefix and suffix each contain one one (and have the same length), giving an Abelian border. The reverse-sided case is symmetric. This proves the displayed factor set, including completeness. Its five disjoint families have sizes \(2,\max(a,b),\max(b,c),(a-b)_+,(c-b)_+\), where \(y_+=\max(y,0)\). Therefore
\[
U=2+2\bigl[b+(a-b)_++(c-b)_+\bigr]
=2+2\max\{a,b,c,a+c-b\}.
\]
When \(m=0\), the only factor without an Abelian border is \(1\), explaining the exception.

**3. Extremizers.** Since \(T\ge\max(a,b,c)\ge\lceil m/3\rceil\), every count is at least the stated minimum. Taking the nearly balanced triples \((q,q,q)\), \((q,q+1,q)\), and \((q+1,q+1,q)\) at \(m=3q,3q+1,3q+2\), respectively, attains this bound. The characterization of minimizers is exactly the four inequalities in the definition of \(T\). Since \(a+c-b=m-2b\le m\) and each gap is at most \(m\), one has \(T\le m\). Equality forces \(b=0\) or a gap equal to \(m\); the latter gives only the additional case \((0,m,0)\) beyond the \(m+1\) triples with \(b=0\). This proves the maximum and its exact multiplicity.

**4. Exact finite distribution.** Fix an integer \(t\) in the nontrivial range \(\lceil m/3\rceil\le t<m\), and write \(c=m-a-b\). The inequality \(a+c-b\le t\) requires \(b\ge\lceil(m-t)/2\rceil\), while \(b\le t\) is also necessary. At such a fixed \(b\), the remaining inequalities \(a,c\le t\) leave precisely
\[
m-b+1-2\max(m-b-t,0)
\]
nonnegative pairs \((a,c)\) with \(a+c=m-b\). This quantity is nonnegative throughout the stated \(b\) range because \(t\ge m/3\) ensures \(m-b\le2t\). Summation proves the finite CDF, and both outer ranges follow from the extremal values.

**5. Limiting law and moments.** Uniform triples \((a,b,c)\) with sum \(m\) converge after division by \(m\) to the uniform area distribution on the simplex \(A,B,C\ge0\), \(A+B+C=1\). The continuous statistic is \(X=\max(A,B,C,A+C-B)\). At a threshold \(x\in[1/3,1]\), one must have \((1-x)/2\le B\le x\); at fixed \(B\), the permissible interval of \(A\) has length
\[
(1-B)-2\max(1-B-x,0).
\]
Since the full simplex has coordinate area \(1/2\), multiplying the integral over \(B\) by two yields the stated quadratic expressions, with the interval split at \(B=1-x\) when \(x\ge1/2\). Elementary integration of \(1-F(x)\) and \(2x(1-F(x))\) on \([1/3,1]\) yields \(\mathbb E X=2/3\) and \(\mathbb E X^2=17/36\). As the integrands are bounded piecewise-polynomial Lipschitz functions on a compact simplex, elementary lattice Riemann-sum error bounds are \(O(m^{-1})\) for both moments. Thus \(\mathbb E T=(2/3)m+O(1)\), \(\operatorname{Var}(T)=m^2/36+O(m)\). Substituting \(U=2+2T\) and \(m=n-2\) gives the final two asymptotic formulas.

## Verification

Run `python3 check.py` using Python 3 standard library only. The script constructs all distinct factors and independently tests Abelian borders using prefix sums. It checks exact factor sets for every nonnegative gap triple with at most 22 zeros, exact finite CDFs and extrema for each such sum, the low-support border property through word length 14, and rational moment consistency at 600 zeros. These finite checks do not substitute for the all-length proof.

## Relationship to prior work

Christodoulakis, Christou, Crochemore and Iliopoulos (2014) studied the shortest Abelian borders of binary words and global counts of border-free words. Goč, Rampersad, Rigo and Salimov (2014) developed global enumeration of Abelian-bordered words and automatic-sequence examples; their text also already records a four-one word having an Abelian border but no ordinary border. Charlier, Harju, Puzynina and Zamboni (2015/2016) study how the existence of infinitely many Abelian-unbordered **factors** constrains periodicity, and give a sufficient palindrome-based construction. The present result is instead an exact **per-word count of distinct factors** under a fixed two-one composition, plus its finite conditional law and limit distribution. Neither the global word counts nor the qualitative periodicity results imply the displayed formula without an additional classification of the sparse factors.

## Limitations

The theorem is restricted to finite binary words with exactly two ones. It does not enumerate factors counted with multiplicity, arbitrary Hamming weights, circular factors, or Abelian-unbordered words of all lengths. The asymptotic law concerns only the specified uniform weight-two model. Priority is assessed against accessible primary work and published search records, not guaranteed absolutely: the full text of *Abelian Borders in Binary Words* (2014) was not accessible for direct examination, although its abstract was compared. The symbolic proof is self-contained; computational checks are finite corroboration. No independent mathematical audit has been performed.

## References

1. M. Christodoulakis, M. Christou, M. Crochemore, C. S. Iliopoulos, *Abelian borders in binary words*, Discrete Applied Mathematics 171 (2014), 141–146. DOI: 10.1016/j.dam.2014.02.012. Published 10 July 2014.
2. D. Goč, N. Rampersad, M. Rigo, P. Salimov, *On the Number of Abelian Bordered Words (with an Example of Automatic Theorem-Proving)*, International Journal of Foundations of Computer Science 25 (2014), 1097–1110. DOI: 10.1142/S0129054114400267.
3. É. Charlier, T. Harju, S. Puzynina, L. Zamboni, *Abelian bordered factors and periodicity*, European Journal of Combinatorics 51 (2016), 407–418; first public arXiv version 29 January 2015, arXiv:1501.07464.
4. G. Fici, S. Puzynina, *Abelian Combinatorics on Words: a Survey*, arXiv:2207.09937 (2022), section 6.3 (later reference only).
