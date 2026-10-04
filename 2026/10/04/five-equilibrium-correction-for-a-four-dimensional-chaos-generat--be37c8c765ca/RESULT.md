# Five-equilibrium correction for a four-dimensional chaos generator
## Finding
For the autonomous system
\[
\dot x=-12x+yz+\frac{1}{20}w^2-\frac{2}{5},\qquad
\dot y=8y-xz+w|y|,
\]
\[
\dot z=xy-45z,\qquad
\dot w=w-10z,
\]
the real equilibrium set consists of exactly five points. One is
\[
E_0=\left(-\frac{1}{30},0,0,0\right).
\]
For the other four, let
\[
P(r)=r^5+9r^4-720r^3-492480r^2+113400r+1166400.
\]
This polynomial has exactly three real roots. They lie respectively in
\[
(-1.43,-1.42),\qquad (1.65,1.66),\qquad (78.92,78.93).
\]
Only the first and third are admissible. If \(r\) is one of those two roots and
\[
s=\frac{r^2-360}{10r}>0,
\]
then the two equilibria attached to \(r\) are
\[
E_{r,\varepsilon}=\left(r,\varepsilon s,\frac{\varepsilon rs}{45},\frac{2\varepsilon rs}{9}\right),
\qquad \varepsilon\in\{-1,1}.
\]
Numerically, the four nonzero equilibria are approximately
\[
(-1.4295404143,\pm25.0399646372,\mp0.7954586982,\mp7.9545869823)
\]
and
\[
(78.9241446448,\pm7.4362802845,\pm13.0422680176,\pm130.4226801759).
\]
At \(E_0\), the characteristic polynomial is
\[
(\lambda+12)(\lambda-1)\left(\lambda^2+37\lambda-\frac{323999}{900}\right),
\]
so the spectrum is
\[
-12,\quad 1,\quad -\frac{37}{2}\pm\frac{\sqrt{158006}}{15}.
\]
The two latter values are approximately \(7.9999790356\) and \(-44.9999790356\). Thus \(E_0\) has two unstable and two stable linear directions.

## Assumptions and scope
The statement concerns the real equilibria of the printed ordinary differential equation at the parameter vector used in the source's dynamical and encryption examples. No claim is made about the security of the image-encryption construction, about existence of a particular attractor, or about basin connectivity. The vector field is continuously differentiable at \(E_0\): although \(|y|\) is nonsmooth at \(y=0\), the product \(w|y|\) has derivative zero at \((y,w)=(0,0)\).

## Proof
At an equilibrium, the last two equations give
\[
z=\frac{xy}{45},\qquad w=10z=\frac{2xy}{9}.
\]
Substituting these into the second equation yields
\[
y\left(8-\frac{x^2}{45}+\frac{2x|y|}{9}\right)=0.
\]
If \(y=0\), then \(z=w=0\), and the first equation gives \(x=-1/30\), producing \(E_0\).

Now suppose \(y\ne0\), and write \(s=|y|>0\). Then \(x\ne0\) and
\[
s=\frac{x^2-360}{10x}.
\]
The first equilibrium equation becomes
\[
-12x-\frac{2}{5}+\frac{xs^2}{45}+\frac{x^2s^2}{405}=0.
\]
Substituting the expression for \(s\), clearing the nonzero denominator \(40500x\), and expanding gives
\[
P(x)=x^5+9x^4-720x^3-492480x^2+113400x+1166400=0.
\]
An exact Sturm sequence for \(P\) has variation counts \(4\) at \(-\infty\) and \(1\) at \(+\infty\), hence \(P\) has exactly three real roots. The variation drops by one on each of the rational intervals \((-143/100,-71/50)\), \((33/20,83/50)\), and \((1973/25,7893/100)\), so each interval contains exactly one real root and there are no others.

The condition \(s>0\) is equivalent to
\[
\frac{x^2-360}{x}>0.
\]
Since \(18^2<360<19^2\), the negative root near \(-1.43\) is admissible, the positive root near \(1.66\) is not, and the large positive root near \(78.92\) is admissible. Each admissible root gives exactly two choices \(y=\pm s\), and then \(z\) and \(w\) are forced by the last two equilibrium equations. Together with \(E_0\), this proves that there are exactly five equilibria.

For the linearization at \(E_0\), direct differentiation gives the block-triangular Jacobian used in the source, and therefore
\[
\det(\lambda I-J(E_0))=(\lambda+12)(\lambda-1)\left(\lambda^2+37\lambda-\frac{323999}{900}\right).
\]
The quadratic factor has negative constant term, hence one positive and one negative root. Its discriminant is \(2528096/900\), giving the exact pair \(-37/2\pm\sqrt{158006}/15\).

## Verification
The accompanying `verify.py` uses only the Python standard library. It reconstructs the elimination polynomial with exact rational arithmetic, builds the Sturm sequence by exact Euclidean division, checks the global real-root count and the three isolating intervals, verifies which roots satisfy the sign constraint \(s>0\), reconstructs all four nonzero equilibria, checks the printed vector-field residuals numerically, and verifies the exact characteristic polynomial at \(E_0\). Running `python3 verify.py` returns `VERIFY_OK`.

## Relationship to prior work
Zhao, Wang and Zhang introduced this exact four-dimensional system and, at the same parameter vector, stated that the system has only the displayed equilibrium \(E_0\). Their printed characteristic polynomial is also incompatible with their listed eigenvalues: the polynomial has no zero root and instead gives a second positive eigenvalue near \(8\). The present result completes the real equilibrium calculation at that published parameter vector and corrects the local spectrum of \(E_0\). Exact-equation, DOI, title, and semantic searches located the introducing article and downstream citations, but no published source found in those searches gave the five-equilibrium classification or the corrected spectrum.

## Limitations
This is an equilibrium and local-linearization result. It does not establish whether the plotted chaotic or hyperchaotic set exists for the reported numerical settings, does not determine whether any such attractor is hidden or self-excited, does not compute the basins of the four additional equilibria, and does not assess the cryptographic security claims. A non-indexed correction or independent analysis could exist despite the searches described above.

## References
1. J. Zhao, S. Wang, and L. Zhang, “Block Image Encryption Algorithm Based on Novel Chaos and DNA Encoding,” *Information* 14 (2023), 150. DOI: 10.3390/info14030150. The source gives the vector field, parameter vector, asserted equilibrium calculation, Jacobian, and characteristic polynomial in its Section 2.1.
2. MSC2020, 37C25, “Fixed points and periodic points of dynamical systems; fixed-point index theory; local dynamics.”
