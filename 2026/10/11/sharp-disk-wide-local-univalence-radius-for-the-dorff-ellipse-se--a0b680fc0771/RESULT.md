# Sharp disk-wide local-univalence radius for the Dorff ellipse self-convolution

## Finding

For the specific normalized bounded convex harmonic ellipse mapping \(f=h+\overline g\) of Wang and Zhong (arXiv:2609.11556v1), let \(F=f\widetilde *f=p+\overline q\) be its harmonic Hadamard self-convolution. There is an exact critical radius \(\rho\) such that

\[
J_F(z)=|p'(z)|^2-|q'(z)|^2>0\qquad(|z|<\rho),
\]

and on the *entire* boundary circle \(|z|=\rho\) one has \(J_F\ge0\), with equality **only** at \(z=-\rho\). Thus the centered disk \(|z|<\rho\) is the largest centered disk on which \(F\) is everywhere sense-preserving and locally univalent. The radius is the unique \(\rho\in(0,1)\) satisfying \(P_6(-\rho)=0\), with \(P_6\) defined below, and obeys the exact rational enclosure

\[
0.961916078016035<\rho<0.961916078016036.
\]

This is a **disk-wide** first-contact statement: no nonreal Jacobian zero occurs at a smaller modulus or elsewhere on the first-contact circle. It neither asserts global injectivity on that disk nor classifies the Jacobian outside it.

## Assumptions and scope

Fix the coefficients in the cited normalized ellipse construction:

\[
\begin{aligned}
a&=-\frac{10}{11},& b&=\frac1{44},\\
A&=-\frac{9890884608}{9139543205},& B&=-\frac{251761689}{562995861428},\\
D&=\frac{1373955264}{9139543205},& C&=\frac{41190732}{12795360487}.
\end{aligned}
\]

For all integers \(n\ge2\), its coefficient tails are \(M_n=Aa^{n-2}+Bb^{n-2}\) and \(N_n=Da^{n-2}+Cb^{n-2}\), where \(h(z)=z+\sum_{n\ge2}M_nz^n\), \(g(z)=\sum_{n\ge2}N_nz^n\). Harmonic Hadamard self-convolution gives \(p(z)=z+\sum_{n\ge2}M_n^2z^n\) and \(q(z)=\sum_{n\ge2}N_n^2z^n\). These series converge on an open neighborhood of the closed unit disk because the geometric rates have modulus less than one.

Define \(S_u(z)=z(2-uz)/(1-uz)^2\). Then, as identities of rational analytic functions,

\[
\begin{aligned}
p'(z)&=1+A^2S_{a^2}(z)+2AB S_{ab}(z)+B^2S_{b^2}(z),\\
q'(z)&=D^2S_{a^2}(z)+2DC S_{ab}(z)+C^2S_{b^2}(z).
\end{aligned}
\]

The polynomial denominators stay nonzero for \(|z|\le1\).

## Proof

**1. Exact algebra and the sole radial candidate.** Put

\[
\begin{aligned}
P_4(z)={}&24297200z^4-94137557624z^3+96137381658603z^2\\
&-231722242336904z-360263217096475,\\[2mm]
P_6(z)={}&20269382049144670000z^6-76570023016489888285400z^5\\
&+64433804996566834468116815z^4+6563513204097494574954697684z^3\\
&+196525575821143049386765307327z^2-546666175276725488438747500196z\\
&-701902078885331749352905757780.
\end{aligned}
\]

Expansion of the displayed rational derivatives gives exact identities

\[
\begin{aligned}
p'-q'&=-\frac{3748096P_4(z)}{24606462475(z-1936)^2(100z-121)^2},\\
p'+q'&=-\frac{3748096P_6(z)}{818606249961404385845(z-1936)^2(5z+242)^2(100z-121)^2}.
\end{aligned}
\]

These algebraic identities, also occurring in earlier real-diameter analysis, are independently checked by rational polynomial cross-multiplication in the included script. The derivative of \(r\mapsto P_6(-r)\) is strictly positive on \([0,1]\): all its terms are nonnegative except the cubic contribution \(-3c_3r^2\), and the constant linear contribution \(-c_1\) exceeds \(3c_3\), where \(c_j\) is the coefficient of \(z^j\) in \(P_6\). Moreover \(P_6(0)<0<P_6(-1)\), so there is exactly one \(\rho\in(0,1)\) with \(P_6(-\rho)=0\). Exact rational evaluation gives the stated interval, and the script verifies it.

**2. The denominator is zero-free on the closed disk.** Set \(w=(1+z)/(1-z)\), so the right half-plane is the image of the unit disk. The Cayley transform of \(P_4\) is

\[
\begin{aligned}
Q(w)&=-(w+1)^4P_4\!\left(\frac{w-1}{w+1}\right)\\
&=495942191035200w^4+1904309175133260w^3\\
&\quad+2353853920112856w^2+977796756016140w+32309431246144.
\end{aligned}
\]

In descending order write these coefficients as \(a_4,a_3,a_2,a_1,a_0\). They are strictly positive and satisfy the two further quartic Routh–Hurwitz inequalities

\[
a_3a_2>a_4a_1,
\qquad a_3a_2a_1>a_4a_1^2+a_3^2a_0.
\]

The exact integer comparisons in the script prove both strict inequalities, so all roots of \(Q\) lie strictly in the left half-plane. It follows that \(P_4\) has no root on or inside \(|z|=1\). The linear factors \(5z+242\), \(100z-121\) and \(z-1936\) likewise have no zeros there. Thus \(p'-q'\ne0\) throughout \(|z|\le1\).

**3. A rational positivity certificate for the entire critical circle.** Let

\[
\Phi(z)=\frac{p'(z)+q'(z)}{p'(z)-q'(z)}
=\frac{24606462475}{818606249961404385845}\frac{P_6(z)}{P_4(z)(5z+242)^2}.
\]

Set \(W(z)=P_4(z)(5z+242)^2\), which is zero-free on \(|z|\le1\). On the circle \(z=re^{i\theta}\) let \(x=\cos\theta\), and form the real polynomial

\[
T(r,x)=\operatorname{Re}\!\bigl(P_6(re^{i\theta})\overline{W(re^{i\theta})}\bigr)
=\sum_{j=0}^6 t_j(r)x^j.
\]

Real coefficients and \(\cos(j\theta)=T_j(\cos\theta)\), with \(T_j\) the Chebyshev polynomials, justify this degree-six representation. Define

\[
H(r,x)=\frac{T(r,x)-T(r,-1)}{x+1},
\qquad x\in[-1,1],
\]

where the quotient is polynomial of degree at most five. Put \(x=2u-1\), \(u\in[0,1]\), and write the **degree-five Bernstein representation**

\[
H(r,2u-1)=\sum_{j=0}^{5}\beta_j(r)\binom5j u^j(1-u)^{5-j}.
\]

Each \(\beta_j(r)\) is a polynomial with integer coefficients in \(r\). The standalone `check_radius.py` derives all six coefficient polynomials from \(P_6\) and \(W\) without numerical interpolation. On the exact rational interval \([\ell,h]\) with

\[
\ell=\frac{961916078016035}{10^{15}},\qquad
h=\frac{961916078016036}{10^{15}},
\]

it verifies, separately for each \(j=0,\ldots,5\), the *exact rational* inequality

\[
\beta_j(\ell)-(h-\ell)\sum_{k\ge1}k|[r^k]\beta_j(r)|>0.
\]

This bounds the possible coefficient change using \(|r^k-\ell^k|\le k(h-\ell)\) for \(0\le\ell\le r\le h\le1\). Therefore every \(\beta_j(\rho)>0\) and hence \(H(\rho,x)>0\) for all \(-1\le x\le1\), including endpoints.

Because \(P_6(-\rho)=0\), we have \(T(\rho,-1)=0\), so

\[
T(\rho,x)=(x+1)H(\rho,x)\ge0,
\]

with equality exactly at \(x=-1\), or \(z=-\rho\). The constant multiplying \(P_6/W\) in \(\Phi\) is positive, and \(\operatorname{Re}(P_6/W)=T/|W|^2\). Consequently \(\operatorname{Re}\Phi\) is nonnegative all around \(|z|=\rho\), positive except at \(-\rho\). The harmonic minimum principle then gives \(\operatorname{Re}\Phi>0\) in \(|z|<\rho\).

**4. Jacobian and sharpness.** The elementary identity

\[
J_F(z)=|p'(z)-q'(z)|^2\operatorname{Re}\Phi(z)
\]

now yields \(J_F>0\) in \(|z|<\rho\), and \(J_F\ge0\) on its boundary with a unique zero at \(-\rho\). The inverse-function theorem makes \(F\) locally univalent and sense-preserving throughout that open disk. Every larger centered open disk contains \(-\rho\), where the differential has zero determinant and a harmonic map cannot be locally injective (Lewy's theorem). This proves optimality.

## Verification

Run `python3 check_radius.py` with an ordinary Python 3 installation; no third-party packages or network access are required. The checker was executed successfully against the exact bundled source, with output beginning `PASS: all polynomial identities, root bounds, Hurwitz test, and six Bernstein certificates`.

The checker reconstructs the rational derivatives from \(a,b,A,B,C,D\); cross-multiplies both factorizations; evaluates the exact \(P_6\) root bracket and monotonicity inequality; verifies the positive Cayley–Hurwitz coefficients and conditions; expands the trigonometric polynomial by Chebyshev recurrence; converts the divided difference to degree-five Bernstein form; and certifies six strictly positive *rational* interval margins. The six lower margins, divided by \(10^{49}\), all exceed \(1.56\). The finite computation is a certificate of a universal circle statement because the polynomial and interval inequalities prove positivity continuously for all angles and all radii in the root enclosure; it is not a numerical sample.

## Relationship to prior work

Wang and Zhong's September 2026 paper constructs the bounded convex harmonic ellipse mapping and proves that its self-convolution fails local univalence by exhibiting a negative Jacobian at one real point and a positive Jacobian at the origin. The previously published *Unique real-axis fold point in the Dorff ellipse counterexample* derives exact polynomial factors and counts the critical points on the **real diameter only**. Neither statement rules out nonreal critical points with smaller modulus.

The disk-wide argument here adds a Cayley–Hurwitz denominator proof and a positive Bernstein certificate on the **whole critical circle**. It proves that the known real root is the first loss of sense-preserving local univalence anywhere in a centered disk. Earlier harmonic convolution results for half-plane/strip maps and special dilatation classes do not imply a statement about this new ellipse self-convolution. Primary-paper, published-record, and equivalence/alias searches were compared on their mathematical implications, not only their titles.

## Limitations

Only this specific normalized rational ellipse mapping is covered; the radius is not universal over all convex harmonic mappings. Local univalence is not global injectivity. No classification of the Jacobian's zero set outside \(|z|=\rho\), or of the locus under variation of the ellipse parameters, is asserted. Unindexed equivalent literature is an originality risk. Independent validation has not been performed.

## References

1. Z.-G. Wang and D. Zhong, *A counterexample to an open problem of Dorff*, arXiv:2609.11556v1 (first public September 10, 2026).
2. *Unique real-axis fold point in the Dorff ellipse counterexample* (2026), public mathematical record identifier `8f1ef438e553`, available in the published-finding corpus 2026 mathematical archive.
3. M. Dorff, *Convolutions of planar harmonic convex mappings*, Complex Variables 45 (2001), 263–271. DOI: 10.1080/17476930108815381.
4. Z. Boyd, M. Dorff, M. Nowak, M. Romney and M. Wołoszkiewicz, *Univalency of convolutions of harmonic mappings*, Applied Mathematics and Computation 234 (2014), 326–332. DOI: 10.1016/j.amc.2014.01.162.
5. O. P. Ahuja and J. M. Jahangiri, *Convolutions of Harmonic Functions with Certain Dilatations*, International Journal of Mathematics and Mathematical Sciences (2017), Article 4015268. DOI: 10.1155/2017/4015268.
