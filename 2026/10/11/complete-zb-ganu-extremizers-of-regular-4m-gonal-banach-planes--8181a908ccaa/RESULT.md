# Complete Zbăganu extremizers of regular \(4m\)-gonal Banach planes
## Finding
For every integer \(m\ge1\), let \(X_m=(\mathbb R^2,N_m)\) have as unit ball the regular \(4m\)-gon whose vertices are
\[
v_k=\left(\cos\frac{k\pi}{2m},\sin\frac{k\pi}{2m}\right),
\qquad k=0,\ldots,4m-1.
\]
Write
\[
C_Z(X_m)=\sup_{(x,y)\ne(0,0)}
\frac{N_m(x+y)N_m(x-y)}{N_m(x)^2+N_m(y)^2}.
\]
Then a pair \((x,y)\) attains \(C_Z(X_m)\) if and only if there exist nonzero real numbers \(a,b\), an index \(k\) modulo \(4m\), and an integer \(j\in\{0,\ldots,m-1\}\) such that
\[
x=a\,v_k,\qquad y=b\,v_{k+m},
\qquad
\left|\frac ba\right|
=\tan\frac{(2j+1)\pi}{4m}.
\]
Consequently
\[
C_Z(X_m)=\sec^2\frac{\pi}{4m}.
\]
Thus every Zbăganu extremizer consists of two Euclidean-orthogonal vertex rays, and the allowed length ratios form exactly the finite odd-half-angle ladder above.

## Assumptions and scope
The scalar field is real. For an integer \(m\ge1\), the unit ball is the Euclidean regular \(4m\)-gon with circumradius \(1\) and one vertex at \((1,0)\). The Euclidean norm is denoted by \(E(z)=|z|_2\).

The Zbăganu constant is
\[
C_Z(X_m)=\sup_{(x,y)\ne(0,0)}
\frac{N_m(x+y)N_m(x-y)}{N_m(x)^2+N_m(y)^2}.
\]
The theorem classifies every pair attaining this supremum.

## Proof
Set
\[
c_m=\cos\frac{\pi}{4m}.
\]
For the regular \(4m\)-gon, elementary radial geometry gives, for every \(z\in\mathbb R^2\),
\[
E(z)\le N_m(z)\le \frac{E(z)}{c_m}.
\]
For nonzero \(z\), equality in the left inequality holds exactly on the vertex rays. Equality in the right inequality holds exactly on the outward-normal rays through the edge midpoints, whose angles are
\[
\frac{(2\ell+1)\pi}{4m},
\qquad \ell\in\mathbb Z.
\]

For any \((x,y)\ne(0,0)\),
\[
\frac{N_m(x+y)N_m(x-y)}{N_m(x)^2+N_m(y)^2}
\le
\frac{E(x+y)E(x-y)}
{c_m^2\bigl(E(x)^2+E(y)^2\bigr)}.
\]
The Euclidean identity
\[
E(x+y)^2E(x-y)^2
=
\bigl(E(x)^2+E(y)^2\bigr)^2
-4\langle x,y\rangle^2
\]
then gives
\[
\frac{N_m(x+y)N_m(x-y)}{N_m(x)^2+N_m(y)^2}
\le \frac1{c_m^2}.
\]

Suppose equality holds. Since the extremal value is positive, neither \(x+y\) nor \(x-y\) is zero. Equality in the norm-comparison chain forces all of the following:

1. \(x\) and \(y\) lie on vertex rays;
2. \(\langle x,y\rangle=0\);
3. both \(x+y\) and \(x-y\) lie on edge-normal rays.

The vertex directions occur at multiples of \(\pi/(2m)\). Hence the first two conditions imply, after a common dihedral symmetry and harmless signs,
\[
x=a(1,0),\qquad y=b(0,1),
\qquad a,b\ne0.
\]
The direction of \(x+y\) is an edge-normal direction exactly when
\[
\left|\frac ba\right|
=
\tan\frac{(2j+1)\pi}{4m}
\]
for some \(j\in\{0,\ldots,m-1\}\). For these same ratios, \(x-y\) is automatically on an edge-normal ray. Therefore the displayed condition is necessary.

Conversely, if
\[
x=a\,v_k,\qquad y=b\,v_{k+m},
\qquad
\left|\frac ba\right|
=
\tan\frac{(2j+1)\pi}{4m},
\]
then \(x\) and \(y\) are Euclidean-orthogonal vertex-ray vectors, while \(x+y\) and \(x-y\) are edge-normal vectors. Every inequality in the chain above is therefore an equality, so the pair attains
\[
C_Z(X_m)=\frac1{c_m^2}
=\sec^2\frac{\pi}{4m}.
\]
This proves both the value and the complete equality classification.

## Verification
The proof uses only two exact ingredients: the radial comparison between a regular \(4m\)-gon and its Euclidean circumcircle, and the Euclidean parallelogram-product identity.

As a boundary check, \(m=1\) gives the square plane:
\[
C_Z(X_1)=2,
\]
and the only allowed ratio is \(1\). For \(m=2\), the regular octagon gives
\[
C_Z(X_2)=4-2\sqrt2,
\]
with the two reciprocal ratios
\[
\tan\frac{\pi}{8},\qquad \tan\frac{3\pi}{8}.
\]
These agree with direct substitution into the defining norm.

Finite numerical sampling was used only as a stress test for small values of \(m\); it is not part of the proof.

## Relationship to prior work
Llorens-Fuster, Mazcuñán-Navarro, and Reich study the Zbăganu constant as a Banach-space geometric constant, relate it to normal structure and fixed-point theory, and calculate exact values in several spaces.

Mizuguchi and Saito prove a broad theorem for real two-dimensional absolute normalized norms: when the norm function dominates its Euclidean counterpart, the Zbăganu constant equals the square of the maximal norm-to-Euclidean ratio. Applied to a regular \(4m\)-gon, that theorem already implies the numerical value
\[
C_Z(X_m)=\sec^2\frac{\pi}{4m}.
\]
The new assertion here is the complete equality set: the inspected full text does not classify all pairs attaining the constant for regular polygons, nor does it state the discrete length-ratio ladder.

## Limitations
The theorem is restricted to real regular polygons with a number of sides divisible by \(4\). It does not classify Zbăganu extremizers for arbitrary centrally symmetric polygons or arbitrary absolute normalized norms.

The numerical value is already implied by the general 2012 absolute-normalized-norm theorem; originality is claimed only for the complete regular-polygon extremizer classification. A differently phrased equality-set result outside the inspected sources remains a bibliographic risk.

## References
1. E. Llorens-Fuster, E. M. Mazcuñán-Navarro, and S. Reich, “The Ptolemy and Zbăganu constants of normed spaces,” *Nonlinear Analysis* 72 (2010), 3984--3993, DOI 10.1016/j.na.2010.01.030; published 2010-06-01.
2. H. Mizuguchi and K.-S. Saito, “The Zbăganu constant of absolute normalized spaces,” *RIMS Kôkyûroku* 1819 (2012), 103--110.
