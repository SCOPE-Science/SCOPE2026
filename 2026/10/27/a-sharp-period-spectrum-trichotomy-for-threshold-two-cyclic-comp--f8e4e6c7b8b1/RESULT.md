# A sharp period-spectrum trichotomy for threshold-two cyclic competition on tripartite graphs

## Finding

On each labelled complete tripartite simple graph \(K_{a,b,c}\), \(a,b,c\ge1\), run the parallel three-colour cyclic cellular automaton with contact threshold two. Write \(F\) for its update. Then
\[
F^{21}=F^9,
\]
and the bound nine on the first entrance into a periodic orbit is sharp. Every primitive period belongs to \(\{1,3,4,6,12\}\); primitive period two never occurs.

For \(n\ge1\), define
\[
 B(n)=\begin{cases}2^n-2n-2,&n\ge4,\\0,&n<4,\end{cases}
 \qquad
 J(n)=\begin{cases}1,&n=1,\\2,&n=2\text{ or }3,\\0,&n\ge4.\end{cases}
\]
The exact numbers \(R_p(a,b,c)\) of *labelled configurations* of primitive period \(p\) for the three exceptional periods are
\[
\begin{aligned}
 R_4(a,b,c)&=24\bigl(\mathbf1_{a=b=2}B(c)+\mathbf1_{a=c=2}B(b)+\mathbf1_{b=c=2}B(a)\bigr),\\
 R_6(a,b,c)&=48\mathbf1_{a=b=c=2},\\
 R_{12}(a,b,c)&=18\bigl(J(a)B(b)B(c)+J(b)B(a)B(c)+J(c)B(a)B(b)\bigr).
\end{aligned}
\]
Consequently, primitive four-cycles occur precisely on the part-size permutations of \((2,2,n)\) with \(n\ge4\); primitive six-cycles precisely on \(K_{2,2,2}\); and primitive twelve-cycles precisely on the part-size permutations of \((s,m,n)\) with \(1\le s\le3\) and \(m,n\ge4\). These three regimes are mutually disjoint. In particular, \(K_{2,2,2}\) has eight primitive six-cycles and no primitive four- or twelve-cycles. The formulas count states, so divide by their respective periods to obtain numbers of cycles.

There is also an exact fixed finite-state sum for the count of configurations with **each** transient length and eventual period, stated below, which includes periods one and three without an additional case-by-case formula.

## Assumptions and scope

The graph has three nonempty, independent, *labelled* parts \(A,B,C\), of cardinalities \(a,b,c\). Two vertices are adjacent exactly when they belong to different parts; no self-loops occur. Each vertex has a state in \(\mathbb Z/3\mathbb Z\). Simultaneously, a vertex in colour \(j\) changes to \(j+1\pmod3\) if and only if at least two distinct neighbours currently have colour \(j+1\pmod3\); otherwise it retains \(j\). A configuration is recurrent exactly when it is periodic. Its first periodic-entry time is the smallest nonnegative \(t\) for which \(F^t(x)\) belongs to a periodic orbit. All results hold for **every** positive integer triple, with no random-initialisation assumption.

## Proof

**1. Exact capped population factor.** For a configuration \(x\), let \(n_{ij}(x)\) be its number of vertices of colour \(j\) in part \(i\), and put \(s_{ij}=\min(2,n_{ij})\), where \(i,j\in\{0,1,2\}\). Because vertices within one part have identical external neighbourhoods, all vertices initially in one part/colour class make the same update. A class in part \(i\) and colour \(j\) advances precisely when
\[
 \sum_{h\ne i}s_{h,j+1\bmod3}\ge2.
\]
The advanced and retained classes are accumulated in their destination colour classes by truncated addition \(u\oplus v=\min(2,u+v)\). Since truncation respects both the threshold test and nonnegative addition, this yields an **exact** map \(\Phi\) on the \(3^9\) possible capped population signatures. Its \(17{,}576\) signatures with all three parts nonempty form an invariant subset.

**2. Tagged-vertex lift.** The population factor alone does not establish a period or preperiod bound for the labelled configuration: two distinct large colour classes can remain indistinguishable after capping. To remedy this, augment \(s\) by a chosen part \(i\) and an *occupied* colour \(j\). The tagged state \((s,i,j)\) changes to \((\Phi(s),i,j')\), where \(j'\) is determined by the same threshold-two test. This constructs exactly \(109{,}512\) reachable tagged states, without a parameter cutoff. For each tagged state, define \(t\) as its first entry into a cycle and \(p\) as its least eventual period. Every labelled vertex follows one of these tagged orbits exactly, even when its initial class size exceeds two.

For each population signature \(s\), write \(\mathcal T(s)\) for its occupied tags. The full labelled configuration represented by \(s\) has exactly
\[
 \tau(s)=\max_{q\in\mathcal T(s)}t(q),\qquad
 \pi(s)=\operatorname{lcm}_{q\in\mathcal T(s)}p(q).
\]
Indeed, a full state is periodic if and only if its population signature and every individual tagged colour are periodic; conversely their simultaneous return time is the displayed least common multiple. This also proves that the preperiod and least eventual period depend **only** on \(s\), not on actual class sizes greater than two.

**3. Bounded finite exhaustive lemma.** The accompanying human-readable Python certificate enumerates all \(17{,}576\) admissible signatures, constructs the exact tagged transition on all \(109{,}512\) states, and computes the entry times and least periods of its finite functional graph. The result is
\[
 \max_s\tau(s)=9,
 \qquad
 \{\pi(s):s\text{ admissible}\}=\{1,3,4,6,12\}.
\]
The certificate also independently checks \(T^{21}=T^9\) for every tagged state. From the lift it follows for each labelled configuration that \(F^{21}=F^9\). Sharpness has a fully explicit vertex-level witness on \(K_{5,3,2}\): initial part-colour populations \((2,1,2),(0,1,2),(1,1,0)\) give first periodic entry at precisely time nine, as checked independently by direct labelled-vertex updates.

**4. Classification of exceptional recurrent patterns.** Under permutations of the three parts and common rotations of the three colours, the same exact finite certificate finds exactly two canonical recurrent-signature families of physical primitive period four (18 signatures altogether), one of primitive period six (six signatures), and seven of primitive period twelve (126 signatures). The finite checker records the **complete explicit signature templates** as exact tuples and checks equality of the calculated canonical classes with those templates; it does not infer exhaustiveness from randomly sampled configurations. Their part-size forms are, respectively: two size-two parts each split into one vertex of each of two colours, and a third part split into two colour classes each of size at least two; all three size-two parts each split into two singletons; or precisely one small part of size one, two, or three with its occupied colours each represented once, and two large parts each split into two classes of size at least two. The allowed orientations within these forms are precisely the canonical templates checked in the certificate, so the size conditions are necessary **and** sufficient.

For any large part of size \(n\), the number of labelled assignments to two specified nonempty colour classes of sizes at least two is \(B(n)\). In the four-period case there are six allowed capped signature orientations for each choice of the large part; the two small shores contribute \(2!\) assignments each, giving \(6\cdot2\cdot2 B(n)=24B(n)\). In the six-period case there are six allowed signature orientations and \(2^3\) labelled assignments, giving 48. For the twelve-period case, for each specified small shore there are 18 allowed orientations when its size is one or two, and six when its size is three. The small shore contributes one, two, or six labelled assignments respectively; therefore its total coefficient is \(18J(s)\). Multiplying by the two large-shore factors gives the claimed three formulas. These disjoint regimes cannot overlap because their part-size requirements conflict.

**5. Exact transient/period census for all parameters.** For \(u=(u_0,u_1,u_2)\in\{0,1,2\}^3\), let
\[
 W_n(u)=\sum_{\substack{x_0+x_1+x_2=n\\\min(2,x_j)=u_j\ (j=0,1,2)}}\frac{n!}{x_0!x_1!x_2!}.
\]
For every \(t\ge0\) and \(p\ge1\), the exact number of labelled initial configurations with first periodic-entry time \(t\) and eventual primitive period \(p\) is
\[
 D_{t,p}(a,b,c)=\sum_{\substack{s\in\{0,1,2\}^{3\times3}\\\text{each row nonzero}\\\tau(s)=t,\ \pi(s)=p}}W_a(s_{0,*})W_b(s_{1,*})W_c(s_{2,*}).
\]
This is a fixed finite sum with the \(\tau,\pi\) table determined solely by the provided 109,512-state finite construction. It is executable for arbitrary positive part sizes. It is zero for all \(t>9\), all \(p\notin\{1,3,4,6,12\}\), and its sum over \(t,p\) is \(3^{a+b+c}\).

## Verification

Run `python3 verify_tripartite_cca.py` to enumerate the exact capped and tagged functional graphs, check the power identity and canonical signature templates, and evaluate multiple weighted censuses. Run `c++ -std=c++17 -O2 direct_vertex_check.cpp -o direct_vertex_check && ./direct_vertex_check` to exhaustively update the **original labelled vertices**, without using the quotient transition. The second checker covers every initial configuration on \(K_{1,4,4}\), \(K_{2,2,2}\), \(K_{2,2,4}\), \(K_{2,4,4}\), \(K_{3,4,4}\), and \(K_{5,3,2}\), a total of \(322{,}218\) configurations, and corroborates the sharp time-nine witness. The recorded command output is in `verification_output.txt`. Both source files are included, and require only a Python 3 interpreter or a standard C++17 compiler, respectively. These finite checks constitute an exhaustive proof on the exact bounded factor **because** the capping/tagging lemma above covers every graph size; direct small-graph enumeration alone would not prove the theorem.

## Relationship to prior work

The contact-threshold cellular automaton framework is classical (Fisch, Gravner and Griffeath, 1991; Durrett and Griffeath, 1993). Their inspected work analyzes predominantly spatial lattice waves and threshold/range behaviour, rather than an exact complete-tripartite orbit census. Gravner, Lyu and Sivakoff (arXiv:1610.07320) analyze three-colour dynamics on arbitrary graphs under the **one-neighbour** contact rule, so their general conclusions do not directly imply the threshold-two classification. Complete multipartite threshold-one cyclic competition and threshold-two complete-bipartite competition have different graph/rule hypotheses; in particular their primitive-period spectra do not force the isolated six-period regime found here. Likewise, the threshold-two Greenberg–Hastings rule advances refractory states automatically and is not dynamically identical to the cyclic competition rule studied here. No comprehensive historical uniqueness claim is made.

## Limitations

The theorem covers synchronous deterministic three-colour **threshold-two CCA** only, on complete tripartite graphs with three nonempty parts. It does not assert the same classification on four or more parts, other thresholds, asynchronous variants, or lattice graphs. The finite signature enumeration is part of the proof and must be rerun or audited to independently validate the computational exhaustive lemma. Originality is assessed relative to specified accessible material and may be affected by unindexed equivalent prior work. No independent external audit has been performed.

## References

1. R. Fisch, J. Gravner and D. Griffeath, *Threshold-range scaling of excitable cellular automata*, Statistics and Computing 1 (1991), 23–39. Freely available author PDF: https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf; also arXiv:patt-sol/9304001, public posting 1993-04-02.
2. R. Durrett and D. Griffeath, *Asymptotic behavior of excitable cellular automata*, Experimental Mathematics 2 (1993), 183–208. arXiv:patt-sol/9303002, public posting 1993-03-22; author PDF: https://sites.math.duke.edu/~rtd/reprints/paper79.pdf.
3. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, initial posting 2016-10-24. This later paper is cited for related threshold-one work only.
