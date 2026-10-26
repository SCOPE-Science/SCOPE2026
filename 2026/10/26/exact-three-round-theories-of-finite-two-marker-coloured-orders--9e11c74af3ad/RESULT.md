# Exact three-round theories of finite two-marker coloured orders

## Finding
Let \(B\) and \(R\) be the two colours of a finite linearly ordered structure, and write
\[
W_{a,b,c}=B^a R B^b R B^c,\qquad a,b,c\in\mathbb N_0.
\]
Thus precisely two positions are red. Let \(\equiv_3\) denote agreement on every first-order sentence of quantifier rank at most three (equivalently, Duplicator wins the three-move Ehrenfeucht--Fraïssé game).

Define the canonical triple \(\nu(a,b,c)\) by the following exhaustive cases, retaining every zero coordinate:

* If all three coordinates are positive, truncate the first and last coordinates at \(6\) and the middle at \(5\): \(\nu(a,b,c)=(\min(a,6),\min(b,5),\min(c,6))\).
* If exactly two coordinates are positive, truncate both positive coordinates at \(6\), keeping the zero coordinate equal to zero.
* If exactly one coordinate is positive, truncate it at \(7\), keeping both zero coordinates.
* If all are zero, \(\nu(a,b,c)=(0,0,0)\).

**Theorem.** For all nonnegative integer triples,
\[
W_{a,b,c}\equiv_3W_{a',b',c'}
\quad\Longleftrightarrow\quad
\nu(a,b,c)=\nu(a',b',c').
\]
Consequently there are exactly
\[
1+3\cdot7+3\cdot 6^2+6\cdot5\cdot6=310
\]
distinct rank-three theories in the two-red family. Each class has a shortest representative with at most \(19\) positions. Exactly one canonical class attains that maximum: \(\nu=(6,5,6)\), represented by \(B^6RB^5RB^6\). Every rank-three-equivalent coloured word, even without the two-red restriction, also has exactly two red points, so the sharp minimum is global within all two-colour words.

## Assumptions and scope
The language consists of a strict total order and unary predicates for red and blue; exactly one of the predicates holds at each element. Structures are finite and may have no blue points but always have exactly two red points. Quantifier rank counts nesting, not total quantifier occurrences. The claim is restricted to rank three and exactly two red positions: it does not classify arbitrary binary words or higher ranks.

## Proof
**Step 1 (finite truncation).** For monochromatic finite orders of lengths \(m,n\), the standard linear-order game characterization gives
\[
B^m\equiv_q B^n\quad\Longleftrightarrow\quad
\min(m,2^q-1)=\min(n,2^q-1).
\]
In particular, at rank three each blue run can be shortened to length \(7\). The concatenation lemma for Ehrenfeucht--Fraïssé equivalence (Mwesigye--Truss 2011, Lemma 1.3) preserves \(\equiv_q\) under concatenation with fixed coloured words. Apply it successively to the three blue runs to obtain
\[
W_{a,b,c}\equiv_3 W_{\min(a,7),\min(b,7),\min(c,7)}.
\]
This is a logically justified exhaustive reduction to \(8^3=512\) finite cases; no bound on the original word lengths is needed.

**Step 2 (exact type recurrence).** For any finite word \(w\), define a recursively built, immutable mathematical object \(T_q(w)\) by
\[
T_0(w)=\varnothing,
\qquad
T_{q+1}(w)=\bigl\{\bigl(w_i,T_q(w_{<i}),T_q(w_{>i})\bigr):i\text{ is a position of }w\bigr\}.
\]
The triple records the colour of the selected position and the lower-rank types of the segments on its two sides. By the character theorem of Mwesigye--Truss (2011, Theorem 1.2; 2018, Theorem 1.1),
\[
w\equiv_q v\quad\Longleftrightarrow\quad T_q(w)=T_q(v).
\]
The equality is exact, not probabilistic hashing: sets of nested tuples are compared structurally.

**Step 3 (finite exhaustive lemma).** Apply the explicit recurrence from Step 2 at \(q=1,2,3\) to every triple in \(\{0,1,\ldots,7\}^3\). The complete reproducible enumeration in `verify.py` checks both implications
\[
T_3(W_{a,b,c})=T_3(W_{a',b',c'})
\quad\Longleftrightarrow\quad
\nu(a,b,c)=\nu(a',b',c')
\]
without enumerating pairs: it constructs a dictionary keyed by the exact rank-three type and another keyed by the proposed canonical triple and rejects any disagreement in either direction. The loop iterates over all \(512\) triples. The number of canonical keys is \(310\). This establishes a finite mathematical lemma with a complete, replayable certificate; sample testing is not being used as an infinite proof.

**Step 4 (class count and optimality).** Among canonical triples, zero, one, two, or three positive coordinates contribute, respectively, \(1\), \(3\cdot7\), \(3\cdot6^2\), or \(6\cdot5\cdot6\) possibilities. Thus there are exactly \(310\) classes. In the three-positive case, the longest canonical word has \(6+5+6+2=19\) positions; in the other cases the maxima are \(14,9,2\). The finite lemma shows that distinct canonical triples are not equivalent, so the word \(B^6RB^5RB^6\) cannot be shortened within the two-red family. Rank-three formulas assert the existence of two distinct red elements and deny the existence of three pairwise distinct red elements; hence any equivalent binary-coloured word still has exactly two reds. This proves the sharp global representative bound for these classes.

## Verification
Run `python3 verify.py` using the Python standard library. The program builds exact nested-set character types for every one of the \(512\) truncated triples, checks both directions of the canonical-form biconditional, counts the \(310\) classes, verifies the maximum and unique extremal canonical triple, and compares its type computation with a separately implemented direct Duplicator/Spoiler game recurrence on fourteen boundary pairs. Its successful final line is `VERIFY_OK`.

The infinite-domain part of the theorem rests on the truncation and concatenation theorems, not on finite experimentation. The finite lemma is exhaustive over the rigorously reduced \(512\)-element parameter box.

## Relationship to prior work
Mwesigye and Truss (2011) prove the character recursion and concatenation principle, and provide general computability bounds for optimal representatives. Their 2018 paper classifies rank-two coloured-order equivalence and analyzes difficult general rank-three examples, including optimal strings of length \(70\) and \(74\). Neither paper's inspected results state this closed canonical form, the number \(310\), or the sharp \(19\)-point bound for words with exactly two red markers.

A separate published result establishes an all-rank formula for **one** red marker, which does not imply the two-marker classification: adding the second distinguished position creates a middle gap with a new visibility threshold, \(5\), instead of the outer threshold \(6\). The present result is an exact rank-three classification of that next natural finite-parameter family, not a general rank-three classification of all two-colour words.

## Limitations
The proof relies on a finite recurrence certificate for a \(512\)-case combinatorial lemma; a shorter hand-only derivation of the seven-case thresholds is not claimed. The full priority of the numerical and canonical-form result cannot be established from indexed searches alone; a related 2009 Leeds doctoral thesis was not inspected. No independent mathematical audit has been performed.

## References
1. F. Mwesigye and J. K. Truss, “On Optimal Representatives of Finite Coloured Linear Orders,” *Order* 36 (2019), 107–117; author manuscript deposited 6 April 2018; online 2 May 2018. DOI: 10.1007/s11083-018-9458-3. Open-access full text: https://link.springer.com/content/pdf/10.1007/s11083-018-9458-3.pdf.
2. F. Mwesigye and J. K. Truss, “Classification of Finite Coloured Linear Orderings,” *Order* 28 (2011), 387–397; first online 7 September 2010. DOI: 10.1007/s11083-010-9178-9. Lawful institutional repository copy: https://ir.must.ac.ug/bitstreams/ce8f9fc1-8064-4e56-b7ae-a30dd6b401c0/download.
3. “Exact quantifier-rank profiles for finite one-red linear orders,” publicly posted mathematical result (2026); it establishes the single-marker formula \((2^q-1)^2+2\) for \(q\ge2\). Its one-red hypotheses differ from the present two-red family.
