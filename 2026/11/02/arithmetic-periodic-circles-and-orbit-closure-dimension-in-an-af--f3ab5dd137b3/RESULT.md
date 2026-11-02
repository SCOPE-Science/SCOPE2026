# Arithmetic periodic circles and orbit-closure dimension in an affine torus map

## Finding

Let \(\mathbb T=\mathbb R/\mathbb Z\) and consider, for arbitrary real translation parameters \(e,f\), the continuous degree-four torus map
\[
F_{e,f}(x,y)=(3x+2y+e,\;x+2y+f)\pmod 1
\qquad ((x,y)\in\mathbb T^2).
\]
Put \(\delta=e-2f\pmod1\). The following complete arithmetic dichotomy holds.

**Irrational case.** If \(\delta\notin\mathbb Q/\mathbb Z\), the map has no periodic points of any period. Haar probability is ergodic, but not weakly mixing, and Haar-almost every forward orbit is dense in the entire torus.

**Rational case.** If \(\delta=p/q\pmod1\), with \(p,q\) coprime and \(q\ge1\), there are no periodic points of least period not divisible by \(q\). For every \(k\ge1\), the points of **least period exactly** \(qk\) form precisely
\[
B_{q,k}=\frac13\sum_{d\mid k}\mu(k/d)\bigl(4^{qd}-1\bigr)
\]
pairwise disjoint, embedded, essential circles, all of primitive homology class \((1,-1)\) (up to orientation) in the original \((x,y)\) torus. Each circle consists entirely of points with that same least period, and its return derivative has tangent multiplier \(1\) and transverse multiplier \(4^{qk}\). Haar-almost every forward orbit is dense in exactly the union of \(q\) parallel circles \(x-2y=u+jp/q\pmod1\), \(0\le j<q\), where \(u=x_0-2y_0\). Its orbit closure therefore has Hausdorff dimension \(1\); for irrational \(\delta\) the typical orbit closure has dimension \(2\).

Haar probability is ergodic exactly for irrational \(\delta\). Its \(L^2\) Koopman eigenvalues for any \(\delta\) are exactly \(\{e^{2\pi i m\delta}:m\in\mathbb Z\}\); there are no eigenfunctions depending nontrivially on the expanding fiber coordinate. In the rational case the invariant sigma-field is generated (modulo null sets) by \(qx-2qy\pmod1\), giving the precise Haar ergodic decomposition. Haar is never weakly mixing for any translation.

For the explicitly published choice \((e,f)=(1/10,1/5)\), \(\delta=-3/10\), so the first possible period is \(10\), with exactly \((4^{10}-1)/3=349525\) distinct primitive-period-ten circles. Haar-typical orbit closures are ten parallel circles, notwithstanding the strictly expanding transverse direction.

## Assumptions and scope

All arithmetic is on the **continuous torus** \(\mathbb T^2\), not on a finite-precision digitization of the unit square. Both matrix coefficients are integers, so coordinatewise fractional-part representatives define one unambiguous continuous torus map. The result concerns the integer-matrix example (10) of Wang and Ding and its full translation-parameter family; it makes no assertion about their noninteger-matrix example (11), which does not define the same continuous torus endomorphism. Haar-typical statements mean with respect to two-dimensional normalized Lebesgue measure; they do not assert that every starting point has a dense orbit. The Möbius function \(\mu\) is the ordinary number-theoretic Möbius function.

## Proof

**Integral torus conjugacy.** The integer unimodular coordinate change \((u,v)=(x-2y,y)\) has inverse \((x,y)=(u+2v,v)\). Direct substitution gives the torus skew product
\[
S_{\delta,f}(u,v)=(u+\delta,\;4v+u+f)\pmod1.
\]
The difference \(e-2f\) is a torus-invariant rotation parameter. Put \(L_n=4^n-1\), \(H_n=L_n/3\), and \(W_n=(4^n-1-3n)/9\), which are integers for \(n\ge1\). Summing the affine recurrence, or inducting, yields
\[
S_{\delta,f}^{n}(u,v)
=\bigl(u+n\delta,\;4^n v+H_n(u+f)+W_n\delta\bigr)\pmod1.
\]
The first coordinate can return precisely when \(n\delta=0\pmod1\). For irrational \(\delta\), this never happens. For rational \(p/q\), it happens exactly when \(q\mid n\).

**Fixed circles and their topology.** When \(q\mid n\), the fixed-point condition is the single character congruence
\[
H_n u+L_n v+H_nf+W_n\delta=0\pmod1.
\]
For each fixed \(u\) there are exactly \(L_n\) distinct \(v\)'s. Label these by \(j\pmod{L_n}\). As \(u\) winds once around its circle, the branch labels undergo the cyclic translation \(j\mapsto j-H_n\pmod{L_n}\). Since \(\gcd(L_n,H_n)=H_n\), there are exactly \(H_n\) connected components, each of which projects with degree \(3\) onto the \(u\)-circle. Its tangent lifts as \((\Delta u,\Delta v)=(3,-1)\); the inverse coordinate change sends this to \((\Delta x,\Delta y)=(1,-1)\). Thus all fixed components are embedded circles of the asserted homology class.

For two admissible periods, each component has the **same** connected kernel direction, hence a smaller-period fixed circle is an entire component of every applicable larger-period fixed set, never a proper arc. Write \(A(k)=(4^{qk}-1)/3\) for the number of components fixed by the iterate \(qk\), and \(B_{q,k}\) for the number of components whose points have least period \(qk\). Then \(A(k)=\sum_{d\mid k}B_{q,d}\). Möbius inversion gives precisely the formula in the Finding. No finite numerical search is used to infer completeness. The constant derivative in \((u,v)\) coordinates is \(\left(\begin{smallmatrix}1&0\\1&4\end{smallmatrix}\right)\); the eigenvalues of its \(n\)-th power are \(1\) and \(4^n\). The neutral eigenline agrees with the circle tangent, proving normal expansion and the multipliers.

**Invariant measure and spectrum.** The base rotation preserves Haar probability in \(u\), and for each fixed \(u\), the fourfold circle covering \(v\mapsto4v+u+f\) sends Haar probability in \(v\) to Haar. Product Haar probability is therefore invariant. For the Fourier characters \(\chi_{a,b}(u,v)=e^{2\pi i(au+bv)}\), the Koopman operator \(U\) satisfies
\[
U\chi_{a,b}=e^{2\pi i(a\delta+bf)}\chi_{a+b,4b}.
\]
If \(Uh=\lambda h\) for a nonzero \(L^2\) function and \(|\lambda|=1\), then \(h=\lambda^{-n}U^nh\) for every \(n\). Every Fourier frequency in the \(v\)-coordinate occurring in \(U^n h\) is divisible by \(4^n\). Consequently all nonzero \(v\)-frequencies of \(h\) vanish, so \(h=h(u)\). The remaining eigenvalue equation is \(h(u+\delta)=\lambda h(u)\), whose Fourier solutions have exactly the eigenvalues \(e^{2\pi i m\delta}\). In particular, \(\lambda=1\) has only constants for irrational \(\delta\), proving Haar ergodicity, and for rational \(p/q\) has precisely functions of \(qu\), proving the claimed invariant sigma-field. The nonconstant character \(e^{2\pi i u}\) is always a unit-modulus eigenfunction; hence Haar is never weakly mixing.

**Typical orbit closures.** Irrational \(\delta\) makes Haar ergodic with full support. Apply the pointwise ergodic theorem to a countable collection of open sets forming a basis: almost every orbit visits every nonempty open set, and its closure is the whole torus. For rational \(p/q\), the \(q\) values of the base coordinate form a finite cycle. On each base fiber, the \(q\)-return acts as \(v\mapsto4^qv+c(u)\pmod1\), conjugate by a circle translation to the \(4^q\)-fold map. Almost every fiber initial point has dense return orbit. Combining the \(q\) base fibers gives exactly the \(q\) circles stated in the Finding, with one-dimensional orbit closure. This also supplies an explicit conditional-ergodic decomposition of Haar over the invariant \(qu\)-coordinate.

## Verification

The accompanying `verify_affine_torus.py` performs exact rational arithmetic for six translation pairs with rational rotation orders \(1,2,3,7,10\). For admissible periods it constructs sampled points from the character congruence, checks their entire returns under the *original* coordinate map, verifies the rotation-coordinate invariant and exclusion of shorter periods in the first admissible period, and checks integer divisibilities and component counts. These are finite consistency tests only. All infinite statements, including the component census, orbit-closure dichotomy and Fourier spectrum, are proved above without reliance on sampling.

## Relationship to prior work

Wang and Ding, *A New Two-Dimensional Map with Hidden Attractors* (2018), introduced the integer-matrix map as their equation (10), with \((e,f)=(1/10,1/5)\), and studied the existence of fixed points, Lyapunov exponents, phase plots, implementation and approximate entropy. Their displayed eigenvalue \(1\) is consistent with the neutral direction used here; their stated fixed-point and Lyapunov information does **not by itself** determine the full periodic-point topology, arbitrary-translation rationality transition, Koopman eigenfunctions or Haar-typical orbit closures established here. The complete open-access article text was read in its PMC HTML representation, including the model definition, eigenvalue analysis, dynamical plots, digitization, complexity analysis and conclusion.

Baake, Neumärker and Roberts (2013) investigate periodic orbit structure on invariant **rational lattices** of integer toral matrices; that discrete-lattice scope does not provide this continuous family of essential fixed circles, the translation-dependent irrational no-periodic-points regime, or the Haar spectral classification. Adler, Tresser and Worfolk (1997) study topological conjugacy of linear toral endomorphisms, a general background framework rather than a checked statement of the arithmetic component formula for this affine example. Llibre and Neumärker (2015) classify **period sets** for linear toral endomorphisms. Their period-set classification does not supply the counts of connected primitive-period circles in the affine translated family, the dependence on \(e-2f\), the Koopman point spectrum, or the typical orbit-closure dimension. Standard rotation and expanding-map facts are openly used as proof ingredients and are not represented as newly discovered theory. The specific formulas and combined classification were not found in the inspected sources; an equivalent statement in unindexed or incompletely accessible literature remains possible.

## Limitations

The finding is about the exact mathematical torus map and Haar-typical orbit behavior, not finite-state implementations or cryptographic randomness. Positive transverse expansion does not make the system Haar-mixing. The circle-component numbers count connected sets, not geometrically isolated points or orbits. The formula does not claim novelty for generic facts about circle rotations, covering maps, or Möbius inversion. Publication-priority uncertainty remains because not every relevant full text could be retrieved. No independent mathematical audit has been performed.

## References

1. C. Wang and Q. Ding, “A New Two-Dimensional Map with Hidden Attractors,” *Entropy* **20** (2018), article 322, published 2018-04-27, DOI: 10.3390/e20050322, https://doi.org/10.3390/e20050322; open indexed text at https://pmc.ncbi.nlm.nih.gov/articles/PMC7845775/ .
2. M. Baake, N. Neumärker and J. A. G. Roberts, “Orbit structure and (reversing) symmetries of toral endomorphisms on rational lattices,” *Discrete and Continuous Dynamical Systems* **33** (2013), 527–553, https://doi.org/10.3934/dcds.2013.33.527 .
3. R. Adler, C. Tresser and P. A. Worfolk, “Topological conjugacy of linear endomorphisms of the 2-torus,” *Transactions of the AMS* **349** (1997), 1633–1652, DOI: 10.1090/S0002-9947-97-01895-3.
4. M. Lemańczyk and C. Mauduit, “Ergodicity of a Class of Cocycles Over Irrational Rotations,” *Journal of the London Mathematical Society* **49** (1994), 124–132, https://doi.org/10.1112/jlms/49.1.124 (related skew-product ergodicity in a different fiber regime).
5. J. Llibre and N. Neumärker, “Period sets of linear toral endomorphisms on \(\mathbb T^2\),” *Topology and its Applications* **185–186** (2015), 41–49, DOI: 10.1016/j.topol.2015.02.003 (period-set classification for unshifted linear endomorphisms).
