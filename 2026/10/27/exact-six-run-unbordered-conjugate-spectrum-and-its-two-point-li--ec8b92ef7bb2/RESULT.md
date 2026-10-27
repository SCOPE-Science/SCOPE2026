# Exact six-run unbordered-conjugate spectrum and its two-point limit

## Finding

Let \(a,b,c,d,e,f\) be arbitrary positive integers and set
\[
w=0^a1^b0^c1^d0^e1^f,\qquad n=a+b+c+d+e+f.
\]
A **border** of a word is a nonempty proper prefix that is also a suffix. A word without a border is **unbordered**. Write \(U(w)\) for the number of its \(n\) positional cyclic shifts that are unbordered. For this family, even if the word is periodic, no unbordered shift is counted repeatedly.

**Exact six-parameter formula.** With \(\mathbf 1_{P}\) equal to one when the proposition \(P\) holds and zero otherwise,
\[
\begin{aligned}
U(w)={}&\mathbf 1_{a>e\;\lor\;b<f}
+\mathbf 1_{b>f\;\lor\;c<a}
+\mathbf 1_{c>a\;\lor\;d<b}\\
&+\mathbf 1_{d>b\;\lor\;e<c}
+\mathbf 1_{e>c\;\lor\;f<d}
+\mathbf 1_{f>d\;\lor\;a<e}.
\end{aligned}
\]
The only possible values are \(0,2,3,4,5\). Moreover, \(U(w)=0\) exactly when \(a=c=e\) and \(b=d=f\), meaning \(w=(0^a1^b)^3\). The maximum \(5\) is attained, and the shortest length allowing it is \(n=11\).

**Complete fixed-length distribution.** Let \(N_j(n)\) be the number of length-\(n\) binary words *beginning in zero and having exactly six nonempty runs* with \(U(w)=j\), and put \(F_j(z)=\sum_{n\ge6}N_j(n)z^n\). Then
\[
\begin{aligned}
F_0(z)&=\frac{z^6}{(1-z^3)^2},\\
F_1(z)&=0,\\
F_2(z)&=\frac{3z^7(2+4z-2z^2-3z^3)}{(1-z^2)^2(1-z^3)^2},\\
F_3(z)&=\frac{6z^8(1+5z-z^2-3z^3)}{(1-z)(1-z^2)^2(1-z^3)^2},\\
F_4(z)&=\frac{3z^8(1+2z+10z^2-2z^3-5z^4)}{(1-z)^2(1-z^2)^2(1-z^3)^2},\\
F_5(z)&=\frac{6z^{11}(2+z)}{(1-z)^2(1-z^2)^2(1-z^3)^2},\\
F_6(z)&=0.
\end{aligned}
\]
Their sum is \(z^6/(1-z)^6\), as required for positive six-part compositions. In particular, \(N_5(11)=12\), and \(N_5(n)>0\) for every \(n\ge11\). Including words beginning in one doubles every count.

**Two-point limit.** Among uniformly chosen length-\(n\) words beginning in zero and having exactly six nonempty runs,
\[
\lim_{n\to\infty}\Pr(U(w)=4)
=\lim_{n\to\infty}\Pr(U(w)=5)=\frac12,
\]
while the total probability of \(U(w)\in\{0,2,3\}\) tends to zero. Thus the limiting law is concentrated equally on exactly four and exactly five unbordered rotations.

## Assumptions and scope

The alphabet is binary and all six displayed run lengths are positive integers. The word is linear when borders are tested, and a cyclic shift is read with exactly \(n\) letters. A cut at each of the \(n\) positions is considered, but an unbordered word is necessarily primitive, so duplicate shifts never affect the positive count. Enumeration treats ordered run-length sextuples, equivalently linear six-run words starting in zero, not necklaces modulo rotation. The complex variable \(z\) is a formal power-series indeterminate; probabilities are uniform over the \(\binom{n-1}{5}\) permitted sextuples.

## Proof

**1. A border criterion for six alternating runs.** First consider
\[
X=x^p y^q x^r y^s x^t y^u,
\]
where \(x\ne y\) are letters and all six exponents are positive. A proper border must begin in \(x\) and end in \(y\), hence has an even number of runs. A six-run proper border is impossible: any six-run suffix starts strictly inside the first run, so its first run is shorter than the whole first run of the corresponding prefix. A two-run border is possible exactly when the entire initial \(x\)-run fits into the penultimate \(x\)-run and the final \(y\)-run fits into the second run, i.e.
\[
p\le t\quad\text{and}\quad q\ge u.
\]
Indeed the matching prefix and suffix are then \(x^p y^u\); necessity follows by comparing their first and final runs. A four-run border would compare the prefix \(x^p y^q x^r y^v\) with the suffix \(x^h y^s x^t y^u\), forcing \(p=h\le r\), \(q=s\), \(r=t\), and \(v=u\le s\). In particular it already forces \(p\le t\) and \(q\ge u\), and so a two-run border exists. Thus \(X\) is unbordered **if and only if** \(p>t\) or \(q<u\).

Every rotation cut inside a constant run begins and ends with the same symbol and has a one-letter border. Only the six run-boundary cuts can be unbordered. Applying the criterion to the six boundary-start rotations in cyclic order gives the stated indicator formula, with no missed cuts.

**2. Exact enumerative calculation.** Write \(A=(a,c,e)\) and \(B=(b,d,f)\). Every positive triple has one of exactly thirteen weak-order patterns: a surjective rank triple with entries \(0,\ldots,r-1\), for \(1\le r\le3\). Let the multiplicities of its increasing rank levels be \(m_0,\ldots,m_{r-1}\), and let \(S_j=\sum_{i=j}^{r-1}m_i\). If the distinct positive values are \(v_0<\cdots<v_{r-1}\), their independent consecutive increments are positive integers. Hence the weight-generating function of all positive triples with this specified pattern is precisely
\[
G_{m_0,\ldots,m_{r-1}}(z)
=\prod_{j=0}^{r-1}\frac{z^{S_j}}{1-z^{S_j}}.
\]
The six-indicator formula depends only on the two weak-order patterns. If \(\mathcal P\) denotes the thirteen patterns and \(u(P,Q)\) the indicator sum after replacing \(A,B\) by rank triples \(P,Q\), then the following is an *exact finite rational identity*, not a sampled extrapolation:
\[
F_j(z)=\sum_{P,Q\in\mathcal P}\mathbf 1_{u(P,Q)=j}\,G_P(z)G_Q(z).
\]
Direct comparison of the \(13\cdot13=169\) rank-pattern pairs gives respectively \(1,0,15,42,81,30,0\) pairs with \(u=0,1,2,3,4,5,6\). Since every denominator factor belongs to \(\{1-z,1-z^2,1-z^3\}\), the entire identity is checked by multiplying by the common denominator \(D(z)=(1-z)^2(1-z^2)^2(1-z^3)^2\) and collecting finitely many integer coefficients. This yields the seven rational functions displayed above. The accompanying standard-library verifier performs all \(169\) comparisons and checks these exact polynomial identities; the weight formula proves why the finite calculation enumerates **all** positive integer sextuples.

The zero-pattern pair is the one in which both triples are constant, proving the characterization of \(U=0\); no pair yields \(1\) or \(6\). The first nonzero term of \(F_5\) is \(12z^{11}\). Its denominator has nonnegative coefficients and the numerator is positive, so all later coefficients are positive. This proves the sharp length threshold and maximum.

**3. Limit distribution.** At \(z=1\), each of \(F_4,F_5\) has a sixth-order pole with leading coefficient \(1/2\): for example \(6(2+1)/(2^2 3^2)=1/2\) for \(F_5\). All other poles of these rational functions have order at most two. The functions \(F_0,F_2,F_3\) have poles of order at most two, four, and five respectively. Consequently, coefficient extraction gives
\[
N_4(n)=\frac12\binom{n-1}{5}+O(n^4),\qquad
N_5(n)=\frac12\binom{n-1}{5}+O(n^4),
\]
and \(N_0(n)+N_2(n)+N_3(n)=O(n^4)\). Dividing by the exact number \(\binom{n-1}{5}\) of admissible words proves the claimed limiting law. Independently, when both triples have three distinct values (a proportion tending to one), direct evaluation of their \(36\) pairs of strict order types gives eighteen with value four and eighteen with value five.

## Verification

Run `python3 verify.py` in a directory containing the standalone verification file. It independently tests the literal border definition on every one of the \(4^6=4096\) sextuples with run lengths \(1\) through \(4\), checks all \(169\) exact weak-order rational identities using integer polynomial arithmetic, and compares generating-function coefficients with direct sextuple counts for each \(6\le n\le18\). The successful output is `VERIFY_OK rotations=4096 weak_order_pairs=169 generating_functions=5 fixed_lengths=6..18`. This is supplemental finite evidence; the argument in the Proof section establishes all lengths.

## Relationship to prior work

Harju and Nowotka introduced binary border-correlation sequences and bounded unbordered conjugates globally. Holub and Müller studied the special case of precisely two unbordered conjugates and characterized fully bordered words. Clokie, Gabrić, and Shallit established the unrestricted extremal count, realizability of all feasible counts, and the expectation for a uniformly random binary word of fixed length. Those settings differ from the present *conditional six-run* spectrum: their global bounds and unconditional expectation do not supply the six-parameter inequalities, fixed-length rational distributions, first five-rotation threshold, or equal four-versus-five limit. The general background results are acknowledged rather than claimed anew.

## Limitations

No result is asserted for words with eight or more runs; longer proper borders may require additional analysis. The rational generating functions enumerate linear words with exactly six nonempty runs, not rotation-equivalence classes. Finite checks do not certify the infinite conclusions independently, and an unindexed derivation of the same six-run law cannot be excluded. The primary 2004 article by Harju and Nowotka was not available in full text during comparison; its abstract, citation records, and its later treatment in the inspected 2019 article were considered, leaving a specific residual literature risk.

## References

1. T. Clokie, D. Gabrić, and J. Shallit, *Circularly squarefree words and unbordered conjugates: a new approach*, arXiv:1904.08187v1 (first public arXiv submission April 17, 2019), especially Sections 3–5, https://arxiv.org/abs/1904.08187.
2. Š. Holub and M. Müller, *Fully bordered words*, arXiv:1504.02222 (2015, revised 2016), https://arxiv.org/abs/1504.02222.
3. T. Harju and D. Nowotka, *Border correlation of binary words*, Journal of Combinatorial Theory, Series A 108 (2004), 331–341, https://doi.org/10.1016/j.jcta.2004.07.009.
