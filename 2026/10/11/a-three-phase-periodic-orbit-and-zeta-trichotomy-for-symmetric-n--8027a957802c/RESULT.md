# A three-phase periodic-orbit and zeta trichotomy for symmetric negative-doubling holes

## Finding

Let \(T:[0,1]\setminus\{1/2\}\to[0,1]\) be the negative-doubling map
\[
T(x)=\begin{cases}1-2x,&0\le x<1/2,\\2-2x,&1/2<x\le1.\end{cases}
\]
For every real \(a\in(0,2/5]\), let \(H_a=(a,1-a)\) be an **open** symmetric hole and let the survivor set be
\[
S_a=\{x\in[0,1]:T^j(x)\notin H_a\text{ for every integer }j\ge0\}.
\]
(The orbit of a survivor never meets \(1/2\), so the arbitrary value of \(T(1/2)\) is irrelevant.) Every point in \(S_a\) is eventually periodic, \(S_a\) is at most countable, and \(h_{\mathrm{top}}(T|_{S_a})=0\).

More precisely, all the periodic orbits of \(T|_{S_a}\) are the period-two orbit \(\{0,1\}\), the two fixed points \(1/3\) and \(2/3\) when \(a\ge1/3\), and the period-four orbit \(\{1/5,2/5,3/5,4/5\}\) when \(a=2/5\). No other periodic orbit occurs. Thus for every integer \(n\ge1\),
\[
\#\operatorname{Fix}((T|_{S_a})^n)
=2\mathbf1_{2\mid n}+2\mathbf1_{a\ge1/3}
+4\mathbf1_{a=2/5}\mathbf1_{4\mid n},
\]
and the Artin–Mazur dynamical zeta function is exactly
\[
\boxed{\displaystyle
\zeta_a(z)=(1-z^2)^{-1}(1-z)^{-2\mathbf1_{a\ge1/3}}
(1-z^4)^{-\mathbf1_{a=2/5}}.}
\]
The two changes at \(a=1/3\) and \(a=2/5\) are sharp despite the entropy remaining zero throughout the stated parameter interval.

## Assumptions and scope

Only the specified interval map and its actual interval survivor set are considered: no symbolic completion, identification of \(0\) with \(1\), or closed-hole convention is used. In particular, \(0\) and \(1\) are distinct points of a period-two orbit; the hole endpoints are **retained**. The classification covers all real parameters \(0<a\le2/5\), including both endpoints of each phase. It does not characterize the survivor set for \(a>2/5\), general asymmetric holes, or nonlinear decreasing Lorenz maps. The listed zeta function is the formal exponential of finite fixed-point counts; no convergence claim beyond this rational expression is needed.

## Proof

Write \(L=[0,a]\) and \(R=[1-a,1]\). The hole is nonempty and contains \(1/2\), so every survivor has a unique infinite itinerary in the two letters \(L,R\). The map is continuous on \(S_a\) because the entire open interval separating the branches is removed.

**An irreversible pair below the threshold.** A survivor transition \(L\to R\) must start at \(x\le a/2\), since \(T(x)=1-2x\ge1-a\). A transition \(L\to L\) ends at some \(y=T(x)\ge1-2a\). For \(a<2/5\),
\[
1-2a>a/2.
\]
Therefore, after two consecutive \(L\) symbols the next symbol cannot be \(R\); survival forces \(L\) again. Repeating the same argument shows that the itinerary remains \(L\) forever. By the reflection relation \(T(1-x)=1-T(x)\) on the two branches, two consecutive \(R\) symbols likewise force \(R\) forever. A full forward orbit remaining in \(L\) must be the fixed point \(1/3\): on that branch, \(T^k(x)-1/3=(-2)^k(x-1/3)\) cannot stay bounded as \(k\to\infty\) otherwise. Similarly, an eventual all-\(R\) tail is the fixed point \(2/3\). These points belong to \(L\) and \(R\), respectively, exactly when \(a\ge1/3\).

**The alternating case.** If no two consecutive itinerary symbols agree, the itinerary alternates forever. Starting at \(x\in L\), the two specified branches give \(T^2(x)=4x\); boundedness of \(T^{2k}(x)=4^kx\) in \(L\) forces \(x=0\). Starting at \(x\in R\), reflection gives \(x=1\). Thus the only indefinitely alternating orbit is \(0\mapsto1\mapsto0\). Every survivor below \(2/5\) is either on this orbit or eventually constant on one side, hence eventually fixed. No additional periodic orbits are possible.

**The critical endpoint.** At \(a=2/5\), the preceding inequality becomes equality. If an itinerary contains \(LL\) and then switches to \(R\), examine the last two consecutive \(L\) symbols before the switch, represented by \(x\in L\), \(y=T(x)\in L\), \(T(y)\in R\). Their constraints give
\[
y\ge1-2a=1/5,\qquad y\le a/2=1/5,
\]
so \(y=1/5\), \(x=2/5\), and the next iterates are \(3/5,4/5,2/5\). Consequently this orbit joins the primitive cycle
\[
2/5\mapsto1/5\mapsto3/5\mapsto4/5\mapsto2/5.
\]
Likewise \(RR\) followed by \(L\) is, by reflection, forced onto the same cycle. If a repeated symbol is never followed by a change to the other symbol, the orbit is eventually confined to one side and hence reaches its fixed point. If no symbols repeat from some time onward, its tail is alternating and hence reaches the period-two orbit. This proves the complete eventual-periodicity assertion at equality. All four displayed cycle points lie in \(L\cup R\), and each is a survivor because the hole is open.

**Cardinality and entropy.** Let \(P_a\) be the finite union of the periodic orbits just identified. Every survivor eventually enters \(P_a\), so
\[
S_a\subseteq\bigcup_{k\ge0}T^{-k}(P_a).
\]
Every point has at most two branch-preimages in \(L\cup R\), making this union countable. Invariant probability measures for the continuous map \(T|_{S_a}\) are supported on \(P_a\): every point outside \(P_a\) is transient and not recurrent, whereas Poincaré recurrence gives full measure to recurrent points. Each such measure has measure-theoretic entropy zero, and the variational principle for the compact invariant system gives topological entropy zero.

**Exact zeta factors.** The primitive orbit list contains one orbit of length two for all \(a\), two length-one orbits for \(a\ge1/3\), and one length-four orbit at \(a=2/5\). A primitive orbit of length \(\ell\) contributes \(\ell\) fixed points to \(T^n\) if and only if \(\ell\mid n\). Therefore the displayed fixed-point formula follows. Using \(\exp(\sum_{j\ge1}z^{j\ell}/j)=(1-z^{\ell})^{-1}\) yields the asserted product for \(\zeta_a\).

## Verification

A self-contained integer-and-rational-arithmetic program (`verify_periods.py`) enumerates every admissible branch itinerary of length \(n\le13\), solves its exact linear periodicity equation, filters the resulting rational periodic points against the open hole, and checks the stated formula for \(a\in\{1/4,1/3,7/20,2/5\}\). This finite calculation checks representative interior and boundary parameters only. The exhaustive quantifiers over all real \(a\in(0,2/5]\) and all integers \(n\ge1\) follow from the proof, not the computation.

## Relationship to prior work

Ding, Steiner and Sun [1] study open negative-doubling/decreasing-Lorenz systems, symbolic boundary admissibility, survivor-space plateaux and entropy/dimension devil's staircases. Those conclusions motivate the symmetric-hole slice but do not explicitly supply the complete fixed-period spectrum or this zeta function. Glendinning and Hege [2] characterize boundary-of-chaos mechanisms for broader piecewise-monotone systems, including periodic-orbit creation, rather than the exact subcritical, symmetric-hole orbit list. Olivares-Vinales [3] studies rationality and variation of Artin–Mazur zeta functions for piecewise-monotone interval maps; its general zeta framework does not state the periodic orbit counts for this open discontinuous negative-doubling survivor family. These comparisons do not exclude an equivalent classification under different terminology elsewhere.

## Limitations

The conclusion is not a zeta or entropy classification beyond \(a=2/5\) or for asymmetric holes. Although all points in the stated survivor sets are eventually periodic, most need not themselves be periodic; fixed-point counts must not include transient preimages. The finite verifier cannot establish nonexistence of high-period orbits, which is why the itinerary argument is essential.

## References

[1] Y. Ding, W. Steiner and Y. Sun, *Open dynamical systems in topologically expansive decreasing Lorenz maps*, arXiv:2610.03327v1 (first public 2 October 2026), https://arxiv.org/html/2610.03327v1 .

[2] P. Glendinning and C. Hege, *The boundary of chaos for piecewise smooth maps and the boundary of positive Hausdorff dimension for survivor sets of open maps*, arXiv:2508.21429v1 (2025), https://arxiv.org/pdf/2508.21429 .

[3] J. Olivares-Vinales, *The Artin-Mazur zeta function for interval maps*, arXiv:2405.10560v2 (2024), https://arxiv.org/html/2405.10560v2 .
