# Exact maxima for the three residual three-block LRC cases

## Statement

For a prime power \(q\), let \(A_q(n,d;r,\delta)\) denote the largest size of a
\(q\)-ary length-\(n\) code of minimum distance at least \(d\) with all-symbol
\((r,\delta)\)-locality. Let \(K_q(n,d;r,\delta)\) denote the largest dimension
of a linear code with the same parameters.

The three parameter sets excluded from the exact linear-dimension conclusion in
Kang and Xiong, Corollary V.2, satisfy

\[
A_2(15,5;1,3)=16,\qquad
A_3(7,3;1,3)=9,\qquad
K_2(14,4;2,2)=7.
\]

Consequently,

\[
K_2(15,5;1,3)=4,\qquad
K_3(7,3;1,3)=2,
\]

so every parameter row in their Table V.1 has an exact maximum linear
dimension. The first two equalities are stronger: they determine the maximum
size even for nonlinear codes.

The remaining nonlinear question in these three rows is the binary
\((n,d,r,\delta)=(14,4,2,2)\) case. The construction below has size \(128\),
while the three-block LP gives

\[
A_2(14,4;2,2)\le
\left\lfloor\frac{1359968}{8555}\right\rfloor=158.
\]

## An elementary locality-one partition lemma

Let \(\mathcal C\subseteq\mathbb F_q^n\) have at least two codewords and
all-symbol \((1,\delta)\)-locality. For each coordinate \(i\), choose a recovery
view \(T_i\) containing \(i\). The locality definition gives
\(|T_i|\le\delta\) and \(d(\mathcal C|_{T_i})\ge\delta\). Hence
\(|T_i|=\delta\).

For a coordinate \(j\), let \(\Pi_j\) be the partition of \(\mathcal C\) into
classes having the same symbol in coordinate \(j\). If \(j,k\in T_i\), then
\(\Pi_j=\Pi_k\): if two codewords agree at one coordinate of \(T_i\) but have
different projections on \(T_i\), those two projected words differ in at most
\(\delta-1\) positions, contradicting the local minimum distance \(\delta\).

Thus equality of the coordinate partitions defines equivalence classes
\(E_1,\ldots,E_s\) of coordinates, each of size at least \(\delta\). Choose one
representative from every class and map each codeword to its tuple of
representative symbols. This map is injective, so

\[
|\mathcal C|\le q^s,\qquad s\le\left\lfloor\frac n\delta\right\rfloor.
\]

Moreover, if two representative tuples differ in class \(E_a\), then the
original codewords differ at every coordinate of \(E_a\). Hence their Hamming
distance is exactly the sum of the sizes of the equivalence classes on which
the representative tuples differ.

This lemma uses only the locality definition and does not assume linearity.

## The binary \((15,5;1,3)\) case

The partition lemma gives \(s\le5\). If \(s\le4\), then
\(|\mathcal C|\le2^4=16\). If \(s=5\), all five classes have size exactly
three. The representative tuples therefore form a binary length-\(5\) code
with minimum distance at least \(2\), because a pair differing in only one
representative would have original distance \(3<5\).

A binary length-\(5\) code of minimum distance at least \(2\) has size at most
\(16\): pair the \(32\) binary words into the \(16\) edges
\(\{x,x+e_1\}\) of the five-cube; at most one endpoint of each edge can belong
to the code. Hence \(A_2(15,5;1,3)\le16\).

Equality is attained by taking the binary even-parity \([5,4,2]\) code and
repeating each of its five coordinates three times. The resulting code has
length \(15\), size \(16\), minimum distance \(6\), and every coordinate lies
in a three-coordinate repetition block of local distance \(3\).

This linear construction is not claimed as new. Xia and Chen's 2019
characterization of optimal linear locality-one \((r,\delta)\)-LRCs already
reduces this parameter regime to an MDS construction.

## The ternary \((7,3;1,3)\) case

The partition lemma gives at most
\(\lfloor7/3\rfloor=2\) coordinate classes, so every such code has size at
most \(3^2=9\).

Equality is attained by

\[
\mathcal C=\{(a,a,a,b,b,b,b):a,b\in\mathbb F_3\}.
\]

It has size \(9\) and minimum distance \(3\). Every coordinate can choose
three coordinates inside its own repetition class as a recovery view, so the
code has all-symbol \((1,3)\)-locality. Therefore
\(A_3(7,3;1,3)=9\).

## The binary \((14,4;2,2)\) linear case

Kang and Xiong's three-block LP gives

\[
|\mathcal C|\le\frac{1359968}{8555}<2^8.
\]

For a binary linear code, \(|\mathcal C|=2^k\), hence \(k\le7\).

The following generator matrix attains dimension \(7\):

\[
G=
\begin{pmatrix}
1&0&0&0&0&0&0&0&1&0&0&1&1&0\\
0&1&0&0&0&0&0&1&1&0&0&1&0&0\\
0&0&1&0&0&0&0&0&1&1&1&1&1&1\\
0&0&0&1&0&0&0&0&0&0&0&1&1&1\\
0&0&0&0&1&0&0&1&1&0&0&1&1&1\\
0&0&0&0&0&1&0&0&0&1&0&0&1&1\\
0&0&0&0&0&0&1&0&0&0&1&0&1&1
\end{pmatrix}.
\]

Its weight enumerator is

\[
1+16z^4+12z^5+18z^6+24z^7+23z^8+28z^9+6z^{10},
\]

so its minimum distance is \(4\). The five local triples

\[
\{1,13,14\},\ \{2,5,8\},\ \{3,6,10\},\
\{3,7,11\},\ \{4,9,12\}
\]

cover all fourteen coordinates. On each triple the punctured code is a binary
\([3,2,2]\) single-parity-check code, establishing all-symbol
\((2,2)\)-locality. Thus \(K_2(14,4;2,2)=7\).

Existence of a binary \([14,7,4;2]\) locally recoverable code was already
recorded by Yang, Li, Fu, Yang, and Rao; the contribution here is not the
existence claim by itself, but its combination with the new three-block upper
bound and the closure of the residual parameter row.

## Reproducibility

`artifacts/verify.py` uses only the Python standard library. It enumerates the
three displayed linear codes, checks ranks, minimum distances and weight
enumerators, and verifies an admissible recovery view for every coordinate.

A successful run prints:

```text
binary [14,7,4]: all-symbol (2,2) locality verified
binary [15,4,6]: all-symbol (1,3) locality verified
ternary [7,2,3]: all-symbol (1,3) locality verified
all checks passed
```

## Limitations

The binary \((14,4,2,2)\) maximum size among nonlinear codes is not determined
here; only its maximum linear dimension is determined. The two locality-one
maximum-size arguments are specific to \(r=1\), where every recovery view has
length exactly \(\delta\).

The originality claim is only to the best of our knowledge. The elementary
locality-one structure and the individual linear constructions have substantial
prior context; the claimed contribution is the exact closure of the three
residual parameter rows of the September 2026 three-block LP study, including
nonlinear exactness for the two locality-one rows.

## References

1. Ming-Hsuan Kang and Maosheng Xiong, *Linear Programming Bounds for Locally
   Recovery Codes II*, arXiv:2609.16044v1 (2026).
   https://arxiv.org/abs/2609.16044
2. Ruipan Yang, Ruihu Li, Qiang Fu, Sen Yang, and Yi Rao, *On locality of binary
   distance-optimal codes*, Cryptography and Communications 16 (2024), 49–69.
   https://doi.org/10.1007/s12095-023-00626-6
3. Yichong Xia and Bin Chen, *Complete Characterizations of Optimal Locally
   Repairable Codes With Locality 1 and K-1*, IEEE Access 7 (2019),
   111271–111276. https://doi.org/10.1109/ACCESS.2019.2934769
