# Sharp reversal cutoff and reflection complexity of the Currie–Ochem–Rampersad–Shallit ternary word
## Finding
Let \(\mathbf p\) be the infinite ternary word beginning
\[
012102101021012101021012\cdots
\]
and fixed by
\[
0\mapsto01,\qquad 1\mapsto21,\qquad 2\mapsto0.
\]
Let \(r_{\mathbf p}(n)\) denote its reflection complexity: the number of length-\(n\) factors up to reversal equivalence. Then
\[
r_{\mathbf p}(n)=
\begin{cases}
3,&n=1,\\
3,&n=2,\\
6,&n=3,\\
7,&n=4,\\
10,&n=5,\\
12,&n=6,\\
2n+1,&n\ge7.
\end{cases}
\]

More strongly, length \(8\) is the sharp reversal-avoidance cutoff. The only length-\(7\) factor whose reversal also occurs is the palindrome
\[
1012101,
\]
whereas no factor of length at least \(8\) occurs together with its reversal.

## Assumptions and scope
Two words are reflection-equivalent when one is equal to the other or to its reversal. The factor complexity \(\rho_{\mathbf p}(n)\) counts distinct length-\(n\) factors before quotienting by reversal.

Currie, Ochem, Rampersad, and Shallit proved
\[
\rho_{\mathbf p}(n)=2n+1
\]
for every positive integer \(n\). The present result uses that theorem as an exhaustiveness certificate for finite factor lists.

The claim concerns this one morphic ternary word. It does not assert the same cutoff for other words of factor complexity \(2n+1\).

## Proof
Take a sufficiently long iterated prefix of the defining morphism. For every \(1\le n\le8\), the prefix contains exactly \(2n+1\) distinct length-\(n\) factors. By the published factor-complexity theorem, these observed sets are therefore the complete factor sets of the infinite word.

At length \(8\), the complete factor set is
\[
\begin{aligned}
\{&
01021012,01210102,01210210,02101021,02101210,\\
&10102101,10121010,10121021,10210102,10210121,\\
&12101021,12102101,21010210,21012101,21012102,\\
&21021010,21021012
\}.
\end{aligned}
\]
Direct reversal of these \(17\) words shows that none of their reversals belongs to the set.

Suppose now that \(u\) is a factor of length \(n\ge8\) and that \(u^R\) is also a factor. Let \(v\) be the first eight letters of \(u\). Then \(v\) is a length-\(8\) factor, and \(v^R\) occurs as the final eight letters of \(u^R\), contradicting the preceding complete length-\(8\) check. Hence no factor of length at least \(8\) occurs together with its reversal.

Therefore every reflection-equivalence class at length \(n\ge8\) contains exactly one factor of \(\mathbf p\), so
\[
r_{\mathbf p}(n)=\rho_{\mathbf p}(n)=2n+1.
\]

At length \(7\), the complete factor set has \(15\) members and the only factor whose reversal occurs is \(1012101\), which is itself a palindrome. A palindrome does not merge two distinct factors, so
\[
r_{\mathbf p}(7)=15=2\cdot7+1.
\]
For \(1\le n\le6\), direct quotienting of the complete factor sets gives
\[
3,3,6,7,10,12,
\]
respectively. This proves the stated formula and the sharp cutoff.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier generates an iterated prefix from the defining morphism. For each length from \(1\) through \(8\), it checks that the observed factor count is exactly the published value \(2n+1\), which makes the finite factor set exhaustive once the published theorem is invoked.

It then recomputes the reflection-class counts
\[
3,3,6,7,10,12,15,17,
\]
checks that \(1012101\) is the sole reversible length-\(7\) factor, and checks that the complete \(17\)-element length-\(8\) factor set contains no word together with its reversal. As a regression check, it verifies the same no-reversal property directly for all lengths from \(8\) through \(40\) in a much longer generated prefix.

The infinite statement for all \(n\ge8\) follows from the length-\(8\) prefix/suffix argument in the proof, not from the finite regression range.

## Relationship to prior work
Allouche, Campbell, Li, Shallit, and Stipulanti introduced reflection complexity and emphasized its relation to the older problem of words avoiding reversed factors. Their general theory proves that a uniformly recurrent sequence not closed under reversal has no reflected factors at all sufficiently large lengths. It does not give the sharp cutoff or reflection-complexity profile for \(\mathbf p\).

Currie, Ochem, Rampersad, and Shallit studied \(\mathbf p\) in detail before reflection complexity was introduced. They proved its factor complexity \(2n+1\), noted that its language is not closed under reversal because \(02\) occurs while \(20\) does not, and studied its balance, critical exponent, abelian complexity, bispecial factors, and avoided factors. They did not determine the sharp length at which all reversed-factor pairs disappear.

Rampersad and Shallit, and later Fleischer and Shallit, studied existence and enumeration questions for words avoiding reversed factors. Those results provide the surrounding reversal-avoidance theory but do not state this exact cutoff for \(\mathbf p\).

The result therefore supplies the exact reflection-complexity profile of a canonical low-factor-complexity ternary word and sharpens the general eventual-avoidance theorem to the concrete threshold \(8\).

## Limitations
The argument relies on the published theorem \(\rho_{\mathbf p}(n)=2n+1\) to certify that the finite factor lists through length \(8\) are exhaustive.

The result is specific to \(\mathbf p\). It does not classify all morphic or all uniformly recurrent words that eventually avoid reversed factors.

No claim is made that the threshold \(8\) is extremal among ternary words or among words with factor complexity \(2n+1\).

## References
1. J.-P. Allouche, J. M. Campbell, S. Li, J. Shallit, and M. Stipulanti, “The reflection complexity of sequences over finite alphabets,” arXiv:2406.09302v1, first public 2024-06-13; later published in *Theory of Computing Systems*.
2. J. D. Currie, P. Ochem, N. Rampersad, and J. Shallit, “Properties of a Ternary Infinite Word,” arXiv:2206.01776v1, 2022; RAIRO Theoretical Informatics and Applications 57 (2023), article 1.
3. N. Rampersad and J. Shallit, “Words Avoiding Reversed Subwords,” *Journal of Combinatorial Mathematics and Combinatorial Computing* 54 (2005), 157–164.
4. L. Fleischer and J. Shallit, “Words Avoiding Reversed Factors, Revisited,” arXiv:1911.11704, 2019.
5. OEIS A287072, fixed point of \(0\mapsto01\), \(1\mapsto21\), \(2\mapsto0\).
