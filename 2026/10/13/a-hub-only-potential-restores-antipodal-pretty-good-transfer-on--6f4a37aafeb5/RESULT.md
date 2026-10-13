# A hub-only potential restores antipodal pretty good transfer on the five-vertex wheel, but never perfect transfer

## Finding
Let \(W_5=K_1\vee C_4\) be the five-vertex wheel. Put a real onsite potential \(q\) only at the hub, and use the continuous-time Hamiltonian \(H(q)=A(W_5)+q|h\rangle\langle h|\). Between opposite rim vertices, **perfect state transfer never occurs, at any real potential**. Pretty good state transfer (PGST) occurs for **every transcendental real \(q\)**. For **rational** \(q\), PGST occurs if and only if both conditions hold:
\[
\operatorname{den}\!\left(\frac{q+2}{4}\right)\ \text{is odd},\qquad
(q-2)^2+16\notin (\mathbb Q)^2,
\]
where \(\operatorname{den}\) denotes the positive denominator after reducing a rational number to lowest terms. Successful approximating times in these cases may all be chosen as \(t=s\pi/2\), with \(s\) positive and odd. For instance, \(q=-2\) enables PGST whereas \(q=0\) does not. Irrational algebraic potentials are not classified by this statement.

## Assumptions and scope
The rim is the undirected four-cycle with labels \(0,1,2,3\); the hub \(h\) is connected by unit-weight edges to every rim vertex. All cycle edges also have unit weight, the sole diagonal entry is \(H_{hh}=q\), and \(U_q(t)=\exp(itH(q))\). PGST from \(0\) to \(2\) means there are positive times \(t_j\) with \(|\langle2|U_q(t_j)|0\rangle|\to1\). Perfect transfer means that this modulus equals one at a finite positive time. The theorem makes no assertion about arbitrary multi-vertex onsite controls, other wheel orders, or irrational algebraic values excluded from the sufficient transcendence clause.

## Proof
Set
\[
 a=\tfrac12(1,1,1,1,0),\quad b=\tfrac12(1,-1,1,-1,0),\quad c=2^{-1/2}(1,0,-1,0,0),\quad h=(0,0,0,0,1).
\]
These are orthonormal, and the two target coordinate vectors satisfy
\[
 |0\rangle=\tfrac12a+\tfrac12b+2^{-1/2}c,\qquad
 |2\rangle=\tfrac12a+\tfrac12b-2^{-1/2}c.
\]
The vector \(b\) has eigenvalue \(-2\); \(c\) has eigenvalue \(0\). On \(\operatorname{span}\{a,h\}\), the Hamiltonian has matrix
\[
 B(q)=\begin{pmatrix}2&2\\2&q\end{pmatrix},\quad
 \lambda_\pm=\frac{q+2\pm\sqrt{(q-2)^2+16}}2.
\]
The \(a\)-coordinate has strictly positive spectral weight at both distinct eigenvalues \(\lambda_\pm\), because the off-diagonal entries of \(B(q)\) equal two. Consequently transfer from \(0\) to \(2\) has modulus one precisely when the phases of \(b,a\)'s two eigencomponents all equal \(-1\), while the \(c\)-phase equals \(+1\). Equivalently,
\[
 e^{-2it}=e^{it\lambda_+}=e^{it\lambda_-}=-1.\tag{1}
\]
The same spectral weights show that PGST is equivalent to simultaneous *approximation* of these three phase equalities.

**No perfect transfer.** Equation (1) forces \(t=s\pi/2\) with a positive odd integer \(s\) and forces \(s\lambda_\pm/2=u_\pm\) for odd integers \(u_+,u_-\). Since
\[
 \lambda_++\lambda_-=q+2,\qquad \lambda_+\lambda_-=2q-4,
\]
these relations imply
\[
 (u_+-s)(u_--s)=-s^2.\tag{2}
\]
The left side is divisible by four, while the right side is odd. Thus (2) is impossible for every real \(q\).

**Every transcendental potential gives PGST.** For transcendental \(q\), the numbers \(1,\lambda_+/4,\lambda_-/4\) are linearly independent over \(\mathbb Q\). Indeed, a rational dependence with equal coefficients on \(\lambda_+\) and \(\lambda_-\) would force \(q\) rational. A dependence with unequal coefficients would force \(\sqrt{(q-2)^2+16}\) to equal a rational-affine function of \(q\). Squaring would yield a nonzero rational polynomial vanishing at transcendental \(q\), impossible: \((X-2)^2+16\) is not the square of a rational-affine polynomial. Kronecker's theorem then makes the odd subsequence
\[
 \left(\frac{s\lambda_+}4,\frac{s\lambda_-}4\right)\pmod 1,
 \qquad s=1,3,5,\ldots,
\]
dense in the two-dimensional torus. Choosing it close to \((1/2,1/2)\) ensures \(e^{i(s\pi/2)\lambda_\pm}\to-1\); the \(-2\) phase equals \(-1\) exactly. Therefore PGST holds.

**Rational potentials: necessity.** For rational \(q\), suppose PGST holds. The \(-2\) phase tending to \(-1\) implies any approximating times can be written as \(t_j=s_j\pi/2+o(1)\), with odd integers \(s_j\). Multiplying the limiting \(\lambda_+\)- and \(\lambda_-\)-phases gives \(e^{it_j(q+2)}\to1\). Hence \(e^{i\pi s_j(q+2)/2}\to1\). Because \(q\) is rational, these phases form a finite set. One of them must equal one; thus there exists an odd integer \(s\) with \(s(q+2)/4\in\mathbb Z\), exactly the stated odd-denominator condition. If \(\Delta=(q-2)^2+16\) were a rational square, all active frequencies would be rational. The one-parameter phase orbit would then be periodic and closed, so PGST would entail PST, already disproved. Hence \(\Delta\) is not a rational square.

**Rational potentials: sufficiency.** Conversely let \(q\in\mathbb Q\), \(\Delta\notin(\mathbb Q)^2\), and \((q+2)/4=a/b\) with \(a\in\mathbb Z\), positive odd \(b\), and \(\gcd(a,b)=1\). Choose \(s=b(2j+1)\), with \(j\ge0\). Then \(s(q+2)/4=a(2j+1)\) is an integer of fixed parity. The sequence \(s\sqrt\Delta/4\pmod2\) is dense in \(\mathbb R/2\mathbb Z\), since \(b\sqrt\Delta/2\) is irrational. Select \(j\)'s for which this sequence approaches the opposite parity class, i.e. approaches \(1-a\pmod2\). It follows that both
\[
 \frac{s\lambda_\pm}{2}=\frac{s(q+2)}4\pm\frac{s\sqrt\Delta}4
\]
approach odd integers modulo two. Their time phases approach \(-1\), establishing PGST at \(t=s\pi/2\). This completes the classification claimed.

## Verification
The accompanying portable `verify.py` checks the exact invariant subspaces, trace, determinant, and discriminant for 1,267 rational inputs. It separately checks finite parity samples, nine rational boundary examples, the first five negative-Pell approximants at \(q=-2\), and a numerical odd-time witness for \(q=e\). Run `python3 verify.py` with Python 3 standard library. The finite tests are corroboration; all universal assertions rest on the preceding exact proof and Kronecker's theorem.

## Relationship to prior work
Coutinho, Ferreira Baptista, Godsil, Spier, and Werner, *Irrational quantum walks*, arXiv:2208.08971 (first public 2022-08-18), develops exact spectral and Diophantine methods for quantum walks generated by integral Hamiltonians. For each rational hub potential, clearing denominators lets its general integral-Hamiltonian decision methods apply after time rescaling, but those per-instance methods do not state the explicit family-wide arithmetic classification here. At transcendental potentials the Hamiltonian is not integral up to rational rescaling. The unperturbed five-vertex wheel is known not to admit this antipodal PGST; the \(q=0\) negative case is not claimed as new.

Kempton, Lippner, and Yau, *Perfect state transfer on graphs with a potential*, arXiv:1611.02093, prove that nonadjacent twin vertices can exhibit PST when suitable onsite potentials are allowed across the graph. Their existence theorem allows a much larger family of controls and does not imply PST using a potential **only at the hub**. Drazen, Kempton, and Lippner, *Pretty good fractional revival via magnetic fields: theory and examples*, arXiv:2311.18143, provides a related diagonal-perturbation method, but does not state the hub-only five-vertex-wheel rational/transcendental criterion. These previously published spectral and Diophantine techniques are credited; the claimed novelty is the exact one-control obstruction and the arithmetic PGST boundary for this specified network.

## Limitations
No classification for irrational algebraic \(q\) is asserted. The theorem does not rule out PST after changing more than the hub's onsite energy, nor does it address robustness to other edge weights. Closely related diagonal-perturbation and twin-vertex theories make an unindexed equivalent specialization a residual literature risk. Direct finite computation is not an infinite existence proof.

## References
1. G. Coutinho, P. Ferreira Baptista, C. Godsil, T. J. Spier, R. Werner, *Irrational quantum walks*, arXiv:2208.08971, 2022; https://arxiv.org/abs/2208.08971.
2. M. Kempton, G. Lippner, S.-T. Yau, *Perfect state transfer on graphs with a potential*, arXiv:1611.02093, 2016; https://arxiv.org/abs/1611.02093.
3. W. Drazen, M. Kempton, G. Lippner, *Pretty good fractional revival via magnetic fields: theory and examples*, arXiv:2311.18143, 2023; https://arxiv.org/abs/2311.18143.
