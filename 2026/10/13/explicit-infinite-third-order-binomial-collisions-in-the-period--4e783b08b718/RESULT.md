# Explicit infinite third-order binomial collisions in the period-doubling word
## Finding
Let \(\mathbf{pd}\) be the period-doubling word, the fixed point beginning in \(0\) of
\[
\sigma(0)=01,\qquad \sigma(1)=00.
\]
Set
\[
u=\mathtt{0101010001},
\qquad
v=\mathtt{1000101010}.
\]
Then \(u\) and \(v\) are distinct factors of \(\mathbf{pd}\) and are \(3\)-binomially equivalent.

Moreover, for every integer \(t\ge0\), the two words
\[
\sigma^t(u),\qquad \sigma^t(v)
\]
are distinct factors of \(\mathbf{pd}\), have common length
\[
10\cdot2^t,
\]
and remain \(3\)-binomially equivalent. Consequently
\[
\mathsf b_{\mathbf{pd}}^{(3)}(10\cdot2^t)
<
\mathsf p_{\mathbf{pd}}(10\cdot2^t)
\qquad(t\ge0),
\]
so
\[
\mathsf b_{\mathbf{pd}}^{(3)}\prec\mathsf p_{\mathbf{pd}}.
\]

## Assumptions and scope
For finite words \(x,y\), write
\[
\binom{x}{y}
\]
for the number of occurrences of \(y\) as a subsequence of \(x\). Two words are \(k\)-binomially equivalent when these counts agree for every subsequence of length at most \(k\).

For an infinite word \(\mathbf{x}\), the function \(\mathsf b_{\mathbf{x}}^{(k)}(n)\) counts \(k\)-binomial equivalence classes represented among its length-\(n\) factors, while \(\mathsf p_{\mathbf{x}}(n)\) counts the factors themselves. The notation
\[
f\prec g
\]
means that \(f(n)<g(n)\) for infinitely many \(n\).

The result proves strict third-order binomial collisions at the explicit infinite family of lengths \(10\cdot2^t\). It does not determine the complete third-order binomial complexity function, nor does it address the conjectured fourth-order equality.

## Proof
First,
\[
\sigma^4(0)=\mathtt{0100010101000100}.
\]
Inside this word, \(v\) begins at position \(1\) and \(u\) begins at position \(4\), with positions numbered from \(0\). Hence both seeds are factors of \(\mathbf{pd}\).

Direct subsequence counting gives the same complete data through length \(3\):
\[
\begin{array}{c|rrrrrrrrrrrrrr}
x&
0&1&00&01&10&11&
000&001&010&011&100&101&110&111\\ \hline
\binom{u}{x}=\binom{v}{x}&
6&4&15&12&12&6&
20&19&22&10&19&16&10&4.
\end{array}
\]
Thus
\[
u\sim_3 v.
\]
The words are genuinely distinct; for example,
\[
\binom{u}{0001}=21,\qquad
\binom{v}{0001}=15.
\]

It remains to propagate the third-order equivalence. We use the following general fact.

If \(h\) is any morphism and \(x\) is a target word of length at most \(k\), every occurrence of \(x\) as a subsequence of \(h(w)\) uses letters from some \(r\) source positions, where
\[
1\le r\le |x|\le k.
\]
Grouping an occurrence according to those source positions and according to the nonempty consecutive pieces \(x_1,\ldots,x_r\) of \(x\) selected inside the corresponding image blocks gives
\[
\binom{h(w)}{x}
=
\sum_{r=1}^{|x|}
\ \sum_{a_1,\ldots,a_r}
\binom{w}{a_1\cdots a_r}
\sum_{\substack{x=x_1\cdots x_r\\x_i\ne\varepsilon}}
\prod_{i=1}^r
\binom{h(a_i)}{x_i}.
\]
The coefficients in this expression depend on \(h\) and \(x\), but not on \(w\). Therefore
\[
w\sim_k w'
\quad\Longrightarrow\quad
h(w)\sim_k h(w').
\]

Applying this fact repeatedly with \(h=\sigma\) gives
\[
\sigma^t(u)\sim_3\sigma^t(v)
\qquad(t\ge0).
\]
Because \(\sigma\) is \(2\)-uniform with two distinct codewords \(01\) and \(00\), it is injective, so the two images remain distinct.

Finally, an occurrence of \(u\) or \(v\) in \(\sigma^4(0)\) maps under \(\sigma^t\) to an occurrence of its image in
\[
\sigma^{t+4}(0).
\]
Thus both images are factors of \(\mathbf{pd}\). Their common length is \(10\cdot2^t\), and two distinct factors occupy one \(3\)-binomial class at every such length. Hence the strict inequality and the relation \(\prec\) follow.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier computes all subsequence counts through length \(3\) by generic dynamic programming, confirms the displayed seed table, and verifies that the seed factors occur at the stated positions in \(\sigma^4(0)\). It also checks a length-\(4\) coefficient on which the seeds differ.

For \(0\le t\le10\), it constructs both iterated images directly, checks that they remain distinct factors of \(\sigma^{t+4}(0)\), and recomputes their complete third-order signatures.

Separately, the verifier implements the morphism-transfer formula from the proof and checks it exhaustively for all binary source words of length at most \(5\), all binary nonempty morphism images of length at most \(2\), and all target words of length at most \(3\). This finite validation supplements the symbolic argument; it is not used to extrapolate the theorem to untested \(t\).

## Relationship to prior work
Rigo, Stipulanti, and Whiteland explicitly single out the period-doubling word when discussing how far binomial complexity is from ordinary factor complexity. They cite an exact second-order result and then state that computer experiments show
\[
\mathsf b_{\mathbf{pd}}^{(3)}\prec\mathsf p_{\mathbf{pd}},
\]
while experiments suggest fourth-order equality.

The present result supplies a proof of the third-order strictness statement by exhibiting a concrete seed collision and an infinite morphic propagation mechanism. It therefore replaces the empirical observation by an explicit infinite certificate.

Earlier exact work on binomial complexity treats the Thue--Morse word rather than period doubling. It develops general tools for subsequence counts under morphisms, but it does not provide the displayed period-doubling seed pair or the resulting infinite collision family.

Targeted searches using the period-doubling name, third-order binomial equivalence, the exact seed strings, and the strict-complexity formulation did not locate a published proof or an equivalent explicit family.

## Limitations
The theorem proves strictness on the infinite subsequence of lengths
\[
10\cdot2^t.
\]
It does not give the exact value of \(\mathsf b_{\mathbf{pd}}^{(3)}(n)\) at those lengths or elsewhere.

No fourth-order conclusion is claimed. The two seed words are not \(4\)-binomially equivalent, but that fact does not establish fourth-order reconstruction for all period-doubling factors.

An unindexed note, thesis, or unpublished computation could contain the same seed family.

## References
1. M. Rigo, M. Stipulanti, and M. A. Whiteland, “Characterizations of families of morphisms and words via binomial complexities,” arXiv:2201.04603v1, first public version 2022-01-12; European Journal of Combinatorics 118 (2024), 103932, DOI 10.1016/j.ejc.2024.103932.
2. M. Lejeune, J. Leroy, and M. Rigo, “Computing the \(k\)-binomial complexity of the Thue--Morse word,” arXiv:1812.07330v1, 2018; Journal of Combinatorial Theory, Series A 176 (2020), 105284.
