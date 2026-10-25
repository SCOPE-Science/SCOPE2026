# Two-round theories of finite two-coloured equivalence structures

## Finding
Consider nonempty finite structures \((A,E,R)\), where \(E\) is an equivalence relation and \(R\) is a unary predicate; call the elements in \(R\) red and the other elements blue. Two structures are two-equivalent when they satisfy the same first-order sentences of quantifier rank at most two in the language \(\{E,R,=\}\), with no counting quantifiers or constants.

**Theorem.** There are exactly \(207\) two-equivalence classes of such structures. Every class contains a representative with at most \(13\) elements, and this universal bound is sharp. Exactly two of the \(207\) classes require \(13\) elements. The distribution by the *minimum* size of a representative is:

| Minimum size | Number of classes |
| ---: | ---: |
| 1 | 2 |
| 2 | 6 |
| 3 | 10 |
| 4 | 17 |
| 5 | 22 |
| 6 | 28 |
| 7 | 30 |
| 8 | 29 |
| 9 | 26 |
| 10 | 18 |
| 11 | 12 |
| 12 | 5 |
| 13 | 2 |

A complete, exact invariant is the set \(\{\chi(x):x\in A\}\), where \(\chi(x)\) comprises five Boolean values: the colour of \(x\), whether another red element lies in its \(E\)-class, whether another blue element lies in its \(E\)-class, whether a red element lies outside its \(E\)-class, and whether a blue element lies outside its \(E\)-class. This gives an explicit characterization of two-equivalence, independently of the enumeration.

## Assumptions and scope
All domains are finite and nonempty. An \(E\)-class has two nonnegative counts \((r,b)\) for its red and blue members. Colours are distinguished (not identified under swapping). Empty colour classes are permitted; the binary relation is required to be reflexive, symmetric, and transitive. First-order quantifier rank counts the maximum nesting of individual quantifiers; arbitrary finite Boolean combinations do not increase it.

For reproducibility, use the ordered list of capped block shapes
\[
(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2).
\]
A canonical profile records their eight multiplicities, each in \(\{0,1,2\}\), not all zero. For example, the profile `11100111` denotes one block of each of the first, second, third, sixth, seventh, and eighth shapes.

## Proof
**Step 1: complete local invariant.** Fix a point \(x\). The one-round type of \(x\) is determined by its colour and by the set of quantifier-free binary types of \((x,y)\), as \(y\) ranges over the domain. Since \(E\) is an equivalence, these binary types reduce exactly to the existence flags of another point of each colour inside or outside \([x]_E\), plus the automatic possibility \(y=x\). Thus the one-round type is precisely the five-bit character \(\chi(x)\). In the two-round Ehrenfeucht–Fraïssé game, Duplicator wins exactly when every possible first choice on either side has a response with the same one-round type. Therefore the two-equivalence invariant is exactly \(\{\chi(x):x\in A\}\). Each bit is expressed by an existential formula with one bound variable after naming \(x\), proving both directions without relying on computation.

**Step 2: finite reduction.** Replace the red and blue counts of every individual \(E\)-class by their minimum with two. Then, for each resulting nonzero block shape, retain at most two blocks. This operation preserves two-equivalence: in a two-round game, at most two different blocks can be visited, and at most two individual elements of a given colour can be selected from one block. Duplicator can match a first selected block by its capped colour counts and can match a second move either within that block, to the same element, or in another block of the required shape. The same argument works in both directions. Consequently every finite nonempty structure is two-equivalent to one of the \(3^8-1=6560\) canonical profiles above. Every canonical profile represents an actual finite structure; there are no infeasible profiles.

**Step 3: exact finite classification.** For a profile \((m_t)\), the total red and blue counts are \(R_0=\sum_t m_t r_t\) and \(B_0=\sum_t m_t b_t\). Each present block shape \((r,b)\) contributes the following characters (using \(1\) for red and \(0\) for blue):
\[
\begin{aligned}
&r>0:\quad (1,[r\ge2],[b\ge1],[R_0>r],[B_0>b]),\\
&b>0:\quad (0,[r\ge1],[b\ge2],[R_0>r],[B_0>b]).
\end{aligned}
\]
Here brackets denote the truth value of the enclosed comparison. Taking the union over present shapes produces the exact invariant from Step 1. The standalone `verify_colored_equivalence.py` enumerates all \(6560\) profiles, groups them by this set, and minimizes \(\sum_t m_t(r_t+b_t)\) within each group. It obtains exactly \(207\) groups with the table of minimum sizes displayed above. This is a **finite exhaustive proof** for the reduced domain; Step 2 independently establishes that it covers every finite structure. `CLASSIFICATION.csv` lists every group, its least profile, its exact minimum size, and its number of canonical profiles. The algorithm uses exact integers and set equality, with no floating point or heuristic search.

**Step 4: sharpness.** Two minimal extremal representatives are the six-block structures whose class colour multisets are, respectively,
\[
\{B,BB,R,RR,RRB,RRBB\},\qquad
\{B,BB,R,RR,RBB,RRBB\}.
\]
Each has \(1+2+1+2+3+4=13\) elements. For the first structure, the five-bit invariant requires blue-only singleton and doubleton classes, red-only singleton and doubleton classes, a mixed class with exactly one blue, and a mixed class with at least two blues. It also excludes any red point having a blue classmate but no *other* red classmate. Thus the last two mixed classes must contain at least \((2,1)\) and \((2,2)\) red-blue counts, respectively, and all six required blocks are distinct; any equivalent structure has at least \(13\) elements. The second structure is obtained by interchanging red and blue, giving the same lower bound. Step 3 shows that every other group has a representative of size at most \(12\).

## Verification
Run `python3 verify_colored_equivalence.py` from the directory containing the script. The script generates `CLASSIFICATION.csv` and checks all \(6560\) canonical profiles by **two independently implemented character computations**: the closed-form five-bit formula and direct enumeration of quantifier-free extensions of every element. It asserts that both computations induce precisely the same partition, checks the exact count and the complete minimum-size distribution, and checks both extremal profiles. The recorded output is in `verification_output.txt` and ends with `ALL_CHECKS_PASSED`.

The only non-finite logical step is the two-round reduction; its game argument is given in Step 2. No inference about arbitrary structures is made solely from unbounded numerical extrapolation.

## Relationship to prior work
Pratt-Hartmann, *The two-variable fragment with counting and equivalence* (2015), studies much stronger languages and develops local-configuration and satisfiability machinery for equivalence structures; its investigated conclusions concern complexity and certificates rather than the exact \(207\)-class, rank-two classification and its sharp thirteen-point bound. Mwesigye and Truss, *On Optimal Representatives of Finite Coloured Linear Orders* (online 2018), examine two- and three-move games for coloured **linear orders**, not equivalence-class partitions. Fagin, Lenchner, Regan, and Vyas, *Multi-Structural Games and Number of Quantifiers* (first preprint 2021), distinguish quantifier number from quantifier rank and provide the ordinary Ehrenfeucht–Fraïssé equivalence theorem as background; their numerical results concern ordered structures. None of these inspected results states the present count or its extremal bound.

The unary predicate is essential: an uncoloured equivalence relation's shallow types do not determine how red and blue elements are distributed *within* classes. General existence of an algorithm for finite-model comparison, without the exact induced count and smallest representatives, does not itself provide those numerical conclusions. A possible equivalent historical classification under the terminology *coloured partitions*, *one-point characters*, or *unary expansions of equivalence relations* remains a publication-priority risk.

## Limitations
This theorem concerns **one unary predicate**, **one equivalence relation**, **nonempty finite domains**, and **quantifier rank at most two**. It does not classify greater quantifier ranks, counting-quantifier languages, arbitrary additional predicates, or infinite structures. The exact numerical classification depends on executing the supplied deterministic exhaustive enumeration after the proved canonical reduction. Historical priority beyond the inspected sources is not certified.

## References
1. F. Mwesigye and J. K. Truss, *On Optimal Representatives of Finite Coloured Linear Orders*, Order 36 (2019), 107–117; first online 2018-05-02. DOI: 10.1007/s11083-018-9458-3. https://link.springer.com/article/10.1007/s11083-018-9458-3
2. R. Fagin, J. Lenchner, K. W. Regan and N. Vyas, *Multi-Structural Games and Number of Quantifiers*, first public arXiv version 2021-04-30, arXiv:2104.14709. https://arxiv.org/abs/2104.14709
3. I. Pratt-Hartmann, *The two-variable fragment with counting and equivalence*, Mathematical Logic Quarterly 61 (2015), 474–515. DOI: 10.1002/malq.201400102. https://onlinelibrary.wiley.com/doi/10.1002/malq.201400102
