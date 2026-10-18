# Exactly two conjugate trigonal pencils on a tetragonal singular genus-four curve

## Finding
Let \(k=\mathbb F_3\), and let \(Y/k\) be the smooth projective normalization of
\[
 y^2=x^5-x^3-1.
\]
Let \(\alpha\in\mathbb F_9\) satisfy \(\alpha^2-\alpha-1=0\). Define
\(a=(\alpha,1)\), \(b=(\alpha^3,1)\),
\(a^-=(\alpha,-1)\), and \(b^-=(\alpha^3,-1)\).
Let \(C/k\) be the projective integral curve obtained by identifying \(a\) with
\(b\), and \(a^-\) with \(b^-\), in two ordinary nonsplit nodes. This is the
curve constructed in Example 4.13 of Hilario--Salomão--Vidal Martins. Its
geometric genus is \(2\) and arithmetic genus is \(4\).

The scheme of degree-three pencils (complete base-point-free linear series
\(g^1_3\)) on \(C_{\overline{k}}\) consists of **exactly two reduced geometric
points**. They are defined over \(\mathbb F_9\), exchanged by
\(\operatorname{Gal}(\mathbb F_9/\mathbb F_3)\), and represented on \(Y\) by
\[
 f_c=\frac{y-c}{x(x-1)},\qquad
 f_{-c}=\frac{y+c}{x(x-1)},\qquad c^2=-1.
\]
Both descend to finite degree-three morphisms \(C_{\mathbb F_9}\to\mathbb P^1\).
There is no degree-three pencil over \(\mathbb F_3\). Accordingly, for the
rank-one torsion-free pencil definition of gonality used in the originating
paper,
\[
 \operatorname{gon}_{\mathbb F_3}(C)=4,
 \qquad \operatorname{gon}_{\mathbb F_9}(C)
 =\operatorname{gon}_{\overline{\mathbb F}_3}(C)=3.
\]
Thus the least extension degree on which a trigonal pencil exists is exactly
\(2\), and the obstruction is Galois descent of a two-element pencil scheme.

## Assumptions and scope
All schemes and morphisms are over fields of characteristic \(3\), and all
pencils are taken up to projective coordinate changes on their target. The
ordinary nodes of \(C\) are specifically the pushout identifications written
above. A degree-three pencil on the singular curve means a rank-one
base-point-free pencil with total degree three; its pullback to \(Y\) is
measured with the local node corrections from the fractional-ideal definition.
When the local corrections vanish, it is an invertible pencil and determines
a degree-three morphism. The assertion classifies these pencils, not all
higher-degree maps.

## Proof
**The normalization and nodes.** The derivative of \(F(x)=x^5-x^3-1\)
in characteristic \(3\) is \(2x^4\), and \(F(0)=-1\ne0\); hence \(F\) is
squarefree and \(Y\) is a smooth genus-two hyperelliptic curve. The polynomial
\(x^2-x-1\) is irreducible over \(\mathbb F_3\), with conjugate roots
\(\alpha\) and \(\alpha^3=1-\alpha\). The relations
\(F(\alpha)=F(\alpha^3)=1\) exhibit the four named points of \(Y\).
Gluing each indicated pair creates one geometric ordinary node and is
Frobenius-stable. The genus formula yields \(p_a(C)=2+2=4\).

**Construction over the quadratic extension.** Fix \(c\in\mathbb F_9\) with
\(c^2=-1\); such an element exists and does not lie in \(\mathbb F_3\).
Since \(\alpha^2-\alpha=1\) and \((\alpha^3)^2-\alpha^3=1\), the denominator \(x(x-1)\) evaluates to
\(1\) on the two branches of each node. Accordingly \(f_c\) has the common
value \(1-c\) on \(a,b\) and the common value \(-1-c\) on \(a^-,b^-\).
The local ring of an ordinary node is the subring of its normalized pair of
branches consisting of functions with equal finite residues. Thus \(f_c\)
is regular at both nodes and descends to a rational function on \(C\)
regular there.

To determine its degree, observe the exact factorization
\[
 F(x)-c^2=x^5-x^3=x^3(x-1)(x+1).
\]
At \(x=0\) and \(x=1\), the two points over each value have coordinates
\(y=\pm c\). At \(y=c\), the numerator \(y-c\) vanishes to orders
\(3\) and \(1\), respectively, because
\((y-c)(y+c)=F(x)-c^2\) and \(y+c\ne0\) there.
At \(y=-c\) the numerator is nonzero; the denominator has a simple zero
at both values of \(x\). At the unique point \(\infty\) of \(Y\),
\(x\) and \(y\) have pole orders \(2\) and \(5\), so \(f_c\) has pole
order \(5-4=1\). Therefore
\[
 (f_c)_\infty=\infty+(0,-c)+(1,-c),
 \qquad \deg(f_c)_\infty=3.
\]
There are no other poles. Since the three poles are nonsingular points of
\(C\), the descended function defines a finite morphism of degree \(3\)
from \(C_{\mathbb F_9}\) to \(\mathbb P^1\). Replacing \(c\) with
\(-c\) gives the other morphism, with pole divisor
\(\infty+(0,c)+(1,c)\). Frobenius sends \(c\) to
\(c^3=-c\), so it interchanges the two pencils.

**Upper bound of two pencils.** Work over \(\overline{k}\). A degree-two
nonconstant rational function on \(Y\) is a fractional linear function of
\(x\), by uniqueness of the hyperelliptic \(g^1_2\). It separates the two
branches \(a,b\) (which have distinct \(x\)-coordinates) and likewise
\(a^-,b^-\). In the degree formula for a rank-one pencil on a nodal curve,
each of those two node mismatches contributes one, after choosing a
projective coordinate on the pencil finite on all four branches. Thus a
normalization-degree-two pencil has total degree \(2+1+1=4\), and no
pencil of degree at most \(2\) exists on \(C_{\overline{k}}\).
Nor can a total-degree-three pencil arise from normalization degree two.
Every total-degree-three pencil therefore pulls back to a degree-three
base-point-free \(g^1_3\) on \(Y\) with zero node corrections, so its
morphism takes the same value on each glued pair.

Let \(A=a+b\) and \(B=a^-+b^-\), as effective degree-two divisors on
\(Y_{\overline{k}}\). For such a degree-three morphism, a fibre containing
\(a,b\) is \(A+R\) for some \(R\in Y\), and a fibre containing
\(a^-,b^-\) is \(B+S\) for some \(S\in Y\). Consequently the degree-three
pencil class lies in
\[
 T_A\cap T_B\subset\operatorname{Pic}^3(Y),\qquad
 T_A=\{[A+R]:R\in Y\},\quad T_B=\{[B+S]:S\in Y\}.
\]
These are translates of the theta curve on the principally polarized
Jacobian surface of \(Y\), each of self-intersection \(2\). They are
distinct: if \(A\sim B\), then the degree-two divisor \(A\) would move
in a nontrivial pencil and hence be a hyperelliptic fibre; but its points
have distinct \(x\)-coordinates. Therefore their intersection is proper
and has length \(T_A\cdot T_B=2\).

Both explicit functions yield points in this intersection. They are
**different**: if their complete pencils agreed, then
\(f_{-c}=M\circ f_c\) for some \(M\in\operatorname{PGL}_2(\overline{k})\).
Both functions have a pole at \(\infty\), forcing \(M(\infty)=\infty\),
so \(M\) is affine; it would preserve the entire pole divisor. But the two
pole divisors have different points above \(x=0\) and \(x=1\). Thus
there are two distinct points in a proper intersection of total length
\(2\); each has intersection multiplicity \(1\), and there are no further
geometric trigonal pencils.

**Descent and the lower field.** Frobenius exchanges these two reduced
points, so neither pencil is \(\mathbb F_3\)-rational and no degree-three
pencil descends. The rational function \(x\) on \(Y\) has degree \(2\),
but its values disagree across both glued pairs, producing a torsion-free
pencil of total degree \(2+1+1=4\) on \(C/\mathbb F_3\). Combining this
upper bound with the exclusion of degrees below \(4\) proves the asserted
arithmetic gonality and the minimal splitting extension.

## Verification
The standalone `verify.py` uses only Python's standard library and
checks the defining finite-field relations, irreducibility of the quadratic,
absence of affine \(\mathbb F_3\)-points, the exact factorization controlling
the poles, the node residue equalities, and the Frobenius exchange. It
reports `VERIFY_OK` when all assertions pass. These finite calculations
support the algebraic argument; the two-pencils classification follows
from theta intersection theory and the explicit distinct witnesses, not
from numerical sampling.

## Relationship to prior work
Hilario, Salomão, and Vidal Martins construct this curve and prove in
Example 4.13 that its gonality over \(\mathbb F_3\) is \(4\). Their
Theorem 4.11 supplies a criterion for trigonality over a specified ground
field. The present result identifies the exact geometric pencil scheme,
constructs both degree-three maps after quadratic base change, and
computes the least field of definition. The fact that a generic genus-four
canonical curve has at most two trigonal pencils is classical; the new
arithmetic content is the explicit two-node curve's sharp Galois descent
behaviour and exact maps.

## Limitations
The theorem is for the specified projective curve and its indicated two
non-split nodes. The classification concerns degree-three pencils and
does not classify all maps of higher degree, automorphisms of the curve,
or analogous constructions for every hyperelliptic normalization.
The two explicit maps are defined over \(\mathbb F_9\) and need not be
unique as rational expressions, only as pencils up to target automorphism.
No independent mathematical audit has been performed.

## References
1. C. Hilario, R. Salomão, R. Vidal Martins, *Maximal singular curves over finite fields from elliptic and hyperelliptic curves*, arXiv:2609.22557v1 (18 September 2026), especially Theorem 3.3, Theorem 4.11 and Example 4.13. Accessible revised text: arXiv:2609.22557v2.
2. X. Faber, J. Grantham, E. W. Howe, *On the Maximum Gonality of a Curve over a Finite Field*, arXiv:2207.14307 (smooth-curve context; not a result for this singular curve).
3. Standard genus-two Jacobian theta intersection: for the principal polarization \(\Theta\) on an abelian surface, \(\Theta^2=2\); see the classical Riemann--Roch theorem for abelian varieties.
