# Exact one-step tortoise complexity of the binary Rudin–Shapiro word

## Finding

Let \(r=r_0r_1\cdots\) be the binary Rudin–Shapiro word, in which \(r_i\) is the parity of the number of overlapping occurrences of `11` in the binary expansion of \(i\). Let \(F_n\) denote its distinct factors of length \(n\). For a binary finite word \(w\), define \(T(w)\) by moving its *first* `1` to the end, leaving all zeroes in their original order; put \(T(0^n)=0^n\). Define one-step tortoise complexity \(\rho_T(n)=|\{T(w):w\in F_n\}|\). Then

\[
(\rho_T(1),\ldots,\rho_T(11))=(2,3,5,9,14,24,31,43,52,61,71),
\qquad \rho_T(n)=8n-16\quad(n\ge12).
\]

The ordinary factor complexity is \(p(n)=|F_n|=8n-8\) for \(n\ge8\), so the loss in one-step tortoise complexity is exactly eight at every length \(n\ge12\).

## Assumptions and scope

All factors are contiguous factors of the *one-sided infinite* standard Rudin–Shapiro word, and \(n\) ranges over positive integers. A morphic representation uses alphabet \(\{a,b,c,d\}\), the fixed point \(u=\mu^\omega(a)\), morphism
\[
\mu(a)=ab,\quad\mu(b)=ac,\quad\mu(c)=db,\quad\mu(d)=dc,
\]
and letter coding \(\pi(a)=\pi(b)=0\), \(\pi(c)=\pi(d)=1\). In this convention \(r=\pi(u)\), which agrees with parity of occurrences of binary `11` in the input index. No unproved statistical or empirical asymptotic assumption is made; the standard, published factor-complexity formula is the sole external enumerative input.

## Proof

**1. Exact finite-factor certificate.** The length-two factors of \(u\) are exactly

`ab ac ba bd ca cd db dc`.

Starting with the factor `ab` and repeatedly taking the three adjacent pairs occurring in each \(\mu(xy)\) stabilizes at precisely this set. For any factor length \(L\), choose \(j\ge0\) with \(2^j\ge L\). Every length-\(L\) factor of \(u\) lies in \(\mu^j(xy)\) for some adjacent pair \(xy\) from the stated list: the constant-length level-\(j\) block decomposition places a window of length at most \(2^j\) inside at most two adjacent blocks. Conversely, each pair \(xy\) occurs in \(u\), hence every factor of its image occurs in \(u\). Coding by \(\pi\) therefore gives exact finite binary factor sets as well. The accompanying self-contained program implements this certificate, without sampling or a truncation guess.

**2. Four-letter special-context rigidity.** Exhaustively applying the preceding formula at length seven, the four-letter factors \(v\) of length five with two distinct immediate left letters are precisely

`abaca abacd abdba abdbd dcaca dcacd dcdba dcdbd`.

For *each* such \(v\), its complete two-letter left-context set is exactly \(\{ac,db\}\). In particular the corresponding binary context words are `01` and `10`. Exhaustive length-eight factor generation additionally proves that \(\pi\) is injective on the 56 four-letter factors of length eight. Consequently \(\pi\) is injective on every longer fixed-length factor set: two length-\(L\) factors sharing their binary code share all overlapping length-eight four-letter factors, hence agree letter by letter.

Fix \(m\ge10\). A length-\(m\) binary factor \(z\) is left-special if both \(0z\) and \(1z\) occur. Its four-letter lift \(Z\) is unique, because its length-eight binary prefix has a unique four-letter antecedent and successive overlapping eight-windows determine the rest. The two binary left extensions must lift to two distinct four-letter left letters, so \(Z\) is left-special. Its length-five prefix is in the eight-word list, which forces its two-letter preceding contexts to be `ac` and `db`; both actually occur because two distinct preceding letters are required. Thus the binary factors `01z` and `10z` both occur. Conversely, if both occur, \(z\) is plainly left-special. Therefore

\[
\{z\in F_m:0z,1z\in F_{m+1}\}
=\{z\in F_m:01z,10z\in F_{m+2}\}\qquad(m\ge10).
\]

The morphism is primitive (every letter appears in a sufficiently high iterate of each letter), so the infinite fixed point and its coding are recurrent: each factor has a preceding occurrence. Hence the number of length-\(m\) left-special factors equals \(p(m+1)-p(m)\). By Berthé's Theorem 4, \(p(t)=8t-8\) for \(t\ge8\). There are therefore *exactly eight* factors \(z\) in the displayed set for each \(m\ge10\).

**3. Finite collision classification and inheritance.** The exact binary length-12 factor set has 88 words, and its 80 one-step tortoise images have exactly eight non-singleton fibers, each a doubleton of form \(\{01z,10z\}\) with a common length-ten suffix. The complete eight pairs are printed in `rudin_tortoise_certificate.txt`. There are no other collisions, a certified finite statement established by exhaustive generation in Step 1 and the included code.

The same finite-factor generator shows that `00000` is not a binary factor. Thus every length-12 factor contains a `1`. For any longer factor \(w\), writing \(w_{12}\) for its first 12 symbols, the first 11 symbols of \(T(w)\) equal the first 11 symbols of \(T(w_{12})\). Appending `1` reconstructs \(T(w_{12})\), so equality \(T(w)=T(w')\) implies equality of the tortoise images of their first 12 symbols. If \(w\ne w'\), those first 12 symbols are one of the eight pairs from Step 3; indeed if the prefixes were equal, deletion of their common first `1` followed by appending `1` is injective in the remaining tails, so \(w=w'\). In particular the prefixes must be `01` and `10` followed by the same ten letters. Directly from the definition of \(T\), equality then forces their *entire* suffixes after the first two symbols to be identical. Hence all and only collisions at length \(n\ge12\) are the doubletons \(\{01z,10z\}\) with \(|z|=n-2\) and both words factors.

By Step 2 there are exactly eight such suffixes \(z\). Each pair reduces the total image count by one, hence \(\rho_T(n)=p(n)-8=8n-16\) for every \(n\ge12\). For \(1\le n\le11\), the exact finite-factor census yields the sequence in the statement.

## Verification

Run `python3 verify_rudin_tortoise.py` using Python 3 standard library. It independently generates complete fixed-length factor languages from the length-two morphism closure and performs exact set arithmetic. The recorded output `rudin_tortoise_certificate.txt` includes all eight length-five four-letter special factors and contexts; all 56 distinct length-eight decoded four-letter factors; the initial ordinary and tortoise complexities; the eight complete length-12 collision pairs; and optional cross-checks through length 128. The `00000` exclusion and all finite lemmas used by the proof are asserted by the program. The proof for arbitrary lengths comes from the symbolic implications above, not from extrapolating checked prefixes.

## Relationship to prior work

Campbell and Rampersad (arXiv:2604.25811, initial public version 2026-04-28) introduced one-step tortoise complexity of automatic words and proved a general bounded-deficit comparison for binary words of linear factor complexity with bounded gaps between `1` symbols. They explicitly compute examples for paperfolding and Thue–Morse words, not this Rudin–Shapiro exact formula. Their bounded-deficit theorem does not supply the constant eight or the exact threshold twelve. Berthé's earlier Theorem 4 supplies the well-known \(p(n)=8n-8\) and the four-letter morphic model, but does not count one-step tortoise images. The new ingredient is the special-factor two-letter-context rigidity plus finite collision inheritance. The result is distinct from tortoise results for other automatic words.

## Limitations

This determines **one** tortoise iteration, for the specified binary Rudin–Shapiro word. It does not claim formulas for higher tortoise iterates, differently coded Rudin–Shapiro variants or arbitrary automatic words. Standard published factor-complexity input is used and explicitly cited. Finite checks are self-contained but do not constitute an independent external mathematical audit. An earlier unindexed evaluation of the same invariant cannot be ruled out.

## References

1. John M. Campbell and Narad Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811, first public 2026-04-28, version 2 (2026-10-05), especially Definitions 1–2, Lemma 1 and Theorem 1. https://arxiv.org/pdf/2604.25811v2
2. Valérie Berthé, *Conditional entropy of some automatic sequences*, especially the Rudin–Shapiro discussion and Theorem 4, which states \(p(n)=8n-8\) for \(n\ge8\). https://www.irif.fr/~berthe/Articles/auto.pdf
3. Colin Defant and Noah Kravitz, *Stack-sorting for words*, *Australasian Journal of Combinatorics* 77 (2020), 51–68 (original word-tortoise operation), cited in reference 1.
