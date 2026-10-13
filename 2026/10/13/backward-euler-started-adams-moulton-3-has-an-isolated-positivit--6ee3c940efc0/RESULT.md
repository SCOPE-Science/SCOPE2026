# Backward-Euler-started Adams–Moulton 3 has an isolated positivity point at its stability boundary
## Finding
Consider the scalar decay equation \(y'=-\lambda y\) with \(\lambda>0\), fixed step \(h>0\), and \(z=h\lambda\). Set \(y_0=1\), take one backward Euler start
\[
y_1=\frac{1}{1+z},
\]
and then apply the third-order Adams–Moulton formula
\[
y_{n+1}=y_n+\frac{h}{12}\left(5f_{n+1}+8f_n-f_{n-1}\right),\qquad n\ge1.
\]
Then
\[
y_n>0\quad\text{for every }n\ge0
\]
holds if and only if
\[
0<z\le\frac32\quad\text{or}\quad z=6.
\]
Thus the all-step positivity set is disconnected. The point \(z=6\) is exactly the negative-real stability boundary of this Adams–Moulton recurrence, and at that single boundary value the backward Euler starter cancels the alternating mode exactly.

## Assumptions and scope
The claim is trajectory-specific: it concerns the scalar positive decay test equation, the stated backward Euler starter, and the classical constant-step third-order Adams–Moulton method. It is not a nonlinear SSP or arbitrary-data monotonicity theorem. The parameter satisfies \(z=h\lambda>0\).

## Proof
Substitution of \(f_n=-\lambda y_n\) gives
\[
(12+5z)y_{n+1}=(12-8z)y_n+zy_{n-1}.
\]
Write
\[
a=\frac{12-8z}{12+5z},\qquad b=\frac{z}{12+5z},
\]
so \(y_{n+1}=ay_n+by_{n-1}\). For \(0<z\le3/2\), both \(a\) and \(b\) are nonnegative and the two starting values are positive, hence every iterate is positive.

Now suppose \(z>3/2\). The characteristic polynomial
\[
p(r)=r^2-ar-b
\]
has one positive root \(r_+\) and one negative root \(r_-\), and \(a=r_++r_-<0\) implies \(|r_-|>r_+\). Therefore
\[
y_n=C r_+^n+D r_-^n,
\qquad
D=\frac{r_+-y_1}{r_+-r_-}.
\]
A direct evaluation at the backward Euler starter gives the exact identity
\[
p(y_1)=-\frac{z^2(z-6)}{(1+z)^2(12+5z)}.
\]
Because \(p(0)=-b<0\), the sign of this expression determines whether \(y_1\) lies below or above \(r_+\).

If \(3/2<z<6\), then \(p(y_1)>0\), hence \(y_1>r_+\), so \(D<0\) and \(C=1-D>0\). Every odd term is positive, while
\[
y_{2m}=C r_+^{2m}+D|r_-|^{2m}
\]
is eventually negative because \(|r_-|/r_+>1\). Thus all-step positivity fails.

At \(z=6\), one has \(r_+=1/7\), \(r_-=-1\), and \(y_1=1/7=r_+\). Hence \(D=0\) and
\[
y_n=7^{-n}>0
\]
for every \(n\). This is the isolated positive boundary point.

If \(z>6\), then \(p(y_1)<0\), hence \(0<y_1<r_+\) and \(D>0\). Moreover \(D<1\), so \(C>0\). All even terms are positive, but
\[
y_{2m+1}=C r_+^{2m+1}-D|r_-|^{2m+1}
\]
is eventually negative. Again all-step positivity fails.

For the stability comparison, observe
\[
p(1)=\frac{12z}{12+5z}>0,
\qquad
p(-1)=-\frac{4(z-6)}{12+5z}.
\]
Thus for \(0<z<6\), \(r_+\in(0,1)\) and \(r_-\in(-1,0)\); at \(z=6\), \(r_-=-1\). Hence the interval \(3/2<z<6\) is linearly stable but eventually sign-changing, while \(z=6\) is the stability-boundary resonance described above.

## Verification
At the exact interior-stable witness \(z=2\), the recurrence has \(a=-2/11\), \(b=1/11\), and
\[
y_0=1,\quad y_1=\frac13,\quad y_2=\frac1{33},\quad y_3=\frac3{121},\quad y_4=-\frac7{3993}<0.
\]
At \(z=6\), exact recurrence replay gives \(y_n=7^{-n}\). The bundled `verify.py` checks these rational identities, the formulas for \(p(y_1)\), \(p(1)\), and \(p(-1)\), and the boundary recurrence. These checks support but do not replace the all-parameter root-sign argument above.

## Relationship to prior work
Adams–Moulton stability theory is classical; Brown, Riley, and Bennett studied stability properties of Adams–Moulton-type methods in 1965. Hundsdorfer, Ruuth, and Spiteri studied positivity and monotonicity of linear multistep methods with starting procedures, and their 2002 report explicitly emphasizes that suitable starting procedures can change which multistep methods admit useful monotonicity statements. Hundsdorfer and Ruuth later developed general monotonicity and boundedness theory for implicit multistep methods. Lóczi's later exact step-size-coefficient work treats recurrence-sign methods for broad linear multistep families and explicitly notes Adams–Moulton among the classical families, while its exact tabulated results focus on BDF and Adams–Bashforth families.

The present claim is narrower and different: it classifies the exact all-step sign of one canonical positive scalar trajectory for third-order Adams–Moulton with a backward Euler starter. The disconnected set \((0,3/2]\cup\{6}\), especially the isolated cancellation at the stability boundary, is not implied by the general monotonicity coefficients or stability intervals inspected here.

## Limitations
No claim is made about arbitrary starting values, nonlinear equations, systems, variable steps, componentwise positivity for semidiscretized PDEs, or other Adams–Moulton orders. The isolated point \(z=6\) depends on the exact backward Euler starter; perturbing the starter generally reintroduces the \((-1)^n\) mode. The principal residual originality risk is older Adams–Moulton stability or positivity literature phrased directly in terms of starting polynomials rather than modern monotonicity terminology.

## References
1. W. Hundsdorfer, S. J. Ruuth, R. J. Spiteri, *Monotonicity-preserving linear multistep methods*, CWI Report MAS-R0210, April 30, 2002; journal version DOI:10.1137/S0036142902406326.
2. W. Hundsdorfer, S. J. Ruuth, *On monotonicity and boundedness properties of linear multistep methods*, CWI Report MAS-E0404, March 10, 2004; DOI:10.1090/S0025-5718-05-01794-1.
3. R. R. Brown, J. D. Riley, M. M. Bennett, *Stability properties of Adams-Moulton type methods*, Mathematics of Computation 19 (1965), 90–96, DOI:10.1090/S0025-5718-1965-0178572-1.
4. L. Lóczi, *Exact optimal values of step-size coefficients for boundedness of linear multistep methods*, arXiv:1609.07858.
