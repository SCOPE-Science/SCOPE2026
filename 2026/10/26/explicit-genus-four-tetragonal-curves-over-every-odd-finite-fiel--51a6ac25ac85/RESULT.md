# Explicit genus-four tetragonal curves over every odd finite field

## Finding
For every odd prime power \(q\), there is an explicit geometrically smooth canonical curve of genus \(4\) and \(\mathbb F_q\)-gonality exactly \(4\). This settles the odd-characteristic genus-four case of Question 1.3 in Faber–Grantham–Howe [1], which gives the nonsplit-quadric strategy but not a uniform smooth cubic.

Let \(p=\operatorname{char}\mathbb F_q\), and put
\[
 t=\begin{cases}2,&p=7,\\3,&p=13,\\1,&\text{otherwise},\end{cases}\qquad
 \kappa=(t^3+t)^2\in\mathbb F_p^\times.
\]
Choose **any** nonsquare \(c\in\mathbb F_q^\times\). The following two homogeneous equations in \(\mathbb P^3_{\mathbb F_q}\) cut out the required curve:
\[
 Q=xy-z^2+cw^2=0,\qquad
 F=y^3+x^2y+2y(z^2+cw^2)-\kappa x^3=0.
\]
In particular, \(P=[1:t^2:t:0]\) is a rational point on this curve. The construction applies to every extension field of every odd prime characteristic, using an arbitrary nonsquare \(c\) of that field. No uniqueness of isomorphism type or point-count extremality is asserted.

## Assumptions and scope
All varieties are taken over \(k=\mathbb F_q\) with \(q\) odd, and smoothness means geometric smoothness after extension to an algebraic closure. Gonality means the least degree of a **\(k\)-defined** nonconstant morphism to \(\mathbb P^1_k\), not geometric gonality. The constant \(t\) and the scalar \(\kappa\) are read in the prime subfield; the nonsquare \(c\) depends on \(k\). The two displayed equations are interpreted as a scheme-theoretic complete intersection in projective three-space.

## Proof
**1. Nonvanishing parameter.** If \(p\notin\{7,13\}\), then \(t=1\) and \(\kappa=4\). In the integers,
\[
 (27\cdot4)^2-16=11648=2^7\cdot7\cdot13.
\]
Thus \((27\kappa)^2\ne16\) in each odd characteristic except potentially \(7\) and \(13\). In characteristic \(7\), our choice \(t=2\) gives \(\kappa=2\), and \((27\kappa)^2-16=2\) modulo \(7\); in characteristic \(13\), \(t=3\) gives \(\kappa=3\), and the same expression equals \(6\) modulo \(13\). Each selected \(\kappa\) is nonzero. The condition also holds in characteristic \(3\), where the left side is \(-16\ne0\).

**2. Splitting the quadric and the cubic.** Fix \(d\) in an algebraic closure with \(d^2=c\), and set \(u=z+dw\), \(v=z-dw\). Since the characteristic is odd, this is invertible, and \(Q=xy-uv\). The Segre parametrization of \(Q\) over the algebraic closure is
\[
 x=s_0t_0,\quad y=s_1t_1,\quad u=s_0t_1,\quad v=s_1t_0.
\]
Substitution into \(F\), using \(u^2+v^2=2(z^2+cw^2)\), gives exactly
\[
 (s_1^3+s_1s_0^2)(t_1^3+t_1t_0^2)-\kappa s_0^3t_0^3=0.
\]
This is a divisor of bidegree \((3,3)\) on \(\mathbb P^1\times\mathbb P^1\), equivalently the fiber product equation \(f(s)=\kappa/f(t)\) for the separable degree-three map \(f(r)=r^3+r\) on \(\mathbb P^1\).

**3. Geometric smoothness.** The fiber product of separable finite morphisms between smooth curves is smooth at each point where their branch loci are disjoint: in local uniformizers, simultaneous ramification would be necessary for both defining partial derivatives to vanish. In characteristic \(3\), \(f'(r)=1\), and the only branch value of \(f\) is \(\infty\); the branch locus of \(\kappa/f\) is \(\{0\}\). These loci are disjoint. In characteristic other than \(3\), the branch values of \(f\) are \(\{\infty,v_0,-v_0\}\), where \(v_0^2=-4/27\), since its two finite critical points have square \(-1/3\) and critical values \(\pm v_0\). The branch values of \(\kappa/f\) are \(\{0,\kappa/v_0,-\kappa/v_0\}\). The two sets meet exactly when \(\kappa=\pm v_0^2\), equivalently \((27\kappa)^2=16\), already excluded in Step 1. Hence the complete intersection is geometrically smooth, including its points at infinity.

**4. Genus and canonical geometry.** Any decomposition of a divisor of type \((3,3)\) on \(\mathbb P^1\times\mathbb P^1\) into two nonempty effective pieces has positive intersection number. Consequently a smooth such divisor is geometrically integral. Adjunction gives
\[
 \omega_C\cong\mathcal O_C(1,1),\qquad g(C)=(3-1)(3-1)=4.
\]
The Segre embedding is therefore the canonical embedding of \(C\) in \(\mathbb P^3\). Its unique containing quadric is \(Q\) (equivalently, the space of quadrics vanishing on a smooth \((2,3)\) complete intersection is spanned by \(Q\)). Since \(c\) is a nonsquare, \(Q\) is a smooth nonsplit quadric over \(k\), with no \(k\)-rational line or \(k\)-defined ruling. A \(k\)-defined degree-three map from a nonhyperelliptic canonical genus-four curve would produce a \(k\)-defined ruling of its canonical quadric. Therefore \(C\) has no \(k\)-defined map of degree \(3\). It also has no map of degree \(1\) or \(2\), since it is canonically embedded and nonhyperelliptic. Thus \(\operatorname{gon}_k(C)\ge4\).

**5. Rational point and upper bound.** Direct substitution of \(P=[1:t^2:t:0]\) gives \(Q(P)=0\) and
\[
 F(P)=t^6+t^2+2t^4-\kappa=(t^3+t)^2-\kappa=0.
\]
For its canonical divisor \(K_C\), Riemann–Roch yields
\[
 \ell(K_C-2P)=1+\ell(2P)\ge2,
\]
so the degree-four divisor class \(K_C-2P\) carries a pencil. Removing any base divisor yields a \(k\)-morphism to \(\mathbb P^1\) of degree at most \(4\). The lower bound just proved forces degree exactly \(4\). This proves the assertion for every odd prime power \(q\).

## Verification
The accompanying standalone `verify.py` checks the integral factorization and exceptional-characteristic parameter values; checks the Segre polynomial identity; and uses exact modular Gröbner bases of the Jacobian-minor ideals in all four affine projective charts to exclude geometric singularities at primes \(3,5,7,13,17\) for sample nonsquare choices of \(c\). It also enumerates rational points and verifies the displayed rational point for those primes. These are finite cross-checks, **not** the proof for all odd prime powers; the universal proof is the branch-locus argument above.

For replay: install Python 3 with `sympy` and run `python verify.py`. No network access, previous computations, or external data files are required.

## Relationship to prior work
Faber, Grantham and Howe [1, Introduction, Question 1.3] ask whether curves of genus \(g\) and gonality exactly \(g\) exist over every finite field; their paragraph following Question 1.3 proposes the genus-four **nonsplit-quadric plus cubic** construction for odd \(q\) but does not exhibit a cubic working for all such fields. The equivalence between trigonal canonical genus-four curves and rulings of their canonical quadrics, and finite-field gonality bounds in the presence of rational points, are standard and are also developed in Faber–Grantham [2]. The present contribution is the explicit cubic and its uniform, characteristic-by-characteristic smoothness proof, giving the stated existence conclusion for **all odd prime powers**. No absolute novelty relative to unindexed later literature is asserted.

## Limitations
This result proves existence, not a classification or a point-count bound, and does not cover characteristic two or genus other than four. The source [2] was available via bibliographic abstract and via [1]'s precise citation of its Lemma 5.1, but its full text was not independently obtained. Other unindexed constructions may partially overlap. There has been no independent external audit or certification.

## References
1. X. Faber, J. Grantham, E. W. Howe, *On the Maximum Gonality of a Curve over a Finite Field*, arXiv:2207.14307, first posted 2022-07-28; Introduction, Question 1.3. https://arxiv.org/html/2207.14307v2
2. X. Faber, J. Grantham, *Ternary and Quaternary Curves of Small Fixed Genus and Gonality with Many Rational Points*, arXiv:2010.07992, first posted 2020-10-15; especially the nonsplit-quadric criterion cited as Lemma 5.1 in [1]. https://arxiv.org/abs/2010.07992
