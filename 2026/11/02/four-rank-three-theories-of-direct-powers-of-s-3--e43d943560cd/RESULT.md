# Four rank-three theories of direct powers of \(S_3\)

## Finding

For each positive integer \(n\), equip the group \(G_n=S_3^n\) with equality, a constant \(e\), and the ternary relation \(M(a,b,c)\iff ab=c\). At first-order quantifier rank three,
\[
G_m\equiv_3G_n\quad\Longleftrightarrow\quad
(m=n\in\{1,2,3\})\ \lor\ (m,n\ge4).
\]
Hence there are exactly four theories. Their least representatives have orders \(6,36,216,1296\); the final order is sharp.

## Assumptions and scope

The language has no multiplication function or inverse function. Only atomic formulas \(u=v\) and \(M(u,v,w)\) are allowed, where every argument is a selected variable or the named identity. Quantifier rank is the maximum nesting depth of quantifiers. The parameter \(n\) is a positive integer and the group is the full direct Cartesian power (not a symmetric wreath product).

## Proof

**Atomic game invariant.** For an ordered triple of elements \((a,b,c)\), write \(\alpha(a,b,c)\) for the complete truth vector of all six distinct equality atoms between \(e,a,b,c\), followed by the 64 multiplication atoms \(M(u,v,w)\) with \(u,v,w\in\{e,a,b,c\}\). The vector has 70 bits and is exactly the quantifier-free type of the tuple. For any finite group \(H\), recursively put
\[
P_H(a,b)=\{\alpha(a,b,c):c\in H\},\qquad
Q_H(a)=\{P_H(a,b):b\in H\},\qquad
T_H=\{Q_H(a):a\in H\}.
\]
The elementary backward-induction proof of the Ehrenfeucht--Fraisse game states that \(T_H=T_K\) precisely when Duplicator wins the three-move game on \(H,K\): after the first chosen elements, equality of the \(Q\)-sets provides the matching second choice, equality of the \(P\)-sets provides a matching third choice, and the last equality is exactly preservation of every atomic formula. The converse follows by reversing Spoiler's choices at the earliest unequal extension set. This is also an exact recursive definition independent of any algorithm.

**Finite exhaustive certificate.** Represent \(S_3\) as the six permutations of three letters. Its diagonal conjugation action on ordered pairs \((a,b)\in S_3^2\) has exactly eleven orbits; their first coordinates have conjugacy classes distributed \(3,4,4\) among the identity, transposition and three-cycle classes. The standalone `s3_orbit_check.py` constructs all eleven orbits directly from the six permutations. For each orbit representative \((a,b)\) it obtains the six potential atomic masks \(\alpha(a,b,c)\), removing repeated masks. For a pair \((A,B)\in G_n^2\), the coordinates belong to these eleven orbit types, giving a count vector \((t_1,\ldots,t_{11})\) of nonnegative integers summing to \(n\). The quantifier-free mask of a triple in the direct product is the **bitwise conjunction** of its coordinate masks, because every relation (including equality) holds in the direct product exactly when it holds in every coordinate. Taking all possible coordinate masks therefore computes \(P_{G_n}(A,B)\) exactly. All such count vectors are enumerated, without sampling or unproved symmetry assumptions. Grouping them by the three first-coordinate conjugacy-class counts produces every \(Q_{G_n}(A)\) and hence \(T_{G_n}\).

The exact results are:

| \(n\) | \(\lvert T_{G_n}\rvert\) | Canonical SHA-256 of the full \(T_{G_n}\) |
|---:|---:|---|
| 1 | 3 | `45267de14abd9d944ef1ad2d21633515f80645210a8621a49dfab0e3af1c7c6b` |
| 2 | 6 | `602955f8f3b3964a20715dcd05caa551840e11b0b504645f968b73bd405f095e` |
| 3 | 9 | `dabd238d056b1b7f6e91db5ae07dedc07b46f112bd30be9000576c672a8184f6` |
| 4 | 10 | `d05d681b98f5da2d622bbc540068be12e349c60285a9a206a5836e8828fdeb6c` |
| 5 | 10 | `d05d681b98f5da2d622bbc540068be12e349c60285a9a206a5836e8828fdeb6c` |

The hashes summarize exact recursively nested finite sets; the program also directly asserts \(T_{G_4}=T_{G_5}\), not merely equal hashes or equal cardinalities. Since the first four cardinalities differ, these four structures are pairwise non-equivalent at rank three. The independently coded `s3_direct_check.cpp` checks the pointed two-round type counts \(3,6,9\) for \(n=1,2,3\) by directly enumerating all element triples in the full groups, without the eleven-orbit reduction.

**Infinite tail.** If relational structures \(A,B\) are \(q\)-equivalent, then \(A\times C,B\times C\) are \(q\)-equivalent. For a \(q\)-round game, Duplicator plays the known strategy in the first coordinates and copies Spoiler's second coordinate identically. Equalities and each product relation hold coordinatewise, so the induced final correspondence is a partial isomorphism. Iterating this lemma on \(G_4\equiv_3G_5\) gives \(G_{4+k}\equiv_3G_{5+k}\) for every integer \(k\ge0\). Transitivity yields the full infinite equivalence class for all \(n\ge4\). The finite table plus this argument proves every quantifier of the stated claim.

## Verification

Run `python3 s3_orbit_check.py` to reproduce the complete eleven-orbit exhaustive certificate for powers one through five. Run `g++ -O3 -std=c++17 s3_direct_check.cpp -o s3_direct_check` and then execute it to reproduce independent full-group checks for powers one through three. The included output files record successful runs and exact canonical values. All programs use only standard Python/C++ libraries and integer/exact set operations. In particular, no finite enumeration is invoked as an unproved extrapolation to arbitrarily large powers: the tail follows from the proved product-game congruence.

## Relationship to prior work

Gomaa's 2007 dissertation analyzes relational group multiplication and Ehrenfeucht--Fraisse games, primarily for finite cyclic and other abelian groups; its full text (chapter 3, especially pp. 48–53 and 85–91) does not state the present sharp nonabelian direct-power classification. Feferman and Vaught (1959) develop general model-theoretic product reductions; those reductions supply context but no explicit four-class enumeration or least-representative threshold for \(S_3^n\). The proof of product congruence above is given independently. An exact-priority search has not established whether this explicit special-family classification appears in unindexed historical work.

## Limitations

The theorem is only for the relational multiplication language with named identity, not functional multiplication. No assertion is made about quantifier rank four or greater, direct powers of other finite groups, or the elementary theories of arbitrary direct products. Independent mathematical verification has not occurred. Published general product theorems and the inspected abelian-group literature do not themselves certify historical priority of the exact sharp cutoff.

## References

- W. Gomaa, *Model Theory and Complexity Theory*, PhD dissertation, University of Maryland (public repository record 2007-07-06), https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440 ; open PDF https://drum.lib.umd.edu/bitstreams/5a564fe0-5c19-4da2-8ce0-2cc76964e427/download .
- S. Feferman and R. L. Vaught, *The first order properties of products of algebraic systems*, Fundamenta Mathematicae 47 (1959), 57–103, DOI 10.4064/fm-47-1-57-103; publisher record https://www.impan.pl/pl/wydawnictwa/czasopisma-i-serie-wydawnicze/fundamenta-mathematicae/all/pl/wydawnictwa/czasopisma-i-serie-wydawnicze/fundamenta-mathematicae/all/47/1/94418/the-first-order-properties-of-products-of-algebraic-systems .
- Y. Vourtsanis, *A direct proof of the Feferman–Vaught theorem and other preservation theorems in products*, Journal of Symbolic Logic 56 (1991), 632–636, DOI 10.2307/2274705.
