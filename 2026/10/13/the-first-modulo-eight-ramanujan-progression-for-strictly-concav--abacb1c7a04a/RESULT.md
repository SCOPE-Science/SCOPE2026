# The first modulo-eight Ramanujan progression for strictly concave compositions

## Finding

Let \(s_1(n)\) be the strictly concave composition counting function defined below. For integers \(m\ge1\) and \(0\le r<m\), call \((m,r)\) a universal modulo-eight zero progression if
\[
  s_1(mk+r)\equiv0\pmod 8\qquad\text{for every integer }k\ge0.
\]
**Theorem.** Among all moduli \(1\le m\le25\), universal modulo-eight zero progressions occur **exactly** for
\[
  (m,r)\in\{(25,8),(25,13),(25,18),(25,23)\}.
\]
In particular, \(25\) is the least modulus admitting any such progression, and these are its only four valid residue classes.

## Assumptions and scope

For \(|q|<1\), define the integer coefficient sequence by
\[
 \sum_{n\ge0}s_1(n)q^n=\sum_{a\ge0}q^a\prod_{j>a}(1+q^j)^2.
\]
This is the generating function for the strictly concave compositions, equivalently the two-color distinct-part partitions whose least part has one prescribed color. The universal quantifier over \(k\) is essential. The theorem makes a complete statement only for moduli at most \(25\); it does not classify larger moduli.

## Proof

**Positive progressions.** Theorem 1.4 of Liu and Xia [2] proves, for a prime \(p\equiv5,7\pmod8\), integers \(j\ge0\), and positive \(h\) not divisible by \(p\), that
\[
 s_1\left(p^{2j+1}h+\frac{p^{2j+2}-1}{8}\right)\equiv0\pmod8.
\]
Set \(p=5\), \(j=0\), and \(h=5k+t\) with \(k\ge0\) and \(t\in\{1,2,3,4\}\). The argument of \(s_1\) becomes \(25k+5t+3\), giving exactly the four claimed progressions.

**A finite obstruction certificate for all smaller moduli.** Write the triangular numbers \(T_a=a(a+1)/2\). Theorem 1.1 in [2], proved by Andrews and El Bachraoui [1], says
\[
 s_1(T_a)\equiv(-1)^a\pmod4.
\]
Thus every triangular number is a nonzero modulo-eight coefficient. For a fixed modulus \(m\), the triangular residues are exhausted by \(T_a\bmod m\) for \(0\le a<2m\), because
\[
 T_{a+2m}-T_a=m(2a+2m+1).
\]
It remains to cover residue classes that contain no triangular number.

Consider the following fixed finite set of indices:
\[
\mathcal W=\{5,7,12,16,17,94,103,119,128,222,249,251,261,277,284,382,386,422\}.
\]
Direct **exact** evaluation of the defining generating function gives \(s_1(w)\equiv4\pmod8\) for each \(w\in\mathcal W\). A finite certificate, reproduced by the accompanying standalone program, verifies the following finite combinatorial identity:
\[
\forall m\in\{1,\ldots,24\},\quad
\forall r\in\{0,\ldots,m-1\},\quad
\bigl(\exists a<2m:T_a\equiv r\pmod m\bigr)
\ \lor\ 
\bigl(\exists w\in\mathcal W:w\equiv r\pmod m\bigr).
\]
The second alternative accounts for all \(124\) modulus-residue pairs not hit by triangular numbers. Each class modulo every \(m\le24\) therefore contains an explicitly identified index at which \(s_1\) is nonzero modulo eight, and hence cannot be universal.

**Excluding the other residues at modulus 25.** The nonzero coefficient witnesses for the remaining \(21\) residue classes are, respectively, the following mapping \(r\mapsto w_r\):
\[
\begin{array}{c|rrrrrrrr}
r&0&1&2&3&4&5&6&7\\\hline
w_r&0&1&2&3&4&5&6&7
\end{array}
\]
\[
\begin{array}{c|rrrrrrrrrrrrr}
r&9&10&11&12&14&15&16&17&19&20&21&22&24\\\hline
w_r&9&10&36&12&39&15&16&17&44&45&21&22&24
\end{array}
\]
Every displayed witness satisfies \(w_r\equiv r\pmod{25}\) and \(s_1(w_r)\not\equiv0\pmod8\), by the same exact coefficient calculation. The only remaining residues are \(8,13,18,23\), already proved universal. This completes the classification. \(\square\)

## Verification

The accompanying `verify.py` is standalone Python 3 with no dependencies. It computes \(s_1(n)\bmod8\) for all \(0\le n\le500\) using polynomial truncation of the defining product, independently computes the same coefficients from Liu and Xia's identities (2.9) and (3.1), and asserts agreement at every index. It then verifies all eighteen \(\mathcal W\) values equal four modulo eight, all finite triangular-or-witness coverings for \(m\le24\), and all twenty-one modulus-25 exclusion witnesses. The output is recorded in `verification_output.txt`. Because this is a finite certificate for a genuinely finite coverage assertion, and because each witness is checked by exact coefficient arithmetic, there is no sampling-to-infinity step in the negative proof. The positive infinite congruences depend on the published theorem [2].

## Relationship to prior work

Andrews and El Bachraoui [1] identify the series, its composition interpretation, and the triangular-number modulo-four dichotomy. Liu and Xia [2] prove the four modulo-eight progressions as a special case of their broader prime-power theorem. Neither work, in its inspected available full text, classifies *all* possible smaller progression moduli or determines whether the four residue classes exhaust modulus \(25\). The new claim is precisely that optimality and exhaustiveness statement; the published four congruences are not claimed as newly discovered. Another July 2026 paper concerning the associated companion series [3] was checked at abstract level only, creating residual bibliographic risk.

## Limitations

No assertion is made for moduli above \(25\), and the minimality certificate is specific to the function defined above and to congruence modulo eight. The source-backed infinite positive congruences have not been independently re-proved here. Primary-text inspection and semantic searches do not exclude unindexed equivalent work; scientific priority remains subject to outside verification. The finite certificate is not a computation of infinitely many sequence values.

## References

[1] G. E. Andrews and A. El Bachraoui, *On a two-color partition series and its companions*, arXiv:2606.30208v1 (29 June 2026), https://arxiv.org/abs/2606.30208 .

[2] E. H. Liu and E. X. W. Xia, *A proof of Andrews-El Bachraoui's conjecture on the parity of coefficients of a q-series*, arXiv:2607.07145v1 (8 July 2026), https://arxiv.org/abs/2607.07145 . See Theorems 1.1 and 1.4, formulas (2.9) and (3.1).

[3] T. Dhar, M. Goswami and S. K. Tripathi, related preprint on the companion series, arXiv:2607.10576 (July 2026); abstract-level comparison only.
