# Exact fourth-moment rigidity of the eight-mode cubic Fourier aperture

## Finding

Let \(\mathbb T=\{z\in\mathbb C:|z|=1\}\) carry Haar probability measure. For any eight unit-modulus coefficients \(c_{ijk}\), indexed by \((i,j,k)\in\{0,1\}^3\), put
\[
P(x,y,z)=\sum_{i,j,k\in\{0,1\}}c_{ijk}x^iy^jz^k,\qquad
\mathcal M(P)=\int_{\mathbb T^3}|P(x,y,z)|^4\,dm(x,y,z).
\]
Then the **exact attainable range** is
\[
88\leq\mathcal M(P)\leq216.
\]
Every number in this interval is attained. The upper endpoint is attained exactly when
\[
c_{ijk}=\lambda\alpha^i\beta^j\gamma^k,
\]
with \(\lambda,\alpha,\beta,\gamma\in\mathbb T\). The lower endpoint is attained exactly when
\[
c_{ijk}=\lambda\alpha^i\beta^j\gamma^k(-1)^{Q(i,j,k)},
\]
where \(Q\) is **one** of the three quadratic functions
\[
Q(i,j,k)=ij+ik,\qquad Q(i,j,k)=ij+jk,\qquad Q(i,j,k)=ik+jk.
\]
These are three distinct orbits under scalar and coordinate-phase modulation. The normalized aperiodic autocorrelation merit factor at the minimum is \(64/(88-64)=8/3\).

If the coefficients are restricted to the \(q\)-th roots of unity for any integer \(q\ge2\), the global minimum \(88\) is attainable **if and only if** \(q\) is even. In that case there are exactly \(3q^4\) coefficient arrays achieving it. The maximum \(216\) is attained by exactly \(q^4\) arrays for every \(q\ge2\).

The same fourth-moment bounds and equality classifications hold when the Haar integral is replaced by the normalized average over \(\mu_m\times\mu_n\times\mu_r\), for any integers \(m,n,r\ge3\), where \(\mu_s\) denotes the \(s\)-th roots of unity.

## Assumptions and scope

The coefficients are independently constrained to the complex unit circle; no reality, binary-phase, or factorization hypothesis is assumed. The torus carries Haar **probability** measure, and discrete cyclic products carry normalized uniform measure. Support is the complete degree-at-most-one cube \(\{0,1\}^3\) in the integer character lattice; it is not the Boolean group with mod-two frequency arithmetic. Phase-modulation orbits refer to the action \(c_{ijk}\mapsto\lambda\alpha^i\beta^j\gamma^k c_{ijk}\). The finite alphabet statement concerns all coefficient entries belonging to \(\mu_q\), irrespective of the underlying sampling group.

## Proof

**1. Orthogonality.** By expanding \(|P|^4\) and integrating monomials, or equivalently by Parseval for the coefficient convolution, we have
\[
\mathcal M(P)=\sum_{(a,b,c)\in\{0,1,2\}^3}\left|\sum_{u+v=(a,b,c)}c_uc_v\right|^2.
\]
The inner sum is over ordered pairs of cube vertices. Multiplication of all coefficients by a common unit scalar and by coordinate phases leaves this expression unchanged. Choose the unique such normalization
\[
c_{000}=c_{100}=c_{010}=c_{001}=1,\qquad
(c_{110},c_{101},c_{011},c_{111})=(A,B,C,D),
\]
where \(|A|=|B|=|C|=|D|=1\). Define
\[
S_1=1+A+B+C,\qquad S_2=A+B+C+AB+AC+BC.
\]
A direct grouping of the 27 convolution coefficients, or of the 13 nonzero aperiodic autocorrelations modulo conjugate symmetry, gives the **exact identity**
\[
\boxed{\mathcal M(P)=104+4|S_1|^2+8\operatorname{Re}(D\overline{S_2}).}
\tag{1}
\]
For clarity, the four opposite-corner correlation pairs each have squared magnitude one; the six face-diagonal correlations (one per sign-pair) are
\[
1+B\overline A,\ 1+C\overline A,\ 1+C\overline B,\
\overline A+\overline D,\ \overline B+\overline D,\ \overline C+\overline D,
\]
and the three axial correlations are
\[
1+\overline A+\overline B+C\overline D,\quad
1+\overline A+\overline C+B\overline D,\quad
1+\overline B+\overline C+A\overline D.
\]
Thus the moment equals \(72\) plus twice the sum of squares of these nine correlations; its expansion is (1). The exact Laurent-polynomial expansion is also reproduced by the standalone checker.

**2. Lower bound and rigidity.** Newton's elementary identity for the four unit complex numbers \(1,A,B,C\) reads
\[
2S_2=S_1^2-(1+A^2+B^2+C^2).
\]
Consequently,
\[
2|S_2|\le |S_1|^2+|1+A^2+B^2+C^2|\le |S_1|^2+4.
\tag{2}
\]
Equations (1)--(2) imply
\[
\mathcal M(P)\ge104+4|S_1|^2-8|S_2|\ge88.
\]
If equality holds, the last inequality in (2) is equality, so all four unit numbers \(1,A^2,B^2,C^2\) point in the same direction. Since the first is \(1\), necessarily \(A,B,C\in\{1,-1\}\). Equality in the first triangle inequality in (2) now says
\[
|S_1^2-4|=S_1^2+4;
\]
as \(S_1\) is real, this forces \(S_1=0\). Therefore exactly two of \(A,B,C\) are negative, the third is positive, and \(S_2=-2\). Equality in the initial estimate \(\operatorname{Re}(D\overline{S_2})\ge-|S_2|\) then requires \(D=1\). Conversely these three normalized choices give equality, proving all lower equality cases.

**3. Upper bound and rigidity.** In the convolution identity from step 1, each coefficient is a sum of unit-modulus terms; its magnitude is no larger than the number of those terms. The all-one coefficient array attains every such triangle inequality and satisfies
\[
P(x,y,z)=(1+x)(1+y)(1+z),\qquad
\mathcal M(P)=6^3=216.
\]
If an arbitrary coefficient array attains the same total, equality must hold in every convolution triangle inequality. The three convolution coefficients at multiindices \((1,1,0)\), \((1,0,1)\), and \((0,1,1)\) then force \(A=B=C=1\). The coefficient at multiindex \((1,1,1)\) is \(2(A+B+C+D)\), and its maximal modulus forces \(D=1\). This gives precisely the affine character-phase family.

**4. Intermediate values and finite alphabets.** The phase torus \(\mathbb T^8\) is connected and the fourth moment is continuous, hence its image is the entire interval between its achieved endpoints. When \(c_{ijk}\in\mu_q\), the equality invariants \(A,B,C,D\) are all \(q\)-th roots of unity. The three minimizing patterns contain \(-1\), and hence are permitted exactly when \(2\mid q\). In the permitted case, each normalized minimizer has exactly \(q^4\) distinct lifts, indexed freely by the common scalar and three coordinate phases; the three classes are disjoint. The maximizing pattern likewise has exactly \(q^4\) lifts.

**5. Finite sampling.** For \(m,n,r\ge3\), the 27 multiindices in \(\{0,1,2\}^3\) remain pairwise distinct modulo \((m,n,r)\). Discrete character orthogonality therefore reproduces exactly the same convolution sum as in step 1, including every equality condition.

## Verification

Run `python3 checker.py` with Python 3. The checker independently expands the full coefficient convolution as an integer Laurent polynomial in \(A,B,C,D\) and compares it with identity (1). A second, independent Gaussian-integer convolution implementation exhaustively tests the normalized binary and quaternary coefficient patterns, confirming respectively \(3\) minimizing patterns, \(1\) maximizing pattern, and the predicted lifting counts. It also confirms the no-aliasing premise for selected cyclic orders \(3,4,5,7\). The checker has no scientific dependencies. These finite checks support, but do not replace, the proof for all continuous phases and all orders.

## Relationship to prior work

Pai and Chen's 2021 paper on generalized-Boolean two-dimensional Golay complementary array **sets** (arXiv:2102.04043v1) defines aperiodic array autocorrelations and constructs pairs/sets whose summed nonzero correlations cancel. Its Theorem 9 produces complementary *pairs* from quadratic generalized Boolean functions, not an extremal single three-dimensional array inequality. Zhang, Fan and Mesnager (arXiv:2107.11599v1) similarly construct two-dimensional Z-complementary array pairs and derive zero-correlation-zone properties. Their Theorems 1--2 do not determine a single \(2\times2\times2\) array's global fourth-moment range or equality classes. Barker-array results of Jedwab and collaborators concern binary two-dimensional arrays with individual correlation amplitudes at most one, rather than this unrestricted three-dimensional unimodular fourth-moment optimization. The normalized minimizers here happen to be quadratic Boolean path phases, but their global optimality among all complex phases and completeness are additional assertions proved here. An equivalent older polyphase-array classification remains a bibliographic risk.

## Limitations

No claim is made about cube support dimensions above three, arbitrary coefficient magnitudes, cyclic sampling factors below three, or the exact optimal fourth moment for any odd finite phase alphabet. The statement is not about Boolean-group Walsh moments: aliasing in characteristic two changes the fourth moment. The provenance of an exact equivalent theorem outside the inspected literature remains unverified; independent review has not been performed.

## References

1. Cheng-Yu Pai and Chao-Yu Chen, *Two-Dimensional Golay Complementary Array Sets from Generalized Boolean Functions*, arXiv:2102.04043v1, 8 February 2021. https://arxiv.org/html/2102.04043v1
2. Hui Zhang, Cuiling Fan and Sihem Mesnager, *New constructions of q-Ary 2-D Z-Complementary Array Pairs*, arXiv:2107.11599v1, 24 July 2021. https://arxiv.org/html/2107.11599v1
3. Jonathan Jedwab, *Barker Arrays I: Even Number of Elements*, SIAM J. Discrete Math. 6 (1993), 294--308. https://doi.org/10.1137/0406024
4. Jonathan Jedwab, Sheelagh Lloyd and Miranda Mowbray, *Barker Arrays II: Odd Number of Elements*, SIAM J. Discrete Math. 6 (1993), 309--328. https://doi.org/10.1137/0406025
