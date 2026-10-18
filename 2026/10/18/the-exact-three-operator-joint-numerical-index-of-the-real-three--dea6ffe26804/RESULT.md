# The exact three-operator joint numerical index of the real three-dimensional taxicab space

## Finding

For the real Banach space \(X=\ell_1^3(\mathbb R)\), the Euclidean three-operator joint numerical index is exactly
\[
\boxed{n_{(2,3)}(X)=\frac35}.
\]
Equivalently, for every three bounded real-linear operators \(T_1,T_2,T_3:X\to X\),
\[
w_2(T_1,T_2,T_3)\ge\frac35\|(T_1,T_2,T_3)\|_2,
\]
with equality for an explicit rank-one-source triple. This identifies the precise real value at the first odd equal-dimension case not settled by the Fourier--Walsh saturation method, and exhibits its strict separation from the complex value \(1/\sqrt3\).

A sharp auxiliary matrix inequality holds for **every** real \(3\times3\) matrix \(A\) with columns \(a_1,a_2,a_3\):
\[
\left(\sum_{j=1}^3\|a_j\|_1^2\right)^{1/2}
\le\frac53\max_{s\in\{-1,1\}^3}\|A^{\mathsf T}s\|_2.
\]
The constant \(5/3\) cannot be decreased.

## Assumptions and scope

The scalar field is \(\mathbb R\), the space is exactly \(\ell_1^3\), the tuple has exactly three operators, and the joint exponent is exactly two. Write
\[
\Pi_X=\{(x,f):\|x\|_1=\|f\|_\infty=1,\ f(x)=1\},
\quad
\|\mathcal T\|_2=\sup_{\|x\|_1=1}\left(\sum_{j=1}^3\|T_jx\|_1^2\right)^{1/2},
\]
\[
w_2(\mathcal T)=\sup_{(x,f)\in\Pi_X}\left(\sum_{j=1}^3|f(T_jx)|^2\right)^{1/2},
\qquad
n_{(2,3)}(X)=\inf_{\|\mathcal T\|_2=1}w_2(\mathcal T).
\]
These are the joint-numerical-index conventions introduced in the cited 2022 paper. No complex-field, other-exponent, or higher-dimensional claim is asserted.

## Proof

**1. Reduction to a sharp three-column matrix inequality.** Let \(e_i\) be the three coordinate vectors. Convexity on the \(\ell_1\) unit ball gives
\[
\|\mathcal T\|_2=
\max_{1\le i\le3}\left(\sum_{j=1}^3\|T_je_i\|_1^2\right)^{1/2}.
\]
Also,
\[
w_2(\mathcal T)=\max_{1\le i\le3}\ 
\max_{s\in\{-1,1\}^3}
\left(\sum_{j=1}^3|s\cdot T_je_i|^2\right)^{1/2}.
\]
To justify the latter equality without assuming an unsupported extreme-point reduction, let \((x,f)\in\Pi_X\). For each nonzero coordinate, \(f_i=\operatorname{sgn}(x_i)\), and
\(x=\sum_i|x_i|\operatorname{sgn}(x_i)e_i\).
The three-component scalar image \((f(T_jx))_j\) is therefore a convex combination of the vectors obtained at the norming pairs \((\operatorname{sgn}(x_i)e_i,f)\). Their Euclidean norms are bounded by the displayed coordinate maximum. For each fixed coordinate, the Euclidean image norm is convex in the allowable dual coefficients \(f_r\in[-1,1]\) and hence its maximum occurs at a sign vector; conversely a sign vector \(s\) is norming at \(s_ie_i\). Thus the coordinate formula is exact. For each \(i\), form the matrix \(A_i\) whose \(j\)-th column is \(T_je_i\). It suffices to prove the stated inequality for every \(A_i\).

**2. Four sign classes and the sharp matrix inequality.** Fix a real \(3\times3\) matrix \(A=(a_1\ a_2\ a_3)\), and set
\[
D=\left(\sum_j\|a_j\|_1^2\right)^{1/2},
\qquad W=\max_{s\in\{-1,1\}^3}\|A^{\mathsf T}s\|_2.
\]
For each column \(a_j\), choose \(s_j\in\{-1,1\}^3\) with \(|s_j\cdot a_j|=\|a_j\|_1\). Up to overall sign, there are exactly four sign classes, represented for example by
\[(1,1,1),\quad(1,1,-1),\quad(1,-1,1),\quad(-1,1,1).\]
If the three chosen \(s_j\) occupy at most two classes, group the indices by class: the squared contribution in either class is at most the squared norm \(\|A^{\mathsf T}s\|_2^2\le W^2\). Hence \(D^2\le2W^2<25W^2/9\) when \(W>0\); the zero case is immediate.

Otherwise the three classes are distinct. A direct inspection of the displayed four projective sign representatives shows that one can independently reverse the orientations of \(s_1,s_2,s_3\) so that
\[
s_0=s_1+s_2+s_3\in\{-1,1\}^3,
\]
where \(s_0\) belongs to the fourth class. Such reversals preserve the absolute-value identities \(|s_j\cdot a_j|=\|a_j\|_1\). Put \(v_j=A^{\mathsf T}s_j\) for \(j=0,1,2,3\). Then \(v_0=v_1+v_2+v_3\), all \(\|v_j\|_2\le W\), and
\[
D=\left(\sum_{j=1}^3|(v_j)_j|^2\right)^{1/2}
=\max_{\|y\|_2=1}\sum_{j=1}^3y_j(v_j)_j.
\]
For an arbitrary real unit vector \(y\), choose \(z=-y/6\). The sum relation yields
\[
\begin{aligned}
\sum_{j=1}^3y_j(v_j)_j
&=\sum_{j=1}^3(y_je_j+z)\cdot v_j-z\cdot v_0\\
&\le W\left(\sum_{j=1}^3\|y_je_j+z\|_2+\|z\|_2\right)\\
&=\frac W6\left(1+\sum_{j=1}^3\sqrt{1+24y_j^2}\right)\\
&\le\frac W6\left(1+\sqrt{3\sum_{j=1}^3(1+24y_j^2)}\right)
=\frac{5W}{3}.
\end{aligned}
\]
Here the penultimate inequality is Cauchy--Schwarz and the last equality uses \(\|y\|_2^2=1\). Maximizing over \(y\) proves the universal matrix inequality.

**3. Exact sharpness and the operator tuple.** Take
\[
A_*=\begin{pmatrix}-1&-2&2\\2&-2&-1\\2&1&2\end{pmatrix}.
\]
Its column \(\ell_1\) norms all equal five, so \(D^2=75\). Direct multiplication gives \(A_*A_*^{\mathsf T}=9I_3\); thus every sign vector \(s\) satisfies \(\|A_*^{\mathsf T}s\|_2^2=27\). Consequently \(W/D=\sqrt{27/75}=3/5\). Define three operators \(T_j\) by \(T_je_1=a_j\) (the columns of \(A_*\)) and \(T_je_2=T_je_3=0\). The exact coordinate norm and numerical-radius formulas from step 1 give
\[
\|\mathcal T\|_2=5\sqrt3,
\qquad w_2(\mathcal T)=3\sqrt3.
\]
The matrix inequality gives the same ratio as a universal lower bound for all triples. Hence the infimum is attained and is exactly \(3/5\).

## Verification

Run `python3 verification/check_joint_three.py` using Python 3's standard library. It evaluates both sides using integer squares for every one of the \(3^9=19{,}683\) ternary-entry matrices and for \(50{,}000\) fixed-seed integer matrices with entries between negative and positive twenty. It independently checks the explicit witness Gram matrix, the squared sharp values \(D^2=75\), \(W^2=27\), and all four omitted-class sign relations. Expected output begins with `VERIFY_OK`. These finite experiments are consistency checks, **not** the proof for arbitrary real matrices; that proof is the analytical argument above.

## Relationship to prior work

Mal's original 2022 paper defines the same joint operator norm and numerical radius (Introduction and Section 3) and proves the general bound \(n(X)/\sqrt k\) in Theorem 3.1. Its Theorem 3.9 establishes the relevant finite \(\ell_1\) value for **two** operators but not for three. The published research record *Fourier saturation and a real three-dimensional obstruction for joint numerical indices* constructs exact complex and dyadic real families and proves that the real three-dimensional three-tuple value is strictly greater than \(1/\sqrt3\), explicitly leaving its numerical value undetermined. The present result supplies that exact value using a four-sign-class dual certificate, not merely the qualitative odd-order obstruction. The known complex value \(1/\sqrt3\) therefore differs sharply from the real value \(3/5\).

The matrix inequality is an equivalent reformulation of the exact index through the coordinate reduction; it is not claimed as a separate independent finding. The usual one-operator numerical index, complex Hilbert-space numerical radius, and tensor injective norm bounds have different input/output norm normalizations and do not directly give the stated sharp real constant.

## Limitations

The result treats the single dimension/tuple/exponent triple \((m,k,p)=(3,3,2)\) over the real field, not arbitrary real non-dyadic dimensions or \(p\ne2\). The equality witness uses source-supported rank-one operators; no classification of **all** extremizing tuples is asserted. Exhaustive small-integer tests do not settle uniqueness or higher-dimensional behavior. Bibliographic searches can miss unindexed formulations of this mixed-norm matrix inequality; independent scientific audit has not been performed.

## References

1. A. Mal, *On joint numerical radius of operators and joint numerical index of a Banach space*, arXiv:2212.06500v1, first posted 13 December 2022. https://arxiv.org/html/2212.06500v1 . See definitions in Section 1, Theorem 3.1 and Theorem 3.9.
2. *Fourier saturation and a real three-dimensional obstruction for joint numerical indices*, publicly available mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-fourier-saturation-and-a-real-three-dimensional-obstruction-for--72d0f9b245b7 . See its proof of strict separation and explicit statement of the unresolved exact real value in the limitations.
