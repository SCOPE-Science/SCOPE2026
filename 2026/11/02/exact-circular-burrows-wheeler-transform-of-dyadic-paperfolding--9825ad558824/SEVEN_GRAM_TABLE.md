# Complete seven-factor local enumeration

For the binary macroblocks in `RESULT.md`, set \(q=2^{k-5}\), with \(k\ge6\). Each row lists the unique seven-letter prefix, all possible start offsets modulo sixteen, its total cyclic multiplicity, and the predecessor-string block in lexicographic rotation order. The four mixed entries are proved by the longer-lookahead and recursive arguments in `RESULT.md`. The other entries are constant predecessor strings. This table is obtained exhaustively from the four explicit macrotypes and sixteen offsets; each type occurs \(r,r,r-1,r+1\) times with \(r=q/2\).

| Seven-factor | Offsets | Multiplicity | Preceding letters after sorting |
|---|---|---|---|
| `0001100` | `5` | \(q\) | \(1^{q}\) |
| `0001101` | `13` | \(q-1\) | \(1^{q-1}\) |
| `0010001` | `10` | \(q-1\) | \(1^{q-1}\) |
| `0010011` | `10` | \(q+1\) | \(1^{q+1}\) |
| `0011001` | `6` | \(q\) | \(0^{q}\) |
| `0011011` | `14` | \(q-1\) | \(0^{q-1}\) |
| `0011100` | `5` | \(q\) | \(1^{q}\) |
| `0011101` | `13` | \(q+1\) | \(1^{q+1}\) |
| `0100011` | `11` | \(q-1\) | \(0^{q-1}\) |
| `0100111` | `11` | \(q+1\) | \(0^{q+1}\) |
| `0110001` | `2` | \(q\) | \(1^{q}\) |
| `0110010` | `7` | \(q\) | \(0^{q}\) |
| `0110011` | `2` | \(q\) | \(1^{q}\) |
| `0110110` | `15` | \(q-1\) | \(0^{q-1}\) |
| `0111001` | `6` | \(q\) | \(0^{q}\) |
| `0111011` | `14` | \(q+1\) | \(0^{q+1}\) |
| `1000110` | `4,12` | \(2q-1\) | \(1^q0^{q-1}\) |
| `1001000` | `9` | \(q-1\) | \(1^{q-1}\) |
| `1001001` | `9` | \(q+1\) | \(1^{q+1}\) |
| `1001110` | `4,12` | \(2q+1\) | \(1^q0^{q+1}\) |
| `1011000` | `1` | \(q\) | \(1^{q}\) |
| `1011001` | `1` | \(q\) | \(1^{q}\) |
| `1100011` | `3` | \(q\) | \(0^{q}\) |
| `1100100` | `8` | \(2q\) | \(A_{k+1}\) |
| `1100111` | `3` | \(q\) | \(0^{q}\) |
| `1101100` | `0` | \(2q\) | \(B_k\) |
| `1110010` | `7` | \(q\) | \(0^{q}\) |
| `1110110` | `15` | \(q+1\) | \(0^{q+1}\) |

For the two factors starting at offsets `4` and `12`, the eighth bit distinguishes the two predecessor classes. For offset `8` the eighth and sixteenth bits distinguish classes. At offset `0` the sorting of full shorter-word rotations gives the recursive block. The table is a mathematical finite-case certificate, not a substitute for the unrestricted argument.
