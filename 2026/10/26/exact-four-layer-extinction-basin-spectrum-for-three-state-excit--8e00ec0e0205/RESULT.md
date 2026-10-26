# Exact four-layer extinction-basin spectrum for three-state excitation on complete tripartite graphs

## Finding

For every triple of integers \(a,b,c\ge1\), let \(K_{a,b,c}\) carry the synchronous three-state Greenberg–Hastings rule specified below. For a configuration \(x\), let \(T(x)\) be the first time the all-rest configuration is reached, and put \(T(x)=\infty\) when extinction never occurs. With \(N=a+b+c\), define
\[
q_k=3^k-2^{k+1}+1,\qquad Q=q_a+q_b+q_c,\qquad S=2^a+2^b+2^c.
\]
The number \(d_t=|\{x:T(x)=t\}|\) of labelled initial configurations of each **finite** extinction time is exactly
\[
\begin{aligned}
d_0&=1,\\
d_1&=2^N-1,\\
d_2&=2^N-1+Q,\\
d_3&=2^N+4-S+Q,\\
d_4&=S-6+Q,\\
d_t&=0\quad(t\ge5).
\end{aligned}
\]
Every other initial configuration retains excitation forever. In particular the complete extinction-basin cardinality is
\[
E(a,b,c)=3\cdot2^N-3+3Q.
\]
Finite extinction occurs **if and only if** the initial assignment has no transversal triangle with the three distinct states \(0,1,2\). The extinction-time cutoff four is sharp precisely when at least one of the part sizes exceeds one; for \(K_{1,1,1}\) the sharp cutoff is three.

For independent uniformly distributed initial vertex states, this produces two sharply different shape regimes:
\[
\Pr_{K_{m,1,1}}(T<\infty)=\frac13+\frac23(2/3)^m\longrightarrow\frac13,
\]
whereas
\[
\Pr_{K_{m,m,m}}(T<\infty)=\frac{3\cdot8^m+9\cdot3^m-18\cdot2^m+6}{27^m}\sim3(8/27)^m.
\]

## Assumptions and scope

The graph \(K_{a,b,c}\) is the simple complete tripartite graph with three nonempty, labelled vertex parts of sizes \(a,b,c\). Vertex states lie in \(\{0,1,2\}\), interpreted as resting, excited and refractory. At each integer time all vertices update simultaneously: state \(1\) becomes \(2\), state \(2\) becomes \(0\), and state \(0\) becomes \(1\) exactly when at least one adjacent vertex currently has state \(1\); otherwise it stays \(0\). There is no stochastic updating, self-loop or random tie convention. Counts are of labelled vertex assignments, not colorings modulo symmetries.

## Proof

**1. A permanent-excitation obstruction.** Suppose a transversal triangle (one vertex in each part) initially has states \(0,1,2\) in some order. Its three states rotate synchronously \(0\mapsto1\mapsto2\mapsto0\): at each step the vertex in state \(0\) is adjacent to the vertex in state \(1\), while the other two transitions are automatic. This triangle therefore never loses excitation, even with arbitrary extra neighbors. Thus its presence rules out extinction.

**2. Exact absence-of-obstruction classification.** Let \(U_1,U_2,U_3\) be the sets of colors present in the three respective graph parts. A transversal rainbow triangle exists exactly when the three sets admit a system of distinct representatives. If all three colors occur somewhere but no such triple exists, Hall's condition fails. A one-set violation is impossible because all sets are nonempty, and a three-set violation is impossible because the global union contains all three colors. Therefore a two-set violation occurs: two of the parts have union size one, i.e., they are both monochromatic in a common color \(j\). Conversely, those two equal-color parts prevent any rainbow transversal. Consequently, the no-rainbow assignments partition uniquely into (A) assignments using at most two colors globally and (B) assignments using all three colors with exactly two parts monochromatic in the same color \(j\). In (B) the remaining part must contain both other colors, and the unique exceptional part and color \(j\) are determined by the configuration.

**3. Direct finite-time dynamics.** If only colors \(0,2\) occur initially, the system is all-rest after one step. If only \(1,2\) occur, it becomes all-rest after two steps. If only \(0,1\) occur, every vertex is at rest after three steps except possibly vertices initially in state \(0\) in the unique part containing *all* initial state-\(1\) vertices. Those exceptional vertices are refractory at time three and reach rest at time four. Hence a \(\{0,1\}\)-assignment with both colors has time four precisely when its excited vertices are confined to one part and that part contains both \(0\) and \(1\); all other genuinely mixed assignments have time three. All-\(0\) has time zero; all-\(1\) has time two; all-\(2\) has time one.

For case (B), fix the exceptional part and the common monochromatic color \(j\) of the other two parts. Every color absent from the exceptional part is already represented by the monochromatic parts only when it equals \(j\); hence the exceptional part necessarily contains both colors unequal to \(j\). A direct time-step check using the preceding update rule gives extinction at time \(2\) for \(j=2\), at time \(3\) for \(j=1\), and at time \(4\) for \(j=0\). These checks hold irrespective of whether \(j\) itself is also present in the exceptional part. For example, in the \(j=0\) case the other two parts evolve as \(0,1,2,0\), and initially refractory vertices of the exceptional part traverse \(2,0,1,2,0\), forcing the fourth step. This also proves extinction for every no-rainbow initial assignment. Combined with step 1 it proves the claimed if-and-only-if criterion and finite bound.

**4. Exact enumeration.** A designated exceptional part with \(k\) vertices contains both specified other colors in exactly \(q_k=3^k-2\cdot2^k+1\) ways, by inclusion-exclusion; the two other parts are forced monochromatic. Therefore for each \(j\in\{0,1,2\}\), case (B) has exactly \(Q\) assignments, contributing respectively to \(d_4,d_3,d_2\).

In case (A), \(\{0,2\}\) assignments provide \(2^N-1\) time-one states after excluding all-zero. \(\{1,2\}\) assignments contribute \(2^N-1\) time-two states after excluding all-two. At time four, \(\{0,1\}\) assignments contribute \(\sum_{k\in\{a,b,c\}}(2^k-2)=S-6\), since the single excited-containing part must be mixed. Of the \(2^N\) assignments using \(\{0,1\}\), excluding all-zero, all-one and these time-four assignments leaves \(2^N-2-(S-6)=2^N+4-S\) time-three states. The pure constant states have already been accounted for, so the categories are pairwise disjoint. Adding the \(Q\) contributions yields each asserted coefficient and \(E=3\cdot2^N-3+3Q\).

For \(a=b=c=1\), both \(Q\) and \(S-6\) vanish, while \(d_3>0\). If some part has at least two vertices, \(S-6>0\), hence a time-four configuration exists. Finally, substituting \((a,b,c)=(m,1,1)\) and \((m,m,m)\) into \(E\) and dividing by \(3^N\) proves the two displayed probability formulas and their limits.

## Verification

The self-contained Python script `verify.py` enumerates all \(3^N\) labelled initial configurations and directly applies the vertex update rule for every \(1\le a\le b\le c\le4\) with \(N\le10\). It independently calculates the five finite-time classes, checks their precise formulas, verifies that every remaining state is in a nonzero three-cycle by time four, and checks the sharp cutoff. The recorded output `verification_output.txt` reports `VERIFY_OK triples=18 total_initial_states=206172`. These finite checks corroborate, but do not replace, the all-size analytical argument above.

## Relationship to prior work

Fisch, Gravner and Griffeath's early excitable-automata work provides the historical Greenberg–Hastings framework. Gravner, Lyu and Sivakoff prove a general graph-circulation criterion for eventual extinction or sustained excitation. Doba studies the finite-graph Greenberg–Hastings dynamics through circuit structure. A previously established complete-multipartite periodic-orbit census, *Four-step periodic entry and exact three-cycle census for multipartite excitable dynamics* (identifier `2327e9a1-48f2-4b71-8d77-fd24dccd688a`), also gives a uniform four-step **entry-to-periodicity** result and a count of periodic configurations. None of these ingredients is claimed new here. The contribution isolated above is the **exact labelled extinction-basin time histogram**, the necessary-and-sufficient rainbow-transversal test on tripartite graphs, and the explicitly contrasted basin probabilities in two graph-shape regimes. Periodic-orbit counts do not directly give attraction-basin cardinalities or the counts at each finite first-hitting time.

## Limitations

Only the synchronous three-state rule on complete tripartite graphs with all parts nonempty is covered. No claim is made about more than three parts, asynchronous updates, stochastic convergence times, basin sizes of individual nonzero attractors, or general finite graphs. The novelty comparison covers indexed research and accessible closely related original texts; an unindexed equivalent counting identity remains possible. Independent scientific validation has not been performed.

## References

1. R. Fisch, J. Gravner and D. Griffeath, *Threshold-Range Scaling of Excitable Cellular Automata*, arXiv:patt-sol/9304001, first public version 1993-04-02.
2. J. Gravner, H. Lyu and G. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320 (2016).
3. N. Doba, *The Time Evolution of a Greenberg-Hastings Cellular Automaton on a Finite Graph*, *Complex Systems* 27 (2018), 101–126, DOI: 10.25088/ComplexSystems.27.2.101.
4. *Four-step periodic entry and exact three-cycle census for multipartite excitable dynamics*, prior result, opaque identifier `2327e9a1-48f2-4b71-8d77-fd24dccd688a`.
