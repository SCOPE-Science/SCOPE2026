# Even phase moments recover the normalized geometry of a three-frequency spectrum
## Finding
Let \(n_0<n_1<n_2\) be integers and
\[
P(x)=c_0e^{2\pi i n_0x}+c_1e^{2\pi i n_1x}+c_2e^{2\pi i n_2x},\qquad |c_0|=|c_1|=|c_2|=1.
\]
Write \(g=\gcd(n_1-n_0,n_2-n_0)\), \(A=(n_1-n_0)/g\), and \(B=(n_2-n_0)/g\). Thus \(0<A<B\) and \(\gcd(A,B)=1\). With normalized Lebesgue measure on \(\mathbb T\), define
\[
D_r=\sum_{u_0+u_1+u_2=r}\binom{r}{u_0,u_1,u_2}^2,
\qquad z=\frac{c_1^B}{c_0^{B-A}c_2^A}.
\]
For \(1\le t\le\lfloor r/B\rfloor\), put
\[
C_{r,A,B}(t)=\sum_{u_0+u_1+u_2=r-tB}
\binom{r}{u_0,u_1+tB,u_2}
\binom{r}{u_0+t(B-A),u_1,u_2+tA}.
\]
Then for every integer \(r\ge1\),
\[
\boxed{\ \|P\|_{2r}^{2r}=D_r+2\sum_{t=1}^{\lfloor r/B\rfloor}C_{r,A,B}(t)\operatorname{Re}(z^t)\ }.
\]
In particular, the coefficient phases are invisible to all even moments of orders below \(2B\), while order \(2B\) is phase-sensitive and obeys
\[
\boxed{\ \|P\|_{2B}^{2B}=D_B+2\binom{B}{A}\operatorname{Re}(z)\ }.
\]
Hence the exact first-response range is
\[
\left[D_B-2\binom{B}{A},\ D_B+2\binom{B}{A}\right].
\]
The first phase-sensitive even order determines \(B\), and the range width \(4\binom{B}{A}\) determines \(A\) up to the reflection \(A\leftrightarrow B-A\). Thus these phase-response data recover the normalized three-point spectrum \(\{0,A,B}\) up to reflection.

## Assumptions and scope
The frequencies are distinct integers and the three Fourier coefficients are unimodular. Translation of the frequency set, multiplication of all frequencies by their common gap \(g\), and a common coefficient phase do not affect the normalized statement. The theorem concerns normalized Lebesgue \(L^{2r}(\mathbb T)\) moments. It does not assert a closed formula for the minimum of the higher-harmonic cosine polynomial when \(r\ge2B\); instead it gives that polynomial exactly.

## Proof
Expand \(P^r\). A term indexed by \(m=(m_0,m_1,m_2)\) with \(m_0+m_1+m_2=r\) has multinomial coefficient \(\binom{r}{m_0,m_1,m_2}\), coefficient factor \(c_0^{m_0}c_1^{m_1}c_2^{m_2}\), and frequency
\[
r n_0+g(Am_1+Bm_2).
\]
By Parseval,
\[
\|P\|_{2r}^{2r}=\|P^r\|_2^2,
\]
so two count vectors \(m,m'\) interact exactly when
\[
A(m_1-m'_1)+B(m_2-m'_2)=0.
\]
Set \(d=m-m'\). Since \(d_0+d_1+d_2=0\) and \(\gcd(A,B)=1\), every collision difference has the unique form
\[
d=t\,(-(B-A),B,-A),\qquad t\in\mathbb Z.
\]
For \(t>0\), the positive mass of this difference is \(tB\), as is its negative mass. Because both count vectors have total mass \(r\), necessarily \(tB\le r\). Conversely every \(1\le t\le\lfloor r/B\rfloor\) occurs: write
\[
m=(u_0,u_1+tB,u_2),\qquad
m'=(u_0+t(B-A),u_1,u_2+tA),
\]
where \(u_0+u_1+u_2=r-tB\). Summing the products of the two multinomial coefficients over these residual triples gives exactly \(C_{r,A,B}(t)\).

The diagonal \(t=0\) contributes \(D_r\). For positive \(t\), the coefficient phase factor is
\[
c_0^{-t(B-A)}c_1^{tB}c_2^{-tA}=z^t,
\]
and the negative collision contributes its conjugate. This proves the displayed moment formula.

If \(r<B\), there is no nonzero collision, so the moment is phase-independent. At \(r=B\), only \(t=1\) is possible and the residual triple is \((0,0,0)\). The two colliding multiplicity vectors are \((0,B,0)\) and \((B-A,0,A)\), so
\[
C_{B,A,B}(1)=\binom{B}{A}.
\]
Because \(z\) can be any point of the unit circle, the stated range follows. For every \(r\ge B\), \(C_{r,A,B}(1)>0\), so the moment function is genuinely nonconstant in phase. Finally, for fixed \(B\), \(\binom{B}{A}\) is strictly increasing for \(1\le A\le\lfloor B/2\rfloor\); therefore the first-response width identifies \(A\) up to \(A\leftrightarrow B-A\).

## Verification
The accompanying `verify_resonance.py` independently enumerates all multinomial collision pairs for \(1\le r\le10\) and all coprime \(0<A<B\le25\). It checks, with exact integer arithmetic, that the only collision differences are the predicted multiples of \((-(B-A),B,-A)\), that every coefficient equals the stated residual-triple sum, and that the first resonant coefficient is \(\binom{B}{A}\). Its expected terminal line is `VERIFY_OK cases=... r_max=10 B_max=25 exact_integer_collision_check`. This finite replay corroborates the symbolic proof; it is not used to infer the all-\(r\), all-spectrum statement.

## Relationship to prior work
Neuwirth studied arbitrary trigonometric trinomials in the maximum-modulus norm and described phase dependence for \(L^\infty\), exposed points, multiplier norms, and Sidon constants; that does not determine finite even moments. Krenedits studied the Hardy--Littlewood majorant problem for the special trinomials \(1+e(x)\pm e((k+2)x)\) at non-even exponents, while recording Parseval equalities at even endpoints in the low cases. The 2026 resolution of Mockenhaupt's three-term conjecture explicitly observes, for the special support \(\{0,1,N}\), that no collision occurs in the \(m\)-th power for \(m<N\) and that the first collision occurs at \(m=N\). That special collision-threshold observation is therefore prior work and is not claimed here. The finding above supplies the exact all-even-moment resonance polynomial for every coprime normalized three-point support \(\{0,A,B}\), its first-resonance coefficient \(\binom{B}{A}\), and the resulting inverse recovery of the normalized support up to reflection.

## Limitations
The proof is elementary once the collision lattice is isolated, and the originality claim is correspondingly narrow: it concerns the explicit arbitrary-gap all-even-moment formula and inverse phase-response consequence, not the general Parseval mechanism, the even-exponent majorant inequality, or the previously published \(\{0,1,N}\) first-collision observation. Older trinomial literature may contain equivalent formulas under different terminology; targeted searches and the inspected full texts did not locate one. No claim is made for non-unimodular coefficient magnitudes or for optimization of the higher-harmonic phase polynomial beyond the first resonant moment.

## References
1. Stefan Neuwirth, *The maximum modulus of a trigonometric trinomial*, arXiv:math/0703236v1, first submitted 2007-03-08; primary MSC 42A05.
2. Sándor Krenedits, *Three-term idempotent counterexamples in the Hardy-Littlewood majorant problem*, arXiv:1006.0409v1, first submitted 2010-06-02; primary MSC 42A05.
3. Guancheng Pan, Chengsong You, Hengyu Wang, Junwei Zhou, Wenjun Zhang, and Yongchao Chen, *Mockenhaupt's Three-Term Hardy-Littlewood Majorant Conjecture*, arXiv:2609.09740v2, 2026; primary MSC 42A05.
