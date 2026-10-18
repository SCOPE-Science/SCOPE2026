# The rank-two power hierarchy of binary words

## Finding
Let \(\mathcal W\) denote the nonempty finite binary words in which both letters \(0\) and \(1\) occur. Regard a word as a finite linearly ordered structure whose positions carry exactly one of the two named predicates \(P_0,P_1\). The vocabulary is \(\{<,P_0,P_1\}\), **without a successor predicate**. Write \(\operatorname{Th}_2(v)\) for its complete first-order sentence theory of quantifier rank at most two, and set
\[
\mathcal T_k=\{\operatorname{Th}_2(w^k):w\in\mathcal W\}\qquad(k\geq1).
\]
Then
\[
|\mathcal T_1|=90,\qquad |\mathcal T_2|=30,\qquad |\mathcal T_k|=16\quad(k\geq3),
\]
and \(\mathcal T_3\subsetneq\mathcal T_2\subsetneq\mathcal T_1\). More strongly, **for each fixed root** \(w\in\mathcal W\),
\[
\operatorname{Th}_2(w^k)=\operatorname{Th}_2(w^3)\quad\text{for all }k\geq3.
\]
The uniform stabilization exponent three is sharp: \(01\,01\) and \(01\,01\,01\) are not rank-two equivalent.

Every class in \(\mathcal T_2\) has a square root of length at most six; **exactly two classes require length six**, with shortest roots `001100` and `110011`. Every class in \(\mathcal T_3\) has a cube root of length at most five; **exactly two classes require length five**, with shortest roots `00100` and `11011`. These length bounds are optimal over all possible roots containing both letters. Full shortest-root histograms are:

| Shortest root length | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|
| Square classes | 2 | 6 | 10 | 10 | 2 |
| Cube (all \(k\geq3\)) classes | 2 | 6 | 6 | 2 | 0 |

The count of 90 unrestricted mixed-letter rank-two theories is included as context rather than claimed as a separate new finding. The power-constrained counts, their sharp root-size distribution, and the sharp exponent-three stabilization are the subject of this result.

## Assumptions and scope
All quantifiers range over word **positions**. A word has at least one occurrence of each letter, and each position belongs to exactly one of the two named colour predicates. Repetition \(w^k\) means concatenation of \(k\) copies of the *same* root. Both colour names and the left-to-right orientation of the order are fixed: neither swapping the colours nor reversing the word is identified unless rank-two equivalence itself identifies them. The result does not concern the richer vocabulary containing an immediate-successor relation, nor unbounded-rank theories, nor arbitrary unions of different roots.

## Proof
**1. A complete rank-two invariant.** For the letter \(a_i\) at position \(i\) in a word \(v\), put
\[
L_i(v)=\{a_j:j<i\},\qquad R_i(v)=\{a_j:j>i\},\qquad
S(v)=\{(a_i,L_i(v),R_i(v)):i\in v\}.
\]
An arbitrary formula of quantifier rank one with one free position variable is a Boolean combination of the letter test at that position and tests expressing the existence of a letter of a specified colour strictly to its left or right. The equal-position case is already determined by the letter test. Thus the pointed rank-one type at \(i\) is exactly \((a_i,L_i,R_i)\). A sentence of rank at most two is a Boolean combination of assertions that a rank-one pointed type is realized (the outer quantifier is existential, with universal quantifiers expressed by negation). Conversely, each pointed type is definable by a rank-one conjunction. Consequently, for any two nonempty binary words,
\[
v\equiv_2 v'\ \Longleftrightarrow\ S(v)=S(v').
\tag{1}
\]
The same characterization follows from the two-round Ehrenfeucht--Fraisse game, and uses no bound on word length.

**2. Powers depend on a pair of one-sided profiles.** Let \(A(w)\) be the set of letters used by \(w\), and define
\[
X(w)=\{(a_i,L_i(w)):i\in w\},\qquad
Y(w)=\{(a_i,R_i(w)):i\in w\}.
\]
Because a first copy of \(w\) in \(w^2\) has a full second copy to its right, and the last copy has a full first copy to its left,
\[
S(w^2)=\{(a,L,A(w)):(a,L)\in X(w)\}\cup
\{(a,A(w),R):(a,R)\in Y(w)\}.
\tag{2}
\]
Every position in an interior copy of \(w\) in \(w^k\), for \(k\geq3\), has the full alphabet both before and after it. Thus
\[
S(w^k)=S(w^2)\cup\{(a,A(w),A(w)):a\in A(w)\}\quad(k\geq3).
\tag{3}
\]
Equations (1)--(3) prove universal stabilization after three copies, regardless of root length. They also show that a cube theory is realized by a square: \(w^3\equiv_2 w^4=(w^2)^2\), so \(\mathcal T_3\subseteq\mathcal T_2\).

Sharpness is witnessed by \(w=01\). In \(010101\) there is a \(0\)-position with both colours strictly to its left and strictly to its right; in \(0101\) there is none. This is expressible by a rank-two sentence, with one outer quantified position and four parallel one-step existence tests.

**3. Exact finite closure certifies all roots, not merely a bounded sample.** Encode subsets of \(\{0,1\}\) by bit masks \(0,1,2,3\). A prefix state is \((A,X,Y)\), with \(X\) and \(Y\) sets of ordered pairs \((a,B)\) where \(a\in\{0,1\}\) and \(B\subseteq\{0,1\}\). The state of the empty prefix is \((\varnothing,\varnothing,\varnothing)\). Appending letter \(b\) acts by the **exact** recurrence
\[
(A,X,Y)\longmapsto\Big(A\cup\{b\},\ X\cup\{(b,A)\},\
\{(a,R\cup\{b\}):(a,R)\in Y\}\cup\{(b,\varnothing)\}\Big).
\tag{4}
\]
The included `verify.py` enumerates the state graph reachable from the empty prefix by both transitions, with no word-length cutoff. Its `certificate.json` records every state, both successors, and the full square and cube signatures. There are exactly \(37\) reachable states, of which \(32\) use both letters. For these \(32\) states, (2) has exactly \(30\) distinct images and (3) exactly \(16\). The shortest roots for the distinct images have the distributions in the table above. Breadth-first discovery of every state in increasing word length proves that these minima range over **all** binary roots, not just roots within a preset enumeration bound. In particular the sharp maxima are six and five, with the specified extremal roots.

Finally, direct literal enumeration of roots up to lengths six and five reconstructs the respective complete sets and minimum-length distributions without using (4). A separate two-round game implementation distinguishes every pair of unequal computed power signatures. The full-word rank-two closure yields \(90\) both-letter theories, confirming the background value used to compare the hierarchy.

## Verification
With Python 3 (standard library only) in the directory containing `verify.py` and `certificate.json`, run:

```text
python3 verify.py
```

The program requires all \(37\) states and their successor closure, exactly \(32\) two-letter states, \(30\) square images, \(16\) cube images, the complete shortest-root histograms, the two pairs of extremal roots, and the \(90\)-class unrestricted reference count. For every reachable two-letter state it also constructs actual words from its shortest representative and compares (2)--(3) against directly evaluated position signatures of its powers. Independent bounded literal-word enumeration supplies a check on the image counts. All pairwise distinct candidate classes are cross-checked by a direct two-round game routine. The certificate is regenerated canonically in memory and compared byte-for-byte to the bundled `certificate.json`.

## Relationship to prior work
Weis and Immerman established a general ranker characterization of two-variable first-order logic on words at each quantifier depth, including their Theorem 8. Rank two of unrestricted first-order sentences coincides here with rank two in the two-variable fragment, since at most two bound variables are simultaneously needed along any syntactic branch. That broad characterization supplies general logical context, but the present result instead calculates the exact **power-restricted** theory images, sharp root lengths, and the first universal stabilization exponent. None of those numerical power classifications is stated in the inspected material. The established equivalence of two-variable logic with unary temporal logic, due to Etessami, Vardi, and Wilke, provides further context, not an exact power-image census. The distinct notion of two-binomial word equivalence studied by Rao, Rigo, and Salimov counts scattered subsequences and is not the logical equivalence used here.

## Limitations
The enumeration is an exhaustive **finite-state closure derived from a proved recurrence**, not a proof that all word properties are first-order definable, and it concerns only rank at most two with named binary colours and strict order. The result does not establish any statement at quantifier rank three, with a named successor predicate, or over larger alphabets. General logical equivalence theorems precede it; numerical priority of the power-specific census may be affected by an unlocated earlier finite tabulation. Independent audit of the computation and literature priority has not been performed.

## References
1. Philipp Weis and Neil Immerman, *Structure Theorem and Strict Alternation Hierarchy for FO² on Words*, ECCC TR07-008 (publicly issued January 18, 2007); Logical Methods in Computer Science 5(3), 2009; arXiv:0907.0616v2, especially Theorem 8 and Sections 2, 3, 6. https://arxiv.org/html/0907.0616v2
2. Kousha Etessami, Moshe Y. Vardi, and Thomas Wilke, *First-Order Logic with Two Variables and Unary Temporal Logic*, LICS, 1997. https://lics.siglog.org/archive/1997/EtessamiVardiWilke-FirstOrderLogicwith.html
3. Michaël Rao, Michel Rigo, and Pavel Salimov, *Avoiding 2-binomial squares and cubes*, Theoretical Computer Science 572 (2015), 83–91. https://orbi.uliege.be/handle/2268/178702
