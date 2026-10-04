# Fixed-content bracelet orbit profiles for Simon’s circular finite-cover quotients
## Finding
For each integer \(d\ge 1\), let \(M_d\) be the structure in Simon's second reduct example: start with the Fraïssé limit of finite separation relations carrying an equivalence relation whose classes all have size \(d\), and quotient by that equivalence relation. For \(k\ge 1\), write \(a_d(k)\) for the number of \(\operatorname{Aut}(M_d)\)-orbits on injective ordered \(k\)-tuples.

Then \(a_d(k)\) is exactly the number of dihedral bracelets of length \(dk\) with \(k\) labeled colors, each occurring exactly \(d\) times. Put \(N=dk\) and
\[
S_{d,k}=\sum_{\ell\mid d}\varphi(\ell)\frac{(N/\ell)!}{((d/\ell)!)^k}.
\]
Define the reflection contribution \(R_{d,k}\) by
\[
R_{d,k}=
\begin{cases}
N\dfrac{(N/2)!}{((d/2)!)^k},& d\text{ even},\\
d,& d\text{ odd and }k=1,\\
2d\dfrac{(d-1)!}{(((d-1)/2)!)^2},& d\text{ odd and }k=2,\\
0,& d\text{ odd and }k\ge3.
\end{cases}
\]
Then
\[
\boxed{a_d(k)=\frac{S_{d,k}+R_{d,k}}{2dk}}.
\]
For example,
\[
(a_1(k))_{k=1}^7=(1,1,1,3,12,60,360),
\]
\[
(a_2(k))_{k=1}^7=(1,2,11,171,5736,312240,24327000),
\]
and
\[
(a_3(k))_{k=1}^7=(1,3,94,15402,5605608,3811808040,4345461120240).
\]
For fixed \(d\), the identity rotation dominates the Burnside sum, giving
\[
\frac{\log a_d(k)}{k\log k}\longrightarrow d.
\]
Thus the finite-cover degree \(d\) is encoded by the ordered-tuple orbit-growth exponent. If \(b_d(n)\) denotes the number of orbits on all ordered \(n\)-tuples, repetitions allowed, then
\[
b_d(n)=\sum_{k=1}^n {n\brace k}a_d(k).
\]

## Assumptions and scope
The structure \(M_d\) is the quotient family described by Simon for each positive integer \(d\). The count concerns the full automorphism group of the quotient and ordered tuples of quotient points. The finite-cover model is used only to classify finite tuple types; no claim is made about unordered age profiles.

## Proof
Take an injective ordered tuple \((x_1,\ldots,x_k)\) in \(M_d\). Its preimage in the separation-relation cover consists of \(dk\) points partitioned into \(k\) named fibers of size \(d\). A finite separation relation is precisely a cyclic arrangement up to reversal. Therefore the finite type of the ordered tuple is represented by a cyclic word of length \(dk\) in symbols \(1,\ldots,k\), with each symbol occurring exactly \(d\) times, modulo rotation and reversal. Homogeneity of the Fraïssé cover and the quotient construction show that two injective tuples lie in the same automorphism orbit exactly when these fixed-content words are dihedrally equivalent.

Burnside's lemma now gives the formula. For a rotation whose cycles have length \(\ell\), a fixed word exists exactly when \(\ell\mid d\). There are \(\varphi(\ell)\) rotations with cycle length \(\ell\), and the cycles can be assigned to the \(k\) labels in
\[
\frac{(N/\ell)!}{((d/\ell)!)^k}
\]
ways, giving \(S_{d,k}\).

For reflections, if \(d\) is even then every color multiplicity can be paired, and each of the \(N\) reflections fixes
\[
\frac{(N/2)!}{((d/2)!)^k}
\]
words. If \(d\) is odd, a fixed word can use the reflection's fixed positions only to absorb odd multiplicities. This is possible for one odd color when \(k=1\), and for exactly two odd colors when \(k=2\); for \(k\ge3\) it is impossible. Counting the fixed-position assignments yields the displayed \(R_{d,k}\). Division by the dihedral group order \(2N\) proves the exact formula.

For fixed \(d\), every nonidentity rotation term and every reflection term is superexponentially smaller than the identity contribution \((dk)!/(d!)^k\). Stirling's formula therefore gives \(\log a_d(k)=dk\log k+O_d(k)\), proving the orbit-growth limit. Finally, an arbitrary ordered tuple is determined by its equality partition together with the injective orbit of its distinct values, giving the Stirling transform.

## Verification
The bundled verifier evaluates the closed formula using exact integer arithmetic and independently enumerates all fixed-content words up to dihedral equivalence whenever \(dk\le10\). It checks all pairs \((d,k)\) in that range, the displayed initial rows, and the \(d=1\) specialization to the generic separation relation. It prints `VERIFY_OK` on success.

## Relationship to prior work
Simon explicitly constructs this quotient family and proves that each member has no proper nontrivial reduct. His paper also emphasizes orbit-growth functions as natural invariants for homogeneous and \(\omega\)-categorical structures. The fixed-content bracelet enumeration itself is classical: Karim, Sawada, Alamgir and Husnine study generation of bracelets with fixed content, and OEIS A214609 records a Burnside formula for a prescribed content partition. The contribution here is the exact identification of Simon's quotient tuple-orbits with the equal-content bracelet problem, together with the resulting closed orbit profile and the recovery of the cover degree from its orbit-growth exponent.

## Limitations
The originality claim is for the model-theoretic bridge and its orbit-growth consequence, not for fixed-content bracelet enumeration in isolation. Searches did not locate a published statement making this identification for Simon's family, but unindexed folklore about finite covers and permutation-group profiles remains possible. The proof assumes the standard interpretation of the quotient structure induced by Simon's finite cover; it does not classify reducts beyond what Simon already proves.

## References
1. Pierre Simon, *NIP omega-categorical structures: the rank 1 case*, arXiv:1807.07102. Submitted 18 July 2018; primary MSC 03C15. Example 1.1 gives the size-two circular-cover quotient, and Section 6.7 describes the general separation-relation quotient with fiber cardinality \(d\) and proves it has no proper nontrivial reduct.
2. S. Karim, J. Sawada, Z. Alamgir, and S. M. Husnine, *Generating Bracelets with Fixed Content*, Theoretical Computer Science 475 (2013), 103–112, DOI 10.1016/j.tcs.2012.11.024.
3. OEIS A214609, fixed-content bracelet counts by content partition, including the general Burnside formula.
