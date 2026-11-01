# Exact inverse-sheet and observation-window transitions in coupled Gumowski–Mira rings

## Finding

Let \(N\ge2\), \(a,b>0\), \(\mu\in\mathbb R\), and \(0\le\varepsilon<1\). Set
\[
 g_\mu(t)=\mu t+\frac{2(1-\mu)t}{1+t^2},\qquad
 h(t)=(1+a)t-abt^3,
\]
and let \(P\) be the nearest-neighbor averaging operator on a ring of \(N\) nodes, so \((Px)_i=(x_{i-1}+x_{i+1})/2\) with indices taken cyclically (including repeated neighbors when \(N=2\)). Consider the full-space map \(T:\mathbb R^{2N}\to\mathbb R^{2N}\),
\[
 X_i=(1-\varepsilon)\{g_\mu(x_i)+h(y_i)\}+\varepsilon(Px)_i,
 \qquad Y_i=-x_i+g_\mu(X_i).
\]
Define the natural fold radius and fold value
\[
 s=\sqrt{\frac{1+a}{3ab}},\qquad
 H=\frac23(1+a)s.
\]

**Theorem.** There is an explicit global smooth change of *output* coordinates \(\Psi\) satisfying
\[
 \Psi\circ T(x,y)=(x,h(y_1),\ldots,h(y_N)).
\]
Consequently \(T\) is surjective, and the number of distinct preimages of a target with transformed coordinates \((u,v)=\Psi(X,Y)\) is exactly
\[
 \#T^{-1}(X,Y)=\prod_{i=1}^N m(v_i),\qquad
 m(t)=\begin{cases}3,&|t|<H,\\2,&|t|=H,\\1,&|t|>H.\end{cases}
\]
Its maximum full-space inverse multiplicity is therefore \(3^N\), attained at the origin. Its critical locus consists of the \(2N\) smooth hypersurfaces \(y_i=\pm s\); their critical-value hypersurfaces become \(v_i=\pm H\) under \(\Psi\). Distinct-coordinate critical-value hypersurfaces meet transversely. More precisely,
\[
 \det DT(x,y)=(1-\varepsilon)^N\prod_{i=1}^N\bigl((1+a)-3ab y_i^2\bigr).
\]

For a finite observation window \(B_L=[-L,L]^{2N}\), \(L>0\), define \(M_N(L)=\max_{z\in\mathbb R^{2N}}\#(T^{-1}(z)\cap B_L)\), counting distinct inputs. Then the **exact window transition** is
\[
 \boxed{M_N(L)=\begin{cases}
 1,&0<L\le s,\\
 2^N,&s<L<\sqrt3\,s,\\
 3^N,&L\ge\sqrt3\,s.
 \end{cases}}
\]
In particular the map is injective on \(B_L\) if and only if \(3abL^2\le1+a\). These conclusions hold for all \(\mu\) and for all ring sizes and coupling strengths in the stated range.

## Assumptions and scope

The coordinate space is all of \(\mathbb R^{2N}\), and the finite-window statement concerns the restriction of the map to the closed cube \(B_L\). The term *left-right equivalence* describes a coordinate change applied to the target, not a conjugacy between iterated dynamical systems. No compact invariant set or boundedness of subsequent trajectories is assumed. All counts are counts of distinct real one-step preimages, including fold targets where two roots merge. For \(\varepsilon=1\), which is deliberately excluded, the map loses all dependence on \(y\) and nonempty inverse fibers are infinite.

## Proof

Write \(\lambda=1-\varepsilon>0\), and use componentwise \(g_\mu\) and \(h\) on vectors. For any output \((X,Y)\), set
\[
 u=g_\mu(X)-Y,\qquad
 v=\frac{X-\lambda g_\mu(u)-\varepsilon Pu}{\lambda}.
\]
This defines \(\Psi(X,Y)=(u,v)\). Conversely, given \((u,v)\) set
\[
 X=\lambda\bigl(g_\mu(u)+v\bigr)+\varepsilon Pu,
 \qquad Y=g_\mu(X)-u.
\]
These are mutually inverse smooth maps, so \(\Psi\) is a global diffeomorphism for every \(\lambda\ne0\). The defining equations for \(T\) imply \(u=x\) and \(v=h(y)\) exactly. Hence \(\Psi\circ T=\operatorname{id}_{\mathbb R^N}\times h^{\times N}\). This reduction proves that every inverse fiber factors into \(N\) scalar cubic fibers, even though the forward dynamics couple the nodes.

Put \(A=1+a>0\) and \(B=ab>0\). The scalar cubic \(h(t)=At-Bt^3\) is onto \(\mathbb R\), with derivative \(h'(t)=A-3Bt^2\) and turning points \(\pm s\), whose images are \(\pm H\). On the three intervals cut out by \(\pm s\), \(h\) is strictly monotone; the limiting cubic values at infinity and the turning values give exactly three, two, or one distinct root as claimed. All scalar preimages are finite, and the target coordinate transformation preserves the cardinality. In particular \(h(t)=0\) has exactly the roots \(0,\pm\sqrt{A/B}\). Since \(g_\mu(0)=0\), precisely the \(3^N\) inputs with \(x=0\) and each \(y_i\) one of those roots map to \((X,Y)=(0,0)\).

For the Jacobian statement, let \(U=\lambda\operatorname{diag}(g_\mu'(x))+\varepsilon P\), \(D=\lambda\operatorname{diag}(h'(y))\), and \(G=\operatorname{diag}(g_\mu'(X))\). Direct differentiation gives
\[
 DT=\begin{pmatrix}U&D\\-I+GU&GD\end{pmatrix}.
\]
Subtracting \(G\) times the first block row from the second leaves \(\left(\begin{smallmatrix}U&D\\-I&0\end{smallmatrix}\right)\), whose determinant is \(\det D\). This yields the exact product and critical locus; \(\Psi\) carries the critical-value set to the independent-coordinate equations \(v_i=\pm H\). Their normals are independent whenever their node indices differ, establishing the asserted transverse intersection property.

It remains to prove the *sharp* finite-window bound. The inverse transformation fixes \(x=u\), so, for any target, preimages in \(B_L\) are bounded by the product of the numbers of scalar roots of \(h(t)=v_i\) in \([-L,L]\). That upper bound is attained by setting \(x=0\), choosing a scalar value \(v_i\) with the maximal allowed scalar count independently for each node, and forming its image using the explicit inverse \(\Psi^{-1}\). Thus it suffices to classify the maximal number of scalar roots in \([-L,L]\).

If \(L\le s\), \(h\) is strictly increasing on \([-L,L]\), including at the endpoint \(L=s\), so the maximum is one. If \(s<L<\sqrt3s\), there are scalar values just below \(H\) with two roots arbitrarily close to \(+s\) and therefore inside the window. There cannot be three roots inside the window: for each \(|v|<H\), the leftmost and rightmost roots \(r_-(v)<-s< s<r_+(v)\) both decrease strictly as \(v\) increases (implicit differentiation uses the negative derivatives on those branches). By oddness their magnitudes are equal at \(v=0\), where \(r_-(0)=-\sqrt3s\) and \(r_+(0)=\sqrt3s\). Thus
\[
 \min_{|v|<H}\max\{|r_-(v)|,|r_+(v)|\}=\sqrt3s,
\]
so a triple fiber cannot fit when \(L<\sqrt3s\). Finally if \(L\ge\sqrt3s\), all three roots of \(h(t)=0\) fit, and the cubic degree bounds every scalar fiber by three. Taking products gives the stated exact values \(1,2^N,3^N\) and establishes the equivalence with injectivity.

## Verification

The companion standard-library Python script `verify.py` evaluates the map, its inverse-coordinate formula, and its full \(2N\)-dimensional Jacobian using exact rational arithmetic. In 90 independent exact tests for \(N=2,3,4\), the reconstruction and determinant identities held. It also checks the \(3^N\) exact origin fibers at \(N=2,3,5\) with \(a=1\), \(b=1/2\), \(\mu=1/2\), \(\varepsilon=1/4\), where the scalar preimages of zero are \(-2,0,2\). For a concrete two-preimage witness, \(h(t)=2t-t^3/2\) and \(h(t)=3/2\) has roots \(1,(-1\pm\sqrt{13})/2\); precisely the first two lie in \([-3/2,3/2]\). These finite checks confirm examples and algebra; the proof above establishes the universal claims.

For the two parameter regimes used in the motivating study, the exact fold radii are
\[
 (a,b)=(1/100,1/20):\quad s=\sqrt{2020/3},
\qquad
 (a,b)=(33/100,1/10):\quad s=\sqrt{1330/99}.
\]
Both exceed one, so the entire initial cube \([-1,1]^{2N}\) has a unique-preimage restriction, although the full-space map has \(3^N\)-point fibers. This is a statement about one step and a chosen observation window, not about later iterates staying inside that window.

## Relationship to prior work

Fatoyinbo and Ghosh (2026) introduce the coupled nearest-neighbor Gumowski–Mira architecture and numerically explore synchronization, clustering and irregular regimes. The present theorem instead determines its global inverse-fiber geometry, singular hypersurfaces, and sharp finite-window ambiguity thresholds. Mira's noninvertible-map survey explains the classical one-dimensional cubic \(Z_1\)-\(Z_3\)-\(Z_1\) pattern and critical curves; those background facts are used, not claimed as new. The nontrivial network-specific step here is the global target diffeomorphism showing that the apparent feedback and ring coupling do not alter the multiplicity product, together with the full window transition. Literature on coupled noninvertible maps considers critical-curve basin bifurcations in other coupled systems, rather than this exact network's independent inverse-sheet stratification.

## Limitations

The theorem does not describe forward attractors, invariant probability measures, basins of attraction, or multistep preimage growth. Output equivalence is not dynamical conjugacy. The finite-cube count is not restricted to biologically or physically invariant cubes; it applies to prescribed bounded initial-data windows. The earlier noninvertible-map literature is extensive, and a historical-priority risk remains, especially for older treatments of Gumowski–Mira critical lines that could not all be inspected in full. No independent verification or priority certification has been performed.

## References

1. H. O. Fatoyinbo and I. Ghosh, *Collective Phase Reorganization and Cluster Synchronization in Networks of Coupled Gumowski–Mira Maps*, arXiv:2607.03686v1, first submitted 2026-07-04, https://arxiv.org/abs/2607.03686.
2. C. Mira, *Noninvertible maps*, Scholarpedia **2**(9):2328 (2007), https://doi.org/10.4249/scholarpedia.2328.
3. *Dynamics and Global Bifurcations in Two Symmetrically Coupled Non-Invertible Maps*, Mathematics **11**(6):1517 (2023), https://doi.org/10.3390/math11061517.
