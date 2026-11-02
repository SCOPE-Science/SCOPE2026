# Cycle spectra and a Kloosterman coefficient census for a binary permutation trinomial

## Finding
For every \(q=2^m\), \(m\ge2\), put \(K=\mathbb F_q\) and \(L=\mathbb F_{q^2}\). Consider the polynomial
\[
F_t(X)=X+tX^q+X^{2q-1},\qquad t\in K^\times,\qquad \operatorname{Tr}_{K/\mathbb F_2}(1/t)=0.
\]
The stated trace condition is exactly the known permutation criterion for this even-characteristic family [1]. Let \(\operatorname{ord}(a)\) denote the multiplicative order of a nonzero element of \(K\), and set
\[
S_q=\{z\in K^\times:\operatorname{Tr}_{K/\mathbb F_2}(1/z)=1\}.
\]
There are exactly \(q/2\) elements of \(S_q\). The complete disjoint-cycle count of \(F_t\), by cycle length \(\ell\ge1\), is
\[
C_\ell(t)=\mathbf1_{\ell=1}
+\frac{q-1}{\operatorname{ord}(t)}\mathbf1_{\ell=\operatorname{ord}(t)}
+\sum_{z\in S_q}\frac{q-1}{\operatorname{ord}(t+z)}\mathbf1_{\ell=2\operatorname{ord}(t+z)}.
\tag{1}
\]
The terms represent the fixed point zero, the nonzero subfield, and disjoint conjugate pairs of norm-one fibers, respectively. The expression is integral; \(t+z\ne0\) because the two inverse traces differ.

A two-cycle occurs precisely when \(t\ne1\) and \(\operatorname{Tr}(1/(1+t))=1\). In that case there are exactly \(q-1\) two-cycles; otherwise there are none. Define the binary Kloosterman sum
\[
\mathcal K_q=\sum_{w\in K^\times}(-1)^{\operatorname{Tr}(w+w^{-1})}.
\]
Among the \(q/2-1\) admissible parameters \(t\), the exact number with two-cycles is
\[
\boxed{\quad T_q=\frac{q-1-\mathcal K_q}{4}.\quad}
\tag{2}
\]
In particular \(T_4=0\), while \(T_q>0\) for every \(q\ge8\); the proportion of admissible parameters with two-cycles approaches \(1/2\) as \(q\) grows.

## Assumptions and scope
All finite-field traces without subscripts are absolute traces from \(K\) to \(\mathbb F_2\). Every \(\ell\) is a positive integer, and the formula counts cycles, not periodic points; points of least period \(\ell\) number \(\ell C_\ell(t)\). The polynomial acts on all \(q^2\) elements of \(L\), including zero. The hypothesis \(m\ge2\) ensures \(q>2\), as in the cited permutation classification. No assertion is made for nonpermuting parameters or odd-characteristic fields.

## Proof
**Step 1: norm-one parameter and two-step multiplier.** For each \(x\in L^\times\), let \(u=x^{q-1}\). Then \(u^{q+1}=1\), and
\[
F_t(x)=x\bigl(1+tu+u^2\bigr)=x^q\bigl(t+u+u^{-1}\bigr).
\]
Put \(s(u)=t+u+u^{-1}\). Because \(u^q=u^{-1}\) and \(t\in K\), \(s(u)^q=s(u)\), hence \(s(u)\in K\). Moreover \(s(u)\ne0\): if \(u=1\), then \(s(u)=t\ne0\); otherwise \(s(u)=0\) would imply \(u+u^{-1}=t\) and that \(u\notin K\) solves \(U^2+tU+1=0\). The latter polynomial is irreducible over \(K\) exactly when \(\operatorname{Tr}(1/t)=1\), contradicting the coefficient condition. Thus
\[
\bigl(F_t(x)\bigr)^{q-1}=u^{-1},\qquad F_t^{\circ2}(x)=s(u)^2x.
\tag{3}
\]
The last relation holds also for the two-step orbit, since \(s(u^{-1})=s(u)\).

**Step 2: disjoint cycle classification.** The fiber \(u=1\) is \(K^\times\), on which \(F_t(x)=tx\). It has \((q-1)/\operatorname{ord}(t)\) cycles of length \(\operatorname{ord}(t)\). For \(u\ne1\), the pair of fibers labeled \(u,u^{-1}\) contains \(2(q-1)\) elements and is invariant under \(F_t\). The parameter flips at each application, so every cycle length is even. By (3), the least even return is twice the order of \(s(u)^2\). Since \(K^\times\) has odd order, \(\operatorname{ord}(s(u)^2)=\operatorname{ord}(s(u))\). Therefore every point in the pair has least period exactly \(2\operatorname{ord}(s(u))\), giving \((q-1)/\operatorname{ord}(s(u))\) cycles.

For \(u\ne1\), set \(z=u+u^{-1}\). The polynomial \(U^2+zU+1\) is irreducible over \(K\) because its distinct roots \(u,u^{-1}\) lie outside \(K\). In characteristic two, this is equivalent to \(z\ne0\) and \(\operatorname{Tr}(1/z)=1\). Conversely, every such \(z\) gives precisely one conjugate pair \(u,u^{-1}\) in the norm-one subgroup. Consequently \(z\) runs once through \(S_q\), which has size \(q/2\). Counting all invariant fibers yields (1), and the total number of represented points is
\[
1+(q-1)+|S_q|\,2(q-1)=q^2.
\]
Since all orders in \(K^\times\) are odd, the only way to get period two is \(s(u)=1\). This means \(z=t+1\in S_q\), equivalent to the displayed trace condition, and contributes precisely \(q-1\) two-cycles.

**Step 3: exact parameter census.** Let \(\psi(a)=(-1)^{\operatorname{Tr}(a)}\). Set \(v=1/t\); the condition for admissibility and existence of a two-cycle is
\[
v\in K\setminus\{0,1\},\quad \psi(v)=1,\quad \psi\left(\frac{v}{1+v}\right)=-1.
\]
By character orthogonality the number of such \(v\) is
\[
T_q=\frac14\sum_{v\ne0,1}
(1+\psi(v))\left(1-\psi\left(\frac{v}{1+v}\right)\right).
\]
The two one-character sums over \(v\ne0,1\) are equal to \(-1-\psi(1)\): the second is the same as the first because \(v\mapsto v/(1+v)\) permutes \(K\setminus\{0,1\}\). They therefore cancel with opposite signs in the expansion, for either parity of \(m\). The mixed character is
\[
\psi\left(v+\frac{v}{1+v}\right)=\psi\left(\frac{v^2}{1+v}\right).
\]
Substituting \(w=1/(1+v)\) gives \(v^2/(1+v)=w+w^{-1}\) and bijects the summation domain onto \(K^\times\setminus\{1\}\). Thus its sum equals \(\mathcal K_q-1\). Therefore \(4T_q=q-1-\mathcal K_q\), proving (2).

**Step 4: positivity and asymptotics.** The smooth projective elliptic curve obtained from
\[
E:\qquad Y^2+XY=X^3+1
\]
has exactly \(q+1+\mathcal K_q\) rational points over \(K\). Indeed for \(X\ne0\), writing \(Y=XZ\) gives \(Z^2+Z=X+X^{-2}\), and \(\operatorname{Tr}(X^{-2})=\operatorname{Tr}(X^{-1})\); there are \(1+\psi(X+X^{-1})\) solutions. The unique point at \(X=0\) and the point at infinity supply the other two points. The curve is nonsingular (its partial derivatives have no common zero on the affine equation, and it has a nonsingular point at infinity). Hasse's bound therefore yields \(|\mathcal K_q|\le2\sqrt q\). Equation (2) implies \(T_q=q/4+O(\sqrt q)\) and \(T_q>0\) for all powers of two \(q\ge8\). For \(q=4\), the three nonzero elements all contribute \(+1\) to \(\mathcal K_4\), so \(\mathcal K_4=3\) and \(T_4=0\).

## Verification
A standalone Python 3 verifier implements arithmetic in five quadratic extensions of binary finite fields without external packages. It tests every admissible coefficient, constructs the complete map on every field element, enumerates its disjoint cycles independently, compares the result with (1), and checks (2) by explicit absolute-trace and Kloosterman calculations. The tested base-field orders are \(4,8,16,32,64\), totaling 57 parameter instances and 144336 evaluated field states. All checks passed. These are finite corroborations, not substitutes for the general proof.

## Relationship to prior work
Hou's 2013 original paper [1] proves exactly when the indicated trinomial is a permutation; its proof expresses the map using a norm-one trace scalar. It does not state a cycle-index classification or a Kloosterman count of the coefficients admitting two-cycles. The present proof makes the dynamics on paired norm-one fibers explicit, and counts coefficients by an independent character-sum argument. Gerike and Kyureghyan [2] classify cycles of different trace-form permutation families on extension fields; the cited polynomials are not the trinomial here. Zeng and collaborators [3] treat four other even-characteristic polynomial families. Classical binary Kloosterman and elliptic-point-count relations [4] support the bound used in the census. Searches did not identify a published classification equivalent to (1) together with (2); that negative search is not proof of historical priority.

## Limitations
The explicit cycle spectrum is restricted to the even-characteristic permutation case and expresses most lengths by multiplicative orders in \(K^\times\); it does not simplify the order distribution for arbitrary \(q\) and \(t\). The density statement is asymptotic over powers of two, not a statement that exact half of coefficients always possess two-cycles. The link to Hou's pointwise semilinear identity means some ingredients are elementary consequences of previously published algebra; the potentially new portion is the complete cycle index and its exact Kloosterman coefficient census. No independent verification of priority has been performed.

## References
[1] X.-D. Hou, *A Class of Permutation Trinomials over Finite Fields*, arXiv:1303.0568v1, publicly submitted 2013-03-03; subsequently *Acta Arithmetica* 162 (2014), 51–64, DOI: 10.4064/aa162-1-3.

[2] D. Gerike and G. M. Kyureghyan, *Permutations on finite fields with invariant cycle structure on lines*, *Designs, Codes and Cryptography* 88 (2020), 1723–1740, DOI: 10.1007/s10623-020-00721-2.

[3] D. Zeng, X. Zeng, L. Li and Y. Xu, *The cycle structure of a class of permutation polynomials*, *Designs, Codes and Cryptography* 91 (2023), 1373–1400, DOI: 10.1007/s10623-022-01155-8.

[4] M. Moisio, *Kloosterman sums, elliptic curves, and irreducible polynomials with prescribed trace and norm*, arXiv:0706.2112 (2007).