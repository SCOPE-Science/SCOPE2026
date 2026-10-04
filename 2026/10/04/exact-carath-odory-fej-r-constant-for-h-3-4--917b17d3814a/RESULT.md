# Exact Carathéodory–Fejér constant for \(H=\{3,4\}\)
## Finding
For \(H=\{3,4\}\), consider the Carathéodory–Fejér extremal quantity
\[
M(H)=\sup\left\{\lambda:\exists b,c\in\mathbb R,\ 1+\lambda\cos(2\pi t)+b\cos(6\pi t)+c\cos(8\pi t)\ge0\ \text{for every }t\in\mathbb T}\right\}.
\]
Then
\[
M(\{3,4\})=2\cos\!\left(\frac{2\pi}7\right).
\]
Put \(r=\cos(2\pi/7)\). The extremizer is unique:
\[
\lambda_*=2r,\qquad b_*=\frac{3-10r}7,\qquad c_*=\frac{4(r-1)}7.
\]

## Assumptions and scope
The variable is \(t\in\mathbb T=\mathbb R/\mathbb Z\), and all coefficients are real. The normalization is the constant Fourier coefficient \(1\), while the distinguished coefficient is the first cosine coefficient. No discrete sampling is used: nonnegativity is required for every \(t\). The assertion concerns exactly the allowed higher-frequency set \(H=\{3,4\}\).

## Proof
Set
\[
r=\cos\!\left(\frac{2\pi}7\right),\qquad s=\cos\!\left(\frac{\pi}7\right).
\]
For any feasible \(T\), evaluate at \(t=1/2\) and \(t=5/14\). At these points the triples of cosine values at frequencies \(1,3,4\) are respectively
\[
(-1,-1,1),\qquad(-r,s,-s).
\]
Since \(s>0\) and both values of \(T\) are nonnegative,
\[
0\le sT(1/2)+T(5/14)=1+s-\lambda(r+s).
\]
The higher-frequency coefficients cancel. If \(a=\pi/14\), then
\[
\frac{1+s}{r+s}=\frac{2\cos^2 a}{2\cos(3a)\cos a}
=\frac{\cos a}{\cos(3a)}=2\cos(4a)=2r,
\]
because \(2\cos(4a)\cos(3a)=\cos(7a)+\cos a=\cos a\). Hence every feasible polynomial satisfies \(\lambda\le2r\).

For attainability, write \(x=\cos(2\pi t)\). Using the Chebyshev identities \(\cos(6\pi t)=4x^3-3x\) and \(\cos(8\pi t)=8x^4-8x^2+1\), direct algebra with \(8r^3+4r^2-4r-1=0\) gives
\[
1+2rx+\frac{3-10r}7(4x^3-3x)+\frac{4(r-1)}7(8x^4-8x^2+1)
=
\frac{32(1-r)}7(x+1)(x+r)^2(q-x),
\]
where
\[
q=\frac{5+2r-4r^2}4.
\]
Here \(0<r<\cos(\pi/5)=(1+\sqrt5)/4\), so \(q-1=(1+2r-4r^2)/4>0\). Thus every factor on the right is nonnegative for \(-1\le x\le1\), proving attainability.

For uniqueness, equality in the positive weighted certificate forces \(T(1/2)=T(5/14)=0\). The second zero corresponds to the interior point \(x=-r\), so the associated algebraic polynomial in \(x\) also satisfies derivative zero there. The three linear equations \(T(-1)=0\), \(T(-r)=0\), and \(T'(-r)=0\) have determinant \(7(2r^2-r-1)\ne0\), because \(0<r<1\). Hence they uniquely determine \(\lambda,b,c\), yielding the coefficients displayed above.

## Verification
The accompanying checker works in the exact cubic field \(\mathbb Q[r]/(8r^3+4r^2-4r-1)\). It verifies the factorization coefficient by coefficient, the two contact-point Chebyshev identities, the sharp upper-certificate identity, and the nonzero uniqueness determinant. Its final output is `VERIFY_OK`. The positivity step \(q>1\) and the interpretation of the correct real root \(r=\cos(2\pi/7)\) are proved analytically above rather than inferred from finite sampling.

## Relationship to prior work
Kolountzakis and Révész formulate \(M(H)\) for arbitrary \(H\subset\mathbb N\cap[2,\infty)\) and connect it to pointwise positive-definite-function extremal problems. Their inspected full text records exact values for singleton supports, singleton complements, tails, odd indices, and even indices, and records the complement duality \(M(H)M(\mathbb N_2\setminus H)=2\). The finite support \(H=\{3,4\}\) is not among those listed cases, and neither the listed cases nor the complement duality supplies its value. Krenedits and Révész later extend the general framework to locally compact Abelian groups without, in the inspected material, giving this sparse numerical case.

The older Révész duality paper is a particularly plausible source because it concerns nonnegative cosine polynomials and equivalent dual problems. Only its abstract and bibliographic record were accessible here; therefore the possibility that this exact small case occurs there or in similarly indexed older literature remains the principal literature risk.

## Limitations
The theorem evaluates one natural two-element support and does not classify \(M(H)\) for arbitrary two-element sets. The originality assessment is literature-based rather than a proof of absence: terminology changes or unindexed tables could conceal an earlier occurrence. No independent audit has been performed.

## References
1. M. N. Kolountzakis and S. Gy. Révész, *On pointwise estimates of positive definite functions with given support*, arXiv:math/0302193v1 (submitted 2003-02-17); Canadian Journal of Mathematics 58 (2006), 401–418, DOI 10.4153/CJM-2006-017-8.
2. S. Krenedits and S. Gy. Révész, *The Carathéodory-Fejér type extremal problem on locally compact Abelian groups*, arXiv:1304.0071.
3. S. Gy. Révész, *The least possible value at zero of some nonnegative cosine polynomials and equivalent dual problems*, DIMACS Technical Report 93-66; Journal of Fourier Analysis and Applications, Special Issue (1995), 485–508.
