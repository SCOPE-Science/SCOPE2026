# A ratio-free CFL frontier and sharp equal-step optimum for periodic Adams–Bashforth two

## Finding

For standard variable-coefficient two-step Adams–Bashforth (AB2) applied to the scalar decay equation \(y'=-\lambda y\), where \(\lambda>0\), suppose the positive time steps alternate forever between \(h_1\) and \(h_2\). Write
\[
c=\lambda(h_1+h_2),\qquad r=h_2/h_1.
\]
The two-step transfer matrix is strictly Schur stable **if and only if** \(0<c<2\), regardless of the ratio \(r>0\). It is marginally stable at \(c=2\) (one Floquet multiplier equals \(1\)) and unstable for \(c>2\).

At each fixed \(0<c<2\), equal splitting \(h_1=h_2\) is the **unique** choice minimizing asymptotic spectral radius per two numerical steps. Defining \(a(c)=1-c+c^2/2\), the exact minimum and supremum over positive ratios are
\[
\rho_*(c)=\frac{\left(\sqrt{(1-3c/4)^2+c}+|1-3c/4|\right)^2}{4},
\qquad \sup_{r>0}\rho(c,r)=a(c).
\]
The supremum is approached as \(r\to0\) or \(r\to\infty\), never at a finite ratio, and the sharp overall penalty satisfies
\[
\sup_{0<c<2}\sup_{r>0}\frac{\rho(c,r)}{\rho_*(c)}=\frac53.
\]
Its limiting maximizer is \(c=4/3\) with extreme step imbalance. At \(c=4/3\) and equal steps, the two-step matrix is exactly \(I/3\).

## Assumptions and scope

Use the **interpolatory variable-coefficient AB2 method**, rather than an interpolated Nordsieck step-change implementation:
\[
y_{n+1}=y_n+h_n\left[\left(1+\frac{h_n}{2h_{n-1}}\right)f(y_n)
-\frac{h_n}{2h_{n-1}}f(y_{n-1})\right],\qquad f(y)=-\lambda y.
\]
The two lengths \(h_1,h_2\) are fixed positive constants repeated periodically. Stability means that the homogeneous two-step state-transfer matrix has spectral radius strictly below one; it is not a bound on the Euclidean norm of every individual step. For the scalar proof, starting values are arbitrary deterministic numbers and no stochastic assumptions are made.

## Proof

**Transfer matrix.** Write the two-component state as \(w_n=(y_n,y_{n-1})^{\mathsf T}\). For a current step of dimensionless size \(z>0\) following a step with size ratio \(q>0\), the transfer is
\[
B(q,z)=\begin{pmatrix}1-z(1+q/2)&zq/2\\1&0\end{pmatrix}.
\]
Put \(z=\lambda h_1=c/(1+r)\). The two consecutive transfers are \(B(1/r,z)\) and \(B(r,rz)\). Their product
\[
P=B(r,rz)B(1/r,z)
\]
has the **exact** trace and determinant
\[
\operatorname{tr}P=a+d,\qquad \det P=d,\qquad
a=1-c+\frac{c^2}{2},\qquad d=\frac{c^2r}{4(1+r)^2}.
\]
The nonzero eigenvalues of the reversed product coincide, so the stability result is independent of which step starts the cycle.

**Sharp CFL condition.** The characteristic polynomial is
\[
p(s)=s^2-(a+d)s+d.
\]
For \(0<c<2\), one has \(1/2\le a<1\), \(0<d\le c^2/16<1/4\), and \(p(1)=1-a=c(1-c/2)>0\). The discriminant \(\Delta=(a+d)^2-4d\) is decreasing in \(d\) throughout this range because \(\partial_d\Delta=2(a+d-2)<0\). Its minimum occurs for \(d=c^2/16\) (equal steps), where
\[
\Delta_{\min}=\frac{(3c-4)^2(9c^2-8c+16)}{256}\ge0.
\]
Consequently the roots are real, positive, and, since their sum is below \(2\) and \(p(1)>0\), both are below \(1\). The only repeated-root case is \(c=4/3\), \(r=1\), where the two-step matrix is \(I/3\). At \(c=2\), \(p(1)=0\), so a unit eigenvalue appears. When \(c>2\), \(p(1)<0\), forcing a real root strictly greater than \(1\). This proves the necessary-and-sufficient stability condition on the whole positive parameter domain.

**Unique optimal splitting.** At fixed \(c\in(0,2)\), the ratio enters the characteristic polynomial only through \(d\), and
\[
0<d\le c^2/16,
\]
with equality if and only if \(r=1\), whereas \(d\to0\) at both extreme ratios. Writing \(s_+(d)\) for the dominant positive root, implicit differentiation away from the sole double root gives
\[
\frac{ds_+}{dd}=\frac{s_+-1}{\sqrt{\Delta}}<0.
\]
Continuity includes the double-root endpoint. Hence the spectral radius decreases strictly as \(d\) grows: equal steps uniquely minimize it, while \(\lim_{d\downarrow0}s_+(d)=a\). At equal steps, the one-step matrix has eigenvalues
\[
\mu_\pm=\frac{1-3c/4\pm\sqrt{(1-3c/4)^2+c}}{2},
\]
so taking the spectral radius of its square gives the stated formula for \(\rho_*(c)\).

**Global sharp penalty.** Evaluate the equal-step characteristic polynomial at \(s=3a/5\):
\[
p_{\mathrm{eq}}(3a/5)=-\frac{(3c-4)^2(7c^2-6c+12)}{800}\le0.
\]
Since the two equal-step roots are nonnegative and real, this places \(3a/5\) between them. Therefore \(\rho_*(c)\ge3a/5\), with equality exactly at \(c=4/3\). For every ratio, \(\rho(c,r)<a\) and hence \(\rho(c,r)/\rho_*(c)<5/3\). At \(c=4/3\), \(a=5/9\) and \(\rho_*=1/3\), and taking an extreme ratio attains the **supremum** \(5/3\) in the limit. No maximizer with a finite positive unequal ratio is claimed.

**Extension to symmetric positive-definite matrices.** For \(y'=-Ay\), with real symmetric positive-definite \(A\), the two-step state transfer is a polynomial in \(A\) in each block. Orthogonally diagonalizing \(A\) splits the transfer into independent scalar modes with \(c_j=\lambda_j(h_1+h_2)\). All modes are strictly Schur stable exactly when \(\lambda_{\max}(A)(h_1+h_2)<2\). At fixed pair sum, equal steps strictly improve each scalar spectral radius, so they uniquely minimize the maximum over the finite spectrum. The universal ratio bound \(5/3\) passes to this maximum and is sharp in dimension one.

## Verification

The standalone `verify_ab2.py` checks the symbolic trace, determinant, Schur identity, nonnegative-discriminant factor, sharp-penalty polynomial factor, equal-step scalar identity and extreme-ratio phase matrix. It also performs exact rational recurrence comparisons and floating-point spectral spot checks across stable, boundary and unstable parameter values. Run `python verify_ab2.py` with the dependency in `requirements.txt`. Its successful output is recorded in `VERIFICATION.md`; numerical tests are supplementary to the proof.

## Relationship to prior work

Calvo, Montijano and Rández (2016) investigate step-change techniques and zero-stability for Adams methods, using different interpolation or Nordsieck constructions. López and Romay (2010) analyze finite sets of admissible step ratios and implementation costs. A November 2022 numerical-analysis lecture gives the exact variable-step AB2 formula used here. The present theorem instead analyzes the **negative-real-axis absolute stability** of a fixed two-periodic scalar AB2 recurrence and optimizes its Floquet radius at fixed combined step length. Ordinary constant-step AB2 is recovered at \(r=1\), but constant-step stability alone does not imply the ratio-free sharp periodic frontier or the global \(5/3\) spectral penalty.

## Limitations

The stability condition is specific to **strictly two-periodic** step lengths, the real negative scalar test spectrum, and the standard variable-coefficient formula. It does not establish stability for arbitrary step sequences, nonlinear systems, complex spectra, or nonsymmetric/non-normal matrices. A different starting phase has the same eigenvalues but may have a much larger two-step operator norm. In fact, for fixed \(c\in(0,2)\) the reverse-phase product obeys
\[
\lim_{r\to\infty}\frac{B(1/r,z)B(r,rz)}{r}
=\frac c2\begin{pmatrix}-1&1\\-1&1\end{pmatrix},
\]
so its Euclidean norm grows asymptotically like \(cr\). Strict spectral stability therefore must not be advertised as a ratio-uniform transient-error guarantee. Independent literature-priority review is outstanding; an inaccessible earlier full paper may contain a specialized equivalent derivation.

## References

- M. Calvo, J. I. Montijano and L. Rández, *A new stepsize change technique for Adams methods*, Applied Mathematics and Nonlinear Sciences 1 (2016), 547–558, DOI: `10.21042/AMNS.2016.2.00043`. Available online November 18, 2016.
- D. J. López and J. G. Romay, *Implementing Adams Methods with Preassigned Stepsize Ratios*, Mathematical Problems in Engineering (2010), article 765620, DOI: `10.1155/2010/765620`.
- J. Verschelde, *Variable Step Methods*, Numerical Analysis course notes, November 4, 2022, section on variable-step two-step Adams–Bashforth, https://homepages.math.uic.edu/~jan/mcs471/variablestep.pdf.
- M. Calvo, F. Lisbona and J. Montijano, *On the Stability of Interpolatory Variable-Stepsize Adams Methods in Nordsieck Form*, SIAM Journal on Numerical Analysis 26 (1989), 946–962, DOI: `10.1137/0726052` (abstract inspected; complete article not accessible).
