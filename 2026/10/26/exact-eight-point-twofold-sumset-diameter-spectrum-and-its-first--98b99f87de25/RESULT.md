# Exact eight-point twofold-sumset diameter spectrum and its first monotonicity reversal

## Finding

For a finite integer set \(A\), write \(2A=\{a+a':a,a'\in A\}\) and \(\operatorname{diam}(A)=\max A-\min A\). For integers \(k\ge2\) and \(2k-1\le t\le k(k+1)/2\), define
\[
 d_k(t)=\min\{\operatorname{diam}(A):A\subseteq\mathbb Z,\ |A|=k,\ |2A|=t\}.
\]
The exact minimum-diameter profiles for every \(2\le k\le8\) are as follows. Each vector is indexed by consecutive values of \(t\) beginning at \(2k-1\).

| Cardinality \(k\) | Consecutive \(t\) values | Exact \(d_k(t)\) vector | Maximum search diameter | Normalized sets checked |
| ---: | :--- | :--- | ---: | ---: |
| 2 | 3–3 | 1 | 1 | 1 |
| 3 | 5–6 | 2, 3 | 3 | 3 |
| 4 | 7–10 | 3, 4, 4, 6 | 6 | 20 |
| 5 | 9–15 | 4, 5, 5, 6, 6, 8, 11 | 11 | 330 |
| 6 | 11–21 | 5, 6, 6, 7, 7, 8, 8, 10, 10, 13, 17 | 17 | 6,188 |
| 7 | 13–28 | 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 12, 14, 14, 16, 21, 25 | 25 | 177,100 |
| 8 | 15–36 | 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 15, 15, 16, 17, 20, 19, 25, 28, 34 | 34 | 5,379,616 |

The profiles are nondecreasing through \(k=7\), but at \(k=8\) the first strict reversal occurs:
\[
 d_8(32)=20>19=d_8(33).
\]
Explicit minimum-span witnesses are \(A_{32}=\{0,1,3,4,9,11,16,20\}\) and \(A_{33}=\{0,1,3,7,12,16,18,19\}\); their twofold sumsets have exactly \(32\) and \(33\) elements respectively. The smallest single interval in which all attainable eight-point twofold-sumset sizes occur has length \(34\), namely \(N(2,8)=34\) under the interval normalization \([0,N]\). The maximum-size endpoint is witnessed by the classical eight-mark Golomb ruler \(\{0,1,4,9,15,22,32,34\}\), which has \(|2A|=36\); the optimal ruler length itself was known previously.

## Assumptions and scope

All sets are ordinary subsets of the integers, without repeated elements. The twofold sumset includes diagonal sums and ignores multiplicity. The term “diameter” means numerical span, not number of distinct gaps or scale-normalized affine diameter. Translation does not change \(|2A|\) or diameter; hence every minimizing set may be translated to minimum zero. The result is an exact finite classification for \(2\le k\le8\), not a general theorem for arbitrary \(k\).

## Proof

**Exhaustive finite certificate.** Fix \(k\) and the certified search limit \(L_k\) from the table. Every translated integer \(k\)-set with diameter at most \(L_k\) occurs uniquely among
\[
 \{0=a_0<a_1<\cdots<a_{k-1}\le L_k\}.
\]
There are exactly \(\binom{L_k}{k-1}\) choices. These are \(1,3,20,330,6188,177100,5379616\) choices, respectively, for \(k=2,3,4,5,6,7,8\). The included `enumerate.cpp` recursively enumerates all choices, computes the cardinality of the set of unordered sums \(a_i+a_j\) for \(0\le i\le j<k\), and records the smallest last entry for each cardinality. The generated integer-only profile, counts, and actual witnesses are recorded in `spectrum.json`.

An independent implementation, `independent.cpp`, enumerates those normalized subsets separately and uses integer-marked sum occurrences rather than the primary algorithm's two-word bitset. For each \(k\) its resulting minimum-diameter vector and total count agree exactly with the first implementation, and `verify.py` compares the resulting vectors against every entry of `spectrum.json` and checks the witness sums directly. The finite search covers all possible cardinalities \(2k-1,\ldots,k(k+1)/2\), and it gives a witness of diameter at most \(L_k\) for every such cardinality. Therefore a hypothetical set with a smaller span than the listed minimum would be translated into one of the exhaustively examined sets, contradicting the recorded minimum. The conclusion is not based on extrapolation beyond the enumerated range.

Reading the certified vectors shows that the entries are nondecreasing for \(k\le7\), whereas the only strict downward step for \(k=8\) is \(20\) to \(19\) when \(t\) increases from \(32\) to \(33\). Finally, the maximum of the complete eight-point profile is \(34\). Since there is a witness for every allowable size with diameter at most \(34\), but no size-\(36\) witness with smaller diameter, the universal interval length is exactly \(34\).

## Verification

Run `python3 verify.py` in a directory containing the included `spectrum.json`, `enumerate.cpp`, and `independent.cpp`. This compiles both programs with `g++ -O3 -std=c++17`, performs the two full integer enumerations, checks each of the seven vectors and all stored witnesses, and asserts the first and only reversal up to cardinality eight. Its actual successful output was:

```
VERIFY_OK independent_enumerations=2 total_scanned=5563258 first_drop=k8_at_32_to_33 universal_N_2_8=34
```

The loops are exhaustive because after translation each allowable set is a strictly increasing \((k-1)\)-tuple of integers from \(1\) to \(L_k\). The largest enumerated sum is \(68\), within the primary implementation's exact 128-bit two-word set and the independent implementation's marker range. This is an exhaustive finite proof once the provided code is inspected and replayed, not a random-sampling or asymptotic argument.

## Relationship to prior work

Nathanson's July 2026 study of the sumset-size problem for integer and lattice subsets motivates the search for minimum interval lengths supporting all prescribed sumset cardinalities. Rajagopal's work establishes the attainable cardinality range in the twofold case; attainability by itself does not determine optimal diameters. Nathanson's earlier compression work provides general bounded-diameter reductions, but its accessible summary does not supply the present exact seven profiles. The classical optimal eight-mark Golomb ruler establishes the already-known endpoint \(d_8(36)=34\), not the remaining minimum-diameter vector or the strict descent \(d_8(32)>d_8(33)\). The claimed contribution is precisely the complete small-cardinality inverse profile and its first monotonicity reversal, not the earlier coverage theorem or optimal Golomb-ruler length.

## Limitations

Only cardinalities at most eight are classified. The total number of sets is counted after translation, not after quotienting by reflection or dilation; that choice does not change the minima. No general monotonicity criterion, closed formula in arbitrary cardinality, or claim of computational efficiency for growing cardinality is established. Related compression literature has an inaccessible full text in this comparison, leaving a residual bibliographic priority risk. Independent scientific audit has not been performed.

## References

1. M. B. Nathanson, *A problem on sumset sizes of sets of lattice points*, arXiv:2607.20571, first posted 21 July 2026. https://arxiv.org/abs/2607.20571
2. I. Rajagopal, *Possible Sizes of Sumsets*, Discrete Analysis (2026), arXiv:2510.23022. https://arxiv.org/abs/2510.23022
3. M. B. Nathanson, *Compression and complexity for sumset sizes in additive number theory*, Journal of Number Theory 281 (2026), 321–343, arXiv:2505.20998. https://arxiv.org/abs/2505.20998
4. M. B. Nathanson, *Inverse problems for sumset sizes of finite sets of integers*, Fibonacci Quarterly 64 (2026), 70–82, arXiv:2412.16154. https://arxiv.org/abs/2412.16154
5. Classical optimal Golomb-ruler tables, eight marks and span 34 (not claimed new). https://en.wikipedia.org/wiki/Golomb_ruler
