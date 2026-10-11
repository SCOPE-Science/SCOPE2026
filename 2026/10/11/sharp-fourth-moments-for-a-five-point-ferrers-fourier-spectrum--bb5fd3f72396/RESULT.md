# Sharp fourth moments for a five-point Ferrers Fourier spectrum

## Finding
Let \(G\) be a compact abelian group with normalized Haar probability measure \(\mu\). Let \(\chi,\eta,\gamma\) be continuous characters, and suppose that the fifteen characters \(\chi^j\eta^k\), \(0\le j\le4\), \(0\le k\le2\), are pairwise distinct. For arbitrary complex \(a,b,c,d,e\), put
\[
F(g)=\gamma(g)\left(a+b\chi(g)+c\chi(g)^2+d\eta(g)+e\chi(g)\eta(g)\right).
\]
Define \(\rho\) as the unique positive solution of
\[
2\rho^4+10\rho^3-19\rho-4=0,
\]
and put
\[
\tau=\frac{\rho^4+4\rho^3-4\rho^2+8\rho+2}{\rho^2+8\rho+2},
\qquad
K=\frac{5\rho^4+32\rho^3+28\rho^2+64\rho+14}
{3\rho^4+16\rho^3-4\rho^2+32\rho+8}.
\]
Then the following inequality has its **optimal** constant:
\[
\int_G|F(g)|^4\,d\mu(g)\le K\bigl(|a|^2+|b|^2+|c|^2+|d|^2+|e|^2\bigr)^2.
\]
Numerically \(\rho=1.320162620401\ldots\), \(\tau=1.246542777672\ldots\), and \(K=2.646915130955\ldots\).

All nonzero equality vectors, and no others, are
\[
(a,b,c,d,e)=\lambda\left(1,\rho e^{i\phi},e^{2i\phi},
\sqrt{\tau}\,e^{i\psi},\sqrt{\tau}\,e^{i(\phi+\psi)}\right),
\qquad\lambda\in\mathbb C\setminus\{0\},\quad\phi,\psi\in\mathbb R.
\]
Thus the sharp coefficient amplitudes are nonuniform, and the only free relative phases are the two character-modulation phases. The same constant holds on the continuous two-torus and on every discrete product \(\mathbb Z_N\times\mathbb Z_M\) with \(N\ge5\) and \(M\ge3\), for the two standard generating characters.

## Assumptions and scope
The five-point support is the minimal two-row Ferrers subset with a three-point row and a two-point row, producing both a row-midpoint collision and two linked mixed-row collisions:
\[
S=\{(0,0),(1,0),(2,0),(0,1),(1,1)\}\subset\mathbb Z^2.
\]
The fifteen-character hypothesis ensures that all pair sums in \(S+S\) remain distinct unless they already coincide as integer lattice pairs. This is the exact non-aliasing condition used in the proof. It holds for the continuous two-torus; for standard characters of a finite direct product it holds for \(N\ge5\), \(M\ge3\). The extra modulation character \(\gamma\) has modulus one and does not change fourth moments. The coefficient norm is the unweighted Euclidean squared norm, and Haar measure has total mass one. No restriction on coefficient phases or moduli is imposed.

## Proof
Write \(N_0=|a|^2+|b|^2+|c|^2+|d|^2+|e|^2\). By the assumed character distinctness, Fourier orthogonality and the ordered pair-sum convolution give the exact identity
\[
\begin{aligned}
\int_G|F|^4\,d\mu={}&2N_0^2-(|a|^4+|b|^4+|c|^4+|d|^4+|e|^4)\\
&+4\operatorname{Re}(b^2\overline{ac})+8\operatorname{Re}(ae\overline{bd})
+8\operatorname{Re}(be\overline{cd}).
\end{aligned}
\tag{1}
\]
There are exactly three nontrivial types of pair-sum collision: the midpoint \((0,0)+(2,0)=2(1,0)\), and the linked equalities \((0,0)+(1,1)=(1,0)+(0,1)\) and \((1,0)+(1,1)=(2,0)+(0,1)\). The identity is valid for all complex coefficients, including zero coefficients.

Put \(u=|a|^2+|c|^2\), \(v=|d|^2+|e|^2\), and \(B=|b|\). Applying \(2|ac|\le u\), \(2|de|\le v\), \(|a|+|c|\le\sqrt{2u}\), and the two quartic Cauchy bounds to (1), with \(N_0=u+v+B^2\), yields
\[
\int_G|F|^4\,d\mu
\le 2N_0^2-\frac{u^2}{2}-\frac{v^2}{2}-B^4+2uB^2+4Bv\sqrt{2u}.
\tag{2}
\]
Every step in (2) is simultaneously sharp when \(|a|=|c|\), \(|d|=|e|\), and the three interaction terms in (1) have positive real part equal to their moduli.

If \(u=0\), the remaining three lattice frequencies have no nontrivial sum collisions, so the ratio of the fourth moment to \(N_0^2\) is at most \(5/3<K\). Suppose \(u>0\), write \(x=\sqrt{u/2}>0\), \(r=B/x\ge0\), \(t=v/(2x^2)\ge0\), and divide (2) by \(N_0^2=x^4(2+r^2+2t)^2\). The quotient is at most
\[
H(r,t)=2-\frac{2+2t^2+r^4-4r^2-16rt}{(2+r^2+2t)^2}.
\tag{3}
\]
A direct derivative calculation, valid on the entire closed quadrant, gives
\[
\frac{\partial H}{\partial t}=
\frac{4\left(A(r)-B_0(r)t\right)}{(2+r^2+2t)^3},
\quad A(r)=r^4+4r^3-4r^2+8r+2,
\quad B_0(r)=r^2+8r+2.
\]
Both polynomials are strictly positive for \(r\ge0\): in particular \(A(r)=r^4+4r(r^2-r+2)+2>0\). Hence for each fixed \(r\ge0\) there is exactly one maximizer in \(t\ge0\):
\[
t(r)=\frac{A(r)}{B_0(r)}>0.
\]
Substitution, without approximation, simplifies the quotient to
\[
J(r)=H(r,t(r))=\frac{P(r)}{D(r)},
\quad P(r)=5r^4+32r^3+28r^2+64r+14,
\quad D(r)=3r^4+16r^3-4r^2+32r+8.
\]
The denominator is strictly positive since \(D(r)=(2+r^2)B_0(r)+2A(r)\). Exact differentiation gives
\[
J'(r)=\frac{-8B_0(r)(2r^4+10r^3-19r-4)}{D(r)^2}.
\tag{4}
\]
The quartic factor in (4) has exactly one positive real root: its ordered nonzero coefficients have one sign change, and the polynomial is negative at zero and tends to positive infinity. Thus \(J\) strictly increases up to \(r=\rho\) and strictly decreases thereafter, proving the sharp bound with \(t=\tau\) and optimal value \(K=J(\rho)\). Both limiting regimes are strictly smaller: \(J(0)=7/4\) and \(\lim_{r\to\infty}J(r)=5/3\).

For equality, the strictness of the preceding optimization requires \(u>0\), \(B=\rho x>0\), and \(v=2\tau x^2>0\). The equality conditions in (2) force \(|a|=|c|=x\) and \(|d|=|e|=\sqrt\tau\,x\). Equality in the three real-part bounds in (1) then forces
\[
2\arg b=\arg a+\arg c,\qquad
\arg a+\arg e=\arg b+\arg d,\qquad
\arg b+\arg e=\arg c+\arg d
\quad(\mathrm{mod}\ 2\pi).
\]
The third relation follows from the first two, and they are equivalent to the two-phase parametrization in the theorem. Conversely the displayed coefficient family makes all inequalities equalities and attains \(K\). This proves both the global bound and its complete equality classification.

## Verification
The standalone pure-Python program `checker.py` implements exact-rational polynomial arithmetic. It checks the four polynomial identities behind the \(t\)-derivative, substitution and \(r\)-derivative; enumerates the twelve distinct pair sums and their exact collision multiplicities; and isolates the unique positive quartic root in a rational interval. Separate deterministic checks evaluate the convolution identity on 2,400 integer-complex coefficient vectors, the inequality on 2,200 general complex vectors, Fourier averages on eighty finite product-group instances, and three members of the equality family. The script, executed from its packaged path, completed 4,694 checks without failure. These finite checks are independent corroborations of the exact symbolic argument, not a claim that sampling proves the universal theorem. The key identities are fully derived in (1)--(4), so no external computation is required to accept the algebraic proof.

For comparison, the five all-one coefficients give normalized fourth moment \(65/25=13/5=2.6\), strictly smaller than \(K\). The gain and its optimizer amplitudes are a genuine effect of the coupled row and column collisions.

## Relationship to prior work
Ciccone and Gonçalves study an arithmetic restriction on Fourier coefficients for a sharp extension inequality from the geometric circle to the Euclidean plane. Their result is an endpoint \(L^2\to L^6\) extension inequality with a different input measure and output operator; it does not supply the discrete two-character \(L^2\to L^4\) constant determined here. The arXiv submission dated 2022-08-19 provides the motivating connection between additive restrictions and exact Fourier extension constants.

Schmidt's analysis of unimodular polynomials supplies the standard autocorrelation representation of fourth moments and studies minimal fourth moments in long one-variable coefficient sequences. The present statement instead maximizes over unrestricted complex magnitudes on a fixed two-dimensional, five-point nonproduct support and determines all equality vectors.

The published calculation *Four-point support geometry quantizes the phase-only fourth Fourier moment* minimizes fourth moments on four-point prime-cyclic supports under equal-magnitude constraints. Its conclusion concerns an opposite optimization direction, smaller support and one cyclic coordinate. The published *Phase-only Fourier-zero spectrum of a four-point rectangle on cyclic product groups* classifies Fourier zero counts, not fourth moments. The published *Complete exact-support five-point Fourier spectrum on \(\mathbb F_3^2\)* classifies attainable numbers of Fourier zeros in a field where the distinctness hypothesis above is not satisfied along the length-three row. None of these inspected statements implies the optimal constant \(K\) or the equality set here.

## Limitations
The required distinctness of fifteen characters matters: smaller character orders or other frequency relations can introduce additional pair-sum collisions and change the sharp constant. No formula is asserted in such aliased cases. This statement does not classify all five-point support shapes or all local stationary points, and it does not claim robustness estimates for nearly maximizing coefficients. An equivalent older result expressed as a short two-dimensional \(\Lambda(4)\) constant or a filter-autocorrelation optimization remains a bibliographic risk.

## References
1. V. Ciccone and F. Gonçalves, *Sharp Fourier Extension on the Circle Under Arithmetic Constraints*, arXiv:2208.09441v1, first publicly posted 2022-08-19; primary MSC 42B10.
2. K.-U. Schmidt, *On a problem due to Littlewood concerning polynomials with unimodular coefficients*, arXiv:1302.2766v1, first posted 2013-02-12; J. Fourier Anal. Appl. 19 (2013), 457--466, primary MSC 42A05.
3. D. Oliveira e Silva, C. Thiele, and P. Zorin-Kranich, *Band-limited maximizers for a Fourier extension inequality on the circle*, arXiv:1806.06605v1, first posted 2018-06-18.
4. *Four-point support geometry quantizes the phase-only fourth Fourier moment*, published research record (2026), repository published-finding corpus/2026.
5. *Phase-only Fourier-zero spectrum of a four-point rectangle on cyclic product groups*, published research record (2026), repository published-finding corpus/2026.
6. *Complete exact-support five-point Fourier spectrum on \(\mathbb F_3^2\)*, published research record (2026), repository published-finding corpus/2026.
