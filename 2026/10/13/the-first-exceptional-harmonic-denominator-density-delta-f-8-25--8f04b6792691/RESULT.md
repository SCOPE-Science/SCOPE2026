# The first exceptional harmonic-denominator density: \(\delta(f_8)=25/64\)
## Finding
For
\[
f_d(x)=\sum_{i=0}^d\prod_{\substack{0\le j\le d\\j\ne i}}(x-j),
\]
the first exceptional even index in the published Galois computation has an exact local description. The splitting-field Galois group of \(f_8\), in its natural action on its eight roots, is
\[
\operatorname{Gal}(f_8/\mathbb Q)\cong W(D_4)\cong 2^3\rtimes S_4,
\]
of order \(192\). Consequently, if \(\delta(f_8)\) denotes the natural density of primes \(p\) for which \(f_8(x)\equiv0\pmod p\) is solvable, then
\[
\delta(f_8)=\frac{25}{64}.
\]
Thus the \(d=8\) contribution to
\[
c=\sum_{d\ge1}\frac{\delta(f_d)}{d(d+1)}
\]
is exactly \(25/4608\).

## Assumptions and scope
All fields are over \(\mathbb Q\). Densities exclude the finite set of ramified primes, which does not affect natural density. The use of factorization types modulo unramified primes is the standard Frobenius correspondence, and the conversion from fixed points in the Galois action to prime-root density is the Frobenius--Chebotarev statement used in the motivating literature.

The result determines only the exceptional index \(d=8\). It does not determine the corresponding groups at \(d=24\) or \(d=48\), and it does not evaluate the full infinite constant \(c\).

## Proof
Translate to the center by writing \(z=x-4\). Direct expansion gives
\[
g_8(z)=f_8(z+4)=9z^8-210z^6+1365z^4-2460z^2+576=h(z^2),
\]
where
\[
h(T)=9T^4-210T^3+1365T^2-2460T+576.
\]

First determine the Galois group of \(h\). Modulo \(17\),
\[
h(T)\equiv-8\bigl(T^4+5T^3-7T^2-7T-4\bigr),
\]
and the displayed quartic is irreducible. Hence \(h\) is irreducible over \(\mathbb Q\), and its Galois group contains a \(4\)-cycle. Modulo \(11\),
\[
h(T)\equiv-2(T+1)(T^3+5T^2-2),
\]
with the cubic irreducible, so the group also contains a \(3\)-cycle. A transitive subgroup of \(S_4\) containing both a \(4\)-cycle and a \(3\)-cycle is \(S_4\). Therefore \(\operatorname{Gal}(h/\mathbb Q)=S_4\).

Let \(y_1,\ldots,y_4\) be the roots of \(h\), and choose \(z_i\) with \(z_i^2=y_i\). Since
\[
y_1y_2y_3y_4=\frac{576}{9}=64,
\]
we may choose the signs so that \(z_1z_2z_3z_4=8\). Hence every automorphism of the splitting field flips an even number of the four signs. Thus the Galois group \(G\) of \(g_8\) embeds into the even signed permutation group
\[
E\rtimes S_4,
\qquad
E=\ker\!\left((\mathbb Z/2\mathbb Z)^4\xrightarrow{\,\sum\,}\mathbb Z/2\mathbb Z\right),
\]
which has order \(8\cdot24=192\). Restriction to the splitting field of \(h\) maps \(G\) onto \(S_4\). Its kernel \(K\) is therefore an \(S_4\)-stable subgroup of \(E\).

Modulo \(7\), the exact squarefree factorization is
\[
g_8(z)\equiv2(z+3)(z-3)(z^2+1)(z^4+z^2+3),
\]
where the quadratic and quartic factors are irreducible. A Frobenius element therefore has cycle type \((4,2,1,1)\) on the eight signed roots. On the four opposite root-pairs, such an element projects to a transposition: the \(4\)-cycle is a negative signed \(2\)-cycle, the \(2\)-cycle is a negative fixed pair, and the two fixed roots form one positive fixed pair. Squaring this Frobenius element fixes all four root-pairs and flips exactly the two signs belonging to the negative \(2\)-cycle. Hence \(K\) contains a sign vector of Hamming weight \(2\).

Conjugating by the surjective \(S_4\)-action gives every weight-\(2\) vector. These vectors generate all of \(E\), so \(K=E\). Therefore
\[
G=E\rtimes S_4\cong W(D_4).
\]
In particular, \(G\) acts transitively on the eight roots, so \(f_8\) is irreducible.

It remains to count elements of \(G\) with a fixed signed root. For a permutation \(\pi\in S_4\), a signed root over a fixed index is fixed exactly when the sign at that index is positive. Among the eight even sign vectors:

- for the identity permutation, \(7\) have at least one positive sign;
- for each of the \(6\) transpositions, which have two fixed indices, \(6\) sign vectors fix a signed root;
- for each of the \(8\) three-cycles, which have one fixed index, \(4\) sign vectors fix a signed root;
- double transpositions and four-cycles have no fixed index and contribute none.

Thus precisely
\[
7+6\cdot6+8\cdot4=75
\]
of the \(192\) group elements are non-derangements. Frobenius--Chebotarev gives
\[
\delta(f_8)=\frac{75}{192}=\frac{25}{64}.
\]
Dividing by \(8\cdot9\) gives the contribution \(25/4608\) to \(c\).

## Verification
The standalone `verify.py` reconstructs \(f_8\) from its defining sum, verifies the centered polynomial, checks the displayed modular factorizations with exact finite-field arithmetic, proves the required modular irreducibility tests by Rabin's criterion, exhausts all \(192\) even signed permutations, and counts exactly \(75\) with a fixed signed root. The recorded replay is:

`VERIFY_OK centered_f8=yes h17=irreducible4 h11=1+3 g7=4+2+1+1 group_order=192 fixed=75 density=25/64`

The program is a finite exact check of the algebraic certificates and group count. The infinite prime-density conclusion uses the proved Galois group together with the standard Frobenius--Chebotarev theorem; it is not inferred from finite prime sampling.

## Relationship to prior work
Van Doorn's 2024/2025 paper defines \(f_d\) and \(\delta(f_d)\), identifies \(\delta(f_d)\) with the non-derangement proportion when \(f_d\) is irreducible, and reports that the full hyperoctahedral group occurs for every even \(d\le60\) tested except \(d=8,24,48\). The exceptional cases are then left inside an uncontrolled remainder when bounding \(c\). The present result resolves the first of those three exceptions by identifying its proper subgroup and its exact non-derangement proportion.

The 2026 paper makes the same density constant \(c\) central to the exact lower-limit theorem for the first decrease of a harmonic denominator and explicitly notes that it does not try to compute the constant very precisely. That theorem does not identify the \(d=8\) local group or density.

Targeted searches for the polynomial, the value \(25/64\), the notation \(W(D_4)\), and equivalent Galois/fixed-point formulations found no published statement that implies this local identification. This is evidence against coverage, not a proof of uniqueness in the literature.

## Limitations
The argument is specific to \(d=8\). It leaves \(d=24\) and \(d=48\) unresolved and does not determine whether other exceptional even indices occur beyond the reported computational range. It also does not turn the infinite series defining \(c\) into a closed form. A residual originality risk remains that an unindexed computation may have recorded the same exceptional group without appearing in the inspected primary text or targeted searches.

## References
1. W. van Doorn, *On the non-monotonicity of the denominator of generalized harmonic sums*, arXiv:2411.03073v1 (first public version 2024-11-05; later v2 2025).
2. W. van Doorn, *The shortest harmonic sums with decreasing denominator*, arXiv:2609.00104v1 (2026).
