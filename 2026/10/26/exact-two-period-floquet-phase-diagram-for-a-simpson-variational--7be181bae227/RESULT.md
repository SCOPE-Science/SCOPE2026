# Exact two-period Floquet phase diagram for a Simpson variational integrator

## Finding

The fourth-order harmonic-oscillator Simpson variational map of Dubois and Rojas-Quintero is symplectic and individually stable at every dimensionless step \(0<s<\sqrt 8\). Nevertheless, alternating two individually stable steps can be exponentially unstable. The entire strict stability region has the following polynomial description, including its neutral boundary, a protected reciprocal-step curve, and a sharp resonance growth law.

For \(s,t\in(0,\sqrt8)\), define
\[
F(s,t)=s^2t^2-8s^2+st^3-24st-12t^2+96,
\qquad \Delta(s,t)=F(s,t)F(t,s).
\]
For the alternating-step two-update map \(P(s,t)\) defined below:

* If \(\Delta(s,t)>0\), every trajectory of the repeated two-update map is bounded.
* If \(\Delta(s,t)<0\), its two real Floquet multipliers have reciprocal moduli, with one strictly larger than one, so generic nonzero trajectories grow exponentially.
* If \(\Delta(s,t)=0\), the multiplier \(-1\) is repeated. Except at \(s=t=s_0\), where \(P=-I\), the map has a nontrivial Jordan block, so some trajectories grow linearly. Here \(s_0=\sqrt{11-\sqrt{73}}\).

The entire reciprocal-step curve \(st=4\) within the allowed square is strictly stable. At the resonant point \(s_0\), arbitrarily small alternating modulation is unstable: for \(s=s_0+\delta\), \(t=s_0-\delta\), and sufficiently small nonzero \(\delta\),
\[
\log\rho(P(s,t))=\gamma|\delta|+O(|\delta|^3),\qquad
\gamma=\frac{s_0(4-s_0^2)}{s_0^2+24}>0,
\]
where \(\rho\) denotes spectral radius. Thus there is a first-order-in-modulation exponential growth rate despite exact fixed-step energy conservation.

## Assumptions and scope

Take a harmonic oscillator with \(m>0\), \(\omega>0\), canonical coordinate \(q\) and momentum \(p\). For a step \(h>0\), write \(s=\omega h\) and scale the state as \(y=(p/(m\omega),q)^\mathsf T\). The one-step *canonical map* is exactly equation (26) of Dubois and Rojas-Quintero, in the scaled form
\[
M(s)=\frac1{s^2+24}
\begin{pmatrix}
(s^4-22s^2+48)/2&-s(12-s^2)(24-s^2)/12\\
3s(8-s^2)&(s^4-22s^2+48)/2
\end{pmatrix}.
\]
The two-step map is \(P(s,t)=M(t)M(s)\). The sequence uses steps \(s/\omega,t/\omega,s/\omega,t/\omega,\ldots\), and the canonical momentum is passed from one step to the next without resetting. Both steps are restricted to \(0<s,t<\sqrt8\), the source's strict individual-stability interval. These are exact linear updates, not rounded implementations or an arbitrary choice of a variable-step multistep restart.

## Proof

Put \(A(z)=z^4-22z^2+48\), \(B(z)=z(12-z^2)(24-z^2)\), \(C(z)=z(8-z^2)\), and \(D(z)=z^2+24\). Direct polynomial expansion establishes
\[
A(z)^2+B(z)C(z)=4D(z)^2,
\]
so \(\det M(z)=1\) for all real \(z\). Write \(T=\operatorname{tr}P(s,t)\). Another exact expansion gives
\[
T+2=\frac{F(s,t)F(t,s)}{4(s^2+24)(t^2+24)}
\]
and
\[
T-2=\frac{(s+t)^2(st-12)
\left(s^2t^2-8(s+t)^2+192\right)}
{4(s^2+24)(t^2+24)}.
\]
The polynomial \(Q(s,t)=s^2t^2-8(s+t)^2+192\) decreases strictly in each positive argument on \((0,\sqrt8)^2\): \(\partial_sQ=2st^2-16(s+t)<-16t<0\), and similarly for \(t\). Since \(Q(\sqrt8,\sqrt8)=0\), one has \(Q>0\) throughout the open square. Also \(st<8<12\); hence \(T<2\) throughout.

Every real \(2\times2\) matrix of determinant one has characteristic polynomial \(z^2-Tz+1\). Therefore \(-2<T<2\) gives two distinct unit-modulus conjugate eigenvalues and bounded powers, while \(T<-2\) gives distinct real reciprocal multipliers, one outside the unit disk. Together with the factored identity for \(T+2\), these yield both strict cases of the theorem.

On \(\Delta=0\), one has \(T=-2\), so \((P+I)^2=0\). If \(P\ne-I\), its powers contain a nonzero term linear in the number of two-step periods. If \(P=-I\), then \(M(t)=-M(s)^{-1}\). Comparing the off-diagonal entries implies that the ratios of their positive off-diagonal magnitudes coincide. That ratio equals
\[
R(z)=\frac{(12-z^2)(24-z^2)}{36(8-z^2)},\qquad
R'(z)=\frac{z^3(16-z^2)}{18(8-z^2)^2}>0
\quad(0<z<\sqrt8).
\]
Thus \(s=t\), and the diagonal entry condition gives \(A(s)=0\). Of the two positive roots \(\sqrt{11\pm\sqrt{73}}\), only \(s_0=\sqrt{11-\sqrt{73}}\) is in \((0,\sqrt8)\). Conversely, \(M(s_0)^2=-I\). This proves the exact neutral-boundary classification.

The identity
\[
F(s,t)-F(t,s)=-(s-t)(s+t)(st-4)
\]
shows that when \(st=4\), both factors equal \(-8(s^4-2s^2+16)/s^2<0\). The strict Floquet region follows because \(s^4-2s^2+16=(s^2-1)^2+15>0\).

Finally set \(s=s_0+\delta\), \(t=s_0-\delta\). Since \(F(s_0,s_0)=2A(s_0)=0\), symmetry and the last identity imply
\[
F(s,t)=2s_0(4-s_0^2)\delta+O(\delta^2),\quad
F(t,s)=-2s_0(4-s_0^2)\delta+O(\delta^2).
\]
Their product is even in \(\delta\), so the odd remainder vanishes, and the trace factorization yields
\[
T=-2-\left(\frac{s_0(4-s_0^2)}{s_0^2+24}\right)^2\delta^2+O(\delta^4).
\]
For a determinant-one hyperbolic matrix with \(T<-2\), \(\log\rho(P)=\operatorname{arcosh}(-T/2)\). The displayed trace expansion proves the asserted first-order resonance law.

## Verification

The standalone standard-library file `verify.py` verifies, using exact rational bivariate polynomial arithmetic, the determinant identity, both factorizations of \(T\pm2\), and the antisymmetric factorization of \(F\). It also checks the exact rational unstable witness \((s,t)=(5/3,22/15)\) and strictly stable reciprocal pair \((3/2,8/3)\). Run with `python verify.py` from the directory containing the file. The expected output is `VERIFY_OK: four exact polynomial identities and two rational witnesses`. The analytic positivity, monotonicity, Jordan classification, and asymptotic steps remain established in the proof above, not by finitely many tests.

## Relationship to prior work

Dubois and Rojas-Quintero introduce the Simpson variational harmonic oscillator map and prove symplecticity, strict fixed-step stability, and conservation of a step-dependent modified quadratic energy. This finding uses their *unchanged* map but answers the distinct two-period step-switching Floquet question, which is not a consequence of fixed-step energy conservation. Their later work on general quadratic Lagrangians develops an implicit Simpson variational scheme and illustrates multiple oscillatory modes. Skeel's classical work proves that variable step sizes can destabilize the Störmer/leapfrog/Verlet method; that establishes an important precedent for the phenomenon, but not this Simpson-map polynomial phase diagram, its neutral boundary, its reciprocal-step stable curve, or its first-order resonance constant.

## Limitations

This is a theorem for the specified one-degree-of-freedom linear oscillator and *canonical composition* of the displayed Simpson maps. It is not a claim about arbitrary adaptive variational implementations, all symplectic methods, nonlinear dynamics, arbitrary step sequences, finite-precision behavior, or accuracy at large physical time. Individual fixed-step stability does not imply switched stability. At an unstable parameter pair, initial vectors in the contracting eigenspace decay, rather than grow. Literature searches do not establish absolute novelty; a related 2024 full text and the complete 1993 Skeel paper were not accessible during this comparison.

## References

1. F. Dubois and J. A. Rojas-Quintero, *A Variational Symplectic Scheme Based on Simpson's Quadrature*, Geometric Science of Information (2023), pp. 22–31, DOI: 10.1007/978-3-031-38299-4_3; full author manuscript arXiv:2406.16423, especially equations (22), (26), and (28). The proceedings ebook was released 2023-07-31.
2. J. A. Rojas-Quintero, F. Dubois, J. G. Cabrera-Díaz, *Simpson's Variational Integrator for Systems with Quadratic Lagrangians*, Axioms 13 (2024), 255, DOI: 10.3390/axioms13040255.
3. R. D. Skeel, *Variable step size destabilizes the Störmer/leapfrog/Verlet method*, BIT 33 (1993), 172–175, DOI: 10.1007/BF01990352.
