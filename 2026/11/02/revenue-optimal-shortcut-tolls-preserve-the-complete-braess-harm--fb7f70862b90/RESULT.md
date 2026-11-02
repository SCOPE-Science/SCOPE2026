# Revenue-optimal shortcut tolls preserve the complete Braess harm interval

## Finding

Consider the canonical directed four-vertex Braess network with fixed nonatomic demand \(Q>0\), congestion latency \(f\) on the arcs from origin to the upper vertex and from the lower vertex to destination, constant latency \(1\) on the two other original arcs, and a new directed upper-to-lower shortcut of intrinsic latency \(\kappa\ge0\). Only the shortcut owner may levy a nonnegative, flow-independent toll \(\tau\); the other four arcs are unpriced. All users choose a minimum *latency-plus-toll* path (Wardrop equilibrium), while actual physical delay excludes toll transfers. The owner maximizes its total toll revenue, with zero construction and operating costs.

Write \(B=1-\kappa\). If \(B\le0\), the shortcut is unused at every toll. If \(B>0\), the owner's revenue-maximizing toll is unique whenever \(0<Q<2B\), and is
\[
\tau_*(Q,\kappa)=
\begin{cases}
B-Q,&0<Q\le 2B/3,\\
(2B-Q)/4,&2B/3<Q<2B.
\end{cases}
\]
The corresponding shortcut flow is, respectively, \(z_*=Q\) or \(z_*=(2B-Q)/2\). For \(Q\ge2B\), no nonnegative toll induces positive shortcut flow and every nonnegative toll maximizes the zero revenue. The optimized revenue is \(Q(B-Q)\) in the first regime and \((2B-Q)^2/8\) in the second.

Let \(L_*\) denote mean physical delay at the owner's optimal toll, and let \(L_0=1+Q/2\) denote the Wardrop mean delay when the shortcut is unavailable. Then, for \(B>0\),
\[
L_*-L_0=\begin{cases}
(3Q-2B)/2,&0<Q\le2B/3,\\
\dfrac{(2B-Q)(3Q-2B)}{8Q},&2B/3<Q<2B,\\
0,&Q\ge2B.
\end{cases}
\]
In particular, **revenue-optimal tolling leaves the Braess harm interval exactly \(2B/3<Q<2B\)**, the same interval as under zero toll. The toll reduces the harm strictly inside that interval, but never reverses its sign. Maximizing the absolute harm over all demands \(Q>0\) at fixed \(B>0\) yields the unique maximizer \(Q=2B/\sqrt3\) and exact maximum \(B(1-\sqrt3/2)\).

The fixed-demand physical-delay-minimizing shortcut flow is \(z_{\mathrm{soc}}=\min\{Q,\max\{0,B-Q\}\}\). Consequently \(z_*>z_{\mathrm{soc}}\) exactly for \(B/2<Q<2B\) and the two flows agree outside this interval. For \(B/2<Q<B\), a social planner can implement the exact optimum with the demand-independent shortcut toll \(\tau=B/2\); for \(Q\ge B\), closing the shortcut is optimal. Thus a single-edge revenue-maximizing toll is systematically too low to implement the physical-delay optimum whenever an interior social-control tradeoff exists.

## Assumptions and scope

The graph has directed arcs \(s\to u\), \(u\to t\), \(s\to v\), \(v\to t\), \(u\to v\). The first and fourth arc delays equal their own flows; the second and third equal \(1\); the fifth has constant physical delay \(\kappa\). Travel demand is the fixed positive real \(Q\), divisible among users. The shortcut alone has a nonnegative monetary toll expressed in units of travel time; all users have the same unit conversion and fully perceive that toll. The owner chooses a single toll before Wardrop routing and has no fixed costs. There is no demand elasticity, toll revenue redistribution, link capacity, asymmetric preference or stochastic travel time. Ties are permitted, and the unique equilibrium arc loads determine physical delay even when path flows are not explicitly observed. All claims quantify over every \(Q>0\) and \(\kappa\ge0\), with equality cases above.

## Proof

Denote by \(x_1,x_2,z\) the flows on the upper original path, lower original path and zigzag shortcut path, so \(x_1+x_2+z=Q\). Their generalized path costs are
\[
C_1=x_1+z+1,\qquad C_2=1+x_2+z,\qquad C_3=Q+z+\kappa+\tau.
\]
If at least one original path is used, equality of the original-path costs, together with the fact that any unused original path cannot be strictly cheaper, gives \(x_1=x_2=(Q-z)/2\). The same equality also holds trivially when \(z=Q\). At these loads the common direct cost is \(1+(Q+z)/2\), and the shortcut-path cost is \(Q+z+\kappa+\tau\). The Wardrop complementarity conditions yield exactly
\[
z(Q,\kappa,\tau)=\max\{0,\min\{Q,2(B-\tau)-Q\}\},\qquad x_1=x_2=(Q-z)/2.
\]
These conditions also establish uniqueness of the physical arc loads: for \(z=0\), zigzag cost is at least the direct cost; for \(0<z<Q\), they are equal; for \(z=Q\), zigzag cost is at most the direct cost. Each is sufficient for a Wardrop equilibrium, and the three cases are exhaustive.

The revenue is \(R(\tau)=\tau z(Q,\kappa,\tau)\). If \(B\le0\) or \(Q\ge2B\), then \(z=0\) for every \(\tau\ge0\). Otherwise \(R\) grows linearly as \(Q\tau\) on the all-shortcut interval \(0\le\tau\le B-Q\) when this interval exists; on the partly used interval it equals the strictly concave quadratic \(\tau(2B-Q-2\tau)\); and it vanishes above \(\tau=B-Q/2\). The quadratic vertex is \(\tau_v=(2B-Q)/4\), and it lies to the right of the all-shortcut boundary precisely when \(Q\ge2B/3\). This proves the stated unique toll, shortcut flow and revenue, including the matching boundary \(Q=2B/3\).

The physical (rather than generalized) mean latency is
\[
L(Q,\kappa,z)=\frac{(Q-z)[1+(Q+z)/2]+z(Q+z+\kappa)}Q
=1+\frac Q2+\frac{z(2Q-2B+z)}{2Q}.
\]
Substituting the revenue-maximizing \(z\) gives the three formulas for \(L_*-L_0\). For zero toll, \(z_0=\max\{0,\min\{Q,2B-Q\}\}\): when \(0<Q\le B\), \(L(Q,\kappa,z_0)-L_0=(3Q-2B)/2\); when \(B<Q<2B\), that difference equals \((2B-Q)/2\); and otherwise it vanishes. Both with and without optimized toll the difference is strictly positive precisely on \((2B/3,2B)\), and the optimized positive difference is strictly smaller there. In the interior, the positive difference simplifies to \(B-3Q/8-B^2/(2Q)\). Its derivative \(-3/8+B^2/(2Q^2)\) has a unique zero at \(Q=2B/\sqrt3\), and the endpoints have zero difference. This yields the sharp absolute maximum.

Finally \(L-L_0\) is a strictly convex quadratic in \(z\in[0,Q]\), with unconstrained minimizer \(B-Q\). Its constrained minimizer is \(z_{\mathrm{soc}}=\min\{Q,\max\{0,B-Q\}\}\). Subtracting this flow from the three forms of \(z_*\) proves equality exactly when \(Q\le B/2\) or \(Q\ge2B\) (also for all \(Q\) if \(B\le0\)), and strict overuse otherwise. For \(B/2<Q<B\), setting \(\tau=B/2\) induces \(z=B-Q\) by the Wardrop formula. For \(Q\ge B\), some sufficiently large nonnegative toll forces \(z=0\), achieving the social minimum. All edge and demand boundaries are included by the displayed non-strict definitions.

## Verification

The accompanying standalone `verify.py` uses exact rational arithmetic to test the Wardrop complementarity inequalities, conservation of flow, physical-delay identity, global revenue domination over a sampled rational toll grid, and social-delay convex minimization over a sampled rational flow grid. It checks 55,507 assertions over 37 positive rational demand values, 13 intrinsic shortcut latencies and dozens of rational tolls each, as well as the exact switching demand boundaries for several rational values of \(B\). Run `python3 verify.py` from the package directory. The infinite-domain results, uniqueness and sharp maximizer are established analytically above; finite checks are not a substitute for those arguments.

## Relationship to prior work

The four-node Braess example and Wardrop equilibrium are standard. Huang, Ozdaglar and Acemoglu, *Efficiency and Braess' Paradox under Pricing in General Networks*, consider a provider choosing a price for **each whole path** and prove the absence of a weak Braess paradox at their monopoly equilibrium. Their provider has more pricing instruments and a different monopoly objective than the owner restricted to the *single added shortcut edge* here; their conclusion does not imply ours or contradict it. Verhoef, *Second-best Road Pricing Through Highway Franchising* (first archived 2005), analyzes second-best road franchises with capacity choice, including network externalities and Braess-type adverse welfare results. That broad framework motivates this fixed-capacity, fixed-demand exact phase diagram but the inspected sections do not establish its all-parameter boundary, coincidence or closed maximum. Penchina's 2008 results concern **minimum-revenue** tolls implementing desired flows, rather than private revenue maximization. The precise two-parameter classification, its link-ownership qualification and equality cases are the objects assessed here.

## Limitations

The result is an exact result for one canonical affine routing graph, not a universal bound for arbitrary networks or users. Zero construction and operating costs are essential to the stated private objective, and the toll is a constant per-user shortcut charge rather than a full set of path prices. This analysis establishes no empirical congestion outcome or welfare statement with elastic demand. An older equivalent edge-specific pricing computation in the transport-economics literature cannot be ruled out by available source searches. There has been no independent mathematical validation.

## References

1. J. G. Wardrop, *Some Theoretical Aspects of Road Traffic Research*, Proceedings of the Institution of Civil Engineers, 1952.
2. D. Braess, *Über ein Paradoxon aus der Verkehrsplanung*, Unternehmensforschung 12 (1968), 258–268.
3. X. Huang, A. Ozdaglar and D. Acemoglu, *Efficiency and Braess' Paradox under Pricing in General Networks*, full manuscript at https://web.mit.edu/asuman/Desktop/asuman/www/documents/pricing_general_final.pdf (Sections II and V).
4. E. T. Verhoef, *Second-best Road Pricing Through Highway Franchising*, Tinbergen Institute Discussion Paper 05-082/3 (public listing dated 2005-08-16), https://papers.tinbergen.nl/05082.pdf.
5. C. M. Penchina, *Power-Law Congestion Costs: Minimal Revenue (MR) Pricing and the Braess Paradox*, The Open Transportation Journal 2 (2008), 47–52, https://trid.trb.org/View/899625.
