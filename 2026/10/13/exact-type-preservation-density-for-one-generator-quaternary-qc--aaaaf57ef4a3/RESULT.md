# Exact type-preservation density for one-generator quaternary QC searches
## Finding

Let \(m\) be odd and use the Chinese-remainder decomposition
\[
R=\mathbb Z_4[x]/(x^m-1)
\cong
\prod_{i=1}^r R_i,
\qquad
R_i=\mathbb Z_4[x]/(p_i),
\qquad
d_i=\deg p_i.
\]
For a cyclic seed
\[
C_g=\langle g\rangle,
\]
write
\[
S=\{i:g_i\ne0\}
\]
for the active CRT components.

Fix a QC index
\[
\ell\ge1
\]
and count ordered multiplier **residue** tuples
\[
(f_1,\ldots,f_\ell)\in R^\ell.
\]
The number for which
\[
C=
\langle(f_1g,\ldots,f_\ell g)\rangle
\]
has the same \(\mathbb Z_4\)-type as \(C_g\) is
\[
N_{\mathrm{tp}}(g,\ell)
=
4^{m\ell}
\prod_{i\in S}
\left(1-2^{-\ell d_i}\right).
\]

Therefore uniformly random independent multiplier residues preserve type with exact probability
\[
P_{\mathrm{tp}}(g,\ell)
=
\prod_{i\in S}
\left(1-2^{-\ell d_i}\right).
\]

This law depends on an active component only through its degree \(d_i\). It is insensitive to whether \(g_i\) is a unit or a nonzero element of \(2R_i\).

The paper also gives the stronger sufficient condition that the multipliers be jointly coprime to all of \(x^m-1\). The number satisfying that condition is
\[
N_{\mathrm{joint}}(\ell)
=
4^{m\ell}
\prod_{i=1}^r
\left(1-2^{-\ell d_i}\right).
\]
Hence the exact criterion enlarges the accepted multiplier search space by the factor
\[
\frac{N_{\mathrm{tp}}(g,\ell)}
{N_{\mathrm{joint}}(\ell)}
=
\prod_{i\notin S}
\left(1-2^{-\ell d_i}\right)^{-1}.
\]
Equality occurs exactly when every CRT factor is active.

For the source's length-three seed
\[
g'=2x^2+2x,
\]
only the degree-two factor is active. Thus the exact type-preservation probabilities for
\[
\ell=1,2,3
\]
are
\[
\frac34,\qquad
\frac{15}{16},\qquad
\frac{63}{64},
\]
while the paper's joint-coprimality sufficient condition accepts proportions
\[
\frac38,\qquad
\frac{45}{64},\qquad
\frac{441}{512}.
\]

## Assumptions and scope

The setup is the odd-length case of Aydin and Tyagi. Since \(m\) is odd,
\[
x^m-1
\]
is squarefree modulo \(2\), so its distinct irreducible factors lift to pairwise coprime monic factors
\[
p_1,\ldots,p_r
\]
over \(\mathbb Z_4\), giving the displayed CRT decomposition.

Each \(R_i\) is a finite chain ring with
\[
0\subsetneq2R_i\subsetneq R_i,
\]
and
\[
|R_i|=4^{d_i},
\qquad
|2R_i|=2^{d_i}.
\]
Its nonunits are exactly \(2R_i\).

The count is of residue tuples in \(R^\ell\), which are precisely the multiplier data relevant to the QC construction modulo \(x^m-1\). It is not a count of arbitrary polynomial representatives in \(\mathbb Z_4[x]\).

## Proof

Aydin--Tyagi Theorem 4.1 proves that type is preserved exactly when, for every active component
\[
i\in S,
\]
at least one local multiplier
\[
f_{j,i}\in R_i
\]
is a unit.

Fix an active component \(i\). There are
\[
|R_i|^\ell
=
4^{\ell d_i}
\]
ordered local multiplier tuples. Such a tuple fails the type-preservation condition at \(i\) exactly when all \(\ell\) entries are nonunits. Since the nonunits are precisely \(2R_i\), their number is
\[
|2R_i|^\ell
=
2^{\ell d_i}.
\]
Thus the number of good local tuples is
\[
4^{\ell d_i}-2^{\ell d_i}.
\]

For an inactive component
\[
i\notin S,
\]
Theorem 4.1 imposes no restriction, so all
\[
4^{\ell d_i}
\]
local tuples are allowed.

The CRT identifies \(R^\ell\) with the direct product of all these local tuple spaces, independently across \(i\). Multiplying the local counts gives
\[
N_{\mathrm{tp}}(g,\ell)
=
\prod_{i\notin S}4^{\ell d_i}
\prod_{i\in S}
\left(4^{\ell d_i}-2^{\ell d_i}\right).
\]
Since
\[
\sum_{i=1}^r d_i=m,
\]
this simplifies to
\[
N_{\mathrm{tp}}(g,\ell)
=
4^{m\ell}
\prod_{i\in S}
\left(1-2^{-\ell d_i}\right).
\]

Dividing by
\[
|R|^\ell=4^{m\ell}
\]
gives the exact probability formula.

The proof of Theorem 4.1 treats both active valuation classes in the same way: whether \(g_i\) is a unit or a nonzero element of \(2R_i\), type is preserved locally exactly when some \(f_{j,i}\) is a unit. This proves the asserted independence from the valuation class of \(g_i\).

For the paper's Theorem 3.2 joint-coprimality condition, the same local unit requirement is imposed at **every** factor, active or inactive. Repeating the product with \(S=\{1,\ldots,r\}\) gives
\[
N_{\mathrm{joint}}(\ell)
=
4^{m\ell}
\prod_{i=1}^r
\left(1-2^{-\ell d_i}\right).
\]
The ratio follows immediately.

## Verification

`artifacts/verify.py` uses only the Python standard library.

It reconstructs the source's
\[
m=3
\]
factorization
\[
x^3-1=(x-1)(x^2+x+1)
\]
over \(\mathbb Z_4\), with component degrees \(1\) and \(2\).

It directly reduces the source seed
\[
g=x^2+x+3
\]
modulo the two lifted factors and obtains a unit component and a nonzero valuation-one component, so both factors are active. It similarly reduces
\[
g'=2x^2+2x
\]
and verifies that only the degree-two factor is active, exactly as stated in the source.

The script then exhausts all
\[
64^\ell
\]
ordered multiplier residue tuples for
\[
\ell=1,2,3.
\]
For each tuple it tests the local unit criterion factor by factor from the reductions modulo \(2\). It compares the exact brute-force counts against the closed formula for three active sets: both factors, only the degree-two factor, and only the degree-one factor.

It separately counts tuples satisfying the joint-coprimality sufficient condition and verifies the claimed ratios. Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Aydin and Tyagi solve the type-preservation problem by proving the exact CRT criterion used here. Their paper emphasizes that only the factors on which \(g\) remains nonzero matter, and then uses that criterion to guide a systematic computer search that produced \(36\) improved quaternary codes.

The source does not enumerate the successful multiplier tuples or state their density. The formula here converts the qualitative criterion into an exact search-space law. In particular, it quantifies precisely how much the paper's simpler whole-polynomial joint-coprimality sufficient condition can discard.

Earlier enumeration work on one-generator quasi-cyclic and generalized quasi-cyclic codes over finite fields and finite chain rings counts distinct code submodules, often with a fixed parity-check polynomial. That is a different enumeration object: the result here fixes a cyclic seed and counts ordered multiplier residue tuples that preserve its \(\mathbb Z_4\)-type. Different multiplier tuples can generate the same QC code, so the two counts do not imply one another.

Focused searches using the new paper's identifier, type-preservation terminology, active CRT factors, multiplier-tuple enumeration, and probability language found no prior statement of the product formula.

## Limitations

The formula assumes odd \(m\), exactly the squarefree setting of the source's Theorem 4.1. The paper itself identifies extension to even \(m\) as an open direction, where the local rings need not have the same simple chain structure.

The result counts ordered multiplier residues, not distinct QC codes up to equality or equivalence. It is therefore a search-space and representation count rather than a code-isomorphism enumeration.

The probability statement uses independent uniform sampling from \(R^\ell\). Searches that restrict multiplier degrees or impose additional normalizations have a different sampling distribution.

## References

1. Nuh Aydin and Aditya Tyagi, *Resolution of an Open Problem on Quasi-Cyclic Codes over \(\mathbb Z_4\) and New Quaternary Linear Codes*, arXiv:2609.21601v1, first public 18 September 2026.
2. Yonglin Cao, *Generalized quasi-cyclic codes over Galois rings: structural properties and enumeration*, Applicable Algebra in Engineering, Communication and Computing 22 (2011), 219--233, DOI 10.1007/s00200-011-0145-5.
3. Yonglin Cao, *1-generator quasi-cyclic codes over finite chain rings*, Applicable Algebra in Engineering, Communication and Computing 24 (2013), 53--72, DOI 10.1007/s00200-012-0182-8.
