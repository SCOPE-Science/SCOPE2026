# Exact return-shift law for ramified quadratic p-adic maps

## Finding
Let \(p\ge5\) be prime and \(c\in\mathbb Z_p\) satisfy \(v_p(1-4c)=1\). Put \(f_c(x)=x^2+c\), \(\delta=1-4c\), and \(B=\frac12+p\mathbb Z_p\). Then \(B\) is invariant, has no fixed point of \(f_c\), and for every \(x\in B\) and integer \(n\ge0\),
\[
f_c^{\,p^n}(x)\equiv x-\frac{p^n\delta}{4}\pmod{p^{n+2}}.
\]
Thus, modulo \(p^m\), the \(p^{m-1}\) residue classes contained in \(B\) form one cycle of length \(p^{m-1}\), for every \(m\ge1\). In particular, \(f_c|_B\) is minimal and is topologically conjugate to the \(p\)-adic adding machine.

## Assumptions and scope
The coefficient \(c\) lies in the ring of \(p\)-adic integers. The valuation condition means \(\delta=pu\) for a unit \(u\in\mathbb Z_p^\times\). Since \(p\) is odd, \(1/2\) and \(1/4\) are elements of \(\mathbb Z_p\). The restriction \(p\ge5\) is essential to the proof below: the sum of squares of all residues modulo \(p\) vanishes modulo \(p\) precisely in the prime range used here. No global classification outside \(B\) is asserted.

## Proof
Write \(a=-\delta/(4p)\), a unit of \(\mathbb Z_p\), and use the affine coordinate \(x=\frac12+pt\). Direct expansion gives
\[
f_c\!\left(\frac12+pt\right)=\frac12+p g(t),\qquad g(t)=t+a+pt^2.
\]
Hence \(B\) is invariant and the restricted map is conjugate to \(g\) on \(\mathbb Z_p\). Also,
\[
f_c(x)-x=\left(x-\frac12\right)^2-\frac{\delta}{4}.
\]
For \(x\in B\), the square term is divisible by \(p^2\), whereas \(\delta/4\) has valuation one; therefore \(f_c(x)\ne x\).

Let \(t_j=g^j(t)\). The recursion \(t_{j+1}=t_j+a+pt_j^2\) gives
\[
g^p(t)=t+pa+p\sum_{j=0}^{p-1}t_j^2.
\]
Modulo \(p\), \(t_j\equiv t+ja\). As \(a\) is a unit, these are all residues modulo \(p\), and
\[
\sum_{r=0}^{p-1}r^2=\frac{p(p-1)(2p-1)}6\equiv0\pmod p
\]
for every prime \(p\ge5\). Thus \(g^p(t)\equiv t+pa\pmod{p^2}\), while \(g(t)\equiv t+a\pmod p\).

For the lift, set \(G_n=g^{p^n}\). The derivative identities \(g'(t)=1+2pt\equiv1\pmod p\) and \(g''(t)=2p\equiv0\pmod p\) imply \(G_n'(t)\equiv1\pmod p\) and \(G_n''(t)\equiv0\pmod p\) for every \(n\ge0\). Suppose \(n\ge1\) and \(G_n(t)\equiv t+p^n a\pmod{p^{n+1}}\). Taylor expansion at \(t\), with increments divisible by \(p^n\), has remainder divisible by \(p^{n+2}\): the quadratic coefficient is divisible by \(p\), and terms of degree at least three have valuation at least \(3n\ge n+2\). If \(\lambda=G_n'(t)\), then \(\lambda\equiv1\pmod p\) and \(\sum_{j=0}^{p-1}\lambda^j\equiv p\pmod{p^2}\). Iterating the first-order expansion therefore yields
\[
G_n^p(t)\equiv t+p^{n+1}a\pmod{p^{n+2}}.
\]
Induction proves \(g^{p^n}(t)\equiv t+p^n a\pmod{p^{n+1}}\) for every \(n\ge0\). Returning to \(x=\frac12+pt\), and using \(pa=-\delta/4\), gives the displayed return-shift congruence.

The shift at level \(p^{n+2}\) has valuation exactly \(n+1\), so each return cycle advances through all \(p\) lifts at the next precision. Starting with the single residue class of \(B\) modulo \(p\), induction shows that the quotient of \(B\) modulo \(p^m\) is one cycle of length \(p^{m-1}\). These cycles are compatible under reduction; their inverse limit is the adding-machine system on \(\mathbb Z_p\). Hence every orbit in \(B\) is dense and the restriction is minimal.

## Verification
The proof uses an exact affine conjugacy, the finite-field identity \(\sum_{r\in\mathbb F_p}r^2=0\) for \(p\ge5\), and an induction on the return iterate. The specialization \(p=5\), \(c=-1\) gives \(f(x)=x^2-1\), \(B=3+5\mathbb Z_5\), and \(f^5(3)\equiv28\pmod{125}\), agreeing with the formula. This finite congruence is a sanity check only; the induction supplies the infinite-level proof.

## Relationship to prior work
Fan and Liao establish a general minimal-decomposition theory for polynomial maps on \(\mathbb Z_p\), including cycle-lifting tools and the fact that minimal clopen components are odometers [1]. Their detailed classification of arbitrary quadratic polynomials in that paper is for \(p=2\), not this odd-prime family. Their later paper completely treats the square map \(x\mapsto x^2\), which is different from \(x\mapsto x^2+c\) [2]. Jeong's general ergodicity criteria apply after the affine change of variables and already cover the minimality consequence; in particular, for \(p\ge5\), \(g(t)=a+t+p\Delta H(t)\) with \(H(t)=t^3/3-t^2/2+t/6\) and \(\Delta H(t)=H(t+1)-H(t)=t^2\) [3]. The present claim is therefore not a novelty claim for minimality alone: it is the explicit return-shift coefficient \(-\delta/4\) at every precision, which those general criteria do not state. A search of the inspected primary texts and the available claim index did not locate this exact family-level formula; that bounded search is not proof of absolute novelty.

## Limitations
The theorem excludes \(p=2\) and \(p=3\); the sum-of-squares step used in the base lift does not apply unchanged at \(p=3\). It does not classify the complement of \(B\), nor does it claim a new general criterion for p-adic ergodicity. Existing cycle-lifting theory is closely related, and an unindexed source may contain the same explicit congruence. Independent audit has not been performed.

## References
[1] A.-H. Fan and L. Liao, “On minimal decomposition of p-adic polynomial dynamical systems,” arXiv:1010.5583 (first public version 2010-10-27).

[2] S. Fan and L. Liao, “Dynamics of the square mapping on the ring of p-adic integers,” arXiv:1408.4574 (first public version 2014-08-20).

[3] S. Jeong, “Toward the ergodicity of p-adic 1-Lipschitz functions represented by the van der Put series,” arXiv:1210.5001 (first public version 2012-10-18).

[4] A.-H. Fan, S. Fan, L. Liao, and Y. Wang, “Minimality of p-adic rational maps with good reduction,” arXiv:1511.04856 (first public version 2015-11-16).
