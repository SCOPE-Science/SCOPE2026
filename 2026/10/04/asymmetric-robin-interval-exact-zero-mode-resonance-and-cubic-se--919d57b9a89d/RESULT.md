# Asymmetric Robin interval: exact zero-mode resonance and cubic secular multiplicity jump

## Finding

Consider \(-\mathrm d^2/\mathrm dx^2\) on \([0,\ell]\), with \(\ell>0\), and independent nonzero real Robin parameters \(\lambda_0\) and \(\lambda_\ell\):
\[
\psi'(0)+\lambda_0\psi(0)=0,
\qquad
-\psi'(\ell)+\lambda_\ell\psi(\ell)=0.
\]
In the boundary parametrisation \(P=0\), \(L=\operatorname{diag}(\lambda_0,\lambda_\ell)\), the secular function is
\[
F(k)=1-
\frac{(\lambda_0-\mathrm i k)(\lambda_\ell-\mathrm i k)}
{(\lambda_0+\mathrm i k)(\lambda_\ell+\mathrm i k)}
\mathrm e^{2\mathrm i k\ell}.
\]
Let \(g_0\) be the spectral multiplicity of the zero eigenvalue, \(N=\operatorname{ord}_{k=0}F(k)\), and \(\widetilde N\) the zero-energy scattering multiplicity. Then
\[
g_0=1\quad\Longleftrightarrow\quad
\ell=\frac1{\lambda_0}+\frac1{\lambda_\ell},
\]
and otherwise \(g_0=0\). Moreover,
\[
\widetilde N=1\quad\text{for every }\lambda_0\lambda_\ell\ne0,
\]
while
\[
N=\begin{cases}
3,&\ell=\lambda_0^{-1}+\lambda_\ell^{-1},\\
1,&\text{otherwise}.
\end{cases}
\]
Thus the cubic secular-multiplicity anomaly occurs exactly on the full asymmetric zero-mode resonance surface, not only on the equal-Robin diagonal. On resonance the zero mode is proportional to
\[
\psi_0(x)=1-\lambda_0x.
\]
The trace-formula combination is nevertheless constant across the whole family:
\[
g_0-\frac N2=-\frac12=\frac14\operatorname{tr}\mathfrak S_0.
\]

## Assumptions and scope

The interval length is positive and both Robin parameters are finite, real, and nonzero. The signs of \(\lambda_0\) and \(\lambda_\ell\) are otherwise unrestricted. The result concerns only the zero eigenvalue and the two algebraic notions used in the cited quantum-graph trace-formula framework. Dirichlet or Neumann endpoint limits, complex Robin parameters, and non-self-adjoint boundary conditions are not included.

## Proof

A zero mode is affine, \(\psi_0(x)=ax+b\). The two boundary conditions give
\[
a+\lambda_0b=0,
\qquad
-a+\lambda_\ell(a\ell+b)=0.
\]
The determinant of this two-by-two system is
\[
\lambda_0+\lambda_\ell-\lambda_0\lambda_\ell\ell.
\]
Because the first boundary equation is nontrivial, the kernel has dimension one exactly when that determinant vanishes. This is equivalent to
\[
\ell=\lambda_0^{-1}+\lambda_\ell^{-1},
\]
and the choice \(b=1\) gives \(a=-\lambda_0\), hence \(\psi_0(x)=1-\lambda_0x\).

For \(P=0\), the endpoint scattering factors are
\[
s_j(k)=-\frac{\lambda_j-\mathrm i k}{\lambda_j+\mathrm i k},
\]
so multiplication by the one-edge propagation matrix gives the stated \(F(k)\). Since both Robin parameters are nonzero, \(\mathfrak S_0=-I_2\). With the edge-exchange matrix \(J\),
\[
I_2-\mathfrak S_0J=I_2+J=
\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]
whose nullity is one. Therefore \(\widetilde N=1\) identically.

To determine \(N\), write
\[
1-F(k)=\exp h(k),
\]
where a local analytic logarithm near zero gives
\[
h(k)=2\mathrm i k\left(\ell-\frac1{\lambda_0}-\frac1{\lambda_\ell}\right)
+\frac{2\mathrm i}{3}k^3
\left(\frac1{\lambda_0^3}+\frac1{\lambda_\ell^3}\right)
+O(k^5).
\]
Off resonance the linear coefficient is nonzero, so \(F\) has a simple zero at \(k=0\), hence \(N=1\).

On resonance the linear term vanishes. The cubic coefficient cannot vanish: using \(\lambda_0+\lambda_\ell=\lambda_0\lambda_\ell\ell\),
\[
\frac1{\lambda_0^3}+\frac1{\lambda_\ell^3}
=
\ell\,
\frac{\lambda_0^2-\lambda_0\lambda_\ell+\lambda_\ell^2}
{\lambda_0^2\lambda_\ell^2}>0.
\]
The strict inequality holds because \(\ell>0\), the denominator is positive, and \(\lambda_0^2-\lambda_0\lambda_\ell+\lambda_\ell^2>0\) for nonzero real parameters. Therefore \(F(k)\) has exact order three and \(N=3\). Combining \((g_0,N)=(0,1)\) off resonance and \((1,3)\) on resonance yields \(g_0-N/2=-1/2\), while \(\operatorname{tr}\mathfrak S_0=-2\).

## Verification

`verify_robin_interval.py` uses exact rational arithmetic in a truncated formal power series ring over Gaussian rationals. It reconstructs the secular series from its two Robin reflection factors and the propagation exponential, checks exact order one off resonance and exact order three on several positive-positive and mixed-sign resonance points, verifies the cubic coefficient, checks the affine zero-mode boundary equations, and confirms \(g_0-N/2=-1/2\). The proof above, rather than the finite replay, establishes the statement for all admissible real parameters.

## Relationship to prior work

Bolte, Egger, and Steiner introduced the three zero-energy multiplicities used here and gave a one-edge Robin example only on the symmetric diagonal \(L=\lambda I_2\). Their example proves \(g_0=1\) exactly at \(\ell=2/\lambda\), \(N=3\) there and \(N=1\) otherwise, while \(\widetilde N=1\); they also prove general sufficient conditions ensuring \(N=\widetilde N\) away from anomalous zero-energy behavior. The result above keeps the same one-edge model but removes the equality of the two endpoint Robin parameters and classifies the entire two-parameter family exactly.

Targeted searches for unequal-Robin versions, reciprocal-parameter resonance conditions, and the cubic secular-order jump found the symmetric source example and general Robin-interval literature, but no source stating the asymmetric classification above. The claim is therefore limited to this explicit completion of the source example; it does not claim a new general theory of Robin spectra or quantum-graph trace formulas.

## Limitations

The calculation is elementary once the asymmetric secular determinant is written down, so a residual priority risk remains: an equivalent two-parameter formula may appear in Sturm--Liouville or boundary-condition literature not indexed by the searches. The scientific value is the complete classification of the anomaly in the exact framework where the symmetric counterexample was introduced, rather than a claim that the Robin interval itself is a new object.

## References

1. J. Bolte, S. Egger, and F. Steiner, “Zero modes of quantum graph Laplacians and an index theorem,” arXiv:1311.5485; *Annales Henri Poincaré* 16 (2015), 1155–1189, DOI: 10.1007/s00023-014-0347-z.
2. J. Bolte and S. Endres, “The trace formula for quantum graphs with general self adjoint boundary conditions,” *Annales Henri Poincaré* 10 (2009), 189–223.
3. G. Berkolaiko and P. Kuchment, *Introduction to Quantum Graphs*, American Mathematical Society, 2013.
