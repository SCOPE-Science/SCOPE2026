# Two equality types of optimal dimension-four four-server PIR encoders
## Finding
Let \(G\) be a rank-four binary \(4\times 9\) generator matrix, and regard its columns as a multiset in \(\mathbb F_2^4\). A nonzero target \(t\in\mathbb F_2^4\) is **four-recoverable** when there are four pairwise disjoint nonempty sets of column indices whose column sums are all \(t\). We call the column multiset **four-PIR after a change of information basis** when its four-recoverable targets contain a basis of \(\mathbb F_2^4\).

There are exactly \(1120\) such length-nine column multisets with nonzero columns. Under the natural \(\operatorname{GL}(4,2)\) action they form exactly two orbits, of sizes \(280\) and \(840\). Thus, after column permutation and invertible change of information basis, optimal binary dimension-four four-server PIR encoders have exactly two equivalence types.

The size-\(280\) type is projective: all nine columns are distinct, and every one of the \(15\) nonzero vectors of \(\mathbb F_2^4\) is four-recoverable. The size-\(840\) type has exactly eight distinct columns, with one column occurring twice, and exactly \(14\) of the \(15\) nonzero vectors are four-recoverable. The stabilizers in \(\operatorname{GL}(4,2)\) have orders \(72\) and \(24\), respectively.

## Assumptions and scope
The result concerns binary linear PIR encoders of information dimension \(4\) and four mutually disjoint recovery sets per information symbol. Two generator matrices are considered equivalent when one is obtained from the other by a permutation of the nine encoded coordinates and an invertible change of the four-dimensional information basis. This is deliberately a generator-matrix statement: the PIR property depends on the chosen information coordinates, so the invariant formulation is that some information basis consists of four-recoverable targets.

The known exact optimum \(P(4,4)=9\) is used as prior input. Zero columns need not be considered at optimum: deleting a zero column from every recovery set preserves every recovered nonzero target and would produce a length-eight four-PIR encoder, contradicting \(P(4,4)=9\).

## Proof
A standard necessary condition for a binary \(k\)-PIR code is minimum Hamming distance at least \(k\). For a column multiset \(C\subseteq\mathbb F_2^4\), the minimum distance of the generated code is
\[
\min_{0\ne a\in\mathbb F_2^4} |\{c\in C: a\cdot c=1\}|.
\]
There are
\[
inom{15+9-1}{9}=817190
\]
multisets of nine nonzero columns. Exhaustive evaluation of the displayed minimum-distance formula leaves exactly \(1345\) multisets with minimum distance at least \(4\).

For each surviving multiset and each nonzero target \(t\), all \(2^9-1\) nonempty subsets of the nine column positions are evaluated by XOR. The target \(t\) is four-recoverable exactly when four of the subset masks with XOR \(t\) are pairwise disjoint. This predicate was evaluated in two independent ways: direct recursive four-set packing, and an independent pair-of-disjoint-pairs formulation. The two implementations agree for every nonzero target of all \(1345\) distance-qualified multisets.

A multiset admits a four-PIR information basis if and only if its set of four-recoverable nonzero targets has rank \(4\). This yields exactly \(1120\) multisets. Of these, \(280\) have nine distinct columns and \(840\) have eight distinct columns with multiplicity profile \(2,1,1,1,1,1,1,1\). The first group has all \(15\) nonzero targets four-recoverable; every member of the second has exactly \(14\).

Finally, all \(|\operatorname{GL}(4,2)|=20160\) invertible changes of basis are generated and applied to the \(1120\) multisets. They give precisely two orbits, of sizes \(280\) and \(840\). Orbit-stabilizer therefore gives stabilizer orders \(20160/280=72\) and \(20160/840=24\). Together with the known equality \(P(4,4)=9\), this exhausts the optimal encoders.

## Verification
Run `python3 verify_pir44.py`. The program uses only the Python standard library and reconstructs the complete search space rather than reading a precomputed candidate list. Its terminal certificate is:

`VERIFY_OK ambient=817190 d4=1345 basis_flexible=1120 standard_basis=896 projective=280 one_double=840 orbits=280,840 stabilizers=72,24 algorithms_agree=true`

The machine-readable census is in `census.json`; its core-result digest is `7d37b665c341a72d8c252e793661d1627f5cf9a9f48ae422c0451f65bfd7b273`.

Representative column multisets, written as four-bit vectors, are:

- projective type: `0001 0010 0011 0100 0101 1000 1010 1100 1111`;
- one-double-point type: `0001 0001 0010 0100 0110 1000 1010 1101 1111`.

For the second representative the unique non-four-recoverable nonzero target is `0011`; its position changes under basis equivalence.

## Relationship to prior work
Fazeli, Vardy, and Yaakobi introduced binary \(k\)-server PIR codes and the disjoint-recovery-set condition in 2015. Their work supplies the foundational object and constructions/bounds, not an equivalence classification of the present equality layer.

Vajha, Ramkumar, and Kumar later constructed optimal systematic four-server PIR codes from shortened projective Reed-Muller codes. At information dimension \(4\), their construction attains length \(9\), providing a projective optimal example. The present classification shows that this projective construction belongs to one of the two exhaustive equivalence types and that a second, nonprojective type also exists.

Kurz and Yaakobi proved the exact value \(P(4,4)=9\) (Proposition 21 of the 2020 preprint), define projective versus repeated-column generator matrices, and analyze short-block PIR codes by coding-theoretic and integer-programming methods. The inspected full text gives the optimum and constructions but does not state a census or equivalence classification of all length-nine dimension-four four-PIR encoders.

## Limitations
This is a finite classification at the single parameter pair \(s=k=4\). It does not classify longer four-server PIR encoders, higher dimensions, nonlinear encoders, or equivalence under transformations outside coordinate permutation and invertible information-basis change. The originality comparison cannot rule out an obscure unindexed finite census; no such census was found in the inspected foundational, projective-Reed-Muller, short-block, database-oriented, or targeted exact-parameter sources.

## References
1. A. Fazeli, A. Vardy, E. Yaakobi, *PIR with Low Storage Overhead: Coding instead of Replication*, arXiv:1505.06241v1, first public 22 May 2015.
2. M. Vajha, V. Ramkumar, P. V. Kumar, *Binary, Shortened Projective Reed Muller Codes for Coded Private Information Retrieval*, arXiv:1702.05074, 2017.
3. S. Kurz, E. Yaakobi, *PIR Codes with Short Block Length*, arXiv:2001.03433v1, 2020; later Designs, Codes and Cryptography 89 (2021), 559–587.
4. University of Bayreuth repository record for *PIR Codes with Short Block Length*, urn:nbn:de:bvb:703-epub-4578-1; subject classification MSC 68P30.
