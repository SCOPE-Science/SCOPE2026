# Elliptic traces in mixed cubic–even-quartic Fourier energy

## Finding

Let \(F=\mathbb F_q\) be any finite field of characteristic \(p\ge5\), and let \(\chi:F\to\{-1,0,1\}\) be its quadratic character, with \(\chi(0)=0\). For each \(c\in F\), consider two distinct polynomial graphs in \(F^2\):
\[
A=\{(t,t^3):t\in F\},\qquad B_c=\{(u,u^4+c u^2):u\in F\}.
\]
For each \((s,y)\in F^2\), let \(r_c(s,y)\) be the number of **ordered** pairs \((t,u)\) such that \(t+u=s\) and \(t^3+u^4+cu^2=y\). Define the mixed additive energy
\[
E_c=\sum_{s,y\in F}r_c(s,y)^2.
\]
Introduce the cubic \(P_c(v)=4v^3+2cv\), its quadratic-character sum, and two exceptional corrections:
\[
C_c=\sum_{v\in F}\chi(P_c(v)),\qquad
H_c=\sum_{\substack{v\in F:\;P_c(v)=0\\v\ne1/4}}\chi(v-1/4),\qquad
J_c=\chi(1+8c).
\]
(The sum defining \(H_c\) is over **distinct elements**, not roots counted with multiplicity.) For every \(c\in F\), including \(c=0\) and \(c=-1/8\), the exact identity is
\[
\boxed{E_c=2q^2-q+\chi(3)\bigl(-C_c+qH_c+qJ_c\bigr).}
\]
If \(c\ne0\), the nonsingular elliptic curve \(\mathcal C_c:\ w^2=4v^3+2cv\) has Frobenius trace \(a_q(c)=q+1-\#\mathcal C_c(F)=-C_c\). Equivalently,
\[
\boxed{E_c=2q^2-q+\chi(3)a_q(c)+q\chi(3)(H_c+J_c)\qquad(c\ne0).}
\]
In particular, after subtracting the explicit local branch correction, the remaining arithmetic fluctuation is exactly an elliptic Frobenius trace and has magnitude at most \(2\sqrt q\) by the Hasse bound. At the singular degeneration \(c=0\), the formula becomes
\[
E_0=2q^2-q+q\bigl(\chi(3)+\chi(-3)\bigr)
=\begin{cases}
2q^2+q,&q\equiv1\pmod{12},\\
2q^2-3q,&q\equiv5\pmod{12},\\
2q^2-q,&q\equiv7,11\pmod{12}.
\end{cases}
\]
Thus the undeformed mixed cubic/quartic convolution has **three distinct arithmetic regimes**, while its even-quartic deformation introduces an elliptic trace together with completely explicit singular corrections.

For any nontrivial additive character \(\psi:F\to\mathbb C^\times\), put
\[
\mathcal S_3(\xi,\eta)=\sum_{t\in F}\psi(\xi t+\eta t^3),\qquad
\mathcal S_{4,c}(\xi,\eta)=\sum_{u\in F}\psi(\xi u+\eta(u^4+cu^2)).
\]
The identical invariant is a mixed constant-input Fourier fourth moment:
\[
E_c=\frac1{q^2}\sum_{\xi,\eta\in F}
|\mathcal S_3(\xi,\eta)|^2|\mathcal S_{4,c}(\xi,\eta)|^2.
\]

## Assumptions and scope

The theorem holds for **every** finite field \(F\) of size \(q=p^n\) and characteristic \(p\ge5\), every parameter \(c\in F\), and any nontrivial additive character. The first coordinates make \(A\) and \(B_c\) injectively parametrized sets of size \(q\). The energy is the count of quadruples \((t,u,t',u')\in F^4\) for which the two mixed point sums agree, with all four variables ordered. The normalization of the displayed Fourier moment uses the uniform probability average \(q^{-2}\) in frequency space and unnormalized character sums.

For \(c\ne0\), \(\mathcal C_c\) denotes the smooth projective completion of the affine cubic equation, including its single point at infinity. For \(c=0\), its cubic is singular and no elliptic trace is asserted. Characteristic two or three is excluded because the proof uses invertibility of \(2\) and \(3\).

## Proof

**1. Parametrize nontrivial mixed collisions.** Equality of first-coordinate sums implies \(t'=t+h\) and \(u'=u-h\) for a unique \(h\in F\). The \(h=0\) solutions are the \(q^2\) trivial quadruples. For \(h\ne0\), change variables bijectively by
\[
w=t+h/2,\qquad v=u-h/2.
\]
A direct expansion gives
\[
\begin{aligned}
& t^3+u^4+cu^2-(t+h)^3-(u-h)^4-c(u-h)^2\\
&\qquad=h\left[-3w^2+4v^3+2cv+h^2(v-1/4)\right].
\end{aligned}
\]
Thus the required second-coordinate equality is exactly
\[
3w^2=P_c(v)+(v-1/4)h^2.
\]
For fixed \(h\ne0\) and \(v\), the number of \(w\) is
\[
1+\chi(3)\chi\bigl(P_c(v)+(v-1/4)h^2\bigr).
\]
Indeed \(\chi(1/3)=\chi(3)\). Summing all \(q(q-1)\) choices of \((h,v)\) yields
\[
E_c=2q^2-q+\chi(3)\sum_{v\in F}\sum_{h\in F^\times}\chi\bigl(P_c(v)+(v-1/4)h^2\bigr).
\]

**2. Evaluate the quadratic character sum, including its degeneracies.** For every \(a,b\in F\),
\[
\sum_{h\in F^\times}\chi(a+bh^2)
=-\chi(a)-\chi(b)
+q\mathbf1_{a=0}\chi(b)
+q\mathbf1_{b=0}\chi(a).
\]
For \(ab\ne0\), apply \(\sum_{h\in F}\chi(h^2+d)=-1\) when \(d\ne0\). To prove that identity directly, the number of pairs \((h,z)\) satisfying \(z^2-h^2=d\) is \(q-1\): the substitution \((h,z)\mapsto(z-h,z+h)\) is a bijection onto the solutions of \(xy=d\). On the other hand it equals \(q+\sum_h\chi(h^2+d)\). Multiplying by \(\chi(b)\) and removing \(h=0\) gives \(-\chi(a)-\chi(b)\). When \(a=0\) or \(b=0\), direct evaluation gives the two correction terms displayed, also valid when both vanish.

**3. Sum over the cubic branch parameter.** Apply Step 2 with \(a=P_c(v)\) and \(b=v-1/4\). Since \(v\mapsto v-1/4\) bijects \(F\), its quadratic-character sum vanishes. The \(-\chi(a)\) terms contribute \(-C_c\). The exceptional \(a=0\) terms contribute \(qH_c\), because the possible common zero \(v=1/4\) has zero quadratic character. The unique \(b=0\) term contributes \(q\chi(P_c(1/4))\). A calculation gives
\[
P_c(1/4)=1/16+c/2=(1+8c)/16,
\]
so \(\chi(P_c(1/4))=\chi(1+8c)=J_c\), including \(c=-1/8\). Substitution gives the first boxed theorem. This argument includes repeated roots of \(P_c\) because it sums over field elements, never root multiplicities.

**4. Identify elliptic traces and the singular degeneration.** If \(c\ne0\), the cubic \(4v^3+2cv\) is squarefree in characteristic at least five: a common root with derivative \(12v^2+2c\) would imply \(v=0=c\). Hence its projective equation \(w^2=P_c(v)\) is elliptic. Its point count is \(q+1+C_c\), giving \(a_q(c)=-C_c\). The standard Hasse bound gives \(|a_q(c)|\le2\sqrt q\).

If \(c=0\), then \(C_0=\sum_v\chi(4v^3)=\sum_v\chi(v)=0\), the only distinct root of \(P_0\) is \(v=0\), and so \(H_0=\chi(-1/4)=\chi(-1)\), \(J_0=\chi(1)=1\). Thus \(E_0=2q^2-q+q\chi(3)(1+\chi(-1))\). For any finite field of characteristic at least five, \(\chi(-1)\) and \(\chi(3)\) have their usual character values according to \(q\bmod4\) and \(q\bmod12\), respectively. The three listed cases follow for all prime powers, not merely prime \(q\).

**5. Fourier interpretation.** Expand the mixed Fourier moment into sums over \((t,t',u,u')\). Averaging over \((\xi,\eta)\in F^2\) uses nontrivial additive-character orthogonality and enforces
\[
(t,t^3)+(u,u^4+cu^2)=(t',t'^3)+(u',u'^4+cu'^2).
\]
Each such quadruple contributes one, and all others contribute zero. The average is therefore exactly \(E_c\).

## Verification

The standalone file `verify.py` uses Python 3 standard-library integer arithmetic. Run `python verify.py` in its extracted directory. For all parameters \(c\) in each of the nine prime fields of orders \(5,7,11,13,17,19,23,29,31\), it directly enumerates ordered mixed convolution targets, squares their multiplicities, and compares against the closed formula. It independently tests six parameter choices in each quadratic extension field of orders \(25,49,121,169\), represented explicitly by irreducible quadratic polynomials. In total, the tests cover \(179\) parameter/field pairs and verify the elliptic point-count identity, Hasse-bound sanity check, and undeformed specialization. The exact reproduced summary is embedded in `verification_output.txt`.

A symbolic expansion independently checked the key shift identity in Step 1. Neither the 179 finite instances nor the symbolic check replaces the general character-sum proof.

## Relationship to prior work

González-Riquelme and Oliveira e Silva [1] establish sharp finite-field Fourier extension inequalities for paraboloids and cones and develop precise convolution-count methods. Their Theorems 1.1–1.3 and §3 treat self-convolutions of those quadratic surfaces, not the **mixed** convolution of a cubic and an even quartic graph.

The published exact quartic-graph energy [2] concerns collisions in \(B_0+B_0\). The published sharp cubic-graph Fourier-extension theorem [3] concerns \(A+A\) and its weighted extremizers. The present energy instead concerns \(A+B_c\), with a different collision equation, a trace of \(w^2=4v^3+2cv\), and a three-regime congruence law at \(c=0\). Neither self-energy result determines mixed energy from its statement, and their proof identities involve different pair-sum fibers. Hughes and Wooley [4] study high moments of cubic polynomial sequences on the integer torus, not this finite-field mixed fourth moment.

## Limitations

The result computes an exact **constant-input mixed fourth moment**, not the sharp bilinear extension operator norm for arbitrary coefficient functions; it also does not classify every target fiber \(r_c(s,y)\). Characteristics two and three are not addressed. The elliptic-trace language applies only when \(c\ne0\). A search of available literature and mathematical-result records found no equivalent theorem, but an older unindexed mixed character-sum identity or an unsuspected specialization of a more general formula remains a residual bibliographic risk. No independent audit has been performed.

## References

1. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1 (26 May 2024), https://arxiv.org/html/2405.16647v2.
2. *Exact additive energy of the finite-field quartic graph*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-additive-energy-of-the-finite-field-quartic-graph--235f10989b3f.
3. *Sharp cubic-graph Fourier extension and its inflection-point deficit*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-cubic-graph-fourier-extension-and-its-inflection-point-def--5a2b58c43575.
4. K. Hughes and T. D. Wooley, *Discrete restriction for \((x,x^3)\) and related topics*, arXiv:1911.12262 (27 November 2019), https://arxiv.org/abs/1911.12262.
