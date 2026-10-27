# Three Weil spectra among the six forms of the exceptional genus-three bielliptic Picard curve over \(\mathbb F_{13}\)

## Finding

Put \(k=\mathbb F_{13}\). For \(A\in\{1,2,4\}\) and \(d\in\{1,2\}\), let \(C_{A,d}\subset\mathbb P^2_k\) be the smooth plane curve
\[
X^3Z+A(d^2Y^4+dY^2Z^2+5Z^4)=0.
\]
These are exactly six pairwise nonisomorphic \(k\)-forms of one geometric genus-three curve (with its unique order-six action); its Jacobian has \(13\)-rank one and \(a\)-number two. The abstract geometric-isomorphism and sextic-twist classification is known; the new assertion is their exact zeta spectrum:
\[
Z(C_{A,d}/k,T)=\frac{L_A(T)}{(1-T)(1-13T)},
\]
where
\[
\begin{aligned}
L_1(T)&=(1+13T^2)^2(1+2T+13T^2),\
L_2(T)&=(1-13T^2+169T^4)(1+5T+13T^2),\
L_4(T)&=(1-13T^2+169T^4)(1-7T+13T^2).
\end{aligned}
\]
Thus there are precisely **three** arithmetic Jacobian isogeny classes among the six distinct \(k\)-forms, with **two** curves per Weil polynomial. For \(m=1,2,3\), the vectors of point counts \((\#C(\mathbb F_{13}),\#C(\mathbb F_{13^2}),\#C(\mathbb F_{13^3}))\) are \((16,244,2128)\), \((19,145,2128)\), and \((7,121,2128)\) for \(A=1,2,4\), respectively, independent of \(d\). In particular the quadratic subfamily of twists preserves the entire zeta function although its two forms are not \(k\)-isomorphic.

## Assumptions and scope

All models are over the prime field \(k\) of cardinality \(13\). The numerical labels \(A\) and \(d\) denote representatives of the three cube classes and two square classes of \(k^\times\). The point at infinity is \([1:0:0]\). The assertion concerns all unmarked \(k\)-forms of this single **geometric** curve; it does not classify all genus-three curves over \(k\). Isogenies below are over \(k\), and distinct Weil polynomials imply different \(k\)-isogeny classes.

## Proof

**Smoothness and geometric locus.** Write \(h_d(t)=d^2t^4+dt^2+5\). Its discriminant criterion (equivalently \(1-4\cdot5=7\ne0\) after \(t\mapsto\sqrt d\,t\)) shows that \(h_d\) has four simple roots. The affine chart \(Z=1\) is the nonsingular cyclic cover \(X^3=-Ah_d(Y)\) except possibly where \(3X^2=h'_d(Y)=0\); separability rules those points out. At \([1:0:0]\), the \(Z\)-derivative is nonzero. The curve is geometrically connected, smooth of degree four, hence genus three. In a geometric coordinate change \(X'=A^{-1/3}X\), \(Y'=\sqrt d\,Y\) and subsequent rescaling of \(Y'\) and \(Z\), it acquires the normal form \(X^3 Z+Y^4+rY^2Z^2+Z^4=0\) with \(r^2=1/5=8\) in \(k\). This is the unique exceptional geometric class at characteristic \(13\) in Ohashi–Kudo–Harashita, Theorem B. Its full geometric automorphism group is cyclic of order six because \(r\ne0\) (Theorem A), or equivalently by Laga–Shnidman's non-special criterion.

**Six inequivalent forms.** The full automorphism group is \(\mu_6\), split over \(k\) as \(6\mid12=\#k^\times\). By cyclic Galois descent, \(H^1(k,\mu_6)\simeq k^\times/(k^\times)^6\) contains exactly six elements; there is no larger automorphism group to identify them. Changing independently the cube-root coordinate \(X\) by a cube-class parameter and the square-root coordinate \(Y\) by a square-class parameter produces exactly \(C_{A,d}\). The subgroup representatives \(A=1,2,4\) are distinct cube classes, and \(d=1,2\) are distinct square classes. Hence all six classes occur once. This structural classification of sextic twists is not asserted to be novel; it specializes §2.4 of Laga–Shnidman.

**Cartier–Manin check.** For a plane quartic \(F\) in characteristic \(p=13\), index the Hasse–Witt matrix by the degree-one monomials \(X,Y,Z\); its \((i,j)\)-entry is the coefficient of \(X^{12+13i_X-j_X}Y^{12+13i_Y-j_Y}Z^{12+13i_Z-j_Z}\) in \(F^{12}\). The \(X\)-exponent divisibility by three and parity of the \(Y\)-exponent force every off-diagonal entry to vanish. Exact multinomial evaluation gives diagonal entries \((0,h_A,0)\), with \(h_1=11\), \(h_2=8\), and \(h_4=7\), independently of \(d\). Thus the Hasse–Witt rank and stable semilinear rank are both one. The Jacobian has \(a=3-1=2\) and \(13\)-rank one, agreeing with the published exceptional locus classification.

**Exact point counts.** For \(q=13^m\), each \(t\in\mathbb F_q\) contributes one affine point when \(-Ah_d(t)=0\), three when it is a nonzero cube, and zero otherwise. Since \(q\equiv1\pmod3\), the nonzero-cube condition is \((-Ah_d(t))^{(q-1)/3}=1\). Add the unique point at infinity. Exhaustive field arithmetic with the irreducible moduli \(u^2+3u+1\) and \(u^3+4u+1\) gives for \(m=1,2,3\) the three vectors displayed above. The entire enumeration is reproducible by the attached standalone \(\texttt{verify.py}\): it iterates every element of all three fields, uses exact multiplication modulo \(13\), tests power residues, and asserts the point counts for each of the six curves. Thus the counts are complete and not statistical sampling.

**Full Weil polynomials.** Let \(N_m\) be a count, \(S_m=13^m+1-N_m\), and \(L_A(T)=\sum_{j=0}^{6}c_jT^j\). Newton identities give
\[
c_1=-S_1,\quad c_2=(S_1^2-S_2)/2,\quad c_3=-(S_1^3-3S_1S_2+2S_3)/6.
\]
For a smooth genus-three curve over \(\mathbb F_{13}\), the functional equation gives \(c_4=13c_2\), \(c_5=13^2c_1\), \(c_6=13^3\). Substitution yields coefficient tuples \((1,2,39,52,507,338,2197)\), \((1,5,0,-65,0,845,2197)\), \((1,-7,0,91,0,-1183,2197)\), factoring exactly as stated. These calculations determine \(\#C(\mathbb F_{13^m})\) for **every** \(m\ge1\), not just the three enumerated degrees. Weil's isogeny classification identifies exactly the three \(k\)-isogeny classes; the first has a product of two supersingular elliptic factors in the Prym isogeny class, while the other two have the displayed irreducible quartic supersingular Prym factors.

## Verification

Run \(\texttt{python3 verify.py}\) using Python 3 with no third-party modules. The code independently checks the irreducibility of the degree-two and degree-three field moduli, all 18 field/curve point counts, the three resulting Weil polynomials, and the full \(3\)-by-\(3\) Hasse–Witt matrices for the six models. Successful execution prints \(\texttt{VERIFY_OK}\). Exhaustive enumeration establishes the three field-level counts; the infinite-extension conclusion additionally uses the genus-three Weil functional equation, not extrapolation.

## Relationship to prior work

Ohashi, Kudo and Harashita (arXiv:2111.09777, 2021) classify the \(a\)-number and geometric isomorphism types of order-six genus-three curves; at characteristic \(13\) they identify the one exceptional geometric class. Laga and Shnidman (arXiv:2308.15297, first public 2023, §2.4) already provide the **general** sextic-twist classification and Jacobian–Prym isogeny. Li, Mantovan, Pries and Tang (arXiv:1805.06914, 2018) discuss broader Newton-polygon families of cyclic covers. Meagher and Top (2010) give general methods for finite-field twists and treat explicit quartics with at least sixteen geometric automorphisms, unlike the present six-automorphism curve. None of the relevant inspected sections states the three explicit Weil polynomials above or their precise two-per-polynomial assignment to the six \(k\)-forms. Consequently, the claimed addition is solely their explicit full zeta-spectrum classification, not the general twist theory, the exceptional geometric locus, or the splitting of the Jacobian into Prym and elliptic factors.

## Limitations

This is a **single characteristic-thirteen geometric class**, not a uniform statement for all primes. The six classes are \(k\)-nonisomorphic but become isomorphic over an algebraic closure. The zeta polynomials alone do not determine polarization classes or Jacobian isomorphism. Zeta polynomials may individually appear in existing tabulations of abelian varieties over finite fields; such entries would not on their own identify these six Picard models. No general theorem ruling out unindexed earlier exact computations is claimed.

## References

1. R. Ohashi, M. Kudo and S. Harashita, *The a-numbers of non-hyperelliptic curves of genus 3 with cyclic automorphism group of order 6*, arXiv:2111.09777 (first public 2021-11-18), Theorems A and B and Cartier–Manin calculations.
2. J. Laga and A. Shnidman, *The geometry and arithmetic of bielliptic Picard curves*, arXiv:2308.15297 (first public 2023-08-29), §§2.1–2.5 and especially §2.4 on sextic twists.
3. W. Li, E. Mantovan, R. Pries and Y. Tang, *Newton polygons arising for special families of cyclic covers of the projective line*, arXiv:1805.06914 (first public 2018-05-17), special cyclic-cover families and Newton polygons.
4. S. Meagher and J. Top, *Twists of genus three curves over finite fields*, Finite Fields and Their Applications 16 (2010), 347–368, explicit twist arithmetic for plane quartics with at least sixteen automorphisms.
