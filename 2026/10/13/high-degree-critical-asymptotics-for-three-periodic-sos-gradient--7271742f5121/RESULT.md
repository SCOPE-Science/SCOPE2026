# High-degree critical asymptotics for three-periodic SOS gradient Gibbs measures
## Finding
For the three-periodic mirror-symmetric boundary-law family of the ferromagnetic SOS model on the \(k\)-regular Cayley tree, \(k\ge2\), define
\[
\psi_k(a)=2+\frac{2a^k+1}{a+a^2+\cdots+a^{k-1}},\qquad a>0.
\]
The critical parameter isolated in the source is
\[
\tau_c(k)=\min_{a>0}\psi_k(a),
\]
with a unique minimizer \(a_k\). If \(\tau_c(k)=2\cosh\beta_c(k)\), then as \(k\to\infty\),
\[
-k\log a_k=c_*+O(k^{-1}),
\]
where \(c_*>0\) is the unique positive root of
\[
e^{c}+1-2e^{-c}=3c.
\]
Numerically,
\[
c_*=1.0356584794018931933513404876\ldots.
\]
The critical coupling has the two-term expansion
\[
\boxed{\tau_c(k)=2+\frac{C_*}{k}+\frac{D_*}{k^2}+O(k^{-3})},
\]
where
\[
C_*=\frac{c_*(e^{c_*}+2)}{e^{c_*}-1}
=2.7456435767327243968834656458\ldots,
\]
and
\[
D_*=\frac{c_*^2(1+2e^{-c_*})(1+e^{-c_*})}{2(1-e^{-c_*})^2}
=2.9867777254276540482433751344\ldots.
\]
Consequently,
\[
\boxed{\beta_c(k)=\frac{\sqrt{C_*}}{\sqrt{k}}+
\frac{D_*-C_*^2/12}{2\sqrt{C_*}\,k^{3/2}}+O(k^{-5/2})},
\]
with
\[
\sqrt{C_*}=1.6569983635274732512228914058\ldots.
\]
Thus the three-periodic transition occurs at inverse temperature of order \(k^{-1/2}\), with an explicit universal constant determined by a one-dimensional transcendental equation.

## Assumptions and scope
The model and normalization are those of Henning, Külske, Le Ny, and Rozikov: the ferromagnetic SOS model with integer heights on the Cayley tree of order \(k\), whose vertices have degree \(k+1\), and \(\tau=2\cosh\beta\). The boundary-law family is
\[
u_{3m}=1,\qquad u_{3m+1}=u_{3m+2}=a.
\]
For this family the source reduces nontrivial three-periodic boundary laws to
\[
2a^k+(2-\tau)(a^{k-1}+\cdots+a)+1=0,
\]
which is equivalent to \(\tau=\psi_k(a)\). The claim concerns the existence threshold for this boundary-law family. It does not identify an extremality, reconstruction, or thermodynamic free-energy transition, and it does not assert an asymptotic for arbitrary nonsymmetric three-periodic boundary laws beyond the source's identification of those solutions with this family.

## Proof
Put
\[
m_k(a)=\psi_k(a)-2=\frac{2a^k+1}{a+a^2+\cdots+a^{k-1}}.
\]
Differentiation shows that the critical points are the positive roots of
\[
2\sum_{j=1}^{k-1}(k-j)a^{k+j-1}-\sum_{j=1}^{k-1}j a^{j-1}=0.
\]
Its coefficient sequence has exactly one sign change, while its value is negative at \(a=0\) and positive for large \(a\). Hence there is exactly one positive critical point. Since \(m_k(a)\to\infty\) at both endpoints \(a\downarrow0\) and \(a\to\infty\), this point is the unique global minimizer \(a_k\).

The minimizer lies below one. Indeed, for \(a>1\),
\[
m_k(a^{-1})=\frac{a^k+2}{a+a^2+\cdots+a^{k-1}}
<\frac{2a^k+1}{a+a^2+\cdots+a^{k-1}}=m_k(a),
\]
and \(a=1\) is not critical. Hence \(0<a_k<1\).

Set
\[
c_k=-k\log a_k>0.
\]
Since \(m_k(a_k)\le m_k(1)=3/(k-1)\), while for \(0<a<1\)
\[
m_k(a)=\frac{(1+2a^k)(1-a)}{a(1-a^{k-1})}\ge a^{-1}-1,
\]
we obtain
\[
0<c_k\le \frac{3k}{k-1}\le6.
\]
Thus all minimizers live on a fixed compact set after the logarithmic rescaling.

For \(c\ge0\), with continuous extension at \(c=0\), define
\[
F_k(c)=k\,m_k(e^{-c/k})
=(1+2e^{-c})\frac{k(e^{c/k}-1)}{1-e^{-c+c/k}}.
\]
Using the analytic functions \((e^x-1)/x\) and \((1-e^{-x})/x\), Taylor expansion is uniform together with one derivative on every fixed compact interval. It gives
\[
F_k(c)=F(c)+\frac{G(c)}{k}+O(k^{-2}),
\]
where
\[
F(c)=\frac{c(1+2e^{-c})}{1-e^{-c}}
=\frac{c(e^c+2)}{e^c-1},
\]
and
\[
G(c)=\frac{c^2(1+2e^{-c})(1+e^{-c})}{2(1-e^{-c})^2}.
\]
The derivative of \(F\) is
\[
F'(c)=\frac{e^c\bigl(e^c+1-2e^{-c}-3c\bigr)}{(e^c-1)^2}.
\]
Let
\[
h(c)=e^c+1-2e^{-c}-3c.
\]
Here \(h(0)=h'(0)=0\), \(h''(0)=-1\), and \(h'''(c)=e^c+2e^{-c}>0\). Hence \(h''\) has one positive zero, \(h'\) first decreases and then increases, and \(h\) first decreases below zero and then increases to infinity. Therefore \(h\) has exactly one positive zero \(c_*\), and \(F\) has a unique nondegenerate minimum there.

Because \(c_k\in[0,6]\), uniform convergence of \(F_k\) to \(F\) and uniqueness of the minimum imply \(c_k\to c_*\). The local \(C^1\) expansion and \(F''(c_*)>0\) sharpen this to \(c_k=c_*+O(k^{-1})\). Evaluating the expansion at the moving minimizer gives
\[
F_k(c_k)=F(c_*)+\frac{G(c_*)}{k}+O(k^{-2}),
\]
because the displacement contributes only at second order to \(F\). Dividing by \(k\) proves
\[
\tau_c(k)-2=\frac{F(c_*)}{k}+\frac{G(c_*)}{k^2}+O(k^{-3}),
\]
which is the stated formula with \(C_*=F(c_*)\) and \(D_*=G(c_*)\).

Finally, \(2\cosh\beta=2+\beta^2+\beta^4/12+O(\beta^6)\). Substitution of the expansion for \(\tau_c(k)-2\) and coefficient comparison yield the displayed expansion for \(\beta_c(k)\).

## Verification
The accompanying `verify.py` independently evaluates the defining transcendental equation by bisection, reconstructs \(C_*\) and \(D_*\), solves the exact derivative equation for \(a_k\) by bisection for a range of tree orders, and checks the predicted scaling. These finite numerical checks are regression tests only; the all-\(k\) and asymptotic statements are proved analytically above.

Representative values are consistent with the theorem: for \(k=20\), \(\tau_c(k)\approx2.145114851780354\); for \(k=100\), \(\tau_c(k)\approx2.027757914158848\); and for \(k=1000\), \(\tau_c(k)\approx2.002748633128227\). The rescaled minimizer \(-k\log a_k\) approaches \(c_*\).

## Relationship to prior work
Henning, Külske, Le Ny, and Rozikov derive the scalar function \(\psi_k\), prove the existence and uniqueness of its minimum \(\tau_c(k)\), and give the explicit value only for \(k=2\). Their paper also notes that the general three-periodic equations are identifiable with those of a three-state Potts model at a transformed inverse temperature.

Külske and Schriever derive that Potts correspondence as
\[
\widetilde\beta=\log(2\cosh\beta-1),
\]
and give an explicit three-state threshold only for the binary tree. Külske, Rozikov, and Khakimov classify translation-invariant splitting Gibbs measures of the ferromagnetic Potts model for general tree order, but likewise state explicit critical-temperature formulae only for the binary tree. None of these inspected sources states the high-order asymptotic constants \(c_*\), \(C_*\), \(D_*\), or the \(k^{-1/2}\) inverse-temperature law with its explicit coefficient.

## Limitations
The asymptotic describes one distinguished existence threshold for three-periodic gradient boundary laws. It does not determine extremality, reconstruction, free-energy dominance, or the full phase diagram. The Potts correspondence means that an equivalent asymptotic could in principle be derivable in alternative Potts variables; no such statement was located in the inspected primary literature, but weakly indexed older Bethe-lattice calculations remain a residual originality risk. The big-O constants are not optimized.

## References
1. F. Henning, C. Külske, A. Le Ny, U. A. Rozikov, “Gradient Gibbs measures for the SOS model with countable values on a Cayley tree,” arXiv:1902.04909v1; Electronic Journal of Probability 24 (2019), article 104, DOI 10.1214/19-EJP364.
2. C. Külske, P. Schriever, “Gradient Gibbs measures and fuzzy transformations on trees,” arXiv:1609.00159v2; Markov Processes and Related Fields 23 (2017), 553–590.
3. C. Külske, U. A. Rozikov, R. M. Khakimov, “Description of the translation-invariant splitting Gibbs measures for the Potts model on a Cayley tree,” arXiv:1310.6220; Journal of Statistical Physics 156 (2014), 189–200.
