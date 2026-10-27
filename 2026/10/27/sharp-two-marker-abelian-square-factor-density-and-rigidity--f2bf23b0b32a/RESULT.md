# Sharp two-marker Abelian-square factor density and rigidity

## Finding
An **Abelian square** is a nonempty contiguous word of even length whose two equal-length halves contain the same number of each symbol. Let \(D(w)\) be the number of **distinct** nonempty Abelian-square factors of a binary word \(w\), counting equal factor strings only once.

For all integers \(a,b,c\ge0\), put \(w=0^a1\,0^b1\,0^c\), \(e(t)=1\) when \(t\) is even and \(0\) otherwise, and
\[
H(t)=\left\lfloor\frac{\max(t,0)^2}{4}\right\rfloor\qquad(t\in\mathbb Z).
\]
Then the following is an exact, all-parameter count:
\[
\boxed{D(w)=\left\lfloor\frac{\max(a,b,c)}2\right\rfloor
+\frac{(a+1)(c+1)+(-1)^b e(a)e(c)}2
-H(a-b)-H(c-b)+H(a-b-c-1)+H(c-b-a-1).}
\]
In particular, if \(M_2(n)\) is the maximum of \(D(w)\) over all length-\(n\) binary words containing exactly two ones, then
\[
\boxed{\lim_{n\to\infty}\frac{M_2(n)}{n^2}=\frac1{16}.}
\]
There is an asymptotic **rigidity** statement: for any sequence of such words with lengths \(n_j\to\infty\) and \(D(w_j)/n_j^2\to1/16\), their three zero-gap lengths, in word order and divided by \(n_j\), converge to
\[
\boxed{\left(\frac38,\frac14,\frac38\right).}
\]
For example, at every integer \(t\ge1\), the explicit words \(w_t=0^{3t}1\,0^{2t}1\,0^{3t}\) have length \(8t+2\) and satisfy
\[
D(w_t)=4t^2+3t+1+\left\lfloor\frac{3t}{2}\right\rfloor.
\]
The exact finite-length maximum \(M_2(n)\) is **not** claimed in an unsimplified closed form; the count formula permits its finite determination without examining substring factors.

## Assumptions and scope
The alphabet is \(\{0,1\}\). All gaps may be zero; adjacent ones, boundary ones, and the word \(11\) are included. Factors are linear contiguous factors, not cyclic factors or scattered subsequences. Only distinct nonempty factors are counted; they are not identified by Abelian equivalence. In particular, this does **not** count occurrences or different Parikh vectors.

## Proof
**Exact factor classification.** An Abelian square has an even total number of ones. A factor of a word containing exactly two ones can thus have either zero ones or two ones; a one-one factor is impossible. The distinct zero-one squares are \(0^2,0^4,\ldots,0^{2\lfloor m/2\rfloor}\), where \(m=\max(a,b,c)\), giving \(\lfloor m/2\rfloor\).

Every factor containing both ones is uniquely of the form \(0^i1\,0^b1\,0^k\), with \(0\le i\le a\) and \(0\le k\le c\). Its length is even exactly when \(i+b+k\) is even. When this holds, its midpoint lies between the two ones (one in each half) exactly when \(|i-k|\le b\): the midpoint after \((i+b+k+2)/2\) letters must follow the first one and precede the second, and the parity restriction reduces the resulting inequalities to this symmetric bound. Hence the number of distinct two-one Abelian squares is
\[
B(a,b,c)=\#\{(i,k)\in[0,a]\times[0,c]\cap\mathbb Z^2:\ i+k\equiv b\pmod2,\ |i-k|\le b\}.
\]
All eligible pairs produce different factor strings.

**Closed form.** Without the band restriction, the parity condition admits precisely
\[
\frac{(a+1)(c+1)+(-1)^b e(a)e(c)}2
\]
pairs, by multiplying the alternating sums over the two integer intervals. Forbidden pairs with \(i-k>b\), under the parity condition, have \(i=k+b+2r\) for some \(r\ge1\). Summing first over \(r\), then over \(k\le c\), their number is \(H(a-b)-H(a-b-c-1)\), since
\[
\sum_{r\ge1}\max(z-2r+1,0)=\left\lfloor\frac{\max(z,0)^2}{4}\right\rfloor.
\]
The other forbidden corner contributes \(H(c-b)-H(c-b-a-1)\). Subtracting these disjoint corners proves the exact formula.

**Sharp asymptotic coefficient.** Set \(s=a+b+c=n-2\). In the real rectangle \(R=[0,a]\times[0,c]\), define
\[
A(a,b,c)=\operatorname{area}\{(x,y)\in R:|x-y|\le b\}.
\]
For each integer \(i\), the allowed integer \(k\)'s occupy an interval with one prescribed parity, so their count differs from half the interval's real length by at most one. The interval-length function in \(i\) is uniformly Lipschitz with constant at most two. Summing over rows and comparing to the area integral therefore gives, **uniformly in nonnegative** \(a,b,c\),
\[
B(a,b,c)=\frac12 A(a,b,c)+O(s+1).
\]
The zero-one contribution is at most \(s/2\), so \(D(w)=A(a,b,c)/2+O(s+1)\).

By symmetry assume \(a\le c\). If \(b\le a\), put \(h=c-a\). Subtracting the two exterior corner triangles of the diagonal strip, with the necessary clipping correction when \(h>b\), yields the exact area identity
\[
A(a,b,c)=bs-2b^2-\frac{h^2}{2}+\frac{\max(h-b,0)^2}{2}
=\frac{s^2}{8}-2\left(b-\frac{s}{4}\right)^2
-\frac{h^2-\max(h-b,0)^2}{2}.
\]
Both displayed deficits are nonnegative. Equality for \(s>0\) requires \(b=s/4\) and \(h=0\), hence \(a=c=3s/8\). If instead \(b>a\) and \(a>0\), then \(A\le ac<a(s-2a)\le s^2/8\); if \(a=0\), then \(A=0\). Thus \(A\le s^2/8\) globally, with a **unique** maximizing ratio \((a,b,c)/s=(3/8,1/4,3/8)\) for \(s>0\). This proves \(M_2(n)\le n^2/16+O(n)\).

Take \(a=c=3t\), \(b=2t\). Substitution in the exact formula (or summing its permitted difference diagonals) gives \(B(3t,2t,3t)=4t^2+3t+1\), whence the displayed value of \(D(w_t)\) and \(M_2(8t+2)\ge4t^2+O(t)\). For lengths between successive \(8t+2\), insert at most seven zeros into one outer gap; adding symbols cannot eliminate an existing factor, so the lower bound extends to all \(n\) with the same leading coefficient. This proves the limit.

**Rigidity.** Rescale each gap triple by \(s\). The normalized area is a continuous function on the compact simplex and the preceding cases identify its unique maximizer. Since the discrete-to-area error is uniform \(O(s)\), every sequence attaining normalized count \(1/16+o(1)\) must converge to that maximizing ratio. Dividing by \(n=s+2\) instead of \(s\) has the same limit.

## Verification
The standalone `verify.py` enumerates distinct Abelian-square factors independently of the formula for all \(1331\) triples with \(0\le a,b,c\le10\); every comparison agrees. It also computes the finite maximum values for lengths \(2\) through \(36\) directly from the proved formula and checks the explicit family identity for \(1\le t\le9\). The separate `verify_geometry.py` checks the stated planar area identity, global inequality, and equality conditions by exact-rational independent polygon clipping for 9261 triples. These finite checks corroborate the proof but are not used to infer the infinite assertion. Reproduce with `python3 verify.py` and `python3 verify_geometry.py`.

## Relationship to prior work
Kociumaka–Radoszewski–Rytter–Waleń (DLT 2014, publicly dated proceedings edition August 4, 2014; arXiv 2016) established quadratic growth of the **unrestricted** maximum and displayed a two-marker sparse construction. Fici–Mignosi (WORDS 2015, first arXiv version June 11, 2015) gave the family \(0^t1\,0^t1\,0^t\) to establish quadratic growth; its two-one contribution has leading coefficient \(1/18\) relative to word length squared. Neither inspected result states the exact three-gap formula, the sharp **fixed-two-one** coefficient \(1/16\), or rigidity of all asymptotic optimizers. Their known quadratic lower bounds are not claimed as new here. The unrestricted maximum sequence in OEIS A262249 addresses a different optimization domain and does not determine this constrained extremum.

## Limitations
No closed quasipolynomial for the exact finite maximum \(M_2(n)\), nor its finite-length equality words, is asserted. The asymptotic result is only for binary words with exactly two ones, not arbitrary weight or nonbinary alphabets. The literature comparison cannot rule out unindexed equivalent statements. The review is not independent validation.

## References
1. T. Kociumaka, J. Radoszewski, W. Rytter, T. Waleń, *Maximum Number of Distinct and Nonequivalent Nonstandard Squares in a Word*, DLT 2014, DOI:10.1007/978-3-319-09698-8_19; arXiv:1604.02238, https://arxiv.org/abs/1604.02238 ; full preprint discussed at https://www.researchgate.net/publication/264232396_Maximum_Number_of_Distinct_and_Nonequivalent_Nonstandard_Squares_in_a_Word .
2. G. Fici, F. Mignosi, *Words with the Maximum Number of Abelian Squares*, WORDS 2015; arXiv:1506.03562, https://arxiv.org/abs/1506.03562 ; full text at https://www.researchgate.net/publication/278048164_Words_with_the_Maximum_Number_of_Abelian_Squares .
3. OEIS A262249, unrestricted maximum number of distinct Abelian-square factors, https://oeis.org/A262249 .
