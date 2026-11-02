# Sixteen rank-three theories of finite strict-coordinate grid orders

## Finding
Let \(S_{m,n}\) be the rectangular grid with a binary strict-coordinate relation as below. For any positive parameters \(m,n,p,q\), its quantifier-rank-three theory is classified by a finite key \(K\):
\[
S_{m,n}\equiv_3 S_{p,q}\quad\Longleftrightarrow\quad K(m,n)=K(p,q).
\]
Write \(a=\min(m,n)\), \(b=\max(m,n)\), \(u=\min(a,7)\), and \(v=\min(b,7)\). Put
\[
c_1=3,\quad c_2=4,\quad c_3=5,\quad c_4=c_5=c_6=6.
\]
For \(u\le6\), set \(K(m,n)=(u,\min(v,c_u))\); for \(u=7\), set \(K(m,n)=(7,7)\). There are exactly sixteen distinct keys, with their lexicographically smallest grid representatives
\[
(1,1),(1,2),(1,3),(2,2),(2,3),(2,4),(3,3),(3,4),(3,5),
(4,4),(4,5),(4,6),(5,5),(5,6),(6,6),(7,7).
\]
Each equivalence class consequently has a grid representative of at most \(49\) points; this is sharp within the family.

## Assumptions and scope
For each positive integer \(s\), write \([s]=\{1,\ldots,s\}\). Define the finite relational structure
\[
S_{m,n}=([m]\times[n],\triangleleft),\qquad
(i,j)\triangleleft(k,\ell)\ \Longleftrightarrow\ i<k\ \text{and}\ j<\ell.
\]
The first-order signature has precisely the binary relation \(\triangleleft\) and built-in equality; there are no coordinate projections, endpoints, or named constants. In particular \(\triangleleft\) is *not* the strict part of the usual componentwise non-strict product order: both coordinates must increase. The notation \(\equiv_3\) means agreement on every first-order sentence of quantifier rank at most three.

## Proof
**Finite comparison reduction.** A finite linear order with at least \(2^r-1\) elements is equivalent, for \(r\) rounds of the Ehrenfeucht--Fraïss\u00e9 game, to every other such order. One standard proof maintains, between previously selected corresponding points and the endpoints, that each gap either has the same cardinality below \(2^t-1\) or both cardinalities are at least \(2^t-1\), where \(t\) moves remain. A point can be answered at the same short-end distance, or with long gaps on each side; the invariant then holds at \(t-1\). This also handles an empty list of selected points. Consequently at \(r=3\) all orders of size at least seven are equivalent.

Play such a three-round order strategy independently in the first and second coordinates of two product grids. Each newly played pair induces one move in each coordinate game. The componentwise pair of responses exists, even when a coordinate value repeats. Corresponding selected pairs have exactly the same equality pattern (equality holds precisely when both coordinate equalities hold) and the same strict-coordinate relation (the conjunction of the two coordinate strict inequalities). Hence
\[
S_{m,n}\equiv_3 S_{\min(m,7),\min(n,7)}.
\]
This step establishes a genuine infinite tail; no inference from numerical stabilization is used.

**Exact finite classification.** It remains to compare the \(28\) unordered pairs \(1\le m\le n\le7\). For a finite structure \(A\), and ordered selected points \(a,b,c\), let \(D_A(a,b,c)\) denote its complete atomic diagram: all equality comparisons and all ordered \(\triangleleft\) comparisons among these three (possibly repeated) variables. Define types recursively by
\[
T_1^A(a,b)=\{D_A(a,b,c):c\in A\},\qquad
T_2^A(a)=\{T_1^A(a,b):b\in A\},\qquad
T_3^A=\{T_2^A(a):a\in A\}.
\]
These are finite sets, without counting multiplicities. Backward induction in the three-round game shows that two structures have the same \(T_3\) exactly when Duplicator can win three rounds: at each move the available response types are *exactly* the displayed extension sets. This includes repeated variables and all equality atoms.

The attached `verify_strict.cpp` exhaustively constructs these sets by interning their sorted, deduplicated child-type lists, using nine oriented relation atoms and three equality atoms for each triple. The independently coded `verify_strict.py` instead represents pairwise diagrams with four symbols (equality, forward strict order, reverse strict order, incomparable), then applies immutable-set recursion. Their outputs agree byte-for-byte: among all \(28\) finite test grids there are precisely sixteen distinct \(T_3\), and their key fibres are exactly those defined above. This complete finite classification, combined with the preceding infinite reduction, proves both directions of the claimed equivalence.

**Optimal bound.** Every key has the indicated representative of cardinality at most \(49\). The \((7,7)\) class has no representative with fewer points in this grid family by the exhaustive finite comparison, and every parameter exceeding seven reduces to a parameter-seven grid; therefore the bound is sharp.

## Verification
Run `sh reproduce.sh` with Python 3 and a C++17 compiler. It recompiles both independently specified finite-type enumerators, compares their entire outputs, and prints exactly `verification_output.txt`. All \(28\) unordered dimensions from one to seven are examined exhaustively; both repeated choices and incompatible coordinate orderings are represented. The scripts do not purport to check the infinite game lemma, which is proved above.

## Relationship to prior work
Finite linear-order Ehrenfeucht--Fraïss\u00e9 classification supplies the seven-point reduction at quantifier rank three; Mwesigye and Truss discuss such methods for coloured finite linear orders. Kurilić treats products of chains under the ordinary product order, not the strict-coordinate conjunction relation used here. In the ordinary product order a one-coordinate increase may be comparable, while under \(\triangleleft\) it is not; those are different structures, and a bounded-rank classification of one signature does not automatically give the result for the other. The current statement is an exact fixed-rank classification of the strict-coordinate reduct. Historical priority beyond the inspected sources is not conclusively established.

## Limitations
Only finite nonempty products of **two** chains, in the equality-plus-\(\triangleleft\) signature and at quantifier rank three, are classified. No statement is proved about additional coordinate projections, expanded order signatures, higher quantifier ranks, or arbitrary finite posets. The table was independently computed but has not been independently audited outside these checks. Relevant older literature not found in searched indexes remains a priority uncertainty.

## References
1. F. Mwesigye and J. K. Truss, *Classification of Finite Coloured Linear Orderings*, Order **28** (2011), 387--397, DOI: 10.1007/s11083-010-9178-9; first publicly available 2010-09-07. Institutional open-access PDF: https://ir.must.ac.ug/bitstreams/ce8f9fc1-8064-4e56-b7ae-a30dd6b401c0/download.
2. M. S. Kurilić, *Model Theory of Products of Chains*, arXiv:2610.24683 (2026), https://arxiv.org/abs/2610.24683; contextual comparison, not an archival priority source.
3. R. Siders, *On quantifier-rank equivalence between linear orders*, Information and Computation **208** (2010), 417--432, DOI: 10.1016/j.ic.2009.11.006; bibliographic/abstract comparison only.
