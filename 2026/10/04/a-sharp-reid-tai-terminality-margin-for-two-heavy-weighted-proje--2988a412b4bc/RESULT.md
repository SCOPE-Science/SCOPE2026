# A sharp Reid–Tai terminality margin for two-heavy weighted projective spaces
## Finding
For every integer \(r\ge2\), let
\[
X_{r,a,b}=\mathbb P(1^r,a,b),\qquad 1\le a\le b,
\]
and suppose \(X_{r,a,b}\) is canonical and singular. Define \(\alpha(X)\) as the minimum Reid–Tai age among nonidentity elements in the two cyclic quotient charts centered at the coordinates of weights \(a\) and \(b\). Then
\[
\alpha(X)=\min\!\left(\left\{\frac{r+(b\bmod a)}{a}:a>1\right\}\cup\left\{\frac{r+(a\bmod b)}{b}:b>1\right\}\right).
\]
In particular, \(\alpha(X)=1\) exactly on the canonical non-terminal boundary. If \(X\) is terminal and singular, then
\[
\alpha(X)\ge 1+\frac{1}{3r-3},
\]
with equality if and only if
\[
(a,b)=(2r-2,3r-3).
\]

## Assumptions and scope
The statement concerns the well-formed weighted projective space with \(r\) coordinates of weight \(1\) and two additional positive weights \(a\le b\). The quantity \(\alpha(X)\) is deliberately defined as a minimum of local Reid–Tai ages in the two heavy-coordinate charts; no identification with a differently normalized global minimal-log-discrepancy convention is asserted.

Write \(d=b-a\). For this family the canonical region is
\[
0\le d\le r,\qquad 1\le a\le r+d,
\]
and the terminal region is
\[
0\le d<r,\qquad 1\le a<r+d.
\]
These criteria are used only to delimit the family over which the quantitative age estimate is proved.

## Proof
At the weight-\(a\) coordinate, the local quotient is represented by
\[
\frac1a(1^r,b).
\]
For \(1\le k<a\), its Reid–Tai age is
\[
A_k=\frac{rk+(kb\bmod a)}{a}=\frac{rk+(kd\bmod a)}{a}.
\]
We show that \(A_1\) is minimal throughout the canonical region. If \(a\le r\) and \(k\ge2\), then
\[
A_k\ge\frac{2r}{a}\ge \frac r a+1>\frac{r+(d\bmod a)}a=A_1.
\]
If instead \(a>r\), canonicity gives \(d\le r<a\), so \(d\bmod a=d\); hence for \(k\ge2\),
\[
A_k\ge\frac{2r}{a}\ge\frac{r+d}{a}=A_1.
\]
Thus, whenever \(a>1\),
\[
\min_{1\le k<a}A_k=\frac{r+(b\bmod a)}a.
\]

At the weight-\(b\) coordinate, the local quotient is
\[
\frac1b(1^r,a),
\]
with ages
\[
B_k=\frac{rk+(ka\bmod b)}b.
\]
If \(d=0\), then \(a=b\) and \(B_k=rk/b\), so \(B_1=r/b\) is minimal. Assume \(d>0\). Write \(kd=qb+s\) with \(0\le s<b\). Since \(a=b-d\), when \(s=0\) one has
\[
rk=kd+k(r-d)=qb+k(r-d)\ge b+(r-d)=r+a,
\]
and when \(s>0\),
\[
rk+(ka\bmod b)=rk+b-s=(q+1)b+k(r-d)\ge b+(r-d)=r+a.
\]
Equality is attained at \(k=1\). Therefore, whenever \(b>1\),
\[
\min_{1\le k<b}B_k=\frac{r+(a\bmod b)}b.
\]
Taking the minimum of the two chart minima proves the displayed formula for \(\alpha(X)\).

Now consider the canonical non-terminal boundary. If \(d=r\), then
\[
\frac{r+a}{b}=\frac{r+a}{a+r}=1.
\]
If \(a=r+d\), the weight-\(a\) chart has first age \(1\) (including the case \(d=0\), where it is \(r/a=1\)). Conversely, the strict terminal inequalities make both chart minima strictly greater than \(1\). Hence \(\alpha(X)=1\) exactly for canonical non-terminal members.

Finally suppose \(X\) is terminal and singular. If \(d=0\), then
\[
\alpha(X)=\frac r a\ge\frac r{r-1}=1+\frac1{r-1}>1+\frac1{3r-3}.
\]
If \(d>0\), the weight-\(b\) chart gives
\[
B_1=\frac{r+a}{b}=1+\frac{r-d}{b}.
\]
Terminality gives \(d\le r-1\) and \(a\le r+d-1\), so
\[
b=a+d\le r+2d-1\le3r-3.
\]
Thus
\[
B_1\ge1+\frac1{3r-3}.
\]
Equality forces \(r-d=1\) and \(b=3r-3\), hence \(d=r-1\) and \(a=2r-2\). The weight-\(a\) chart cannot lower this value: terminality makes its first age an integer-over-\(a\) rational strictly larger than \(1\), so
\[
A_1\ge1+\frac1a\ge1+\frac1{2r-2}>1+\frac1{3r-3}.
\]
At \((a,b)=(2r-2,3r-3)\), the weight-\(b\) first age is exactly the claimed bound. This proves sharpness and uniqueness.

## Verification
The accompanying script `verify_reid_tai_margin.py` evaluates every nonidentity element in both heavy-coordinate cyclic quotient charts for every canonical parameter pair with \(2\le r\le60\). It checks the closed formula for \(\alpha(X)\), the canonical/terminal threshold, the lower bound, and the unique equality pair in every tested dimension. Its successful terminal output is `VERIFY_OK`.

## Relationship to prior work
Reid–Tai age criteria for cyclic quotient singularities are standard; Borisov formulates terminal/canonical cyclic quotient conditions in terms of sums of fractional coordinates, and Kasprzyk uses the corresponding fractional-part criterion in the classification of terminal weighted projective spaces. The contribution here is the family-specific reduction of all nonidentity age checks to the first group element in each heavy chart, followed by the exact sharp terminality margin and its unique equality family. Searches against published-finding corpus for the same family, Reid–Tai ages, minimal-discrepancy language, and weighted-projective terminality did not return a statement implying this all-dimensional quantitative formula.

## Limitations
The result is restricted to the two-heavy family \(\mathbb P(1^r,a,b)\). The finite replay through \(r=60\) is a regression check, not the proof of the all-dimensional statement. The terminology \(\alpha(X)\) is local Reid–Tai age terminology and should not be silently replaced by a global minimal-log-discrepancy normalization.

## References
- A. Borisov, *Quotient singularities, integer ratios of factorials and the Riemann Hypothesis*, arXiv:math/0505167 (first public version 2005-05-10).
- A. M. Kasprzyk, *Classifying terminal weighted projective space*, arXiv:1304.3029 (first public version 2013-04-10).
