# Complete Gabor-projector spectra of split quadratic graphs over every finite field

## Finding

For every prime power \(q\) and integer \(r\ge2\), let \(F=\mathbb F_q\), \(G=F^r\times F^r\times F\), and \(D=|G|=q^{2r+1}\). The split quadratic graph and its unit vector are
\[
C=\{(x,y,z)\in G:z=x\cdot y\},\qquad g=q^{-r}\mathbf1_C\in\mathbb C^G.
\]
Using every translation and additive-character modulation of \(g\), form the \(D^2\) rank-one projectors and their unweighted Hilbert--Schmidt Gram matrix \(K\). Put
\[
B=q^{2r-1}+(q-1)q^{r-1}.
\]
**The following list gives every eigenvalue of \(K\), with its complete multiplicity.**

When \(q\) is odd, the nonzero eigenvalues and multiplicities are
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
D&1\\
q^{2r-1}&q^2(q^{2r}-1)\\
q&(q-1)q^{2r}B\\
1&(q-1)q^{2r+1}(q^{2r}-B).
\end{array}
\]
When \(q\) is even, the nonzero eigenvalues and multiplicities are
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
D&1\\
q^{2r-1}&q^2(q^{2r}-1)\\
q&(q-1)q^{4r}.
\end{array}
\]
In both cases, zero has multiplicity \(D^2\) minus the sum of the displayed multiplicities. In particular, these sums are the **exact complex linear ranks of the Gabor intensity-lifting operators**, which fail complete arbitrary-matrix tomography. For fixed field order \(q\) and increasing \(r\), the identifiable fraction tends to
\[
\lim_{r\to\infty}\frac{\operatorname{rank}K}{D^2}=
\begin{cases}
\dfrac{(q-1)(q^2-q+1)}{q^3},&q\text{ odd},\\[2mm]
\dfrac{q-1}{q^2},&q\text{ even}.
\end{cases}
\]
The eigenvalue lists, not just the ranks, are sharp and exhaustive.

## Assumptions and scope

The dot product in the definition of \(C\) is the standard bilinear form on \(F^r\). Fix any nontrivial additive character \(\psi:F\to\mathbb C^\times\). A modulation by \(\eta=(u,v,w)\in G\) acts at \(t=(x,y,z)\in G\) as \(\psi(u\cdot x+v\cdot y+wz)\); a translation by \(h\in G\) shifts the argument by \(h\). Multiplication of modulations and translations is only projective, but their projectors are unambiguous. Every coefficient of \(g\) on \(C\) is \(q^{-r}\), and \(\|g\|_2=1\) since \(|C|=q^{2r}\). The Gram matrix uses the ordinary Hilbert--Schmidt inner product, not a dimension-rescaled convention.

The classification is for **all** finite fields of both characteristics and every \(r\ge2\). It concerns linear identifiability of arbitrary complex matrices and gives no unproved assertion about nonlinear pure-signal phase retrieval.

## Proof

**1. General finite-Gabor diagonalization.** Put \(W_{h,\eta}=M_\eta T_h\), \(\Pi_{h,\eta}=|W_{h,\eta}g\rangle\langle W_{h,\eta}g|\), and
\[
A(h,\eta)=\langle g,W_{h,\eta}g\rangle.
\]
The \(D^2\) Weyl operators, each divided by \(\sqrt D\), form an orthonormal basis of the complex matrix space. Weyl conjugation acts on each basis operator by a character of \(G\times\widehat G\). Therefore the projector orbit analysis map is a unitary character transform followed by diagonal multipliers \(\sqrt D\,A(h,\eta)\), up to harmless phases and a permutation. Equivalently its projector Gram matrix has eigenvalues \(D|A(h,\eta)|^2\) once each. This is the finite-abelian-group version of the Gabor-projector Gram diagonalization in [2]; the Weyl-basis argument just given independently establishes the normalization.

**2. Reduction to a quadratic sum.** Let \(h=(a,b,c)\) and \(\eta=(u,v,w)\), where \(a,b,u,v\in F^r\). Set \(d=c-a\cdot b\). A point \((x,y,x\cdot y)\) and its translate by \(h\) both lie on \(C\) precisely when
\[
a\cdot y+b\cdot x=d.
\]
Hence, ignoring a unit phase which cannot affect magnitudes,
\[
A(h,\eta)=q^{-2r}\sum_{a\cdot y+b\cdot x=d}
\psi(u\cdot x+v\cdot y+w x\cdot y).
\]
Insert additive-character orthogonality for the linear constraint. When \(w\ne0\), successive summation over \(y\) and \(x\) yields
\[
A(h,\eta)=q^{-r-1}\psi(-u\cdot v/w)
\sum_{s\in F}\psi\!\left(
-\frac{(a\cdot b)s^2+(wd+u\cdot a+v\cdot b)s}{w}
\right).
\tag{1}
\]
This formula includes zero shifts and every field characteristic.

**3. Cases for \(w=0\).** If \((a,b)=(0,0)\), a nonempty overlap requires \(c=0\); then the Fourier transform of the graph at \(w=0\) is nonzero only for \(u=v=0\), where \(|A|=1\). If \((a,b)\ne(0,0)\), for every \(c\) the overlap is a nonempty affine hyperplane of size \(q^{2r-1}\). Its Fourier transform vanishes unless \((u,v)=s(b,a)\) for one of the \(q\) scalars \(s\in F\), and each surviving coefficient has \(|A|=q^{-1}\). There are therefore \(q^2(q^{2r}-1)\) coefficients of magnitude \(q^{-1}\).

**4. Cases for \(w\ne0\), odd characteristic.** If \(a\cdot b\ne0\), the quadratic coefficient in (1) is nonzero. The complete quadratic Gauss sum has magnitude \(\sqrt q\), independently of its linear coefficient, so \(|A|=q^{-r-1/2}\) for every \(c,u,v,w\). If \(a\cdot b=0\), the summand is additive-linear in \(s\): it vanishes unless
\[
wd+u\cdot a+v\cdot b=0,
\]
where it has magnitude \(q^{-r}\). For \((a,b)\ne(0,0)\), this equation holds for exactly \(q^{2r-1}\) choices of \((u,v)\) at each \(c,w\); if \((a,b)=0\), it is equivalent to \(c=0\) and all \(q^{2r}\) pairs \((u,v)\) survive. The number of pairs \((a,b)\) satisfying \(a\cdot b=0\) is
\[
B=q^r+(q^r-1)q^{r-1}=q^{2r-1}+(q-1)q^{r-1}.
\]
After including the zero pair, the number of coefficients with \(|A|=q^{-r}\) is \((q-1)q^{2r}B\). The number with \(|A|=q^{-r-1/2}\) is \((q-1)q^{2r+1}(q^{2r}-B)\). All other coefficients in these cases vanish.

**5. Cases for \(w\ne0\), characteristic two.** Every nontrivial additive character has the form \(\psi(t)=(-1)^{\operatorname{Tr}_{F/\mathbb F_2}(\beta t)}\) with \(\beta\ne0\). Therefore the function \(s\mapsto\psi(\alpha s^2+\gamma s)\) is an additive character of \((F,+)\), **even when \(\alpha\ne0\)**. Its sum equals either \(q\) or zero. For each nonzero \((a,b)\), fixed \(c,w\ne0\), the additive-character coefficient varies nontrivially with \((u,v)\), so exactly \(q^{2r-1}\) of the \(q^{2r}\) pairs survive. The zero \((a,b)\) case is as in Step 4. Combining these gives \((q-1)q^{4r}\) coefficients of magnitude \(q^{-r}\), with no intermediate Gauss magnitude.

**6. Eigenvalues, exact rank, and asymptotics.** Multiplication of the squared magnitudes \(1\), \(q^{-2}\), \(q^{-2r}\), and (odd characteristic only) \(q^{-2r-1}\) by \(D=q^{2r+1}\) gives the displayed eigenvalues. The preceding disjoint counts give their precise multiplicities. Every remaining Fourier multiplier is zero, so its Weyl matrix lies in the lifting kernel. Finally, division of each multiplicity sum by \(q^{4r+2}\) and passage to \(r\to\infty\) gives the two displayed limiting fractions. A trace check gives \(\sum \lambda =D^2\), matching the sum of Hilbert--Schmidt norms squared of all \(D^2\) unit projectors.

## Verification

The standalone Python checker `checks/verify_graph.py` directly enumerates overlap sets and additive characters, without using the Gauss-sum classification as input, for \((q,r)=(2,1),(3,1),(4,1),(5,1),(2,2),(3,2)\). These include odd, prime-power, and characteristic-two examples, with the nontrivial field \(\mathbb F_4\) implemented by a polynomial quotient. Every enumerated magnitude histogram equals the theorem's predicted histogram. The test at \((2,1)\) also permits an independent direct construction and diagonalization of the \(64\)-projector Gram matrix, with eigenvalue multiplicities \(35,28,1\) at eigenvalues \(0,2,8\) respectively. The infinite statement rests on the proof, not these samples.

## Relationship to prior work

Iosevich--Koh--Lewko [1] study restriction estimates and additive energies on finite-field paraboloids. Goldberger--Kang--Okoudjou [2] establish the finite Gabor-projector eigenvalue method. The complete spectrum here specializes that general method to the indicator of a **split quadratic graph**, including both characteristics and all dimensions specified above. The individual Gauss-sum and Weyl facts are standard ingredients, not claimed as new.

A separate classification of Gabor ranks for **hyperbolic quadratic level-one shells** in even-dimensional spaces has also appeared [3]. That object is \(\{(x,y):x\cdot y=1\}\subset F^{2r}\), not the present graph \(\{(x,y,x\cdot y)\}\subset F^{2r+1}\); the ambient translation groups, intersection geometry, and resulting ambiguity transforms differ. The shell classification does not give the new even-characteristic graph spectrum or the four-band odd-characteristic formula by restriction or substitution.

## Limitations

No universal pure-state phase-retrieval conclusion, quantitative nonlinear stability estimate, or claim of informational completeness is asserted. The exact spectrum is for the uniform, unit-normalized indicator of the named split quadratic graph; weighted windows and arbitrary quadratic surfaces are outside scope. Public literature searching is not a proof of publication priority; an unindexed equivalent graph-spectrum calculation could exist. Independent audit has not been performed.

## References

1. A. Iosevich, D. Koh, and M. Lewko, *Finite field restriction estimates for the paraboloid in high even dimensions*, arXiv:1712.05549v1, first posted 2017-12-15, https://arxiv.org/abs/1712.05549.
2. A. Goldberger, S. Kang, and K. A. Okoudjou, *Towards a classification of incomplete Gabor POVMs in \(\mathbb C^d\)*, arXiv:2106.01509v1, first posted 2021-06-02, https://arxiv.org/abs/2106.01509.
3. *Exact Gabor tomography rank for hyperbolic quadratic shells over odd finite fields*, public published-finding corpus mathematical record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-gabor-tomography-rank-for-hyperbolic-quadratic-shells-over--b9e240edb677.
