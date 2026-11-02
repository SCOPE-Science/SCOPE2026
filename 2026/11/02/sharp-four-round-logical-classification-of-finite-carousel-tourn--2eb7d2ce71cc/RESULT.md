# Sharp four-round logical classification of finite carousel tournaments

## Finding
For each odd integer \(n\ge3\), let \(R_n\) be the tournament on \(\mathbb Z/n\mathbb Z\) in which \(a\to b\) holds precisely when the residue \(b-a\) lies in \(\{1,\ldots,(n-1)/2\}\). Work in first-order logic with equality and the single binary edge relation \(E\), with no circular order, constants, antipodal map, or arithmetic named.

**Theorem.** For all odd \(n,n'\ge3\),
\[
R_n\equiv_4R_{n'}\quad\Longleftrightarrow\quad
\bigl(n=n'<15\bigr)\ \lor\ \bigl(n,n'\ge15\bigr).
\]
There are exactly seven four-round theories in this family, represented by orders \(3,5,7,9,11,13,15\). The sharp largest minimum representative has \(15\) vertices. At rank three, the equivalence classes are the individual orders \(3\) and \(5\), and all odd orders at least \(7\).

There is also a uniform quantitative statement at **every** depth: for every integer \(q\ge1\), all odd \(n,n'\ge\max\{3,2^q-1\}\) satisfy \(R_n\equiv_qR_{n'}\). This general upper bound is not asserted to be optimal for arbitrary \(q\).

## Assumptions and scope
A finite carousel tournament is exactly the directed complete graph above. The binary relation is irreflexive and chooses exactly one orientation of each distinct pair. Quantifier rank counts maximum nesting depth of first-order quantifiers; \(\equiv_q\) is agreement on every sentence of rank at most \(q\), equivalently a win for the Duplicator in a \(q\)-round Ehrenfeucht–Fraïssé game. All quantifiers range over the tournament vertices. Auxiliary circular marks in the proof are **not** symbols of the theorem's language.

## Proof
**1. Antipodal doubled-circle representation.** Fix odd \(n\). On a cyclic array of \(2n\) unit positions, encode tournament vertex \(a\) as the even mark \(2a\), and give it the antipodal odd mark \(2a+n\), modulo \(2n\). Then \(a\to b\) if and only if the even mark of \(b\) occurs strictly clockwise between the even mark of \(a\) and its antipodal odd mark. Indeed, this interval contains exactly the \((n-1)/2\) even marks with positive residue difference at most \((n-1)/2\).

After one or more vertices have been chosen, their labeled even and antipodal odd marks form an antipodally invariant set. The complementary open gaps of the doubled circle occur in distinct pairs interchanged by the half-turn. Each gap has an integer step length \(L\) between its successive endpoint marks, and opposite gaps have the same length. Corresponding endpoint marks have the same even/odd labels under any label-preserving partial correspondence, so corresponding gap lengths have the same parity, even when their lengths differ.

**2. A gap-halving extension lemma.** Define \(T_0=0\) and \(T_{r+1}=2T_r+2\), so \(T_r=2^{r+1}-2\). Suppose two circular marked configurations have the same circular order of labeled even and odd marks, and corresponding gap lengths are either equal and at most \(T_r\), or are both strictly greater than \(T_r\). If a previously unchosen even vertex mark is inserted in either configuration while \(r\ge1\), then an even mark can be inserted in the corresponding gap in the other configuration so that the same invariant holds with \(T_{r-1}\); inserting both antipodal odd marks preserves it simultaneously in the paired opposite gaps.

To prove the lemma, write \(t=T_{r-1}\). Suppose the chosen even mark is \(d\) steps from the left endpoint of a gap of length \(L\). In an exactly matched gap, use the same \(d\). Otherwise \(L,L'>2t+2\). If \(d\le t\), take \(d'=d\); if \(L-d\le t\), take \(d'=L'-(L-d)\). Both choices match one short subgap exactly and leave the other above \(t\). In the remaining case \(d,L-d>t\), choose an integer \(d'\) strictly between \(t\) and \(L'-t\), with parity equal to \(d\). Such an integer exists because \(L'>2t+2\) gives at least two consecutive eligible integers. The parity match makes the chosen target position even because corresponding left endpoints have the same parity. In the second case, parity compatibility uses \(L\equiv L'\pmod2\). Both new subgaps have matching truncated lengths. The antipodal choices split the opposite paired gaps by the same step offsets, so their invariants follow identically. Existing selected vertices are answered by their correspondents and require no gap change.

**3. Uniform upper bound.** In a \(q\)-round game, after the first move the Duplicator answers any first chosen vertex by any vertex. The two circular gap lengths in either structure are exactly \(n\) and \(n\), respectively \(n'\) and \(n'\). For odd \(n,n'\ge2^q-1\), these lengths exceed \(T_{q-1}=2^q-2\), so the lemma supplies a legal answer to every remaining move, lowering the threshold once per round. At the end \(r=0\), the matched order of selected marks and their antipodes determines all directed-edge relations, and repeated choices preserve equality. Hence Duplicator wins. In particular, all odd orders at least \(15\) agree at rank four and all odd orders at least \(7\) agree at rank three.

**4. Exact finite lower boundary.** For a tuple \(\bar a\) in a finite tournament define \(\tau_0(\bar a)\) as its complete atomic diagram, encoding every ordered pair of positions as equality, forward edge, or backward edge. Recursively define
\[
\tau_{r+1}(\bar a)=
\left(\tau_0(\bar a),\ \{\tau_r(\bar a,b):b\in V\}\right).
\]
Induction on \(r\) proves that equality of these signatures for two tuples is equivalent to the Duplicator's winning the remaining \(r\) moves: the two extension sets encode both sides of the game's back-and-forth requirement. The supplied dependency-free exact program constructs every atomic diagram and every set of extensions. For odd orders \(3,5,7,9,11,13,15\), its seven rank-four empty-tuple signatures are pairwise different (all \(21\) pair comparisons). For rank three the signatures for \(3,5,7\) are pairwise different. This is a complete finite exhaustive check, not a sample or probabilistic experiment. The proven upper bound covers all remaining infinitely many odd orders. The theorem and sharpness follow.

## Verification
Run `python3 verify_carousel.py` with Python 3. The verifier constructs the complete nested set-valued signatures exactly, with no hashes used for comparison and no dependencies outside the standard library. Rotational normalization is justified by the tournament automorphisms \(a\mapsto a+c\); an independent unnormalized recursion agrees on all four-round signatures for orders \(3,5,7,9\). Exact comparison separates all \(21\) pairs of small representative orders, confirms the three rank-three classes, and also checks six extra tail orders. The recorded `verification_output.txt` ends with `VERIFY_OK`.

The finite calculations alone do not establish the infinite tail: that conclusion uses the antipodal gap-halving proof in Step 3. The program is an exact exhaustive finite proof component for Step 4.

## Relationship to prior work
Coregliano's *Quasi-Carousel Tournaments* (initially public March 13, 2015) introduces and studies these canonical balanced locally transitive tournaments and their flag-algebra/density convergence. Its inspected introduction, asymptotic proofs, convergence section, and concluding section do not state a finite quantifier-rank partition or an exact seven-class boundary.

Goodall, Nešetřil, and Ossona de Mendez's *Strongly Polynomial Sequences as Interpretations* (dated December 15, 2015), especially Section 5.1.11 and Proposition 5.4, shows the carousel family is strongly polynomial under homomorphism counting. Its logical interpretation framework provides related qualitative finiteness/convergence context but does not give the exact rank-four equivalence cutoff or the seven separating finite signatures. Counting homomorphisms is not itself a four-round equivalence theorem.

Published finite-model investigations of rank cutoffs for directed paths and prime cyclic groups use different relational structures and cannot be substituted for the present tournament statement. Searches of equivalent titles, cyclic/round-tournament aliases, antipodal circular-order strategies, stronger logical bounds, and relevant published research records found no direct covering implication. Lack of a located source is not a mathematical proof of priority.

## Limitations
The exact seven-class statement is specific to the one-relation tournament signature and rank four. Naming circular order or arithmetic may distinguish larger orders sooner. No exact rank-five or general-rank classification is claimed. The exponential uniform upper bound is proved but may not be sharp beyond the depths settled here. Independent scientific audit has not been performed, and unindexed or inaccessible prior equivalences remain a priority risk.

## References
- Leonardo Nagami Coregliano, *Quasi-Carousel Tournaments*, initial arXiv publication March 13, 2015, arXiv:1503.04124; https://arxiv.org/abs/1503.04124 .
- A. J. Goodall, J. Nešetřil, and P. Ossona de Mendez, *Strongly Polynomial Sequences as Interpretations*, manuscript December 15, 2015, Section 5.1.11, Proposition 5.4; https://iti.mff.cuni.cz/series/2015/631.pdf .
- Classical Ehrenfeucht–Fraïssé back-and-forth characterization of bounded quantifier rank, used explicitly through the displayed finite recursion.
