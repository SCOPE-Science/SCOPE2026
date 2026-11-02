# Seven rank-two theories and a mod-eight oscillation among alternating groups

## Finding

Let \(A_n\) be the finite alternating group of even permutations of \(n\) letters, for any integer \(n\ge5\), in the **relational** first-order signature consisting of equality, the named identity \(e\), and \(M(a,b,c)\), true precisely when \(ab=c\). Let \(\equiv_2\) denote equivalence for every sentence of quantifier rank at most two.

There are **exactly seven** such theories among the nonabelian simple groups \(A_n\). Their classes, with sharp least-degree representatives in parentheses, are

1. \(\{5\}\) (5);
2. \(\{6\}\) (6);
3. \(\{7,9\}\) (7);
4. \(\{8\}\) (8);
5. \(\{10\}\) (10);
6. \(\{n\ge11:n\bmod8\notin\{4,5\}\}\) (11);
7. \(\{n\ge11:n\bmod8\in\{4,5\}\}\) (12).

Equivalently, after the five exceptional parameter classes, the quantifier-rank-two theory never stabilizes: for every \(n\ge11\), its sole residual parameter is whether \(n\bmod8\in\{4,5\}\). In particular \(A_7\equiv_2 A_9\), whereas \(A_{8k+12}\not\equiv_2 A_{8k+14}\) for every \(k\ge0\). The maximum least degree needed to represent one of these theories is sharply 12; this is a bound on the alternating-group **degree**, not group order.

## Assumptions and scope

All groups are ordinary finite alternating groups \(A_n\), \(n\ge5\). A multiplication atom uses a **ternary relation** \(M\), not a binary function symbol; the latter would make arbitrarily long powers atomic and would change the statement. Identity is a constant. The group elements are permutations but the ambient permutation action is not part of the first-order language. In the following, \(S(u,v)\) abbreviates the atomic formula \(M(u,u,v)\), and \(u\) is a square if \(\exists v\,S(v,u)\).

## Proof

**1. Reduction to one-element extension profiles.** In a two-round Ehrenfeucht–Fraïssé game, the second selected element \(y\) is tested only by atomic formulas on \(e,x,y\), where \(x\) is the first element. For an arbitrary group \(G\) having at least five involutions and at least five elements of order three, these atomic patterns are controlled by the following possible collisions: \(y=e\), \(y=x\), \(y=x^{-1}\), \(y=x^2\), \(y^2=e\), and \(y^2=x\). All remaining multiplication atoms on \(e,x,y\) are either group identities or instances of these collisions. The only possible overlaps are determined by the order of \(x\) being \(1,2,3,4\), or outside those four values. A nonexceptional involution \(y\) is always available, because there are many involutions and at most three collision points. A nonexceptional element \(y\) of order three is similarly always available, because \(A_n\) has at least twenty 3-cycles. It follows that one-element extension profiles are exactly the following nine categories (only some need occur in a given group):

- \(E\): the identity;
- \(I^+,I^-\): order-two elements with, respectively without, a square root;
- \(T^+,T^-\): order-three elements with, respectively without, a square root **different from** \(x^{-1}\);
- \(F^+,F^-\): order-four elements with, respectively without, a square root;
- \(X^+,X^-\): elements of order outside \(\{1,2,3,4\}\), with, respectively without, a square root.

For clarity, in the order-three case \(x^{-1}\) is always a square root of \(x\). The extra-root flag is necessary: \(A_7\) realizes both \(T^+\) and \(T^-\), while \(A_8\) realizes only \(T^+\). Each category is definable as a property of \(x\) by a formula of quantifier rank at most one with \(x\) free: the order-two test is \(x\ne e\land S(x,e)\), the order-three test is \(x\ne e\land\exists y(S(x,y)\land S(y,x))\), the order-four test is \(x\ne e\land\neg S(x,e)\land\exists y(S(x,y)\land y\ne e\land S(y,e))\), and the remaining order category is their complement outside the identity. Square-root existence is \(\exists y\,S(y,x)\); the extra order-three root is \(\exists y(S(y,x)\land\neg M(x,y,e))\). Thus existence of each of the nine categories is detected by a **sentence of rank at most two**. Conversely, matching the realized categories gives a winning two-round Duplicator strategy, by the complete atomic extension-profile description. Therefore two groups in this family are rank-two equivalent exactly when their category-presence sets agree.

**2. Even square-root criterion.** Suppose a permutation \(x\in A_n\) has \(c_j\) cycles of length \(j\), including fixed points. It has a square root in \(A_n\) if and only if every \(c_j\) with even \(j\) is even, and either
\[
\sum_{j\text{ even}}\frac{c_j}{2}\equiv0\pmod2,
\]
or some odd \(j\) satisfies \(c_j\ge2\). Indeed, the square of an even-length cycle splits into two equal cycles, forcing even-length cycles of \(x\) to pair; each pair is supplied by a root cycle of length \(2j\), which is an odd permutation. Every odd-length cycle has a unique root supported on that cycle, and this root is even. Pairing two equal odd-length cycles instead creates one additional even-length root cycle and flips the root's parity. These are all possibilities, proving both necessity and sufficiency, including the length-one case.

**3. Order-two, order-four, and other categories.** An involution in \(A_n\) has an even number \(t\) of transpositions and \(f=n-2t\) fixed points. Its square roots must pair its transpositions into \(t/2\) four-cycles, and an even root exists if and only if \(t/2\) is even or \(f\ge2\). Hence a nonsquare involution exists precisely when \(n\equiv4\) or \(5\pmod8\), for \(n\ge4\). A square involution exists in \(A_n\) precisely when \(n\ge6\), using the square of an even permutation of cycle type \((4,2)\). A nonsquare order-four element exists for every \(n\ge6\), namely one of type \((4,2,1^{n-6})\). A square order-four element requires an even square root of order eight. The smallest such even permutation has type \((8,2)\) and therefore needs ten letters; it exists for every \(n\ge10\). An element of order outside \(\{1,2,3,4\}\) that is a square exists for all \(n\ge5\), using a 5-cycle. A nonsquare element of that order exists for \(n=7\) (type \((3,2,2)\), whose only symmetric-group square roots are odd) and all \(n\ge8\) (type \((6,2,1^{n-8})\), which lacks a symmetric-group square root). There are no such elements for \(n=5,6\), by listing their even cycle partitions.

**4. The order-three exceptional root.** Such an element has cycle type \((3^t,1^f)\), \(t\ge1\). Every root is \(x^{-1}z\), where \(z\) is an involution (possibly the identity) commuting with \(x\). An additional root exists exactly when the centralizer \((C_3\wr S_t)\times S_f\) contains a nontrivial even involution. An even involution can be built using two transpositions among fixed points, by swapping two 3-cycles together with two fixed points, or by independently swapping two pairs of 3-cycles; their respective conditions are \(f\ge4\), \(t\ge2\) and \(f\ge2\), or \(t\ge4\). Conversely, any involution in this centralizer is assembled from these swaps, and the parity condition forces one of those three alternatives. Consequently \(T^-\) is realized for \(n\ge5\) exactly at
\[
 n\in\{5,6,7,9,10\},
\]
while \(T^+\) is realized exactly when \(n\ge7\).

**5. Assemble the complete spectrum.** For all \(n\ge5\), the realized-category conditions are:

| Category | Exactly when present |
| --- | --- |
| \(E\) | all \(n\ge5\) |
| \(I^+\) | \(n\ge6\) |
| \(I^-\) | \(n\bmod8\in\{4,5\}\) |
| \(T^+\) | \(n\ge7\) |
| \(T^-\) | \(n\in\{5,6,7,9,10\}\) |
| \(F^+\) | \(n\ge10\) |
| \(F^-\) | \(n\ge6\) |
| \(X^+\) | all \(n\ge5\) |
| \(X^-\) | \(n\ge7\) |

The seven distinct row-presence sets yield exactly the seven classes in the finding. The rank-two-definable category predicates separate distinct classes; Duplicator's strategy from step 1 proves equivalence within each class. In particular the recurrence of \(I^-\) is an *infinite* congruence phenomenon, not an extrapolation from the calculations below.

## Verification

Three standalone programs accompany this result. `alt_rank2_types.py` enumerates all even cycle partitions and uses the explicit even-root and centralizer criteria for parameters from 3 through 40; its output is `alt_partition_table.tsv`. `alt_rank2_fast.py` independently enumerates all even permutations for \(n=5,6,7,8,9\), represents each symmetric-conjugacy type once, and computes the full two-pebble atomic extension spectrum by group permutation arithmetic. Its recorded output is `alt_fast_output.txt`. `alt_rank2_direct.py` separately computes all 27 named-identity multiplication atoms on triples drawn from \(e,x,y\) for \(n=5,6,7,8\); its output is `alt_direct_output.txt`. The computations agree on every tested class. Full direct enumeration at \(n=10\) is not claimed. Neither a finite census nor a direct test replaces the proofs in steps 1–5.

## Relationship to prior work

Classical permutation cycle decomposition and square-root combinatorics supply the ingredients of step 2. Baranov and Klyachko (2011) study economical adjunction of square roots to groups, not the first-order equivalence classification of alternating groups. Gomaa (2010) investigates bounded logical resources for **finite abelian** groups. Mahmood and Rajah (2011 issue) treat power equations in selected alternating-group conjugacy classes, with restrictions including distinct odd cycle lengths; neither the cycle-type root ingredients nor the cited statements alone establish the seven rank-two classes or their infinite mod-eight oscillation. The standard Ehrenfeucht–Fraïssé characterization is the logical framework. Published indexed-result comparisons did not identify an equivalent classification; this is not a proof of bibliographic uniqueness.

## Limitations

No classification of rank three or higher is claimed. The result is language-specific: changing ternary relational multiplication to a multiplication **function**, adding permutation-action predicates, or changing constants changes quantifier rank. The proof establishes only the stated rank-two classification; the finite checks are reproducible supporting evidence rather than a substitute for the symbolic arguments.

## References

1. W. Gomaa, *Descriptive complexity of finite abelian groups*, International Journal of Algebra and Computation **20** (2010), 1087–1116, DOI 10.1142/S0218196710006047.
2. D. V. Baranov and A. A. Klyachko, *Economical adjunction of square roots to groups*, arXiv:1101.3019v1, submitted 2011-01-15.
3. S. Mahmood and A. Rajah, *Solving the class equation \(x^d=\beta\) in an alternating group*, Journal of the Association of Arab Universities for Basic and Applied Sciences **10** (2011), 42–50, DOI 10.1016/j.jaubas.2011.06.006. Its online presentation was dated 2018; the issue year is not treated as the first public posting date.
4. J. Väänänen and T. Wang, *An Ehrenfeucht–Fraïssé Game for \(L_{\omega_1\omega}\)*, arXiv:1212.0108v1 (2012-12-01), for the historical game context.
