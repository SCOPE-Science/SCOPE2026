# The positive-equilibrium global-attractivity criterion is vacuous

## Finding

Theorem 7 of the modified discrete Leslie–Gower predator–prey model states that the positive equilibrium is globally attractive if
\[
(1+kU_1^y)(d+bU_1^y)<r_0\le d+1
\]
and
\[
\frac{1+a}{b}<h\le1,
\]
where
\[
U_1^x=\frac{r_0-d}{a}+\varepsilon,
\qquad
U_1^y=h(m+U_1^x)+\varepsilon.
\]

For positive model parameters, these two hypotheses cannot hold simultaneously. The theorem therefore has an empty parameter regime and supplies no actual sufficient condition for global attractivity.

## Assumptions and scope

All model parameters appearing in the theorem are positive, as in the source. The auxiliary quantity \(\varepsilon\) is positive; the contradiction also survives in the formal limit \(\varepsilon\downarrow0\).

The result concerns Theorem 7 exactly as printed. It does not assert that the positive equilibrium is never globally attractive, nor does it replace the theorem with a new global-attractivity criterion.

The source's numerical example is not used to prove the contradiction. It is relevant only because the article itself observes that the example fails the theorem's conditions and characterizes those conditions as overly restrictive.

## Proof

Since
\[
1+kU_1^y>1,
\]
the first theorem inequality implies
\[
d+bU_1^y<r_0.
\]
Therefore
\[
r_0-d>bU_1^y>0.
\]
In particular,
\[
r_0-d>0.
\]

Now substitute the theorem's definitions:
\[
U_1^y
=
h\left(m+\frac{r_0-d}{a}+\varepsilon\right)+\varepsilon.
\]
Multiplying by \(b\) and subtracting \(r_0-d\) gives the exact identity
\[
bU_1^y-(r_0-d)
=
bhm
+
\frac{bh-a}{a}(r_0-d)
+
b(h+1)\varepsilon.
\]

The second theorem condition yields
\[
bh>1+a>a,
\]
so
\[
bh-a>0.
\]
Together with
\[
m>0,
\qquad
r_0-d>0,
\qquad
\varepsilon>0,
\]
every term on the right-hand side is positive. Hence
\[
bU_1^y-(r_0-d)>0,
\]
or equivalently
\[
bU_1^y>r_0-d.
\]
This contradicts the consequence
\[
bU_1^y<r_0-d
\]
of the first theorem hypothesis.

Thus the theorem's hypotheses are mutually inconsistent.

## Verification

The bundled `verify.py` symbolically expands the theorem definitions and verifies the identity
\[
bU_1^y-(r_0-d)
=
bhm+
\frac{bh-a}{a}(r_0-d)+
b(h+1)\varepsilon.
\]

It also constructs the sign certificate obtained after introducing the positive quantities
\[
D=r_0-d,
\qquad
P=bh-a.
\]
Under the theorem's consequences \(D>0\) and \(P>0\), the difference is a sum of strictly positive terms.

No numerical search or finite parameter enumeration is used to establish the contradiction.

## Relationship to prior work

The motivating paper develops local stability, bifurcation, permanence, and a global-attractivity theorem for a discrete Leslie–Gower predator–prey model with fear effect. Its numerical section explicitly notes that the displayed example does not meet Theorem 7 and says that the sufficient conditions are too strict. The present calculation identifies the stronger structural reason: those conditions define the empty set.

A closely related earlier discrete fear-effect predator–prey model also proves global stability results by comparison and iteration methods, but its equations and sufficient inequalities differ. That predecessor does not imply the incompatibility of the later theorem's \(U_1^x\) and \(U_1^y\) conditions.

Exact-title, DOI, theorem-number, global-attractivity, contradiction, correction, and erratum searches did not locate a published correction stating that Theorem 7's admissible region is empty.

## Limitations

The result does not decide the true global-attractivity region of the positive equilibrium.

A typographical change to one of the theorem inequalities could in principle produce a nonempty sufficient region, but no such replacement is inferred here.

An unindexed author correction could exist outside the checked records.

## References

1. S. Lin, F. Chen, Z. Li, L. Chen, “Complex Dynamic Behaviors of a Modified Discrete Leslie–Gower Predator–Prey System with Fear Effect on Prey Species,” Axioms 11 (2022), 520. DOI: 10.3390/axioms11100520.
2. F. Chen et al., “The Influence of Fear Effect to a Discrete-Time Predator-Prey System with Predator Has Other Food Resource,” Mathematics 9 (2021), 865. DOI: 10.3390/math9080865.
