# Complete two-sum spectrum of the finite-field fifth-power graph

## Finding
Let \(F\) be a finite field of odd cardinality \(q\) and let
\[
C_5=\{(t,t^5):t\in F\}\subset F^2,\qquad
r(s,w)=\#\{(u,v)\in F^2:u+v=s,\ u^5+v^5=w\}.
\]
When \(\operatorname{char}F\ne5\), let \(\chi\) be the quadratic character extended by \(\chi(0)=0\), and write \(\epsilon=\chi(-1)\) and \(\eta=\chi(-2)\). For every \(s\ne0\), exactly \(k_j\) values of \(w\) have \(r(s,w)=j\), where
\[
\boxed{(k_1,k_2,k_3,k_4)=
\left(\frac{1-\eta}{2},\frac{q+3\epsilon}{4},
\frac{1+\eta}{2},\frac{q-4-3\epsilon-2\eta}{8}\right).}
\]
No positive multiplicity greater than four occurs at nonzero \(s\). On the remaining first-coordinate fiber, \(r(0,0)=q\) and \(r(0,w)=0\) for \(w\ne0\). Thus
\[
\boxed{|C_5+C_5|=1+\frac{(q-1)(3q+4+3\epsilon-2\eta)}8,}
\qquad
\boxed{E(C_5)=q^2+3(q-1)(q-1-\epsilon).}
\]
Here \(E(C_5)=\sum_{s,w}r(s,w)^2\) is the ordered additive energy.

For \(\operatorname{char}F=5\), the graph is an additive subgroup: precisely \(q\) targets have multiplicity \(q\), all others have multiplicity zero, and
\[
\boxed{|C_5+C_5|=q,\qquad E(C_5)=q^3.}
\]
For any nontrivial additive character \(\psi\), define the constant-input extension by
\[
\mathcal E1(X,Y)=\frac1q\sum_{t\in F}\psi(Xt+Yt^5).
\]
In all these cases the exact fourth moment (with counting measure on \(F^2\)) is
\[
\boxed{\sum_{X,Y\in F}|\mathcal E1(X,Y)|^4=\frac{E(C_5)}{q^2}.}
\]

## Assumptions and scope
The field may have prime or nonprime order; only odd characteristic is assumed. In characteristic five, Frobenius additivity gives a separate, degenerate branch. The multiplicity table counts target values with *positive* representation multiplicity on a fixed first-coordinate slice; targets of multiplicity zero are not included. All representation pairs \((u,v)\) are ordered. The extension has normalization \(q^{-1}\) and its fourth norm uses counting measure on the full two-dimensional ambient group.

## Proof
Suppose first that the characteristic is odd and different from five. Fix \(s=u+v\) and make the invertible substitution \(u=s/2+x\), \(v=s/2-x\). Expanding the fifth powers gives
\[
u^5+v^5=\frac{s^5}{16}+\frac{5s^3}{2}x^2+5sx^4.
\]
For \(s=0\), the two odd powers cancel for all \(x\), so \(r(0,0)=q\), with every other \(r(0,w)=0\).

For \(s\ne0\), the leading coefficient \(5s\) is nonzero. Two choices \(x,y\in F\) give the same second-coordinate sum precisely when
\[
(x^2-y^2)\left(x^2+y^2+\frac{s^2}{2}\right)=0.
\]
Let \(A\) denote \(x^2=y^2\) and \(B\) denote \(x^2+y^2=-s^2/2\). The set \(A\) has \(2q-1\) points. Because its right-hand side is nonzero, the quadratic-character identity
\[
\#\{(x,y)\in F^2:x^2+y^2=c\}=q-\chi(-1)\quad(c\ne0)
\]
gives \(|B|=q-\epsilon\). To prove that identity, count \(y^2=c-x^2\) and use \(\sum_x\chi(x^2-c)=-1\), itself obtained by counting \((y-x)(y+x)=-c\): there are exactly \(q-1\) pairs because \(2\) and \(c\) are invertible. On \(A\cap B\), either \(x=y\) or \(x=-y\), and necessarily \(x^2=-s^2/4\). Each sign contributes \(1+\epsilon\) solutions and the branches do not meet on \(B\), so \(|A\cap B|=2(1+\epsilon)\). The total number of ordered collision pairs within the fixed \(s\)-fiber is therefore
\[
\sum_{w\in F}r(s,w)^2=|A|+|B|-|A\cap B|
=3(q-1-\epsilon). \tag{1}
\]

The quartic polynomial in \(x\) depends only on \(x^2\). Every nonzero root occurs with its negative, and each value has at most four preimages. The unique target reached by \(x=0\) has \(1+\#\{y\ne0:y^2=-s^2/2\}=2+\eta\) preimages. Thus it has multiplicity one when \(\eta=-1\) and three when \(\eta=1\). All other nonempty targets have multiplicity two or four. Consequently
\[
k_1=\frac{1-\eta}{2},\qquad k_3=\frac{1+\eta}{2}.
\]
Using that all \(q\) choices of \(x\) map to some target and using the exact collision count (1),
\[
k_1+2k_2+3k_3+4k_4=q,\qquad
k_1+4k_2+9k_3+16k_4=3(q-1-\epsilon).
\]
Solving these two equations yields
\[
k_2=\frac{q+3\epsilon}{4},\qquad
k_4=\frac{q-4-3\epsilon-2\eta}{8}.
\]
This proves the complete positive-fiber spectrum, including integrality and nonnegativity: each quantity counts an actual fiber stratum. Summing its four entries gives \((3q+4+3\epsilon-2\eta)/8\) distinct targets per nonzero \(s\). Together with the sole target at \(s=0\), this proves the twofold-sumset formula. Summing the squared fiber multiplicities proves
\[
E(C_5)=q^2+(q-1)\,3(q-1-\epsilon).
\]

When the characteristic is five, Frobenius gives \((u+v)^5=u^5+v^5\); hence the graph map \(t\mapsto(t,t^5)\) is injective and additive. Each of the \(q\) points in its image has exactly \(q\) ordered representations as a sum of two graph points. This gives the announced subgroup spectrum and energy.

Finally, expand the displayed fourth moment. Character orthogonality over \(F^2\) kills all quadruples except those satisfying \((a,a^5)+(b,b^5)=(c,c^5)+(d,d^5)\). Its ambient sum produces \(q^2\), while the four extension factors contribute \(q^{-4}\), giving \(E(C_5)/q^2\) exactly.

## Verification
The accompanying self-contained `verify_fifth_graph.py` uses only integer arithmetic and explicit quotient-field multiplication. It exhaustively forms all ordered graph-pair sums, checks the positive multiplicity histogram separately for each \(s\), and verifies the full image size and additive energy. It checks prime-field orders \(3,5,7,11,13,17,19,23,29,31,37,41\), and nonprime orders \(9,25,27,49,125\). It checks the characteristic-five subgroup degeneration in orders \(5,25,125\). Run `python verify_fifth_graph.py` in the same directory; successful completion prints `All exact tests passed.`. These finite calculations are corroborative only; the preceding argument proves the claims for all finite fields of odd characteristic.

## Relationship to prior work
Iosevich, Koh and Lewko study finite-field Fourier extension and additive-energy bounds for paraboloids, with different underlying quadratic surfaces and no fifth-power two-sum representation classification. Mockenhaupt and Tao formulate the finite-field restriction and representation-count machinery, and their complete moment curves retain every intermediate power; our two-coordinate quintic graph does not. González-Riquelme and Oliveira e Silva determine sharp finite-field extension inequalities for quadratic surfaces and a cone, not the two-coordinate fifth-power graph. A separately published classification of the *quartic* graph determines its additive energy by a different discriminant involution, but does not give the present fifth-power fiber spectrum. General orthogonality identities alone do not determine the exact multiplicity strata, which here also detect \(\chi(-2)\) beyond the energy's dependence on \(\chi(-1)\).

## Limitations
Characteristic two is not covered. The calculation treats the constant-input fourth extension moment, not the unrestricted best \(L^2\)-to-\(L^4\) operator norm or all possible weighted inputs. Nonzero fibers may have zero-target values not listed in the positive-multiplicity table. Targeted indexed searches and comparisons did not reveal an equivalent fifth-power spectrum, but an unindexed algebraic-curve or finite-field additive-combinatorics computation could still imply it; independent validation is not claimed here.

## References
1. A. Iosevich, D. Koh and M. Lewko, *Finite field restriction estimates for the paraboloid in high even dimensions*, arXiv:1712.05549v1 (first public 15 December 2017), especially Section 1 on extension normalization and Section 4 on additive energy. Primary MSC 42B05.
2. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234v1 (2002), especially Lemma 5.1 on even-exponent counting.
3. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1 (26 May 2024), especially Theorems 1.1--1.5 and the convolution method.
4. *Exact additive energy of the finite-field quartic graph*, publicly indexed mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-additive-energy-of-the-finite-field-quartic-graph--235f10989b3f, notably its full RESULT.md.
