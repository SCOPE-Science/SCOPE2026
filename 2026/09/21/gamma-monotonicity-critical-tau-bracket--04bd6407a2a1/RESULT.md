# A rigorous near-sharp bracket for the Gamma monotonicity parameter

For \(\tau>0\), define
\[
D_\tau(x)=\log\frac{x^2+\tau}{x+\tau}
\]
and
\[
u_\tau(x)=
\begin{cases}
\dfrac{\log\Gamma(x)}{D_\tau(x)},&x\ne1,\\[1ex]
-(1+\tau)\gamma,&x=1.
\end{cases}
\]
Kupán, Márton and Szász (2017) proved that \(u_\tau\) is strictly increasing on \((0,\infty)\) for every \(0<\tau\le25\).  They also gave a counterexample at \(\tau=1000\) and reported numerical evidence for a transition parameter in \((212,213)\).

## Theorem

Every \(u_\tau\) with
\[
0<\tau\le 212.435
\]
is strictly increasing on \((0,\infty)\).

Let \(\tau_9\) be the unique positive solution of
\[
\left(\frac{761}{280}-\gamma\right)
\log\frac{\tau+81}{\tau+9}
=
\log(40320)
\left(\frac{18}{\tau+81}-\frac1{\tau+9}\right).
\]
Then
\[
212.508612771<\tau_9<212.508612772,
\]
and \(u_\tau\) is not increasing on \((0,\infty)\) for every \(\tau>\tau_9\).

Consequently, if
\[
\tau_c=\sup\{\tau>0:u_\tau\text{ is strictly increasing on }(0,\infty)\},
\]
then
\[
\boxed{212.435\le \tau_c\le \tau_9<212.508612772.}
\]
Thus the previously rigorous sufficient range \(\tau\le25\) is extended to \(\tau\le212.435\), while the earlier numerical indication \(\tau_c\in(212,213)\) is narrowed to an interval of width less than \(0.074\).

## Proof

Write
\[
N(x)=\log\Gamma(x),\qquad
A_\tau(x)=\psi(x)D_\tau(x)-N(x)D_\tau'(x).
\]
Away from \(x=1\), the sign of \(u_\tau'(x)\) is the sign of \(A_\tau(x)\), because the denominator is \(D_\tau(x)^2\).

### 1. The range below \(2.23\)

Kupán, Márton and Szász prove, for every \(\tau>1\), monotonicity from the origin through the point \(x_3=2.2324\ldots\) determined by \(\psi(x_3)=\psi'(x_3)\): their Lemmas 2--4, combined with the monotone l'Hospital rule, give strict increase on the subintervals separated by \(x=1\). Their Theorem 1 already covers \(0<\tau\le25\). Hence for the new parameter range it remains only to treat \(x\ge2.23\).

### 2. A Binet/Stirling lower certificate

Binet's second formula gives, for \(x>0\),
\[
N(x)=\left(x-\frac12\right)\log x-x+\frac12\log(2\pi)
+2\int_0^\infty\frac{\arctan(t/x)}{e^{2\pi t}-1}\,dt.
\]
Since \(\arctan y<y\) for \(y>0\) and
\[
\int_0^\infty\frac{t}{e^{2\pi t}-1}\,dt=\frac1{24},
\]
we have the strict upper bound
\[
N(x)<S(x):=
\left(x-\frac12\right)\log x-x+\frac12\log(2\pi)+\frac1{12x}.
\]
Differentiating Binet's formula gives
\[
\psi(x)=\log x-\frac1{2x}
-2\int_0^\infty\frac{t}{(t^2+x^2)(e^{2\pi t}-1)}\,dt,
\]
so
\[
\psi(x)>\log x-\frac1{2x}-\frac1{12x^2}=S'(x).
\]
For \(x\ge2.23\), \(D_\tau(x)>0\) and \(D_\tau'(x)>0\). Therefore
\[
A_\tau(x)>P_\tau(x):=S'(x)D_\tau(x)-S(x)D_\tau'(x).
\]

Set \(T=212.435\). Directed interval arithmetic at 70 decimal digits certifies
\[
P_T(x)>0\qquad(2.23\le x\le15).
\]
The certificate partitions the interval into subintervals of width \(10^{-3}\) and uses the centered mean-value enclosure
\[
P_T(I)\subset P_T(c)+P_T'(I)(I-c),
\]
where \(c\) is the midpoint. The smallest certified lower endpoint occurs on \([8.890,8.891]\) and is greater than \(2.29\times10^{-7}\). The standalone verifier is included in `artifacts/verify_tau_bracket.py`.

For the tail, observe that
\[
P_T'(x)=S''(x)D_T(x)-S(x)D_T''(x).
\]
The numerator of \(D_T''\), after multiplication by the positive denominator \((x^2+T)^2(x+T)^2\), is
\[
K_T(x)=2T^3-2T^2x^2+4T^2x+T^2-4Tx^3+4Tx^2-x^4.
\]
At \(T=212.435\), interval evaluation gives
\[
K_T(15)<-1.1085\times10^6,
\qquad
K_T'(15)<-3.0887\times10^6.
\]
Moreover
\[
K_T''(x)=-12x^2-24Tx+8T-4T^2<0\qquad(x>0).
\]
Thus \(K_T<0\), hence \(D_T''<0\), for all \(x\ge15\). Also \(S,S'',D_T>0\) there, so \(P_T'(x)>0\). Since \(P_T(15)>0\), it follows that \(P_T>0\) on \([15,\infty)\). We have therefore proved \(u_T'(x)>0\) for all \(x\ge2.23\), and hence on all of \((0,\infty)\).

Kupán, Márton and Szász's Theorem 2 states that, for \(\alpha>\beta>0\),
\[
g_{\alpha,\beta}(x)=\frac{D_\alpha(x)}{D_\beta(x)}
\]
is strictly increasing. On \(x>1\), this is equivalent to
\[
\frac{D_\alpha'(x)}{D_\alpha(x)}>
\frac{D_\beta'(x)}{D_\beta(x)}.
\]
Since the monotonicity criterion for \(u_\tau\) on \(x\ge2.23\) is
\[
\frac{\psi(x)}{N(x)}>\frac{D_\tau'(x)}{D_\tau(x)},
\]
the result for \(T\) propagates to every smaller \(\tau\). Together with the already established small-\(x\) part, this proves strict increase for all \(0<\tau\le212.435\).

### 3. A sharp explicit obstruction at \(x=9\)

At \(x=9\),
\[
\psi(9)=H_8-\gamma=\frac{761}{280}-\gamma,
\qquad
N(9)=\log(40320).
\]
Hence \(A_\tau(9)=0\) is exactly the displayed equation defining \(\tau_9\). The same parameter monotonicity from Theorem 2 shows that \(D_\tau'(9)/D_\tau(9)\) is strictly increasing in \(\tau\), so this zero is unique. Directed interval evaluation gives opposite signs at \(212.508612771\) and \(212.508612772\), proving the numerical bracket.

For every \(\tau>\tau_9\),
\[
A_\tau(9)<0,
\]
so \(u_\tau'(9)<0\); such \(u_\tau\) cannot be increasing. This completes the bracket for \(\tau_c\).

## Relation to prior work

Zhao, Guo and Qi (2012) conjectured monotonicity of \(u_\tau\) for all \(\tau>0\). Kupán, Márton and Szász (2017) refuted that unrestricted conjecture with \(\tau=1000\), proved monotonicity for \(0<\tau\le25\), and reported numerical evidence for a critical value in \((212,213)\). The theorem above turns that numerical location into a rigorous narrow bracket and raises the proven sufficient endpoint by more than a factor of eight.

Searches by the exact quotient, the 2017 paper title and DOI, the numerical interval \((212,213)\), the phrase “critical parameter”, and synonymous Gamma-function monotonicity formulations did not locate a later proof extending the rigorous endpoint beyond 25 or a published narrow bracket for the critical parameter, to the best of our knowledge.

## Limitations

- The exact value of \(\tau_c\) is not determined; the interval between the certified lower bound and the \(x=9\) obstruction remains open.
- At \(\tau=\tau_9\), the derivative vanishes at \(x=9\), which alone does not rule out strict monotonicity; no endpoint claim is made there.
- The lower bound uses a computer-assisted interval certificate for one explicit elementary inequality. It is not a formal proof assistant verification.
- The originality search may miss later work using substantially different notation for the same quotient.


## Reproducibility

Run `python artifacts/verify_tau_bracket.py` with Python 3 and mpmath 1.3.0. The script verifies the finite-interval lower certificate, the tail-polynomial endpoint signs, and the numerical bracket for \(\tau_9\).

## References

1. J.-L. Zhao, B.-N. Guo, F. Qi, *A refinement of a double inequality for the gamma function*, Publicationes Mathematicae Debrecen 80 (2012), 333--342. DOI: https://doi.org/10.5486/PMD.2012.5010 ; arXiv: https://arxiv.org/abs/1001.1495
2. P. A. Kupán, Gy. Márton, R. Szász, *A result regarding monotonicity of the Gamma function*, Acta Universitatis Sapientiae, Mathematica 9 (2017), 291--302. DOI: https://doi.org/10.1515/ausm-2017-0022 ; open PDF: https://www.kurims.kyoto-u.ac.jp/EMIS/journals/AUSM/C9-2/math92-03.pdf
3. NIST Digital Library of Mathematical Functions, §5.9, Binet's formula for \(\log\Gamma\). https://dlmf.nist.gov/5.9
