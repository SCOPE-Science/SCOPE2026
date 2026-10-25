# A four-step relaxation law and complete orbit-depth census for bipartite excitable dynamics

## Finding

Consider the deterministic, synchronous three-state Greenberg–Hastings map on the **labelled** loopless complete bipartite graph \(K_{a,b}\), for arbitrary integers \(a,b\geq1\). Each vertex has state \(0\) (resting), \(1\) (excited), or \(2\) (refractory). A state \(0\) becomes \(1\) precisely when at least one neighbor is in state \(1\); otherwise it stays \(0\). States \(1\) and \(2\) become \(2\) and \(0\), respectively.

Write \(\tau(x)\) for the least nonnegative time at which \(F^{\tau(x)}(x)\) is on a periodic orbit, and \(\rho(x)\) for that orbit's least positive period. Define \(N_{p,t}(a,b)=\#\{x:\rho(x)=p,\ \tau(x)=t\}\). Set
\[
A=2^a,\quad B=2^b,\quad P=3^a,\quad Q=3^b,\qquad
U=A-2,\quad W=B-2,\quad V=P-3A+3,\quad Z=Q-3B+3.
\]
Here \(U,W\) count assignments onto a prescribed pair of states and \(V,Z\) count assignments onto all three states, on the corresponding part.

The **complete** nonzero orbit-depth census is

| Least eventual period \(p\) | Preperiod \(t\) | Number \(N_{p,t}(a,b)\) |
|:---:|:---:|---|
| 1 | 0 | \(1\) |
| 1 | 1 | \(AB-1\) |
| 1 | 2 | \(AB-2A-2B+P+Q+1\) |
| 1 | 3 | \(AB-3A-3B+P+Q+4\) |
| 1 | 4 | \(P+Q-A-B-2\) |
| 3 | 0 | \(VZ\) |
| 4 | 0 | \(2UW\) |
| 4 | 1 | \(2UW+UZ+VW\) |
| 4 | 2 | \(2UW+UZ+VW\) |
| 4 | 3 | \(UZ+VW\) |

All other \(N_{p,t}\) are zero. In particular, all \(3^{a+b}\) states enter a periodic orbit within **four** synchronous updates. The maximum preperiod is \(3\) when \(a=b=1\), and \(4\) otherwise. For \((a,b)\ne(1,1)\), exactly
\[
\boxed{3^a+3^b-2^a-2^b-2}
\]
initial configurations attain that maximum. The complete set of prime periods is \(\{1\}\), augmented by \(4\) when \(a,b\ge2\), and by \(3\) when \(a,b\ge3\). There are exactly
\[
\boxed{\frac{VZ}{3}\text{ primitive three-cycles},\qquad
\frac{UW}{2}\text{ primitive four-cycles}.}
\]
Thus the Artin–Mazur dynamical zeta function is
\[
\boxed{\zeta_F(z)=\frac{1}{(1-z)(1-z^3)^{VZ/3}(1-z^4)^{UW/2}}.}
\]
A further striking consequence is that **every configuration attracted to a three-cycle is already on that cycle**. In contrast, four-cycles admit transient branches of depths \(1,2,3\).

## Assumptions and scope

The graph has two nonempty, individually labelled independent parts of sizes \(a\) and \(b\), with an edge between every vertex of opposite parts and no edges within a part. Updates are parallel, deterministic, and have excitation threshold one. The three colors are distinguished and no quotient by graph automorphisms or global color shifts is taken. A preperiod is the *first* entrance time into a periodic orbit, not time to the all-resting state. The formula includes the small cases \(a=1\), \(b=1\), and \(a=b=1\). This theorem does not concern graphs missing any of the complete bipartite edges, stochastic excitation, or four-or-more-state variants.

## Proof

**1. Support factorization.** For a state \(x\), let \(C_A(x)\) and \(C_B(x)\) be the sets of colors occurring in its two graph parts. Both are nonempty subsets of \(\{0,1,2\}\), so there are at most \(7^2=49\) ordered support pairs for any fixed graph size (all 49 are realizable once both part sizes are at least three). If the opposite part contains color \(1\), every \(0\) in the given part goes to \(1\); otherwise all its \(0\)'s remain \(0\). In both cases colors \(1\) and \(2\) go to \(2\) and \(0\). Consequently the support pair at the next time depends *only* on the current support pair, via simultaneous application of these two explicit color maps. A missing color cannot be created by splitting an existing color, so the support cardinality within either part never increases.

**2. A complete 49-case finite certificate.** The following table gives, for *every* support pair, `p/t`, meaning the eventual primitive period \(p\) of **every actual configuration** with those supports and its exact preperiod \(t\). The row is the first part's support, the column the second part's support. The labels `01`, `02`, `12`, and `012` denote the corresponding sets of colors. The entries follow by repeatedly applying the two color maps from step 1 until reaching one of the three closed support classes described below. This is a finite exhaustive calculation over 49 explicitly given cases; the supplied verifier recomputes it independently from the transition rule.

| First part \\ second part | 0 | 1 | 2 | 01 | 02 | 12 | 012 |
|---|---|---|---|---|---|---|---|
| 0 | 1/0 | 1/3 | 1/1 | 1/4 | 1/1 | 1/4 | 1/4 |
| 1 | 1/3 | 1/2 | 1/2 | 1/3 | 1/3 | 1/2 | 1/3 |
| 2 | 1/1 | 1/2 | 1/1 | 1/2 | 1/1 | 1/2 | 1/2 |
| 01 | 1/4 | 1/3 | 1/2 | 1/3 | 4/0 | 4/2 | 4/3 |
| 02 | 1/1 | 1/3 | 1/1 | 4/0 | 1/1 | 4/1 | 4/1 |
| 12 | 1/4 | 1/2 | 1/2 | 4/2 | 4/1 | 1/2 | 4/2 |
| 012 | 1/4 | 1/3 | 1/2 | 4/3 | 4/1 | 4/2 | 3/0 |

The only support cycles are: the fixed pair `(0,0)`; the fixed pair `(012,012)`; and the two-cycle `(01,02) ↔ (02,01)`. At `(0,0)` every vertex is fixed. At `(012,012)` every vertex advances by one color modulo three on every update, so the actual configuration has exact period three. At `(01,02)` and `(02,01)`, two successive updates exchange the two present colors inside each part. That exchange cannot fix any configuration whose support contains both colors; four updates restore all colors, and the *actual* least period is exactly four. In these three support classes all configurations are already periodic. Outside them, the support has not yet reached a closed class, so no actual configuration can be periodic. This establishes that the table's `t` is the **minimal** periodic-entry time, not merely an upper bound.

**3. Converting supports into exact state counts.** For a specified \(k\)-element color support on a part of size \(m\), the number of assignments that use *each* color is, by inclusion–exclusion,
\[
w_m(k)=\sum_{j=0}^{k}(-1)^j\binom{k}{j}(k-j)^m.
\]
Since \(m\ge1\), these weights are \(w_m(1)=1\), \(w_m(2)=2^m-2\), and \(w_m(3)=3^m-3\cdot2^m+3\). Multiply the two support weights for each of the 49 table cells, and sum those cells with equal `p/t`. Direct grouping gives the ten formulas in the finding. For example, the four-cycle classes at depths \(0,1,2,3\) have respective weights
\[
2UW,\quad 2UW+UZ+VW,\quad 2UW+UZ+VW,\quad UZ+VW.
\]
The unique three-cycle support class weighs \(VZ\). The maximum-depth four-cell support configurations are `(0,01)`, `(0,12)`, `(0,012)` and their part-swapped counterparts, with weight \(2U+V+2W+Z=P+Q-A-B-2\). Such states exist exactly when at least one part has at least two vertices. For \(a=b=1\) the table has maximum feasible depth three. Summing all ten groups gives \(PQ=3^{a+b}\), independently confirming that all configurations are accounted for.

**4. Periodic-orbit and zeta identities.** Exactly one state is fixed. The \(VZ\) configurations of least period three partition into triples. The \(2UW\) configurations of least period four partition into quadruples, giving the stated integral primitive-orbit counts. Since no other periods exist, the Euler product defining the finite dynamical zeta function is the stated rational expression. The numerator-exponent integrality is automatic from the orbit partition.

## Verification

Run the included standalone script with `python3 verify.py`. It independently recomputes the 49 support transitions, detects their eventual support cycles, checks the table, evaluates all state-count formulas by support-weight inclusion–exclusion, and enumerates each individual three-state configuration for positive part sizes up to total size nine. It also compares 3000 seeded larger random configurations against the predictions by directly running the full vertex update rule. The observed result was:

```text
VERIFY_OK macro_pairs=49 exhaustive_states=72720 random_states=3000 support_table_and_all_formulas=verified
```

The theorem is all-size because the support-factorization proof checks all 49 **potential support pairs** regardless of graph size. Exhaustive testing of particular graph sizes by itself would not establish the unrestricted claim; it serves here as an additional independent check on the fully enumerated finite certificate.

## Relationship to prior work

Greenberg and Hastings introduced excitable-media dynamics, and Durrett and Griffeath developed rigorous asymptotic analysis for such models. Gravner, Lyu, and Sivakoff give an arbitrary-graph limiting-behavior description using covering spaces and cycle integrals; Doba derives an arbitrary-finite-graph criterion based on maximum cycle density. Those broader qualitative descriptions are *not* claimed as new here. The present statement instead identifies a sharp four-step cutoff and gives the **entire labelled-state two-parameter census by both first periodic-entry time and eventual least period**, including the exact periodic-orbit zeta function. The inspected texts do not state that census for complete bipartite graphs. The previous general theories may provide alternative routes to selected qualitative consequences, but do not directly give the displayed 49-support computation or its ten counting formulas. Historical priority remains open to independent checking.

## Limitations

The results require threshold-one deterministic three-state dynamics on a complete bipartite graph. They are not a classification of arbitrary graphs, stochastic models, higher thresholds, or higher-state excitable media. Exhaustive microstate verification is finite, though the proof itself is all-size. A full independent mathematical audit and exhaustive historical-priority review have not been performed. The 1978 foundational paper's original issue is identified by month, not by a verified first-public calendar day; the day-verified archival motivating source cited below was publicly posted on 1993-03-22.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, first posted 1993-03-22, https://arxiv.org/abs/patt-sol/9303002 .
2. J. M. Greenberg and S. P. Hastings, *Spatial Patterns for Discrete Models of Diffusion in Excitable Media*, SIAM J. Appl. Math. 34 (1978), 515–523, https://doi.org/10.1137/0134040 .
3. J. Gravner, H. Lyu, and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (2016-10-24), https://arxiv.org/pdf/1610.07320 .
4. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems 27 (2018), 101–126, https://doi.org/10.25088/ComplexSystems.27.2.101 .
