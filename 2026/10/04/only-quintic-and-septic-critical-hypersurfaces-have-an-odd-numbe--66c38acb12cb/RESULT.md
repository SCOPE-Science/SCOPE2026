# Only quintic and septic critical hypersurfaces have an odd number of planes
## Finding
Let \(d\ge4\) and suppose \(3\nmid d\). Set
\[
n=2+\frac{(d+1)(d+2)}6.
\]
For a general degree-\(d\) hypersurface \(X_d\subset\mathbb P^n_{\mathbb C}\), the Fano scheme \(F_2(X_d)\) of planes has expected dimension
\[
3(n-2)-\binom{d+2}{2}=0,
\]
and is a finite smooth scheme. Let
\[
P_d=\deg F_2(X_d)
\]
be its length, equivalently the number of planes on a general hypersurface.

Then
\[
P_d\equiv1\pmod2
\]
if and only if
\[
d=5\quad\text{or}\quad d=7.
\]
In particular,
\[
P_5=420760566875
\]
for a general quintic hypersurface in \(\mathbb P^9\), and
\[
P_7=279101475496912988004267637
\]
for a general septic hypersurface in \(\mathbb P^{14}\); both numbers are odd. Every other admissible critical degree \(d\ge4\) gives an even plane count.

There is a real consequence. For any real degree-\(5\) hypersurface in \(\mathbb P^9_{\mathbb R}\), or real degree-\(7\) hypersurface in \(\mathbb P^{14}_{\mathbb R}\), lying in the open locus where the plane Fano scheme is zero-dimensional and transverse, at least one plane is real.

## Assumptions and scope
The ground field for the parity theorem is \(\mathbb C\). The condition \(3\nmid d\) is exactly the integrality condition for the ambient dimension in the zero-dimensional plane problem, because
\[
3(n-2)=\binom{d+2}{2}.
\]
The restriction \(d\ge4\) removes low-degree exceptional geometry and isolates the infinite critical hypersurface family. Generality places the Fano scheme in the smooth zero-dimensional regime supplied by the standard Fano-scheme transversality theorem.

The real corollary applies only to real members of that transverse open locus. It does not assert that every smooth real quintic or septic has a finite reduced plane scheme.

## Proof
Debarre and Manivel express the degree of a Fano scheme as a coefficient. For planes on a hypersurface, put
\[
Q_d(x,y,z)=\prod_{i+j+k=d}(ix+jy+kz)
\]
and
\[
\Delta(x,y,z)=(x-y)(x-z)(y-z).
\]
In the zero-dimensional case their formula becomes
\[
P_d=[x^n y^{n-1}z^{n-2}]\,\Delta(x,y,z)Q_d(x,y,z).
\]

If \(d\) is even, the factor indexed by \((i,j,k)=(d,0,0)\) is \(dx\), which is zero modulo \(2\). Hence
\[
Q_d\equiv0\pmod2,
\]
so \(P_d\) is even.

Now suppose \(d\) is odd and write
\[
d=2m+1.
\]
Because \(3\nmid d\), one has \(m\equiv0\) or \(2\pmod3\), so
\[
q=\frac{m(m+1)}6
\]
is an integer. Reduce every factor of \(Q_d\) modulo \(2\). A composition \((i,j,k)\) of the odd integer \(d\) has either exactly one odd coordinate or three odd coordinates. The number with any specified coordinate as the unique odd coordinate is
\[
A=\binom{m+2}{2},
\]
while the number with all three coordinates odd is
\[
B=\binom{m+1}{2}=3q.
\]
Therefore
\[
Q_d(x,y,z)\equiv (xyz)^A(x+y+z)^{3q}\pmod2.
\]
The critical dimension satisfies
\[
n-A=q+2.
\]
Thus
\[
P_d\equiv [x^{q+2}y^{q+1}z^q]\,\Delta(x,y,z)(x+y+z)^{3q}\pmod2.
\]
Expanding the six monomials of the Vandermonde and simplifying the resulting multinomial coefficients gives the exact integer identity
\[
[x^{q+2}y^{q+1}z^q]\,\Delta(x,y,z)(x+y+z)^{3q}
=
K_q,
\]
where
\[
K_q=\frac{2(3q)!}{q!(q+1)!(q+2)!}.
\]
Consequently
\[
P_d\equiv K_q\pmod2.
\]

It remains to determine when \(K_q\) is odd. Legendre's formula gives
\[
\nu_2(K_q)=1+\sum_{k\ge1}
\left(
\left\lfloor\frac{3q}{2^k}\right\rfloor
-\left\lfloor\frac q{2^k}\right\rfloor
-\left\lfloor\frac{q+1}{2^k}\right\rfloor
-\left\lfloor\frac{q+2}{2^k}\right\rfloor
\right).
\]
The contribution for \(2^k=2\) is always \(-1\). For a power \(M\ge4\), write \(q=aM+r\), with \(0\le r<M\). The corresponding summand is
\[
D_M=
\left\lfloor\frac{3r}{M}\right\rfloor
-\mathbf 1_{r=M-1}
-\mathbf 1_{r\ge M-2},
\]
which is always nonnegative.

For every \(q\ge3\), at least one such \(D_M\) is positive. Indeed, let \(M\) be the least power of two strictly larger than \(q\). If \(q\le M-3\), then \(q\ge M/2\), so \(D_M\ge1\). If \(q=M-2\), then \(q\ge3\) forces \(M\ge8\), and again \(D_M=1\). If \(q=M-1\), then the summand for \(2M\) equals \(1\). Hence
\[
\nu_2(K_q)\ge1\qquad(q\ge3).
\]
Directly,
\[
K_1=1,\qquad K_2=5.
\]
Therefore \(K_q\) is odd precisely for \(q=1,2\).

For admissible odd \(d\ge4\), the cases \(q=1,2\) correspond to \(m=2,3\), hence to
\[
d=5,7.
\]
All later admissible odd degrees have \(q\ge3\), completing the parity classification.

For the real statement, a zero-dimensional Fano scheme defined over \(\mathbb R\) has its non-real points paired by complex conjugation. Such pairs contribute even total degree. Hence odd complex degree forces a real closed point, i.e. a real projective plane contained in the hypersurface.

## Verification
The bundled exact-integer checker reconstructs the Debarre--Manivel coefficient directly by multiplying the linear factors of \(Q_d\) and extracting the Vandermonde coefficient. It reproduces
\[
P_4=3297280,
\]
\[
P_5=420760566875,
\]
\[
P_7=279101475496912988004267637,
\]
and verifies even parity again for critical degrees \(8,10,11\).

Separately, the checker verifies the reduction
\[
P_d\equiv K_q\pmod2
\]
for every admissible odd degree through \(d=299\), and checks the valuation argument numerically for \(1\le q\le5000\). These bounded calculations are regression evidence only. The infinite classification follows from the symbolic mod-\(2\) factorization and the uniform \(2\)-adic argument in the proof.

## Relationship to prior work
Debarre and Manivel prove the general smoothness/expected-dimension theorem for Fano schemes and give the coefficient formula used here for their degrees. Their paper also supplies numerical examples for low-degree hypersurfaces, but it does not state a parity classification for the entire critical plane family.

Hashimoto and Kadets later study monodromy of finite Fano problems. They recall the Debarre--Manivel degree machinery and prove a general divisibility statement: in a finite Fano problem the degree is divisible by the product of the defining degrees raised to the power \(r+1\). For hypersurface planes this immediately explains evenness when \(d\) is even, but it gives no parity information when \(d\) is odd. Their paper contains no occurrence of “quintic” or “septic” in this context and no classification of odd plane counts.

The closest previously recorded result for the same broad enumerative theme classifies parity of finite line counts on complete intersections. It concerns \(r=1\), has a different critical-dimension equation, and its all-odd criterion does not extend to planes: for planes, odd defining degree is usually insufficient, and only \(d=5,7\) survive.

Claim-specific searches for parity of plane Fano-scheme degrees, odd plane counts, and the exact quintic and septic counts did not locate a source stating the theorem above.

## Limitations
The theorem concerns planes on hypersurfaces, not higher-dimensional linear spaces or complete intersections of several hypersurfaces. It classifies parity only in the critical zero-dimensional family. It does not determine the full \(2\)-adic valuation of \(P_d\) in the even cases.

The real conclusion is a parity existence certificate on the transverse zero-dimensional locus; it does not estimate the number of real planes or cover special hypersurfaces with nonreduced or positive-dimensional plane schemes.

A residual literature risk remains because classical enumerative tables can contain isolated values without formulating the global parity theorem. The exact searches and the two inspected degree/monodromy sources did not reveal an equivalent classification.

## References
Olivier Debarre and Laurent Manivel, *Sur la variété des espaces linéaires contenus dans une intersection complète*, Math. Ann. 312 (1998), 549--574. Earliest public version: arXiv:alg-geom/9611033, 26 November 1996. DOI: 10.1007/s002080050235.

Sachi Hashimoto and Borys Kadets, *38406501359372282063949 and All That: Monodromy of Fano Problems*, International Mathematics Research Notices 2022, no. 5, 3349--3370; published online 9 November 2020. DOI: 10.1093/imrn/rnaa275.
