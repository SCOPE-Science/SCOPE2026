# Root topology and two-speed boundary condensation for gap-four Hartogs diagonals

## Finding
For each odd integer \(n\ge3\), put \(m=n+4\). The degree-eight diagonal Bergman-numerator polynomial \(Q_{m,n}\) of the rational Hartogs triangle \(\mathbb H_{m/n}\) has eight simple roots, four in the punctured unit disk and four their reciprocals outside the closed unit disk. The four inside consist of exactly two negative real roots and a nonreal conjugate pair. Denote the two real interior roots by \(r_{n,0}\) and \(r_{n,1}\), chosen so that \(r_{n,0}\to-2+\sqrt3\) and \(r_{n,1}\to-1\), and choose \(z_{n,\pm}\) with \(\operatorname{Im}z_{n,\pm}\gtrless0\). As odd \(n\to\infty\),
\[
\begin{aligned}
r_{n,0}&=-2+\sqrt3+\frac{17\sqrt3-51/2}{n^2}+O(n^{-3}),\\
r_{n,1}&=-1+\frac{2\sqrt3}{n}+O(n^{-2}),\\
z_{n,\pm}&=\pm i\left(1-\frac{\sqrt3}{n}\right)+O(n^{-2}).
\end{aligned}
\]
In particular \(n(1-|r_{n,1}|)\to2\sqrt3\) and \(n(1-|z_{n,\pm}|)\to\sqrt3\). The qualitative gap-four nonvanishing previously announced by Edholm and Mathew is not claimed as new; the root topology, simplicity, and explicit two-speed condensation law are the findings.

## Assumptions and scope
Define \(\mathbb H_{m/n}=\{(z_1,z_2)\in\mathbb C^2:|z_1|^{m/n}<|z_2|<1\}\). For two domain points put \(s=z_1\overline w_1\), \(t=z_2\overline w_2\). Edholm--Mathew [1], Theorem 1.3, define the kernel numerator \(P_{m,n}(s,t)\) and its diagonal normalization \(Q_{m,n}(s)=s^{1-2n}P_{m,n}(s,s)\). As \(\gcd(n,n+4)=1\) if and only if \(n\) is odd, precisely these indices are considered. The statement concerns the eight zeros of this *one-variable numerator* and the four interior diagonal zero parameters, not all zeros of the full two-variable kernel. Roots are counted algebraically, and all asymptotics are along odd positive integers.

## Proof
**1. Exact quartic.** Let \(s\ne0\), \(x=s+s^{-1}\), and \(\rho\in\{1,3\}\) be the residue of \(n\pmod4\). Reindex Edholm--Mathew's five numerator sums [1, equations (1.4c)--(1.4h)] with \(k=j+1\) and \(h=\lfloor(4k-1)/(n+4)\rfloor\). The contribution of each \(k\) to \(Q_{n+4,n}\) is
\[
\begin{aligned}
&k((n+4)(h+1)-4k)s^h+k(4k-(n+4)h)s^{h+1}\\
&+((n+4)-k)((n+4)(h+1)-4k)s^{h+4}\\
&+((n+4)-k)(4k-(n+4)h)s^{h+5},
\end{aligned}
\]
plus \((n+4)^2s^4\), summed for \(1\le k\le n+3\). When \(m=n+4=4q+1\), the four successive \(k\)-ranges are \([1,q]\), \([q+1,2q]\), \([2q+1,3q]\), \([3q+1,4q]\). When \(m=4q+3\), they are \([1,q]\), \([q+1,2q+1]\), \([2q+2,3q+2]\), \([3q+3,4q+2]\). Applying the formulas for \(\sum k\) and \(\sum k^2\), using palindromicity, gives
\[
s^{-4}Q_{n+4,n}(s)=\Phi_n(x),\qquad
96\Phi_n(x)=n^2(n+12)F(x)+nB(x)+6C_\rho(x),
\]
where
\[
\begin{aligned}
F(x)&=x^2(x+2)(x+4),\\
B(x)&=41x^4+294x^3+400x^2-48x+96,\\
C_1(x)&=7x^4+66x^3+92x^2-24x+64,\\
C_3(x)&=5x^4+70x^3+100x^2-40x+64.
\end{aligned}
\]
The standalone checker verifies the coefficient identities as polynomial identities in the unrestricted residue parameter \(q\), not by numerical fitting.

**2. Exactly two real transformed roots.** For \(x\in[-2,2]\), \(F(x)\ge0\). Both \(B\) and \(C_\rho\) are *strictly positive* on that interval: subdivide into the four unit intervals and express each quartic in the degree-four Bernstein basis. All twenty coefficients for each polynomial are strictly positive rational numbers; the complete exact coefficient verification is included in the checker. For \(x\ge2\), the same polynomials have strictly positive coefficients in the shifted monomial basis \(x=2+t\), \(t\ge0\), while \(F(x)\ge0\). Therefore \(\Phi_n(x)>0\) for every real \(x\ge-2\).

Set \(t=-x-2>0\) on the other real half-line. The five coefficients of \(\Phi_n(-2-t)\), from highest degree to constant, have sign pattern \((+,+,-,-,+)\). More explicitly, for \(\rho=1\) they are
\[
\frac{(n+2)(n+3)(n+7)}{96},\quad
\frac{(n-1)(n+3)(n+10)}{48},\quad
-\frac{(n+3)(n^2+9n+68)}{24},\quad
-\frac{(n+3)(n^2+9n+44)}{12},\quad n+4;
\]
for \(\rho=3\) they are
\[
\frac{(n+1)(n+5)(n+6)}{96},\quad
\frac{(n-2)(n+5)(n+9)}{48},\quad
-\frac{(n+5)(n^2+7n+60)}{24},\quad
-\frac{(n+5)(n^2+7n+36)}{12},\quad n+4.
\]
Since \(n\ge3\), Descartes' rule gives at most two positive \(t\)-roots, counted with multiplicity. But \(\Phi_n(-2)=n+4>0\), \(\Phi_n(-4)=-17n-50<0\) when \(\rho=1\), and \(\Phi_n(-4)=-17n-86<0\) when \(\rho=3\), whereas \(\Phi_n(x)\to+\infty\) as \(x\to-\infty\). Hence there are exactly two *distinct simple* real roots, one in \((-\infty,-4)\), the other in \((-4,-2)\). As the quartic has real coefficients, its other two roots are a simple nonreal conjugate pair.

**3. Lift to the disk.** Each transformed root \(x\notin[-2,2]\) produces exactly one solution of \(s+s^{-1}=x\) in \(0<|s|<1\) and its reciprocal outside: an alleged solution on the unit circle would have real \(x\in[-2,2]\). Distinct transformed roots give distinct \(s\); none equals \(\pm1\). The two real \(x<-2\) produce two distinct negative-real interior roots. The nonreal conjugate pair produces the interior nonreal conjugate pair. Every root is simple. By the diagonal zero correspondence in [1], all four are genuine interior zero parameters of the rational Hartogs kernel.

**4. Sharp coalescence rates.** Write \(\epsilon=1/n\). Dividing the quartic formula by \(n^3\) yields
\[
(1+12\epsilon)F(x)+\epsilon^2 B(x)+6\epsilon^3C_\rho(x)=0.
\]
At \(\epsilon=0\), \(F(x)\) has a simple root at \(-4\), a simple root at \(-2\), and a double root at \(0\). At \(-4\), since \(F'(-4)=-32\) and \(B(-4)=-1632\), the root has \(x=-4-51\epsilon^2+O(\epsilon^3)\). The interior branch of \(s+s^{-1}=x\) is \(s=-2+\sqrt3+(17\sqrt3-51/2)\epsilon^2+O(\epsilon^3)\). At \(-2\), since \(F'(-2)=8\) and \(B(-2)=96\), we have \(x=-2-12\epsilon^2+O(\epsilon^3)\). Thus \(s=-1+2\sqrt3\epsilon+O(\epsilon^2)\) for the interior negative branch. At \(0\), set \(x=\epsilon u\); the rescaled equation is \(8u^2+96+O(\epsilon)=0\), with simple limiting roots \(u=\pm2i\sqrt3\). Since \(\frac{d}{ds}(s+s^{-1})=2\) at \(s=\pm i\), the two interior branches are \(s=\pm i(1-\sqrt3\epsilon)+O(\epsilon^2)\). The implicit-function theorem applied to these rescaled equations justifies the stated uniform remainder orders along each residue class; their leading coefficients coincide, so the asymptotics hold along all odd integers.

## Verification
Execute `python verify_gap4.py` with SymPy installed. The checker reconstructs the diagonal coefficients by closed power-sum identities for both residue classes, confirms the quartic reduction symbolically, checks every Bernstein coefficient and the shifted large-\(x\) positivity coefficients exactly, and checks the leading collision balances. The proof of the sign-based root count and analytic implicit-function steps is explicitly given above. Finite numerical root plots are not used as proofs.

## Relationship to prior work
Edholm and Mathew [1] derive the universal rational kernel formula and the palindromic diagonal polynomial. **Their §4.3 already announces a proof of qualitative unit-circle nonvanishing for gaps \(3,4,6\)**, and Conjecture 4.20 concerns all gaps: neither that announced gap-four theorem nor its implied four-interior-zero count is a novelty claim here. The present result gives the **full real/complex root topology and simplicity for every coprime gap-four numerator**, then determines two different sharp first-order boundary-collision speeds and the second-order displacement of the persistent real root. The gap-three root-condensation result [2] has a different degree-six polynomial and a different limit configuration. Related gap-five and gap-seven-through-seventeen nonvanishing records [3,4] determine counts but do not logically give this gap-four geometry.

## Limitations
The roots treated here belong to the diagonal numerator; this does not classify the entire several-complex-variable kernel zero variety. The finite-\(n\) theorem does not identify an elementary closed form for every root. The asymptotic expansions give the displayed orders but no claim of uniformity in a second varying geometric parameter. Edholm--Mathew report additional work in preparation, which might contain overlapping unpublished root geometry. No independent audit has been performed.

## References
[1] L. D. Edholm and V. T. Mathew, *Arithmetic properties and zeros of the Bergman kernel on a class of quotient domains*, arXiv:2505.20489v1 (first posted 2025-05-26); *Mathematische Zeitschrift* 313, article 43 (2026), DOI: 10.1007/s00209-026-04059-8. In particular Theorem 1.3, Theorem 1.5 and §4.3.
[2] *Cubic-root condensation of diagonal Bergman-kernel zeros in gap-three Hartogs triangles*, published-finding corpus record `indexed 2026 publication (title given)` (indexed summary consulted; full record was not accessible).
[3] *Difference-five Bergman numerator polynomials have no unit-circle zeros*, published-finding corpus record `indexed 2026 publication (title given)` (indexed summary consulted).
[4] *Bergman zeros for every rational Hartogs numerator gap from seven through seventeen*, published-finding corpus record `indexed 2026 publication (title given)` (indexed summary consulted).
