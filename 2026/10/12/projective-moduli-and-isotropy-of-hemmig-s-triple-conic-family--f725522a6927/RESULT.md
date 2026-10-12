# Projective moduli and isotropy of Hemmig's triple-conic family

## Finding
For \(\lambda\in\mathbb C\setminus\{0,-1\}\), set
\[
\Lambda:xy+xz+yz=0,
\]
\[
\Gamma_\lambda:x^2-(1+\lambda)xy-\lambda xz-(1+\lambda)yz=0,
\]
and
\[
\Delta_\lambda:z^2-\left(1+\lambda^{-1}\right)xy-\lambda^{-1}xz-\left(1+\lambda^{-1}\right)yz=0.
\]
Let \(\mathcal T_\lambda=\{\Lambda,\Gamma_\lambda,\Delta_\lambda\}\) be the unordered triple. Then
\[
\mathcal T_\lambda\cong_{\mathrm{PGL}_3}\mathcal T_\mu
\]
if and only if
\[
\mu\in\left\{\lambda,\lambda^{-1},-1-\lambda,-\frac{1+\lambda}{\lambda},-\frac1{1+\lambda},-\frac{\lambda}{1+\lambda}\right\}.
\]
Equivalently,
\[
J(\lambda)=256\frac{(\lambda^2+\lambda+1)^3}{\lambda^2(\lambda+1)^2}
\]
is a complete invariant for projective equivalence inside this family.

The full projective stabilizer of the unordered triple is generically trivial. It is isomorphic to \(C_2\) for
\[
\lambda\in\left\{1,-\frac12,-2\right\},
\]
and it is isomorphic to \(C_3\) when
\[
\lambda^2+\lambda+1=0.
\]

## Assumptions and scope
The ground field is \(\mathbb C\). The parameter restrictions \(\lambda\ne0,-1\) are those of Hemmig's family; they also ensure that all three displayed conics are nonsingular. The equivalence is for the unordered triple of embedded conics in \(\mathbb P^2\), not for a labeling of its three members.

All three conics meet at
\[
P=[0:1:0]
\]
with intersection multiplicity three for each pair. Their residual pairwise intersection points are
\[
A=[0:0:1],\qquad B=[1:0:0],\qquad C_\lambda=[\lambda:0:1].
\]
These three points are distinct and lie on the line \(L:y=0\).

## Proof
The point \(P\) is the unique point common to all three conics. The residual point of each pair is intrinsic to the unordered triple, so a projective equivalence \(\mathcal T_\lambda\to\mathcal T_\mu\) fixes \(P\), preserves the residual line \(L\), and permutes the three conics together with their three residual pairwise intersections.

A projectivity fixing \(P\) and preserving \(L\) has the form
\[
[x:y:z]\longmapsto[ax+bz:hy:dx+ez]
\]
with \(h(ae-bd)\ne0\). For each of the six permutations of \(\{\Lambda,\Gamma,\Delta\}\), the images of \(A,B,C_\lambda\) determine the induced fractional-linear map on \(L\). Substitution into the three quadratic equations then leaves exactly one relation between \(\lambda\) and \(\mu\). The six relations are
\[
\mu=\lambda,
\qquad \lambda\mu=1,
\qquad \lambda+\mu+1=0,
\]
\[
\lambda\mu+\lambda+1=0,
\qquad \lambda\mu+\mu+1=0,
\qquad \lambda\mu+\lambda+\mu=0.
\]
Solving for \(\mu\) gives precisely the six values stated in the finding.

Sufficiency is witnessed by explicit projectivities. Up to an overall nonzero scalar, their \((x,z)\)-blocks and \(y\)-multipliers can be chosen as follows:

- for \(\mu=\lambda\): \(\begin{psmallmatrix}1&0\\0&1\end{psmallmatrix}\), with \(h=1\);
- for \(\mu=\lambda^{-1}\): \(\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\), with \(h=1\);
- for \(\mu=-1-\lambda\): \(\begin{psmallmatrix}(\lambda+1)/\lambda&0\\-1/\lambda&1\end{psmallmatrix}\), with \(h=(\lambda+1)^2/\lambda^2\);
- for \(\mu=-(1+\lambda)/\lambda\): \(\begin{psmallmatrix}0&-(\lambda+1)/\lambda\\-1/\lambda&1\end{psmallmatrix}\), with \(h=-(\lambda+1)^2/\lambda\);
- for \(\mu=-1/(1+\lambda)\): \(\begin{psmallmatrix}-1/(\lambda+1)&\lambda/(\lambda+1)\\1&0\end{psmallmatrix}\), with \(h=(\lambda+1)/\lambda\);
- for \(\mu=-\lambda/(1+\lambda)\): \(\begin{psmallmatrix}1/(\lambda+1)&-\lambda/(\lambda+1)\\0&1\end{psmallmatrix}\), with \(h=\lambda+1\).

Direct pullback shows, in each case, that the target conics become nonzero scalar multiples of the prescribed source conics. Hence every relation above is realized projectively.

For completeness of the scalar invariant, direct expansion gives
\[
\begin{aligned}
&\operatorname{num}\!\left(J(\lambda)-J(\mu)\right)/256\\
&=(\lambda-\mu)(\lambda\mu-1)(\lambda+\mu+1)
(\lambda\mu+\lambda+1)(\lambda\mu+\lambda+\mu)(\lambda\mu+\mu+1).
\end{aligned}
\]
Because \(\lambda,\mu\notin\{0,-1\}\), equality \(J(\lambda)=J(\mu)\) is therefore equivalent to one of the six projective-equivalence relations.

Finally, the stabilizer at a given parameter consists of those six parameter transforms that fix \(\lambda\). The three transpositions have fixed points \(\lambda=1\), \(\lambda=-1/2\), and \(\lambda=-2\), respectively. The two nontrivial three-cycles have the common fixed locus \(\lambda^2+\lambda+1=0\). These loci are disjoint in the allowed parameter space, which gives the claimed trivial, \(C_2\), and \(C_3\) stabilizers.

## Verification
The accompanying verifier uses exact rational-function arithmetic over \(\mathbb Q(\lambda)\). It checks all six pullback identities for the displayed projectivities, invariance of \(J\) under all six parameter transforms, the exact six-factor numerator identity for \(J(\lambda)-J(\mu)\), and the fixed-point equations giving the stabilizer strata. No floating-point computation is used.

## Relationship to prior work
Hemmig's Lemma 4.31 introduces exactly these three conics and proves the pairwise intersection pattern. For the symmetry needed in the degree-eight complement construction, it asks only when an automorphism preserving \(\Lambda\) exchanges \(\Gamma_\lambda\) and \(\Delta_\lambda\), obtaining precisely \(\lambda=1\). The present result treats all six permutations simultaneously, classifies projective equivalence between arbitrary parameters in the family, and determines the full isotropy stratification. The six parameter transforms become the classical anharmonic six transforms after the change of parameter \(t=-\lambda\), but the realization of the entire action by projectivities of this specific triple is established here by the explicit pullback computation.

## Limitations
This is a classification internal to Hemmig's one-parameter triple-conic family; it does not classify arbitrary triples of conics with the same local intersection multiplicities. It is over \(\mathbb C\); over non-algebraically closed or positive-characteristic fields, rationality of the projectivities and exceptional stabilizer behavior require separate analysis. No claim is made about automorphisms of the later degree-eight curves beyond the consequences already encoded by their auxiliary conic triples.

## References
1. M. Hemmig, *Isomorphisms between complements of projective plane curves*, arXiv:1902.06324v1; published in *Épijournal de Géométrie Algébrique* 3 (2019), DOI 10.46298/epiga.2019.volume3.5541. See Lemma 4.31 and the proof of Theorem 3.
