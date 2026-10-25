# Affine-equivariant Frattini-core homotopy of odd dihedral groups

## Finding

Let \(n\ge 3\) be odd, \(q=\operatorname{rad}(n)=\prod_{p\mid n}p\), and \(k=\omega(n)\). For the order-\(2n\) dihedral group \(D_{2n}=\langle a,s\mid a^n=s^2=1,\;sas=a^{-1}\rangle\), let \(\Phi\) be its Frattini subgroup. Define its non-generating Frattini core
\[
C_n=\{E\subseteq D_{2n}\setminus\Phi:\langle E\rangle\ne D_{2n}\}.
\]
The full automorphism group is \(\mathcal A_n=\operatorname{Aut}(D_{2n})\), with elements \(\varphi_{u,v}(a)=a^u\), \(\varphi_{u,v}(s)=a^v s\), where \(u\in(\mathbb Z/n)^\times\), \(v\in\mathbb Z/n\). There is an \(\mathcal A_n\)-equivariant homotopy equivalence
\[
|C_n|\simeq_{\mathcal A_n}\bigvee_{c\in\mathbb Z/q}S_c^{k-1},
\]
in which the common basepoint is fixed and every \(\varphi_{u,v}\) maps the sphere indexed by \(c\) onto the sphere indexed by \(uc+v\pmod q\) by an orientation-preserving homeomorphism. Here \(\bigvee^q S^0\) means a discrete space of \(q+1\) points with one distinguished fixed point.

Consequently, for **every** subgroup \(H\le\mathcal A_n\), writing
\[
f(H)=|\{c\in\mathbb Z/q:\;uc+v\equiv c\pmod q\ \text{for every }\varphi_{u,v}\in H\}|,
\]
the ordinary fixed locus has homotopy type
\[
|C_n|^H\simeq\bigvee^{f(H)}S^{k-1}.
\]
A wedge of zero spheres of any specified dimension is interpreted as its basepoint. The integral top reduced homology is the untwisted affine permutation module
\[
\widetilde H_{k-1}(|C_n|;\mathbb Z)\cong\mathbb Z[\mathbb Z/q],
\]
and every other reduced integral homology group vanishes. In particular,
\[
\operatorname{tr}(\varphi_{u,v}|\widetilde H_{k-1}(|C_n|;\mathbb Q))=
\begin{cases}d,&d\mid v,\\0,&d\nmid v,\end{cases}
\qquad d=\gcd(u-1,q).
\]
The orbit space under the **full** automorphism group satisfies
\[
|C_n|/\mathcal A_n\simeq S^{k-1}.
\]
This is an equivariant homotopy classification, not merely a nonequivariant sphere count.

## Assumptions and scope

All groups and complexes are finite. Simplicial complexes include the empty face. Geometric realization is topological realization with the indicated simplicial automorphism action. The Frattini subgroup is the intersection of maximal proper subgroups, and \(\Phi=\langle a^q\rangle\) for odd \(n\). The integer \(k\) counts *distinct* prime divisors; no squarefreeness assumption on \(n\) is made. The spherical model is based; an automorphism cannot interchange different prime labels because primes label different subgroup indices. The theorem concerns the core obtained by deleting the Frattini cone vertices, not the unreduced non-generating complex, which is contractible.

## Proof

**1. Explicit maximal subgroups and symmetry.** For odd \(n\), the maximal subgroups are the rotation subgroup \(R=\langle a\rangle\) and, for every prime \(p\mid n\), the \(p\) subgroups
\[
M_{p,t}=\langle a^p,a^t s\rangle\quad(t\in\mathbb Z/p).
\]
Indeed, a subgroup not contained in \(R\) has the form \(\langle a^d,a^t s\rangle\) for some \(d\mid n\); maximality forces \(d=p\) prime. Their intersection is \(\Phi=\langle a^q\rangle\). Every group automorphism fixes \(R\) and sends \(M_{p,t}\) to \(M_{p,ut+v}\), reducing the parameters modulo \(p\). The standard dihedral automorphism description is valid since \(n\) is odd.

**2. An equivariant nerve.** The maximal-subgroup simplices \(2^{M\setminus\Phi}\) cover \(C_n\). A nonempty finite intersection of these covering simplices is itself a simplex, and every setwise stabilizer fixes its barycenter. The equivariant nerve lemma therefore identifies \(|C_n|\), up to \(\mathcal A_n\)-homotopy, with the nerve \(K\) whose faces correspond to intersections containing some element outside \(\Phi\). Equivariance follows from the canonical permutation of the maximal-subgroup cover, not from an arbitrary choice of contracting homotopies.

**3. Exact nerve face criterion.** Introduce the vertex \(R\) and a block \(B_p=\{M_{p,t}:t\in\mathbb Z/p\}\) for each distinct \(p\mid n\). A set of selected maximal subgroups is a face of \(K\) precisely under either of the following conditions:

(i) it omits at least one whole prime block \(B_p\); or

(ii) it contains no \(R\) and selects exactly one vertex from **every** prime block.

For (i), if \(d\) is the product of primes of all blocks met, then \(d\mid q\), \(d<q\), and \(a^d\) lies in the intersection but not in \(\Phi\). If all prime blocks are met and \(R\) is selected, the intersection of rotation subgroups is exactly \(\Phi\). If all blocks are met without \(R\), a reflection can lie in the intersection only if its exponent has the same residue modulo \(p\) as each selected \(t\); this forbids two distinct selections from any one block. Conversely, exactly one selection per block yields a reflection by the Chinese remainder theorem. The resulting \(q\) full simplices are canonically indexed by \(c\in\mathbb Z/q\), by selecting \(M_{p,c\bmod p}\) for every \(p\mid n\).

**4. Equivariant contraction.** Let \(B\) be the simplicial complex on all prime-block vertices consisting of subsets missing at least one whole block. Then the subcomplex \(A=\{R\}*B\) is a cone with an \(\mathcal A_n\)-fixed apex. The criterion above describes \(K\) as \(A\) with the \(q\) full \((k-1)\)-simplices \(\sigma_c\) attached along their complete boundaries; those boundaries already lie in \(A\). Because \(|A|\) contracts equivariantly onto its fixed apex and its inclusion in the finite simplicial \(\mathcal A_n\)-complex \(|K|\) is an equivariant cofibration, the quotient \(|K|\to |K|/|A|\) is an \(\mathcal A_n\)-homotopy equivalence. The quotient is *literally* a wedge of the \(q\) spheres \(\sigma_c/\partial\sigma_c\). For \(k=1\), the boundary is empty: the nerve is a fixed isolated apex plus \(q\) points, giving the same based zero-sphere convention.

Fix an increasing order of prime labels. Every automorphism preserves each block \(B_p\), acts by \(c\mapsto uc+v\), and never permutes the prime positions of an ordered simplex \(\sigma_c\). Hence all sphere-map degrees are \(+1\). This proves the asserted equivariant homotopy type.

**5. Fixed loci, characters and quotient.** Equivariant homotopy equivalences restrict to homotopy equivalences on every subgroup's fixed sets. On the wedge model, a point outside the common basepoint is \(H\)-fixed exactly when its sphere index is fixed by every element of \(H\). Thus the fixed-set formula follows. The sphere orientations give the stated integral permutation module, including the reduced degree-zero group when \(k=1\). The congruence \((u-1)c\equiv-v\pmod q\) has exactly \(d=\gcd(u-1,q)\) solutions if \(d\mid v\), otherwise none. Translations act transitively on \(\mathbb Z/q\), so quotienting the wedge by the full affine action identifies all spheres by degree-one identifications and gives exactly one \(S^{k-1}\).

## Verification

A standalone standard-library script (`verify_dihedral.py`) independently enumerates all maximal-subgroup intersections, checks the face criterion and reduced Euler characteristic for \(n=3,5,9,15,21,45,105\), and computes the signed simplicial Lefschetz trace of all affine automorphisms for \(n\le21\) plus selected automorphisms for \(n=45,105\). The checked counts of maximal-subgroup nerve faces are respectively \(4,6,4,92,290,92,10522\), with reduced Euler characteristics respectively \(3,5,3,-15,-21,-15,105\). The trace tests match the predicted fixed-residue counts. This finite computation is a consistency check, not a substitute for the general equivariant proof.

## Relationship to prior work

Dupont García, arXiv:2610.10296v1, Proposition 3.2, supplies the general Frattini-core/coatom-nerve reduction and its naturality under automorphisms. That result is an essential premise here, **not claimed as new**. Its explicit equivariant homology calculations are for finite \(p\)-groups, not for the family of odd dihedral groups with unrestricted odd \(n\). Woodroofe, arXiv:0708.3539v3, Theorem 1.4 ascribed to Thévenaz, states that proper subgroup lattices of solvable groups have a wedge-of-spheres homotopy type, with summands indexed by complement chains; thus the ordinary wedge property is already covered and is not the claimed contribution. Kramarev–Lokutsievskiy, arXiv:0911.4136, studies group-lattice homotopy for other groups. The new assertion is the **explicit full-automorphism equivariant decomposition**, including all fixed-subgroup homotopy types and the integral affine character, obtained from a concrete invariant nerve decomposition. Welker's work on equivariant subgroup-lattice topology may supply more general equivariant tools and is a significant comparison risk; no assertion of its noncoverage is made without full-text inspection.

## Limitations

The classification requires \(n\ge3\) odd. Nothing is asserted about even dihedral groups, other families of solvable groups, or the full non-generating complex before deletion of the Frattini cone. The nerve-reduction theorem and general solvable-lattice wedge theorem are established prior results. The claim is not an exhaustive literature-uniqueness certificate. The complete 1985 Thévenaz and 1995 Welker papers were not materially inspected; possible prior equivalent equivariant statements in those sources remain unresolved originality risks. The finite tests do not certify infinite-family assertions, which follow from the displayed proof.

## References

1. L. A. Dupont García, *Frattini Geometry of Non-Generating Complexes: Symmetry, Homology and Betti Numbers*, arXiv:2610.10296v1 (first public 2026-10-07), https://arxiv.org/html/2610.10296v1.
2. R. Woodroofe, *An EL-labeling of the subgroup lattice*, arXiv:0708.3539v3, https://arxiv.org/html/0708.3539v3.
3. I. P. Kramarev and L. V. Lokutsievskiy, *Homotopy types of group lattices*, arXiv:0911.4136v1, https://arxiv.org/abs/0911.4136.
4. J. Thévenaz, *The top homology of the lattice of subgroups of a soluble group*, Discrete Mathematics 55 (1985), 291–303, https://doi.org/10.1016/S0012-365X(85)80005-4.
5. V. Welker, *Equivariant homotopy of posets and some applications to subgroup lattices*, Journal of Combinatorial Theory, Series A 69 (1995), 61–86, https://doi.org/10.1016/0097-3165(95)90107-8.
