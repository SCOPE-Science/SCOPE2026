# Exact bounded-morphism multiplicities and a sharp root-gluing window for starlike Kripke frames

## Finding

A surjective bounded morphism of finite rooted starlike Kripke frames is determined by independent, locally bounded arm maps subject to a single global covering condition. This gives an exact multiplicity formula for arbitrary labelled arm-length vectors and a sharp Poisson root-gluing window in the homogeneous case.

For \(r\ge1\), \(k\ge2\), and positive integers \(a_i,b_j\), define
\[
W_{ij}=\sum_{d=1}^{\min(a_i,b_j)}\binom{a_i-1}{d-1},\qquad
F_{ij}=\begin{cases}\binom{a_i-1}{b_j-1}&a_i\ge b_j,\\0&a_i<b_j,\end{cases}
\quad W_i=\sum_{j=1}^k W_{ij}.
\]
Then the number \(N(\mathbf a,\mathbf b)\) of surjective bounded morphisms is
\[
\boxed{N(\mathbf a,\mathbf b)=\sum_{S\subseteq[k]}(-1)^{|S|}\prod_{i=1}^r\left(W_i-\sum_{j\in S}F_{ij}\right).}
\]
Choose independently and uniformly among the \(W_i\) local maps on each source arm, and let \(Z\) count the target arms not completely covered by any one source arm. Its exact probability-generating polynomial is
\[
\boxed{\mathbb E[u^Z]=\sum_{S\subseteq[k]}(u-1)^{|S|}\prod_{i=1}^r\left(1-\frac{\sum_{j\in S}F_{ij}}{W_i}\right).}
\]
In particular, the extension probability is \(\Pr(Z=0)=N(\mathbf a,\mathbf b)/\prod_iW_i\).

For fixed positive integers \(a\ge b\), suppose all \(r=r_k\) source arms have length \(a\) and all \(k\) target arms have length \(b\). Put
\[
W=\sum_{d=1}^b\binom{a-1}{d-1},\qquad F=\binom{a-1}{b-1},\qquad\rho=F/W>0.
\]
For any fixed real \(t\), if \(r_k=\lfloor(k/\rho)(\log k+t)\rfloor\), then
\[
\boxed{Z_k\ \Longrightarrow\ \operatorname{Poisson}(e^{-t}),\qquad
\frac{N((a)^{r_k},(b)^k)}{(kW)^{r_k}}\longrightarrow\exp(-e^{-t}).}
\]
Here the limiting Poisson occupancy law is classical; the result identifies the exact frame-theoretic gluing obstruction and its weight \(\rho\).

## Assumptions and scope

The rooted starlike frame \(T(\mathbf a)\) has a least point \(o\) and \(r\) pairwise disjoint chains above it, with \(a_i\) nonroot points on labelled arm \(i\). The target \(T(\mathbf b)\) is defined likewise, with at least two arms. All frames and arms are finite and labelled. A bounded morphism is a map \(f\) such that for every \(x\), \(f(\uparrow x)=\uparrow f(x)\), where \(\uparrow x=\{y:x\le y\}\). This condition includes order preservation. Only surjective bounded morphisms between these frames are counted. A *local arm map* is a bounded morphism from a source chain to the forest of target arms (with the roots deleted), without imposing the separate global condition at the source root. An arm *fully covers* a target arm when its image contains every nonroot point of that target arm.

## Proof

**1. Root and arm rigidity.** If \(f\) is surjective, \(f(o)\) lies below all points of the target and therefore equals its least point. For any nonroot \(x\), the set \(\uparrow x\) is a chain and so is \(f(\uparrow x)\). The target root has an upset containing incomparable points because \(k\ge2\); hence \(f(x)\) cannot be the target root. Order preservation therefore sends every source arm into one target arm. Conversely, any collection of local bounded maps can be joined by mapping source root to target root; the bounded-morphism condition away from that root is automatic.

**2. Local maps.** On a source arm of \(a_i\) points mapped to target arm \(j\), a bounded map is precisely a nondecreasing surjection onto a terminal segment of that target arm. Indeed, its top source point must hit the top target point, and the equality of principal upsets forces no gaps in the visited interval. For terminal-segment length \(d\), the positive multiplicities of its \(d\) target points sum to \(a_i\), giving \(\binom{a_i-1}{d-1}\) maps. Summing yields \(W_{ij}\); hitting all \(b_j\) points gives \(F_{ij}\).

**3. Gluing and exact counts.** At the source root, the condition \(f(\uparrow o)=\uparrow f(o)\) holds exactly when every target arm is fully covered by at least one source arm. Failure to fully cover arm \(j\) rules out \(F_{ij}\) of source arm \(i\)'s \(W_i\) options. As one source arm can map into only one target arm, the forbidden sets for different \(j\) are disjoint within that source arm. Inclusion–exclusion over the set \(S\) of uncovered target arms proves the displayed formula for \(N\).

For the distribution of \(Z\), expand the identity \(u^Z=\prod_{j=1}^k(1+(u-1)\mathbf1_{j\text{ uncovered}})\) and use independence of the source-arm choices. This gives the exact probability-generating polynomial, including cases where no global bounded morphism exists.

**4. Sharp window.** In the homogeneous case, each source arm fully covers each designated target arm with probability \(F/(kW)=\rho/k\). For every fixed integer \(s\ge1\), the probability that \(s\) specified target arms all remain uncovered after \(r_k\) choices is \((1-s\rho/k)^{r_k}\). Thus the \(s\)-th factorial moment of \(Z_k\) is
\[
\mathbb E[(Z_k)_s]=(k)_s(1-s\rho/k)^{r_k}\longrightarrow e^{-st},
\]
which equals the factorial moment of \(\operatorname{Poisson}(e^{-t})\). The method of factorial moments yields convergence in distribution; evaluating the probability at the continuity-isolated state \(0\) by inclusion–exclusion (or the standard discrete weak-convergence property) gives \(\Pr(Z_k=0)\to e^{-e^{-t}}\). Since the number of possible local collections is \((kW)^{r_k}\), the normalized bounded-morphism count has the asserted limit.

## Verification

The accompanying self-contained `check_starlike.py` independently enumerates every root-fixed function on sufficiently small labelled source/target frames and tests the defining principal-upset condition directly. It compares this brute-force count with the displayed inclusion–exclusion formula. A second, independently implemented enumeration checks the entire defect-count distribution. Running `python3 check_starlike.py` returned `VERIFY_OK` on \(319\) rooted-frame count checks and \(319\) defect-profile checks. For example, \(N((2,2),(2,2))=2\) and \(N((3,3,3),(2,2))=96\). The finite computations do not prove the infinite-window limit; that follows from the factorial-moment argument.

## Relationship to prior work

Adam-Day, Bezhanishvili, Gabelaia and Marra (2021), Proposition 6.1, establish a qualitative bounded-morphism existence criterion for finite starlike frames as part of a Jankov–Fine analysis of intermediate logics. The structural assumptions about finite rooted frames and bounded morphisms follow their setting. The exact multiplicities, complete root-extension defect law, and its sharp homogeneous threshold are additional quantitative statements, not their existence criterion. The coupon-collector Poisson window itself is classical: its occurrence here is a consequence of identifying the precise locally bounded arm choices and global root obstruction.

## Limitations

The target must have at least two positive-length arms; the proof uses this to exclude mapping nonroot worlds to the target root. Morphisms are counted on labelled frames. The probability model samples uniformly among admissible local arm maps, not uniformly among all raw set maps or all maps satisfying the full bounded-morphism condition. The asymptotic theorem fixes positive arm lengths \(a\ge b\) while the numbers of source and target arms grow; other joint length-growth regimes are not addressed. The literature comparison cannot establish absolute uniqueness, particularly where older morphism enumerations or unpublished theses were not available in full text. Independent external mathematical validation has not been performed.

## References

1. S. Adam-Day, N. Bezhanishvili, D. Gabelaia and V. Marra, *Polyhedral completeness of intermediate logics: the Nerve Criterion*, arXiv:2112.07518v1 (first public 2021-12-14), especially §2.1 and Proposition 6.1 in §6.1. https://arxiv.org/abs/2112.07518
2. Classical coupon-collector and Poisson occupancy methods, used only for the final limit theorem after the frame-theoretic reduction.
