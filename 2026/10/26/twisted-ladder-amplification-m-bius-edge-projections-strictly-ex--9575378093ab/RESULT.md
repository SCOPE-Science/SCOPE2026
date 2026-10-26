# Twisted-ladder amplification: Möbius edge projections strictly exceed prism projections

## Finding
Let \(M_m\), for every integer \(m\ge3\), be the Möbius ladder on vertices \(\mathbb Z/(2m)\), with all cycle edges \(\{j,j+1\}\) and the \(m\) opposite-vertex edges \(\{j,j+m\}\). Let \(Q_m=C_m\square K_2\) be the ordinary prism on the same numbers of vertices and edges. Write \(P^M_m\) and \(P^Q_m\) for the orthogonal projections of their Euclidean edge-coordinate spaces onto graph-gradient flows. All graph edges have unit conductance.

Set \(r=2-\sqrt3\), \(q=r^{-1}=2+\sqrt3\), and, for \(0\le j\le m\), define
\[
b_j=\frac{r^j-r^{m-j}}{2\sqrt3(1+r^m)},\qquad
p_j=\frac{r^j+r^{m-j}}{2\sqrt3(1-r^m)}.
\]
The exact sharp maximum-coordinate norm on the Möbius ladder is
\[
\boxed{\|P^M_m\|_{\infty\to\infty}=1-\frac1m+\sum_{j=1}^{m-1}\max\!\left\{\frac1m,2|b_j|\right\}+2b_0.}
\]
All \(2m\) cycle-edge rows attain this norm. The rung-edge rows have the exact, generally smaller, sum
\[
R_m=4b_0+2\sum_{j=0}^{m-1}|b_j|.
\]
At \(m=3\), both edge orbits tie at \(17/9\); for every \(m\ge4\), cycle-edge rows strictly dominate rung rows. Thus amplification strictly exceeds two precisely from \(m=4\) onward: the first case has eight vertices and norm \(29/14\). Every finite norm is less than three, and
\[
3-\|P^M_m\|_{\infty\to\infty}=\frac{2\log m}{m\log(2+\sqrt3)}+O(m^{-1}).
\]

**Sharp twist comparison.** For every integer \(m\ge3\),
\[
\boxed{\|P^M_m\|_{\infty\to\infty}>\|P^Q_m\|_{\infty\to\infty}.}
\]
Moreover, for positive integers \(h\to\infty\),
\[
\boxed{\|P^M_{2h}\|-\|P^Q_{2h}\|=\frac{2}{\sqrt3}r^h+o(r^h),}
\]
\[
\boxed{\|P^M_{2h+1}\|-\|P^Q_{2h+1}\|=\frac{1+r}{\sqrt3}r^h+o(r^h).}
\]
Norm subscripts in these last two displays are \(\infty\to\infty\). Every sharp norm is attained by a sign-valued edge vector.

## Assumptions and scope
All spaces are real finite-dimensional coordinate spaces with the usual \(\ell^\infty\) norm. Given an arbitrary orientation, let \(B\) be the edge-by-vertex incidence matrix. The projection is \(P=B(B^{\mathsf T}B)^\dagger B^{\mathsf T}\), with Moore–Penrose pseudoinverse. Reversing an edge changes only a coordinate sign, so operator norms are orientation-independent. All quantifiers above hold for every integer \(m\ge3\); no weighted or irregular ladders are claimed.

## Proof
**1. Periodic and antiperiodic Green functions.** Pair vertex \(j\) with its antipode \(j+m\). The vertex Laplacian splits orthogonally into the symmetric sector, where the relevant \(m\)-cycle Laplacian is \(2I-S-S^{-1}\), and the antisymmetric sector, where it is \(4I-S_a-S_a^{-1}\); \(S_a\) is the antiperiodic shift (the wrap edge carries a negative sign). In the antisymmetric sector, the Green function at source zero is \(b_j\) above, extended by \(b_{j+m}=-b_j\). Indeed, \(4b_j-b_{j-1}-b_{j+1}=0\) at interior indices, \(4b_0-2b_1=1\), and the antiperiodic boundary identities hold. These facts follow directly from \(r^2-4r+1=0\). The massive periodic Green function for the prism is \(p_j\), extended \(m\)-periodically; it satisfies the analogous recurrence and \(4p_0-2p_1=1\). Both inverses are unique because the respective matrices are positive definite. The massless symmetric sector has cycle-edge projection entries \(\delta_{j0}-1/m\).

**2. Exact transfer-current row sums.** Orient each Möbius cycle edge forward around the \(2m\)-cycle and each rung from \(j\) to \(j+m\), \(0\le j<m\). For a chosen cycle edge, its two cycle-edge coefficients above opposite copies of index \(j\) are half the sum and difference of \(\delta_{j0}-1/m\) and \(d_j\), where \(d_0=2(b_0-b_1)\) and \(d_j=-2b_j\) for \(1\le j<m\). Their combined absolute value is \(\max\{|\delta_{j0}-1/m|,|d_j|\}\). Since \(0<d_0<1-1/m\) for all \(m\ge3\), the \(j=0\) contribution is \(1-1/m\). The coefficients at rungs telescope in absolute value to \(2b_0\), because \(b_j\) decreases strictly over \(0\le j\le m\) and satisfies \(b_m=-b_0\). This proves the displayed cycle-row formula. A rung row has two opposing cycle copies whose combined sum is \(4b_0\), and rung-rung entries \(2b_j\), proving the formula for \(R_m\). Rotation and antipodal symmetry reduce all edges to these two row classes. An operator on finite \(\ell^\infty\) attains its induced norm on a rowwise sign input, proving sharpness.

**3. Which edge maximizes; the first norm above two.** Put \(A_m=\sum_{j=1}^{m-1}|b_j|\). The cycle-row formula gives \(S_m\ge2-2/m+2b_0\), while \(R_m=6b_0+2A_m\). Since \(b_0<1/(2\sqrt3)\) and \(A_m<r/[\sqrt3(1-r)]\),
\[
S_m-R_m>1-\frac2m-\frac1{\sqrt3}>0\quad(m\ge5).
\]
Direct exact calculations give \((S_3,R_3)=(17/9,17/9)\) and \((S_4,R_4)=(29/14,2)\). Also \(b_0\ge b_0|_{m=4}=2/7\) when \(m\ge4\), so \(S_m\ge2-2/m+2b_0>2\). The \(m=3\) value is below two.

**4. Prism formula.** In the ordinary prism, the symmetric sector is unchanged and the antisymmetric sector is periodic rather than antiperiodic. Let \(h=\lfloor m/2\rfloor\). The same edge-row calculation yields
\[
H_m=1-\frac1m+\sum_{j=1}^{m-1}\max\!\left\{\frac1m,2p_j\right\}+2(p_0-p_h),\qquad V_m=1+4(p_0-p_h).
\]
Here \(V_m\) is the rung row, and \(H_m\) the cycle row. At \(m=3\), \((H_m,V_m)=(26/15,9/5)\), and at \(m=4\) both equal two. For \(m\ge5\),
\[
H_m-V_m\ge1-2/m-2p_0>0,
\]
since \(p_0\) decreases in \(m\) and \(2p_0|_{m=5}<3/5\). Hence the prism norm is \(H_m\) for \(m\ge4\).

**5. Strict twist amplification.** Since \(p_j>|b_j|\) for every \(j\), comparing the two cycle-row formulas gives
\[
S_m-H_m=2(b_0-p_0+p_h)-\sum_{j=1}^{m-1}\left[\max\{1/m,2p_j\}-\max\{1/m,2|b_j|\}\right].
\]
For \(m\ge4\), put \(h=\lfloor m/2\rfloor\). The one or two central indices, at distance \(h\) from zero, satisfy \(2p_h<1/m\), by the geometric formulas and monotonicity of \(mr^{\lfloor m/2\rfloor}\); so their bracket vanishes. Other indices pair by reflection. Since the function \(x\mapsto\max\{1/m,2x\}\) is increasing and 2-Lipschitz, the total bracket is bounded above by \(4\sum_{j=1}^{h-1}(p_j-b_j)\), where
\[
p_j-b_j=\frac{r^{m-j}+r^{m+j}}{\sqrt3(1-r^{2m})}\quad(1\le j<h).
\]
For even \(m=2h\), the leading positive term is exactly
\[
2(b_0-p_0+p_h)=\frac{2r^h(1-2r^h)}{\sqrt3(1-r^{2h})}.
\]
The ratio of the above geometric upper bound for the bracket to this positive term is strictly smaller than
\[
\frac{2r}{1-r}\frac{1+r^2}{1-2r^2}<1\qquad(h\ge2).
\]
For odd \(m=2h+1\) and \(h\ge2\), the positive term and the geometric penalty are respectively bounded below and above by
\[
\frac{r^h[(1+r)(1+r^{2h+1})-4r^{h+1}]}{\sqrt3(1-r^{4h+2})},
\quad
\frac{4r^{h+2}(1+r^h)}{\sqrt3(1-r)(1-r^{4h+2})}.
\]
The first exceeds the second because \(1+r-4r^3>4r^2(1+r^2)/(1-r)\). The remaining \(m=3\) comparison is \(17/9>9/5\). This proves strict domination for all \(m\).

**6. Asymptotic effects.** The preceding bracket vanishes except for indices whose distance from zero is \(O(\log m)\), because \(p_j\le C r^{\min(j,m-j)}\). At such indices \(p_j-|b_j|=O(r^{m-\min(j,m-j)})\). Summation gives a bracket of \(O(m\log m\,r^m)=o(r^{\lfloor m/2\rfloor})\). Expanding the explicit positive term in step 5 proves the two parity-sharp difference formulas.

For the overall norm, the set of \(j\) satisfying \(2|b_j|>1/m\) consists of two endpoint blocks of common length \(k_m=\log_q(m/\sqrt3)+O(1)\). Consequently
\[
S_m=2-\frac{2(k_m+1)}m+2b_0+4\sum_{j=1}^{k_m}b_j,
\]
and the last two terms equal \(1+O(m^{-1})\) by geometric summation. This yields the claimed logarithmic deficit. Finally, the periodic massive Green function satisfies \(p_j>|b_j|\) and \(\sum_{j=0}^{m-1}p_j=1/2\). Thus \(\sum|b_j|<1/2\), and \(S_m<3-2/m<3\). The rung-row formula also gives \(R_m<3\).

## Verification
Run `python check.py` with SymPy installed. It constructs the incidence and Laplacian matrices independently, computes all edge-projection rows over the exact rationals for each \(3\le m\le12\), and checks the derived Green, row-sum, maximizing-orbit, threshold, strict twist inequality, and endpoint-block formulas. This is a finite consistency check; the all-size statements and parity limits are established in the proof. Sign-vector attainment follows algebraically from the row-sum formula and does not require numerical optimization.

## Relationship to prior work
Jiang–Lim–Yao–Ye (arXiv:0811.1067, initially posted 2008-11-07) established the least-squares graph-Hodge decomposition. Kassel–Wu (arXiv:1312.2946) developed transfer-current methods. Cinkir (arXiv:1503.06353) computed resistances for open ladders. Most directly, Azimi–Farrokhi (arXiv:2306.10497, §4–5, especially Theorem 5.1 and Corollary 5.4) gave explicit Moore–Penrose inverses for both Möbius and ordinary circular ladders. Those known inverses are a critical starting point, not claimed as new here. Their results do not state the induced maximum-coordinate norm, the all-size strict norm comparison between the two topologies, the eight-vertex threshold, or the sharp parity-dependent exponential difference. The present argument supplies the necessary absolute-value row optimization and comparison estimates. An equivalent interpretation via determinantal spanning-tree transfer currents is possible.

## Limitations
The result concerns equal-conductance, real, finite graph-gradient orthoprojections only, not minimum-norm projections among all projections, arbitrary conductances, or other operator norms. Existing full pseudoinverse formulas imply that its exact finite norms can be computed; the new mathematical assertion is the explicit sharp norm classification together with the strict all-size twist inequality and its parity asymptotics. Other formulations of the same comparison might exist; historical priority is not established by a negative search alone. No independent audit is claimed.

## References
1. X. Jiang, L.-H. Lim, Y. Yao, Y. Ye, *Statistical ranking and combinatorial Hodge theory*, arXiv:0811.1067 (2008), Mathematical Programming 127 (2011), 203–244.
2. A. Kassel, W. Wu, *Transfer current and pattern fields in spanning trees*, arXiv:1312.2946 (2013).
3. Z. Cinkir, *Effective Resistances, Kirchhoff index and Admissible Invariants of Ladder Graphs*, arXiv:1503.06353 (2015).
4. A. Azimi, M. Farrokhi Derakhshandeh Ghouchan, *Explicit formulas for matrices associated to ladder, circular ladder, and Möbius ladder graphs*, arXiv:2306.10497 (2023), especially §4–5.
