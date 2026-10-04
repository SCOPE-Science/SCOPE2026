# Exact spectrum and minimum-support geometry of Example 8's Hermitian dual
## Finding

In Example 8 of Abdukhalikov--Shat, let \(C\) be the quaternary index-\(3\) quasi-cyclic code of length \(21\) generated over
\[
R=\mathbb F_4[x]/(x^7-1)
\]
by
\[
(1,1,x^2+x+\omega),
\]
\[
(0,p_0,x^5+x^4+\omega^2x^3+\omega x^2+\omega),
\]
and
\[
(0,0,p_1p_2),
\]
where
\[
p_0=x+1,\qquad p_1=x^3+x+1,\qquad p_2=x^3+x^2+1.
\]
The source states that \(C\) has parameters \([21,14,5]_4\) and that its Hermitian dual
\[
D=C^{\perp_h}
\]
is an optimal \([21,7,11]_4\) code.

For this specific \(D\), the exact Hamming weight enumerator is
\[
\begin{aligned}
W_D(z)={}&1+357z^{11}+756z^{12}+1113z^{13}+1998z^{14}\\
&+2520z^{15}+3633z^{16}+3024z^{17}+1722z^{18}\\
&+987z^{19}+210z^{20}+63z^{21}.
\end{aligned}
\]

Its Hermitian hull is one-dimensional. In coordinates grouped by the three length-\(7\) polynomial components,
\[
\operatorname{Hull}_h(D)
=
\left\langle(1,1,1,1,1,1,1\mid1,1,1,1,1,1,1\mid0,0,0,0,0,0,0)\right\rangle_{\mathbb F_4}.
\]

The \(357\) minimum-weight words give exactly \(119\) distinct supports. Under simultaneous cyclic shift in all three length-\(7\) blocks, these \(119\) supports split into exactly \(17\) orbits, each of size \(7\).

Writing the three block weights of a minimum support as \((a,b,c)\), their exact multiplicities are
\[
\begin{array}{c|r}
(a,b,c)&\text{number of supports}\\
(2,5,4)&14\\
(3,2,6)&14\\
(3,3,5)&7\\
(3,4,4)&21\\
(3,5,3)&14\\
(4,2,5)&7\\
(4,3,4)&14\\
(4,4,3)&14\\
(5,2,4)&7\\
(5,3,3)&7.
\end{array}
\]

## Assumptions and scope

The field is
\[
\mathbb F_4=\mathbb F_2(\omega),\qquad \omega^2+\omega+1=0.
\]
The Hermitian inner product is
\[
\langle u,v\rangle_h=\sum_i u_i v_i^2.
\]

For reproducibility, coordinates are grouped as the coefficient vectors of the first, second, and third polynomial components, each in constant-to-\(x^6\) order. This differs from the interleaved vector ordering used in the source correspondence only by a fixed coordinate permutation, so Hamming weights, hull dimension, support counts, and simultaneous-block cyclic orbits are unchanged.

The result concerns the exact Example 8 code, not every optimal quaternary \([21,7,11]_4\) code.

## Proof

Take all seven cyclic shifts of each of the three displayed \(R\)-module generators. Row reduction over \(\mathbb F_4\) gives rank \(14\), reproducing the source dimension of \(C\).

Let \(M\) be the resulting generator matrix of \(C\). A vector \(y\) belongs to the Hermitian dual exactly when
\[
M\overline y^{\mathsf T}=0,
\]
where
\[
\overline y=y^2
\]
coordinatewise. Hence the conjugates of a basis of the ordinary nullspace of \(M\) form a basis of \(D\). The nullspace has dimension \(7\), again matching the source.

Exhausting all
\[
4^7=16384
\]
linear combinations of this Hermitian-dual basis gives the weight enumerator stated above. In particular, the smallest nonzero weight is \(11\), independently reproducing the published minimum distance.

For the hull, form the Hermitian Gram matrix
\[
G_D\overline{G_D}^{\mathsf T}.
\]
Its rank is \(6\), so
\[
\dim\operatorname{Hull}_h(D)
=
7-6
=
1.
\]
The displayed weight-\(14\) vector lies in both \(D\) and \(D^{\perp_h}\), so it spans the hull.

There are \(357\) minimum words. Direct support canonicalization gives \(119\) distinct supports. Each support is represented by the three nonzero scalar multiples of one minimum word. Simultaneous cyclic shift preserves \(D\), and direct orbit closure gives \(17\) disjoint orbits of size \(7\). Counting nonzero positions within each of the three seven-coordinate blocks gives the stated block-weight multiplicities.

## Verification

`artifacts/verify.py` uses only the Python standard library. It reconstructs \(\mathbb F_4\), the three source generators, and all cyclic shifts. It verifies rank \(14\) for \(C\), constructs the Hermitian dual from the conjugated nullspace, and verifies rank \(7\).

The verifier enumerates all \(16384\) dual codewords and checks every coefficient of the displayed weight enumerator. It computes the Hermitian Gram rank and the explicit one-dimensional hull. It then canonicalizes all minimum supports, confirms the count \(119\), verifies closure under simultaneous cyclic shift, obtains exactly \(17\) seven-element orbits, and checks every block-weight multiplicity.

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

The primary article develops the structure and Euclidean/Hermitian dual theory of index-\(3\) quasi-cyclic codes. Example 8 gives the three generators above and states the parameters \([21,14,5]_4\) and \([21,7,11]_4\), identifying the Hermitian dual as optimal. The article does not state a weight enumerator, hull dimension, minimum-support count, orbit decomposition, or block-support distribution for this example.

The standard linear-code tables determine parameter bounds such as optimality of a \([21,7,11]_4\) code, but parameter bounds do not determine the weight enumerator or support incidence structure of a particular generator.

Focused searches for the source title and Example 8 together with the full parameter set, weight-distribution coefficients, hull terminology, \(357\) minimum words, and \(119\) minimum supports did not locate an earlier statement of these same-object invariants. Nearby work on one-generator quaternary Hermitian LCD codes does not dominate this result: an LCD code has zero Hermitian hull, whereas the code here has hull dimension \(1\).

## Limitations

The calculation is exact but finite and specific to Example 8. It is not a classification of optimal quaternary \([21,7,11]_4\) codes.

The source already establishes the parameters and optimality. The new content is the complete weight spectrum, Hermitian hull, and minimum-support geometry.

A different optimal code with the same parameters may have a different weight enumerator or support-orbit structure.

## References

1. Kanat Abdukhalikov and Rasha M. Shat, *On Quasi-Cyclic Codes of Index 3*, Entropy 27 (2025), 1096, DOI 10.3390/e27111096.
2. Markus Grassl, *Bounds on the Minimum Distance of Linear Codes*, online code tables.
