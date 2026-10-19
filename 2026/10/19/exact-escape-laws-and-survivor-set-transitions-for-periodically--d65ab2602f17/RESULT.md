# Exact escape laws and survivor-set transitions for periodically alternating holes in the doubling map

## Finding

Let \(T:[0,1)\to[0,1)\) be \(T(x)=2x\bmod 1\). Fix \(h\in[1/4,1]\). At times \(j=0,2,4,\ldots\), remove \(H_j=[0,h]\); at times \(j=1,3,5,\ldots\), remove \(H_j=[1-h,1)\). If initial states have normalized Lebesgue distribution, write \(S_n(h)\) for the probability of avoiding the prescribed hole at all times \(j=0,\ldots,n-1\). Then \(S_0(h)=1\), \(S_1(h)=1-h\), and, for **every integer \(n\ge2\)**,

\[
S_n(h)=2^{-n}\begin{cases}
4h+(2-6h)n,&1/4\le h<1/3,\\
2(1-h),&1/3\le h\le1/2,\\
4-6h,&1/2<h<2/3,\\
0,&2/3\le h\le1.
\end{cases}
\]

The infinite-time survivor set \(K_h=\{x\in[0,1):T^j(x)\notin H_j\text{ for every }j\ge0\}\) has an exact three-phase classification:

\[
K_h=\begin{cases}
\displaystyle\left\{\frac23+\frac{(-1)^{m+1}}{3\cdot2^m}:m=0,1,2,\ldots\right\}\cup\{2/3\},&1/4\le h<1/3,\\
\{2/3\},&1/3\le h<2/3,\\
\varnothing,&2/3\le h\le1.
\end{cases}
\]

In the first regime the survival law has a **strictly positive linear-in-time prefactor**, arising from a nontrivial Jordan block in the two-period transfer operator. At \(h=1/3\), the infinite survivor becomes a singleton and the linear prefactor disappears, while the escape exponent remains \(\log2\). At \(h=1/2\) its prefactor changes expression, and at \(h=2/3\) every state is removed in at most two observations. The full finite-time formula is continuous in \(h\) at all the transition points.

## Assumptions and scope

The holes are **phase-dependent** and fixed in the order left at even times, right at odd times. The parameter \(h\) belongs to \([1/4,1]\), the map uses \(2x\bmod1\), and the initial measure is Lebesgue probability. All intervals and endpoints are as defined above: the two holes are closed at their interior endpoints. Endpoints play no role in finite-time Lebesgue probabilities, but they do determine the infinite survivor set, so that convention is essential. Statements about mixing, stationary escape through a single static hole, and holes with arbitrary switching schedules are not made here.

## Proof

**Step 1: pair reduction.** Two consecutive observations can be grouped under \(G=T^2=4x\bmod1\). Outside an irrelevant finite collection of interval endpoints, survival through one complete pair means \(x\in D_h\), where

\[
D_h=L_h\cup R_h,\quad
L_h=(h,(1-h)/2)\ (h<1/3),\quad
R_h=(\max\{h,1/2\},1-h/2)\ (h<2/3).
\]

Empty intervals are omitted. Indeed, at even time the condition is \(x>h\). On \((0,1/2)\), the additional odd-time condition \(2x<1-h\) gives \(L_h\); on \((1/2,1)\), the condition \(2x-1<1-h\) gives \(R_h\). The hole constraints exclude the boundary values in this formula.

**Step 2: the two-state inverse-branch structure.** Assume \(1/4\le h<1/3\). The inverse branches of \(G\) are \(x=(t+j)/4\), \(j=0,1,2,3\). For \(t\in L_h\), exactly \((t+1)/4\) belongs to \(L_h\), and \((t+2)/4,(t+3)/4\) belong to \(R_h\). For \(t\in R_h\), exactly \((t+2)/4\) belongs to \(R_h\), and no branch belongs to \(L_h\). These assertions follow from the interval bounds and \(1/4\le h<1/3\), and hold except on null endpoints. Therefore the Lebesgue-length vector of \(D_h\cap G^{-k}(D_h)\), split according to membership in \(L_h,R_h\) at the first phase, propagates through the matrix

\[
M=\frac14\begin{pmatrix}1&0\\2&1\end{pmatrix},\qquad
M^k=4^{-k}\begin{pmatrix}1&0\\2k&1\end{pmatrix}.
\]

The starting length vector is

\[
\ell=\begin{pmatrix}(1-3h)/2\\(1-h)/2\end{pmatrix}.
\]

For \(m\ge1\), survival through \(2m\) observations is

\[
S_{2m}(h)=(1,1)M^{m-1}\ell
=4^{-m}[4h+(4-12h)m].
\]

Since \(4^{-m}=2^{-2m}\), this equals the first line in the theorem for \(n=2m\).

**Step 3: odd observation counts.** After \(m\) full pairs, an additional even-phase observation requires \(G^m(x)\in E_h=(h,1)\). Its one-pair pullback is \(D_h\cap G^{-1}(E_h)\). The lengths of the pieces in \(L_h\) and \(R_h\) are respectively

\[
v=\begin{pmatrix}(1-3h)/4\\(1-2h)/2\end{pmatrix}.
\]

Thus, for \(m\ge1\),

\[
S_{2m+1}(h)=(1,1)M^{m-1}v
=4^{-m}[(2m+1)-(6m+1)h]
\]

or, simplifying directly, \(S_{2m+1}(h)=2^{-(2m+1)}[4h+(2-6h)(2m+1)]\). The displayed vector multiplication is the defining exact expression; the final simplified expression is obtained by ordinary algebra. Together with \(S_1=1-h\), this proves all observation counts.

**Step 4: the one-component regimes.** If \(1/3\le h\le1/2\), only \(R_h=(1/2,1-h/2)\) is nonempty, with length \((1-h)/2\). If \(1/2<h<2/3\), only \(R_h=(h,1-h/2)\) is nonempty, with length \((2-3h)/2\). In both cases the only inverse branch of \(G\) taking \(R_h\) back into \(R_h\) is \(t\mapsto(t+2)/4\). Its derivative is \(1/4\), and the terminal single even-time observation keeps exactly half the current interval length. Consequently, respectively,

\[
S_n(h)=2(1-h)2^{-n}\quad\text{and}\quad S_n(h)=(4-6h)2^{-n}\quad(n\ge2).
\]

For \(h\ge2/3\), the one-pair survivor \(D_h\) is empty, giving \(S_n=0\) for all \(n\ge2\). Equality boundaries are covered directly by the closed-hole convention and the limiting length formulas.

**Step 5: infinite survivors.** In the two-component regime the directed inverse-branch graph just established has a persistent \(L\)-loop, a persistent \(R\)-loop, and an \(R\)-to-\(L\) switch, but no \(L\)-to-\(R\) switch. The full intersection \(\bigcap_{m\ge0}G^{-m}D_h\) therefore consists of the infinite persistent \(L\) and \(R\) itineraries and the finitely delayed transitions from \(R\) to \(L\). Solving the branch affine recursions gives the \(G\)-fixed point \(1/3\), the \(G\)-fixed point \(2/3\), and the explicit preimages \(2/3+(-1)^{m+1}/(3\cdot2^m)\) for \(m\ge0\). Every listed point satisfies every phased hole restriction when \(h<1/3\); they are the only such points because the inverse-branch contractions have ratio \(1/4\). The limiting point is \(2/3\). For \(1/3\le h<2/3\), only the unique \(R\)-loop remains and fixes \(2/3\). For \(h\ge2/3\), \(D_h\) is empty. Dyadic preimages of \(0\) cannot survive because their orbits eventually visit the even-time left hole; the listed survivors avoid all forbidden boundary points. This establishes the claimed infinite-time sets.

## Verification

The supplementary `verify.py` uses Python `fractions.Fraction` arithmetic and constructs finite survivors by direct backwards intersection of safe sets under the two inverse branches of \(T\), without using the pair-transition formula. It tests the exact finite-time expression across a rational parameter grid spanning the transition points and all observation lengths up to \(31\), and checks the explicitly classified survivor orbits through finite depths. Running the program in its containing directory prints `VERIFY_OK 3165 exact rational comparisons and orbit checks`. This is finite computational corroboration only; the proof of the all-parameter, all-time statements is analytical above.

## Relationship to prior work

Livorati, Georgiou, Dettmann and Leonel study time-dependent holes for the doubling map, including escape rates using Ulam approximations and orbit-overlap calculations [1]. Their construction and numerical questions motivate the exact two-phase protocol; the closed-form finite-time law and survivor-set transition in this particular endpoint-switching family are not stated in their inspected treatment. Glendinning and Sidorov analyze a *static single interior hole* for the doubling map [2], and Sidorov studies supercritical static holes [3]. Their survivor classifications do not imply the present periodically forced result: phase-dependent exclusion requires a two-step transfer and is not equivalent to one fixed interval. The underlying expanding inverse-branch method is standard; the contribution claimed is the evaluated phase diagram and exact time-dependent survival law for the specified moving holes.

## Limitations

The theorem concerns the prescribed deterministic period-two switching, macroscopic \(h\ge1/4\), and Lebesgue initial states; no result for smaller holes or arbitrary switching protocols is asserted. The survival set is countable in the first regime, a singleton in the second, and empty in the third; no claim is made about invariant physical measures on these nonautonomous survivors. Historical priority is assessed from the cited accessible primary texts and mathematical-index comparisons, not an exhaustive guarantee that every prior general theorem has been considered.

## References

[1] S. Livorati, O. Georgiou, C. P. Dettmann, E. D. Leonel, *Escape through a time-dependent hole in the doubling map*, arXiv:1312.7030 (first publicly posted 2013-12-25), https://arxiv.org/abs/1312.7030 .

[2] P. Glendinning, N. Sidorov, *The doubling map with asymmetrical holes*, arXiv:1302.2486 (2013), https://arxiv.org/abs/1302.2486 .

[3] N. Sidorov, *Supercritical holes for the doubling map*, arXiv:1204.1920 (2012), https://arxiv.org/abs/1204.1920 .
