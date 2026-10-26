# Sharp sixth moments and nonlocal optimal stability for the fundamental–adjoint character pair of \(SU(3)\)

## Finding
Let \(G=SU(3)\) have probability Haar measure. Write \(\chi_{\mathrm f}(g)=\operatorname{tr}(g)\) for the defining three-dimensional character and \(\chi_{\mathrm{ad}}(g)=|\operatorname{tr}(g)|^2-1\) for the eight-dimensional adjoint character. For any \(a,b\in\mathbb C\), set \(F=a\chi_{\mathrm f}+b\chi_{\mathrm{ad}}\) and \(S=|a|^2+|b|^2=\|F\|_2^2\). Then
\[
\int_G|F|^6\,dg
=6|a|^6+117|a|^4|b|^2+360|a|^2|b|^4+145|b|^6+44\operatorname{Re}(a^3\overline b^{\,3}).
\]
In particular, the following is sharp:
\[
\boxed{\int_G|F|^6\,dg\le145S^3,}
\]
with equality, for nonzero \(F\), precisely when \(a=0\).

There is also a globally optimal quadratic stability inequality
\[
\boxed{145S^3-\int_G|F|^6\,dg\ge\kappa |a|^2S^2,}
\]
where \(u_*\in(0,1/4)\) is the unique root in that interval of
\[
20u^3-33u^2-84u+11=0,
\]
and
\[
\kappa=\frac{75-44u_*+318u_*^2+139u_*^4}{(1+u_*^2)^2}=72.227917510590\ldots.
\]
The coefficient \(\kappa\) cannot be increased. Apart from \(a=0\), equality in the stability inequality occurs exactly when \(b\ne0\), \(|a|=u_*|b|\), and \(a^3\overline b^{\,3}\) is positive real. Thus there are three relative-phase directions at the sharp nonzero stability ratio. The local second-variation coefficient at the pure-adjoint optimizer is \(75\), strictly greater than the global optimal coefficient \(\kappa\).

## Assumptions and scope
The characters are *ordinary trace characters*, not divided by representation dimension. Haar mass is \(1\). Coefficients \(a,b\) are arbitrary complex numbers, with no reality or phase restrictions. The statement concerns this two-character central subspace, not the larger span including the conjugate fundamental character, and not higher even moments. The inequality also holds at \(a=b=0\), where equality is trivial.

## Proof
Write \(w=\chi_{\mathrm f}\) and \(h=\chi_{\mathrm{ad}}=w\overline w-1\). The latter identity is the character identity \(\mathbf3\otimes\overline{\mathbf3}=\mathbf1\oplus\mathbf8\). Schur orthogonality gives \(\int|w|^2=\int h^2=1\) and \(\int wh=0\), proving the asserted formula for \(S\).

For completeness, the moments used below can be recovered directly by Weyl integration. On the maximal torus put \(z_3=(z_1z_2)^{-1}\), \(w=z_1+z_2+z_3\), and \(\overline w=z_1^{-1}+z_2^{-1}+z_3^{-1}\). For each class Laurent polynomial \(P\),
\[
\int_G P\,dg=\frac16\operatorname{CT}_{z_1,z_2}\left(P\prod_{1\le i<j\le3}(2-z_i/z_j-z_j/z_i)\right).
\]
Here \(\operatorname{CT}\) extracts the coefficient of \(z_1^0z_2^0\). Multiplying the explicitly displayed Laurent polynomials yields
\[
\left(\int_G|w|^{2j}\,dg\right)_{j=0}^{6}=(1,1,2,6,23,103,513)
\]
and
\[
\left(\int_Gw^{3+j}\overline w^{\,j}\,dg\right)_{j=0}^{3}=(1,3,11,47).
\]
In particular, binomial expansion of \(h=|w|^2-1\) gives the five exact inputs
\[
\int h^6=145,\quad\int |w|^2h^4=40,\quad\int|w|^4h^2=13,\quad\int|w|^6=6,\quad\int w^3h^3=22.
\]
(The standalone checker reproduces these values independently by integer Laurent-polynomial arithmetic.) Multiplication by a central element of order three rotates \(w\) by a cube root of unity and fixes \(h\). Thus in the expansion of \((aw+bh)^3(\overline a\overline w+\overline b h)^3\), only terms with equal exponents of \(w,\overline w\), or exponents differing by three, contribute. The displayed moment values and binomial coefficients yield the exact sixth-moment identity.

Subtracting that identity from \(145S^3\) gives, without omitted terms,
\[
\mathcal D=75|a|^2|b|^4+318|a|^4|b|^2+139|a|^6-44\operatorname{Re}(a^3\overline b^{\,3}).
\]
If \(b\ne0\), put \(u=|a|/|b|\) and \(\theta=3(\arg a-\arg b)\). For \(a\ne0\),
\[
\frac{\mathcal D}{|a|^2S^2}=\frac{75-44u\cos\theta+318u^2+139u^4}{(1+u^2)^2}\ge R(u):=\frac{75-44u+318u^2+139u^4}{(1+u^2)^2}.
\]
The same formula holds by continuity at \(u=0\) for its limiting value. An elementary differentiation gives
\[
R'(u)=-\frac{4(20u^3-33u^2-84u+11)}{(1+u^2)^3}.
\]
The cubic has exactly two positive zeros: one in \((0,1/4)\) and the other in \((1,3)\). Existence follows from opposite signs at these endpoints; there are exactly two by Descartes' rule of signs. Hence \(R\) strictly decreases to its first positive critical point \(u_*\), increases to its second positive critical point, and then decreases to \(139\) at infinity. Since \(R(u_*)\le R(1/8)<139\), its unique global minimum is \(\kappa=R(u_*)\). This proves the optimal stability inequality and the complete equality conditions. The case \(b=0\) gives \(\mathcal D/(|a|^2S^2)=139>\kappa\); the case \(a=0\) gives zero deficit. The numerator of \(R(u)\) is strictly positive for every \(u\ge0\), since \(75-44u+318u^2>0\) has negative discriminant and \(139u^4\ge0\); hence \(\kappa>0\). Therefore the sharp sixth-moment maximizers are exactly the nonzero pure-adjoint functions. Finally, \(R(0)=75>\kappa\), demonstrating strict separation between local and global optimal stability.

## Verification
The accompanying `checker.py` uses only the Python standard library. It independently forms the maximal-torus Weyl density and both characters as finite integer Laurent polynomials, evaluates all five critical moments by exact constant terms, checks the polynomial deficit and derivative identities, brackets the two positive roots, and tests 600 arbitrary complex coefficient pairs. Run `python3 checker.py` from the directory containing the file. The included `checks.txt` is a recorded successful execution. All universal and optimality statements follow from the above exact algebra and calculus, not from the numerical tests.

## Relationship to prior work
Agarwal and Nahmgoong (first posted January 23, 2020) derive recurrences for multiplicities of trivial representations in tensor powers of the \(SU(3)\) adjoint representation; their table already gives \(\int_G h^6\,dg=145\). That number is acknowledged here as known. Their published result does not state the present sharp mixed fundamental–adjoint inequality, exact complex mixed-moment polynomial, or globally best stability coefficient and its nontrivial equality families. The character integrals used in the proof are standard consequences of Weyl integration and representation theory. No novelty is claimed for those techniques alone.

## Limitations
The theorem is for exactly two specified irreducible characters of \(SU(3)\). It does not give the sharp sixth-moment norm on the three-dimensional space also containing the antifundamental character, nor a uniform statement for \(SU(N)\) as \(N\) varies. The local/global stability separation is exact for this example; no universality is asserted. Originality is a best-knowledge literature assessment, not an independent priority determination.

## References
1. P. Agarwal and J. Nahmgoong, *Singlets in the tensor product of an arbitrary number of Adjoint representations of SU(3)*, arXiv:2001.10826, first public version 2020-01-23, especially §3 and the table of singlet multiplicities.
2. Classical Weyl integration formula and character orthogonality for compact Lie groups (standard background identities; the needed forms are given explicitly in the proof).
