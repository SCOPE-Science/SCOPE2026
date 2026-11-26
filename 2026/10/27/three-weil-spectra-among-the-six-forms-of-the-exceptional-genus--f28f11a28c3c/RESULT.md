# Three Weil spectra among the six forms of the exceptional genus-three bielliptic Picard curve over \(\mathbb F_{13}\)

## Finding

Put \(k=\mathbb F_{13}\). For \(A\in\{1,2,4\}\) and \(d\in\{1,2\}\), let \(C_{A,d}\subset\mathbb P^2_k\) be the smooth plane curve
\[
X^3Z+A(d^2Y^4+dY^2Z^2+5Z^4)=0.
\]
These are exactly six pairwise nonisomorphic unmarked \(k\)-forms of one geometric genus-three curve. Its full geometric automorphism group is cyclic of order six, and the \(\mu_6\)-action normalized to act on the tangent line at the fixed point by the identity character is unique. The Jacobian has \(13\)-rank one and \(a\)-number two. The geometric classification and sextic-twist classification are known; the new assertion is the exact assignment of zeta numerators to these six forms:
\[
Z(C_{A,d}/k,T)=\frac{L_A(T)}{(1-T)(1-13T)},
\]
where
\[
\begin{aligned}
L_1(T)&=(1+13T^2)^2(1+2T+13T^2),\\
L_2(T)&=(1-13T^2+169T^4)(1+5T+13T^2),\\
L_4(T)&=(1-13T^2+169T^4)(1-7T+13T^2).
\end{aligned}
\]
Thus there are precisely **three** arithmetic Jacobian isogeny classes among the six distinct \(k\)-forms, with **two** curves per Weil polynomial. For \(m=1,2,3\), the vectors of point counts \((\#C(\mathbb F_{13}),\#C(\mathbb F_{13^2}),\#C(\mathbb F_{13^3}))\) are \((16,244,2128)\), \((19,145,2128)\), and \((7,121,2128)\) for \(A=1,2,4\), respectively, independent of \(d\). In particular the pair of quadratic twists at each fixed \(A\) has the same entire zeta function although the curves are not \(k\)-isomorphic.

## Assumptions and scope

All models are over the prime field \(k\) of cardinality \(13\). The numerical labels \(A\) and \(d\) denote representatives of the three cube classes and two square classes of \(k^\times\). The point at infinity is \([1:0:0]\). The assertion concerns all unmarked \(k\)-forms of this single **geometric** curve; it does not classify all genus-three curves over \(k\). Isogenies below are over \(k\). The uniqueness of the action refers to the tangent-normalized action, not to an arbitrary choice of generator of the cyclic automorphism group.

## Proof

**Smoothness and geometric locus.** Write \(h_d(t)=d^2t^4+dt^2+5\). Its discriminant criterion (equivalently \(1-4\cdot5=7\ne0\) after \(t\mapsto\sqrt d\,t\), with constant term \(5\ne0\)) shows that \(h_d\) has four simple roots. In the affine chart \(Z=1\), a singular point of \(X^3=-Ah_d(Y)\) would satisfy \(3X^2=h'_d(Y)=0\), contrary to separability. At \([1:0:0]\), the \(Z\)-derivative is nonzero, and this is the only point at infinity. The smooth plane quartic has genus three. Over an algebraic closure set \(X'=(5A)^{-1/3}X\) and \(Y'=(d^2/5)^{1/4}Y\), with \(Z\) unchanged. Dividing the equation by \(5A\) gives the normal form \(X'^3Z+Y'^4+rY'^2Z^2+Z^4=0\), with \(r^2=1/5=8\) in \(k\). The two possible signs of \(r\) are geometrically equivalent by rescaling \(Y'\). This is the unique exceptional geometric class at characteristic \(13\) in Ohashi–Kudo–Harashita, Theorem B. Its full geometric automorphism group is cyclic of order six since \(r\ne0,\pm2\) (Theorem A). The bielliptic involution and the cubic deck transformations generate it. The identity-tangent normalization singles out one action among the two faithful identifications of \(\mu_6\) with this group, as in Laga–Shnidman, Definition 2.5 and Lemma 2.6.

**Six inequivalent forms.** The full automorphism group is \(\mu_6\), split over \(k\) as \(6\mid12=\#k^\times\) and visible from the coordinate actions on \(X\) and \(Y\). Galois descent classifies unmarked forms by \(H^1(k,\mu_6)\simeq k^\times/(k^\times)^6\), with exactly six elements. Changing independently the cube-root coordinate \(X\) by a cube-class parameter and the square-root coordinate \(Y\) by a square-class parameter in the model \(C_{1,1}\) produces \(C_{A,d}\): over the algebraic closure the map to \(C_{1,1}\) uses \(A^{-1/3}X\) and \(\sqrt d\,Y\). The cocycle components are the corresponding Kummer classes (inverting a class does not affect exhaustiveness). The representatives \(A=1,2,4\) are distinct cube classes, and \(d=1,2\) are distinct square classes. Hence all six classes occur once. This structural classification specializes §2.4 of Laga–Shnidman.

**Cartier–Manin check.** For a plane quartic \(F\) in characteristic \(p=13\), index the Hasse–Witt matrix by the degree-one monomials \(X,Y,Z\); its \((i,j)\)-entry is the coefficient of \(X^{12+13i_X-j_X}Y^{12+13i_Y-j_Y}Z^{12+13i_Z-j_Z}\) in \(F^{12}\). Divisibility of the \(X\)-exponent by three and parity of the \(Y\)-exponent force every off-diagonal entry to vanish. Exact multinomial evaluation gives diagonal entries \((0,h_A,0)\), with \(h_1=11\), \(h_2=8\), and \(h_4=7\), independently of \(d\). Thus the Hasse–Witt rank and stable Frobenius rank are both one. The Jacobian has \(a=3-1=2\) and \(13\)-rank one, agreeing with the published exceptional locus classification.

**Exact point counts.** For \(q=13^m\), each \(t\in\mathbb F_q\) contributes one affine point when \(-Ah_d(t)=0\), three when it is a nonzero cube, and zero otherwise. Since \(q\equiv1\pmod3\), the nonzero-cube condition is \((-Ah_d(t))^{(q-1)/3}=1\). Add the unique point at infinity. Exhaustive field arithmetic with the irreducible moduli \(u^2+3u+1\) and \(u^3+4u+1\) gives for \(m=1,2,3\) the three vectors displayed above. The enumeration is reproducible by the attached standalone `verify.py`: it iterates every element of all three fields, uses exact multiplication modulo \(13\), tests power residues, and asserts the point counts for each of the six curves.

**Full Weil polynomials.** Let \(N_m\) be a count, \(S_m=13^m+1-N_m\), and \(L_A(T)=\sum_{j=0}^{6}c_jT^j\). Newton identities give
\[
c_1=-S_1,\quad c_2=(S_1^2-S_2)/2,\quad c_3=-(S_1^3-3S_1S_2+2S_3)/6.
\]
For a smooth genus-three curve over \(\mathbb F_{13}\), the functional equation gives \(c_4=13c_2\), \(c_5=13^2c_1\), \(c_6=13^3\). Substitution yields coefficient tuples \((1,2,39,52,507,338,2197)\), \((1,5,0,-65,0,845,2197)\), \((1,-7,0,91,0,-1183,2197)\), factoring exactly as stated. These calculations determine \(\#C(\mathbb F_{13^m})\) for **every** \(m\ge1\). Tate's isogeny theorem identifies exactly the three \(k\)-isogeny classes.

The elliptic quotient by the bielliptic involution has equation \(W^2=7-4X^3/A\), obtained by setting \(W=2dY^2+1\) in the affine chart. It is ordinary: the \(X^{12}\)-coefficient of \((7-4X^3/A)^6\) is \(\binom64 7^2(-4/A)^4\ne0\) modulo \(13\). Hence it accounts for the ordinary quadratic factor of each \(L_A\); the remaining factor is the Prym polynomial. For \(A=1\) it gives a product of two supersingular elliptic factors in the Prym isogeny class. For \(A=2,4\) the remaining polynomial is the irreducible supersingular quartic: its reciprocal has roots \(\alpha=\sqrt{13}\,\zeta\) with \(\zeta\) a primitive twelfth root of unity. Each \(\alpha^2=(13/2)(1\pm\sqrt{-3})\) generates \(\mathbb Q(\sqrt{-3})\), but if \(\alpha=x+y\sqrt{-3}\) were in this quadratic field, comparison of the real part of \(\alpha^2\) with \(|\alpha|^2=13\) would give \(x^2=39/4\), impossible for rational \(x\).

## Verification

Run `python3 verify.py` from the original package using Python 3 with no third-party modules. The unchanged verifier checks the irreducibility of the degree-two and degree-three field moduli, all 18 field/curve point counts, the three resulting Weil polynomials, and the full \(3\)-by-\(3\) Hasse–Witt matrices for the six models. Successful execution prints `VERIFY_OK`. Exhaustive enumeration establishes the three field-level counts; the infinite-extension conclusion additionally uses the genus-three Weil functional equation, not extrapolation.

## Relationship to prior work

Ohashi, Kudo and Harashita (arXiv:2111.09777) classify the \(a\)-number and geometric isomorphism types of order-six genus-three curves; at characteristic \(13\) they identify the one exceptional geometric class. The characteristic-thirteen Hasse polynomial and the corresponding rank and \(a\)-number are also treated in the Resultary record [6da8625d9e59](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-the-doubled-nonordinary-hasse-divisor-of-the-bielliptic-picard-f--6da8625d9e59). Laga and Shnidman (arXiv:2308.15297, §2.4) give the general sextic-twist classification and Jacobian–Prym isogeny. Li, Mantovan, Pries and Tang (arXiv:1805.06914) discuss broader Newton-polygon families of cyclic covers. Meagher and Top (2010) give general methods for finite-field twists and treat explicit quartics with at least sixteen geometric automorphisms, unlike the present six-automorphism curve.

The three polynomials and their associated extension-field counts are tabulated at the abelian-variety isogeny-class level in LMFDB entries [3.13.c_bn_ca](https://www.lmfdb.org/Variety/Abelian/Fq/3/13/c_bn_ca), [3.13.f_a_acn](https://www.lmfdb.org/Variety/Abelian/Fq/3/13/f_a_acn), and [3.13.ah_a_dn](https://www.lmfdb.org/Variety/Abelian/Fq/3/13/ah_a_dn). Those entries do not identify the six nonhyperelliptic models; the latter two entries do not determine whether the classes contain a nonhyperelliptic Jacobian. The addition here is the exact two-per-polynomial assignment to the six \(k\)-forms of this particular geometric curve, not the individual polynomials as abstract Weil polynomials, the general twist theory, the exceptional geometric locus, or the Jacobian splitting.

## Limitations

This is a single characteristic-thirteen geometric class, not a uniform statement for all primes. The six classes are \(k\)-nonisomorphic but become isomorphic over an algebraic closure. The zeta polynomials alone do not determine polarization classes or Jacobian isomorphism. No exhaustive exclusion of earlier unindexed model-level computations is claimed.

## References

1. R. Ohashi, M. Kudo and S. Harashita, *The a-numbers of non-hyperelliptic curves of genus 3 with cyclic automorphism group of order 6*, arXiv:2111.09777, Theorems A and B and Cartier–Manin calculations.
2. J. Laga and A. Shnidman, *The geometry and arithmetic of bielliptic Picard curves*, arXiv:2308.15297, §§2.1–2.5, especially Definition 2.5, Lemma 2.6 and §2.4 on sextic twists.
3. W. Li, E. Mantovan, R. Pries and R. Tang, *Newton polygons arising for special families of cyclic covers of the projective line*, arXiv:1805.06914, special cyclic-cover families and Newton polygons.
4. S. Meagher and J. Top, *Twists of genus three curves over finite fields*, Finite Fields and Their Applications 16 (2010), 347–368, explicit twist arithmetic for plane quartics with at least sixteen automorphisms.
