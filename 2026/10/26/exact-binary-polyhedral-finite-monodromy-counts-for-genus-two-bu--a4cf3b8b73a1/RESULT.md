# Exact binary polyhedral finite-monodromy counts for genus-two bundles

## Finding
Let \(C\) be an arbitrary smooth connected projective complex curve of genus \(2\). In the moduli space of stable rank-\(2\) bundles \(E\) satisfying \(\det E\simeq\mathcal O_C\), define the \(2O\)-stratum, respectively the \(2I\)-stratum, by requiring the image of the associated Narasimhan–Seshadri representation \(\rho_E:\pi_1(C)\to\mathrm{SU}(2)\) to be conjugate to the binary octahedral group \(2O\), respectively the binary icosahedral group \(2I\). Then these strata have exactly
\[
\#\mathcal M_{2O}(C)=8{,}640,\qquad \#\mathcal M_{2I}(C)=46{,}080.
\]
The counts are independent of the complex structure of \(C\). The image condition concerns the actual subgroup of \(\mathrm{SU}(2)\), not just its projection to \(\mathrm{SO}(3)\).

## Assumptions and scope
The base field is \(\mathbb C\), the genus is exactly \(2\), the bundles have rank \(2\), degree \(0\), and holomorphically trivial determinant, and stability means slope stability. Two bundles are identified when isomorphic; a determinant trivialization is not part of the object. The finite subgroups \(2O\) and \(2I\) are the full inverse images in \(\mathrm{SU}(2)\to\mathrm{SO}(3)\) of the rotational octahedral group \(S_4\) and icosahedral group \(A_5\), of orders \(48\) and \(120\). They act irreducibly on \(\mathbb C^2\). No assertion is made about arbitrary finite-image or merely projectively finite-image bundles.

## Proof
**Step 1 (the moduli quotient).** By Narasimhan–Seshadri, stable rank-\(2\) degree-zero bundles with trivial determinant are equivalent to irreducible conjugacy classes of representations into \(\mathrm{SU}(2)\). Fix an embedded copy \(G\) of either binary polyhedral group. Every representation whose image is conjugate to \(G\) has a representative surjecting onto this fixed copy. Two such epimorphisms become conjugate in \(\mathrm{SU}(2)\) precisely when related by conjugation in the normalizer \(N_{\mathrm{SU}(2)}(G)\). The octahedral rotation group is its own normalizer in \(\mathrm{SO}(3)\): its three fourfold-rotation axes are permuted by any normalizing rotation, and the oriented signed permutations of these axes are exactly the octahedral rotation group. The icosahedral rotation group is likewise self-normalizing: any normalizer is a finite rotation subgroup containing \(A_5\), which is maximal among finite rotation subgroups. Therefore \(N_{\mathrm{SU}(2)}(G)=G\) in both cases. The centralizer of a surjective image is the center \(\{\pm I\}\), so each conjugation orbit of epimorphisms has size \(|G|/2\). Both embedded representations are irreducible because these groups are nonabelian and not contained in a maximal torus. Thus it remains to determine \(\#\operatorname{Epi}(\pi_1(C),G)\).

**Step 2 (exact surface-group count).** Present
\[
\pi_1(C)=\langle a,b,c,d\mid [a,b][c,d]=1\rangle,
\quad [x,y]=xyx^{-1}y^{-1}.
\]
For every subgroup \(H\le G\), let \(q_H(t)=\#\{(x,y)\in H^2:[x,y]=t\}\). The number of homomorphisms with image contained in \(H\) is then exactly
\[
F(H)=\sum_{t\in H}q_H(t)q_H(t^{-1}).
\]
Let \(E(H)\) count epimorphisms onto \(H\). Partition all homomorphisms by their unique image, to obtain the *finite exact recursion*
\[
E(H)=F(H)-\sum_{K<H}E(K).
\]
Enumerate all subgroups by adjoining a new group element to each subgroup until the generated subgroup closes; every subgroup is reached because each has finitely many generators. In the binary octahedral model this gives exactly \(35\) subgroups, and in \(\mathrm{SL}_2(\mathbb F_5)\cong2I\) exactly \(76\).

**Step 3 (reproducible arithmetic).** The accompanying independent-execution script implements the actual multiplication for \(2O\) using exact quaternions with coordinates in \(\frac12\mathbb Z[\sqrt2]\); for \(2I\), it uses all determinant-one \(2\times2\) matrices over \(\mathbb F_5\). It computes every commutator by exact multiplication and inverses and applies the recursion of Step 2 over the entire subgroup lattice. It outputs
\[
\begin{array}{c|rrrr}
G&|G|&\#\{H\le G\}&F(G)&E(G)\\\hline
2O&48&35&335{,}616&207{,}360\\
2I&120&76&3{,}309{,}120&2{,}764{,}800
\end{array}.
\]
As a separate arithmetic consistency check, the known irreducible-character degree multisets are \((1,1,2,2,2,3,3,4)\) for \(2O\) and \((1,2,2,3,3,4,4,5,6)\) for \(2I\). The Frobenius–Mednykh genus-two formula \(F(G)=|G|^3\sum_{\chi\in\operatorname{Irr}(G)}\chi(1)^{-2}\) independently reproduces both values of \(F(G)\).

For an additional independently inspectable subgroup-poset certificate, define \(\mu(H,G)\) by \(\mu(G,G)=1\) and \(\mu(H,G)=-\sum_{H<K\le G}\mu(K,G)\). The script calculates \(\sum_{|H|=r}\mu(H,G)F(H)\) by subgroup order. For \(2O\), the nonzero contributions at orders \(2,4,6,8,12,16,24,48\) are respectively \(-192,3072,5184,6528,-31104,-58368,-53376,335616\), totaling \(207360\). For \(2I\), the nonzero contributions at orders \(2,4,6,12,20,24,120\) are respectively \(-960,15360,25920,-77760,-240000,-266880,3309120\), totaling \(2764800\). The recursion and Möbius computations use different summation orders and agree.

**Step 4 (divide by actual conjugation).** Since each epimorphism orbit has size \(24\) for \(2O\) and \(60\) for \(2I\), respectively, the number of stable-bundle classes equals
\[
207360/24=8640,\qquad 2764800/60=46080.
\]
The argument uses only the fixed topological surface group, and so applies to every complex structure of genus \(2\). \(\square\)

## Verification
Run `python3 verify_finite_monodromy.py` with Python 3 and no external dependencies. It asserts the two centers, the exact subgroup and epimorphism counts, the complete subgroup-poset Möbius identity, and the independent character-degree check of the unrestricted homomorphism counts. The final output contains `VERIFY_OK`. No probabilistic tests, sampling, or floating-point computations enter the census. The program checks finite groups exhaustively; the deduction for all complex curves is supplied by Steps 1 and 4, not inferred from finite sampling.

## Relationship to prior work
McPherson, arXiv:2610.22573v1, studies symmetric tensors on ruled surfaces \(\mathbb P_C(E)\) and records the relevance of stable symmetric powers, with remaining challenging exceptional cases. Kim, arXiv:2006.11733v3, proves finiteness of exceptional stable bundles under the relevant stability hypothesis, without providing these exact two finite-monodromy counts. The general Frobenius–Mednykh count of surface-group homomorphisms is classical and is discussed by Klug, arXiv:2106.11089v2. This result combines those existing frameworks with a complete explicit epimorphism/subgroup calculation and the exact unitary conjugacy quotient. It does **not** assert a new general counting formula or identify the two strata with every exceptional symmetric-power case.

## Limitations
The result fixes genus \(2\), trivial determinant, and actual monodromy groups \(2O\) and \(2I\). It neither classifies all finite-monodromy bundles nor computes the full algebras of symmetric tensors. The abstract finite-group census and normalizer argument are complete; historical priority remains subject to unlocated equivalent group-specific enumerations. 

## References
- L. McPherson, *Computing S(X) for Ruled Surfaces Defined by Stable Bundles on Curves of Genus 2*, arXiv:2610.22573v1 (15 October 2026), https://arxiv.org/html/2610.22573v1 .
- J.-S. Kim, *Stability of symmetric powers of vector bundles of rank two with even degree on a curve*, arXiv:2006.11733v3, https://arxiv.org/abs/2006.11733 .
- M. R. Klug, *Counting homomorphisms from surface groups to finite groups*, arXiv:2106.11089v2, https://arxiv.org/abs/2106.11089 .
- M. S. Narasimhan and C. S. Seshadri, *Stable and unitary vector bundles on a compact Riemann surface*, Annals of Mathematics **82** (1965), 540–567.
