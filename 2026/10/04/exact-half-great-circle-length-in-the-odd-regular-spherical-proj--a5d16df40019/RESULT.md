# Exact half-great-circle length in the odd regular spherical projective-billiard family

## Finding
For every odd integer \(n\ge 3\), take the unique spherical member of the regular \(n\)-gon family in González, namely \(j=(n-1)/2\). Put \(\alpha=\pi/n\) and \(v=\cos\alpha\). Its midpoint orbit has spherical length exactly \(\pi\), not merely an odd multiple of \(\pi\). Therefore a connected open neighborhood of primitive \(n\)-periodic trajectories containing the midpoint orbit has the same exact spherical length \(\pi\).

## Assumptions and scope
The billiard is the central-facet projective billiard of Theorem 4.6 in arXiv:2609.28817v1 on a Euclidean regular \(n\)-gon in the affine chart \(z=1\), and \(n\) is odd. The member \(j=(n-1)/2\) is used; Proposition 4.10 of the source identifies it as the unique member with positive-definite invariant form. Length means round spherical length for the Cayley--Klein metric determined by that form. The conclusion concerns the connected component of the open \(n\)-periodic family containing the midpoint witness; it does not claim that every trajectory in the whole billiard has period \(n\), nor that every periodic component has length \(\pi\).

## Proof
For \(j=(n-1)/2\), the source parameter satisfies \(\theta=\alpha\) and \(C=\cos\theta=v\). Substitution into its formula
\[
\lambda=v\frac{2v^2-1-C}{C-1}
\]
gives
\[
\lambda=v\frac{2v^2-v-1}{v-1}=v(2v+1)>0.
\]
The invariant quadratic form from Lemma 4.4 is therefore, up to a positive scalar,
\[
Q=\operatorname{diag}(1,1,\lambda v)=\operatorname{diag}(1,1,v^2(2v+1)).
\]

Let \(M_k\) be the Euclidean midpoint of side \(k\). In the chart \(z=1\), choose the representative
\[
M_k=\bigl(v\cos((2k+1)\alpha),\,v\sin((2k+1)\alpha),\,1\bigr).
\]
Theorem 4.6 proves that the cyclic sequence of these midpoints is the strict primitive \(n\)-periodic witness. Its squared \(Q\)-norm is
\[
\langle M_k,M_k\rangle_Q
=v^2+v^2(2v+1)=2v^2(v+1).
\]
For consecutive midpoints,
\[
\begin{aligned}
\langle M_k,M_{k+1}\rangle_Q
&=v^2\cos(2\alpha)+v^2(2v+1)\\
&=v^2(2v^2-1+2v+1)\\
&=2v^3(v+1).
\end{aligned}
\]
After \(Q\)-normalization, the spherical inner product is thus exactly \(v\). All chosen lifts have positive \(z\)-coordinate, so consecutive impacts use the minor great-circle arc, and its length is
\[
\arccos v=\arccos(\cos\alpha)=\alpha=\frac{\pi}{n}.
\]
Summing the \(n\) equal arcs gives total length \(n\alpha=\pi\).

The source's openness criterion gives an open two-parameter family of primitive \(n\)-periodic trajectories around this strict midpoint witness. In the positive-definite case these are ordinary spherical billiard trajectories. The source's metric unfolding theorem states that lengths are locally constant on a connected periodic family; equivalently, its spherical theorem gives the discrete congruence class \(L\equiv\pi\pmod{2\pi}\). Shrinking to the connected component containing the midpoint orbit therefore propagates the computed value \(L=\pi\) to every trajectory in that component.

## Verification
The proof is symbolic. The only parameter simplification is \(2v^2-v-1=(v-1)(2v+1)\). The midpoint coordinates have Euclidean radius \(v\) and angular separation \(2\alpha\). Substitution into the displayed \(Q\)-inner products gives normalized consecutive inner product exactly \(v\); no numerical approximation is used. The source was checked at Theorem 4.6, Proposition 4.10, Theorem 5.25, Theorem 5.33, and Remark 5.34, where it explicitly warns that \(L\equiv\pi\pmod{2\pi}\) does not by itself imply \(L=\pi\).

## Relationship to prior work
González constructs the regular polygon family for every period, identifies one spherical member for each odd period, and proves only the general odd-family residue \(L\equiv\pi\pmod{2\pi}\). The same paper proves \(L=\pi\) for a different period-five configuration by a chord-budget argument, but it does not state the exact midpoint length for the arbitrary odd regular family. The 2024 work of Fierobe supplies earlier reflective projective-billiard examples, including the right-spherical triangle and even-period centrally projective polygons, but does not give this all-odd exact length identity. Targeted statement and alias searches found no stronger result covering the arbitrary odd regular spherical members.

## Limitations
The conclusion is local to the connected open primitive family containing the midpoint witness. It does not classify all periodic trajectories of the spherical regular billiard, and it does not address the indefinite members of the projective family. The originality search cannot exclude unindexed folklore or an equivalent observation in unpublished notes.

## References
1. J. L. González, *Reflective projective billiards in the plane: odd periods, period five, and metric rigidity*, arXiv:2609.28817v1, first public 2026-09-23.
2. C. Fierobe, *Examples of projective billiards with open sets of periodic orbits*, Discrete and Continuous Dynamical Systems 44 (2024), 3287--3301, DOI:10.3934/dcds.2024059.
