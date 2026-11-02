# A single period-five defect makes optimal independent sets of generalized Petersen graphs form one cycle

## Finding

Let \(G_n=GP(n,2)\), for \(n\ge5\), have outer vertices \(a_i\), inner vertices \(b_i\), and edges \(a_i a_{i+1}\), \(a_i b_i\), and \(b_i b_{i+2}\), with indices modulo \(n\). The **optimal token-jumping graph** \(\mathcal J_n\) has the maximum-cardinality independent subsets of \(G_n\) as vertices, with an edge when one selected graph vertex is removed and one different graph vertex is inserted, retaining independence.

The following complete exchange-graph decompositions hold for every integer \(k\ge1\):
\[
\mathcal J_{5k}\cong5K_1,\qquad
\mathcal J_{5k+4}\cong C_{3(5k+4)}.
\]
Moreover, every exchange appearing in these two families can be performed by sliding a token along an edge of the original graph. Hence the token-sliding and token-jumping graphs of maximum independent sets coincide in both families.

In particular, for \(n=5k+4\), every optimal set has exactly two immediate neighbors, all \(3n\) optimal sets lie in one cycle, and the diameter is \(\lfloor3n/2\rfloor\). For \(n=5k\), exactly five optimum configurations exist and every one is frozen even under arbitrary one-token jumps. These values of the independence number and the maximum-set counts are background consequences of the classification; the contribution asserted here is their **exact exchange geometry**.

## Assumptions and scope

An independent set contains no adjacent pair. We encode an independent set by a cyclic word over \(\{0,A,B\}\): column \(i\) has symbol \(A\) if \(a_i\) is selected, \(B\) if \(b_i\) is selected, and \(0\) if neither is selected. A column cannot have two selected vertices because of its spoke edge. The word is legal exactly when adjacent columns never both contain \(A\) and columns at cyclic distance two never both contain \(B\).

An edge of the token-jumping graph is an unordered pair of independent sets \(S,T\) satisfying \(|S|=|T|=\alpha(G_n)\) and \(|S\setminus T|=|T\setminus S|=1\). In the token-sliding graph, the removed and inserted vertices must additionally be adjacent in \(G_n\). We make no connectivity claim for lengths congruent to one, two, or three modulo five, or for nonmaximum independent sets.

## Proof

**1. The five-column obstruction.** A run of consecutive nonzero symbols has length at most four. Indeed, the legal three-letter nonzero words are precisely \(ABA\), \(ABB\), and \(BBA\). The only legal four-letter extension is \(ABBA\); neither \(ABBAA\) nor \(ABBAB\) is legal, so no run has five nonzero symbols. The same argument applies to a cyclic window of five columns. Summing over all cyclic five-column windows yields \(5|S|\le4n\) for every independent set \(S\).

**2. Exact optima at multiples of five.** If \(n=5k\), the word \((0ABBA)^k\) is legal and contains \(4k\) vertices, attaining the bound. Equality forces exactly \(k\) zero columns and \(k\) runs of four selected columns separated by single zeros. Each run must be \(ABBA\). Hence all optimal words are exactly the five cyclic translates of \((0ABBA)^k\).

**3. Exact optima one below a multiple of five.** If \(n=5k+4\), the word \(0ABA(0ABBA)^k\) is legal and contains \(4k+3=\lfloor4n/5\rfloor\) selected vertices. An optimal word has exactly \(k+1\) zeros. Splitting the cyclic word at these zeros gives \(k+1\) nonzero runs of lengths at most four. Their combined length is \(4k+3=4(k+1)-1\), so precisely one run has length three and the other \(k\) runs have length four. The three possible length-three runs are \(ABA\), \(ABB\), and \(BBA\), and each length-four run is forced to be \(ABBA\). Because \(k\ge1\), the short run has a length-four run across each zero boundary, so each of the three choices is globally legal. There is a unique short run; locating its preceding zero identifies an unambiguous index \(i\in\mathbb Z_n\).

Define \(X_i,Y_i,Z_i\), respectively, as the words obtained by starting at column \(i\) with
\[
X_i:\ 0ABA(0ABBA)^k,\quad
Y_i:\ 0ABB(0ABBA)^k,\quad
Z_i:\ 0BBA(0ABBA)^k.
\]
Their start positions are cyclically shifted, so there are exactly \(3n\) optima, all distinct.

**4. Every one-token exchange.** An exchange either preserves the set of zero columns or moves one zero to the column formerly occupied by the removed token.

If the zero columns do not change, the exchange flips \(A\leftrightarrow B\) at one column. Within a length-four \(ABBA\) run any such flip violates either the adjacent-\(A\) or distance-two-\(B\) rule. Within the short run, the only possible flips are \(ABA\leftrightarrow ABB\) at its third position and \(ABA\leftrightarrow BBA\) at its first position. These are exactly \(X_iY_i\) and \(X_iZ_i\).

If the zero columns change, remove an old zero separating neighboring nonzero runs of lengths \(p,q\). Filling this zero creates one uninterrupted run of \(p+q+1\) symbols, which must be split by the newly emptied column into runs of length at most four. When \(p=q=4\), the only split into admissible run lengths is \(4+4\), requiring the new zero to occupy exactly the old zero position; thus no genuine zero movement is possible there. The unique short run allows only \((p,q)=(3,4)\) or \((4,3)\); a new zero may then lie only one column to the appropriate side of its former position. Checking the forced \(ABBA\) pattern shows that the only admissible such move is \(Y_i\leftrightarrow Z_{i+5}\). These are all the exchanges, with indices taken modulo \(n\):
\[
X_i\sim Y_i,\qquad X_i\sim Z_i,\qquad Y_i\sim Z_{i+5}.
\]
The first two are slides along spoke edges; the third slides an outer vertex between consecutive columns. Thus no unrestricted token jump adds any further edge beyond token sliding.

For \(n=5k\), changing one zero position would replace two adjacent length-four runs by two length-four runs; their unique split position is unchanged. Preserving zeros permits no letter flip in \(ABBA\). Therefore all five optimum configurations are isolated.

**5. Connectivity and diameter.** In the \(n=5k+4\) family the displayed exchange relations make every vertex degree two. Following \(Y_i\sim Z_{i+5}\sim X_{i+5}\sim Y_{i+5}\) advances the index by five. Because \(\gcd(n,5)=1\), all \(n\) indices and all three types lie in one component. This two-regular connected simple graph is \(C_{3n}\), whose diameter is \(\lfloor3n/2\rfloor\).

## Verification

The accompanying standalone standard-library scripts are `verify_gp_maximum.py` and `verify_gp_templates.py`.

`verify_gp_maximum.py` independently enumerates every optimal cyclic word by a finite-state dynamic program (not by assuming the claimed three families), then constructs **all** one-for-one exchanges. It compares the result to the formulas for lengths \(5,9,10,14,15,19,20,24\) and verifies connectivity and degree two where applicable. It also checks that all enumerated words are independent.

`verify_gp_templates.py` uses a different representation: the actual \(2n\)-vertex graph and integer bitsets. It exhaustively enumerates combinations of maximum cardinality at lengths \(5,9,10\), verifies the complete templates and every legal exchange, and independently checks all indicated residue-class lengths from \(5\) through \(99\). Its checks are finite corroboration; the proof above is the justification for **all** \(k\ge1\).

To reproduce: run `python3 verify_gp_maximum.py` and `python3 verify_gp_templates.py` from the directory containing these files. Both use only the Python standard library.

## Relationship to prior work

The independence number \(\alpha(G_n)=\lfloor4n/5\rfloor\) is established in the earlier minimum-vertex-cover and generalized-Petersen independence-number literature; it is not new. Besharati, Ebrahimi, and Azadi (2010) explicitly report this formula, and Fox, Gera, and Stănică (2012), Theorem 2.5, give another proof. The prior exact cardinality enumeration of inclusion-maximal independent sets also yields the optimal-set counts \(5\) and \(3n\); those counts alone do not specify which optima are adjacent.

The general reconfiguration formalism is classical; Ito and collaborators (2011) analyze the complexity of several reconfiguration problems. The present result instead identifies the **entire fixed-optimum exchange graph** in two infinite residue classes of a named cubic graph family. No broader claim of uniqueness in the literature is made.

## Limitations

The complete theorem concerns \(n\equiv0,4\pmod5\) only. It does not imply a classification at other residues or a generic connectivity theorem for all generalized Petersen graphs. The two independent programs test finite ranges, not the infinite claim. An unavailable full text of Behzad, Hatami, and Mahmoodian's 2009 paper on vertex covers of \(P(n,2)\), and possible alternative reconfiguration terminology, leave residual historical originality risk. No independent scholarly audit has been performed.

## References

1. N. Besharati, J. Ebrahimi B., and A. Azadi, *Independence number of generalized Petersen graphs*, arXiv:1008.2583v1 (first public version 2010-08-16).
2. J. Fox, R. Gera, and P. Stănică, *The Independence Number for the Generalized Petersen Graphs*, Ars Combinatoria **103** (2012), 439–451; publicly available PDF at `https://combinatorialpress.com/article/ars/Volume%20103/volume-103-paper-37.pdf`.
3. B. Behsaz, P. Hatami, and E. S. Mahmoodian, *On minimum vertex cover of generalized Petersen graphs*, arXiv:1008.3208v1 (2010-08-19).
4. T. Ito, E. D. Demaine, N. J. A. Harvey, C. H. Papadimitriou, M. Sideri, R. Uehara, and Y. Uno, *On the Complexity of Reconfiguration Problems*, Theoretical Computer Science **412** (2011), 1054–1065, doi:10.1016/j.tcs.2010.12.005.
5. M. Behzad, P. Hatami, and E. S. Mahmoodian, *Minimum vertex covers in the generalized Petersen graphs \(P(n,2)\)*, Bulletin of the Institute of Combinatorics and its Applications **56** (2009), 98–102 (full text not inspected).
