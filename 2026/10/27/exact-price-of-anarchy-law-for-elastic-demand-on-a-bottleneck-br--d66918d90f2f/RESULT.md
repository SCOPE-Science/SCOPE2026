# Exact price-of-anarchy law for elastic demand on a bottleneck Braess network

## Finding

In the four-vertex bottleneck network described below, let the mass of potential travelers be 3 and let their common travel benefit satisfy \(1<B<2\). Put \(B_*=4-2\sqrt2\). Then the worst Nash combined cost is \(3B\), the minimum combined cost is
\[
CC_{\min}=\min\{3B-B^2/4,\, B+2\},
\qquad
\operatorname{PoA}=\frac{3B}{\min\{3B-B^2/4,\,B+2\}}.
\]
For \(B<B_*\) the unique minimizing path flow is \((B/2,0,0)\), and for \(B>B_*\) it is \((0,1,1)\). At equality these are the only two minimizers.

All Nash flows have equal loads \(w\) on the two variable-latency edges and are of the form \((x,w-x,w-x)\). They consist of:

* flows with total travel \(r=2B-x<3\), where \(w=B\) and \(0\le x\le B\), with combined cost \(3B\);
* flows with all 3 units traveling, present only for \(B\ge3/2\), where \(3/2\le w\le B\) and \(x=2w-3\), with combined cost \(3w\).

Thus Nash travel ranges over \([B,\min(2B,3)]\). In the upper regime \(B>B_*\), the shortcut-only equilibrium with travel \(B\) is a worst equilibrium with less travel than the optimum (which has travel 2). There are also Nash flows with more travel than the optimum. At \(B=6/5\), the worst Nash and optimal costs are respectively \(18/5\) and \(16/5\), so the ratio is \(9/8\).

## Assumptions and scope

The directed edges are \(sa,at,sb,bt,ab\), with respective latency functions \(f,1,1,f,0\) of edge flow \(f\). Write \((x,y,z)\) for nonnegative flows on the shortcut \(sabt\) and the outer paths \(sat,sbt\), respectively; \(r=x+y+z\le3\). Each path costs the maximum latency of its edges. The outside option of not traveling costs \(B\). A Nash flow assigns positive mass only to options of minimum cost (including the outside option). The combined cost \(CC\) sums all path payments and the lost benefit \(B(3-r)\).

## Proof

Let \(u=x+y\), \(v=x+z\), so the path costs in order are
\[
C_0=\max(u,v),\quad C_1=\max(u,1),\quad C_2=\max(v,1).
\]

**Nash flows.** Zero travel is not a Nash flow, since the empty shortcut costs zero. If \(r<3\) at a Nash flow, the common used path cost is \(B\), by indifference with the used outside option. If \(r=3\), the common used path cost \(c\) is at most \(B\); moreover \(u,v\le c\), since each positive edge load comes from a used path whose bottleneck cost is at least that load. As \(r=u+v-x\le u+v\), in the latter case \(c\ge 3/2\). In both cases the common used path cost is greater than 1, so \(\max(u,v)>1\). If \(u>v\), both paths using the first variable-latency edge cost \(u\), but the other outer path costs \(\max(v,1)<u\). This contradicts \(u>0\) in a Nash flow. The same argument rules out \(v>u\). Hence \(u=v=w>1\), so all three paths cost \(w\) and \(y=z=w-x\). Indifference for \(r<3\) now gives \(w=B\); for \(r=3\), feasibility and the outside option give \(x=2w-3\) and \(3/2\le w\le B\). Conversely each listed flow obeys the minimum-cost conditions. The cost is \(3B\) in the first class and \(3w\) in the second. In particular \((B,0,0)\) attains the worst cost \(3B\). The travel range follows from \(0\le x\le B\) and, when available, the full-travel class.

**Global minimizers.** Let \(F=CC-3B\). For fixed \((u,v)\), extend the expression
\[
F=x\max(u,v)+(u-x)\max(u,1)+(v-x)\max(v,1)-B(u+v-x)
\]
as an affine function on \(0\le x\le\min(u,v)\), even if \(r>3\) at the left endpoint. The minimum of the two extended endpoint values is a lower bound at every feasible point. Both minimizing endpoint configurations found below are themselves feasible.

At \(x=0\), the expression is \(g(u)+g(v)\), where \(g(q)=q\max(q,1)-Bq\). On \([0,1]\) it strictly decreases to \(1-B\); on \([1,\infty)\) it strictly increases from this value because \(B<2\). The left endpoint therefore has minimum \(2(1-B)\), attained only at \(u=v=1\).

At \(x=\min(u,v)\), assume \(u\le v\) by symmetry. The expression becomes \(uv+(v-u)\max(v,1)-Bv\). For \(v\le1\) it is \(u(v-1)+(1-B)v\ge v^2-Bv\ge -B^2/4\); equality requires \(u=v=B/2<1\). For \(v\ge1\) it is \(v^2-Bv\ge1-B>-B^2/4\), the last inequality being strict since \(B<2\). Thus the right endpoint minimum is \(-B^2/4\), only at \(u=v=B/2\). No interior \(x\) can attain the global lower bound: that would require both endpoint values to attain it at the same \((u,v)\), and their minimizing pairs are different. The asserted global minimizers and costs now follow, since \(2(1-B)\) is strictly smaller than \(-B^2/4\) precisely for \(B>B_*\) within \(1<B<2\). Dividing the worst equilibrium cost by the optimal cost proves the ratio.

## Verification

The proof covers the continuum and both boundary points \(B=B_*\) and \(B=3/2\). The accompanying `verify_braess_benchmark.py` checks exact rational flow examples and enumerates feasible rational grids in both optimization regimes and at the full-travel threshold. Grid checks are finite corroboration, not proofs of the continuum optimization or classification.

## Relationship to prior work and limitations

The elastic-demand model, bottleneck path norm and combined-cost objective follow Cole, Dodis and Roughgarden. Their author manuscript, §5, discusses a flow-order assumption requiring Nash traffic to be at least optimal traffic, and its bottleneck bound also assumes subpath optimality. We require only that no traveler can improve by switching full routes or participation. In particular at full participation a common cost strictly less than \(B\) is allowed; if equality with \(B\) is imposed even at that boundary, only the \(w=B\) member of the full-travel family remains, and the worst cost and its ratio are unchanged. The shortcut-only equilibrium is not subpath-optimal: travel from \(s\) to \(b\) along the shortcut costs \(B>1\), while the direct \(sb\) edge costs 1. This is a calculation for one five-edge network, not a network-wide bound. No assertion is made for other benefits or population masses.

Cole, Dodis and Roughgarden, “Bottleneck Links, Variable Demand, and the Tragedy of the Commons,” *Networks* 60(3), 194–203 (2012), DOI: [10.1002/net.21458](https://doi.org/10.1002/net.21458); SODA 2006 version, DOI: [10.1145/1109557.1109630](https://doi.org/10.1145/1109557.1109630).
