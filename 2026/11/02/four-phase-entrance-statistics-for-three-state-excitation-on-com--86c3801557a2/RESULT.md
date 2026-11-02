# Four-phase entrance statistics for three-state excitation on complete split graphs

## Finding
For every pair of integers \(m,n\ge1\), consider synchronous three-state Greenberg–Hastings excitation on the labelled complete split graph \(G_{m,n}=K_m\vee\overline{K_n}\). Let \(D_{t,p}(m,n)\) count labelled initial colorings whose **first periodic configuration** occurs after exactly \(t\) simultaneous updates and whose eventual least period is \(p\). Put
\[
x=2^m-2,\qquad y=2^n-2,\qquad
u=3^m-3\cdot2^m+3,\qquad v=3^n-3\cdot2^n+3.
\]
Then the complete distribution is

| \(t\) | \(D_{t,1}\) | \(D_{t,3}\) |
|---:|---:|---:|
| 0 | \(1\) | \(uv+3uy+3u+3xy+3x\) |
| 1 | \(xy+2x+2y+3\) | \(xv+xy\) |
| 2 | \(v+xy+2x+3y+3\) | \(xv+xy\) |
| 3 | \(v+xy+2x+2y+2\) | \(xv+xy\) |
| 4 | \(v+2y\) | \(0\) |

Every other entry/period pair has count zero. Thus \(F^{7}=F^{4}\) on the entire state space. The maximum first-entry time is exactly \(4\) for \(n\ge2\) and exactly \(3\) for \(n=1\), for every \(m\ge1\).

There is one fixed configuration, the all-resting state. The exact number of initial colorings attracted to it is
\[
E(m,n)=3^{n+1}+3(2^m-2)2^n.
\]
All other trajectories eventually enter a primitive three-cycle; their number of distinct primitive orbits is
\[
Q_3(m,n)=\frac{(3^m-3\cdot2^m+3)3^n+3(2^m-2)(2^n-1)}{3}.
\]
For each **fixed clique size \(m\ge3\)**, conditional on eventual period-three oscillation and with \(n\to\infty\), the entrance-time distribution converges to
\[
\mathbb P(t=0\mid p=3)\longrightarrow\frac{u}{3^m-3},\qquad
\mathbb P(t=j\mid p=3)\longrightarrow\frac{2^m-2}{3^m-3}\quad(j=1,2,3).
\]
For \(m=3\), the four probabilities are **exactly \(1/4\)** in the limit: the entry times \(0,1,2,3\) become equiprobable. This is the unique nondegenerate clique size for which all four limiting masses coincide. For \(m\ge4\), the immediately-periodic class strictly dominates each delayed oscillatory class in this limit. In contrast, the probability of being initially periodic tends to one whenever \(m\to\infty\), uniformly over \(n\ge1\). The \(m=2\) book-graph entrance law and its three-way equidistribution are already known and are not claimed as new here.

## Assumptions and scope
The two vertex sets are disjoint and labelled; all edges within the \(m\)-vertex clique and between the two parts are present, while no edges occur among the \(n\) independent vertices. Each vertex has color \(0\) (rest), \(1\) (excited), or \(2\) (refractory). A color-\(1\) vertex changes to \(2\), and a color-\(2\) vertex changes to \(0\). A resting vertex changes to \(1\) if and only if a neighbor is excited; otherwise it remains at \(0\). Updates are synchronous and use the previous, not partially updated, configuration. The graph and rule are deterministic. The entry time \(t\) is the least nonnegative integer for which the configuration after \(t\) updates belongs to a periodic orbit; the orbit period is measured in simultaneous updates. A singleton part is allowed. Empty parts, other refractory lengths, higher excitation thresholds, and asynchronous updates are not covered.

## Proof
**1. Exact 49-state reduction.** For a coloring define two nonempty three-bit masks \(C,I\in\{1,\ldots,7\}\), where bit \(j\) indicates that color \(j\in\{0,1,2\}\) occurs in the clique or independent part. Let \(e_C=\mathbf1_{\{C\mathbin{\&}2\ne0\}}\) and \(e_I=\mathbf1_{\{I\mathbin{\&}2\ne0\}}\). On an individual color support mask \(M\), define
\[
\Phi_e(M)=
(4\,\mathbf1_{\{M\mathbin{\&}2\ne0\}})
\mathbin{|}(\mathbf1_{\{M\mathbin{\&}4\ne0\}})
\mathbin{|}\Bigl((2e+1-e)\mathbf1_{\{M\mathbin{\&}1\ne0\}}\Bigr),
\]
where \(\mathbin{|}\) denotes bitwise OR. The exact mask evolution is
\[
(C,I)\longmapsto\bigl(\Phi_{e_C\lor e_I}(C),\Phi_{e_C}(I)\bigr).
\]
Indeed, a resting clique vertex sees an excited neighbor exactly when an excited color occurs anywhere (the vertex itself is resting); a resting independent vertex sees an excited neighbor exactly when an excited clique vertex exists. Non-resting colors advance unconditionally. This reduction loses no information needed for the entry-time classification because the same old color in a given part always has the same successor color.

**2. Exhaustive finite recurrent classification.** The transition above has exactly \(49\) possible nonempty mask pairs. Direct substitution yields the following recurrent components, with masks written as decimal integers:

- Fixed support \((1,1)\), representing the all-zero microscopic fixed point.
- Three-step support cycles \((3,4)\to(6,1)\to(5,2)\to(3,4)\), \((3,5)\to(6,3)\to(5,6)\to(3,5)\), \((7,1)\to(7,2)\to(7,4)\to(7,1)\), and \((7,3)\to(7,6)\to(7,5)\to(7,3)\).
- Fixed support \((7,7)\), with every represented microscopic state rotating all vertex colors by one modulo three on each update.

The remaining \(35\) support pairs flow into these components in at most \(4\) steps. On every recurrent component other than \((1,1)\), every color-\(0\) vertex is excited on each update, so every vertex advances by one modulo three. Consequently all microscopic recurrent configurations outside zero have **least** period three, even when their support pair is fixed. Entering a recurrent support pair is precisely entering a microscopic periodic orbit: the recurrent color maps are bijective on represented colors, while a microscopic periodic orbit must project to a recurrent support pair. The complete, reproducible 49-row mask transition/classification table is embedded as `support_table.csv`; the transparent standalone script `verify_split_gh.py` reconstructs it from the local rule.

**3. Counting labelled configurations.** Exactly one coloring of a labelled nonempty part has a prescribed singleton color support, exactly \(2^k-2\) colorings have a prescribed two-color support, and exactly \(3^k-3\cdot2^k+3\) colorings have all three colors, for part size \(k\ge1\). For each pair of masks, multiply these surjection numbers for the clique and independent part. Partition the 49 mask pairs by their first periodic entry \(t\) and final microscopic least period \(p\), then sum. The nine resulting coefficient polynomials are the displayed table, with no overlap between mask pairs. Summing its period-one column simplifies to the stated expression for \(E(m,n)\). Its entry-zero period-three cell divided by three gives \(Q_3(m,n)\), since each such orbit contains exactly three labelled configurations.

**4. Sharp boundaries and asymptotics.** The only masks first entering after four steps have clique mask \(1\) and independent mask \(3\), \(6\), or \(7\). Such a mask is realizable exactly when \(n\ge2\). With \(n=1\), the mask \((1,2)\) has first-entry time three, so the smaller maximum is attained. For fixed \(m\ge3\) and \(n\to\infty\), the period-three basin is \((3^m-3)3^n-3x2^n\), the immediate oscillatory class is \(u3^n+3x(2^n-1)\), and each delayed class at \(t=1,2,3\) is \(x(3^n-2^{n+1}+1)\). Dividing yields the conditional limit in the statement. Four-way equidistribution requires \(u=x\), equivalent to \(3^m-4\cdot2^m+5=0\). The latter expression vanishes at \(m=3\), while for \(m\ge4\) it is strictly positive: writing it \(f(m)\), the identity \(f(m+1)-3f(m)=4\cdot2^m-10>0\) for \(m\ge2\) proves this inductively from \(f(4)=22\). The case \(m=2\) has \(u=0\), and its previously known three-way conditional equidistribution is a consistency check rather than new. For fixed or varying \(n\ge1\), the fraction of initially period-three configurations is at least \(u/3^m\), which tends to one as \(m\to\infty\). These computations establish the assertions without finite-size extrapolation.

## Verification
Running `python3 verify_split_gh.py` from the extracted package reconstructs and checks all 49 support transitions and all nine polynomial coefficient identities using only the Python standard library. A separate direct vertex-neighborhood implementation then compares full microscopic trajectories against the formulas for every pair \(1\le m,n\le7\) satisfying \(m+n\le10\): in total 477,315 labelled initial configurations across 39 graph-size pairs. Exact formula, extinction-basin and sharp-clock checks also run on 49 size pairs. The embedded `verification_output.txt` reports the results and all support-transition rows. All calculations use exact integer arithmetic. These tests corroborate the finite-quotient proof; tests alone would not prove the theorem for all sizes.

## Relationship to prior work
Gravner, Lyu, and Sivakoff (arXiv:1610.07320v1, initially posted 24 October 2016), Theorem 3 and Section 4, characterize fixation versus persistent excitation on **arbitrary finite connected graphs** through contour integrals of an initial edge 1-form. That stronger qualitative criterion already determines which individual initial states eventually synchronize, and its diameter bound implies a general upper bound on the extinction transient on the present graphs. Neither the recurrent-versus-transient criterion nor the qualitative upper bound is claimed anew. The contribution here is the fully evaluated, all-clique-size nine-cell **first-periodic-entry distribution** for \(m\ge3\), its complete primitive-orbit and basin census, and the four-phase conditional limit, especially the unique four-way equidistribution at \(m=3\). The book-graph case \(m=2\), including its exact first-entry census and three-way delayed-time equidistribution, was established previously; those formulas are included for continuity only and are not new. Unlike the contour-integral test, these statements quantify precisely how many labelled initial states follow each clock and final period. The cited primary text does not tabulate these counts or classify first periodic entry by time for complete split graphs. The earlier book-graph case and the general qualitative fixation criterion are explicitly excluded from the new-priority assertion.

## Limitations
This is an exact finite-graph result for threshold-one, three-state synchronous excitation; it does not cover general split graphs or different local rules. The complete-support calculation is particular to this two-module homogeneous graph family. Earlier general theory already supplies qualitative oscillation/fixation classification, and the present exact counts could in principle be recovered by further nontrivial enumeration from that theory. No claim is made that the general criterion or the period-three mechanism is newly discovered. Equivalent enumerative formulas may exist in historical literature not surfaced by searches; in particular this statement generalizes, rather than claims priority over, a known complete \(m=2\) book-graph calculation. No external independent audit has been performed.

## References
1. J. Gravner, H. Lyu, and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (initial public posting 24 October 2016), especially Section 2, Theorem 3 and Section 4. https://arxiv.org/html/1610.07320v1
