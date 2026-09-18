# Full Morita corners split support tau-tilting gluing into joins and meets

## Statement

Let \(k\) be a field and let
\[
\Lambda=
\begin{pmatrix}
A&N\\
M&B
\end{pmatrix}_{\phi,\psi}
\]
be a finite-dimensional Morita context algebra, with complementary diagonal idempotents
\(e\) and \(f=1-e\). Assume both corners are full:
\[
\Lambda e\Lambda=\Lambda=\Lambda f\Lambda.
\]
Equivalently, this is the strict Morita-context regime. Put
\[
A=e\Lambda e,\qquad B=f\Lambda f,\qquad
M=f\Lambda e,\qquad N=e\Lambda f.
\]
Then
\[
\Theta=-\otimes_B M:\operatorname{mod}B\longrightarrow\operatorname{mod}A,
\qquad
\Psi=-\otimes_A N:\operatorname{mod}A\longrightarrow\operatorname{mod}B
\]
are mutually quasi-inverse Morita equivalences.

For
\[
X\in \mathrm{s}\tau\text{-}\mathrm{tilt}A,\qquad
Y\in \mathrm{s}\tau\text{-}\mathrm{tilt}B,
\]
write
\[
\mathcal U=\operatorname{Fac}_A X,\qquad
\mathcal V=\Theta(\operatorname{Fac}_B Y)
          =\operatorname{Fac}_A\Theta(Y).
\]
Let
\[
F_A=-\otimes_A e\Lambda,\qquad F_B=-\otimes_B f\Lambda
\]
be the corner-induction functors, and let
\[
\mathcal T_{X,Y}
=
\{W\in\operatorname{mod}\Lambda:
We\in\operatorname{Fac}_A X,\ 
Wf\in\operatorname{Fac}_B Y\}
\]
be the componentwise torsion class used in the recent bilateral-gluing construction.

Then restriction along the full corner,
\[
R_e=(-)e:\operatorname{mod}\Lambda\longrightarrow\operatorname{mod}A,
\]
identifies the two natural gluing operations as follows:
\[
\boxed{R_e(\mathcal T_{X,Y})=\mathcal U\cap\mathcal V.}
\]

Moreover
\[
R_e(F_A X\oplus F_B Y)\cong X\oplus\Theta(Y),
\]
and hence
\[
R_e\!\left(\operatorname{Fac}_\Lambda(F_A X\oplus F_B Y)\right)
=
\operatorname{Fac}_A(X\oplus\Theta(Y)).
\]
Whenever \(F_A X\oplus F_B Y\) is support \(\tau\)-tilting, this latter torsion class is exactly the join
\[
\boxed{\mathcal U\vee\mathcal V}
\]
in the lattice of all torsion classes; because it is then functorially finite, it is also the join inside the poset of functorially finite torsion classes.

Thus in the strict/full-corner regime the prescribed componentwise gluing is a **meet phenomenon**, while direct corner induction, when support \(\tau\)-tilting, is a **join phenomenon**.

There are three exact consequences.

1. The componentwise class is functorially finite precisely when the transported intersection is:
   \[
   \boxed{
   \mathcal T_{X,Y}\text{ is functorially finite}
   \iff
   \mathcal U\cap\mathcal V\text{ is functorially finite}.
   }
   \]
   When this holds, the desired glued support \(\tau\)-tilting module is, up to basicization,
   \[
   F_A P(\mathcal U\cap\mathcal V),
   \]
   where \(P(-)\) denotes the Ext-projective generator.

2. The two cross-membership conditions
   \[
   Y\otimes_B M\in\operatorname{Fac}_A X,
   \qquad
   X\otimes_A N\in\operatorname{Fac}_B Y
   \]
   are equivalent in the strict regime to the single equality
   \[
   \boxed{\mathcal U=\mathcal V.}
   \]

3. Consequently
   \[
   \boxed{
   \operatorname{Fac}_\Lambda(F_A X\oplus F_B Y)
   =\mathcal T_{X,Y}
   \iff
   \mathcal U=\mathcal V.
   }
   \]
   In this equality case the directly induced module is automatically support \(\tau\)-tilting. Outside it, direct induction may still be support \(\tau\)-tilting, but it cannot have the prescribed componentwise torsion class.

## Proof

Because \(e\) is full, \(e\Lambda\) is a progenerator and
\[
R_e=(-)e:\operatorname{mod}\Lambda\to\operatorname{mod}A
\]
is a Morita equivalence with quasi-inverse \(F_A=-\otimes_Ae\Lambda\). Similarly \(R_f=(-)f\) is a Morita equivalence with quasi-inverse \(F_B\). Restricting the standard counit isomorphism
\[
(We)\otimes_A e\Lambda\xrightarrow{\sim}W
\]
to the \(f\)-corner yields
\[
Wf\cong (We)\otimes_A e\Lambda f=(We)\otimes_A N=\Psi(We).
\]
Likewise,
\[
\Theta(Wf)=(Wf)\otimes_BM\cong We.
\]
In particular \(\Theta\) and \(\Psi\) are mutually quasi-inverse exact equivalences.

For \(W\in\operatorname{mod}\Lambda\),
\[
W\in\mathcal T_{X,Y}
\]
is equivalent to
\[
We\in\mathcal U
\quad\text{and}\quad
Wf\in\operatorname{Fac}_B Y.
\]
Applying \(\Theta\) to the second condition and using \(\Theta(Wf)\cong We\), this becomes
\[
We\in\mathcal U\cap\Theta(\operatorname{Fac}_B Y)
=\mathcal U\cap\mathcal V.
\]
Hence \(R_e(\mathcal T_{X,Y})=\mathcal U\cap\mathcal V\). Exact equivalences preserve functorial finiteness, proving the first criterion. If the intersection is functorially finite, the Adachi--Iyama--Reiten correspondence gives its unique basic support \(\tau\)-tilting generator \(P(\mathcal U\cap\mathcal V)\), and transporting it back by \(F_A\) gives the stated glued module.

Next,
\[
R_e(F_A X)\cong X,
\]
while
\[
R_e(F_B Y)
=(Y\otimes_Bf\Lambda)e
\cong Y\otimes_Bf\Lambda e
=Y\otimes_BM
=\Theta(Y).
\]
Therefore
\[
R_e(F_A X\oplus F_B Y)\cong X\oplus\Theta(Y).
\]
Since a Morita equivalence preserves finite sums, quotients, and direct summands,
\[
R_e(\operatorname{Fac}_\Lambda(F_A X\oplus F_B Y))
=
\operatorname{Fac}_A(X\oplus\Theta(Y)).
\]
If the induced module is support \(\tau\)-tilting, the right-hand side is a torsion class. It contains both \(\mathcal U\) and \(\mathcal V\), and every torsion class containing \(\mathcal U\) and \(\mathcal V\) contains \(X\oplus\Theta(Y)\) and hence its factor closure. It is therefore the join \(\mathcal U\vee\mathcal V\).

For the cross conditions, note first that
\[
Y\otimes_BM=\Theta(Y)\in\mathcal U
\iff
\mathcal V=\operatorname{Fac}_A\Theta(Y)\subseteq\mathcal U.
\]
Similarly,
\[
X\otimes_AN=\Psi(X)\in\operatorname{Fac}_B Y.
\]
Applying \(\Theta\) and using \(\Theta\Psi\cong\mathrm{Id}\) gives
\[
X\in\mathcal V
\iff
\mathcal U\subseteq\mathcal V.
\]
Thus the two cross conditions hold exactly when \(\mathcal U=\mathcal V\).

Finally, suppose
\[
\operatorname{Fac}_\Lambda(F_AX\oplus F_BY)=\mathcal T_{X,Y}.
\]
Transporting to \(A\) gives
\[
\operatorname{Fac}_A(X\oplus\Theta Y)=\mathcal U\cap\mathcal V.
\]
But the left side contains both \(\mathcal U\) and \(\mathcal V\), so necessarily
\(\mathcal U=\mathcal V\). Conversely, if \(\mathcal U=\mathcal V\), then \(X\) and
\(\Theta Y\) are the two basic support \(\tau\)-tilting representatives of the same
functorially finite torsion class. By the support \(\tau\)-tilting--torsion
bijection they are isomorphic up to basic representative. Hence
\(X\oplus\Theta Y\) basicizes to \(P(\mathcal U)\), so \(F_AX\oplus F_BY\) is
support \(\tau\)-tilting and both displayed classes equal \(\mathcal U\).

## A sharp semisimple family

Let
\[
C=k^n,\qquad \Lambda=M_2(C),
\]
with the two standard diagonal idempotents. Then \(A=B=C\), the corner equivalence
\(\Theta\) is the identity, and basic support \(\tau\)-tilting \(C\)-modules are indexed by subsets
\(I\subseteq[n]\):
\[
X_I=\bigoplus_{i\in I}S_i,\qquad
\operatorname{Fac}_C X_I
=
\{\text{modules supported on }I\}.
\]

For every ordered pair \((I,J)\),
\[
X_I\oplus X_J
\]
basicizes to \(X_{I\cup J}\), hence the directly induced \(\Lambda\)-module is support
\(\tau\)-tilting. Under the Morita equivalence its generated torsion class is the union class
\(I\cup J\), whereas the prescribed componentwise class is the intersection class
\(I\cap J\). They coincide exactly when \(I=J\).

Therefore, among the
\[
4^n
\]
ordered pairs of corner support \(\tau\)-tilting modules, **every one** gives a support
\(\tau\)-tilting direct induction, but only
\[
2^n
\]
of them satisfy the bilateral cross conditions and realize the prescribed componentwise
torsion class. The compatible proportion is exactly
\[
\boxed{2^{-n}}.
\]
The \(n=1\) case contains the matrix-algebra counterexample in arXiv:2609.18746; the
family shows that the failure of the converse outside the radical-valued regime can grow
exponentially rather than being an isolated small example.

## Literature context and limitations

Zhang, arXiv:2609.18746v1, introduces the bilateral componentwise class
\(\mathcal T_{X,Y}\), proves that the two cross-membership conditions are sufficient
for direct corner induction for arbitrary connecting maps, and proves their necessity
under radical-valued connecting maps. The paper also contains matrix-algebra examples
showing that the converse can fail outside that hypothesis and that in a strict
\(M_2(C)\) context the componentwise class can encode an intersection which need not
be functorially finite. Those observations are prior work and are not claimed here.

The new claim is the general full-corner theorem above: in every strict finite-dimensional
Morita context, the two constructions transport canonically to meet and join operations
in a single corner; the bilateral cross conditions become exactly equality of the two
transported torsion classes; and the full semisimple matrix family gives the exact
\(4^n\) versus \(2^n\) gap.

The Morita-equivalence ingredients themselves are classical. Green--Psaroudakis
(arXiv:1303.2083) give the corner functors for finite-dimensional Morita-context
algebras. Kashu's 2003 paper on Morita contexts proves order-preserving correspondences
between appropriate lattices of torsion theories, which in the strict case is compatible
with the classical equivalence of module categories. Adachi--Iyama--Reiten
(arXiv:1210.1036) provide the support \(\tau\)-tilting/functorially-finite-torsion
bijection used above.

Originality is asserted only to the best of our knowledge. Targeted searches for strict
Morita contexts together with support \(\tau\)-tilting, functorially finite torsion
classes, direct induction, and join/meet formulations did not locate the theorem above.
The most plausible residual coverage risk is older Morita/torsion-theory literature:
Kashu's broader papers on torsion theories and localizations in Morita contexts establish
general lattice correspondences, and not every older source in that literature was
inspected theorem-by-theorem. No located source combined those results with support
\(\tau\)-tilting direct induction or stated the join-versus-meet criterion or the
semisimple exponential gap.

## References

1. Y. Zhang, *Support \(\tau\)-tilting modules over Morita context algebras: A bilateral approximation approach*, arXiv:2609.18746v1 (2026), https://arxiv.org/abs/2609.18746.
2. T. Adachi, O. Iyama, I. Reiten, *\(\tau\)-tilting theory*, Compos. Math. 150 (2014), 415--452, arXiv:1210.1036, https://arxiv.org/abs/1210.1036.
3. E. L. Green, C. Psaroudakis, *On Artin algebras arising from Morita contexts*, Algebr. Represent. Theory 17 (2014), 1485--1525, arXiv:1303.2083, https://arxiv.org/abs/1303.2083.
4. A. I. Kashu, *On equivalence of some subcategories of modules in Morita contexts*, Algebra Discrete Math. 3 (2003), 46--53, https://admjournal.luguniv.edu.ua/index.php/adm/article/view/963.
