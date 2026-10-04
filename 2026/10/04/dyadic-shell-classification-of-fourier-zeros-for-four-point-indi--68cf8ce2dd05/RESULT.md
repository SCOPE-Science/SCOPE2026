# Dyadic shell classification of Fourier zeros for four-point indicators
## Finding
For every integer \(m\ge 3\), set \(N=2^m\) and let \(A\subset \mathbb Z_N\) have four distinct elements. Define the unnormalised Fourier transform of the indicator by
\[
\widehat{1_A}(k)=\sum_{a\in A}\exp(-2\pi i k a/N),\qquad k\in\mathbb Z_N.
\]
For nonzero \(x\in\mathbb Z_N\), let \(\nu(x)=v_2(x)\in\{0,\ldots,m-1}\). For a perfect matching \(A=\{a,b\}\sqcup\{c,d\}\), call the matching balanced at level \(r\) when \(\nu(a-b)=\nu(c-d)=r\), and let \(B(A)\) be the set of its balanced levels over the three perfect matchings.

Then the Fourier zero set is the disjoint union
\[
\{k\in\mathbb Z_N:\widehat{1_A}(k)=0\}=
\bigsqcup_{r\in B(A)}\{k\ne0:v_2(k)=m-1-r\}.
\]
The set \(B(A)\) is exactly one of the following forms: \(\varnothing\); a singleton \(\{r\}\) with \(0\le r\le m-3\); or a pair \(\{r,s\}\) with \(0\le r<s\le m-1\). Every allowed form occurs. Hence the exact possible numbers of vanishing Fourier coefficients are
\[
\{0\}\cup\{2^r:0\le r\le m-3\}\cup\{2^r+2^s:0\le r<s\le m-1\},
\]
and the exact possible Fourier-support sizes are \(N\) minus these numbers.

## Assumptions and scope
The group is the cyclic dyadic group \(\mathbb Z_{2^m}\) with \(m\ge3\). The function is specifically the coefficient-one indicator of a four-element set. No assertion is made here for arbitrary four-sparse coefficients, noncyclic \(2\)-groups, or cyclic groups with odd prime factors. The value at frequency \(0\) is \(4\), so it is never a zero.

## Proof
First use a geometric four-unit lemma. If four complex numbers of modulus one sum to zero, they split into two antipodal pairs. Indeed, after grouping two terms on each side, equality of two chord sums on the unit circle forces the two unordered pairs to be negatives of each other; if either chord sum is zero, both pairs are already antipodal. Therefore \(\widehat{1_A}(k)=0\) if and only if some perfect matching \(A=\{a,b\}\sqcup\{c,d\}\) satisfies
\[
k(a-b)\equiv 2^{m-1}\pmod{2^m},\qquad
k(c-d)\equiv 2^{m-1}\pmod{2^m}.
\]

For nonzero \(x\in\mathbb Z_{2^m}\) with \(v_2(x)=r\), write \(x=2^r u\) with \(u\) odd. Dividing the congruence \(kx\equiv2^{m-1}\pmod{2^m}\) by \(2^r\) shows that it holds exactly when \(v_2(k)=m-1-r\). Thus one matching contributes a Fourier zero precisely when its two difference valuations agree, and in that case it contributes the entire valuation shell \(\{k:v_2(k)=m-1-r\}\). Different shells are disjoint, proving the zero-set formula. Such a shell has exactly \(2^r\) elements.

It remains to classify the possible balanced levels. Let \(r_0\) be the minimum \(2\)-adic valuation among the six nonzero pairwise differences of points of \(A\). Translate \(A\), divide all differences by \(2^{r_0}\), and work modulo \(2^{m-r_0}\). The normalized set meets both parity classes. If its parity split is \(1+3\), every perfect matching has one odd difference and one even difference, so no matching is balanced. If the split is \(2+2\), the two cross-parity matchings are balanced at normalized level \(0\). The remaining same-parity matching is balanced exactly when its two differences have a common valuation \(t\ge1\). Undoing the normalization gives \(B(A)=\{r_0\}\) or \(B(A)=\{r_0,r_0+t\}\). When \(m-r_0=2\), the normalized set is all of \(\mathbb Z_4\), so the same-parity differences both have valuation \(1\); hence a singleton can occur only when \(r_0\le m-3\).

All allowed cases are attained explicitly. The set \(\{0,1,2,4\}\) has no balanced matching. For \(0\le r\le m-3\), the set
\[
\{0,2^{r+1},2^r,2^r+2^{r+2}\}
\]
has exactly the balanced level \(r\). For \(0\le r<s\le m-1\), the set
\[
\{0,2^s,2^r,2^r+2^s\}
\]
has exactly the balanced levels \(r\) and \(s\). This proves both the classification and the exact zero-count spectrum.

## Verification
The accompanying `verify.py` uses exact integer arithmetic. For \(N=2^m\), reduction modulo the cyclotomic polynomial \(\Phi_N(X)=X^{N/2}+1\) makes a Fourier value zero exactly when the reduced integer coefficient vector is zero. The verifier exhausts every four-element subset for \(N\in\{8,16,32\}\), compares the direct cyclotomic zero set with the valuation-shell formula, and checks the predicted classification of \(B(A)\). It also checks the explicit witness families for all allowed patterns through \(m=9\). A successful replay prints `VERIFY_OK`.

The finite enumeration is corroborative only. The theorem for all \(m\ge3\) follows from the four-unit lemma, the exact dyadic congruence calculation, and the parity-split classification above.

## Relationship to prior work
Lam and Leung study vanishing sums of roots of unity in general and, for prime-power orders, their structural results reduce minimal vanishing relations to the prime-length pattern. That literature supports the antipodal-pair mechanism for dyadic roots but does not give the frequency-shell decomposition or the complete four-point indicator spectrum above. Krahmer, Pfander, and Rashkov give uncertainty principles and rank criteria for finite Abelian groups; their bounds do not classify the Fourier zeros of a fixed coefficient-one four-point support. Filaseta, Finch, and Nicol study cyclotomic divisibility of sparse \(0,1\)-polynomials, including strong restrictions for dyadic exponent patterns, but the inspected results do not state the valuation-shell formula or its attainable shell-union classification.

Thus the contribution here is not the general fact that sparse root-of-unity sums can vanish, but the exact dyadic geometry: for every four-point indicator, every zero frequency belongs to a whole \(2\)-adic shell determined by a balanced matching, and the possible shell unions are completely classified.

## Limitations
The claim is confined to four-element indicators on cyclic groups of order a power of two. It does not classify arbitrary complex coefficients, larger supports, odd-prime factors, or noncyclic groups. The originality comparison cannot exclude an equivalent result phrased only in specialized mask-polynomial, tiling, or cyclotomic-divisibility terminology that was not indexed by the searches performed.

## References
1. T. Y. Lam and K. H. Leung, *On vanishing sums for roots of unity*, arXiv:math/9511209, first public version 1995-11-13.
2. F. Krahmer, G. E. Pfander, and P. Rashkov, *Uncertainty in time-frequency representations on finite Abelian groups and applications*, arXiv:math/0611493, first public version 2006-11-16.
3. M. Filaseta, C. Finch, and C. Nicol, *On three questions concerning 0, 1-polynomials*, Journal de Théorie des Nombres de Bordeaux 18 (2006), 357–370, manuscript received 2004-11-16.
