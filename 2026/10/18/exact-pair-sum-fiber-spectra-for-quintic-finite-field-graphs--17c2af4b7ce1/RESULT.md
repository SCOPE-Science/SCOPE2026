# Exact pair-sum fiber spectra for quintic finite-field graphs

## Finding

Let \(q=p^r\), where \(p\ge7\) is prime and \(r\ge1\). For the graph
\[
C_5=\{(t,t^5):t\in\mathbb F_q\}\subset\mathbb F_q^2,
\]
define the ordered pair-sum multiplicities
\[
R(s,z)=\#\{(x,y)\in\mathbb F_q^2:x+y=s,\ x^5+y^5=z\}.
\]
Let \(\chi\) be the quadratic character of \(\mathbb F_q\), extended by \(\chi(0)=0\), and put \(\varepsilon=\chi(-1)\), \(\eta=\chi(-2)\). For every \(s\ne0\), the number of \(z\in\mathbb F_q\) with \(R(s,z)=j\) is exactly
\[
\begin{array}{c|ccccc}
j&0&1&2&3&4\\ \hline
\#\{z:R(s,z)=j\}&
\frac{5q-4+2\eta-3\varepsilon}{8}&
\frac{1-\eta}{2}&
\frac{q+3\varepsilon}{4}&
\frac{1+\eta}{2}&
\frac{q-4-2\eta-3\varepsilon}{8}.
\end{array}
\]
These are nonnegative integers and their sum is \(q\). On the zero-sum row, \(R(0,0)=q\) and \(R(0,z)=0\) for \(z\ne0\).

Consequently the exact additive energy of the graph is
\[
\boxed{\mathcal A(C_5)=\sum_{s,z}R(s,z)^2
=q^2+3(q-1)(q-1-\varepsilon)
=4q^2-6q+3-3\varepsilon(q-1).}
\]
The full fiber spectrum records both \(\chi(-1)\) and \(\chi(-2)\), whereas the energy depends only on \(\chi(-1)\).

For any nontrivial additive character \(\psi\) and the normalized extension operator
\[
\mathcal E f(\xi,\upsilon)=q^{-1}\sum_{t\in\mathbb F_q}f(t)\psi(\xi t+\upsilon t^5),
\]
with counting measure on the dual plane, the constant-input fourth moment is therefore
\[
\boxed{\|\mathcal E\mathbf1\|_{\ell^4(\mathbb F_q^2)}^4
=\frac{\mathcal A(C_5)}{q^2}
=4-\frac6q+\frac3{q^2}-\frac{3\varepsilon(q-1)}{q^2}.}
\]
This is an exact value for constant input, **not** a claim of the sharp \(L^2\)-to-\(\ell^4\) operator norm.

## Assumptions and scope

All field operations and character symbols are in \(\mathbb F_q\), and \(\chi(a)\in\{-1,0,1\}\). The assumption \(p\ge7\) ensures that \(2\), \(5\), and \(16\) are invertible; it also permits the same argument over all extension degrees \(r\ge1\). The quantity \(R(s,z)\) counts ordered pairs, so a pair of distinct elements contributes two and a repeated element contributes one. Both the histogram and the energy include all frequency and sum parameters. No assertion is made about characteristics \(2,3,5\) or the optimizing complex-valued weights for this graph.

## Proof

**1. Reduction to two quadratic discriminants.** Fix \(s\ne0\), write \(y=s-x\), and set \(u=xy/s^2\). The fifth Newton identity gives
\[
\frac{x^5+y^5}{s^5}=1-5u+5u^2.
\]
The quantity \(\delta=1-4u=((x-y)/s)^2\) satisfies
\[
\frac{x^5+y^5}{s^5}=\frac5{16}(\delta+1)^2-\frac14.
\]
The number of ordered solutions with a prescribed \(\delta\) is \(1+\chi(\delta)\), since \(x=(s/2)(1+v)\) and \(v^2=\delta\). Let \(w=(\delta+1)^2\); multiplication by \(5s^5/16\) and translation biject \(w\) with the possible second sum coordinates \(z\). If \(w\) is a nonsquare, its fiber has size zero. If \(w=0\), then \(\delta=-1\) and its fiber has size \(1+\varepsilon\). If \(w=1\), the two values \(\delta=0,-2\) give fiber size \(2+\eta\). For every other nonzero square \(w\), the two values \(\delta=-1\pm\sqrt w\) are nonzero and the fiber size is \(2+\chi(\delta_+)+\chi(\delta_-)\in\{0,2,4\}\).

**2. Exact character count.** Put \(\delta'=-2-\delta\). For \(\delta\ne0,-2\), the pair \(\{\delta,\delta'\}\) describes one nonzero square \(w\), except for the fixed value \(\delta=-1\), which corresponds to \(w=0\). Elementary quadratic-character orthogonality gives
\[
\sum_{\delta\in\mathbb F_q}\chi(\delta\delta')=-\varepsilon.
\]
Indeed, \(\delta\delta'=1-(\delta+1)^2\); the count of solutions of \(a^2-b^2=1\) is \(q-1\) via \((a-b)(a+b)=1\), so \(\sum_a\chi(a^2-1)=-1\) and multiplication by \(\chi(-1)\) gives the displayed identity. Furthermore,
\[
\sum_{\delta\ne0,-2}\chi(\delta)
=\sum_{\delta\ne0,-2}\chi(\delta')=-\eta.
\]
Applying the indicators \((1\pm\chi(\delta))/2\), subtracting the possible fixed point at \(\delta=-1\), and dividing by two for the nonfixed involution orbits yields
\[
N_{++}=\frac{q-4-2\eta-3\varepsilon}{8},\qquad
N_{--}=\frac{q-4+2\eta+\varepsilon}{8}.
\]
These count respectively the nonzero-square \(w\ne1\) with two square discriminants and with two nonsquare discriminants. Among the remaining \((q-3)/2\) nonzero-square \(w\ne1\), exactly
\[
N_{+-}=\frac{q-2+\varepsilon}{4}
\]
have one discriminant of each sign. Including the special values \(w=0,1\) and the \((q-1)/2\) nonsquare values of \(w\) proves all five histogram entries in the Finding. Since they count actual fibers, integrality and nonnegativity follow without additional congruence assumptions.

**3. Zero row and energy.** If \(s=0\), then \(y=-x\), so \(x^5+y^5=0\) for all \(q\) choices of \(x\). For each \(s\ne0\), the histogram gives
\[
\sum_z R(s,z)^2=1^2N_1+2^2N_2+3^2N_3+4^2N_4
=3(q-1-\varepsilon).
\]
Adding the zero row's contribution \(q^2\) gives the energy formula.

**4. Fourier fourth moment.** Expand \(\sum_{\xi,\upsilon}|\sum_t\psi(\xi t+\upsilon t^5)|^4\). Orthogonality of nontrivial additive characters makes this sum equal to \(q^2\mathcal A(C_5)\). The normalization factor \(q^{-4}\) from the four extension factors yields \(\|\mathcal E\mathbf1\|_4^4=q^{-2}\mathcal A(C_5)\), exactly as claimed. This argument applies to every nontrivial additive character and every permitted extension field.

## Verification

The standalone standard-library program `verify_quintic.py` reconstructs all \(q^2\) ordered pairs and every \(s\)-row histogram with exact integer arithmetic for nine prime fields and the extension fields of orders \(49\) and \(121\). It checks the three energy formulas and independently compares direct complex Fourier fourth moments for prime fields of orders \(7,11,13\). The program reports `VERIFY_OK`, with 11 fields, 346 nonzero rows, and 21,731 ordered pairs inspected. These examples are finite corroboration; the algebraic steps above prove the unrestricted statement.

## Relationship to prior work

Koh and Shen (2010, Theorem 1.1) establish the finite-field \(L^2\)-to-\(L^4\) extension *boundedness* criterion for algebraic plane curves without linear factors. It applies to the quintic graph but gives neither its exact two-sum histogram nor the constant-input fourth moment. González-Riquelme and Oliveira e Silva (2024, introductory Theorems 1.1–1.6) compute sharp extension inequalities on selected paraboloids, a parabola, and cones, rather than this fifth-power graph. Related published work on the quartic monomial graph computes its constant-input additive energy, but changes in degree modify the collision polynomial and do not imply the quintic character-discriminant census. An equivalent specialized historical identity is not ruled out.

## Limitations

This theorem does not optimize the fourth moment over arbitrary nonconstant weights \(f\), determine a sharp operator norm, or treat excluded characteristics. Exact novelty in the entire older character-sum literature cannot be certified from the inspected sources. The finite checker is supplementary to the displayed proof. Independent mathematical audit has not been performed.

## References

1. D. Koh and C.-Y. Shen, *Sharp extension theorems and Falconer distance problems for algebraic curves in two dimensional vector spaces over finite fields*, arXiv:1003.4240 (first posted 2010-03-22), Theorem 1.1 and Section 3.
2. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v2 (2024), Introduction, Theorems 1.1–1.6.
3. *Exact additive energy of the finite-field quartic graph*, published mathematical research record (2026), used for an adjacent-degree comparison, not as proof of the quintic claim.
