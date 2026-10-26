# Three Belyi loci among six-\(I_2\) rational elliptic surfaces

## Finding
Let \(f:S\to\mathbb P^1_{\mathbb C}\) be a relatively minimal rational elliptic surface with a chosen zero section and precisely six singular fibres, all of Kodaira type \(I_2\). Consider isomorphisms preserving the elliptic fibration and its zero section, while permitting automorphisms of the base. The \(j\)-invariant map \(j_f:\mathbb P^1\to\mathbb P^1\) is a Belyi map (branched only over \(0,1728,\infty\)) for exactly **three** such isomorphism classes.

Write \(\eta_+=(1+\sqrt{-3})/2\) and \(\eta_-=(1-\sqrt{-3})/2\). For \((u,v)\) in the following three-row table, let \(S_{u,v}\) be the minimal regular model of
\[
y^2=x\bigl(x-(t^2+1)\bigr)\bigl(x-(u t^2+v)\bigr).
\]
These representatives and the complete ramification partitions of their degree-twelve \(j\)-maps are:

| Class | \((u,v)\) | Over \(0\) | Over \(1728\) | Over \(\infty\) |
|---|---|---|---|---|
| equianharmonic/equianharmonic | \((\eta_+,\eta_-)\) | \((6,6)\) | \((2,2,2,2,2,2)\) | \((2,2,2,2,2,2)\) |
| harmonic/harmonic | \((-1,2)\) | \((3,3,3,3)\) | \((4,4,2,2)\) | \((2,2,2,2,2,2)\) |
| harmonic/equianharmonic | \((-1,\eta_+)\) | \((6,3,3)\) | \((4,2,2,2,2)\) | \((2,2,2,2,2,2)\) |

The three passports distinguish the isomorphism classes. No assertion is made about isomorphisms of the abstract surfaces after forgetting their elliptic fibrations.

## Assumptions and scope
All schemes and maps are over \(\mathbb C\). A Belyi \(j\)-map means that every ramification point of the rational function \(j_f\) maps to \(0\), \(1728\), or \(\infty\); the normalization \(j/1728\) gives the usual branch values \(0,1,\infty\). The singular-fibre condition is exactly six distinct geometric base points carrying reduced multiplicative Kodaira fibres of type \(I_2\), and no other singular fibres. Isomorphism means a zero-section-preserving isomorphism of fibrations after an automorphism of the base.

## Proof
**1. The degree-two Legendre parameter.** The Weierstrass normal form for this fibre configuration, established in the cited classification, has three globally split two-torsion roots with pairwise differences binary quadratics whose zero loci consist of six disjoint simple points. Translate the cubic root and, using homogeneous coordinates on the base, write its generic fibre as \(y^2=x(x-D)(x-N)\), where \(D,N,D-N\) are binary quadratics, each with two distinct zeros and no common zero. Set \(\lambda=N/D\). Because \(D\) and \(N\) are coprime quadratics, \(\lambda\) is a degree-two map. The six singular fibres are exactly its simple inverse images of \(0,1,\infty\), hence \(\lambda\) is unramified over these three points.

Conversely, any degree-two \(\lambda\) unramified over \(0,1,\infty\) can be expressed as \(N/D\) for coprime binary quadratics, with the three reduced preimage divisors of degree two. Its associated split Weierstrass equation has exactly six \(I_2\) fibres: locally at a simple zero of one difference, two Weierstrass roots meet transversely, the Weierstrass model has an ordinary double point, and its minimal desingularization has multiplicative type \(I_2\). No additional fibres occur, including at infinity, since all three binary quadratic zero divisors have precisely two distinct points. The discriminant is a nonzero scalar multiple of \(D^2N^2(D-N)^2\), of degree twelve. The resulting elliptic surface has \(\chi(\mathcal O_S)=1\) and a section, so is rational by the standard elliptic-surface classification.

**2. Branch locus of the universal \(j\)-function.** Directly from Legendre's formula,
\[
 j_f=J\circ\lambda,\qquad J(z)=256\frac{(z^2-z+1)^3}{z^2(z-1)^2}.
\]
The degree-six map \(J\) has ramification index three at the two roots \(\eta_\pm\) of \(z^2-z+1\), index two at \(-1,1/2,2\) (the roots of \(J(z)-1728\)), and index two at \(0,1,\infty\) (poles). By the chain rule for local ramification indices, a ramification point of \(\lambda\) is allowed for the Belyi condition precisely when its image lies over one of these three \(J\)-branch values. The two distinct branch values of a quadratic rational map cannot be \(0,1,\infty\) by Step 1. Thus the necessary and sufficient condition is
\[
 \operatorname{Br}(\lambda)\subseteq\{\eta_+,\eta_-,-1,1/2,2\}.
\]
Because every degree-two cover \(\mathbb P^1\to\mathbb P^1\) has two distinct simple branch values, this means an unordered pair of distinct elements of the displayed five-point set.

**3. Classification modulo fibre-label permutations.** A degree-two cover of \(\mathbb P^1\) with any specified two distinct target branch values is unique up to automorphism of its source: send its branch points and branch values to \(0,\infty\) and reduce to \(t\mapsto t^2\). Permuting the three nonzero two-torsion points induces on \(\lambda\) the anharmonic group \(S_3=\langle z\mapsto1-z, z\mapsto1/z\rangle\). It preserves the pair \(\{\eta_+,\eta_-\}\), permutes the triple \(\{-1,1/2,2\}\), and acts transitively on the unordered pairs of each of the three kinds: two equianharmonic points, two harmonic points, or one of each. Therefore the ten admissible unordered branch pairs fall into exactly three orbits. These orbits classify zero-section-preserving elliptic fibrations: for a fixed \(\lambda\), any other elliptic curve with the same \(j\) is a quadratic twist, but a nonconstant twist over \(\mathbb C(t)\) has a branch point and changes a smooth or an \(I_2\) fibre to additive type. Since the prescribed fibre types exclude additive fibres, only an unramified quadratic twist is permitted. Such a twist is trivial over \(\mathbb P^1_{\mathbb C}\). Constant twists are also trivial over \(\mathbb C\). Hence the three parameter orbits are precisely the three isomorphism classes in the claim.

**4. Models and passports.** Given a branch pair \(\{u,v\}\), take \(D=t^2+1\) and \(N=u t^2+v\). Then \(\lambda=N/D\) has critical points \(0,\infty\) and critical values \(v,u\). Because none of the selected values is \(0\), \(1\), or \(\infty\), the three divisors of \(D\), \(N\), and \(D-N\) are reduced and disjoint. The numerator of \(j\) is a scalar times \((D^2-DN+N^2)^3\); its denominator is \(D^2N^2(D-N)^2\). The identity
\[
 256(D^2-DN+N^2)^3-1728D^2N^2(D-N)^2
 =64(D+N)^2(2D-N)^2(D-2N)^2
\]
gives the complete ramification partitions listed above by tracking whether either ramification value \(u,v\) of \(\lambda\) is equianharmonic or harmonic. Multiplying local indices gives the partitions; in all cases the Riemann–Hurwitz sum is \(22=2\cdot12-2\). Their distinct partitions prove pairwise nonisomorphism.

## Verification
The accompanying standalone `verify_belyi.py` uses exact arithmetic in \(\mathbb Q(\sqrt{-3})\). It computes the divisors of the rational functions \(j\), \(j-1728\), and \(1/j\) on \(\mathbb P^1\), including infinity, checks pairwise coprimality of the three quadratic factors and the stated identity, compares all three passports, and checks Riemann–Hurwitz. Running `python verify_belyi.py` outputs `VERIFY_OK`. The proof of completeness uses the argument above, not numerical experiments.

## Relationship to prior work
Ciliberto, Grassi, Miranda, Verra, and Zanardini (2026), Section 2.4, classify and parameterize the two-dimensional family of rational elliptic surfaces with precisely six \(I_2\) fibres using three quadratic Weierstrass roots. That published general normal form is the starting point here; the finite Belyi \(j\)-map locus, its three equivalence classes, explicit representatives, and ramification passports are the present distinct claims. Beukers and Montanus (2008) compute degree-24 Belyi \(J\)-maps for semistable elliptic K3 surfaces with six singular fibres; their fibre Euler number and maps differ from the degree-12 rational surfaces here. The degree-12 Jacobian-surfaces statement is not implied merely by the standard fibre-configuration lists.

## Limitations
The theorem concerns only fibration isomorphisms with a zero section over \(\mathbb C\), not all abstract surface isomorphisms or arithmetic models. Search-based literature comparison cannot exclude an equivalent result in an unindexed source. The Beukers–Montanus chapter was compared on its accessible abstract/introduction, not independently read in full; an implicit relevant construction there or in older dessins literature remains a residual priority risk. Independent mathematical audit has not been performed.

## References
1. C. Ciliberto, A. Grassi, R. Miranda, A. Verra, and A. Zanardini, *Rational elliptic surfaces with six singular double fibres*, arXiv:2602.11725v1 (first public version, 2026-02-12), Section 2.4. https://arxiv.org/html/2602.11725v1
2. F. Beukers and H. Montanus, *Explicit calculation of elliptic fibrations of K3-surfaces and their Belyi-maps*, in *Number Theory and Polynomials* (2008), pp. 33–51, DOI:10.1017/CBO9780511721274.005.
3. R. Vidunas and Y.-H. He, *Composite genus one Belyi maps*, *Indagationes Mathematicae* 29 (2018), 916–947. https://openaccess.city.ac.uk/id/eprint/20365/
