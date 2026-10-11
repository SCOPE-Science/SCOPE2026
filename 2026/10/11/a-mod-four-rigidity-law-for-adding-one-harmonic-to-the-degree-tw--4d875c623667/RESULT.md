# A mod-four rigidity law for adding one harmonic to the degree-two Carathéodory–Fejér problem
## Finding
For every integer \(n\ge3\), define
\[
M_n=\sup\left\{a\in\mathbb R:\exists b,c\in\mathbb R,\ 
1+a\cos\theta+b\cos(2\theta)+c\cos(n\theta)\ge0
\text{ for every }\theta\in\mathbb R\right\}.
\]
Then
\[
M_n=\sqrt2\quad\Longleftrightarrow\quad n\equiv2\pmod4.
\]
For every \(n\not\equiv2\pmod4\), the additional \(n\)-th harmonic gives a genuine improvement:
\[
M_n>\sqrt2.
\]

## Assumptions and scope
The integer \(n\) satisfies \(n\ge3\), so the added harmonic is distinct from the first two harmonics. Coefficients \(a,b,c\) are real and nonnegativity is required at every real \(\theta\). The normalization fixes the constant Fourier coefficient at \(1\).

The result classifies exactly when one extra allowed harmonic leaves the classical degree-two Carathéodory–Fejér optimum unchanged. It does not determine the exact value of \(M_n\) in the strict-improvement residue classes.

## Proof
Start from the classical degree-two extremizer
\[
Q(\theta)
 =1+\sqrt2\cos\theta+\frac12\cos(2\theta)
 =\left(\cos\theta+\frac1{\sqrt2}\right)^2.
\]
Thus \(Q(\theta)\ge0\) for every \(\theta\), so \(M_n\ge\sqrt2\) for every \(n\ge3\).

Put
\[
\theta_0=\frac{3\pi}{4}.
\]
Then
\[
\cos\theta_0=-\frac1{\sqrt2},
\qquad
\cos(2\theta_0)=0.
\]

Suppose first that \(n\equiv2\pmod4\). Then
\[
\cos(n\theta_0)=\cos\left(\frac{3\pi n}{4}\right)=0.
\]
For any admissible polynomial
\[
T(\theta)=1+a\cos\theta+b\cos(2\theta)+c\cos(n\theta),
\]
evaluation at \(\theta_0\) gives
\[
0\le T(\theta_0)=1-\frac{a}{\sqrt2}.
\]
Hence \(a\le\sqrt2\). Since \(Q\) attains \(a=\sqrt2\), it follows that
\[
M_n=\sqrt2.
\]

Now suppose that \(n\not\equiv2\pmod4\). Set
\[
\gamma_n=\cos\left(\frac{3\pi n}{4}\right),
\qquad
s=\operatorname{sgn}(\gamma_n),
\qquad
P_n(\theta)=\cos\theta+2s\cos(n\theta).
\]
The zero set of \(Q\) modulo \(2\pi\) is
\[
Z=\left\{\frac{3\pi}{4},\frac{5\pi}{4}\right\}.
\]
Because
\[
\cos\left(\frac{5\pi n}{4}\right)
=\cos\left(2\pi n-\frac{3\pi n}{4}\right)
=\gamma_n,
\]
the perturbation has the same value at both contact points:
\[
P_n(\theta)
=-\frac1{\sqrt2}+2|\gamma_n|
\qquad(\theta\in Z).
\]
If \(n\) is odd, then \(|\gamma_n|=1/\sqrt2\); if \(n\equiv0\pmod4\), then \(|\gamma_n|=1\). In either case
\[
-\frac1{\sqrt2}+2|\gamma_n|>0.
\]

By continuity there is an open neighborhood \(U\) of \(Z\) and a number \(\eta>0\) such that
\[
P_n(\theta)\ge\eta
\qquad(\theta\in U).
\]
On the compact complement of \(U\) modulo \(2\pi\), the continuous function \(Q\) has no zeros, so
\[
Q(\theta)\ge\delta>0
\]
there. Let
\[
B=\max_{\theta\in\mathbb R}|P_n(\theta)|.
\]
Choose \(0<\varepsilon\le\delta/(2B)\). On \(U\),
\[
Q(\theta)+\varepsilon P_n(\theta)\ge\varepsilon\eta>0,
\]
while outside \(U\),
\[
Q(\theta)+\varepsilon P_n(\theta)
\ge\delta-\varepsilon B
\ge\frac{\delta}{2}>0.
\]
Therefore
\[
T_\varepsilon(\theta)=Q(\theta)+\varepsilon P_n(\theta)
\]
is nonnegative for every real \(\theta\). Its first-harmonic coefficient is
\[
\sqrt2+\varepsilon>\sqrt2,
\]
so \(M_n>\sqrt2\).

The two cases exhaust the integers \(n\ge3\), proving the claimed equivalence.

## Verification
The proof is analytic and uses only an explicit square factorization, evaluation at the two contact points, and compactness away from those contacts.

The accompanying checker independently confirms the residue-class identity
\[
\cos\left(\frac{3\pi n}{4}\right)=0
\quad\Longleftrightarrow\quad
n\equiv2\pmod4
\]
over a finite test range, checks positivity of the proposed perturbation at both contacts in every strict residue class, and performs dense-grid stress tests of small perturbations. These finite checks are corroborative only; they are not used to infer the universal theorem.

## Relationship to prior work
Krenedits and Révész formulate the Carathéodory–Fejér extremal problem for prescribed frequency supports on locally compact abelian groups and connect it with positive-definite functions and sequences. Their framework contains the present optimization problem as a special support choice but does not, in the inspected text, give the mod-four classification above.

Kolountzakis and Révész likewise formulate the one-dimensional support-restricted problem for an arbitrary set of allowed higher frequencies. Their general formulation motivates asking which added frequencies actually improve the classical degree-two optimum. The present result gives a complete answer when exactly one additional frequency \(n\ge3\) is allowed.

The closest indexed comparisons located during the literature check concern finite-grid degree-two Carathéodory–Fejér constants, the isolated support \(\{1,2,4\}\), and other incomparable sparse supports. Those results neither state nor imply the all-\(n\) continuous mod-four dichotomy proved here.

## Limitations
The theorem determines only whether the value stays at \(\sqrt2\) or becomes strictly larger. It does not compute the exact value of \(M_n\) when \(n\not\equiv2\pmod4\), nor does it classify extremizers in those strict cases.

An equivalent short contact-point argument may exist in older sparse trigonometric-polynomial literature under different notation. The literature searches and full-text comparisons described in the review reduce but do not eliminate that residual risk.

## References
1. S. Krenedits and Sz. Gy. Révész, *The Caratheodory-Fejér type extremal problem on locally compact Abelian groups*, arXiv:1304.0071.
2. M. N. Kolountzakis and Sz. Gy. Révész, *On Pointwise Estimates of Positive Definite Functions With Given Support*, Canadian Journal of Mathematics 58 (2006), 401–426, DOI 10.4153/CJM-2006-017-8.
