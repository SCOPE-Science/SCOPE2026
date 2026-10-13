# Complete parameterization of degree-one binary Goppa realizations
## Finding

Let
\[
C\subseteq\mathbb F_2^n
\]
be a binary \([n,k]\) code with
\[
d(C)\ge3,
\]
and write
\[
s=n-k.
\]
Fix \(M\ge s\) and a specified field
\[
F=\mathbb F_{2^M}.
\]

An anchored ordered degree-one Goppa realization of \(C\) is a pair
\[
(\beta,L),\qquad
\beta\in F,\qquad
L=(\alpha_1,\ldots,\alpha_n),
\]
where the \(\alpha_i\) are distinct elements of \(F\setminus\{\beta\}\), the original coordinate labels are retained, and
\[
C=\Gamma_2(L,x-\beta).
\]

Put
\[
V=\mathbb F_2^n/C.
\]
Then anchored ordered realizations are in bijection with injective \(\mathbb F_2\)-linear maps
\[
\psi:V\hookrightarrow F.
\]
The correspondence is
\[
\psi(e_i+C)=(\beta-\alpha_i)^{-1},
\]
and conversely
\[
\alpha_i=\beta+\psi(e_i+C)^{-1}.
\]

Hence the exact number of realizations is
\[
R_M(C)
=
2^M\prod_{j=0}^{s-1}(2^M-2^j).
\]
This count depends only on the redundancy \(s\), not on the particular code.

If \(M<s\), then
\[
R_M(C)=0.
\]
At the minimum possible extension degree \(M=s\),
\[
R_s(C)
=
2^s|\operatorname{GL}(s,2)|
=
2^s\prod_{j=0}^{s-1}(2^s-2^j).
\]

Thus every minimal-field realization is exactly a choice of anchor together with an \(\mathbb F_2\)-linear identification
\[
\mathbb F_2^n/C\cong\mathbb F_{2^s}.
\]

## Assumptions and scope

The binary degree-one Goppa code is written
\[
\Gamma_2(L,x-\beta)
=
\left\{
c\in\mathbb F_2^n:
\sum_{i=1}^n
\frac{c_i}{\beta-\alpha_i}=0
\right\}.
\]

The recent source proves that a binary linear code is representable in this form with distinct support points if and only if its minimum distance is at least \(3\). It also proves that if the redundancy is \(s\), then extension degree \(s\) suffices and no smaller binary extension degree can work.

The theorem here counts anchored, coordinate-labeled representations over a fixed field. It does not quotient by coordinate permutations, field automorphisms, or projective transformations.

## Proof

Let
\[
\pi:\mathbb F_2^n\longrightarrow V=\mathbb F_2^n/C
\]
be the quotient map and put
\[
v_i=\pi(e_i).
\]

Because \(d(C)\ge3\), every \(v_i\) is nonzero: otherwise \(e_i\in C\) would give a word of weight \(1\). The \(v_i\) are pairwise distinct: if \(v_i=v_j\), then
\[
e_i+e_j\in C
\]
would give a word of weight \(2\). They span \(V\), because the standard basis vectors span \(\mathbb F_2^n\).

Suppose \((\beta,L)\) is a realization and define
\[
b_i=(\beta-\alpha_i)^{-1}.
\]
The Goppa check is
\[
C=
\left\{
c\in\mathbb F_2^n:
\sum_i c_i b_i=0
\right\}.
\]
Hence
\[
T(c)=\sum_i c_i b_i
\]
is an \(\mathbb F_2\)-linear map with kernel \(C\). It therefore factors uniquely through the quotient:
\[
T=\psi\circ\pi
\]
for a linear map
\[
\psi:V\longrightarrow F.
\]
Since \(\ker T=C\), the induced map \(\psi\) is injective, and
\[
\psi(v_i)=b_i.
\]

Conversely, take any injective linear map
\[
\psi:V\hookrightarrow F
\]
and any anchor
\[
\beta\in F.
\]
Because the \(v_i\) are nonzero and pairwise distinct, the elements
\[
b_i=\psi(v_i)
\]
are nonzero and pairwise distinct. Define
\[
\alpha_i=\beta+b_i^{-1}.
\]
Then the support points are distinct and avoid the anchor. For every \(c\in\mathbb F_2^n\),
\[
\sum_i c_i(\beta-\alpha_i)^{-1}
=
\sum_i c_i b_i
=
\psi(\pi(c)).
\]
Since \(\psi\) is injective, this vanishes exactly when \(c\in C\). Thus the resulting support realizes \(C\).

The two constructions are inverse, proving the bijection.

Finally, \(V\) has binary dimension \(s\), while \(F\) has binary dimension \(M\). An injective linear map is determined by an ordered linearly independent \(s\)-tuple in \(F\), of which there are
\[
(2^M-1)(2^M-2)\cdots(2^M-2^{s-1}).
\]
The anchor contributes a factor \(2^M\), giving
\[
R_M(C)
=
2^M\prod_{j=0}^{s-1}(2^M-2^j).
\]

## Verification

`artifacts/verify.py` uses only the Python standard library.

It implements \(\mathbb F_{2^M}\) for \(M=2,3,4\), including multiplication and inversion. It tests the binary repetition code \([3,1,3]\), the Hamming code \([7,4,3]\), and a shortened Hamming code \([6,3,3]\).

For the fully replayed cases, every ordered independent image of a syndrome-space basis and every anchor are enumerated. The verifier forms
\[
\alpha_i=\beta+\psi(e_i+C)^{-1}
\]
and directly checks that the support points are distinct, avoid the anchor, and produce exactly the same binary kernel as the original parity-check system.

The exact census is compared with
\[
2^M\prod_{j=0}^{s-1}(2^M-2^j).
\]
The two distinct redundancy-three codes each have
\[
8\cdot7\cdot6\cdot4=1344
\]
anchored ordered realizations over \(\mathbb F_8\).

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Liang and Zhang prove that every binary code with minimum distance at least \(3\) admits a degree-one binary Goppa representation and that the minimum required extension degree equals the redundancy. Their proof constructs one representation from a parity-check matrix and, conversely, extracts a scalar parity-check map from any such representation.

The present result identifies the whole representation space rather than only proving existence. The quotient
\[
\mathbb F_2^n/C
\]
is the intrinsic syndrome space, and every representation is shown to arise from exactly one linear injection of this quotient into the extension field together with one anchor. This yields an exact count for every extension degree and shows that the count is universal among all distance-at-least-three codes with the same redundancy.

Older enumeration work on binary Goppa codes counts inequivalent irreducible or extended irreducible Goppa codes via group actions on irreducible polynomials. That problem varies the code and quotients by equivalence; the result here fixes one arbitrary code, uses a degree-one polynomial, retains coordinate labels, and counts all anchored realizations of that code.

Focused searches for degree-one representation enumeration, minimal-field support realizations, quotient-space parameterizations, and exact representation counts found no prior statement of the formula above.

## Limitations

The enumeration is for anchored, ordered representations over a fixed finite field. Quotienting by coordinate permutations, field automorphisms, or other equivalences requires a separate orbit analysis.

The theorem applies only to binary codes with minimum distance at least \(3\), exactly the range in which distinct-support degree-one representations exist.

The result counts representations of a fixed code, not inequivalent Goppa codes. A differently phrased linear-algebra classification could contain the same bijection, although no such coding-theoretic formulation was found in the inspected literature.

## References

1. Shuhua Liang and Guanghui Zhang, *New lower bounds for the minimum distance of a class of binary Goppa codes*, AIMS Mathematics 11 (2026), 30145--30161, DOI 10.3934/math.20261194.
2. Bocong Chen and Guanghui Zhang, *The number of extended irreducible binary Goppa codes*, arXiv:2204.02083, 2022.
3. V. D. Goppa, *A new class of linear correcting codes*, Problems of Information Transmission 6 (1970), 207--212.
