# Two-defect reachability in cyclic defect-one automata

## Finding
Let \(n\ge 3\), let \(Q=\mathbb Z/n\mathbb Z\), and consider the two-letter deterministic automaton in which
\[
a(i)=i+1\pmod n
\]
and the transformation \(b:Q\to Q\) has rank \(n-1\). Let \(e\) be the unique excluded state of \(b\), let \(d\) be its unique duplicated image, and write
\[
\rho=d-e\pmod n.
\]
For distinct \(x,y\in Q\), the target \(Q\setminus\{x,y\}\) is reachable by a word containing exactly two occurrences of \(b\) if and only if at least one of the two oriented differences \(y-x\) and \(x-y\) differs from \(\rho\).

Equivalently, every \((n-2)\)-subset is reachable using exactly two occurrences of \(b\), except in the single parity configuration in which \(n\) is even and \(\rho=n/2\). In that configuration, the only exceptions are the \(n/2\) targets whose two missing states are antipodal. Every target covered by the criterion has a reaching word of the form \(ba^kba^j\) of length at most \(2n\).

Thus, if \(n\) is odd, or if \(n\) is even with \(\rho\ne n/2\), every \((n-2)\)-subset has reaching threshold at most \(2n\), without any assumption of complete reachability or of a coprimality condition on \(\rho\). The uniform constant \(2n\) cannot be improved over this class: the classical Černý family is a special case and is known to attain Don's bound \(2n\) for some \((n-2)\)-subset.

## Assumptions and scope
Words act from left to right on subsets. The symbol \(a^k\) means \(k\) applications of the cyclic letter, with exponents reduced to \(0,1,\ldots,n-1\). Since \(b\) has rank \(n-1\), there is exactly one excluded state \(e\), exactly one duplicated image \(d\), and exactly two states in the kernel class mapping to \(d\). Denote that two-element kernel class by \(K\).

The theorem classifies reachability of \((n-2)\)-subsets by words containing exactly two occurrences of the defect-one letter \(b\). In the exceptional antipodal case it does not assert that the exceptional targets are globally unreachable; it only proves that two occurrences of \(b\) cannot reach them.

The literature-led scope is formal languages and automata theory. The earliest owning source used here was first public on 2020-07-17 and is explicitly classified under MSC \(68Q45\) as primary.

## Proof
Any word containing exactly two occurrences of \(b\) can, for the purpose of acting on \(Q\), be reduced to
\[
ba^kba^j,
\]
with \(0\le k,j<n\), because a leading power of \(a\) fixes the full set \(Q\) setwise and adjacent powers of \(a\) combine modulo \(n\).

After the first \(b\), the image is \(Q\setminus\{e\}\). After the following \(a^k\), the sole missing state is
\[
h=e+k\pmod n.
\]
If \(h\in K\), deleting \(h\) from the domain does not remove the duplicated image \(d\), because its other preimage remains; therefore the second \(b\) still has image size \(n-1\), so a target of size \(n-2\) cannot result.

Suppose instead that \(h\notin K\). Then \(h\) is the unique preimage of \(b(h)\). Applying the second \(b\) therefore removes exactly \(e\) and \(b(h)\) from the image:
\[
(Q\setminus\{h\})b=Q\setminus\{e,b(h)\}.
\]
The final rotation gives the two missing states
\[
\{e+j,\ b(h)+j\}.
\]
Because \(b\) maps \(Q\setminus K\) bijectively onto \(Q\setminus\{e,d\}\), the difference
\[
b(h)-e
\]
runs through every residue except \(0\) and \(\rho=d-e\).

Now fix a desired missing pair \(\{x,y\}\). Choose an orientation \((x,y)\) and put \(\Delta=y-x\pmod n\). If \(\Delta\ne\rho\), then \(e+\Delta\notin\{e,d\}\), so there is a unique \(h\notin K\) such that \(b(h)=e+\Delta\). Choose
\[
k=h-e\pmod n,\qquad j=x-e\pmod n
\]
with representatives in \(0,1,\ldots,n-1\). The word \(ba^kba^j\) then has missing pair
\[
\{e+j,b(h)+j\}=\{x,y\},
\]
and its length is
\[
2+k+j\le 2+2(n-1)=2n.
\]

If \(\Delta=\rho\), reverse the orientation. The reverse orientation also fails exactly when
\[
-\Delta=\rho=\Delta\pmod n.
\]
For a nonzero \(\Delta\), this is equivalent to \(n\) being even and \(\Delta=\rho=n/2\). Hence the only missing pairs excluded from the two-\(b\) construction are the antipodal pairs in this single case. There are exactly \(n/2\) such unordered pairs. This proves both the classification and the \(2n\) bound.

## Verification
The standalone verifier `artifacts/verify_two_defect.py` independently implements the set action, enumerates all normal-form words \(ba^kba^j\), and checks the theorem's predicted classification and explicit witness construction.

It exhaustively checks every rank-\((n-1)\) transformation for \(3\le n\le7\): respectively \(18\), \(144\), \(1200\), \(10800\), and \(105840\) transformations. It also checks 200 deterministic random rank-\((n-1)\) transformations for each \(8\le n\le13\). The output in `artifacts/verification.txt` ends with `VERIFY_OK`. These finite checks are supplementary; the proof above establishes the theorem for every \(n\ge3\).

## Relationship to prior work
Don proved that for a circular automaton with a defect-one letter, if the cyclic displacement from its excluded state to its duplicated state is coprime to \(n\), then every \(k\)-subset is reachable within \(n(n-k)\) letters. The present theorem recovers the \(k=n-2\) bound in that coprime regime but also covers arbitrary non-coprime displacement at codimension two, apart from the explicitly classified antipodal two-occurrence obstruction. For example, it applies when \(n=9\) and \(\rho=3\), where Don's coprimality hypothesis fails.

Hoffmann proved complete reachability after adjoining an arbitrary rank-\((n-1)\) transformation to a primitive permutation group. A group generated only by an \(n\)-cycle is primitive when \(n\) is prime, so that result does not supply the composite-\(n\), arbitrary-displacement statement proved here, nor does it give the two-occurrence classification or the explicit \(2n\) witness.

Casas and Volkov, and later Zhu, study Don-type bounds for standardized binary completely reachable automata. Their hypotheses impose complete reachability and additional structure on the defect-one letter; Zhu's general standardized bound is \(n(n-k)+n-1\). The theorem here is narrower in target size but broader in the local transition hypothesis: it requires only one cycle letter and one arbitrary rank-\((n-1)\) letter, and in the nonexceptional codimension-two case gives \(2n\) rather than \(3n-1\).

Ferens and Szykuła give a general bound of \(2n(n-|S|)-nH_{n-|S|}\) for completely reachable automata, which becomes \(5n/2\) when \(|S|=n-2\). Their discussion also records that the Černý automata meet Don's bound by subset cardinality, furnishing sharpness of the coefficient \(2\) for the nonexceptional class here.

## Limitations
The claim is a structural theorem about two occurrences of the defect-one letter and a corollary for all codimension-two targets in the nonexceptional displacement case. It does not classify shortest reaching words target by target, and in the even antipodal case it does not determine whether the exceptional targets are reachable using three or more occurrences of \(b\).

Originality is asserted only to the best of the literature and database searches performed. The closest older circular and defect-one literature was inspected, including Don's 2016 paper; a differently phrased equivalent statement could still exist in older transformation-semigroup or automata literature.

## References
1. S. Hoffmann, *Completely Reachable Automata, Primitive Groups and the State Complexity of the Set of Synchronizing Words*, arXiv:2007.09104, first submitted 2020-07-17. https://arxiv.org/abs/2007.09104
2. D. Casas and M. V. Volkov, *Don's conjecture for binary completely reachable automata: an approach and its limitations*, arXiv:2311.00077, first submitted 2023-10-31; Journal of Automata, Languages and Combinatorics 29 (2024), 159-175. https://arxiv.org/abs/2311.00077
3. Y. Zhu, *Around Don's conjecture for binary completely reachable automata*, arXiv:2402.19089, first submitted 2024-02-29. https://arxiv.org/abs/2402.19089
4. H. Don, *The Černý Conjecture and 1-Contracting Automata*, Electronic Journal of Combinatorics 23(3) (2016), #P3.12. https://doi.org/10.37236/5616
5. R. Ferens and M. Szykuła, *Recognizing Completely Reachable Automata in Quadratic Time*, ACM Transactions on Algorithms 22(2) (2026), Article 24. https://doi.org/10.1145/3798283
