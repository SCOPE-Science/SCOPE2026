# Three-primary torsion vanishes for four-point configurations of large complete bipartite graphs

## Finding

For all integers \(a,b\ge7\), let \(X_{a,b}=\operatorname{UConf}_4(|K_{a,b}|)\) be the unordered configuration space of four distinct points in the geometric realization of the simple complete bipartite graph with part sizes \(a,b\). Then
\[
\operatorname{Tors}_3 H_3(X_{a,b};\mathbb Z)=0.
\]
More precisely, define
\[
d(x)=x(x-1)(x-2)(x-3)-4x(x-1)(x-2)+6x(x-1)-4x+1,
\qquad t(x)=-x^2+3x-1.
\]
The mod-three and rational fourth Betti numbers coincide, with common value
\[
\dim_{\mathbb F_3}H_4(X_{a,b};\mathbb F_3)=\dim_{\mathbb Q}H_4(X_{a,b};\mathbb Q)
=\frac{d(a)d(b)-6t(a)t(b)+8(a-1)(b-1)-3}{24}.
\]
For \((a,b)=(7,7),(7,8),(8,8)\), respectively, these numbers are \(1911,5726,16716\).

## Assumptions and scope

Graphs are simple finite one-dimensional CW complexes; points are unordered and cannot collide. All three-primary assertions concern integral \(H_3\), **not** arbitrary homological degrees or other primes. The graph-part restriction \(a,b\ge7\) is essential to the shellability input below. Throughout the proof, \(F=\mathbb F_3\), \(G=S_4\), \(V=\{1,(12)(34),(13)(24),(14)(23)\}\triangleleft G\), and \(G/V\cong S_3\). A module called projective is projective over the indicated finite group algebra in characteristic three.

For \(x\ge7\), define \(D(x)\) to be the space of \(F\)-valued functions on injections \([4]\hookrightarrow[x]\) whose sum over completions of any one missing slot is zero. The \(S_4\)-action permutes slots *without* an extra sign. This is precisely the slot module in An's Proposition 5.1, which gives over **every field**
\[
H_4(X_{a,b};F)\cong\operatorname{Hom}_{FG}(\operatorname{sgn},D(a)\otimes_F D(b)).
\]

## Proof

**1. Stable modular structure.** The chessboard complex \(\Delta_{4,x}\), consisting of nonattacking rook sets on \([4]\times[x]\), has reduced integral homology free and concentrated in degree three when \(x\ge7\), by the shellability result used in An, Section 5. The oriented top homology over \(F\) is \(D(x)\otimes\operatorname{sgn}\); the sign comes from ordering the four row slots.

Consider its augmented oriented chain complex, with \(C_{k-1}\) spanned by the \(k\)-rook faces. For \(k\ge2\), each rook face has row-permutation stabilizer \(S_{4-k}\), of order not divisible by three; hence \(C_1,C_2,C_3\) are projective \(FG\)-modules. Also \(C_0\) is a sum of \(x\) copies of the permutation representation \(F^4\), and \(F^4\cong F\oplus P\), where \(P\) is projective: its restriction to a Sylow three-subgroup is free of rank one. Because \(4\) is invertible in \(F\), the augmentation kernel is
\[
N=\ker(C_0\longrightarrow C_{-1})\cong F^{x-1}\oplus P^{x}.
\]
Exactness below degree three identifies the top oriented homology, up to projective summands, with the third syzygy of \(N\). The idempotent for the trivial \(V\)-character selects the block equivalent to \(F[S_3]\). In that block, write \(U_j^\pm\) for the length-\(j\) indecomposable module with a nilpotent length-\(j\) chain and the transposition acting alternately, beginning with eigenvalue \(\pm1\). The projective indecomposables are \(U_3^+\) and \(U_3^-\), while
\[
\Omega(F)=U_2^-,\quad\Omega^2(F)=U_1^-,\quad\Omega^3(F)=U_2^+.
\]
The orientation-sign twist therefore shows that the \(V\)-trivial block of \(D(x)\) has the decomposition
\[
D(x)^V\cong (x-1)U_2^-\oplus P_x U_3^+\oplus Q_x U_3^-.
\]
Every nontrivial \(V\)-character block is projective: its inertia quotient has order two and so is semisimple in characteristic three.

**2. Characters and multiplicities.** A row permutation fixes an oriented rook face setwise only if it fixes each occupied row, since its columns remain fixed and distinct. Taking the alternating sum of chain traces, and undoing the top orientation sign, gives the following ordinary characters of \(D(x)\) on the five classes of \(S_4\):
\[
\begin{array}{c|ccccc}
\text{cycle type}&1&(12)&(12)(34)&(123)&(1234)\\\hline
\chi_{D(x)}&d(x)&t(x)&1&1-x&-1.
\end{array}
\]
These are also the Brauer traces of the integral top-homology lattice on elements of order prime to three. They determine the dimensions of the \(V\)-isotypical parts and their transposition eigenmultiplicities. Specifically,
\[
\begin{aligned}
P_x&=\frac{x(x-7)(x-2)(x-1)}{24},&
Q_x&=\frac{(x-4)(x-3)(x-2)(x-1)}{24},\\
U_x&=\frac{x(x-6)(x-3)(x-1)}8,&
V_x&=\frac{x(x-5)(x-3)(x-2)}8.
\end{aligned}
\]
Here \(U_x,V_x\) are the respective \(+1,-1\) eigenspace dimensions for the transposition \((12)\) on the nontrivial \(V\)-character space satisfying \(\chi((12)(34))=1\), \(\chi((13)(24))=-1\). To check the formulas directly, its dimension is \((d(x)-1)/4\) and its transposition trace is \((t(x)+1)/2\). The \(V\)-fixed part has dimension \((d(x)+3)/4\) and transposition trace \((t(x)-1)/2\); subtracting \(x-1\) copies of \(U_2^-\) gives the stated \(P_x,Q_x\). No semisimplicity of the three-cycles is presumed.

**3. Dimension in characteristic three.** The group \(S_3\) has a normal cyclic subgroup of order three generated by \(c\); writing \(M=c-c^{-1}\), one has \(M^3=0\), while a transposition \(s\) satisfies \(sMs=-M\). A homomorphism of the indicated indecomposables is determined by the image of a generator, subject to its transposition parity and annihilation by the appropriate power of \(M\). Consequently the dimensions of
\(\operatorname{Hom}_{FS_3}(\operatorname{sgn},U_i^\epsilon\otimes U_j^\delta)\), with rows and columns ordered as \(U_2^-,U_3^+,U_3^-\), form exactly
\[
\begin{pmatrix}1&1&1\\1&1&2\\1&2&1\end{pmatrix}.
\]
Set \(k_x=x-1\). The contribution of the \(V\)-fixed block is therefore
\[
\begin{split}
A_{a,b}={}&k_ak_b+k_a(P_b+Q_b)+k_b(P_a+Q_a)\\
&+P_aP_b+2P_aQ_b+2Q_aP_b+Q_aQ_b.
\end{split}
\]
The other three nontrivial \(V\)-characters form a single \(S_3\)-orbit; sign invariants on this orbit are precisely the sign eigenspace for its order-two stabilizer. Hence their combined contribution is \(U_aV_b+V_aU_b\). Proposition 5.1 yields
\[
\dim_F H_4(X_{a,b};F)=A_{a,b}+U_aV_b+V_aU_b.
\]

**4. Compare with characteristic zero.** The same Proposition 5.1 and ordinary character averaging yield
\[
\dim_{\mathbb Q}H_4(X_{a,b};\mathbb Q)
=\frac{d(a)d(b)-6t(a)t(b)+3+8(1-a)(1-b)-6}{24}.
\]
Substituting the displayed formulas for \(k,P,Q,U,V\) shows by expansion, as an exact identity of rational bivariate polynomials, that this equals \(A_{a,b}+U_aV_b+V_aU_b\). The standalone verifier checks the polynomial coefficient identity and the nine modular Hom computations by finite-field linear algebra.

**5. Universal coefficients.** Integral top homology \(H_4(X_{a,b};\mathbb Z)\) is free, being a subgroup of the free top cellular chains of the reduced graph configuration model. The integral universal coefficient theorem gives
\[
\dim_F H_4(X_{a,b};F)-\operatorname{rank}_{\mathbb Z}H_4(X_{a,b};\mathbb Z)
=\dim_F\operatorname{Tor}^{\mathbb Z}_1(H_3(X_{a,b};\mathbb Z),F).
\]
The left side is zero, so the right side is zero; in particular there is no cyclic \(3\)-power summand in \(H_3\). This proves the claim for all \(a,b\ge7\). \(\square\)

## Verification

Run `python3 verify.py` with Python's standard library. It derives the bivariate rational-polynomial identity coefficient by coefficient, constructs the nine small modular Hom spaces from exact linear equations over \(\mathbb F_3\), and checks nonnegative integral multiplicities and equality on all \(1089\) parameter pairs \(7\le a,b\le39\). Its expected final line begins `VERIFY_OK` and records \(1911,5726,16716\) at the first three test pairs. Two independent exploratory calculations also directly constructed the complete modular slot kernels for \(x=7\) and \(x=8\), giving dimensions \(225\) and \(641\) and the predicted \(V\)-isotypical parity profiles; these finite cases are checks, not the general proof.

## Relationship to prior work

An, *Torsion of every finite order in the homology of graph braid groups*, arXiv:2610.04305v1 (first public October 3, 2026), Proposition 5.1 gives the exact slot-Hom description. Theorem 5.10 proves odd-primary vanishing when \(p\ge m\), and Question 8.2(1) explicitly asks whether it remains true for \(p<m\), identifying \(m=4,p=3\) as the first excluded case. The present theorem settles precisely that case throughout the range \(a,b\ge2m-1=7\), using the exceptional modular projective structure of \(S_4\). Earlier chessboard-complex literature concerns homology and representation theory of chessboard complexes themselves, without this four-particle graph-braid torsion conclusion. This result does not assert that a literature search proves uniqueness.

## Limitations

There is no claim about two-primary torsion, three-primary torsion in homological degrees other than three, fewer than four particles, part sizes less than seven, or a full integral homology classification. The calculation relies on the shellability theorem for the \(4\)-row chessboard complex and An's natural slot-module identification; it supplies an independent modular representation argument, not an independent reconstruction of those external theorems. As with other mathematical originality searches, unindexed equivalent results cannot be categorically excluded.

## References

1. B. H. An, *Torsion of every finite order in the homology of graph braid groups*, arXiv:2610.04305v1 (2026-10-03), especially Proposition 5.1, Sections 5.1–5.2, and Question 8.2(1). https://arxiv.org/html/2610.04305v1
2. G. M. Ziegler, shellability theorem for sufficiently rectangular chessboard complexes, as stated and cited in An, Section 5.2.
3. J. Shareshian and M. L. Wachs, *Torsion in the matching complex and chessboard complex*, Advances in Mathematics 212 (2007), 525–570; arXiv:math/0409054 (context for chessboard torsion, not the asserted graph braid calculation).
