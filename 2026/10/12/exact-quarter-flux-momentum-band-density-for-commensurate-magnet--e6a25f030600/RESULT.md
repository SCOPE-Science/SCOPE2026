# Exact quarter-flux momentum-band density for commensurate magnetic ring chains
## Finding
Consider the tight magnetic ring chain with preferred-orientation coupling studied by Baradaran, Exner, and Lipovský. Normalize the ring circumference by \(\ell_2+\ell_3=2\pi\), take quarter flux \(A\equiv 1/4\pmod{1/2}\), and assume
\[
\frac{\ell_2}{\ell_3}=\frac{p}{q},\qquad p,q\in\mathbb N,\qquad \gcd(p,q)=1.
\]
Let \(P_{p,q}\) denote the high-energy momentum-band density \(P_{\sigma(H)}\) defined by the limiting relative measure of spectral momenta. Then
\[
P_{p,q}=\frac34-\frac{1}{4(p+q)}
\left(\frac{\mathbf 1_{p\text{ odd}}}{p}+\frac{\mathbf 1_{q\text{ odd}}}{q}\right).
\]
Equivalently,
\[
P_{p,q}=
\begin{cases}
\displaystyle \frac34-\frac1{4pq},&p,q\text{ both odd},\\[6pt]
\displaystyle \frac34-\frac1{4r(p+q)},&\text{exactly one of }p,q\text{ is odd, denoted }r.
\end{cases}
\]
(The coprimality assumption excludes the case where both are even.) In particular every finite commensurate ratio has density strictly below \(3/4\), while rational approximants with large coprime numerator and denominator approach \(3/4\) with the explicit defect above. The symmetric case \(p=q=1\) gives \(P_{1,1}=1/2\), agreeing with the source's separate symmetric-chain formula at quarter flux.

## Assumptions and scope
The graph, coupling, gauge convention, and momentum-band density are those of arXiv:2201.01502v1. The claim concerns the tight-chain limit \(\ell_1=0\), positive high-energy momentum, and the distinguished quarter-flux class \(A\equiv 1/4\pmod{1/2}\). Flat bands and isolated zeros have zero momentum measure and do not change the density. The source reduces the large-momentum band condition to equation (34), with relative error \(O(k^{-2})\); the argument below computes the density of that limiting condition exactly. Since its leading trigonometric factor is periodic with finitely many zeros per period, the lower-order error does not alter the limiting relative measure: outside arbitrarily small neighborhoods of those zeros the sign is eventually stable, and those neighborhoods have arbitrarily small relative measure.

## Proof
At quarter flux,
\[
\sin\!\bigl(\pi(k-\tfrac14)\bigr)\sin\!\bigl(\pi(k+\tfrac14)\bigr)
=\sin^2(\pi k)-\frac12=-\frac12\cos(2\pi k).
\]
Write \(s=p+q\), so that
\[
\ell_2=\frac{2\pi p}{s},\qquad \ell_3=\frac{2\pi q}{s},
\]
and put \(t=2\pi k/s\). Equation (34) is therefore, away from its zero set, equivalent to
\[
-\cos(st)\sin(pt)\sin(qt)>0.
\]
This sign function has period \(\pi\). Set \(u=t/\pi\in[0,1)\), and define
\[
x=\{su\},\qquad y=\{pu\}.
\]
For points away from the zero set,
\[
\operatorname{sgn}\sin(\pi n u)=(-1)^{\lfloor nu\rfloor},\qquad
\operatorname{sgn}\cos(\pi s u)=(-1)^{\lfloor su+1/2\rfloor}.
\]
Because \(q=s-p\), one has
\[
\lfloor qu\rfloor=\lfloor su\rfloor-\lfloor pu\rfloor-\mathbf 1_{y>x}.
\]
Consequently the band sign is positive exactly when
\[
(x<1/2\text{ and }y>x)\quad\text{or}\quad(x\ge1/2\text{ and }y\le x).
\]

Partition \([0,1)\) into the \(s\) cells \(u=(j+x)/s\), \(0\le j<s\). Since \(\gcd(p,s)=1\), the residue \(r=pj\pmod s\) runs once through \(0,1,\ldots,s-1\). In a cell,
\[
y=\left\{\frac{r+px}{s}\right\},
\]
and, except at finitely many boundary values of \(x\),
\[
y>x\quad\Longleftrightarrow\quad qx<r<s-px.
\]
Hence the number of cells satisfying \(y>x\) at a given \(x\) is
\[
N(x)=s-1-\lfloor px\rfloor-\lfloor qx\rfloor.
\]
Averaging the two sign alternatives gives
\[
P_{p,q}=\frac1s\left(\int_0^{1/2}N(x)\,dx+\int_{1/2}^1(s-N(x))\,dx\right)
=\frac12-\frac{D_p+D_q}{s},
\]
where
\[
D_n=\int_0^{1/2}\lfloor nx\rfloor\,dx-\int_{1/2}^1\lfloor nx\rfloor\,dx.
\]
Direct integration over the \(n\) equal subintervals yields
\[
D_n=
\begin{cases}
-n/4,&n\text{ even},\\[3pt]
-n/4+1/(4n),&n\text{ odd}.
\end{cases}
\]
Substitution proves the stated formula.

## Verification
The standalone checker `verify.py` constructs the exact rational zero partition of one period using the zeros of \(\cos(\pi s u)\), \(\sin(\pi p u)\), and \(\sin(\pi q u)\). It determines the sign on each open interval by exact floor arithmetic and sums interval lengths as rational numbers. For every coprime pair \(1\le p,q\le40\), the resulting exact fraction equals the closed formula. It also checks the floor-integral identity for \(1\le n\le100\). No numerical quadrature is used in the certificate.

## Relationship to prior work
Baradaran--Exner--Lipovský derive the limiting sign condition in their equation (34), state that for commensurate \(\ell_2/\ell_3\in\mathbb Q\) they were unable to find the momentum-band probability in closed form, and plot the quarter-flux case numerically in their Fig. 8. They further note that large coprime rational approximants give values near \(0.749\), close to the incommensurate quarter-flux value \(3/4\). The formula above resolves exactly that distinguished commensurate slice and explains the arithmetic dips and convergence rate. The earlier non-magnetic chain analysis gives a different sign condition and does not imply this magnetic quarter-flux formula. Band--Berkolaiko universality concerns generic edge lengths and therefore does not cover these rationally dependent lengths.

## Limitations
The formula is for the quarter-flux class only; no closed form for arbitrary magnetic flux is claimed. It addresses the limiting momentum-band density, not finite-energy band widths or the detailed location of individual bands. The proof uses the source's high-energy reduction to equation (34), independently checking the exact sign-measure calculation that follows from it. No claim is made about rational ratios with a different normalization of the flux beyond the source's stated periodicity.

## References
1. M. Baradaran, P. Exner, J. Lipovský, *Magnetic ring chains with vertex coupling of a preferred orientation*, arXiv:2201.01502v1; J. Phys. A: Math. Theor. 55 (2022), DOI:10.1088/1751-8121/ac820b.
2. M. Baradaran, P. Exner, M. Tater, *Spectrum of periodic chain graphs with time-reversal non-invariant vertex coupling*, arXiv:2012.14344v1; Ann. Phys. 443 (2022), 168992.
3. R. Band, G. Berkolaiko, *Universality of the momentum band density of periodic networks*, arXiv:1304.6028v1; Phys. Rev. Lett. 111 (2013), 130404.
