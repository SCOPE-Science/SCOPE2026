# Exact half-crossing law and critical exponential scaling in the Hata–Yano random map

## Finding
Let a point move under independent selections of the two Hata–Yano piecewise-affine interval maps described below. Let \(N\) count all transitions between the open left half \(L=(0,1/2)\) and the open right half \(R=(1/2,1)\) over its entire forward trajectory. The initial point is independent of the map choices and uniformly distributed on either \(L\) or \(R\).

Write \(p\) for the probability of the first map and \(q=1-p\) for that of the second, where \(0<p<1\). If \(p\ne1/2\), put
\[
\Delta=|2p-1|,\qquad \rho=\frac{1-\Delta}{1+3\Delta},\qquad
s=\begin{cases}0,&\text{the initial half is the attracting half},\\1,&\text{otherwise},\end{cases}
\]
where the attracting half is \(L\) when \(p>1/2\) and \(R\) when \(p<1/2\). Then \(N\) is almost surely finite and, for every integer \(j\ge0\),
\[
\boxed{\Pr(N=2j+s)=(1-\rho)\rho^j.}
\]
No other finite value has positive probability. In particular,
\[
\boxed{\mathbb E(N\mid X_0\text{ uniform on }L)=\frac{q}{|2p-1|},\qquad
\mathbb E(N\mid X_0\text{ uniform on }R)=\frac{p}{|2p-1|}.}
\]
The variance from either starting half is \(4\rho/(1-\rho)^2\). As \(p\to1/2\) from either side and for either starting half,
\[
\boxed{|2p-1|N\ \Longrightarrow\ \operatorname{Exp}(2),}
\]
where \(\operatorname{Exp}(2)\) denotes the exponential law of rate \(2\). At the fair parameter \(p=1/2\), \(\Pr(N=\infty)=1\).

The same argument gives the almost-sure endpoint convergence rates off criticality: if \(p>1/2\), then \(X_n\to0\) and \(-n^{-1}\log X_n\to(2p-1)\log2\); if \(p<1/2\), then \(X_n\to1\) and \(-n^{-1}\log(1-X_n)\to(1-2p)\log2\).

## Assumptions and scope
For \(0<x<1\), away from the harmless switching point, define
\[
f_0(x)=\begin{cases}x/2,&0<x<1/2,\\2x-1,&1/2<x<1,\end{cases}
\quad
f_1(x)=\begin{cases}2x,&0<x<1/2,\\(x+1)/2,&1/2<x<1.\end{cases}
\]
The random recursion is \(X_{n+1}=f_{\xi_{n+1}}(X_n)\), where \(\xi_n\) are independent and identically distributed, \(\Pr(\xi_n=0)=p\), and \(\Pr(\xi_n=1)=q\). The initial law is normalized Lebesgue measure on exactly one of the open halves and is independent of all choices. Boundary values of the maps can be prescribed arbitrarily: by absolute continuity, the forward orbit hits an endpoint or the switch point with probability zero. The conclusions concern this annealed initial law, not every exceptional deterministic initial condition and not an invariant probability measure.

## Proof
**Dyadic shell dynamics.** For integers \(k\ge0\) define
\[
L_k=(2^{-k-2},2^{-k-1}),\qquad
R_k=(1-2^{-k-1},1-2^{-k-2}).
\]
Up to endpoints of measure zero these shells partition \(L\) and \(R\). Direct substitution gives
\[
f_0(L_k)=L_{k+1},\quad f_1(L_k)=L_{k-1}\ (k\ge1),\quad f_1(L_0)=R,
\]
\[
f_1(R_k)=R_{k+1},\quad f_0(R_k)=R_{k-1}\ (k\ge1),\quad f_0(R_0)=L.
\]
Each displayed map is affine and maps its entire source shell onto the full target shell or full opposite half. Uniformity conditional on a shell is therefore preserved by every history of shell moves. Upon any half crossing, the image is uniformly distributed on the opposite full half, independently of the earlier shell history. For a uniform point in either full half its shell index \(K\) satisfies \(\Pr(K=k)=2^{-k-1}\). Hence the annealed process on the side and shell index is an exact nearest-neighbor Markov process with identical geometric resetting at each crossing.

**One-crossing probabilities.** On the left, the depth \(k\) moves outward to \(k+1\) with probability \(p\) and inward to \(k-1\) with probability \(q\). A move inward from zero is a half crossing. The corresponding probabilities on the right are interchanged. For a nearest-neighbor walk with outward probability \(u\) and inward probability \(v=1-u\), started at depth \(k\), the probability of eventually hitting \(-1\) is
\[
H_k(u,v)=\begin{cases}1,&u\le v,\\(v/u)^{k+1},&u>v.\end{cases}
\]
For completeness, this follows from the two-boundary gambler's-ruin recurrence \(H_k=uH_{k+1}+vH_{k-1}\), with boundary value \(H_{-1}=1\), by first imposing an absorbing upper boundary at \(B\) and then letting \(B\to\infty\). In the zero-drift case recurrence of the simple symmetric walk gives the first line as well. Averaging over the geometric initial/reset shell gives the chance of a subsequent crossing from an entire half:
\[
C_L=\begin{cases}1,&p\le q,\\\dfrac{q}{2p-q},&p>q,\end{cases}
\qquad
C_R=\begin{cases}1,&q\le p,\\\dfrac{p}{2q-p},&q>p.\end{cases}
\]
Indeed, for \(0<t<1\), \(\sum_{k\ge0}2^{-k-1}t^{k+1}=t/(2-t)\). The equality case has crossing probability one on both halves.

**Complete crossing count.** If \(p>q\), every excursion from \(R\) crosses back to \(L\), while each new excursion from \(L\) crosses to \(R\) with probability \(\rho=q/(2p-q)\). If \(p<q\), interchange the halves, and the crossing probability from the outward-drifting half is \(\rho=p/(2q-p)\). The strong Markov property at a crossing, together with its uniform reset distribution, makes these trials independent and identically distributed. Consequently \(N=2G+s\), where \(G\) is geometric on \(\{0,1,2,\ldots\}\) with \(\Pr(G=j)=(1-\rho)\rho^j\), and \(s\) is as stated. Both expressions for \(\rho\) equal \((1-\Delta)/(1+3\Delta)\). This proves the full law, the means and the variance. When \(p=q\), every half excursion crosses again almost surely; repeating this countably many times proves \(N=\infty\) almost surely.

**Endpoint rates and scaling.** Off criticality, \(G\) is finite almost surely, so there is a last crossing and the final half must be the outward-drifting half. Thereafter the depth increments are the original independent Bernoulli choices with signs appropriate to that half. The strong law gives depth divided by time converging to \(\Delta\); the shell inequalities give the announced logarithmic endpoint rate. Finally, as \(\Delta\downarrow0\), \(1-\rho=4\Delta/(1+3\Delta)\), so for every fixed \(t\ge0\), the geometric tail formula implies \(\Pr(\Delta(2G+s)>t)\to e^{-2t}\). This proves the exponential limit.

## Verification
The accompanying stand-alone `check.py` uses exact rational arithmetic in two independently coded representations. One propagates full interval pieces under the two affine maps, with exact density Jacobians and explicit crossing counts. The other propagates the geometric dyadic-shell Markov process, truncating only shell depths that provably cannot cross in the remaining finite horizon. For six rational probabilities, both starting halves, and horizons one through eight, their 96 finite-time crossing-count distributions agree exactly. The checker also verifies the one-crossing harmonic recurrences and moment identities on rational samples. Run `python3 check.py` using only the Python standard library. These finite checks are diagnostics; the all-time and all-parameter claims are proved above, not inferred from them.

## Relationship to prior work
Hata and Yano [1] introduced these exact affine maps and proved the fair-coin arcsine and Darling–Kac laws. They explicitly leave the unequal-selection case untreated because the required skew-product Markov construction was unavailable; see their introduction immediately after Theorem 1.1. Nakamura, Nakano, Toyokawa, and Yano [2] extend fair-choice arcsine laws to maps with core random dynamics, but their theorem and Hata–Yano example still select the maps equally often. Classical gambler's-ruin hitting probabilities are standard [3]; here the additional dynamical step is the exact uniform reset on crossing a full half, giving an explicit *total* crossing law and its singular selection-bias limit. These conclusions are not assertions about general random interval systems, and the endpoint convergence by itself is not claimed as a new general principle.

## Limitations
The distribution requires an initial law uniform on either complete half; arbitrary fixed initial points or nonuniform distributions need not obey the geometric formula. The zero-measure switching boundaries are excluded. No explicit distribution of the last crossing *time*, invariant density, return-time sequence, or non-dyadic generalized map is asserted. The reduction to gambler's ruin makes an equivalent unpublished or differently formulated crossing-count computation a remaining priority risk.

## References
[1] G. Hata and K. Yano, *Arcsine and Darling–Kac laws for piecewise linear random interval maps*, arXiv:2108.01332 (first public version, 3 August 2021), especially Eqs. (1.10), (1.13), Theorem 1.1, and Section 3. https://arxiv.org/abs/2108.01332

[2] F. Nakamura, Y. Nakano, H. Toyokawa, and K. Yano, *Arcsine law for random dynamics with a core*, arXiv:2206.00226 (first public version, 1 June 2022), especially the fair-selection assumptions and generalized Hata–Yano examples. https://arxiv.org/abs/2206.00226

[3] J. R. Norris, *Markov Chains*, Cambridge University Press (1997), classical nearest-neighbor hitting-probability background.
