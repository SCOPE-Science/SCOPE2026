# Exact Lie complexity of the period-doubling word
## Finding
Let
\[
\delta(0)=01,\qquad \delta(1)=00,
\]
and let
\[
\mathbf d=\delta^\omega(0)
\]
be the period-doubling word. For an integer \(n\ge1\), let \(L_{\mathbf d}(n)\) be its Lie complexity: the number of cyclic-conjugacy classes of length-\(n\) factors whose every cyclic shift is again a factor of \(\mathbf d\).

Then
\[
L_{\mathbf d}(n)=
\begin{cases}
2,& n=2^k\text{ or }n=3\cdot2^k\text{ for some }k\ge0,\\
0,&\text{otherwise}.
\end{cases}
\]

More precisely, the two classes are completely explicit. At length \(2^k\) they are
\[
[\delta^k(0)]_C,\qquad [\delta^k(1)]_C,
\]
and at length \(3\cdot2^k\) they are
\[
[\delta^k(000)]_C,\qquad [\delta^k(001)]_C.
\]

The key structural identity is the exact doubling law
\[
L_{\mathbf d}(2m)=L_{\mathbf d}(m)
\qquad(m\ge1).
\]
Together with the odd-length classification
\[
L_{\mathbf d}(1)=L_{\mathbf d}(3)=2,\qquad
L_{\mathbf d}(m)=0\quad(m\ge5\text{ odd}),
\]
this gives the formula.

## Assumptions and scope
A cyclic conjugate of a word \(u=u_0u_1\cdots u_{n-1}\) is any cyclic shift
\[
u_tu_{t+1}\cdots u_{n-1}u_0\cdots u_{t-1}.
\]
The notation \([u]_C\) denotes its cyclic-conjugacy class.

The period-doubling word is indexed from \(0\). Since every image under \(\delta\) starts with \(0\),
\[
d_{2j}=0
\]
for every \(j\ge0\). Hence every occurrence of \(1\) in \(\mathbf d\) lies at an odd global position.

The theorem concerns ordinary Lie complexity introduced by Bell and Shallit. It does not concern cyclic complexity, which counts a conjugacy class when at least one representative occurs rather than requiring every representative to occur.

## Proof
We first record two elementary properties of \(\mathbf d\). Since \(d_{2j}=0\), no adjacent pair can be \(11\). Also \(\mathbf d\) has no factor \(0000\). Indeed, if four zeros begin at either \(2j\) or \(2j+1\), then the two odd positions among them are \(2j+1\) and \(2j+3\). From
\[
\delta(0)=01,\qquad\delta(1)=00,
\]
having zeros at both odd positions forces
\[
d_j=d_{j+1}=1,
\]
contradicting the absence of \(11\).

We now prove the doubling law. Suppose first that a length-\(2m\) conjugacy class \(C\) is counted by Lie complexity.

For \(m=1\), the claim can be checked directly, so assume \(m\ge2\). Choose \(y\in C\). Because \(y\) is a factor of \(\mathbf d\), all occurrences of \(1\) in \(y\) have the same parity relative to the beginning of \(y\). Rotating once if necessary, choose a representative \(x\in C\) whose \(1\)'s occur only in odd positions. Then every even position of \(x\) is \(0\), so there is a unique binary word \(u\) of length \(m\) such that
\[
x=\delta(u).
\]

Because \(2m\ge4\) and \(\mathbf d\) contains no \(0000\), the word \(x\) is not all zeros. Thus \(u\) contains at least one \(0\), and so every conjugate \(v\) of \(u\) has \(\delta(v)\) containing a \(1\).

For each conjugate \(v\) of \(u\), the word \(\delta(v)\) is an even cyclic shift of \(x\), hence is a factor of \(\mathbf d\). Any occurrence of \(\delta(v)\) must start at an even global position: its \(1\)'s lie at odd positions relative to its start, while all \(1\)'s of \(\mathbf d\) lie at odd global positions. Since
\[
\mathbf d=\delta(\mathbf d),
\]
an occurrence aligned at an even position desubstitutes to an occurrence of \(v\) in \(\mathbf d\). Therefore every conjugate of \(u\) is a factor, so \([u]_C\) is counted at length \(m\).

Conversely, suppose every conjugate of a length-\(m\) word \(u\) occurs in \(\mathbf d\). Every even cyclic shift of \(\delta(u)\) has the form
\[
\delta(v)
\]
for a conjugate \(v\) of \(u\), and hence occurs in \(\delta(\mathbf d)=\mathbf d\).

Every odd cyclic shift also occurs. If \(v\) occurs in \(\mathbf d\) beginning at position \(j\), then the length-\(2m\) factor beginning at position \(2j+1\) is
\[
\delta(v)[1\,..\,2m-1]\,0.
\]
Because the first symbol of every \(\delta\)-image is \(0\), this is exactly the one-step cyclic shift of \(\delta(v)\). Hence all cyclic shifts of \(\delta(u)\) occur.

The induced map on Lie classes is injective. If \(\delta(u)\) and \(\delta(v)\) are related by an even cyclic shift, then \(u\) and \(v\) are conjugate. If they are related by an odd cyclic shift, then the shifted word can have zeros in every even position only if \(\delta(u)\) also has zeros in every odd position. Thus \(\delta(u)\) is all zeros, so \(u\) is a power of \(1\). For \(m\ge2\) this cannot be a factor of \(\mathbf d\), because \(11\) does not occur. The case \(m=1\) is direct. Therefore
\[
L_{\mathbf d}(2m)=L_{\mathbf d}(m).
\]

It remains to classify odd lengths. At length \(1\), both letters occur, so
\[
L_{\mathbf d}(1)=2.
\]
At length \(3\), the classes
\[
[000]_C
\quad\text{and}\quad
[001]_C=\{001,010,100\}
\]
are present. The prefix
\[
010001
\]
already exhibits \(010,100,000,001\), so
\[
L_{\mathbf d}(3)=2.
\]
No other length-\(3\) class can qualify because any class containing a word with \(11\) is excluded.

Now let \(n\ge5\) be odd and suppose, for contradiction, that a length-\(n\) class is counted. A representative \(w\) cannot contain no \(1\), because then it contains \(0000\). It cannot contain exactly one \(1\), because some cyclic shift then contains at least four consecutive zeros. Thus \(w\) contains at least two \(1\)'s.

All \(1\)'s of \(w\), as a factor of \(\mathbf d\), have the same relative parity. Choose a cyclic cut with at least one \(1\) on each side. Under the corresponding rotation, the \(1\)'s on one side shift without wraparound, while those on the other side acquire an additional displacement of \(n\). Since \(n\) is odd, the two groups acquire opposite parities. The rotated word therefore has \(1\)'s in both parity classes, which is impossible for a factor of \(\mathbf d\). This contradiction proves
\[
L_{\mathbf d}(n)=0
\qquad(n\ge5\text{ odd}).
\]

Repeatedly dividing an arbitrary \(n\) by \(2\) now reduces to its odd part. The only odd parts with nonzero Lie complexity are \(1\) and \(3\). The explicit classes follow by iterating the class map
\[
[u]_C\longmapsto[\delta(u)]_C.
\]

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier independently generates the period-doubling word from the morphism. For every length through \(192\), it computes the complete factor set seen in a prefix of length \(2^{15}\) and confirms that it is already identical in a prefix of length \(2^{14}\).

For each tested length, it enumerates cyclic-conjugacy classes directly and checks that the only accepted classes are exactly the two morphic families stated in the theorem. It separately checks
\[
L_{\mathbf d}(2m)=L_{\mathbf d}(m)
\]
through \(m=96\), as well as the base classes at lengths \(1\) and \(3\), and the structural exclusions \(11\) and \(0000\).

The finite computation is regression evidence. The theorem for all lengths follows from the parity and desubstitution proof above, not from extrapolation.

## Relationship to prior work
Bell and Shallit introduced Lie complexity and proved that the Lie-complexity sequence of every automatic word is automatic. Their examples give exact formulas for the Thue--Morse word, its ternary squarefree variant, the Cantor word, the Fibonacci word, and the Tribonacci word. The period-doubling word is not among the examples in the inspected paper.

The support of the Thue--Morse formula in that paper is closely related: its nonzero lengths also lie on dyadic families involving \(2^k\) and \(3\cdot2^k\), but the values and qualifying classes are different. The present proof is a direct morphic classification for the period-doubling language.

Li later developed extended and prefix versions of Lie complexity and proved further automaticity results. The inspected paper discusses the Thue--Morse word as its concrete automatic example and does not give a period-doubling Lie-complexity formula.

Cassaigne, Fici, Sciortino, and Zamboni study the older cyclic complexity. They explicitly discuss the period-doubling word, but cyclic complexity counts a conjugacy class when some representative occurs. Lie complexity imposes the strictly different requirement that every representative occur. Their period-doubling result therefore does not determine the function proved here.

## Limitations
The argument uses the particularly rigid length-\(2\) substitution
\[
0\mapsto01,\qquad1\mapsto00.
\]
No corresponding formula is claimed for generalized period-doubling words or arbitrary Toeplitz words.

The theorem determines ordinary Lie complexity and the qualifying conjugacy classes. It does not compute the extended or prefix Lie-complexity functions.

The proof is language-specific; it does not provide a general algorithm replacing the automatic-sequence method of Bell and Shallit.

## References
1. J. P. Bell and J. Shallit, “Lie complexity of words,” arXiv:2102.03821v1, first public 2021-02-07; *Theoretical Computer Science* 927 (2022), 45–59, DOI 10.1016/j.tcs.2022.06.001.
2. S. Li, “A note on the Lie complexity and beyond,” arXiv:2207.05859v1, first public 2022-07-12; *Theoretical Computer Science* 986 (2024), 114343, DOI 10.1016/j.tcs.2023.114343.
3. J. Cassaigne, G. Fici, M. Sciortino, and L. Q. Zamboni, “Cyclic Complexity of Words,” arXiv:1402.5843; *Journal of Combinatorial Theory, Series A* 145 (2017), 36–56.
