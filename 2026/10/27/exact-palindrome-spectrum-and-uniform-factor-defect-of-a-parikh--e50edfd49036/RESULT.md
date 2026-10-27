# Exact palindrome spectrum and uniform factor defect of a Parikh-collinear word

## Finding
Let \(f\) be the binary morphism \(f(0)=010011\), \(f(1)=1001\), and let \(w=f^{\omega}(0)\) be its infinite fixed point. A palindrome is a contiguous factor equal to its reversal. Write \(P_w(n)\) for the number of **distinct** palindromic factors of length \(n\), with \(n\geq 1\).

The complete palindromic-complexity spectrum is
\[
(P_w(1),\ldots,P_w(25))=(2,2,3,2,2,2,2,2,2,2,2,1,3,0,2,0,2,0,2,0,2,0,2,0,0),
\qquad P_w(n)=0\quad(n\geq 26).
\]
Thus \(w\) has exactly **37 distinct nonempty palindromic factors** and its maximum palindrome length is exactly **23**. The two palindromes of length 23 are `01100101001110010100110` and `10100111001010011100101`.

For any finite word \(v\), let \(D(v)=|v|+1-\#\operatorname{Pal}(v)\), where \(\operatorname{Pal}(v)\) contains its distinct palindromic factors, including the empty word. **Every contiguous factor** \(v\) of \(w\) with \(|v|\geq 1249\) has exactly the same 37 nonempty palindromes, and therefore
\[
D(v)=|v|-37 \qquad (|v|\geq1249).
\]
The cutoff 1249 is sufficient, not asserted to be least.

## Assumptions and scope
The alphabet is the fixed binary alphabet \(\{0,1\}\). All factors are contiguous and counted by distinct word value rather than occurrence; the empty palindrome is excluded from \(P_w(n)\) for \(n\geq1\) but included in the definition of defect. The result concerns this particular nonuniform, Parikh-collinear morphism, not all such morphisms. Positions begin at zero. Every assertion about factors or palindromes is for the entire infinite fixed point, not for one finite prefix.

## Proof
**1. A derived uniform presentation.** Define a five-uniform morphism \(g\) on \(\{0,1,2,3,4,5\}\) by
\[
\begin{aligned}
g(0)&=01023,&g(1)&=14501,&g(2)&=10102,\\
g(3)&=31450,&g(4)&=45010,&g(5)&=10231,
\end{aligned}
\]
and the coding \(\tau(0)=\tau(2)=\tau(5)=0\), \(\tau(1)=\tau(3)=\tau(4)=1\). We first justify the identity \(w=\tau(g^{\omega}(0))\), rather than assuming that finite-prefix agreement proves it.

For each binary letter \(a\), introduce states \((a,i)\), with \(0\leq i<|f(a)|\). Form the state word \(H(a)\) by replacing, for each letter \(b\) of \(f(a)\), its occurrence with the decorated sequence \((b,0)(b,1)\cdots(b,|f(b)|-1)\). Since both \(f(0)\) and \(f(1)\) contain equally many zeros and ones, \(|H(a)|=5|f(a)|\). Let \(\theta(a,i)\) be the \(i\)-th consecutive length-five block of \(H(a)\). This is a ten-state five-uniform morphism; its fixed point starting at \((0,0)\) is the position-decorated form of \(w=f(w)\).

Map the ten states to six states as follows:

| State | \((0,0)\) | \((0,1)\) | \((0,2)\) | \((0,3)\) | \((0,4)\) | \((0,5)\) | \((1,0)\) | \((1,1)\) | \((1,2)\) | \((1,3)\) |
|---|---|---|---|---|---|---|---|---|---|---|
| Image | 0 | 1 | 0 | 2 | 3 | 1 | 4 | 5 | 0 | 1 |

Call this map \(q\). Direct substitution of the ten finite state images gives \(q\theta=gq\) and \(\tau(q(a,i))=f(a)[i]\) for every state. Consequently \(\tau(g^{\omega}(0))=f^{\omega}(0)\). The standalone verifier checks all ten identities explicitly, and the six-state presentation agrees with the one given by Rigo, Stipulanti, and Whiteland.

**2. Exact length-two state language.** From \(g(0)=01023\), the adjacent state pairs are initially `01`, `10`, `02`, `23`. Substituting once yields
\[
B=\{01,02,10,14,23,31,45,50\}.
\]
Every pair in \(B\) appears in \(g^2(0)\); scanning each \(g(x)g(y)\) for \(xy\in B\) shows that every adjacent pair of such an image again lies in \(B\). Induction shows that \(B\) is **exactly** the set of adjacent pairs in \(g^{\omega}(0)\).

**3. Exhaustive local characterization of infinite factors.** Since \(g^2\) has uniform block length 25, any factor of length \(1\leq n\leq25\) in \(\tau(g^{\omega}(0))\) lies inside two consecutive projected blocks. Their underlying letters form a pair \(xy\in B\). Conversely, every pair in \(B\) actually occurs. Hence there is the exact identity
\[
\operatorname{Fac}_n(w)=\bigcup_{xy\in B}\operatorname{Fac}_n\bigl(\tau(g^2(xy))\bigr),
\qquad 1\leq n\leq25.
\]
This is a finite identity **for factors of the entire infinite word**. Each of the eight words on the right has length 50. Literal comparison with reversal in these explicitly determined words produces the displayed 25-entry spectrum. As independent checks, the full factor sets have size 78 at length 24 and 81 at length 25, but neither set contains a palindrome. At length 23 the two displayed witnesses occur, respectively, at offset 24 of \(\tau(g^2(02))\) and offset 14 of \(\tau(g^2(10))\). A palindrome of length at least 26 contains, at its center, a palindrome of length 24 if even, or of length 25 if odd. Thus no longer palindromes exist. Summing the 25 counts gives 37.

**4. Uniform saturation in every long factor.** For each of the six letters \(a\), direct inspection shows that \(g^2(a)\) contains every pair in \(B\). Therefore \(g^4(a)=g^2(g^2(a))\) contains every \(g^2(xy)\), \(xy\in B\), as a contiguous subword. Consequently each 625-symbol block \(\tau(g^4(a))\) contains *all* 37 palindromes of \(w\), with none additional possible. Since \(w=\tau(g^4(g^{\omega}(0)))\) is partitioned into consecutive such 625-symbol blocks, any factor of length at least \(2\cdot625-1=1249\) contains a complete aligned block. Every such factor therefore has exactly 37 distinct nonempty palindromic factors. The definition of \(D\) now gives \(D(v)=|v|-37\).

## Verification
Run `python3 verify.py` using the Python 3 standard library. It reconstructs the ten-state positional lift and verifies the commuting map; obtains and closes the exact eight-pair state language; computes all binary factors of length at most 25 from the eight projected 50-letter pair blocks; verifies the full palindrome spectrum, the two 23-letter witnesses, and the 24/25 obstructions; and independently compares the resulting factor sets with a prefix generated using the original nonuniform morphism. It also verifies that each of the six 625-letter blocks contains all 37 palindromes. The essential infinite quantifiers are justified in Steps 2–4; the finite calculation implements the explicitly bounded identities rather than extrapolating a prefix experiment.

## Relationship to prior work
Rigo, Stipulanti, and Whiteland introduced and analyzed this particular Parikh-collinear fixed point and its six-state uniform presentation, proving that its abelian-complexity function is aperiodic; their 2024 continuation establishes general automaticity results for abelian complexity. Neither analyzed its palindromic spectrum or uniform factor defect in the relevant inspected portions. Frid, Laborde, and Peltomäki proved that an automatic word with finitely many palindromes has regular prefix palindromic length, with applications to the paperfolding and Rudin–Shapiro words. Applying their **existing** theorem to the present 5-automatic word yields a 5-regular prefix-palindromic-length function; the present result supplies the previously unverified finite-palindrome hypothesis for this distinct example. Also, any factor \(v\) requires at least \(\lceil|v|/23\rceil\) palindromic blocks in a palindrome factorization. These are consequences, not separate novel theorems.

## Limitations
The threshold 1249 is a convenient explicit guarantee, not an optimal threshold. The result does not supply a closed formula for the prefix-palindromic-length function, nor does it classify arbitrary Parikh-collinear fixed points. The finite exact certificate has been checked computationally from a completely specified finite set; independent mathematical audit remains unperformed. Absence of an equivalent result in unpublished or unindexed literature is not proved.

## References
1. M. Rigo, M. Stipulanti, M. A. Whiteland, *Automaticity and Parikh-collinear Morphisms*, WORDS 2023, LNCS 13899, pp. 247–260; publicly deposited 2023-05-11, https://orbi.uliege.be/handle/2268/302523 . Especially the six-letter morphism in the original paper, page 10.
2. M. Rigo, M. Stipulanti, M. A. Whiteland, *Automatic Abelian Complexities of Parikh-Collinear Fixed Points*, Theory of Computing Systems (2024), first preprint 2024-05-28, https://arxiv.org/abs/2405.18032 .
3. A. E. Frid, E. Laborde, J. Peltomäki, *On prefix palindromic length of automatic words*, arXiv:2009.02934, first submitted 2020-09-07, https://arxiv.org/abs/2009.02934 .
