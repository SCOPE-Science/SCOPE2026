# Four-run Lyndon factors: exact spectrum, sharp rigidity, and a Dirichlet limit

## Finding

For all positive integers \(a,b,c,d\), let \(w=0^a1^b0^c1^d\) on the ordered alphabet \(0<1\). Define \(L(w)\) to be the number of **distinct nonempty contiguous Lyndon factors** of \(w\), and \(P_w(t)=\sum_{v\in\mathcal L(w)}t^{|v|}\), where \(\mathcal L(w)\) is their set. Then

\[
\begin{aligned}
P_w(t)={}&2t
+\sum_{i=1}^{a}\sum_{j=1}^{b}t^{i+j}
+\sum_{i=1}^{c}\sum_{j=1}^{d}t^{i+j}
-\sum_{i=1}^{\min(a,c)}\sum_{j=1}^{\min(b,d)}t^{i+j}\\
&+\sum_{i=c+1}^{a}\sum_{j=1}^{d}t^{i+b+c+j}
+\mathbf1_{a\ge c}\sum_{j=b+1}^{d}t^{2c+b+j}.
\end{aligned}
\]

Empty sums are zero. Thus the entire length spectrum is explicit, and in particular

\[
L(w)=2+ab+cd-\min(a,c)\min(b,d)
+(a-c)_+d+\mathbf1_{a\ge c}(d-b)_+,
\qquad (x)_+=\max(x,0).
\]

For every integer \(n\ge4\), the sharp maximum among all positive quadruples of total length \(n\) is

\[
\boxed{\max_{a+b+c+d=n}L(0^a1^b0^c1^d)
=\left\lfloor\frac{n^2}{4}\right\rfloor-1.}
\]

Equality holds **precisely** for \(b=c=1\) and \(|a-d|\le1\); hence there is one maximizing quadruple for even \(n\) and two for odd \(n\). This is exactly three fewer than the unrestricted binary-word maximum \(\lfloor n^2/4\rfloor+2\) of Glen, Simpson and Smyth.

The sum over all positive four-part compositions has the rational generating function

\[
\boxed{\sum_{a,b,c,d\ge1}L(0^a1^b0^c1^d)z^{a+b+c+d}
=\frac{z^4(2z^4-2z^2+6z+3)}{(1-z)^6(1+z)^2}.}
\]

If \(W_n\) is uniform among these \(\binom{n-1}{3}\) words of length \(n\), and \((A,B,C,D)\) has the uniform Dirichlet distribution on \(A+B+C+D=1\), then

\[
\frac{L(W_n)}{n^2}\ \xrightarrow{\mathrm d}\
F(A,B,C,D)=AB+CD-\min(A,C)\min(B,D)+(A-C)_+D.
\]

The convergence holds for the first two moments, and the limiting law is nondegenerate with

\[
\boxed{\mathbb EF=\frac9{80},\qquad
\operatorname{Var}(F)=\frac{19}{6400}.}
\]

In particular \(\mathbb E L(W_n)=\frac9{80}n^2+O(n)\).

## Assumptions and scope

A nonempty word is *Lyndon* if it is lexicographically smaller than each nonempty proper suffix, equivalently the lexicographically least primitive cyclic rotation. Factors are **contiguous**, not scattered subsequences. Different occurrences of an identical factor contribute only once. The alphabet order is \(0<1\), all four run lengths are positive, and the empty word is excluded. \(\mathbf1_Q\) denotes the indicator of proposition \(Q\). Limits concern uniform positive compositions, not independent uniformly sampled binary strings.

## Proof

**1. Exhaustive classification.** A Lyndon factor of length greater than one must contain both symbols, begin with \(0\), and end with \(1\). If it started with \(1\), a suffix beginning with \(0\) would be smaller; if it ended with \(0\), its final one-letter suffix would be smaller. A constant word of length greater than one is not primitive. Consequently, among factors of a four-run word, only those with two or four alternating runs can be nontrivial Lyndon words.

Every \(0^i1^j\) with \(i,j\ge1\) is Lyndon, and occurs precisely when \((i\le a, j\le b)\) or \((i\le c,j\le d)\). Thus the distinct two-run factors form the union of two integer rectangles, with their intersection subtracted once.

A four-run factor must be \(0^i1^b0^c1^j\) with \(1\le i\le a\) and \(1\le j\le d\). The only possibly competing proper suffixes begin inside its middle zero run. If \(i>c\), the factor has more initial zeros than every such suffix and is Lyndon. If \(i<c\), the suffix \(0^c1^j\) is smaller. If \(i=c\), compare \(0^c1^b0^c1^j\) with \(0^c1^j\): the factor is smaller exactly when \(j>b\); otherwise the latter is a smaller proper prefix/suffix. Proper suffixes beginning in a one-run are greater. This proves the disjoint four-run factor family

\[
\bigl\{0^i1^b0^c1^j:i>c,\ i\le a,\ 1\le j\le d\bigr\}
\ \sqcup\
\bigl\{0^c1^b0^c1^j:a\ge c,\ b<j\le d\bigr\}.
\]

Add the two singleton letters and group by length. This yields \(P_w(t)\). Setting \(t=1\) yields the displayed closed count. No factor types are omitted, and the families are disjoint except for the explicitly corrected two-run rectangle overlap.

**2. Sharp extremum and all equality cases.** Put \(Z=a+c\) and \(O=b+d\); thus \(Z+O=n\). Subtracting the exact count from \(ZO\) gives the following exhaustive cases:

\[
ZO-L(w)=
\begin{cases}
 ad+cb+a\min(b,d)-2,&a<c,\\
 c(b+2d)-2,&a\ge c,\ d\le b,\\
 (c-1)d+(2c+1)b-2,&a\ge c,\ d>b.
\end{cases}
\]

The first case is at least \(2\), since \(c\ge2\). The second is at least \(1\), with equality iff \(c=b=d=1\); the third is at least \(1\), with equality iff \(c=b=1\). Together, \(ZO-L(w)\ge1\), and equality holds exactly iff \(b=c=1\). Since \(ZO\le\lfloor n^2/4\rfloor\), the claimed maximum follows. Equality in both inequalities forces \(|Z-O|\le1\), which with \(b=c=1\) is precisely \(|a-d|\le1\). Conversely all such positive quadruples realize equality. For even \(n\), only \(a=d=(n-2)/2\) works; for odd \(n\) the two assignments differ by one.

**3. Sum across compositions.** The constant \(2\), the two rectangle areas, their overlap, the strict excess \((a-c)_+d\), and the tie-boundary term \(\mathbf1_{a\ge c}(d-b)_+\) have separate ordinary generating functions, respectively

\[
\begin{aligned}
&\frac{2z^4}{(1-z)^4},\qquad
\frac{2z^4}{(1-z)^6},\qquad
-\frac{z^4}{(1-z)^4(1-z^2)^2},\\
&\frac{z^5}{(1-z)^5(1-z^2)},\qquad
\frac{z^5}{(1-z)^3(1-z^2)^2}.
\end{aligned}
\]

For example, \(\min(a,c)=\sum_{k\ge1}\mathbf1_{a,c\ge k}\), explaining the overlap denominator. The positive excess and tie terms are geometric sums with the positive-integer identity \(\sum_{h\ge1}hz^h=z/(1-z)^2\). Summing these five rational functions and simplifying gives the stated generating function; it is an identity of formal power series, requiring no numerical extrapolation.

**4. Conditional limit and moments.** Uniform positive quadruples summing \(n\), rescaled by \(n\), converge to the uniform Dirichlet distribution on the three-dimensional simplex. The exact count divided by \(n^2\) equals the continuous homogeneous quadratic function \(F\) plus an error bounded by \((n+2)/n^2\), because the tie-boundary term is at most \(n\). Hence distributional convergence holds; boundedness on the compact simplex supplies convergence of the first two moments.

For explicit integration put \(S=A+C\), \(U=A/S\), and \(V=B/(1-S)\). Under Dirichlet\((1,1,1,1)\), \(S\sim\mathrm{Beta}(2,2)\), and \(U,V\) are independent uniforms on \([0,1]\), independent of \(S\). Writing \(F=S(1-S)g(U,V)\), elementary substitution gives, on the four rectangles separated by \(U=1/2\) and \(V=1/2\),

\[
 g(U,V)=
 \begin{cases}
 (1-U)(1-V),&U\le1/2,\ V\le1/2,\\
 1-V-2U+3UV,&U\le1/2,\ V\ge1/2,\\
 UV+U-V,&U\ge1/2,\ V\le1/2,\\
 -1+2U+V-UV,&U\ge1/2,\ V\ge1/2.
 \end{cases}
\]

Direct polynomial integration over those rectangles yields \(\mathbb Eg=9/16\) and \(\mathbb Eg^2=35/96\). The beta integrals give \(\mathbb E[S(1-S)]=1/5\) and \(\mathbb E[S^2(1-S)^2]=3/70\). Independence therefore yields \(\mathbb EF=9/80\), \(\mathbb EF^2=(35/96)(3/70)=1/64\), and \(\operatorname{Var}(F)=1/64-(9/80)^2=19/6400>0\). Expanding the generating function near \(z=1\), or summing the homogeneous terms, yields the stated \(O(n)\) error in the unnormalized expectation.

## Verification

The accompanying standalone `verify.py` uses only Python's standard library. It constructs every distinct factor literally and tests the strict-proper-suffix definition of Lyndon. It compares complete length multisets, not only totals, against the structural families for every quadruple with \(1\le a,b,c,d\le7\) (2,401 cases). It also checks all fixed-length maxima, every optimizer, and the rational generating-function coefficients independently for \(4\le n\le30\), and evaluates the four polynomial integrals for the limiting moments using exact rational arithmetic. These finite checks corroborate but are not used to assert the general theorem. Run `python verify.py`; no external data files or packages are required.

## Relationship to prior work

Glen, Simpson and Smyth [1] prove the unrestricted maximum of distinct Lyndon factors in words of length \(n\), yielding \(\lfloor n^2/4\rfloor+2\) for binary words; they also calculate expectations under the independent uniform-letter model and examine Christoffel words. That general maximum provides an upper bound, but it does **not** give the exact constrained four-run spectrum, the three-unit loss and equality rigidity, or the composition-conditioned law obtained here. The Christoffel formula applies to a special Sturmian/Lyndon family, not arbitrary four-run words. Hirakawa, Nakashima, Inenaga and Takeda [2] summarize known global factor extrema and investigate Lyndon **subsequences**; their unrestricted models differ from this fixed-run factor family. Distinguishing contiguity and the sampling measure is essential to the claim.

## Limitations

The classification concerns exactly four positive runs, binary order \(0<1\), and **distinct** factors. It does not enumerate Lyndon factor occurrences with multiplicity, Lyndon factors over different alphabets or alphabet orders, or arbitrary run counts. The limiting law is given explicitly as a Dirichlet pushforward and its first two moments; an elementary closed-form cumulative distribution is not claimed. Exhaustive finite checks are not infinite certificates, and literature searches cannot rule out every unindexed equivalent derivation. No independent audit has been performed.

## References

[1] A. Glen, J. Simpson, W. F. Smyth, *Counting Lyndon factors*, Electronic Journal of Combinatorics 24(3), P3.28 (2017), DOI 10.37236/6915, first available arXiv:1701.00928 (2017-01-04), https://arxiv.org/abs/1701.00928 .

[2] R. Hirakawa, Y. Nakashima, S. Inenaga, M. Takeda, *Counting Lyndon Subsequences*, arXiv:2106.01190 (first public 2021-06-02), https://arxiv.org/abs/2106.01190 .
