# Uniform odd-length group-complexity gaps for complement-symmetric binary words

## Finding

**Theorem.** Let \(x\in\{0,1\}^{\mathbb N}\) be a one-sided infinite binary word which is not ultimately periodic, and suppose its full factor language is closed under exchanging \(0\) and \(1\). For every positive integer \(n\),
\[
p_x(n)\ge 2n.
\]
At each odd length \(n\), the number \(p_x^G(n)\) of equivalence classes of length-\(n\) factors under any subgroup \(G\le S_n\) of coordinate permutations is even. In particular, for every odd \(n\ge3\),
\[
p_x^{\mathrm{ab}}(n)<p_x^{\mathrm{ab}}(n)+1<p_x(n),\qquad
p_x^G(n)\ne p_x^{\mathrm{ab}}(n)+1
\]
for every \(G\le S_n\). Therefore \(x\) is not universally group-complex. The earliest universally possible gap occurs at length three: no binary infinite word can have a missing intermediate group complexity at length one or two.

For the Thue--Morse fixed point of \(0\mapsto01,\ 1\mapsto10\), the exact length-three set of subgroup group-complexities is \(\{2,4,6\}\). Respectively, \(2,3,1\) of the six subgroups of \(S_3\) attain these values.

## Assumptions and scope

For a positive integer \(n\), \(F_x(n)\) is the set of all contiguous length-\(n\) factors, \(p_x(n)=|F_x(n)|\), and \(p_x^{\mathrm{ab}}(n)\) is the number of distinct numbers of ones attained among factors in \(F_x(n)\). A group \(G\le S_n\) acts on all binary length-\(n\) words by permuting coordinates. Define \(u\sim_Gv\) when \(u\) and \(v\) are in the same full ambient \(G\)-orbit; \(p_x^G(n)\) is the number of equivalence classes induced on \(F_x(n)\). This definition does not assume that a full ambient orbit lies inside the factor language.

Complement closure means that for every length and every factor \(u\), its bitwise complement \(\bar u\) is also a factor. Non-ultimate periodicity is essential for the lower bound on factor growth. The asserted parity property itself requires only complement closure, not aperiodicity.

## Proof

**1. Two distinct right-special factors at every length.** A binary length-\(n\) factor \(u\) is right-special if both \(u0\) and \(u1\) occur. At every positive length an infinite word that is not ultimately periodic has a right-special factor. Indeed, if there were none at some fixed length, every occurring length-\(n\) factor would have a unique successor letter. The sequence of its successive length-\(n\) windows would then follow a deterministic map on a finite set, forcing the infinite word to be ultimately periodic. If \(u\) is right-special, complement closure makes \(\bar u\) right-special as well. Since a nonempty binary word never equals its bitwise complement, these are distinct. Hence at least two length-\(n\) factors have both right extensions.

**2. The factor-complexity lower bound.** Each length-\(n\) factor has at least one right extension, and each right-special factor provides one additional right extension. Thus \(p_x(n+1)-p_x(n)\ge2\) for every positive \(n\). Both letters occur, since a non-ultimately-periodic word cannot have a one-letter factor language; hence \(p_x(1)=2\). Induction gives \(p_x(n)\ge2n\). In particular \(p_x(2)=4\), since there are only four binary words of length two.

**3. Parity of every group complexity at odd length.** Fix odd \(n\) and \(G\le S_n\). Bitwise complementation commutes with all coordinate permutations, so it induces an involution on the set of \(G\)-classes of occurring length-\(n\) factors. If a class were fixed, some factor \(u\) and its complement would be in the same \(G\)-orbit. Coordinate permutations preserve the number of ones, whereas the complement has \(n-|u|_1\) ones. Equality would require \(2|u|_1=n\), impossible for odd \(n\). Thus every class belongs to a two-element complement pair, and \(p_x^G(n)\) is even. Applying this to \(G=S_n\) proves \(p_x^{\mathrm{ab}}(n)\) is even as well.

**4. Strict missing values.** On a binary alphabet there are at most \(n+1\) abelian classes at length \(n\), so \(p_x^{\mathrm{ab}}(n)\le n+1\). At every odd \(n\ge3\),
\[
p_x^{\mathrm{ab}}(n)+1\le n+2<2n\le p_x(n).
\]
The middle candidate is odd because \(p_x^{\mathrm{ab}}(n)\) is even; it is larger than the abelian minimum but cannot equal any even group complexity. This proves the failure of universality at every odd length \(n\ge3\), without relying on any finite computation.

**5. Sharpness of the first length.** At length one the only subgroup is the identity, and ordinary and abelian complexities coincide. At length two the two subgroups of \(S_2\) are \(\{e\}\) and \(S_2\); they attain the ordinary and abelian endpoints. The only two different binary words in the same abelian class at length two are \(01\) and \(10\), so the endpoint complexities differ by at most one. There is therefore no intermediate integer left unrealized at either length, for any binary infinite word.

**6. The Thue--Morse check.** At length three its six factors are \(001,010,011,100,101,110\); the abelian classes are the weight-one and weight-two sets. The six subgroups of \(S_3\) consist of the trivial group, three order-two subgroups, the alternating subgroup, and the full symmetric group. Their numbers of classes are, respectively, \(6,4,2,2\); this yields multiplicities \(\{2:2,4:3,6:1\}\).

## Verification

The bundled standalone file `verification.py` checks complement closure and \(p_x(n)\ge2n\) for Thue--Morse factors of lengths \(1\) through \(10\), derives its exact factors of lengths two and three, enumerates all subgroups of \(S_2\) and \(S_3\), and computes their induced factor-orbit counts. Replaying that program yields the success marker `THUE_MORSE_COMPLEMENT_AND_GROUP_SPECTRUM_OK` and the exact distributions recorded in `verification_output.txt`. The general infinitely quantified theorem is proved above; the finite checks only illustrate and test the example.

## Relationship to prior work

Launer, Puzynina and Voloshinova (2026) introduce the universal group-complexity question, establish positive cases including Sturmian words, and study periodic and low-complexity ternary examples. A detailed publicly available secondary review also attributes a nonuniversality argument for the individual Thue--Morse word to that paper, using an odd-length parity mechanism. Thus **nonuniversality for Thue--Morse and the idea of parity as an obstruction are not claimed as new**. The present assertion addresses every aperiodic complement-closed binary language simultaneously, proves the sharp factor-growth inequality \(p_x(n)\ge2n\), identifies an explicitly missing value at every odd length at least three, and proves that the first obstruction has the globally minimum possible length.

Charlier, Puzynina and Zamboni (2015) develop group-action factor complexity and Morse--Hedlund lower bounds; their group-orbit lower bound does not by itself classify the parity-forbidden intermediate values. Searches of indexed research records did not identify the general complement-closed language theorem. These searches do not establish absolute publication priority.

## Limitations

The result does not cover words whose factor languages are not complement-closed, and it does not claim any forbidden values at even lengths. The full 2026 primary manuscript was not obtainable during this examination; its publicly available abstract and a detailed secondary review were examined, but the possibility that its full text already contains this generalization is an important originality risk. No independent external validation has been performed.

## References

1. M. Launer, S. Puzynina, E. Voloshinova, *On possible values of the group complexity function of infinite words*, arXiv:2607.07620v1, first public 2026-07-08. https://arxiv.org/abs/2607.07620
2. E. Charlier, S. Puzynina, L. Q. Zamboni, *On a group theoretic generalization of the Morse--Hedlund theorem*, arXiv:1505.03848, first public 2015-05-14. https://arxiv.org/abs/1505.03848
3. *On possible values of the group complexity function of infinite words*, independent summary at https://www.themoonlight.io/de/review/on-possible-values-of-the-group-complexity-function-of-infinite-words (secondary commentary only).
