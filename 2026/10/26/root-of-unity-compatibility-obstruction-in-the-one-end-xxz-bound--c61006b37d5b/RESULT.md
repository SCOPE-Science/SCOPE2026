# Root-of-unity compatibility obstruction in the one-end XXZ boundary recurrence

## Finding

At the free-fermion XXZ point \(\Delta=0\), choose \(q=i\), an x-directed real boundary field \(\vec g=(g,0,0)\) with \(g\ne0\), and a representation parameter \(s\) satisfying \(\gamma=i\cot(\pi s/2)\) and \(\sin(\pi s)\ne0\). For the Popkov–Prosen boundary recurrence with normalization \(u_0=1\), compatibility at indices \(j=0,1\) forces \(g^2=1/2\); when this condition holds, the \(j=1\) equation still does not determine \(u_2\) because \([2]_i=0\). Thus the printed forward recurrence is not generically well-posed at this standard root-of-unity point. This conclusion concerns the recurrence only and does not imply nonexistence of a nonequilibrium steady state or of an alternative matrix-product representation.

## Assumptions and scope

Use the convention \(\Delta=(q+q^{-1})/2\), the q-number \([x]_q=(q^x-q^{-x})/(q-q^{-1})\), and the auxiliary coefficients \(a_j=(q^{s-j}+q^{j-s})/2\). The boundary equation is the three-term recurrence printed as Eq. (14) by Popkov and Prosen:

\[
\left(-\frac{a_j}{2}+[s-j]_qg_z\right)u_j
+\frac{g^-}{2}[2s-j+1]_q u_{j-1}
+\frac{g^+}{2}[j+1]_q u_{j+1}=0,
\qquad u_{-1}=0,\quad u_0=1.
\]

Here \(g^\pm=g_x\pm i g_y\). We restrict the claim to \(q=i\), \(g_z=0\), and \(g^+=g^-=g\in\mathbb R\setminus\{0\}\). For this choice, \([x]_i=\sin(\pi x/2)\), so \([2]_i=0\). The parameter condition \(\gamma=i\cot(\pi s/2)\) is the source paper's dissipation-representation relation specialized to \(q=i\).

## Proof

At \(q=i\), the q-number and diagonal coefficient reduce to

\[
[x]_i=\sin(\pi x/2),\qquad a_j=\cos(\pi(s-j)/2).
\]

At \(j=0\), the recurrence and \(u_0=1\) give

\[
-\frac{a_0}{2}+\frac{g}{2}u_1=0,
\qquad u_1=\frac{a_0}{g}.
\]

At \(j=1\), the coefficient of \(u_2\) vanishes because \([2]_i=0\), leaving the necessary compatibility condition

\[
-\frac{a_1}{2}u_1+\frac{g}{2}[2s]_i=0,
\qquad g^2[2s]_i=a_0a_1.
\]

But \(a_0=\cos(\pi s/2)\), \(a_1=\sin(\pi s/2)\), and \([2s]_i=\sin(\pi s)\). Hence

\[
a_0a_1=\frac12\sin(\pi s)=\frac12[2s]_i,
\qquad (g^2-1/2)\sin(\pi s)=0.
\]

Under the stated hypothesis \(\sin(\pi s)\ne0\), compatibility requires \(g^2=1/2\). If \(g^2\ne1/2\), no sequence with \(u_0=1\) can satisfy even the first two recurrence equations. If \(g^2=1/2\), the equation at \(j=1\) is independent of \(u_2\), so the forward recurrence does not determine that coefficient there.

This is not an empty parameter case. For example, \(s=i\log(3)/\pi\) gives \(\gamma=i\cot(\pi s/2)=2\) and \(\sin(\pi s)=i\sinh(\log 3)\ne0\). Taking \(g=1\) violates the necessary condition \(g^2=1/2\), furnishing an explicit admissible obstruction.

## Verification

The proof uses only exact trigonometric identities and the printed recurrence. In particular, \([2]_i=\sin(\pi)=0\), and the compatibility equation follows without a numerical approximation or an extrapolation from finite-size data. The explicit parameter example satisfies the source's representation relation exactly. No statement is made about whether a different auxiliary representation solves the same physical steady-state problem.

## Relationship to prior work

Popkov and Prosen give the recurrence for an arbitrary boundary field and state that it is well defined apart from zero field or a field parallel to the z-axis. The calculation above identifies an additional obstruction for the normalized forward recurrence at \(q=i\), including a generic x-directed field. Yao et al. discuss rational anisotropies \(\Delta/J=\cos(\ell\pi/m)\), note finite bond dimension in a weak-dissipation regime, and identify the free-fermion point \(\Delta=0\); that work uses a different matrix-product construction and does not imply that the recurrence above is forward-well-posed. Root-of-unity truncation in XXZ representation theory is established background, so the novelty claim is limited to the exact compatibility condition for this particular one-end boundary recurrence.

## Limitations

The result does not disprove existence or uniqueness of the physical nonequilibrium steady state, and it does not rule out an alternative finite-dimensional or differently normalized matrix-product ansatz. It treats only \(q=i\) and a real x-directed field. It does not classify compatibility at all other roots of unity, derive the full exceptional-field locus, or analyze the resulting steady-state observables. The originality comparison is best-knowledge rather than exhaustive; related root-of-unity auxiliary constructions remain a residual risk.

## References

1. V. Popkov and T. Prosen, “Exact steady state of a one-end driven XXZ spin chain with boundary field,” *Physical Review B* 114, L140305 (2026), first public version arXiv:2604.16102v1 (17 April 2026), Eq. (14) and discussion following it; DOI: 10.1103/2cq3-66ny.
2. M. Yao, A. Lingenfelter, R. Belyansky, D. Roberts, and A. A. Clerk, “Hidden time reversal in driven XXZ spin chains: Exact solutions and new dissipative phase transitions,” *Physical Review Letters* 134, 130404 (2025), especially the discussion of rational anisotropies and the free-fermion point; DOI: 10.1103/PhysRevLett.134.130404.
3. Y. Miao, J. Lamers, and V. Pasquier, “On the Q operator and the spectrum of the XXZ model at root of unity,” *SciPost Physics* 11, 067 (2021), arXiv:2012.10224.
