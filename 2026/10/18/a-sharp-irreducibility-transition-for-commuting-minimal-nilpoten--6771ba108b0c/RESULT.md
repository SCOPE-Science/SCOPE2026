# The full component classification for commuting minimal-nilpotent matrix tuples

## Finding

Let \(k\) be algebraically closed, \(V=k^n\), \(n\ge4\) and \(r\ge1\). Let \(\mathcal C_{n,r}\) be the reduced variety of ordered pairwise commuting tuples \((A_1,\ldots,A_r)\) in which each \(A_i\) has rank at most one and satisfies \(A_i^2=0\). For \(1\le d<n\), let \(\mathcal X_d\) be the locus where there is a subspace \(U\) of dimension \(d\) with
\[
 A_i(V)\subseteq U\subseteq\ker A_i\quad\text{for all }i.
\]
Every \(\mathcal X_d\) is closed and irreducible. If \(n\ge2r\), the full variety is \(\mathcal X_r\), of dimension \(r(2n-r-1)\). If \(n<2r\), the irreducible components are exactly
\[
 \mathcal X_d,\qquad \max(1,n-r)\le d\le\min(r,n-1),
\]
of dimensions \(d(n-d)+r(n-1)\). In particular \(\mathcal C_{n,r}\) is irreducible if and only if \(n\ge2r\), and its dimension in the reducible range is \(r(n-1)+\lfloor n^2/4\rfloor\). The full list matters even when there is a unique component of largest dimension: for \((n,r)=(4,3)\), the three components have dimensions \(12,13,12\).

## Assumptions and scope

The geometry is over an algebraically closed field of arbitrary characteristic. Entries may be zero or equal; the locus of possible individual entries is the closure of the minimal nonzero nilpotent orbit, not only the orbit. No assertion is made about the scheme structure of the commutator equations, or about all tuples of commuting nilpotent matrices without the entrywise rank bound. The case \(n=3\) is not part of the claimed contribution.

## Proof

**Mutual annihilation.** If \(AB=BA\ne0\) for two of the entries, the common product has rank one and its image is both \(\operatorname{im}A\) and \(\operatorname{im}B\). But \(A^2=0\) forces \(A\) to kill this line, contradicting \(AB\ne0\). Commutation is therefore equivalent to mutual annihilation on this locus.

**Cover by incidence images.** Write \(S=\sum_i\operatorname{im}A_i\), \(K=\bigcap_i\ker A_i\), \(a=\dim S\), and \(b=\operatorname{codim}K\). Then \(S\subseteq K\) and \(a,b\le r\). The dimension parameter \(d\) works precisely when \(a\le d\le n-b\). If \(n\ge2r\) one may take \(d=r\). Otherwise the interval \([a,n-b]\) intersects \([\max(1,n-r),\min(r,n-1)]\): use \(a\le r\), \(n-b\ge n-r\), \(a\le n-b\), \(a\le n-1\), and \(n-b\ge1\). The last two inequalities follow from \(S\subseteq K\) and from the fact that if \(S=0\) then every map is zero. This gives the asserted covers.

**Closedness, irreducibility, and dimension.** Over \(\operatorname{Gr}(d,V)\), take the incidence space with fiber the ordered \(r\)-fold product of rank-at-most-one cones in \(\operatorname{Hom}(V/U,U)\). Each cone is irreducible by the outer-product parameterization. Its nonzero stratum is parameterized by two nonzero factors modulo one scalar, giving dimension \(n-1\). Local Grassmannian trivializations make the incidence space irreducible of dimension \(d(n-d)+r(n-1)\); it is closed in the product of the affine tuple space and the projective Grassmannian. The projection to tuples is closed and has image \(\mathcal X_d\). For each retained index \(r\ge d\), so joint image span \(U\) is a nonempty open condition on the incidence space. On this open locus \(U=S\) is recoverable from the tuple; in particular the projection is generically of fiber dimension zero. This proves the stated dimensions (and closedness and irreducibility for every candidate).

**No omitted lower-dimensional components.** If \(n<2r\), then also \(r\ge n-d\) at each retained index. In a fixed fiber, choose \(r\) nonzero vectors spanning \(U\) and independently \(r\) nonzero functionals spanning \((V/U)^*\), possible by the two inequalities. Taking their entrywise outer products gives \(S=K=U\). Such a tuple is in no \(\mathcal X_e\) with \(e\ne d\). Therefore none of the retained closed irreducible varieties is contained in another, so the cover is the full component list. The interval contains a maximizer of \(d(n-d)\) and at least two indices for \(n\ge4\) and \(n<2r\): for odd \(n\) it contains both middle integers, and for even \(n\) it contains \(n/2\) and its neighbors. This proves the dimension and irreducibility statements.

## Finite-field corollary and checks

For comparison, the zero-allowed finite-field census is a marginal of the broader [double-flag enumeration](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-double-flag-enumeration-of-pairwise-annihilating-square-zero-mat--7465760ed8a5/RESULT.md): restrict the rank vector to \(\{0,1\}^r\) and sum over both flag dimensions. It is not an independent originality claim. In the rank-at-most-one case the marginal has the short expression
\[
 N_{n,r}(q)=\sum_{d=0}^{n}{n\brack d}_q
 \sum_{t=0}^d(-1)^{d-t}q^{\binom{d-t}{2}}{d\brack t}_q
 \left(1+\frac{(q^t-1)(q^{n-d}-1)}{q-1}\right)^r,
\]
where \({a\brack b}_q\) is a Gaussian binomial coefficient. To see this form directly, fix a candidate image span \(U\) of dimension \(d\) and count maps through \(V/U\) with images in a subspace \(W\le U\) of dimension \(t\). There are \(1+(q^t-1)(q^{n-d}-1)/(q-1)\) eligible maps per entry, counting nonzero outer products modulo nonzero scalars and including zero. One Möbius inversion over \(W\le U\) enforces that the images span \(U\); every tuple has exactly one image span. This gives the displayed expression, including the all-zero tuple. The nonzero-entry census in [Higher commuting tuples in the minimal nilpotent matrix orbit](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-higher-commuting-tuples-in-the-minimal-nilpotent-matrix-orbit-ex--821c8ec91c9b/RESULT.md) also overlaps: adjoining zeros corresponds to choosing the nonzero positions and counting on that support.

The accompanying `verify_rank_one.py` checks pair multiplication and this count in finite cases, including \(N_{4,2}(2)=2836\) and \(N_{4,3}(2)=38536\), and checks dimension arithmetic over a finite grid. This does not verify the general component theorem; the incidence and noncontainment arguments above do.

## Relationship to prior work

Ngo, [*Mixed Commuting Varieties over Simple Lie Algebras*](https://arxiv.org/abs/1301.2712), §§4.1 and 4.4, treats the minimal/subregular orbit closure in dimension three, including reducibility and a two-branch description. Levy–Ngo–Šivic, [*Commuting Varieties and Cohomological Complexity Theory*](https://arxiv.org/abs/2105.07918), study unrestricted nilpotent tuples, including related dimension bounds under product-zero conditions. Huang, [*Mutually Annihilating Matrices, and a Cohen–Lenstra Series for the Nodal Singularity*](https://arxiv.org/abs/2110.15566), counts unrestricted annihilating pairs. The higher minimal-orbit result linked above gives dimensions of the nonzero-entry image-span strata and classifies maximal-dimensional components, explicitly not the lower-dimensional components. The classification here uses simultaneous control of the joint image span and the common kernel to prove noncontainment, including for the lower-dimensional components. The comparisons concern mathematical coverage, not a claim of chronological priority or exhaustive literature coverage.
