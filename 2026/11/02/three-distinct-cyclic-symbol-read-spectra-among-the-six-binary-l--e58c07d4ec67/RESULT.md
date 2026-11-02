# Three distinct cyclic symbol-read spectra among the six binary length-31 Hamming codes

## Finding

Let \(\mathcal P\) be the six degree-five primitive binary polynomials, encoded by the integer masks

\[
\mathcal P=\{\mathtt{0x25},\mathtt{0x29},\mathtt{0x2f},\mathtt{0x37},\mathtt{0x3b},\mathtt{0x3d}\}.
\]

For each \(p\in\mathcal P\), let \(\alpha\) denote the residue of \(x\) in \(\mathbb F_2[x]/(p)\), and define

\[
C_p=\left\{(c_0,\ldots,c_{30})\in\mathbb F_2^{31}:\ \sum_{i=0}^{30}c_i\alpha^i=0\right\}.
\]

For each \(b\in\{2,3,4\}\), define the cyclic symbol-read weight and enumerator by

\[
w_b(c)=\left|\{i\in\mathbb Z/31\mathbb Z:(c_i,c_{i+1},\ldots,c_{i+b-1})\ne(0,\ldots,0)\}\right|,
\qquad W_{p,b}(z)=\sum_{c\in C_p}z^{w_b(c)}.
\]

The file `spectra.json` specifies, in full and with exact integer coefficients, all eighteen polynomials \(W_{p,b}\), indexed by the polynomial masks and \(b\). For each fixed \(b\), precisely three distinct enumerators occur; the pairs of equal enumerators are

\[
(\mathtt{0x25},\mathtt{0x29}),\quad
(\mathtt{0x2f},\mathtt{0x3d}),\quad
(\mathtt{0x37},\mathtt{0x3b}).
\]

The following *certified distinguishing coefficients* display why there are three types for each read length. In the table, \(A_j\) is the coefficient of \(z^j\).

| Read length | Polynomial representative | First separating coefficients |
| --- | --- | --- |
| \(b=2\) | `0x25` | \(A_9=3193,\ A_{12}=47027\) |
| \(b=2\) | `0x2f` | \(A_9=3131,\ A_{12}=48019\) |
| \(b=2\) | `0x37` | \(A_9=3131,\ A_{12}=48205\) |
| \(b=3\) | `0x25` | \(A_8=62,\ A_{10}=558\) |
| \(b=3\) | `0x2f` | \(A_8=93,\ A_{10}=465\) |
| \(b=3\) | `0x37` | \(A_8=93,\ A_{10}=496\) |
| \(b=4\) | `0x25` | \(A_{10}=62,\ A_{11}=186\) |
| \(b=4\) | `0x2f` | \(A_{10}=62,\ A_{11}=217\) |
| \(b=4\) | `0x37` | \(A_{10}=93,\ A_{11}=155\) |

All six codes are coordinate-permutation equivalent as ordinary binary \([31,26,3]\) Hamming codes, but their natural cyclic coordinate orders induce these genuinely different symbol-read spectra.

## Assumptions and scope

A polynomial mask encodes its coefficients in increasing exponent order: for instance `0x25` encodes \(x^5+x^2+1\). Coordinates are indexed in the order of powers \(1,\alpha,\ldots,\alpha^{30}\), and all cyclic windows wrap around the end. Codewords are binary; the parity-check equation is in a field of thirty-two elements. This concerns exactly the six primitive cyclic Hamming-code realizations and exactly the three read lengths \(b=2,3,4\), not arbitrary coordinate reorderings.

## Proof

**1. Exhaustiveness of the polynomial family.** All monic degree-five polynomials over \(\mathbb F_2\) having constant term one have masks \(\mathtt{0x21},\mathtt{0x23},\ldots,\mathtt{0x3f}\). Multiplication of the residue \(\alpha\) by itself, with reduction modulo each mask, yields multiplicative period thirty-one for exactly the six masks listed above; `verify.py` checks all sixteen odd masks, not only the candidates. Because the multiplicative order of two modulo thirty-one is five, any root of multiplicative order thirty-one has minimal polynomial of degree five over \(\mathbb F_2\). Hence a monic degree-five polynomial annihilating such a residue must be irreducible, and each listed quotient is \(\mathbb F_{32}\). The columns \(1,\alpha,\ldots,\alpha^{30}\) are all nonzero field elements, so the displayed parity-check system has rank five and defines a binary \([31,26,3]\) Hamming code. Conversely, every primitive degree-five polynomial occurs in the checked list.

**2. Exact coefficient recurrence.** Fix a listed polynomial, set \(n=31\), and write \(h_i=\alpha^i\) as a five-bit field coordinate vector. For fixed \(b\) and initial prefix \(u\in\{0,1\}^{b-1}\), start with one state recording (i) syndrome \(s=\sum_{j=0}^{b-2}u_jh_j\), (ii) the last \(b-1\) bits \(t=u\), and (iii) read weight zero. Appending bit \(a\in\{0,1\}\) at position \(i\), for \(b-1\le i<n\), gives the exact transition

\[
(s,t,w)\longmapsto\bigl(s+ah_i,\ \operatorname{shift}(t,a),\ w+\mathbf1_{(t,a)\ne0}\bigr).
\]

All additions of syndromes are over \(\mathbb F_2^5\); identical states accumulate integer counts. After position thirty, retain precisely those states with zero syndrome, and add the number of nonzero windows formed by the last \(b-1\) bits followed by the fixed first \(b-1\) bits. Summing over all \(2^{b-1}\) prefixes gives exactly the coefficient of every \(z^j\), because every cyclic word is visited once and every cyclic \(b\)-window is counted once. This proves the coefficient extraction performed by `verify.py` and specifies finite arithmetic and iteration bounds without any probabilistic assumptions.

**3. Independent coefficient calculation.** In the dual calculation `crosscheck.py`, the zero-syndrome filter is replaced by character orthogonality:

\[
\mathbf 1_{\sum c_ih_i=0}=\frac1{32}\sum_{t\in\mathbb F_2^5}(-1)^{\langle t,\sum c_ih_i\rangle}.
\]

For each character, a signed transfer recurrence tracks only the trailing \(b-1\) bits and the accrued read weight, then adds the cyclic boundary windows. Dividing the sum of all thirty-two signed character counts by thirty-two gives the same eighteen integer arrays. This method does not maintain the syndrome-state counts of step 2. In the smaller degree-three and degree-four primitive-code cases, the second verifier additionally iterates every binary word, filters its syndrome, and counts cyclic reads directly. Both complete verifiers return the success labels stated in `VERIFICATION.md`.

**4. Equality and inequivalence.** Coordinate reversal maps the zero equation for \(p\) to that for its reciprocal polynomial, and preserves cyclic \(b\)-window weight, explaining the three equal pairs. The coefficients shown in the finding table separate the remaining three representatives for each of the three read lengths. Since the primitive-polynomial list is exhaustive, these are all the possible spectrum types.

As an additional exact invariant, every coefficient array sums to \(2^{26}\), has constant term one, and has first weighted moment

\[
\sum_{j=0}^{31}jA_j=31\left(2^{26}-2^{26-b}\right).
\]

This follows because any \(b\le4\) consecutive parity-check columns are linearly independent, making their \(b\)-bit projection uniform. The verifier checks all eighteen instances.

## Verification

The complete arrays are in `spectra.json`. Run `python3 verify.py` and `python3 crosscheck.py` from the same directory using Python 3.10 or later and only the standard library. Both programs recompute the arrays from the defining field arithmetic and compare *every* coefficient. `verify.py` also checks polynomial completeness, reciprocal pairs, distinctness, dimensions, and the first-moment invariants. `crosscheck.py` uses signed character sums and separately performs exhaustive direct-word checks at smaller field dimensions. Expected outputs are exactly `VERIFY_OK` and `CROSSCHECK_OK`.

## Relationship to prior work

Cassuto and Blaum introduced symbol-pair read channels in a 2010 conference publication, and Yaakobi, Bruck and Siegel extended cyclic read metrics to larger windows in 2016. Ma and Luo (2019) calculate complete distributions for MDS and simplex codes; their simplex results concern the *dual* of the present Hamming codes, not the complete distributions of the Hamming codes. Liu and Pan (2021), Section 7, give generalized symbol-read weight hierarchies for two lexicographically ordered small Hamming examples, not the full distribution of the six primitive length-31 cyclic realizations. Shi, Özbudak and Solé (2021), Sections IV and V, establish bounds for general cyclic codes and specialized enumerators for codes with a single nonzero cyclotomic coset; their exact-enumerator hypotheses do not apply to the dimension-26 Hamming codes here, and their stability theorem requires \(b\ge26\), unlike \(b\in\{2,3,4\}\). The Hamming polynomial in the defining equation is the *generator* polynomial, not an irreducible parity-check polynomial, so complete irreducible cyclic-code enumerator theorems do not automatically apply. A previously indexed note on symbol-pair *generation* of primitive Hamming codes does not provide these coefficient multiplicities. The present claim is the explicit exhaustive length-31 cyclic classification and its observed three-way split, not a novel general definition or metric inequality.

## Limitations

The result is a finite, fully reproducible classification at binary length thirty-one and read lengths two through four. It does not give an all-length symbolic formula, classify all coordinate permutations, or establish priority over unindexed historical tables. Its review is not an independent scientific audit. The two counting programs are arithmetic evidence for their precisely stated finite loops, not a claim of external formal certification.

## References

1. Y. Cassuto and M. Blaum, *Codes for symbol-pair read channels*, IEEE ISIT 2010, DOI: 10.1109/ISIT.2010.5513753, publicly indexed July 23, 2010; expanded IEEE Trans. Inf. Theory 57 (2011), DOI: 10.1109/TIT.2011.2164891.
2. E. Yaakobi, J. Bruck and P. H. Siegel, *Constructions and decoding of cyclic codes over b-symbol read channels*, IEEE Trans. Inf. Theory 62 (2016), 1541–1551, DOI: 10.1109/TIT.2016.2522434.
3. J. Ma and J. Luo, *Symbol-pair weight distributions of some linear codes*, arXiv:1911.02184 (2019), https://arxiv.org/abs/1911.02184.
4. H. Liu and X. Pan, *Generalized b-symbol weights of linear codes and b-symbol MDS codes*, arXiv:2103.16299 (2021), https://arxiv.org/abs/2103.16299.
5. M. Shi, F. Özbudak and P. Solé, *Geometric approach to b-symbol Hamming weights of cyclic codes*, IEEE Trans. Inf. Theory 67 (2021), 3735–3751, DOI: 10.1109/TIT.2021.3069772.
6. G. Vega, *The b-symbol weight distributions of all semiprimitive irreducible cyclic codes*, Designs, Codes and Cryptography 91 (2023), 2213–2221, DOI: 10.1007/s10623-023-01193-w.
