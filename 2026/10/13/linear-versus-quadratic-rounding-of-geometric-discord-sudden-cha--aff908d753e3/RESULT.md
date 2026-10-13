# Linear versus quadratic rounding of geometric-discord sudden changes under dephasing

## Finding

There are two natural, equally large perturbations of a separable two-qubit state whose Hilbert–Schmidt geometric discord has a sharp dephasing transition. In one perturbation the transition is rounded on an order-\(\epsilon^2\) time interval; in the other it is rounded on an order-\(\epsilon\) interval. Both share the same exact limiting crossover profile.

Let \(I,X,Y,Z\) be the identity and Pauli operators on \(\mathbb C^2\). Fix real parameters
\[
0<b<a,\qquad a+b<1,\qquad 0<\epsilon<(1-a-b)/2.
\]
Define two density matrices
\[
\begin{aligned}
\rho_{\rm loc}(0,\epsilon)&=\tfrac14\bigl(I\otimes I+aX\otimes X+bZ\otimes Z+\epsilon(X\otimes I+Z\otimes I)\bigr),\\
\rho_{\rm corr}(0,\epsilon)&=\tfrac14\bigl(I\otimes I+aX\otimes X+bZ\otimes Z+\epsilon(X\otimes Z+Z\otimes X)\bigr).
\end{aligned}
\]
Each state evolves under independent Markovian phase damping \(\mathcal D_t\otimes\mathcal D_t\), with \(\mathcal D_t(X)=e^{-t}X\), \(\mathcal D_t(Y)=e^{-t}Y\), and \(\mathcal D_t(Z)=Z\). Write \(G_j(t,\epsilon)\) for the squared Hilbert–Schmidt distance of the evolved state to the zero-discord states on the first qubit, for \(j\in\{\mathrm{loc},\mathrm{corr}\}\). Every state here is strictly positive and separable for all \(t\ge0\). The two initial perturbations have the *same* Hilbert–Schmidt size, namely \(\epsilon/\sqrt2\).

Put \(q=e^{-t}\), \(r=\sqrt{b/a}\), and \(t_0=\tfrac12\log(a/b)\). The exact discord functions are
\[
G_{\rm loc}(t,\epsilon)=\frac18\left[a^2q^4+b^2+\epsilon^2(q^2+1)-\sqrt{\bigl(a^2q^4-b^2+\epsilon^2(q^2-1)\bigr)^2+4\epsilon^4q^2}\right]
\]
and
\[
G_{\rm corr}(t,\epsilon)=\frac18\left[a^2q^4+b^2+2\epsilon^2q^2-\sqrt{\bigl(a^2q^4-b^2\bigr)^2+4\epsilon^2q^2(aq^2+b)^2}\right].
\]
At \(\epsilon=0\), both reduce to \(G_0(t)=\tfrac14\min\{a^2e^{-4t},b^2\}\), with a derivative discontinuity at \(t_0\). Every \(\epsilon>0\) eliminates this finite-time discontinuity in both families.

Define centering times and widths
\[
\begin{array}{ll}
 c_{\rm loc}=t_0+\dfrac{\epsilon^2(r^2-1)}{4b^2},& w_{\rm loc}=\dfrac{\epsilon^2 r}{2b^2},\\[5pt]
 c_{\rm corr}=t_0,& w_{\rm corr}=\dfrac{\epsilon r}{b}.
\end{array}
\]
For every real \(z\), uniformly for \(z\) in a fixed compact set,
\[
\boxed{\lim_{\epsilon\downarrow0}\frac{\partial_tG_j(c_j+w_jz,\epsilon)}{-b^2}=\frac12\left(1+\frac{z}{\sqrt{1+z^2}}\right),\qquad j\in\{\mathrm{loc},\mathrm{corr}\}.}
\]
Thus two equally sized physical imperfections give an exact linear-versus-quadratic contrast in transition width, not merely two differently parametrized instances of one perturbation.

## Assumptions and scope

The parameters \(a,b\) are fixed while \(\epsilon\downarrow0\). The first-subsystem zero-discord manifold and squared, *unnormalized* Hilbert–Schmidt distance specify the discord convention. Dephasing time \(t\) is nonnegative. This is **geometric discord**, not the entropy-based quantum discord. The limiting derivative formula describes times in the stated shrinking windows; it does not claim uniformity over all real \(z\) or all \(a,b\).

Both two-qubit operators are positive definite because they equal one quarter of identity plus Hermitian terms with total operator norm strictly below \(a+b+2\epsilon<1\). Their partial transpose in the *second* qubit is identical to the original matrix: the Pauli operators acting on that qubit are only \(I,X,Z\), all real symmetric. The Peres–Horodecki criterion therefore proves separability. Trace preservation and the local quantum channel preserve these properties for all \(t\ge0\). Orthogonality of Pauli tensors gives the initial perturbation norm \(\epsilon/\sqrt2\) in each family.

## Proof

**Geometric optimization.** Write a two-qubit state in Bloch coordinates as
\[
\rho=\frac14\left(I\otimes I+\sum_i x_i\sigma_i\otimes I+\sum_j y_j I\otimes\sigma_j+\sum_{ij}T_{ij}\sigma_i\otimes\sigma_j\right).
\]
A projective measurement of the first qubit along a unit Bloch direction \(u\) orthogonally projects \(x\) and every column of \(T\) onto the line spanned by \(u\). The postmeasurement state is the nearest state fixed by that measurement in Hilbert–Schmidt norm. Minimizing over first-qubit measurements therefore gives
\[
G(\rho)=\frac14\left(\|x\|^2+\|T\|_{\rm F}^2-\lambda_{\max}(xx^{\mathsf T}+TT^{\mathsf T})\right).
\]
This is also the two-qubit geometric-discord formula of Dakić–Vedral–Brukner [1].

**Exact evaluation.** Under the channel, \(aX\otimes X\) becomes \(aq^2X\otimes X\), while \(bZ\otimes Z\) is unchanged. For the local perturbation,
\[
x=(\epsilon q,0,\epsilon),\qquad T=\operatorname{diag}(aq^2,0,b).
\]
The nonzero \((X,Z)\) block of \(K=xx^{\mathsf T}+TT^{\mathsf T}\) has diagonal entries \(a^2q^4+\epsilon^2q^2\) and \(b^2+\epsilon^2\), and offdiagonal entry \(\epsilon^2q\). Its smaller eigenvalue is \((S-\sqrt{\Delta^2+4\epsilon^4q^2})/2\), where \(S\) is its trace and \(\Delta\) the diagonal difference. The displayed formula for \(G_{\rm loc}\) follows by dividing that eigenvalue by four.

For the correlation perturbation, \(x=0\) and the nontrivial block of \(T\) is
\[
T_{XZ}=\begin{pmatrix}aq^2&\epsilon q\\\epsilon q&b\end{pmatrix}.
\]
Therefore \(TT^{\mathsf T}\) has diagonal entries \(a^2q^4+\epsilon^2q^2\), \(b^2+\epsilon^2q^2\), and offdiagonal entry \(\epsilon q(aq^2+b)\). The same two-by-two eigenvalue formula yields \(G_{\rm corr}\). In either case the offdiagonal entry is strictly positive at every finite time when \(\epsilon>0\), making the largest eigenvalue simple and both discords real-analytic as functions of \(t\).

**Scaled limits.** First take the local case with \(t=t_0+\epsilon^2s\) and fixed real \(s\). Since \(q=r e^{-\epsilon^2s}\), expansion of the exact eigenvalue formula gives, locally uniformly together with first derivatives in \(s\),
\[
G_{\rm loc}(t_0+\epsilon^2s,\epsilon)=\frac{b^2}{4}+\epsilon^2F_{\rm loc}(s)+O(\epsilon^4),
\]
where
\[
F_{\rm loc}(s)=\frac18\left[-4b^2s+r^2+1-\sqrt{(r^2-1-4b^2s)^2+4r^2}\right].
\]
Now \(c_{\rm loc}+w_{\rm loc}z=t_0+\epsilon^2[(r^2-1)/(4b^2)+rz/(2b^2)]\), so the square root inside the derivative has argument \(4r^2(1+z^2)\). Differentiating the smooth scaled expansion establishes the claimed profile.

For the correlation case let \(t=t_0+\epsilon s\). A parallel expansion, locally uniform with first derivatives, gives
\[
G_{\rm corr}(t_0+\epsilon s,\epsilon)=\frac{b^2}{4}+\epsilon F_{\rm corr}(s)+O(\epsilon^2),
\qquad F_{\rm corr}(s)=-\frac12\left[b^2s+b\sqrt{b^2s^2+r^2}\right].
\]
The substitution \(s=rz/b\) again gives the same derivative profile. Uniformity on compact \(s\)-intervals holds because the limiting radicands \((r^2-1-4b^2s)^2+4r^2\) and \(b^2s^2+r^2\) have strictly positive lower bounds for fixed \(0<b<a\).

Finally \(\epsilon=0\) makes both offdiagonals vanish, and a direct comparison of the two diagonal eigenvalues gives \(G_0\). Its left time derivative at \(t_0\) is \(0\), whereas the right derivative is \(-b^2\). The limiting crossover interpolates exactly between those values.

## Verification

The standalone `verify_discord.py` reconstructs both \(4\times4\) density matrices, checks strict positivity and invariance under the second partial transpose, extracts Bloch tensors independently using Pauli traces, diagonalizes \(K\), and compares the result to each exact formula. It also checks the derivative crossover numerically in both scaling windows. The recorded execution passed 42 direct matrix comparisons across both kinds, three perturbation sizes and seven times, as well as both near-critical slope comparisons. A separate five-parameter-pair stress test agreed with the theorem. These finite checks corroborate, but do not prove, the parameter-uniform asymptotics; the proof above establishes them.

## Relationship to prior work

Dakić, Vedral and Brukner [1] derived the general two-qubit geometric-discord spectral formula, which is taken as foundational here and reproved in measurement form. Yao and colleagues [2] studied geometric-discord geometry and Bell-diagonal dephasing sudden changes. Yu, Li and Fan [3] characterize sudden-change points through crossings of geometric-correlation eigenvalues. Pinto, Karpat and Fanchini [4] demonstrate smoothing of *entropy-based* discord sudden changes under experimental imperfections. These works motivate the question but do not, in their inspected results, state the two exact perturbation-width exponents with a common normalized profile for the present separable families. The full text of a potentially related study of non-X states under decoherence [5] was unavailable; its abstract concerns different Bloch-vector orientations. Accordingly, that source is not claimed to be ruled out.

## Limitations

This theorem concerns squared Hilbert–Schmidt geometric discord, not entropy-based discord; the former need not be monotone under arbitrary local processing on the unmeasured subsystem. The two preparation-error directions are explicit, and the result does not classify arbitrary perturbations. The limits are for fixed \(a,b\) and bounded scaled \(z\). Although the cited formula contains the algebraic ingredients to derive this result, priority against unpublished or inaccessible equivalent specializations is not established; in particular, [5] was not available for a full-text implication comparison.

## References

[1] B. Dakić, V. Vedral, Č. Brukner, *Necessary and sufficient condition for non-zero quantum discord*, arXiv:1004.0190 (first posted 2010-04-01); Phys. Rev. Lett. 105, 190502 (2010).

[2] Y. Yao, H.-W. Li, Z.-Q. Yin, and Z.-F. Han, *Geometric interpretation of the geometric discord*, arXiv:1303.4827 (2013).

[3] C.-S. Yu, B. Li, and H. Fan, *The witness of sudden change of geometric quantum correlation*, arXiv:1309.0934 (2013).

[4] J. Pinto, G. Karpat, F. F. Fanchini, *Sudden change of quantum discord for a system of two qubits*, arXiv:1309.7945 (2013).

[5] H. Chen, Y.-Q. Fu, J.-X. Fang, *Geometric Discord of Non-X-Structured State under Decoherence Channels*, Int. J. Theor. Phys. 53 (2014), doi:10.1007/s10773-014-2094-9 (abstract inspected only).
