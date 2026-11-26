# Shortest atypicality witnesses for the three generating Thue–Morse atypical words

## Finding

Let \(\mathbf t\) be the Prouhet–Thue–Morse word, let \(\mu(a)=ab\), \(\mu(b)=ba\), and let \(\xi\) exchange \(a\) and \(b\). For a finite factor \(w\) of \(\mathbf t\), define
\[
\kappa(w)=\min_{\varphi}|\varphi(w)|,
\]
where \(\varphi\) ranges over nonerasing endomorphisms of \(\{a,b\}^{+}\) for which \(\varphi(w)\) is again a contiguous factor of \(\mathbf t\), excluding \(\{\mu^n,\xi\circ\mu^n:n\ge 0\}\).

For the three factors that generate the atypical factors in Almeida and Klíma's classification, the minima and all minimizing pairs up to simultaneous output complementation are:

| \(w\) | \(\kappa(w)\) | \(\varphi(a)\) | \(\varphi(b)\) | \(\varphi(w)\) |
|---|---:|---|---|---|
| `aabab` | 13 | `a` | `bbaab` | `aabbaababbaab` |
| `abaaba` | 8 | `a` | `bb` | `abbaabba` |
| `aabbaab` | 13 | `a` | `bab` | `aababbabaabab` |

Thus the length-17 witness displayed in the source for `aabab` can be replaced by a length-13 witness, and no shorter image works. Each of the other two lengths is already attained by the source witness, and here is shown optimal and attained by just one complement pair.

## Assumptions and scope

The source classification says that, up to reversal and letter exchange, every atypical word is a factor of one of these three words. Its characterization of the monoid of globally language-preserving morphisms gives precisely the excluded maps above: \(\xi\) and \(\mu\) commute and \(\xi^2\) is the identity. The minima here measure witnesses of local atypicality for the three generators, not for all their proper factors.

## Proof

Encode \(a=0\), \(b=1\). The three displayed images are `0011001011001`, `01100110`, and `0010110100101`, respectively. They occur starting at zero-based indices 29, 20, and 9 in \(\mathbf t\), respectively. Each map has unequal image lengths on the two letters, so none is a power of \(\mu\) or its composition with \(\xi\).

For the lower bounds, if \(w\) contains \(A\) copies of \(a\) and \(B\) copies of \(b\), then image lengths \(r=|\varphi(a)|\ge1\) and \(s=|\varphi(b)|\ge1\) give \(|\varphi(w)|=Ar+Bs\). Any witness shorter than or tied with a displayed one therefore occurs among finitely many integer pairs \((r,s)\). For each pair there are \(2^{r+s}\) ordered assignments of images. By Proposition 2.1 of the source, a word of length \(L\ge3\) occurs in \(\mathbf t\) if and only if it occurs in \(\mu^{2+\lceil\log_2(L-1)\rceil}(a)\). At lengths up to 13 the longest such prefix is \(\mu^6(a)\).

Exhaustion of these finite domains considers 228, 12, and 36 image assignments, respectively, before filtering out the globally language-preserving maps. No unexcluded assignment with an image in the factor language occurs below the displayed lengths; at each displayed length, the two assignments that remain are the one in the table and its simultaneous output complement.

## Verification

Run `python3 verify.py` beside `certificate.json`. The verifier exhausts the ordered assignments through each stated minimum and checks membership by the exact bounded-prefix test, also comparing those finite factor sets against direct generation by parity of binary digit sums through a prefix of length 2048. The exact binary images and the complete set of tied witnesses are recorded in `certificate.json`.

The factor membership computation can also be checked by splitting the fixed point into consecutive length-16 substitution blocks. A factor of length at most 13 meets at most two blocks. All four adjacent pairs of block types occur in \(\mu^3(a)\), so its length-128 expansion \(\mu^7(a)\) contains every factor needed in the finite search. For each feasible pair \((r,s)\), cut each factor of length \(Ar+Bs\) into the consecutive image slots dictated by \(w\), and keep it only if the slots for each given letter are identical. This is equivalent to enumerating all assignments followed by the factor test.

## Relationship to prior work and limitations

Almeida and Klíma's Theorem 4.3 classifies the atypical words and gives witnesses fixing \(a\) and sending \(b\) respectively to `bbabaab`, `bb`, and `bab`. These yield image lengths 17, 8, and 13. The theorem does not state exact minimum lengths or classify the ties. The three shortest-image calculations use the source's finite recognition bound and global monoid characterization, but these do not give the minima without the local search. No general formula for \(\kappa\) and no classification of proper atypical factors by witness length is asserted.

## Reference

J. Almeida and O. Klíma, “Binary patterns in the Prouhet–Thue–Morse sequence,” *Discrete Mathematics & Theoretical Computer Science* 23(3), 2021, DOI: 10.46298/dmtcs.5460; arXiv:1904.07137.
