# Weight spectra separate the three optimal free length-eight rank-two codes over \(E\)
## Finding

For the three permutation-inequivalent \(l_2\)-optimal free \([8,2,4]\) codes over the four-element non-unital ring \(E\) listed in Table 10 of Kushwaha--Prakash, in the table order their Hamming weight enumerators are
\[
W_1(z)=1+9z^4+6z^6,
\qquad
W_2(z)=1+3z^4+6z^6+6z^8,
\qquad
W_3(z)=1+6z^4+9z^8.
\]
Thus their numbers of minimum-weight codewords are respectively \(9\), \(3\), and \(6\). In particular, the three classes are pairwise distinguished by ordinary Hamming weight spectrum.

## Assumptions and scope

The codes are exactly the three \([8,2,4]\) entries of Table 10 in the cited source, with generator matrices whose entries are \(0\) and \(\kappa\). The ring notation follows the source: every element of \(E\) is uniquely \(u\kappa+v\zeta\) with \(u,v\in\mathbb F_2\), and right multiplication by \(\kappa\) fixes every ring element. Hamming weight counts nonzero coordinates. The claim concerns these three fixed source codes only; it does not assert a weight-enumerator formula for all free \(E\)-codes.

## Proof

Write the two binary support rows of one listed generator matrix as \(g_1,g_2\), so the source generator is \(\kappa G\). If the two message coefficients are \(a=u_1\kappa+v_1\zeta\) and \(b=u_2\kappa+v_2\zeta\), then the corresponding codeword is
\[
a\kappa g_1+b\kappa g_2=ag_1+bg_2.
\]
Under the coordinatewise identification \(u\kappa+v\zeta\leftrightarrow(u,v)\in\mathbb F_2^2\), this word is the ordered pair of binary words
\[
(x,y)=\bigl(u_1g_1+u_2g_2,\;v_1g_1+v_2g_2\bigr).
\]
Its Hamming support is therefore exactly \(\operatorname{Supp}(x)\cup\operatorname{Supp}(y)\).

Let \(B=\langle g_1,g_2\rangle_{\mathbb F_2}\). There is one ordered pair \((x,y)=(0,0)\). For each of the three nonzero one-dimensional subspaces of \(B\), exactly three ordered pairs span that line, and all three have support equal to the support of its nonzero vector. The remaining six ordered pairs are ordered bases of \(B\), so each has support \(\operatorname{Supp}(B)\). Consequently, if the three nonzero binary weights are \(a,b,c\) and \(s=|\operatorname{Supp}(B)|\), then
\[
W_C(z)=1+3\bigl(z^a+z^b+z^c\bigr)+6z^s.
\]
For the first table matrix the binary weights are \((4,4,4)\) and \(s=6\); for the second they are \((4,6,6)\) and \(s=8\); for the third they are \((4,4,8)\) and \(s=8\). Substitution gives the three displayed enumerators. Their coefficient sums are all \(16=|E|^2\), and each has minimum nonzero exponent \(4\), agreeing with the source parameters.

## Verification

The bundled verifier independently encodes the four ring elements by their \((u,v)\) coordinates, enumerates all \(16\) message pairs for each of the three printed generator matrices, and recomputes Hamming weights directly. It separately derives the same distributions from the three nonzero binary residue words and the full binary support. The replay returns `VERIFY_OK` and prints the distributions \(\{0:1,4:9,6:6\}\), \(\{0:1,4:3,6:6,8:6\}\), and \(\{0:1,4:6,8:9\}\).

## Relationship to prior work

Kushwaha--Prakash classify permutation-inequivalent optimal free \(E\)-codes up to length eight and Table 10 lists precisely the three \(l_2\)-optimal \([8,2,4]\) matrices used here. Their text and table give parameters and representatives but not these ordinary Hamming weight enumerators. Earlier work on codes over this non-unital ring supplies the residue-code description and general duality/weight-enumerator machinery, but the inspected sources do not state the three numerical spectra above. The spectra refine the published classification by giving a simple invariant that distinguishes all three classes without invoking a permutation-equivalence search.

## Limitations

This is an exact finite classification refinement for one natural parameter/hull-rank stratum of the source table. It does not classify all length-eight free \(E\)-codes, and distinct weight enumerators are only a sufficient certificate of inequivalence, not a complete invariant in general. The computation uses the generator matrices as printed in Table 10 and the source's ring convention.

## References

1. A. Kushwaha and O. Prakash, *Hulls of Free Linear Codes over a Non-Unital Ring*, arXiv:2512.12335v1 (first public 2025-12-13); *Advances in Mathematics of Communications* (2026), DOI:10.3934/amc.2026043. See the ring decomposition, the residue/free-code correspondence, and Table 10.
2. A. Kushwaha, S. Debnath, and O. Prakash, *Classification of LCD and self-dual codes over a finite non-unital local ring*, arXiv:2501.03016, for the free-code/residue-code framework used by the later classification.
