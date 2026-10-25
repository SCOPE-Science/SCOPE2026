# A binary-quadratic census of central quotients of the rank-two free class-four Lie algebra

## Finding
Let \(q\) be any prime power and \(F\) the free nilpotent Lie algebra of class \(4\) on two generators over \(\mathbb F_q\). For a nonzero central line \(K\) in its degree-four part, the seven-dimensional quotient \(L_K=F/K\) has a complete adjoint-rank distribution determined by a single number \(\nu\in\{0,1,2\}\), the number of rational projective roots of a naturally associated binary quadratic. Explicitly, with \(N_j=\#\{w\in L_K:\operatorname{rank}(\operatorname{ad}_w)=j\}\),

\[
\begin{aligned}
N_0&=q^2,\\
N_1&=\nu(q-1)q^2,\\
N_2&=(q-1)q^4+(q^2-1-\nu(q-1))q^2,\\
N_3&=\nu(q-1)q^5,\\
N_4&=(q^2-1-\nu(q-1))q^5.
\end{aligned}
\]

All other ranks have multiplicity zero, and the elementwise commuting probability is
\[
\Pr_{w,v\in L_K}([w,v]=0)=\frac{2q^3+q^2-q-1+\nu(q-1)^2(q+1)}{q^7}.
\]
Exactly three isomorphism classes occur as \(K\) varies, characterized by \(\nu=0,1,2\), represented by irreducible, repeated-root, and split-distinct binary quadratics. The numbers of central lines of these respective types are \((q^2-q)/2\), \(q+1\), and \(q(q+1)/2\). These assertions include characteristic two.

## Assumptions and scope
For every prime power \(q\), take the eight-dimensional Lie algebra over \(\mathbb F_q\) with ordered homogeneous basis \(x,y,z,u,v,a,b,c\), and brackets
\[
[x,y]=z,\quad [x,z]=u,\quad [y,z]=v,\quad
[x,u]=a,\quad [y,u]=b,\quad [x,v]=b,\quad [y,v]=c,
\]
with alternating and bilinear extension and all unspecified basic brackets zero. This is the free nilpotent class-four algebra on two generators, with graded dimensions \((2,1,2,3)\). In characteristic two alternating means \([w,w]=0\), not simply a signed skew-symmetry assumption. Its central degree-four space is \(\langle a,b,c\rangle\). For any \((A,B,C)\ne(0,0,0)\), let \(K=\langle Aa+Bb+Cc\rangle\), and define
\[
Q_K(s,t)=At^2-Bst+Cs^2,\qquad
\nu(K)=\#\{[s:t]\in\mathbb P^1(\mathbb F_q):Q_K(s,t)=0\}.
\]
The definition of \(\nu\) is invariant under multiplying \((A,B,C)\) by a nonzero scalar. Its values are \(0,1,2\) also in characteristic two; for a repeated root the support has one rational point.

## Proof
**The adjoint ranks.** Write a representative \(w=\alpha x+\beta y+\gamma z+\delta u+\epsilon v+z_4\), where \(z_4\) is degree-four central. If \((\alpha,\beta)\ne(0,0)\), one combination of \([w,x]\) and \([w,y]\) has a nonzero \(z\)-coefficient, giving one independent image vector. The image \([w,z]=\alpha u+\beta v\) supplies an independent homogeneous degree-three component. The degree-four outputs \([w,u]=\alpha a+\beta b\) and \([w,v]=\alpha b+\beta c\) are linearly independent in the free center: if a linear combination vanishes, its first and third coefficients force the scalars to vanish (including when \(\alpha=0\) or \(\beta=0\), by examining the remaining coefficient). Modulo \(K\), their span has dimension one precisely when \(K\) is contained in it. A normal vector to this two-plane in the coefficient basis \((a,b,c)\) is \((\beta^2,-\alpha\beta,\alpha^2)\). Therefore the rank is \(3\) when \(Q_K(\alpha,\beta)=0\), and \(4\) otherwise. Lower-degree terms \(\gamma,\delta,\epsilon\) do not alter these ranks: the two independent leading-degree images together with the degree-four images span the image after elimination. Each nonzero pair \((\alpha,\beta)\) supports \(q^5\) values of the other five coefficients in \(L_K\).

If \(\alpha=\beta=0\) but \(\gamma\ne0\), the brackets \([w,x]\) and \([w,y]\) have independent \(u,v\) coefficients, while the remaining brackets vanish; the rank is \(2\), with \((q-1)q^4\) elements. If \(\alpha=\beta=\gamma=0\) and \((\delta,\epsilon)\ne(0,0)\), the only nonzero image vectors are, up to sign, \(\delta a+\epsilon b\) and \(\delta b+\epsilon c\); their rank modulo \(K\) is \(1\) on \(Q_K(\delta,\epsilon)=0\) and \(2\) otherwise. Each pair allows \(q^2\) central coefficients. The remaining \(q^2\) central elements have rank \(0\).

Each projective root of \(Q_K\) represents exactly \(q-1\) nonzero pairs. Counting the above cases proves the five displayed multiplicity formulas, and their sum is \(q^7\). The centralizer of an element of adjoint rank \(j\) has size \(q^{7-j}\); summing this against the multiplicities and dividing by \(q^{14}\) gives the commuting-probability identity.

**Classification and multiplicities of central lines.** An invertible linear change of the generating pair \((x,y)\) extends to an automorphism of \(F\). On the three-dimensional central homogeneous part its projective action is the degree-two symmetric-power action (up to the common determinant scalar), and it carries the root locus of \(Q_K\) by the induced projective linear substitution. A nonzero binary quadratic over a finite field has one of three projective divisor types: no rational root, a repeated rational root, or two distinct rational roots. A linear change of variables takes any quadratic of each type to any other of the same type; for the irreducible type this follows by identifying the conjugate pair with the roots of an irreducible quadratic and using the transitive action on conjugate degree-two closed points. This remains valid for characteristic two. Thus the three root types each form one automorphism orbit of central lines and hence one quotient isomorphism class. Conversely the adjoint rank-one multiplicity \(N_1=\nu(q-1)q^2\) is a Lie-algebra isomorphism invariant and distinguishes them.

There are \(q+1\) repeated-root lines (the Veronese image of \(\mathbb P^1\)); there are \(\binom{q+1}{2}=q(q+1)/2\) lines encoding unordered pairs of distinct rational roots; and the remaining \((q^2-q)/2\) of the \(q^2+q+1\) central lines are irreducible. This proves the classification and class multiplicities.

## Verification
The accompanying `verify.py`, run with `python3 verify.py`, computes Lie brackets and Jacobi identities using finite-field arithmetic. It forms an augmented matrix for each adjoint map and its central ideal, checks the induced quotient rank by exact Gaussian elimination, and compares with the five formulas. It exhaustively treats all central lines over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\); over \(\mathbb F_5\) it checks one representative of each verified projective general-linear orbit. It also independently generates the three projective orbits and confirms their sizes. The observed terminating marker is `CENTRAL_QUOTIENT_RANKS_OK`. These finite checks supplement, but do not replace, the field-uniform proof.

## Relationship to prior work
Benito, de-la-Concepción, and Laliena (2016 preprint, later journal article) develop the structure and automorphisms of free nilpotent Lie algebras, especially quadratic (metric) quotients. Here the quotients are not required to admit invariant nondegenerate metrics; the new object is their exact finite-field adjoint-rank distribution and commuting probability. Schneider's finite-field nilpotent Lie classification (2004) enumerates small-dimensional isomorphism classes for selected small fields but does not supply the all-prime-power adjoint-rank formulas. Burde's seven-dimensional degeneration results concern complex-field isomorphism geometry, rather than pointwise finite-field rank multiplicities. The known general adjoint-rank spectra of certain maximal-class filiform families concern different graded Lie algebras and do not cover these class-four central quotients.

## Limitations
The theorem concerns only one-dimensional subspaces of the degree-four center of the rank-two free class-four algebra; it does not classify arbitrary seven-dimensional nilpotent Lie algebras or all central quotients by higher-dimensional ideals. Publication priority outside the specifically inspected material is not proven. An adjoint-cohomology table for complex nilpotent Lie algebras was not fully accessible; cohomology is a different invariant, but unknown embedded tables remain a residual literature risk. The explicit proof, rather than the finite-field tests alone, establishes the asserted uniform scope.

## References
- P. Benito, D. de-la-Concepción, J. Laliena, *Free nilpotent and nilpotent quadratic Lie algebras*, arXiv:1604.02923, version 1 publicly posted 11 April 2016, https://arxiv.org/abs/1604.02923 .
- C. Schneider, *A computer-based approach to the classification of nilpotent Lie algebras*, arXiv:math/0406365, 2004, https://arxiv.org/abs/math/0406365 .
- D. Burde, *Degenerations of 7-dimensional nilpotent Lie algebras*, arXiv:math/0409275, 2004, https://arxiv.org/abs/math/0409275 .
- L. Magnin, *Adjoint and Trivial Cohomologies of Nilpotent Complex Lie Algebras of Dimension ≤7*, 2008, DOI:10.1155/2008/805305 (partial inspection only).
