# Two sharp spectral crossings in a two-recovered-class epidemic model

## Finding

Consider the autonomous, two-recovered-class epidemic model described by Gai, Kolokolnikov, Schrader and Sharma in their Equation (6.4), with the numerical parameters of Figure 8(a). Normalize total population to one, set
\[
\beta_s=\beta_1=1,\qquad \beta_2=0,\qquad \mu_1=\mu_2=m=\frac1{100},
\]
and treat the recovery rate \(\gamma\) as a variable in \(0<\gamma<1\).

There is exactly one positive endemic equilibrium at every such recovery rate. Its infection coordinate \(x\) uniquely solves
\[
x^2+\left(2\gamma-\frac{99}{100}\right)x+\frac{\gamma-1}{100}=0,
\]
and its other coordinates are
\[
S=\frac{\gamma m}{x+m},\qquad
R_1=R_2=\frac{\gamma x}{x+m}.
\]
Define
\[
G(x)=\frac{(1-x)(x+1/100)}{2x+1/100},
\qquad
Q(x)=200000000x^4+8000000x^3+110000x^2-4450x+1.
\]
The quartic has exactly two positive roots, denoted
\[
x_a=0.000226002552181\ldots,
\qquad
x_b=0.015527501843979\ldots.
\]
Set
\[
\gamma_-:=G(x_b)=0.612133022884022\ldots,
\qquad
\gamma_+:=G(x_a)=0.978155994703693\ldots.
\]
The endemic equilibrium is **linearly asymptotically stable relative to the population simplex** precisely for
\[
0<\gamma<\gamma_-
\qquad\text{or}\qquad
\gamma_+<\gamma<1.
\]
For \(\gamma_-<\gamma<\gamma_+\), it has exactly two eigenvalues with positive real parts and one with negative real part. At each endpoint \(\gamma_\pm\), it has one simple conjugate pair on the imaginary axis and a strictly negative third eigenvalue. Both crossings are transverse, destabilizing at \(\gamma_-\) and stabilizing at \(\gamma_+\) as recovery increases.

Thus the same unforced two-recovered-class model exhibits **a bounded interval of endemic spectral instability bracketed by two stable recovery-rate intervals**. In particular, the study's plotted value \(\gamma=0.7\) lies in the unstable interval.

## Assumptions and scope

The population fractions \(S,I,R_1,R_2\) are nonnegative and obey
\[
S+I+R_1+R_2=1.
\]
All other parameters are fixed to the exact Figure 8(a) values displayed above. On the full four-dimensional unconstrained space, conservation of total population creates a zero eigenvalue at every equilibrium; throughout this result, stability and eigenvalue counts refer to the invariant three-dimensional simplex of total population one.

The claimed thresholds concern the linearization at the unique endemic equilibrium. They are not claims of nonlinear Hopf nondegeneracy, existence or stability of periodic orbits, chaos, or global convergence. The source's plotted sustained oscillations are contextual numerical observations, not assumptions in the proof.

## Proof

**1. Reduction and equilibrium.** With the stated parameters, the original equations reduce on the invariant simplex to
\[
\begin{aligned}
\dot I&=I(1-I-R_2-\gamma),\\
\dot R_1&=\gamma I-I R_1-mR_1,\\
\dot R_2&=m(R_1-R_2),
\end{aligned}
\qquad m=\frac1{100},
\]
with \(S=1-I-R_1-R_2\). At a positive endemic equilibrium, put \(I=x>0\). Then
\[
R_1=R_2=\frac{\gamma x}{x+m},
\qquad
S=\frac{\gamma m}{x+m}.
\]
Population conservation yields
\[
(1-x)(x+m)=\gamma(m+2x).
\]
Therefore
\[
x^2+(m+2\gamma-1)x+m(\gamma-1)=0.
\]
Since \(0<\gamma<1\), this quadratic has negative constant term; it has exactly one positive root. Moreover, the resulting \(S,R_1,R_2\) are strictly positive and sum with \(x\) to one. Conversely, every positive endemic equilibrium must have these coordinates, proving uniqueness. Equivalently,
\[
\gamma=G(x)=\frac{(1-x)(x+m)}{m+2x}.
\]
For \(m=1/100\), direct differentiation gives
\[
G'(x)=-\frac{20000x^2+200x+101}{(200x+1)^2}<0.
\]
The function maps \((0,99/100)\) bijectively onto \((0,1)\), with reverse orientation.

**2. Characteristic polynomial.** In coordinates \((I,R_1,R_2)\), the endemic Jacobian is
\[
J=\begin{pmatrix}
-x&0&-x\\
\gamma-\frac{\gamma x}{x+m}&-(x+m)&0\\
0&m&-m
\end{pmatrix}.
\]
Its characteristic polynomial is
\[
\det(\lambda\operatorname{Id}-J)
=\lambda^3+A\lambda^2+B\lambda+C,
\]
where
\[
\begin{aligned}
A&=2(x+m),\\
B&=x^2+3mx+m^2,\\
C&=xm(x+m)+\frac{x\gamma m^2}{x+m}.
\end{aligned}
\]
All three coefficients are positive. Substituting \(m=1/100\) and \(\gamma=G(x)\) into the cubic Routh-Hurwitz determinant gives the exact identity
\[
\boxed{AB-C=\frac{Q(x)}{500000(200x+1)}.}
\]
For a real cubic with \(A,B,C>0\), all roots lie in the open left half-plane exactly when \(AB>C\). When \(AB<C\), the Routh first-column signs are \(+,+,-,+\), so there are precisely two roots in the open right half-plane; there is no positive real root because all coefficients are positive.

**3. Exact root count of the threshold quartic.** The coefficient sequence of \(Q\), in descending powers, is \(+,+,+,-,+\). Descartes' rule of signs therefore allows at most two positive roots, counted with multiplicity. The exact inequalities
\[
Q\left(\frac1{5000}\right)>0,
\qquad
Q\left(\frac1{4000}\right)<0,
\]
and
\[
Q\left(\frac1{100}\right)<0,
\qquad
Q\left(\frac1{50}\right)>0
\]
produce two distinct positive roots in disjoint intervals. Hence there are exactly two positive roots, both simple. They lie within \((0,99/100)\). The quartic is positive below \(x_a\), negative between \(x_a\) and \(x_b\), and positive above \(x_b\), since \(Q(0)=1>0\) and no other positive roots exist.

**4. Stability and crossings.** Because \(G\) is decreasing, \(x>x_b\) corresponds to \(\gamma<\gamma_-\), \(x_a<x<x_b\) corresponds to \(\gamma_-<\gamma<\gamma_+\), and \(x<x_a\) corresponds to \(\gamma>\gamma_+\). The sign of \(AB-C\) gives the stated complete stability classification.

At either threshold \(C=AB\), so the characteristic polynomial factors exactly as
\[
(\lambda+A)(\lambda^2+B).
\]
Its eigenvalues are \(-A\) and \(\pm i\sqrt B\), simple because \(A,B>0\). Both roots of \(Q\) are simple and \(G'(x)\neq0\), so
\[
\frac{d}{d\gamma}(AB-C)\ne0
\]
at either threshold. Implicit differentiation of the cubic at \(\lambda=i\sqrt B\) gives
\[
\frac{d}{d\gamma}\operatorname{Re}\lambda
=-\frac{(AB-C)'_{\gamma}}{2(A^2+B)}.
\]
At \(\gamma_-\), the Routh determinant decreases through zero, so the pair crosses left-to-right. At \(\gamma_+\), it increases through zero, so the crossing is right-to-left. Both crossings are transverse, completing the spectral classification.

## Verification

The accompanying standalone `verify.py` reconstructs the exact equilibrium identity, Jacobian, characteristic coefficients and Routh-Hurwitz quartic using rational symbolic arithmetic. It verifies the rational isolating intervals and the two positive-root count, computes \(\gamma_-\) and \(\gamma_+\), and checks representative Jacobian eigenvalues on both sides of the instability interval. Running it prints `VERIFY_OK`.

Numerical approximations do not establish the completeness of the classification: the exact sign comparisons, Descartes bound and cubic Routh criterion provide that proof.

## Relationship to prior work

Gai, Kolokolnikov, Schrader and Sharma introduce the multi-recovered-class model in §6.3 of their paper. They display numerical recurrent outbreaks at \(n=2\), \((\beta_s,\beta_1,\beta_2)=(1,1,0)\), \(\mu_1=\mu_2=0.01\), \(\gamma=0.7\), and explicitly leave fuller analysis of this family to future work. Their paper derives analytic threshold results for **seasonally forced** dynamics elsewhere, not an all-recovery-rate endemic stability diagram for this **autonomous two-recovered-class** example. The author's accessible preprint contains the same numerical example without this exact spectral classification.

Related literature studies epidemic oscillations with immune-stage or immunity-delay structure. Otto, MacPherson and Colijn analyze an immunity-waning model and note oscillations for many recovered classes, but their resident strain cannot reinfect recovered classes in the relevant model, and they do not provide the exact two-threshold polynomial for the Gai model. Barbarossa, Polner and Röst obtain stability switches in an SIRS model with immune boosting and delays; that is a different model, and its general phenomenon is not claimed as new. Hethcote, Stech and van den Driessche analyze general delay-induced epidemic oscillations. The contribution here is the **exact, exhaustive stability and unstable-dimension partition** for the specific observed two-recovered-class example.

## Limitations

This is a three-dimensional linear spectral theorem on the unit-population simplex. It does not prove emergence, uniqueness, amplitude or stability of nonlinear periodic orbits at the spectral thresholds and does not prove chaos. Extrapolation to other immunity-transition rates or other recovered-class susceptibilities requires separate analysis.

A differently formulated equivalent spectral threshold could exist in literature not recovered by the targeted searches; broad epidemic delay/bifurcation sources are related but not model-specific confirmations of novelty.

## References

1. C. Gai, T. Kolokolnikov, J. Schrader and V. Sharma, “Recurrent and chaotic outbreaks in SIR model,” European Journal of Applied Mathematics 35 (2024), 662–674. DOI: 10.1017/S0956792523000360; first published online 18 January 2024.
2. C. Gai et al., “Recurrent and chaotic outbreaks in SIR model,” author-hosted public preprint, https://www.mathstat.dal.ca/~tkolokol/papers/sir-chaos.pdf.
3. S. P. Otto, A. MacPherson and C. Colijn, “Endemic does not mean constant as SARS-CoV-2 continues to evolve,” Evolution 78 (2024), 1092–1108. DOI: 10.1093/evolut/qpae041.
4. M. V. Barbarossa, M. Polner and G. Röst, “Stability switches induced by immune system boosting in an SIRS model with discrete and distributed delays,” arXiv:1606.03962 (2016).
5. H. W. Hethcote, H. W. Stech and P. van den Driessche, “Nonlinear Oscillations in Epidemic Models,” SIAM Journal on Applied Mathematics 40 (1981), 1–9. DOI: 10.1137/0140001.
