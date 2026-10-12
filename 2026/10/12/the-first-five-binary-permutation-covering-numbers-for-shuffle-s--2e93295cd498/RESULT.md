# The first five binary permutation-covering numbers for shuffle squares

## Finding
For each integer \(2\le n\le6\), let \(m_2(n)\) be the minimum number of coordinate permutations needed so that every even binary word of length \(2n\) splits into two complementary length-\(n\) subsequences related by at least one permutation in the chosen set. Then
\[
\bigl(m_2(2),m_2(3),m_2(4),m_2(5),m_2(6)\bigr)=(2,2,3,3,4).
\]
In particular, \(n=6\) is the first order in the stated range requiring four permutations, and the established cyclic-permutation upper bound is attained at every order \(2\le n\le6\).

## Assumptions and scope
Let \(\Sigma=\{0,1\}\). A word \(W\in\Sigma^{2n}\) is **even** when both letters have even multiplicities; equivalently its number of ones is even. A partition of its positions into two increasing subsequences of \(n\) positions each gives two length-\(n\) words \(U,V\). A permutation \(\pi\in S_n\) acts by \((\pi U)_i=U_{\pi(i)}\). We call \(W\) a shuffle \(\pi\)-square if such a partition yields \(V=\pi U\). Reversing the two subsequences gives the inverse permutation, so both orientations are included in the definition.

For \(C\subseteq S_n\), say \(C\) **covers** the even binary words of length \(2n\) if every such word is a shuffle \(\pi\)-square for some \(\pi\in C\); \(m_2(n)\) is the minimum size of a covering set. The statement concerns all binary even words at the five specified lengths and all permutations, not merely cyclic permutations. The checking program uses zero-based rather than one-based position indices.

## Proof
**Finite upper certificates.** For each \(n\in\{2,3,4,5,6\}\), choose the \(\lfloor n/2\rfloor+1\) cyclic permutations
\[
\pi_k(i)=1+((i-1+k)\bmod n),\qquad 0\le k\le\lfloor n/2\rfloor.
\]
The verifier enumerates every binary word of length \(2n\) with an even number of ones, every applicable \(\pi_k\), and every partition into two ordered length-\(n\) subsequences. It verifies that at least one ordered partition realizes \(V=\pi_k U\). The exact sizes of these complete word sets are \(8,32,128,512,2048\), respectively. Thus \(m_2(n)\le2,2,3,3,4\) for these five orders. This enumeration is also consistent with the general cyclic upper bound established in the cited 2023 paper; the proof here checks the concrete small-order certificates directly.

**Lower certificates at orders two through five.** For a permutation \(\pi\), form the bit vector indicating which even words it covers, with all words in lexicographic order. Exhausting all \(n!\) permutations and all ordered complementary subsequence partitions gives the maximum single-permutation coverage of \(6\) out of \(8\) words for \(n=2\), and \(28\) out of \(32\) for \(n=3\). For \(n=4\) the greatest coverage of the union of any two permutation neighborhoods is \(126\) out of \(128\) words; for \(n=5\) it is \(496\) out of \(512\). Hence one permutation is insufficient in the first two cases and two are insufficient in the next two cases.

**Nine-word obstruction at order six.** Consider the following nine even binary words of length twelve:

```
000000111111
011111100000
000011111100
000111111000
001111100001
000111110001
001110000001
000000111001
011110000110
```

For each of the \(720\) permutations of six positions, record the nine-bit signature marking exactly which of these words admit a complementary subsequence partition related by that permutation. Exhausting the \(\binom{12}{6}=924\) partitions for each word produces exactly \(73\) distinct signatures. Let \(F(T)\) be true if some signature contains every index in a subset \(T\) of the nine words. The verifier constructs all \(512\) values of \(F\) by downward subset propagation and checks, for every pair of the \(73\) signatures \(A,B\), that
\[
F\bigl(\{1,\ldots,9\}\setminus(A\cup B)\bigr)=\mathrm{false}.
\]
Thus no three permutations, even chosen freely from the full symmetric group, cover these nine words. In particular no three cover all \(2048\) even binary words of length twelve. Hence \(m_2(6)\ge4\), completing the claimed five exact values.

The exhaustive steps are finite and exhaustive because every word, permutation, and complementary position partition in their respective finite ranges is generated explicitly. No inference from a proper subsample is made: the nine-word subset is used only to prove a lower bound, for which a subset obstruction is sufficient.

## Verification
The self-contained Python 3 checker `verify.py` uses only the standard library. Run `python3 verify.py` from the directory containing this file and the checker, without disabling assertions. It independently checks the upper certificates by direct search over position partitions, and generates the lower certificates from pair-of-subsequences compatibility masks. The nine-word lower certificate is validated using exhaustive nine-bit superset dynamic programming; no integer optimizer, external package, heuristic or database is required. A successful invocation prints:

```
VERIFY_OK m2(2..6)=2,2,3,3,4 upper-even=8,32,128,512,2048 n6_obstructions=9 n6_signatures=73 max_pair_n4=126 max_pair_n5=496
```

## Relationship to prior work
Grytczuk, Pawlik and Pleszczyński introduced the minimum permutation-covering number \(m_k(n)\) in Section 2.4 of *Variations on shuffle squares* (arXiv:2308.13882). Their Theorem 2 gives a cyclic-permutation covering upper bound for binary even words, reduced using inverse permutations; Proposition 2 reports \(m_2(2)=2\) alongside values for different alphabets. Neither result establishes the binary exact values for \(n=3,4,5,6\). The new lower certificates establish sharpness for this initial range without imposing cyclicity on candidate optimal covers.

The later *Shuffle squares and ordered nest-free graphs* (arXiv:2503.22043v2) treats existence of **identical** shuffled subsequences, run-pattern criteria, and cutting/deletion distances. It does not state the minimum size of a family of arbitrary coordinate permutations covering every even binary word; these are distinct predicates even though the underlying word class is shared.

## Limitations
The theorem is an exact finite classification for \(2\le n\le6\), not a proof that the cyclic upper bound is always optimal. Nothing here determines \(m_2(n)\) for \(n\ge7\), larger alphabets, or unrestricted word transformations. The verification is executable and exhaustively finite, but independent mathematical audit has not been performed. Published or unindexed equivalent results may exist beyond the sources compared.

## References
1. J. Grytczuk, B. Pawlik and M. Pleszczyński, *Variations on shuffle squares*, arXiv:2308.13882 (first submitted 2023-08-26), especially Theorem 2 and Section 2.4. https://arxiv.org/abs/2308.13882
2. J. Grytczuk, B. Pawlik and A. Ruciński, *Shuffle squares and ordered nest-free graphs*, arXiv:2503.22043v2, especially Sections 1, 3 and 6. https://arxiv.org/abs/2503.22043
