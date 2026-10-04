# Exact sampling rigidity for singleton Carathéodory–Fejér extremals
## Finding
For integers \(m\ge 3\) and \(n\ge 3\), define
\[
D_{m,n}=\sup\Bigl\{\lambda\in\mathbb R:\exists c\in\mathbb R,\ 1+\lambda\cos(2\pi j/m)+c\cos(2\pi n j/m)\ge0\ \text{for every }j\in\mathbb Z\Bigr\}.
\]
Then
\[
D_{m,n}\ge \sec\!\left(\frac{\pi}{2n}\right),
\]
with equality if and only if \(4n\mid m\). If \(4n\nmid m\), then the inequality is strict; this includes the possibility \(D_{m,n}=+\infty\) when the sampled frequencies alias.

Thus the finite cyclic grid reproduces the continuous singleton Carathéodory–Fejér extremal value exactly when it contains the two contact points of the continuous extremizer. The arithmetic criterion for that event is precisely \(4n\mid m\).

## Assumptions and scope
The parameters are integers \(m\ge3\) and \(n\ge3\). The coefficient \(c\) is unrestricted and real. Nonnegativity is required only on the \(m\)-point grid. The assertion concerns the higher singleton harmonics; no claim of a finite value is made in aliasing cases, where the supremum can be infinite.

Put
\[
\alpha=\frac{\pi}{2n},\qquad C=\cos\alpha,\qquad S=\sin\alpha,
\]
and set
\[
\lambda_*=\sec\alpha,\qquad c_*=\frac{(-1)^n}{n}\tan\alpha.
\]
The reference continuous polynomial is
\[
\phi_n(\theta)=1+\lambda_*\cos\theta+c_*\cos(n\theta).
\]

## Proof
We first prove that \(\phi_n\) is nonnegative on the whole circle and has exactly two zeros.

Write \(\theta=\pi+x\), put \(y=\cos x\), and let \(T_n\) be the Chebyshev polynomial characterized by \(T_n(\cos x)=\cos(nx)\). Multiplication by \(C>0\) gives
\[
C\phi_n(\pi+x)=F_n(y):=C-y+\frac{S}{n}T_n(y).
\]
Since \(T_n(C)=\cos(n\alpha)=0\) and
\[
T_n'(C)=nU_{n-1}(C)=\frac{n}{S},
\]
we can rewrite
\[
F_n(y)=\frac{S}{n}\Bigl(T_n(y)-T_n(C)-T_n'(C)(y-C)\Bigr).
\]
Let \(x_0=\cos(\pi/n)=\cos(2\alpha)\). On \([x_0,1]\), the polynomial \(T_n\) is strictly convex. Indeed, for \(y=\cos t\) with \(0<t<\pi/n\),
\[
T_n'(y)=n\frac{\sin(nt)}{\sin t}.
\]
The quotient on the right strictly decreases with \(t\): for \(0<t<\pi/(2n)\) this follows from \(\tan(nt)>n\tan t\), while for \(\pi/(2n)<t<\pi/n\) its derivative has both terms negative. Because \(y=\cos t\) decreases with \(t\), this proves strict convexity. Therefore the tangent line to \(T_n\) at \(C\) lies strictly below \(T_n\) on \([x_0,1]\) except at \(C\).

For \(y\le x_0\), the tangent line
\[
L(y)=T_n'(C)(y-C)=\frac{n}{S}(y-C)
\]
is increasing, and
\[
-L(x_0)=n\frac{\sin(3\alpha/2)}{\cos(\alpha/2)}>1.
\]
The last inequality follows from \(\sin t\ge 2t/\pi\) on \([0,\pi/2]\), which gives \(n\sin(3\alpha/2)\ge3/2\). Hence \(L(y)<-1\le T_n(y)\) for \(y\le x_0\). Combining the two regions shows
\[
F_n(y)\ge0\quad(-1\le y\le1),
\]
with equality only at \(y=C\). Consequently \(\phi_n\ge0\) on the circle, and its zeros are exactly
\[
\theta=\pi-\alpha\quad\text{and}\quad\theta=\pi+\alpha\pmod{2\pi}.
\]
This also gives the continuous singleton value directly: evaluating any globally nonnegative polynomial of the stated form at \(\theta=\pi-\alpha\), where \(\cos(n\theta)=0\) and \(\cos\theta=-C\), gives \(\lambda\le1/C\), while \(\phi_n\) attains equality.

Now pass to the finite grid. The fractions of a full turn corresponding to the two contact points are
\[
\frac{2n-1}{4n}\quad\text{and}\quad\frac{2n+1}{4n}.
\]
Each fraction is reduced because \(\gcd(2n\pm1,4n)=1\). Hence a contact point belongs to the \(m\)-point grid if and only if \(4n\mid m\).

If \(4n\mid m\), evaluation at a contact grid point annihilates the \(n\)-th harmonic and gives \(1-\lambda C\ge0\), so every feasible sampled polynomial has \(\lambda\le1/C\). Since \(\phi_n\) is feasible, \(D_{m,n}=\sec\alpha\).

If \(4n\nmid m\), the grid misses both zeros, so \(\phi_n\) is strictly positive at every sampled point. Define
\[
\varepsilon=\frac12\min_{\substack{0\le j<m\\ \cos(2\pi j/m)<0}}
\frac{\phi_n(2\pi j/m)}{-\cos(2\pi j/m)}.
\]
The set in this minimum is nonempty and finite, and every numerator is positive, so \(\varepsilon>0\). Increasing the first-harmonic coefficient from \(\lambda_*\) to \(\lambda_*+\varepsilon\) preserves nonnegativity: points with nonnegative cosine only increase, and points with negative cosine retain at least half their positive margin. Thus \(D_{m,n}>\lambda_*\), as claimed.

## Verification
The proof above is the certificate for all \(m\ge3\) and \(n\ge3\); finite computation is not used to infer the theorem. The accompanying standard-library script `artifacts/verify.py` independently checks the explicit extremizer, contact-point criterion, and strict-margin perturbation for every \(3\le n\le40\) and \(3\le m\le300\). It also samples the continuous polynomial densely as a corroborative numerical check.

## Relationship to prior work
Kolountzakis and Révész introduced the continuous and discretized Carathéodory–Fejér quantities \(M(H)\) and \(M_m(H)\), recorded the basic inequality \(M_m(H)\ge M(H)\), and treated the singleton continuous extremum in the positive-definite-function framework. Their discrete discussion also notes that frequency aliasing can make a sampled extremum infinite. The present statement isolates a different question: for a singleton higher harmonic, exactly which finite grids already have the continuous extremal value? The answer is the contact-set divisibility criterion \(4n\mid m\), with strict gain on every other grid.

Krenedits and Révész later extended the Carathéodory–Fejér framework to locally compact Abelian groups and explained the reduction to discrete problems on cyclic groups. That broader framework supplies context but does not by itself determine when a finite cyclic sample has equality rather than strict gain; the contact-set argument above supplies that comparison.

## Limitations
The result determines the exact equality-versus-strict-gain dichotomy but does not give a closed formula for \(D_{m,n}\) when \(4n\nmid m\). Some such sampled problems are unbounded because of frequency aliasing. The proof is specialized to a single auxiliary harmonic and does not classify arbitrary finite sets of permitted harmonics.

## References
1. M. N. Kolountzakis and S. Gy. Révész, *On pointwise estimates of positive definite functions with given support*, arXiv:math/0302193v1, first submitted 2003-02-17; Canadian Journal of Mathematics 58 (2006), 401–418. Primary MSC 42B10.
2. S. Krenedits and S. Gy. Révész, *The Carathéodory–Fejér type extremal problem on locally compact Abelian groups*, arXiv:1304.0071v1, first submitted 2013-03-30; Journal of Approximation Theory 194 (2015), 108–131.
