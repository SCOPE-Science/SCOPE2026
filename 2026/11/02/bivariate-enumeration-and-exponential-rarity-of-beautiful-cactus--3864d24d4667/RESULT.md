# Bivariate enumeration and exponential rarity of beautiful cactus graphs

## Finding

Let \(a_{n,i,j}\) count **connected labelled simple cactus graphs** on \(n\geq1\) vertices which are beautiful, with exactly \(i\) triangular blocks and \(j\) cycle blocks of even length at least six. Define the exponential generating function
\[
 C(x;s,t)=\sum_{n\geq1}\sum_{i,j\geq0}a_{n,i,j}s^i t^j\frac{x^n}{n!}.
\]
Define the formal series \(T\in x\mathbb Q[s,t][[x]]\) uniquely by
\[
 \boxed{T=x\exp\left(T+s\left(xT-\frac{x^2}{2}\right)+\frac{tT^5}{2(1-T^2)}\right).}
\]
Then the complete bivariate enumeration is
\[
 \boxed{x\frac{\partial C}{\partial x}=T+\frac{sx}{2}(T-x)^2.} \tag{1}
\]
In particular the numbers \(a_n=\sum_{i,j}a_{n,i,j}\), for \(n=1,\dots,9\), are
\[
 1,\;1,\;4,\;28,\;290,\;3936,\;66472,\;1352632,\;32325372.
\]

There is also a sharp asymptotic density statement. Define
\[
 F(x,y)=y+xy-\frac{x^2}{2}+\frac{y^5}{2(1-y^2)}.
\]
Let \((\rho,\tau)\) be the strictly positive solution, on the dominant combinatorial branch with \(\tau<1\), of
\[
 \tau=\rho e^{F(\rho,\tau)},\qquad 1=\tau F_y(\rho,\tau).
\]
Set
\[
 \kappa=\tau\sqrt{\frac{2(1+\rho F_x(\rho,\tau))}{1+\tau^2 F_{yy}(\rho,\tau)}},\qquad
 A=\frac{(1+\rho(\tau-\rho))\kappa}{2\sqrt\pi}.
\]
Then
\[
 \boxed{a_n\sim A\,n!\,\rho^{-n}n^{-5/2}},
\]
where \(\rho\approx0.273826905596553\) and \(A\approx0.162935269391370\). If \(c_n\) counts **all** connected labelled cactus graphs on \(n\) vertices, then
\[
 \boxed{\frac{a_n}{c_n}\sim 1.35610090435875\,(0.871865177620160)^n.} \tag{2}
\]
The decimals in (2) denote approximations to constants defined by the two exact implicit systems below; they are not exact rational identities.

## Assumptions and scope

A cactus is a finite connected simple graph in which each edge lies in at most one simple cycle. Its nontrivial two-connected blocks are individual edges or simple cycles. An isolated vertex is included as the one-vertex cactus.

A graph is **beautiful** in the terminology of Wunderlich if each induced subgraph is isomorphic to the intersection graph of the maximal nonempty all-one rectangles of some finite binary matrix. The intersection requires a shared matrix cell. We use the externally proved characterization [1] that beautiful graphs are exactly those with no induced \(C_4\), gem, net, watch, or odd hole. Here a net is a triangle with one private pendant neighbor attached to each triangle vertex. A gem is a four-vertex path plus a universal vertex; a watch contains a diamond. The classification in [1] is an input to the present theorem; its proof is not reproduced here.

The variables \(s\) and \(t\) mark triangle blocks and long even-cycle blocks independently. Graphs are **vertex-labelled**, and equal graph structures are counted once, with no division by automorphisms beyond the exponential generating-function convention.

## Proof

**1. The exact cactus specialization.** Every simple cycle in a cactus is a unique cycle block and is induced. No cactus contains a diamond (two triangles sharing an edge), and both the gem and the watch contain a diamond. Consequently the characterization in [1] excludes exactly cycle blocks of length four, odd cycle blocks of length at least five, and induced nets.

For a triangle block \(B=\{u,v,w\}\), an induced net with triangle \(B\) exists precisely when each of \(u,v,w\) has at least one neighbor outside \(B\). Indeed, such external neighbors lie in different branches of the cactus block-cut tree and cannot be adjacent to one another; choosing one neighbor at each vertex induces the net. Conversely a net's triangle is a triangle block and its three leaves certify the three external incidences. Thus a connected cactus is beautiful **if and only if** (i) every cycle block is a triangle or an even cycle of length at least six, and (ii) every triangle block has at least one vertex of degree exactly two in the complete cactus.

**2. Rooted branches under a parent block.** Let \(T\) count labelled cactus branches rooted at a vertex already incident to an external parent block. Such a root cannot itself certify the degree-two condition for any triangle among its *child* blocks. Every child triangle must therefore have at least one other vertex that has no further incident blocks. The rooted singleton has weight \(x\); the rooted branch with arbitrary descendants has weight \(T\). The unordered pair of children of a rooted triangle has weighted EGF
\[
 \frac{T^2-(T-x)^2}{2}=xT-\frac{x^2}{2}.
\]
A child edge contributes \(T\). A child even cycle of length \(2k\ge6\) contributes \(T^{2k-1}/2\): after fixing the root, the remaining labelled rooted branches appear in cyclic order, with reversal identified. Summing over \(k\ge3\) gives \(T^5/[2(1-T^2)]\). The child blocks incident to the root form an unlabelled set of labelled components. The labelled exponential formula therefore yields exactly
\[
 T=x\exp\left(T+s\left(xT-\frac{x^2}{2}\right)+\frac{tT^5}{2(1-T^2)}\right).
\]
This formal equation defines its coefficients inductively in \(x\), starting at \(T=x+O(x^2)\).

**3. Removing the external parent block.** A vertex-rooted complete cactus can be counted by \(T\), except when the global root itself is the unique degree-two witness of its sole incident triangle: in that situation the root has no other child blocks, while both vertices at the other corners of that triangle have nontrivial descendant blocks. The missing contribution is
\[
 \frac{sx}{2}(T-x)^2.
\]
These exceptional structures are disjoint from those counted in \(T\), since their root triangle has no bare nonroot corner. Every beautiful rooted cactus falls into exactly one of the two cases. The usual rooting identity \(xC_x=R\) now proves equation (1).

**4. Singular asymptotics.** At \(s=t=1\), write \(T=x+U\). The equation for \(U\) becomes
\[
 U=x\left[\exp\left(x+U+\frac{x^2}{2}+xU+\frac{(x+U)^5}{2(1-(x+U)^2)}\right)-1\right]. \tag{3}
\]
Its right side has nonnegative coefficients and nontrivial dependence on \(U\); the recursively generated tree terms have consecutive sufficiently large sizes. The characteristic positive solution satisfies \(\tau<1\) and is unique on the nonnegative combinatorial branch. Since the analytic system is strongly nonlinear with a positive second \(U\)-derivative, the standard smooth implicit-function singularity theorem for aperiodic nonnegative rooted-tree schemas applies to (3). It gives, in a slit neighborhood of the unique dominant real singularity,
\[
 T(x)=\tau-\kappa\sqrt{1-x/\rho}+O(1-x/\rho),
\]
with \(\kappa\) as displayed above: differentiating \(T=xe^{F(x,T)}\) gives \(H_x=\tau(1+\rho F_x)/\rho\) and \(H_{yy}=(1+\tau^2F_{yy})/\tau\) at the critical point. Substitution into (1) yields a square-root coefficient \(-(1+\rho(\tau-\rho))\kappa\). Transfer of square-root singularities gives the asserted \(A\,n!\rho^{-n}n^{-5/2}\) asymptotic.

For comparison, rooted **unrestricted** labelled cacti satisfy
\[
 U_0=x\exp\left(U_0+\frac{U_0^2}{2(1-U_0)}\right).
\]
This is the standard edge-and-cycle block formula, also consistent with the earlier labelled cactus enumeration [2]. Its characteristic pair is defined by \(\tau_0=\rho_0\exp(\tau_0+\tau_0^2/[2(1-\tau_0)])\) and \(1=\tau_0\partial_y(y+y^2/[2(1-y)])|_{y=\tau_0}\). The analogous amplitude is \(A_0=\tau_0\sqrt{2/(1+\tau_0^2F_0''(\tau_0))}/(2\sqrt\pi)\). Here \(\rho_0\approx0.238740143685117\) and \(A_0\approx0.120149812501170\). Taking the ratio of the two asymptotics yields equation (2). In particular beautiful cacti are exponentially rare inside all labelled cacti.

## Verification

The standalone program `verify.py` runs using Python 3 and its standard library only:

```sh
python3 verify.py
```

It independently expands the two-marked formal series using exact rational arithmetic through nine vertices and matches the totals \(1,1,4,28,290,3936,66472,1352632,32325372\). Its second check enumerates all simple labelled graphs on at most six vertices, independently recognizes cactus blocks using a depth-first lowlink algorithm, and directly tests forbidden **induced** subgraphs \(C_4,C_5\), gem, net, and watch without using the triangle-degree simplification. The bivariate distribution of accepted graphs matches the formal series exactly at every tested order. The direct six-vertex total is \(3936\), including exactly \(60\) labelled six-cycles. All checks finish with `VERIFY_OK`.

The finite checks do not prove the all-order generating functions or asymptotic assertions. Those are deduced from the block decomposition and analytic schema above. Numerical constants were independently evaluated from the displayed characteristic equations; the approximations do not replace those defining equations.

## Relationship to prior work

Wunderlich's 2026 Theorem 1.1 [1] supplies the necessary and sufficient forbidden-induced-subgraph characterization of beautiful graphs, but does not state an exact labelled cactus generating function, a two-cycle-type refinement, or an exponential density. The present cactus characterization is a specialization of his theorem; novelty is claimed for the full block-coupled enumeration and its asymptotic consequences, **not** for his general characterization.

Voblyi and Meleshko [2] enumerate labelled block-cactus graphs and discuss asymptotic counts of related unrestricted classes. Their unrestricted block product does not impose the local requirement that at least one vertex in each triangle have no other incident blocks; naive specialization of allowed block sizes therefore overcounts. OEIS A091485 [3] counts all labelled triangular cacti with bridges, not the present class: its six-vertex value is \(3996\), while the present six-vertex class has \(3936\). In fact the net removes \(120\) labelled triangular cacti at order six, while \(60\) labelled six-cycles are added. Mathar [4] studies unlabelled graphs with vertex-disjoint cycles, a different counting convention and narrower cactus topology.

## Limitations

Only connected simple cacti are counted, not all beautiful graphs, general block-cactus graphs with larger clique blocks, or unlabelled cacti. The result depends on Wunderlich's externally published characterization and on the standard smooth implicit-function transfer theorem. The asymptotic constants are defined implicitly; their displayed decimals are approximations, not certified enclosures. Finite computational checks cover nine vertices for formal-series coefficients and six for direct forbidden-subgraph tests. Equivalent earlier counting formulas under different terminology remain a possible historical-priority risk. Independent mathematical audit has not been performed.

## References

[1] H. Wunderlich, *A forbidden-induced-subgraph characterization of beautiful graphs*, arXiv:2610.07924v1, first submitted 6 October 2026. https://arxiv.org/abs/2610.07924

[2] V. A. Voblyi and A. K. Meleshko, *Enumeration of Labeled Block-Cactus Graphs*, Journal of Applied and Industrial Mathematics 8 (2014), 422–427. DOI:10.1134/S1990478914030156.

[3] OEIS A091485, *Number of labeled 2,3 cacti (triangular cacti with bridges)*. https://oeis.org/A091485

[4] R. J. Mathar, *Counting Connected Graphs without Overlapping Cycles*, arXiv:1808.06264v1 (2018). https://arxiv.org/abs/1808.06264
