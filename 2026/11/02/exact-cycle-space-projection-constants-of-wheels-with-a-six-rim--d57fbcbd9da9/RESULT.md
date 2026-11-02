# Exact cycle-space projection constants of wheels, with a six-rim saturation law

## Finding

For every integer \(n\ge3\), let \(G_n=K_1\vee C_n\) be the unweighted wheel with \(n\) rim vertices and one hub. Orient each edge arbitrarily, let \(E_n\) be its \(2n\)-element edge set, and give \(\mathbb R^{E_n}\) the real \(\ell_1\) norm. Let \(Z_n\subseteq\mathbb R^{E_n}\) be the real circulation space, namely the kernel of the oriented edge-to-vertex boundary map. Define its relative minimum projection constant

\[
\lambda_n=\inf\{\|P\|_{\ell_1(E_n)\to\ell_1(E_n)}:P^2=P,\ \operatorname{ran}P=Z_n\}.
\]

Then this infimum is attained and

\[
\boxed{\lambda_n=\min\left\{2-\frac1{n-1},\frac95\right\}.}
\]

In particular, the first four distinct values are \(\lambda_3=3/2\), \(\lambda_4=5/3\), \(\lambda_5=7/4\), and \(\lambda_6=9/5\). Thereafter the exact constant stays \(9/5\), independently of rim length. This is a statement about projections from the **canonical edge** \(\ell_1\) space onto its circulation subspace, not about absolute projection constants or Banach–Mazur distances of the quotient.

## Assumptions and scope

The graph is finite, simple, connected, unweighted, undirected, and has precisely one hub adjacent to every vertex of one chordless rim cycle. The ambient norm is the sum of absolute real edge coefficients. The result is invariant under changing edge orientations, because each such change is a coordinate sign isometry. The circulation space has dimension \(2n-(n+1)+1=n\). All claims quantify over every integer \(n\ge3\) and every real linear projection onto this exact subspace.

## Proof

**1. Facial coordinates and symmetrization.** Number rim vertices modulo \(n\). Orient spokes from the hub to vertex \(i\) and rim edges from vertex \(i+1\) to vertex \(i\). Identify spoke and rim edge spaces with \(\mathbb R^n\), and put \((Dx)_i=x_{i-1}-x_i\) with cyclic indices. The \(n\) oriented triangular facial circuits are the columns of the injective map

\[
F:\mathbb R^n\to\mathbb R^n\oplus\mathbb R^n,\qquad Fw=(Dw,w).
\]

Their boundaries vanish. Their rim coordinates prove independence; the dimension formula proves \(\operatorname{ran}F=Z_n\).

The group of cyclic rotations acts by isometric coordinate permutations on \(\ell_1(E_n)\) and preserves \(Z_n\). Averaging any projection over this finite group cannot increase its norm, preserves its range and its identity action on \(Z_n\), and produces a rotation-commuting projection. Every projection onto \(Z_n\) has the form \(P=F[U\ V]\) with \(UD+V=I\). For a rotation-commuting projection, \(U,V\) are circulant. Writing \(u=Ue_0\), \(v=e_0-Du\), its two edge-column norms are therefore

\[
A(u)=\|u\|_1+\|Du\|_1,\qquad
B(u)=\|e_0-Du\|_1+\|D(e_0-Du)\|_1.
\]

Hence, **exactly**, \(\lambda_n=\min_{u\in\mathbb R^n}\max\{A(u),B(u)\}\). There is no loss in this reduction because a circulant \(U\) with first column \(u\), together with \(V=I-UD\), always defines such a projection. The finite-dimensional convex objective attains its minimum, as demonstrated by the explicit vectors below.

**2. Matching upper bounds.** Put \(u\), in cyclic coordinate order, equal to

\[
\begin{array}{c|l}
n&u\\\hline
3&(-1/4,0,1/4)\\
4&(-1/6,0,1/6,1/3)\\
5&(-1/4,-1/8,0,1/8,1/4)\\
 n\ge6&(-3/10,0,\ldots,0,3/10).
\end{array}
\]

For each displayed vector a direct absolute-value calculation gives \(A(u)=B(u)\), equal in order to \(3/2,5/3,7/4,9/5\). Forming the corresponding circulant \(U\) gives a genuine projection with this norm, for every permitted \(n\).

**3. A general dual lower-certificate lemma.** Suppose \(\alpha,\beta\ge0\), \(\alpha+\beta=1\), and four vectors \(s,t,r,h\in\mathbb R^n\) obey

\[
\|s\|_\infty,\|t\|_\infty\le\alpha,\quad
\|r\|_\infty,\|h\|_\infty\le\beta,\quad
s+D^Tt-D^Tr-(D^2)^Th=0.
\]

Applying the four dual \(\ell_\infty\)-bounds to the four \(\ell_1\) terms and cancelling all coefficients of \(u\) yields, for **every** \(u\),

\[
\max\{A(u),B(u)\}\ge\alpha A(u)+\beta B(u)
\ge r_0+h_1-h_0.
\]

This lemma uses only linear duality and makes the lower bound uniform over all circulant projections.

**4. Exact finite certificates.** The following rows give \(s,t,r,h\) as displayed integer vectors divided by the common denominator \(d\), with \(\alpha=a/d\) and \(\beta=b/d\). Each row satisfies the lemma by direct cyclic substitution, and its constant \(r_0+h_1-h_0\) equals the indicated value:

\[
\begin{array}{c|ccc|l|l|l|l}
n&a&b&d&s d&t d&r d&h d\\\hline
3&1&1&2&(-1,0,1)&(1,-1,-1)&(1,1,1)&(-1,1,0)\\
4&4&5&9&(-4,-4,4,4)&(4,-4,-4,-4)&(5,5,5,5)&(-5,5,3,-3)\\
5&5&7&12&(-5,-5,0,5,5)&(5,-5,-5,-5,-5)&(7,7,7,7,7)&(-7,7,6,0,-6)\\
6&2&3&5&(-2,-2,0,0,2,2)&(2,-2,-2,-2,-2,-2)&(3,3,3,3,3,3)&(-3,3,3,1,-1,-3).
\end{array}
\]

**5. A single certificate for every \(n\ge7\).** Let \(z\) denote the cyclic shift, so \(D=z-1\) on coordinate vectors and \(D^T=z^{-1}-1\). Introduce four integer Laurent polynomials

\[
\begin{aligned}
S(z)&=-2(1+z+z^2)-z^3+z^{-4}+2(z^{-3}+z^{-2}+z^{-1}),\\
T(z)&=2-2(z+z^2+z^3+z^{-3}+z^{-2}+z^{-1}),\\
R(z)&=3(1+z+z^2+z^{-2}+z^{-1}),\\
H(z)&=-3+3z+3z^2+z^3-z^{-2}-3z^{-1}.
\end{aligned}
\]

Read the coefficients modulo \(z^n-1\), and put \((s,t,r,h)=(S,T,R,H)/5\), \(\alpha=2/5\), \(\beta=3/5\). For \(n\ge8\) the listed nonzero terms in each polynomial occupy distinct cyclic coordinates. For \(n=7\), the two terms of \(S\) at exponents \(3\) and \(-4\) cancel. Thus in every case the required supnorm bounds hold. The **formal Laurent-polynomial identity**

\[
S+(z^{-1}-1)T-(z^{-1}-1)R-(z^{-1}-1)^2H=0
\]

holds over the integers, not merely at tested values of \(n\). Consequently the cancellation identity holds after reducing modulo \(z^n-1\) for every \(n\ge7\). Finally \(r_0=3/5\), \(h_1=3/5\), and \(h_0=-3/5\), giving the exact uniform lower bound \(9/5\).

**6. Conclusion.** The four finite certificates and the universal Laurent certificate give lower bounds equal to the upper constructions for all \(n\ge3\). Symmetrization transfers this optimum from circulant projections to **all** projections onto the wheel's real circulation subspace. This proves both the formula and the saturation at six rim vertices.

## Verification

Run `python3 wheel_projection_verify.py` from the directory containing this document. The stdlib-only checker reconstructs each proposed projection from its cyclic columns, checks that it fixes every facial circuit, computes exact \(\ell_1\) column norms, verifies all dual inequalities, and checks the formal Laurent identity using integer coefficients. A replay returned `CHECK_OK 109531 exact rational and Laurent identities n=3..200`. The finite range is a cross-check; the unlimited-\(n\) step is proved by the formal Laurent identity and its support-collision argument.

## Relationship to prior work

Dilworth, Kutzarova, and Ostrovskii (arXiv:1807.03814v1, July 10, 2018) identify the real Lipschitz-free space of an unweighted finite graph with \(\ell_1(E)/Z(G)\), and use symmetry averaging to study projection constants of recursively generated diamond and Laakso graphs. Their Section 4.4 supplies the general averaging paradigm, but the inspected main results, Sections 4–6 and graph families do not give the wheel constant or its six-rim plateau. The calculation here is an exact optimization of the nonunique cyclicly invariant projections for a different graph family, with matching explicit primal and dual witnesses. Existing results on weighted-wheel negative type, wheel symmetric edge polytopes, and coordinate projections of cactus transportation spaces concern different spaces or invariants; they do not imply the stated relative \(\ell_1\) projection constant. A historical equivalent under different terminology remains possible.

## Limitations

No claim is made for edge weights, arbitrary graph cones, cycle spaces of other graphs, absolute projection constants, or Banach–Mazur distance of the quotient. Symmetry averaging itself is prior methodology; the exact wheel optimization and its saturation phenomenon are the proposed contribution. The proof is mathematical and exact, but the literature comparison does not constitute an independent historical priority certification. All norm and orientation conventions matter.

## References

1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz-free spaces on finite metric spaces*, arXiv:1807.03814v1 (first public version July 10, 2018), https://arxiv.org/abs/1807.03814 . Full text inspected: https://denka.web.illinois.edu/DKO.pdf (Sections 1.1, 1.3, 4.4, 5.3 and relevant contents).
