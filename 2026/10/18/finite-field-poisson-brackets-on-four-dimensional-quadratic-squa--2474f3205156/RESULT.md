# Finite-field Poisson brackets on four-dimensional quadratic-square algebras

## Finding
Let \(K=\mathbb F_q\) with \(q\) odd. Let \(V\) be three-dimensional, \(B:V\times V\to K\) a nondegenerate symmetric bilinear form, and \(\eta\) a nonzero alternating trilinear form. On the four-dimensional **nonunital** commutative associative algebra \(A=V\oplus Kz\), impose
\[
uv=B(u,v)z,\qquad zA=0 \quad (u,v\in V).
\]
Define the cross product \(C\) by \(B(C(u,v),w)=\eta(u,v,w)\). Every Poisson bracket compatible with this fixed multiplication is uniquely
\[
\{u,v\}_{t,w}=tC(u,v)+\eta(u,v,w)z,\quad \{z,A\}_{t,w}=0,
\qquad (t,w)\in K\times V.
\]
There are exactly \(q^4\) such labeled brackets. Under isomorphisms preserving the associative product, **exactly \(q+2\) classes** occur: one for all \(t\ne0\), and \(q+1\) for \(t=0\). The latter are distinguished by \(w=0\), \(w\ne0\) with \(B(w,w)=0\), and one class for each \(a\in K^\times\) with \(B(w,w)=a\). This includes the characteristic-three case. The zero associative-product algebra and degenerate \(B\) are not included.

## Assumptions and scope
A Poisson bracket means a bilinear, alternating Lie bracket satisfying the Leibniz identity \(\{ab,c\}=\{a,c\}b+a\{b,c\}\). No associative unit is adjoined. All counts refer to a fixed presented associative algebra \(A\); the \(q^4\) count is of bracket maps, whereas \(q+2\) counts orbits under its full associative automorphism group. The chosen volume form determines parameter labels, not the numerical counts.

## Proof
**(1) The central square is Lie-central.** Nondegeneracy gives \(\operatorname{Ann}_{\cdot}(A)=Kz\) and \(A^2=Kz\). Every Hamiltonian derivation preserves the associative annihilator, hence \(\{z,u\}=\beta(u)z\) for a linear functional \(\beta\). Applying Leibniz to \(\{u^2,u\}=0\) yields \(B(u,u)\beta(u)=0\). Nonisotropic vectors span \(V\): choose one nonisotropic \(a\); for isotropic \(v\), at least one of \(a+v\) and \(a-v\) is nonisotropic, since their quadratic values sum to \(2B(a,a)\ne0\). Hence \(\beta=0\).

**(2) The complete bracket space.** Write \(\{u,v\}=D(u,v)+\omega(u,v)z\), with \(D:\bigwedge^2V\to V\) and \(\omega\in\bigwedge^2V^*\). Leibniz and \(\{z,V\}=0\) give
\[
B(D(u,w),v)+B(u,D(v,w))=0 \quad (u,v,w\in V).
\]
Consequently \(T(u,v,w)=B(D(u,v),w)\) is alternating in all three variables. Since \(\bigwedge^3V^*\) is one-dimensional, \(T=t\eta\), hence \(D=tC\). The map \(w\mapsto \eta(-,-,w)\) is an isomorphism \(V\to\bigwedge^2V^*\), giving a unique central parameter \(w\).

**(3) No extra Jacobi equations.** Choose an orthogonal basis \(e_1,e_2,e_3\) for \(B\), with \(B(e_i,e_i)=b_i\in K^\times\). Each \(C(e_i,e_j)\) is a multiple of the remaining basis vector. The two alternating trilinear Jacobi expressions \(\sum_{\mathrm{cyc}}C(C(u,v),w)\) and \(\sum_{\mathrm{cyc}}\omega(C(u,v),w)\) vanish on \((e_1,e_2,e_3)\), hence vanish identically. Thus every pair \((t,w)\) defines a genuine Poisson bracket, producing \(q\cdot q^3=q^4\) distinct labeled brackets.

**(4) Full automorphism action.** Every associative automorphism has the unique shape
\[
\Phi(u)=Pu+f(u)z,\qquad \Phi(z)=c z,
\qquad B(Pu,Pv)=cB(u,v),
\]
where \(P\in\operatorname{GO}(B)\), \(f\in V^*\), and \(c\in K^\times\). Taking determinants gives \((\det P)^2=c^3\). Because \(q\) is odd, \(c=s^2\) for some \(s\in K^\times\), so \(P=sO\) for \(O\in\operatorname O(B)\). The cross-product transformation is
\[
C(Pu,Pv)=\frac{\det P}{c}P C(u,v).
\]
Comparing the \(V\)-components of \(\Phi\{u,v\}_{t,w}=\{\Phi u,\Phi v\}_{t',w'}\) gives \(t'=tc/\det P=t/(s\det O)\). For \(t\ne0\), scalar \(s\) moves \(t\) to any chosen nonzero value. The free functional \(f\), combined with the isomorphism \(C:\bigwedge^2V\to V\), independently removes any central two-form. Hence all \(t\ne0\) brackets form one orbit, and none meets \(t=0\).

When \(t=0\), the parameter transforms as
\[
w'=\frac{c}{\det P}Pw=(\det O)Ow.
\]
The matrices \((\det O)O\) form \(\operatorname{SO}(B)\). Witt extension and an orientation-reversing reflection in the stabilizer of each nonzero vector show that \(\operatorname{SO}(B)\) is transitive on every nonzero quadratic-norm fiber. In dimension three over every odd finite field, \(B\) is isotropic and represents every \(a\in K\); the nonzero null cone exists. Therefore the orbits are precisely the zero vector, the nonzero isotropic vectors, and one orbit for each of the \(q-1\) nonzero values \(B(w,w)\). This gives \(q+1\) central orbits and \(q+2\) in total.

## Verification
The standalone `verify.py` constructs all 24 coordinates of an arbitrary alternating bracket on the displayed basis for \(B=I_3\), forms every Leibniz linear equation and computes rank \(20\), leaving a four-dimensional bracket space over \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\). It then independently evaluates all \(q^4\) displayed brackets against the original multiplication and every basis-triple Leibniz and Jacobi equation. Finally it enumerates \(\operatorname{SO}_3(q)\) matrices directly and their orbits on \(K^3\). Results: \((q,\#\text{brackets},\#\operatorname{SO}_3,\#\text{central orbits},\#\text{all classes})=(3,81,24,4,5),(5,625,120,6,7),(7,2401,336,8,9)\). Run `python3 verify.py` using Python's standard library. These finite tests do not replace the unrestricted proof.

## Relationship to prior work
Petrov--Pypka (arXiv:2609.13784, first publicly posted September 12, 2026) address arbitrary-field Poisson classification up to dimension three, motivating the next-dimensional nonunital problem. Abdelwahab--Sánchez (Axioms 14 (2025), article 804) give the global classification of all **complex** four-dimensional Poisson algebras; the present statement does not claim its complex normal forms as new. Its distinct contribution is the complete finite-field count of bracket maps and exact finite-field isomorphism-orbit stratification for the specified quadratic-square multiplication, including all odd characteristics and the isotropic orbit distinction. Search and scope comparisons are documented in the accompanying scientific review; no global novelty certification is asserted.

## Limitations
The field must have odd finite order, the associative form is nondegenerate, and the algebra is four-dimensional without unit. The statement does not classify arbitrary four-dimensional Poisson algebras, degenerate quadratic squares, even characteristic, or infinite-field orbit strata. The related published complex classification was available through substantial indexed excerpts, but not all of its tables could be retrieved for close comparison; an equivalent earlier finite-field formula cannot be categorically excluded. The verification checks only the split presentation \(B=I_3\) in three prime fields, while the symbolic proof treats all nondegenerate forms and odd prime powers.

## References
1. A. V. Petrov and O. O. Pypka, *On the Structure of Low-Dimensional Poisson Algebras over Arbitrary Fields*, arXiv:2609.13784 (first version submitted September 12, 2026).
2. H. Abdelwahab and J. M. Sánchez, *Classification of Four-Dimensional Complex Poisson Algebras*, Axioms 14 (2025), 804, DOI:10.3390/axioms14110804.
3. Finite-field quadratic-form transitivity (Witt extension theorem and orthogonal-group reflections), a standard fact used in the orbit argument.
