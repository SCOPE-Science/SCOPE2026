# Minimal skew forts and the skew-zero-forcing polynomial of complete prisms

## Finding

Write \(H_n=K_n\square K_2\) for the graph with vertices \(a_i,b_i\), \(i\in[n]\), edges joining every distinct pair in the same lettered layer and the matching edges \(a_ib_i\). For every integer \(n\ge3\), the **inclusion-minimal skew forts** are exactly the following three families of nonempty vertex subsets \(F\). Put \(A=\{i:a_i\in F\}\), \(B=\{i:b_i\in F\}\), and \(c=|A\cap B|\):

1. \(A=B\) and \(|A|=|B|=2\), for every \(n\ge3\).
2. \((|A|,|B|,c)=(1,n-1,0)\) or \((n-1,1,0)\), for \(n\ge4\).
3. \(|A|=|B|=3\) and \(c\le1\), for \(n\ge5\).

A skew fort is a nonempty set \(F\) such that every vertex has either zero or at least two neighbors in \(F\). Equivalently, no skew color change can occur while exactly \(F\) remains white.

For every integer \(n\ge4\), define the polynomial

\[
\begin{aligned}
W_n(t)={}&2(1+t)^n-1\\
&+2nt\sum_{b=1}^{n-2}\binom nb t^b-n^2t^2
+2n(n-1)t^n\\
&+2\binom n2t^2\sum_{b=2}^{n-2}
\left(\binom nb-\binom{n-2}{b-2}\right)t^b\\
&-\binom n2\left(\binom n2-1\right)t^4.
\end{aligned}
\]

For \(n=3\), put \(W_3(t)=1+6t+15t^2+20t^3+12t^4\). Then the full **skew-zero-forcing polynomial**, with exponent recording the number of initially blue vertices, is

\[
\boxed{\mathcal Z^-(H_n;z)=z^{2n}W_n(z^{-1})\qquad(n\ge3).}
\]

The minimum skew-zero-forcing numbers, and the exact number of minimum sets, are

\[
Z^-(H_n)=\begin{cases}2,&n=3,\\n,&n\ge4,\end{cases}
\qquad
\#\{\text{minimum sets}\}=\begin{cases}
12,&n=3,\\56,&n=4,\\2n^3-3n^2+n+2,&n\ge5.
\end{cases}
\]

The largest size of a failed initial blue set is \(F^-(H_n)=2n-4\). Thus the skew zero-forcing span, when defined as the number of cardinalities admitting both successful and failed initial sets, is \(\lambda^-(H_3)=1\) and \(\lambda^-(H_n)=n-3\) for \(n\ge4\). The count of inclusion-minimal skew forts is

\[
\binom n2+\mathbf1_{\{n\ge4\}}2n
+\mathbf1_{\{n\ge5\}}
\left(\binom n3\binom{n-3}{3}+n\binom{n-1}{2}\binom{n-3}{2}\right).
\]

## Assumptions and scope

All graphs are finite, simple, and labeled as above. In skew zero forcing, **every** vertex (whether initially blue or white) with exactly one white neighbor may turn that neighbor blue. A set \(S\) of initially blue vertices succeeds if some finite legal forcing sequence makes all vertices blue; its complement \(W\) is the initial white set. The polynomials count labeled vertex subsets, not isomorphism classes; the variable \(t\) counts white vertices and \(z\) counts blue vertices. The formulas hold for every integer \(n\ge3\) without assumptions about simultaneous versus sequential choices: success is equivalent for these choices because turning a white vertex blue cannot create additional white neighbors.

## Proof

**1. Local forcing test.** For an arbitrary remaining white set \(F\), write \(A=\{i:a_i\in F\}\) and \(B=\{i:b_i\in F\}\), with cardinalities \(a,b\). Directly from the two cliques and matching, for every \(i\in[n]\),

\[
|N(a_i)\cap F|=a-\mathbf1_{\{i\in A\}}+\mathbf1_{\{i\in B\}},
\quad
|N(b_i)\cap F|=b-\mathbf1_{\{i\in B\}}+\mathbf1_{\{i\in A\}}.
\tag{1}
\]

The set \(F\) is a skew fort exactly when both expressions avoid the value one for every index. If \(a=0<b\), the first expression equals one at any \(i\in B\); similarly \(b=0<a\). Hence every nonempty skew fort meets both layers.

If \(a=1\) and \(A=\{i\}\), the expression in the first layer is one precisely when either \(i\in B\) or some \(j\ne i\) lies outside \(B\). Thus a fort with \(a=1\) requires \(B=[n]\setminus\{i\}\). The second expression then avoids one precisely when \(n-1\ge3\), which is \(n\ge4\). This gives the second family and its layer-swapped counterpart. If \(a=2\), the first expression is one precisely for indices in \(A\setminus B\). Thus it avoids one if and only if \(A\subseteq B\). For \(a\ge3\), its value is at least two, with no further restriction; symmetric statements hold for the second layer.

Consequently every skew fort not of the singleton-layer type has either \(a=b=2\) and \(A=B\); \(a=2\), \(b\ge3\), \(A\subseteq B\) (or swapped); or \(a,b\ge3\) with no restriction. In the \(a=2\) case, the vertices from the two columns indexed by \(A\) form a proper skew subfort unless \(b=2\). In the \(a,b\ge3\) case, if \(|A\cap B|\ge2\), the two common columns give a proper four-vertex subfort. Otherwise choose three indices in \(A\) and three in \(B\): because their intersection has size at most one, these six vertices are a skew fort, so the original fort is minimal only when \(a=b=3\). Conversely, those \(3+3\) forts with intersection at most one contain no two-column fort and no singleton-layer fort, and no smaller fort of \(3+3\) type. The two other stated families are also minimal for the same reason. This proves the complete list, including the small-order exclusions.

**2. Obstruction duality.** A forcing process that stops with at least one white vertex has a nonempty remaining set \(F\) for which no vertex has exactly one white neighbor, hence a skew fort. Conversely, suppose the initial white set \(W\) contains a skew fort \(F\). If any sequence of forces attempted to turn an element of \(F\) blue for the first time, every vertex adjacent to it would have at least one *additional* still-white neighbor in \(F\), contradicting legality. Therefore a blue set succeeds precisely when its white complement contains no skew fort, equivalently when it contains none of the inclusion-minimal forts classified in step 1.

**3. Complete classification of successful white sets.** The obstruction list is equivalent, for \(n\ge4\), to three mutually organized cases: (i) \(a=0\) or \(b=0\); (ii) one of \(a,b\) is one, while the other lies in \(\{1,\ldots,n-2\}\), or the other equals \(n-1\) and the intersection equals one; (iii) both side sizes lie between two and \(n-2\), at least one size equals two, and the intersection is at most one. To see exhaustiveness: both sizes at least three contain a \(3+3\) fort (if overlap at most one) or a two-column fort (if overlap at least two); a size-two side forbids all matched pairs, forcing intersection at most one; a size-one side forbids precisely the disjoint \((1,n-1)\) fort and all supersets of it. The separate condition for \(n=3\) is obtained directly from step 1: one must avoid all matched two-column sets, allowing all white sets of sizes at most three and exactly twelve four-vertex white sets.

**4. Enumeration.** White sets with an empty side contribute \(2(1+t)^n-1\). For the size-one side, choosing which layer has size one and then its lone index contributes

\[
2nt\sum_{b=1}^{n-2}\binom nb t^b;
\]

the symmetric count duplicates all \(n^2\) possibilities with \(a=b=1\), hence the subtraction \(n^2t^2\). The two orientations of \((a,b)=(1,n-1)\) with intersection one contribute \(2n(n-1)t^n\). For the size-two side and opposite size \(b\in\{2,\dots,n-2\}\), choose its index set in \(\binom n2\) ways and the other index set avoiding full containment of this pair in \(\binom nb-\binom{n-2}{b-2}\) ways. Summing the two orientations duplicates exactly \(\binom n2(\binom n2-1)\) sets with \(a=b=2\), requiring the final subtraction at degree four. The stated formula for \(W_n\) follows, and complementing white sets gives \(\mathcal Z^-(H_n;z)=z^{2n}W_n(z^{-1})\).

**5. Extremal coefficients and forts.** For \(n\ge5\), the maximum possible number of white vertices in a successful configuration is \(n\); its coefficient is

\[
2+2n(n-1)+2\binom n2
\left(\binom n2-\binom{n-2}{2}\right)
=2n^3-3n^2+n+2.
\]

For \(n=4\), the size-two symmetric overcount contributes a further subtraction, giving \(2+24+60-30=56\); for \(n=3\), the exceptional polynomial has top exponent four with coefficient twelve. All skew forts have cardinality at least four, and four-vertex matched-pair forts exist, so the largest failed blue set has cardinality \(2n-4\). The span formula follows from monotonicity of successful blue sets and failed blue sets and the already known relation \(\lambda^-=F^--Z^-+1\) (or directly by checking the integer interval). Finally, the \(3+3\) forts have overlap zero in \(\binom n3\binom{n-3}{3}\) ways and overlap one in \(n\binom{n-1}{2}\binom{n-3}{2}\) ways, yielding the fort count.

## Verification

The standalone program `verification/verify_skew_prism.py` uses only the Python standard library. Run it with `python3 verification/verify_skew_prism.py` after extracting the files from this package. It constructs the actual adjacency lists, simulates the defining skew forcing rule with bit masks, independently identifies all stalled white sets and their inclusion-minimal members, and compares the observed complete cardinality distribution to the formula for **every** white subset at orders \(3\le n\le8\). It also checks the obstruction equivalence and minimum-set counts. A direct run terminated with `VERIFY_OK subset_rule_and_obstruction_checks=174720`. These exhaustive finite checks test implementation and small boundaries; the all-order assertion is proved by the preceding combinatorial argument.

## Relationship to prior work

Curl, Geneson, and Hogben introduced skew throttling and studied skew forcing in their 2019 preprint; their explicit graph families concern paths, cycles, and spiders, not the complete prism all-subsets problem. Jacob subsequently defined the skew zero-forcing polynomial and the skew span, but the accessible article does not give this complete-prism enumeration. Johnson, Vick, and Narayan characterize graphs with failed skew forcing number one, rather than the present unbounded parameter. Cooper and Fickes develop general skew-forcing closure and nullvector relationships for trees and hypergraphs, without the present family-specific fort classification. Abiad and collaborators investigate skew forcing for tensor products, joins, and selected Cartesian products in a cospectrality setting, rather than the exact polynomial on \(K_n\square K_2\).

The distinction from **ordinary** zero forcing is essential: ordinary forcing requires the acting vertex to be blue, while skew forcing permits white vertices to act. Thus ordinary forcing polynomials and their one-leak variants, do not imply this skew enumeration. The minimally stalled-white-set characterization supplies more than the previously considered scalar skew forcing number.

## Limitations

This is a mathematical proof supported by independent finite computation, **not** an independently audited or externally certified result. The checks do not prove the infinite theorem by exhaustion. Literature novelty is assessed against the inspected sources and available indexed records; unindexed articles or equivalent formulations may exist, so publication priority is not guaranteed. The smallest graph \(n=2\) is excluded: it is a cycle with different boundary behavior. The formula concerns labeled vertex subsets, not temporal propagation-time distributions or skew-throttling numbers.

## References

- E. Curl, J. Geneson, and L. Hogben, *Skew throttling*, arXiv:1909.07235v1, publicly posted September 16, 2019, https://arxiv.org/abs/1909.07235.
- B. Jacob, *The zero forcing span of a graph*, arXiv:2309.06234, publicly posted September 12, 2023, https://arxiv.org/abs/2309.06234.
- A. Johnson, A. E. Vick, and D. A. Narayan, *Characterization of Graphs With Failed Skew Zero Forcing Number of 1*, arXiv:2209.09379v1, September 19, 2022, https://arxiv.org/abs/2209.09379.
- R. Cooper and N. Fickes, *Zero loci of nullvectors and skew zero forcing in graphs and hypergraphs*, arXiv:2303.17419, publicly posted March 30, 2023, https://arxiv.org/abs/2303.17419.
- A. Abiad, B. Brimkov, J. Breen, T. R. Cameron, H. Gupta, and R. R. Villagrán, *Constructions of cospectral graphs with different zero forcing numbers*, Electronic Journal of Linear Algebra 38 (2022), 280–294, DOI: 10.13001/ela.2022.6737.
