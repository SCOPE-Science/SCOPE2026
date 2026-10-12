# Fixed-space spectrum and five element orbits of the four-dimensional model filiform Lie algebra
## Finding
Let \(q\) be an odd prime power and let \(\mathfrak f_4(q)\) be the four-dimensional Lie algebra over \(\mathbb F_q\) with basis \(e_1,e_2,e_3,e_4\), brackets \([e_1,e_2]=e_3\), \([e_1,e_3]=e_4\), and all other basic brackets zero. If \(N_j(q)\) denotes the number of \(\mathbb F_q\)-linear Lie-algebra automorphisms whose fixed subspace has dimension \(j\), then
\[
N_0=(q-3)^2q^5,\qquad N_1=q^3(4q^3-8q^2-3q+1),
\]
\[
N_2=3q^4-2q^3-q^2+q,\qquad N_3=q^3+q^2-q-1,\qquad N_4=1.
\]
These are all possible fixed-space dimensions and the five numbers sum to \((q-1)^2q^5=|\operatorname{Aut}(\mathfrak f_4(q))|\). Their Burnside average is exactly \(5\). Equivalently, the automorphism group has exactly five element-orbits, namely \(\{0\}\), \(Z\setminus\{0\}\), \([\mathfrak f_4,\mathfrak f_4]\setminus Z\), \(C_{\mathfrak f_4}([\mathfrak f_4,\mathfrak f_4])\setminus[\mathfrak f_4,\mathfrak f_4]\), and \(\mathfrak f_4\setminus C_{\mathfrak f_4}([\mathfrak f_4,\mathfrak f_4])\), where \(Z=Z(\mathfrak f_4)\).

## Assumptions and scope
The field is an arbitrary finite field \(\mathbb F_q\) of odd characteristic. The Lie algebra is the standard four-dimensional model filiform algebra
\[
\mathfrak f_4(q)=\langle e_1,e_2,e_3,e_4\mid [e_1,e_2]=e_3,\ [e_1,e_3]=e_4\rangle.
\]
No assertion is made here for characteristic \(2\). Write \(Z=\langle e_4\rangle\), \(\gamma_2=[\mathfrak f_4,\mathfrak f_4]=\langle e_3,e_4\rangle\), and \(C=C_{\mathfrak f_4}(\gamma_2)=\langle e_2,e_3,e_4\rangle\).

## Proof
Every automorphism is uniquely determined by parameters \(a,h\in\mathbb F_q^\times\) and \(b,c,d,r,s\in\mathbb F_q\) through
\[
\begin{aligned}
\phi(e_1)&=a e_1+b e_2+c e_3+d e_4,\\
\phi(e_2)&=h e_2+r e_3+s e_4,\\
\phi(e_3)&=ah e_3+ar e_4,\\
\phi(e_4)&=a^2h e_4.
\end{aligned}
\]
Indeed, start with arbitrary images of \(e_1,e_2\). Their classes modulo \(\gamma_2\) must be independent. If the \(e_1\)-coefficient of \(\phi(e_2)\) were \(p\), then \(\phi(e_3)=[\phi(e_1),\phi(e_2)]\) has nonzero \(e_3\)-coefficient, while preservation of \([e_2,e_3]=0\) forces \(p=0\). The displayed form and uniqueness then follow from the two defining brackets. Thus
\[
|\operatorname{Aut}(\mathfrak f_4(q))|=(q-1)^2q^5.
\]

For a vector \(x=x_1e_1+x_2e_2+x_3e_3+x_4e_4\), the fixed-vector equations are triangular:
\[
\begin{aligned}
(a-1)x_1&=0,\\
bx_1+(h-1)x_2&=0,\\
cx_1+rx_2+(ah-1)x_3&=0,\\
dx_1+sx_2+arx_3+(a^2h-1)x_4&=0.
\end{aligned}
\]
For \((a,h)\in(\mathbb F_q^\times)^2\), the four diagonal factors \(a-1,h-1,ah-1,a^2h-1\) have: no zero in \((q-3)^2\) cases; exactly one zero in respectively \(q-2,q-3,q-2,q-3\) cases; exactly the two zeros \(h-1=a^2h-1=0\) in the single case \((a,h)=(-1,1)\); and all four zeros only at \((1,1)\). The first five strata contribute fixed dimensions \(0\) and \(1\) immediately.

At \((a,h)=(-1,1)\), the equations give \(x_1=0\), \(x_3=(r/2)x_2\), and
\[
\left(s-\frac{r^2}{2}\right)x_2=0,
\]
with \(x_4\) free. Hence exactly \(q^4\) automorphisms in this stratum have fixed dimension \(2\), and the other \(q^5-q^4\) have fixed dimension \(1\).

At \((a,h)=(1,1)\), \(x_4\) is always free and the rank of the remaining system is the rank of
\[
B=\begin{pmatrix}b&0&0\\ c&r&0\\ d&s&r\end{pmatrix}.
\]
For \(r\ne0,b\ne0\), the rank is \(3\), giving \((q-1)^2q^3\) choices. Rank \(2\) occurs in \((q-1)q^3+(q-1)q(q^2-1)=(q-1)(2q^3-q)\) choices. Rank \(1\) occurs in \((q-1)q+(q^3-1)=q^3+q^2-q-1\) choices, and rank \(0\) once. Combining this identity-diagonal count with the preceding strata gives
\[
N_0=(q-3)^2q^5,
\]
\[
N_1=q^3(4q^3-8q^2-3q+1),
\]
\[
N_2=3q^4-2q^3-q^2+q,\qquad N_3=q^3+q^2-q-1,\qquad N_4=1.
\]
Direct addition gives \(\sum_jN_j=(q-1)^2q^5\), and Burnside's lemma gives
\[
\frac{\sum_{j=0}^4N_jq^j}{(q-1)^2q^5}=5.
\]

The five orbits can also be identified without Burnside. The characteristic chain
\[
0\subset Z\subset\gamma_2\subset C\subset\mathfrak f_4
\]
is preserved by every automorphism. The displayed automorphism formula is transitive on each successive difference: when the first nonzero coordinate is respectively in positions \(4,3,2,1\), the free scaling parameter and the subsequent shear parameters normalize that coordinate and eliminate all later coordinates. Together with \(\{0\}\), these are exactly the five orbits.

## Verification
The accompanying `verify.py` enumerates all automorphisms over the prime fields \(\mathbb F_3,\mathbb F_5,\mathbb F_7\), computes the rank of \(\phi-I\), and compares the resulting spectra with the closed formulas. It also reconstructs all element-orbits for \(q=3\) and checks that each orbit is exactly one of the five intrinsic layers. The successful replay prints `VERIFY_OK`. These finite checks corroborate, but do not replace, the symbolic proof for arbitrary odd prime powers.

## Relationship to prior work
Karimjanov and Ladra's filiform-algebra paper records the standard model family \(\mathcal L_n\) with brackets \([e_1,e_i]=e_{i+1}\) and supplies the archive-era structural context. Sheng, Liu, and Liu give explicit automorphism matrix forms for model filiform Lie (super)algebras over characteristic-zero fields; that structural result is closely related to the normal form used above, but their paper studies local and 2-local automorphisms rather than finite-field fixed-space distributions. Burde and Dekimpe study existence of fixed-point-free automorphisms for complex filiform Lie algebras; their criterion does not enumerate the finite-field fibers of \(\dim\operatorname{Fix}(\phi)\). Targeted searches of the published published-finding corpus corpus found adjacent fixed-point and filiform results, but not this complete spectrum or its five-orbit consequence.

## Limitations
Characteristic \(2\) is excluded because the exceptional stratum uses division by \(2\) and the diagonal-collision pattern changes. The verifier exhausts only three prime fields; extension fields are covered by the symbolic argument, not by finite enumeration. The structural automorphism parametrization itself is not claimed as new. The originality claim is limited to the stated finite-field fixed-space distribution and the accompanying intrinsic five-orbit classification; literature under different notation could still present a residual indexing risk.

## References
1. I. A. Karimjanov and M. Ladra, *Minimal linear representations of filiform Lie algebras and their application for construction of Leibniz algebras*, arXiv:1605.06259, first public 20 May 2016; later Journal of Geometry and Physics 144 (2019), DOI 10.1016/j.geomphys.2019.06.009.
2. Y. Sheng, W. Liu, and Y. Liu, *Local Automorphisms and Local Superderivations of Model Filiform Lie Superalgebras*, Journal of Mathematics (2024), DOI 10.1155/2024/6650997.
3. D. Burde and K. Dekimpe, *Fixed-point-free automorphisms of solvable Lie algebras*, arXiv:2604.27916 (2026).
