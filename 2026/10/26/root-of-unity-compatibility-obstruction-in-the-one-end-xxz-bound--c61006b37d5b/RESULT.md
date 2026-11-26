# Root-of-unity compatibility obstruction in the one-end XXZ boundary recurrence

## Finding

At the free-fermion XXZ point \(\Delta=0\), take \(q=i\), a real x-directed boundary field \(\vec g=(g,0,0)\) with \(g\ne0\), and a representation parameter \(s\) satisfying \(\gamma=i\cot(\pi s/2)\) and \(\sin(\pi s)\ne0\). The first two equations of the normalized boundary recurrence printed by Popkov and Prosen, Eq. (14), are compatible if and only if \(g^2=1/2\). Even in this exceptional case, the equation at index \(j=1\) does not determine \(u_2\). Thus the printed forward recurrence is not generically well posed at \(q=i\). This is an obstruction to that recurrence with its printed normalization, not to the physical steady state or to another matrix-product representation.

## Assumptions and scope

Use \(\Delta=(q+q^{-1})/2\), \([x]_q=(q^x-q^{-x})/(q-q^{-1})\), and \(a_j=(q^{s-j}+q^{j-s})/2\). At \(q=i\), the exponent convention is \(q^x=\exp(i\pi x/2)\). The recurrence is
\[
\left(-\frac{a_j}{2}+[s-j]_qg_z\right)u_j
+\frac{g^-}{2}[2s-j+1]_q u_{j-1}
+\frac{g^+}{2}[j+1]_q u_{j+1}=0,
\qquad u_{-1}=0,\quad u_0=1.
\]
Here \(g^\pm=g_x\pm i g_y\), so the specified field has \(g_z=0\) and \(g^+=g^-=g\). The relation between \(\gamma\) and \(s\) is Eq. (12) of [1] specialized to \(q=i\).

## Proof

We have \([x]_i=\sin(\pi x/2)\) and \(a_j=\cos(\pi(s-j)/2)\). At \(j=0\) the equation is \(-a_0+g u_1=0\), so \(u_1=a_0/g\). At \(j=1\), \([2]_i=0\), so the equation is \(-a_1u_1+g[2s]_i=0\). Substitution gives
\[
g^2[2s]_i=a_0a_1=\cos(\pi s/2)\sin(\pi s/2)=\tfrac12[2s]_i.
\]
Since \([2s]_i=\sin(\pi s)\ne0\), compatibility is equivalent to \(g^2=1/2\). If that condition holds, these two equations are satisfied by \(u_1=a_0/g\) with any \(u_2\), since the coefficient of \(u_2\) is zero. Otherwise no sequence with \(u_0=1\) satisfies even those two equations.

For an admissible failure example, take \(s=i\log(3)/\pi\) and \(g=1\). The representation relation gives \(\gamma=\coth((\log 3)/2)=2\), and \(\sin(\pi s)=i\sinh(\log 3)\ne0\). This field fails the compatibility requirement.

## Verification

The obstruction follows by exact substitution into the printed first two recurrence equations; it uses no numerical approximation or assumption about later coefficients. The explicit example checks that the representation relation admits a positive real dissipation strength in the obstructed regime.

## Relationship to prior work

Popkov and Prosen [1] state after Eq. (14) that their recurrence is well defined except for zero field or a z-directed field. This calculation gives an explicit additional exception for the normalized forward recurrence. Popkov and Prosen identify Supplemental Eq. (S.14) of Yao et al. [2] as the precursor of their boundary recurrence for the special x-directed field. The recurrence and the x-field setup are therefore not claimed as new. Yao et al.'s discussion of rational anisotropies and root-of-unity truncation in XXZ spectral theory [3] provide related background. The claim here concerns the specific \(g^2=1/2\) compatibility condition and loss of forward determination in the printed normalization, not the existence of an earlier recurrence or any general novelty of root-of-unity degeneracies.

## Limitations

The result does not establish whether the exceptional fields yield a solution of all the later equations or a physical matrix-product steady state. It treats only \(q=i\), a real x-directed field, and \(\sin(\pi s)\ne0\). It does not classify other roots of unity, boundary directions, representations, or steady-state observables. The relationship of the compatibility calculation to the full text of [2]'s supplement is not settled by [1]'s identification of the recurrence.

## References

1. V. Popkov and T. Prosen, *Exact steady state of a one-end driven XXZ spin chain with boundary field*, Physical Review B 114, L140305 (2026), arXiv:2604.16102v1, Eqs. (12), (14) and their discussion. DOI: 10.1103/2cq3-66ny.
2. M. Yao, A. Lingenfelter, R. Belyansky, D. Roberts, and A. A. Clerk, *Hidden time reversal in driven XXZ spin chains: Exact solutions and new dissipative phase transitions*, Physical Review Letters 134, 130404 (2025), Supplemental Eq. (S.14) as cited in [1]. DOI: 10.1103/PhysRevLett.134.130404.
3. Y. Miao, J. Lamers, and V. Pasquier, *On the Q operator and the spectrum of the XXZ model at root of unity*, SciPost Physics 11, 067 (2021), arXiv:2012.10224.
