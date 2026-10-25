# Two Weil spectra for smooth plane-filling quintics over \(\mathbb F_3\)

## Finding

Let \(C/\mathbb F_3\) be any smooth plane quintic containing all thirteen rational points of \(\mathbb P^2(\mathbb F_3)\). There are exactly two \(\mathbb F_3\)-projective equivalence classes of such quintics, and their zeta functions are precisely
\[
 Z(C/\mathbb F_3,T)=\frac{L_i(T)}{(1-T)(1-3T)},\qquad i\in\{A,B\},
\]
where
\[
 L_A(T)=(1+3T+5T^2+9T^3+9T^4)^3
\]
and
\[
\begin{aligned}
L_B(T)={}&1+9T+42T^2+131T^3+308T^4+601T^5+1067T^6\\
&+1803T^7+2772T^8+3537T^9+3402T^{10}+2187T^{11}+729T^{12}.
\end{aligned}
\]
The two \(\mathbb F_3\)-Jacobians have sharply different isogeny decompositions: for class \(A\), the Jacobian is isogenous over \(\mathbb F_3\) to the cube of an ordinary simple abelian surface; for class \(B\), the Jacobian is simple over \(\mathbb F_3\). Both Jacobians are ordinary. The prior classification of the defining curves is acknowledged; the claimed contribution is the *complete finite-field Frobenius spectrum and corresponding isogeny distinction*.

## Assumptions and scope

All fields and projective equivalences in this result are over \(\mathbb F_3\) unless otherwise stated. A *plane-filling* curve contains every \(\mathbb F_3\)-point of the projective plane. Geometric smoothness is required, and all curves considered have genus \((5-1)(5-2)/2=6\). The term *two spectra* means the exhaustive list of complete zeta numerators, not that these are the only genus-six curves or all geometric forms.

For \(c_0,c_1,c_2\in\mathbb F_3\), define
\[
\begin{aligned}
U&=Y^3Z-YZ^3,\\
V&=Z^3X-ZX^3,\\
W&=X^3Y-XY^3,\\
F_{c_0,c_1,c_2}&=YU+ZV-(c_0X+c_1Y+c_2Z)W,\\
f_{c_0,c_1,c_2}(t)&=t^3+c_2t^2+c_1t+c_0.
\end{aligned}
\]
We use the projective curve \(C_{c_0,c_1,c_2}: F_{c_0,c_1,c_2}=0\). Representatives of the two classes are \((c_2,c_1,c_0)=(0,2,1)\) and \((1,0,2)\), respectively; the first has defining equation \(YU+ZV-(X+2Y)W=0\), and the second has \(YU+ZV-(2X+Z)W=0\).

## Proof

**1. Completeness and smoothness.** Homma and Kim's representation theorem, in the formulation of Homma [1, §2, Theorem 2.4], says that all degree-five plane-filling curves are represented by matrices \(M\in M_3(\mathbb F_3)\) via \((X,Y,Z)M(U,V,W)^t\); the curve is smooth precisely when the characteristic cubic of \(M\) is irreducible. The companion matrix
\[
M=\begin{pmatrix}0&0&-c_0\\1&0&-c_1\\0&1&-c_2\end{pmatrix}
\]
has characteristic polynomial \(f_{c_0,c_1,c_2}\), so the displayed representatives are smooth. Every irreducible cubic over \(\mathbb F_3\) is conjugate to the companion matrix of its characteristic polynomial.

Homma's projective-equivalence criterion [1, Corollary 2.3] identifies two matrices exactly when they differ by similarity, nonzero scalar multiplication and addition of a scalar matrix. Therefore the projective classes are indexed by orbits of monic irreducible cubics under affine changes \(t\mapsto at+b\), with \(a\in\mathbb F_3^\times\) and \(b\in\mathbb F_3\). A monic cubic over \(\mathbb F_3\) is irreducible if and only if it has no field root. Enumerating the \(27\) monic cubics produces exactly eight irreducibles, namely those with \((c_2,c_1,c_0)\) equal to
\[
(0,2,1), (0,2,2), (1,0,2), (1,1,2), (1,2,1), (2,0,1), (2,1,1), (2,2,2).
\]
Their affine-change orbits have respective sizes \(2\) and \(6\), represented by the two curves above. The irreducibility and orbit enumerations are reproduced in `check_arithmetic.py`.

**2. Exact finite-field counts.** Work with each representative and each \(n\in\{1,2,3,4,5,6\}\). On the affine patch \(Z=1\), write \(x=X/Z\) and \(y=Y/Z\). The equation is
\[
 y^4-y^2+x-x^3=(c_0x+c_1y+c_2)(x^3y-xy^3).
\]
On the line \(Z=0\), the equation is \(-(c_0X+c_1Y)(X^3Y-XY^3)=0\). The linear factor defines one of the four rational zeros of the second factor, so exactly four distinct points lie at infinity over **every** extension. Hence the precise exhaustive formula is
\[
\#C_{c_0,c_1,c_2}(\mathbb F_{3^n})=4+
\sum_{x,y\in\mathbb F_{3^n}}
\mathbf1_{\{y^4-y^2+x-x^3=(c_0x+c_1y+c_2)(x^3y-xy^3)\}}.
\]
The standalone program `verify.cpp` implements this exact sum over the six extension fields as explicit polynomial-residue representations, including all eight characteristic cubics. Their moduli (in increasing powers of \(t\)) are
\[
\begin{array}{c|l}
n&\text{monic modulus}\\\hline
1&t\\
2&t^2+1\\
3&t^3+2t^2+1\\
4&t^4+t^3+t^2+1\\
5&t^5+2t^4+1\\
6&t^6+t^5+t^4+1.
\end{array}
\]
`check_arithmetic.py` independently verifies that these moduli are irreducible by exhaustive trial division, so the quotient rings really are the indicated fields. Exact counts for the two classes, in order of degrees \(n=1,\ldots,6\), are
\[
(N_{A,n})=(13,13,55,13,208,913),\qquad
(N_{B,n})=(13,13,16,117,273,640).
\]
The same verifier obtains these counts for **every** one of the eight irreducible companion representatives, grouped into the corresponding two affine orbits.

**3. Reconstruction of all Weil coefficients.** Put \(N_{i,n}=\#C_i(\mathbb F_{3^n})\) and \(p_{i,n}=3^n+1-N_{i,n}\). If \(L_i(T)=\sum_{k=0}^{12}a_{i,k}T^k\), the first six coefficients are exactly determined by Newton's recurrence
\[
 a_{i,0}=1,\qquad ka_{i,k}=-\sum_{j=1}^{k}a_{i,k-j}p_{i,j},\quad 1\le k\le6.
\]
For a smooth genus-six curve over \(\mathbb F_3\), the Weil functional equation determines the remaining coefficients:
\[
 a_{i,k}=3^{k-6}a_{i,12-k},\qquad 7\le k\le12.
\]
The arithmetic checker independently evaluates both recurrences and obtains precisely the two boxed numerator expressions. Thus counts through degree six are **sufficient** for the full infinite-extension zeta function; no finite-experiment extrapolation is used.

**4. Jacobian factors.** The quartic \(Q(T)=1+3T+5T^2+9T^3+9T^4\) and the degree-twelve polynomial \(L_B(T)\) are irreducible over \(\mathbb Q\): their reductions modulo two are irreducible, as certified by standard finite-field Frobenius-gcd tests implemented in `check_arithmetic.py`. By the isogeny decomposition theorem for abelian varieties over finite fields, the factorizations give the asserted simple-dimensional factors. Ordinarity follows directly from the middle coefficients \(5\) of \(Q\) and \(1067\) of \(L_B\), both prime to three (and agrees with [3]).

## Verification

From the directory containing the supplied standalone files, run:

```sh
g++ -std=c++17 -O2 -Wall -Wextra -Werror verify.cpp -o verify
./verify
python3 check_arithmetic.py
```

Successful outputs terminate in `VERIFY_OK` and `ORBIT_AND_WEIL_CHECK_OK`, respectively. The former enumerates \(\sum_{n=1}^6 8\cdot 3^{2n}\) affine point tests and checks all forty-eight extension-curve counts; the latter checks all eight cubics, both projective-characteristic orbits, irreducibility of all field moduli, two Weil recurrences and the factor irreducibility tests. All operations are exact integer or residue-field arithmetic. These scripts are not a substitute for the cited complete structural classification of smooth plane-filling quintics, which is an input theorem.

## Relationship to prior work

The representation, smoothness and projective-equivalence theorems used in the proof are results of Homma and Kim [2] and Homma [1]. The fact that the curves are geometrically related, their automorphisms, and their ordinarity are addressed in Cunha [3]. The later study of plane-filling curves of higher degree [4] situates the degree-five case. None of these identified primary sources states the present explicit pair of complete \(\mathbb F_3\) Weil polynomials with its dichotomy of Jacobian isogeny factors in the material inspected. The classification into two projective classes is a deduction from [1], not claimed as independently new. A generic point-counting algorithm or geometric isomorphism statement does not by itself imply either listed polynomial without arithmetic specialization.

## Limitations

The statement concerns the finite field \(\mathbb F_3\) and *smooth degree-five plane-filling curves*, not higher degrees or arbitrary quintics. It distinguishes projective \(\mathbb F_3\)-classes; no claim is made about all abstract-curve isomorphisms or canonical polarizations. The calculations yield zeta functions and isogeny types, not explicit geometric isogeny maps. An unindexed earlier arithmetic table or special instance of a more general Frobenius formula might contain the same spectra; no comprehensive uniqueness guarantee follows from literature searching. The exact field enumeration is finite but the zeta conclusions are rigorous because the known genus-six functional equation closes the coefficient reconstruction.

## References

[1] M. Homma, *Fragments of plane filling curves of degree \(q+2\) over the finite field of \(q\) elements, and of affine-plane filling curves of degree \(q+1\)* (first public 2019-06-01), arXiv:1906.00164, especially §2, Corollary 2.3 and Theorem 2.4.

[2] M. Homma and S. J. Kim, *Nonsingular plane filling curves of minimum degree over a finite field*, arXiv:0903.1918 (2009).

[3] G. Duran Cunha, *Curves containing all points of a finite projective Galois plane*, arXiv:1805.07345 (2018).

[4] S. Asgarli and D. Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072 (2023).
