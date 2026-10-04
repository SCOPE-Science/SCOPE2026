# Degree six is the first exact blind spot of adaptive Simpson's local error test
## Finding
Let \(S_1\) be the one-panel Simpson rule on \([-1,1]\), let \(S_2\) be the sum of the Simpson rules on \([-1,0]\) and \([0,1]\), and let
\[
D(p)=S_2(p)-S_1(p).
\]
The standard local adaptive Simpson test uses \(D\) as its Richardson error signal and accepts an interval when \(|D|/15\) is below the requested local tolerance.

For every polynomial
\[
p(t)=\sum_{j=0}^{6} a_j t^j
\]
of degree at most six,
\[
D(p)=-\frac14a_4-\frac5{16}a_6.
\]
Consequently, among polynomials of degree at most six,
\[
D(p)=0
\quad\Longleftrightarrow\quad
4a_4+5a_6=0,
\]
and on this kernel the true error of the accepted two-panel value is exactly
\[
\int_{-1}^{1}p(t)\,dt-S_2(p)=-\frac1{21}a_6.
\]
It follows that no polynomial of degree at most five can give a false zero of the local test, while degree six is the first possible degree.

The failure does not require a zero or singular integrand. The strictly positive polynomial
\[
p_*(t)=-t^6+\frac54t^4+\frac1{84}
      =t^4\left(\frac54-t^2\right)+\frac1{84}
\]
satisfies
\[
p_*(t)\ge\frac1{84}>0\qquad(-1\le t\le1),
\]
yet
\[
S_1(p_*)=S_2(p_*)=\frac4{21},
\qquad
\int_{-1}^{1}p_*(t)\,dt=\frac5{21}.
\]
Thus a standard adaptive Simpson call whose root decision is based only on the classical difference test accepts immediately for every positive tolerance and returns a value with relative error \(1/5\).

After the affine change \(t=(2x-a-b)/(b-a)\), the same classification holds on every nondegenerate interval \([a,b]\). If \(a_6\) denotes the coefficient of \(t^6\) in normalized coordinates, then a false-zero degree-six polynomial satisfies \(4a_4+5a_6=0\) and has exact local error
\[
\int_a^b f(x)\,dx-S_2(f)=-\frac{b-a}{42}a_6.
\]

## Assumptions and scope
The statement concerns exact arithmetic and the classical local comparison between one Simpson panel and two equal half-panel Simpson panels. It applies to implementations that make the root acceptance decision solely from the standard Richardson signal \(S_2-S_1\), with or without adding the usual correction \((S_2-S_1)/15\) to the accepted value.

The result is not a claim that every modern automatic integrator has this failure. Production codes may impose minimum refinement, use independent error estimators, vary the quadrature family, inspect interpolants, or add other safeguards. Floating-point evaluation of the displayed witness may produce a tiny nonzero difference because of rounding, whereas the theorem is an exact-arithmetic statement about the mathematical rule.

## Proof
By symmetry, the integral, \(S_1\), and \(S_2\) all vanish on odd monomials. Both Simpson rules are exact on polynomials of degree at most three. It therefore suffices to evaluate the even monomials of degrees four and six.

For \(t^4\),
\[
S_1(t^4)=\frac23,\qquad
S_2(t^4)=\frac5{12},\qquad
\int_{-1}^{1}t^4\,dt=\frac25.
\]
Hence
\[
D(t^4)=-\frac14,\qquad
\int_{-1}^{1}t^4\,dt-S_2(t^4)=-\frac1{60}.
\]

For \(t^6\),
\[
S_1(t^6)=\frac23,\qquad
S_2(t^6)=\frac{17}{48},\qquad
\int_{-1}^{1}t^6\,dt=\frac27.
\]
Hence
\[
D(t^6)=-\frac5{16},\qquad
\int_{-1}^{1}t^6\,dt-S_2(t^6)=-\frac{23}{336}.
\]

Linearity now gives
\[
D(p)=-\frac14a_4-\frac5{16}a_6.
\]
If \(D(p)=0\), then \(a_4=-5a_6/4\). Substituting this relation into the true error gives
\[
-\frac1{60}a_4-\frac{23}{336}a_6
=
\frac1{48}a_6-\frac{23}{336}a_6
=
-\frac1{21}a_6.
\]
For degree at most five, \(a_6=0\), so \(D(p)=0\) forces \(a_4=0\), and the remaining polynomial is integrated exactly. Degree six is therefore minimal.

For the displayed witness, \(a_6=-1\) and \(a_4=5/4\), so \(D(p_*)=0\) and the true error is \(1/21\). Positivity follows from
\[
t^4\left(\frac54-t^2\right)\ge0
\]
on \([-1,1]\). Direct evaluation gives \(S_1(p_*)=S_2(p_*)=4/21\) and the exact integral \(5/21\).

Under the affine normalization from \([a,b]\) to \([-1,1]\), the integral and both Simpson functionals are multiplied by \((b-a)/2\). Therefore the kernel condition is unchanged and the true error is multiplied by the same factor, yielding \(-(b-a)a_6/42\).

## Verification
The accompanying `verify.py` uses exact rational arithmetic. It computes \(S_1\), \(S_2\), and the exact integral on every monomial through degree six; reconstructs the displayed formulas by linearity; verifies that degree at most five has no false-zero direction; and checks the positive witness exactly, including
\[
S_1=S_2=\frac4{21},\qquad I=\frac5{21}.
\]
It also checks the affine scaling formula on several rational intervals. These calculations verify the arithmetic identities; the proof above establishes the all-polynomial statement.

## Relationship to prior work
The standard adaptive Simpson mechanism and its difference-based stopping rule are classical. Plaskota's analysis explicitly notes that the standard procedure can terminate too early and gives an extreme smooth polynomial example,
\[
f(x)=\prod_{i=0}^{4}(x-i)^2
\]
on \([0,4]\), for which all five root-panel sampling values vanish and the routine returns zero although the integral is positive. That prior example already establishes the existence of catastrophic premature termination and is not claimed here.

Gonnet likewise explains that difference-based error estimators can become accidentally small and thereby produce false small error estimates. That general reliability diagnosis is also prior work.

The present result isolates a different and sharper boundary: it completely identifies the false-zero kernel through degree six, proves that degree six is the first possible degree, gives the exact missed-error functional on that kernel, and supplies a strictly positive degree-six witness whose sampled values do not vanish. The failure is therefore caused by cancellation in the estimator rather than by hiding all mass between sampled zeros.

## Limitations
The theorem classifies only the first local one-versus-two-panel Simpson comparison. It does not claim that safeguarded or hybrid adaptive quadrature software will accept the interval, and it does not analyze floating-point perturbations of the exact cancellation.

The lower-degree nonfailure is closely related to the classical fact that Richardson-corrected Simpson is exact through degree five, so that portion of the boundary is structurally expected. The originality claim is the explicit degree-six kernel, exact missed-error law, and strictly positive cancellation witness. Older adaptive-quadrature literature is extensive, so an equivalent low-degree calculation under different terminology remains a residual literature risk.

## References
1. Leszek Plaskota, *Automatic integration using asymptotically optimal adaptive Simpson quadrature*, Numerische Mathematik 131 (2015), 173–198, DOI: 10.1007/s00211-014-0684-3; first published online November 25, 2014.
2. Pedro Gonnet, *Increasing the Reliability of Adaptive Quadrature Using Explicit Interpolants*, arXiv:1006.3962v1, June 20, 2010; ACM Transactions on Mathematical Software 37 (2010), Article 26.
3. J. N. Lyness, *Notes on the Adaptive Simpson Quadrature Routine*, Journal of the ACM 16 (1969), 483–495, DOI: 10.1145/321526.321537.
