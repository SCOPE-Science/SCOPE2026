# Exact maximal-spanning vectors for two-dimensional dihedral irreducibles
## Finding
Let \(D_{2n}=\langle r,s:r^n=s^2=e,\ srs=r^{-1}\rangle\) have order \(2n\), with \(n\ge3\). Every irreducible unitary representation of \(D_{2n}\) admits a vector whose orbit rank-one projectors span the full matrix algebra. Consequently every irreducible representation of \(D_{2n}\) does matrix recovery, and therefore phase retrieval.

The one-dimensional irreducibles are immediate. Every two-dimensional irreducible is equivalent to
\[
\pi_k(r)=\begin{pmatrix}\zeta^k&0\\0&\zeta^{-k}\end{pmatrix},
\qquad
\pi_k(s)=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
1\le k<n/2,
\]
where \(\zeta=e^{2\pi i/n}\). Put \(q=\zeta^{2k}\), \(m=\operatorname{ord}(q)=n/\gcd(n,2k)\), and \(\eta=(a,b)^T\).

The exact maximal-spanning criterion is:
\[
m>2:\quad ab\ne0\ \text{ and }\ |a|\ne|b|;
\]
\[
m=2:\quad |a|\ne|b|\ \text{ and }\ \operatorname{Im}((a\overline b)^2)\ne0.
\]
Thus \(\eta=(1,2)^T\) works whenever \(m>2\), while \(\eta=(1,2e^{i\pi/8})^T\) works when \(m=2\).

## Assumptions and scope
A vector \(\eta\) is called maximal-spanning here when the complex linear span of
\[
P_g=\pi(g)\eta\eta^*\pi(g)^*,\qquad g\in D_{2n},
\]
is \(M_d(\mathbb C)\), where \(d\) is the representation dimension. This is stronger than ordinary phase retrieval: equality of all phaseless orbit measurements annihilates the difference of the two rank-one signal Gram matrices against every \(P_g\); full matrix span forces those signal Gram matrices to agree.

The statement concerns ordinary complex irreducible unitary representations of finite dihedral groups. It does not claim that arbitrary reducible dihedral representations have the same property, nor does it classify full-spark or Haar-property orbit frames in higher representation dimension.

## Proof
For a two-dimensional irreducible, write
\[
A=|a|^2,\qquad B=|b|^2,\qquad c=a\overline b.
\]
For the rotation orbit one obtains
\[
P_j=
\begin{pmatrix}
A&cq^j\\
\overline c q^{-j}&B
\end{pmatrix},
\qquad 0\le j<m,
\]
and for the reflected rotation orbit,
\[
Q_j=
\begin{pmatrix}
B&\overline c q^{-j}\\
cq^j&A
\end{pmatrix}.
\]

Assume first that \(m>2\). Averaging the \(P_j\) and \(Q_j\) over one \(q\)-cycle gives
\[
\frac1m\sum_jP_j=\operatorname{diag}(A,B),
\qquad
\frac1m\sum_jQ_j=\operatorname{diag}(B,A).
\]
These span the two-dimensional diagonal subspace exactly when \(A\ne B\). Since \(q\) has order greater than two,
\[
\sum_{j=0}^{m-1}q^{-j}P_j=mcE_{12},
\qquad
\sum_{j=0}^{m-1}q^jP_j=m\overline c E_{21},
\]
because the unwanted term contains \(\sum_jq^{\pm2j}=0\). Hence the two off-diagonal matrix units are recovered exactly when \(c\ne0\). This proves the criterion for \(m>2\).

Now assume \(m=2\), so \(q=-1\). Again \(P_0+P_1\) and \(Q_0+Q_1\) span the diagonal subspace exactly when \(A\ne B\). For the off-diagonal part,
\[
P_0-P_1=
2\begin{pmatrix}0&c\\\overline c&0\end{pmatrix},
\qquad
Q_0-Q_1=
2\begin{pmatrix}0&\overline c\\c&0\end{pmatrix}.
\]
These two matrices span the full off-diagonal subspace exactly when
\[
c^2-\overline c^2\ne0,
\]
equivalently \(\operatorname{Im}(c^2)\ne0\). This proves the second criterion.

All irreducible complex representations of a finite dihedral group have dimension one or two. A nonzero vector is maximal-spanning in a one-dimensional representation, and the explicit vectors above treat every two-dimensional irreducible. Therefore every irreducible representation of \(D_{2n}\) has a maximal-spanning vector.

Finally, if two signals \(f,h\) have equal phaseless orbit measurements, then
\[
\operatorname{tr}((ff^*-hh^*)P_g)=0
\]
for every \(g\). Full matrix span implies \(ff^*=hh^*\), hence \(h=\alpha f\) for some \(|\alpha|=1\).

## Verification
The analytic proof above is complete and does not depend on finite enumeration. The bundled `verify.py` independently constructs every two-dimensional irreducible parameter \(k\) for \(3\le n\le80\), forms all rotation and reflection orbit projectors, and computes their complex span by Gaussian elimination. It checks the explicit working vectors and representative failures for each branch of the exact criterion.

The replay returns `VERIFY_OK irreps=1560 m2_cases=20 n_range=3..80`. This finite replay is a consistency check only; it is not used to infer the all-\(n\) theorem.

## Relationship to prior work
Oussa and Sheehan study a different \(n\)-dimensional induced dihedral representation and prove a Haar/full-spark property for almost every orbit vector when \(n\) is odd. Their theorem concerns linear independence of vector subfamilies, not the span of rank-one orbit projectors, and their representation is not the two-dimensional irreducible family classified here.

Führ and Oussa develop phase retrieval for irreducible representations of nilpotent groups and, in the finite setting, focus mainly on \(p\)-groups. Their finite results do not give the all-\(n\) dihedral classification above. Malikiosis and Oussa likewise treat full-spark orbit frames for semidirect-product representations; full spark does not imply the present rank-one-projector spanning criterion.

A later article by Cheng has the broad title *On the phase retrievability of irreducible representations of finite groups*. Its accessible bibliographic metadata and indexing were checked, but a materially readable full text was not available in the inspected sources. No accessible search evidence located a dihedral theorem or the exact order-\(2\) resonance criterion above. This remains the principal literature risk.

## Limitations
The result is restricted to irreducible complex representations of finite dihedral groups. It is not a classification for reducible representations, projective representations with a nontrivial multiplier, or other semidirect products. The later Cheng paper noted above was not materially inspected in full text, so a residual priority risk remains despite targeted searches finding no matching statement.

The direct numerical replay covers \(3\le n\le80\) only. It checks the formulas but does not replace the proof for arbitrary \(n\).

## References
1. V. Oussa and B. Sheehan, *Dihedral Group Frames with the Haar Property*, arXiv:1705.00085v1, first posted 2017-04-28; later published in *Linear and Multilinear Algebra*.
2. H. Führ and V. Oussa, *Phase Retrieval for Nilpotent Groups*, arXiv:2201.08654v1, first posted 2022-01-21; *Journal of Fourier Analysis and Applications* 29 (2023), Article 47, DOI 10.1007/s00041-023-10031-5.
3. R. D. Malikiosis and V. Oussa, *Full Spark Frames in the Orbit of a Representation*, arXiv:1909.06223v1, first posted 2019-09-13; *Applied and Computational Harmonic Analysis*.
4. C. Cheng, *On the Phase Retrievability of Irreducible Representations of Finite Groups*, *Linear Algebra and its Applications* 714 (2025), 64–95, DOI 10.1016/j.laa.2025.03.011.
