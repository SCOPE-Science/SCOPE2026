# Exponential bounds for the shortest digit-appending step in an algebraic recurrence

## Finding

For a fixed integer linear recurrence with one simple dominant root and for a multiplicatively independent digit base, the smallest number of digits needed to append in any outgoing step grows **exponentially** with the source index. Precisely, for the quantity \(T(m)\) defined below, there are \(0<c<C<\infty\) and \(M\) such that

\[
 e^{cm}\le T(m)\le e^{Cm}\qquad(m\ge M).
\]

This supplies a two-sided quantitative counterpart to the qualitative existence and bounded-length obstruction in [1]. In particular, \(\log T(m)=\Theta(m)\), with implicit constants depending on the recurrence and base.

## Assumptions and scope

Let \((a_n)_{n\ge0}\) be integers satisfying a constant-depth recurrence with rational coefficients. Suppose its **minimal** characteristic polynomial has a unique dominant root \(\alpha\in\mathbb R\), this root is simple, and \(r=|\alpha|>1\). Denote the largest modulus of other nonzero roots by \(\rho<r\), allowing \(\rho=0\). Generalized Binet expansion gives

\[
 a_n=A\alpha^n+E_n,\qquad A\ne0,\qquad
 |E_n|\le K(qr)^n
\]

for any fixed \(q\in(\rho/r,1)\) and suitable \(K>0\), uniformly for sufficiently large \(n\). Repeated subordinate roots are absorbed into the chosen \(q\). In particular, \(|a_m|\asymp r^m\) and \(a_m\ne0\) for large \(m\).

Fix an integer \(b\ge2\). Assume multiplicative independence of \(r\) and \(b\): there do not exist positive integers \(u,v\) with \(r^u=b^v\). Define a digit-appending step from index \(m\) to \(m+k\) to mean

\[
 a_{m+k}=b^t a_m+d\operatorname{sgn}(a_m),
 \quad k,t\in\mathbb Z_{\ge1},\quad d\in\mathbb Z,\quad 0\le d<b^t.
\]

For large \(m\) define \(T(m)\) as the minimum such \(t\) among all permissible \(k,d\). Finiteness is proved below, not presupposed. The constants in the theorem are not uniform across recurrences or bases.

## Proof

**1. A polynomial irrationality bound.** Since \(r\) and \(b\) are positive algebraic numbers, their real logarithms are linearly independent over \(\mathbb Q\). The standard lower bound for nonzero linear forms in logarithms of fixed algebraic numbers [3] gives constants \(L>0\) and \(D\ge1\), depending only on \(r,b\), such that

\[
 |u\log r-v\log b|\ge
 L\max(u,v,2)^{-D}
\]

for positive integers \(u,v\). In particular, with \(h=1\) if \(\alpha>0\) and \(h=2\) if \(\alpha<0\), the irrational rotation \(\theta=h\log_b r\) obeys

\[
 \|j\theta\|\ge L_1 j^{-D}\qquad(j\ge1)
\]

for a possibly smaller \(L_1>0\). Here \(\|x\|\) means distance to the nearest integer. For large \(j\), the nearest integer is positive and comparable with \(j\); the remaining finite set can be absorbed into \(L_1\).

**2. Universal exponential lower bound.** The dominant-root estimate implies [1, Lemma 2.2] that, for all sufficiently large \(m\) and every \(k\ge0\),

\[
 \frac{|a_{m+k}|}{r^k|a_m|}=1+O(q^m),
\]

with a constant independent of \(k\). If a digit-appending step exists, then

\[
 \frac{|a_{m+k}|}{b^t|a_m|}
 =1+\frac{d}{b^t|a_m|}
 =1+O(r^{-m}).
\]

Dividing these identities, and putting \(\eta=\max(q,r^{-1})<1\), gives

\[
 \left|\frac{r^k}{b^t}-1\right|\ll\eta^m,
 \qquad |k\log r-t\log b|\ll\eta^m.
\]

(The logarithm estimate follows for large \(m\), when the displayed ratio is close to one.) Consequently \(k\log r=t\log b+O(1)\), so \(\max(k,t,2)\ll t\). The logarithmic-form bound from Step 1 yields

\[
 L' t^{-D}\ll\eta^m,
 \qquad t\gg\eta^{-m/D}.
\]

After decreasing the positive exponent to absorb multiplicative constants, every outgoing step from large \(m\) requires \(t\ge e^{cm}\). This proves the lower estimate for \(T(m)\), if it exists.

**3. Quantitative visits to a shrinking interval.** For the irrational rotation by \(\theta\), the geometric-sum identity and Step 1 imply, for every \(j_0\ge0\), integer \(Q\ge1\), and integer frequency \(s\ge1\),

\[
 \left|\sum_{j=j_0+1}^{j_0+Q}
 e^{2\pi i s j\theta}\right|
 \le\frac{1}{2\|s\theta\|}\ll s^D.
\]

The Erdős–Turán discrepancy inequality [4], applied with cutoff \(H\), therefore gives, for every circular interval \(J\) of length \(\delta\),

\[
 \left|\#\{j_0<j\le j_0+Q:\{j\theta\}\in J\}-Q\delta\right|
 \ll \frac{Q}{H}+H^D.
\]

Choose \(H=\lfloor Q^{1/(D+1)}\rfloor\), with the usual adjustment when \(H<1\), to obtain an error \(O(Q^{D/(D+1)})\), uniformly in both interval position and starting index. Thus there is a constant \(K_0\) such that every interval of length \(0<\delta<1\) contains a rotation point \(\{j\theta\}\) with

\[
 Q\le j<2Q,
 \qquad Q=\left\lceil K_0\delta^{-(D+1)}\right\rceil.
\]

Indeed, the expected count \(Q\delta\) exceeds the discrepancy error for sufficiently large \(K_0\).

**4. Constructing an outgoing step with exponentially many digits.** Fix sufficiently large \(m\). Consider the positive interval

\[
 I_m=\left(
 \frac{|a_m|+1/3}{|A|r^m},
 \frac{|a_m|+2/3}{|A|r^m}
 \right).
\]

It lies near one, and its logarithmic interval \(\log_b I_m\) has length

\[
 \delta_m=
 \log_b\!\left(\frac{|a_m|+2/3}{|a_m|+1/3}\right)
 \asymp r^{-m}.
\]

For large \(m\), \(\delta_m<1\); its projection modulo one is an interval of that length on the unit circle, including the possible wrap at zero. Apply Step 3 with this circular interval and with \(Q=\lceil K_0\delta_m^{-(D+1)}\rceil\). Some \(j\in[Q,2Q)\) then satisfies

\[
 j\theta-t\in\log_b I_m
\]

for an integer \(t\); since \(j\to\infty\), this \(t\) is positive for large \(m\). Put \(k=hj\). Thus \(k\ge Q\), \(k\) is even when \(\alpha<0\), and

\[
 \frac{r^k}{b^t}\in I_m,
 \qquad t\asymp j\le2Q\ll r^{(D+1)m}.
\]

By the choice of \(I_m\),

\[
 |a_m|+\tfrac13<\frac{|A|r^{m+k}}{b^t}
 <|a_m|+\tfrac23.
\]

Meanwhile, because \(k\ge Q\) and \(Q\asymp r^{(D+1)m}\),

\[
 \frac{|E_{m+k}|}{b^t}
 \le K(qr)^m q^k\frac{r^k}{b^t}
 \ll (qr)^m q^Q<\tfrac13
\]

for all large \(m\), even when \(qr>1\). It follows that

\[
 b^t|a_m|<|a_{m+k}|<b^t(|a_m|+1).
\]

Since \(k\) is even when \(\alpha<0\), the eventual signs of \(a_m\) and \(a_{m+k}\) agree. Set the integer \(d=|a_{m+k}|-b^t|a_m|\). Then \(0<d<b^t\), and the required signed digit-appending identity holds. Hence \(T(m)\) exists and

\[
 T(m)\le t\ll r^{(D+1)m}\le e^{Cm}
\]

for some fixed \(C>0\) and all sufficiently large \(m\). This finishes the proof. \(\square\)

## Verification

The standalone `verify.py` calculates first eligible outgoing steps using only Python integer arithmetic. It checks ten source indices for the powers \(2^n\) in base \(10\), six for \(3^n+1\) in base \(2\), and six for the negative-dominant-root sequence \((-2)^n\) in base \(10\). It checks every smaller index jump up to each first witness; it also verifies the exact appended block and the parity restriction in the negative-root case. The finite output is `VERIFY_OK: 10 power, 6 shifted-power, 6 negative-root cases`. These experiments do **not** verify an asymptotic exponential bound, the Baker–Wüstholz inequality, or the discrepancy lemma, all of which are used analytically above.

## Relationship to prior work

Mosahab, Boyyakar, Bruda, Kominers, and Miller [1, Theorems 1.2 and 1.3] establish respectively an eventual obstruction to any *fixed* appended digit bound and infinitely many outgoing steps when the bound is unrestricted. Their proofs use asymptotic rigidity and qualitative Kronecker density; neither theorem gives a uniform quantitative scale of the **shortest** permissible appended block as a function of starting index. The present claim yields matched exponential-order lower and upper bounds by combining the same dominant-root estimate with a quantitative logarithmic-form separation and polynomial discrepancy for algebraic logarithmic rotations.

Kominers [2] proves bounds on the number of steps in an at-most-\(N\)-digits Fibonacci/Lucas walk. Even where those imply an eventual linear lower bound on the permitted digit length for one family, they do not imply the claimed exponential lower bound nor the constructive exponential upper bound for all recurrences in the stated class. The earlier Fibonacci walk work [5] treats bounded digits and not this invariant. The mathematical ingredients from [3,4] are classical; what is asserted here is the application to the previously unquantified least outgoing digit length. A stronger implicit quantitative implication in unlocated literature remains a residual originality risk.

## Limitations

The bounds give only the exponential scale, not an exact limit or sharp exponent for \(\log T(m)/m\). All constants depend on the fixed algebraic recurrence and base, and the result assumes one simple dominant root and multiplicative independence. It does not classify dependent bases or multiple dominant roots. The proof relies on the standard (non-elementary) lower bound for linear forms in algebraic logarithms; the verifier is finite supporting evidence, not its proof. Independent mathematical review has not been performed.

## References

1. A. Mosahab, S. Boyyakar, G. Bruda, S. D. Kominers, S. J. Miller, *On Digit-Appending Walks Along Linear Recurrences*, arXiv:2610.18919v1 (first public 2026-10-12), Sections 2–4. https://arxiv.org/html/2610.18919v1
2. S. D. Kominers, *Uniform Bounds for Digit-Appending Fibonacci Walks*, arXiv:2512.06446v1 (2025), Sections 2–4. https://arxiv.org/html/2512.06446v1
3. A. Baker and G. Wüstholz, *Logarithmic Forms and Diophantine Geometry*, Cambridge University Press (2007), lower bounds for nonzero algebraic logarithmic forms.
4. L. Kuipers and H. Niederreiter, *Uniform Distribution of Sequences*, Wiley (1974), Erdős–Turán inequality and discrepancy estimates.
5. S. J. Miller, F. Peng, T. Popescu, N. Wattanawanichkul, *Walking to Infinity on the Fibonacci Sequence*, arXiv:2204.08138 (2022).
