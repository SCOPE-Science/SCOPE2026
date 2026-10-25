# Exactly three closure components of the alternating divisor range on squarefull integers

## Finding
For the positive squarefull integers \(\mathcal Q\), including \(1\), the multiplicative alternating divisor function at exponent \(-2\) satisfies
\[
\overline{s_{-2}(\mathcal Q)}
=\left[\frac{630}{\pi^6},\frac{13}{16}\right]
\cup\left[\frac{13440}{17\pi^6},\frac{73}{81}\right]
\cup\left[\frac{612360}{697\pi^6},1\right].
\]
These are exactly three disjoint closed intervals. In particular, restricting to squarefull integers changes the two-component range closure known on all positive integers into three components.

## Assumptions and scope
A positive integer \(n\) is squarefull if every prime \(p\mid n\) satisfies \(\nu_p(n)\ge2\); by convention \(1\) is squarefull. For every prime \(p\) and integer \(a\ge0\), define
\[
s_{-2}(p^a)=\sum_{j=0}^{a}(-p^{-2})^j,
\]
and extend multiplicatively. Closure is in the usual real topology. Only the parameter \(-2\) and the specified squarefull domain are claimed. Set
\[
F_p=1-p^{-2}+p^{-4}-p^{-6}=\frac{1-p^{-8}}{1+p^{-2}},\qquad
L=\prod_{p\ge5}F_p.
\]
The convergent Euler products give
\[
\prod_p F_p=\frac{\zeta(4)}{\zeta(2)\zeta(8)}
=\frac{630}{\pi^6},\qquad
L=\frac{612360}{697\pi^6}.
\]

## Proof
**1. Prime-power envelopes.** Put \(x=p^{-2}\). Since the geometric alternating series has decreasing terms, for every \(a\ge2\),
\[
F_p=s_{-2}(p^3)\le s_{-2}(p^a)\le s_{-2}(p^2)=1-x+x^2<1.
\]
Equality in the first and second bounds is attained at exponents \(3\) and \(2\), respectively. Absence of the prime contributes the factor \(1\).

**2. A full interval from prime cubes above three.** Put \(w_p=-\log F_p>0\) for primes \(p\ge5\). Their sum converges. For each such prime we prove
\[
w_p\le\sum_{q>p}w_q.
\]
For \(p\in\{5,7,11,13,17,19,23\}\), the displayed inequality follows from the stronger finite products
\[
F_p\ge\prod_{p<q\le Q_p}F_q,
\]
with respective terminal primes \(Q_p=19,19,17,19,23,29,31\). Each comparison is an exact rational inequality reproduced by the standalone checker.

For \(p\ge25\), set \(x=p^{-2}\). The elementary estimate \(e^{-x}\le1-x+x^2/2<F_p\) (valid for \(0<x\le1/25\)) gives \(w_p<x\). For any \(q\ge5\),
\[
w_q\ge1-F_q=q^{-2}-q^{-4}+q^{-6}\ge\frac{24}{25q^2}.
\]
Nagura's classical prime-interval theorem supplies distinct successive primes \(q_j>p\) with \(q_j<(6/5)^j p\), for all \(j\ge1\). Consequently
\[
\sum_{q>p}w_q\ge\frac{24}{25}\sum_{j\ge1}\frac1{q_j^2}
>\frac{24}{25p^2}\sum_{j\ge1}\left(\frac56\right)^{2j}
=\frac{24}{11p^2}>w_p.
\]
For a summable sequence of positive numbers whose every term does not exceed the remaining tail, the set of all subsums is the full interval from zero to the total sum: recursively choose a term precisely if the remainder exceeds the sum of the later terms. Apply this standard greedy lemma to \((w_p)_{p\ge5}\) and exponentiate. Finite products of \(F_p\), corresponding to prime cubes, are dense in \([L,1]\). Every allowed squarefull product supported on primes at least five also belongs to \([L,1]\) by Step 1. Therefore
\[
\overline{\{s_{-2}(m):m\in\mathcal Q,\ \gcd(m,6)=1\}}=[L,1].
\]

**3. Separating the prime factors two and three.** Every squarefull \(n\) has the form \(n=2^a3^b m\) with \(\gcd(m,6)=1\), where each of \(a,b\) is either zero or at least two. The exact extremal local factors are
\[
\begin{array}{c|cc}
 &s_{-2}(p^3)&s_{-2}(p^2)\\ \hline
p=2&51/64&13/16\\
p=3&656/729&73/81
\end{array}
\]
By Steps 1--2, every fixed pair \((a,b)\) contributes the entire interval
\([s_{-2}(2^a)s_{-2}(3^b)L,\ s_{-2}(2^a)s_{-2}(3^b)]\) to the closure. In each of the four support cases (neither, only three, only two, both), the intervals arising from exponents \(2,3\) overlap into one interval. More explicitly, the four enclosing bands are
\[
\begin{array}{c|c}
\text{support of }\{2,3\}&\text{enclosing and filled interval}\\\hline
\varnothing &[L,1]\\
\{3\}&[(656/729)L,\ 73/81]\\
\{2\}&[(51/64)L,\ 13/16]\\
\{2,3\}&[(51/64)(656/729)L,\ (13/16)(73/81)].
\end{array}
\]
The asserted overlap within each support case follows by sorting the finite constants \(s_{-2}(2^a)s_{-2}(3^b)\) for \(a,b\in\{0,2,3\}\) and verifying for every consecutive pair \(c<d\) in the case that \(dL<c\). The checker verifies the stronger exact-rational bounds using \(157/50<\pi<22/7\). The same bounds prove that the bands with both \(2,3\) and with only \(2\) overlap, while
\[
\frac{13}{16}<\frac{656}{729}L,
\qquad \frac{73}{81}<L.
\]
Thus the four bands form exactly three components, with the first two low bands merging. Substitution of \(L=612360/(697\pi^6)\) and simplification yield the displayed three intervals. Their endpoints belong to the closure by the prime-cube products and the finite local factors. This proves both inclusion directions and all strict gaps.

## Verification
The bundled, dependency-free `verify.py` computes the finite-prime inequalities using exact rational arithmetic, derives and checks all Euler-product coefficient identities and band-overlap/separation inequalities using the rigorous bounds \(157/50<\pi<22/7\), and independently samples the first 50,000 integers to check that every squarefull input lies in the asserted bands. It prints `VERIFY_OK`. The infinite interval assertion rests on Nagura's theorem and the proved subsum argument, not on the finite enumeration.

## Relationship to prior work
Defant (2015) defined \(s_{-r}\) and established when its unrestricted range is dense in one interval. A later public scientific result, *Exactly two closure components for the alternating divisor range at parameter two* (identifier `f19c7ab30430`), establishes the unrestricted two-interval closure at \(r=2\), using prime factors with exponent one in its tail density argument. That unrestricted conclusion does not determine the closure on squarefull integers: deleting all exponent-one cases changes the permitted subsums and, as proved above, creates an additional gap. The prime-cube tail lemma and explicit three-band classification are the additional mathematical content. Defant's separate work on restricted domains concerns the ordinary generalized divisor function \(\sigma_t\), rather than the alternating function on squarefull integers.

## Limitations
This theorem does not determine any other parameter, any refined distribution or density of squarefull integers by value, or the closure on k-full integers for larger \(k\). The finite script does not prove the infinite prime-interval theorem or establish novelty; those aspects respectively use the cited classical theorem and explicit literature comparisons. Independent mathematical validation has not been performed.

## References
1. C. Defant, *On Ranges of Variants of the Divisor Functions that are Dense*, arXiv:1507.01128v1 (first public 2015-07-04), especially Definition 1.1 and Theorems 2.2--2.4.
2. J. Nagura, *On the interval containing at least one prime number*, Proc. Japan Acad. 28 (1952), 177--181.
3. *Exactly two closure components for the alternating divisor range at parameter two*, public research record, scientific identifier `f19c7ab30430`.
4. C. Defant, *On the Density of Ranges of Generalized Divisor Functions with Restricted Domains*, arXiv:1507.02663 (2015), concerning the distinct \(\sigma_t\) family.
