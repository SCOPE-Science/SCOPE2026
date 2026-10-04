# Universal index-two hyperbolicity in a four-dimensional Sprott-B feedback flow
## Finding
Consider the smooth autonomous system introduced by Huang, Zhang, Xiang, and Wang,
\[
\dot x=a(y-x),\qquad
\dot y=xz+w,\qquad
\dot z=b-xy,\qquad
\dot w=yz-cw,
\]
with \(a>0\), \(b>0\), and \(c>0\). Its two equilibria
\[
E_\pm=(\pm\sqrt b,\pm\sqrt b,0,0)
\]
are hyperbolic for every positive parameter triple, and each has exactly two eigenvalues in the open right half-plane and two in the open left half-plane. Consequently, the unstable dimension is identically two throughout the full positive parameter octant. In particular, no local equilibrium bifurcation can occur while \(a,b,c\) remain positive; the parameter-dependent periodic and chaotic windows reported for this system must therefore be organized by non-equilibrium dynamics rather than by a change of equilibrium stability.

## Assumptions and scope
The claim concerns the printed four-dimensional ordinary differential equation and the open parameter domain \(a,b,c>0\). It is a local spectral statement about the two finite equilibria. It does not classify periodic or chaotic invariant sets, prove the existence of the numerically reported attractors, or determine their basins.

The source labels some portions of a numerical dynamical map as “stable” when the computed maximum Lyapunov exponent is negative. The theorem above does not by itself diagnose those pixels. It does rule out interpreting any positive-parameter pixel as attraction to an asymptotically stable equilibrium. For a regular non-equilibrium invariant trajectory of an autonomous flow, the flow direction supplies the usual zero Lyapunov exponent, so a genuinely asymptotic non-equilibrium recurrent state is also not characterized by a strictly negative largest exponent.

## Proof
At an equilibrium, \(\dot x=0\) gives \(y=x\). Then \(\dot z=0\) gives \(x^2=b\), so \(x=y=\pm\sqrt b\). The remaining equations give \(z=w=0\). Thus there are exactly the two equilibria \(E_\pm\).

Writing \(s=\pm\sqrt b\), the Jacobian at either equilibrium is
\[
J_s=
\begin{pmatrix}
-a&a&0&0\\
0&0&s&1\\
-s&-s&0&0\\
0&0&s&-c
\end{pmatrix}.
\]
Using \(s^2=b\), direct expansion gives the same characteristic polynomial at both equilibria:
\[
p(\lambda)=\lambda^4+A_1\lambda^3+A_2\lambda^2+A_3\lambda+A_4,
\]
where
\[
A_1=a+c,\qquad
A_2=ac+b,\qquad
A_3=b(2a+c+1),\qquad
A_4=2ab(c+1).
\]
All four coefficients are positive. The third quartic Hurwitz determinant is
\[
\Delta_3=A_1A_2A_3-A_3^2-A_1^2A_4,
\]
and exact simplification yields
\[
\Delta_3
=-b\!\left(
2a^3+2a^2b+a^2c^2+3a^2c+abc+3ab+ac^3+ac^2+bc+b
\right)<0.
\]

There are no eigenvalues on the imaginary axis. Indeed, \(\lambda=0\) is excluded because \(A_4>0\). If \(\lambda=i\omega\) with \(\omega\ne0\), the imaginary and real parts of \(p(i\omega)=0\) give
\[
A_3=A_1\omega^2,\qquad
\omega^4-A_2\omega^2+A_4=0.
\]
Eliminating \(\omega^2\) forces \(\Delta_3=0\), contradicting the strict negative formula above. Hence both equilibria are hyperbolic everywhere in the connected domain \(a,b,c>0\), and their number of right-half-plane eigenvalues is constant on that domain.

It remains to determine that constant. At the positive sample \((a,b,c)=(1,1,2)\),
\[
(A_1,A_2,A_3,A_4)=(3,3,5,6),
\]
and
\[
\Delta_2=A_1A_2-A_3=4,\qquad
\Delta_3=-34.
\]
The first column of the quartic Routh array has signs
\[
+,\ +,\ +,\ -,\ +,
\]
so there are exactly two roots in the open right half-plane. Hyperbolicity and connectedness therefore imply exactly two right-half-plane and two left-half-plane roots for every \(a,b,c>0\).

## Verification
The bundled `verify.py` uses only the Python standard library. It constructs the polynomial matrix \(\lambda I-J_s\), expands its determinant exactly, reduces \(s^2=b\), verifies the four displayed coefficients, expands \(\Delta_3\), and checks the exact Routh signs at \((a,b,c)=(1,1,2)\). Running it prints `VERIFY_OK`.

The proof is symbolic and parameter-uniform. No finite trajectory integration or floating-point eigenvalue calculation is used to establish the theorem.

## Relationship to prior work
Huang, Zhang, Xiang, and Wang introduced this system and stated, using the Routh–Hurwitz criterion, that its two equilibria are unstable for positive parameters. They also gave one numerical saddle-focus calculation at \(a=6\), \(b=11\), \(c=5\) and then studied parameter-dependent periodic and chaotic windows numerically. The result here strengthens that local statement to a complete spectral-index classification on the entire positive octant: both equilibria are everywhere hyperbolic of unstable dimension two, so the positive parameter family contains no equilibrium stability crossing at all.

Statement-level literature and overlap searches using the DOI, article title, the printed vector field, “unstable index,” “Routh–Hurwitz,” and “no equilibrium bifurcation” returned no checked same-system source implying this parameter-uniform index theorem. The closest retrieved mathematical results concern different vector fields and do not subsume the claim.

## Limitations
The source already proves the weaker fact that both equilibria are unstable for positive parameters, so originality is specifically in the exact hyperbolicity and unstable-index classification and its no-equilibrium-bifurcation consequence, not in rediscovering instability. The searches performed cannot prove global novelty, and later or difficult-to-index literature could contain an equivalent Routh-index calculation.

The statement does not identify the global bifurcations responsible for the source’s reported periodic and chaotic windows. It also does not certify any numerical Lyapunov exponent, circuit experiment, or attractor.

## References
1. L. Huang, Z. Zhang, J. Xiang, and S. Wang, “A New 4D Chaotic System with Two-Wing, Four-Wing, and Coexisting Attractors and Its Circuit Simulation,” *Complexity* 2019, Article 5803506. DOI: 10.1155/2019/5803506. First published 29 October 2019.
2. MSC2020, 37C25: fixed points and periodic points of dynamical systems; fixed-point index theory; local dynamics.
