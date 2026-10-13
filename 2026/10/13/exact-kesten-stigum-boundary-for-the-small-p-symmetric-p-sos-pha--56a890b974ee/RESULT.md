# Exact Kesten–Stigum boundary for the small-p symmetric p-SOS phase
## Finding
For the three-state \(p\)-SOS model on the binary Cayley tree, consider the symmetric translation-invariant splitting Gibbs measure \(\mu_1\) at \(p=1/10\). In the antiferromagnetic regime \(\theta>1\), the Kesten--Stigum sufficient non-extremality condition has the exact boundary
\[
\theta_{\mathrm{KS}}=r_*^5=6.88189437635365161332786339775379998579\ldots,
\]
where \(r_*\) is the unique real root greater than \(1\) of
\[
P(r)=16r^{40}-192r^{31}-192r^{30}-112r^{28}-336r^{27}-336r^{26}-336r^{25}-72r^{22}-144r^{21}-72r^{20}+32r^{19}+128r^{18}+192r^{17}+188r^{16}+72r^{15}-60r^{14}-48r^{13}+36r^{12}+72r^{11}+8r^{10}-20r^9-40r^8-48r^7-36r^6-12r^5+r^4+4r^3+6r^2+4r+1.
\]
It is isolated by \(1.47075929<r_*<1.47075930\). The Kesten--Stigum condition fails for \(1<\theta\le\theta_{\mathrm{KS}}\) and holds for \(\theta>\theta_{\mathrm{KS}}\). The public preprint reports instead an anti-ferromagnetic numerical Kesten--Stigum threshold near \(1523.4\); the calculation below follows from its displayed boundary-law and transition-matrix formulas.

## Assumptions and scope
The tree has order \(2\), the spin set is \(\{0,1,2\}\), \(p=1/10\), and \(\theta>1\). The boundary law is the source's symmetric branch \((x,y)=(1,y_1)\). The result classifies only when the Kesten--Stigum sufficient non-extremality inequality \(2\lambda_{\max}^2>1\) holds. Failure of that inequality is not asserted to imply extremality, and no claim is made about the source's separate Martinelli--Sinclair--Weitz sufficient extremality computation.

## Proof
Put \(r=\theta^{1/5}>1\). The source's cubic boundary-law equation becomes
\[
F(r,y)=r^5y^3-y^2+(r+1)y-2r^5=0.
\]
Its derivative is \(F_y=3r^5y^2-2y+r+1\), whose discriminant as a quadratic in \(y\) is \(4-12r^5(r+1)<0\). Hence \(F(r,\cdot)\) is strictly increasing. Since \(F(r,1)=r-r^5<0\), the physical root is unique and satisfies \(y(r)>1\).

For this branch the two nontrivial transition eigenvalues printed in the source become
\[
\lambda_1=\frac{(r+1-2r^{10})y^2}{D},\qquad
\lambda_2=\frac{1-r}{r+r^5y^2+1},
\]
with \(D=r^5y^4+(r+2r^{10}+1)y^2+2r^5(r+1)>0\). For \(r>1\), \(\lambda_1<0\). Also \(y>1\) gives
\[
|\lambda_2|<\frac{r-1}{r^5}\le\frac{256}{3125}<\frac1{\sqrt2},
\]
where the elementary maximum occurs at \(r=5/4\). Thus only \(\lambda_1\) can trigger Kesten--Stigum.

Set \(N=(r+1-2r^{10})y^2\) and \(H(r,y)=2N^2-D^2\). Then \(2\lambda_1^2>1\) is equivalent to \(H>0\). Exact elimination gives
\[
\operatorname{Res}_y(F,H)=4r^{20}(r-1)^4Q(r)^4P(r),
\]
where \(Q(r)=1+2r+2r^2+\cdots+2r^9>0\) for \(r>1\). A Sturm count gives exactly one zero of \(P\) on \((1,\infty)\), and exactly one zero in \((1.47075929,1.47075930)\).

At \(r=1\), the physical root is \(y=1\) and \(H(1,1)<0\). At \(r=2\), exact rational evaluation gives \(249/200<y(2)<623/500\). On this interval,
\[
H(2,y)=-1024y^8-131264y^6+4145161y^4-787584y^2-36864>8202325.
\]
The physical root \(y(r)\) is continuous because \(F_y>0\). Any zero of \(H(r,y(r))\) with \(r>1\) must therefore be the single root \(r_*\) of \(P\), and the sign changes from negative to positive there.

## Verification
The standalone file `verify.py` reconstructs the resultant exactly, uses an exact Sturm root count for \(P\), checks the rational isolation interval and the \(r=2\) sign certificate, and verifies the uniform \(\lambda_2\) bound. Its successful output begins `VERIFY_OK resultant=exact roots_gt1=1` and prints the certified decimal values of \(r_*\) and \(\theta_{\mathrm{KS}}\). Numerical decimals are consequences of the exact certificates, not substitutes for them.

## Relationship to prior work
Jahnel and Rozikov derive the boundary-law cubic, transition matrix, and its two nontrivial eigenvalue formulas, then apply Kesten--Stigum. For \(p=0.1\) their public preprint states from computer analysis that the anti-ferromagnetic Kesten--Stigum condition first holds beyond a numerical value near \(1523.4\). The calculation above uses those displayed formulas but gives a unique exact algebraic crossing near \(6.8819\). The earlier \(p=1\) SOS work of Külske and Rozikov treats a different interaction exponent and does not imply the \(p=0.1\) boundary.

Targeted searches for the source identifier, the reported value \(1523.4\), the corrected decimal, the degree-40 polynomial coefficients, and Kesten--Stigum aliases found no published correction or implication-equivalent statement. A publisher-final-text revision could not be inspected separately from the lawful public preprint; that version difference remains a literature risk.

## Limitations
The result does not determine the true extremality threshold. Kesten--Stigum is a sufficient condition for non-extremality, not a converse. The finding does not reassess the source's separate sufficient extremality calculation, the ferromagnetic regime \(0<\theta<1\), the other TISGMs, or other values of \(p\). The exact polynomial is an elimination invariant for this \(p=1/10\) branch and is not claimed to be irreducible.

## References
1. B. Jahnel and U. Rozikov, *Three-state p-SOS models on binary Cayley trees*, arXiv:2402.09839v1; WIAS Preprint 3089; J. Stat. Mech. Theory Exp. 2024, 113202, DOI 10.1088/1742-5468/ad8749.
2. C. Külske and U. A. Rozikov, *Extremality of translation-invariant phases for a finite-state SOS-model on the binary tree*, arXiv:1411.5886v1; J. Stat. Phys. 160 (2015), 659--680, DOI 10.1007/s10955-015-1279-9.
3. H. Kesten and B. P. Stigum, *Additional limit theorems for indecomposable multidimensional Galton--Watson processes*, Ann. Math. Statist. 37 (1966), 1463--1481.
