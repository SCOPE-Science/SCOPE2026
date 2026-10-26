# A smooth nonsplit-quadric genus-four pencil in characteristic two

## Finding

Let \(k=\mathbb F_q\), where \(q=2^m\) and \(m\ge2\). Choose \(c\in k\) with absolute trace \(\operatorname{Tr}_{k/\mathbb F_2}(c)=1\). For each \(\kappa\in k\), define \(X_{c,\kappa}\subset\mathbb P^3_k\), with homogeneous coordinates \([x:y:z:w]\), by
\[
Q=xy+z^2+zw+cw^2=0,
\]
\[
F_\kappa=y^3+y^2w+w^3+xyw+xy^2+xw^2+(1+\kappa)x^3=0.
\]
Then \(X_{c,\kappa}\) is geometrically smooth if and only if \(\kappa\notin\{0,1\}\). For all such parameters it is geometrically connected and has genus \(4\), with canonical embedding given by these equations. It has no \(k\)-morphism of degree at most \(3\) to \(\mathbb P^1_k\).

Put \(f(T)=T^3+T^2+1\). Whenever \(t\in k\) satisfies \(f(t)\notin\{0,1\}\) and \(\kappa=f(t)^2\), the curve contains the rational point \([1:t^2:t:0]\) and has \(k\)-gonality exactly \(4\). Such a \(t\) exists for *every* \(q\ge4\) of characteristic two. Thus the formulas give an explicit genus-four curve of gonality four over every \(\mathbb F_{2^m}\) with \(m\ge2\).

The restriction \(m\ge2\) is sharp for this pencil: \(\mathbb F_2\) has no parameter \(\kappa\notin\{0,1\}\). The existence of genus-four, gonality-four curves over \(\mathbb F_2\) is previously known, via a different construction.

## Assumptions and scope

All smoothness and connectedness assertions are geometric (over an algebraic closure). The gonality is **over the displayed ground field**; the curves are geometrically trigonal after the quadric splits. The parameter choices are coefficient-marked, and no claim is made about pairwise isomorphism classes, rational-point maxima, or characteristic different from two.

The trace condition is equivalent to the irreducibility of \(T^2+T+c\) over \(k\), and hence to the nonsplit nature of the smooth quadric \(Q\).

## Proof

**1. Split the quadric and identify the cubic.** Choose a root \(\alpha\) of \(T^2+T+c\) in \(\mathbb F_{q^2}\), so \(\alpha^q=\alpha+1\). Put \(u=z+\alpha w\), \(v=z+\alpha^q w\); then \(uv=z^2+zw+cw^2\), \(u+v=w\), and \(Q=xy+uv\). Over \(\overline{k}\) choose Segre parameters
\[
x=s_0t_0,\quad y=s_1t_1,\quad u=s_0t_1,\quad v=s_1t_0.
\]
The restriction of the displayed cubic becomes
\[
F_\kappa|_Q=(s_1^3+s_1^2s_0+s_0^3)(t_1^3+t_1^2t_0+t_0^3)-\kappa(s_0t_0)^3.
\]
This identity follows by expanding and using \(u+v=w\), \(uv=xy\); `verify.py` checks it symbolically in characteristic two. The bidegree of the resulting divisor is \((3,3)\).

**2. Exact geometric smoothness boundary.** On the affine Segre chart \(s_0=t_0=1\), the equation is \(f(s)f(t)=\kappa\). Since the characteristic is two, \(f'(T)=T^2\). The two partial derivatives are \(s^2 f(t)\) and \(t^2 f(s)\). If \(\kappa\ne0\), both polynomial values are nonzero on the curve, so a singular affine point would force \(s=t=0\), and then \(\kappa=f(0)^2=1\). Conversely, \((s,t)=(0,0)\) is singular when \(\kappa=1\).

On the chart \(s=\infty\) the homogenized equation requires \(f(t)=0\), with \(t\ne\infty\). Every such root is simple because \(f(0)=1\) and \(f'(t)=t^2\). Thus the defining derivative along \(t\) is nonzero. The case \(t=\infty\) is symmetric, and \((\infty,\infty)\) is not on the curve. When \(\kappa=0\), the equation is the union of the vertical and horizontal divisors \(f(s)=0\) and \(f(t)=0\), meeting at points, and is singular. This proves the exact criterion.

**3. Connectedness, genus, and canonical embedding.** The divisor is of class \((3,3)\) on \(\mathbb P^1\times\mathbb P^1\). The exact sequence \(0\to\mathcal O(-3,-3)\to\mathcal O\to\mathcal O_X\to0\), together with \(H^1(\mathcal O(-3,-3))=0\), gives \(H^0(X,\mathcal O_X)=\overline{k}\), hence geometric connectedness. A smooth connected curve is integral. By adjunction, \(\omega_X\simeq\mathcal O_X(1,1)\); the canonical degree is \((1,1)\cdot(3,3)=6\), so the genus is \(4\). The degree-six canonical map is the given closed embedding in \(\mathbb P^3\).

**4. Exact ground-field gonality.** The complete-intersection ideal has a unique quadric generator, namely \(Q\). For a nonhyperelliptic canonically embedded genus-four curve, a degree-three pencil over the ground field induces a ground-field ruling on its unique quadric; see Faber–Grantham, Lemma 5.1. Because the norm-form quadric \(Q\) is nonsplit, it has no such ruling. The canonical embedding also excludes gonality \(1\) or \(2\). Therefore \(\operatorname{gon}_k(X)\ge4\).

If \(f(t)\notin\{0,1\}\), take \(\kappa=f(t)^2\); then \(\kappa\ne0,1\). Direct substitution gives \(Q(1,t^2,t,0)=0\) and \(F_\kappa(1,t^2,t,0)=f(t)^2+\kappa=0\). The rational point \(P\) implies a degree-at-most-four pencil: if \(K_X\) is canonical, Riemann–Roch yields \(\ell(K_X-2P)=1+\ell(2P)\ge2\), and \(\deg(K_X-2P)=4\). Removing any base divisor only lowers the degree. Thus \(\operatorname{gon}_k(X)\le4\), proving equality.

**5. All even fields of size at least four.** For \(q=4\), choose \(t\in\mathbb F_4\setminus\mathbb F_2\); then \(t^3=1\) and \(f(t)=t^2\notin\{0,1\}\). For \(q\ge8\), the polynomial \(f(T)(f(T)+1)\) has degree six, so at most six of the \(q\) elements violate the required condition. Every finite field of characteristic two admits a trace-one element \(c\). This completes the construction for every \(m\ge2\).

## Verification

`verify.py` is a standalone exact checker requiring Python 3 and SymPy. It verifies the polynomial identity on the Segre quadric over characteristic two. It implements explicit binary finite fields and checks a choice of trace-one \(c\), allowed \(t\), the rational-point certificate, and Jacobian rank of the quadric–cubic complete intersection at every rational point over \(\mathbb F_4\), \(\mathbb F_8\), \(\mathbb F_{16}\), and additionally all points over \(\mathbb F_{16}\) and \(\mathbb F_{64}\) for the respective models over \(\mathbb F_4\) and \(\mathbb F_8\). The exact geometric proof above, not finite testing, covers arbitrary algebraic extensions and every \(m\ge2\).

## Relationship to prior work

Faber, Grantham, and Howe posed the existence of genus-\(g\) curves with gonality \(g\) over each finite field (Question 1.3 in their 2022 preprint). They discussed non-split quadrics and proposed choosing suitable cubics in the genus-four odd-characteristic case; their text records previously known genus-four instances for \(q\le4\), without the displayed uniform even-characteristic cubic and smoothness criterion. Faber and Grantham (2020) give the geometric classification of the containing genus-four quadric (Lemma 5.1) and an explicit genus-four gonality-four example over \(\mathbb F_2\) (Theorem 5.3). The present contribution is the fully explicit characteristic-two \((2,3)\)-complete-intersection pencil, its sharp geometric smoothness boundary \(\kappa\notin\{0,1\}\), and its rational-point selection valid for every even \(q\ge4\).

## Limitations

The family has no allowable parameter over \(\mathbb F_2\), and the already known \(\mathbb F_2\) construction is not recovered from it. The theorem does not identify distinct arithmetic isomorphism classes, zeta functions, or exact point counts. It gives no claim of geometric gonality four: the curves become trigonal after splitting the quadric. The bibliographic comparison does not rule out an unindexed equivalent explicit construction.

## References

1. X. Faber, J. Grantham, E. W. Howe, *On the Maximum Gonality of a Curve over a Finite Field*, arXiv:2207.14307, first posted 2022-07-28. See Question 1.3 and the discussion following it. https://arxiv.org/abs/2207.14307
2. X. Faber, J. Grantham, *Binary Curves of Small Fixed Genus and Gonality with Many Rational Points*, arXiv:2005.07054, first posted 2020-05-14. See Lemma 5.1 and Theorem 5.3. https://arxiv.org/abs/2005.07054
