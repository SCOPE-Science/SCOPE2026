# Universal dyadic short-border rigidity for generalized paperfolding words

## Finding
For every infinite instruction stream \(\varepsilon\in\{0,1\}^{\mathbb N}\), every integer \(k\ge2\), every start position \(t\ge0\), and \(N=2^k\), the length-\(N\) factor \(w=p_t p_{t+1}\cdots p_{t+N-1}\) of the associated generalized paperfolding word has **no proper even border**. Moreover, if it has any proper border, it has one of length \(1\) or \(3\). Thus
\[
 w\text{ is unbordered}\quad\Longleftrightarrow\quad
 w_0\ne w_{N-1}\ \text{and}\ w_0w_1w_2\ne w_{N-3}w_{N-2}w_{N-1}.
\]
Both tests require at most six boundary symbols. Length \(3\) cannot be dropped: for the regular paperfolding word, the factor beginning at position \(3\) has shortest proper border \(3\) at every length \(2^k\ge8\).

## Assumptions and scope
Indices start at zero. For each \(i\ge0\), write \(i+1=2^v(2q+1)\) uniquely with \(v,q\ge0\), and put
\[
 p_i=\varepsilon_v\oplus(q\bmod2),
\]
where \(\oplus\) is addition modulo two. This representation defines a generalized paperfolding word for every instruction stream, including the regular stream \(\varepsilon_v=0\). A border of a finite word \(w\) is an integer \(b\), \(1\le b<|w|\), for which its prefix and suffix of length \(b\) coincide. A word with no proper border is unbordered. The theorem concerns **contiguous factors at lengths that are powers of two**, not all lengths or general automatic words.

## Proof
**Decimation and nonalternation.** From the index definition, for all \(j\ge0\),
\[
 p_{2j}=\varepsilon_0\oplus(j\bmod2),\qquad
 p_{2j+1}=p^{\varepsilon'}_j,
\]
where \(\varepsilon'=(\varepsilon_1,\varepsilon_2,\ldots)\). In particular, letters on even absolute indices alternate. The same is true in every decimated generalized paperfolding word. Hence no contiguous factor of length four can itself alternate: among its four positions, the two even absolute positions are two steps apart and differ, whereas positions two apart in an alternating word agree.

**Even-border exclusion.** We prove by induction on \(k\ge1\) that a length-\(2^k\) factor has no proper border of even length. For \(k=1\) this is vacuous. Suppose a length-\(2^k\) factor has a border of length \(2h\), with \(1\le h<2^{k-1}\) and \(k\ge2\). Comparing the letters in the border at *even absolute indices*, using their forced alternating pattern, shows that the shift \(2^k-2h\) must be a multiple of four. Indeed the induced shift in the even-index lane is \(2^{k-1}-h\), which must be even. As \(2^{k-1}\) is even, \(h\) is even. Comparing the letters at *odd absolute indices* in the same border equality gives a border of length \(h\) in the length-\(2^{k-1}\) factor of the decimated word. This is a proper even border and contradicts induction. Therefore no proper even border exists.

**Long odd-border exclusion.** Suppose a length-\(N\) factor has odd border \(b=2h+1\). The prefix and suffix start at opposite absolute parities, because \(N\) is even and \(b\) is odd. Their equal letters at offsets \(0,2,\ldots,2h\) therefore compare \(h+1\) consecutive letters from an alternating even-index lane with \(h+1\) consecutive letters of the odd-index decimated paperfolding word. If \(h\ge3\), the latter word would contain an alternating factor of length at least four, contradiction. Consequently every odd border has length at most five.

**A five-border forces a one-border.** When the border length equals five, equality at offsets \(0,2,4\) compares one alternating even-index triple with an odd-decimated triple. The alternating triple has equal first and third letters, hence \(w_0=w_4\). Since a border of length five also gives \(w_4=w_{N-1}\), we obtain \(w_0=w_{N-1}\), a border of length one. Together with the even-border exclusion this proves the stated criterion.

**Sharpness.** Take \(\varepsilon_v=0\) for every \(v\). For every multiple \(N\) of eight, the factor beginning at \(t=3\) has first three symbols \(001\) and last three symbols \(001\): these are the symbols at absolute positions \(3,4,5\) and \(N,N+1,N+2\), respectively. Its first symbol is \(0\) and its last is \(1\), so it has no border of length one. By the proved theorem, its shortest border has length three. This proves sharpness at every \(N=2^k\ge8\).

## Verification
The standalone `verify.py` computes generalized paperfolding words directly from the 2-adic index formula and compares the six-symbol rule with exhaustive inspection of every possible proper border. It tests all \(16\) instruction prefixes of length four, completed by zero instructions, for every distinct factor of lengths \(4,8,16,32,64,128\) within prefixes of length \(4096\), and independently checks the claimed sharpness examples through length \(1024\). The program prints `VERIFY_OK` when all finite tests pass. These computations are checks, **not a substitute for the induction** establishing the infinite statement.

## Relationship to prior work
Allouche determined the ordinary factor-complexity function of generalized paperfolding sequences. Goč, Mousavi, and Shallit developed systematic enumeration of unbordered factors in automatic words, including Thue–Morse and period-doubling examples. Neither inspected text asserts the above uniform *shortest-border classification* for generalized paperfolding at all dyadic lengths. The property is not entailed by a formula for total factor complexity, and it is stronger than counting unbordered factors: it determines the boundary certificate for each individual dyadic factor. Holub and Müller classify binary words by unbordered conjugates, a different quantification over rotations of arbitrary finite words.

## Limitations
The theorem gives an exact boundary criterion but does not enumerate the number of distinct unbordered factors at a given length or describe all possible border lengths once a short border is present. It makes no claim for nondyadic lengths. Unindexed equivalent literature remains a possible originality risk. No independent audit was performed.

## References
1. J.-P. Allouche, "The number of factors in a paperfolding sequence," *Bull. Austral. Math. Soc.* 46 (1992), 23–32, DOI: 10.1017/S0004972700011655.
2. D. Goč, H. Mousavi and J. Shallit, "On the number of unbordered factors," arXiv:1211.1301 (2012), LATA 2013, DOI: 10.1007/978-3-642-37064-9_27.
3. Š. Holub and T. Müller, "Unbordered conjugates of words," 2015, arXiv:1504.??? (publication metadata not asserted here).
