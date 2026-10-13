# The six isolated Calabi--Yau singularities have Milnor number \(27\)
## Finding
Let \(Q\) be the anticanonical quartic threefold constructed in arXiv:2610.01276v1. Its six isolated singular points all have total-space Milnor number
\[
\mu(Q,p)=27.
\]
Equivalently, the Milnor fiber of each isolated hypersurface germ has reduced third homology of rank \(27\), hence Euler characteristic
\[
\chi(F_p)=1-27=-26.
\]

This is not the Milnor number \(9\) computed in the source for the singular quartic surface fiber \(Q_{v_0}\). The two numbers measure different germs: \(9\) is the Milnor number after fixing the base parameter, while \(27\) is the Milnor number of the isolated singularity of the threefold total space.

## Assumptions and scope
All germs are complex analytic. The threefold \(Q\) and its six singular points are exactly those in Burek's anticanonical quartic model. In local coordinates \((x,y,s,z)\), the source gives weights
\[
\operatorname{wt}(x)=\operatorname{wt}(y)=\operatorname{wt}(s)=1,\qquad
\operatorname{wt}(z)=2,
\]
and weighted initial form
\[
f_4=\lambda z^2+\mu s^4-q(x,y),\qquad \lambda\mu\ne0,
\]
where
\[
q(x,y)=xy(x+25y)(x+9y).
\]
The exact local equations have only terms of weighted degree strictly greater than \(4\) beyond \(f_4\). Thus the germs are semiquasihomogeneous.

## Proof
For the weighted-homogeneous initial form, the Jacobian ideal is
\[
\left(2\lambda z,\ 4\mu s^3,\ q_x,\ q_y\right).
\]
The binary quartic \(q\) has four distinct projective zeros. Hence \(q_x\) and \(q_y\), two homogeneous cubics, have no common projective zero and form a regular sequence in \(\mathbf C[x,y]\). Therefore
\[
\dim_{\mathbf C}\mathbf C[x,y]/(q_x,q_y)=3\cdot3=9.
\]
The \(z\)-derivative kills \(z\), while the \(s\)-derivative leaves the three classes \(1,s,s^2\). Consequently
\[
\mu(f_4)
=
\dim_{\mathbf C}
\frac{\mathbf C[x,y,s,z]}
{(2\lambda z,4\mu s^3,q_x,q_y)}
=
1\cdot3\cdot9
=
27.
\]

A standard theorem for semiquasihomogeneous isolated hypersurface singularities says that adding terms of strictly larger weighted degree does not change the Milnor number. Burek's local equations have precisely this form at all six points: the points over \(v=0\) and \(v=\infty\) share one initial form, while the points over \(v=\pm1,\pm i\) have the same form up to nonzero scalar coefficients. Hence every exact total-space germ has Milnor number \(27\).

Milnor's bouquet theorem for an isolated hypersurface singularity in complex dimension \(3\) identifies the Milnor fiber, up to homotopy, with a bouquet of \(\mu\) three-spheres. Thus its only nonzero reduced homology is
\[
\widetilde H_3(F_p,\mathbf Z)\cong\mathbf Z^{27},
\]
and \(\chi(F_p)=1-27=-26\).

## Verification
The accompanying `verify.py` checks the explicit quartic, its two cubic partial derivatives, the absence of a common projective root, the complete-intersection length \(9\), and the resulting Milnor-algebra dimension \(27\). It also checks the weighted-degree separation in the exact local equation printed by the source over \(v=0\). The replay output in `VERIFY.txt` ends with `VERIFY_OK`.

The non-computational inputs are the source's six-germ local normal forms, the semiquasihomogeneous invariance of Milnor number, and Milnor's bouquet theorem.

## Relationship to prior work
Burek proves that the anticanonical quartic has six isolated singularities, resolves each by a crepant weighted blow-up of weights \((1,1,1,2)\), and identifies the exceptional divisor as a smooth degree-two del Pezzo surface. In the Euler-characteristic calculation, the paper separately computes Milnor number \(9\) for the singular quartic surface fiber by the two-variable Jacobian algebra \(\mathbf C[[x,y]]/(q_x,q_y)\).

The total-space calculation above keeps the transverse base variable \(s\). Its derivative contributes the factor
\[
\dim_{\mathbf C}\mathbf C[s]/(s^3)=3,
\]
which changes the local Milnor number from \(9\) for the surface fiber to \(27\) for the threefold germ. Targeted searches for the source identifier together with “Milnor number \(27\),” “vanishing cycles,” “Jacobian algebra,” and the weighted local equation did not locate a prior statement of this total-space invariant.

## Limitations
The result concerns only the six isolated singularities of this explicit complex threefold. It does not classify their analytic isomorphism types beyond the semiquasihomogeneous information used here, and it does not assert the existence of a global smoothing of \(Q\). The Milnor-fiber statement is local. Because the initiating preprint is very recent, an equivalent calculation could exist in material not indexed by the searches used here.

## References
1. Dominik Burek, *An elliptic Calabi--Yau threefold of Mordell--Weil rank twelve*, arXiv:2610.01276v1, 1 October 2026.
2. Masako Furuya and Masataka Tomari, *A characterization of semi-quasihomogeneous functions in terms of the Milnor number*, Proceedings of the American Mathematical Society 132 (2004), 1885--1890, DOI 10.1090/S0002-9939-04-07383-6.
3. John Milnor, *Singular Points of Complex Hypersurfaces*, Annals of Mathematics Studies 61, Princeton University Press, 1968.
