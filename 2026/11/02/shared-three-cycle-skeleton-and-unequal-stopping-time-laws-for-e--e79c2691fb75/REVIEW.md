# Independent mathematical audit

## correctness

PASS

For F_n bouquet of n labelled triangles, synchronous 3-color CCA and threshold-one GHM, all initial states correspond to center color c in {0,1,2} and a sequence of n ordered leaf-pair types from 9 choices. Since contact rules depend on *presence*, not multiplicity, the nonempty support subset S suffices for all time, giving exactly 3(2^9-1)=1533 universal finite symbolic cases. Reviewed source explicit symbolic transition algorithm; complete support census verifies C_n^5=C_n^2, G_n^7=G_n^4 and exact first periodic entry coefficient rows. Onto(s,n)=sum(-1)^j binom(s,j)(s-j)^n transforms the support counts to exact all-n formula: CCA D0=3*3^n,D1=3*6^n,D2=3*(9^n-6^n-3^n); GHM D0=3^(n+1)-2,D1=6^n+4^n-3^n,D2=9^n-3^n+1,D3=9^n-4^n+1,D4=9^n-6^n-3^n. Primitive 3-cycle configurations share identical update maps, 3*(3^n-1) states => 3^n-1 orbits; eventually enter 3-cycle iff one originally rainbow petal. Independent direct graph-neighborhood enumeration for all 3^(2n+1) initial states n=1,2,3 confirmed exact distribution and common periods. As n->infinity, CCA T->2 while GHM T uniform {2,3,4}. The all-n assertion follows from exact support quotient and symbolic count, not extrapolating n<=3.

## originality

PASS

Best-of-knowledge originality after checking exact formulations, stronger work, tables and implication: Triangle bouquet is also the friendship/dutch windmill graph F_n, included in searches by both names. General zero-circulation theorem covers the basin predicate, explicitly credited, but not exact finite stopping histograms or orbit count. Prior frameworks are broader in graph families, but do not mathematically dominate the specific sharp entry-time and periodic-orbit enumeration, with no identified bound that specializes exactly to it. The new laws are not corollaries of a previously tabulated basin probability or diameter-based synchronization bound. Exact two-model support-state analysis yields distinct leading 9^n terms at t=2,3,4.

## value

PASS

Exact microscopic finite-time distributions and shared periodic skeleton provide a sharp and informative comparison of two standard excitable-graph automata: same oscillator basin yet nonidentical limiting transient-time laws. A complete natural family with unbounded n is classified by a finite support reduction, yielding a reusable technique and meaningful dynamical distinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
