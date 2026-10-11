# Exact \(\Lambda(4)\) constants for every three-character subset of a cyclic group
## Finding
Let \(N\ge3\) and let \(A\subset\mathbb Z_N\) have three elements. For
\[
f(x)=\sum_{a\in A}c_a e^{2\pi i ax/N},
\]
where \(\mathbb Z_N\) has normalized counting measure, define
\[
\mathsf L_4(A)=\sup_{c\ne0}\frac{\|f\|_4}{(\sum_{a\in A}|c_a|^2)^{1/2}}.
\]
Then exactly one of the following five additive configurations applies, and
\[
\mathsf L_4(A)^4=
\begin{cases}
3,&A\text{ is a coset of the order-three subgroup},\\
7/3,&A=a+\{0,d,2d\}\text{ with }\operatorname{ord}(d)=4,\\
2,&A\text{ contains an antipodal pair and is not of the preceding type},\\
15/7,&A\text{ is a three-term arithmetic progression and is not of the first two types},\\
5/3,&\text{otherwise}.
\end{cases}
\]
Thus the sharp \(L^2\)-to-\(L^4\) growth of a three-character polynomial on a cyclic group has exactly five levels, caused respectively by order-three torsion, order-four torsion, an isolated order-two collision, one midpoint relation, or no pair-sum collision.

The equality cases are explicit. For an order-three coset \(A=a+\{0,d,2d\}\), equality holds exactly for
\[
c_{a+jd}=\lambda\omega^{kj}
\]
with \(\lambda\ne0\), \(k\in\{0,1,2\}\), and \(\omega^3=1\). For an order-four fragment \(A=a+\{0,d,2d\}\), equality holds exactly for
\[
c_{a+jd}=\lambda\eta^j,
\qquad \eta^4=1.
\]
For an isolated antipodal pair, equality holds exactly when the third coefficient is zero and the two antipodal coefficients are equal up to sign. For a nondegenerate progression \(A=\{a,a+d,a+2d\}\), equality holds exactly when
\[
|c_a|^2:|c_{a+d}|^2:|c_{a+2d}|^2=2:3:2
\]
and
\[
c_{a+d}^2\overline{c_a c_{a+2d}}>0.
\]
In the generic case, equality holds exactly when the three coefficient moduli are equal; their phases are arbitrary.

## Assumptions and scope
The group is the finite cyclic group \(\mathbb Z_N\) with \(N\ge3\). Frequencies are residues modulo \(N\), characters are \(x\mapsto e^{2\pi i ax/N}\), and all \(L^r\) norms use normalized counting measure. Coefficients may vanish; this matters in the isolated-antipodal case, whose optimum is already attained on the antipodal pair.

A three-term arithmetic progression means a set \(\{a,a+d,a+2d\}\) of three distinct residues. An antipodal pair is a pair whose difference is the unique element of order two, so it can occur only for even \(N\). The order-three and order-four cases are listed first because they are precisely the multiple-collision degeneracies of the ordinary midpoint and antipodal relations.

## Proof
By character orthogonality,
\[
\|f\|_4^4=\|f^2\|_2^2
=\sum_{s\in\mathbb Z_N}\left|\sum_{u+v=s}c_uc_v\right|^2,
\qquad
\|f\|_2^2=\sum_{a\in A}|c_a|^2.
\]
Translate the frequency set so that \(A=\{0,x,y\}\). The six unordered pair sums are
\[
0,\quad 2x,\quad 2y,\quad x,\quad y,\quad x+y.
\]
Because the three residues are distinct, every nontrivial collision among these six is one of
\[
x+y=0,\qquad 2x=y,\qquad 2y=x,
\]
or
\[
2x=0,\qquad 2y=0,\qquad 2x=2y.
\]
The first line consists of midpoint relations and the second of double-sum collisions. Two distinct midpoint relations force \(A\) to be an order-three coset. A midpoint relation together with a double-sum collision forces an order-four fragment. Two independent double-sum collisions cannot occur in a cyclic group because there is at most one nonzero element of order two. Hence the five cases in the statement exhaust all possibilities.

Normalize \(X+Y+Z=1\), where \(X,Y,Z\) are the squared coefficient moduli in a suitable ordering.

If there is no collision, orthogonality gives
\[
\|f\|_4^4=2-(X^2+Y^2+Z^2)\le\frac53,
\]
with equality exactly at \(X=Y=Z=1/3\).

Suppose there is exactly one midpoint relation, with \(Y\) the midpoint coefficient. The only phase-sensitive fiber gives
\[
\|f\|_4^4\le 2-(X^2+Y^2+Z^2)+4Y\sqrt{XZ}.
\]
For fixed \(Y\), put \(S=X+Z=1-Y\) and \(q=\sqrt{XZ}\le S/2\). The right-hand side is
\[
2-Y^2-S^2+2q^2+4Yq,
\]
which is increasing in \(q\). Thus \(X=Z=S/2\), and the remaining quadratic is
\[
\frac32+3Y-\frac72Y^2\le\frac{15}{7},
\]
with equality at \(Y=3/7\). Equality in the triangle step is exactly the displayed phase condition in the statement.

Suppose there is exactly one double-sum collision, coming from an antipodal pair. With \(Z\) the third coefficient and \(S=X+Y=1-Z\),
\[
\|f\|_4^4\le S^2+Z^2+4XY+4ZS
\le 2-Z^2\le2.
\]
Equality forces \(Z=0\), \(X=Y=1/2\), and alignment of the two colliding squares, which is exactly equality up to sign on the antipodal pair.

For an order-four fragment, order the coefficients along \(a,a+d,a+2d\). Both collision fibers can be phase-aligned simultaneously. Writing \(S=X+Z=1-Y\) and \(q=\sqrt{XZ}\le S/2\),
\[
\|f\|_4^4\le S^2+(Y+2q)^2+4YS.
\]
Again this is increasing in \(q\), so \(X=Z=S/2\), and
\[
\|f\|_4^4\le 2+2Y-3Y^2\le\frac73.
\]
Equality occurs at \(X=Y=Z=1/3\); simultaneous phase alignment is equivalent to the geometric phase progression \(c_{a+jd}=\lambda\eta^j\) with \(\eta^4=1\).

Finally, if \(A\) is an order-three coset, multiplication by a common character reduces the problem to all functions on the three-point quotient. On a three-point probability space,
\[
\|g\|_4\le3^{1/4}\|g\|_2,
\]
with equality exactly for a point mass. Fourier inversion translates those point masses to the stated equal-modulus geometric coefficient phases. This proves both the constants and every equality case.

## Verification
The accompanying checker enumerates every three-element subset of \(\mathbb Z_N\) for \(3\le N\le80\), verifies that its unordered pair-sum collision pattern falls into exactly one of the five proved types, and directly evaluates an extremizing coefficient vector for each encountered type. It reports

`VERIFY_OK N=3..80 triples=1663740 counts={'order3': 351, 'order4': 840, 'antipodal': 41800, 'ap': 82607, 'generic': 1538142} targets={'order3': '3', 'order4': '7/3', 'antipodal': '2', 'ap': '15/7', 'generic': '5/3'}`.

This finite replay is a stress test only. The proof above is uniform in \(N\) and does not depend on enumeration.

## Relationship to prior work
Neuwirth's work on trigonometric trinomials gives a complete three-frequency extremal theory for the supremum norm and an exact Sidon constant, while his earlier work on metric unconditionality emphasizes that even \(L^p\) norms are polynomial expressions controlled by arithmetic relations among frequencies. Those sources motivate asking for an exact three-frequency \(\Lambda(4)\) classification, but the inspected statements concern supremum-norm/Sidon constants, unconditionality, or asymptotic arithmetic criteria rather than the five sharp finite-cyclic \(L^4/L^2\) constants above.

A previously available sharp fourth-moment result for a single repeated pair-sum in odd-order finite abelian groups implies the nondegenerate arithmetic-progression value \(15/7\) as one special regime. It does not cover the order-two, order-three, or order-four torsion patterns, nor does it classify all three-element cyclic frequency sets. The present classification includes that already-known regime only as one row in the complete cyclic taxonomy.

## Limitations
The theorem is specific to three frequencies and the fourth moment. At four or more frequencies, pair-sum collision hypergraphs can have many interacting fibers, so the five-case reduction no longer applies. The result also does not claim an analogous finite classification for non-even exponents. A residual literature risk remains that the small-cardinality \(\Lambda(4)\) optimization may have appeared implicitly in older thin-set or additive-energy literature under different terminology.

## References
1. Stefan Neuwirth, *Metric unconditionality and Fourier analysis*, arXiv:math/9707211, first public 1997-07-28; Studia Mathematica 131 (1998), 19–62.
2. Stefan Neuwirth, *The Sidon constant of sets with three elements*, arXiv:math/0102145, first public 2001-02-19.
3. Stefan Neuwirth, *The maximum modulus of a trigonometric trinomial*, HAL hal-00135804, version 1 public 2007-03-08; primary classification includes 42A05.
