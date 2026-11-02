# Exact two-tortoise complexity of the Thue–Morse word from length eighteen

## Finding

Let \(\mathbf t=011010011001\cdots\) be the fixed point beginning in \(0\) of the binary substitution \(\mu(0)=01\), \(\mu(1)=10\). For a binary finite word \(w\), let \(T(w)\) remove its first occurrence of \(1\) and append a \(1\), fixing a word having no \(1\). Write \(F_n=\operatorname{Fact}_n(\mathbf t)\), \(p(n)=|F_n|\), and
\[
D_j(n)=p(n)-|\{T^j(w):w\in F_n\}|\qquad(j=1,2).
\]
**Theorem.** For every integer \(n\ge18\),
\[
\boxed{D_2(n)=D_1(n)+D_1(n-2).}
\]
In particular, defining for integers \(m\ge10\)
\[
\delta(m)=\begin{cases}4,&\text{the binary representation of }m-3\text{ starts with }10,\\2,&\text{it starts with }11,\end{cases}
\]
one has the explicit formula
\[
\boxed{|\{T^2(w):w\in F_n\}|=p(n)-\delta(n)-\delta(n-2)\quad(n\ge18).}
\]
Thus the deficit is always one of \(4,6,8\). The threshold \(18\) is sharp for this identity: \(D_2(17)=5\), while \(D_1(17)+D_1(15)=4\).

## Assumptions and scope

All words are finite binary factors of the one-sided infinite Thue–Morse fixed point; factors are distinct *words*, not indexed occurrences. A \(j\)-tortoise class consists of factors with equal images under \(T^j\). A factor \(y\) is *left special* if both \(0y\) and \(1y\) are factors. The theorem is for every integer length \(n\ge18\), not merely a finite prefix or an experimental range. The formula for \(\delta\) uses the established one-step result in Campbell–Rampersad, Theorem 6; no new claim of priority is made for that one-step result.

## Proof

**1. Exact finite boundary and propagation.** For any \(k\ge0\), every factor of length at most \(2^k\) is contained in \(\mu^k(ab)\) for some \(ab\in\{00,01,10,11\}\): the fixed point decomposes into consecutive length-\(2^k\) substituted blocks, all four adjacent pairs occur, and a factor of length at most one block crosses at most two blocks. For length \(18\), use \(k=5\). Exact enumeration gives \(|F_{18}|=52\) and precisely four nontrivial two-tortoise fibres, each a pair:

```text
011001011001101001  /  101001011001101001
010110100110010110  /  100110100110010110
011010010110011010  /  100110010110011010
011001101001100101  /  100101101001100101
```

The first two pairs have the form \(\{01z,10z\}\). The last two have the form \(\{0110y,1001y\}\). The accompanying standalone checker constructs all \(52\) factors from the four substituted block pairs and verifies exactly this complete list; it also checks that neither alternating word \(01010\) nor \(10101\) occurs in \(\mathbf t\).

Every length-\(18\) factor has at least two \(1\)'s. For \(n\ge18\), if two length-\(n\) words have the same \(T^2\)-image, deleting their first two \(1\)'s yields the same length-\((n-2)\) word. Their length-\(18\) prefixes then have the same \(T^2\)-image: deleting the first two \(1\)'s in either prefix gives exactly the first \(16\) symbols of the common deleted word. Equal length-\(18\) prefixes would also force the original length-\(n\) words to be equal. Accordingly, every nontrivial fibre for \(n\ge18\) is a pair, and each such pair extends one of the four displayed pairs. Equality of the deleted words forces the appended suffixes to agree. Therefore every nontrivial pair has exactly one of the two forms
\[
\{01z,10z\}\qquad\text{or}\qquad\{0110y,1001y\}.
\]
The two families cannot coincide, and no two different pairs have a common image, by the complete length-\(18\) fibre list and prefix inheritance.

**2. The left-special lifting lemma.** We establish that for every left-special factor \(y\) of length at least \(14\), both \(0110y\) and \(1001y\) are factors. First, consider any left-special factor \(v\) of length at least \(5\). Since neither \(01010\) nor \(10101\) occurs, \(v\) contains \(00\) or \(11\). In the decomposition \(\mathbf t=\mu(\mathbf t)\), equal adjacent letters occur only across substitution-block boundaries, i.e. at odd global positions (starting at zero). Hence every occurrence of \(v\) has the same starting parity. That parity cannot be odd: at an odd position the immediately preceding symbol is forced to be the complement of the first symbol of \(v\), contradicting left specialness. Thus all occurrences of \(v\) start at even positions. Since both \(0v\) and \(1v\) occur, their immediately preceding two-letter substitution blocks are respectively \(10\) and \(01\); therefore both \(10v\) and \(01v\) occur. Recurrence of the fixed point ensures the needed occurrences away from the initial boundary.

Now let \(y\) be left special with length \(L\ge14\). Its occurrences start at even positions. Reading the aligned substitution blocks, there is a unique source factor \(v\) of length \(\lceil L/2\rceil\) such that \(y\) is the length-\(L\) prefix of \(\mu(v)\). The uniqueness also holds for odd \(L\), since the first symbol of the last incomplete block determines its source symbol. The occurrences of \(0y\) and \(1y\) give opposite immediately preceding source symbols, so \(v\) is left special. Since \(|v|\ge7\), the preceding paragraph implies that both \(01v\) and \(10v\) occur. Substituting these factors gives \(0110\mu(v)\) and \(1001\mu(v)\). Taking their first \(L+4\) symbols yields both \(0110y\) and \(1001y\), as claimed.

Conversely, if \(0110y\) and \(1001y\) occur, deleting their first two symbols shows that both \(10y\) and \(01y\) occur, whence \(y\) is left special. Consequently the new, non-one-tortoise pairs \(\{0110y,1001y\}\) are in bijection with the left-special factors of length \(n-4\). Indeed they have the common two-tortoise image \(00y11\), and they are not one-tortoise-equivalent.

**3. Count the two strata.** Campbell–Rampersad, Theorem 4, proves that for \(n\ge10\) the nontrivial one-tortoise classes are precisely pairs \(\{01z,10z\}\), with \(z\) left special of length \(n-2\); the preceding parity argument also establishes existence for every such \(z\) here. Let \(s(m)\) be the number of left-special length-\(m\) Thue–Morse factors. The directly inherited first stratum therefore consists of \(s(n-2)=D_1(n)\) two-tortoise pairs. The new stratum consists of \(s(n-4)=D_1(n-2)\) pairs, by the lifting lemma and the same one-tortoise classification at length \(n-2\). Since every nontrivial two-tortoise fibre has two members and the strata are disjoint, the total number of lost classes is their sum. This proves the claimed identity for **every** \(n\ge18\). The published Theorem 6 evaluates \(D_1(m)=\delta(m)\) for \(m\ge10\), giving the digit formula.

**4. Sharpness.** The same exhaustive substituted-block factor construction at length \(17\) gives \(D_2(17)=5\), \(D_1(17)=2\), and \(D_1(15)=2\). Hence the stated identity fails at length \(17\); its all-length threshold cannot be lowered.

## Verification

Run `python3 thue_second_verifier.py` with Python 3 and no third-party dependencies. The verifier regenerates the *entire* length-\(18\) factor set from \(\mu^5(ab)\), checks all four collision pairs and the two forbidden alternating factors, independently verifies failure at length \(17\), and checks every length from \(18\) through \(512\) by exhaustive morphic-block enumeration against both the one-step and two-step digit formulas. Its successful marker is `TM_TWO_TORTOISE_VERIFY_OK`. For the \(495\) tested lengths the deficits \(4,6,8\) occur \(237,20,238\) times, respectively. The proof of **unbounded** lengths is the prefix-inheritance and parity/desubstitution argument above; the finite test is not substituted for that proof.

## Relationship to prior work

The tortoise map on words was introduced by Defant–Kravitz, *Stack-sorting for words* (2018 preprint, 2020 journal). Campbell–Rampersad, *Subword enumeration up to stack-sorting equivalence* (first publicly available April 28, 2026), introduces the fixed-iterate complexity and proves the one-tortoise Thue–Morse formula in Theorems 4–6; its conclusion suggests exploring higher iterates but does not state the two-tortoise convolution identity, four-pair classification, or sharp threshold \(18\). The established maximum size \(2\) of a two-tortoise fibre for large Thue–Morse factors determines no number of such fibres; it is strictly weaker than the exact deficit formula here. Distinct notions such as reduced factor complexity, abelian and binomial complexity, and the unrelated Thue–Morse transform do not imply this claim from their definitions or published statements.

## Limitations

The theorem only concerns the standard binary Thue–Morse fixed point and exactly two tortoise passes. It does not establish formulas for three or more passes or for other automatic words. The proof uses a complete, reproducible *finite* factor check at length \(18\) plus a new symbolic extension argument; further independent formalization of the symbolic argument has not been performed. A prior equivalent formulation not located in the accessible literature remains a publication-priority risk.

## References

1. J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811v1 (April 28, 2026); inspected updated arXiv:2604.25811v2 (October 5, 2026), especially Sections 3, 4, 6 and Theorems 4–6. https://arxiv.org/html/2604.25811v2
2. C. Defant and N. Kravitz, *Stack-sorting for words*, arXiv:1809.09158 (2018), Australasian Journal of Combinatorics 77 (2020), 51–68. https://arxiv.org/abs/1809.09158
3. A. de Luca and S. Varricchio, *Some combinatorial properties of the Thue-Morse sequence and a problem in semigroups*, Theoretical Computer Science 63 (1989), 333–348; left-special factor counts as quoted and used in Campbell–Rampersad.
