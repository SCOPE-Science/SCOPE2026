# Sharp drift threshold for fourth-order Gauss positivity on a bidirectional four-cycle

## Finding
Let \(P\) be the cyclic shift of four states, with \(P_{i,j}=1\) when \(j=i+1\pmod4\). For rates \(a,b>0\), set
\[
Q=a(P-I)+b(P^{\mathsf T}-I),\qquad
T(h)=\bigl(12I+6hQ+h^2Q^2\bigr)\bigl(12I-6hQ+h^2Q^2\bigr)^{-1}.
\]
The two-stage, fourth-order Gauss--Legendre approximation \(T(h)\) is entrywise nonnegative for **every** step \(h\ge0\) if and only if
\[
\boxed{\frac1{\sqrt3}\le\frac ab\le\sqrt3.}
\]
Outside this closed bias interval, there is a **unique** positive limiting timestep \(H(a,b)\): the approximation is entrywise nonnegative precisely for \(0\le h\le H(a,b)\), and one nearest-neighbor transition is strictly negative for every \(h>H(a,b)\).

For \(a>\sqrt3b\), the horizon \(H(a,b)\) is the unique positive root of
\[
F_a(h)=216a+216a(a+b)h+36(2a^3+5a^2b+2ab^2+b^3)h^2
+36b(a+b)(a^2+b^2)h^3
+3(a+b)(a^2+b^2)(3b^2-a^2)h^4.
\]
For \(b>\sqrt3a\), it is the unique positive root of \(F_b\), obtained by exchanging \(a\) and \(b\) in \(F_a\). At either exact boundary \(a=\sqrt3b\) or \(b=\sqrt3a\), positivity holds for every finite step.

## Assumptions and scope
The state space consists of four cyclically ordered vertices labeled \(0,1,2,3\). Both clockwise and anticlockwise rates are constant around the loop and strictly positive, but need not be equal. The generator \(Q\) has row sums zero and strictly positive transition rates along both directions, so the exact semigroup \(e^{hQ}\) is strictly positive for every \(h>0\). Matrix nonnegativity means **entrywise** nonnegativity of the completed numerical update; it does not assert positivity of internal Runge--Kutta stages. All comparisons hold for arbitrary real \(a,b>0\) and real \(h\ge0\). No claim is made for nonconstant edge rates, larger cycles, or different integrators.

## Proof
Put \(s=a+b\) and \(r(z)=(12+6z+z^2)/(12-6z+z^2)\). The eigenvalues of \(Q\) are \(0\), \(-2s\), and \(-s\pm i(a-b)\), so diagonalization by the four-point discrete Fourier transform gives the four distinct entries in the first row of \(T(h)\):
\[
 t_0=\frac{1+r(-2sh)+2\Re r((-s+i(a-b))h)}4,\qquad
 t_2=\frac{1+r(-2sh)-2\Re r((-s+i(a-b))h)}4,
\]
\[
 t_1=\frac{1-r(-2sh)+2\Im r((-s+i(a-b))h)}4,\qquad
 t_3=\frac{1-r(-2sh)-2\Im r((-s+i(a-b))h)}4.
\]
(The labels of the two nearest-neighbor entries follow the chosen orientation of \(P\).) The rational functions share the strictly positive denominator
\[
D(h)=2(s^2h^2+3sh+3)\bigl((a^2+b^2)^2h^4+6s(a^2+b^2)h^3
 +(18(a^2+b^2)+24ab)h^2+36sh+36\bigr).
\]
Indeed, both factors have strictly positive coefficients. Direct exact simplification yields \(t_j=N_j/D\), where
\[
\begin{aligned}
N_0={}&216+216sh+72(a^2+4ab+b^2)h^2+144absh^3\\
&+6(a^2+4ab+b^2)^2h^4+3s(a^2+b^2)(3a^2+4ab+3b^2)h^5+2s^2(a^2+b^2)^2h^6,\\
N_2={}&3h^2(a^2+b^2)\bigl(36+36sh+12s^2h^2+s(a^2+4ab+b^2)h^3\bigr),\\
N_1={}&hF_a(h),\qquad N_3=hF_b(h).
\end{aligned}
\]
Thus \(N_0>0\) for every \(h\ge0\), and \(N_2>0\) whenever \(h>0\). Each of the two direction polynomials \(F_a,F_b\) has **four strictly positive coefficients**, at degrees zero through three. Their respective quartic leading coefficients are
\[
3s(a^2+b^2)(3b^2-a^2),\qquad 3s(a^2+b^2)(3a^2-b^2).
\]
If these are both nonnegative, both direction polynomials are strictly positive for all finite \(h\ge0\), giving the asserted bias interval. Otherwise exactly one leading coefficient is negative; the other direction polynomial is positive for all \(h\ge0\). The polynomial with negative leading term starts positive and tends to \(-\infty\). Its sequence of nonzero coefficients in descending powers has exactly one sign change, so Descartes' rule of signs supplies at most one positive root, while the intermediate value theorem supplies at least one. The root is simple (its single sign change and leading behavior imply crossing), and its sign is positive below and negative above that root. Since \(T(0)=I\), the complete positivity set is exactly the interval stated above. This proves all quantifiers and endpoint cases.

## Verification
The accompanying `verify.py` constructs the spectral expressions symbolically, verifies all four exact numerator and common-denominator identities, and compares them with direct inverses of the full four-by-four numerical update for 60 rational rate-and-step choices (240 matrix entries), also checking stochastic row sums. It prints `VERIFY_OK` on completion. The proof above, rather than a finite sample, establishes the universal bias and timestep classification.

## Relationship to prior work
Zappavigna, Colaneri, Kirkland and Shorten (2010) developed positivity criteria for Padé discretizations of Metzler matrices, including second-order diagonal Padé sufficient conditions, counterexamples and the complete two-state setting. Their bounds do not imply the exact all-step *necessary and sufficient* asymmetric four-cycle threshold or the unique quartic horizon. Their 2012 related paper emphasizes that stability and positivity preservation may differ and proposes alternative integrators. These works motivate an exact structured class rather than settle this instance. General four-state Markov statements and symmetric or unidirectional cyclic specializations do not alone entail the strict asymmetric threshold or its full phase diagram.

## Limitations
The result concerns only a four-state translation-invariant, two-way cycle and one rational approximation. Its nonnegativity is a completed-step statement; no stagewise positivity, higher-state generalization, or strict novelty theorem about all historical literature is asserted. Fourier numerator identities are elementary exact algebra, independently checked by the standalone program. Historical equivalence risks remain, especially in specialized positive-systems and circulant-matrix literature.

## References
1. A. Zappavigna, P. Colaneri, S. Kirkland, R. N. Shorten, *On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems* (MTNS 2010), accessible manuscript and bibliographic metadata: https://mural.maynoothuniversity.ie/id/eprint/2195/ (repository deposit 2010-10-15).
2. A. Zappavigna, P. Colaneri, S. Kirkland, R. N. Shorten, *Essentially Negative News About Positive Systems* (2012), open preprint: https://mural.maynoothuniversity.ie/id/eprint/3761/ (repository deposit 2012-06-19).
