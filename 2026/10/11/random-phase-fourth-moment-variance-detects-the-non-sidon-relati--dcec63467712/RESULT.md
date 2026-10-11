# Random-phase fourth-moment variance detects the non-Sidon relations of a finite integer support
## Finding
Let \(A\subset\mathbb Z\) be finite and nonempty, put \(n=|A|\), and let \((\xi_a)_{a\in A}\) be independent Haar-uniform random variables on the unit circle. Define
\[
P_A(t)=\sum_{a\in A}\xi_a e^{2\pi iat},\qquad X_A=\|P_A\|_{L^4(\mathbb T)}^4,
\]
where \(\mathbb T=\mathbb R/\mathbb Z\) has normalized Haar measure. Let
\[
T(A)=\#\{(x,d):d\in\mathbb Z_{>0},\ x,x+d,x+2d\in A\}
\]
be the number of three-term arithmetic progressions with positive step, and let
\[
Q(A)=\#\{(a,b,c,d)\in A^4:a<b<c<d,\ a+d=b+c\}.
\]
Then
\[
\mathbb E X_A=2n^2-n
\]
and the exact variance is
\[
\boxed{\operatorname{Var}(X_A)=8T(A)+32Q(A)}.
\]
In particular, \(X_A\) is almost surely constant exactly when \(A\) is a Sidon \(B_2\) set, meaning that the map from unordered pairs \(\{a,b\}\) with \(a\le b\) to their sum \(a+b\) is injective. In this zero-variance case one has the stronger phase-independent identity
\[
\left\|\sum_{a\in A}u_a e^{2\pi iat}\right\|_4^4=2n^2-n
\]
for every choice of coefficients satisfying \(|u_a|=1\).

## Assumptions and scope
The support \(A\) is an arbitrary finite subset of the integers. Random coefficients are independent and Haar-uniform on \(\{z\in\mathbb C:|z|=1\}\). The \(L^4\) norm uses normalized Haar measure on \(\mathbb T\). The counts \(T(A)\) and \(Q(A)\) are literal integer counts with the displayed order restrictions; no quotienting by affine symmetries or multiplicities is implicit.

The final equivalence uses the standard finite-integer \(B_2\) convention that equal pair sums are trivial only when the two unordered pairs coincide. A nontrivial equal-sum relation among three distinct points is exactly a three-term arithmetic progression; a nontrivial equal-sum relation among four distinct points has, after sorting, the unique form \(a+d=b+c\). Thus \(T(A)=Q(A)=0\) is equivalent to the \(B_2\) property.

## Proof
For every positive integer \(h\), define the aperiodic correlation
\[
C_h=\sum_{x:\,x,x+h\in A}\xi_{x+h}\overline{\xi_x}.
\]
Fourier orthogonality gives the exact identity
\[
X_A=n^2+2\sum_{h>0}|C_h|^2.
\]
Write \(E_A=\sum_{h>0}|C_h|^2\). Expanding one summand gives
\[
|C_h|^2=r_h+\sum_{\substack{x\ne y\\x,x+h,y,y+h\in A}}
\xi_{x+h}\xi_y\overline{\xi_x\xi_{y+h}},
\]
where \(r_h=\#\{x:x,x+h\in A\}\). Summing \(r_h\) over positive \(h\) counts each unordered pair of distinct elements of \(A\) once, so
\[
\mathbb E E_A=\binom n2,
\]
which yields \(\mathbb E X_A=2n^2-n\).

It remains to compute the squared \(L^2\) norm, over the phase torus, of the nonconstant part of \(E_A\). Haar characters on that torus are orthogonal. Fix an ordered cross term with \(x<y\) and write \(d=y-x\). If the correlation offset is also \(d\), its character is
\[
\xi_{x+d}^2\overline{\xi_x\xi_{x+2d}},
\]
so it records the three-term progression \(x,x+d,x+2d\). This character occurs with coefficient \(1\), and its conjugate occurs with coefficient \(1\). Hence each element counted by \(T(A)\) contributes \(2\) to \(\operatorname{Var}(E_A)\).

If the correlation offset is \(h\ne d\), the four involved points are distinct and the character is
\[
\xi_{x+h}\xi_{x+d}\overline{\xi_x\xi_{x+h+d}}.
\]
The same character occurs exactly twice: once by viewing the four points as two pairs separated by \(h\), and once by viewing them as two pairs separated by \(d\). After sorting the four points, this is exactly one relation \(a+d=b+c\) counted by \(Q(A)\). The character and its conjugate therefore contribute \(2^2+2^2=8\) to \(\operatorname{Var}(E_A)\). The exponent vector of a phase character determines its signed multiset of endpoints, so there are no further collisions between these two relation types or between distinct relations.

Consequently
\[
\operatorname{Var}(E_A)=2T(A)+8Q(A).
\]
Since \(X_A=n^2+2E_A\), multiplication by \(4\) gives
\[
\operatorname{Var}(X_A)=8T(A)+32Q(A).
\]
The variance vanishes exactly when there is no nontrivial equal-sum relation, which is exactly the Sidon \(B_2\) condition. When this happens every nonconstant phase character in the expansion is absent, proving the deterministic phase-independent identity as well.

## Verification
The supplied `artifacts/verify.py` reconstructs the phase-character expansion using exact integer exponent vectors. It checks every nonempty subset of \(\{0,1,\ldots,7\}\), verifying directly that the character-square norm equals \(2T(A)+8Q(A)\). It also checks consecutive supports of sizes \(2\) through \(20\) against their independently simplified parity formulas. The replay is corroborative; the all-support theorem is proved by the character classification above, not by finite enumeration.

## Relationship to prior work
Neuwirth's work on three-frequency Sidon constants treats phase extremality and unconditionality for sparse trigonometric spectra, providing a natural archive-era setting in which the additive geometry of the frequency support controls phase behavior. It does not study random phases or variance of the fourth norm. Borwein and Lockhart study expected \(L^p\) norms of random polynomials, while Katz emphasizes the exact link between fourth norms and mean-square aperiodic autocorrelation for structured unimodular polynomials. The sources inspected do not state the support-sensitive variance decomposition above or the exact \(B_2\)-rigidity criterion.

The new formula separates the only two possible nontrivial collision types for an arbitrary integer support: three-point progressions have weight \(8\), while four-distinct equal-sum relations have weight \(32\). This is stronger than a support-specific variance computation because it identifies the complete additive invariant governing random-phase fourth-moment fluctuations.

## Limitations
The coefficients are Steinhaus phases; different coefficient laws can change collision weights because their higher moments need not match Haar character orthogonality. The support is a subset of \(\mathbb Z\); finite cyclic groups can introduce wraparound and torsion relation types that are absent here. The theorem gives the exact variance, not the full distribution of \(X_A\). Literature searches and source inspections did not locate an equivalent statement, but older random-Fourier or additive-combinatorial literature using different terminology remains a residual originality risk.

## References
1. S. Neuwirth, *The Sidon constant of sets with three elements*, arXiv:math/0102145v1, first public version 19 February 2001; MSC 42A05.
2. P. Borwein and R. Lockhart, *The expected \(L^p\) norm of random polynomials*, Proceedings of the American Mathematical Society 129 (2001), 1463–1472, DOI 10.1090/S0002-9939-00-05690-2.
3. D. J. Katz, *Asymptotic \(L^4\) norm of polynomials derived from characters*, arXiv:1205.1069v1, first public version 4 May 2012; secondary MSC 42A05.
