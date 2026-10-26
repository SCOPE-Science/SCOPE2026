# Scientific review

## Correctness: PASS

Finite indegree/outdegree at most one makes each weak component a directed path or a directed cycle. Stability forces the alternating path choice uniquely and exactly two phase choices on an even cycle, with no choice on odd cycles. Different phases change all vertices of their cycle. In a triple of phases every nonconstant column has exactly one agreeing pair; constant columns can be made nonconstant without decreasing any distance. This proves the exact three-bin formula, and the two-sum dynamic program computes the bin optimum. The finite checker was executed and returned 35 successful direct-enumeration comparisons. Its finite reach does not stand in for the proof.

## Originality: PASS, with residual priority risk

Fichte–Hecher–Mahmood–Wang (2026), Sections 3–4 and Lemma 24, explicitly analyze distances between two extensions and componentwise composition, but do not give simultaneous three-extension max-min diversity or the exact weighted three-bin expression. Matsuoka–Ito (2023) defines general multi-solution max-min weighted Hamming diversity and proves approximation/hardness results; this does not provide the stated exact value for the full cycle-choice product. The weighted-binary coding perspective supplies the general two-thirds distance-sum bound but not the length-sensitive optimum or the stable extension characterization. Indexed research searches and examined published mathematical claims yielded no covering statement. Residual risk: an equivalent full-binary-cube three-point packing formula may appear in older coding or diversity literature under another name; absence from search results does not establish absolute priority.

## Value: PASS

The 2026 argumentation-diversity motivation naturally raises the question of balancing three simultaneously incompatible accepted positions, rather than choosing only a most-separated pair. Degree-one attack graphs are a natural finite structural class with exponentially many stable extensions; the exact optimum is not determined by the number of extensions or total cycle length alone. The formula identifies a genuine three-way scheduling bottleneck, yields a polynomial exact algorithm without listing stable extensions, and characterizes sharp equality and the equal-cycle family. This is a complete exact invariant for the stated class rather than a sample table or arbitrary parameter slice.

## Limits and comparison

The proof does not extend to branching attack graphs, graphs with odd directed cycles, or other semantics. The general max-min diversity literature has some shared concepts and admits a possible equivalent specialization not located by the inspected material.

Self-review: passed. Independent audit: not yet performed.
