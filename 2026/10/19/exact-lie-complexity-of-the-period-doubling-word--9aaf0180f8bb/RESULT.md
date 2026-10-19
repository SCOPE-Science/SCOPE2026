# Exact Lie complexity of the period-doubling word

## Finding

Let \(p=0100010101000100\cdots\) be the period-doubling word, the fixed point beginning in \(0\) of \(\delta(0)=01\) and \(\delta(1)=00\). For a finite word \(u\), write \([u]\) for its distinct cyclic rotations, and let \(\mathcal F_n(p)\) be the set of length-\(n\) contiguous factors of \(p\). Its Lie complexity is
\[
L_p(n)=\#\{[u]:|u|=n,\ [u]\subseteq \mathcal F_n(p)\}.
\]
Then, for every integer \(n\ge1\),
\[
\boxed{L_p(n)=\begin{cases}2,&n=2^k\text{ or }n=3\cdot2^k\text{ for some }k\ge0,\\0,&\text{otherwise}.\end{cases}}
\]
More strongly, the substitution \(\delta\) induces a bijection between the Lie conjugacy classes of lengths \(m\) and \(2m\) for every \(m\ge2\). No odd length \(n\ge5\) admits any Lie conjugacy class.

## Assumptions and scope

All words are binary. Indices of the infinite word start at zero, and a factor means a contiguous block, not a scattered subsequence. A *Lie conjugacy class* must have **every distinct cyclic rotation** occurring as a factor; mere occurrence of one representative is insufficient. The result is an exact statement about the infinite fixed point \(p\), for all positive lengths. The empty-word convention is not part of the claim.

## Proof

**1. Parity and forbidden factors.** From the definition of the length-two substitution,
\[
p_{2j}=0,\qquad p_{2j+1}=1-p_j\quad(j\ge0).
\]
In particular \(11\) cannot occur. Four consecutive zeros would include two zero symbols at consecutive odd absolute indices \(2j+1\) and \(2j+3\), requiring \(p_j=p_{j+1}=1\), so \(0000\) cannot occur either. Also every occurrence of the symbol \(1\) has odd absolute index. Consequently, in any factor all occurrences of \(1\) have positions of a common parity relative to the beginning of that factor.

**2. Odd lengths.** Suppose a conjugacy class of odd length \(n\ge5\) has all its rotations among the factors of \(p\). If a representative has at least two occurrences of \(1\), choose two such positions separated by a (linear) distance \(d\). Since it is a factor, \(d\) is even. Rotating the word so that the second occurrence comes before the first makes their linear distance \(n-d\), which is odd. That rotation cannot be a factor of \(p\), a contradiction. If the representative has at most one occurrence of \(1\), one of its rotations has a block of at least four zeros, likewise impossible. Hence \(L_p(n)=0\) for all odd \(n\ge5\).

**3. Substitution sends Lie classes to Lie classes.** Fix \(m\ge2\). A length-\(m\) factor \(u\) of \(p\) contains a zero, since \(11\) is forbidden. Therefore \(\delta(u)\) contains at least one \(1\), always in an odd relative position. If every rotation of \(u\) is a factor of \(p\), its substitution is a factor because \(p=\delta(p)\). Every even cyclic rotation of \(\delta(u)\) is the substitution of a cyclic rotation of \(u\), and is therefore a factor. Every odd rotation is obtained by shifting one position into that substitution block: the additional final symbol is \(0\), which occurs at the next even absolute index of \(p\). Thus every odd rotation is also a factor. We have a well-defined map \([u]\mapsto[\delta(u)]\) on Lie classes.

**4. Surjectivity.** Let \([w]\) be any Lie class of length \(2m\ge4\). Since \(0000\) is forbidden, \(w\) contains \(1\). In any occurrence all its ones occupy one relative parity. Choose a cyclic rotation with the ones in odd relative positions. This representative begins with zero and has the unique form \(\delta(u)\) for a binary word \(u\) of length \(m\). For every cyclic rotation \(v\) of \(u\), the even rotation \(\delta(v)\) of \(\delta(u)\) is a factor of \(p\). It has a one in an odd relative position, so its occurrence cannot start at an odd absolute index (all even absolute indices of \(p\) contain zero). Hence it starts at an even absolute index and desubstitutes to an occurrence of \(v\) in \(p\). All cyclic rotations of \(u\) occur; thus \([u]\) is a Lie class and \([w]=[\delta(u)]\).

**5. Injectivity.** For length-\(m\) Lie classes with \(m\ge2\), each \(\delta(u)\) contains a one at an odd relative position and no ones at even relative positions. An odd cyclic rotation therefore cannot equal \(\delta(v)\), since it would put all ones in even relative positions. Any conjugacy between \(\delta(u)\) and \(\delta(v)\) is an even rotation, which is exactly a cyclic rotation of \(u\) followed by \(\delta\). Hence \([u]=[v]\). This proves the claimed bijection and
\[
L_p(2m)=L_p(m)\qquad(m\ge2).
\]

**6. Base cases and closed form.** The length-one factors are \(0,1\), giving two classes. The length-two factors are \(00,01,10\), giving \([00]\) and \([01]\). The length-three factors are \(000,001,010,100,101\), giving \([000]\) and \([001]\); no class containing \(11\) is permitted. Thus \(L_p(1)=L_p(2)=L_p(3)=2\). Repeatedly halving every even \(n\ge4\) leaves its odd part. The odd part is \(1\), \(3\), or at least \(5\), and the six preceding steps give the stated formula. \(\square\)

As a direct consequence, the number of positive lengths at most \(N\) having nonzero Lie complexity is exactly
\[
\lfloor\log_2N\rfloor+1+\max\{0,\lfloor\log_2(N/3)\rfloor+1\}.
\]
Thus the support has density zero even though the word itself is aperiodic.

## Verification

The included `verify.py` (standard-library Python 3) constructs period-doubling prefixes in two ways: iterated substitution and the two-adic valuation identity \(p_j\equiv\nu_2(j+1)\pmod 2\). It checks equality of the resulting prefixes, confirms stabilization of factor sets between lengths \(8192\) and \(16384\) for every tested factor length \(1\le n\le200\), enumerates all cyclic classes directly, checks the formula, and separately tests the substitution-induced bijection at every even tested length. Execute `python3 verify.py` in the same directory as this document. These are **finite corroborating checks**, not a replacement for the all-length proof above.

## Relationship to prior work

Bell and Shallit introduced Lie complexity, proved automaticity for automatic words, and gave explicit examples including Thue–Morse and the Fibonacci and Tribonacci words; their paper does not give the period-doubling formula shown here [1]. Li's later extension concerns broader Lie-type complexity measures rather than this explicit fixed-point census [2]. De Luca and Fici determine Lie complexity for Sturmian words, a different word class [3]. Currie analyzes avoidance and desubstitution properties of the period-doubling word, including a parity-based factorization lemma; the parity property is therefore **not** asserted to be new [4]. Cassaigne, Fici, Sciortino, and Zamboni determine the *cyclic complexity* of this word at dyadic lengths [5]. Their cyclic complexity counts classes with **some** factor representative, whereas Lie complexity requires **all** rotations. In particular, the known cyclic count of two at dyadic lengths does not itself establish the new Lie classification at every length.

## Limitations

The claim concerns only the substitution \(0\mapsto01,1\mapsto00\); it does not classify Lie complexity for arbitrary Toeplitz sequences or morphic words. The finite verifier checks through length \(200\), not an infinite domain. The novelty comparison is based on the cited inspected primary literature and targeted searches; obscure or unindexed equivalent results cannot be ruled out. No external independent scientific audit is claimed.

## References

[1] J. P. Bell and J. Shallit, *Lie complexity of words*, arXiv:2102.03821 (first public version 2021-02-07), Theoretical Computer Science (2022). https://arxiv.org/pdf/2102.03821

[2] S. Li, *A note on the Lie complexity and beyond*, arXiv:2207.05859 (2022-07-12). https://arxiv.org/pdf/2207.05859

[3] A. De Luca and G. Fici, *On the Lie complexity of Sturmian words*, arXiv:2206.00995 (first public version 2022-06-02). https://arxiv.org/pdf/2206.00995

[4] J. D. Currie, *The Analog of Overlap-Freeness for the Period-Doubling Sequence*, Journal of Integer Sequences 26 (2023), Article 23.8.2. https://cs.uwaterloo.ca/journals/JIS/VOL26/Currie/currie16.pdf

[5] J. Cassaigne, G. Fici, M. Sciortino and L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843 (first public version 2014-02-24), Journal of Combinatorial Theory Series A. https://arxiv.org/pdf/1402.5843
