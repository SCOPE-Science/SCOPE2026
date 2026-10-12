# Exact two-variable counting depth of finite paths

## Finding
Let \(P_n\) be the undirected path on \(n\) vertices, and let \(D^2_{\#}(G)\) denote the minimum quantifier depth of a first-order sentence with counting quantifiers that uses at most two variables and defines \(G\) up to isomorphism. Then
\[
D^2_{\#}(P_1)=1,\qquad D^2_{\#}(P_2)=2,
\]
and, for every \(n\ge 3\),
\[
D^2_{\#}(P_n)=\left\lfloor\frac{n+1}{2}\right\rfloor.
\]

More precisely, among nonisomorphic graphs of order \(n\) that survive the first color-refinement round against \(P_n\), every graph has the form
\[
P_m\;\dot\cup\;C_{c_1}\;\dot\cup\cdots\dot\cup\;C_{c_t},
\qquad m\ge2,\quad c_i\ge3,
\]
with \(m+\sum_i c_i=n\). Such a rival is first separated from \(P_n\) in color-refinement round
\[
\left\lfloor\frac m2\right\rfloor+1.
\]
Consequently the latest possible first separation is \(\lfloor(n-1)/2\rfloor\), attained in particular by \(P_{n-3}\dot\cup C_3\), and the exact logical depth is one larger.

## Assumptions and scope
Graphs are finite, simple, undirected, and uncolored. Counting quantifiers \(\exists^{\ge q}\) have quantifier depth one, independently of \(q\). Color refinement starts from the uniform vertex color; round one therefore records vertex degrees. The logical parameter is the two-variable counting depth used in the standard finite-model-theory literature.

## Proof
The standard equivalence between one-dimensional Weisfeiler--Leman (color refinement) and two-variable counting logic gives the exact bridge needed here. In the notation of Pikhurko--Verbitsky, Theorem 4.4 with \(k=1\) says that if \(R(G)\) is the least number of color-refinement rounds that correctly distinguishes \(G\) from every nonisomorphic graph, then
\[
D^2_{\#}(G)=R(G)+1.
\]
For paths, two variables with counting suffice, so there is no width obstruction.

Different graph orders are already separated by the multiplicity of the uniform round-zero color. Hence it remains to compare \(P_n\) with graphs \(H\) of the same order. For \(n\ge3\), the degree multiset of \(P_n\) is two vertices of degree one and \(n-2\) vertices of degree two. If \(H\) survives round one, it has exactly this degree multiset. Every finite graph whose degrees all lie in \(\{1,2\}\), with exactly two degree-one vertices, consists of exactly one path component and any number of cycle components. Thus every surviving nonisomorphic rival is
\[
H=P_m\dot\cup C_{c_1}\dot\cup\cdots\dot\cup C_{c_t}
\]
with \(m\ge2\), all \(c_i\ge3\), and \(m<n\). Conversely, each such graph has the same degree multiset as \(P_n\).

Fix one such rival and write \(s=\lfloor m/2\rfloor\). For every refinement round \(r\le s\), the endpoint information in a path has propagated exactly \(r\) layers inward. There are two vertices in each of the \(r\) boundary layers, and every remaining vertex has the common interior color. All cycle vertices keep that same interior color forever because every cycle is 2-regular and starts monochromatic. Therefore, through round \(s\), \(P_n\) and \(H\) have identical color multiplicities: the shorter path contributes the same two copies of every boundary-layer color, while its missing interior vertices are replaced exactly by the cycle vertices.

At round \(s+1\), the two wave fronts from the endpoints meet inside \(P_m\). If \(m=2s\), the two central vertices now see one another where the corresponding boundary vertices of the longer path see an interior vertex. If \(m=2s+1\), the unique center now sees two already exposed boundary colors, unlike an interior vertex of the longer path or any cycle vertex. Thus the color multisets first differ in round
\[
\rho(m)=s+1=\left\lfloor\frac m2\right\rfloor+1.
\]

A nonisomorphic same-order rival must contain at least one cycle, so \(m\le n-3\). Since \(\rho(m)\) is nondecreasing in \(m\), the latest first distinction is
\[
R(P_n)=\left\lfloor\frac{n-3}{2}\right\rfloor+1
      =\left\lfloor\frac{n-1}{2}\right\rfloor
\]
for \(n\ge5\), and the bound is attained by \(P_{n-3}\dot\cup C_3\). For \(n=3,4\), no nonisomorphic same-order graph has the path degree multiset, so \(R(P_n)=1\), which equals \(\lfloor(n-1)/2\rfloor\). For \(n=2\), one refinement round distinguishes the edge from the edgeless two-vertex graph, so \(R(P_2)=1\); for \(n=1\), round zero already distinguishes \(P_1\) from every graph of a different order, so \(R(P_1)=0\). Applying \(D^2_{\#}=R+1\) proves the formula.

## Verification
A standalone verifier independently implements joint color refinement from the uniform initial coloring. It enumerates every decomposition of the form \(P_m\dot\cup C_{c_1}\dot\cup\cdots\) for every \(5\le n\le30\), checks that the first distinguishing round is exactly \(\lfloor m/2\rfloor+1\), and checks that the maximum over all rivals is \(\lfloor(n-1)/2\rfloor\). It covers 6,699 rival decompositions and returns:

`VERIFY_OK rival_decompositions=6699 n_range=5..30 max_cases=26 formula=D2#(P_n)=1,2,2,2 then floor((n+1)/2)`

The computation is supplementary; the proof above is uniform in \(n\).

## Relationship to prior work
Pikhurko and Verbitsky explicitly recorded only
\[
D^2_{\#}(P_n)=n/2-O(1),
\]
and pointed to \(P_{n-3}\dot\cup C_3\) as a lower-bound witness for color refinement. Their Theorem 4.4 supplies the exact color-refinement/counting-logic correspondence used above. Krebs and Verbitsky later again described the path as giving the easy linear lower bound \(D(P_n)\ge n/2-O(1)\) while developing nearly linear worst-case lower bounds for general graphs. The present result removes the unspecified additive constant for the natural path benchmark and classifies all same-order competitors that can delay color refinement after the degree round.

Targeted searches of published-finding corpus and the indexed literature located the asymptotic path statement and later work on long refinement, but no indexed source stating the exact formula above. A 2015 master's thesis on WL iteration numbers is cited by later literature but was not available in the inspected indexed text; an unindexed or folklore occurrence of this short exact argument remains the principal priority risk.

## Limitations
The theorem concerns undirected paths and two-variable counting logic only. It does not determine exact depths for arbitrary trees, for paths without counting quantifiers, or for higher-dimensional WL. The originality assessment is based on targeted indexed searches rather than a proof of absence from all theses, lecture notes, or folklore.

## References
1. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865 (first posted 25 March 2010); Contemporary Mathematics 558 (2011), 129--180, DOI: 10.1090/conm/558/11050. In particular, Theorem 4.4 gives the WL/depth bridge and the discussion after Theorem 5.2 records \(D^2_{\#}(P_n)=n/2-O(1)\) with witness \(P_{n-3}\dot\cup C_3\).
2. A. Krebs and O. Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175 (first posted 11 July 2014); LICS 2015, DOI: 10.1109/LICS.2015.69.
3. S. Kiefer and B. D. McKay, *The Iteration Number of Colour Refinement*, ICALP 2020, DOI: 10.4230/LIPIcs.ICALP.2020.73. This later work treats extremal stabilization time and cites the 2015 thesis of M. Gödicke; its indexed text does not state the path formula above.
4. M. Grohe, M. Lichter, and D. Neuen, *The Iteration Number of the Weisfeiler-Leman Algorithm*, ACM Transactions on Computational Logic 26(1) (2025), Article 6, DOI: 10.1145/3708891. Its indexed full text describes the general iteration/depth correspondence; searches within the paper for “path”, “paths”, and “P_n” returned no occurrence.
