# Weak log del Pezzo and anticanonical classification of Schubert surfaces of matrix pencils

## Finding
Let \(L\subseteq\operatorname{Hom}(V,W)\) be a two-dimensional complex matrix pencil, and let \(Y_L\) be the closure of its graph chart in \(\operatorname{Gr}(\dim V,V\oplus W)\). For every distinct eigenvalue in the regular Kronecker summand, let \(k_{i1}<\dots<k_{ih_i}\) denote the distinct sizes of its Jordan blocks. Put
\[
\kappa=\sum_{i=1}^{s}k_{i h_i},
\]
with empty sum zero. Here *regular pencil* means a general member is an invertible square matrix; otherwise the pencil is *singular*.

**Theorem.** Every \(Y_L\) is a normal projective klt surface. In the regular case, necessarily \(\kappa\ge 2\), and
\[
-K_{Y_L}\text{ is nef and big},\qquad (-K_{Y_L})^2=\frac{4\kappa}{\kappa-1}.
\]
It is ample if and only if \(h_i=1\) for every eigenvalue. In the singular case,
\[
(-K_{Y_L})^2=9-\kappa,
\]
and \(-K_{Y_L}\) is nef and big if and only if \(\kappa\le3\), whereas it is ample if and only if \(\kappa\le2\) and all \(h_i=1\).

Whenever \(-K_{Y_L}\) is nef and big, its sufficiently divisible complete linear systems define a birational anticanonical contraction. Its exceptional curves are exactly the images of the surviving exceptional curves attached to sizes \(k_{ij}\) with \(j<h_i\), and, only when the pencil is singular with \(\kappa=3\), the image \(C_\infty\) of the line at infinity. In particular, the regular-pencils stratum is entirely weak log del Pezzo, although not every member is log del Pezzo.

## Assumptions and scope
The ground field is \(\mathbb C\). The term *weak log del Pezzo* means a normal projective klt surface with \(-K\) nef and big; *log del Pezzo* additionally requires \(-K\) ample. The distinct Jordan sizes are used, not their multiplicities: the latter affect the Plücker embedding, but not this criterion. A pencil with no regular Kronecker summand has \(\kappa=0\), and its Schubert surface is a Veronese model of \(\mathbb P^2\). The claim does not address general matrix nets or pencils in positive characteristic.

## Proof
We use the explicit resolution of the Schubert surface in [1, Sections 3–4]. Write \(f:X\to Y_L\) for the resolution, where \(X\) is the blow-up of \(\mathbb P^2\) at \(\kappa\) (possibly infinitely near) centers on the strict transform of its distinguished line at infinity. The centers form one chain of length \(k_{i h_i}\) for each distinct eigenvalue. Let \(H\) be the pullback of a line, and let \(E_{i\ell}\) be the **total transforms** of the exceptional classes, so that
\[
H^2=1,\quad H E_{i\ell}=0,\quad E_{i\ell}E_{jt}=-\delta_{ij}\delta_{\ell t}.
\]
Because every center lies on the successively transformed line at infinity, its final strict transform is
\[
B=H-\sum_{i,\ell}E_{i\ell},\qquad B^2=1-\kappa.
\]
The canonical formula for iterated point blow-ups gives
\[
K_X=-3H+\sum_{i,\ell}E_{i\ell},\qquad -K_X=2H+B.
\]
The strict exceptional curves are \(A_{i\ell}=E_{i\ell}-E_{i,\ell+1}\) for \(\ell<k_{i h_i}\), and \(A_{i,k_{i h_i}}=E_{i,k_{i h_i}}\). They satisfy
\[
H A_{i\ell}=0,\qquad
B A_{i\ell}=\begin{cases}0&\ell<k_{i h_i},\\1&\ell=k_{i h_i}.\end{cases}
\]
By [1, Propositions 3.7 and 4.5 and Theorem 4.6], \(f\) contracts exactly the strings of \((-2)\)-curves for which \(\ell\) is not a distinct Jordan size, and additionally contracts \(B\) if and only if the pencil is regular. The surviving curves \(A_{i,k_{ij}}\) map birationally to distinguished rational curves \(C_{ij}\). All contracted \((-2)\)-strings are Du Val and hence crepant.

For a **singular** pencil the line \(B\) survives. Since the other contractions are crepant,
\[
f^*(-K_{Y_L})=-K_X=2H+B.
\]
Thus \((-K_{Y_L})^2=(2H+B)^2=9-\kappa\), and the intersection on the infinity curve is \((2H+B)B=3-\kappa\).

For a **regular** pencil, \(B\) is contracted and \(B^2=-(\kappa-1)\); the remaining contractions are crepant. Write \(K_X=f^*K_{Y_L}+aB\). Intersecting with \(B\) and using adjunction gives \(K_X B=\kappa-3\); hence \(a=(3-\kappa)/(\kappa-1)\). Therefore
\[
f^*(-K_{Y_L})=-K_X+aB=2H+\frac{2}{\kappa-1}B,
\]
whose square is \(4+4/(\kappa-1)=4\kappa/(\kappa-1)>0\). This divisor intersects \(B\) in zero, as required for a pullback.

We now test **every irreducible curve**, rather than only distinguished curves. If a curve \(D\subset X\) is neither \(B\) nor exceptional for the blow-up \(X\to\mathbb P^2\), then \(HD\ge1\) and \(BD\ge0\): the first fact follows by projection to a plane curve, and the second is nonnegative intersection of distinct effective curves on a smooth surface. In either formula above, the pullback of \(-K_{Y_L}\) intersects \(D\) strictly positively. For exceptional curves, the intersections vanish on \(A_{i\ell}\) with \(\ell<k_{i h_i}\) and equal \(1\) in the singular case, or \(2/(\kappa-1)\) in the regular case, on the final \(A_{i,k_{i h_i}}\). The only additional test curve is \(B\), with intersection zero in the regular case and \(3-\kappa\) in the singular case.

It follows that \(-K_{Y_L}\) is nef for every regular pencil, and nef for singular pencils exactly when \(\kappa\le3\). Its calculated square is positive in every nef case, establishing bigness. A quotient surface has klt singularities, and the characteristic-zero base-point-free theorem makes nef-and-big \(-K_{Y_L}\) semiample. Consequently its anticanonical morphism contracts exactly the curves with intersection zero. The surviving intermediate exceptional curves occur precisely when some \(h_i>1\); in the singular case \(\kappa=3\), the infinity curve also has intersection zero. A semiample big divisor is ample precisely when its morphism contracts no curves. These observations give all claimed ampleness criteria and identify every anticanonically contracted curve. \(\square\)

## Verification
The accompanying dependency-free program `verify.py` performs exact rational intersection calculations in the blow-up lattice, checks the canonical-pullback identities and the vanishing and positivity of the distinguished curves, and runs regression tests on all distinct-size profiles with up to six blow-ups and at most three eigenvalues (304 profiles). The program returns `VERIFY_OK`. The classification of *all* curves depends on the geometric nonnegative-intersection argument in the proof; finite tests are not substituted for it.

As calibration, a regular two-eigenvalue size-one pencil gives \(\mathbb P^1\times\mathbb P^1\), which is log del Pezzo. A single regular size-two Jordan block yields a quadric cone, also log del Pezzo. By contrast, the regular block profile \((1,2)\) gives \(\mathbb F_2\), weak log del Pezzo but not log del Pezzo, as described in [1, Examples 2.8–2.10].

## Relationship to prior work
Galgano, Gesmundo and Keneshlou [1] construct the resolution of \(Y_L\), identify its quotient singularities, and determine distinguished curve intersections and the cohomology ring. The present theorem uses their geometry as input and supplies a complete **anticanonical** classification, including sharp weak-Fano/Fano thresholds, volumes and the exact anticanonical contraction locus. Their examples include both a quadric cone and \(\mathbb F_2\), but their stated results do not supply the above classification across Kronecker types. Standard surface base-point freeness supplies the semiampleness step. The general machinery and known small examples are not claimed as new.

## Limitations
This is a consequence built using the detailed resolution in [1], not a new independent construction of Schubert surfaces. The result applies only over \(\mathbb C\) to two-dimensional linear spaces of matrices. An unindexed explicit version of the classification in other literature cannot be excluded; independent audit remains outstanding. The finite checker tests numerical identities, not positivity for arbitrary curves, which is proved geometrically.

## References
[1] Vincenzo Galgano, Fulvio Gesmundo, Hanieh Keneshlou, *Schubert compactifications of matrix pencils*, arXiv:2610.07164 (first publicly posted 2026-10-05), especially Sections 2.6, 3.2, 4.1–4.3 and 6.

[2] János Kollár and Shigefumi Mori, *Birational Geometry of Algebraic Varieties*, Cambridge Tracts in Mathematics 134 (1998), the base-point-free theorem for klt pairs.
