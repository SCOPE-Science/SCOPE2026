# A parity-resolved last-coverage law for alternating zero-drift walks on cycles

## Finding

Fix an integer \(n\ge3\), a parameter \(0<p<1\), and \(q=1-p\). A nearest-neighbour random walk starts at vertex \(0\) of the oriented cycle \(C_n\). Its clockwise probability at step \(t\to t+1\) is \(p\) when \(t\) is even and \(q\) when \(t\) is odd; all step choices are independent. Let \(L\in\{1,\ldots,n-1\}\) be the last vertex discovered before complete coverage. The walk completes coverage almost surely.

**Odd-cycle law.** If \(n=2m+1\) with \(m\ge1\), then, for every permitted label,
\[
\Pr(L=2j+1)=\frac{q}{m}\quad(0\le j<m),\qquad
\Pr(L=2j)=\frac{p}{m}\quad(1\le j\le m).
\]
Thus all odd labels tie and all even labels tie, with the two classes having different probabilities whenever \(p\ne1/2\).

**Even-cycle law.** If \(n=2m\) with \(m\ge2\), set
\[
A=\frac{q}{m-p},\qquad B=\frac{p}{m-q},\qquad
\Delta=\frac{p-q}{(m-p)(m-q)}.
\]
Then the entire last-discovery law is
\[
\Pr(L=2j+1)=A+j\Delta\quad(0\le j<m),\qquad
\Pr(L=2j)=B-(j-p)\Delta\quad(1\le j<m).
\]
For \(p>1/2\), the odd-label profile increases strictly and the even-label profile decreases strictly. The reverse holds for \(p<1/2\). In all cycle sizes, the law is uniform **if and only if** \(p=1/2\).

Although the walk has zero mean displacement over each pair of consecutive steps, its last-discovered vertex is generally not uniformly distributed. The result gives elementary closed forms for every label, cycle size, and nondegenerate alternating complementary bias; no infinite trajectory series or numerical truncation is required.

## Assumptions and scope

The state space is \(C_n=\mathbb Z/n\mathbb Z\), the starting vertex is \(0\), and clockwise means adding \(1\) modulo \(n\). A step at time \(t\) adds \(+1\) with probability \(p\) for even \(t\) and \(q\) for odd \(t\); otherwise it adds \(-1\). The schedule is deterministic and starts in the \(p\) phase. All probabilities are strictly between zero and one. The vertex \(L\) is the vertex first visited at the cover time, not the last vertex occupied during a longer observation window.

The deterministic complementary schedule has independent two-step blocks with expected net displacement zero: the clockwise probabilities in each block sum to one. The statement does not extend by continuity to the degenerate endpoints \(p=0\) or \(p=1\), where complete coverage can fail.

## Proof

**1. Spatialization of the temporal bias.** Lift the walk to \(S_0=0\) on \(\mathbb Z\), with increments \(\pm1\), so that the cycle position is \(S_t\bmod n\). Always \(S_t\equiv t\pmod2\). Therefore the lifted process is a *time-homogeneous* birth-and-death chain: from an even integer its right-step probability is \(p\), and from an odd integer it is \(q\). Its left-step probabilities are respectively \(q\) and \(p\).

Define a strictly increasing scale function \(s:\mathbb Z\to\mathbb R\) by
\[
s(2h)=h,\qquad s(2h+1)=h+q\qquad(h\in\mathbb Z).
\]
The increment \(s(x)-s(x-1)\) equals \(p\) for even \(x\) and \(q\) for odd \(x\). At every integer, the right probability multiplied by the right scale increment equals the left probability multiplied by the left scale increment, both being \(pq\). Hence \(s(S_t)\) is a martingale. For any integers \(u<x<v\), bounded optional stopping at the first exit from \((u,v)\) gives
\[
\Pr_x(\tau_v<\tau_u)=\frac{s(x)-s(u)}{s(v)-s(u)}.
\tag{1}
\]
The stopped interval is finite and every jump probability is positive, so the exit time is almost surely finite. Formula (1) also holds at the endpoints with the usual zero-one interpretation.

**2. Exact two-boundary characterization.** Fix \(k\in\{1,\ldots,n-1\}\) and set
\[
a=k-n+1,\qquad b=k-1.
\]
Then \(a\le0\le b\), and \([a,b]\cap\mathbb Z\) consists of \(n-1\) consecutive integers whose residues are exactly the vertices other than \(k\). The nearest lifts of the forbidden residue immediately outside this interval are \(a-1=k-n\) and \(b+1=k\). Thus \(L=k\) **if and only if** the lifted walk hits both \(a\) and \(b\) before hitting either \(a-1\) or \(b+1\). This equivalence uses nearest-neighbour steps: a trajectory that has visited both endpoints has visited the entire intervening interval, while the first exit through either adjacent forbidden lift would discover \(k\) prematurely.

The first of \(a,b\) reached partitions this event into two disjoint alternatives. Using (1) twice and the strong Markov property gives the exact identity
\[
\begin{aligned}
\Pr(L=k)={}&
\frac{s(b)-s(0)}{s(b)-s(a)}
\frac{s(a)-s(a-1)}{s(b)-s(a-1)}\\
&+\frac{s(0)-s(a)}{s(b)-s(a)}
\frac{s(b+1)-s(b)}{s(b+1)-s(a)}.
\end{aligned}
\tag{2}
\]
If \(a=0\) or \(b=0\), the corresponding first-hit factor equals one and the other equals zero, and (2) still applies. Because the underlying finite cycle with the alternating clock phase is an irreducible finite-state chain on its reachable class, eventual coverage occurs almost surely. Alternatively, blocks of \(n\) consecutive clockwise steps have uniformly positive probability, giving a geometric tail bound on the time to cover.

**3. Odd cycles.** Write \(n=2m+1\). If \(k=2j+1\), then \(a=2(j-m)+1\) is odd and \(b=2j\) is even. In (2), the two conditional factors for reaching the opposite endpoint after the first hit are both \(q/m\), because
\[
s(a)-s(a-1)=s(b+1)-s(b)=q,
\qquad s(b)-s(a-1)=s(b+1)-s(a)=m.
\]
The first-hit factors sum to one, proving \(\Pr(L=2j+1)=q/m\). If \(k=2j\), then \(a=2(j-m)\) is even and \(b=2j-1\) is odd. Both conditional factors are \(p/m\) by the same calculation, yielding \(\Pr(L=2j)=p/m\).

**4. Even cycles.** Write \(n=2m\), \(m\ge2\). When \(k=2j+1\), the boundaries are \(a=2(j-m+1)\), \(b=2j\), both even. The probabilities of reaching \(a\) or \(b\) first are respectively \(j/(m-1)\) and \((m-1-j)/(m-1)\). The subsequent probabilities of reaching the opposite boundary before discovering \(k\) are respectively \(B=p/(m-q)\) and \(A=q/(m-p)\). Therefore
\[
\Pr(L=2j+1)=\frac{jB+(m-1-j)A}{m-1}=A+j\Delta,
\]
since \(B-A=(m-1)\Delta\).

When \(k=2j\), both boundaries are odd. The first-hit probabilities of \(a\) and \(b\) are \((j-p)/(m-1)\) and \((m-j-q)/(m-1)\). The probabilities of subsequently hitting the opposite boundary before the forbidden residue are respectively \(A\) and \(B\). Consequently
\[
\Pr(L=2j)=\frac{(j-p)A+(m-j-q)B}{m-1}=B-(j-p)\Delta.
\]
All denominators are positive on the specified domain. The stated monotonicities follow from the sign of \(\Delta\). For odd cycles, a uniform last-vertex law forces \(p=q\). For even cycles, equality at labels \(1\) and \(n-1\) forces \(A=B\), which implies \((p-q)(m-1)=0\), hence \(p=q\). At \(p=q=1/2\), each displayed probability equals \(1/(n-1)\). This proves the classification.

## Verification

The accompanying `verify.py` is a Python standard-library program. It first evaluates (2) exactly in rational arithmetic for cycle sizes \(3\) through \(64\) and five rational choices of \(p\), checking the closed forms, positivity, and normalization. Independently, it solves finite absorbing Markov chains on states recording the visited vertex mask, current position, and temporal phase, without using the scale-function formula. Those exact-rational results agree with the theorem for sizes \(3\) through \(7\) and four rational choices of \(p\). Execution produced `VERIFIED 20580 exact rational checks`.

These are finite computational checks only. The proof above establishes all \(n\ge3\) and all real \(p\in(0,1)\). Reproduction: run `python3 verify.py` with Python 3.10 or later; no external packages are required.

## Relationship to prior work

Idnani and Salem (2026, arXiv:2610.15115v1) formulate last-coverage probabilities for the same cycle walk with an arbitrary deterministic time-varying bias, giving an infinite trajectory series and an error-controlled truncation. They also obtain a geometric closed form for *constant* bias and recover the classical uniform law for a symmetric walk. The present result does **not** claim those constructions or the classical gambler's-ruin formula. Instead, it evaluates a structurally special *alternating complementary* schedule exactly, with an odd/even cycle-size dichotomy and a persistent parity bias despite zero two-step drift. Mere substitution into the general series does not give the evaluated finite formulas or their parity geometry.

Lovász and Winkler (1993) establish the uniform last-new-vertex property for ordinary symmetric graph walks; Buchanan, Horn and Rombach (2022/2023) extend an associated classification to directed graphs with uniform outgoing-neighbor choices. Haslegrave, Sauerwald and Sylvester (2021) investigate controller-biased walks and cover-time bounds in a different time-dependent model. These do not state the complementary two-phase exact law. No priority claim is made for the underlying scale-function or two-sided hitting machinery.

## Limitations

Only independent nearest-neighbour steps, a fixed known initial clock phase, and exactly complementary two-periodic probabilities are covered. A different starting phase exchanges \(p\) and \(q\); noncomplementary or longer-period schedules require further work. The result determines the last-vertex probabilities, not the full joint distribution with the cover time. The general exact-series result in the motivating paper already represents this law implicitly; the new content is its closed-form evaluation and the resulting parity-resolved structure. An unlocated general periodic-environment cover-law evaluation could potentially imply the expressions, and an earlier symmetric-cover-tour article was accessible only by abstract; independent priority assessment has not been performed.

## References

1. K. Idnani and J. Salem, *Last-Coverage Probabilities of Random Walks on Cycle Graphs for Symmetric, Biased, and Time-Dependent Walks*, arXiv:2610.15115v1, submitted October 10, 2026. https://arxiv.org/html/2610.15115v1
2. L. Lovász and P. Winkler, *A Note on the Last New Vertex Visited by a Random Walk*, Journal of Graph Theory 17 (1993), 593–596. https://doi.org/10.1002/jgt.3190170505
3. C. Buchanan, P. Horn and P. Rombach, *On the Last New Vertex Visited by a Random Walk in a Directed Graph*, arXiv:2209.08079v2 (2022); Discrete Mathematics Letters 11 (2023), 96–98. https://arxiv.org/html/2209.08079v2
4. J. Haslegrave, T. Sauerwald and J. Sylvester, *Time Dependent Biased Random Walks*, arXiv:2006.02475v2 (2021). https://arxiv.org/html/2006.02475v2
