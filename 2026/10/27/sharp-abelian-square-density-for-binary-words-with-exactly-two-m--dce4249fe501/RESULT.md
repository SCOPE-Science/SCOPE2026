# Sharp Abelian-square density for binary words with exactly two marked letters

## Finding

Let \(w\) be a finite binary word containing exactly two occurrences of \(1\), with \(n\ge2\). Every such word has a unique representation
\[
w=0^a1\,0^b1\,0^c,\qquad a,b,c\in\mathbb Z_{\ge0},\qquad a+b+c=n-2.
\]
An *Abelian square* is a nonempty even-length contiguous factor whose first and second halves contain the same number of each symbol. Let \(\operatorname{AS}(w)\) be the number of **distinct strings** that are Abelian-square factors (not the number of occurrences or Parikh-equivalence classes).

**Exact all-parameter classification.** The entire collection of Abelian-square factors consists of
\[
\{0^{2r}:1\le r\le\lfloor\max(a,b,c)/2\rfloor\}
\quad\cup\quad
\{0^i1\,0^b1\,0^j:0\le i\le a,\ 0\le j\le c,\ |i-j|\le b,\ i+j+b\equiv0\pmod2\}.
\]
The two sets are disjoint, and the strings inside either set are distinct. Equivalently, with \([x]_+=\max(0,x)\), the exact count is
\[
\boxed{\operatorname{AS}(w)=\left\lfloor\frac{\max(a,b,c)}2\right\rfloor+
\sum_{\substack{-b\le d\le b\\d\equiv b\ (\mathrm{mod}\ 2)}}
\left[\min(a,c+d)-\max(0,d)+1\right]_+.}
\]

**Sharp extremal asymptotic and rigidity.** Write
\[
M_2(n)=\max_{\substack{w\in\{0,1\}^n\\\#_1(w)=2}}\operatorname{AS}(w).
\]
Then
\[
\boxed{M_2(n)=\frac{n^2}{16}+O(n)}\qquad(n\to\infty).
\]
For any sequence of such words with \(n\to\infty\), the ratio \(\operatorname{AS}(w)/n^2\to1/16\) holds **if and only if**
\[
\frac{a}{n}\to\frac38,\qquad\frac{b}{n}\to\frac14,\qquad\frac{c}{n}\to\frac38.
\]
In particular, the explicit family \(w_k=0^{3k}1\,0^{2k}1\,0^{3k}\), \(k\ge1\), has length \(8k+2\) and exactly
\[
\boxed{\operatorname{AS}(w_k)=4k^2+3k+1+\lfloor3k/2\rfloor.}
\]

## Assumptions and scope

The alphabet is \(\{0,1\}\), factors are contiguous, and words with exactly two \(1\)'s are considered. Zero runs may have length zero, so the result includes adjacent marked symbols and marked symbols at either endpoint. The empty factor is excluded. All exact statements hold for nonnegative integers \(a,b,c\), including \(a=b=c=0\). The asymptotic result concerns the maximum *restricted to this two-marked-letter class*; it is not a claimed bound for arbitrary binary words.

## Proof

**1. Exhaustive factor classification.** A factor with exactly one \(1\) cannot be an Abelian square, since equal halves would require an even total number of \(1\)'s. A factor with no \(1\)'s is \(0^{2r}\), present exactly for the stated \(r\)'s. Every factor containing both \(1\)'s has exactly the form \(v=0^i1\,0^b1\,0^j\) with the displayed bounds on \(i,j\). If \(v\) is an Abelian square, each half must contain one \(1\). If its half-length is \(h=(i+j+b+2)/2\), the number of zeros between the first \(1\) and the midpoint is
\[
h-i-1=\frac{b+j-i}{2}.
\]
The two marked symbols belong to different halves exactly when this is an integer in \(\{0,1,\ldots,b\}\). That is equivalent to \(i+j+b\) even and \(|i-j|\le b\). Conversely these conditions put one \(1\) in each half and, because the halves have equal lengths, the zero counts also agree. Distinct pairs \((i,j)\) give distinct strings. For fixed \(d=i-j\), the number of pairs is the number of integers in
\[
[0,a]\cap[d,c+d],
\]
which is the displayed positive-part summand. This proves the exact classification and count.

**2. Continuum band and lattice error.** Let \(s=a+b+c=n-2\) and define
\[
A(a,b,c)=\int_0^a\!\int_0^c\mathbf1_{\{|u-v|\le b\}}\,dv\,du.
\]
Integration of the two off-diagonal triangles gives the exact identity
\[
A=ac-\tfrac12(a-b)_+^2-\tfrac12(c-b)_+^2
+\tfrac12(a-b-c)_+^2+\tfrac12(c-b-a)_+^2.
\]
The section length \(f(d)=\max(0,\min(a,c+d)-\max(0,d))\) is \(1\)-Lipschitz and has support inside \([-c,a]\). At each integer \(d\), its corresponding integer-point count differs from \(f(d)\) by at most one. Comparing the mesh-two sum over \(d=-b,-b+2,\ldots,b\) with \(\frac12\int_{-b}^b f(d)\,dd=\frac12A\) introduces an error bounded by a constant times \(s+1\): there are at most \(s+1\) mesh points, each mesh interval contributes an error at most one by the Lipschitz property, and the endpoint contributes at most \(s\). Consequently, **uniformly** over all triples,
\[
\operatorname{AS}(w)=\tfrac12A(a,b,c)+O(s+1).
\]
This is an exact comparison bound between finite integer counts and continuum area; it does not identify finite and continuum counts.

**3. Sharp area inequality and equality case.** For all \(a,b,c\ge0\) with \(s=a+b+c>0\),
\[
A(a,b,c)\le\frac{s^2}{8},
\]
with equality **only** at \((a,b,c)=(3s/8,s/4,3s/8)\). Indeed, if \(b\ge s/3\), then \(A\le ac\le(s-b)^2/4\le s^2/9<s^2/8\). Suppose \(b<s/3\). If \(\min(a,c)<b\), assume \(a<b\); then \(a\le(s-b)/2\) and
\[
A\le ac=a(s-b-a)<b(s-2b)\le s^2/8,
\]
where the last maximum is the elementary quadratic maximum at \(b=s/4\). Otherwise \(a,c\ge b\); put \(\delta=|a-c|\). For \(\delta\le b\), the area formula reduces to
\[
A=bs-2b^2-\delta^2/2\le s^2/8,
\]
with equality precisely when \(b=s/4\) and \(\delta=0\). For \(\delta>b\), it reduces instead to
\[
A=bs-\tfrac32b^2-b\delta<bs-\tfrac52b^2\le s^2/10<s^2/8.
\]
The case \(b=0\) gives area zero directly. The stated equality case is feasible, completing the inequality.

**4. Maximum, construction, and rigidity.** By the uniform lattice error and the area bound, \(M_2(n)\le (n-2)^2/16+O(n)\). Rounding the unique maximizing real proportions to integral run lengths, with their sum \(n-2\), achieves \(A=(n-2)^2/8+O(n)\) and therefore matches the upper bound within \(O(n)\). Hence \(M_2(n)=n^2/16+O(n)\). For the explicit lengths \(n=8k+2\), we have \(a=c=3k\ge b=2k\) and the allowed differences are \(-2k,-2k+2,\ldots,2k\). Their integer cross-section sizes are \(3k+1-|d|\), so the mixed-factor count is
\[
(2k+1)(3k+1)-2k(k+1)=4k^2+3k+1.
\]
Adding the unary count \(\lfloor3k/2\rfloor\) proves the explicit formula. Finally, after division by \(n^2\), the uniform error vanishes. Compactness of the simplex of normalized nonnegative triples, together with the *unique* continuum equality case, gives the asserted necessity of the run-length ratios; continuity of \(A\) proves sufficiency.

## Verification

The standalone file `verify.py` constructs the actual sets of distinct even-length Abelian-square factors by direct substring enumeration and independently compares them with both the structural description and the diagonal count. Its finite checks include all \(13^3=2197\) nonnegative triples with coordinates at most \(12\), plus \(25\) terms of each of the two closed-form specializations. Execute `python3 verify.py` in the directory containing this file and the script. These checks test finite instances only; the infinite-family classification and extremal rigidity rest on the proof above.

## Relationship to prior work

Fici, Mignosi, and Shallit [1, Proposition 1, pp. 3–4] used the equal-run word \(0^k1\,0^k1\,0^k\) to demonstrate a quadratic number of distinct Abelian-square factors, without stating the exact count for every two-marked-letter word or optimizing the leading coefficient within that class. Their equal-run construction yields asymptotic coefficient \(1/18\) in total word length; the sharp coefficient here is \(1/16\). Simpson [2, pp. 3–4] gives an explicit count for the *different fixed subfamily* \(0^k1\,0^k1\,0^{2k}\); substituting \((a,b,c)=(k,k,2k)\) in the present general formula reproduces that previously known count exactly. Kociumaka and collaborators [3] established quadratic order for unrestricted binary Abelian-square extremals. None of these earlier general quadratic-order statements implies the restricted sharp constant or its unique asymptotic optimizer; the particular Simpson enumeration is an acknowledged special case, not claimed as new.

## Limitations

This work does not determine the exact maximum \(M_2(n)\) for each finite \(n\), nor classify all finite maximizers. It does not resolve unrestricted binary Abelian-square extrema. The special case cited from Simpson is prior knowledge. The full text of [3] was not accessible during the comparison, and unindexed or otherwise missed equivalent results remain an originality risk. Numerical checking is finite; the analytic proof supplies the all-length claims.

## References

[1] G. Fici, F. Mignosi, and J. Shallit, *Abelian-Square-Rich Words*, arXiv:1701.00948, first posted 2017-01-04, especially Proposition 1. https://arxiv.org/abs/1701.00948

[2] J. Simpson, *Solved and unsolved problems about abelian squares*, arXiv:1802.04481, first posted 2018-02-13, especially pp. 3–4. https://arxiv.org/abs/1802.04481

[3] T. Kociumaka, J. Radoszewski, W. Rytter, and T. Waleń, *Maximum Number of Distinct and Nonequivalent Nonstandard Squares in a Word*, DLT 2014; arXiv:1604.02238, first posted 2016-04-08. https://arxiv.org/abs/1604.02238
