# The domination polynomial is complete on finite CC-ring commuting graphs

## Finding

Let \(R\) be a finite noncommutative CC-ring, meaning that the centralizer of every noncentral element is commutative, and let \(\Gamma_R\) be its commuting graph. If \(S_1,\ldots,S_t\) are the distinct centralizers of noncentral elements and \(m_i=|S_i|-|Z(R)|\), then \[D(\Gamma_R,x)=\prod_{i=1}^t\big((1+x)^{m_i}-1\big).\] Moreover this polynomial uniquely determines the multiset \(\{m_1,\ldots,m_t\}\). Consequently, for finite CC-rings \(R\) and \(T\), \[D(\Gamma_R,x)=D(\Gamma_T,x)\iff \Gamma_R\cong\Gamma_T.\] Equivalently, the ordinary domination polynomial is a complete isomorphism invariant on the class of finite CC-ring commuting graphs, even though the same polynomial need not determine the graph among arbitrary finite graphs. If additionally \(R/Z(R)\cong C_p\times C_p\), then the polynomial also recovers \(p\), \(|Z(R)|\), and \(|R|\).

The reconstruction is explicit. Put
\[
Q_R(y)=D(\Gamma_R,y-1).
\]
For every positive integer \(d\), let
\[
E_d=v_{\Phi_d}(Q_R),
\]
the exponent of the \(d\)-th cyclotomic polynomial in \(Q_R\). If
\[
a_m=\#\{i:m_i=m\},
\]
then
\[
E_d=\sum_{d\mid m}a_m
\]
and therefore
\[
a_m=\sum_{k\ge1}\mu(k)E_{km},
\]
where the sum is finite. Thus the component-size multiset is recovered coefficient-free from the cyclotomic factorization of the shifted domination polynomial.

## Assumptions and scope

For a noncommutative ring \(R\) with center \(Z(R)\), the commuting graph \(\Gamma_R\) has vertex set
\[
R\setminus Z(R),
\]
with two distinct vertices adjacent exactly when they commute.

A finite ring \(R\) is a CC-ring when every centralizer of a noncentral element is a commutative subring. Let
\[
S_1,\ldots,S_t
\]
be the distinct centralizers of noncentral elements and define
\[
m_i=|S_i|-|Z(R)|.
\]

The domination polynomial of a finite graph \(G\) is
\[
D(G,x)=\sum_{k}d(G,k)x^k,
\]
where \(d(G,k)\) counts dominating sets of cardinality \(k\).

The theorem concerns equality of domination polynomials inside the class of commuting graphs arising from finite CC-rings. It does not claim that these graphs are domination-unique among all finite graphs.

## Proof

Dutta and Nath prove that for a finite CC-ring, distinct noncentral centralizers intersect exactly in the center and
\[
\Gamma_R\cong\bigsqcup_{i=1}^t K_{m_i}.
\tag{1}
\]
Indeed, the noncentral part of each centralizer is a clique, and the CC condition prevents a noncentral element from lying in two distinct such centralizers.

For a complete graph,
\[
D(K_m,x)=(1+x)^m-1,
\]
because every nonempty vertex subset dominates. The domination polynomial is multiplicative over connected components, so (1) gives
\[
D(\Gamma_R,x)=\prod_{i=1}^t\big((1+x)^{m_i}-1\big).
\tag{2}
\]

It remains to prove that the multiset of positive integers \(m_i\) is determined by the product in (2). Set
\[
y=1+x
\]
and write
\[
Q_R(y)=D(\Gamma_R,y-1)
      =\prod_{i=1}^t(y^{m_i}-1).
\tag{3}
\]
Over \(\mathbb Z[y]\),
\[
y^m-1=\prod_{d\mid m}\Phi_d(y),
\]
where \(\Phi_d\) is the \(d\)-th cyclotomic polynomial. Unique factorization therefore makes the exponent
\[
E_d=v_{\Phi_d}(Q_R)
\]
an invariant of \(D(\Gamma_R,x)\), and (3) gives
\[
E_d=\#\{i:d\mid m_i\}.
\tag{4}
\]

If
\[
a_m=\#\{i:m_i=m\},
\]
then (4) is
\[
E_d=\sum_{k\ge1}a_{kd}.
\]
Möbius inversion on the divisibility poset yields
\[
a_m=\sum_{k\ge1}\mu(k)E_{km}.
\tag{5}
\]
Only finitely many terms are nonzero. Equation (5) recovers every multiplicity \(a_m\), hence the complete component-size multiset.

A disjoint union of complete graphs is determined up to graph isomorphism by its multiset of component sizes. Therefore, for finite CC-rings \(R\) and \(T\),
\[
D(\Gamma_R,x)=D(\Gamma_T,x)
\]
if and only if
\[
\Gamma_R\cong\Gamma_T.
\]

Finally, suppose
\[
R/Z(R)\cong C_p\times C_p.
\]
The known CC-ring decomposition gives
\[
\Gamma_R\cong (p+1)K_{(p-1)|Z(R)|}.
\]
The recovered component multiset therefore has
\[
t=p+1
\]
equal components, each of order
\[
m=(p-1)|Z(R)|.
\]
Hence
\[
p=t-1,
\qquad
|Z(R)|=\frac{m}{p-1},
\qquad
|R|=p^2|Z(R)|.
\]
All three quantities are therefore determined by the domination polynomial.

## Verification

The accompanying `verify.py` uses only the Python standard library.

It constructs domination polynomials of cluster graphs, performs the substitution \(y=1+x\), builds cyclotomic polynomials recursively, factors the shifted polynomial by exact integer polynomial division, and reconstructs every component multiplicity using the divisibility inversion above.

It exhaustively checks every integer partition of every total graph order through \(12\); no two distinct cluster profiles have the same domination polynomial, and every profile is reconstructed exactly. It also constructs the commuting graph of the upper-triangular matrix ring
\[
UT_2(\mathbb F_p)
\]
directly from matrix multiplication for \(p=2\) and \(p=3\). These graphs have the predicted profiles
\[
3K_2
\quad\text{and}\quad
4K_6,
\]
respectively. For \(p=2\), all \(2^6\) vertex subsets are enumerated to verify the domination polynomial directly.

Exact output:

```text
VERIFY_OK
cluster_profiles_exhaustive_total_order_le_12=271
UT2_F2_noncentral=6 center=2 components=3xK2 brute_polynomial=matched
UT2_F3_noncentral=24 center=3 components=4xK6
cyclotomic_profile_reconstruction=passed
```

The finite checks are corroborative only. The general theorem is the unique-factorization argument above.

## Relationship to prior work

Dutta and Nath prove the structural decomposition (1) for finite CC-rings and use it to compute spectra and genera of their commuting graphs. Their theorem supplies the algebraic cluster-graph structure but does not study domination polynomials or reconstruction from them.

Alikhani proves that domination polynomials multiply over connected components. Jahari and Alikhani later study domination equivalence and explicitly show that graphs such as
\[
K_{n_1}\cup\cdots\cup K_{n_t}
\]
can have nonisomorphic domination-equivalent graphs obtained by adding irrelevant edges between clique blocks. They leave the full domination-equivalence class of such clique unions open.

The present result is deliberately narrower and different: it does not claim global domination-uniqueness. Instead, it proves that inside the finite CC-ring commuting-graph class, the polynomial uniquely recovers the clique-component multiset by cyclotomic inversion. Thus the domination polynomial becomes a complete graph-isomorphism invariant on this algebraically defined class even though it is not complete on arbitrary graphs with the same polynomial.

A later finite-ring commuting-graph paper lists \(16P10\) first in its Mathematics Subject Classification, consistent with treating the ring/centralizer structure as the primary algebraic object here.

## Limitations

Equality of domination polynomials does not imply graph isomorphism outside the CC-ring commuting-graph class. In particular, known constructions add domination-irrelevant edges to clique unions without changing the polynomial.

The theorem recovers
\[
|C_R(a)|-|Z(R)|
\]
for the distinct noncentral centralizers, not the center size or the ring isomorphism type in general. The stronger recovery of \(|Z(R)|\) and \(|R|\) is asserted only for the subclass
\[
R/Z(R)\cong C_p\times C_p.
\]

No claim is made that two CC-rings with isomorphic commuting graphs are isomorphic as rings.

## References

1. J. Dutta and R. K. Nath, “Spectrum and genus of commuting graphs of some classes of finite rings,” arXiv:1604.02865, first posted 11 April 2016.
2. S. Jahari and S. Alikhani, “On \(\mathcal D\)-equivalence classes of some graphs,” arXiv:1511.00159, first posted 31 October 2015.
3. S. Alikhani, “On the Domination Polynomial of Some Graph Operations,” *International Scholarly Research Notices* 2013, Article 146595. DOI: 10.1155/2013/146595.
4. W. N. T. Fasfous, R. K. Nath, and R. Sharafdini, “Various spectra and energies of commuting graphs of finite rings,” *Hacettepe Journal of Mathematics and Statistics* 49 (2020), 1915–1925. DOI: 10.15672/hujms.540309.
