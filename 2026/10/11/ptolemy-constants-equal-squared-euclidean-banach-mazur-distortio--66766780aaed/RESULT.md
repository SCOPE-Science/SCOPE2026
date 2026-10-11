# Ptolemy constants equal squared Euclidean Banach--Mazur distortion for a symmetric absolute plane class
## Finding
Let \(\psi\) be a continuous convex function on \([0,1]\) with \(\psi(0)=\psi(1)=1\), \(\max\{1-t,t\}\le \psi(t)\le1\), and \(\psi(t)=\psi(1-t)\). Let \(N_\psi\) be the associated absolute normalized norm on \(\mathbb R^2\), and put \(\psi_2(t)=\sqrt{(1-t)^2+t^2}\). If either (i) \(\psi\ge\psi_2\) and \(\psi/\psi_2\) attains its maximum at \(t=1/2\), or (ii) \(\psi\le\psi_2\) and \(\psi_2/\psi\) attains its maximum at \(t=1/2\), then the Ptolemy constant and Euclidean Banach--Mazur distance satisfy \(C_{\mathrm{Pt}}(N_\psi)=d_{\mathrm{BM}}((\mathbb R^2,N_\psi),\ell_2^2)^2\). In case (i) both equal \(2\psi(1/2)^2\); in case (ii) both equal \(1/(2\psi(1/2)^2)\).

This gives a structural reason that two a priori different quantities coincide on a broad class of absolute symmetric Banach planes: the metric four-point distortion measured by the Ptolemy constant equals the square of the best linear Euclidean distortion.

## Assumptions and scope
For a continuous convex function \(\psi:[0,1]\to\mathbb R\) satisfying
\[
\psi(0)=\psi(1)=1,\qquad \max\{1-t,t\}\le \psi(t)\le1,
\]
define the associated absolute normalized norm by
\[
N_\psi(z,w)=
\begin{cases}
(|z|+|w|)\,\psi\!\left(\dfrac{|w|}{|z|+|w|}\right),&(z,w)\ne(0,0),\\
0,&(z,w)=(0,0).
\end{cases}
\]
Assume additionally that \(\psi(t)=\psi(1-t)\). Write
\[
\psi_2(t)=\sqrt{(1-t)^2+t^2}.
\]
The claim applies when either \(\psi\ge\psi_2\) and \(\psi/\psi_2\) has its global maximum at \(1/2\), or \(\psi\le\psi_2\) and \(\psi_2/\psi\) has its global maximum at \(1/2\).

For a real normed plane \(X\), the Ptolemy constant used here is
\[
C_{\mathrm{Pt}}(X)=
\sup \frac{\|x-y\|\,\|z\|}
{\|x-z\|\,\|y\|+\|z-y\|\,\|x\|},
\]
where the supremum is over nonzero pairwise distinct \(x,y,z\in X\). The Euclidean Banach--Mazur distance is
\[
d_{\mathrm{BM}}(X,\ell_2^2)=
\inf_T \|T\|\,\|T^{-1}\|,
\]
where the infimum ranges over linear isomorphisms from \(X\) onto \(\ell_2^2\).

## Proof
First consider the Banach--Mazur distance. Let \(E(x,y)=\sqrt{x^2+y^2}\). For a nonzero vector, after changing signs and scaling it can be written as \((1-t,t)\) with \(0\le t\le1\), and therefore
\[
\frac{N_\psi}{E}=\frac{\psi(t)}{\psi_2(t)}.
\]
In case (i), the smallest value of this ratio is \(1\), attained on the coordinate axes, while the largest value is
\[
M=\frac{\psi(1/2)}{\psi_2(1/2)}=\sqrt2\,\psi(1/2).
\]
Thus the coordinate Euclidean norm gives distortion \(M\). In case (ii), the reciprocal ratio has minimum \(1\) on the axes and maximum
\[
M=\frac{\psi_2(1/2)}{\psi(1/2)}=\frac{1}{\sqrt2\,\psi(1/2)}.
\]
Again the coordinate Euclidean norm gives distortion \(M\).

It remains to prove that no tilted or anisotropic ellipse improves this. Let \(H(x)=\sqrt{q(x)}\) be any Euclidean pullback arising from a positive-definite quadratic form. After multiplying \(H\) by a scalar, write its distortion as \(d\) with
\[
N_\psi(x)\le H(x)\le d\,N_\psi(x)\qquad\text{for every }x\in\mathbb R^2.
\]
Let \(G\) be the eight signed coordinate permutations. Symmetry of \(\psi\) implies \(N_\psi(gx)=N_\psi(x)\) for every \(g\in G\). Hence
\[
N_\psi(x)^2\le q(gx)\le d^2N_\psi(x)^2.
\]
Averaging over \(G\) gives another quadratic form
\[
\overline q(x)=\frac1{|G|}\sum_{g\in G}q(gx)
\]
with the same pointwise inequalities. Invariance under sign changes kills the mixed term, and invariance under coordinate interchange makes the two diagonal coefficients equal. Therefore
\[
\overline q(x)=c(x^2+y^2)
\]
for some \(c>0\). Consequently the coordinate Euclidean norm, up to scale, also has distortion at most \(d\). Since \(H\) was arbitrary, the coordinate Euclidean norm is optimal and
\[
d_{\mathrm{BM}}=M.
\]

Zuo's Theorem 2.3 states that under case (i),
\[
C_{\mathrm{Pt}}=2\psi(1/2)^2=M^2,
\]
and Theorem 2.2 gives under case (ii)
\[
C_{\mathrm{Pt}}=\frac1{2\psi(1/2)^2}=M^2.
\]
Thus in both branches
\[
C_{\mathrm{Pt}}=d_{\mathrm{BM}}^2.
\]

## Verification
The proof has two independent components. The Ptolemy-value component is exactly the midpoint-extremum theorem in the cited open-access article. The Euclidean-distortion component was checked directly from the quadratic-form inequalities and finite-group averaging; it does not assume that an arbitrary optimal ellipse is axis-aligned.

As consistency checks, the theorem recovers the classical \(\ell_p^2\) identity
\[
C_{\mathrm{Pt}}(\ell_p^2)=2^{|2/p-1|}
=d_{\mathrm{BM}}(\ell_p^2,\ell_2^2)^2
\]
and also applies to several symmetric absolute examples in the cited paper whenever their midpoint hypothesis is verified there.

## Relationship to prior work
Zuo's 2012 paper proves the exact Ptolemy formulas used above for absolute normalized norms whose Euclidean comparison ratio has its extremum at the midpoint. It does not formulate or prove the Banach--Mazur equality established here. Searches for the combined statement located published special cases where Ptolemy and Euclidean distortion coincide for particular max-norm and Lorentz planes, but no general theorem covering the present symmetric midpoint class.

The new contribution is the finite-group averaging argument showing that, for every norm in this symmetric class, arbitrary linear Euclidean reparametrization cannot improve on the coordinate circle. Combining that affine statement with the source's Ptolemy theorem yields the exact invariant identity across the full class.

## Limitations
The result requires coordinate-interchange symmetry and the stated one-sided Euclidean comparison with midpoint extremum. It does not claim equality for arbitrary absolute norms, for nonsymmetric absolute norms, or when the relevant ratio is maximized away from \(1/2\). The literature search cannot exclude every unindexed or differently phrased prior formulation; the main residual originality risk is an implicit occurrence of the same averaging bridge in older Banach--Mazur literature.

## References
Z. Zuo, “The Ptolemy constant of absolute normalized norms on \(\mathbb R^2\),” Journal of Inequalities and Applications 2012, Article 107, published 17 May 2012, DOI: 10.1186/1029-242X-2012-107.
