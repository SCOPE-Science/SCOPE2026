# Dihedral conjugacy and rank enumeration of retractions of finite cycles

## Finding

Let \(C_n\) be the undirected, loopless cycle with vertex set \(\mathbb Z/n\mathbb Z\), for \(n\ge3\). Let \(M_n=\operatorname{End}(C_n)\) denote **full graph endomorphisms** (adjacent vertices must have adjacent, hence unequal, images). Write \(\mathcal I_n=\{f\in M_n:f^2=f\}\). Define the labeled rank enumerator and the **unit-conjugacy** rank enumerator by
\[
E_n(z)=\sum_{f\in\mathcal I_n}z^{|\operatorname{im}f|},\qquad
K_n(z)=\sum_{[f]\in\mathcal I_n/\operatorname{Aut}(C_n)}z^{|\operatorname{im}f|},
\]
where \(\operatorname{Aut}(C_n)\) acts by \(f\mapsto gfg^{-1}\).

For odd \(n\ge3\), both polynomials equal \(z^n\). For even \(n=2m\ge4\), set \(L_{m,k}=2m-k\) for \(1\le k\le m\), and let \(A_k\) be the ordinary adjacency matrix of the \((k+1)\)-vertex path on \(\{0,1,\ldots,k\}\). Define
\[
b_{m,k}=(A_k^{L_{m,k}})_{k,0}
\]
and the reflection-fixed number
\[
s_{m,k}=\begin{cases}
(A_k^{L_{m,k}/2})_{k,k/2},&k\text{ even},\\
(A_k^{(L_{m,k}-1)/2})_{k,(k-1)/2}+(A_k^{(L_{m,k}-1)/2})_{k,(k+1)/2},&k\text{ odd}.
\end{cases}
\]
Then, **for every** \(m\ge2\),
\[
\boxed{E_{2m}(z)=z^{2m}+2m\sum_{k=1}^{m}b_{m,k}z^{k+1}},\qquad
\boxed{K_{2m}(z)=z^{2m}+\sum_{k=1}^{m}\frac{b_{m,k}+s_{m,k}}2z^{k+1}}.
\]
The division by two is integral in each summand. In particular, for every proper rank \(k+1\), all unit-conjugacy classes are described by nearest-neighbor walks of length \(2m-k\) from \(k\) to \(0\) inside \(\{0,\ldots,k\}\), modulo reversing the walk and complementing heights.

There is also a finite coefficient formula. Put \(F_0(u)=F_1(u)=1\) and \(F_j(u)=F_{j-1}(u)-uF_{j-2}(u)\) for \(j\ge2\). Then
\[
b_{m,k}=[u^{m-k}]\frac{1}{F_{k+1}(u)}
=\sum_{j\in\mathbb Z}\left(\binom{2m-k}{m+j(k+2)}-\binom{2m-k}{m+1+j(k+2)}\right),
\]
where out-of-range binomial coefficients are zero and the sum has finite support. Summing over \(k\) counts Dyck paths of semilength \(m\) whose **initial ascent reaches their maximum height**, giving the previously catalogued unranked Dyck sequence after the explicit factor \(2m\).

## Assumptions and scope

Every integer parameter is finite. Graphs are undirected and simple, with **no loops**; hence a full endomorphism never identifies adjacent vertices. A rank means the number of image vertices, not the minimum size of a generating set. Unit-conjugacy is conjugation by the graph's dihedral automorphism group, not natural conjugacy, Green's \(\mathcal D\)-relation, or semigroup conjugacy under arbitrary nonunits. The formulas do not concern weak endomorphisms, partial graph maps, or metric partial isometries.

## Proof

**1. Odd cycles.** An endomorphism \(f\) of \(C_n\) is a closed walk of \(n\) nearest-neighbor steps \(\pm1\) modulo \(n\). Its signed displacement must be divisible by \(n\), and has absolute value at most \(n\). For odd \(n\), this displacement cannot be zero by parity; it is thus \(\pm n\). All step signs are equal, so \(f\) is a rotation or a reflection. An idempotent in this finite group is the identity. This includes \(n=3\).

**2. Exact image classification on even cycles.** The image of every idempotent endomorphism is fixed pointwise: \(f(y)=y\) whenever \(y\in\operatorname{im}f\). Since the image is connected, if it is a proper vertex subset it is a consecutive arc \(I\) of \(k+1\) vertices, for some \(1\le k<n\). The complementary cycle arc is a path with \(L=n-k\) edges joining the same endpoints. As the fixed image endpoints are distance \(k\) apart inside \(I\), the complementary path can map into \(I\) only when \(L\ge k\), so \(1\le k\le m\) for \(n=2m\). Conversely, fix \(I=\{0,\ldots,k\}\) pointwise and assign to the complementary arc any nearest-neighbor walk \(w(0)=k,w(L)=0\) with \(0\le w(t)\le k\). The resulting function is an idempotent graph endomorphism of rank \(k+1\). This correspondence is bijective. There are exactly \(n=2m\) possible image arcs for each \(k\le m\), which proves the labeled formula; the only idempotent of full rank is the identity.

**3. Unit conjugacy and its fixed points.** The dihedral group \(\operatorname{Aut}(C_n)\) acts transitively on the \(n\) image arcs of each given length, and the stabilizer of one proper arc consists of the identity and the reflection \(r:x\mapsto k-x\pmod n\). On the complementary path, this reflection sends the walk to \(r\cdot w\) with \((r\cdot w)(t)=k-w(L-t)\). Hence its two-element action has \((b_{m,k}+s_{m,k})/2\) orbits by Burnside's lemma. A fixed walk satisfies \(w(t)+w(L-t)=k\). If \(L\) is even, necessarily \(k\) is even; the midpoint is \(k/2\), and the first \(L/2\) steps determine the remaining steps uniquely, giving the first displayed formula for \(s_{m,k}\). If \(L\) is odd, \(k\) is odd; the central edge must join \((k-1)/2\) and \((k+1)/2\), and the first \((L-1)/2\) steps determine the rest, giving the second formula. Distinct image-ranks are never conjugate. Summing the orbit numbers and adding the fixed identity proves the formula for \(K_{2m}\).

**4. Coefficient formula.** The usual walk resolvent and the unique shortest walk yield
\[
\sum_{\ell\ge0}(A_k^{\ell})_{k,0}t^{\ell}=\frac{t^k}{\det(I-tA_k)}.
\]
The path determinant \(D_{k+1}(t)=\det(I-tA_k)\) satisfies \(D_0=D_1=1\) and \(D_j=D_{j-1}-t^2D_{j-2}\), by last-row expansion; therefore \(D_{k+1}(t)=F_{k+1}(t^2)\). Taking the coefficient of \(t^{2m-k}\) proves \(b_{m,k}=[u^{m-k}]/F_{k+1}(u)\). The second binomial expression follows independently from the reflection principle for a nearest-neighbor path confined to the integer interval \([0,k]\): the free-walk count from \(k\) to \(0\) is corrected by reflected paths crossing either forbidden boundary \(-1\) or \(k+1\), with reflection period \(k+2\).

**5. Dyck interpretation.** Given a strip walk, prepend \(k\) up-steps from height \(0\) to height \(k\). The combined walk has \(2m\) steps, ends at \(0\), stays nonnegative, and its initial ascent attains the global maximum \(k\). Conversely, remove the maximal initial ascent of any such Dyck path to obtain exactly one strip walk of the prescribed kind. This establishes the asserted total-count correspondence without asserting that the Dyck paths avoid later returns to height \(k\).

## Verification

Two independent finite computations accompany the theorem. `verify_counts.py` enumerates full cycle graph homomorphisms directly by their local edge steps, filters by composition-idempotence, and compares every rank with both the strip adjacency-matrix formula and its binomial-reflection version for cycle lengths \(3\) through \(16\). `verify_orbits.py` directly constructs all such idempotents for lengths \(3\) through \(15\), forms complete dihedral conjugacy orbits, and independently counts reflection-fixed strip walks; all rank coefficients agree. Run both scripts with an ordinary Python 3 installation, using `python verify_counts.py` and `python verify_orbits.py`. Both scripts depend only on the Python standard library.

For example, at \(n=10\) the labeled rank distribution at ranks \(2,3,4,5,6,10\) is respectively \((10,80,80,40,10,1)\); the corresponding unit-conjugacy distribution is \((1,4,5,2,1,1)\). The checks corroborate the proof but do not certify its all-parameter statements merely by finite enumeration.

## Relationship to prior work

Dimitrova, Fernandes, Koppitz, and Quinteiro, *On monoids of endomorphisms of a cycle graph*, arXiv:2310.04149v1 (public 2023-10-06), study the full and weak cycle-endomorphism monoids, including cardinality, regularity, Green's relations, and generating ranks. Their developed results give the precise algebraic setting, but not the rank enumeration of idempotent retracts or their unit-conjugacy orbit enumerator.

OEIS A287709 already records the number of Dyck paths whose initial ascent achieves the maximum, and the equivalent unrefined sequence. Thus **the Dyck sequence itself is not asserted to be new**. Axel Bacher's *Progressive and rushed Dyck paths*, initially public in 2024 (arXiv:2403.08120), studies a related, different refinement; a rushed path is further prohibited from revisiting its maximal height. Neither the OEIS entry nor the Dyck-path results classifies dihedral conjugacy classes of graph-endomorphism retractions. Lin and Zeng, *On the number of congruence classes of paths* (arXiv:1112.4026), address graph-homomorphism congruence counts for paths rather than conjugation orbits of cycle idempotents. The rank and reflection-fixed orbit formulas are the specific claimed additions, not a new count of the already known unrefined sequence.

## Limitations

The result concerns full adjacency-preserving maps only. It does not enumerate idempotents of weak endomorphism monoids, partial isometries, or partial automorphism monoids. The connection to OEIS A287709 does not claim that its total counts were undiscovered. The literature comparison is bounded to the cited accessible sources and performed searches; unindexed or differently formulated equivalent work remains possible. No independent mathematical validation has yet been performed.

## References

1. I. Dimitrova, V. H. Fernandes, J. Koppitz, T. M. Quinteiro, *On monoids of endomorphisms of a cycle graph*, arXiv:2310.04149v1, https://arxiv.org/html/2310.04149v1 (posted 2023-10-06).
2. OEIS A287709, https://oeis.org/A287709 (in particular the Asinowski--Jelínek Dyck-path characterization).
3. A. Bacher, *Progressive and rushed Dyck paths*, arXiv:2403.08120, https://arxiv.org/abs/2403.08120 (first public 2024-03-12).
4. Z. Lin and J. Zeng, *On the number of congruence classes of paths*, arXiv:1112.4026, https://arxiv.org/abs/1112.4026 (2011).
