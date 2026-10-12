# Exact all-prefix scattered-subsequence universality of the ternary Thue difference word

## Finding

For the ternary difference word \(x(n)=1+t(n)-t(n+1)\), where \(t(n)\) is the Thue–Morse digit-parity word, every prefix has an exact scattered-subsequence universality index. If \(N=16k+r\), with integers \(k\ge0\) and \(0\le r<16\), then

\[
U(N)=5k+\left\lfloor\frac r3\right\rfloor+
\mathbf 1_{\{k\ge1,\ r=2,\ t(k-1)\ne t(k)\}}.
\]

In particular \(U(16k)=5k\), and
\[
-10\le16U(N)-5N\le6,\qquad
\lim_{N\to\infty}\frac{U(N)}N=\frac5{16}.
\]
Both discrepancy extrema occur infinitely often. The shortest absent subsequence of each prefix consequently has length \(U(N)+1\).

## Assumptions and scope

Throughout, \(t(n)=s_2(n)\bmod2\) for \(n\ge0\), where \(s_2\) denotes the sum of binary digits. Define \(x(n)=1+t(n)-t(n+1)\) for \(n\ge0\); its values are in \(\{0,1,2\}\). This is a standard difference coding of the ternary square-free Thue word (also the fixed point of \(0\mapsto012,\ 1\mapsto02,\ 2\mapsto1\)). Only the explicit difference definition is needed here. For \(N\ge0\), write \(X_N=x(0)\cdots x(N-1)\). A scattered subsequence of a word is obtained by deleting letters without changing the order of those retained. \(U(N)\) is the largest \(m\ge0\) for which every word in \(\{0,1,2\}^m\) is a subsequence of \(X_N\). This is not a claim about contiguous factors or circular universality.

## Proof

**Arch characterization.** An arch is a shortest initial segment containing every letter in \(\{0,1,2\}\). Repeatedly remove the shortest such segment until the remaining suffix omits some letter. The number of removed arches equals the scattered-subsequence universality index; this standard characterization is in Barker et al. and Schnoebelen–Veron. We calculate that arch count without extrapolation.

**Four aligned templates.** The Thue–Morse recurrence gives \(t(8j+i)=t(j)\oplus t(i)\) for \(0\le i<8\), with the eight digits \((0,1,1,0,1,0,0,1)\); also \(t(8j+8)=t(j+1)\). For \(0\le i<8\),
\[
x(16j+2i)=2t(8j+i),\qquad
x(16j+2i+1)=2-t(8j+i)-t(8j+i+1).
\]
Hence the aligned 16-letter block depends only on \((t(j),t(j+1))\). The four possibilities, obtained by substitution in these displayed identities, are

| Pair \((t(j),t(j+1))\) | Block \(x(16j)\cdots x(16j+15)\) |
|:---:|:---|
| \((0,0)\) | `0120210121020121` |
| \((0,1)\) | `0120210121020120` |
| \((1,0)\) | `2102012101202102` |
| \((1,1)\) | `2102012101202101` |

**Finite state certificate.** Represent the set of letters seen since the latest completed arch by a 3-bit mask. On reading letter \(z\), replace the mask by its union with \(\{z\}\); if it is all three letters, count one arch and reset the mask to empty. Direct inspection of the four explicit blocks shows that each contributes **exactly five** arches for *every one of the eight possible incoming masks*. Moreover, for every incoming singleton mask, the exiting mask is the singleton containing the block's last letter. These are sixteen-symbol finite assertions, independently reproduced exhaustively by the included `verify.py`.

At the beginning, the first block has pair \((t(0),t(1))=(0,1)\), starts with empty mask, contributes five arches, and leaves the singleton \(\{0\}\). Inductively every complete aligned block contributes five arches and leaves a singleton: the last letter of the most recent block. Thus \(U(16k)=5k\) for all \(k\ge0\).

For \(k\ge1\), the incoming singleton to the next block is its predecessor's final letter, equal to \(1+t(k-1)-t(k)\), as read from the four-block table. The current block depends on \((t(k),t(k+1))\). There are just six possible triples of consecutive Thue–Morse letters: `001`, `010`, `011`, `100`, `101`, `110`. Indeed, the recurrences \(t(2j+1)=1-t(j)\) and \(t(2j)=t(j)\) rule out `000` and `111` at both parities. The complete finite prefix-scan certificate is:

| Triple \((t(k-1),t(k),t(k+1))\) | Arches completed in the first \(r\) letters, \(0\le r<16\) |
|:---:|:---|
| `001`, `110` | \(\lfloor r/3\rfloor\) |
| `010`, `011`, `100`, `101` | \(\lfloor r/3\rfloor+\mathbf1_{\{r=2\}}\) |

Both lines follow by scanning the actual 16-letter words with the specified singleton input; no conjectural recurrence is used. For the initial partial block (\(k=0\)) the count is \(\lfloor r/3\rfloor\). Adding five for every preceding complete block proves the claimed formula for all \(N\ge0\).

**Sharp discrepancy.** Substituting the formula gives
\[
16U(N)-5N=16\lfloor r/3\rfloor-5r+
16\mathbf1_{\{k\ge1,\ r=2,\ t(k-1)\ne t(k)\}}.
\]
Checking \(0\le r<16\) yields the sharp interval \([-10,6]\). At \(r=2\), the value is \(-10\) when \(t(k-1)=t(k)\) and \(6\) when they differ. Both alternatives occur infinitely often: for every \(j\ge0\), \(t(4j+1)=t(4j+2)=1-t(j)\), whereas \(t(4j)\ne t(4j+1)\). Take respectively \(k=4j+2\) and \(k=4j+1\). Finally, bounded discrepancy implies the limiting density \(5/16\).

## Verification

Run `python3 verify.py` with Python 3.9 or newer. It exhausts the four 16-symbol blocks against all eight input masks, checks all six admissible three-bit contexts and every partial prefix of each template, independently generates the difference word and a long prefix of the ternary Thue morphism, checks the formula at every one of those positions, compares explicit subsequences of short prefixes, and tests the extremal discrepancies. Expected output starts with `VERIFY_OK`. The symbolic four-block calculation and the six finite context cases constitute the infinite proof; numerical prefix checks only corroborate it.

## Relationship to prior work

Barker et al. introduced scattered-factor universality and the arch characterization. Schnoebelen and Veron develop compositional arch signatures and algorithms for compressed words. Adamson et al. determine extremal counts of absent subsequences over finite words at prescribed universality index. These algorithms and extremal bounds neither specify the ternary Thue difference word nor yield the displayed exact 16-residue formula and sharp all-prefix discrepancy without a new word-specific analysis. This theorem credits the general arch method and contributes the word-specific complete evaluation.

## Limitations

The invariant concerns ordinary order-preserving subsequences of prefixes, not contiguous factors, cyclic rotations, arbitrary factors of the infinite word, or minimal absent-subsequence multiplicities. The ternary word is fixed by its explicit digit-difference definition. Verification is a finite certificate of the symbolic block reduction and does not claim independent review. Prior equivalent work not indexed by the sources consulted remains a bibliographic possibility.

## References

1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words* (2020), arXiv:2003.04629, https://arxiv.org/abs/2003.04629.
2. Ph. Schnoebelen, J. Veron, *On arch factorization and subword universality for words and compressed words* (first public 2023-04-24), arXiv:2304.11932, https://arxiv.org/abs/2304.11932.
3. D. Adamson, P. Fleischmann, A. Huch, F. Manea, P. Sarnighausen-Cahn, M. Wiedenhöft, *Tight Bounds for the Number of Absent Subsequences* (first public 2024-07-26), arXiv:2407.18599, https://arxiv.org/abs/2407.18599.
