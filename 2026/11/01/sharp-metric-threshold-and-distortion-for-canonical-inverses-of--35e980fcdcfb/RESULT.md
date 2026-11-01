# Sharp metric threshold and distortion for canonical inverses of rank-one \(2\)-partial isometries

## Finding
Let \(T\ne0\) be a bounded rank-one \(2\)-partial isometry on a complex Hilbert space, let \(S=2T^*-(T^*)^2T\), and write \(s=|\operatorname{tr}T|^2\). The canonical reflexive generalized inverse \(S\) is the Moore–Penrose inverse of \(T\) for **one common equivalent Hilbert inner product** if and only if
\[
\|T\|^2<2\quad\Longleftrightarrow\quad s<\frac32.
\]
For eligible operators, among all such metrics \(G\) the sharp condition-number infimum \(\kappa(T)=\inf\|G\|\|G^{-1}\|\) is
\[
\kappa(T)=\begin{cases}
1,&s=0\ \text{or}\ s=1,\\[2pt]
\dfrac{2(2-s)}{3-2s},&0<s<\tfrac32,\ s\ne1.
\end{cases}
\]
For \(\tfrac32\le s<2\), no positive boundedly invertible metric works; equivalently set \(\kappa(T)=+\infty\). At the endpoint \(s=\tfrac32\), an explicit two-dimensional counterexample settles negatively, in general, the equivalent-inner-product question posed in the motivating source. The formula applies in every Hilbert-space dimension admitting \(T\), including infinite dimensions.

## Assumptions and scope
All Hilbert spaces and operators are complex. A bounded operator \(T\) is a \(2\)-partial isometry here precisely when
\[
T\bigl((T^*)^2T^2-2T^*T+I\bigr)=0.
\]
For rank one write \(T=uv^*\) with \(\|v\|=1\) and \(u\ne0\); the notation \(v^*x=\langle x,v\rangle\) uses a linear-first inner product. Put
\[
a=v^*u,\quad s=|a|^2,\quad L=\|u\|^2=\|T\|^2,\quad P=vv^*,\quad b=u-av\perp v.
\]
The operator trace of \(T\) equals \(a\), so \(s\) is representation-independent. An equivalent Hilbertian inner product means \(\langle x,y\rangle_G=\langle Gx,y\rangle\) with \(G=G^*>0\), bounded and boundedly invertible on the same Hilbert space. Both Penrose adjoint equations are interpreted using the **same** \(G\). The condition number \(\|G\|\|G^{-1}\|\) is scale-independent.

## Proof
**1. Rank-one reduction.** Since \(T^2=aT\),
\[
(T^*)^2T^2=sT^*T,\qquad T^*T=LP,
\]
so \(T\) is a \(2\)-partial isometry exactly when
\[
L(2-s)=1.\tag{1}
\]
Consequently \(0\le s<2\), \(L=(2-s)^{-1}\), and
\[
\|b\|^2=L-s=\frac{(s-1)^2}{2-s}.\tag{2}
\]
Thus \(b=0\) precisely at \(s=1\).

**2. Canonical generalized inverse and two idempotents.** Define \(w=2u-La v=(2-L)av+2b\). Direct multiplication gives
\[
S=vw^*,\quad w^*u=L(2-s)=1,\quad ST=P,\quad TS=Q=uw^*.
\]
Hence \(TST=T\), \(STS=S\), and \(Q^2=Q\). The first two Penrose equations already hold; the remaining two ask precisely that \(P\) and \(Q\) be self-adjoint under \(\langle\cdot,\cdot\rangle_G\):
\[
GP=PG,\qquad GQ=Q^*G.\tag{3}
\]
Because \(Q=uw^*\), the second equation is equivalent to \(Gu=cw\) for some real \(c>0\). Indeed the common rank-one operator is self-adjoint if and only if its generating vectors are real-proportional; positivity and \(w^*u=1\) enforce \(c=\langle Gu,u\rangle>0\).

**3. Necessary threshold.** From \(GP=PG\), write \(Gv=gv\) with \(g>0\); the decomposition \(\mathcal H=\mathbb Cv\oplus v^\perp\) is \(G\)-reducing. Comparing the components of \(Gu=cw\) gives
\[
(g-c(2-L))a=0,\qquad Gb=2cb.\tag{4}
\]
If \(a\ne0\), then \(g=c(2-L)>0\), so \(L<2\). If \(a=0\), (1) gives \(L=1/2<2\). Necessarily \(L<2\), equivalently \(s<3/2\).

**4. Sufficiency.** For \(L<2\), the explicit positive invertible operator
\[
G_0=(2-L)P+2(I-P)\tag{5}
\]
satisfies \(G_0P=PG_0\) and \(G_0u=w\). Hence \(G_0Q=ww^*=Q^*G_0\), verifying all four Penrose equations in the same inner product.

**5. Optimal distortion and exceptional endpoints.** For \(a\ne0\) and \(b\ne0\), (4) forces \(G\) to have orthogonal eigenvectors \(v\), \(b\) with respective eigenvalues \(c(2-L)\), \(2c\). Therefore \(\|G\|\|G^{-1}\|\ge2/(2-L)\), and (5) attains equality. Substituting (1) yields \(2(2-s)/(3-2s)\). The only cases without both nonzero eigenvectors are \(s=0\) and \(s=1\), by (2). In either case \(w=u/L\), hence \(S\) is already the ordinary Moore–Penrose inverse and \(G=I\) attains condition number one. This completes the classification.

**6. Explicit negative witness.** On \(\mathbb C^2\), let
\[
T=\begin{pmatrix}\sqrt{3/2}&0\\1/\sqrt2&0\end{pmatrix},\quad
S=\begin{pmatrix}0&\sqrt2\\0&0\end{pmatrix}.
\]
Equation (1) holds with \(L=2\) and \(s=3/2\), so \(T\) is a \(2\)-partial isometry. But
\[
ST=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
TS=\begin{pmatrix}0&\sqrt3\\0&1\end{pmatrix},\quad
(TS)(ST)=0\ne(ST)(TS).
\]
If both idempotents were orthogonal projections for any common inner product, the adjoint of \((TS)(ST)=0\) would give \((ST)(TS)=0\), a contradiction. This witness is independent of the optimal-distortion calculation.

## Verification
The algebraic equalities (1)–(5) provide an exact infinite-dimensional proof. A standalone standard-Python script `verify.py` checks the \(2\)-partial identity, two reflexive inverse identities, the metric equations and the predicted norm threshold on independently sampled real parameters and complex phases. Its finite computations are supplementary and are not a substitute for the proof. The strict boundary case is also proved symbolically above, without numerical inference.

## Relationship to prior work
Aouichaoui, Buchała and Garcia establish that \(2T^*-(T^*)^2T\) is a reflexive generalized inverse of a \(2\)-partial isometry (Lemma 2.8) and ask in their Question 6 whether it can always be Moore–Penrose relative to some inner product. They demonstrate that it need not be Moore–Penrose for the **original** inner product, which does not by itself rule out a different equivalent Hilbert metric. The rank-one threshold above gives a negative answer to the broader question and exactly describes the rank-one positive-metric cases, with the minimal distortion. Standard Penrose theory supplies the criterion that the two associated idempotents be self-adjoint in a common metric; equations (1)–(5) and the sharp metric formula constitute the specialization here.

## Limitations
This result classifies rank-one operators only. It does not characterize analogous metrics for general higher-rank \(2\)-partial isometries, or answer every case of the source's question. The condition number concerns positive boundedly invertible Hilbert metrics, not arbitrary indefinite forms or different inner products on domain and codomain. Although the final witness is two-dimensional, the theorem includes every rank-one operator on any complex Hilbert space. Publication priority beyond inspected sources is not independently certified.

## References
1. R. Aouichaoui, P. Buchała, S. R. Garcia, *On m-partial isometries: spectra, weighted shifts, and similarity*, arXiv:2606.12865v1 (first publicly submitted June 11, 2026), specifically Lemma 2.8 and Question 6, https://arxiv.org/abs/2606.12865.
2. Standard Moore–Penrose inverse criterion: the four Penrose equations and the characterization of the two idempotents as orthogonal projections in the chosen Hilbert inner product. Used as established background, not claimed as new.
