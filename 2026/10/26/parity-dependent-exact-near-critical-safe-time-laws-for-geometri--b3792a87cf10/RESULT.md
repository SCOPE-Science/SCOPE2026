# Parity-dependent exact near-critical safe-time laws for geometric runner speeds

## Finding
For every integer \(b\ge2\) and horizon \(m\ge2\), consider simultaneous avoidance of integers by the geometric speeds \(1,b,\ldots,b^{m-1}\). The exact *near-critical* safe-time measure exhibits a sharp parity dichotomy.

For odd \(b\ge3\) and \((b-1)/(2b)\le\delta<1/2\),
\[
G_m(b,\delta)=\frac{1-2\delta}{b^{m-1}}.
\]
The safe-time set is a single open interval centered at \(1/2\).

For even \(b\ge2\) and \((b-1)/(2b)\le\delta<b/(2(b+1))\),
\[
G_m(b,\delta)=\frac{1-2(b+1)\delta/b}{b^{m-2}}
=\frac{2(b+1)}{b^{m-1}}\left(\frac{b}{2(b+1)}-\delta\right).
\]
The safe-time set consists of precisely two nonempty open intervals, reflected in \(1/2\). In either parity, \(G_{m+1}/G_m=1/b\) throughout the stated range. Hence conditional on survival for two steps (one step for odd \(b\)), the first subsequent failed step has an exact geometric law with continuation probability \(1/b\) and failure probability \(1-1/b\).

For every \(m\ge2\), the sharp largest achievable distance \(\sup_{t\in\mathbb R/\mathbb Z}\min_{0\le j<m}\|b^jt\|\) is \(1/2\) if \(b\) is odd (unique maximizer \(t=1/2\)); it is \(b/[2(b+1)]\) if \(b\) is even (exactly two maximizers \(t=b/[2(b+1)]\) and \(1-b/[2(b+1)]\)). These are non-strict boundary statements: at the critical distance, the strict safe-time set is empty.

## Assumptions and scope
Here \(b\) and \(m\) are integers, \(b\ge2\), \(m\ge2\). We identify \(\mathbb R/\mathbb Z\) with the circle of circumference one and write \(\|x\|\) for distance to the nearest integer. For real \(\delta\in[0,1/2]\), put
\[
S_m(b,\delta)=\{t\pmod1:\|b^jt\|>\delta\text{ for all }0\le j<m\},\qquad G_m(b,\delta)=\operatorname{Leb}(S_m(b,\delta)).
\]
The claimed formulas hold only on the explicitly displayed parameter strips. No claim is made for the complete threshold profile below \((b-1)/(2b)\).

## Proof
Write \(T(t)=bt\pmod1\), and \(J=(\delta,1-\delta)\). Then \(S_m=\bigcap_{j=0}^{m-1}T^{-j}J\), with \(S_{m+1}=J\cap T^{-1}S_m\).

**Odd case.** Put \(b=2r+1\) and suppose \(\delta\ge(b-1)/(2b)\). Every \(t\in J\) lies inside the single monotonicity strip \((r/b,(r+1)/b)\), on which \(T(t)=bt-r\). The unique fixed point in this strip is \(t=1/2\). Its affine inverse \(f(y)=(r+y)/b\) carries \(J\) strictly inside \(J\). Consequently \(S_m=f^{m-1}(J)\), exactly one open interval centered at \(1/2\) and of length \((1-2\delta)b^{-(m-1)}\). At the boundary \(\delta=1/2\), only \(t=1/2\) realizes the non-strict bound; since no distance can exceed \(1/2\), the sharpness and uniqueness follow.

**Even case.** Put \(b=2r\) and \(\delta_0=(b-1)/(2b)\), \(\delta_*=b/(2(b+1))\). For \(\delta_0\le\delta<\delta_*\), the interval \(J\) lies in the union of the central two monotonicity strips, carrying translations \(bt-(r-1)\) and \(bt-r\). Directly intersecting \(J\) with its one-step preimage gives precisely
\[
S_2=I_L\cup I_R,\quad I_L=(\delta,1/2-\delta/b),\quad I_R=(1/2+\delta/b,1-\delta).
\]
Both intervals have length \(\ell_2=1/2-(1+1/b)\delta>0\). For \(t\in I_L\) one has \(T(t)>1/2\), and for \(t\in I_R\) one has \(T(t)<1/2\); these statements use exactly \(\delta\ge\delta_0\), and the endpoints are excluded. Write the relevant inverse branches as \(f_L(y)=(r-1+y)/b\) and \(f_R(y)=(r+y)/b\). Within \(J\), a point whose image lies in \(S_2\) must belong to \(f_L(I_R)\) or \(f_R(I_L)\), and these intervals are respectively contained in \(I_L\) and \(I_R\). Inductively, if \(S_m=L_m\cup R_m\) consists of intervals in \(I_L,I_R\), then
\[
S_{m+1}=f_L(R_m)\cup f_R(L_m).
\]
Thus for each \(m\ge2\) there are exactly two intervals, each length \(\ell_2/b^{m-2}\). The stated measure is \(2\ell_2/b^{m-2}\).

At \(\delta=\delta_*\), the closed-inequality version of \(S_2\) consists of exactly the two common endpoints of the shrinking intervals, \(t_*=\delta_*\) and \(1-t_*\). Indeed the same preimage-interval calculations are valid with closed endpoints at equality. Direct substitution gives \(T(t_*)=1-t_*\) and \(T(1-t_*)=t_*\). These two points therefore attain distance \(\delta_*\) at every horizon; there is no point attaining a larger distance, since its first two distances would exceed \(\delta_*\), for which \(S_2\) is empty. Equality at horizon two allows only these two points, establishing uniqueness for every \(m\ge2\).

Finally the ratio \(G_{m+1}/G_m=1/b\) follows in both cases. Nested survivor events under uniform Lebesgue initial time give the stated geometric conditional first-exit law, without any independence assumption.

## Verification
The accompanying `verify.py` independently intersects the exact rational preimages \(T^{-j}(J)\) for all tested horizons, rather than invoking the interval recursion proved above. It compares component counts and exact rational lengths against the displayed formulas, including both lower parameter endpoints and odd/even critical boundaries. All computations are rational and finite; the universal claim follows from the affine inverse-branch proof.

## Relationship to prior work
Hu and Jing, *Near optimal gap in the Lonely Runner Conjecture* (arXiv:2610.23790, publicly posted 2026-10-16), give a uniform near-optimal loneliness guarantee and positive safe-time density for arbitrary distinct integral speeds. Their general results do not determine the near-critical measure at every horizon for the geometric speed family, or the odd/even exact escape law. Glendinning and Sidorov, *The doubling map with asymmetrical holes* (arXiv:1302.2486), classify infinite survivor-set and Hausdorff-dimension transitions for the doubling map with a single interval hole; the present finite-horizon formulas concern avoidance of the complementary two-end hole and all integer bases. Such symbolic dynamical methods can in principle imply special cases, and unstated classical equivalence remains an originality risk.

## Limitations
The exact lengths cover only the near-critical parameter windows stated, not smaller thresholds, arbitrary nongeometric speeds, or mixed multipliers. The escape law refers to Lebesgue-uniform starting times conditioned on survival and is not an assertion of independence of successive events. Prior implicit derivations of these elementary affine formulas cannot be completely excluded.

## References
1. Z. Hu and Q. Jing, *Near optimal gap in the Lonely Runner Conjecture*, arXiv:2610.23790, first public version 2026-10-16. https://arxiv.org/abs/2610.23790
2. P. Glendinning and N. Sidorov, *The doubling map with asymmetrical holes*, arXiv:1302.2486. https://arxiv.org/pdf/1302.2486
