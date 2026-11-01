# An isolated period-ten resonance in three-color cyclic dynamics on crown graphs

## Finding
Let \(\operatorname{Cr}_n=K_{n,n}\setminus M\) be the crown graph with vertex sets \(\{L_1,\ldots,L_n\}\) and \(\{R_1,\ldots,R_n\}\), and with edge \(L_iR_j\) exactly when \(i\ne j\). Let \(F\) be synchronous three-color cyclic cellular automaton: a vertex of color \(c\in\mathbb Z/3\mathbb Z\) advances to \(c+1\) precisely when at least one neighbor has color \(c+1\); otherwise it retains \(c\).

For every \(n\ge1\) and every initial coloring, the first entry into a periodic orbit is no later than update 4. The complete eventual least-period spectrum and the **sharp** maximum first-entry time are:

| Shore size | Eventual least periods | Sharp maximum initial preperiod |
|---|---|---:|
| \(n=1\) | \(\{1\}\) | 0 |
| \(n=2\) | \(\{1\}\) | 1 |
| \(n=3\) | \(\{1,3,6\}\) | 3 |
| \(n=4\) | \(\{1,3,4\}\) | 3 |
| \(n=5\) | \(\{1,3,4,10\}\) | 4 |
| \(n\ge6\) | \(\{1,3,4\}\) | 4 |

In particular, **primitive ten-cycles occur only for the single graph size \(n=5\)**, with exactly \(72\) distinct labelled-state ten-cycle orbits. All \(720\) period-ten states are recurrent from time zero: the ten-cycles have no strictly preperiodic initial configurations in their attraction basins. On \(\operatorname{Cr}_3\) there are exactly \(20\) distinct primitive six-cycle orbits.

An explicit ten-cycle starts with the five ordered matched-pair colors \( (0,1),(0,2),(1,0),(1,2),(2,0)\); its successive phases are verified by the accompanying independent vertex-level checker.

## Assumptions and scope
The graph is simple and undirected, with precisely the deleted perfect matching; all shores are labelled, and temporal phase shifts are identified when counting distinct periodic orbits. The three-color update uses the standard *contact* condition, not the Greenberg–Hastings refractory update nor an inhibitory firefly rule. Initial colorings and shore sizes are arbitrary. First periodic-entry time means the least \(t\ge0\) for which \(F^t(x)\) is on a recurrent orbit. A primitive period is the least positive \(p\) with \(F^p(x)=x\) on that orbit. The theorem does not classify the multiplicity of all periods other than six and ten.

## Proof
**Step 1: exact paired-type reduction.** For each \(a,b\in\mathbb Z/3\mathbb Z\), let \(c_{ab}\) be the number of indices \(i\) with \((X(L_i),X(R_i))=(a,b)\). Define the left and right marginal counts \(A_a=\sum_b c_{ab}\) and \(B_b=\sum_a c_{ab}\). Every index of type \((a,b)\) changes identically, and the new pair is
\[
(a',b')=\left(a+\mathbf1\{B_{a+1}>\mathbf1\{b=a+1\}\},\ b+\mathbf1\{A_{b+1}>\mathbf1\{a=b+1\}\}\right)\pmod3.
\]
The inner indicator excludes the deleted matched vertex. A threshold of zero or one after that exclusion can be determined from \(\sigma_{ab}=\min(2,c_{ab})\) alone. The nine-entry vector \(\sigma\in\{0,1,2\}^9\) therefore determines both the image of **each currently occupied pair type** and the next saturated profile. If several types merge, the new count of an image type is the sum of their old counts, truncated at two; and \(\min(2,\sum_i c_i)=\min(2,\sum_i\min(2,c_i))\). Thus the nine-trit map is an exact deterministic factor for arbitrary (even unbounded) shore sizes.

**Step 2: recover microscopic temporal periods.** A saturated signature by itself can return before its labelled vertices do. To avoid such a false identification, attach to each starting signature the ordered list of its initially present pair types, and iteratively transport every representative through the just-computed type map. Each original labelled matched pair follows the representative of its initial type for all time. Therefore the first repeated state in the joint record (saturated signature, transported representative-type list) gives exactly the microscopic first periodic-entry time and least period, not merely a support-period estimate. This is a rigorous finite quotient of the entire family of colourings, because the represented pair types can never split.

**Step 3: exhaustive bounded classification.** The accompanying complete standalone verifier visits **every one of the \(3^9=19{,}683\) possible nine-trit signatures**, including signatures that do not represent a fixed shore size. For each one it builds the exact next-signature/type maps from the displayed formulas, iterates the joint record until repetition, and counts classes. The exhaustive class counts by eventual period are
\[
\begin{array}{c|rrrrr}
\text{period}&1&3&4&6&10\\\hline
\text{number of signatures}&397&15711&3519&50&6
\end{array}
\]
and by first periodic-entry time are
\[
\begin{array}{c|rrrrr}
\text{time}&0&1&2&3&4\\\hline
\text{number of signatures}&13317&5016&1146&174&30.
\end{array}
\]
This finite exhaustion is the nonstandard computational lemma used here; it is supplied as transparent executable source and independently checks each claimed count. No sample-to-infinity inference is made.

**Step 4: realize the spectra for every shore size.** All fifty period-six signatures have entries only zero or one and exactly three ones. Consequently their exact shore size is \(n=3\), and conversely twenty of these signatures are immediately periodic. All six period-ten signatures have entries only zero or one and exactly five ones. Consequently their exact shore size is \(n=5\), and each is immediately periodic. The checker also explicitly finds period-three and period-four signatures with at least one entry equal to two and at most four total units, and a preperiod-four signature with an entry equal to two and at most five total units. Adding arbitrary extra copies to any type already of multiplicity at least two does not change the saturated signature or the joint orbit classification. This proves the existence of periods three and four for all \(n\ge4\), sharp four-step entry for all \(n\ge5\), and absence of exceptional periods otherwise. The finite table also gives the \(n=1,2,3,4\) boundary cases and their sharp preperiods; the independent direct microscopic checker re-enumerates every coloring through \(n=6\).

**Step 5: exact exceptional orbit populations.** At \(n=5\), each of the six immediately periodic signatures contains five distinct pair types, each exactly once. Each admits \(5!\) assignments to the labelled indices. These sets are disjoint and give \(6\cdot5!=720\) distinct recurrent colorings of primitive period ten. Each orbit contains ten such states, hence \(720/10=72\) distinct orbits. Since all period-ten signatures have initial preperiod zero, no nonperiodic state can enter them. Similarly, precisely twenty of the period-six signatures are immediately periodic for \(n=3\); each has \(3!\) labellings. Thus the number of distinct six-cycles equals \(20\cdot3!/6=20\). This completes the classification.

## Verification
Run `python3 verify_crown_cca3.py` using Python's standard library. It exhaustively classifies the finite factor and directly computes the global vertex-neighbor update for all \(3^{2n}\) labelled configurations for \(1\le n\le6\), a total of \(597{,}870\) microscopic configurations. It compares exact first preperiods and primitive periods for each configuration. At \(n=5\), its period-ten basin count is \(720\), matching the recurrent-state census exactly. A successful run ends `CROWN_CCA3_VERIFY_OK`; `verification_output.txt` gives a recorded execution transcript. The proof of the infinite family is the finite exact-quotient argument, not the six tested shore sizes alone.

## Relationship to prior work
Gravner, Lyu and Sivakoff (arXiv:1610.07320, first made public 2016-10-24; later *Annals of Applied Probability*, 2018) analyze the **same three-color contact rule on arbitrary graphs**. Their Theorem 3 characterizes fixation and asymptotic excitation activity via cycles and their associated edge-color 1-form. It applies to crown graphs and gives broad qualitative/quantitative constraints, but its theorem does not state the present sharp finite-time bound, the size-five-only period-ten spectrum, or the 72-orbit enumeration. The present finite census is consistent with, but not an immediate restatement of, that activity characterization. Prior complete-bipartite and complete-multipartite three-color censuses apply to graphs with all cross edges present, not to the crown graph with one excluded neighbor per vertex. The excluded matched neighbor is exactly why individual pair types, rather than shore color support alone, are needed.

## Limitations
The 19,683-case exhaustion is a finite computational certificate rather than a conventional handwritten case partition; independently checking the short program and its execution is necessary for this proof presentation. Unindexed equivalent historical treatments of cyclic dynamics on crown graphs cannot be ruled out absolutely. Only orbit numbers for exceptional periods six and ten are supplied, not closed formulas for every orbit or basin size at arbitrary \(n\). No independent external audit has been performed.

## References
1. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320 (first posted 2016-10-24), subsequently *Annals of Applied Probability* **28** (2018), 3324–3357. https://arxiv.org/abs/1610.07320 ; author-hosted full text: https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf .
2. `verify_crown_cca3.py` and `verification_output.txt`, self-contained finite-state verification artifacts accompanying this result.
