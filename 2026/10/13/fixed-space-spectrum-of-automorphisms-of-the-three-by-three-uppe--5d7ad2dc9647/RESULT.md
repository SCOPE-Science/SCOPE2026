# Fixed-space spectrum of automorphisms of the three-by-three upper triangular algebra
## Finding
Let \(q\) be a prime power and let \(T=T_3(\mathbb F_q)\). For \(d\in\{3,4,5,6\}\), write \(N_d(q)\) for the number of \(\mathbb F_q\)-algebra automorphisms of \(T\) whose fixed subspace has dimension \(d\). Then
\[
N_6(q)=1,\qquad N_5(q)=q-1,\qquad N_4(q)=q(3q^2-4q-2),
\]
and
\[
N_3(q)=q^5-2q^4-2q^3+4q^2+q.
\]
No other fixed-space dimension occurs. Hence the action of the invertible upper triangular group on \(T\) by conjugation has exactly
\[
q^3+3q^2+q
\]
orbits.

## Assumptions and scope
The field is an arbitrary finite field \(\mathbb F_q\); no restriction on the characteristic is imposed. Automorphisms are \(\mathbb F_q\)-algebra automorphisms. Upper-triangular similarity means conjugacy by the group \(B=T^\times\) of invertible upper triangular matrices.

A classical theorem of Kezlan, as summarized and generalized by Jøndrup, states that every algebra automorphism of an upper triangular matrix algebra over a commutative coefficient ring is inner in the field case. Thus every automorphism considered here has the form \(X\mapsto UXU^{-1}\) with \(U\in B\). Two such matrices induce the same automorphism exactly when their quotient is a central unit, so
\[
\operatorname{Aut}_{\mathbb F_q}(T)\cong B/(\mathbb F_q^\times I),
\qquad
|\operatorname{Aut}_{\mathbb F_q}(T)|=q^3(q-1)^2.
\]

## Proof
Write
\[
U=\begin{pmatrix}a&x&y\\0&b&z\\0&0&c\end{pmatrix}\in B,
\qquad
X=\begin{pmatrix}r&p&s\\0&t&u\\0&0&v\end{pmatrix}\in T,
\]
where \(a,b,c\ne0\). The fixed subspace of the automorphism induced by \(U\) is the centralizer \(C_T(U)\). Expanding \(UX=XU\) gives the three equations
\[
(a-b)p+x(t-r)=0,
\]
\[
(b-c)u+z(v-t)=0,
\]
and
\[
(a-c)s+xu+y(v-r)-pz=0.
\]
With variables ordered as \((r,t,v,p,u,s)\), the coefficient matrix is
\[
M(U)=
\begin{pmatrix}
-x&x&0&a-b&0&0\\
0&-z&z&0&b-c&0\\
-y&0&y&-z&x&a-c
\end{pmatrix}.
\]
Therefore
\[
\dim C_T(U)=6-\operatorname{rank}M(U).
\]

The rank can be classified completely from the three diagonal-equality patterns.

If \(a,b,c\) are all distinct, the columns belonging to \(p,u,s\) give three nonzero pivots, so the rank is \(3\). If exactly two diagonal entries are equal, the rank is \(2\) only in the following cases; otherwise it is \(3\):

* when \(a=b\ne c\), exactly when \(x=0\);
* when \(b=c\ne a\), exactly when \(z=0\);
* when \(a=c\ne b\), exactly when \(y=-xz/(a-b)\).

If \(a=b=c\), the rank is \(0\) exactly for \(x=y=z=0\); it is \(1\) exactly for \(x=z=0\) and \(y\ne0\); it is \(2\) exactly when precisely one of \(x,z\) is nonzero; and it is \(3\) when both \(x\) and \(z\) are nonzero.

Counting matrices \(U\in B\) in each rank stratum gives
\[
R_0=q-1,
\qquad
R_1=(q-1)^2,
\]
and
\[
R_2=2q(q-1)^2+3q^2(q-1)(q-2)
=q(q-1)(3q^2-4q-2).
\]
The remaining matrices have rank \(3\). Division by the \(q-1\) central scalar units gives the claimed automorphism multiplicities
\[
N_6=1,
\quad
N_5=q-1,
\quad
N_4=q(3q^2-4q-2),
\]
and, by subtraction from \(q^3(q-1)^2\),
\[
N_3=q^5-2q^4-2q^3+4q^2+q.
\]

Finally Burnside's lemma applied to the automorphism action on the \(q^6\)-element set \(T\) gives
\[
\#(T/\operatorname{Aut}(T))
=
\frac{N_6q^6+N_5q^5+N_4q^4+N_3q^3}{q^3(q-1)^2}
=q^3+3q^2+q.
\]
Because the kernel of the conjugation action of \(B\) is precisely the scalar subgroup, the same number is the number of \(B\)-conjugacy orbits in \(T\).

## Verification
The standalone script `artifacts/verify.py` independently enumerates every invertible upper triangular \(U\) and computes the rank of the displayed commutator coefficient matrix for \(q=2,3,5,7,11\). It recovers the four multiplicity formulas exactly. For \(q=2,3\) it also constructs the actual conjugation orbits on all elements of \(T\) and verifies the orbit count \(q^3+3q^2+q\). The replay output is stored in `artifacts/verification_output.txt`.

These finite checks are consistency tests only. The proof above establishes the statement for every prime power because it uses only field arithmetic, equality patterns, linear rank, and exact finite counting.

## Relationship to prior work
Ánh and van Wyk study automorphism groups of generalized triangular matrix rings; their article was available online on 11 November 2010 and lists AMS classification 16S50 first. Its structural automorphism description supplies the natural background for asking for a finite-field fixed-space spectrum. Jøndrup records the classical innerness theorem for algebra automorphisms of upper triangular matrix rings over commutative coefficient rings and provides a broader structural generalization.

The orbit-count portion was compared against the closest Borel-orbit literature. Melnikov classifies \(B\)-orbits only inside the square-zero strictly upper triangular locus and, over finite fields, counts points in those restricted orbits. Fresse studies intersections of nilpotent conjugacy classes with upper triangular matrices and determines when such nilpotent pieces have finitely many \(B\)-orbits. Those results concern nilpotent subvarieties, not the full six-dimensional algebra and not the automorphism fixed-space distribution proved here. Bhunia's later work concerns conjugacy classes of centralizers inside the invertible upper triangular group, again a different invariant and a different underlying set.

Targeted searches for the full \(T_3(\mathbb F_q)\) fixed-space distribution, the all-matrix \(B\)-orbit count, and the polynomial \(q^3+3q^2+q\) did not locate a statement implying the theorem. This negative search is not treated as a novelty proof; originality rests on the statement-level comparison with the structurally closest automorphism and Borel-orbit results above.

## Limitations
The result is specific to \(3\times3\) upper triangular matrices. It does not give the fixed-space distribution or orbit count for \(T_n(\mathbb F_q)\) when \(n\ge4\), where the rank stratification of centralizers is substantially more complicated. Literature searches cannot exclude unindexed or non-digitized finite-field orbit enumerations, so that remains a residual originality risk.

## References
1. P. N. Ánh and L. van Wyk, *Automorphism groups of generalized triangular matrix rings*, Linear Algebra and its Applications 434 (2011), 1018–1026. DOI: 10.1016/j.laa.2010.10.007. Available online 11 November 2010.
2. S. Jøndrup, *Automorphisms and derivations of upper triangular matrix rings*, Linear Algebra and its Applications 221 (1995), 205–218. DOI: 10.1016/0024-3795(93)00255-X.
3. A. Melnikov, *B-Orbits in solutions to the equation \(X^2=0\) in triangular matrices*, Journal of Algebra 223 (2000), 101–108. DOI: 10.1006/jabr.1999.8056.
4. L. Fresse, *Upper triangular parts of conjugacy classes of nilpotent matrices with finite number of \(B\)-orbits*, Journal of the Mathematical Society of Japan 65 (2013), 967–992. DOI: 10.2969/jmsj/06530967.
