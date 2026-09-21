# Exact q=9 linear strong AONT size via cyclic difference packing

## Result

For a prime power \(q\), let \(M_R([1,2],q)\) be the largest \(s\) for which there exists a linear \((2,s,q)\)-strong all-or-nothing transform. Equivalently, there is an invertible \(s\times s\) matrix over \(\mathbb F_q\) for which every \(1\times1\) and every \(2\times2\) submatrix is invertible.

Then

\[
\boxed{M_R([1,2],9)=6.}
\]

The previously published bounds were \(6\le M_R([1,2],9)\le7\). Thus the remaining size-seven case is impossible.

A supporting extremal result is also obtained. In the standard notation for cyclic difference packing arrays,

\[
\boxed{\max\{k:\operatorname{CDPA}(k,7;8)\text{ exists}\}=4.}
\]

Here a \(\operatorname{CDPA}(k,7;8)\) is a \(k\times7\) array over \(\mathbb Z_8\) such that for every two distinct rows the seven coordinatewise differences are pairwise distinct.

## Reduction from a size-seven strong AONT

Suppose that a \(7\times7\) matrix \(M\) over \(\mathbb F_9\) has no zero entries and all of its \(2\times2\) minors are nonzero. The contradiction below does not require the additional hypothesis that \(M\) itself is invertible.

Scale columns and then rows by nonzero field elements so that the first row and first column are all 1. These scalings preserve zero versus nonzero status of every minor. Fix a primitive element \(\alpha\in\mathbb F_9^*\), whose multiplicative group has order 8, and write

\[
M_{ij}=\alpha^{d_{ij}},\qquad d_{ij}\in\mathbb Z_8.
\]

The first row and first column of the exponent array \(D=(d_{ij})\) are zero.

For any nonfirst row \(i\), compare that row with the first row. A \(2\times2\) minor in columns \(j\ne k\) is nonzero exactly when

\[
\alpha^{d_{ij}}\ne\alpha^{d_{ik}}.
\]

Hence the seven entries of row \(i\) of \(D\) are pairwise distinct. Since its first entry is zero, its other six entries are six distinct nonzero residues of \(\mathbb Z_8\).

More generally, for two rows \(i\ne h\), the minor in columns \(j\ne k\) is nonzero exactly when

\[
d_{ij}-d_{hj}\not\equiv d_{ik}-d_{hk}\pmod 8.
\]

Thus the seven coordinatewise differences between every pair of rows are pairwise distinct. Therefore \(D\) is a \(\operatorname{CDPA}(7,7;8)\).

It remains to show that even \(\operatorname{CDPA}(5,7;8)\) cannot exist.

## Exact extremum for CDPA(k,7;8)

Any \(\operatorname{CDPA}(k,7;8)\) can be normalized without changing its defining property: subtract the first row columnwise, then subtract each row's first entry from the whole row. The first row and first column are then zero.

Every nonzero row has the form

\[
(0,r_1,\ldots,r_6),
\]

where \(r_1,\ldots,r_6\) are six distinct members of \(\{1,\ldots,7\}\). Consequently there are exactly

\[
7\cdot6!=5040
\]

possible normalized nonzero rows.

Choose one nonzero row. A permutation of the last six columns puts it into one of seven canonical forms

\[
c_m=(0,1,2,\ldots,\widehat m,\ldots,7),\qquad m\in\{1,\ldots,7\},
\]

where the hat denotes the missing residue.

For each of the seven values of \(m\), exact enumeration gives:

- exactly 64 normalized rows compatible with \(c_m\);
- exactly 24 compatible pairs among those 64 rows;
- no compatible triple among those 64 rows.

If a \(\operatorname{CDPA}(5,7;8)\) existed, after the normalization and canonicalization above its three remaining nonzero rows would have to form such a compatible triple. Hence no \(\operatorname{CDPA}(5,7;8)\) exists, and therefore no array with more than five rows exists either.

The bound is sharp because the following \(4\times7\) array is a \(\operatorname{CDPA}(4,7;8)\):

```text
0 0 0 0 0 0 0
0 2 3 4 5 6 7
0 3 5 7 2 4 6
0 5 2 6 3 7 4
```

Every pair of rows has seven distinct coordinatewise differences modulo 8. Thus the maximum number of rows is exactly 4.

The exponent-array reduction therefore rules out a \(7\times7\) strong-AONT defining matrix over \(\mathbb F_9\).

## Matching lower bound

Nasr Esfahani and Stinson exhibited a linear \((2,6,9)\)-strong AONT over
\(\mathbb F_9=\mathbb F_3[x]/(x^2+1)\) with defining matrix

\[
\begin{pmatrix}
1&1&1&1&1&1\\
1&2&x&x+1&x+2&2x\\
1&x&2&2x&2x+1&x+1\\
1&x+1&2x+2&x+2&2x&2x+1\\
1&x+2&2x&x&2x+2&2\\
1&2x&x+2&2&x+1&x
\end{pmatrix}.
\]

The verification artifact separately checks that this matrix has nonzero determinant, no zero entries, and no zero \(2\times2\) minors. Thus \(M_R([1,2],9)\ge6\), while the preceding argument gives \(M_R([1,2],9)\le6\). Therefore

\[
M_R([1,2],9)=6.
\]

## Reproducibility

`artifacts/verify.py` uses only exact integer and finite-field arithmetic. It verifies the published \(6\times6\) matrix and performs the complete normalized \(\mathbb Z_8\) enumeration described above. For every canonical missing residue it reports 64 compatible rows, 24 compatible pairs, and zero compatible triples. `artifacts/verification_output.txt` contains the verified output.

## Literature context and originality

Nasr Esfahani and Stinson introduced range/strong AONTs and proved in their Theorem 3.11 that

\[
6\le M_R([1,2],9)\le7,
\]

with the lower bound furnished by their explicit \(6\times6\) example. Their neighboring results connect strong AONT defining matrices to difference matrices through discrete logarithms, but do not resolve this \(s=q-2\) case.

Difference packing arrays were introduced by Yin (2004), and cyclic difference packing arrays were studied systematically by Yin (2005). The accessible abstract of the latter proves the general even-order column bound \(n\le q-1\) for \(k\ge3\) and gives four-row constructions at or near that bound. The present supporting result concerns the orthogonal parameter direction: at the maximum column length \(n=7\) over \(\mathbb Z_8\), the maximum number of rows is exactly four.

Targeted searches through current literature under the terms strong/range AONT, difference packing array, cyclic difference packing array, difference matrix, and the exact parameters \(q=9\) and \((k,n;q)=(5,7;8)\) found no prior resolution of either exact statement. To the best of our knowledge, the two boxed equalities above are new.

## Limitations

The nonexistence proof for five-row cyclic difference packing arrays at \((n,q)=(7,8)\) uses an exact finite enumeration after a complete symmetry reduction, rather than a parameter-uniform closed-form obstruction. The result concerns linear strong AONTs; it does not settle nonlinear variants.

The full texts of Jianxing Yin's 2004 paper *Difference packing arrays and systematic authentication codes* (DOI 10.1360/03ys0037) and 2005 paper *Cyclic Difference Packing and Covering Arrays* (DOI 10.1007/s10623-004-3991-3) were not inspected. Their accessible abstracts and indexed descriptions were checked and do not state the exact \(\operatorname{CDPA}(5,7;8)\) nonexistence result, but those papers remain the most plausible residual source of prior coverage under older terminology.

## References

1. N. Nasr Esfahani and D. R. Stinson, “Rectangular, Range, and Restricted AONTs: Three Generalizations of All-or-Nothing Transforms,” *Advances in Mathematics of Communications* 18(1) (2024), 26–38. DOI: https://doi.org/10.3934/amc.2021068. Preprint: https://eprint.iacr.org/2021/1498.
2. J. Yin, “Difference packing arrays and systematic authentication codes,” *Science in China Series A: Mathematics* 47(4) (2004), 566–571. DOI: https://doi.org/10.1360/03ys0037.
3. J. Yin, “Cyclic Difference Packing and Covering Arrays,” *Designs, Codes and Cryptography* 37(2) (2005), 281–292. DOI: https://doi.org/10.1007/s10623-004-3991-3.
