# Complete automorphism fixed-space spectrum of the two-branch cubic monomial algebra

## Finding
For every finite field \(k=\mathbb F_q\), consider the five-dimensional commutative monomial algebra
\[
 A_q=k[x,y]/(xy,x^3,y^3).
\]
Write \(N_j(q)=|\{\varphi\in\operatorname{Aut}_k(A_q):\dim_k\operatorname{Fix}(\varphi)=j\}|\). When \(q\) is odd,
\[
\begin{aligned}
N_1&=2q^4(q-3)(q-2),\\
N_2&=q^3(2q-1)(3q-7),\\
N_3&=q(7q^3-8q^2-3q+1),\\
N_4&=q^3+3q^2-q-1,\\
N_5&=1.
\end{aligned}
\]
When \(q\) is even,
\[
\begin{aligned}
N_1&=q^4(q-2)(2q-3),\\
N_2&=q^3(q-1)(3q-5),\\
N_3&=q(4q^3-6q^2-q+1),\\
N_4&=(q-1)(q+1)^2,\\
N_5&=1.
\end{aligned}
\]
There are no other fixed-space dimensions. The total group order is \(2(q-1)^2q^4\). Burnside averaging gives \(8q\) element-orbits for odd \(q\), versus \(5q\) for even \(q\).

## Assumptions and scope
Automorphisms are unital \(k\)-algebra automorphisms, not semilinear maps. All finite fields, including characteristic two and nonprime finite fields, are covered. Fixed dimensions include the obligatory scalar line \(k1\). No claim is made for higher truncation orders or other numbers of branches.

## Proof
Set \(\mathfrak m=(x,y)\) and \(S=\mathfrak m^2=\langle x^2,y^2\rangle_k\); then \(\mathfrak m^3=0\), \(\dim_k\mathfrak m/\mathfrak m^2=2\), and \(\dim_k S=2\). A unital automorphism preserves both \(\mathfrak m\) and \(S\). If its induced matrix on \(\mathfrak m/S\) has columns \((a,b)\) and \((c,d)\), the equation \(\varphi(x)\varphi(y)=0\) yields \(ac=bd=0\), since \(x^2,y^2\) are independent. Invertibility forces the matrix to be either diagonal or anti-diagonal. Conversely all such invertible linear parts, with arbitrary socle additions to \(\varphi(x),\varphi(y)\), give automorphisms because the defining relations survive and the induced cotangent-space map is invertible. There are thus \(2(q-1)^2q^4\) automorphisms.

Relative to \(\mathfrak m=(\mathfrak m/S)\oplus S\), each automorphism has block matrix \(\begin{pmatrix}P&0\\B&Q\end{pmatrix}\), with arbitrary \(B\in M_2(k)\). In the diagonal case \(P=\operatorname{diag}(a,d)\) and \(Q=\operatorname{diag}(a^2,d^2)\). In the branch-swapping case \(P=\begin{pmatrix}0&d\\a&0\end{pmatrix}\) and \(Q=\begin{pmatrix}0&d^2\\a^2&0\end{pmatrix}\). Always \(a,d\in k^\times\).

Put \(r=\dim\ker(P-I)\) and \(s=\dim\ker(Q-I)\). The fixed-vector equations are \((P-I)v=0\) and \((Q-I)w=-Bv\). Let \(K=\ker(P-I)\). Modulo \(\operatorname{im}(Q-I)\), the restriction of \(B\) gives an arbitrary linear map \(K\to\operatorname{coker}(Q-I)\) of size \(s\times r\), with each such matrix represented exactly \(q^{4-rs}\) times by the original \(B\). If its rank is \(h\), the fixed dimension in \(A_q\) is \(1+s+r-h\). This is a uniform count, not a probabilistic approximation.

For odd \(q\), the possible pairs \((r,s)\) and numbers of diagonal/anti-diagonal linear parts are
\[
\begin{array}{c|rrrrrr}(r,s)&(0,0)&(0,1)&(0,2)&(1,1)&(1,2)&(2,2)\\\hline
\#&2(q-3)(q-2)&3q-7&1&3q-7&2&1\end{array}.
\]
Indeed, in the diagonal case each scalar is either \(1\), \(-1\), or one of the \(q-3\) remaining nonzero values; in the anti-diagonal case the determinant product \(ad\) is \(1\), \(-1\), or neither, with exactly \(q-1\) choices of the ordered pair for each prescribed product. For even \(q\), the only pairs are \((0,0)\), \((1,1)\), and \((2,2)\), with respective numbers \((q-2)(2q-3)\), \(3q-5\), and \(1\), since \(1=-1\).

The matrix-rank distribution needed to sum over \(B\) is elementary: an \(s\times r\) matrix has rank zero in exactly one way; for \((r,s)=(1,1)\) there are \(q-1\) rank-one choices; for \((1,2)\) there are \(q^2-1\); for \((2,2)\) there are \((q-1)(q+1)^2\) rank-one matrices and \((q^2-1)(q^2-q)\) rank-two matrices. Multiply these by \(q^{4-rs}\) and the displayed pair multiplicities. Collecting coefficients of fixed dimension \(1+s+r-h\) yields precisely the five formulas in the Finding. Direct expansion verifies that their sum is \(2(q-1)^2q^4\) in either characteristic.

Each \(\varphi\) fixes exactly \(q^j\) elements when its fixed-space dimension is \(j\). Burnside's lemma therefore gives \(\frac{\sum_{j=1}^5N_j(q)q^j}{2(q-1)^2q^4}\), simplifying to \(8q\) in odd characteristic and \(5q\) in characteristic two.

## Verification
Run `python3 verify.py` using the included standalone verifier. It exhaustively enumerates all automorphism normal forms over the prime fields of orders \(2,3,5\), calculates the fixed dimensions via modular Gaussian elimination, compares every bin with the closed formulas, and checks direct radical-element orbit counts for orders \(2,3\). The expected spectra are \((0,8,14,9,1)\), \((0,270,327,50,1)\), and \((7500,9000,3305,194,1)\), with entries ordered from dimensions \(1\) through \(5\). These finite checks do not replace the general proof.

## Relationship to prior work
Strametz studies Hochschild cohomology and the connected outer-automorphism group for finite-dimensional monomial algebras, furnishing an archive-era structural setting but no finite-field fixed-vector distribution. Díaz and Lucchini Arteche explicitly consider the same ideal \((x^3,xy,y^3)\) in a characteristic-zero automorphism-reconstruction study, but examine derivation weights, not fixed-subspace fiber counts. The published published-finding corpus treatment of truncated coordinate-cross algebras supplies the general full automorphism normal form (and group order) for precisely this family; those structural ingredients are credited. The additional result here is a complete distribution by fixed-space dimension and the characteristic-dependent Burnside orbit counts, which are not supplied by the cited classification statements.

## Limitations
The new contribution is not a new description of the automorphism group; that was available in the published cross-algebra result. The finite-field fiber census is supported by an elementary proof and small-prime-field consistency checks. Broader literature under fiber-product or Artinian Stanley–Reisner terminology may contain implicit or explicit equivalent enumerations; the indexed searches and inspected same-object sources did not establish such coverage. No independent audit has been performed.

## References
1. C. Strametz, *The Lie algebra structure on the first Hochschild cohomology group of a monomial algebra*, arXiv:math/0111060v1, first public 2001-11-06, primary MSC 16E40.
2. R. Díaz and G. Lucchini Arteche, *Finite-dimensional monomial algebras are determined by their automorphism group*, arXiv:2409.15081, first public 2024-09-23, Example 2.2 on the same ideal.
3. *Automorphisms of truncated coordinate-cross algebras over arbitrary fields*, published published-finding corpus finding, `2026/10/4/SCOPE-automorphisms-of-truncated-coordinate-cross-algebras-over-arbitr--625ba30274cb`, `RESULT.md`.
