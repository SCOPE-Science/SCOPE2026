# Parity-stable restricted derivation algebras and exact square-zero rank spectra in characteristic two

## Finding

Let \(K\) be any field of characteristic \(2\) and let \(s\ge1\) be an integer. Write \(A_m=K[t]/(t^m)\) and \(\mathfrak D_m=\operatorname{Der}_K(A_m)\), with the restricted Lie structure given by commutators and operator squaring. There is an explicit restricted Lie algebra isomorphism
\[
\Phi_s:\mathfrak D_{2s}\xrightarrow{\ \cong\ }\mathfrak D_{2s+1}
\]
which preserves the ordinary rank of every derivation and, more strongly, preserves the number and sizes of every nonzero Jordan block in its action on its natural truncated-polynomial module. The natural representation in odd dimension is the natural even-dimensional representation plus one trivial one-dimensional summand, after identifying the two Lie algebras by \(\Phi_s\).

For \(q=2^f\), \(f\ge1\), and \(h=\lfloor s/2\rfloor\), define the rank enumerator of square-zero derivations by
\[
H_{s,q}(T)=\sum_{\substack{D\in\mathfrak D_{2s}\\D^2=0}}T^{\operatorname{rank}_{\mathbb F_q}D}.
\]
Then the same polynomial is obtained with \(\mathfrak D_{2s+1}\) in place of \(\mathfrak D_{2s}\), and
\[
\boxed{H_{s,q}(T)=1+(q^2-1)\sum_{r=1}^{h}q^{2r-2}T^r
        +(q-1)q^{s-1}\sum_{r=h+1}^{s}T^r.}
\]
Thus every rank from \(0\) through \(s\) occurs, and
\[
\boxed{\#\{D\in\mathfrak D_{2s}:D^2=0\}=q^s+\lfloor s/2\rfloor(q-1)q^{s-1}}
\]
with the identical count in \(\mathfrak D_{2s+1}\). The low-rank coefficients form a geometric progression, while the upper half of the spectrum has constant multiplicity.

For example, \(H_{4,2}(T)=1+3T+12T^2+8T^3+8T^4\), applying simultaneously to derivations of the length-eight and length-nine truncated polynomial algebras.

## Assumptions and scope

The algebras are unital, commutative, associative, and truncated by the *ordinary monomial ideal* \((t^m)\), not a divided-power algebra. Characteristic \(2\) is essential. The integer \(s\) is unrestricted except \(s\ge1\). The first assertion holds over every characteristic-two field, finite or infinite. The enumerator requires \(K=\mathbb F_q\) with \(q\) a power of two. \(D^2=0\) means the square of the underlying linear operator, equivalently the restricted \(2\)-power, not the vanishing of the coefficient polynomial \(D(t)^2\).

Every derivation of \(A_{2s}\) is uniquely \(D_f=f(t)d/dt\), where
\[f(t)=e(t^2)+t g(t^2),\qquad e,g\in R=K[z]/(z^s).\]
Every derivation of \(A_{2s+1}\) is uniquely \(D_F=F(t)d/dt\) with \(F\in tA_{2s+1}\): the quotient relation \(t^{2s+1}=0\) forces \(t^{2s}F=0\), or exactly a zero constant term. By contrast, \(2s=0\) in \(K\), so no coefficient restriction arises for \(A_{2s}\). Define
\[
\Phi_s(D_{e(t^2)+t g(t^2)})=D_{t^2e(t^2)+t g(t^2)}.
\]
This is a linear bijection because each side has exactly \(2s\) free coefficient parameters.

## Proof

**1. A characteristic-two representation intertwiner.** Let \(J_s:A_{2s}\to tA_{2s+1}\) be the \(K\)-linear bijection defined on the monomial basis by
\[
J_s(t^{2j})=t^{2j+2},\qquad J_s(t^{2j+1})=t^{2j+1}
\quad(0\le j<s).
\]
The target monomials are exactly \(t,t^2,\ldots,t^{2s}\), each appearing once. Every even monomial has derivative zero. For an odd monomial, the derivative is \(t^{2j}\); consequently for \(f=e(t^2)+t g(t^2)\), direct multiplication gives
\[
J_s D_f(t^{2j+1})=t^{2j+2}e(t^2)+t^{2j+1}g(t^2)
=\Phi_s(D_f)J_s(t^{2j+1}).
\]
The corresponding equality on even monomials is zero on both sides. Hence \(J_sD_f=\Phi_s(D_f)J_s\). The codomain derivation annihilates \(1\), so on the vector-space decomposition \(A_{2s+1}=K\cdot1\oplus tA_{2s+1}\), its matrix is \(0\oplus J_sD_fJ_s^{-1}\). In particular ranks of all powers and nonzero Jordan blocks agree. Because conjugation of linear operators preserves commutators and squaring, \(\Phi_s\) preserves the bracket and restricted \(2\)-map. Its bijectivity proves the claimed restricted Lie isomorphism.

**2. Square-zero criterion.** In characteristic \(2\), the composition square of a derivation is again a derivation, and \(D_f^2(t)=D_f(f)=ff'\). Here \(f'=g(t^2)\). The even and odd coefficients of \(ff'\) are respectively \(e(z)g(z)\) and \(g(z)^2\); these lie in disjoint monomial subspaces of \(A_{2s}\). Therefore
\[
D_f^2=0\quad\Longleftrightarrow\quad eg=0\ \text{and}\ g^2=0\quad\text{in }R.
\]
For a polynomial \(a\in R\), let \(v(a)\) be its \(z\)-adic valuation, with \(v(0)=s\). The images of the odd monomials under \(D_f\) are precisely \(z^jf\), \(0\le j<s\). Their span therefore has dimension
\[
\operatorname{rank}D_f=s-\min\{v(e),v(g)\}.
\]

**3. Counting pairs \((e,g)\).** The case \(g=0\) contributes one derivation of rank zero and \((q-1)q^{r-1}\) derivations of each rank \(1\le r\le s\), by counting \(e\) of valuation \(s-r\).

For \(g\ne0\), the equation \(g^2=0\) means \(v(g)\ge\lceil s/2\rceil\), so write \(v(g)=s-m\) for an integer \(1\le m\le h\). There are \((q-1)q^{m-1}\) such \(g\). Since the leading coefficient of \(g\) is nonzero, the annihilator equation \(eg=0\) is equivalent to \(e\in z^mR\). Among these \(e\), exactly \(q^m\) have \(v(e)\ge s-m\), producing rank \(m\); for every \(m+1\le r\le s-m\), exactly \((q-1)q^{r-1}\) have \(v(e)=s-r\), producing rank \(r\). No other ranks occur for this fixed \(m\).

Consequently the coefficient of \(T^r\) for \(r\ge1\) equals
\[
(q-1)q^{r-1}
+\mathbf1_{\{r\le h\}}(q-1)q^{2r-1}
+\sum_{m=1}^{\min(h,r-1,s-r)}(q-1)^2q^{m+r-2}.
\]
For \(1\le r\le h\), the sum runs through \(1\le m<r\), giving \((q^2-1)q^{2r-2}\) after simplification. For \(h<r\le s\), it runs through \(1\le m\le s-r\), giving \((q-1)q^{s-1}\). This proves the polynomial. At \(T=1\), its low-rank geometric sum is \(q^{2h}-1\); adding the high-rank terms yields \(q^s+h(q-1)q^{s-1}\) for both parities of \(s\).

**4. Odd truncation.** The intertwining bijection \(\Phi_s\) preserves \(D^2=0\) and preserves rank, so its count and every rank coefficient coincide exactly with those already calculated for the even truncation. This completes the proof.

## Verification

The supplied standard-library Python program `verify.py` constructs derivation matrices by applying the Leibniz rule to every monomial, tests the operator equation \(D^2=0\) by actual finite-field matrix multiplication, and calculates ranks by Gaussian elimination. It exhaustively checks each derivation for \(q=2\) with \(1\le s\le4\), and \(q=4\) with \(1\le s\le3\), for *both* lengths \(2s\) and \(2s+1\). It also checks every intertwining matrix entry for every tested derivation. Representative outputs are \(1+3T+12T^2+8T^3+8T^4\) for \((q,s)=(2,4)\), and \(1+15T+48T^2+48T^3\) for \((q,s)=(4,3)\). Execute `python3 verify.py`. The successful end marker is `VERIFY_OK_EVEN_ODD_DERIVATIONS`. These finite checks corroborate; they do not replace the symbolic proof for all fields and \(s\).

## Relationship to prior work

Premet, *Regular derivations of truncated polynomial rings*, arXiv:1405.2426 (first publicly posted 2014-05-10), studies derivation Lie algebras, the restricted power map, nilpotent fibres, and regularity for algebras of the form \(K[X_1,\ldots,X_n]/(X_1^p,\ldots,X_n^p)\), under the explicit hypothesis \(p>2\) and algebraically closed ground field. Its main theorems concern regular elements and invariant-quotient geometry; its hypotheses do not cover the characteristic-two even–odd pair of ordinary one-variable truncations or the finite-field square-zero rank polynomial proved here.

Elementary facts about derivatives, truncated polynomial rings, and finite-field valuations are classical ingredients; no originality is claimed for them individually. The proposed contribution is the explicit parity-stabilizing restricted Lie isomorphism *combined with* an exact square-zero rank-fibre distribution. Targeted searches of published mathematical records and related literature did not locate this full statement. Bibliographic priority is not independently established, and an equivalent representation-theoretic statement may be present in older modular Witt-algebra literature under different language.

## Limitations

The theorem is specific to characteristic \(2\), ordinary one-variable monomial truncations, and *square-zero* derivations for the enumerative assertion. It does not classify conjugacy orbits of derivations under algebra automorphisms, nor does it compute all possible ranks of nonsquare-zero derivations. In other characteristics the displayed linear intertwiner and isomorphism need not exist. The exhaustive computer tests establish only their explicitly listed finite cases. The general proof is symbolic; independent mathematical verification has not been performed.

## References

1. A. Premet, *Regular derivations of truncated polynomial rings*, arXiv:1405.2426, first version publicly submitted 10 May 2014; full text available at https://arxiv.org/pdf/1405.2426. The source assumes odd characteristic and studies different fibres.
2. Standard commutative-algebra identities for \(K[t]/(t^m)\): the Leibniz rule, the universal property of the quotient, and elementary valuation counts. These are used with complete computations above, not as an external novelty claim.
