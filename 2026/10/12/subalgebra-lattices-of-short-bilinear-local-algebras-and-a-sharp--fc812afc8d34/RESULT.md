# Subalgebra lattices of short bilinear local algebras and a sharp characteristic-two rank ambiguity

## Finding

Let \(k=\mathbb F_q\), \(n\ge1\), and let \(B\) be a nonzero symmetric bilinear form on an \(n\)-dimensional \(k\)-space \(V\). Put \(A_B=k1\oplus V\oplus kz\), with products \(uv=B(u,v)z\) and \(z(V\oplus kz)=0\). The following theorem gives the full lattice of unital \(k\)-subalgebras and determines exactly what its dimension-counting polynomial can distinguish.

**Structural classification.** Every unital subalgebra occurs exactly once in one of two families:

\[
Z(U)=k1\oplus U\oplus kz\quad (U\le V),
\]
\[
I(U,f)=k1\oplus\{u+f(u)z:u\in U\}
\quad (B(U,U)=0,\ f\in U^*).
\]

Inclusions are precisely
\[
\begin{aligned}
Z(U)\subseteq Z(W)&\Longleftrightarrow U\le W,\\
I(U,f)\subseteq I(W,g)&\Longleftrightarrow U\le W\text{ and }g|_U=f,\\
I(U,f)\subseteq Z(W)&\Longleftrightarrow U\le W,
\end{aligned}
\]
and no \(Z(U)\) lies in an \(I(W,g)\). In particular, this explicitly determines the entire subalgebra lattice, not merely its size.

Let \(I_d(B)\) be the number of \(d\)-dimensional totally \(B\)-isotropic subspaces, with \(I_0(B)=1\). Write \({n\brack d}_q\) for a Gaussian binomial coefficient and take it to be zero outside \(0\le d\le n\). The subalgebra dimension enumerator is
\[
\boxed{P_{A_B}(t)=\sum_{d=0}^{n+1}\left({n\brack d-1}_q+q^d I_d(B)\right)t^d,}
\]
where \(P_{A_B}(t)=\sum_S t^{\dim_kS-1}\), summing over unital \(k\)-subalgebras.

**Sharp reconstruction.** For fixed \(q,n\), if \(q\) is odd, equality of \(P_{A_B}\) and \(P_{A_C}\) holds **if and only if** \(A_B\cong_k A_C\). If \(q\) is even, equality of those polynomials holds **if and only if** the complete unital-subalgebra lattices are isomorphic. More precisely, in even characteristic the possibilities are: both forms are alternating of the same rank; or both are nonalternating with the same \(\lceil\operatorname{rank}(B)/2\rceil\). Consequently nonalternating consecutive ranks \(2h-1\) and \(2h\), whenever \(2h\le n\), produce **nonisomorphic algebras with isomorphic complete subalgebra lattices**.

The smallest example, valid over every \(\mathbb F_{2^e}\), is \(n=2\) with \(B_1=\operatorname{diag}(1,0)\) and \(B_2=\operatorname{diag}(1,1)\): both have
\[
P(t)=1+(q+1)t+(q+1)t^2+t^3,
\]
but the first has socle dimension two and the second is Gorenstein (socle dimension one). Thus even the full unital-subalgebra lattice need not detect the Gorenstein property in characteristic two.

## Assumptions and scope

All subalgebras contain the same identity and are \(k\)-linear. The form \(B\) is symmetric and nonzero but need not be nonsingular. The product extends by bilinearity from \(1\) as identity, \(uv=B(u,v)z\) for \(u,v\in V\), and every product involving \(z\) and an element of \(V\oplus kz\) as zero. The resulting \(k\)-algebra is commutative, associative, split local, has \(\mathfrak m=V\oplus kz\), \(\mathfrak m^2=kz\), and \(\mathfrak m^3=0\). Conversely, every split commutative local \(k\)-algebra with these radical-layer dimensions has this presentation after choosing a complement and a generator of the square.

Two such algebras are isomorphic exactly when their defining symmetric bilinear forms are similar: a change of basis in \(V\), together with a nonzero scaling of \(z\), identifies the forms. Indeed, an algebra isomorphism must preserve \(\mathfrak m\) and \(\mathfrak m^2\); the induced map on \(\mathfrak m/\mathfrak m^2\) and on \(\mathfrak m^2\) gives the required similarity. The socle has dimension \(n-\operatorname{rank}(B)+1\), so the algebra is Gorenstein precisely when \(B\) is nondegenerate.

## Proof

**1. Complete lattice.** Since \(A_B/\mathfrak m=k\), any unital \(k\)-subalgebra is uniquely \(k1\oplus W\), with a linear subspace \(W\le\mathfrak m\). If \(z\in W\), its projection \(U\) onto \(V\) gives \(W=U\oplus kz\) and closure is automatic. Otherwise projection to \(V\) is injective, so \(W\) is the graph of a unique linear map \(f:U\to k\); closure is equivalent to \(B(U,U)=0\). Checking containment of vector-space graphs gives exactly the asserted inclusion rules. Each subalgebra admits a chain of subalgebras starting at \(k1\) and increasing the vector-space dimension by exactly one at each step: use flags of \(U\) for graph-type subalgebras, and pass from \(k1\) through \(k1\oplus kz\) and then a flag of \(U\) for subalgebras containing \(z\). Strict inclusion always increases vector-space dimension, so the intrinsic height of a subalgebra in this lattice is exactly \(\dim_k S-1\). Consequently abstract lattice isomorphisms preserve subalgebra dimensions and the polynomial \(P_{A_B}\). For \(\dim U=d\), the first class contributes \({n\brack d}_q\) subalgebras in dimension \(d+2\), and the second contributes \(q^d I_d(B)\) in dimension \(d+1\); reindexing proves the polynomial.

**2. Completely explicit isotropic counts.** Let \(s=n-r\), where \(r=\operatorname{rank}B\), and let \(\overline B\) be its nonsingular quotient on \(V/\operatorname{rad} B\). For each integer \(d\ge0\),
\[
\boxed{I_d(B)=\sum_{a+b=d}{s\brack a}_q q^{b(s-a)}I_b(\overline B).}
\]
Indeed, a totally isotropic \(d\)-space meets the form radical in an \(a\)-space, projects to a totally isotropic \(b\)-space in the quotient, and is determined by a lift in a vector space of dimension \(b(s-a)\). All sums below use \(I_b=0\) when \(b\) is outside the possible range.

For clarity, set
\[
S_h(b)=\begin{cases}\displaystyle\prod_{i=0}^{b-1}\frac{q^{2(h-i)}-1}{q^{b-i}-1},&0\le b\le h,\\0,&\text{otherwise},\end{cases}
\]
with an empty product equal to one. For nonsingular quotient rank \(r\), the exact input to the preceding formula is:

- Odd characteristic, \(r=2h+1\): \(I_b=S_h(b)\).
- Odd characteristic, \(r=2h\), split orthogonal type: \(I_b=\displaystyle\prod_{i=0}^{b-1}\frac{(q^{h-i}-1)(q^{h-i-1}+1)}{q^{b-i}-1}\) for \(0\le b\le h\), otherwise zero.
- Odd characteristic, \(r=2h\), nonsplit orthogonal type: \(I_b=\displaystyle\prod_{i=0}^{b-1}\frac{(q^{h-i}+1)(q^{h-i-1}-1)}{q^{b-i}-1}\) for \(0\le b\le h-1\), otherwise zero.
- Even characteristic, alternating rank \(r=2h\): \(I_b=S_h(b)\).
- Even characteristic, nonalternating rank \(r=2h+1\): \(I_b=S_h(b)\).
- Even characteristic, nonalternating rank \(r=2h\): \(I_b=q^bS_{h-1}(b)+S_{h-1}(b-1)\).

The odd-characteristic and alternating formulas follow by counting incident pairs of totally isotropic subspaces of consecutive dimensions: after choosing a \((b-1)\)-space, its orthogonal quotient is of the same polar type with two fewer dimensions, and each \(b\)-space contains \((q^b-1)/(q-1)\) such \((b-1)\)-spaces. The required numbers of singular lines in a nonsingular space of rank \(2j+1\), split \(2j\), nonsplit \(2j\), and alternating \(2j\) are respectively \((q^{2j}-1)/(q-1)\), \((q^j-1)(q^{j-1}+1)/(q-1)\), \((q^j+1)(q^{j-1}-1)/(q-1)\), and \((q^{2j}-1)/(q-1)\). This proves the products by induction starting from \(I_0=1\).

For characteristic two with nonalternating \(B\), \(v\mapsto \sqrt{B(v,v)}\) is a nonzero \(k\)-linear functional, and a subspace is totally \(B\)-isotropic exactly when it is totally isotropic for the alternating restriction of \(B\) to the kernel \(H\) of that functional. To verify its rank, in the nonsingular quotient choose \(t\) with \(B(t,v)=\sqrt{B(v,v)}\) for all \(v\), so \(H=t^\perp\). A nonalternating nonsingular symmetric form over a finite field of characteristic two is congruent to the identity matrix; its characteristic vector \(t\) belongs to \(H\) precisely when its rank is even. Thus for odd rank \(2h+1\), \(B|_H\) is nonsingular alternating of rank \(2h\), while for even rank \(2h\), the restriction has rank \(2h-2\) and one-dimensional radical. Applying the displayed degeneracy formula yields the two even-characteristic nonalternating expressions.

**3. Odd-characteristic recognition.** The coefficients of \(P\) recover every \(I_d(B)\), since \(q,n\) are given. The number of zero vectors of the quadratic function \(v\mapsto B(v,v)\) is \(Z=1+(q-1)I_1(B)\). The standard finite-field quadratic Gauss-sum evaluation, obtainable by diagonalizing the nonsingular part and summing the additive characters, yields
\[
Z=\begin{cases}
q^{n-1},&r=2h+1,\\
q^{n-1}+\varepsilon(q-1)q^{n-h-1},&r=2h,
\end{cases}
\]
where \(\varepsilon=+1\) for split and \(-1\) for nonsplit even rank. If the deviation is nonzero, its size and sign recover \(h\) and the orthogonal type. If it vanishes, the rank is odd, and \(w=\max\{d:I_d(B)>0\}=n-h-1\) recovers \(h\). Over a finite field of odd characteristic, these data determine a symmetric form up to similarity: there is one odd-rank similarity class and two even-rank classes. Consequently \(P\) determines \(A_B\) up to algebra isomorphism.

**4. Characteristic-two recognition and collisions.** The invariant \(I_1(B)\) identifies whether \(B\) is alternating: in that case every line is isotropic and \(I_1=(q^n-1)/(q-1)\); otherwise \(I_1=(q^{n-1}-1)/(q-1)\). For an alternating \(B\) of rank \(2h\), the maximal isotropic dimension is \(w=n-h\), recovering its rank, and alternating forms of equal rank are congruent. For nonalternating \(B\) of rank either \(2h-1\) or \(2h\), the alternating form \(B|_H\) has rank \(2h-2\) and radical dimension \(n-2h+1\), and the maximal totally isotropic dimension is again \(w=n-h\). Thus \(P\) recovers \(h\), but not which of the two consecutive ranks occurs. Conversely, two such nonalternating forms with the same \(h\) have linearly isomorphic hyperplanes \(H\) with congruent restricted alternating forms. Extend this isomorphism to \(g:V\to V'\). The map
\[
Z(U)\longmapsto Z(gU),\qquad I(U,f)\longmapsto I(gU,f\circ g^{-1}|_{gU})
\]
is a bijective order-preserving map of the complete subalgebra lattices by the inclusion rules in step 1. Their ranks may differ, so the algebras are nonisomorphic despite the lattice isomorphism. The smallest example follows with \(n=2\), completing the proof.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. Run `python3 verify.py`. It constructs the algebra multiplication directly from symmetric-form matrices, enumerates every vector subspace of \(\mathfrak m\) by reduced row echelon bases, tests multiplication closure independently, and compares its complete dimension histogram with the Gaussian/polar formulas. It checks nondegenerate forms over field orders \(2,3,4,5,7\), including the nonprime field \(\mathbb F_4\), and degenerate forms over field orders \(2,3,4\), with ranks and both available orthogonal/alternating types as applicable. It also checks that collisions in the tested cases follow the stated characteristic dichotomy. Successful execution prints `VERIFY_OK` and `VERIFY_GENERAL_OK`. These tests cover only finite instances: the full theorem is justified by the proof above, not by experimental extrapolation.

## Relationship to prior work

Elias and Rossi (2012) study analytic isomorphism classes of short Artinian Gorenstein rings, with an emphasis on socle degree three over characteristic-zero fields. Jelisiejew (2015) develops inverse-system classifications for local Artinian Gorenstein algebras and includes the quadratic-form context relevant to socle degree two. Neither inspected treatment gives the full finite-field lattice of all unital subalgebras or this sharp rank-pair obstruction in characteristic two. Iovanov and Sistko (2017) classify maximal subalgebras of finite-dimensional algebras: that covers the top layer of the present poset, not its lower strata, dimension enumerator, or reconstruction/collision classification. Classical finite polar-space counts, including symplectic isotropic-subspace formulas, are used as known combinatorial input and are not claimed as new. Classical symplectic polar-space subspace counts are used only as background; the present contribution is the complete degenerate/form-type lattice and reconstruction theorem.

## Limitations

The theorem concerns unital \(k\)-linear subalgebras for the stated radical-cube-zero, one-dimensional-radical-square family. It is not a classification of arbitrary finite-dimensional local algebras, higher-dimensional radical squares, or subalgebras not containing the identity. Isomorphism of lattices does not assert isomorphism of rings. Bibliographic comparison is substantial but cannot exclude every equivalent formulation; there has been no independent external verification.

## References

1. J. Elias and M. E. Rossi, “Isomorphism Classes of Short Gorenstein Local Rings via Macaulay's Inverse System,” *Transactions of the American Mathematical Society* **364** (2012), 4589–4604. DOI: 10.1090/S0002-9947-2012-05430-4; electronically published April 11, 2012.
2. J. Jelisiejew, “Classifying local Artinian Gorenstein algebras,” arXiv:1511.08007v1 (public November 25, 2015).
3. M. C. Iovanov and Z. Sistko, “Maximal Subalgebras of Finite-Dimensional Algebras,” arXiv:1705.00762v1 (public May 2, 2017).
