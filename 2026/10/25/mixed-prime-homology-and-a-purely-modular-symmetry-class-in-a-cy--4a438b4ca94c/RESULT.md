# Mixed-prime homology and a purely modular symmetry class in a cyclic chessboard quotient

## Finding
Let \(\Delta_{5,5}\) be the ordinary simplicial complex of nonattacking rook placements on a five-by-five board. The order-five group \(C_5\) acts by cyclically shifting columns, and let \(Y=|\Delta_{5,5}|/C_5\). Then
\[
\pi_1(Y)\cong C_5,\qquad
H_i(Y;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z/5,&i=1,\\
\mathbb Z/3,&i=2,\\
\mathbb Z^{12},&i=3,\\
0,&i\ge4.
\end{cases}
\]
The row-permutation group \(S_5\) acts on \(Y\). Fix the generator of \(C_5\) that advances every column by one, and let \(u\in H^1(Y;\mathbb F_5)\) classify the corresponding covering. If \(\beta_{\mathbb Z}\) is the integral Bockstein, then
\[
w=u\smile\overline{\beta_{\mathbb Z}u}\ \in H^3(Y;\mathbb F_5)
\]
is a **nonzero \(S_5\)-fixed class**, whereas
\[
H^3(Y;\mathbb Q)^{S_5}=0.
\]
Thus this natural quotient has adjacent-degree torsion at two different primes and a genuinely modular symmetry-invariant cohomology class without a rational invariant counterpart.

For completeness, the character of \(S_5\) on \(H_3(Y;\mathbb Q)\) is as follows:

| Cycle type | Class size | Homology trace |
| --- | ---: | ---: |
| \((1,1,1,1,1)\) | 1 | 12 |
| \((2,1,1,1)\) | 10 | -2 |
| \((2,2,1)\) | 15 | 0 |
| \((3,1,1)\) | 20 | 3 |
| \((3,2)\) | 20 | 1 |
| \((4,1)\) | 30 | 0 |
| \((5)\) | 24 | -3 |

## Assumptions and scope
Use row and column coordinates in \(\mathbb Z/5\mathbb Z\). A simplex is a collection of cells with no repeated row or column. The generator of \(C_5\) sends \((r,c)\) to \((r,c+1)\). Row permutations commute with this action and induce the stated \(S_5\)-action on the quotient. All integral homology and cohomology groups have ordinary, unreduced conventions. The statement concerns exactly this five-by-five board, not a general family of sizes.

## Proof
**Free covering and fundamental group.** Every nonempty rook placement has trivial stabilizer under a nonidentity column shift: a fixed placement containing \((r,c)\) would have to contain another rook in row \(r\). Consequently the action is free on the geometric realization. The standard chessboard connectivity bound gives that \(\Delta_{5,5}\) is simply connected; with this free action its quotient is covered universally with deck group \(C_5\), so \(\pi_1(Y)=C_5\).

**Integral cellular chains.** Order each matching by increasing row. From every column-translation orbit, take the unique representative whose rook in the least row has column zero. For an oriented \(j\)-cell \(\sigma=((r_0,c_0),\ldots,(r_j,c_j))\), set
\[
\partial_j[\sigma]=\sum_{a=0}^j(-1)^a
[\operatorname{norm}(\sigma\setminus\{(r_a,c_a)\})].
\]
Column shifts preserve the increasing-row orientation, so this is the integral cellular boundary of the quotient. The exhaustive orbit counts in dimensions zero through four are \((5,40,120,120,24)\). Exact integer Smith reduction yields the following nonzero invariant factors:
\[
\begin{array}{c|c}
\partial_1&1^{\times4}\\
\partial_2&1^{\times35},\ 5\\
\partial_3&1^{\times83},\ 3\\
\partial_4&1^{\times24}.
\end{array}
\]
Their ranks are \((4,36,84,24)\); direct multiplication gives \(\partial^2=0\). Since every kernel of a homomorphism between free abelian groups is primitive, these Smith factors, together with the chain ranks, give all the asserted integral homology groups. In particular, the third reduced homology has rank \(120-84-24=12\) and no torsion. A separate structural check is that every four-rook placement extends uniquely to a five-rook placement; the top boundary has disjointly supported columns containing coefficients of absolute value one, hence primitive image.

**A modular class and an explicit witness.** Orient edges by increasing row. For a canonical edge whose two columns are \((0,c)\), choose the integer lift \(U(\sigma)=c\in\{1,2,3,4\}\) of the covering cocycle \(u\). The coboundary of \(U\) is divisible by five; the integer two-cocycle \(B=(\delta U)/5\) represents \(\beta_{\mathbb Z}u\). The Alexander–Whitney representative of \(w\) on an ordered four-rook simplex is
\[
w(v_0,v_1,v_2,v_3)=U(v_0,v_1)\,B(v_1,v_2,v_3)\pmod5,
\]
where each face is normalized before evaluation. Fix rows \(0,1,2,3\). Sum the 24 normalized four-rook simplices on those rows, giving each the sign of the permutation of the five columns formed by its four used columns followed by its unique unused column. Call this integral three-chain \(z\). Every three-rook face has two completions with opposite signs, so \(\partial z=0\). Explicit summation with the above formulas gives
\[
\langle w,z\rangle=2\pmod5,
\]
hence \(w\neq0\). Each row permutation commutes with deck translation and therefore fixes \(u\) in cohomology; naturality of the Bockstein and cup product shows that \(w\) is \(S_5\)-fixed.

**Absence of rational fixed vectors.** For each row permutation, count its signed fixed quotient cells and form the ordinary cellular Lefschetz number. Since rational homology is concentrated in degrees zero and three, the degree-three trace equals one minus that Lefschetz number. The seven resulting traces are tabulated above. Their class-size-weighted sum is
\[
12+10(-2)+15(0)+20(3)+20(1)+30(0)+24(-3)=0.
\]
Dividing by \(|S_5|=120\) gives zero multiplicity of the trivial rational representation. Rational homology and cohomology have equal characters, so the rational invariant cohomology vanishes.

## Verification
Run `python3 check.py` with Python, NumPy and SymPy. The standalone checker enumerates all 1,545 nonempty rook placements, confirms every column-shift orbit has size five, constructs all quotient matrices, checks \(\partial^2=0\), and computes their exact integer Smith factors. Independent finite-field elimination at primes \(2,3,5,7,11\) verifies the predicted ranks. It further constructs the 24-cell integral cycle \(z\), checks its boundary and the mod-five pairing, and evaluates the signed cellular Lefschetz numbers for all 120 row permutations. This finite exhaustive computation is part of the proof for this particular board, not an assertion about larger boards.

## Relationship to prior work
Jojić, Panina, Vrećica and Živaljević develop the chessboard-complex and discrete-Morse framework. Shareshian and Wachs establish the three-primary torsion of the unquotiented \(\Delta_{5,5}\), and Reiner and Roberts determine rational symmetric-group representations for ordinary chessboard complexes. In particular, the intrinsic order-three class is already known; its mere existence is not claimed as new. Those statements concern the unquotiented complex or its characteristic-zero representations and do not directly state the integral homology and the modular-versus-rational symmetry comparison for this specific free column-translation quotient. The quotient computation and explicit modular class are the subject of the present result.

## Limitations
No claim is made about a complete homotopy type, integral \(S_5\)-module decomposition, or analogous quotients for other board sizes. Some aspects of the calculation (notably the fundamental group and the three-primary part) follow from classical connectivity and transfer arguments; the precise integral quotient chains, complete homology and symmetry-character contrast are separately established here. A search of accessible primary sources and indexed findings found no equivalent full statement; absence of a match is not a proof of global novelty.

## References
1. D. Jojić, G. Panina, S. T. Vrećica, R. T. Živaljević, *Generalized chessboard complexes and discrete Morse theory*, first publicly available 2020-03-09, arXiv:2003.04018, https://arxiv.org/abs/2003.04018.
2. J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, 2004 preprint arXiv:math/0409054, https://arxiv.org/abs/math/0409054; see the five-by-five entry in Table 1.2 and Section 5.
3. V. Reiner and J. Roberts, *Minimal Resolutions and the Homology of Matching and Chessboard Complexes*, Journal of Algebraic Combinatorics 11 (2000), Theorem 1.3, DOI:10.1023/A:1008728115910.
