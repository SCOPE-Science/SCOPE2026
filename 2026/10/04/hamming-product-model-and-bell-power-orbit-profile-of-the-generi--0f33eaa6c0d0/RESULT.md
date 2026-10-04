# Hamming-product model and Bell-power orbit profile of the generic Boolean ultrametric space

## Finding
Fix \(d\ge1\) and let \(B_d=\mathcal P([d])\), ordered by inclusion, with join union. The generic \(B_d\)-ultrametric space has the concrete model
\[
U_d=\mathbb N^d,\qquad \delta(x,y)=\{i\in[d]:x_i\ne y_i\}.
\]
Its isometry group is \(\operatorname{Aut}(U_d)=S_\infty^d\), acting independently on coordinates. Thus, if \(b_d(n)\) counts orbits on all ordered \(n\)-tuples and \(a_d(n)\) counts orbits on injective ordered \(n\)-tuples, then
\[
b_d(n)=B_n^d,\qquad a_d(n)=\sum_{k=1}^n s(n,k)B_k^d,
\]
where \(B_n\) is the Bell number and \(s(n,k)\) is the signed Stirling number of the first kind. Equivalently, \(a_d(n)\) counts \(d\)-tuples of partitions of \([n]\) whose meet is discrete. For \(d=2\), the injective profile starts \(1,3,15,113,1153,15125,245829,4815403\), while the all-tuple profile starts \(1,4,25,225,2704,41209,769129,17139600\).

## Assumptions and scope
Automorphisms are isometries of the labeled \(B_d\)-valued metric, so the Boolean atoms themselves are fixed rather than permuted. The parameter \(d\) is finite. “Generic” means the Fraïssé limit of all finite \(B_d\)-ultrametric spaces in the standard Braunfeld–Simon sense.

## Proof
For each \(i\in[d]\), put \(xE_i y\) iff \(i\notin d(x,y)\). The ultrametric inequality \(d(x,z)\subseteq d(x,y)\cup d(y,z)\) makes each \(E_i\) an equivalence relation, and \(d(x,y)=\varnothing\iff x=y\) gives \(\bigcap_iE_i=\Delta\). Conversely, any \(d\) equivalence relations with common intersection \(\Delta\) define a \(B_d\)-ultrametric by \(d(x,y)=\{i:\neg(xE_i y)\}\).

On \(\mathbb N^d\), take \(E_i\) to be equality in coordinate \(i\). Every finite \(B_d\)-ultrametric embeds by assigning a distinct natural-number label to each \(E_i\)-class in coordinate \(i\). A finite partial isometry preserves every \(E_i\), hence induces a finite partial bijection of the coordinate labels; extend each of these to a permutation \(\sigma_i\in S_\infty\). Their coordinatewise product extends the partial isometry. Therefore \(U_d\) is universal and homogeneous, hence is the generic \(B_d\)-ultrametric.

Every coordinatewise \(d\)-tuple of permutations is an isometry. Conversely, every isometry preserves each labeled \(E_i\), so it induces one permutation on the set of \(E_i\)-classes in each coordinate and is exactly their coordinatewise product. Hence \(\operatorname{Aut}(U_d)=S_\infty^d\).

For an ordered \(n\)-tuple, coordinate \(i\) determines the equality partition \(\pi_i\) of \([n]\). The ordered list \((\pi_1,\ldots,\pi_d)\) is a complete orbit invariant and every such list occurs, giving \(b_d(n)=B_n^d\). The tuple is injective exactly when \(\pi_1\wedge\cdots\wedge\pi_d=\hat0\). Hence \(a_d(n)\) is Canfield's \(M_n(d)\), and the usual equality-pattern decomposition
\[
B_n^d=\sum_{k=1}^n \left\{ {n\atop k} \right\}a_d(k)
\]
inverts to \(a_d(n)=\sum_{k=1}^n s(n,k)B_k^d\).

## Verification
The accompanying `verify.py` generates set partitions as restricted-growth strings and directly counts tuples with discrete meet for \(d\le3\), \(n\le5\). It also computes Bell and Stirling numbers recursively, checks the closed formula and Stirling transform through \(n=10\), and reproduces Canfield's published \(d=2\) table through \(n=8\). The recorded replay ends with `VERIFY_OK`. The finite replay checks consequences only; universality and homogeneity are proved above.

## Relationship to prior work
Braunfeld and Simon define generic finite-distributive-lattice \(\Lambda\)-ultrametric spaces and give their equivalence-relation presentation. In the inspected primary pages, they do not specialize the Boolean case to \(\mathbb N^d\), identify the full isometry group as \(S_\infty^d\), or give the Bell-power orbit profile.

The partition enumeration is prior work: Canfield, building on Pittel, defines \(M_n(t)\) as the number of \(t\)-tuples of set partitions with discrete meet and proves \(M_n(t)=\sum_k s(n,k)B_k^t\). That formula and its numerical values are not claimed as new. The contribution here is the structural bridge identifying the generic Boolean-lattice ultrametric with a Hamming-support Cartesian power and thereby identifying its injective and full tuple-orbit profiles.

Targeted searches for the Boolean specialization, Hamming-support product, direct-product automorphism group, Bell-power orbit profile, and partition-meet reformulation found no prior statement of this combined model-theoretic result. The closest indexed findings concerned a different random distributive lattice and unrelated reduct groups.

## Limitations
An equivalent Boolean specialization could exist as unindexed folklore, in a thesis, or in uninspected parts of the literature. The Pittel–Canfield partition formula is explicitly known. If symmetries are enlarged to allow automorphisms of the Boolean lattice itself, coordinate permutations add a semidirect factor.

## References
1. Samuel Braunfeld and Pierre Simon, *The classification of homogeneous finite-dimensional permutation structures*, arXiv:1807.07110; Electronic Journal of Combinatorics 27(1), P1.38 (2020), DOI 10.37236/8321. First public version: 2018-07-18.
2. E. Rodney Canfield, *Meet and Join within the Lattice of Set Partitions*, Electronic Journal of Combinatorics 8(1), R15 (2001), DOI 10.37236/1559.
3. Samuel Braunfeld, *Ramsey expansions of \(\Lambda\)-ultrametric spaces*, arXiv:1710.01193.
