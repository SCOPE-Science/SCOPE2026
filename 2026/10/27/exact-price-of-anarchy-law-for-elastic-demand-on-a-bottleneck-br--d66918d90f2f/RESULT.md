# Exact price-of-anarchy law for elastic demand on a bottleneck Braess network

## Finding

For every benefit level \(B\in(4-2\sqrt2,2)\), the four-vertex directed Braess network described below has an exact elastic-demand price of anarchy
\[
\operatorname{PoA}=\frac{3B}{B+2}.
\]
Every Nash flow has combined cost \(3B\) and total travel \(B\). The unique cost-minimizing flow sends one unit on each outer path and none on the shortcut, so its total travel is \(2\) and its combined cost is \(B+2\). Thus equilibrium travel is strictly below optimal travel throughout this parameter interval. At \(B=6/5\), the exact ratio is \(9/8\).

## Assumptions and scope

The directed graph has vertices \(s,a,b,t\) and five edges. The edge-latency functions are
\[
c_{sa}(f)=f,\quad c_{at}(f)=1,\quad c_{sb}(f)=1,\quad
c_{bt}(f)=f,\quad c_{ab}(f)=0.
\]
There is one source–destination pair \((s,t)\). The three paths are the shortcut \(P_0=s\to a\to b\to t\), and the outer paths \(P_1=s\to a\to t\) and \(P_2=s\to b\to t\). A path's cost is the \(\ell_\infty\) norm of its edge-latency vector, i.e. the maximum edge latency on that path, not the sum.

The population has mass \(3\), and each potential traveler has constant benefit \(B\) for traveling, with \(4-2\sqrt2<B<2\). For path flows \(x,y,z\ge0\) on \(P_0,P_1,P_2\), respectively, total travel is \(r=x+y+z\le3\). The combined-cost objective is total path cost paid plus lost benefit of nontravelers:
\[
CC(x,y,z)=xC_0+yC_1+zC_2+B(3-r).
\]
No claim is made for other path norms, benefit curves, edge costs, or network topologies.

## Proof

Set \(u=x+y\) and \(v=x+z\). The path costs are exactly
\[
C_0=\max\{u,v\},\quad C_1=\max\{u,1\},\quad
C_2=\max\{1,v\}.
\]

**Equilibrium.** The flow \((x,y,z)=(B,0,0)\) is feasible because \(B<2<3\). Since \(B>1\), all three path costs at this flow equal \(B\). This is a Nash flow: every used path costs the travel benefit, and no unused path is cheaper. More generally, at any Nash flow the common cost of used paths equals \(B\). Hence its congestion-cost term is \(Br\), while the lost-benefit term is \(B(3-r)\). Every Nash flow therefore has \(CC=3B\).

**Global optimum.** Subtract the constant \(3B\) and write
\[
F:=CC-3B=x\max\{u,v\}+(u-x)\max\{u,1\}
 +(v-x)\max\{v,1\}-B(u+v-x).
\]
For fixed \(u,v\), this expression is affine in \(x\) on \(0\le x\le\min\{u,v\}\). Its minimum is therefore attained at \(x=0\) or \(x=\min\{u,v\}\).

If \(x=0\), then \(F=g(u)+g(v)\), where
\[
g(q)=q\max\{q,1\}-Bq=
\begin{cases}(1-B)q,&0\le q\le1,\\q^2-Bq,&q\ge1.\end{cases}
\]
Because \(1<B<2\), the first branch decreases to \(q=1\), and the second branch increases from \(q=1\). Thus \(g(q)\ge1-B\), with equality only at \(q=1\). Consequently \(F\ge2(1-B)\), with equality only at \(u=v=1\), which gives \((x,y,z)=(0,1,1)\).

For the other endpoint, assume without loss of generality \(u\le v\), so \(x=u\), \(y=0\), \(z=v-u\), and
\[
F=uv+(v-u)\max\{v,1\}-Bv.
\]
If \(v\le1\), then \(F=u(v-1)+(1-B)v\ge v^2-Bv\ge-B^2/4\). If \(v\ge1\), then \(F=v^2-Bv\ge1-B\), since \(B<2\) makes this branch increasing for \(v\ge1\). The parameter condition \(B>4-2\sqrt2\) is equivalent to \(2(1-B)<-B^2/4\); also \(2(1-B)<1-B\) because \(B>1\). Therefore this endpoint has strictly larger objective than \(2(1-B)\).

It follows that the unique global optimum is \((x,y,z)=(0,1,1)\), with total travel \(2\) and
\[
CC_{\rm opt}=3B+2(1-B)=B+2.
\]
The exact price of anarchy is \(CC_{\rm Nash}/CC_{\rm opt}=3B/(B+2)\). At \(B=6/5\), the equilibrium and optimal costs are \(18/5\) and \(16/5\), respectively, and the ratio is \(9/8\). This proves the claim for the full stated interval.

## Verification

The included exact-rational Python script was run from the packaged path and printed `VERIFY_OK`. It checks the representative value \(B=6/5\), the displayed path costs, feasibility, combined costs, ratio, and exact rational inequalities. The continuum result rests on the piecewise analytic proof above; the script is corroboration, not an independent or formal proof.

## Relationship to prior work

Cole, Dodis, and Roughgarden introduced elastic traffic together with nonadditive path-cost norms and a prize-collecting combined-cost objective. Their Section 5 explicitly leaves unanalyzed the nonlinear-path-norm case when Nash flow sends less total traffic than an optimum. The present result supplies an exact parameterized benchmark in that case for the \(\ell_\infty\) norm; it does not solve the general problem. Earlier work on nonadditive path costs studies equilibrium existence, uniqueness, and computation, while standard elastic-demand price-of-anarchy bounds for separable costs do not directly imply this max-aggregated path-cost formula.

## Limitations

This is a one-topology theorem for a single commodity, constant benefits, five specified latency functions, and the bottleneck norm. It gives neither a worst-case bound over networks nor a general comparison theorem for elastic demand. Related older literature may contain an equivalent special example; two plausible papers were available only through their abstracts and metadata, so priority is not exhaustively settled.

## References

1. R. Cole, Y. Dodis, and T. Roughgarden, “Bottleneck Links, Variable Demand, and the Tragedy of the Commons,” Proceedings of the 17th ACM-SIAM Symposium on Discrete Algorithms (SODA), 2006, pp. 668–677. DOI: 10.1145/1109557.1109630.
2. R. Cole, Y. Dodis, and T. Roughgarden, “Bottleneck links, variable demand, and the tragedy of the commons,” *Networks* 60(3), 194–203 (2012). DOI: 10.1002/net.21458.
3. S. A. Gabriel and D. Bernstein, “The Traffic Equilibrium Problem with Nonadditive Path Costs,” *Transportation Science* 31(4), 337–348 (1997). DOI: 10.1287/trsc.31.4.337.
4. C. K. Chau and K. M. Sim, “The price of anarchy for non-atomic congestion games with symmetric cost maps and elastic demands,” *Operations Research Letters* 31(5), 327–334 (2003). DOI: 10.1016/S0167-6377(03)00030-0.
