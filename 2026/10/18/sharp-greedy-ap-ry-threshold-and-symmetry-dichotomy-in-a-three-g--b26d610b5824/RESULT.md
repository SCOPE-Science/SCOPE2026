# Sharp greedy Apéry threshold and symmetry dichotomy in a three-generator \(h\)-ary family

## Finding
For every integer \(h\ge4\), put
\[
R=h^2-h+1,\qquad a_0=(h-3)R+h+1.
\]
For every integer \(a\ge a_0\), consider
\[
S_{h,a}=\langle a,A,B\rangle,\quad A=ha+1,\quad B=h^2a+R.
\]
The **entire Apéry set** relative to the smallest generator \(a\) is
\[
\operatorname{Ap}(S_{h,a},a)=\{w(r):0\le r<a\},\qquad
w(r)=\left\lfloor\frac rR\right\rfloor B+(r\bmod R)A.
\]
The threshold is sharp as a *uniform* assertion: at \(a=a_0-1\) the displayed formula is false.

Write uniquely \(a-1=qR+t\) with \(q\ge1\), \(0\le t<R\), and set
\[
U=(q-1)B+(R-1)A-a,\qquad V=qB+tA-a.
\]
Then the entire pseudo-Frobenius set is
\[
\operatorname{PF}(S_{h,a})=
\begin{cases}
\{V\},&t=R-1,\\
\{U,V\},&0\le t\le R-2.
\end{cases}
\]
In particular, \(S_{h,a}\) is symmetric **if and only if** \(R\mid a\), and otherwise has type two. Its Frobenius number is
\[
F(S_{h,a})=
\begin{cases}
U,&0\le t\le(h-1)^2-2,\\
V,&(h-1)^2-1\le t<R.
\end{cases}
\]
Its genus (number of positive gaps) is exactly
\[
g(S_{h,a})=\frac{1}{a}\left[
\left(\frac{Rq(q-1)}2+(t+1)q\right)B+
\left(\frac{R(R-1)q}2+\frac{t(t+1)}2\right)A
\right]-\frac{a-1}{2}.
\]

## Assumptions and scope
All semigroup parameters and coefficients are integers; \(h\ge4\) and \(a\ge a_0(h)\). The semigroup is additive and includes zero. Its generators have greatest common divisor one because \(A\equiv1\pmod a\); consequently the Apéry set, Frobenius number, genus and pseudo-Frobenius set are defined. The generator \(a\) is the multiplicity, since \(A,B>a\). The generator \(B\) is not redundant: \(B\equiv R\pmod a\), \(R<a\), and \(B<RA\), so no nonnegative combination of \(a,A\) equals \(B\).

A pseudo-Frobenius number is a gap \(z\notin S_{h,a}\) for which \(z+s\in S_{h,a}\) for every nonzero \(s\in S_{h,a}\). Symmetric means pseudo-Frobenius type one. The word *sharp* concerns failure at \(a=a_0(h)-1\), not the assertion that every smaller parameter fails.

## Proof
**1. Fixed-residue coin normalization.** For nonnegative integers \(x,y\), let \(s=x+Ry\), so \(xA+yB\equiv s\pmod a\). The exact identity
\[
RA-B=h(h-1)^2a>0
\]
gives
\[
xA+yB=sA-y(RA-B).
\]
At fixed \(s\), this is minimized when \(y=\lfloor s/R\rfloor\) and \(x=s\bmod R\). The least cost at fixed \(s\) is therefore \(w(s)\).

**2. Monotonicity under adding \(a\).** Write \(a=mR+u\), \(0\le u<R\), and write \(s=nR+v\), \(0\le v<R\). Direct calculation gives
\[
w(s+a)-w(s)=
\begin{cases}
mB+uA,&v+u<R,\\
(m+1)B-(R-u)A,&v+u\ge R.
\end{cases}
\]
The first expression is positive. A carry in the second branch requires \(u\ge1\). The second expression equals
\[
h\bigl(h(m-h+2)+u-1\bigr)a+(mR+u).
\]
Because \(a\ge(h-3)R+h+1\), either \(m\ge h-2\), in which case the parenthesis is nonnegative for \(u\ge1\), or \(m=h-3\) and \(u\ge h+1\), when it is likewise nonnegative. Thus \(w(s+a)>w(s)\) for every \(s\ge0\). Every \(s\ge0\) congruent to \(r\in\{0,\ldots,a-1\}\) modulo \(a\) has the form \(s=r+ja\) for \(j\ge0\). By step 1, its least cost is \(w(s)\), which by strict monotonicity is minimized at \(j=0\). This proves the asserted complete Apéry set.

**3. Sharp boundary.** At \(a=a_0-1=(h-3)R+h\), the residue \(r=R-h=(h-1)^2\) satisfies \(0<r<a\). The formula would assign \(w(r)=(R-h)A\), but the explicit alternative
\[
(h-2)B=(R-h)A-(h-1)a<(R-h)A
\]
has the same residue modulo \(a\). Therefore the formula fails immediately below \(a_0\), proving uniform sharpness.

**4. Maximal Apéry elements and pseudo-Frobenius numbers.** For each \(r+1<a\) with \(r\bmod R<R-1\), one has \(w(r+1)=w(r)+A\). For each \(r+R<a\), one has \(w(r+R)=w(r)+B\). Thus an Apéry element can be maximal under the semigroup order \(x\preceq_S y\iff y-x\in S_{h,a}\) only at residue \(p=qR-1\) or \(a-1=qR+t\). The corresponding candidates after subtracting \(a\) are \(U\) and \(V\).

If \(t=R-1\), then \(w(a-1)=w(p)+B\), so the only maximum is \(w(a-1)\).

Suppose \(t\le R-2\). Put \(\beta=t+1\), so \(1\le\beta\le R-1<a\). Their difference is
\[
\Delta=V-U=\beta A-h(h-1)^2a,\qquad \Delta\equiv\beta\pmod a.
\]
If \(\Delta>0\), it is below the minimum \(w(\beta)=\beta A\) in its residue, so \(\Delta\notin S_{h,a}\). If \(\Delta<0\), then \(-\Delta=(R-\beta)A-B\), which is below the minimum \(w(a-\beta)=w(qR)=qB\): the latter inequality follows from step 2 applied to \(R-\beta\), since \(w((R-\beta)+a)=w((q+1)R)=(q+1)B>w(R-\beta)=(R-\beta)A\). Thus \(-\Delta\notin S_{h,a}\). Finally \(\Delta\neq0\) because \(\Delta\equiv\beta\pmod a\) with \(0<\beta<a\). Therefore both candidates are incomparable maximal Apéry elements. The standard Apéry-maximality characterization of pseudo-Frobenius numbers gives precisely \(\{U,V\}\).

**5. The Frobenius branches.** From the preceding equation,
\[
V-U=h\bigl(\beta-(h-1)^2\bigr)a+\beta.
\]
It is positive for \(\beta\ge(h-1)^2\) and negative for \(\beta\le(h-1)^2-1\), since then \(h(a)>\beta\) under the standing lower bound. With \(\beta=t+1\), this gives exactly the two stated branches. Type one holds exactly when \(t=R-1\), or \(a\equiv0\pmod R\).

**6. The genus.** The Apéry genus identity is
\[
g=\frac1a\sum_{r=0}^{a-1}w(r)-\frac{a-1}{2}.
\]
There are \(q\) complete blocks of length \(R\) and a final block \(0\le r\bmod R\le t\). Thus
\[
\sum_{r=0}^{a-1}\left\lfloor\frac rR\right\rfloor
=\frac{Rq(q-1)}2+(t+1)q,
\quad
\sum_{r=0}^{a-1}(r\bmod R)=\frac{R(R-1)q}{2}+\frac{t(t+1)}2.
\]
Substitution proves the genus formula.

## Verification
Execute \(\texttt{python3 verify.py}\) with Python 3 standard library. The included executable independently computes Apéry sets with Dijkstra's shortest paths on residues modulo \(a\) (edges of weights \(A,B\)), then checks the complete stated Apéry formula, the pseudo-Frobenius set using semigroup membership, both Frobenius branches, genus and symmetry. It verifies 640 stable parameter pairs with \(4\le h\le11\), eight explicit sharp-boundary failures, and another 196 checks at \(h=3\) outside the theorem's range. Expected output: `PASS 640 stable pairs h=4..11, 8 sharp boundary failures, 196 h=3 boundary checks`. The finite computational range does not prove the universal statement; the six symbolic steps above supply the proof.

## Relationship to prior work
Liu, Xin, Ye and Yin (arXiv:2306.03459, public June 6, 2023) treat the binary-base repunit/Mersenne-type semigroup \(\langle a,2a+d,4a+3d,\ldots\rangle\) and explicitly discuss extension to general bases \(h\ge2\) in their final remark. The present family is the first nontrivial three-generator truncation of that general-base extension at \(d=1\), with \(h\ge4\). The binary-base formulas are not substitutions giving the sharp \(a_0(h)\), Apéry set or symmetry criterion here.

The general reduction of Liu and Xin (arXiv:2303.07149) explains optimization of residue minima and treats families with common slopes, such as \(\langle a,ha+d,ha+jd\rangle\). Here the two noninitial slopes are distinct, \(h\) and \(h^2\). Morales and Dung (arXiv:2601.07467) develop broad algorithms for generalized almost-arithmetic semigroups, including three generators. Such a method may in principle compute a particular instance; the present result states and proves a closed two-parameter stabilization threshold, full Apéry normal form and exact symmetry dichotomy. A general algorithm alone does not explicitly provide these uniform formulas. Derivation from broader methods remains a relevant originality risk.

## Limitations
The theorem starts at \(a_0(h)\). Failure at \(a_0(h)-1\) demonstrates only optimality of the uniform all-larger-parameters threshold, not a classification below it. No claim is made for general \(d>1\), higher truncation lengths, or a complete classification of all three-generator numerical semigroups. The inspected literature may omit a result expressible by different parameter changes or a nontrivial specialization of a general three-generator algorithm; such an overlap would require further specialist scrutiny. Mathematical audit beyond the recorded self-review has not been performed.

## References
1. F. Liu, G. Xin, S. Ye and J. Yin, *On the Frobenius Number and Genus of a Collection of Semigroups Generalizing Repunit Numerical Semigroups*, arXiv:2306.03459, initially public 2023-06-06; especially concluding remark on general base \(h\).
2. F. Liu and G. Xin, *A Combinatorial Approach to Frobenius Numbers of Some Special Sequences (Complete Version)*, arXiv:2303.07149, 2023; especially Sections 2 and 3.
3. M. Morales and N. T. Dung, *Frobenius Number of Almost Symmetric Numerical Generalized Almost Arithmetic Semigroups*, arXiv:2601.07467, 2026.
4. Standard Apéry-set characterizations of the Frobenius number, genus and pseudo-Frobenius maximal elements, as recalled in the cited semigroup literature.
