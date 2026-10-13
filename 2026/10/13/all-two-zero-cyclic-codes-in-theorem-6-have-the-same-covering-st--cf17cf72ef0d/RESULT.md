# All two-zero cyclic codes in Theorem 6 have the same covering structure
## Finding

Let \(q\) be an odd prime power. Hernández and Vega's Theorem 6 considers the cyclic codes
\[
\mathcal C_{((q-1)e_1,e_2)}
\]
of length \(q^2-1\) and dimension \(4\), under
\[
\gcd(q+1,e_1)=1,
\qquad
\gcd(q^2-1,e_2)=1.
\]

Every code in this family has the same covering structure as the canonical member
\[
\mathcal C_{((q-1),-1)}.
\]

For \(q=3\), the minimal nonzero codewords are exactly those of weights
\[
4\quad\text{and}\quad5.
\]

For every \(q>3\), the minimal nonzero codewords are exactly those of weights
\[
(q-1)^2,
\qquad
q(q-1)-1,
\qquad
q(q-1)+1.
\]
The codewords of weights
\[
q(q-1)
\qquad\text{and}\qquad
q^2-1
\]
are nonminimal.

Using the published weight distribution, the exact number of minimal nonzero codewords for \(q>3\) is therefore
\[
\frac{q^2-1}{2}(2q-1)
+
\frac{(q^2-1)^2}{2}
+
\frac{q^2-1}{2}(q-1)^2
=
\frac{(q^2-1)(2q^2-1)}{2}.
\]

This answers affirmatively the paper's stated future-work question asking whether the remaining codes in Theorem 6 share the covering structure already proved there for \(\mathcal C_{((q-1),-1)}\).

## Assumptions and scope

The code is written in the trace form from Theorem 6:
\[
\mathcal C_{((q-1)e_1,e_2)}
=
\{\mathbf c(a,b):a,b\in\mathbb F_{q^2}\},
\]
where
\[
\mathbf c(a,b)
=
\left(
\operatorname{Tr}_{q^2/q}
\left(
 a\gamma^{(q-1)e_1i}+b\gamma^{e_2i}
\right)
\right)_{i=0}^{q^2-2}.
\]

For \(q\ne3\), the source proves that the dual has minimum distance \(3\). Hence a generator matrix has no zero column and no two proportional columns. Its \(q^2-1\) columns therefore form a set
\[
S\subset\operatorname{PG}(3,q)
\]
of \(q^2-1\) distinct projective points.

A nonzero codeword corresponds to a hyperplane \(H\) in \(\operatorname{PG}(3,q)\), and its zero coordinates are exactly the points of
\[
S\cap H.
\]
A codeword is minimal if and only if \(S\cap H\) spans \(H\). Indeed, failure to span means the zero section lies in a line or a point and hence is contained in another hyperplane section, which is equivalent to strict support containment by an independent codeword.

The published five nonzero weights correspond to zero-section sizes
\[
2q-2,
\qquad
q,
\qquad
q-1,
\qquad
q-2,
\qquad
0.
\]

## Proof

Assume first that \(q>3\).

The minimum-weight codewords have weight \((q-1)^2\), so their zero sections have size
\[
(q^2-1)-(q-1)^2=2q-2.
\]
A projective line contains only \(q+1\) points, and
\[
2q-2>q+1
\]
for \(q>3\). Hence every such zero section spans its hyperplane. These codewords are minimal.

Next consider a codeword of weight \(q(q-1)\). The source's trace classification shows that these are exactly the words
\[
\mathbf c(0,b),
\qquad
b\ne0.
\]
Let
\[
y_i=\gamma^{e_2i},
\qquad
x_i=\gamma^{(q-1)e_1i}.
\]
Because \(e_2\) is invertible modulo \(q^2-1\), the values \(y_i\) run through \(\mathbb F_{q^2}^*\). The zero condition is
\[
\operatorname{Tr}_{q^2/q}(b y_i)=0.
\]
The nonzero solutions form the \(q-1\) nonzero points of a one-dimensional \(\mathbb F_q\)-subspace, so they are
\[
y_i=\lambda y_0,
\qquad
\lambda\in\mathbb F_q^*.
\]
If \(r\equiv(q-1)e_1e_2^{-1}\pmod{q^2-1}\), then
\[
x_i=y_i^r.
\]
Since \(r\) is divisible by \(q-1\),
\[
(\lambda y_0)^r=y_0^r.
\]
Thus the corresponding generator columns have the projective form
\[
[(x_0,\lambda y_0)],
\qquad
\lambda\in\mathbb F_q^*,
\]
and all lie on the projective line spanned by \((x_0,0)\) and \((0,y_0)\). Therefore every weight-\(q(q-1)\) codeword is nonminimal.

Now consider weight \(q(q-1)-1\), whose zero section has size \(q\). Suppose such a section were contained in a line \(L\). There are \(q+1\) hyperplanes through \(L\). For any point set \(S\subset\operatorname{PG}(3,q)\),
\[
\sum_{H'\supset L}|S\cap H'|
=|S|+q|S\cap L|,
\]
because points on \(L\) are counted \(q+1\) times and points outside \(L\) exactly once. Here the right side would be
\[
(q^2-1)+q^2=2q^2-1.
\]
But every hyperplane through \(L\) contains at least \(q\) points of \(S\), so the only allowed section sizes are \(q\) and \(2q-2\). Their total is at most
\[
(q+1)(2q-2)=2q^2-2,
\]
a contradiction. Hence every weight-\(q(q-1)-1\) codeword is minimal.

It remains to treat weight \(q(q-1)+1\), with zero-section size \(q-2\). Suppose such a section were contained in a line \(L\). The pencil identity gives
\[
\sum_{H'\supset L}|S\cap H'|
=(q^2-1)+q(q-2)
=2q^2-2q-1.
\]
Measure deficits from the maximum allowed section size \(2q-2\). Across the \(q+1\) planes through \(L\), the total deficit is
\[
(q+1)(2q-2)-(2q^2-2q-1)=2q-1.
\]
The original \(q-2\) section contributes deficit \(q\). The remaining deficit is \(q-1\). For \(q\ge5\), among the possible positive deficits
\[
q,
\qquad
q-1,
\qquad
q-2,
\]
the only way for the other \(q\) planes to contribute exactly \(q-1\) is that exactly one has deficit \(q-1\). Thus exactly one other hyperplane through \(L\) has section size \(q-1\).

But every \(q-1\) section is one of the weight-\(q(q-1)\) sections already proved to lie on a projective line. It contains the \(q-2\ge3\) points of \(S\cap L\), so that line must be \(L\) itself. This would force \(|S\cap L|\ge q-1\), contradicting \(|S\cap L|=q-2\). Hence every weight-\(q(q-1)+1\) codeword is minimal.

A full-weight codeword has empty zero section, which does not span a hyperplane, so every weight-\(q^2-1\) codeword is nonminimal.

This proves the covering structure for every \(q>3\).

For \(q=3\), the admissibility conditions imply that \(e_1\) is odd and \(e_2\) is a unit modulo \(8\). The first exponent \(2e_1\) belongs to the same ternary cyclotomic coset \(\{2,6\}\) as \(2\). The second exponent belongs to either \(\{1,3\}\) or \(\{5,7\}\). The latter is the canonical second-zero coset. In the former case, the cyclic multiplier \(i\mapsto5i\pmod8\) fixes the first-zero coset and maps \(\{1,3\}\) to \(\{5,7\}\). Therefore every ternary code in Theorem 6 is permutation equivalent to \(\mathcal C_{(2,-1)}\). The source already proves that this canonical code has only weights \(4\) and \(5\) minimal, so the same holds for the entire ternary family.

## Verification

`artifacts/verify.py` uses only the Python standard library.

For prime fields \(q=3,5,7,11\), it constructs \(\mathbb F_{q^2}\), finds a primitive element, and reconstructs the trace generator matrix directly from Theorem 6. It checks representatives of every multiplier class of the exponent ratio modulo \(q+1\) for these values.

For every nonzero projective message vector, the verifier computes the codeword weight and the projective rank of its zero columns. Minimality is checked through the criterion
\[
\operatorname{rank}(S\cap H)=3.
\]
The resulting minimal-weight sets agree with the theorem:
\[
q=3:\ \{4,5\},
\]
\[
q=5:\ \{16,19,21\},
\]
\[
q=7:\ \{36,41,43\},
\]
\[
q=11:\ \{100,109,111\}.
\]

The script also verifies the source's complete ordinary weight distribution in every tested representative and checks the exact predicted number of minimal projective codewords.

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Hernández and Vega determine the full five-weight distribution for every code in Theorem 6, but determine the covering structure only for the canonical member \(\mathcal C_{((q-1),-1)}\). Their conclusion explicitly asks whether the remaining codes in Theorem 6 share this covering structure.

Their proof for the canonical member proceeds by comparing it with a code from Li, Qu, and Ling built from a perfect nonlinear function. Li--Qu--Ling characterize minimal codewords for that perfect-nonlinear construction, not for arbitrary exponent pairs in Hernández--Vega Theorem 6.

Earlier work of Hernández and Vega on subfield codes also determines covering structures for different optimal cyclic-code families. Those results concern subfield constructions with different parameter and generator geometries and do not imply the present two-zero family theorem.

The present argument is instead intrinsic to the full Theorem 6 family: it combines projectivity, the published five hyperplane-section sizes, the exact trace description of the \(q(q-1)\)-weight class, and a projective-plane pencil count. It therefore covers every admissible exponent pair at once.

Focused searches by the source title, exact family notation, “remaining codes” wording, covering-structure terminology, and the equivalent two-zero cyclic-code description did not locate a prior theorem answering the source's stated question.

## Limitations

The result is specific to the five-weight two-zero cyclic family of Theorem 6. It does not assert that codes outside this family with the same ordinary weight enumerator have the same covering structure.

For \(q>3\), the proof uses the source's dual-distance-three result to obtain a projective generator point set. The ternary case requires the separate multiplier-equivalence argument above.

The theorem classifies minimal codewords by weight and counts them. It does not enumerate inequivalent minimal supports or determine the automorphism group of the resulting access structures.

## References

1. Félix Hernández and Gerardo Vega, *Few-weight linear codes and their application to secret sharing*, Applicable Algebra in Engineering, Communication and Computing, published 30 September 2026, DOI 10.1007/s00200-026-00758-1.
2. Chao Li, Longjiang Qu, and San Ling, *On the Covering Structures of Two Classes of Linear Codes From Perfect Nonlinear Functions*, IEEE Transactions on Information Theory 55 (2009), 70--82, DOI 10.1109/TIT.2008.2008145.
3. Félix Hernández and Gerardo Vega, *On the Subfield Codes of a Subclass of Optimal Cyclic Codes and Their Covering Structures*, LATIN 2022, LNCS 13568, 255--270, DOI 10.1007/978-3-031-20624-5_16.
