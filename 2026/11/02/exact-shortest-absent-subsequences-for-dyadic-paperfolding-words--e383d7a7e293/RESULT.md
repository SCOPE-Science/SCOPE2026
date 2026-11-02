# Exact shortest absent subsequences for dyadic paperfolding words and a four-block concatenation family

## Finding

Work over the fixed binary alphabet \(\Sigma=\{0,1\}\). A *scattered subsequence* is obtained by deleting symbols without changing the order of the survivors. Write \(\operatorname{SAS}(w)\) for the set of all shortest binary words that do not occur as scattered subsequences of a finite word \(w\), and \(\iota(w)\) for the greatest length for which every binary word occurs.

Define the four binary blocks of length \(32\)
\[
 A_{a,b}=110110011100100\;a\;110110001100100\;b,
 \qquad a,b\in\Sigma,
\]
and the four-word language
\[
 \mathcal B=\{00x011001y11:x,y\in\Sigma\}.
\]
**Four-block concatenation theorem.** For every integer \(q\ge1\) and every choice of \(a_1,b_1,\ldots,a_q,b_q\in\Sigma\), let \(W=A_{a_1,b_1}\cdots A_{a_q,b_q}\). Then
\[
 \operatorname{SAS}(W)=
 \begin{cases}
 \mathcal B^q,&b_q=0,\\
 \mathcal B^q\Sigma,&b_q=1.
 \end{cases}
\]
Here products of languages are concatenation products, not unions. In particular,
\[
 \iota(W)=12q-1+b_q,
 \qquad
 |\operatorname{SAS}(W)|=4^q\,2^{b_q}.
\]
Thus arbitrary choices of both internal block parameters affect neither the shortest-absence language nor the universality index, except for the final bit of the last block.

For the regular paperfolding word \(f_1f_2\cdots\), define \(f_j=1\) if the odd part of \(j\) is \(1\pmod4\), and \(f_j=0\) otherwise. Let \(P_k=f_1\cdots f_{2^k}\). **Dyadic-prefix corollary.** For every \(k\ge5\), with \(q=2^{k-5}\),
\[
 \operatorname{SAS}(P_k)=\mathcal B^{q}\Sigma,\quad
 \iota(P_k)=12q=3\cdot2^{k-3},\quad
 |\operatorname{SAS}(P_k)|=2\cdot4^q=2^{2^{k-4}+1}.
\]
The first exceptional ranks have \((\iota(P_3),|\operatorname{SAS}(P_3)|)=(3,3)\) and \((\iota(P_4),|\operatorname{SAS}(P_4)|)=(6,4)\). The stated uniform formula begins at \(k=5\).

## Assumptions and scope

Symbols in \(A_{a,b}\) denote literal binary digits, and there are exactly two freely selected digits in each length-\(32\) block. All subsequences and missing words use the *fixed* two-symbol alphabet even for suffixes. The concatenation theorem covers every nonempty finite sequence of these four blocks, regardless of whether that sequence actually occurs in the regular paperfolding word. The corollary concerns complete prefixes of length \(2^k\), not arbitrary prefixes or factors. The word \(\mathcal B^q\Sigma\) denotes a language with independently free binary choices in the specified positions; each of its members has length \(12q+1\).

## Proof

**1. A recurrence for shortest absent scattered words.** For any binary word \(u\), let \(L(u)\) be the minimum length of an absent binary subsequence and let \(S(u)\) be its complete shortest-absence language. For \(c\in\Sigma\), let \(r_c(u)\) be the suffix strictly after the *first* occurrence of \(c\) in \(u\), if it exists. Greedy earliest-position embedding is optimal: a target word \(cv\) is a subsequence of \(u\) if and only if \(c\) occurs and \(v\) is a subsequence of \(r_c(u)\). Therefore, if both digits occur,
\[
 L(u)=1+\min_{c\in\Sigma}L(r_c(u)),\qquad
 S(u)=\bigcup_{\substack{c\in\Sigma\\L(r_c(u))+1=L(u)}}cS(r_c(u)).
\]
If at least one digit is missing, \(L(u)=1\) and \(S(u)\) consists exactly of the missing single letters. This also specifies the base \(L(\varepsilon)=1\), \(S(\varepsilon)=\Sigma\). Finally \(\iota(u)=L(u)-1\). These are exact identities, not upper or lower bounds.

**2. Four finite base checks.** Applying the preceding recurrence from right to left to each literal \(A_{a,b}\) gives
\[
 S(A_{a,0})=\mathcal B,\qquad
 S(A_{a,1})=\mathcal B\Sigma,
\]
with \(L(A_{a,0})=12\) and \(L(A_{a,1})=13\), independently of \(a\). If \(U=A_{a,b}\), write \(U[j:]\) for its zero-based suffix starting at position \(j\). The same four computations give, setting \(m=L(U)\) and \(R=S(U[3:])\),
\[
 L(U[1:])=m,\quad L(U[3:])=m-1,\quad
 S(U)=S(U[1:])=0R.
\]
The accompanying standalone checker performs these exact four computations with a general greedy-subsequence dynamic program. No search over exponentially many candidate target words is needed for the base cases.

**3. One-block symbolic transfer.** Suppose \(U\) is any binary word beginning with \(110\), with the three boundary identities
\[
 L(U)=L(U[1:])=m,\quad L(U[3:])=m-1,\quad
 S(U)=S(U[1:])=0R,\quad S(U[3:])=R.
\]
Prepend any one of the four blocks \(A=A_{a,b}\). A recurrence application at a suffix beginning strictly inside \(A\) can only refer to later positions in \(A\) or to the suffixes \(U\), \(U[1:]\), and \(U[3:]\). Indeed, the three initial digits of \(U\) are \(110\), so either digit has a first occurrence by the third digit of \(U\); after matching it, precisely those three types of terminal suffix can occur.

For each position in \(A\), propagate an integer length \(m+d\) and a finite language of literal prefixes to be concatenated with the formal residual language \(R\). The only input states on the right are \((m,0R)\), \((m,0R)\), and \((m-1,R)\). Applying the exact recurrence in step 1 to the \(32\) positions in reverse order gives, for **each** of the four choices \((a,b)\), the same output:
\[
\begin{array}{c|rrrrrr}
\text{suffix start }j & 0&1&2&3&4&5\\ \hline
L((AU)[j:])-m&12&12&12&11&11&10\\
\text{number of prefix choices before }R&4&4&10&4&6&2
\end{array}
\]
and, more strongly,
\[
 S(AU)=S((AU)[1:])=\mathcal B\,0R,
 \qquad S((AU)[3:])=0^{-1}(\mathcal B\,0R).
\]
Here \(0^{-1}X=\{v:0v\in X\}\) is a left quotient. The finite transfer is an exact four-case calculation: at each position, find the first occurrences of \(0\) and \(1\), retain successors attaining the smaller length, and union their prefixed residual languages. The packaged `checker.py` explicitly reproduces all \(32\) steps for all four blocks, including literal comparison of the output languages; the use of a representative boundary length \(m=100\) is valid for arbitrary \(m\) because every length occurring in the calculation is \(m\) plus an integer offset, so comparisons are translation-invariant. Thus no finite experimental extrapolation is used.

Since \(S(U)=0R\), the transfer identity reads
\[
 S(AU)=\mathcal B S(U),\qquad L(AU)=L(U)+12.
\]
As each word of \(\mathcal B\) starts in \(0\), the three boundary identities also hold for \(AU\). By induction over the number of blocks, starting from step 2,
\[
 S(A_{a_1,b_1}\cdots A_{a_q,b_q})=\mathcal B^{q-1}S(A_{a_q,b_q}),
\]
which proves the entire concatenation theorem. Since the four words of \(\mathcal B\) are distinct and have the common length \(12\), their concatenation representations are uniquely decodable at those fixed-length boundaries; hence their cardinalities multiply to give the claimed counts.

**4. The paperfolding specialization.** Let \(f_j\) be the odd-part sequence in the statement. For a positive integer \(j\) in an aligned block \(32r+1,\ldots,32r+32\), its value is fixed independently of \(r\) unless \(j\) is divisible by \(16\). Indeed, removing powers of two from each other residue leaves an odd part congruent to the same element of \(\{1,3\}\pmod4\) for every \(r\). The two exceptional positions are \(j=32r+16\) and \(j=32r+32\). Evaluating the other thirty residues gives precisely the template \(A_{a,b}\) above (the two exceptional bits may vary). Thus the length-\(2^k\) prefix for \(k\ge5\) is a concatenation of \(q=2^{k-5}\) allowed blocks. Its last position is \(2^k\), whose odd part is \(1\), so its final bit is \(1\). Substitute \(b_q=1\) into the theorem.

## Verification

Run `python3 checker.py` with Python 3 and the standard library. The script verifies the four exact base absence languages and suffix invariants; the four complete symbolic \(32\)-step transfers in the indeterminate residual-language setting; every one of the \(4+16+64=84\) concatenations of one, two, and three allowed blocks using an independent full greedy-subsequence automaton; and the paperfolding decomposition, universality index, and shortest-absence counts at ranks \(5\) through \(11\). The symbolic transfer and mathematical induction—not the small-instance tests—establish all lengths and all numbers of blocks. The script prints `PASS` only after all assertions succeed.

## Relationship to prior work

Holub, *Abelian powers in paper-folding words* (2012 preprint; 2013 journal), develops the paperfolding digit structure and proves existence of arbitrarily high Abelian powers in paperfolding words. Its objects are contiguous Abelian repetitions, not scattered-subsequence absence languages. Kosche, Koß, Manea and Siemer, *Absent Subsequences in Words* (first public 2021), establish the general shortest-absent-subsequence framework, combinatorial characterizations and algorithms. That framework allows any particular finite instance to be processed but does not state the present paperfolding formulas or the four-block product identity. Related published results on general binary extremal numbers of shortest missing subsequences concern optimization over all words, not this exact structured family. Known analogous block-transfer formulas for other automatic-word families do not imply the literal paperfolding language identity: the substituted blocks and their residual languages differ.

The overlap comparisons concern the *entire stated language identity*, not only the scalar universality index or cardinality. The literature assessment is evidence-limited; an absence of matches does not establish unconditional historical novelty.

## Limitations

All formulas depend on the fixed binary alphabet, the exact displayed four-block template, and the indicated complete dyadic prefixes. No formula is claimed for arbitrary paperfolding factors, arbitrary prefix lengths or every other paperfolding instruction sequence. The proof certifies shortest absent scattered subsequences only, not all minimal absent scattered subsequences (which can be longer). The finite transfer has not undergone independent external verification. The available literature comparison does not establish exhaustive priority across every historical source.

## References

1. Štěpán Holub, *Abelian powers in paper-folding words*, arXiv:1207.3585, first submitted 2012-07-16; Journal of Combinatorial Theory A 120 (2013), 872–881. https://arxiv.org/html/1207.3585v2
2. Maria Kosche, Tore Koß, Florin Manea and Stefan Siemer, *Absent Subsequences in Words*, arXiv:2108.13968, first submitted 2021-08-31; Fundamenta Informaticae 189 (2023), 199–240. https://arxiv.org/html/2108.13968v6
