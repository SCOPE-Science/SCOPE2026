# Finite-field commuting-nilpotent tuple census for the five-dimensional Witt algebra

## Finding
For every finite field \(k=\mathbb F_q\) with \(q=5^f\) and \(f\ge1\), define the Witt Lie algebra \(W=\operatorname{Der}_k(k[t]/(t^5))\), its restricted nilpotent cone \(\mathcal N=\{D\in W:D^5=0\}\), and \(C_m(q)\) as the number of ordered pairwise commuting \(m\)-tuples from \(\mathcal N\). The empty tuple is counted once. Then, for every integer \(m\ge0\),
\[
C_m(q)=(q+1)q^{2m}+(q^3-q)q^m-q^3.
\]
Consequently the ordinary generating function, in a formal variable \(z\), is
\[
\sum_{m\ge0} C_m(q)z^m
=\frac{q+1}{1-q^2z}+\frac{q^3-q}{1-qz}-\frac{q^3}{1-z}.
\]
For example, \(C_1(5)=625\), \(C_2(5)=6625\), and \(C_3(5)=108625\). The result concerns point counts over finite fields of characteristic five, not geometric irreducible-component counts.

## Assumptions and scope
Let \(A=k[t]/(t^5)\) and \(\partial=d/dt\); every derivation is uniquely \(D_f=f(t)\partial\) with \(f\in A\). The restricted fifth power is composition as a linear endomorphism of \(A\), so \(D_f\in\mathcal N\) means \(D_f^5\) vanishes on all of \(A\). The Lie bracket is \([D_f,D_g]=D_{fg'-gf'}\). All fields here are finite of characteristic exactly five. Tuple length \(m\) is unrestricted and repetitions and zero entries are allowed.

## Proof
**Step 1: Count nilpotent elements.** If \(f(0)=0\), the action of \(D_f\) on the ordered monomial basis is triangular, with diagonal entries \(0,f_1,2f_1,3f_1,4f_1\), where \(f_1\) is the coefficient of \(t\). Therefore \(D_f\) is nilpotent exactly when \(f_1=0\). This contributes \(q^3\) elements in \(t^2A\partial\).

If \(f(0)\ne0\), then \(f\) is a unit, and \(\ker D_f=\ker\partial=k\). If \(D_f\) is nilpotent, its five-dimensional linear operator has one Jordan block. Hence \(1\), which spans its kernel, lies in its image: choose \(u\in A\) with \(u(0)=0\) and \(D_f(u)=1\). Necessarily \(u'(0)=f(0)^{-1}\ne0\), so substitution \(t\mapsto u\) is an algebra automorphism and conjugates \(D_f\) to \(\partial\). Conversely this conjugation implies \(D_f^5=0\). The coordinate \(u\) is unique since two solutions differ by a constant. There are exactly \((q-1)q^3\) coordinates \(u=u_1t+\cdots+u_4t^4\) with \(u_1\ne0\). Hence \(|\mathcal N|=q^4\), split into a single open family of size \((q-1)q^3\) and the subspace \(t^2A\partial\) of size \(q^3\). No algebraic-closedness assumption is needed.

**Step 2: Centralizer partition.** Compare the coefficients in \(fg'-gf'=0\). For a nonzero element of the open family, its centralizer in \(W\) is its one-dimensional span; conjugation reduces this to \(Z_W(\partial)=k\partial\). For nonzero \(D_f\) whose first nonzero term has degree two, the centralizer is \(kD_f+k t^4\partial\), a two-dimensional abelian subalgebra. At degree three the centralizer is \(\langle t^3\partial,t^4\partial\rangle\), again two-dimensional abelian. At degree four it is \(H=\langle t^2\partial,t^3\partial,t^4\partial\rangle\), with sole nonzero basis bracket \([t^2\partial,t^3\partial]=t^4\partial\); thus \(H\) is a three-dimensional Heisenberg algebra. All these centralizers consist of restricted-nilpotent elements. The respective counts of nonzero first entries are
\[
(q-1)q^3,\qquad (q-1)q^2,\qquad(q-1)q,\qquad q-1.
\]
The zero first entry has centralizer \(W\) but its allowed companions are precisely \(\mathcal N\).

**Step 3: Commuting tuples in the exceptional centralizer.** For every \(r\ge0\), write an ordered \(r\)-tuple in \(H\) as \(a_j t^2\partial+b_jt^3\partial+c_jt^4\partial\). These elements commute pairwise exactly when the \(2\times r\) matrix with rows \((a_j)\) and \((b_j)\) has rank at most one. The number of such matrices is \(1+(q+1)(q^r-1)\): the zero matrix plus a uniquely specified projective line of nonzero columns with \(q^r-1\) coefficient vectors. The \(c_j\) are arbitrary. Thus the exact Heisenberg count is
\[
H_r(q)=q^r\bigl((q+1)q^r-q\bigr).
\]

**Step 4: All arities.** Conditioning on the first entry of an \(m\)-tuple, for every \(m\ge1\) obtain
\[
\begin{aligned}
C_m(q)={}&C_{m-1}(q)+(q-1)q^3 q^{m-1}\\
&+(q-1)(q^2+q)q^{2m-2}+(q-1)H_{m-1}(q).
\end{aligned}
\]
Indeed the zero first entry leaves \(C_{m-1}(q)\), and each nonzero first entry constrains all remaining entries to a common centralizer; those centralizers are abelian except \(H\), counted separately. Substituting the preceding Heisenberg formula simplifies the recurrence to
\[
C_m(q)-C_{m-1}(q)
=(q-1)\bigl((q+1)^2q^{2m-2}+(q^3-q)q^{m-1}\bigr).
\]
Summing from \(C_0(q)=1\) gives the displayed closed formula for every nonnegative \(m\). Summing geometric series gives the generating function. The proof requires neither experimental interpolation nor any unproved claim about a larger commuting variety.

## Verification
The included standalone Python 3 checker `verify_witt_tuples.py` runs using only the standard library. Over \(\mathbb F_5\), it enumerates all \(3125\) derivations, identifies the \(625\) nilpotent ones by fifth iterates on the full monomial basis, directly computes all allowed centralizers, and verifies the \(m=2\) count \(6625\) and the \(m=3\) count \(108625\). It also directly enumerates commuting pairs in representatives of every nonzero centralizer type and verifies the three-dimensional Heisenberg formula. This finite-field computation is a cross-check, not a substitute for the all-arity proof.

## Relationship to prior work
Yao and Chang, *Nilpotent commuting varieties of the Witt algebra* (arXiv:1301.5667v1, 23 January 2013), study pairs of nilpotent elements over algebraically closed fields. Their Lemma 2.3 already contains the centralizer stratification used above, and their Section 3 classifies pair-variety components. That centralizer lemma and the nilpotent cone stratification are not asserted as new. Yao, *On nilpotent commuting varieties of r-tuples in the Witt algebra* (Journal of Pure and Applied Algebra 219 (2015), DOI 10.1016/j.jpaa.2015.02.005), studies geometric components and dimensions for higher tuples, over an algebraically closed base. Its available abstract does not give finite-field point counts; the complete text was not accessible for a decisive exclusion of an implicit equivalent formula. Yao and Zhang (2021) examine all commuting, not necessarily restricted-nilpotent, tuples and describe their geometric components and dimensions. The present result is the explicit rational all-arity finite-field point-count series for the restricted-nilpotent locus when the characteristic is five. A geometric component list or dimension statement by itself does not determine this series, though it could yield it when accompanied by sufficiently explicit arithmetic stratification.

## Limitations
The result concerns precisely the five-dimensional truncated-polynomial Witt algebra in characteristic five. It does not give a formula uniform in the characteristic, scheme-theoretic structure, an irreducible-component classification, or point counts for full (not restricted-nilpotent) commuting tuples. Historical priority remains uncertain because complete 2015 text was unavailable. Independent mathematical validation has not been performed.

## References
1. Yu-Feng Yao and Hao Chang, *Nilpotent commuting varieties of the Witt algebra*, arXiv:1301.5667v1, 2013-01-23, Section 2 (especially Lemma 2.3), Section 3. https://arxiv.org/abs/1301.5667
2. Yu-Feng Yao, *On nilpotent commuting varieties of r-tuples in the Witt algebra*, Journal of Pure and Applied Algebra 219 (2015), DOI 10.1016/j.jpaa.2015.02.005 (abstract examined; full text unavailable).
3. Yu-Feng Yao and Yajing Zhang, *Commuting variety of r-tuples over the Witt algebra*, Journal of East China Normal University (Natural Science), 2021 (3):1–7, DOI 10.3969/j.issn.1000-5641.2021.03.001 (abstract and article landing page examined).
