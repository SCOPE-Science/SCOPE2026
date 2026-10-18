# Exact rank-one Fourier support spectrum of the rotational octahedral group

## Finding
Let \(G\) be the rotational octahedral group of order \(24\), isomorphic to \(S_4\), and let \(\rho:G\to\mathrm{SO}(3)\) be its natural three-dimensional irreducible representation. For nonzero vectors \(u,v\in\mathbb C^3\), consider the rank-one matrix coefficient
\[
f_{u,v}(g)=u^{\mathsf T}\rho(g)v.
\]
Then the **complete attainable time-support spectrum** is
\[
\boxed{\bigl\{|\operatorname{supp}f_{u,v}|:u,v\in\mathbb C^3\setminus\{0\}\bigr\}
=\{8,12,16,18,20,21,22,23,24\}.}
\]
Every number in this set is attained. The same set holds for the other irreducible three-dimensional representation of \(S_4\), obtained by tensoring with the sign character. Each coefficient has exactly one nonzero rank-one Fourier block, so its rank-weighted Fourier support is \(3\).

The spectrum has genuine gaps above its sharp uncertainty minimum. For example, support sizes \(19\), \(17\), and \(13\) cannot occur, even though the rank-weighted uncertainty inequality alone only requires a support of at least \(8\). The odd size \(21\) occurs through an explicit cubic-root-of-unity configuration.

## Assumptions and scope
We work over \(\mathbb C\), using *bilinear* matrix coefficients, not a positivity assumption. The group is the set of determinant-one signed permutation matrices:
\[
G=\{\rho(\pi,\varepsilon)=\operatorname{diag}(\varepsilon_1,\varepsilon_2,\varepsilon_3)P_\pi:
\pi\in S_3,\ \varepsilon_i\in\{\pm1\},\ \varepsilon_1\varepsilon_2\varepsilon_3=\operatorname{sgn}(\pi)\}.
\]
We choose \((P_\pi v)_i=v_{\pi(i)}\). There are exactly four sign choices for each of six permutations. The group permutes the four unoriented body diagonals of a cube faithfully and hence is isomorphic to \(S_4\). Its defining complex representation is irreducible: diagonal determinant-one sign matrices have distinct joint coordinate characters, while coordinate three-cycles permute the three coordinate spaces transitively. Thus the only invariant subspaces are \(0\) and \(\mathbb C^3\).

For a finite group, use the normalization
\[
\widehat f(\tau)=\frac1{|G|}\sum_{g\in G}f(g)\tau(g^{-1}),\qquad
\sigma(f)=\sum_{\tau\in\widehat G}(\dim\tau)\operatorname{rank}\widehat f(\tau).
\]
Schur orthogonality gives \(\widehat f_{u,v}(\rho)=\tfrac13vu^{\mathsf T}\) and every inequivalent Fourier block is zero; hence \(\sigma(f_{u,v})=3\). The theorem concerns this **pure irreducible, rank-one stratum**, not arbitrary sums of Fourier blocks whose combined rank-weighted size happens to equal \(3\).

## Proof
**1. Four sign equations per permutation.** For each \(\pi\in S_3\), put \(X=u_1v_{\pi(1)}\), \(Y=u_2v_{\pi(2)}\), \(Z=u_3v_{\pi(3)}\). After dividing the four allowed signs by their first entry (which does not affect vanishing), the corresponding four coefficient values have the same zeros as
\[
L_{\pi,\eta,\theta}=X+\eta Y+\theta Z,
\qquad \eta,\theta\in\{\pm1\}.
\]
Write \(N\) for the number of zeros among all \(24\) coefficient values. Then \(|\operatorname{supp}f_{u,v}|=24-N\).

**2. Coordinates with small support.** Write \(r=|\operatorname{supp}u|\) and \(s=|\operatorname{supp}v|\), where support now refers to their three coordinates. By interchanging the vectors and inverting the group matrices, we may assume \(r\le s\).

If \(r=s=1\), exactly four permutations send the nonzero coordinate of \(u\) to a zero coordinate of \(v\); their four sign choices all vanish, giving \(N=16\). If \((r,s)=(1,2)\), exactly two permutations give four zeros each, so \(N=8\). If \((r,s)=(1,3)\), every coefficient has one nonzero summand, so \(N=0\).

If \((r,s)=(2,2)\), exactly two permutations map both nonzero coordinates of \(u\) into those of \(v\). Each such permutation has either zero or two vanishing sign choices, and all other permutations have none. Consequently \(N\in\{0,2,4\}\).

If \((r,s)=(2,3)\), label the two nonzero coordinates of \(u\) by \(a,b\) and define
\[
R=(u_a/u_b)^2,\qquad B_j=v_j^2\in\mathbb C^\times.
\]
For each ordered pair \((i,j)\) of distinct indices of \(v\) there is exactly one coordinate permutation mapping \((a,b)\) to \((i,j)\). It contributes exactly two zeros when \(B_j=RB_i\), and none otherwise. Thus
\[
N=2m,\qquad m=\#\{(i,j):i\ne j,\ B_j=RB_i\}.
\]
Here \(0\le m\le6\), but \(m=5\) is impossible. Indeed five of the six directed edges on three vertices necessarily contain a directed three-cycle and a bidirectional pair. Multiplying the respective relations yields \(R^3=R^2=1\), hence \(R=1\). The five relations then force all three \(B_j\) equal, so the sixth also holds, a contradiction. Therefore \(N\in\{0,2,4,6,8,12\}\). This covers all cases where at least one of \(u,v\) has a zero coordinate.

**3. All six coordinates nonzero.** Now \(r=s=3\). For each permutation, no two of the four sign equations can simultaneously vanish: subtracting two distinct equations would force at least one of \(X,Y,Z\) to be zero. Thus each permutation contributes at most one zero and \(0\le N\le6\).

Set \(a_i=u_i^2\), \(b_j=v_j^2\), and define the quartic sign product
\[
Q_\pi=\prod_{\eta,\theta\in\{\pm1\}}
\bigl(X+\eta Y+\theta Z\bigr)
=\sum_{i=1}^3 a_i^2 b_{\pi(i)}^2
-2\sum_{1\le i<j\le3}a_i a_j b_{\pi(i)}b_{\pi(j)}.
\]
The crucial alternating identity is
\[
\boxed{\sum_{\pi\in S_3}\operatorname{sgn}(\pi)Q_\pi=0.}
\]
It holds term by term: for each fixed \(i\), the assignments of the two other indices cancel in the first sum; for each fixed unordered pair \(\{i,j\}\), interchanging their assigned indices changes permutation parity but preserves the product in the second sum. Therefore, if five permutations had a zero sign value, their five quartics would vanish and the identity would force the sixth quartic to vanish as well. Exactly five zeros are impossible. Hence
\[
N\in\{0,1,2,3,4,6\}
\]
when all coordinates of both vectors are nonzero.

**4. Exhaustive attainment.** Write \(\omega\) for a primitive third root of unity, with \(1+\omega+\omega^2=0\). The following table lists an explicit vector pair for every attainable zero count; substitution into the four sign equations is exact:

| \(N\) | \(u\) | \(v\) | \(24-N\) |
|---:|---|---|---:|
| 0 | \((1,1,1)\) | \((1,1,1)\) | 24 |
| 1 | \((1,2,3)\) | \((1,2,4)\) | 23 |
| 2 | \((1,1,2)\) | \((1,2,3)\) | 22 |
| 3 | \((1,\omega,\omega^2)\) | \((1,\omega,\omega^2)\) | 21 |
| 4 | \((1,1,2)\) | \((1,1,3)\) | 20 |
| 6 | \((1,1,1)\) | \((1,1,2)\) | 18 |
| 8 | \((1,0,0)\) | \((1,1,0)\) | 16 |
| 12 | \((1,1,0)\) | \((1,1,1)\) | 12 |
| 16 | \((1,0,0)\) | \((1,0,0)\) | 8 |

In the \(N=3\) row, the three cyclic coordinate permutations contribute one zero each and the three opposite-parity permutations contribute none. The union of the possibilities in Steps 2 and 3 is exactly \(\{0,1,2,3,4,6,8,12,16\}\); taking complements in \(24\) proves the theorem. Tensoring the representation with any one-dimensional character multiplies each value by a nonzero scalar and preserves its support. \(\square\)

## Verification
The accompanying `check_s4_support.py` uses only the Python standard library and exact arithmetic in \(\mathbb Z[\omega]\), representing \(a+b\omega\) by integer pairs. It constructs every one of the \(24\) group matrices, checks their determinant-one signs and the full matrix-coefficient orthogonality relations, verifies all nine support-size witnesses, and checks instances of the alternating quartic identity in the exact cyclotomic ring.

Run: `python3 check_s4_support.py`. The verified output has nine distinct support sizes (\(8,12,16,18,20,21,22,23,24\)) followed by `all exact group, Fourier, witness, and parity tests passed`. The impossibility claims are proved algebraically above, not inferred from finite sampling.

## Relationship to prior work
Alagic and Russell, *Uncertainty Principles for Compact Groups* (arXiv:math/0608702, first publicly posted August 28, 2006), prove the rank-weighted finite-group uncertainty bound \(|\operatorname{supp}f|\sigma(f)\ge |G|\). Applied here, it yields only \(|\operatorname{supp}f|\ge8\); it does not determine the eight larger attainable support sizes or exclude the intervening integers. Their discussion of subgroup indicators addresses extremal behavior rather than this rank-one pure-block spectrum.

Jiang, Liu, and Wu, *Noncommutative Uncertainty Principles* (arXiv:1408.1165, first publicly posted August 6, 2014), study general noncommutative inequalities and equality minimizers. Their minimizer classification does not imply the full nonextremal spectrum obtained here. Standard descriptions of octahedral rotations give the signed-permutation representation but do not provide the support classification.

The distinction from Fourier-support tables on abelian groups is essential: the present observable comes from a **single rank-one noncommutative Fourier block**, and the proof uses the alternating identity across the six coordinate permutations.

## Limitations
This is an exact theorem for the two three-dimensional irreducible blocks of the order-\(24\) group, not a classification for arbitrary functions on \(S_4\), for every rank-weighted support size, or for higher-order symmetric groups. No stability estimate or numerical conditioning theorem is claimed. The literature comparison rules out the inspected general inequalities and minimizer theorems as implications, not every possible unpublished or uncatalogued classification. Independent mathematical validation has not been performed.

## References
1. Gorjan Alagic and Alexander Russell, *Uncertainty Principles for Compact Groups*, arXiv:math/0608702 (first version August 28, 2006), https://arxiv.org/abs/math/0608702.
2. Chunlan Jiang, Zhengwei Liu, and Jinsong Wu, *Noncommutative Uncertainty Principles*, arXiv:1408.1165 (first version August 6, 2014), https://arxiv.org/abs/1408.1165.
3. *Octahedral Group*, Wolfram MathWorld, https://mathworld.wolfram.com/OctahedralGroup.html (group identification and rotation structure; no publication date inferred).
